#!/usr/bin/env python3
"""Extract the BSB structural apparatus (section headings, paragraph breaks,
poetry indentation, Selah, acrostic/psalm headings) from the public-domain
Berean Standard Bible spreadsheet into a per-book JSON layer.

Source: sources/bsb/download/bsb_tables.xlsx, sheet `biblosinterlinear96`,
which is word-aligned and BSB-versified — the same versification the Eremos
translation uses — so the structure maps 1:1 onto our verses.

Columns (0-indexed, values_only), confirmed against src/parseSpreadsheet.ts:
    12  verseRef   "Genesis 1:1"  (present only on a verse's first word)
    13  headingFmt "<p class=|hdg|>The Creation"
    15  paraFmt    "<p class=|reg|>"  /  "<p class=|indent1|>" ...
    18  text       the English token (unused here)

Output: data/structure_bsb/<slug>.json — an ordered list of structure events
keyed to (chapter, verse). This is the ENGLISH-only layer; Thai headings are
added by a later pass. Additive: never reads or writes verse translations.

CC0 provenance: the BSB text and apparatus are dedicated to the public domain
(sources/bsb/LICENSE.md). This derived structure layer is likewise CC0.
"""
from __future__ import annotations

import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

# Hebrew alphabet: codepoint -> transliterated stanza name (Psalm 119, Lamentations).
ACROSTIC_NAMES = {
    0x05D0: "Aleph", 0x05D1: "Beth", 0x05D2: "Gimel", 0x05D3: "Daleth",
    0x05D4: "He", 0x05D5: "Waw", 0x05D6: "Zayin", 0x05D7: "Heth",
    0x05D8: "Teth", 0x05D9: "Yodh", 0x05DB: "Kaph", 0x05DC: "Lamed",
    0x05DE: "Mem", 0x05E0: "Nun", 0x05E1: "Samek", 0x05E2: "Ayin",
    0x05E4: "Pe", 0x05E6: "Tsadhe", 0x05E7: "Qoph", 0x05E8: "Resh",
    0x05E9: "Sin", 0x05EA: "Taw",
}


def decode_acrostic(raw: str) -> dict:
    letter = html.unescape(raw).strip()
    name = ACROSTIC_NAMES.get(ord(letter[0])) if letter else None
    return {"letter": letter, "name": name} if name else {"letter": letter}

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "sources" / "bsb" / "download" / "bsb_tables.xlsx"
OUT = ROOT / "data" / "structure_bsb"

# BSB English book name -> our reader/output slug.
NAME_TO_SLUG = {
    "Genesis": "genesis", "Exodus": "exodus", "Leviticus": "leviticus",
    "Numbers": "numbers", "Deuteronomy": "deuteronomy", "Joshua": "joshua",
    "Judges": "judges", "Ruth": "ruth", "1 Samuel": "1samuel",
    "2 Samuel": "2samuel", "1 Kings": "1kings", "2 Kings": "2kings",
    "1 Chronicles": "1chronicles", "2 Chronicles": "2chronicles",
    "Ezra": "ezra", "Nehemiah": "nehemiah", "Esther": "esther", "Job": "job",
    "Psalm": "psalms", "Psalms": "psalms", "Proverbs": "proverbs",
    "Ecclesiastes": "ecclesiastes",
    "Song of Solomon": "songofsongs", "Song of Songs": "songofsongs",
    "Isaiah": "isaiah", "Jeremiah": "jeremiah", "Lamentations": "lamentations",
    "Ezekiel": "ezekiel", "Daniel": "daniel", "Hosea": "hosea", "Joel": "joel",
    "Amos": "amos", "Obadiah": "obadiah", "Jonah": "jonah", "Micah": "micah",
    "Nahum": "nahum", "Habakkuk": "habakkuk", "Zephaniah": "zephaniah",
    "Haggai": "haggai", "Zechariah": "zechariah", "Malachi": "malachi",
    "Matthew": "matthew", "Mark": "mark", "Luke": "luke", "John": "john",
    "Acts": "acts", "Romans": "romans", "1 Corinthians": "1corinthians",
    "2 Corinthians": "2corinthians", "Galatians": "galatians",
    "Ephesians": "ephesians", "Philippians": "philippians",
    "Colossians": "colossians", "1 Thessalonians": "1thessalonians",
    "2 Thessalonians": "2thessalonians", "1 Timothy": "1timothy",
    "2 Timothy": "2timothy", "Titus": "titus", "Philemon": "philemon",
    "Hebrews": "hebrews", "James": "james", "1 Peter": "1peter",
    "2 Peter": "2peter", "1 John": "1john", "2 John": "2john",
    "3 John": "3john", "Jude": "jude", "Revelation": "revelation",
}

VERSE_RE = re.compile(r"^(.*?) (\d+):(\d+)$")
CLASS_RE = re.compile(r"<p class=\|([^|]+)\|>([^<]*)")

# paraFmt class -> block type at a verse's opening line.
POETRY1 = {"indent1", "indent1stline", "indent1stlinered", "indentred1", "tab1",
           "tab1stline", "tab1stlinered"}
POETRY2 = {"indent2", "indentred2"}
LIST1 = {"list1", "list1stline"}
LIST2 = {"list2"}


def block_for(cls: str) -> str | None:
    if cls == "reg":
        return "p"
    if cls in POETRY1:
        return "q1"
    if cls in POETRY2:
        return "q2"
    if cls in LIST1:
        return "li1"
    if cls in LIST2:
        return "li2"
    if cls == "inscrip":
        return "inscription"
    return None


def main() -> int:
    wb = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)
    ws = wb["biblosinterlinear96"]
    rows = ws.iter_rows(values_only=True)
    next(rows)  # header

    books: dict[str, dict] = {}
    cur_slug: str | None = None
    cur_ref: tuple[int, int] | None = None
    seen_para_this_verse = False
    unmapped: Counter = Counter()
    counts: Counter = Counter()

    for r in rows:
        ref = r[12]
        heading_fmt = r[13]
        para_fmt = r[15]

        if ref:
            m = VERSE_RE.match(str(ref).strip())
            if not m:
                continue
            name, ch, vs = m.group(1), int(m.group(2)), int(m.group(3))
            slug = NAME_TO_SLUG.get(name)
            if not slug:
                unmapped[name] += 1
                cur_slug = None
                continue
            cur_slug = slug
            cur_ref = (ch, vs)
            seen_para_this_verse = False
            books.setdefault(slug, {"book": slug, "en": name if name != "Psalm" else "Psalms",
                                    "source": "Berean Standard Bible (CC0)", "structure": []})

        if cur_slug is None or cur_ref is None:
            continue

        ch, vs = cur_ref
        struct = books[cur_slug]["structure"]

        def event() -> dict:
            if struct and struct[-1]["c"] == ch and struct[-1]["v"] == vs:
                return struct[-1]
            e = {"c": ch, "v": vs}
            struct.append(e)
            return e

        # headings (a verse may carry several: suphdg book-divider + pshdg, or hdg + subhdg)
        if heading_fmt:
            for cls, txt in CLASS_RE.findall(str(heading_fmt)):
                txt = html.unescape(txt.strip())
                counts[cls] += 1
                if cls in ("hdg", "ihdg"):
                    event().setdefault("heading", []).append(
                        {"level": 2, "en": txt, **({"italic": True} if cls == "ihdg" else {})})
                elif cls == "subhdg":
                    event().setdefault("heading", []).append({"level": 3, "en": txt})
                elif cls == "pshdg":
                    event().setdefault("heading", []).append({"level": 2, "en": txt, "psalm": True})
                elif cls == "suphdg":
                    event()["book_divider"] = txt  # e.g. "I" (Book One of Psalms)
                elif cls == "acrostic":
                    event().setdefault("acrostic", []).append(decode_acrostic(txt))

        # paragraph / poetry — the class of the verse's FIRST line-start marker
        if para_fmt:
            classes = CLASS_RE.findall(str(para_fmt))
            for cls, _ in classes:
                counts["para:" + cls] += 1
                if cls == "selah":
                    event()["selah"] = True
                    continue
                b = block_for(cls)
                if b and not seen_para_this_verse:
                    event()["start"] = b
                    seen_para_this_verse = True

    OUT.mkdir(parents=True, exist_ok=True)
    total_headings = 0
    for slug, data in books.items():
        # prune empty events (defensive) and count
        data["structure"] = [e for e in data["structure"]
                             if any(k in e for k in ("heading", "start", "selah", "acrostic", "book_divider"))]
        total_headings += sum(len(e.get("heading", [])) for e in data["structure"])
        (OUT / f"{slug}.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"books: {len(books)}  headings: {total_headings}")
    print("heading classes:", {k: v for k, v in counts.items() if not k.startswith("para:")})
    if unmapped:
        print("UNMAPPED book names:", dict(unmapped), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
