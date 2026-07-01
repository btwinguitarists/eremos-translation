#!/usr/bin/env python3
"""
Verify the exported Eremos app bundle against BSB's chapter/verse structure.

The app (plans, book browser, cross-references, and the parallel versions)
uses English versification, so the bundle must match BSB exactly:

  - same 66 books, same chapter sets per book
  - same verse set per chapter, with only these exceptions:
      * OT verses listed in eremos_translation_gaps.json (a split MT verse
        covers two English verses; the text sits on the first — e.g. ISA 64:1
        lives inside 63:19 until the source verse is editorially split)
      * OT_ALLOWED_MISSING — English verses with no MT counterpart at all
      * NT_ALLOWED_* — long-shipped critical-text numbering / inclusion
        decisions in the NT, kept as-is pending owner review
  - an EXTRA verse (present in the bundle, absent in BSB) outside the NT
    allowlist is always fatal: it means stale MT numbering leaked through.

Exit 0 = structurally sound; exit 1 prints every offending chapter.

Usage: python3 scripts/check_eremos_bundle.py [bundle.json]
  (defaults to ~/EremosVercel2/server/data/eremos_translation.json; BSB
   structure is read from ~/EremosVercel2/server/data/engbsb_usfx.xml)
"""
import json
import re
import sys
from pathlib import Path

EREMOS_DIR = Path.home() / "EremosVercel2" / "server" / "data"
BUNDLE = Path(sys.argv[1]) if len(sys.argv) > 1 else EREMOS_DIR / "eremos_translation.json"
GAPS = BUNDLE.parent / "eremos_translation_gaps.json"
BSB_USFX = EREMOS_DIR / "engbsb_usfx.xml"

NT = {"MAT","MRK","LUK","JHN","ACT","ROM","1CO","2CO","GAL","EPH","PHP","COL",
      "1TH","2TH","1TI","2TI","TIT","PHM","HEB","JAS","1PE","2PE","1JN","2JN",
      "3JN","JUD","REV"}

# English verses with no Masoretic counterpart: a numbered gap in the Eremos
# text, exactly like the NT inclusion-variant gaps the app already ships.
# NEH 7:68 exists in BSB via the Ezra 2:66 parallel; the MT lacks it.
OT_ALLOWED_MISSING = {("NEH", 7, 68)}

# NT spots where the long-shipped bundle deliberately follows critical-text
# numbering/inclusion rather than BSB. Kept as-is pending owner review.
NT_ALLOWED_MISSING = {("2CO", 13, 14), ("ACT", 19, 41)}
NT_ALLOWED_EXTRA = {("3JN", 1, 15), ("REV", 12, 18), ("ROM", 16, 24)}

# NT verses BSB prints but the Eremos NT relegates to footnotes (inclusion-
# variant policy). BSB brackets most of these; where BSB includes one the
# bundle's absence is expected.
NT_INCLUSION_VARIANTS = {
    ("MAT",17,21),("MAT",18,11),("MAT",23,14),("MRK",7,16),("MRK",9,44),
    ("MRK",9,46),("MRK",11,26),("MRK",15,28),("LUK",17,36),("LUK",23,17),
    ("JHN",5,4),("ACT",8,37),("ACT",15,34),("ACT",24,7),("ACT",28,29),
    ("ROM",16,24),
}


def bsb_structure():
    xml = BSB_USFX.read_text(encoding="utf-8")
    struct = {}
    book = ch = None
    for m in re.finditer(r'<book id="([A-Z0-9]{3})"|<c id="(\d+)"|<v id="(\d+)[a-z]?"', xml):
        if m.group(1):
            book = m.group(1)
        elif m.group(2):
            ch = int(m.group(2))
        elif m.group(3) and book and ch:
            struct.setdefault(book, {}).setdefault(ch, set()).add(int(m.group(3)))
    return struct


def main():
    bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
    gaps = {tuple(g) for g in json.loads(GAPS.read_text(encoding="utf-8"))} if GAPS.exists() else set()
    bsb = bsb_structure()

    have = {}
    dupes = []
    for r in bundle:
        key = (r["book"], r["chapter"], r["verse"])
        if key in have:
            dupes.append(key)
        have[key] = True
    bset = set(have)

    books = {r["book"] for r in bundle}
    problems = []
    if dupes:
        problems.append(f"DUPLICATE keys in bundle: {sorted(dupes)[:20]}")
    if books != set(bsb):
        problems.append(f"book set mismatch: missing {sorted(set(bsb)-books)}, extra {sorted(books-set(bsb))}")

    sset = {(b, c, v) for b, chs in bsb.items() for c, vs in chs.items() for v in vs}
    missing = sset - bset  # in BSB, not in bundle
    extra = bset - sset    # in bundle, not in BSB

    bad_missing = []
    for k in sorted(missing):
        if k[0] in NT:
            if k in NT_ALLOWED_MISSING or k in NT_INCLUSION_VARIANTS:
                continue
        else:
            if k in gaps or k in OT_ALLOWED_MISSING:
                continue
        bad_missing.append(k)

    bad_extra = [k for k in sorted(extra) if not (k[0] in NT and k in NT_ALLOWED_EXTRA)]

    def by_chapter(keys):
        out = {}
        for b, c, v in keys:
            out.setdefault((b, c), []).append(v)
        return out

    if bad_missing:
        problems.append("MISSING vs BSB (bundle lacks these English verses):")
        for (b, c), vs in sorted(by_chapter(bad_missing).items()):
            problems.append(f"  {b} {c}: {sorted(vs)}")
    if bad_extra:
        problems.append("EXTRA vs BSB (stale MT numbering leaked through):")
        for (b, c), vs in sorted(by_chapter(bad_extra).items()):
            problems.append(f"  {b} {c}: {sorted(vs)}")

    ot_books = len(books - NT)
    print(f"Bundle: {len(bundle)} rows, {len(books)} books ({ot_books} OT). "
          f"Gaps file: {sorted(gaps) if gaps else '—'}")
    if problems:
        print(f"\nFAIL — {len(bad_missing)} missing / {len(bad_extra)} extra / {len(dupes)} dupes:\n")
        print("\n".join(problems))
        sys.exit(1)
    print("PASS — bundle matches BSB versification (with documented exceptions).")


if __name__ == "__main__":
    main()
