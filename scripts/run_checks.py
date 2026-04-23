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

CODE_TO_SLUG = {
    "MAT": "matthew", "MRK": "mark", "LUK": "luke", "JHN": "john",
    "ACT": "acts", "ROM": "romans", "1CO": "1corinthians", "2CO": "2corinthians",
    "GAL": "galatians", "EPH": "ephesians", "PHP": "philippians", "COL": "colossians",
    "1TH": "1thessalonians", "2TH": "2thessalonians", "1TI": "1timothy", "2TI": "2timothy",
    "TIT": "titus", "PHM": "philemon", "HEB": "hebrews", "JAS": "james",
    "1PE": "1peter", "2PE": "2peter", "1JN": "1john", "2JN": "2john",
    "3JN": "3john", "JUD": "jude", "REV": "revelation",
}


def run(cmd: list[str]) -> tuple[int, str]:
    """Run a subprocess, return (exit_code, stdout+stderr)."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout + result.stderr


def resolve_book_slug(book_arg: str) -> str:
    up = book_arg.upper()
    if up in CODE_TO_SLUG:
        return CODE_TO_SLUG[up]
    return book_arg.lower()


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

    print(f"\n=== Running checks on {slug} ch. {args.chapter} ===\n")

    # 1. Rebuild glossary & run key-term consistency
    print("[1/8] Key-term consistency...")
    run([sys.executable, str(SCRIPTS / "build_glossary.py")])
    code, _ = run([sys.executable, str(SCRIPTS / "check_key_term_consistency.py"),
                   "--book", slug, "--chapter", str(args.chapter)])
    record("Key-term consistency", code, f"key_term_consistency_{slug}_{args.chapter:02d}.md")

    # 2. TNBT structural comparison
    print("[2/8] TNBT structural comparison...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_against_tnbt.py"),
                   "--book", slug, "--chapter", str(args.chapter)])
    record("TNBT structural comparison", code, f"tnbt_comparison_{slug}_{args.chapter:02d}.md")

    # 3. OT citation check
    print("[3/8] OT citation check...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_ot_citations.py"),
                   "--book", slug, "--chapter", str(args.chapter)])
    record("OT citation acknowledgment", code, f"ot_citations_{slug}_{args.chapter:02d}.md")

    # 4. Parallel-passage check
    print("[4/8] Synoptic parallel-passage check...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_parallel_passages.py")])
    record("Synoptic parallels", code, "parallel_passages.md")

    # 5. Back-translation — in-chat mode by default (no API needed).
    # The script reads output/back_translations/<slug>_<NN>.json if present,
    # otherwise emits a prompt file AND exits non-zero (ship-blocker). Prior
    # behavior treated missing BT as "pending == clean," which let 14
    # chapters silently ship without back-translation through 2026-04-18.
    # Hardened 2026-04-19; pass exit code through directly.
    if args.skip_back_translation:
        print("[5/8] Back-translation — skipped per flag")
        record("Back-translation", 0, "(skipped)", "skipped via --skip-back-translation")
    else:
        print("[5/8] Back-translation...")
        code, out = run([sys.executable, str(SCRIPTS / "check_back_translation.py"),
                        "--book", slug, "--chapter", str(args.chapter)])
        bt_file = ROOT / "output" / "back_translations" / f"{slug}_{args.chapter:02d}.json"
        if bt_file.exists():
            record("Back-translation", code, f"back_translation_{slug}_{args.chapter:02d}.md")
        else:
            record("Back-translation", code,
                   f"back_translations/{slug}_{args.chapter:02d}_PROMPT.md",
                   "MISSING — Claude must back-translate per prompt before re-running")

    # 6. Summary-coverage check (informational only, non-blocking)
    # Surfaces verses that warrant a thai_summary but don't have one. Existing
    # chapters (Mark 1-8, 1 Tim 3) translated before this field existed will
    # show warranted-but-missing; that's expected and OK — not a ship gate.
    print("[6/8] Thai-summary coverage (informational)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_summary_coverage.py"),
                   "--book", slug, "--chapter", str(args.chapter)])
    record("Thai-summary coverage (info)", 0,  # always status "clean" — informational
           f"summary_coverage_{slug}_{args.chapter:02d}.md",
           "informational only — not a ship gate")

    # 7. Claim-consistency check (hallucination detector)
    # Fails ship if the translator's notes claim a pipeline side-effect
    # (glossary updated, nt_ot_citations entry added, etc.) that didn't
    # actually happen. Introduced 2026-04-17 after Opus 4.7 was observed
    # claiming "Added to nt_ot_citations.json" without performing the action.
    print("[7/8] Claim-consistency (hallucination check)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_claim_consistency.py"),
                   "--book", slug, "--chapter", str(args.chapter)])
    record("Claim consistency (hallucination)", code,
           f"claim_consistency_{slug}_{args.chapter:02d}.md")

    # 8. Greek-field integrity check (schema/metadata hallucination detector)
    # Fails ship if key_decisions[].greek contains Thai characters (schema
    # violation) or Greek tokens that don't appear in the verse's source
    # without a scholarly excuse (variant/classical/LXX/hapax/morphology).
    # Introduced 2026-04-21 after LUK 13/14 shipped with fabricated Greek
    # tokens ("ἐσδέจ" mixed-script) and Thai pronouns stuffed into the
    # greek slot. All seven prior checks passed green on that content.
    # See docs/LUKE_DRIFT_2026-04-21.md.
    print("[8/9] Greek-field integrity (metadata hallucination check)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_greek_field_integrity.py"),
                   "--book", slug, "--chapter", str(args.chapter), "--quiet"])
    record("Greek-field integrity", code,
           f"greek_field_integrity_{slug}_{args.chapter:02d}.md")

    # 9. Phrase-consistency audit (CORPUS-WIDE; catches cross-book drift)
    # Extends key-term consistency to multi-word Greek phrases that carry
    # corpus-level theological weight (ἄφεσις ἁμαρτιῶν, βασιλεία τοῦ θεοῦ,
    # ἀμὴν λέγω ὑμῖν, etc.). Each phrase is tied to a translator_decisions
    # doc. Added 2026-04-23 after Claude external-review surfaced ἄφεσις drift
    # (MAT 26:28 vs. LUK 24:47) that the per-lemma checker missed because
    # it treated ἄφεσις as a single token rather than as part of the locked
    # phrase ἄφεσις ἁμαρτιῶν.
    # This is a CORPUS check — it re-scans all books on each invocation
    # but fast (< 1s on 2900+ verses). Blocks ship if corpus drift detected.
    print("[9/9] Phrase-consistency audit (corpus-wide)...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_phrase_consistency.py")])
    record("Phrase consistency (corpus-wide)", code, "phrase_consistency.md")

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
