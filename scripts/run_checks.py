#!/usr/bin/env python3
"""
Run all post-draft checks on a translated chapter.

Executes in order:
  1. Key-term consistency audit (+ glossary rebuild)
  2. TNBT structural comparison
  3. OT citation acknowledgment check
  4. Parallel-passage check (synoptics)
  5. Back-translation check (requires ANTHROPIC_API_KEY)

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
    print("[1/5] Key-term consistency...")
    run([sys.executable, str(SCRIPTS / "build_glossary.py")])
    code, _ = run([sys.executable, str(SCRIPTS / "check_key_term_consistency.py"),
                   "--book", slug, "--chapter", str(args.chapter)])
    record("Key-term consistency", code, f"key_term_consistency_{slug}_{args.chapter:02d}.md")

    # 2. TNBT structural comparison
    print("[2/5] TNBT structural comparison...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_against_tnbt.py"),
                   "--book", slug, "--chapter", str(args.chapter)])
    record("TNBT structural comparison", code, f"tnbt_comparison_{slug}_{args.chapter:02d}.md")

    # 3. OT citation check
    print("[3/5] OT citation check...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_ot_citations.py"),
                   "--book", slug, "--chapter", str(args.chapter)])
    record("OT citation acknowledgment", code, f"ot_citations_{slug}_{args.chapter:02d}.md")

    # 4. Parallel-passage check
    print("[4/5] Synoptic parallel-passage check...")
    code, _ = run([sys.executable, str(SCRIPTS / "check_parallel_passages.py")])
    record("Synoptic parallels", code, "parallel_passages.md")

    # 5. Back-translation (optional)
    if args.skip_back_translation:
        print("[5/5] Back-translation — skipped per flag")
        record("Back-translation", 0, "(skipped)", "skipped via --skip-back-translation")
    elif not os.environ.get("ANTHROPIC_API_KEY"):
        print("[5/5] Back-translation — skipped (no ANTHROPIC_API_KEY)")
        code, _ = run([sys.executable, str(SCRIPTS / "check_back_translation.py"),
                       "--book", slug, "--chapter", str(args.chapter)])
        record("Back-translation", 0, f"back_translation_{slug}_{args.chapter:02d}.md",
               "skipped — ANTHROPIC_API_KEY not set")
    else:
        print("[5/5] Back-translation (this takes ~1-2 min)...")
        code, _ = run([sys.executable, str(SCRIPTS / "check_back_translation.py"),
                       "--book", slug, "--chapter", str(args.chapter)])
        record("Back-translation", code, f"back_translation_{slug}_{args.chapter:02d}.md")

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
