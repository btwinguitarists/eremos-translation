#!/usr/bin/env python3
"""
Back-translation check — in-chat mode.

The workflow is:
  1. After translating a chapter, Claude (same chat, same model, no external
     API call) back-translates each verse's Thai into literal English.
  2. Those back-translations are saved to
     output/back_translations/<slug>_<NN>.json
  3. This script diffs each back-translation against BSB and produces the
     comparison report.

If no back-translations file exists, the script writes a prompt file and
exits with a HARD FAILURE (exit 2). Missing BT is a ship-blocker — the
in-chat step must be completed before the chapter ships. This was changed
2026-04-19 after an audit found 14 chapters had silently shipped with
only PROMPT.md placeholders (no actual back-translation done).

Usage:
  python3 scripts/check_back_translation.py --book 1TI --chapter 3
"""
import argparse
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
BACK_TRANSLATIONS = ROOT / "output" / "back_translations"
REPORTS = ROOT / "output" / "check_reports"

SLUG_TO_CODE = {
    "matthew": "MAT", "mark": "MRK", "luke": "LUK", "john": "JHN",
    "acts": "ACT", "romans": "ROM", "1corinthians": "1CO", "2corinthians": "2CO",
    "galatians": "GAL", "ephesians": "EPH", "philippians": "PHP", "colossians": "COL",
    "1thessalonians": "1TH", "2thessalonians": "2TH", "1timothy": "1TI", "2timothy": "2TI",
    "titus": "TIT", "philemon": "PHM", "hebrews": "HEB", "james": "JAS",
    "1peter": "1PE", "2peter": "2PE", "1john": "1JN", "2john": "2JN",
    "3john": "3JN", "jude": "JUD", "revelation": "REV",
    "genesis": "GEN", "exodus": "EXO", "leviticus": "LEV", "numbers": "NUM",
    "deuteronomy": "DEU", "joshua": "JOS", "judges": "JDG", "ruth": "RUT",
    "1samuel": "1SA", "2samuel": "2SA", "1kings": "1KI", "2kings": "2KI",
    "1chronicles": "1CH", "2chronicles": "2CH", "ezra": "EZR", "nehemiah": "NEH",
    "esther": "EST", "job": "JOB", "psalms": "PSA", "proverbs": "PRO",
    "ecclesiastes": "ECC", "songofsongs": "SNG", "isaiah": "ISA", "jeremiah": "JER",
    "lamentations": "LAM", "ezekiel": "EZK", "daniel": "DAN", "hosea": "HOS",
    "joel": "JOL", "amos": "AMO", "obadiah": "OBA", "jonah": "JON",
    "micah": "MIC", "nahum": "NAM", "habakkuk": "HAB", "zephaniah": "ZEP",
    "haggai": "HAG", "zechariah": "ZEC", "malachi": "MAL",
}


def similarity(a: str, b: str) -> float:
    """Simple sequence-ratio similarity 0..1."""
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


def resolve_book_slug(arg: str) -> str:
    up = arg.upper()
    for slug, code in SLUG_TO_CODE.items():
        if code == up:
            return slug
    return arg.lower()


def write_pending_instructions(slug: str, chapter: int, verses: list) -> None:
    """Produce a prompt file Claude fills in when no back-translations exist."""
    BACK_TRANSLATIONS.mkdir(parents=True, exist_ok=True)
    prompt_path = BACK_TRANSLATIONS / f"{slug}_{chapter:02d}_PROMPT.md"

    lines = [
        f"# Back-translation prompt — {slug} ch. {chapter}",
        "",
        "Claude: back-translate each verse's Thai to literal English, WITHOUT consulting",
        "the Bible, BSB, or any known translation. Work only from the Thai input.",
        "",
        "Output: write a file at `output/back_translations/{}_{:02d}.json` containing:".format(slug, chapter),
        "```json",
        "[",
        '  { "verse": <number>, "back_translation": "<literal English>" },',
        "  ...",
        "]",
        "```",
        "",
        "Rules:",
        "- Preserve honorifics in English (e.g., ทรง → passive/formal; พระองค์ → 'He/Him' for divine subject)",
        "- Do NOT paraphrase for style. Render the Thai sense directly.",
        "- Do NOT add theological interpretation. If the Thai is ambiguous, keep the English ambiguous.",
        "- One line per verse (do NOT reproduce verse numbers in the back-translation text itself).",
        "",
        "## Verses",
        "",
    ]
    for v in verses:
        lines.append(f"### Verse {v['verse']}")
        lines.append(f"Thai: {(v.get('translation', {}) or {}).get('thai', '')}")
        lines.append("")

    prompt_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"   Prompt written to: {prompt_path}")
    print(f"   Expected output: {BACK_TRANSLATIONS / f'{slug}_{chapter:02d}.json'}")


def process(slug: str, chapter: int, translation_file: Path, bt_file: Path, threshold: float) -> int:
    with open(translation_file, encoding="utf-8") as f:
        verses = json.load(f)
    with open(bt_file, encoding="utf-8") as f:
        back_translations = json.load(f)

    bt_by_verse = {int(b["verse"]): b["back_translation"] for b in back_translations}

    results = []
    for v in verses:
        verse_num = v["verse"]
        thai = (v.get("translation", {}) or {}).get("thai", "") or ""
        bsb = v.get("bsb_english", "") or ""
        bt = bt_by_verse.get(verse_num, "")

        if not bt:
            results.append({
                "verse": v["reference"], "thai": thai, "back_translation": "",
                "bsb_english": bsb, "similarity": 0.0, "has_rationale": False,
                "flagged": True, "missing_bt": True,
            })
            continue

        sim = similarity(bt, bsb)
        has_rationale = bool(
            (v.get("translation", {}) or {}).get("notes")
            or (v.get("translation", {}) or {}).get("key_decisions")
        )

        results.append({
            "verse": v["reference"], "thai": thai, "back_translation": bt,
            "bsb_english": bsb, "similarity": sim, "has_rationale": has_rationale,
            "flagged": sim < threshold and not has_rationale,
            "missing_bt": False,
        })

    flagged = [r for r in results if r["flagged"]]
    low_sim_with_rationale = [r for r in results if r["similarity"] < threshold and r["has_rationale"] and not r["missing_bt"]]
    missing = [r for r in results if r.get("missing_bt")]

    lines = [
        f"# Back-translation check — {slug} ch. {chapter}",
        "",
        f"Mode: in-chat (Claude-produced back-translations) | Threshold: {threshold}",
        "",
        f"- Verses checked: {len(results)}",
        f"- Missing back-translations: **{len(missing)}**",
        f"- Flagged (low similarity AND no rationale): **{len(flagged) - len(missing)}**",
        f"- Low similarity but with rationale: {len(low_sim_with_rationale)}",
        f"- Acceptable similarity: {len(results) - len(flagged) - len(low_sim_with_rationale)}",
        "",
    ]

    if missing:
        lines.append("## ❌ Missing back-translations")
        lines.append("")
        for r in missing:
            lines.append(f"- {r['verse']}")
        lines.append("")

    if flagged and not all(r.get("missing_bt") for r in flagged):
        lines.append("## ⚠ Flagged verses (low similarity, no rationale documented)")
        lines.append("")
        for r in flagged:
            if r.get("missing_bt"):
                continue
            lines.append(f"### {r['verse']}  (sim={r['similarity']:.2f})")
            lines.append(f"- **Thai**:    {r['thai']}")
            lines.append(f"- **Back-EN**: {r['back_translation']}")
            lines.append(f"- **BSB**:     {r['bsb_english']}")
            lines.append("")

    if low_sim_with_rationale:
        lines.append("## ℹ Low similarity — rationale documented (intentional divergence)")
        lines.append("")
        for r in low_sim_with_rationale:
            lines.append(f"- **{r['verse']}** (sim={r['similarity']:.2f})")
            lines.append(f"  - Thai: {r['thai']}")
            lines.append(f"  - Back: {r['back_translation']}")
            lines.append(f"  - BSB:  {r['bsb_english']}")
        lines.append("")

    lines.append("## Acceptable")
    lines.append("")
    lines.append(f"{len(results) - len(flagged) - len(low_sim_with_rationale)} verses passed the similarity threshold without issue.")

    REPORTS.mkdir(parents=True, exist_ok=True)
    out_path = REPORTS / f"back_translation_{slug}_{chapter:02d}.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"  Missing: {len(missing)}")
    print(f"  Flagged (no rationale): {len(flagged) - len(missing)}")
    print(f"  Low-sim with rationale: {len(low_sim_with_rationale)}")

    return 1 if (flagged and any(not r.get("missing_bt") for r in flagged)) or missing else 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--threshold", type=float, default=0.35)
    args = parser.parse_args()

    slug = resolve_book_slug(args.book)
    translation_file = TRANSLATIONS / f"{slug}_{args.chapter:02d}.json"
    if not translation_file.exists():
        print(f"No translation file at {translation_file}")
        return 1

    bt_file = BACK_TRANSLATIONS / f"{slug}_{args.chapter:02d}.json"
    if not bt_file.exists():
        with open(translation_file, encoding="utf-8") as f:
            verses = json.load(f)
        write_pending_instructions(slug, args.chapter, verses)
        print(f"✗ MISSING back-translation — ship blocked.")
        print(f"  Claude must produce {bt_file} per the prompt above.")
        return 2  # hard failure: missing BT is a ship-blocker (changed 2026-04-19)

    return process(slug, args.chapter, translation_file, bt_file, args.threshold)


if __name__ == "__main__":
    sys.exit(main())
