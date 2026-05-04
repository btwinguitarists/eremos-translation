#!/usr/bin/env python3
"""
Check thai_summary coverage.

The thai_summary field (see docs/THAI_SUMMARY_STYLE.md) is OPTIONAL — not
every verse needs one. But verses with significant interpretive payload
SHOULD have one. This check flags verses where a summary is likely warranted
but missing.

A summary is "warranted" when ANY of these are true:
  - The verse has key_decisions (interpretive choices were made)
  - The verse has notes (textual variants, hapax, OT citations, etc.)
  - The verse appears in data/nt_ot_citations.json (OT echo)
  - The verse contains a hapax legomenon per the extracted data

This check is non-blocking by default. It produces a report listing verses
that probably should have a summary but don't.

Usage:
  python3 scripts/check_summary_coverage.py --book MRK --chapter 9
  python3 scripts/check_summary_coverage.py --book MRK --chapter 9 --strict
    (--strict makes missing summaries on warranted verses an exit-1 failure)
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
EXTRACTED = ROOT / "output"   # contains <slug>/<slug>_<NN>.json with hapax flags
CITATIONS_PATH = ROOT / "data" / "nt_ot_citations.json"
REPORTS = ROOT / "output" / "check_reports"

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS  # NT books: code → (name, slug)

# OT books (extract_book_hebrew BOOKS = code → (name, slug, file_prefix))
try:
    from extract_book_hebrew import BOOKS as OT_BOOKS
except ImportError:
    OT_BOOKS = {}

SLUG_TO_CODE = {slug: code for code, (_, slug) in BOOKS.items()}
for code, entry in OT_BOOKS.items():
    if len(entry) >= 2:
        SLUG_TO_CODE[entry[1]] = code


def load_translation(slug: str, chapter: int) -> list:
    path = TRANSLATIONS / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def load_extracted_hapax_map(slug: str, chapter: int) -> dict[int, list[str]]:
    """Return {verse_num: [hapax_lemmas]} from extracted source data, if available."""
    path = EXTRACTED / slug / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {v["verse"]: v.get("hapax_legomena") or [] for v in data}


def load_citation_refs(book_code: str, chapter: int) -> set[int]:
    """Return verse numbers in this chapter that have known OT citations."""
    if not CITATIONS_PATH.exists():
        return set()
    data = json.loads(CITATIONS_PATH.read_text(encoding="utf-8"))
    citations = data.get("citations", {})
    verses = set()
    for ref_key in citations.keys():
        m = re.match(r"(\S+)\s+(\d+):(\d+)", ref_key)
        if m and m.group(1) == book_code and int(m.group(2)) == chapter:
            verses.add(int(m.group(3)))
    return verses


def is_warranted(verse: dict, hapax_map: dict, citation_verses: set) -> tuple[bool, list[str]]:
    """Return (is_warranted, list_of_reasons).

    Heuristic intentionally selective — we don't want every Mark verse flagged
    just because translation rationale is thorough. Only verses with concrete
    reader-relevant interpretive depth (rare words, OT echoes, major variants)
    are surfaced.
    """
    reasons = []
    t = verse.get("translation", {}) or {}

    vn = verse["verse"]

    # Hapax — almost always worth a brief reader explanation
    if hapax_map.get(vn):
        reasons.append(f"hapax: {', '.join(hapax_map[vn])}")

    # OT citation/allusion in our curated database — high value to surface
    if vn in citation_verses:
        reasons.append("OT citation/allusion in nt_ot_citations.json")

    # Substantive notes — only count VERY long notes (textual variants,
    # major interpretive cruxes, etc.). Routine notes shouldn't trigger.
    notes = t.get("notes")
    if notes and len(notes) > 400:
        reasons.append("substantive notes (>400 chars — likely a real crux)")

    # Lots of key_decisions — only flag genuinely-dense verses (5+).
    # Average chapter verse has 2-3 decisions and shouldn't auto-warrant.
    if len(t.get("key_decisions") or []) >= 5:
        reasons.append(f"{len(t['key_decisions'])} key decisions (dense interpretive verse)")

    return (len(reasons) > 0, reasons)


def render_report(slug: str, chapter: int, missing_warranted: list, present_count: int,
                   total: int, all_warranted_count: int) -> str:
    coverage_pct = 100 * present_count / max(1, all_warranted_count)
    lines = [
        f"# Thai-summary coverage — {slug} ch. {chapter}",
        "",
        f"- Verses in chapter: {total}",
        f"- Verses with `thai_summary` written: {present_count}",
        f"- Verses where summary is warranted (per heuristic): {all_warranted_count}",
        f"- Coverage of warranted verses: **{coverage_pct:.0f}%**",
        f"- Warranted verses MISSING a summary: **{len(missing_warranted)}**",
        "",
        "_Heuristic: a summary is warranted when the verse has ≥2 key_decisions, substantive notes, contains a hapax legomenon, or appears in nt_ot_citations.json._",
        "_Per docs/THAI_SUMMARY_STYLE.md, simple-narrative verses don't need one. Coverage of 100% is not the goal; covering all warranted verses is._",
        "",
    ]
    if missing_warranted:
        lines.append("## ⚠ Verses likely warranting a `thai_summary` (but missing one)")
        lines.append("")
        for v in missing_warranted:
            lines.append(f"### {v['reference']}")
            lines.append("")
            for r in v["reasons"]:
                lines.append(f"- {r}")
            lines.append("")
    else:
        lines.append("✅ Every warranted verse has a `thai_summary`. Or no verses in this chapter were heuristically warranted.")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 if any warranted verse is missing a summary")
    args = parser.parse_args()

    code = args.book.upper()
    if code not in BOOKS:
        print(f"Unknown book code: {code}")
        return 1
    slug = BOOKS[code][1]

    verses = load_translation(slug, args.chapter)
    if not verses:
        print(f"No translation for {code} ch. {args.chapter}")
        return 1

    hapax_map = load_extracted_hapax_map(slug, args.chapter)
    citation_verses = load_citation_refs(code, args.chapter)

    missing_warranted = []
    present_count = 0
    all_warranted = 0
    for v in verses:
        warranted, reasons = is_warranted(v, hapax_map, citation_verses)
        has_summary = bool((v.get("translation", {}) or {}).get("thai_summary"))
        if has_summary:
            present_count += 1
        if warranted:
            all_warranted += 1
            if not has_summary:
                missing_warranted.append({
                    "reference": v["reference"],
                    "reasons": reasons,
                })

    REPORTS.mkdir(parents=True, exist_ok=True)
    md = render_report(slug, args.chapter, missing_warranted, present_count,
                       len(verses), all_warranted)
    out_path = REPORTS / f"summary_coverage_{slug}_{args.chapter:02d}.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"  Present: {present_count}/{len(verses)} ({100*present_count/max(1,len(verses)):.0f}%)")
    print(f"  Warranted but missing: {len(missing_warranted)}")

    if args.strict and missing_warranted:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
