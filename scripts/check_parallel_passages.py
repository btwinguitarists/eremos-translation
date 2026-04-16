#!/usr/bin/env python3
"""
Flag synoptic parallel passages where our renderings diverge.

For each entry in data/synoptic_parallels.json that has ≥2 translated parallels,
compares the Thai renderings. Same Greek words → should map to same Thai words.
Different Greek → expected to diverge.

Minimal for now — only applies when we have 2+ synoptic gospel chapters translated.

Usage:
  python3 scripts/check_parallel_passages.py
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
PARALLELS_PATH = ROOT / "data" / "synoptic_parallels.json"
REPORTS = ROOT / "output" / "check_reports"

CODE_TO_SLUG = {
    "MAT": "matthew", "MRK": "mark", "LUK": "luke", "JHN": "john",
}


def parse_ref(ref: str):
    """Parse 'MRK 1:9-11' → ('MRK', 1, 9, 11)."""
    m = re.match(r"(\w+)\s+(\d+):(\d+)(?:-(\d+))?", ref)
    if not m:
        return None
    book = m.group(1)
    chapter = int(m.group(2))
    start = int(m.group(3))
    end = int(m.group(4)) if m.group(4) else start
    return (book, chapter, start, end)


def load_verses_for_ref(ref: str):
    parsed = parse_ref(ref)
    if not parsed:
        return []
    book_code, chapter, start, end = parsed
    slug = CODE_TO_SLUG.get(book_code)
    if not slug:
        return []
    path = TRANSLATIONS / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        verses = json.load(f)
    return [v for v in verses if start <= v["verse"] <= end]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()

    with open(PARALLELS_PATH, encoding="utf-8") as f:
        groups = json.load(f)["groups"]

    usable_groups = []
    for g in groups:
        translated = []
        for ref in g["refs"]:
            verses = load_verses_for_ref(ref)
            if verses:
                translated.append({"ref": ref, "verses": verses})
        if len(translated) >= 2:
            usable_groups.append({"name": g["name"], "translated": translated})

    lines = ["# Synoptic parallel-passage check", ""]
    if not usable_groups:
        lines.append("No parallel-passage comparisons available yet — needs ≥2 synoptic passages translated.")
        lines.append("")
        lines.append("Parallel groups defined in `data/synoptic_parallels.json`:")
        for g in groups:
            lines.append(f"- **{g['name']}** — {', '.join(g['refs'])}")
    else:
        lines.append(f"Parallel groups with ≥2 translated passages: **{len(usable_groups)}**")
        lines.append("")
        for g in usable_groups:
            lines.append(f"## {g['name']}")
            lines.append("")
            # Show the Thai renderings side by side
            max_len = max(len(t["verses"]) for t in g["translated"])
            for row in range(max_len):
                for t in g["translated"]:
                    if row < len(t["verses"]):
                        v = t["verses"][row]
                        lines.append(f"- **{v['reference']}**: {v.get('translation', {}).get('thai', '')}")
                lines.append("")

    md = "\n".join(lines)
    if args.stdout:
        print(md)
    else:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS / "parallel_passages.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}")
        print(f"  Usable groups: {len(usable_groups)}")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
