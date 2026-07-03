#!/usr/bin/env python3
"""Canonical MT → English(BSB) versification converter.

The translation source files (output/translations/<slug>_<NN>.json) are
MT-anchored (Hebrew chapter/verse numbering). Every downstream artifact that
must match modern Bibles — the app bundle (build_eremos_bundle.py), the reader
edition (render_reader.py), and the public website — needs the same English
(BSB) numbering. This module is the ONE place that conversion lives, so the
bundle and the reader can never drift apart again.

Resolution priority per reference (from PR #213):
  1. the verse's own `versification.english_ref` (chapter file, authoritative)
  2. data/versification_map.json entry keyed BOOK-CH-VS (fallback)
  3. identity (aligned verse; the vast majority)

Special forms handled: superscription ("Psalm 3:title" → merged into English
verse 1), split MT verse spanning two English verses ("Isaiah 63:19–64:1" with
`english_split`), and two MT rows merging onto one English ref (e.g. NUM 25:19
+ 26:1). Text is never dropped or invented — english_split must reassemble to
the source verse exactly, or the converter fails loudly.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSIFICATION_MAP = ROOT / "data" / "versification_map.json"

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


def to_english_rows(code, mt_verses, vmap, code_order_rank=0):
    """Convert one book's MT verses (in MT order, across all chapters) into
    English(BSB)-numbered rows. Each input verse is a translation-source dict
    {chapter, verse, translation:{...}, versification?}.

    SUPERSCRIPTIONS: a verse whose english_ref is "…:title" (66 Psalm
    superscriptions) is NOT a numbered verse under English/BSB numbering — v1
    is the real first line, matching THSV 2011 / Thai KJV / BSB and the live
    app bundle (corrected 2026-07-02, EremosVercel2 a3fecdac). Such verses are
    therefore DROPPED from the numbered rows and returned separately (keyed by
    English chapter) so the reader can show them as unnumbered text above v1.
    (The earlier fold-into-v1 approach was the bug that fix corrected.)

    Returns (rows, superscriptions):
      rows — list sorted by (english_chapter, english_verse), each
        {book, chapter, verse, thai, thai_literal, thai_summary,
         key_decisions, notes}
      superscriptions — {english_chapter: thai_superscription_text}
    `code_order_rank` only affects cross-book ordering; within one book it is
    constant, so any value gives the same per-book result.
    """
    staged = []  # (sort_key, english_key, row)
    superscriptions = {}
    seq = 0
    for v in mt_verses:
        t = v.get("translation", {}) or {}
        (eng_ch, eng_vs), span_end = english_target(
            code, v["chapter"], v["verse"], v.get("versification"), vmap
        )
        seq += 1

        if eng_vs == "title":
            # Not a numbered verse under English numbering — keep the text aside
            # for unnumbered display, do not stage a row.
            superscriptions[eng_ch] = t.get("thai", "").strip()
            continue

        split = None
        if span_end:
            vsf = v.get("versification") or {}
            split = vsf.get("english_split")
            if split is not None:
                where = f"{code} {v['chapter']}:{v['verse']}"
                if not (isinstance(split, list) and len(split) == 2
                        and all(isinstance(s, str) and s.strip() for s in split)):
                    raise SystemExit(f"FATAL: english_split at {where} must be two non-empty strings")
                if " ".join(" ".join(split).split()) != " ".join(t.get("thai", "").split()):
                    raise SystemExit(f"FATAL: english_split at {where} does not reassemble to translation.thai")

        row = {
            "book": code,
            "chapter": eng_ch,
            "verse": eng_vs,
            "thai": split[0] if split else t.get("thai", ""),
            "thai_literal": t.get("thai_literal") or None,
            "thai_summary": t.get("thai_summary") or None,
            "key_decisions": t.get("key_decisions") or [],
            "notes": t.get("notes") or None,
        }
        sort_key = (code_order_rank, eng_ch, eng_vs, 1, seq)
        staged.append((sort_key, (code, eng_ch, eng_vs), row))
        if split:
            seq += 1
            second = {
                "book": code, "chapter": span_end[0], "verse": span_end[1],
                "thai": split[1], "thai_literal": None, "thai_summary": None,
                "key_decisions": [], "notes": None,
            }
            staged.append((
                (code_order_rank, span_end[0], span_end[1], 1, seq),
                (code, span_end[0], span_end[1]), second,
            ))

    by_key = {}
    order = []
    for _sort, key, row in sorted(staged, key=lambda s: s[0]):
        if key in by_key:
            by_key[key] = merge_rows(by_key[key], row)
        else:
            by_key[key] = row
            order.append(key)
    rows = [by_key[k] for k in order]
    rows.sort(key=lambda v: (v["chapter"], v["verse"]))
    return rows, superscriptions
