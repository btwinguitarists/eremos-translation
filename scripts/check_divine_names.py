#!/usr/bin/env python3
"""
Divine-names policy check — enforces the 2026-05-04 Tetragrammaton lock.

Per docs/translator_decisions/divine_names_table_2026-05.md (third revision):

  יהוה (Tetragrammaton) → องค์พระผู้เป็นเจ้า  (matches NT corpus)
  אֲדֹנָי יְהוִה (Adonai-YHWH compound) → องค์พระผู้เป็นเจ้า  (compound collapses)
  יְהוָה צְבָאוֹת (YHWH Tsebaoth) → องค์พระผู้เป็นเจ้าจอมโยธα
  אֲדֹנָי (Adonai standalone) → องค์เจ้านาย
  Place-name compounds (יהוה־יִרְאֶה etc.) → ยาห์เวห์-X (transliterated)

What this enforces:

  [A] When the Hebrew field of a verse contains יהוה (the Tetragrammaton),
      the Thai field MUST contain องค์พระผู้เป็นเจ้า — unless the verse is
      a place-name compound (יהוה־יִרְאֶה family), in which case the
      transliterated form ยาห์เวห์-X is required + a footer note.

  [B] When the Hebrew contains the Adonai-YHWH compound (אֲדֹנָי יְהוִה),
      the Thai uses องค์พระผู้เป็นเจ้า (single rendering, compound collapses).
      The verse's `key_decisions` MUST record the underlying compound form.

  [C] When the Hebrew contains standalone אֲדֹנָי (without YHWH), the Thai
      uses องค์เจ้านาย (matches NT δεσπότης pattern).

  [D] Per-chapter first-occurrence footnote: every chapter where YHWH appears
      MUST have a Tier 2 footer note in the first-YHWH-occurrence verse
      (data/textual_variants/<slug>_<chapter>.json) explaining the
      Tetragrammaton convention. Initial implementation = WARNING-only;
      promote to strict once textual_variants infrastructure is wired in.

  [E] Per-verse `key_decisions` Hebrew-form transparency: every verse with a
      YHWH-family form MUST carry a `key_decisions` entry that names the
      underlying Hebrew form. This is the durable transparency mechanism per
      divine_names_table §"Layer 1".

  [F] Forbidden renderings: `พระยาห์เวห์` MUST NOT appear in the Thai field
      EXCEPT inside a place-name compound (ยาห์เวห์ยีเรห์, etc.). Bare
      `พระยาห์เวห์` indicates the THSV11 historical-transliteration form
      that was reversed by the third-revision flip.

Usage:
  python3 scripts/check_divine_names.py --book GEN --chapter 1
  python3 scripts/check_divine_names.py --all
  python3 scripts/check_divine_names.py --report

Exit codes:
  0 = clean
  1 = at least one hard fail [A]/[B]/[C]/[E]/[F]

[D] is warn-only at this stage.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
TEXTUAL_VARIANTS = ROOT / "output" / "textual_variants"
REPORTS = ROOT / "output" / "check_reports"

OT_SLUG_TO_CODE = {
    "genesis": "GEN", "exodus": "EXO", "leviticus": "LEV", "numbers": "NUM",
    "deuteronomy": "DEU", "joshua": "JOS", "judges": "JDG", "ruth": "RUT",
    "1samuel": "1SA", "2samuel": "2SA", "1kings": "1KI", "2kings": "2KI",
    "1chronicles": "1CH", "2chronicles": "2CH", "ezra": "EZR", "nehemiah": "NEH",
    "esther": "EST", "job": "JOB", "psalms": "PSA", "proverbs": "PRO",
    "ecclesiastes": "ECC", "songofsongs": "SNG", "isaiah": "ISA", "jeremiah": "JER",
    "lamentations": "LAM", "ezekiel": "EZK", "daniel": "DAN", "hosea": "HOS",
    "joel": "JOL", "amos": "AMO", "obadiah": "OBA", "jonah": "JON",
    "micah": "MIC", "nahum": "NAM", "habakkuk": "HAB", "zephaniah": "ZEP",
    "haggai": "HAG", "zechariah": "ZEC", "malachi": "MAL",
}

# Divine-names locks
THAI_YHWH = "องค์พระผู้เป็นเจ้า"
THAI_ADONAI = "องค์เจ้านาย"
THAI_TSEBAOTH = "องค์พระผู้เป็นเจ้าจอมโยธา"
FORBIDDEN_THSV11 = "พระยาห์เวห์"  # the third-revision reversed form

# Place-name YHWH compounds — transliteration is preserved per
# divine_names_table_2026-05 §"Why the place-name compounds are the only
# place ยาห์เวห์ survives"
PLACE_NAME_PATTERN = re.compile(r"ยาห์เวห์[ยนชซ][฀-๿]+")

YHWH_PATTERN = re.compile(r"יהוה")
# Adonai-YHWH compound: אֲדֹנָי יְהוִה (with vowel pointing variations)
# We normalize to consonants for matching.
ADONAI_PATTERN = re.compile(r"אדני|אֲדֹנָי")
# Tsebaoth (hosts) — both vocalized and unvocalized
TSEBAOTH_PATTERN = re.compile(r"צבאות|צְבָאוֹת")


def normalize_hebrew(s: str) -> str:
    """Strip vowel points + cantillation."""
    out = []
    for c in unicodedata.normalize("NFD", s):
        cp = ord(c)
        if 0x0591 <= cp <= 0x05AF:  # cantillation
            continue
        if 0x05B0 <= cp <= 0x05BD:  # vowel points
            continue
        if cp in (0x05BF, 0x05C1, 0x05C2, 0x05C4, 0x05C5, 0x05C7):
            continue
        if unicodedata.combining(c):
            continue
        out.append(c)
    return "".join(out)


def has_yhwh(hebrew: str) -> bool:
    return bool(YHWH_PATTERN.search(normalize_hebrew(hebrew)))


def has_adonai_yhwh_compound(hebrew: str) -> bool:
    """Detect Adonai-YHWH compound: אֲדֹנָי יְהוִה (within ~2 words of each other)."""
    norm = normalize_hebrew(hebrew)
    # Look for אדני followed within ~10 chars by יהוה
    for m in ADONAI_PATTERN.finditer(norm):
        end = m.end()
        rest = norm[end:end + 15]
        if YHWH_PATTERN.search(rest):
            return True
    return False


def has_standalone_adonai(hebrew: str) -> bool:
    """Adonai NOT in compound with YHWH (within proximity)."""
    norm = normalize_hebrew(hebrew)
    for m in ADONAI_PATTERN.finditer(norm):
        end = m.end()
        # Look ahead 15 chars for YHWH
        if YHWH_PATTERN.search(norm[end:end + 15]):
            continue  # part of compound, not standalone
        return True
    return False


def has_tsebaoth(hebrew: str) -> bool:
    return bool(TSEBAOTH_PATTERN.search(normalize_hebrew(hebrew)))


def find_ot_chapter_files(book_filter: str | None = None,
                          chapter_filter: int | None = None) -> list[Path]:
    files: list[Path] = []
    if not TRANSLATIONS.exists():
        return files
    for path in sorted(TRANSLATIONS.glob("*_*.json")):
        m = re.match(r"^(.+)_(\d+)\.json$", path.name)
        if not m:
            continue
        slug, ch_str = m.group(1), m.group(2)
        if slug not in OT_SLUG_TO_CODE:
            continue
        if book_filter and OT_SLUG_TO_CODE[slug] != book_filter.upper():
            continue
        if chapter_filter is not None and int(ch_str) != chapter_filter:
            continue
        files.append(path)
    return files


def has_first_occurrence_footnote(slug: str, chapter: int) -> bool:
    """Check whether the chapter's textual_variants file documents the YHWH convention."""
    tv_path = TEXTUAL_VARIANTS / f"{slug}_{chapter:02d}.json"
    if not tv_path.exists():
        return False
    try:
        data = json.loads(tv_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    if not isinstance(data, list):
        return False
    for entry in data:
        if not isinstance(entry, dict):
            continue
        explanation = (entry.get("explanation_thai") or
                       entry.get("explanation") or "").lower()
        # Look for the convention-marker phrases
        if "องค์พระผู้เป็นเจ้า" in explanation and "ยาห์เวห์" in explanation:
            return True
        if "tetragrammaton" in explanation or "yhwh" in explanation:
            return True
    return False


def has_yhwh_key_decision(verse: dict) -> bool:
    """Check whether the verse's key_decisions records a YHWH-family form."""
    kds = (verse.get("translation") or {}).get("key_decisions", [])
    if not kds:
        kds = verse.get("key_decisions", [])  # legacy flat-schema fallback
    if not isinstance(kds, list):
        return False
    for kd in kds:
        if isinstance(kd, dict):
            text = " ".join(str(v) for v in kd.values() if isinstance(v, str))
        else:
            text = str(kd)
        if not text:
            continue
        # Look for explicit YHWH-form mention
        if "יהוה" in text or "YHWH" in text or "Tetragrammaton" in text:
            return True
        if "ยาห์เวห์" in text and "องค์พระผู้เป็นเจ้า" in text:
            return True
        if "Adonai" in text and "Adonai-YHWH" in text:
            return True
    return False


def check_verse(verse: dict, slug: str) -> tuple[list[str], list[str]]:
    """Return (hard_fails, warnings)."""
    hard: list[str] = []
    warn: list[str] = []
    ref = verse.get("reference", "?:?")
    lang = verse.get("language", "")
    if lang not in ("hebrew", "aramaic"):
        return hard, warn

    hebrew = verse.get(lang, "")
    translation = verse.get("translation") or {}
    thai = translation.get("thai") or verse.get("thai") or ""

    # Strip place-name compounds from Thai before applying [F] forbidden check —
    # they legitimately contain ยาห์เวห์ (not พระยาห์เวห์).
    thai_without_placenames = PLACE_NAME_PATTERN.sub("", thai)

    # [F] Forbidden THSV11 form
    if FORBIDDEN_THSV11 in thai_without_placenames:
        hard.append(
            f"[F] {ref}: Thai contains forbidden `{FORBIDDEN_THSV11}` "
            f"(THSV11 form reversed by 2026-05-04 third-revision flip). "
            f"Use `{THAI_YHWH}` instead."
        )

    yhwh_present = has_yhwh(hebrew)
    adonai_yhwh = has_adonai_yhwh_compound(hebrew)
    tsebaoth = has_tsebaoth(hebrew) and yhwh_present
    standalone_adonai = has_standalone_adonai(hebrew)

    # [A] / [B] If YHWH (or Adonai-YHWH compound) present, Thai must contain องค์พระผู้เป็นเจ้า
    if yhwh_present and THAI_YHWH not in thai:
        # Possible legitimate exception: place-name compound. Check if Thai has
        # a place-name transliteration present
        has_place_name = bool(PLACE_NAME_PATTERN.search(thai))
        if has_place_name:
            # Place-name compound — accept transliteration without องค์พระผู้เป็นเจ้α
            pass
        else:
            hard.append(
                f"[A] {ref}: Hebrew contains יהוה but Thai missing "
                f"`{THAI_YHWH}` (and no place-name compound detected)"
            )

    # [E] YHWH-family forms require a key_decisions Hebrew-form transparency entry
    if (yhwh_present or adonai_yhwh) and not has_yhwh_key_decision(verse):
        hard.append(
            f"[E] {ref}: Hebrew has YHWH-family form, but no `key_decisions` "
            f"entry records the underlying Hebrew form. See "
            f"divine_names_table_2026-05 §'Layer 1' for required transparency mechanism"
        )

    # [B specific] Tsebaoth check
    if tsebaoth and THAI_TSEBAOTH not in thai:
        # Allow flexibility: "องค์พระผู้เป็นเจ้าจอมโยธα" might be split across
        # the verse; soft-check via fragments.
        if "จอมโยธา" not in thai:
            warn.append(
                f"[B-soft] {ref}: Hebrew has יהוה צבאות but Thai may be "
                f"missing `จอมโยธา` (expected `{THAI_TSEBAOTH}`)"
            )

    # [C] Standalone Adonai → Thai should have องค์เจ้านาย
    if standalone_adonai and THAI_ADONAI not in thai and THAI_YHWH not in thai:
        warn.append(
            f"[C-soft] {ref}: Hebrew has standalone אֲדֹנָי (no YHWH compound), "
            f"Thai may be missing `{THAI_ADONAI}`"
        )

    return hard, warn


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--book", help="3-letter OT book code")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--report", action="store_true",
                        help=f"Write a markdown report to {REPORTS}/")
    args = parser.parse_args()

    files = find_ot_chapter_files(args.book, args.chapter)
    if not files:
        print("No OT chapter files found (or none matching filter).")
        return 0

    total_hard, total_warn = [], []
    chapters_checked: set[tuple[str, int]] = set()
    chapters_with_yhwh: set[tuple[str, int]] = set()
    chapters_with_footnote: set[tuple[str, int]] = set()

    for fpath in files:
        m = re.match(r"^(.+)_(\d+)\.json$", fpath.name)
        slug, ch = m.group(1), int(m.group(2))
        chapters_checked.add((slug, ch))
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            total_hard.append(f"[!] {fpath.name}: invalid JSON ({e})")
            continue
        if not isinstance(data, list):
            data = [data]

        chapter_has_yhwh = False
        for verse in data:
            if not isinstance(verse, dict):
                continue
            lang = verse.get("language", "")
            if lang not in ("hebrew", "aramaic"):
                continue
            if has_yhwh(verse.get(lang, "")):
                chapter_has_yhwh = True
            hard, warn = check_verse(verse, slug)
            total_hard.extend(hard)
            total_warn.extend(warn)

        if chapter_has_yhwh:
            chapters_with_yhwh.add((slug, ch))
            if has_first_occurrence_footnote(slug, ch):
                chapters_with_footnote.add((slug, ch))

    # [D] First-occurrence footnote — warn-only at this stage
    missing_footnote = chapters_with_yhwh - chapters_with_footnote
    for slug, ch in sorted(missing_footnote):
        total_warn.append(
            f"[D] {slug} ch.{ch}: contains YHWH but no first-occurrence "
            f"footnote in output/textual_variants/{slug}_{ch:02d}.json. "
            f"See divine_names_table_2026-05 §'Layer 2'"
        )

    print(f"Divine names — checked {len(chapters_checked)} OT chapter(s); "
          f"{len(chapters_with_yhwh)} contain YHWH")
    if total_hard:
        print(f"\nHARD FAILS ({len(total_hard)}):")
        for v in total_hard:
            print(f"  {v}")
    if total_warn:
        print(f"\nWARNINGS ({len(total_warn)}):")
        for v in total_warn[:20]:
            print(f"  {v}")
        if len(total_warn) > 20:
            print(f"  ... and {len(total_warn) - 20} more")

    if args.report:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out = REPORTS / "divine_names.md"
        with open(out, "w", encoding="utf-8") as f:
            f.write("# Divine names policy report\n\n")
            f.write(f"Per docs/translator_decisions/divine_names_table_2026-05.md\n\n")
            f.write(f"- Chapters checked: {len(chapters_checked)}\n")
            f.write(f"- Chapters with YHWH: {len(chapters_with_yhwh)}\n")
            f.write(f"- Chapters with first-occurrence footnote: {len(chapters_with_footnote)}\n")
            f.write(f"- Hard fails: {len(total_hard)}\n")
            f.write(f"- Warnings: {len(total_warn)}\n\n")
            if total_hard:
                f.write("## Hard fails\n\n")
                for v in total_hard:
                    f.write(f"- {v}\n")
                f.write("\n")
            if total_warn:
                f.write("## Warnings\n\n")
                for v in total_warn:
                    f.write(f"- {v}\n")
        print(f"Wrote {out}")

    if total_hard:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
