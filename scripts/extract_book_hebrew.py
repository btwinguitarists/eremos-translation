#!/usr/bin/env python3
"""
Extract a Hebrew/Aramaic OT book (or single chapter) from MACULA Hebrew + BSB.

Sibling to scripts/extract_book.py (which handles the NT). Same output schema
modulo the Hebrew/Aramaic source-language fields.

Usage:
  python3 scripts/extract_book_hebrew.py --book GEN              # whole book
  python3 scripts/extract_book_hebrew.py --book RUT --chapter 1  # single chapter
  python3 scripts/extract_book_hebrew.py --list                  # list known books

Output:
  output/<book-slug>/<book-slug>_verses.json     (full book, if extracted)
  output/<book-slug>/<book-slug>_<NN>.json       (per-chapter files)

For each verse, produces a structured JSON object with:
  - hebrew or aramaic source text (reconstructed from per-word unicode + after)
  - language: "hebrew" or "aramaic" (per docs/translator_decisions/verse_schema_and_versification_2026-05.md)
  - word-by-word morphology (lemma, pos, morph, English gloss, Strong's H-number)
  - inline LXX equivalents (per-word `greek` field from MACULA Hebrew, when present)
  - BSB English reference
  - hapax flags (lemmas occurring once across the whole OT)

Per docs/source_license_policy.md §2.2: MACULA Hebrew bundles SDBH-derived
semantic-domain fields (sdbh / lexdomain / coredomain / sensenumber). These
are exposed in the morphology block for translator consultation but should
NOT be republished verbatim outside the MACULA bundle. Use them as keys
into our own glossary work, not as standalone data.

Aramaic sections (Daniel 2:4b–7:28; Ezra 4:8–6:18, 7:12–26; Jer 10:11;
Gen 31:47b) are extracted with `language: "aramaic"`. The dispatcher in
run_checks.py routes accordingly per plan §9.4.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MACULA_LOWFAT_DIR = ROOT / "sources" / "macula-hebrew" / "WLC" / "lowfat"
BSB_TXT = ROOT / "sources" / "bsb-text" / "bsb.txt"
XML_NS_ID = "{http://www.w3.org/XML/1998/namespace}id"

# MACULA OT book code → (BSB book name, friendly slug, file prefix)
# File prefix matches the NN-Xxx form used by macula-hebrew/WLC/lowfat/
BOOKS = {
    "GEN": ("Genesis",         "genesis",         "01-Gen"),
    "EXO": ("Exodus",          "exodus",          "02-Exo"),
    "LEV": ("Leviticus",       "leviticus",       "03-Lev"),
    "NUM": ("Numbers",         "numbers",         "04-Num"),
    "DEU": ("Deuteronomy",     "deuteronomy",     "05-Deu"),
    "JOS": ("Joshua",          "joshua",          "06-Jos"),
    "JDG": ("Judges",          "judges",          "07-Jdg"),
    "RUT": ("Ruth",            "ruth",            "08-Rut"),
    "1SA": ("1 Samuel",        "1samuel",         "09-1Sa"),
    "2SA": ("2 Samuel",        "2samuel",         "10-2Sa"),
    "1KI": ("1 Kings",         "1kings",          "11-1Ki"),
    "2KI": ("2 Kings",         "2kings",          "12-2Ki"),
    "1CH": ("1 Chronicles",    "1chronicles",     "13-1Ch"),
    "2CH": ("2 Chronicles",    "2chronicles",     "14-2Ch"),
    "EZR": ("Ezra",            "ezra",            "15-Ezr"),
    "NEH": ("Nehemiah",        "nehemiah",        "16-Neh"),
    "EST": ("Esther",          "esther",          "17-Est"),
    "JOB": ("Job",             "job",             "18-Job"),
    "PSA": ("Psalms",          "psalms",          "19-Psa"),
    "PRO": ("Proverbs",        "proverbs",        "20-Pro"),
    "ECC": ("Ecclesiastes",    "ecclesiastes",    "21-Ecc"),
    "SNG": ("Song of Songs",   "songofsongs",     "22-Sng"),
    "ISA": ("Isaiah",          "isaiah",          "23-Isa"),
    "JER": ("Jeremiah",        "jeremiah",        "24-Jer"),
    "LAM": ("Lamentations",    "lamentations",    "25-Lam"),
    "EZK": ("Ezekiel",         "ezekiel",         "26-Ezk"),
    "DAN": ("Daniel",          "daniel",          "27-Dan"),
    "HOS": ("Hosea",           "hosea",           "28-HOS"),
    "JOL": ("Joel",            "joel",            "29-Jol"),
    "AMO": ("Amos",            "amos",            "30-Amo"),
    "OBA": ("Obadiah",         "obadiah",         "31-Oba"),
    "JON": ("Jonah",           "jonah",           "32-Jon"),
    "MIC": ("Micah",           "micah",           "33-Mic"),
    "NAM": ("Nahum",           "nahum",           "34-Nam"),
    "HAB": ("Habakkuk",        "habakkuk",        "35-Hab"),
    "ZEP": ("Zephaniah",       "zephaniah",       "36-Zep"),
    "HAG": ("Haggai",          "haggai",          "37-Hag"),
    "ZEC": ("Zechariah",       "zechariah",       "38-Zec"),
    "MAL": ("Malachi",         "malachi",         "39-Mal"),
}

# MACULA's lang attribute → schema language field
LANG_MAP = {"H": "hebrew", "A": "aramaic"}

REF_RX = re.compile(r"(\S+)\s+(\d+):(\d+)!(\d+)")


def load_bsb(book_name: str) -> dict[tuple[int, int], str]:
    """Load BSB verses for the OT book, keyed by (chapter, verse)."""
    verses: dict[tuple[int, int], str] = {}
    prefix = f"{book_name} "
    rx = re.compile(rf"{re.escape(book_name)} (\d+):(\d+)")
    with open(BSB_TXT, encoding="utf-8") as f:
        for line in f:
            if not line.startswith(prefix):
                continue
            parts = line.rstrip("\n").split("\t", 1)
            if len(parts) != 2:
                continue
            ref, text = parts
            m = rx.match(ref)
            if m:
                verses[(int(m.group(1)), int(m.group(2)))] = text.strip()
    return verses


def parse_ref(ref: str) -> tuple[str, int, int, int] | None:
    m = REF_RX.match(ref or "")
    if not m:
        return None
    return (m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))


def chapter_xml_files(book_prefix: str) -> list[Path]:
    """Return per-chapter XML files for a book, sorted by chapter."""
    files = sorted(MACULA_LOWFAT_DIR.glob(f"{book_prefix}-*-lowfat.xml"))
    return files


def chapter_number_from_filename(path: Path) -> int | None:
    m = re.search(r"-(\d+)-lowfat\.xml$", path.name)
    return int(m.group(1)) if m else None


def iter_words(xml_path: Path):
    """Yield (chapter, verse, word_idx, attrib, text) for every <w> in a chapter file."""
    tree = ET.parse(xml_path)
    for w in tree.iter("w"):
        ref = w.get("ref", "")
        parsed = parse_ref(ref)
        if not parsed:
            continue
        _, chapter, verse, word_idx = parsed
        yield chapter, verse, word_idx, dict(w.attrib), (w.text or "")


def load_verse_surface_text(xml_path: Path) -> dict[tuple[int, int], str]:
    """Map (chapter, verse) → surface Hebrew/Aramaic text from <milestone> tails.

    MACULA's <w> elements include analytical duplicates (a noun can appear once as
    object of a preposition and again as the head of a construct chain). Concatenating
    them re-emits the duplicate. The <milestone unit="verse" id="..."/> element's
    tail inside each <sentence> carries the clean MT surface text.
    """
    tree = ET.parse(xml_path)
    surface: dict[tuple[int, int], str] = {}
    for sent in tree.iter("sentence"):
        sid = sent.get("id", "")
        m = re.match(r"\S+\s+(\d+):(\d+)", sid)
        if not m:
            continue
        ch, vs = int(m.group(1)), int(m.group(2))
        for ms in sent.iter("milestone"):
            if ms.get("unit") != "verse":
                continue
            text = (ms.tail or "").strip()
            if text:
                surface[(ch, vs)] = text
                break
    return surface


def compute_lemma_frequencies(book_codes: list[str] | None = None) -> dict[str, int]:
    """Compute lemma counts across the whole OT (or a subset)."""
    counts: dict[str, int] = defaultdict(int)
    codes = book_codes or list(BOOKS.keys())
    for code in codes:
        prefix = BOOKS[code][2]
        for path in chapter_xml_files(prefix):
            for _, _, _, attrib, _ in iter_words(path):
                lemma = (attrib.get("lemma") or "").strip()
                if lemma:
                    counts[lemma] += 1
    return counts


def extract(
    book_code: str,
    book_name: str,
    bsb: dict,
    lemma_counts: dict,
    chapter_filter: int | None,
):
    book_prefix = BOOKS[book_code][2]
    # Verses keyed by (chapter, verse) — per the schema, a verse has ONE language.
    # For boundary verses (Dan 2:4 Heb→Aram split, Gen 31:47 Heb+Aram, Jer 10:11),
    # the verse-level `language` reflects the majority of its words; per-word `lang`
    # in the words[] array preserves the word-level distinction for analysis.
    verses: dict[tuple[int, int], list[dict]] = defaultdict(list)
    # (chapter, verse) → surface Hebrew/Aramaic text from <milestone> tail
    surface_by_verse: dict[tuple[int, int], str] = {}

    for path in chapter_xml_files(book_prefix):
        ch_no = chapter_number_from_filename(path)
        if ch_no is None:
            continue
        if chapter_filter is not None and ch_no != chapter_filter:
            continue
        surface_by_verse.update(load_verse_surface_text(path))
        for chapter, verse, word_idx, attrib, text in iter_words(path):
            unicode_text = (attrib.get("unicode") or text or "").strip()
            after = attrib.get("after", "")
            verses[(chapter, verse)].append({
                "idx": word_idx,
                "unicode": unicode_text,
                "after": after,
                "lemma": (attrib.get("lemma") or "").strip(),
                "stronglemma": (attrib.get("stronglemma") or "").strip(),
                "transliteration": (attrib.get("transliteration") or "").strip(),
                "english_gloss": (attrib.get("english") or "").strip(),
                "phrase_gloss": (attrib.get("gloss") or "").strip(),
                "pos": (attrib.get("pos") or "").strip(),
                "morph": (attrib.get("morph") or "").strip(),
                "person": (attrib.get("person") or "").strip(),
                "gender": (attrib.get("gender") or "").strip(),
                "number": (attrib.get("number") or "").strip(),
                "state": (attrib.get("state") or "").strip(),
                "stem": (attrib.get("stem") or "").strip(),
                "type": (attrib.get("type") or "").strip(),
                "class": (attrib.get("class") or "").strip(),
                "role": (attrib.get("role") or "").strip(),
                "strong": (attrib.get("strongnumberx") or "").strip(),
                "lxx_greek": (attrib.get("greek") or "").strip(),
                "lxx_greek_strong": (attrib.get("greekstrong") or "").strip(),
                "sdbh": (attrib.get("sdbh") or "").strip(),
                "lexdomain": (attrib.get("lexdomain") or "").strip(),
                "coredomain": (attrib.get("coredomain") or "").strip(),
                "sensenumber": (attrib.get("sensenumber") or "").strip(),
                "lang": (attrib.get("lang") or "H").strip(),
            })

    result = []
    for (chapter, verse), words in sorted(verses.items()):
        words.sort(key=lambda w: w["idx"])
        # Verse language = majority of word-level lang attrs ("H"/"A").
        word_langs = [(w["lang"] or "H").upper() for w in words]
        is_aramaic = word_langs.count("A") > word_langs.count("H")
        lang = "aramaic" if is_aramaic else "hebrew"
        # Surface text: prefer the <milestone> tail (true MT surface) over a
        # word-by-word concatenation (which would re-emit MACULA's analytical
        # duplicates — e.g., "Bethlehem" appearing as both prep-object and
        # construct-head in Ruth 1:1).
        source_text = surface_by_verse.get((chapter, verse), "")
        if not source_text:
            source_text = "".join(
                (w["unicode"] or "") + (w["after"] or "") for w in words
            ).strip()
        hapax = [
            w["lemma"]
            for w in words
            if w["lemma"] and lemma_counts.get(w["lemma"], 0) == 1
        ]

        verse_obj: dict = {
            "reference": f"{book_name} {chapter}:{verse}",
            "chapter": chapter,
            "verse": verse,
            "language": lang,
            "bsb_english": bsb.get((chapter, verse), ""),
            "word_count": len(words),
            "hapax_legomena": hapax,
            "words": [
                {
                    "unicode": w["unicode"],
                    "lemma": w["lemma"],
                    "stronglemma": w["stronglemma"],
                    "transliteration": w["transliteration"],
                    "english_gloss": w["english_gloss"],
                    "phrase_gloss": w["phrase_gloss"],
                    "pos": w["pos"],
                    "class": w["class"],
                    "type": w["type"],
                    "role": w["role"],
                    "lang": LANG_MAP.get((w["lang"] or "H").upper(), "hebrew"),
                    "morphology": {
                        "morph": w["morph"],
                        "person": w["person"],
                        "gender": w["gender"],
                        "number": w["number"],
                        "state": w["state"],
                        "stem": w["stem"],
                    },
                    "strong": w["strong"],
                    "lxx_comparator": (
                        {
                            "greek": w["lxx_greek"],
                            "greek_strong": w["lxx_greek_strong"],
                        }
                        if w["lxx_greek"]
                        else None
                    ),
                    "semantic_domain": (
                        {
                            "sdbh": w["sdbh"],
                            "lexdomain": w["lexdomain"],
                            "coredomain": w["coredomain"],
                            "sensenumber": w["sensenumber"],
                        }
                        if (w["sdbh"] or w["lexdomain"] or w["coredomain"])
                        else None
                    ),
                    "ot_frequency": lemma_counts.get(w["lemma"], 0),
                }
                for w in words
            ],
        }

        # Source text under language-specific field (per verse_schema_and_versification §1.1)
        verse_obj[lang] = source_text

        result.append(verse_obj)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Extract a Hebrew/Aramaic OT book from MACULA Hebrew + BSB"
    )
    parser.add_argument("--book", help="3-letter book code (e.g., GEN, RUT)")
    parser.add_argument("--chapter", type=int, help="Single chapter to extract")
    parser.add_argument("--list", action="store_true", help="List known book codes")
    parser.add_argument(
        "--lemma-scope",
        choices=["all-ot", "this-book"],
        default="all-ot",
        help="Frequency scope for hapax flagging (default: all-ot)",
    )
    args = parser.parse_args()

    if args.list:
        print("Known OT books (code → name):")
        for code, (name, _, _) in BOOKS.items():
            print(f"  {code:4s} → {name}")
        return

    if not args.book:
        parser.error("--book is required (or use --list)")

    code = args.book.upper()
    if code not in BOOKS:
        print(f"Unknown OT book code: {code}. Run --list for options.")
        sys.exit(1)

    book_name, slug, _ = BOOKS[code]
    out_dir = ROOT / "output" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading BSB {book_name}...")
    bsb = load_bsb(book_name)
    print(f"  {len(bsb)} BSB verses")

    if args.lemma_scope == "all-ot":
        print("Computing OT-wide lemma frequencies (all 39 books)...")
        lemma_counts = compute_lemma_frequencies(None)
    else:
        print(f"Computing lemma frequencies (scope: {book_name} only)...")
        lemma_counts = compute_lemma_frequencies([code])
    print(f"  {len(lemma_counts)} unique lemmas")

    chapter_label = f" ch.{args.chapter}" if args.chapter else ""
    print(f"Extracting {book_name}{chapter_label}...")
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
    aramaic_count = sum(1 for v in verses if v.get("language") == "aramaic")
    if aramaic_count:
        print(f"\nAramaic verses: {aramaic_count}")
    print(f"Total hapax occurrences: {total_hapax}")


if __name__ == "__main__":
    main()
