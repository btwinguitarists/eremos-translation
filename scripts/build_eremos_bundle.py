#!/usr/bin/env python3
"""
Transform output/translations/<slug>_<NN>.json files into a single bundle JSON
for the Eremos app: [{book, chapter, verse, thai, thai_literal, key_decisions, notes}].

Walks every translated chapter of every book found in output/translations/,
maps the filename slug back to the canonical 3-letter MACULA book code, and
writes ~/EremosVercel2/server/data/eremos_translation.json sorted by
canonical book order → chapter → verse.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
EREMOS_DATA = Path.home() / "EremosVercel2" / "server" / "data" / "eremos_translation.json"

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS  # {code: (name, slug)}

SLUG_TO_CODE = {slug: code for code, (_, slug) in BOOKS.items()}
CODE_ORDER = {code: i for i, code in enumerate(BOOKS.keys())}
FILENAME_RE = re.compile(r"^(?P<slug>[a-z0-9]+)_(?P<chapter>\d{2})\.json$")


def main():
    bundle = []
    for chapter_file in sorted(TRANSLATIONS.glob("*_*.json")):
        if "_demo" in chapter_file.name:
            continue
        m = FILENAME_RE.match(chapter_file.name)
        if not m:
            continue
        slug = m.group("slug")
        code = SLUG_TO_CODE.get(slug)
        if code is None:
            print(f"  skip (unknown slug): {chapter_file.name}")
            continue
        with open(chapter_file, encoding="utf-8") as f:
            verses = json.load(f)
        for v in verses:
            t = v.get("translation", {})
            bundle.append({
                "book": code,
                "chapter": v["chapter"],
                "verse": v["verse"],
                "thai": t.get("thai", ""),
                "thai_literal": t.get("thai_literal") or None,
                "thai_summary": t.get("thai_summary") or None,
                "key_decisions": t.get("key_decisions") or [],
                "notes": t.get("notes") or None,
            })

    bundle.sort(key=lambda v: (CODE_ORDER.get(v["book"], 999), v["chapter"], v["verse"]))

    EREMOS_DATA.parent.mkdir(parents=True, exist_ok=True)
    with open(EREMOS_DATA, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)
    book_counts = {}
    for v in bundle:
        book_counts[v["book"]] = book_counts.get(v["book"], 0) + 1
    print(f"Wrote {len(bundle)} verses to {EREMOS_DATA}")
    print(f"  Size: {EREMOS_DATA.stat().st_size:,} bytes")
    for code, count in book_counts.items():
        print(f"  {code}: {count} verses")


if __name__ == "__main__":
    main()
