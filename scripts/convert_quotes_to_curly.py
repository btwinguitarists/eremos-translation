#!/usr/bin/env python3
"""
One-shot conversion: project-wide quote-mark normalization to Thai curly quotes.

Why: the corpus drifted into three inconsistent quote conventions:
  - Matthew/Luke/John/Acts/1Timothy: « » outer, ‹ › nested (guillemets)
  - Mark: ' ' outer, " " nested (straight quotes — early chapters used '
    only; later chapters switched to " — internally inconsistent too)

This script unifies everything to Thai publishing convention:
  - Outer: " " (U+201C / U+201D — curly double quotes)
  - Nested: ' ' (U+2018 / U+2019 — curly single quotes)

Per-field strategy:
  - For Thai-language fields (translation.thai, thai_literal, thai_summary,
    key_decisions[].thai): apply both the guillemet replacement AND, for
    Mark, a stateful straight-to-curly conversion. (Thai script has no
    native apostrophes, so all ' / " in these fields are quote marks.)
  - For mixed-language fields (translation.notes, key_decisions[].rationale,
    key_decisions[].greek): only replace guillemets «»‹›. Leave ' and "
    untouched (they are real English apostrophes and quotes).
  - Source fields (greek, bsb_english, reference): never touched. SBLGNT
    and BSB are pristine source material.

Pre-existing balance issues (25 chapters with mismatched guillemets, plus
6 Mark chapters with odd-parity straight quotes) are preserved as-is —
they exist now in the original characters; they'll exist after in curly
characters. Fixing them is the scope of a follow-up PR.

The script is idempotent: re-running it on already-converted text is a
no-op (no « » ‹ › left to convert; no ' or " in Thai fields after first
pass except those that were already curly).

Usage:
  python3 scripts/convert_quotes_to_curly.py        # apply to JSONs + glossary + RULES + decision docs
  python3 scripts/convert_quotes_to_curly.py --dry  # show what would change without writing
"""
import argparse
import json
import re
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
GLOSSARY = ROOT / "glossary.json"
RULES = ROOT / "RULES.md"
DECISIONS_DIR = ROOT / "docs" / "translator_decisions"

# Guillemet replacements (mechanical, all books, all fields)
GUILLEMET_MAP = {
    "«": "“",  # "  curly open double
    "»": "”",  # "  curly close double
    "‹": "‘",  # '  curly open single
    "›": "’",  # '  curly close single
}

OPEN_DOUBLE = "“"   # "
CLOSE_DOUBLE = "”"  # "
OPEN_SINGLE = "‘"   # '
CLOSE_SINGLE = "’"  # '

THAI_FIELDS_IN_VERSE = ("thai", "thai_literal", "thai_summary")
THAI_FIELDS_IN_KD = ("thai",)
GUILLEMET_ONLY_FIELDS_IN_VERSE = ("notes",)
GUILLEMET_ONLY_FIELDS_IN_KD = ("rationale", "greek")

stats = Counter()


def replace_guillemets(text):
    """Mechanical 4-char replacement. Idempotent."""
    if not isinstance(text, str):
        return text
    n = sum(text.count(c) for c in GUILLEMET_MAP)
    if n == 0:
        return text
    for src, dst in GUILLEMET_MAP.items():
        text = text.replace(src, dst)
    return text


class QuoteStateMachine:
    """Stateful conversion of straight quotes to curly, per a configurable mapping.

    Mapping: {input_char: (open_curly, close_curly)}.

    For each occurrence of an input char, alternate between the open and close
    curly. Each char tracks its own state independently.

    Caller controls the lifetime of the state. For verse text (`thai` field)
    where speech can span multiple verses, the SAME instance is used across
    all verses of a chapter. For self-contained Thai fields (thai_summary,
    thai_literal, key_decisions.thai), a fresh instance is used per call.

    If the original quote stream is unbalanced over the span, the output
    preserves the same character count — an unmatched open remains a curly
    OPEN with no matching close.
    """
    def __init__(self, mapping):
        self.mapping = mapping
        self.next_open = {ch: True for ch in mapping}

    def convert(self, text):
        if not isinstance(text, str):
            return text
        out = []
        for ch in text:
            if ch in self.mapping:
                open_c, close_c = self.mapping[ch]
                out.append(open_c if self.next_open[ch] else close_c)
                self.next_open[ch] = not self.next_open[ch]
            else:
                out.append(ch)
        return "".join(out)


# Mapping for Thai-summary / thai_literal / key_decisions.thai fields and
# for non-Mark thai-verse fields:
# - " is outer/term-mention level → curly double
# - ' is nested level → curly single
# (For non-Mark thai-verse fields, the actual outer is «» which is already
#  guillemet-replaced; any straight " or ' here is anomalous, treated as
#  the level our universal rule prescribes.)
COMMENTARY_MAPPING = {
    '"': (OPEN_DOUBLE, CLOSE_DOUBLE),
    "'": (OPEN_SINGLE, CLOSE_SINGLE),
}


def detect_mark_chapter_mapping(verses):
    """For a Mark chapter, detect which character is outer vs nested.

    Mark's convention drifted: chapters 1-7 use ' as outer + " as nested,
    chapters 8+ use " as outer + ' as nested. We detect per-chapter by
    counting occurrences in the `thai` field — whichever has more is outer.
    Outer maps to curly double; the other to curly single.

    Returns the mapping dict for the QuoteStateMachine.
    """
    s = sum(((v.get('translation') or {}).get('thai') or '').count("'") for v in verses)
    d = sum(((v.get('translation') or {}).get('thai') or '').count('"') for v in verses)
    if s >= d:
        # ' is outer (Mark 1-7 pattern)
        return {
            "'": (OPEN_DOUBLE, CLOSE_DOUBLE),
            '"': (OPEN_SINGLE, CLOSE_SINGLE),
        }
    else:
        # " is outer (Mark 8+ pattern)
        return {
            '"': (OPEN_DOUBLE, CLOSE_DOUBLE),
            "'": (OPEN_SINGLE, CLOSE_SINGLE),
        }


def process_thai_field(text, sm=None, mapping=None):
    """Apply guillemet replacement + stateful straight-quote conversion.

    If `sm` is provided, use that state machine (preserves state across calls
    — used for `thai` field where speech spans verses within a chapter).
    Otherwise build a one-off state machine using `mapping` (default:
    COMMENTARY_MAPPING).

    Thai script has no native apostrophes, so any ' or " in a Thai-language
    field is treated as a quote mark.
    """
    text = replace_guillemets(text)
    if sm is None:
        sm = QuoteStateMachine(mapping or COMMENTARY_MAPPING)
    return sm.convert(text)


def process_translation_json(path, dry):
    data = json.loads(path.read_text())
    changed = False
    # Per-chapter state machine for verse text. Speech can span verses in a
    # chapter, so the open/close alternation must be continuous across the
    # whole chapter for the `thai` field.
    is_mark = path.name.startswith("mark_")
    if is_mark:
        chapter_mapping = detect_mark_chapter_mapping(data)
    else:
        # For non-Mark chapters, outer is «» (already guillemet-replaced).
        # Any straight quotes are anomalies treated by COMMENTARY_MAPPING:
        # " → outer-style, ' → nested-style.
        chapter_mapping = COMMENTARY_MAPPING
    chapter_sm = QuoteStateMachine(chapter_mapping)

    for v in data:
        # Special case: luke_13 v5 has a stray » in key_decisions.greek
        if path.stem == "luke_13" and v.get("verse") == 5:
            for kd in (v.get("translation") or {}).get("key_decisions") or []:
                g = kd.get("greek") or ""
                if "»" in g:
                    new_g = g.replace("»", "")
                    if new_g != g:
                        kd["greek"] = new_g
                        stats["fix_stray_»_luke_13_v5"] += 1
                        changed = True

        tr = v.get("translation") or {}
        # `thai` field uses per-chapter state (multi-verse speech).
        old = tr.get("thai")
        if isinstance(old, str):
            new = process_thai_field(old, sm=chapter_sm)
            if new != old:
                tr["thai"] = new
                stats["changed.thai"] += 1
                changed = True
        # `thai_literal` and `thai_summary` are per-verse self-contained.
        for fld in ("thai_literal", "thai_summary"):
            old = tr.get(fld)
            if not isinstance(old, str):
                continue
            new = process_thai_field(old)  # fresh state machine per call
            if new != old:
                tr[fld] = new
                stats[f"changed.{fld}"] += 1
                changed = True
        for fld in GUILLEMET_ONLY_FIELDS_IN_VERSE:
            old = tr.get(fld)
            if not isinstance(old, str):
                continue
            new = replace_guillemets(old)
            if new != old:
                tr[fld] = new
                stats[f"changed.{fld}"] += 1
                changed = True
        for kd in tr.get("key_decisions") or []:
            for fld in THAI_FIELDS_IN_KD:
                old = kd.get(fld)
                if not isinstance(old, str):
                    continue
                new = process_thai_field(old)  # per-call state for KD entries
                if new != old:
                    kd[fld] = new
                    stats[f"changed.kd.{fld}"] += 1
                    changed = True
            for fld in GUILLEMET_ONLY_FIELDS_IN_KD:
                old = kd.get(fld)
                if not isinstance(old, str):
                    continue
                new = replace_guillemets(old)
                if new != old:
                    kd[fld] = new
                    stats[f"changed.kd.{fld}"] += 1
                    changed = True

    if changed and not dry:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        stats["files_modified"] += 1
    elif changed:
        stats["files_would_modify"] += 1
    return changed


def process_glossary(dry):
    if not GLOSSARY.is_file():
        return
    text = GLOSSARY.read_text()
    new = replace_guillemets(text)
    if new != text:
        if not dry:
            GLOSSARY.write_text(new)
        stats["glossary_modified"] = 1


def process_rules(dry):
    """RULES.md may not have any guillemets but check anyway."""
    text = RULES.read_text()
    new = replace_guillemets(text)
    if new != text:
        if not dry:
            RULES.write_text(new)
        stats["rules_modified"] = 1


def process_decision_docs(dry):
    """Per audit: 3 pairs of «» in docs/translator_decisions/."""
    if not DECISIONS_DIR.is_dir():
        return
    for f in DECISIONS_DIR.glob("*.md"):
        text = f.read_text()
        new = replace_guillemets(text)
        if new != text:
            if not dry:
                f.write_text(new)
            stats[f"decision_doc_modified.{f.name}"] = 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry", action="store_true", help="show changes without writing")
    args = parser.parse_args()

    # Translation JSONs
    for p in sorted(TRANSLATIONS.glob("*.json")):
        if "demo" in p.name:
            continue
        process_translation_json(p, args.dry)

    process_glossary(args.dry)
    process_rules(args.dry)
    process_decision_docs(args.dry)

    print(f"\n{'DRY RUN' if args.dry else 'APPLIED'}:")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
