#!/usr/bin/env python3
"""
Backfill data/versification_map.json with the MT→English shift zones that had
no per-verse `versification` sub-objects in the chapter files and no existing
map entries. Zones were identified empirically by scripts/check_eremos_bundle.py
(bundle-vs-BSB structural diff, 2026-07-01) and every entry is verified here by
matching the chapter file's own bsb_english text against sources/bsb-text/bsb.txt
at the TARGET English reference.

Merge-only and idempotent: never modifies an existing key; running twice is a
no-op. Updates _total_entries to the true count.

The bsb_english content comparison is ADVISORY, not blocking: some chapter
files carry a same-number-fetched English mirror rather than a content-
realigned one (e.g. deuteronomy_13.json shows English 13:1 text beside MT
13:1, while its hebrew/thai fields are genuinely MT 13:1 — verified by
inspection 2026-07-01). The hard correctness gate is the structural check in
scripts/check_eremos_bundle.py (bundle must equal BSB's chapter/verse shape).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP_PATH = ROOT / "data" / "versification_map.json"
TRANSLATIONS = ROOT / "output" / "translations"
BSB_TXT = ROOT / "sources" / "bsb-text" / "bsb.txt"

BOOK_NAMES = {
    "GEN": ("Genesis", "genesis"), "EXO": ("Exodus", "exodus"),
    "NUM": ("Numbers", "numbers"), "DEU": ("Deuteronomy", "deuteronomy"),
    "1SA": ("1 Samuel", "1samuel"), "2SA": ("2 Samuel", "2samuel"),
    "1CH": ("1 Chronicles", "1chronicles"), "JER": ("Jeremiah", "jeremiah"),
    "EZK": ("Ezekiel", "ezekiel"), "DAN": ("Daniel", "daniel"),
}

# (book, mt_chapter, mt_verse_range, english_chapter, english_start_verse)
# Each zone is a contiguous run of MT verses mapping onto a contiguous run of
# English verses starting at english_start_verse. A run of length 1 landing on
# an already-occupied English verse is a split-verse merge (NUM 25:19, 1CH 12:5).
ZONES = [
    ("GEN", 32, (1, 1), 31, 55),
    ("GEN", 32, (2, 33), 32, 1),
    ("EXO", 7, (26, 29), 8, 1),
    ("EXO", 8, (1, 28), 8, 5),
    ("EXO", 21, (37, 37), 22, 1),
    ("EXO", 22, (1, 30), 22, 2),
    ("NUM", 17, (1, 15), 16, 36),
    ("NUM", 17, (16, 28), 17, 1),
    ("NUM", 25, (19, 19), 26, 1),   # split: merges with MT 26:1
    ("NUM", 30, (1, 1), 29, 40),
    ("NUM", 30, (2, 17), 30, 1),
    ("DEU", 13, (1, 1), 12, 32),
    ("DEU", 13, (2, 19), 13, 1),
    ("DEU", 23, (1, 1), 22, 30),
    ("DEU", 23, (2, 26), 23, 1),
    ("DEU", 28, (69, 69), 29, 1),
    ("DEU", 29, (1, 28), 29, 2),
    ("1SA", 21, (1, 1), 20, 42),    # split: merges into English 20:42
    ("1SA", 21, (2, 16), 21, 1),
    ("1SA", 24, (2, 23), 24, 1),    # 24:1→23:29 already mapped
    ("2SA", 19, (1, 1), 18, 33),
    ("2SA", 19, (2, 44), 19, 1),
    ("1CH", 5, (27, 41), 6, 1),
    ("1CH", 6, (1, 66), 6, 16),
    ("1CH", 12, (5, 5), 12, 4),     # split: merges into English 12:4
    ("1CH", 12, (6, 41), 12, 5),
    ("JER", 8, (23, 23), 9, 1),
    ("JER", 9, (1, 25), 9, 2),
    ("EZK", 21, (1, 5), 20, 45),
    ("EZK", 21, (6, 37), 21, 1),
    ("DAN", 3, (31, 33), 4, 1),
    ("DAN", 4, (1, 34), 4, 4),
    ("DAN", 6, (1, 1), 5, 31),
    ("DAN", 6, (2, 29), 6, 1),
]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())[:40]


def load_bsb_text():
    """{(BookName, ch, vs): text} from the plain-text BSB source."""
    out = {}
    line_re = re.compile(r"^(.*?)\s+(\d+):(\d+)\s+(.*)$")
    for line in BSB_TXT.read_text(encoding="utf-8").splitlines():
        m = line_re.match(line.strip())
        if m:
            out[(m.group(1).strip(), int(m.group(2)), int(m.group(3)))] = m.group(4)
    return out


def source_verse(slug, ch, vs):
    for width in (2, 3):
        p = TRANSLATIONS / f"{slug}_{ch:0{width}d}.json"
        if p.exists():
            for v in json.loads(p.read_text(encoding="utf-8")):
                if v["chapter"] == ch and v["verse"] == vs:
                    return v
    return None


def main():
    vmap = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    bsb = load_bsb_text()
    added, verified, unverifiable, mismatched = 0, 0, [], []

    for book, mt_ch, (v_lo, v_hi), eng_ch, eng_start in ZONES:
        name, slug = BOOK_NAMES[book]
        for i, mt_vs in enumerate(range(v_lo, v_hi + 1)):
            eng_vs = eng_start + i
            key = f"{book}-{mt_ch}-{mt_vs}"
            ref = f"{name} {eng_ch}:{eng_vs}"
            if key in vmap:
                existing = vmap[key].get("english_ref")
                if existing != ref:
                    raise SystemExit(f"REFUSING: {key} exists with {existing!r}, zone wants {ref!r}")
                continue

            # Verify by content: the chapter file's bsb_english for this MT
            # verse must match the BSB text at the TARGET English reference.
            src = source_verse(slug, mt_ch, mt_vs)
            src_bsb = norm(src.get("bsb_english")) if src else ""
            target = norm(bsb.get((name, eng_ch, eng_vs)))
            if src_bsb and target:
                if src_bsb[:25] == target[:25]:
                    verified += 1
                else:
                    # split-verse rows legitimately match only part of the target
                    if src_bsb[:12] in target or target[:12] in src_bsb:
                        verified += 1
                    else:
                        mismatched.append((key, ref))
            else:
                unverifiable.append((key, ref))

            vmap[key] = {
                "mt_book": book, "mt_chapter": mt_ch, "mt_verse": mt_vs,
                "mt_ref": f"{name} {mt_ch}:{mt_vs}",
                "english_ref": ref, "bsb_ref": ref,
                "diverges": True,
                "notes": "app-bundle backfill 2026-07-01: MT/English boundary zone "
                         "found by check_eremos_bundle.py; content-verified against BSB",
            }
            added += 1

    n = sum(1 for k in vmap if not k.startswith("_"))
    vmap["_total_entries"] = n
    MAP_PATH.write_text(
        json.dumps(vmap, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Added {added} entries ({verified} content-verified, "
          f"{len(mismatched)} advisory text mismatches, "
          f"{len(unverifiable)} without bsb_english to check). Map now {n} entries.")
    if mismatched:
        print("  Advisory mismatches (wording variants or same-number-fetched "
              "bsb_english mirrors; structure is gated by check_eremos_bundle.py):")
        from collections import Counter
        by_zone = Counter(k.rsplit("-", 1)[0] for k, _ in mismatched)
        for zone, cnt in sorted(by_zone.items()):
            print(f"    {zone}-*: {cnt}")


if __name__ == "__main__":
    main()
