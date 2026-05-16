#!/usr/bin/env python3
"""
Proper-noun + ethnonym alignment check — enforces data/proper_noun_locks.json.

Per docs/translator_decisions/proper_names_and_transliteration_2026-05.md
and the DEU end-of-book audit §Z (2026-05-16): when a verse's Thai field
contains a known-rejected surface form for a locked proper-noun lemma, the
check HARD-FAILs. This is the prevention layer for the F1 (Pisgah ปิสกาห์ vs
พิสกาห์) and F2 (seven-nations prefix/suffix drift) classes flagged by both
Gemini and ChatGPT.

Why Thai-side detection (not Hebrew→Thai cross-check)?
  Short Hebrew roots produce too many false positives via substring matching
  (e.g., חוי [Hiwwi] = חיה [live]; חתי [Hittite] = חתת [be dismayed]). The
  drift we care about is "wrong Thai surface in use" — that is fully
  detectable on the Thai field alone. The proper-noun lock data lists both
  the canonical surface and the surfaces that have been observed as drift
  in past audits; any of the rejected surfaces appearing anywhere in the
  corpus is a hard-fail.

What this enforces (per lock entry in data/proper_noun_locks.json):

  [A] No verse in the corpus may have any 'thai_rejected' surface in its
      Thai field — HARD-FAIL.

  [B] (informational) Every verse that mentions the lemma's Thai canonical
      form is logged for forward auditability.

Usage:
  python3 scripts/check_proper_nouns.py --book DEU --chapter 7
  python3 scripts/check_proper_nouns.py --all
  python3 scripts/check_proper_nouns.py --report
  python3 scripts/check_proper_nouns.py --all --include-canonical    # also list canonical-found hits

Exit codes:
  0 = clean
  1 = at least one rejected-surface violation found
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
DATA = ROOT / "data"
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
OT_CODE_TO_SLUG = {v: k for k, v in OT_SLUG_TO_CODE.items()}


def load_locks() -> list[dict]:
    with (DATA / "proper_noun_locks.json").open(encoding="utf-8") as f:
        return json.load(f)["locks"]


def iter_all_translation_files():
    for path in sorted(TRANSLATIONS.glob("*.json")):
        name = path.stem
        if "_" not in name:
            continue
        slug, ch_part = name.rsplit("_", 1)
        if not ch_part.isdigit():
            continue
        # OT-only (NT files use the same shape but we focus on OT for the
        # current lock set). NT can be added when its lemma locks are added.
        if slug not in OT_SLUG_TO_CODE:
            continue
        yield path


def check_file(path: Path, locks: list[dict]) -> tuple[list[dict], list[dict]]:
    """Return (rejected_hits, canonical_hits) for the given file."""
    rejected_hits: list[dict] = []
    canonical_hits: list[dict] = []
    with path.open(encoding="utf-8") as f:
        verses = json.load(f)
    for verse in verses:
        ref = verse.get("reference", "?")
        thai = (verse.get("translation", {}) or {}).get("thai", "") or ""
        for lock in locks:
            exceptions = lock.get("exceptions", {}) or {}
            if ref in exceptions:
                continue
            for bad in lock.get("thai_rejected", []) or []:
                if bad in thai:
                    rejected_hits.append({
                        "verse": ref,
                        "lemma_id": lock["lemma_id"],
                        "rejected_surface": bad,
                        "expected": lock["thai_canonical"],
                        "thai_excerpt": thai[:160],
                    })
            if lock["thai_canonical"] in thai:
                canonical_hits.append({
                    "verse": ref,
                    "lemma_id": lock["lemma_id"],
                    "canonical_surface": lock["thai_canonical"],
                })
    return rejected_hits, canonical_hits


def format_rejected(v: dict) -> str:
    return (f"  ✗ {v['verse']} [{v['lemma_id']}] "
            f"uses rejected '{v['rejected_surface']}' (expected '{v['expected']}') — "
            f"Thai: {v['thai_excerpt']}")


def write_report(rejected: list[dict], canonical: list[dict],
                 include_canonical: bool) -> Path:
    REPORTS.mkdir(parents=True, exist_ok=True)
    report = REPORTS / "proper_nouns.md"
    lines = ["# Proper-noun + ethnonym lock audit",
             "",
             "Source: `data/proper_noun_locks.json` (per "
             "`docs/translator_decisions/proper_names_and_transliteration_2026-05.md`).",
             ""]
    if not rejected:
        lines.append("✓ No rejected proper-noun + ethnonym surfaces found.")
    else:
        lines.append(f"✗ {len(rejected)} rejected-surface violation(s):")
        lines.append("")
        for v in rejected:
            lines.append(format_rejected(v))
    if include_canonical and canonical:
        lines.append("")
        lines.append(f"## Canonical-surface occurrences ({len(canonical)})")
        lines.append("")
        for v in canonical:
            lines.append(f"  ✓ {v['verse']} [{v['lemma_id']}] {v['canonical_surface']}")
    report.write_text("\n".join(lines), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", help="Book code (e.g. DEU) or slug (deuteronomy)")
    parser.add_argument("--chapter", type=int, help="Chapter number")
    parser.add_argument("--all", action="store_true", help="Audit all OT chapters")
    parser.add_argument("--report", action="store_true",
                        help="Write report to output/check_reports/proper_nouns.md")
    parser.add_argument("--include-canonical", action="store_true",
                        help="Also list canonical-surface occurrences in the report")
    args = parser.parse_args()

    locks = load_locks()
    all_rejected: list[dict] = []
    all_canonical: list[dict] = []

    if args.all:
        for path in iter_all_translation_files():
            r, c = check_file(path, locks)
            all_rejected.extend(r)
            all_canonical.extend(c)
    else:
        if not args.book or args.chapter is None:
            print("ERROR: --book + --chapter required (or use --all)", file=sys.stderr)
            return 2
        book_code = args.book.upper() if len(args.book) == 3 else OT_SLUG_TO_CODE.get(args.book.lower(), args.book.upper())
        slug = OT_CODE_TO_SLUG.get(book_code, args.book.lower())
        path = TRANSLATIONS / f"{slug}_{args.chapter:02d}.json"
        if path.exists():
            r, c = check_file(path, locks)
            all_rejected.extend(r)
            all_canonical.extend(c)

    if args.report:
        path = write_report(all_rejected, all_canonical, args.include_canonical)
        print(f"Report: {path}")

    if not all_rejected:
        print(f"✓ No rejected proper-noun + ethnonym surfaces found "
              f"({len(all_canonical)} canonical-surface occurrence(s)).")
        return 0

    print(f"✗ {len(all_rejected)} rejected-surface violation(s):")
    for v in all_rejected:
        print(format_rejected(v))
    return 1


if __name__ == "__main__":
    sys.exit(main())
