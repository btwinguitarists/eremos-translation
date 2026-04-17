#!/usr/bin/env python3
"""
Render a per-book reader-friendly Markdown document of the Eremos Translation.

Output: output/reader/<slug>.md — committed to the public repo so anyone can
read the entire book in their browser on github.com without cloning anything.

Content matches what the Eremos app shows by default in its verse popup:
  - Thai translation (the main reading text)
  - thai_summary as inline italic context (when a verse has one)
  - NO Greek, NO BSB English, NO scholarly translator notes
    (Those already live in docs/<slug>_NN_review.md and the verse popup
    for anyone who wants the deep audit-trail view.)

Each book file ends with a SHA-256 footer so a reader can verify they have
the canonical version (matches the per-chapter SHAs recorded in HASHES.md).

Usage:
  python3 scripts/render_reader.py              # render every book that has translated chapters
  python3 scripts/render_reader.py --book MRK   # render one book
  python3 scripts/render_reader.py --book mark  # same, slug form

Designed to be safe to re-run: writes only to output/reader/, never touches
translation source. Wired into ship_chapter.sh so the reader doc regenerates
on every chapter ship.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
READER_DIR = ROOT / "output" / "reader"

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS  # noqa: E402

# Thai book titles. For each book, the on-page heading shown to readers.
# Canonical Thai Christian conventions: พระกิตติคุณ for the four Gospels,
# กิจการของอัครทูต for Acts, individual book names otherwise.
THAI_BOOK_TITLES = {
    "MAT": "พระกิตติคุณตามมัทธิว",
    "MRK": "พระกิตติคุณตามมาระโก",
    "LUK": "พระกิตติคุณตามลูกา",
    "JHN": "พระกิตติคุณตามยอห์น",
    "ACT": "กิจการของอัครทูต",
    "ROM": "โรม",
    "1CO": "1 โครินธ์", "2CO": "2 โครินธ์",
    "GAL": "กาลาเทีย", "EPH": "เอเฟซัส", "PHP": "ฟีลิปปี", "COL": "โคโลสี",
    "1TH": "1 เธสะโลนิกา", "2TH": "2 เธสะโลนิกา",
    "1TI": "1 ทิโมธี", "2TI": "2 ทิโมธี", "TIT": "ทิตัส", "PHM": "ฟีเลโมน",
    "HEB": "ฮีบรู", "JAS": "ยากอบ",
    "1PE": "1 เปโตร", "2PE": "2 เปโตร",
    "1JN": "1 ยอห์น", "2JN": "2 ยอห์น", "3JN": "3 ยอห์น",
    "JUD": "ยูดา", "REV": "วิวรณ์",
}

SLUG_TO_CODE = {slug: code for code, (_, slug) in BOOKS.items()}


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def chapter_files_for(slug: str) -> list[Path]:
    """All translated chapter files for a book, sorted by chapter number.
    Strict pattern match excludes demo / fragment files like mark_01_01_demo.json."""
    pattern = re.compile(rf"^{re.escape(slug)}_(\d+)\.json$")
    matched = [
        (int(m.group(1)), p)
        for p in TRANSLATIONS.glob(f"{slug}_*.json")
        if (m := pattern.match(p.name))
    ]
    return [p for _, p in sorted(matched)]


def render_chapter(verses: list[dict], chapter_num: int) -> str:
    lines = [f"## บทที่ {chapter_num}", ""]
    for v in verses:
        n = v["verse"]
        thai = (v.get("translation") or {}).get("thai", "").strip()
        summary = (v.get("translation") or {}).get("thai_summary")
        # Bold verse number followed by the verse text on the same paragraph.
        # Use Thai numerals? Thai Bibles use Arabic numerals conventionally; keep Arabic.
        lines.append(f"**{n}** {thai}")
        if summary and summary.strip():
            lines.append("")
            # GitHub renders blockquote + italic cleanly. The "บริบท:" label
            # mirrors the in-app popup's "บริบท · Context" header.
            lines.append(f"> _บริบท: {summary.strip()}_")
        lines.append("")
    return "\n".join(lines)


def render_book(book_code: str) -> Path | None:
    if book_code not in BOOKS:
        print(f"  unknown book code: {book_code}", file=sys.stderr)
        return None
    title_en, slug = BOOKS[book_code]
    title_thai = THAI_BOOK_TITLES.get(book_code, title_en)

    chapters = chapter_files_for(slug)
    if not chapters:
        print(f"  {book_code}: no translated chapters yet — skipping")
        return None

    chapter_count = len(chapters)
    parts = [
        f"# {title_thai}",
        "",
        f"_The Gospel of {title_en} — {chapter_count} chapter{'s' if chapter_count != 1 else ''}, "
        f"translated from the SBLGNT Greek text into Thai by the Eremos Translation project._",
        "",
        "_This reader edition shows only the Thai translation and the contextual "
        "summary (บริบท) where one is provided. For the underlying Greek, English "
        "(BSB) reference, and translator decisions per verse, see the per-chapter "
        f"review documents at `docs/{slug}_NN_review.md` or the source JSON at "
        f"`output/translations/`._",
        "",
        "---",
        "",
    ]

    chapter_hashes: list[tuple[str, str]] = []
    for chapter_path in chapters:
        chapter_num = int(re.search(r"_(\d+)\.json$", chapter_path.name).group(1))
        verses = json.loads(chapter_path.read_text(encoding="utf-8"))
        parts.append(render_chapter(verses, chapter_num))
        parts.append("---")
        parts.append("")
        chapter_hashes.append((chapter_path.name, file_sha256(chapter_path)))

    parts.append("## Verification")
    parts.append("")
    parts.append(
        "Each chapter's source JSON has a SHA-256 fingerprint. Anyone can recompute "
        "and verify against the manifest at `HASHES.md` to confirm they have the "
        "canonical Eremos Translation of that chapter."
    )
    parts.append("")
    parts.append("| Chapter file | SHA-256 |")
    parts.append("|---|---|")
    for name, sha in chapter_hashes:
        parts.append(f"| `output/translations/{name}` | `{sha}` |")
    parts.append("")

    READER_DIR.mkdir(parents=True, exist_ok=True)
    out_path = READER_DIR / f"{slug}.md"
    out_path.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", help="Book code (MRK) or slug (mark). If omitted, render all books that have translated chapters.")
    args = parser.parse_args()

    if args.book:
        code = args.book.upper()
        if code not in BOOKS:
            code = SLUG_TO_CODE.get(args.book.lower())
        if not code:
            print(f"Unknown book: {args.book}", file=sys.stderr)
            return 1
        out = render_book(code)
        if out:
            print(f"Wrote {out}")
        return 0

    # Render every book that has translated chapters.
    rendered = 0
    for code, (_, slug) in BOOKS.items():
        if any(TRANSLATIONS.glob(f"{slug}_*.json")):
            out = render_book(code)
            if out:
                print(f"Wrote {out}")
                rendered += 1
    print(f"\nRendered {rendered} book(s) to {READER_DIR}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
