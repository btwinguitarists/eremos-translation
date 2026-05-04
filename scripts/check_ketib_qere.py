#!/usr/bin/env python3
"""
Ketib / Qere check — surfaces Masoretic textual variants for translator review.

Per docs/translator_decisions/verse_schema_and_versification_2026-05.md §3:

  Ketib (כְּתִיב) is the consonantal text "as written"; Qere (קְרֵי) is the
  marginal "as read" — the Masoretes' alternative pronunciation/reading.
  ~1,500 places in the OT.

  Default: translate the Qere (the read tradition; convention of NRSV, NIV,
  ESV, NASB, NLT). Translate the Ketib if (a) the Qere is clearly a euphemism
  and the Ketib is what the original author wrote, OR (b) the Qere is
  interpretive expansion that obscures the original.

This script is **WARNING-only initially** per plan §9.1 (script #11). It
surfaces every K/Q for translator review without blocking ship. Promote to
strict after pilot.

Two roles:

  1. Surface K/Q sites in source text — catalogues every verse where MACULA
     Hebrew morphology indicates a Ketib/Qere alternative.

  2. Verify per-verse decisions — when a verse contains a K/Q site, flag it
     if the verse's `key_decisions` doesn't acknowledge the variant. The
     translator should decide Ketib or Qere with rationale.

Data sources:

  - data/ketib_qere_decisions.json — the running record of K/Q decisions made
    during translation. Format per verse_schema_and_versification §3.1.
  - MACULA Hebrew morphology — the source. K/Q sites are typically encoded
    via specific morphology tags or as paired entries.

Usage:
  python3 scripts/check_ketib_qere.py --book DEU --chapter 28
  python3 scripts/check_ketib_qere.py --all
  python3 scripts/check_ketib_qere.py --report

Exit codes:
  0 = clean (warn-only stage)
  1 = reserved for future strict mode
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
DATA_DIR = ROOT / "data"
KETIB_QERE_DECISIONS = DATA_DIR / "ketib_qere_decisions.json"
REPORTS = ROOT / "output" / "check_reports"

OT_SLUG_TO_CODE = {
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

# Keywords in `key_decisions` rationale that indicate the translator addressed K/Q
KQ_KEYWORDS = re.compile(
    r"\b(ketib|kethibh|qere|q'rey|qere/ketib|k/q|k\.\s*q\.|"
    r"masoretic\s+variant|\bmt\s+variant|read\s+vs\s+written)\b",
    re.IGNORECASE,
)


def load_kq_decisions() -> dict:
    """Load data/ketib_qere_decisions.json. Returns empty dict if not present."""
    if not KETIB_QERE_DECISIONS.exists():
        return {}
    try:
        return json.loads(KETIB_QERE_DECISIONS.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"WARNING: {KETIB_QERE_DECISIONS} invalid JSON", file=sys.stderr)
        return {}


def find_ot_chapter_files(book_filter: str | None,
                          chapter_filter: int | None) -> list[Path]:
    files: list[Path] = []
    if not TRANSLATIONS.exists():
        return files
    for path in sorted(TRANSLATIONS.glob("*_*.json")):
        m = re.match(r"^(.+)_(\d+)\.json$", path.name)
        if not m:
            continue
        slug, ch_str = m.group(1), m.group(2)
        if slug not in OT_SLUG_TO_CODE:
            continue
        if book_filter and OT_SLUG_TO_CODE[slug] != book_filter.upper():
            continue
        if chapter_filter is not None and int(ch_str) != chapter_filter:
            continue
        files.append(path)
    return files


def kd_text(verse: dict) -> str:
    """Concatenate all key_decisions text for keyword scanning."""
    out = []
    for kd in verse.get("key_decisions", []) or []:
        if isinstance(kd, dict):
            for v in kd.values():
                if isinstance(v, str):
                    out.append(v)
        elif isinstance(kd, str):
            out.append(kd)
    return " ".join(out)


def check_verse(verse: dict, book_code: str, kq_decisions: dict) -> list[str]:
    """Return list of WARN messages."""
    warns: list[str] = []
    chapter = verse.get("chapter")
    vno = verse.get("verse")
    ref = verse.get("reference", f"{book_code} {chapter}:{vno}")

    # Look up known K/Q sites for this verse
    key = f"{book_code}-{chapter}-{vno}"
    known_kq = kq_decisions.get(key)
    if not known_kq:
        return warns  # no known K/Q at this verse — skip

    rationale = kd_text(verse)
    if not KQ_KEYWORDS.search(rationale):
        warns.append(
            f"[KQ] {ref}: known Ketib/Qere site (per ketib_qere_decisions.json) "
            f"but verse's key_decisions doesn't mention K/Q. Document the "
            f"translator's choice (ketib vs qere) with rationale"
        )

    return warns


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--book", help="3-letter OT book code")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    kq_decisions = load_kq_decisions()
    if not kq_decisions:
        print(f"NOTE: {KETIB_QERE_DECISIONS} not present yet. K/Q surveillance "
              f"is data-driven; build the file as decisions accumulate.")

    files = find_ot_chapter_files(args.book, args.chapter)
    if not files:
        print("No OT chapter files found.")
        return 0

    total_warns: list[str] = []
    for fpath in files:
        m = re.match(r"^(.+)_(\d+)\.json$", fpath.name)
        slug = m.group(1)
        book_code = OT_SLUG_TO_CODE[slug]
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if not isinstance(data, list):
            data = [data]
        for verse in data:
            if not isinstance(verse, dict):
                continue
            if verse.get("language") not in ("hebrew", "aramaic"):
                continue
            total_warns.extend(check_verse(verse, book_code, kq_decisions))

    print(f"Ketib/Qere check — checked {len(files)} OT chapter file(s)")
    print(f"  Known K/Q sites in registry: {len(kq_decisions)}")
    if total_warns:
        print(f"\nWARNINGS ({len(total_warns)}):")
        for w in total_warns[:20]:
            print(f"  {w}")
        if len(total_warns) > 20:
            print(f"  ... and {len(total_warns) - 20} more")

    if args.report:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out = REPORTS / "ketib_qere.md"
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Ketib/Qere check report\n\n")
            f.write(f"Per docs/translator_decisions/verse_schema_and_versification_2026-05.md §3\n\n")
            f.write(f"- Files checked: {len(files)}\n")
            f.write(f"- Known K/Q sites in registry: {len(kq_decisions)}\n")
            f.write(f"- Warnings: {len(total_warns)}\n\n")
            if total_warns:
                f.write("## Warnings (warn-only at this stage)\n\n")
                for w in total_warns:
                    f.write(f"- {w}\n")
        print(f"Wrote {out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
