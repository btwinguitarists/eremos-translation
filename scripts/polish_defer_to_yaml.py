#!/usr/bin/env python3
"""
polish_defer_to_yaml — bridge polish-pass defer-to-native proposals into the
existing /review form.

The polish-suite (polish_review.py + polish_optimal_equivalence.py) generates
proposals across three confidence buckets:
  - apply              — high-confidence, owner approves directly via the
                         polish-summary doc + apply_polish_deltas.py
  - defer_to_native    — register/feel calls the model can't settle without
                         a Thai-language reviewer's ear  ←  THIS SCRIPT
  - fyi                — informational only

This script walks every polish_proposals/<book>/<book>_NN_optimal.json
sidecar, filters to defer_to_native proposals, and emits one YAML question
file per proposal in the schema EremosVercel2's `/review` form already
consumes (matching shared/review-questions/<id>.yml).

Output: output/review_questions_polish_defer/<id>.yml — gitignored local
working files; user copies approved ones to ~/EremosVercel2/shared/
review-questions/ to land them on the form.

Question shape:
  - kind: choice (the form's enum is choice/yes_no/text — no `radio`)
  - options: keep_current / accept_proposed / other
  - text_prompt: "Notes / reasoning:" (so the reviewer can leave free-text)
  - body: Greek source + current Thai + proposed Thai + rationale
  - tier: A (native_speaker, lay_person, pastor — same as register-feel
    questions)

Bilingual: en + th fields populated. The English content comes straight
from the proposal's rationale; the Thai content is templated using the
verse's existing Thai (which is already in the JSON) plus standard Thai
question wrappers.

Usage:
  python3 scripts/polish_defer_to_yaml.py                # all defer items
  python3 scripts/polish_defer_to_yaml.py --book john    # one book
  python3 scripts/polish_defer_to_yaml.py --dry-run      # count, don't write
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROPOSALS = ROOT / "output" / "polish_proposals"
OUT_DIR = ROOT / "output" / "review_questions_polish_defer"

# Slug → 3-letter code (mirror of build_external_review_packet.py)
SLUG_TO_CODE = {
    "matthew": "MAT", "mark": "MRK", "luke": "LUK", "john": "JHN", "acts": "ACT",
    "romans": "ROM", "1corinthians": "1CO", "2corinthians": "2CO",
    "galatians": "GAL", "ephesians": "EPH", "philippians": "PHP", "colossians": "COL",
    "1thessalonians": "1TH", "2thessalonians": "2TH", "1timothy": "1TI",
    "2timothy": "2TI", "titus": "TIT", "philemon": "PHM", "hebrews": "HEB",
    "james": "JAS", "1peter": "1PE", "2peter": "2PE", "1john": "1JN",
    "2john": "2JN", "3john": "3JN", "jude": "JUD", "revelation": "REV",
    "ruth": "RUT",
}

# Issue-type → bilingual label for the topic line.
ISSUE_LABELS = {
    "register_drift": (
        "register feel",
        "ระดับภาษา"
    ),
    "wooden_passive": (
        "passive voice",
        "การใช้ประโยคถูกกระทำ"
    ),
    "conjunction_overload": (
        "conjunction stack",
        "การใช้คำเชื่อม"
    ),
    "literal_idiom": (
        "idiom rendering",
        "สำนวน"
    ),
    "rigid_metaphor": (
        "metaphor naturalness",
        "ความเป็นธรรมชาติของอุปมา"
    ),
}


def yaml_escape(s: str) -> str:
    """Escape a string for YAML block-scalar pipe form. Indents every line by
    4 spaces and removes any trailing whitespace per line."""
    if not s:
        return ""
    lines = []
    for line in s.split("\n"):
        # strip trailing whitespace; no leading-strip (preserve intentional indent)
        line = line.rstrip()
        lines.append("    " + line if line else "")
    return "\n".join(lines)


def yaml_inline_string(s: str) -> str:
    """Quote-safe a string for YAML inline single-line form."""
    s = (s or "").replace("\\", "\\\\").replace('"', '\\"')
    s = s.replace("\n", " ").strip()
    return f'"{s}"'


def derive_id(book_code: str, verse_ref: str, issue_type: str) -> str:
    """Build a stable id like A_JHN_15_4_polish_register."""
    m = re.search(r"(\d+):(\d+)", verse_ref or "")
    if not m:
        return f"A_{book_code}_polish_{issue_type[:8]}"
    chapter, verse = m.group(1), m.group(2)
    issue_short = {
        "register_drift": "register",
        "wooden_passive": "passive",
        "conjunction_overload": "conjunction",
        "literal_idiom": "idiom",
        "rigid_metaphor": "metaphor",
    }.get(issue_type, issue_type[:10])
    return f"A_{book_code}_{chapter}_{verse}_polish_{issue_short}"


def render_yaml(prop: dict, book_code: str) -> tuple[str, str]:
    """Return (id, yaml_text) for one proposal."""
    verse_ref = prop["verse_ref"]
    issue_type = prop["issue_type"]
    qid = derive_id(book_code, verse_ref, issue_type)

    issue_en, issue_th = ISSUE_LABELS.get(issue_type, (issue_type, issue_type))

    topic_en = f"Polish — {verse_ref}: {issue_en}"
    topic_th = f"ปรับสำนวน — {verse_ref}: {issue_th}"

    question_en = (
        "Which Thai rendering of this verse reads more naturally for a "
        "modern Thai Bible reader? The proposed change is a polish "
        "(not a meaning change); both renderings preserve the underlying "
        "Greek meaning and any locked theological terms."
    )
    question_th = (
        "การแปลภาษาไทยของข้อนี้แบบไหนอ่านได้เป็นธรรมชาติกว่าสำหรับผู้อ่านพระคัมภีร์ภาษาไทยร่วมสมัย? "
        "การเสนอเปลี่ยนเป็นเพียงการปรับสำนวน (ไม่ใช่การเปลี่ยนความหมาย) — "
        "ทั้งสองสำนวนรักษาความหมายของภาษากรีกและคำศัพท์ทางเทววิทยาที่ล็อกไว้เหมือนเดิม"
    )

    greek_lemma = prop.get("greek_lemma_focus") or ""
    rationale_en = (prop.get("rationale") or "").strip()

    # The body shows: current Thai, proposed Thai, brief rationale.
    body_en = (
        f"**Verse:** {verse_ref}\n\n"
        f"**Issue type:** `{issue_type}` ({issue_en})\n\n"
    )
    if greek_lemma:
        body_en += f"**Greek lemma:** `{greek_lemma}`\n\n"
    body_en += (
        f"**Current Thai:**\n"
        f"\n> {prop['current_text']}\n\n"
        f"**Proposed Thai:**\n"
        f"\n> {prop['proposed_text']}\n\n"
        f"**Why proposed:** {rationale_en}\n"
    )

    body_th = (
        f"**ข้อ:** {verse_ref}\n\n"
        f"**ประเภท:** {issue_th}\n\n"
    )
    if greek_lemma:
        body_th += f"**คำกรีก:** `{greek_lemma}`\n\n"
    body_th += (
        f"**ฉบับปัจจุบัน:**\n"
        f"\n> {prop['current_text']}\n\n"
        f"**เสนอเปลี่ยนเป็น:**\n"
        f"\n> {prop['proposed_text']}\n"
    )

    yaml = f"""id: {qid}
tier: A
roles: [native_speaker, lay_person, pastor]
kind: choice
topic:
  en: {yaml_inline_string(topic_en)}
  th: {yaml_inline_string(topic_th)}
question:
  en: |
{yaml_escape(question_en)}
  th: |
{yaml_escape(question_th)}
options:
  - value: keep_current
    label:
      en: "Keep the current rendering"
      th: "เก็บสำนวนเดิม"
  - value: accept_proposed
    label:
      en: "Accept the proposed polish"
      th: "ยอมรับการปรับสำนวน"
  - value: other
    label:
      en: "Other (please explain in notes)"
      th: "อื่น ๆ (โปรดอธิบายในหมายเหตุ)"
text_prompt:
  en: "Notes / reasoning:"
  th: "หมายเหตุ / เหตุผล:"
body:
  en: |
{yaml_escape(body_en)}
  th: |
{yaml_escape(body_th)}
"""
    return qid, yaml


def collect_defer_proposals(book_filter: str | None = None) -> list[tuple[str, dict]]:
    """Return [(book_code, proposal_dict), ...] for every defer-bucket proposal."""
    out = []
    for sidecar in sorted(PROPOSALS.rglob("*_optimal.json")):
        # skip non-NT pattern (e.g., the Ruth chapter sidecar uses same pattern;
        # we want all books that have proposals)
        try:
            data = json.loads(sidecar.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        slug = sidecar.parent.name
        if book_filter and slug != book_filter:
            continue
        code = SLUG_TO_CODE.get(slug)
        if not code:
            continue
        for p in data.get("proposals", []):
            if p.get("confidence") == "defer_to_native":
                out.append((code, p))
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", help="Filter to one book slug (e.g., john)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Count + preview ids; don't write files")
    args = parser.parse_args()

    proposals = collect_defer_proposals(args.book.lower() if args.book else None)
    if not proposals:
        print("No defer-bucket proposals found. Run polish_optimal_equivalence.py first.")
        return 0

    print(f"Found {len(proposals)} defer-to-native proposals.")

    if args.dry_run:
        print("Sample ids (first 10):")
        for book_code, p in proposals[:10]:
            qid = derive_id(book_code, p["verse_ref"], p["issue_type"])
            print(f"  {qid}  ({p['issue_type']})")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for book_code, p in proposals:
        qid, yaml = render_yaml(p, book_code)
        out_path = OUT_DIR / f"{qid}.yml"
        out_path.write_text(yaml, encoding="utf-8")
        written += 1

    print(f"Wrote {written} YAML files to {OUT_DIR}/")
    print()
    print("Next steps:")
    print(f"  1. Review samples: ls {OUT_DIR}/ | head")
    print(f"     cat {OUT_DIR}/$(ls {OUT_DIR}/ | head -1)")
    print(f"  2. Copy to EremosVercel2 (one-line):")
    print(f"     cp {OUT_DIR}/*.yml ~/EremosVercel2/shared/review-questions/")
    print(f"  3. From ~/EremosVercel2 main:")
    print(f"     git checkout -b feat/review-questions-polish-defer")
    print(f"     git add shared/review-questions/")
    print(f"     git commit -m 'feat: add {written} polish-defer questions to /review'")
    print(f"     git push -u origin feat/review-questions-polish-defer")
    print(f"     gh pr create --title 'feat: add polish-defer questions to /review'")
    print(f"  4. Build-step regenerates shared/review-questions-generated.ts on")
    print(f"     `npm run check` / `npm run build`. Reviewer (Tier-A) sees them at")
    print(f"     eremosapp.com/review.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
