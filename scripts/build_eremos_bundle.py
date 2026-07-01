#!/usr/bin/env python3
"""
Transform output/translations/<slug>_<NN>.json files into a single bundle JSON
for the Eremos app: [{book, chapter, verse, thai, thai_literal, key_decisions, notes}].

Walks every translated chapter of every book found in output/translations/,
maps the filename slug back to the canonical 3-letter MACULA book code, and
writes ~/EremosVercel2/server/data/eremos_translation.json sorted by
canonical book order → chapter → verse.

VERSIFICATION: the source files are MT-anchored (Hebrew chapter/verse
numbering), but the app — like modern Bibles (BSB) and the in-app Thai KJV
fallback — uses English versification. This exporter converts every row
MT → English, resolving each reference in priority order:

  1. the verse's own `versification.english_ref` (chapter file, authoritative)
  2. data/versification_map.json entry keyed BOOK-CH-VS (fallback)
  3. identity (aligned verse; the vast majority)

Special forms:
  - "Psalm 3:title"      → superscription; merged into English verse 1
  - "Isaiah 63:19–64:1"  → span: the row lands on the FIRST ref and the rest
                           of the span is recorded in eremos_translation_gaps.json
  - two MT rows → one English ref (split MT verse, e.g. NUM 25:19 + 26:1)
                           → merged into one row in MT order

scripts/check_eremos_bundle.py verifies the result: OT must match BSB's
chapter/verse structure exactly (modulo the recorded gaps) and the NT must
be byte-identical to the pre-conversion NT.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
VERSIFICATION_MAP = ROOT / "data" / "versification_map.json"
EREMOS_DATA = Path.home() / "EremosVercel2" / "server" / "data" / "eremos_translation.json"
GAPS_DATA = EREMOS_DATA.parent / "eremos_translation_gaps.json"

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS as NT_BOOKS  # NT: {code: (name, slug)}
from extract_book_hebrew import BOOKS as OT_BOOKS  # OT: {code: (name, slug, file_prefix)}

# Combined slug → code lookup (NT + OT). OT BOOKS tuples are (name, slug, prefix);
# normalise to (name, slug) and merge preserving canonical Bible-order: OT first
# (Genesis → Malachi), then NT (Matthew → Revelation).
_OT_BOOKS_NORM = {code: (name, slug) for code, (name, slug, _prefix) in OT_BOOKS.items()}
ALL_BOOKS = {**_OT_BOOKS_NORM, **NT_BOOKS}

SLUG_TO_CODE = {slug: code for code, (_, slug) in ALL_BOOKS.items()}
CODE_ORDER = {code: i for i, code in enumerate(ALL_BOOKS.keys())}
FILENAME_RE = re.compile(r"^(?P<slug>[a-z0-9]+)_(?P<chapter>\d{2,3})\.json$")

# "…63:19–64:1" (en-dash or hyphen span) | "…3:title" | "…4:1"
REF_RE = re.compile(
    r"(?P<ch>\d+):(?P<vs>\d+|title)"
    r"(?:\s*[–-]\s*(?:(?P<ch2>\d+):)?(?P<vs2>\d+))?\s*$"
)


def parse_english_ref(ref, where):
    """'Book 63:19–64:1' → ((63,19), (64,1)); 'Book 3:title' → ((3,'title'), None).

    Only two-verse spans exist (a split MT verse covers exactly two English
    verses); anything longer or stranger is a data bug — fail loudly.
    """
    m = REF_RE.search(ref)
    if not m:
        raise SystemExit(f"FATAL: unparseable english_ref {ref!r} at {where}")
    ch = int(m.group("ch"))
    vs = m.group("vs")
    vs = vs if vs == "title" else int(vs)
    span_end = None
    if m.group("vs2"):
        ch2 = int(m.group("ch2")) if m.group("ch2") else ch
        vs2 = int(m.group("vs2"))
        consecutive_same_ch = ch2 == ch and vs != "title" and vs2 == vs + 1
        next_ch_start = ch2 == ch + 1 and vs2 == 1
        if not (consecutive_same_ch or next_ch_start):
            raise SystemExit(f"FATAL: span english_ref {ref!r} at {where} is not a 2-verse span")
        span_end = (ch2, vs2)
    return (ch, vs), span_end


def load_versification_map():
    """{(BOOK, mt_ch, mt_vs): english_ref} for diverging entries only."""
    with open(VERSIFICATION_MAP, encoding="utf-8") as f:
        raw = json.load(f)
    out = {}
    for key, entry in raw.items():
        if key.startswith("_") or not isinstance(entry, dict):
            continue
        if not entry.get("diverges") or not entry.get("english_ref"):
            continue
        book, ch, vs = key.rsplit("-", 2)
        out[(book, int(ch), int(vs))] = entry["english_ref"]
    return out


def english_target(code, mt_ch, mt_vs, versification, vmap):
    """Resolve one MT reference → ((eng_ch, eng_vs|'title'), span_end|None).

    File-level versification wins; the map is the fallback; identity
    otherwise. File and map disagreeing is a data bug — fail loudly.
    """
    where = f"{code} {mt_ch}:{mt_vs}"
    file_ref = None
    if isinstance(versification, dict) and versification.get("diverges"):
        file_ref = versification.get("english_ref")
    map_ref = vmap.get((code, mt_ch, mt_vs))
    if file_ref and map_ref:
        if parse_english_ref(file_ref, where)[0] != parse_english_ref(map_ref, where)[0]:
            raise SystemExit(
                f"FATAL: {where} file english_ref {file_ref!r} disagrees "
                f"with versification_map {map_ref!r}"
            )
    ref = file_ref or map_ref
    if not ref:
        return (mt_ch, mt_vs), None
    return parse_english_ref(ref, where)


def merge_rows(first, second):
    """Two MT rows that land on one English verse (superscription → v1, or a
    split MT verse). Concatenate in MT order; union the metadata."""
    merged = dict(second)
    merged["thai"] = (first["thai"].rstrip() + " " + second["thai"].lstrip()).strip()
    literals = [x for x in [first.get("thai_literal"), second.get("thai_literal")] if x]
    merged["thai_literal"] = " ".join(literals) if literals else None
    merged["thai_summary"] = second.get("thai_summary") or first.get("thai_summary")
    merged["key_decisions"] = (first.get("key_decisions") or []) + (second.get("key_decisions") or [])
    notes = [x for x in [first.get("notes"), second.get("notes")] if x]
    merged["notes"] = "\n\n".join(notes) if notes else None
    return merged


def main():
    vmap = load_versification_map()
    staged = []  # (sort_key, english_key, row)
    expected_gaps = set()
    mt_seq = 0
    converted = 0

    for chapter_file in sorted(TRANSLATIONS.glob("*_*.json")):
        if "_demo" in chapter_file.name:
            continue
        m = FILENAME_RE.match(chapter_file.name)
        if not m:
            continue
        slug = m.group("slug")
        code = SLUG_TO_CODE.get(slug)
        if code is None:
            print(f"  skip (unknown slug): {chapter_file.name}")
            continue
        with open(chapter_file, encoding="utf-8") as f:
            verses = json.load(f)
        for v in verses:
            t = v.get("translation", {})
            (eng_ch, eng_vs), span_end = english_target(
                code, v["chapter"], v["verse"], v.get("versification"), vmap
            )
            if (eng_ch, eng_vs) != (v["chapter"], v["verse"]):
                converted += 1
            if span_end:
                expected_gaps.add((code, span_end[0], span_end[1]))
            mt_seq += 1
            is_title = eng_vs == "title"
            vs_num = 1 if is_title else eng_vs
            row = {
                "book": code,
                "chapter": eng_ch,
                "verse": vs_num,
                "thai": t.get("thai", ""),
                "thai_literal": t.get("thai_literal") or None,
                "thai_summary": t.get("thai_summary") or None,
                "key_decisions": t.get("key_decisions") or [],
                "notes": t.get("notes") or None,
            }
            # Titles sort directly before their English verse 1 so the
            # generic collision-merge below folds them in as the leading text.
            sort_key = (CODE_ORDER.get(code, 999), eng_ch, vs_num, 0 if is_title else 1, mt_seq)
            staged.append((sort_key, (code, eng_ch, vs_num), row))

    by_key = {}
    merges = 0
    for _sort, key, row in sorted(staged, key=lambda s: s[0]):
        if key in by_key:
            by_key[key] = merge_rows(by_key[key], row)
            merges += 1
        else:
            by_key[key] = row

    bundle = list(by_key.values())
    bundle.sort(key=lambda v: (CODE_ORDER.get(v["book"], 999), v["chapter"], v["verse"]))

    EREMOS_DATA.parent.mkdir(parents=True, exist_ok=True)
    with open(EREMOS_DATA, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)
    with open(GAPS_DATA, "w", encoding="utf-8") as f:
        json.dump(sorted([list(g) for g in expected_gaps]), f, indent=2)

    book_counts = {}
    for v in bundle:
        book_counts[v["book"]] = book_counts.get(v["book"], 0) + 1
    print(f"Wrote {len(bundle)} verses to {EREMOS_DATA}")
    print(f"  MT→English: {converted} renumbered, {merges} rows merged, "
          f"{len(expected_gaps)} span gap(s): {sorted(expected_gaps) if expected_gaps else '—'}")
    print(f"  Size: {EREMOS_DATA.stat().st_size:,} bytes")
    for code, count in book_counts.items():
        print(f"  {code}: {count} verses")


if __name__ == "__main__":
    main()
