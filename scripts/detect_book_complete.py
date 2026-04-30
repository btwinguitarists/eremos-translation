#!/usr/bin/env python3
"""
End-of-book detection for ship_chapter.sh.

Reads data/production_order.json. If the just-shipped chapter is the LAST
chapter for its book:
  - prints a loud BOOK COMPLETE banner
  - writes output/.book_complete_signal with book code + timestamp
  - exits 1 so the calling shell halts (and any /loop wrapper detects failure)

The chapter has already been fully shipped (PR merged, TestFlight uploaded)
by the time this runs at the END of ship_chapter.sh — exit 1 only signals
"don't continue to next chapter; run end-of-book audit first."

Usage:
    python3 scripts/detect_book_complete.py <BOOK_CODE> <CHAPTER>

Exit codes:
    0 — not the last chapter; loop can continue
    1 — BOOK COMPLETE; loop must halt for end-of-book audit
    2 — invalid arguments
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BOOK_NAMES = {
    "MAT": "Matthew", "MRK": "Mark", "LUK": "Luke", "JHN": "John",
    "ACT": "Acts", "ROM": "Romans", "1CO": "1 Corinthians", "2CO": "2 Corinthians",
    "GAL": "Galatians", "EPH": "Ephesians", "PHP": "Philippians", "COL": "Colossians",
    "1TH": "1 Thessalonians", "2TH": "2 Thessalonians", "1TI": "1 Timothy",
    "2TI": "2 Timothy", "TIT": "Titus", "PHM": "Philemon", "HEB": "Hebrews",
    "JAS": "James", "1PE": "1 Peter", "2PE": "2 Peter", "1JN": "1 John",
    "2JN": "2 John", "3JN": "3 John", "JUD": "Jude", "REV": "Revelation",
}


def main() -> None:
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <BOOK_CODE> <CHAPTER>", file=sys.stderr)
        sys.exit(2)
    book = sys.argv[1].upper()
    try:
        chapter = int(sys.argv[2])
    except ValueError:
        print(f"chapter must be integer, got: {sys.argv[2]}", file=sys.stderr)
        sys.exit(2)

    order_path = ROOT / "data" / "production_order.json"
    if not order_path.exists():
        print(f"[detect_book_complete] {order_path} missing — skipping check", file=sys.stderr)
        sys.exit(0)

    order = json.loads(order_path.read_text())
    chapters_in_book = [e["chapter"] for e in order["order"] if e["book"] == book]
    if not chapters_in_book:
        print(f"[detect_book_complete] {book} not in production_order.json — skipping check", file=sys.stderr)
        sys.exit(0)

    max_chapter = max(chapters_in_book)
    if chapter < max_chapter:
        # not last — loop continues
        sys.exit(0)

    # BOOK COMPLETE
    book_name = BOOK_NAMES.get(book, book)
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

    signal_path = ROOT / "output" / ".book_complete_signal"
    signal_path.write_text(
        f"book={book}\nname={book_name}\nchapter={chapter}\ntotal={max_chapter}\nts={timestamp}\n"
    )

    bar = "=" * 72
    print()
    print(bar)
    print(f"    \U0001f4d6  BOOK COMPLETE  —  {book_name} ({book})  —  all {max_chapter} chapters shipped")
    print(bar)
    print("  /loop is HALTING before next chapter draft.")
    print()
    print("  Per docs/END_OF_BOOK_CHECKLIST.md, run end-of-book editorial review")
    print("  before continuing to the next book:")
    print()
    print("    §1  Mechanical    — check_key_term_consistency + check_phrase_consistency")
    print("    §2  Editorial     — fresh Claude session with end-of-book review prompt")
    print("                      (writes docs/end_of_book/<book>/<BOOK>_END_OF_BOOK_REVIEW_*.md)")
    print("    §3  External AI   — paste packet into Grok + 1 of (ChatGPT / Gemini / Claude)")
    print("    §4  Reviewer      — Thai + theological reviewers (optional)")
    print(f"    §5  Lock the book — git tag book-{book_name.lower().replace(' ', '')}-v1")
    print()
    print(f"  Marker written: {signal_path.relative_to(ROOT)}")
    print(f"  Resume with `/loop eremos translation: next` after audit + decisions.")
    print(bar)
    sys.exit(1)


if __name__ == "__main__":
    main()
