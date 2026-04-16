#!/usr/bin/env python3
"""
Revision-loop helper. When `run_checks.py` flags a chapter, this script:

  1. Reads all 5 individual check reports
  2. Aggregates flagged verses + the specific failure reason for each
  3. Writes output/check_reports/<slug>_<NN>_REVISIONS_NEEDED.md — a structured
     prompt that Claude (in the same chat) reads and acts on
  4. Tracks iteration count in output/check_reports/<slug>_<NN>_iterations.txt
  5. After 3 iterations of unresolved flags, escalates to "needs human review"

Usage:
  python3 scripts/revise_chapter.py --book MRK --chapter 8

In-chat workflow:
  1. After translation, run_checks.py → if flags, run revise_chapter.py
  2. Claude reads REVISIONS_NEEDED.md, edits the translation JSON
  3. Claude re-runs run_checks.py
  4. If still flagged, run revise_chapter.py again (iteration ++)
  5. ship_chapter.sh gates on check pass — refuses to ship until clean

This script does NOT call any LLM API. It generates the prompt; the in-chat
Claude does the actual revision work. No ANTHROPIC_API_KEY needed.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"

sys.path.insert(0, str(ROOT / "scripts"))
from extract_book import BOOKS

MAX_ITERATIONS = 3


def resolve_slug(book_arg: str) -> str:
    up = book_arg.upper()
    if up in BOOKS:
        return BOOKS[up][1]
    return book_arg.lower()


def read_iter_count(slug: str, chapter: int) -> int:
    path = REPORTS / f"{slug}_{chapter:02d}_iterations.txt"
    if not path.exists():
        return 0
    try:
        return int(path.read_text().strip())
    except Exception:
        return 0


def write_iter_count(slug: str, chapter: int, n: int) -> None:
    path = REPORTS / f"{slug}_{chapter:02d}_iterations.txt"
    path.write_text(str(n), encoding="utf-8")


def parse_summary(slug: str, chapter: int) -> dict:
    """Parse the aggregate summary JSON written by run_checks.py."""
    path = REPORTS / f"{slug}_{chapter:02d}_summary.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def extract_flagged_from_report(report_text: str, check_name: str) -> list[dict]:
    """Pull verse-level flags from a check report's markdown.

    Returns a list of dicts: {verse: "Mark 8:23", reason: "...", details: "..."}
    """
    flags = []
    # Find all `### <Reference>` headers and the prose block that follows
    # (until the next ### or ## or end of file)
    pattern = re.compile(
        r"### ([^\n]+?)\s*(?:\(([^)]+)\))?\n"          # header + optional parenthetical
        r"((?:(?!^##)[\s\S])*?)"                        # body until next heading
        r"(?=^### |^## |\Z)",
        re.MULTILINE,
    )
    for m in pattern.finditer(report_text):
        ref = m.group(1).strip()
        meta = (m.group(2) or "").strip()
        body = m.group(3).strip()
        # Skip section headers that aren't verse references
        if not re.match(r"^[\w\s]+ \d+:\d+", ref):
            continue
        flags.append({
            "verse": ref,
            "meta": meta,
            "details": body[:600],   # truncate per-flag details
            "check": check_name,
        })
    return flags


def gather_flags(slug: str, chapter: int) -> list[dict]:
    """Walk only the FAILED check reports (per summary JSON exit codes) and
    collect verse-level flagged items.

    Critical: a check that exited 0 is "clean" by the orchestrator's gate,
    even if its markdown report has informational warnings (e.g., TNBT
    structural divergences are EXPECTED and exit 0). We only revise on
    checks that exited non-zero.
    """
    summary = parse_summary(slug, chapter)
    failed_check_names = {c["name"] for c in summary.get("checks", []) if c.get("exit_code") != 0}
    if not failed_check_names:
        return []

    chapter_padded = f"{chapter:02d}"
    candidate_sources = [
        ("Key-term consistency", REPORTS / f"key_term_consistency_{slug}_{chapter_padded}.md"),
        ("TNBT structural comparison", REPORTS / f"tnbt_comparison_{slug}_{chapter_padded}.md"),
        ("OT citation acknowledgment", REPORTS / f"ot_citations_{slug}_{chapter_padded}.md"),
        ("Back-translation", REPORTS / f"back_translation_{slug}_{chapter_padded}.md"),
        ("Synoptic parallels", REPORTS / "parallel_passages.md"),
    ]
    all_flags = []
    for check_name, path in candidate_sources:
        if check_name not in failed_check_names:
            continue
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        all_flags.extend(extract_flagged_from_report(text, check_name))
    return all_flags


def render_revision_prompt(slug: str, chapter: int, iteration: int,
                            flags: list[dict], book_name: str) -> str:
    if not flags:
        return f"# Revisions for {book_name} {chapter} — iteration {iteration}\n\n✅ No flags found across any of the 5 check reports. Nothing to revise.\n"

    escalation = ""
    if iteration >= MAX_ITERATIONS:
        escalation = (
            f"\n> **⚠ Escalation:** This is iteration {iteration}. Per the revision policy, "
            f"after {MAX_ITERATIONS} iterations of unresolved flags, the chapter should be reviewed "
            f"manually. Either accept the remaining divergences (add explicit notes to the verse), "
            f"or escalate to a human reviewer for theological/linguistic judgment.\n"
        )

    lines = [
        f"# Revisions needed — {book_name} {chapter} (iteration {iteration})",
        "",
        f"**{len(flags)} verse-level flag(s)** across the check reports. "
        f"Resolve each by either (a) adding a `notes` entry or `key_decisions` rationale to the verse "
        f"in `output/translations/{slug}_{chapter:02d}.json` explaining the deliberate divergence, "
        f"or (b) retranslating the verse if the flag indicates a genuine error.",
        escalation,
        "After making revisions, re-run `python3 scripts/run_checks.py --book <CODE> --chapter <N>`. "
        "If still flagged, re-run this script (iteration count auto-increments).",
        "",
        "---",
        "",
    ]

    # Group by check
    by_check: dict[str, list] = {}
    for flag in flags:
        by_check.setdefault(flag["check"], []).append(flag)

    for check_name, check_flags in by_check.items():
        lines.append(f"## From: {check_name}")
        lines.append("")
        for f in check_flags:
            header = f"### {f['verse']}"
            if f["meta"]:
                header += f"  ({f['meta']})"
            lines.append(header)
            lines.append("")
            lines.append(f["details"])
            lines.append("")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True)
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--reset", action="store_true",
                        help="Reset iteration count (use after a clean run)")
    args = parser.parse_args()

    slug = resolve_slug(args.book)
    book_name = next((n for c, (n, s) in BOOKS.items() if s == slug), slug)

    if args.reset:
        path = REPORTS / f"{slug}_{args.chapter:02d}_iterations.txt"
        if path.exists():
            path.unlink()
        print(f"Reset iteration count for {slug} ch.{args.chapter}.")
        return 0

    REPORTS.mkdir(parents=True, exist_ok=True)

    # Increment iteration count
    iteration = read_iter_count(slug, args.chapter) + 1
    write_iter_count(slug, args.chapter, iteration)

    flags = gather_flags(slug, args.chapter)

    out_path = REPORTS / f"{slug}_{args.chapter:02d}_REVISIONS_NEEDED.md"
    md = render_revision_prompt(slug, args.chapter, iteration, flags, book_name)
    out_path.write_text(md, encoding="utf-8")

    print(f"Iteration {iteration} for {book_name} {args.chapter}")
    print(f"  Flags found: {len(flags)}")
    print(f"  Wrote: {out_path}")
    if iteration >= MAX_ITERATIONS and flags:
        print(f"  ⚠ AT/PAST MAX_ITERATIONS ({MAX_ITERATIONS}) — consider manual review.")
        return 2  # special exit for escalation
    return 0 if not flags else 1


if __name__ == "__main__":
    sys.exit(main())
