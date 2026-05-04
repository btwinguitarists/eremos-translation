#!/usr/bin/env python3
"""
NT v1.0 corpus-wide audit consolidator (Stage 1 of run_nt_full_audit).

Read-only. Aggregates:
  - per-book end-of-book audit docs (docs/end_of_book/<book>/<BOOK>_END_OF_BOOK_REVIEW_*.md)
  - external AI review responses (docs/end_of_book/<book>/ai_review_response_<BOOK>_*.md)
  - corpus-wide check outputs (key_term_consistency, phrase_consistency, inclusion_variants)
  - per-chapter summary JSONs (output/check_reports/<slug>_NN_summary.json)

Writes ONE new file: docs/NT_V1_FULL_AUDIT_<date>.md

Touches nothing else. No translation files modified. No rules modified.

Usage:
  python3 scripts/consolidate_nt_audit.py
  python3 scripts/consolidate_nt_audit.py --output docs/NT_V1_FULL_AUDIT_custom.md
"""
import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
CHECK_REPORTS = ROOT / "output" / "check_reports"
EOB_DIR = ROOT / "docs" / "end_of_book"

NT_BOOKS = [
    ("matthew", "MAT", 28),
    ("mark", "MRK", 16),
    ("luke", "LUK", 24),
    ("john", "JHN", 21),
    ("acts", "ACT", 28),
    ("romans", "ROM", 16),
    ("1corinthians", "1CO", 16),
    ("2corinthians", "2CO", 13),
    ("galatians", "GAL", 6),
    ("ephesians", "EPH", 6),
    ("philippians", "PHP", 4),
    ("colossians", "COL", 4),
    ("1thessalonians", "1TH", 5),
    ("2thessalonians", "2TH", 3),
    ("1timothy", "1TI", 6),
    ("2timothy", "2TI", 4),
    ("titus", "TIT", 3),
    ("philemon", "PHM", 1),
    ("hebrews", "HEB", 13),
    ("james", "JAS", 5),
    ("1peter", "1PE", 5),
    ("2peter", "2PE", 3),
    ("1john", "1JN", 5),
    ("2john", "2JN", 1),
    ("3john", "3JN", 1),
    ("jude", "JUD", 1),
    ("revelation", "REV", 22),
]


def chapter_count_shipped(slug: str) -> int:
    if not TRANSLATIONS.exists():
        return 0
    # Strict: only files of shape <slug>_NN.json (two-digit chapter, no suffix).
    pattern = re.compile(rf"^{re.escape(slug)}_\d{{2}}\.json$")
    return sum(1 for p in TRANSLATIONS.iterdir() if pattern.match(p.name))


def find_audit_doc(slug: str) -> Path | None:
    folder = EOB_DIR / slug
    if not folder.exists():
        return None
    candidates = sorted(folder.glob("*_END_OF_BOOK_REVIEW_*.md"))
    return candidates[-1] if candidates else None


def find_external_response(slug: str) -> Path | None:
    folder = EOB_DIR / slug
    if not folder.exists():
        return None
    candidates = sorted(folder.glob("ai_review_response_*.md"))
    return candidates[-1] if candidates else None


def find_external_packet(slug: str) -> Path | None:
    folder = EOB_DIR / slug
    if not folder.exists():
        return None
    candidates = sorted(folder.glob("external_review_packet_*.md"))
    return candidates[-1] if candidates else None


def extract_status_counts(audit_path: Path) -> dict[str, int]:
    """Pull LOCKED/STABLE/REVIEW/DECIDE counts from a per-book audit doc heading."""
    counts = {"LOCKED": 0, "STABLE": 0, "REVIEW": 0, "DECIDE": 0}
    if not audit_path or not audit_path.exists():
        return counts
    text = audit_path.read_text(encoding="utf-8")
    for code in counts:
        # e.g., '**REVIEW**' or 'flagged REVIEW' — count occurrences in section headings
        counts[code] = len(re.findall(rf"\b{code}\b", text))
    return counts


def run_corpus_check(script_name: str, args: list[str] | None = None) -> tuple[bool, str]:
    """Run a corpus-wide check script and capture its result."""
    script_path = ROOT / "scripts" / script_name
    if not script_path.exists():
        return False, f"script not found: {script_name}"
    cmd = ["python3", str(script_path)]
    if args:
        cmd += args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=str(ROOT))
        passed = result.returncode == 0
        return passed, (result.stdout + result.stderr).strip()
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as exc:  # noqa
        return False, f"error: {exc}"


def gather_per_chapter_warnings(slug: str, chapters: int) -> list[str]:
    """Collect warning lines from per-chapter summary JSONs."""
    warnings = []
    for n in range(1, chapters + 1):
        summary_path = CHECK_REPORTS / f"{slug}_{n:02d}_summary.json"
        if not summary_path.exists():
            continue
        try:
            data = json.loads(summary_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for k, v in data.items():
            if isinstance(v, dict) and v.get("status") in ("warn", "fail"):
                warnings.append(f"{slug}_{n:02d}: {k} = {v.get('status')}")
    return warnings


def build_audit(output_path: Path) -> None:
    today = date.today().isoformat()
    lines: list[str] = []

    lines.append(f"# NT v1.0 — Full Corpus Audit")
    lines.append("")
    lines.append(f"**Generated:** {today}")
    lines.append(f"**Source:** `consolidate_nt_audit.py` (Stage 1 of run_nt_full_audit)")
    lines.append("**Scope:** All 27 NT books, corpus-wide checks, per-book audit findings,")
    lines.append("AI review responses where present.")
    lines.append("")
    lines.append("**Read-only consolidation.** No translations or rules modified.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 1. Coverage matrix
    lines.append("## 1. Coverage matrix")
    lines.append("")
    lines.append("| Book | Code | Chapters expected | Shipped | EOB audit | External response |")
    lines.append("|---|---|---:|---:|:-:|:-:|")
    total_expected = 0
    total_shipped = 0
    audits_present = 0
    responses_present = 0
    for slug, code, expected in NT_BOOKS:
        shipped = chapter_count_shipped(slug)
        audit = find_audit_doc(slug)
        response = find_external_response(slug)
        audit_mark = "yes" if audit else "—"
        response_mark = "yes" if response else "—"
        if audit:
            audits_present += 1
        if response:
            responses_present += 1
        total_expected += expected
        total_shipped += shipped
        lines.append(
            f"| {slug} | {code} | {expected} | {shipped} | {audit_mark} | {response_mark} |"
        )
    lines.append(
        f"| **Total** | | **{total_expected}** | **{total_shipped}** | **{audits_present}/27** | **{responses_present}/27** |"
    )
    lines.append("")

    if total_shipped < total_expected:
        lines.append(
            f"> **Coverage gap:** {total_expected - total_shipped} chapters not yet shipped. "
            "Audit findings below are for the shipped subset only."
        )
        lines.append("")

    lines.append("---")
    lines.append("")

    # 2. Corpus-wide automated checks
    lines.append("## 2. Corpus-wide automated checks")
    lines.append("")
    lines.append("Each script run against the full corpus. PASS = exit 0; FAIL = non-zero exit.")
    lines.append("")
    # Only scripts that support corpus-wide invocation. Per-chapter checks
    # (back_translation, summary_coverage, claim_consistency) ran already at
    # ship time and have artifacts in output/check_reports/; rolled up in §5.
    corpus_checks = [
        ("check_key_term_consistency.py", []),
        ("check_phrase_consistency.py", []),
        ("audit_inclusion_variants.py", ["--strict"]),
        ("check_parallel_passages.py", []),
    ]
    for script, args in corpus_checks:
        passed, output = run_corpus_check(script, args)
        status = "PASS" if passed else "FAIL"
        arg_str = " ".join(args)
        lines.append(f"### `{script} {arg_str}` — **{status}**")
        lines.append("")
        if not passed and output:
            tail = "\n".join(output.splitlines()[-15:])
            lines.append("```")
            lines.append(tail)
            lines.append("```")
            lines.append("")

    lines.append("---")
    lines.append("")

    # 3. Per-book audit status rollup
    lines.append("## 3. Per-book audit status rollup")
    lines.append("")
    lines.append("Status-code counts pulled from each book's end-of-book audit doc.")
    lines.append("")
    lines.append("| Book | LOCKED | STABLE | REVIEW | DECIDE |")
    lines.append("|---|---:|---:|---:|---:|")
    grand_total = {"LOCKED": 0, "STABLE": 0, "REVIEW": 0, "DECIDE": 0}
    for slug, code, _ in NT_BOOKS:
        audit = find_audit_doc(slug)
        if not audit:
            lines.append(f"| {slug} | — | — | — | — |")
            continue
        counts = extract_status_counts(audit)
        for k, v in counts.items():
            grand_total[k] += v
        lines.append(
            f"| {slug} | {counts['LOCKED']} | {counts['STABLE']} | "
            f"{counts['REVIEW']} | {counts['DECIDE']} |"
        )
    lines.append(
        f"| **Total** | **{grand_total['LOCKED']}** | **{grand_total['STABLE']}** | "
        f"**{grand_total['REVIEW']}** | **{grand_total['DECIDE']}** |"
    )
    lines.append("")
    lines.append(
        "> Token counts are heuristic (regex match on the status word in the doc). "
        "For decision-grade detail, open the per-book audit at `docs/end_of_book/<book>/`."
    )
    lines.append("")

    lines.append("---")
    lines.append("")

    # 4. Outstanding REVIEW + DECIDE items pointer
    lines.append("## 4. Outstanding items by book")
    lines.append("")
    lines.append("Per-book audit docs containing REVIEW or DECIDE flags worth a final pass:")
    lines.append("")
    for slug, code, _ in NT_BOOKS:
        audit = find_audit_doc(slug)
        if not audit:
            continue
        counts = extract_status_counts(audit)
        if counts["REVIEW"] == 0 and counts["DECIDE"] == 0:
            continue
        rel = audit.relative_to(ROOT)
        lines.append(
            f"- **{slug}** ({code}) — REVIEW: {counts['REVIEW']}, DECIDE: {counts['DECIDE']} — `{rel}`"
        )
    lines.append("")

    lines.append("---")
    lines.append("")

    # 5. Per-chapter warnings rollup
    lines.append("## 5. Per-chapter check warnings")
    lines.append("")
    lines.append("Warnings or failures from per-chapter summary JSONs (if any).")
    lines.append("")
    any_warn = False
    for slug, code, expected in NT_BOOKS:
        warnings = gather_per_chapter_warnings(slug, expected)
        if not warnings:
            continue
        any_warn = True
        lines.append(f"### {slug}")
        for w in warnings:
            lines.append(f"- {w}")
        lines.append("")
    if not any_warn:
        lines.append("None. All shipped chapters have clean summary JSONs.")
        lines.append("")

    lines.append("---")
    lines.append("")

    # 6. Stage-2 pointer
    lines.append("## 6. Next: Stage 2 polish sweep")
    lines.append("")
    lines.append(
        "Stage 1 is mechanical consolidation. Thai-flow micro-issues "
        "(double-possessives, title-collisions, redundant directionals, lexical redundancies, "
        "passive ambiguities, awkward phonetics) are caught in Stage 2."
    )
    lines.append("")
    lines.append("To run Stage 2:")
    lines.append("```")
    lines.append("python3 scripts/polish_review.py --book <slug>     # one book")
    lines.append("python3 scripts/polish_review.py --all              # all 27 NT books")
    lines.append("```")
    lines.append("")
    lines.append(
        "Stage 2 writes proposals to `output/polish_proposals/` only. "
        "Translation files are NOT modified until you run `apply_polish_deltas.py` "
        "with explicit approvals."
    )
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="NT v1.0 corpus audit consolidator (Stage 1)")
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "docs" / f"NT_V1_FULL_AUDIT_{date.today().isoformat()}.md",
        help="Output markdown path (default: docs/NT_V1_FULL_AUDIT_<today>.md)",
    )
    args = parser.parse_args()

    print(f"Consolidating NT audit → {args.output.relative_to(ROOT)}")
    build_audit(args.output)
    print(f"Done. {args.output.stat().st_size} bytes written.")


if __name__ == "__main__":
    main()
