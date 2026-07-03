#!/usr/bin/env python3
"""Assemble the consumable structure layer: data/structure/<book>.json.

Merges the English BSB structure (data/structure_bsb/, from
extract_bsb_structure.py) with the Thai section-heading drafts, resolving every
anchor from BSB/English versification into the Eremos reader's numbering
(MT-anchored at 23 seams). The site, the Eremos app, and future print all read
this one layer.

Anchor resolution (in order):
  1. exact — BSB (chapter, verse) already exists in our reader verses.
  2. inverse versification_map — data/versification_map.json is MT-anchored
     (mt_ref -> bsb_ref); we invert it to map a BSB ref back to our verse.
  3. hand-verified overrides — cases the map lacks (Leviticus 5/6 boundary),
     each confirmed by verse-content match.
  4. drop — a handful of paragraph/poetry-only marks at NT/Nehemiah chapter
     seams that fall on a verse our numbering merges; dropping them is
     invisible (the verse simply continues its paragraph). Logged, never
     silent. Headings are NEVER dropped.

Additive & CC0: reads the BSB apparatus (public domain) + our reader verse
list only; never mutates output/translations. Thai headings are editorial
DRAFTS (review_status: draft) headed for native review.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BSB_DIR = ROOT / "data" / "structure_bsb"
OUT = ROOT / "data" / "structure"
READER = ROOT / "output" / "reader"
VMAP = ROOT / "data" / "versification_map.json"
TH_HEADINGS = ROOT / "data" / "structure_headings_th.json"

# BSB display name(s) per slug (for building the inverse-map key).
SLUG_TO_NAMES = {
    "psalms": ["Psalm", "Psalms"], "songofsongs": ["Song of Solomon", "Song of Songs"],
}

# Hand-verified overrides for anchors the versification_map lacks.
# (slug, bsb_chapter, bsb_verse) -> (our_chapter, our_verse); confirmed by content.
OVERRIDES = {
    ("leviticus", 6, 24): (6, 17),  # "The Sin Offering": BSB 6:24 "And the LORD said to Moses" = our 6:17
}

CH_RE = re.compile(r"^## บทที่ (\d+)")
V_RE = re.compile(r"^\*\*(\d+)(?:-\d+)?\*\*")
H1_RE = re.compile(r"^# (.+)$")


def reader_info(slug: str):
    """Return (thai_title, set_of_(c,v))."""
    p = READER / f"{slug}.md"
    verses = set()
    title = ""
    ch = None
    for line in p.read_text(encoding="utf-8").splitlines():
        if not title:
            m = H1_RE.match(line)
            if m:
                title = m.group(1).strip()
                continue
        m = CH_RE.match(line)
        if m:
            ch = int(m.group(1))
            continue
        m = V_RE.match(line)
        if m and ch:
            verses.add((ch, int(m.group(1))))
    return title, verses


def build_inverse_map() -> dict[str, tuple[int, int]]:
    m = json.loads(VMAP.read_text(encoding="utf-8"))
    inv = {}
    for v in m.values():
        if not isinstance(v, dict):
            continue
        bsb = v.get("bsb_ref")
        mtc, mtv = v.get("mt_chapter"), v.get("mt_verse")
        if bsb and mtc and mtv:
            inv[bsb] = (int(mtc), int(mtv))
    return inv


def main() -> int:
    inv = build_inverse_map()
    th = json.loads(TH_HEADINGS.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)

    tot_headings = tot_events = dropped = 0
    drop_log = []
    for bsb_file in sorted(BSB_DIR.glob("*.json")):
        d = json.loads(bsb_file.read_text(encoding="utf-8"))
        slug = d["book"]
        title, verses = reader_info(slug)
        names = SLUG_TO_NAMES.get(slug, [d["en"]])

        out_struct = []
        for e in d["structure"]:
            c, v = e["c"], e["v"]
            # resolve anchor into our numbering
            if (c, v) in verses:
                rc, rv = c, v
            elif (slug, c, v) in OVERRIDES:
                rc, rv = OVERRIDES[(slug, c, v)]
            else:
                hit = None
                for nm in names:
                    hit = inv.get(f"{nm} {c}:{v}")
                    if hit:
                        break
                if hit and hit in verses:
                    rc, rv = hit
                else:
                    # unresolved — only drop non-heading marks
                    if e.get("heading"):
                        print(f"UNRESOLVED HEADING {slug} {c}:{v} "
                              f"{[h['en'] for h in e['heading']]}", file=sys.stderr)
                        rc, rv = c, v  # keep with original ref; flagged above
                    else:
                        dropped += 1
                        drop_log.append(f"{slug} {c}:{v} {list(e.keys())}")
                        continue

            ev = {"c": rc, "v": rv}
            if e.get("heading"):
                hs = []
                for h in e["heading"]:
                    en = h["en"]
                    if not en.strip():
                        continue  # e.g. Habakkuk 3:19 trailing musical notation
                    entry = {"level": h["level"], "en": en, "th": th.get(en, "")}
                    if h.get("italic"):
                        entry["italic"] = True
                    if h.get("psalm"):
                        entry["psalm"] = True
                    hs.append(entry)
                    tot_headings += 1
                if hs:
                    ev["heading"] = hs
            if e.get("book_divider"):
                ev["book_divider"] = e["book_divider"]
            if e.get("acrostic"):
                ev["acrostic"] = e["acrostic"]
            if e.get("selah"):
                ev["selah"] = True
            if e.get("start"):
                ev["start"] = e["start"]
            if len(ev) > 2:  # more than c,v
                out_struct.append(ev)

        # merge events that resolved onto the same (c,v)
        merged = {}
        order = []
        for ev in out_struct:
            key = (ev["c"], ev["v"])
            if key in merged:
                base = merged[key]
                for k, val in ev.items():
                    if k in ("c", "v"):
                        continue
                    if k == "heading":
                        base.setdefault("heading", []).extend(val)
                    else:
                        base[k] = val
            else:
                merged[key] = dict(ev)
                order.append(key)
        final = [merged[k] for k in order]

        (OUT / f"{slug}.json").write_text(json.dumps({
            "book": slug, "en": d["en"], "th": title,
            "source": "Berean Standard Bible section apparatus (CC0)",
            "headings_status": "draft",
            "versification": "eremos-reader (MT-anchored at divergent seams)",
            "structure": final,
        }, ensure_ascii=False, indent=1), encoding="utf-8")
        tot_events += len(final)

    print(f"books: 66  events: {tot_events}  headings attached: {tot_headings}  dropped marks: {dropped}")
    for d in drop_log:
        print("  dropped:", d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
