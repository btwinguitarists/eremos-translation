#!/usr/bin/env python3
"""
Resolve "what's the next chapter to translate?" based on:
- output/translations/ (what's already done)
- data/production_order.json (the canonical translation order)

Output formats:
  - default: "MRK 6"  (one line, machine-friendly)
  - --pretty: "Mark 6 (Phase 2 — NT narrative)"
  - --json:   {"book": "MRK", "chapter": 6, "phase": "..."}
  - --status: full progress report (% done, current phase, etc.)

Usage in trigger phrases:
  "Eremos Translation: next"           → resolves and translates the next chapter
  "Eremos Translation: next chapter"   → same
  "Eremos Translation: status"         → just shows progress without translating
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
ORDER_FILE = ROOT / "data" / "production_order.json"

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS

SLUG_TO_CODE = {slug: code for code, (_, slug) in BOOKS.items()}
FILENAME_RE = re.compile(r"^(?P<slug>[a-z0-9]+)_(?P<chapter>\d{2})\.json$")


def load_done() -> set[tuple[str, int]]:
    done: set[tuple[str, int]] = set()
    if not TRANSLATIONS.exists():
        return done
    for f in TRANSLATIONS.glob("*_*.json"):
        if "_demo" in f.name:
            continue
        m = FILENAME_RE.match(f.name)
        if not m:
            continue
        slug = m.group("slug")
        chapter = int(m.group("chapter"))
        code = SLUG_TO_CODE.get(slug)
        if code:
            done.add((code, chapter))
    return done


def load_order() -> list[dict]:
    with open(ORDER_FILE) as f:
        return json.load(f)["order"]


def find_next(done: set, order: list) -> dict | None:
    for entry in order:
        if (entry["book"], entry["chapter"]) not in done:
            return entry
    return None


def status_report(done: set, order: list) -> str:
    total = len(order)
    done_in_order = sum(1 for e in order if (e["book"], e["chapter"]) in done)
    done_total = len(done)
    pct = 100 * done_in_order / total if total else 0

    # Per-book progress
    by_book: dict[str, list[int]] = {}
    for entry in order:
        by_book.setdefault(entry["book"], []).append(entry["chapter"])

    lines = [
        f"=== Eremos Translation — production progress ===",
        f"",
        f"Total NT chapters in order:  {total}",
        f"Chapters translated:         {done_total}  ({pct:.1f}% of NT)",
        f"",
        f"Per-book progress:",
    ]
    for book, chapters in by_book.items():
        book_done = sum(1 for ch in chapters if (book, ch) in done)
        if book_done > 0 or book == "MRK":
            book_name = BOOKS[book][0]
            lines.append(f"  {book_name:20s} {book_done:3d}/{len(chapters):3d}")

    nxt = find_next(done, order)
    if nxt:
        book_name = BOOKS[nxt["book"]][0]
        lines.append("")
        lines.append(f"Next chapter:  {book_name} {nxt['chapter']}  ({nxt['phase']})")
    else:
        lines.append("")
        lines.append("All NT chapters in the production order are translated.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretty", action="store_true", help="Human-readable output")
    parser.add_argument("--json", action="store_true", help="Full JSON entry")
    parser.add_argument("--status", action="store_true", help="Full progress report")
    args = parser.parse_args()

    done = load_done()
    order = load_order()

    if args.status:
        print(status_report(done, order))
        return 0

    nxt = find_next(done, order)
    if nxt is None:
        print("DONE", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(nxt))
    elif args.pretty:
        book_name = BOOKS[nxt["book"]][0]
        print(f"{book_name} {nxt['chapter']}  ({nxt['phase']})")
    else:
        print(f"{nxt['book']} {nxt['chapter']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
