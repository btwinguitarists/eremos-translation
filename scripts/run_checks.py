#!/usr/bin/env python3
"""
Run all post-draft checks on a translated chapter.

Executes in order:
  1. Key-term consistency audit (+ glossary rebuild)
  2. TNBT structural comparison
  3. OT citation acknowledgment check
  4. Parallel-passage check (synoptics)
  5. Back-translation check (requires ANTHROPIC_API_KEY)
  6. Thai-summary coverage (informational)
  7. Claim-consistency (hallucination detector)
  8. Greek-field integrity (schema hallucination detector)
  9. Phrase-consistency audit (corpus-wide; catches cross-book drift)

Aggregates into a single review report at
  output/check_reports/<book>_<NN>_review.md

Usage:
  python3 scripts/run_checks.py --book 1TI --chapter 3
  python3 scripts/run_checks.py --book mark --chapter 1 --skip-back-translation
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
TRANSLATIONS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"

# ─── OT pipeline feature flag ─────────────────────────────────────────────────
# Per the OT-rollout plan §9.5 + §19. NT close confirmed (260/260 NT chapters
# shipped 2026-05-04, including HEB 13/13 + REV 22/22). NT regression smoke-test
# passed. Flag flipped to default ON. Set OT_PIPELINE_ENABLED=false in env to
# revert to NT-only behavior (e.g., for emergency NT-pipeline isolation).
OT_PIPELINE_ENABLED = os.environ.get("OT_PIPELINE_ENABLED", "true").lower() in ("1", "true", "yes")

CODE_TO_SLUG = {
    "MAT": "matthew", "MRK": "mark", "LUK": "luke", "JHN": "john",
    "ACT": "acts", "ROM": "romans", "1CO": "1corinthians", "2CO": "2corinthians",
    "GAL": "galatians", "EPH": "ephesians", "PHP": "philippians", "COL": "colossians",
    "1TH": "1thessalonians", "2TH": "2thessalonians", "1TI": "1timothy", "2TI": "2timothy",
    "TIT": "titus", "PHM": "philemon", "HEB": "hebrews", "JAS": "james",
    "1PE": "1peter", "2PE": "2peter", "1JN": "1john", "2JN": "2john",
    "3JN": "3john", "JUD": "jude", "REV": "revelation",
}

OT_CODE_TO_SLUG = {
    "GEN": "genesis", "EXO": "exodus", "LEV": "leviticus", "NUM": "numbers",
    "DEU": "deuteronomy", "JOS": "joshua", "JDG": "judges", "RUT": "ruth",
    "1SA": "1samuel", "2SA": "2samuel", "1KI": "1kings", "2KI": "2kings",
    "1CH": "1chronicles", "2CH": "2chronicles", "EZR": "ezra", "NEH": "nehemiah",
    "EST": "esther", "JOB": "job", "PSA": "psalms", "PRO": "proverbs",
    "ECC": "ecclesiastes", "SNG": "songofsongs", "ISA": "isaiah", "JER": "jeremiah",
    "LAM": "lamentations", "EZK": "ezekiel", "DAN": "daniel", "HOS": "hosea",
    "JOL": "joel", "AMO": "amos", "OBA": "obadiah", "JON": "jonah",
    "MIC": "micah", "NAM": "nahum", "HAB": "habakkuk", "ZEP": "zephaniah",
    "HAG": "haggai", "ZEC": "zechariah", "MAL": "malachi",
}


def run(cmd: list[str]) -> tuple[int, str]:
    """Run a subprocess, return (exit_code, stdout+stderr)."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout + result.stderr


def resolve_book_slug(book_arg: str) -> str:
    up = book_arg.upper()
    if up in CODE_TO_SLUG:
        return CODE_TO_SLUG[up]
    if up in OT_CODE_TO_SLUG:
        return OT_CODE_TO_SLUG[up]
    return book_arg.lower()


def detect_chapter_language(slug: str, chapter: int) -> str:
    """Determine the source-language path: 'greek' / 'hebrew' / 'aramaic'.

    Resolution order:
      1. Source extract `output/<slug>/<slug>_<NN>.json` (extract_book_hebrew.py
         emits `language: "hebrew"|"aramaic"` per verse). Take the first verse's
         language as the chapter's language.
      2. Slug → NT/OT mapping (NT slugs always 'greek').
      3. Default 'greek' (NT pipeline) — preserves backward compat for
         pre-OT chapters.
    """
    src = ROOT / "output" / slug / f"{slug}_{chapter:02d}.json"
    if src.exists():
        try:
            data = json.loads(src.read_text(encoding="utf-8"))
            if data and isinstance(data, list):
                lang = data[0].get("language")
                if lang in ("hebrew", "aramaic"):
                    return lang
        except Exception:
            pass
    if slug in OT_CODE_TO_SLUG.values():
        return "hebrew"  # default OT-language guess if no extract
    return "greek"


def run_nt_checks(slug: str, chapter: int, args, summary: dict, record) -> None:
    """The original 9-step NT pipeline. Behavior unchanged from the pre-OT-rollout
    version of this script — preserved verbatim under a function so the OT branch
    can be added without touching the NT code path.
    """
    print(f"\n=== Running NT checks on {slug} ch. {chapter} ===\n")

    # 1. Rebuild glossary & run key-term consistency
    print("[1/9] Key-term consistency...")
    run([sys.executable, str(SCRIPTS / "build_glossary.py")])
    code, _ = run([sys.executable, str(SCRIPTS / "check_key_term_consistency.py"),
                   "--book", slug, "--chapter", str(chapter)])
    record("Key-term consistency", code, f"key_term_consistency_{slug}_{chapter:02d}.md")

    # 2. TNBT structural comparison
    print("[2/9] TNBT structural comparison...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_against_tnbt.py"),
                   "--book", slug, "--chapter", str(chapter)])
    record("TNBT structural comparison", code, f"tnbt_comparison_{slug}_{chapter:02d}.md")

    # 3. OT citation check
    print("[3/9] OT citation check...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_ot_citations.py"),
                   "--book", slug, "--chapter", str(chapter)])
    record("OT citation acknowledgment", code, f"ot_citations_{slug}_{chapter:02d}.md")

    # 4. Parallel-passage check
    print("[4/9] Synoptic parallel-passage check...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_parallel_passages.py")])
    record("Synoptic parallels", code, "parallel_passages.md")

    # 5. Back-translation
    if args.skip_back_translation:
        print("[5/9] Back-translation — skipped per flag")
        record("Back-translation", 0, "(skipped)", "skipped via --skip-back-translation")
    else:
        print("[5/9] Back-translation...")
        code, out = run([sys.executable, str(SCRIPTS / "check_back_translation.py"),
                        "--book", slug, "--chapter", str(chapter)])
        bt_file = ROOT / "output" / "back_translations" / f"{slug}_{chapter:02d}.json"
        if bt_file.exists():
            record("Back-translation", code, f"back_translation_{slug}_{chapter:02d}.md")
        else:
            record("Back-translation", code,
                   f"back_translations/{slug}_{chapter:02d}_PROMPT.md",
                   "MISSING — Claude must back-translate per prompt before re-running")

    # 6. Summary-coverage check (informational)
    print("[6/9] Thai-summary coverage (informational)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_summary_coverage.py"),
                   "--book", slug, "--chapter", str(chapter)])
    record("Thai-summary coverage (info)", 0,
           f"summary_coverage_{slug}_{chapter:02d}.md",
           "informational only — not a ship gate")

    # 7. Claim-consistency check (hallucination detector)
    print("[7/9] Claim-consistency (hallucination check)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_claim_consistency.py"),
                   "--book", slug, "--chapter", str(chapter)])
    record("Claim consistency (hallucination)", code,
           f"claim_consistency_{slug}_{chapter:02d}.md")

    # 8. Greek-field integrity check
    print("[8/9] Greek-field integrity (metadata hallucination check)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_greek_field_integrity.py"),
                   "--book", slug, "--chapter", str(chapter), "--quiet"])
    record("Greek-field integrity", code,
           f"greek_field_integrity_{slug}_{chapter:02d}.md")

    # 9. Phrase-consistency audit (corpus-wide)
    print("[9/9] Phrase-consistency audit (corpus-wide)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_phrase_consistency.py")])
    record("Phrase consistency (corpus-wide)", code, "phrase_consistency.md")


def run_ot_checks(slug: str, chapter: int, language: str, args, summary: dict, record) -> None:
    """OT-specific check pipeline. Reachable only when OT_PIPELINE_ENABLED is True.

    Currently wired:
      1. Hebrew/Aramaic-field integrity (sibling to Greek-field check)
      2. Divine-names enforcement (locked Tetragrammaton + family)
      3. Versification anchor (MT verse numbering + divergence-zone metadata)
      4. Back-translation (language-agnostic; reused as-is from NT)
      5. Thai-summary coverage (language-agnostic; reused as-is from NT)

    NOT yet wired (TBD as scripts arrive):
      - check_key_term_consistency (needs Hebrew CANONICAL_TERMS extension)
      - check_phrase_consistency (needs Hebrew PHRASE_LOCKS extension)
      - check_claim_consistency (needs Hebrew claim patterns)
      - check_parallel_passages (needs ot_parallels.json)
      - check_ketib_qere (warning-only, future)
      - check_lxx_mt_divergence (metadata-only, future)
      - check_formula_locks (data-driven; future)
      - check_parallelism / check_acrostic_markers / check_speech_attribution
      - check_aramaic_sections / check_rachasap_consistency
      - check_nt_quotation_alignment
    """
    print(f"\n=== Running OT ({language}) checks on {slug} ch. {chapter} ===\n")

    # OT-specific scripts take a 3-letter book code (uppercase) and write
    # markdown reports via --report. Translate slug → code for them.
    book_code = next(
        (code for code, s in OT_CODE_TO_SLUG.items() if s == slug), slug.upper()
    )

    # 1. Hebrew/Aramaic field integrity
    print("[1/5] Hebrew-field integrity (metadata hallucination check)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_hebrew_field_integrity.py"),
                   "--book", book_code, "--chapter", str(chapter), "--report"])
    record("Hebrew-field integrity", code,
           f"hebrew_field_integrity_{slug}_{chapter:02d}.md")

    # 2. Divine-names enforcement (locked Tetragrammaton policy)
    print("[2/5] Divine-names enforcement...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_divine_names.py"),
                   "--book", book_code, "--chapter", str(chapter), "--report"])
    record("Divine names (locked Tetragrammaton)", code,
           f"divine_names_{slug}_{chapter:02d}.md")

    # 3. Versification anchor (MT versification + divergence zones)
    print("[3/6] Versification anchor (MT-anchored numbering)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_versification_anchor.py"),
                   "--book", book_code, "--chapter", str(chapter), "--report"])
    record("Versification anchor", code,
           f"versification_{slug}_{chapter:02d}.md")

    # 4. Honorifics binding (Rachasap — ทรง- bound to divine/royal subjects only)
    # Catches the Ruth 1:13 class — body-part-of-God (พระหัตถ์, พระเนตร, etc.)
    # in subject position taking ทรง- on the verb. Per ot_register_policy_2026-05.
    print("[4/6] Honorifics binding (Rachasap ทรง- subject check)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_honorifics_binding.py"),
                   "--book", book_code, "--chapter", str(chapter), "--report"])
    record("Honorifics binding (Rachasap)", code,
           f"honorifics_binding_{slug}_{chapter:02d}.md")

    # 5. Back-translation (language-agnostic — reused from NT)
    if args.skip_back_translation:
        print("[5/6] Back-translation — skipped per flag")
        record("Back-translation", 0, "(skipped)", "skipped via --skip-back-translation")
    else:
        print("[5/6] Back-translation...")
        code, out = run([sys.executable, str(SCRIPTS / "check_back_translation.py"),
                        "--book", slug, "--chapter", str(chapter)])
        bt_file = ROOT / "output" / "back_translations" / f"{slug}_{chapter:02d}.json"
        if bt_file.exists():
            record("Back-translation", code, f"back_translation_{slug}_{chapter:02d}.md")
        else:
            record("Back-translation", code,
                   f"back_translations/{slug}_{chapter:02d}_PROMPT.md",
                   "MISSING — Claude must back-translate per prompt before re-running")

    # 6. Summary-coverage (informational, language-agnostic)
    print("[6/6] Thai-summary coverage (informational)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_summary_coverage.py"),
                   "--book", slug, "--chapter", str(chapter)])
    record("Thai-summary coverage (info)", 0,
           f"summary_coverage_{slug}_{chapter:02d}.md",
           "informational only — not a ship gate")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True, help="Book code (MRK, 1TI) or slug (mark, 1timothy)")
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--skip-back-translation", action="store_true",
                        help="Skip Claude API back-translation check")
    args = parser.parse_args()

    slug = resolve_book_slug(args.book)
    translation_file = TRANSLATIONS / f"{slug}_{args.chapter:02d}.json"
    if not translation_file.exists():
        print(f"✗ No translation file at {translation_file}")
        print(f"  Translate {slug} ch. {args.chapter} first, then re-run checks.")
        return 1

    REPORTS.mkdir(parents=True, exist_ok=True)

    summary = {
        "book": slug,
        "chapter": args.chapter,
        "checks": [],
    }

    def record(name: str, exit_code: int, report_file: str, notes: str = ""):
        summary["checks"].append({
            "name": name,
            "exit_code": exit_code,
            "report": report_file,
            "notes": notes,
            "status": "clean" if exit_code == 0 else "flags",
        })

    # ─── Language-aware dispatcher (per OT-rollout plan §9.4) ─────────────────
    # Detect the chapter's source language. NT slugs and chapters with no source
    # extract default to 'greek' (NT pipeline). OT-extracted chapters report
    # 'hebrew' or 'aramaic' from the source verse JSON. The OT branch is gated
    # behind the OT_PIPELINE_ENABLED flag — when False, OT chapters fall through
    # to the (NT-shaped) NT pipeline call, which is harmless because the NT
    # checks expect a `greek` field that won't exist on an OT chapter and will
    # surface flags rather than silently passing. The intended use is to keep
    # the flag False until NT is fully shipped (per plan §19.2 / §20).
    language = detect_chapter_language(slug, args.chapter)

    if language in ("hebrew", "aramaic") and OT_PIPELINE_ENABLED:
        run_ot_checks(slug, args.chapter, language, args, summary, record)
    else:
        if language in ("hebrew", "aramaic"):
            print(
                f"⚠ {slug} ch. {args.chapter} is {language}, but OT_PIPELINE_ENABLED is False. "
                f"Set OT_PIPELINE_ENABLED=true to enable OT-specific checks. "
                f"Falling back to NT pipeline (which will likely flag issues).",
                file=sys.stderr,
            )
        run_nt_checks(slug, args.chapter, args, summary, record)

    # Aggregate report
    review_lines = [
        f"# Check report — {slug} ch. {args.chapter}",
        "",
        "| Check | Status | Report |",
        "|-------|--------|--------|",
    ]
    for c in summary["checks"]:
        icon = "✅" if c["status"] == "clean" else "⚠️"
        review_lines.append(f"| {c['name']} | {icon} {c['status']} | [{c['report']}]({c['report']}) |")

    review_lines.append("")
    review_lines.append("## Ship criterion")
    review_lines.append("")
    has_flags = any(c["status"] == "flags" for c in summary["checks"])
    if has_flags:
        review_lines.append("⚠ **Not ready to ship.** One or more checks flagged issues. Review individual reports, update the chapter's translation notes or verses, and re-run.")
    else:
        review_lines.append("✅ **Ready to ship.** All checks passed. Follow the workflow doc's ship steps (build bundle → push to Eremos branch → Vercel preview).")

    review_lines.append("")
    review_lines.append("## Remaining manual steps (not automated)")
    review_lines.append("")
    review_lines.append("- Native-speaker naturalness review")
    review_lines.append("- Theological review (doctrinal accuracy)")
    review_lines.append("- Community comprehension testing (when applicable)")
    review_lines.append("")
    review_lines.append("See [RULES.md §9](../../RULES.md) for context.")

    review_path = REPORTS / f"{slug}_{args.chapter:02d}_review.md"
    review_path.write_text("\n".join(review_lines), encoding="utf-8")
    print(f"\n✓ Aggregate report: {review_path}")

    # Also dump structured summary
    json_path = REPORTS / f"{slug}_{args.chapter:02d}_summary.json"
    json_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print()
    for c in summary["checks"]:
        icon = "✅" if c["status"] == "clean" else "⚠️"
        print(f"  {icon} {c['name']}: {c['status']}")

    return 1 if has_flags else 0


if __name__ == "__main__":
    sys.exit(main())
