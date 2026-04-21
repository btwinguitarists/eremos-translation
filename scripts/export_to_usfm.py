#!/usr/bin/env python3
"""
Export Eremos Translation output to USFM (Unified Standard Format Markers).

USFM is the interchange format used by Paratext, Scripture Forge, and the
Digital Bible Library. This script converts our per-chapter JSON translations
into per-book .SFM files that Paratext can import directly.

What's exported:
  - Main Thai translation text (one `\\v N` per verse)
  - Paragraph markers at chapter boundaries (minimal — no internal paragraphing
    because our JSON schema doesn't encode paragraph breaks)
  - Thai book metadata (title, running header, TOC entries)
  - Chapter-footer remarks for Tier 2 whole-verse textual variants
    (e.g., Matthew 17:21, 18:11, 23:14 — verses SBLGNT omits that TR/Byz
    includes). Sourced from `output/textual_variants/<slug>_<NN>.json`.

What's NOT exported:
  - `key_decisions` — these are translator's scholarly apparatus, not reader
    text; they live in the JSON for GitHub audit trail and stay out of USFM
  - `notes` — same reason
  - `thai_summary` — app-side reader popup content, not Bible text
  - `thai_literal` — alternative rendering, not part of the published text
  - `bsb_english` — reference-only, not our output

What a reviewer sees in Paratext after import:
  Clean verse-by-verse Thai text with textual-variant footers. The scholarly
  apparatus stays in the thai-bible-ai repo where translators and external
  AI reviewers can see it.

Usage:
  python3 scripts/export_to_usfm.py --book LUK
  python3 scripts/export_to_usfm.py --all
  python3 scripts/export_to_usfm.py --book MAT --output-dir /tmp/export

Output:
  output/paratext/<BOOKCODE>.SFM   (e.g., LUK.SFM, MAT.SFM)

Import into Paratext:
  1. Paratext → File → Import USFM
  2. Point at output/paratext/
  3. Select books to import
  4. Paratext creates or updates the project's book files
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
TEXTUAL_VARIANTS = ROOT / "output" / "textual_variants"
DEFAULT_OUTPUT = ROOT / "output" / "paratext"


# (code, slug, long_thai_name, short_thai_name, abbr_thai, mt_title)
# The English Matthew/Mark/etc. names here are just fallbacks for \id comment.
BOOKS = {
    "MAT": ("matthew",         "พระวรสารตามนักบุญมัทธิว",   "มัทธิว",       "มธ",  "มัทธิว",       "Matthew"),
    "MRK": ("mark",            "พระวรสารตามนักบุญมาระโก",  "มาระโก",      "มก",  "มาระโก",      "Mark"),
    "LUK": ("luke",            "พระวรสารตามนักบุญลูกา",    "ลูกา",        "ลก",  "ลูกา",        "Luke"),
    "JHN": ("john",            "พระวรสารตามนักบุญยอห์น",   "ยอห์น",      "ยน",  "ยอห์น",      "John"),
    "ACT": ("acts",            "กิจการของอัครทูต",          "กิจการ",     "กจ",  "กิจการ",     "Acts"),
    "ROM": ("romans",          "จดหมายถึงชาวโรม",          "โรม",        "รม",  "โรม",        "Romans"),
    "1CO": ("1corinthians",    "จดหมายฉบับที่หนึ่งถึงชาวโครินธ์", "1 โครินธ์",  "1คร", "1 โครินธ์",  "1 Corinthians"),
    "2CO": ("2corinthians",    "จดหมายฉบับที่สองถึงชาวโครินธ์",   "2 โครินธ์",  "2คร", "2 โครินธ์",  "2 Corinthians"),
    "GAL": ("galatians",       "จดหมายถึงชาวกาลาเทีย",      "กาลาเทีย",   "กท",  "กาลาเทีย",   "Galatians"),
    "EPH": ("ephesians",       "จดหมายถึงชาวเอเฟซัส",       "เอเฟซัส",    "อฟ",  "เอเฟซัส",    "Ephesians"),
    "PHP": ("philippians",     "จดหมายถึงชาวฟีลิปปี",        "ฟีลิปปี",    "ฟป",  "ฟีลิปปี",    "Philippians"),
    "COL": ("colossians",      "จดหมายถึงชาวโคโลสี",        "โคโลสี",    "คส",  "โคโลสี",    "Colossians"),
    "1TH": ("1thessalonians",  "จดหมายฉบับที่หนึ่งถึงชาวเธสะโลนิกา", "1 เธสะโลนิกา", "1ธส", "1 เธสะโลนิกา", "1 Thessalonians"),
    "2TH": ("2thessalonians",  "จดหมายฉบับที่สองถึงชาวเธสะโลนิกา",   "2 เธสะโลนิกา", "2ธส", "2 เธสะโลนิกา", "2 Thessalonians"),
    "1TI": ("1timothy",        "จดหมายฉบับที่หนึ่งถึงทิโมธี",  "1 ทิโมธี",   "1ทธ", "1 ทิโมธี",   "1 Timothy"),
    "2TI": ("2timothy",        "จดหมายฉบับที่สองถึงทิโมธี",    "2 ทิโมธี",   "2ทธ", "2 ทิโมธี",   "2 Timothy"),
    "TIT": ("titus",           "จดหมายถึงทิตัส",            "ทิตัส",      "ทต",  "ทิตัส",      "Titus"),
    "PHM": ("philemon",        "จดหมายถึงฟีเลโมน",          "ฟีเลโมน",   "ฟม",  "ฟีเลโมน",   "Philemon"),
    "HEB": ("hebrews",         "จดหมายถึงชาวฮีบรู",         "ฮีบรู",      "ฮบ",  "ฮีบรู",      "Hebrews"),
    "JAS": ("james",           "จดหมายของยากอบ",          "ยากอบ",     "ยก",  "ยากอบ",     "James"),
    "1PE": ("1peter",          "จดหมายฉบับที่หนึ่งของเปโตร", "1 เปโตร",    "1ปต", "1 เปโตร",    "1 Peter"),
    "2PE": ("2peter",          "จดหมายฉบับที่สองของเปโตร",   "2 เปโตร",    "2ปต", "2 เปโตร",    "2 Peter"),
    "1JN": ("1john",           "จดหมายฉบับที่หนึ่งของยอห์น", "1 ยอห์น",    "1ยน", "1 ยอห์น",    "1 John"),
    "2JN": ("2john",           "จดหมายฉบับที่สองของยอห์น",   "2 ยอห์น",    "2ยน", "2 ยอห์น",    "2 John"),
    "3JN": ("3john",           "จดหมายฉบับที่สามของยอห์น",   "3 ยอห์น",    "3ยน", "3 ยอห์น",    "3 John"),
    "JUD": ("jude",            "จดหมายของยูดา",            "ยูดา",      "ยด",  "ยูดา",      "Jude"),
    "REV": ("revelation",      "วิวรณ์",                   "วิวรณ์",     "วว",  "วิวรณ์",     "Revelation"),
}


def emit_header(code: str) -> list[str]:
    """Emit the USFM book header (\\id, \\ide, \\h, \\toc1–3, \\mt1)."""
    _slug, long_th, short_th, abbr_th, mt, en = BOOKS[code]
    return [
        f"\\id {code} Eremos Translation — {en} (Thai CC0)",
        "\\usfm 3.0",
        "\\ide UTF-8",
        f"\\h {short_th}",
        f"\\toc1 {long_th}",
        f"\\toc2 {short_th}",
        f"\\toc3 {abbr_th}",
        f"\\mt1 {mt}",
        "",
    ]


def emit_chapter(code: str, chapter: int, slug: str) -> list[str]:
    """Emit USFM for a single chapter: \\c marker, verses, textual-variant footer."""
    path = TRANSLATIONS / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return []  # chapter not yet translated — silently skip

    verses = json.loads(path.read_text(encoding="utf-8"))

    lines = [f"\\c {chapter}", "\\p"]
    for v in verses:
        verse_num = v["verse"]
        thai = (v.get("translation", {}) or {}).get("thai", "") or ""
        # USFM verse marker: single-line per verse. Thai text is copied verbatim.
        lines.append(f"\\v {verse_num} {thai}")

    # Tier 2 textual-variant chapter-footer notes
    tv_path = TEXTUAL_VARIANTS / f"{slug}_{chapter:02d}.json"
    if tv_path.exists():
        variants = json.loads(tv_path.read_text(encoding="utf-8"))
        absent_verses = [v for v in variants if v.get("type") == "inclusion_variant_absent"]
        if absent_verses:
            lines.append("")
            lines.append("\\rem หมายเหตุด้านต้นฉบับ")
            for av in absent_verses:
                verse_num = av["verse"]
                tr_thai = av.get("tr_byz_thai", "")
                expl = av.get("explanation_thai", "")
                lines.append(
                    f"\\rem ข้อ {chapter}:{verse_num} — ต้นฉบับไบแซนไทน์/TR รวมไว้: «{tr_thai}» "
                    f"— {expl}"
                )

    lines.append("")
    return lines


def export_book(code: str, output_dir: Path) -> Path | None:
    """Export a single book's SFM file. Returns path if written, None if empty."""
    if code not in BOOKS:
        print(f"✗ Unknown book code: {code}", file=sys.stderr)
        return None

    slug = BOOKS[code][0]
    chapters_pattern = TRANSLATIONS.glob(f"{slug}_*.json")
    chapter_numbers = sorted(
        int(p.stem.rsplit("_", 1)[1]) for p in chapters_pattern
        if p.stem.rsplit("_", 1)[1].isdigit()
    )

    if not chapter_numbers:
        return None  # nothing translated for this book yet

    lines = emit_header(code)
    for chapter in chapter_numbers:
        lines.extend(emit_chapter(code, chapter, slug))

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"{code}.SFM"
    # USFM convention: Unix line endings, no trailing blank line beyond content.
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", help="Book code (MAT, MRK, LUK, …)")
    parser.add_argument("--all", action="store_true", help="Export every book with translated chapters")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT,
                        help=f"Output directory (default: {DEFAULT_OUTPUT})")
    args = parser.parse_args()

    if not args.book and not args.all:
        parser.error("Specify --book <CODE> or --all")

    codes = list(BOOKS.keys()) if args.all else [args.book.upper()]
    written = []
    for code in codes:
        path = export_book(code, args.output_dir)
        if path:
            n_chapters = sum(
                1 for p in TRANSLATIONS.glob(f"{BOOKS[code][0]}_*.json")
                if p.stem.rsplit("_", 1)[1].isdigit()
            )
            print(f"  ✓ {code}.SFM ({n_chapters} chapters) → {path}")
            written.append(path)
        else:
            if not args.all:
                print(f"  ⚠ {code}: no translated chapters found — nothing exported")

    if args.all:
        print(f"\nExported {len(written)} book(s) to {args.output_dir}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
