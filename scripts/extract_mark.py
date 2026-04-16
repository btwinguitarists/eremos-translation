#!/usr/bin/env python3
"""
Extract Gospel of Mark verse-by-verse from MACULA Greek + BSB.

For each verse, produces a structured JSON object with:
  - Greek text (reconstructed from word order)
  - Word-by-word morphological analysis (lemma, POS, morphology, English gloss, semantic domain)
  - BSB English translation for reference
  - Flags for hapax legomena and unusual constructions
"""
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MACULA_TSV = ROOT / "sources" / "macula-greek" / "SBLGNT" / "tsv" / "macula-greek-SBLGNT.tsv"
BSB_TXT = ROOT / "sources" / "bsb-text" / "bsb.txt"
OUTPUT_DIR = ROOT / "output" / "mark"

BOOK_CODE = "MRK"
BOOK_NAME_BSB = "Mark"


def load_bsb_mark() -> dict[tuple[int, int], str]:
    """Load BSB verses for Mark into a dict keyed by (chapter, verse)."""
    verses = {}
    with open(BSB_TXT, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.startswith(f"{BOOK_NAME_BSB} "):
                continue
            # Format: "Mark 1:1\tIn the beginning..."
            parts = line.split("\t", 1)
            if len(parts) != 2:
                continue
            ref, text = parts
            m = re.match(rf"{BOOK_NAME_BSB} (\d+):(\d+)", ref)
            if m:
                verses[(int(m.group(1)), int(m.group(2)))] = text.strip()
    return verses


def compute_lemma_frequencies() -> dict[str, int]:
    """Count occurrences of each lemma across all of MACULA so we can flag hapax in Mark."""
    counts: dict[str, int] = defaultdict(int)
    with open(MACULA_TSV, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            lemma = row.get("lemma", "").strip()
            if lemma:
                counts[lemma] += 1
    return counts


def parse_ref(ref: str) -> tuple[str, int, int, int] | None:
    """Parse MACULA ref like 'MRK 1:1!1' into (book, chapter, verse, word_index)."""
    m = re.match(r"(\w+)\s+(\d+):(\d+)!(\d+)", ref)
    if not m:
        return None
    return (m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))


def extract_mark_verses(bsb_verses: dict, lemma_counts: dict) -> list[dict]:
    """Group MACULA words by verse for Mark, return list of verse dicts."""
    verses: dict[tuple[int, int], list[dict]] = defaultdict(list)

    with open(MACULA_TSV, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            ref = row.get("ref", "")
            parsed = parse_ref(ref)
            if not parsed or parsed[0] != BOOK_CODE:
                continue
            _, chapter, verse, word_idx = parsed
            verses[(chapter, verse)].append({
                "idx": word_idx,
                "text": row.get("text", "").strip(),
                "normalized": row.get("normalized", "").strip(),
                "lemma": row.get("lemma", "").strip(),
                "english_gloss": row.get("english", "").strip(),
                "gloss_phrase": row.get("gloss", "").strip(),
                "role": row.get("role", "").strip(),
                "class": row.get("class", "").strip(),
                "type": row.get("type", "").strip(),
                "strong": row.get("strong", "").strip(),
                "morph": row.get("morph", "").strip(),
                "person": row.get("person", "").strip(),
                "number": row.get("number", "").strip(),
                "gender": row.get("gender", "").strip(),
                "case": row.get("case", "").strip(),
                "tense": row.get("tense", "").strip(),
                "voice": row.get("voice", "").strip(),
                "mood": row.get("mood", "").strip(),
                "louw_nida": row.get("ln", "").strip(),
                "after": row.get("after", ""),
            })

    result = []
    for (chapter, verse), words in sorted(verses.items()):
        words.sort(key=lambda w: w["idx"])
        greek_text = "".join(w["text"] + (w["after"] or " ") for w in words).strip()

        # Flag hapax legomena (words appearing 1x in whole NT)
        hapax = [w["lemma"] for w in words if w["lemma"] and lemma_counts.get(w["lemma"], 0) == 1]

        result.append({
            "reference": f"Mark {chapter}:{verse}",
            "chapter": chapter,
            "verse": verse,
            "greek": greek_text,
            "bsb_english": bsb_verses.get((chapter, verse), ""),
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
    print("Loading BSB Mark verses...")
    bsb_verses = load_bsb_mark()
    print(f"  Loaded {len(bsb_verses)} BSB Mark verses")

    print("Computing NT-wide lemma frequencies (for hapax flagging)...")
    lemma_counts = compute_lemma_frequencies()
    print(f"  {len(lemma_counts)} unique lemmas in NT")

    print("Extracting Mark from MACULA...")
    verses = extract_mark_verses(bsb_verses, lemma_counts)
    print(f"  Extracted {len(verses)} verses")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Full book
    full_path = OUTPUT_DIR / "mark_verses.json"
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(verses, f, ensure_ascii=False, indent=2)
    print(f"  Wrote {full_path}")

    # Per-chapter files
    by_chapter: dict[int, list] = defaultdict(list)
    for v in verses:
        by_chapter[v["chapter"]].append(v)
    for ch, vs in by_chapter.items():
        p = OUTPUT_DIR / f"mark_{ch:02d}.json"
        with open(p, "w", encoding="utf-8") as f:
            json.dump(vs, f, ensure_ascii=False, indent=2)

    # Summary
    total_hapax = sum(len(v["hapax_legomena"]) for v in verses)
    print(f"\nSummary:")
    print(f"  Verses: {len(verses)}")
    print(f"  Chapters: {len(by_chapter)}")
    print(f"  Total hapax occurrences in Mark: {total_hapax}")
    print(f"  Sample verse (Mark 1:1):")
    first = next((v for v in verses if v["chapter"] == 1 and v["verse"] == 1), None)
    if first:
        print(f"    Greek: {first['greek']}")
        print(f"    BSB:   {first['bsb_english']}")
        print(f"    Words: {first['word_count']}")


if __name__ == "__main__":
    main()
