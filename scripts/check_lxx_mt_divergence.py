#!/usr/bin/env python3
"""
LXX-MT divergence check — surfaces places where the Septuagint differs from
the Masoretic Text, for translator + auditor review.

Per docs/translator_decisions/ot_canon_and_text_base_2026-05.md §"When to
depart from MT" exception #4: where MT and LXX differ at scale (Jeremiah
~1/8 shorter in LXX; 1 Sam 17 has whole verses missing in LXX; Esther LXX
has six "Greek additions"; Daniel 3 LXX-Theodotion has the Song of the
Three additions): translate **MT only**; document the LXX-only material
in a Tier 3 footer note; do **not** include the LXX-only material in the
main text.

This script is **METADATA-only initially** per plan §9.1 (script #12). It
logs divergences without blocking ship. Promote to strict at Phase 6G
(Major Prophets — Jeremiah is heavy-divergence territory).

Three roles:

  1. Surface known LXX-MT divergence zones — catalogues the chapters where
     Eremos curators must explicitly choose MT-only or document additions.

  2. Verify translator decisions — when a verse is in a known divergence
     zone, flag it if the verse's `key_decisions` doesn't acknowledge the
     LXX-MT relationship.

  3. Audit-cross-check — for NT-cited OT verses where the NT followed LXX
     over MT (Heb 1:6 quoting Deut 32:43 LXX-form, Matt 1:23 quoting
     Isa 7:14 LXX-form, Acts 2:17-21 quoting Joel 2:28-32 LXX-form), the
     Eremos OT (which translates MT) must document the alignment-or-
     divergence with the already-shipped NT.

Data source: data/lxx_mt_divergences.json — running registry of known
divergences with witness IDs + scholarly assessments. Format:
  {
    "JER-25-13": {
      "type": "lxx-shorter",
      "lxx_assessment": "LXX has 25:13 ending; MT continues into oracles vs nations",
      "scholarly_consensus": "MT preserves longer/later edition",
      "eremos_choice": "MT-only; LXX-divergence noted in Tier 3 footer"
    },
    ...
  }

Usage:
  python3 scripts/check_lxx_mt_divergence.py --book JER --chapter 25
  python3 scripts/check_lxx_mt_divergence.py --all
  python3 scripts/check_lxx_mt_divergence.py --report

Exit codes:
  0 = clean (metadata-only stage)
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
LXX_MT_DIVERGENCES = DATA_DIR / "lxx_mt_divergences.json"
NT_OT_CITATIONS = DATA_DIR / "ot_citations_used_in_nt.json"
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

LXX_KEYWORDS = re.compile(
    r"\b(lxx|septuagint|rahlfs|göttingen|gottingen|"
    r"theodotion|symmachus|aquila|"
    r"hexapla|origen|mt-vs-lxx|lxx-vs-mt|"
    r"lxx-shorter|lxx-longer|lxx-aligned|"
    r"lxx-divergent|greek-additions)\b",
    re.IGNORECASE,
)


def load_divergences() -> dict:
    if not LXX_MT_DIVERGENCES.exists():
        return {}
    try:
        return json.loads(LXX_MT_DIVERGENCES.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"WARNING: {LXX_MT_DIVERGENCES} invalid JSON", file=sys.stderr)
        return {}


def load_nt_citations() -> dict:
    """ot_citations_used_in_nt: maps OT verse-key → list of NT verses + LXX/MT alignment notes."""
    if not NT_OT_CITATIONS.exists():
        return {}
    try:
        return json.loads(NT_OT_CITATIONS.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
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
    out = []
    for kd in verse.get("key_decisions", []) or []:
        if isinstance(kd, dict):
            for v in kd.values():
                if isinstance(v, str):
                    out.append(v)
        elif isinstance(kd, str):
            out.append(kd)
    return " ".join(out)


def check_verse(verse: dict, book_code: str, divergences: dict, nt_citations: dict) -> list[str]:
    """Return list of WARN messages."""
    warns: list[str] = []
    chapter = verse.get("chapter")
    vno = verse.get("verse")
    ref = verse.get("reference", f"{book_code} {chapter}:{vno}")
    key = f"{book_code}-{chapter}-{vno}"

    # Role 1+2: divergence-zone verse should acknowledge LXX-MT relationship
    if key in divergences:
        rationale = kd_text(verse)
        if not LXX_KEYWORDS.search(rationale):
            div_info = divergences[key]
            div_type = div_info.get("type", "unspecified")
            warns.append(
                f"[LXX-MT] {ref}: known divergence ({div_type}) per "
                f"data/lxx_mt_divergences.json, but verse's key_decisions "
                f"doesn't mention LXX. Document the MT-only choice + "
                f"any LXX-additions deferred to Tier 3 footer"
            )

    # Role 3: NT-cited OT verses where NT followed LXX
    nt_cite = nt_citations.get(key)
    if nt_cite and isinstance(nt_cite, dict):
        if nt_cite.get("nt_followed") == "lxx":
            rationale = kd_text(verse)
            if not LXX_KEYWORDS.search(rationale):
                nt_refs = ", ".join(nt_cite.get("nt_verses", []))
                warns.append(
                    f"[LXX-MT-NT] {ref}: NT cite at {nt_refs} followed LXX "
                    f"form; OT translates MT. Document the alignment "
                    f"divergence + cross-reference in thai_summary"
                )

    return warns


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--book", help="3-letter OT book code")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--report", action="store_true")
    args = parser.parse_args()

    divergences = load_divergences()
    nt_citations = load_nt_citations()

    if not divergences:
        print(f"NOTE: {LXX_MT_DIVERGENCES} not present yet. Build it as "
              f"divergence cases are documented (Phase 6G — Jeremiah heavy).")
    if not nt_citations:
        print(f"NOTE: {NT_OT_CITATIONS} not present yet (planned in Day 14).")

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
            total_warns.extend(check_verse(verse, book_code, divergences, nt_citations))

    print(f"LXX-MT divergence — checked {len(files)} OT chapter file(s)")
    print(f"  Known divergence sites: {len(divergences)}")
    print(f"  NT-citation entries: {len(nt_citations)}")
    if total_warns:
        print(f"\nWARNINGS ({len(total_warns)}):")
        for w in total_warns[:20]:
            print(f"  {w}")
        if len(total_warns) > 20:
            print(f"  ... and {len(total_warns) - 20} more")

    if args.report:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out = REPORTS / "lxx_mt_divergence.md"
        with open(out, "w", encoding="utf-8") as f:
            f.write("# LXX-MT divergence check report\n\n")
            f.write(f"Per docs/translator_decisions/ot_canon_and_text_base_2026-05.md\n\n")
            f.write(f"- Files checked: {len(files)}\n")
            f.write(f"- Known divergences: {len(divergences)}\n")
            f.write(f"- NT-citations: {len(nt_citations)}\n")
            f.write(f"- Warnings: {len(total_warns)}\n\n")
            if total_warns:
                f.write("## Warnings (metadata-only at this stage)\n\n")
                for w in total_warns:
                    f.write(f"- {w}\n")
        print(f"Wrote {out}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
