#!/usr/bin/env python3
"""
One-time audit: find every verse in our translated corpus where SBLGNT's main
text omits words that mainstream traditions (NA28 / BSB / NIV / ESV / THSV)
include — i.e. inclusion variants where readers will notice the omission.

These are the candidates for the single-bracket convention adopted 2026-04-18:
render the words in `[...]` in the Thai field so readers see them while
brackets honestly signal "this reading is contested in the manuscript tradition."

NOT in scope:
  - Word-choice variants (we picked word A, mainstream picked word B). These
    are handled by `thai_summary` explanation, not by brackets.
  - Orthographic / minor variants. No reader-trust issue.
  - Mark 16:9-20 longer ending — already wrapped in ⟦double-brackets⟧ as a
    larger-block stylistic distinction; keeps that convention.

Usage:
  python3 scripts/audit_inclusion_variants.py
  python3 scripts/audit_inclusion_variants.py --book mark
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"

# Phrases in `notes` (and key_decision rationales) that strongly suggest an
# INCLUSION variant — SBLGNT omits something mainstream traditions include.
INCLUSION_OMIT_PATTERNS = [
    r"SBLGNT omits",
    r"SBLGNT/NA28 omit",
    r"shorter reading",
    r"shorter SBLGNT reading",
    r"shorter\s+(?:SBLGNT\s+)?(?:Alexandrian\s+)?reading\s+is\s+almost certainly original",
    r"omit(?:s|ted) per SBLGNT",
    r"SBLGNT\s+(?:critical\s+text\s+)?(?:and\s+NA28\s+)?omit",
    r"omitted in\s+SBLGNT",
    r"following SBLGNT.{0,40}(?:omit|shorter)",
    r"some\s+(?:Byzantine\s+)?(?:MSS|witnesses|manuscripts)\s+(?:add|insert|include)",
    r"Byzantine.{0,40}(?:add|insert|include)",
    r"(?:variant|MSS|witnesses)\s+(?:add|insert)\s+",
    r"longer reading.{0,80}(?:add|insert|include|expand|harmoniz)",
]

INCLUSION_RE = re.compile("|".join(INCLUSION_OMIT_PATTERNS), re.IGNORECASE)

# Text in notes that suggests this is a WORD-CHOICE variant rather than
# inclusion (so we should EXCLUDE from the candidate list — brackets don't
# apply, thai_summary explanation handles it).
WORD_CHOICE_HINTS = [
    r"\bvs\.?\s+",
    r"harder reading",
    r"lectio difficilior",
    r"different word",
    r"alternate (?:reading|word|spelling)",
]
WORD_CHOICE_RE = re.compile("|".join(WORD_CHOICE_HINTS), re.IGNORECASE)


def scan_chapter(chapter_file: Path) -> list[dict]:
    verses = json.loads(chapter_file.read_text(encoding="utf-8"))
    candidates = []
    for v in verses:
        trans = v.get("translation") or {}
        notes = trans.get("notes") or ""
        rats = " ".join(
            (d.get("rationale") or "") for d in trans.get("key_decisions", []) or []
        )
        combined = notes + "\n" + rats

        # Must mention an inclusion-omit pattern to be a candidate
        inclusion_hits = INCLUSION_RE.findall(combined)
        if not inclusion_hits:
            continue

        # Filter: if it's primarily a word-choice variant, skip
        word_choice_hits = WORD_CHOICE_RE.findall(combined)
        # Heuristic: word-choice signals outweighing inclusion signals = skip
        is_word_choice = len(word_choice_hits) > len(inclusion_hits)
        if is_word_choice:
            continue

        # Skip Mark 16:9-20 (already double-bracketed by separate convention)
        if v["reference"].startswith("Mark 16:") and 9 <= v["verse"] <= 20:
            continue

        candidates.append({
            "ref": v["reference"],
            "thai": trans.get("thai", ""),
            "notes_snippet": notes[:400],
            "inclusion_hits": list(set(h.lower() for h in inclusion_hits))[:3],
        })
    return candidates


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", help="Book slug (mark, matthew, 1timothy). If omitted, scan all.")
    args = parser.parse_args()

    if args.book:
        files = sorted(TRANSLATIONS.glob(f"{args.book.lower()}_*.json"))
        # filter out demo files
        files = [f for f in files if "_demo" not in f.name]
    else:
        files = [
            f for f in sorted(TRANSLATIONS.glob("*.json"))
            if "_demo" not in f.name
        ]

    all_candidates = []
    for f in files:
        all_candidates.extend(scan_chapter(f))

    print(f"# Inclusion-variant candidate audit\n")
    print(f"Scanned {len(files)} chapter files.\n")
    print(f"Found **{len(all_candidates)}** candidate verses where SBLGNT's main text "
          f"appears to omit words that mainstream traditions include.\n")

    if not all_candidates:
        print("(No candidates found.)")
        return 0

    print("Per-verse detail:\n")
    for c in all_candidates:
        print(f"## {c['ref']}\n")
        print(f"**Current Thai**: `{c['thai']}`\n")
        print(f"**Inclusion signals matched**: {', '.join(repr(h) for h in c['inclusion_hits'])}\n")
        print(f"**Notes excerpt** (first 400 chars):")
        print(f"> {c['notes_snippet']}\n")
        print()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
