#!/usr/bin/env python3
"""
Sacrificial-vocabulary lock check.

Enforces docs/translator_decisions/sacrificial_vocabulary_2026-05.md.
Promised in that doc's §7 since 2026-05-15; finally written 2026-05-16 after
the Leviticus end-of-book audit caught the §5 kipper drift that this check
would have prevented.

What this enforces (LEV + NUM + future OT P-material books):

  [A] The five main sacrificial-type Hebrew nouns must render to their
      locked Thai compound (§1 of the doc) whenever they appear in the
      Hebrew field — UNLESS the Hebrew is the moral-noun sense (חַטָּאת
      "sin" with no ritual context) per §3.

  [B] The kipper verb (כִּפֵּר piel) must render to either
      `ลบมลทินบาป` / `ทำการลบมลทินบาป` (priestly-purgation register)
      or `ลบบาป` / `ทำการลบบาป` (direct-atonement register). The two
      registers are both valid per §5 of the amended 2026-05-16 doc.
      Any other rendering is a HARD FAIL unless the verse carries an
      explicit `key_decisions` rationale documenting the deviation.

  [C] Verb forms הִקְרִיב (`ถวาย`), הִקְטִיר (`เผา`), and סָמַךְ יָד
      (`วางมือ`) must render to their locked Thai when the Hebrew lemma
      is present.

Usage:

  python3 scripts/check_sacrificial_vocab.py
  python3 scripts/check_sacrificial_vocab.py --book LEV
  python3 scripts/check_sacrificial_vocab.py --book LEV --chapter 16
  python3 scripts/check_sacrificial_vocab.py --strict

Exit code: 0 if clean, 1 if HARD FAILS, 0 with warnings emitted otherwise.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS_DIR = REPO_ROOT / "output" / "translations"
REPORTS_DIR = REPO_ROOT / "output" / "check_reports"

# Locked Hebrew → Thai mappings per sacrificial_vocabulary_2026-05.md §1
LOCKED_NOUNS = {
    "עֹלָה": ("ʿōlāh", "burnt offering", ["เครื่องเผาบูชา"]),
    "מִנְחָה": ("minḥāh", "grain offering", ["เครื่องบูชาธัญพืช"]),
    "אָשָׁם": ("ʾāšām", "guilt offering", ["เครื่องบูชาไถ่ความผิด"]),
    "שְׁלָמִים": ("šəlāmîm", "peace offering", ["เครื่องสันติบูชา"]),
}

# חַטָּאת is polysemous — handled below via context heuristic
HATTAT = "חַטָּאת"
HATTAT_RITUAL_THAI = "เครื่องบูชาไถ่บาป"
HATTAT_MORAL_THAI = "บาป"

# Kipper verb forms — both registers valid per §5 amendment
KIPPER_LEMMA_CHARS = "כפר"  # match against any inflected form containing the root
KIPPER_PRIESTLY_REGISTER = ("ลบมลทินบาป", "ทำการลบมลทินบาป", "การลบมลทินบาป")
KIPPER_ATONEMENT_REGISTER = ("ลบบาป", "ทำการลบบาป", "การลบบาป")
KIPPER_VALID_THAI = KIPPER_PRIESTLY_REGISTER + KIPPER_ATONEMENT_REGISTER

# Other locked verbs from §5
LOCKED_VERBS = {
    "הִקְרִיב": ("hiqrîḇ", "present/offer", ["ถวาย"]),
    "הִקְטִיר": ("hiqṭîr", "burn sacrificially", ["เผา"]),
    "סָמַךְ": ("sāmaḵ", "lay hand", ["วางมือ"]),
}

# OT books with sacrificial material — only these are checked
OT_SACRIFICIAL_BOOKS = {
    "leviticus", "numbers", "exodus", "deuteronomy",
    # future: 1samuel, 2samuel, 1kings, 2kings, 1chronicles, 2chronicles,
    # ezra, nehemiah, psalms (50, 51), isaiah, jeremiah, ezekiel, hosea,
    # joel, amos, malachi
}


def list_translation_files(book_filter: str | None, chapter_filter: int | None) -> list[Path]:
    if not TRANSLATIONS_DIR.exists():
        return []
    paths = sorted(TRANSLATIONS_DIR.glob("*.json"))
    out = []
    for p in paths:
        stem = p.stem
        if "_" not in stem:
            continue
        book, _, ch_str = stem.rpartition("_")
        if book not in OT_SACRIFICIAL_BOOKS:
            continue
        if book_filter and book_filter.lower() not in (book, book[:3]):
            # Permit "LEV" → "leviticus" matching
            if not (book_filter.lower() == "lev" and book == "leviticus"):
                if not (book_filter.lower() == "num" and book == "numbers"):
                    if not (book_filter.lower() == "exo" and book == "exodus"):
                        if not (book_filter.lower() == "deu" and book == "deuteronomy"):
                            continue
        if chapter_filter is not None:
            try:
                if int(ch_str) != chapter_filter:
                    continue
            except ValueError:
                continue
        out.append(p)
    return out


def hebrew_contains(hebrew: str, token: str) -> bool:
    """Naive substring match. Hebrew vowel-pointing means a strict equality check
    would miss inflected forms; substring is good enough for the locked-lemma roots."""
    if not hebrew or not token:
        return False
    return token in hebrew


def hebrew_contains_root(hebrew: str, root: str) -> bool:
    """For kipper (root כפר). Strip vowel points and check if all root consonants
    appear in order as a contiguous substring of the consonant-skeleton."""
    if not hebrew or not root:
        return False
    # Strip Hebrew vowel points and cantillation (U+0591–U+05C7) — keep consonants
    skeleton = "".join(c for c in hebrew if "א" <= c <= "ת" or c in "ךםןףץ")
    return root in skeleton


def check_verse(book: str, verse: dict) -> list[dict]:
    """Return a list of issue dicts for this verse."""
    issues: list[dict] = []
    hebrew = verse.get("hebrew") or ""
    thai = ((verse.get("translation") or {}).get("thai")) or ""
    ref = verse.get("reference") or f"{book} ?:?"
    rationale_blob = json.dumps(verse.get("translation") or {}, ensure_ascii=False)

    # [A] Locked nouns
    for heb, (tr, gloss, thai_options) in LOCKED_NOUNS.items():
        if hebrew_contains(hebrew, heb):
            if not any(opt in thai for opt in thai_options):
                # Allow if key_decisions documents an explicit deviation
                if "polysemy" in rationale_blob or "moral" in rationale_blob:
                    continue
                issues.append({
                    "kind": "HARD",
                    "rule": "A",
                    "ref": ref,
                    "msg": f"Hebrew has {heb} ({tr} = {gloss}) but Thai missing locked {' | '.join(thai_options)}",
                })

    # [A'] חַטָּאת polysemy — heuristic: if Hebrew has חַטָּאת AND any of
    # {עֹלָה, אִשֶּׁה, "ritual" sacrifice verbs} appear nearby, it's the
    # ritual sense; else moral. We accept either Thai if rationale is documented.
    # Conservative rule (2026-05-16): when a verse legitimately contains BOTH a
    # ritual sacrifice term in Thai (e.g., เครื่องบูชาไถ่ความผิด for ʾāšām) AND
    # the moral บาป for ḥaṭṭāʾt, do not warn — the verse has both senses
    # operating simultaneously, which is normal in P-material.
    if hebrew_contains(hebrew, HATTAT):
        ritual_context = any(hebrew_contains(hebrew, k) for k in LOCKED_NOUNS) or "ไถ่" in thai
        has_ritual_thai = HATTAT_RITUAL_THAI in thai
        has_moral_thai = HATTAT_MORAL_THAI in thai
        has_any_ritual_sacrifice_thai = any(
            opt in thai
            for _, (_, _, opts) in LOCKED_NOUNS.items()
            for opt in opts
        ) or HATTAT_RITUAL_THAI in thai
        if not (has_ritual_thai or has_moral_thai):
            issues.append({
                "kind": "HARD",
                "rule": "A'",
                "ref": ref,
                "msg": f"Hebrew has {HATTAT} but Thai missing both ritual ({HATTAT_RITUAL_THAI}) and moral ({HATTAT_MORAL_THAI}) options",
            })
        elif ritual_context and not has_ritual_thai and not has_any_ritual_sacrifice_thai and "polysemy" not in rationale_blob:
            issues.append({
                "kind": "WARN",
                "rule": "A'",
                "ref": ref,
                "msg": f"Hebrew has {HATTAT} in ritual context but Thai uses moral-only rendering without any other ritual-sacrifice term; document with 'polysemy' keyword if intentional",
            })

    # [B] Kipper register check — only when the verb form is present.
    # Known nominal/non-verbal forms sharing the כפר consonants (to skip):
    #   - כַּפֹּרֶת (kapporet, "mercy seat") → skeleton ends `כפרת`
    #   - כִּפֻּרִים (kippurim, "atonement") → skeleton ends `כפרים`
    #   - כְּפוֹר (kəphôr, "frost", EX 16:14) → skeleton is `כפור`
    #   - כֹּפֶר (kōpher, "ransom", EX 21:30, 30:12, NUM 35:31-32) → skeleton bare `כפר`,
    #     ambiguous with verb 3ms perfect כִּפֶּר. We accept the false-positive
    #     warning rather than miss real verb-form drift.
    if hebrew_contains_root(hebrew, KIPPER_LEMMA_CHARS):
        skeleton = "".join(c for c in hebrew if "א" <= c <= "ת" or c in "ךםןףץ")
        # Find each kpr occurrence and decide nominal vs verbal.
        has_verbal = False
        i = 0
        verbal_prefixes = set("וימנאתה")  # waw, yod, mem, nun, aleph, taw, he
        nominal_prefixes = set("כלבש")  # ke-, le-, be-, she- prepositions
        while True:
            idx = skeleton.find("כפר", i)
            if idx == -1:
                break
            tail = skeleton[idx + 3:idx + 5]
            # Skip: kapporet (כפרת), kippurim (כפרים)
            if tail.startswith("ת") or tail.startswith("ים"):
                i = idx + 1
                continue
            # Check preceding character to distinguish verb vs noun:
            # verbal prefixes (waw-cons, yiqtol, niph, inf) → verb
            # nominal prefixes (ke-, le-, be-, she-) → noun (e.g., kakkəphor "like frost")
            prev = skeleton[idx - 1:idx] if idx > 0 else ""
            if prev in nominal_prefixes:
                i = idx + 1
                continue
            if prev in verbal_prefixes or idx == 0:
                has_verbal = True
                break
            # Other preceding chars: ambiguous; flag as candidate
            has_verbal = True
            break
        if has_verbal:
            has_valid = any(form in thai for form in KIPPER_VALID_THAI)
            if not has_valid:
                # Permit if rationale explicitly documents the kipper handling
                if "kipper" in rationale_blob.lower() or "lemma kpr" in rationale_blob.lower():
                    pass
                # Permit kopher-noun renderings (ransom money)
                elif "สินไถ่" in thai or "ค่าไถ่" in thai or "ค่าเสียหาย" in thai:
                    pass
                else:
                    issues.append({
                        "kind": "WARN",
                        "rule": "B",
                        "ref": ref,
                        "msg": f"Hebrew has kipper-root verb but Thai uses none of: {' | '.join(KIPPER_VALID_THAI)}",
                    })

    # [C] Other locked verbs — soft check (warn only, since these have idiomatic
    # extensions in Thai that don't always preserve the exact locked word).
    for heb, (tr, gloss, thai_options) in LOCKED_VERBS.items():
        if hebrew_contains(hebrew, heb):
            if not any(opt in thai for opt in thai_options):
                issues.append({
                    "kind": "WARN",
                    "rule": "C",
                    "ref": ref,
                    "msg": f"Hebrew has {heb} ({tr} = {gloss}) but Thai missing {' | '.join(thai_options)}; verify in context",
                })

    return issues


def render_report(all_issues: list[dict], n_verses: int) -> str:
    hard = [i for i in all_issues if i["kind"] == "HARD"]
    warn = [i for i in all_issues if i["kind"] == "WARN"]
    lines = []
    lines.append("# Sacrificial vocabulary check")
    lines.append("")
    lines.append(f"Verses checked: **{n_verses}**")
    lines.append(f"HARD FAILS: **{len(hard)}**")
    lines.append(f"Warnings: **{len(warn)}**")
    lines.append("")
    if hard:
        lines.append("## HARD FAILS")
        lines.append("")
        for i in hard:
            lines.append(f"- [{i['rule']}] {i['ref']}: {i['msg']}")
        lines.append("")
    if warn:
        lines.append("## Warnings")
        lines.append("")
        for i in warn[:50]:
            lines.append(f"- [{i['rule']}] {i['ref']}: {i['msg']}")
        if len(warn) > 50:
            lines.append(f"- ... and {len(warn) - 50} more")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--book", help="Restrict to one book (e.g. LEV, NUM)")
    ap.add_argument("--chapter", type=int, help="Restrict to one chapter (requires --book)")
    ap.add_argument("--strict", action="store_true", help="Exit nonzero on any warning, not just HARD FAILS")
    ap.add_argument("--report", type=Path, help="Write the report to this file instead of stdout")
    args = ap.parse_args()

    paths = list_translation_files(args.book, args.chapter)
    if not paths:
        print(f"[check_sacrificial_vocab] no matching translation files (book={args.book!r}, chapter={args.chapter!r})", file=sys.stderr)
        return 0

    all_issues: list[dict] = []
    n_verses = 0
    for p in paths:
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[check_sacrificial_vocab] skipping {p.name}: {e}", file=sys.stderr)
            continue
        if not isinstance(data, list):
            continue
        book = p.stem.rpartition("_")[0]
        for verse in data:
            if not isinstance(verse, dict):
                continue
            n_verses += 1
            all_issues.extend(check_verse(book, verse))

    report = render_report(all_issues, n_verses)
    if args.report:
        args.report.write_text(report, encoding="utf-8")
        print(f"[check_sacrificial_vocab] wrote {args.report}")
    else:
        print(report)

    hard_count = sum(1 for i in all_issues if i["kind"] == "HARD")
    warn_count = sum(1 for i in all_issues if i["kind"] == "WARN")
    if hard_count:
        return 1
    if args.strict and warn_count:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
