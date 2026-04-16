#!/usr/bin/env python3
"""
Extract a book (or single chapter) from MACULA Greek + BSB.

Usage:
  python3 scripts/extract_book.py --book MRK              # whole book
  python3 scripts/extract_book.py --book 1TI --chapter 3  # single chapter
  python3 scripts/extract_book.py --list                  # list known books

Output:
  output/<book-slug>/<book-slug>_verses.json     (full book, if extracted)
  output/<book-slug>/<book-slug>_<NN>.json       (per-chapter files)

For each verse, produces a structured JSON object with Greek text,
word-by-word morphology (lemma, POS, morphology, English gloss, semantic
domain), BSB English reference, and hapax flags.
"""
import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MACULA_TSV = ROOT / "sources" / "macula-greek" / "SBLGNT" / "tsv" / "macula-greek-SBLGNT.tsv"
BSB_TXT = ROOT / "sources" / "bsb-text" / "bsb.txt"

# MACULA book code → (BSB book name, friendly slug)
BOOKS = {
    "MAT": ("Matthew",         "matthew"),
    "MRK": ("Mark",            "mark"),
    "LUK": ("Luke",            "luke"),
    "JHN": ("John",            "john"),
    "ACT": ("Acts",            "acts"),
    "ROM": ("Romans",          "romans"),
    "1CO": ("1 Corinthians",   "1corinthians"),
    "2CO": ("2 Corinthians",   "2corinthians"),
    "GAL": ("Galatians",       "galatians"),
    "EPH": ("Ephesians",       "ephesians"),
    "PHP": ("Philippians",     "philippians"),
    "COL": ("Colossians",      "colossians"),
    "1TH": ("1 Thessalonians", "1thessalonians"),
    "2TH": ("2 Thessalonians", "2thessalonians"),
    "1TI": ("1 Timothy",       "1timothy"),
    "2TI": ("2 Timothy",       "2timothy"),
    "TIT": ("Titus",           "titus"),
    "PHM": ("Philemon",        "philemon"),
    "HEB": ("Hebrews",         "hebrews"),
    "JAS": ("James",           "james"),
    "1PE": ("1 Peter",         "1peter"),
    "2PE": ("2 Peter",         "2peter"),
    "1JN": ("1 John",           "1john"),
    "2JN": ("2 John",           "2john"),
    "3JN": ("3 John",           "3john"),
    "JUD": ("Jude",            "jude"),
    "REV": ("Revelation",      "revelation"),
}


def load_bsb(book_name: str) -> dict[tuple[int, int], str]:
    """Load BSB verses for the book, keyed by (chapter, verse)."""
    verses = {}
    # BSB text uses "1 Timothy" etc. Some book names have numeric prefix.
    prefix = f"{book_name} "
    with open(BSB_TXT, encoding="utf-8") as f:
        for line in f:
            if not line.startswith(prefix):
                continue
            parts = line.rstrip("\n").split("\t", 1)
            if len(parts) != 2:
                continue
            ref, text = parts
            m = re.match(rf"{re.escape(book_name)} (\d+):(\d+)", ref)
            if m:
                verses[(int(m.group(1)), int(m.group(2)))] = text.strip()
    return verses


def compute_lemma_frequencies() -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    with open(MACULA_TSV, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            lemma = (row.get("lemma") or "").strip()
            if lemma:
                counts[lemma] += 1
    return counts


def parse_ref(ref: str) -> tuple[str, int, int, int] | None:
    m = re.match(r"(\S+)\s+(\d+):(\d+)!(\d+)", ref)
    if not m:
        return None
    return (m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))


def extract(book_code: str, book_name: str, bsb: dict, lemma_counts: dict, chapter_filter: int | None):
    verses: dict[tuple[int, int], list[dict]] = defaultdict(list)

    with open(MACULA_TSV, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            parsed = parse_ref(row.get("ref", ""))
            if not parsed or parsed[0] != book_code:
                continue
            _, chapter, verse, word_idx = parsed
            if chapter_filter is not None and chapter != chapter_filter:
                continue
            verses[(chapter, verse)].append({
                "idx": word_idx,
                "text": (row.get("text") or "").strip(),
                "normalized": (row.get("normalized") or "").strip(),
                "lemma": (row.get("lemma") or "").strip(),
                "english_gloss": (row.get("english") or "").strip(),
                "gloss_phrase": (row.get("gloss") or "").strip(),
                "role": (row.get("role") or "").strip(),
                "class": (row.get("class") or "").strip(),
                "type": (row.get("type") or "").strip(),
                "strong": (row.get("strong") or "").strip(),
                "morph": (row.get("morph") or "").strip(),
                "person": (row.get("person") or "").strip(),
                "number": (row.get("number") or "").strip(),
                "gender": (row.get("gender") or "").strip(),
                "case": (row.get("case") or "").strip(),
                "tense": (row.get("tense") or "").strip(),
                "voice": (row.get("voice") or "").strip(),
                "mood": (row.get("mood") or "").strip(),
                "louw_nida": (row.get("ln") or "").strip(),
                "after": (row.get("after") or ""),
            })

    result = []
    for (chapter, verse), words in sorted(verses.items()):
        words.sort(key=lambda w: w["idx"])
        greek_text = "".join(w["text"] + (w["after"] or " ") for w in words).strip()
        hapax = [w["lemma"] for w in words if w["lemma"] and lemma_counts.get(w["lemma"], 0) == 1]

        result.append({
            "reference": f"{book_name} {chapter}:{verse}",
            "chapter": chapter,
            "verse": verse,
            "greek": greek_text,
            "bsb_english": bsb.get((chapter, verse), ""),
            "word_count": len(words),
            "hapax_legomena": hapax,
            "words": [
                {
                    "greek": w["text"],
                    "lemma": w["lemma"],
                    "english_gloss": w["english_gloss"],
                    "phrase_gloss": w["gloss_phrase"],
                    "class": w["class"],
                    "type": w["type"],
                    "morphology": {
                        "tense": w["tense"],
                        "voice": w["voice"],
                        "mood": w["mood"],
                        "person": w["person"],
                        "number": w["number"],
                        "gender": w["gender"],
                        "case": w["case"],
                    },
                    "strong": w["strong"],
                    "louw_nida": w["louw_nida"],
                    "nt_frequency": lemma_counts.get(w["lemma"], 0),
                }
                for w in words
            ],
        })
    return result


def main():
    parser = argparse.ArgumentParser(description="Extract a book from MACULA + BSB")
    parser.add_argument("--book", help="3-letter book code (e.g., MRK, 1TI)")
    parser.add_argument("--chapter", type=int, help="Single chapter to extract")
    parser.add_argument("--list", action="store_true", help="List known book codes")
    args = parser.parse_args()

    if args.list:
        print("Known books (code → name):")
        for code, (name, _) in BOOKS.items():
            print(f"  {code:4s} → {name}")
        return

    if not args.book:
        parser.error("--book is required (or use --list)")

    code = args.book.upper()
    if code not in BOOKS:
        print(f"Unknown book code: {code}. Run --list for options.")
        sys.exit(1)

    book_name, slug = BOOKS[code]
    out_dir = ROOT / "output" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading BSB {book_name}...")
    bsb = load_bsb(book_name)
    print(f"  {len(bsb)} BSB verses")

    print("Computing NT-wide lemma frequencies...")
    lemma_counts = compute_lemma_frequencies()

    print(f"Extracting {book_name}{' ch.' + str(args.chapter) if args.chapter else ''}...")
    verses = extract(code, book_name, bsb, lemma_counts, args.chapter)
    print(f"  {len(verses)} verses extracted")

    if args.chapter:
        p = out_dir / f"{slug}_{args.chapter:02d}.json"
        with open(p, "w", encoding="utf-8") as f:
            json.dump(verses, f, ensure_ascii=False, indent=2)
        print(f"Wrote {p}")
    else:
        p_full = out_dir / f"{slug}_verses.json"
        with open(p_full, "w", encoding="utf-8") as f:
            json.dump(verses, f, ensure_ascii=False, indent=2)
        print(f"Wrote {p_full}")
        by_chapter: dict[int, list] = defaultdict(list)
        for v in verses:
            by_chapter[v["chapter"]].append(v)
        for ch, vs in by_chapter.items():
            p = out_dir / f"{slug}_{ch:02d}.json"
            with open(p, "w", encoding="utf-8") as f:
                json.dump(vs, f, ensure_ascii=False, indent=2)
        print(f"  + {len(by_chapter)} per-chapter files")

    total_hapax = sum(len(v["hapax_legomena"]) for v in verses)
    print(f"\nTotal hapax occurrences: {total_hapax}")


if __name__ == "__main__":
    main()
