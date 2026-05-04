#!/usr/bin/env python3
"""
Hebrew-field integrity check — sibling of check_greek_field_integrity.py.

Catches the same class of metadata-drift surfaced by the LUK 13/14 incident
(see docs/LUKE_DRIFT_2026-04-21.md), now in OT verse files.

What this enforces:

  The `hebrew` (or `aramaic`) field of an OT verse JSON object should contain
  the Hebrew/Aramaic source text as it appears in MACULA Hebrew. The
  `key_decisions` entries' `hebrew` sub-field, where present, should contain
  Hebrew/Aramaic source — not Thai, not Latin transliteration, not
  fabricated tokens.

Three checks:

  [A] HARD FAIL — `hebrew` (or `aramaic`) field of the verse contains Thai
      characters (U+0E00–U+0E7F). There is no legitimate reason for Thai
      to leak into the Hebrew/Aramaic source slot.

  [B] HARD FAIL — `key_decisions[].hebrew` field contains only Hebrew
      letters, and the 3+ char Hebrew tokens don't appear in the verse's
      `hebrew`/`aramaic` source text, AND the rationale doesn't mention any
      of the legitimate-exception keywords (variant, ketib, qere, mt, lxx,
      dss, hapax, composite, apparatus, etc.). This catches fabricated
      Hebrew tokens.

  [C] WARN (non-blocking) — `key_decisions[].hebrew` field is ASCII-only and
      holds a meta-label like "Speaker: X to Y" or "Versification note".
      Legitimate but noisy — surfaced for review.

Usage:
  python3 scripts/check_hebrew_field_integrity.py --book GEN --chapter 1
  python3 scripts/check_hebrew_field_integrity.py --all

Exit codes:
  0 = clean (no hard fails)
  1 = at least one hard fail (ship blocked)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"

# OT slug → MACULA Hebrew code
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

# Rationale keywords that excuse a Hebrew token not appearing verbatim in the
# verse's source text — legitimate scholarly-reference contexts.
EXCUSE_KEYWORDS = re.compile(
    r"\b("
    r"variant|ketib|qere|kethibh|qere|mt\b|"
    r"lxx|septuagint|dss|qumran|4qsam|1qisa|"
    r"masoretic|samaritan|targum|peshitta|vulgate|"
    r"hapax|composite|apparatus|etymolog|gematria|"
    r"lemma|halot|bdb|tdot|dch|sdbh|"
    r"morpholog|stem|state|"
    r"acrostic|wordplay|paronomasia|"
    r"yhwh|adonai|elohim|tetragrammaton|"
    r"switched\s+from|shift(?:ed)?\s+from|cf\.|compare\s+with|parallel"
    r")",
    re.IGNORECASE,
)


def has_thai(s: str) -> bool:
    return any(0x0E00 <= ord(c) <= 0x0E7F for c in s)


def has_hebrew(s: str) -> bool:
    """Hebrew + Aramaic share the U+0590–U+05FF block."""
    return any(0x0590 <= ord(c) <= 0x05FF or 0xFB1D <= ord(c) <= 0xFB4F for c in s)


def has_greek(s: str) -> bool:
    return any(0x0370 <= ord(c) <= 0x03FF or 0x1F00 <= ord(c) <= 0x1FFF for c in s)


def strip_hebrew_punct(word: str) -> str:
    return word.strip(" ,.·;:()[]{}⟦⟧«»…\"'־׃׀")


def normalize_hebrew(s: str) -> str:
    """Strip Hebrew vowel points + cantillation so vocalized vs unvocalized
    tokens compare equal.

    Hebrew vowel points: U+05B0–U+05BD, U+05BF, U+05C1–U+05C2, U+05C4–U+05C5,
    U+05C7. Cantillation marks: U+0591–U+05AF.
    """
    out = []
    for c in unicodedata.normalize("NFD", s):
        cp = ord(c)
        if 0x0591 <= cp <= 0x05AF:  # cantillation
            continue
        if 0x05B0 <= cp <= 0x05BD:  # vowel points
            continue
        if cp in (0x05BF, 0x05C1, 0x05C2, 0x05C4, 0x05C5, 0x05C7):
            continue
        if unicodedata.combining(c):
            continue
        out.append(c)
    return "".join(out).lower()


def find_ot_chapter_files(book_filter: str | None = None,
                          chapter_filter: int | None = None) -> list[Path]:
    """Find OT chapter JSON files based on slug → OT_SLUG_TO_CODE membership.

    NT files are skipped (slug not in OT_SLUG_TO_CODE).
    """
    files: list[Path] = []
    if not TRANSLATIONS.exists():
        return files

    for path in sorted(TRANSLATIONS.glob("*_*.json")):
        # extract slug from path: e.g., "genesis_01.json" → "genesis"
        m = re.match(r"^(.+)_(\d+)\.json$", path.name)
        if not m:
            continue
        slug, ch_str = m.group(1), m.group(2)
        if slug not in OT_SLUG_TO_CODE:
            continue  # skip NT books
        if book_filter and OT_SLUG_TO_CODE[slug] != book_filter.upper():
            continue
        if chapter_filter is not None and int(ch_str) != chapter_filter:
            continue
        files.append(path)
    return files


def check_verse(verse: dict, fname: str) -> tuple[list[str], list[str]]:
    """Return (hard_fails, warnings) for a verse."""
    hard: list[str] = []
    warn: list[str] = []
    ref = verse.get("reference") or f"{verse.get('chapter','?')}:{verse.get('verse','?')}"
    lang = verse.get("language", "")

    # [A] hebrew/aramaic field must not contain Thai characters
    source_text = verse.get(lang, "") if lang in ("hebrew", "aramaic") else ""
    if source_text and has_thai(source_text):
        hard.append(
            f"[A] {ref}: Thai chars found in `{lang}` field — schema violation"
        )

    # [B,C] key_decisions[].hebrew sub-field validation
    kds = (verse.get("translation") or {}).get("key_decisions", [])
    if not kds:
        kds = verse.get("key_decisions", [])  # legacy flat-schema fallback
    if isinstance(kds, list):
        for i, kd in enumerate(kds):
            if not isinstance(kd, dict):
                continue
            heb_field = kd.get("hebrew") or kd.get("aramaic") or ""
            if not heb_field:
                continue
            rationale = (kd.get("rationale") or kd.get("reason") or
                         kd.get("text") or "")

            # [A applies to key_decisions too]
            if has_thai(heb_field):
                hard.append(
                    f"[A] {ref}: Thai chars in key_decisions[{i}].hebrew — "
                    f"schema violation"
                )
                continue

            # [B] Hebrew tokens that don't appear verbatim
            if has_hebrew(heb_field):
                # Tokenize the Hebrew field
                source_norm = normalize_hebrew(source_text)
                tokens = [
                    strip_hebrew_punct(t)
                    for t in re.split(r"\s+", heb_field)
                    if t.strip()
                ]
                missing = []
                for tok in tokens:
                    if len(tok) < 3:
                        continue
                    if not has_hebrew(tok):
                        continue
                    norm_tok = normalize_hebrew(tok)
                    if norm_tok and norm_tok not in source_norm:
                        missing.append(tok)

                if missing and not EXCUSE_KEYWORDS.search(rationale):
                    hard.append(
                        f"[B] {ref}: key_decisions[{i}].hebrew has Hebrew "
                        f"tokens {missing} not in source + no excuse keyword "
                        f"in rationale — possible fabrication"
                    )

            # [C] ASCII-only meta-labels (warning)
            elif not has_hebrew(heb_field) and heb_field.strip() and \
                    all(ord(c) < 128 for c in heb_field):
                warn.append(
                    f"[C] {ref}: key_decisions[{i}].hebrew is ASCII-only "
                    f"meta-label: {heb_field[:60]!r}"
                )

    return hard, warn


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--book", help="3-letter OT book code (e.g., GEN, RUT)")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--all", action="store_true",
                        help="Check all OT chapters (default if no --book)")
    parser.add_argument("--report", action="store_true",
                        help=f"Write a markdown report to {REPORTS}/")
    args = parser.parse_args()

    files = find_ot_chapter_files(args.book, args.chapter)
    if not files:
        print("No OT chapter files found (or none matching filter).")
        # Default-pass when there are no OT files yet — pre-pilot state.
        return 0

    total_hard, total_warn = [], []
    for fpath in files:
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            total_hard.append(f"[!] {fpath.name}: invalid JSON ({e})")
            continue
        if not isinstance(data, list):
            data = [data]
        for verse in data:
            if not isinstance(verse, dict):
                continue
            lang = verse.get("language", "")
            if lang not in ("hebrew", "aramaic"):
                continue  # skip NT verses if any leak in
            hard, warn = check_verse(verse, fpath.name)
            total_hard.extend(hard)
            total_warn.extend(warn)

    print(f"Hebrew field integrity — checked {len(files)} OT chapter file(s)")
    if total_hard:
        print(f"\nHARD FAILS ({len(total_hard)}):")
        for v in total_hard:
            print(f"  {v}")
    if total_warn:
        print(f"\nWARNINGS ({len(total_warn)}):")
        for v in total_warn[:20]:
            print(f"  {v}")
        if len(total_warn) > 20:
            print(f"  ... and {len(total_warn) - 20} more")

    if args.report:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out = REPORTS / "hebrew_field_integrity.md"
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Hebrew field integrity report\n\n")
            f.write(f"- Files checked: {len(files)}\n")
            f.write(f"- Hard fails: {len(total_hard)}\n")
            f.write(f"- Warnings: {len(total_warn)}\n\n")
            if total_hard:
                f.write("## Hard fails\n\n")
                for v in total_hard:
                    f.write(f"- {v}\n")
                f.write("\n")
            if total_warn:
                f.write("## Warnings\n\n")
                for v in total_warn:
                    f.write(f"- {v}\n")
        print(f"Wrote {out}")

    if total_hard:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
