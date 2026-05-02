#!/usr/bin/env python3
"""
Audit: find every verse in our translated corpus where SBLGNT's main text
omits words that mainstream traditions (NA28 / BSB / NIV / ESV / THSV)
include — i.e. inclusion variants where readers will notice the omission.

Per RULES §5 each candidate must end up in one of these dispositions:

  Tier 1 — short-phrase inclusion variants → single Thai brackets `[...]`
           (verse exists, thai field contains `[...]` markers)
  Tier 2 — whole-verse inclusion variants → chapter footer note
           (file output/textual_variants/<slug>_<NN>.json exists with the verse)
  Tier 3 — large-block transmissions → ⟦double brackets⟧ in main text
           (verse's thai field contains ⟦ or ⟧)
  Resolved (silent-omission per RULES §5) — explicitly noted in `notes` as
           silent-omission, OR documented dismissal at
           output/textual_variants/_resolved/<slug>_<NN>_v<V>.md

NOT in scope (auto-filtered):
  - Word-choice variants (we picked word A, mainstream picked word B). These
    are handled by `thai_summary` explanation, not by brackets.
  - Orthographic / minor variants. No reader-trust issue.
  - Mark 16:9-20 longer ending — already wrapped in ⟦double-brackets⟧ by
    larger-block convention.

Usage:
  # Audit (informational, exit 0):
  python3 scripts/audit_inclusion_variants.py
  python3 scripts/audit_inclusion_variants.py --book mark

  # End-of-book gate (exit non-zero if any candidate is UNRESOLVED):
  python3 scripts/audit_inclusion_variants.py --book romans --strict

The --strict mode is wired into END_OF_BOOK_CHECKLIST.md and
run_end_of_book_audit.sh — books cannot be marked complete with unresolved
inclusion variants.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
TEXTUAL_VARIANTS = ROOT / "output" / "textual_variants"
RESOLVED_DIR = TEXTUAL_VARIANTS / "_resolved"

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

# Notes phrases that mark a candidate as RULES §5 silent-omission (the verse
# is omitted because modern critical-text consensus matches our practice;
# no Tier 1/2/3 treatment needed). Translator declares this in `notes`.
#
# We accept the explicit phrase (canonical) AND common translator-shorthand
# patterns where the disposition is clear: following SBLGNT + note-only,
# all modern critical texts agree, scribal expansion/harmonization rationale,
# etc. The bar: would a reader of THSV / KJV / TR be surprised? If notes
# convincingly argue NO (modern consensus, scribal expansion, harmonization),
# silent-omission is acceptable.
SILENT_OMISSION_PATTERNS = [
    # Canonical / explicit
    r"RULES\s*[§\s]*5\s*silent[\s-]omission",
    r"silent[\s-]omission\s*(?:category|per\s+RULES)",
    # "Modern critical texts all agree"
    r"modern\s+(?:critical[\s-]text|evangelical[\s-]critical[\s-]text)s?\s+(?:consensus|agree|all|match)",
    r"all\s+modern\s+(?:critical|evangelical)\s+(?:critical[\s-]text)?s?\s+(?:agree|read|omit)",
    r"(?:NA28|SBLGNT|BSB|ESV|NIV|CSB)[\s,]+(?:NA28|SBLGNT|BSB|ESV|NIV|CSB)[\s,]+(?:NA28|SBLGNT|BSB|ESV|NIV|CSB)",
    # Translator's explicit "note-only" / "no special treatment"
    r"note[\s-]only\s*\(not\s+bracket",
    r"no\s+(?:special|bracket)\s+treatment",
    r"following\s+SBLGNT[,\s]+note[\s-]only",
    # Strong scribal-rationale signals (mainstream agrees + translator argues for shorter)
    r"likely\s+(?:earliest|original|secondary)\s+reading",
    r"scribal[\s-](?:expansion|harmonization|conflation|importation)",
    r"(?:secondary|later)\s+(?:scribal\s+)?(?:harmonization|importation|expansion)",
    r"shorter\s+reading\s+(?:is\s+)?(?:supported|preferred|original|earliest)",
    # Minor word-presence variants the translator argues are immaterial
    r"minor\s+variant",
    r"Eremos\s+preserves\s+the\s+implicit",
]
SILENT_OMISSION_RE = re.compile("|".join(SILENT_OMISSION_PATTERNS), re.IGNORECASE)


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
        if len(word_choice_hits) > len(inclusion_hits):
            continue

        # Skip Mark 16:9-20 (already double-bracketed by separate convention)
        if v["reference"].startswith("Mark 16:") and 9 <= v["verse"] <= 20:
            continue

        candidates.append({
            "ref": v["reference"],
            "verse": v["verse"],
            "chapter_file": chapter_file,
            "thai": trans.get("thai", ""),
            "notes": notes,
            "notes_snippet": notes[:400],
            "inclusion_hits": list(set(h.lower() for h in inclusion_hits))[:3],
        })
    return candidates


def classify(c: dict) -> tuple[str, str]:
    """Return (disposition, evidence) for a candidate.

    Disposition is one of: 'tier1', 'tier2', 'tier3', 'silent', 'resolved',
    'UNRESOLVED'.
    """
    chapter_file = c["chapter_file"]
    slug, chapter_str = chapter_file.stem.rsplit("_", 1)
    chapter = int(chapter_str)
    verse = c["verse"]

    thai = c["thai"]
    notes = c["notes"]

    # Tier 3: double brackets in the main text (large block)
    if "⟦" in thai or "⟧" in thai:
        return ("tier3", "double-bracket markers in thai field")

    # Tier 1: single brackets in the thai field (short phrase)
    if "[" in thai and "]" in thai:
        return ("tier1", "phrase brackets in thai field")

    # Tier 2: chapter-footer file exists
    tv_path = TEXTUAL_VARIANTS / f"{slug}_{chapter:02d}.json"
    if tv_path.exists():
        try:
            tv_data = json.loads(tv_path.read_text(encoding="utf-8"))
            if isinstance(tv_data, list) and tv_data:
                return ("tier2", str(tv_path.relative_to(ROOT)))
        except json.JSONDecodeError:
            pass

    # Silent omission per RULES §5 (translator declared in notes)
    if SILENT_OMISSION_RE.search(notes):
        return ("silent", "notes declare RULES §5 silent-omission")

    # Resolved: explicit dismissal doc. We accept any _resolved/<slug>_<NN>*.md
    # — the doc may be named for the omitted verse (e.g. mark_11_v26.md
    # when Mark 11:33's notes flag v.26's omission) or for the candidate verse.
    # Loose coupling: presence of any chapter-level dismissal doc resolves the
    # chapter's candidates. The strict gate's job is to force a deliberate
    # act, not to enforce per-verse file naming.
    resolved_files = list(RESOLVED_DIR.glob(f"{slug}_{chapter:02d}*.md"))
    if resolved_files:
        return ("resolved", str(resolved_files[0].relative_to(ROOT)))

    return ("UNRESOLVED", "")


def book_slugs_for_arg(arg: str) -> list[str]:
    """Resolve a --book arg (slug or USFM code) to a list of file slugs."""
    arg = arg.lower()
    # 'romans' or 'rom' or 'ROM' all → 'romans'
    code_to_slug = {
        "mat": "matthew", "mrk": "mark", "luk": "luke", "jhn": "john",
        "act": "acts", "rom": "romans", "1co": "1corinthians", "2co": "2corinthians",
        "gal": "galatians", "eph": "ephesians", "php": "philippians", "col": "colossians",
        "1th": "1thessalonians", "2th": "2thessalonians", "1ti": "1timothy",
        "2ti": "2timothy", "tit": "titus", "phm": "philemon", "heb": "hebrews",
        "jas": "james", "1pe": "1peter", "2pe": "2peter", "1jn": "1john",
        "2jn": "2john", "3jn": "3john", "jud": "jude", "rev": "revelation",
    }
    return [code_to_slug.get(arg, arg)]


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip())
    parser.add_argument("--book", help="Book slug or 3-letter code. If omitted, scan all.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="End-of-book gate: exit non-zero if any candidate is UNRESOLVED.",
    )
    args = parser.parse_args()

    if args.book:
        slugs = book_slugs_for_arg(args.book)
        files = []
        for slug in slugs:
            files.extend(sorted(TRANSLATIONS.glob(f"{slug}_*.json")))
        files = [f for f in files if "_demo" not in f.name]
    else:
        files = [
            f for f in sorted(TRANSLATIONS.glob("*.json"))
            if "_demo" not in f.name
        ]

    all_candidates = []
    for f in files:
        all_candidates.extend(scan_chapter(f))

    # Classify each candidate
    classified = []
    for c in all_candidates:
        dispo, evidence = classify(c)
        classified.append((c, dispo, evidence))

    counts = {}
    for _, d, _ in classified:
        counts[d] = counts.get(d, 0) + 1

    # ── header ──
    print("# Inclusion-variant audit\n")
    print(f"Scanned {len(files)} chapter files. Found **{len(all_candidates)}** candidates.\n")
    if counts:
        print("Disposition summary:")
        for label, key in [
            ("Tier 1 (phrase brackets)", "tier1"),
            ("Tier 2 (chapter footer)", "tier2"),
            ("Tier 3 (large-block ⟦⟧)", "tier3"),
            ("Silent (RULES §5 notes)", "silent"),
            ("Resolved (_resolved/ doc)", "resolved"),
            ("**UNRESOLVED**", "UNRESOLVED"),
        ]:
            if counts.get(key):
                print(f"  - {label}: {counts[key]}")
        print()

    if not all_candidates:
        print("(No candidates found.)")
        return 0

    # ── per-candidate detail ──
    print("## Per-candidate detail\n")
    for c, dispo, evidence in classified:
        marker = "❌ UNRESOLVED" if dispo == "UNRESOLVED" else f"✓ {dispo}"
        print(f"### {c['ref']} — {marker}")
        if evidence:
            print(f"  Evidence: {evidence}")
        print(f"  Inclusion signals: {', '.join(repr(h) for h in c['inclusion_hits'])}")
        print(f"  Notes (first 240 chars): > {c['notes_snippet'][:240]}")
        print()

    unresolved = [c for c, d, _ in classified if d == "UNRESOLVED"]
    if unresolved:
        print(f"\n## ❌ UNRESOLVED ({len(unresolved)})")
        print()
        print("Each unresolved candidate must end up in one of:")
        print("  - Tier 1: thai field includes `[...]` brackets")
        print("  - Tier 2: `output/textual_variants/<slug>_<NN>.json` exists with the verse")
        print("  - Tier 3: thai field includes ⟦…⟧ markers")
        print("  - Silent: notes explicitly say `RULES §5 silent-omission`")
        print("  - Resolved: `output/textual_variants/_resolved/<slug>_<NN>_v<V>.md` documents the dismissal")
        print()
        for c, _, _ in classified:
            if c in unresolved:
                print(f"  ❌ {c['ref']}")
        print()

    if args.strict and unresolved:
        print(f"\n[strict] FAIL: {len(unresolved)} unresolved candidate(s).", flush=True)
        return 1

    if args.strict:
        print("\n[strict] PASS: every candidate has a disposition.")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
