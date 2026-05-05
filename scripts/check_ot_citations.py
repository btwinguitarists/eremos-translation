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
    # OT slugs — see OT_SLUGS below for the rationale on why this check
    # default-passes for OT chapters.
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

# OT slugs — for these chapters, this script default-passes. The DB it checks
# (data/nt_ot_citations.json) records NT verses citing OT verses, which is
# meaningless when the chapter under check IS the OT. Inner-OT echoes (e.g.
# Ruth 2:14 noting the eat-be-satisfied-have-leftover formula at Deut 8:10 +
# Exod 16:18) are scholarly cross-references, not NT-OT-citation events, and
# they belong in a separate inner-OT-typology DB (not built yet — when it is,
# add the OT-side check here).
OT_SLUGS = frozenset({
    "genesis", "exodus", "leviticus", "numbers", "deuteronomy",
    "joshua", "judges", "ruth",
    "1samuel", "2samuel", "1kings", "2kings",
    "1chronicles", "2chronicles", "ezra", "nehemiah", "esther",
    "job", "psalms", "proverbs", "ecclesiastes", "songofsongs",
    "isaiah", "jeremiah", "lamentations", "ezekiel", "daniel",
    "hosea", "joel", "amos", "obadiah", "jonah", "micah",
    "nahum", "habakkuk", "zephaniah", "haggai", "zechariah", "malachi",
})


def load_citations():
    with open(CITATIONS_PATH, encoding="utf-8") as f:
        return json.load(f)["citations"]


# Regex for explicit OT book references appearing in translator notes.
OT_REF_RE = re.compile(
    r"\b(?:Gen|Exod?|Lev|Num|Deut|Josh|Judg|Ruth|1\s?Sam|2\s?Sam|1\s?Kgs?|2\s?Kgs?|"
    r"1\s?Chr|2\s?Chr|Ezra|Neh|Esth|Job|Ps|Psa|Prov|Eccl|Song|Isa|Jer|Lam|Ezek|"
    r"Dan|Hos|Joel|Amos|Obad|Jonah|Mic|Nah|Hab|Zeph|Hag|Zech|Mal)\.?\s*\d+(?::\d+)?",
    re.IGNORECASE,
)

# Strong self-attributions: when one of these phrases appears WITHIN ~80 chars
# of an OT book reference, the translator has claimed an intertextual link at
# THIS verse — the curated DB MUST have a corresponding entry. Requiring the
# phrase near the reference (not just in the note somewhere) avoids false
# positives from synoptic-parallel mentions or negated claims.
STRONG_CITATION_PHRASES = [
    "OT CITATION",
    "OT INTERTEXT",
    "OT ECHO",
    "DIRECT CITATION",
    "COMPOSITE CITATION",
    "TRIPLE ALLUSION",
    "COMPOSITE ALLUSION",
    "LXX CITATION",
    "NEAR-VERBATIM",
    "NEAR-CITATION",
    "QUASI-VERBATIM",
    "OT CITATION DATABASE",
    "ADDED TO NT_OT_CITATIONS",
    "ALLUSION AT",
    "CITATION AT",
    "FULFILLS",
    "FULFILLMENT:",  # colon restricts to the 'ISA 53:7 FULFILLMENT:' heading form
    "FULFILMENT:",
    "ECHO:",
    "ECHOES",  # 'X ECHOES' / 'X ECHOES Y'
]

# Negation phrases that suppress a strong match — prevents 'NOT an OT citation'
# from firing drift.
NEGATION_MARKERS = [
    "NOT AN OT",
    "NOT A DIRECT",
    "NOT A FORMAL",
    "NOT A CITATION",
    "NOT DIRECT",
]

_PROXIMITY_WINDOW = 80  # chars between strong phrase and OT ref


def scan_notes_for_drift_candidates(verses) -> dict[str, set[str]]:
    """Return {verse_ref: {ot_refs}} for verses where the translator's notes
    make a citation-claim co-located with an OT reference. Proximity required
    (±80 chars) so that cross-reference mentions elsewhere in a long note
    don't fire."""
    found: dict[str, set[str]] = {}
    for v in verses:
        notes = (v.get("translation", {}) or {}).get("notes", "") or ""
        rats = " ".join(
            (d.get("rationale") or "")
            for d in (v.get("translation", {}) or {}).get("key_decisions", []) or []
        )
        combined = notes + " " + rats
        upper = combined.upper()

        # Any negation that suppresses the claim in this verse? If one appears,
        # we require that a strong phrase also appears AFTER the negation,
        # otherwise skip. (E.g. 'NOT an OT citation but... then Ps X cited at
        # v.Y' would still ship without drift — handled by requiring proximity
        # below; this block short-circuits the simple 'NOT an OT citation' case.)
        negated_fully = any(n in upper for n in NEGATION_MARKERS)
        if negated_fully and not any(
            p in upper[upper.find(next(n for n in NEGATION_MARKERS if n in upper)) + 20:]
            for p in ["OT CITATION DATABASE", "ADDED TO NT_OT_CITATIONS"]
        ):
            continue

        # Collect OT ref positions
        ref_positions = [(m.start(), m.group(0)) for m in OT_REF_RE.finditer(combined)]
        if not ref_positions:
            continue

        # For each strong phrase, check if an OT ref sits within the proximity window
        triggered_refs: set[str] = set()
        for phrase in STRONG_CITATION_PHRASES:
            start = 0
            while True:
                idx = upper.find(phrase, start)
                if idx < 0:
                    break
                for pos, ref in ref_positions:
                    if abs(pos - idx) <= _PROXIMITY_WINDOW:
                        triggered_refs.add(ref)
                start = idx + len(phrase)
        if triggered_refs:
            found[v["reference"]] = triggered_refs
    return found


def check(book_code: str, chapter: int, translation_file: Path):
    citations_db = load_citations()
    with open(translation_file, encoding="utf-8") as f:
        verses = json.load(f)

    results = []
    db_refs_for_chapter = set()
    for v in verses:
        ref_key = f"{book_code} {chapter}:{v['verse']}"
        citation = citations_db.get(ref_key)
        if not citation:
            continue
        db_refs_for_chapter.add(v["reference"])

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

    # Drift detection: notes make an explicit citation-claim at a verse but the
    # DB has no entry. Catches the silent-drop-of-DB-updates failure mode.
    candidates = scan_notes_for_drift_candidates(verses)
    drift = {
        verse_ref: refs
        for verse_ref, refs in candidates.items()
        if verse_ref not in db_refs_for_chapter
    }

    return results, drift


def render_markdown(results, drift, scope, total_verses):
    lines = [
        f"# OT citation check — {scope}",
        "",
        f"NT-to-OT links found: **{len(results)}** / {total_verses} verses",
        "",
    ]

    if drift:
        lines.append(f"## 🚨 DB DRIFT — {len(drift)} verse(s) have OT refs in notes but no DB entry")
        lines.append("")
        lines.append("The translator's notes identify OT book references for these verses,")
        lines.append("but `data/nt_ot_citations.json` has no entry. This means the curated DB")
        lines.append("has fallen out of sync with the translation work — add entries before ship.")
        lines.append("")
        for verse_ref, refs in sorted(drift.items()):
            lines.append(f"- **{verse_ref}** — refs mentioned in notes: {', '.join(sorted(refs))}")
        lines.append("")

    if not results:
        if drift:
            lines.append("_(No DB-recorded citations yet — see DB drift section above.)_")
        else:
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

    # Default-pass for OT chapters. The check's DB models NT-cites-OT; an OT
    # chapter cannot have NT-OT-citation events, and inner-OT echoes (Ruth
    # 2:14 → Deut 8:10, etc.) are a separate concern handled by the planned
    # check_nt_quotation_alignment.py + an inner-OT-typology DB once built.
    if slug in OT_SLUGS:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS / f"ot_citations_{slug}_{args.chapter:02d}.md"
        out_path.write_text(
            f"# OT citation check — {slug} ch. {args.chapter}\n\n"
            f"_Skipped — this is an OT chapter, and `data/nt_ot_citations.json` "
            f"models NT-cites-OT (not OT-cites-OT). Inner-OT echoes are tracked "
            f"in `key_decisions` rationales and will be validated by the planned "
            f"`check_nt_quotation_alignment.py` + inner-OT-typology DB._\n",
            encoding="utf-8",
        )
        print(f"Wrote {out_path} (OT chapter — default-pass)")
        return 0

    results, drift = check(code, args.chapter, translation_file)

    with open(translation_file, encoding="utf-8") as f:
        total = len(json.load(f))

    md = render_markdown(results, drift, f"{slug} ch. {args.chapter}", total)
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
    if drift:
        print(f"  🚨 {len(drift)} verse(s) have OT refs in notes but no DB entry — DB drift")
    # Fail on drift OR unacknowledged — both indicate the chapter isn't ship-ready
    return 1 if (unack or drift) else 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
