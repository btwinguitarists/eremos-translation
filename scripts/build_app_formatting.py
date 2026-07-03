#!/usr/bin/env python3
"""Generate the app's EREMOS section-formatting from the repo's structure layer.

The repo is the single source of truth for the Eremos translation's section
headings + paragraph/poetry structure. The SITE already renders `data/structure`
directly; this script emits the SAME data in the shape the app reads, so the app
and site always agree (no separate heading table in the app).

Source (repo only):
  - data/structure/<slug>.json   — block starts (p/q1/q2), Thai headings
  - output/reader/<slug>.md       — the BSB-numbered verse list (authoritative
                                    order + which verses exist), so poetry/prose
                                    STYLE can be propagated to continuation
                                    verses that carry no structure event.

Output: <APP_FORMATTING_OUT>/<CODE>.json  (default:
  ~/EremosVercel2/client/public/data/formatting/), keyed "CH:VS" → {s?,h?,p?}
    s = poetry style q1/q2 (absent = default prose 'p')
    h = Thai section heading (from the repo — องค์พระผู้เป็นเจ้า, matches text)
    p = paragraph / block start (prose paragraph break; harmless on poetry)
BibleDataService loads <CODE>.json once per book, caches, applies per chapter.
"""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRUCTURE = ROOT / "data" / "structure"
READER = ROOT / "output" / "reader"
OUT = Path(os.environ.get(
    "APP_FORMATTING_OUT",
    str(Path.home() / "EremosVercel2" / "client" / "public" / "data" / "formatting"),
))

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS as NT_BOOKS            # {code: (name, slug)}
from extract_book_hebrew import BOOKS as OT_BOOKS     # {code: (name, slug, prefix)}
_OT = {code: (name, slug) for code, (name, slug, _p) in OT_BOOKS.items()}
ALL_BOOKS = {**_OT, **NT_BOOKS}
SLUG_TO_CODE = {slug: code for code, (_name, slug) in ALL_BOOKS.items()}

CHAPTER_RE = re.compile(r"^## บทที่ (\d+)\s*$")
VERSE_RE = re.compile(r"^\*\*(\d+)(?:-\d+)?\*\*")


def reader_verses(slug):
    """[(chapter, verse), …] in reader order (skips superscription italics)."""
    path = READER / f"{slug}.md"
    out, ch = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = CHAPTER_RE.match(line)
        if m:
            ch = int(m.group(1))
            continue
        m = VERSE_RE.match(line)
        if m and ch is not None:
            out.append((ch, int(m.group(1))))
    return out


def build_book(slug):
    events = {}
    for e in json.loads((STRUCTURE / f"{slug}.json").read_text(encoding="utf-8"))["structure"]:
        events[(e["c"], e["v"])] = e
    verses = reader_verses(slug)

    out = {}
    cur_style = "p"
    cur_ch = None
    for ch, v in verses:
        if ch != cur_ch:
            cur_ch, cur_style = ch, "p"   # each chapter starts prose until a marker
        ev = events.get((ch, v))
        entry = {}
        if ev and ev.get("start"):
            cur_style = ev["start"]        # p / q1 / q2 — begins a block
            entry["p"] = True              # paragraph/block start (ignored on poetry)
        if cur_style.startswith("q"):
            entry["s"] = cur_style         # propagate poetry style to continuation verses
        if ev and ev.get("heading"):
            entry["h"] = " · ".join(h["th"] for h in ev["heading"] if h.get("th"))
        if entry:
            out[f"{ch}:{v}"] = entry
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    books = skipped = total = headings = 0
    for path in sorted(STRUCTURE.glob("*.json")):
        slug = path.stem
        code = SLUG_TO_CODE.get(slug)
        if not code:
            print(f"  skip (no code for slug): {slug}")
            skipped += 1
            continue
        data = build_book(slug)
        (OUT / f"{code}.json").write_text(
            json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        books += 1
        total += len(data)
        headings += sum(1 for e in data.values() if "h" in e)
    print(f"Wrote {books} books ({skipped} skipped) → {OUT}")
    print(f"  {total} formatted verses, {headings} with headings")


if __name__ == "__main__":
    main()
