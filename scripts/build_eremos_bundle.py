#!/usr/bin/env python3
"""
Transform output/translations/mark_XX.json files into a single bundle JSON
for the Eremos app: [{book, chapter, verse, thai, thai_literal, key_decisions, notes}].

Writes to ~/EremosVercel2/server/data/eremos_translation.json
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
EREMOS_DATA = Path.home() / "EremosVercel2" / "server" / "data" / "eremos_translation.json"

BOOK_CODE = "MRK"

def main():
    bundle = []
    for chapter_file in sorted(TRANSLATIONS.glob("mark_*.json")):
        if "_demo" in chapter_file.name:
            continue
        with open(chapter_file, encoding="utf-8") as f:
            verses = json.load(f)
        for v in verses:
            t = v.get("translation", {})
            bundle.append({
                "book": BOOK_CODE,
                "chapter": v["chapter"],
                "verse": v["verse"],
                "thai": t.get("thai", ""),
                "thai_literal": t.get("thai_literal") or None,
                "key_decisions": t.get("key_decisions") or [],
                "notes": t.get("notes") or None,
            })

    EREMOS_DATA.parent.mkdir(parents=True, exist_ok=True)
    with open(EREMOS_DATA, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(bundle)} verses to {EREMOS_DATA}")
    print(f"  Size: {EREMOS_DATA.stat().st_size:,} bytes")

if __name__ == "__main__":
    main()
