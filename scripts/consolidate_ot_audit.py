#!/usr/bin/env python3
"""
OT v1.0 corpus-wide audit consolidator (Stage 1 of the OT full audit).

Read-only. The OT analogue of consolidate_nt_audit.py. Aggregates:
  - per-book end-of-book audit docs (docs/end_of_book/<book>/<BOOK>_END_OF_BOOK_REVIEW_*.md)
  - external AI review responses — BOTH naming conventions:
      external_review_response_<CODE>_*.md  (new, run_book_review_gemini.py)
      ai_review_response_<CODE>_*.md         (legacy)
  - corpus-wide check outputs (key_term_consistency, phrase_consistency,
    inclusion_variants, parallel_passages) with honest scope annotations —
    some of those checks key on the Greek field and so under-cover OT Hebrew.
  - per-chapter summary JSONs (output/check_reports/<slug>_NN_summary.json)

Writes ONE new file: docs/OT_V1_FULL_AUDIT_<date>.md
Touches nothing else. No translation files modified. No rules modified.

Book list + chapter counts are derived from disk (output/translations/<slug>_NN.json),
so the report reflects MT versification automatically (Joel 4, Malachi 3, ...).

Usage:
  python3 scripts/consolidate_ot_audit.py
  python3 scripts/consolidate_ot_audit.py --output docs/OT_V1_FULL_AUDIT_custom.md
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
CHECK_REPORTS = ROOT / "output" / "check_reports"
EOB_DIR = ROOT / "docs" / "end_of_book"
sys.path.insert(0, str(ROOT / "scripts"))
from build_external_review_packet import BOOKS  # CODE -> (slug, name)

# Canonical OT order (Protestant), slug form. Codes/names come from BOOKS.
OT_SLUGS = [
    "genesis", "exodus", "leviticus", "numbers", "deuteronomy",
    "joshua", "judges", "ruth", "1samuel", "2samuel", "1kings", "2kings",
    "1chronicles", "2chronicles", "ezra", "nehemiah", "esther",
    "job", "psalms", "proverbs", "ecclesiastes", "songofsongs",
    "isaiah", "jeremiah", "lamentations", "ezekiel", "daniel",
    "hosea", "joel", "amos", "obadiah", "jonah", "micah", "nahum",
    "habakkuk", "zephaniah", "haggai", "zechariah", "malachi",
]

# Corpus checks, with scope notes. Some are Greek/SBLGNT-oriented and so
# under-report on OT Hebrew — we still run them (cross-testament drift surfaces
# here) but annotate honestly so the OT report isn't falsely reassuring.
CORPUS_CHECKS = [
    ("check_key_term_consistency.py", [],
     "Greek-lemma keyed — covers NT + any OT verse carrying a `greek` field; "
     "OT Hebrew-lemma drift needs a Hebrew-aware equivalent."),
    ("check_phrase_consistency.py", [],
     "Thai-surface phrase drift across the whole corpus — language-agnostic, "
     "covers OT + NT (catches e.g. den-of-robbers Matt vs Jer/Mark/Luke)."),
    ("audit_inclusion_variants.py", ["--strict"],
     "SBLGNT inclusion variants — NT textual-criticism scope; OT MT/LXX & "
     "Ketiv/Qere divergence is a separate dimension not covered here."),
    ("check_parallel_passages.py", [],
     "Parallel/synoptic + cross-testament passages — covers OT↔OT (2 Sam↔1 Chr) "
     "and OT↔NT citation parallels."),
]

OT_CODES = {slug: code for code, (slug, _n) in BOOKS.items()}
OT_NAMES = {slug: name for code, (slug, name) in BOOKS.items()}


def chapters_shipped(slug: str) -> int:
    if not TRANSLATIONS.exists():
        return 0
    # \d{2,3} so Psalms 100-150 (three-digit) are counted, not just 01-99.
    pattern = re.compile(rf"^{re.escape(slug)}_\d{{2,3}}\.json$")
    return sum(1 for p in TRANSLATIONS.iterdir() if pattern.match(p.name))


def find_audit_doc(slug: str) -> Path | None:
    folder = EOB_DIR / slug
    if not folder.exists():
        return None
    cands = sorted(folder.glob("*_END_OF_BOOK_REVIEW_*.md"))
    return cands[-1] if cands else None


def find_external_response(slug: str) -> Path | None:
    folder = EOB_DIR / slug
    if not folder.exists():
        return None
    # Three naming conventions exist across the repo, so match on the shared
    # 'review_response' stem (leading wildcard catches the CODE-prefixed form):
    #   external_review_response_<CODE>_<date>.md   (run_book_review_gemini.py)
    #   <CODE>_external_review_response_<date>.md    (late-May OT books)
    #   ai_review_response_<CODE>_<date>.md          (legacy NT)
    cands = sorted(folder.glob("*review_response*.md"))
    return cands[-1] if cands else None


def extract_status_counts(audit_path: Path | None) -> dict[str, int]:
    counts = {"LOCKED": 0, "STABLE": 0, "REVIEW": 0, "DECIDE": 0}
    if not audit_path or not audit_path.exists():
        return counts
    text = audit_path.read_text(encoding="utf-8")
    for code in counts:
        counts[code] = len(re.findall(rf"\b{code}\b", text))
    return counts


def run_corpus_check(script_name: str, args: list[str] | None = None) -> tuple[bool, str]:
    script_path = ROOT / "scripts" / script_name
    if not script_path.exists():
        return False, f"script not found: {script_name}"
    cmd = ["python3", str(script_path)] + (args or [])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600, cwd=str(ROOT))
        return result.returncode == 0, (result.stdout + result.stderr).strip()
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as exc:  # noqa
        return False, f"error: {exc}"


def gather_per_chapter_warnings(slug: str, chapters: int) -> list[str]:
    warnings = []
    for n in range(1, chapters + 1):
        sp = CHECK_REPORTS / f"{slug}_{n:02d}_summary.json"
        if not sp.exists():
            continue
        try:
            data = json.loads(sp.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for k, v in data.items():
            if isinstance(v, dict) and v.get("status") in ("warn", "fail"):
                warnings.append(f"{slug}_{n:02d}: {k} = {v.get('status')}")
    return warnings


def build_audit(output_path: Path) -> None:
    today = date.today().isoformat()
    L: list[str] = []
    L += [
        "# OT v1.0 — Full Corpus Audit", "",
        f"**Generated:** {today}",
        "**Source:** `consolidate_ot_audit.py` (Stage 1 of the OT full audit)",
        "**Scope:** All 39 OT books, corpus-wide checks, per-book audit findings,",
        "external AI review responses where present.", "",
        "**Read-only consolidation.** No translations or rules modified.", "",
        "> Chapter counts are MT versification (e.g. Joel 4, Malachi 3), read from "
        "`output/translations/` on disk.", "",
        "---", "",
    ]

    # 1. Coverage matrix
    L += ["## 1. Coverage matrix", "",
          "| Book | Code | Chapters | EOB audit | External response |",
          "|---|---|---:|:-:|:-:|"]
    total_ch = audits = responses = 0
    for slug in OT_SLUGS:
        code = OT_CODES.get(slug, "?")
        ch = chapters_shipped(slug)
        a = find_audit_doc(slug)
        r = find_external_response(slug)
        total_ch += ch
        audits += 1 if a else 0
        responses += 1 if r else 0
        L.append(f"| {slug} | {code} | {ch} | {'yes' if a else '—'} | {'yes' if r else '—'} |")
    L.append(f"| **Total** | | **{total_ch}** | **{audits}/39** | **{responses}/39** |")
    L += ["", "---", ""]

    # 2. Corpus-wide automated checks
    L += ["## 2. Corpus-wide automated checks", "",
          "Each script run against the full corpus. PASS = exit 0; FAIL = non-zero exit.",
          "Scope notes matter for the OT — several checks were built NT-first.", ""]
    for script, args, note in CORPUS_CHECKS:
        passed, output = run_corpus_check(script, args)
        status = "PASS" if passed else "FAIL"
        arg_str = (" " + " ".join(args)) if args else ""
        L += [f"### `{script}{arg_str}` — **{status}**", "",
              f"*Scope:* {note}", ""]
        if not passed and output:
            tail = "\n".join(output.splitlines()[-15:])
            L += ["```", tail, "```", ""]
    L += ["---", ""]

    # 3. Per-book audit status rollup
    L += ["## 3. Per-book audit status rollup", "",
          "Status-code counts pulled from each book's end-of-book audit doc.", "",
          "| Book | LOCKED | STABLE | REVIEW | DECIDE |", "|---|---:|---:|---:|---:|"]
    grand = {"LOCKED": 0, "STABLE": 0, "REVIEW": 0, "DECIDE": 0}
    for slug in OT_SLUGS:
        a = find_audit_doc(slug)
        if not a:
            L.append(f"| {slug} | — | — | — | — |")
            continue
        c = extract_status_counts(a)
        for k in grand:
            grand[k] += c[k]
        L.append(f"| {slug} | {c['LOCKED']} | {c['STABLE']} | {c['REVIEW']} | {c['DECIDE']} |")
    L.append(f"| **Total** | **{grand['LOCKED']}** | **{grand['STABLE']}** | "
             f"**{grand['REVIEW']}** | **{grand['DECIDE']}** |")
    L += ["",
          "> Counts are heuristic (regex on the status word). For decision-grade "
          "detail, open the per-book audit at `docs/end_of_book/<book>/`.", "",
          "---", ""]

    # 4. Outstanding items
    L += ["## 4. Outstanding items by book", "",
          "Per-book audit docs containing REVIEW or DECIDE flags worth a final pass:", ""]
    for slug in OT_SLUGS:
        a = find_audit_doc(slug)
        if not a:
            continue
        c = extract_status_counts(a)
        if c["REVIEW"] == 0 and c["DECIDE"] == 0:
            continue
        L.append(f"- **{slug}** ({OT_CODES.get(slug,'?')}) — REVIEW: {c['REVIEW']}, "
                 f"DECIDE: {c['DECIDE']} — `{a.relative_to(ROOT)}`")
    L += ["", "---", ""]

    # 5. Per-chapter warnings
    L += ["## 5. Per-chapter check warnings", "",
          "Warnings or failures from per-chapter summary JSONs (if any).", ""]
    any_warn = False
    for slug in OT_SLUGS:
        ws = gather_per_chapter_warnings(slug, chapters_shipped(slug))
        if not ws:
            continue
        any_warn = True
        L.append(f"### {slug}")
        L += [f"- {w}" for w in ws]
        L.append("")
    if not any_warn:
        L += ["None. All shipped chapters have clean summary JSONs.", ""]
    L += ["---", ""]

    # 6. Stage-2 pointer
    L += ["## 6. Next: Stage 2 polish sweep", "",
          "Stage 1 is mechanical consolidation. Thai-flow micro-issues are caught in Stage 2.",
          "(`polish_review.py` was authored NT-first; confirm it handles OT books before a full run.)",
          "", "```",
          "python3 scripts/polish_review.py --book <slug>     # one book",
          "python3 scripts/polish_review.py --all              # all books",
          "```", "",
          "Stage 2 writes proposals to `output/polish_proposals/` only. Translation files "
          "are NOT modified until you run `apply_polish_deltas.py` with explicit approvals.", ""]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(L), encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser(description="OT v1.0 corpus audit consolidator (Stage 1)")
    p.add_argument("--output", type=Path,
                   default=ROOT / "docs" / f"OT_V1_FULL_AUDIT_{date.today().isoformat()}.md")
    args = p.parse_args()
    print(f"Consolidating OT audit -> {args.output.relative_to(ROOT)}")
    build_audit(args.output)
    print(f"Done. {args.output.stat().st_size} bytes written.")


if __name__ == "__main__":
    main()
