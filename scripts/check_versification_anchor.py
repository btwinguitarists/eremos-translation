#!/usr/bin/env python3
"""
Versification anchor check — enforces MT-anchored verse numbers per
docs/translator_decisions/verse_schema_and_versification_2026-05.md.

Per the policy:
  - Eremos OT verses are anchored on Masoretic Text (MT) versification.
  - Where MT differs from English-Bible / LXX / Vulgate / BSB, the Eremos
    verse stays with MT; the divergence is recorded in the verse's
    `versification` sub-object (with mt_ref / english_ref / bsb_ref / lxx_ref
    / has_superscription / diverges fields).
  - Known divergence zones are pre-populated in data/versification_map.json:
    Psalms (~120 superscripted), Joel 3/2:28-32 boundary, Mal 3:19/4:1 split,
    minor Job 41 / 1 Sam 23-24 shifts, Jeremiah LXX-shorter ordering.

What this enforces:

  [A] HARD FAIL — A verse in a known-divergence zone (per data/versification_map.json)
      is missing its `versification` sub-object.

  [B] HARD FAIL — A verse's `versification.mt_ref` doesn't match its
      (book, chapter, verse) triple. (Catches drift between the verse's own
      reference and the map.)

  [C] WARN — A verse outside known-divergence zones has a `versification`
      sub-object. Either the map needs updating, or the entry is spurious.

Usage:
  python3 scripts/check_versification_anchor.py --book PSA --chapter 3
  python3 scripts/check_versification_anchor.py --all
  python3 scripts/check_versification_anchor.py --report

Exit codes:
  0 = clean
  1 = at least one hard fail
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
VERSIFICATION_MAP = DATA_DIR / "versification_map.json"
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


def load_versification_map() -> dict:
    """Load data/versification_map.json. Returns empty dict if not present yet."""
    if not VERSIFICATION_MAP.exists():
        return {}
    try:
        return json.loads(VERSIFICATION_MAP.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"WARNING: {VERSIFICATION_MAP} is invalid JSON", file=sys.stderr)
        return {}


def map_key(book_code: str, chapter: int, verse: int) -> str:
    """Versification map key: BOOK-CH-VS (e.g., PSA-3-1, JOL-3-1, MAL-3-19)."""
    return f"{book_code}-{chapter}-{verse}"


def find_ot_chapter_files(book_filter: str | None = None,
                          chapter_filter: int | None = None) -> list[Path]:
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


def check_verse(verse: dict, book_code: str, vmap: dict) -> tuple[list[str], list[str]]:
    hard: list[str] = []
    warn: list[str] = []
    chapter = verse.get("chapter")
    vno = verse.get("verse")
    ref = verse.get("reference", f"{book_code} {chapter}:{vno}")
    if chapter is None or vno is None:
        return hard, warn

    key = map_key(book_code, int(chapter), int(vno))
    in_divergence_zone = key in vmap and vmap[key].get("diverges", False)
    has_versification = isinstance(verse.get("versification"), dict)

    # [A] Divergence-zone verse missing the versification sub-object
    if in_divergence_zone and not has_versification:
        hard.append(
            f"[A] {ref}: in known-divergence zone (map key {key}) but "
            f"missing `versification` sub-object. See verse_schema_and_versification §2.1"
        )
        return hard, warn

    # [B] versification.mt_ref must match the verse's own coordinates
    if has_versification:
        v_block = verse["versification"]
        expected_mt_ref = vmap.get(key, {}).get("mt_ref") or \
                          f"{book_code} {chapter}:{vno}"
        actual_mt_ref = v_block.get("mt_ref", "")
        if actual_mt_ref and actual_mt_ref != expected_mt_ref:
            hard.append(
                f"[B] {ref}: `versification.mt_ref` is {actual_mt_ref!r} but "
                f"expected {expected_mt_ref!r} (drift between verse "
                f"coordinates and versification block)"
            )

    # [C] versification block on a non-divergence verse — possible spurious entry
    if has_versification and not in_divergence_zone:
        # Allow if the block explicitly says diverges=False AND records cross-tradition references
        v_block = verse["versification"]
        if v_block.get("diverges") is True:
            warn.append(
                f"[C] {ref}: has versification.diverges=true but key {key} not "
                f"in data/versification_map.json — map may need updating"
            )

    return hard, warn


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--book", help="3-letter OT book code")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--report", action="store_true",
                        help=f"Write a markdown report to {REPORTS}/")
    args = parser.parse_args()

    vmap = load_versification_map()
    if not vmap:
        # Pre-build state — no map yet. Default-pass with informational note.
        print(f"NOTE: {VERSIFICATION_MAP} not present yet. Skipping divergence "
              f"validation. (Build it before Phase 6F per plan §9.6.)")

    files = find_ot_chapter_files(args.book, args.chapter)
    if not files:
        print("No OT chapter files found (or none matching filter).")
        return 0

    total_hard, total_warn = [], []
    for fpath in files:
        m = re.match(r"^(.+)_(\d+)\.json$", fpath.name)
        slug = m.group(1)
        book_code = OT_SLUG_TO_CODE[slug]
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
            if verse.get("language") not in ("hebrew", "aramaic"):
                continue
            hard, warn = check_verse(verse, book_code, vmap)
            total_hard.extend(hard)
            total_warn.extend(warn)

    print(f"Versification anchor — checked {len(files)} OT chapter file(s)")
    print(f"  Map entries: {len(vmap)}")
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
        out = REPORTS / "versification_anchor.md"
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Versification anchor report\n\n")
            f.write(f"Per docs/translator_decisions/verse_schema_and_versification_2026-05.md\n\n")
            f.write(f"- Files checked: {len(files)}\n")
            f.write(f"- Map entries: {len(vmap)}\n")
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
