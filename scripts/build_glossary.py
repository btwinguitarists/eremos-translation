#!/usr/bin/env python3
"""
Build glossary.json by aggregating all key_decisions from translated chapters.

Produces a persistent ledger:
  - For each Greek lemma, the canonical Thai rendering(s) chosen
  - The first verse where each rendering appears
  - All rationale text associated with that lemma

Usage:
  python3 scripts/build_glossary.py              # rebuild from all chapters
  python3 scripts/build_glossary.py --check      # report inconsistencies without writing

This is run both:
  - When seeding: after the first chapter is translated
  - During check: before committing a new chapter, to detect drift
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
GLOSSARY_PATH = ROOT / "glossary.json"


def normalize_greek_key(greek: str) -> str:
    """The key_decisions[*].greek field is informal — sometimes a lemma,
    sometimes a phrase, sometimes with parsing annotation. Normalize to
    extract the core word(s) as a lookup key."""
    if not greek:
        return ""
    # Strip parenthetical notes like "(perf. pass.)" or "(HAPAX)"
    cleaned = re.sub(r"\s*\([^)]+\)\s*", " ", greek).strip()
    # Strip trailing parsing like "(gen.)" that sometimes escapes
    cleaned = re.sub(r"\s+\([^)]*$", "", cleaned)
    return cleaned.strip()


def collect_decisions():
    """Walk all chapter translation files and collect key_decisions."""
    # Greek key → list of (verse_ref, thai_rendering, rationale, raw_greek)
    by_greek: dict[str, list] = defaultdict(list)

    for chapter_file in sorted(TRANSLATIONS.glob("*.json")):
        if "_demo" in chapter_file.name:
            continue
        with open(chapter_file, encoding="utf-8") as f:
            try:
                verses = json.load(f)
            except json.JSONDecodeError:
                print(f"[warn] Could not parse {chapter_file.name}")
                continue
        if not isinstance(verses, list):
            continue
        for v in verses:
            ref = v.get("reference", "")
            t = v.get("translation", {})
            for d in t.get("key_decisions", []) or []:
                raw_greek = d.get("greek", "")
                key = normalize_greek_key(raw_greek)
                thai = d.get("thai", "")
                rationale = d.get("rationale", "")
                if key and thai:
                    by_greek[key].append({
                        "verse": ref,
                        "thai": thai,
                        "rationale": rationale,
                        "raw_greek": raw_greek,
                    })
    return by_greek


def build_glossary(by_greek: dict) -> dict:
    """Collapse into a clean glossary structure."""
    entries = {}
    for greek_key, occurrences in sorted(by_greek.items()):
        # Group by thai rendering
        renderings = defaultdict(list)
        for occ in occurrences:
            renderings[occ["thai"]].append({
                "verse": occ["verse"],
                "rationale": occ["rationale"],
            })

        # Primary rendering = most frequent; ties broken by first appearance
        primary = max(
            renderings.items(),
            key=lambda kv: (len(kv[1]), -list(renderings.keys()).index(kv[0]))
        )[0]

        entries[greek_key] = {
            "primary_thai": primary,
            "all_renderings": dict(renderings),
            "occurrences_count": len(occurrences),
        }

    return {
        "version": "0.1",
        "generated_from": "output/translations/*.json",
        "note": "Auto-generated. Edit output/translations/<chapter>.json — do not hand-edit this file.",
        "entries": entries,
    }


def report_inconsistencies(glossary: dict) -> list[str]:
    """Flag lemmas with multiple renderings that may not be justified."""
    flags = []
    for greek, entry in glossary["entries"].items():
        renderings = entry["all_renderings"]
        if len(renderings) > 1:
            # Multiple renderings — likely fine if contextually varied, but surface for review
            total = entry["occurrences_count"]
            minority_rendering = min(renderings.items(), key=lambda kv: len(kv[1]))
            flags.append(
                f"  [{greek}] {len(renderings)} renderings across {total} occurrences — "
                f"primary='{entry['primary_thai']}', variant='{minority_rendering[0]}' "
                f"at {minority_rendering[1][0]['verse']}"
            )
    return flags


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Only report, do not write glossary")
    args = parser.parse_args()

    by_greek = collect_decisions()
    glossary = build_glossary(by_greek)

    print(f"Lemmas tracked: {len(glossary['entries'])}")
    print(f"Total decisions: {sum(e['occurrences_count'] for e in glossary['entries'].values())}")

    flags = report_inconsistencies(glossary)
    if flags:
        print(f"\nLemmas with multiple renderings (review):")
        for f in flags:
            print(f)
    else:
        print("\nAll lemmas have a single rendering.")

    if not args.check:
        with open(GLOSSARY_PATH, "w", encoding="utf-8") as f:
            json.dump(glossary, f, ensure_ascii=False, indent=2)
        print(f"\nWrote {GLOSSARY_PATH}")


if __name__ == "__main__":
    main()
