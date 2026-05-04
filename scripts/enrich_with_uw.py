#!/usr/bin/env python3
"""
Enrich a chapter with unfoldingWord Translation Notes (CC-BY-SA).

Reads sources/en_tn/tn_<BOOK>.tsv, filters to the target chapter, groups by
verse, and writes a markdown file at
  output/uw_notes/<slug>_<NN>.md

Claude reads this file alongside the extracted verse JSON during translation
to get scholarly context — interpretive cruxes, known issues, "how most
translations handle this" signals. Our translation still originates from
Greek + MACULA morphology; uW TN is *reference only*, never a source to copy.

Per RULES.md §2 and §10, copying uW TN text verbatim into our output would
make our output CC-BY-SA (inheriting their license). We paraphrase if we
use it at all — and typically we don't need to, since we're doing our own
exegesis.

Usage:
  python3 scripts/enrich_with_uw.py --book 1TI --chapter 3
  python3 scripts/enrich_with_uw.py --book MRK --chapter 2
"""
import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UW_TN_DIR = ROOT / "sources" / "en_tn"
OUTPUT = ROOT / "output" / "uw_notes"

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS as NT_BOOKS  # NT: {code: (name, slug)}

# Merge OT BOOKS so loop kickoff works for OT chapters (Ruth, Jonah, Genesis...).
# extract_book_hebrew.BOOKS is a 3-tuple (name, slug, file_prefix).
try:
    from extract_book_hebrew import BOOKS as _OT_BOOKS_3TUPLE
    BOOKS = dict(NT_BOOKS)
    for _code, _entry in _OT_BOOKS_3TUPLE.items():
        if len(_entry) >= 2:
            BOOKS[_code] = (_entry[0], _entry[1])
except ImportError:
    BOOKS = NT_BOOKS


def load_tn(book_code: str, chapter: int) -> tuple[list[dict], dict, dict]:
    """Return (per-verse notes, chapter-level intro note, book-level front intro).
       Each entry: {'verse': int | 'intro' | 'front', 'id': str, 'quote': str,
                    'note': str, 'support': str}
    """
    tsv_path = UW_TN_DIR / f"tn_{book_code}.tsv"
    if not tsv_path.exists():
        return [], {}, {}

    notes = []
    intro = {}
    front = {}
    with open(tsv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            ref = (row.get("Reference") or "").strip()
            if not ref:
                continue
            # Formats: "3:1", "3:intro", "3:16", "front:intro"
            if ":" not in ref:
                continue
            ch_part, v_part = ref.split(":", 1)

            entry = {
                "verse": v_part,
                "id": (row.get("ID") or "").strip(),
                "quote": (row.get("Quote") or "").strip(),
                "note": (row.get("Note") or "").strip().replace("\\n", "\n"),
                "support": (row.get("SupportReference") or "").strip(),
            }

            if ch_part == "front":
                front = entry
                continue

            try:
                row_chapter = int(ch_part)
            except ValueError:
                continue
            if row_chapter != chapter:
                continue

            if v_part == "intro":
                intro = entry
            else:
                notes.append(entry)
    return notes, intro, front


def render_markdown(book_name: str, book_code: str, chapter: int,
                    notes: list[dict], intro: dict) -> str:
    lines = [
        f"# unfoldingWord Translation Notes — {book_name} {chapter}",
        "",
        "_Source: unfoldingWord® Translation Notes, CC-BY-SA 4.0 (github.com/unfoldingWord/en_tn)._",
        "_**Reference only.** Do NOT copy text into our translation — would inherit CC-BY-SA._",
        "_Use for scholarly context: interpretive cruxes, textual issues, translation difficulties._",
        "",
        "---",
        "",
    ]

    if intro:
        lines.append(f"## Chapter intro")
        lines.append("")
        lines.append(intro["note"])
        lines.append("")
        lines.append("---")
        lines.append("")

    by_verse: dict[str, list] = {}
    for n in notes:
        by_verse.setdefault(n["verse"], []).append(n)

    def verse_sort_key(v: str):
        try:
            return (0, int(v))
        except ValueError:
            return (1, v)

    for verse in sorted(by_verse.keys(), key=verse_sort_key):
        lines.append(f"## {book_name} {chapter}:{verse}")
        lines.append("")
        for n in by_verse[verse]:
            if n["quote"]:
                lines.append(f"**Quote:** {n['quote']}")
            if n["support"]:
                lines.append(f"**Support:** {n['support']}")
            if n["note"]:
                lines.append(n["note"])
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True, help="3-letter book code (e.g., MRK, 1TI)")
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()

    code = args.book.upper()
    if code not in BOOKS:
        print(f"Unknown book code: {code}")
        return 1
    book_name, slug = BOOKS[code]

    notes, intro, front = load_tn(code, args.chapter)
    if not notes and not intro and not front:
        print(f"No uW Translation Notes found for {book_name} {args.chapter}.")
        print(f"(Check that sources/en_tn/tn_{code}.tsv exists and contains the chapter.)")
        return 0

    md = render_markdown(book_name, code, args.chapter, notes, intro)

    if args.stdout:
        print(md)
    else:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        out_path = OUTPUT / f"{slug}_{args.chapter:02d}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}")
        print(f"  {len(notes)} verse-level notes + {'intro' if intro else 'no intro'}")

        # Always (re)write the book-level front intro file. This is what
        # translators read FIRST before starting any chapter — author, audience,
        # outline, themes, translation issues. SIL/Wycliffe pro practice.
        if front:
            front_path = OUTPUT / f"{slug}_FRONT.md"
            front_lines = [
                f"# unfoldingWord Book Introduction — {book_name}",
                "",
                "_Source: unfoldingWord® Translation Notes, CC-BY-SA 4.0 (github.com/unfoldingWord/en_tn)._",
                "_**Reference only.** Read BEFORE starting any chapter of this book to ground exegesis in author/audience/themes/structure/translation-issues._",
                "",
                "---",
                "",
                front["note"],
            ]
            front_path.write_text("\n".join(front_lines), encoding="utf-8")
            print(f"  Book intro: {front_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
