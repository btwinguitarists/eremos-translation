#!/usr/bin/env python3
"""
Flag verses in a NT chapter that quote or allude to OT texts.

Reports:
  - Direct citations (with source OT reference)
  - Paraphrases and allusions
  - Whether the Greek matches LXX or MT (when identified)
  - Whether our translation notes acknowledge the OT source

This doesn't automatically check that our Thai rendering harmonizes with our
Thai OT (we don't have an OT yet). When we do, it will also compare.

Usage:
  python3 scripts/check_ot_citations.py --book 1TI --chapter 3
  python3 scripts/check_ot_citations.py --book mark --chapter 1
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
CITATIONS_PATH = ROOT / "data" / "nt_ot_citations.json"
REPORTS = ROOT / "output" / "check_reports"

SLUG_TO_CODE = {
    "matthew": "MAT", "mark": "MRK", "luke": "LUK", "john": "JHN",
    "acts": "ACT", "romans": "ROM", "1corinthians": "1CO", "2corinthians": "2CO",
    "galatians": "GAL", "ephesians": "EPH", "philippians": "PHP", "colossians": "COL",
    "1thessalonians": "1TH", "2thessalonians": "2TH", "1timothy": "1TI", "2timothy": "2TI",
    "titus": "TIT", "philemon": "PHM", "hebrews": "HEB", "james": "JAS",
    "1peter": "1PE", "2peter": "2PE", "1john": "1JN", "2john": "2JN",
    "3john": "3JN", "jude": "JUD", "revelation": "REV",
}


def load_citations():
    with open(CITATIONS_PATH, encoding="utf-8") as f:
        return json.load(f)["citations"]


def check(book_code: str, chapter: int, translation_file: Path):
    citations_db = load_citations()
    with open(translation_file, encoding="utf-8") as f:
        verses = json.load(f)

    results = []
    for v in verses:
        ref_key = f"{book_code} {chapter}:{v['verse']}"
        citation = citations_db.get(ref_key)
        if not citation:
            continue

        notes_text = (v.get("translation", {}) or {}).get("notes", "") or ""
        # Also scan key_decisions rationales — OT links are sometimes noted there.
        rationales_text = " ".join(
            (d.get("rationale") or "") for d in (v.get("translation", {}) or {}).get("key_decisions", []) or []
        )
        scan_text = (notes_text + " " + rationales_text).lower()
        # Heuristic: did the translator already document this OT link?
        acknowledged = False
        for kw in ["ot ", "quot", "cit", "allu", "lxx", " mt ", "septuagint", "masoretic",
                   "isaiah", "isa ", "psalm", "ps ", "genesis", "gen ", "exodus", "exo ",
                   "deuteronomy", "deut", "malachi", "mal ", "job", "intertextual",
                   "อิสยาห์", "บทเพลง", "ปฐมกาล", "อ้างอิง"]:
            if kw in scan_text:
                acknowledged = True
                break

        results.append({
            "verse": v["reference"],
            "ref_key": ref_key,
            "type": citation["type"],
            "sources": citation.get("sources") or [citation.get("source")],
            "greek_matches": citation.get("greek_matches"),
            "citation_notes": citation.get("notes", ""),
            "notes_in_translation": notes_text,
            "acknowledged": acknowledged,
        })

    return results


def render_markdown(results, scope, total_verses):
    lines = [
        f"# OT citation check — {scope}",
        "",
        f"NT-to-OT links found: **{len(results)}** / {total_verses} verses",
        "",
    ]
    if not results:
        lines.append("No known OT citations or allusions in this chapter per our database.")
        lines.append("")
        lines.append("_Note: our `data/nt_ot_citations.json` is curated, not exhaustive. Passages with subtle allusions may not be listed._")
        return "\n".join(lines)

    unack = [r for r in results if not r["acknowledged"]]
    if unack:
        lines.append(f"## ⚠ Not yet acknowledged in verse notes: {len(unack)}")
        lines.append("")
        for r in unack:
            lines.append(f"### {r['verse']}")
            lines.append(f"- **Type**: {r['type']}")
            lines.append(f"- **OT source(s)**: {', '.join(r['sources'])}")
            if r['greek_matches']:
                lines.append(f"- **Greek matches**: {r['greek_matches']}")
            lines.append(f"- **Scholarly note**: {r['citation_notes']}")
            lines.append("")

    ack = [r for r in results if r["acknowledged"]]
    if ack:
        lines.append(f"## ✅ Acknowledged in verse notes: {len(ack)}")
        lines.append("")
        for r in ack:
            lines.append(f"- **{r['verse']}** — {', '.join(r['sources'])} ({r['type']})")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()

    slug = args.book.lower()
    code = SLUG_TO_CODE.get(slug)
    if not code:
        print(f"Unknown book slug: {slug}")
        return 1

    translation_file = TRANSLATIONS / f"{slug}_{args.chapter:02d}.json"
    if not translation_file.exists():
        print(f"No translation file at {translation_file}")
        return 1

    results = check(code, args.chapter, translation_file)

    with open(translation_file, encoding="utf-8") as f:
        total = len(json.load(f))

    md = render_markdown(results, f"{slug} ch. {args.chapter}", total)
    if args.stdout:
        print(md)
    else:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS / f"ot_citations_{slug}_{args.chapter:02d}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}")

    unack = sum(1 for r in results if not r["acknowledged"])
    if unack:
        print(f"  ⚠ {unack} OT link(s) not yet acknowledged in verse notes")
    return 1 if unack else 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
