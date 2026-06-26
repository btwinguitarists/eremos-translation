#!/usr/bin/env python3
"""
Build data/versification_map.json — the authoritative mapping of MT-anchored verses
to English-Bible-tradition refs (BSB / NIV / ESV) for known divergence zones.

Per docs/translator_decisions/verse_schema_and_versification_2026-05.md §2:
the OT pipeline anchors on MT versification. This map records the divergence
zones (Psalm superscriptions, Joel 3-4, Malachi 3-4) so check_versification_anchor.py
can validate each chapter and so reader/feedback rendering can show both refs.

Strategy:
  * Auto-detect Psalm superscription offsets by comparing MT verse counts
    (from sources/macula-hebrew/WLC/lowfat/19-Psa-NNN-lowfat.xml) with BSB counts.
  * Hardcode Joel 3-4 → English 2:28-32 + 3:1-21 mapping.
  * Hardcode Malachi 3:19-24 → English 4:1-6 mapping.
  * Hardcode minor shifts (Job 41 / 1 Sam 23-24 / Daniel-Ezra Aramaic boundaries).
  * Hardcode Jeremiah note (MT-priority means we use MT order; LXX-only material
    excluded per ot_canon_and_text_base — no per-verse mapping needed).

Run:
  python3 scripts/build_versification_map.py
  python3 scripts/build_versification_map.py --dry-run     # print summary, don't write
"""
from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOWFAT = ROOT / "sources" / "macula-hebrew" / "WLC" / "lowfat"
BSB_TXT = ROOT / "sources" / "bsb-text" / "bsb.txt"
OUT = ROOT / "data" / "versification_map.json"


def bsb_max_verse_per_chapter(book_name: str) -> dict[int, int]:
    """Highest verse number per chapter in BSB for a given book name."""
    rx = re.compile(rf"^{re.escape(book_name)} (\d+):(\d+)\t")
    counts: dict[int, int] = {}
    with open(BSB_TXT, encoding="utf-8") as f:
        for line in f:
            m = rx.match(line)
            if m:
                ch, v = int(m.group(1)), int(m.group(2))
                counts[ch] = max(counts.get(ch, 0), v)
    return counts


def mt_verses_per_chapter(book_prefix: str) -> dict[int, set[int]]:
    """Set of distinct MT verse numbers per chapter from MACULA Hebrew."""
    out: dict[int, set[int]] = defaultdict(set)
    for path in sorted(LOWFAT.glob(f"{book_prefix}-*-lowfat.xml")):
        m = re.search(rf"{re.escape(book_prefix)}-(\d+)-lowfat", path.name)
        if not m:
            continue
        ch = int(m.group(1))
        tree = ET.parse(path)
        for sent in tree.iter("sentence"):
            sid = sent.get("id", "")
            mm = re.match(r"\S+\s+\d+:(\d+)", sid)
            if mm:
                out[ch].add(int(mm.group(1)))
    return out


def build_psalm_entries() -> dict[str, dict]:
    """Detect superscription offsets and emit per-verse divergence entries.

    Strategy: for each psalm where MT verse count > BSB verse count, the
    superscription is the leading 1-2 MT verses. Every MT verse for that psalm
    has an english_ref shifted by the offset. Verse 1 (and 2 for double
    superscriptions) maps to english `:title`.
    """
    entries: dict[str, dict] = {}
    bsb = bsb_max_verse_per_chapter("Psalm")
    mt = mt_verses_per_chapter("19-Psa")

    for ch in sorted(mt):
        mt_max = max(mt[ch])
        bsb_max = bsb.get(ch, mt_max)
        offset = mt_max - bsb_max  # 0 = aligned, 1 = single superscription, 2 = double
        if offset <= 0:
            continue
        for v in sorted(mt[ch]):
            key = f"PSA-{ch}-{v}"
            if v <= offset:
                english_v_ref = f"Psalm {ch}:title"
                bsb_v_ref = f"Psalm {ch}:0"
            else:
                eng_v = v - offset
                english_v_ref = f"Psalm {ch}:{eng_v}"
                bsb_v_ref = f"Psalm {ch}:{eng_v}"
            entries[key] = {
                "mt_book": "PSA",
                "mt_chapter": ch,
                "mt_verse": v,
                "mt_ref": f"Psalm {ch}:{v}",
                "english_ref": english_v_ref,
                "bsb_ref": bsb_v_ref,
                "lxx_ref": f"Psalm {ch}:{v}",
                "has_superscription": v <= offset,
                "diverges": True,
            }
    return entries


def build_joel_entries() -> dict[str, dict]:
    """Joel: MT 3:1-5 = English 2:28-32; MT 4:1-21 = English 3:1-21."""
    entries: dict[str, dict] = {}
    # MT 3:1-5 → English 2:28-32 (Acts 2:17-21 quotes these verses)
    for v in range(1, 6):
        eng_v = 27 + v  # MT 3:1 = English 2:28
        entries[f"JOL-3-{v}"] = {
            "mt_book": "JOL",
            "mt_chapter": 3,
            "mt_verse": v,
            "mt_ref": f"Joel 3:{v}",
            "english_ref": f"Joel 2:{eng_v}",
            "bsb_ref": f"Joel 2:{eng_v}",
            "lxx_ref": f"Joel 3:{v}",
            "diverges": True,
            "nt_citations": ["ACT 2:17-21"] if v <= 5 else [],
        }
    # MT 4:1-21 → English 3:1-21
    for v in range(1, 22):
        entries[f"JOL-4-{v}"] = {
            "mt_book": "JOL",
            "mt_chapter": 4,
            "mt_verse": v,
            "mt_ref": f"Joel 4:{v}",
            "english_ref": f"Joel 3:{v}",
            "bsb_ref": f"Joel 3:{v}",
            "lxx_ref": f"Joel 4:{v}",
            "diverges": True,
        }
    return entries


def build_malachi_entries() -> dict[str, dict]:
    """Malachi: MT 3:19-24 = English 4:1-6 (English splits MT chapter 3)."""
    entries: dict[str, dict] = {}
    for v in range(19, 25):
        eng_v = v - 18
        entries[f"MAL-3-{v}"] = {
            "mt_book": "MAL",
            "mt_chapter": 3,
            "mt_verse": v,
            "mt_ref": f"Malachi 3:{v}",
            "english_ref": f"Malachi 4:{eng_v}",
            "bsb_ref": f"Malachi 4:{eng_v}",
            "lxx_ref": f"Malachi 3:{v}",
            "diverges": True,
        }
    return entries


def build_micah_entries() -> dict[str, dict]:
    """Micah 4/5 boundary: MT 4:14 = English 5:1.

    English/KJV begin chapter 5 one verse earlier than the MT: English Micah 5:1
    ("O daughter of troops…") is MT Micah 4:14. So MT chapter 4 has 14 verses
    (4:1-13 align; 4:14 = English 5:1), and all of MT chapter 5 then runs one
    ahead of the English numbering (MT 5:N = English 5:N+1). The MT-5 entries are
    added when that chapter is translated.
    """
    entries: dict[str, dict] = {}
    entries["MIC-4-14"] = {
        "mt_book": "MIC",
        "mt_chapter": 4,
        "mt_verse": 14,
        "mt_ref": "Micah 4:14",
        "english_ref": "Micah 5:1",
        "bsb_ref": "Micah 5:1",
        "lxx_ref": "Micah 4:14",
        "diverges": True,
    }
    return entries


def build_hosea_entries() -> dict[str, dict]:
    """Hosea chapter-boundary divergences between the MT and English/KJV numbering.

    English/KJV place three chapter boundaries one or two verses earlier than the
    MT, so three MT chapters are shifted against the English numbering:

    * Chapter 2  — MT 2:1-2 = English 1:10-11; MT 2:3-25 = English 2:1-23 (+2 shift).
    * Chapter 12 — MT 12:1 = English 11:12; MT 12:2-15 = English 12:1-14 (-1 shift).
    * Chapter 14 — MT 14:1 = English 13:16; MT 14:2-10 = English 14:1-9 (-1 shift).

    Chapters 3-11 and 13 re-sync.
    """
    entries: dict[str, dict] = {}
    # --- Chapter 2: MT 2:1-2 = Eng 1:10-11; MT 2:3-25 = Eng 2:1-23 ---
    for v in range(1, 26):
        if v == 1:
            eng_ref = "Hosea 1:10"
        elif v == 2:
            eng_ref = "Hosea 1:11"
        else:
            eng_ref = f"Hosea 2:{v - 2}"
        entries[f"HOS-2-{v}"] = {
            "mt_book": "HOS",
            "mt_chapter": 2,
            "mt_verse": v,
            "mt_ref": f"Hosea 2:{v}",
            "english_ref": eng_ref,
            "bsb_ref": eng_ref,
            "lxx_ref": f"Hosea 2:{v}",
            "diverges": True,
        }
    # --- Chapter 12: MT 12:1 = Eng 11:12; MT 12:2-15 = Eng 12:1-14 ---
    for v in range(1, 16):
        eng_ref = "Hosea 11:12" if v == 1 else f"Hosea 12:{v - 1}"
        entries[f"HOS-12-{v}"] = {
            "mt_book": "HOS",
            "mt_chapter": 12,
            "mt_verse": v,
            "mt_ref": f"Hosea 12:{v}",
            "english_ref": eng_ref,
            "bsb_ref": eng_ref,
            "lxx_ref": f"Hosea 12:{v}",
            "diverges": True,
        }
    # --- Chapter 14: MT 14:1 = Eng 13:16; MT 14:2-10 = Eng 14:1-9 ---
    for v in range(1, 11):
        eng_ref = "Hosea 13:16" if v == 1 else f"Hosea 14:{v - 1}"
        entries[f"HOS-14-{v}"] = {
            "mt_book": "HOS",
            "mt_chapter": 14,
            "mt_verse": v,
            "mt_ref": f"Hosea 14:{v}",
            "english_ref": eng_ref,
            "bsb_ref": eng_ref,
            "lxx_ref": f"Hosea 14:{v}",
            "diverges": True,
        }
    return entries


def build_aramaic_boundary_entries() -> dict[str, dict]:
    """Mark Aramaic-section boundary verses (Dan 2:4 Heb→Aram, Ezra 4:8, 7:12, etc.).

    These are not versification *divergences* per se but require dispatcher
    awareness. Marked with `aramaic_section: true` for downstream scripts.
    """
    boundaries = [
        # (book_code, chapter, verse, note)
        ("DAN", 2, 4, "Hebrew→Aramaic mid-verse (4a Heb, 4b Aram)"),
        ("DAN", 7, 28, "Aramaic→Hebrew at end of chapter 7"),
        ("EZR", 4, 8, "Hebrew→Aramaic"),
        ("EZR", 6, 18, "Aramaic→Hebrew"),
        ("EZR", 7, 12, "Hebrew→Aramaic"),
        ("EZR", 7, 26, "Aramaic→Hebrew"),
        ("JER", 10, 11, "Single Aramaic verse in Hebrew context"),
        ("GEN", 31, 47, "Two Aramaic words mid-verse (Yegar-Sahadutha)"),
    ]
    entries = {}
    for book, ch, v, note in boundaries:
        entries[f"{book}-{ch}-{v}"] = {
            "mt_book": book,
            "mt_chapter": ch,
            "mt_verse": v,
            "mt_ref": f"{book} {ch}:{v}",
            "diverges": False,
            "aramaic_section": True,
            "note": note,
        }
    return entries


def build_minor_shift_entries() -> dict[str, dict]:
    """Minor MT-vs-English verse-shift cases: 1 Sam 23-24, Job 41, etc.

    These are 1-verse shifts where English groups verses differently than MT.
    We anchor on MT and document the English alternate.
    """
    # 1 Samuel 24: MT 24:1 = English 23:29 (English moves the chapter break)
    # Just record the boundary verses (MT 1 Sa 24:1 → Eng 1 Sa 23:29)
    entries = {
        "1SA-24-1": {
            "mt_book": "1SA",
            "mt_chapter": 24,
            "mt_verse": 1,
            "mt_ref": "1 Samuel 24:1",
            "english_ref": "1 Samuel 23:29",
            "bsb_ref": "1 Samuel 23:29",
            "diverges": True,
            "note": "MT begins ch.24 here; English ends ch.23 here — verse shift continues through 24:22 (MT) = 24:1-21 (English)",
        },
    }
    # Job 40-41 divergence zone (BHS/MT numbering). MT/BHS Job 40 has 32 verses,
    # Job 41 has 26; English Job 40 has 24, Job 41 has 34. The shift:
    #   MT 40:25-32 = English 41:1-8  ;  MT 41:1-26 = English 41:9-34.
    # extract_book_hebrew.py uses BHS numbering. Backfilled 2026-05-30 per the JOB
    # end-of-book audit so cross-reference / USFM export resolves Job 41 correctly.
    for mt_v in range(25, 33):              # MT 40:25..40:32  = English 41:1..41:8
        eng_v = mt_v - 24
        entries[f"JOB-40-{mt_v}"] = {
            "mt_book": "JOB",
            "mt_chapter": 40,
            "mt_verse": mt_v,
            "mt_ref": f"Job 40:{mt_v}",
            "english_ref": f"Job 41:{eng_v}",
            "bsb_ref": f"Job 41:{eng_v}",
            "diverges": True,
            "note": "MT/BHS Job 40 has 32 verses; MT 40:25-32 = English 41:1-8.",
        }
    for mt_v in range(1, 27):               # MT 41:1..41:26  = English 41:9..41:34
        eng_v = mt_v + 8
        entries[f"JOB-41-{mt_v}"] = {
            "mt_book": "JOB",
            "mt_chapter": 41,
            "mt_verse": mt_v,
            "mt_ref": f"Job 41:{mt_v}",
            "english_ref": f"Job 41:{eng_v}",
            "bsb_ref": f"Job 41:{eng_v}",
            "diverges": True,
            "note": (
                "MT/BHS Job 40 has 32 verses, Job 41 has 26. MT 40:25-32 = English 41:1-8; "
                "MT 41:1 = English 41:9 (so MT 41:1-26 = English 41:9-34). The extractor "
                "(extract_book_hebrew.py) uses this BHS numbering — corrected 2026-05-30 from "
                "the earlier 34-verse-English-chapter framing that mislabeled MT 41:1 as Eng 40:25."
            ) if mt_v == 1 else "MT 41:1-26 = English 41:9-34 (BHS numbering).",
        }
    return entries


def build_ecclesiastes_entries() -> dict[str, dict]:
    """Ecclesiastes: MT 4:17 = English 5:1; MT 5:1-19 = English 5:2-20.

    English moves the chapter break — 'Guard your steps' (MT 4:17) opens
    English chapter 5, shifting all of MT ch.5 by one. LXX follows MT.
    Registered 2026-06-03 when ECC 4 entered translation.
    """
    entries: dict[str, dict] = {
        "ECC-4-17": {
            "mt_book": "ECC",
            "mt_chapter": 4,
            "mt_verse": 17,
            "mt_ref": "Ecclesiastes 4:17",
            "english_ref": "Ecclesiastes 5:1",
            "bsb_ref": "Ecclesiastes 5:1",
            "lxx_ref": "Ecclesiastes 4:17",
            "diverges": True,
            "note": "MT ends ch.4 here; English begins ch.5 — shift continues through MT 5:1-19 = English 5:2-20.",
        },
    }
    for mt_v in range(1, 20):  # MT 5:1..5:19 = English 5:2..5:20
        eng_v = mt_v + 1
        entries[f"ECC-5-{mt_v}"] = {
            "mt_book": "ECC",
            "mt_chapter": 5,
            "mt_verse": mt_v,
            "mt_ref": f"Ecclesiastes 5:{mt_v}",
            "english_ref": f"Ecclesiastes 5:{eng_v}",
            "bsb_ref": f"Ecclesiastes 5:{eng_v}",
            "lxx_ref": f"Ecclesiastes 5:{mt_v}",
            "diverges": True,
        }
    return entries


def build_songofsongs_entries() -> dict[str, dict]:
    """Song of Songs: MT 7:1 = English 6:13 ('Return, O Shulammite' ends English
    ch.6), so MT 7:1-14 = English 6:13 + 7:1-13. LXX follows MT.
    Registered 2026-06-04 when SNG 7 entered translation."""
    entries: dict[str, dict] = {
        "SNG-7-1": {
            "mt_book": "SNG",
            "mt_chapter": 7,
            "mt_verse": 1,
            "mt_ref": "Song of Songs 7:1",
            "english_ref": "Song of Songs 6:13",
            "bsb_ref": "Song of Songs 6:13",
            "lxx_ref": "Song of Songs 7:1",
            "diverges": True,
            "note": "MT begins ch.7 here; English ends ch.6 — shift continues through MT 7:2-14 = English 7:1-13.",
        },
    }
    for mt_v in range(2, 15):  # MT 7:2..7:14 = English 7:1..7:13
        eng_v = mt_v - 1
        entries[f"SNG-7-{mt_v}"] = {
            "mt_book": "SNG",
            "mt_chapter": 7,
            "mt_verse": mt_v,
            "mt_ref": f"Song of Songs 7:{mt_v}",
            "english_ref": f"Song of Songs 7:{eng_v}",
            "bsb_ref": f"Song of Songs 7:{eng_v}",
            "lxx_ref": f"Song of Songs 7:{mt_v}",
            "diverges": True,
        }
    return entries


def main():
    parser = argparse.ArgumentParser(description="Build data/versification_map.json")
    parser.add_argument("--dry-run", action="store_true", help="Print summary; do not write file")
    args = parser.parse_args()

    psalm_entries = build_psalm_entries()
    joel_entries = build_joel_entries()
    mal_entries = build_malachi_entries()
    hosea_entries = build_hosea_entries()
    micah_entries = build_micah_entries()
    aramaic_entries = build_aramaic_boundary_entries()
    minor_entries = build_minor_shift_entries()
    ecc_entries = build_ecclesiastes_entries()
    sng_entries = build_songofsongs_entries()

    out = {
        "_meta": {
            "schema": "MT-anchored. Each entry maps a MT-versification reference to its English/BSB/LXX equivalent. Absent entries are assumed aligned across all traditions.",
            "generated_by": "scripts/build_versification_map.py",
            "policy": "docs/translator_decisions/verse_schema_and_versification_2026-05.md",
        },
        "_psalm_superscription_count": sum(
            1 for e in psalm_entries.values() if e.get("has_superscription")
        ),
        "_total_entries": (
            len(psalm_entries)
            + len(joel_entries)
            + len(mal_entries)
            + len(aramaic_entries)
            + len(minor_entries)
            + len(ecc_entries)
        ),
    }
    out.update(psalm_entries)
    out.update(joel_entries)
    out.update(mal_entries)
    out.update(hosea_entries)
    out.update(micah_entries)
    out.update(aramaic_entries)
    out.update(minor_entries)
    out.update(ecc_entries)
    out.update(sng_entries)

    # MERGE-PRESERVE (2026-06-03): the live map contains zones backfilled
    # directly into the JSON during book ships, outside this script
    # (1KI-5, 1KI-22, 2KI-12, 2CH, JON-2, NEH zones — 177 entries as of
    # 2026-06-03). A plain regen silently erased them once; never again.
    # Any entry key present in the existing file but not generated above is
    # carried over verbatim. To intentionally delete an entry, remove it
    # from the JSON *and* note it here.
    preserved = 0
    if OUT.exists():
        existing = json.loads(OUT.read_text(encoding="utf-8"))
        for k, v in existing.items():
            if not k.startswith("_") and k not in out:
                out[k] = v
                preserved += 1
    out["_total_entries"] = sum(1 for k in out if not k.startswith("_"))

    print(f"Psalm divergence entries: {len(psalm_entries)}")
    print(f"  superscription verses: {out['_psalm_superscription_count']}")
    print(f"Joel divergence entries: {len(joel_entries)}")
    print(f"Malachi divergence entries: {len(mal_entries)}")
    print(f"Aramaic boundary markers: {len(aramaic_entries)}")
    print(f"Minor shift entries: {len(minor_entries)}")
    print(f"Ecclesiastes divergence entries: {len(ecc_entries)}")
    print(f"Song of Songs divergence entries: {len(sng_entries)}")
    print(f"Preserved backfilled entries: {preserved}")
    print(f"TOTAL: {out['_total_entries']}")

    if args.dry_run:
        print("\n(dry run — not written)")
        return

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
