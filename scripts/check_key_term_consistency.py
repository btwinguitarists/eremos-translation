#!/usr/bin/env python3
"""
Key-term consistency audit.

For each Greek lemma that appears in multiple verses across our translations,
reports all Thai renderings. Flags lemmas with >1 distinct rendering as
requiring justified divergence.

Also cross-checks against the RULES.md §4 canonical term list — any deviation
from the fixed standards is a hard flag.

Usage:
  python3 scripts/check_key_term_consistency.py                 # audit all
  python3 scripts/check_key_term_consistency.py --book 1TI      # only 1 Timothy
  python3 scripts/check_key_term_consistency.py --book 1TI --chapter 3
  python3 scripts/check_key_term_consistency.py --json          # JSON output

Outputs a markdown report to output/check_reports/key_term_consistency.md
(or printed to stdout with --stdout).
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"

# From RULES.md §4 — these are hard-coded canonical renderings. Any deviation
# without explicit notes is flagged as a rule violation.
CANONICAL_TERMS = {
    "εὐαγγέλιον":   "ข่าวประเสริฐ",
    "εὐαγγελίου":   "ข่าวประเสริฐ",
    "εὐαγγελίῳ":    "ข่าวประเสริฐ",
    "χριστός":      "พระคริสต์",
    "χριστοῦ":      "พระคริสต์",
    "Ἰησοῦς":       "พระเยซู",
    "Ἰησοῦ":        "พระเยซู",
    "Ἰησοῦν":       "พระเยซู",
    "σατανᾶς":      "ซาตาน",
    "σατανᾶ":       "ซาตาน",
    "πνεῦμα ἅγιον": "พระวิญญาณบริสุทธิ์",
    "πνεύματι ἁγίῳ": "พระวิญญาณบริสุทธิ์",
    "βαπτίζω":      "บัพติศมา",
    "βάπτισμα":     "บัพติศมา",
    "ἔρημος":       "ถิ่นทุรกันดาร",   # wilderness region
    "ἐρήμῳ":        "ถิ่นทุรกันดาร",
    "συναγωγή":     "ธรรมศาลา",
    "συναγωγῇ":     "ธรรมศาลา",
    "συναγωγήν":    "ธรรมศาลา",
    "μετάνοια":     "การกลับใจ",
    "μετανοίας":    "การกลับใจ",
    "μετανοεῖτε":   "กลับใจ",
    "μετανοέω":     "กลับใจ",
    "βασιλεία":     "อาณาจักร",
    "ἁμαρτία":      "บาป",
    "ἁμαρτιῶν":     "บาป",
    "ἁμαρτίας":     "บาป",
    "ἀγαπητός":     "ที่รัก",
}


def normalize_greek(greek: str) -> str:
    if not greek:
        return ""
    cleaned = re.sub(r"\s*\([^)]+\)\s*", " ", greek).strip()
    cleaned = re.sub(r"\s+\([^)]*$", "", cleaned)
    return cleaned.strip()


def load_translations(book_filter: str | None, chapter_filter: int | None):
    """Walk chapter translation files; return list of (ref, book_slug, chapter, decisions)."""
    results = []
    for ch_file in sorted(TRANSLATIONS.glob("*.json")):
        if "_demo" in ch_file.name:
            continue
        # Filename pattern: <bookslug>_<NN>.json
        m = re.match(r"(.+?)_(\d+)\.json$", ch_file.name)
        if not m:
            continue
        slug = m.group(1)
        chapter = int(m.group(2))
        if book_filter and slug.lower() != book_filter.lower():
            continue
        if chapter_filter is not None and chapter != chapter_filter:
            continue
        with open(ch_file, encoding="utf-8") as f:
            verses = json.load(f)
        results.append((slug, chapter, verses))
    return results


def audit(loaded):
    """For each Greek lemma, collect all (verse, thai, rationale)."""
    by_greek: dict[str, list] = defaultdict(list)
    for slug, chapter, verses in loaded:
        for v in verses:
            ref = v.get("reference", f"{slug} {chapter}:?")
            for d in (v.get("translation", {}) or {}).get("key_decisions", []) or []:
                key = normalize_greek(d.get("greek", ""))
                thai = d.get("thai", "")
                rationale = d.get("rationale", "")
                if key and thai:
                    by_greek[key].append({
                        "verse": ref,
                        "thai": thai,
                        "rationale": rationale,
                    })
    return by_greek


def build_report(by_greek: dict) -> dict:
    """Group into consistency categories."""
    rule_violations = []     # deviation from CANONICAL_TERMS
    inconsistencies = []     # multiple renderings without explicit rationale per variant
    consistent_multi = []    # multiple renderings WITH per-variant rationale
    consistent_single = []   # single rendering across occurrences

    for greek, occs in sorted(by_greek.items()):
        renderings = defaultdict(list)
        for occ in occs:
            renderings[occ["thai"]].append(occ)

        # Rule check
        canonical = CANONICAL_TERMS.get(greek)
        if canonical:
            for thai, occ_list in renderings.items():
                if thai != canonical:
                    rule_violations.append({
                        "greek": greek,
                        "expected": canonical,
                        "found": thai,
                        "where": [o["verse"] for o in occ_list],
                    })

        # Consistency check
        if len(renderings) == 1:
            consistent_single.append({
                "greek": greek,
                "thai": list(renderings.keys())[0],
                "count": len(occs),
            })
        else:
            # Multiple renderings — check if each has explicit rationale
            all_have_rationale = all(
                any(o.get("rationale", "").strip() for o in occ_list)
                for occ_list in renderings.values()
            )
            entry = {
                "greek": greek,
                "renderings": {th: [o["verse"] for o in ol] for th, ol in renderings.items()},
                "rationales_present": all_have_rationale,
            }
            (consistent_multi if all_have_rationale else inconsistencies).append(entry)

    return {
        "rule_violations": rule_violations,
        "inconsistencies": inconsistencies,
        "consistent_multi": consistent_multi,
        "consistent_single_count": len(consistent_single),
    }


def render_markdown(report: dict, scope: str) -> str:
    lines = [
        f"# Key-term consistency check — {scope}",
        "",
        f"- Rule violations: **{len(report['rule_violations'])}**",
        f"- Undocumented multi-renderings: **{len(report['inconsistencies'])}**",
        f"- Documented multi-renderings: {len(report['consistent_multi'])}",
        f"- Consistent single renderings: {report['consistent_single_count']}",
        "",
    ]

    if report["rule_violations"]:
        lines.append("## ❌ Rule violations (RULES.md §4)")
        lines.append("")
        lines.append("| Greek | Expected | Found | Verses |")
        lines.append("|-------|----------|-------|--------|")
        for v in report["rule_violations"]:
            lines.append(f"| {v['greek']} | {v['expected']} | {v['found']} | {', '.join(v['where'])} |")
        lines.append("")

    if report["inconsistencies"]:
        lines.append("## ⚠ Multi-rendering without documented rationale")
        lines.append("")
        for e in report["inconsistencies"]:
            lines.append(f"### {e['greek']}")
            for thai, verses in e["renderings"].items():
                lines.append(f"- **{thai}** at {', '.join(verses)}")
            lines.append("")

    if report["consistent_multi"]:
        lines.append("## ✅ Documented multi-renderings (contextual variance)")
        lines.append("")
        for e in report["consistent_multi"]:
            lines.append(f"- **{e['greek']}** — {', '.join(f'{th} ({len(vs)}x)' for th, vs in e['renderings'].items())}")
        lines.append("")

    lines.append("## ✅ Single-rendering lemmas")
    lines.append("")
    lines.append(f"{report['consistent_single_count']} lemmas each translated consistently across every occurrence. See `glossary.json` for the full list.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", help="Filter by book slug (e.g., mark, 1timothy)")
    parser.add_argument("--chapter", type=int, help="Filter by chapter")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of markdown")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout instead of writing file")
    args = parser.parse_args()

    loaded = load_translations(args.book, args.chapter)
    if not loaded:
        print("No translations found.")
        return 1

    scope = f"{args.book or 'all books'}"
    if args.chapter:
        scope += f" ch. {args.chapter}"

    by_greek = audit(loaded)
    report = build_report(by_greek)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    md = render_markdown(report, scope)
    if args.stdout:
        print(md)
    else:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out_name = f"key_term_consistency_{args.book or 'all'}"
        if args.chapter:
            out_name += f"_{args.chapter:02d}"
        out_path = REPORTS / f"{out_name}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}")
        print(f"  Rule violations: {len(report['rule_violations'])}")
        print(f"  Undocumented multi-renderings: {len(report['inconsistencies'])}")

    # Exit code: 1 if any rule violations or undocumented inconsistencies
    if report["rule_violations"] or report["inconsistencies"]:
        return 1
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
