#!/usr/bin/env python3
"""
Apply approved polish-review deltas to translation JSONs.

Reads decisions from the SINGLE summary doc:
  docs/NT_V1_POLISH_SUMMARY_<date>.md

For each proposal whose `**Decision:**` line is `approve`:
  - looks up the proposal in `output/polish_proposals/<slug>/<slug>_NN.json`
  - applies it to `output/translations/<slug>_NN.json`
  - runs corpus-wide regression checks per book
  - on regression failure, auto-reverts all commits made in that book

Safety guarantees:
  - Default decision = pending → nothing happens
  - Per-proposal re-validation at apply time (verbatim match, locked-term
    preservation) — rejects if drift since proposal was generated
  - Each successful delta is its own git commit
  - Regression failure auto-reverts that book's commits to start state

Usage:
  python3 scripts/apply_polish_deltas.py --all                    # all approved
  python3 scripts/apply_polish_deltas.py --book john              # filter to one book
  python3 scripts/apply_polish_deltas.py --all --dry-run          # preview, no changes
  python3 scripts/apply_polish_deltas.py --summary <path>         # use specific summary doc
"""
import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
PROPOSALS = ROOT / "output" / "polish_proposals"
DOCS = ROOT / "docs"

DECISION_RE = re.compile(r"^\*\*Decision:\*\*\s*(\w+)\s*$", re.MULTILINE)
PROPOSAL_BLOCK_RE = re.compile(
    r"<!--\s*POLISH_PROPOSAL\s+id=([^\s>]+)\s*-->(.*?)<!--\s*/POLISH_PROPOSAL\s*-->",
    re.DOTALL,
)


def find_latest_summary() -> Path | None:
    """Find the most recent NT_V1_POLISH_SUMMARY_*.md file."""
    candidates = sorted(DOCS.glob("NT_V1_POLISH_SUMMARY_*.md"))
    return candidates[-1] if candidates else None


def parse_summary_decisions(summary_path: Path) -> dict[str, str]:
    """Return {proposal_id: decision} from the summary doc."""
    if not summary_path.exists():
        return {}
    text = summary_path.read_text(encoding="utf-8")
    out = {}
    for match in PROPOSAL_BLOCK_RE.finditer(text):
        proposal_id = match.group(1).strip()
        block = match.group(2)
        m = DECISION_RE.search(block)
        decision = m.group(1).strip().lower() if m else "pending"
        out[proposal_id] = decision
    return out


def proposal_id_to_slug_chapter(proposal_id: str) -> tuple[str, int, int, bool]:
    """Parse 'john_15_001' or 'john_15_optimal_001' -> (slug, chapter, idx, is_optimal).
    Index is 1-based."""
    m = re.match(r"^(.+)_(\d{2})_optimal_(\d{3})$", proposal_id)
    if m:
        return m.group(1), int(m.group(2)), int(m.group(3)), True
    m = re.match(r"^(.+)_(\d{2})_(\d{3})$", proposal_id)
    if not m:
        raise ValueError(f"bad proposal id: {proposal_id}")
    return m.group(1), int(m.group(2)), int(m.group(3)), False


def load_sidecar(slug: str, chapter: int, is_optimal: bool = False) -> dict | None:
    suffix = "_optimal" if is_optimal else ""
    json_path = PROPOSALS / slug / f"{slug}_{chapter:02d}{suffix}.json"
    if not json_path.exists():
        return None
    return json.loads(json_path.read_text(encoding="utf-8"))


def all_locked_thai_in_verse(verse: dict) -> set[str]:
    locked = set()
    kds = verse.get("translation", {}).get("key_decisions", []) or []
    for kd in kds:
        thai = (kd or {}).get("thai")
        if thai:
            locked.add(thai.strip())
    return locked


def apply_proposal_to_chapter(chapter_data: list[dict], proposal: dict) -> tuple[bool, str]:
    """Apply one proposal in-memory. Returns (ok, reason)."""
    ref = proposal["verse_ref"]
    verse = next((v for v in chapter_data if v.get("reference") == ref), None)
    if not verse:
        return False, f"verse not found at apply time: {ref}"
    thai = verse.get("translation", {}).get("thai", "")
    current = proposal["current_text"]
    proposed = proposal["proposed_text"]
    if current not in thai:
        return False, "current_text no longer in Thai (drift since proposal generated)"

    new_thai = thai.replace(current, proposed, 1)
    locked = all_locked_thai_in_verse(verse)
    for term in locked:
        if term and term in thai and term not in new_thai:
            return False, f"would remove corpus-locked term: {term}"

    verse["translation"]["thai"] = new_thai
    return True, "ok"


def run_regression() -> tuple[bool, list[str]]:
    """Run corpus-wide regression. Returns (all_passed, [failure_messages])."""
    checks = [
        ("check_key_term_consistency.py", []),
        ("check_phrase_consistency.py", []),
        ("audit_inclusion_variants.py", ["--strict"]),
    ]
    failures = []
    for script, extra_args in checks:
        cmd = ["python3", str(ROOT / "scripts" / script), *extra_args]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=300, cwd=str(ROOT))
            if r.returncode != 0:
                tail = "\n".join((r.stdout + r.stderr).splitlines()[-10:])
                failures.append(f"{script}: FAIL\n{tail}")
        except Exception as exc:
            failures.append(f"{script}: error {exc}")
    return len(failures) == 0, failures


def git(*args: str) -> tuple[int, str]:
    r = subprocess.run(["git", *args], capture_output=True, text=True, cwd=str(ROOT))
    return r.returncode, (r.stdout + r.stderr).strip()


def in_clean_git_state() -> bool:
    rc, out = git("status", "--porcelain")
    return rc == 0 and not out.strip()


def apply_chapter(slug: str, chapter: int,
                  approved_ids: set[str], dry_run: bool) -> dict:
    """Apply proposals whose ids are in approved_ids for this chapter.
    Walks both heuristic (`<slug>_NN.json`) and optimal-equivalence
    (`<slug>_NN_optimal.json`) sidecars; the ID format embeds which set."""
    stats = {"applied": 0, "rejected": 0, "skipped": 0, "errors": []}

    sidecars = [
        (load_sidecar(slug, chapter, is_optimal=False), ""),
        (load_sidecar(slug, chapter, is_optimal=True), "_optimal"),
    ]
    if all(s is None for s, _ in sidecars):
        return stats

    json_path = TRANSLATIONS / f"{slug}_{chapter:02d}.json"
    if not json_path.exists():
        stats["errors"].append(f"translation file missing: {json_path.name}")
        return stats

    chapter_data = json.loads(json_path.read_text(encoding="utf-8"))

    for sidecar, suffix in sidecars:
        if not sidecar:
            continue
        for i, p in enumerate(sidecar.get("proposals", []), start=1):
            proposal_id = f"{slug}_{chapter:02d}{suffix}_{i:03d}"
            if proposal_id not in approved_ids:
                stats["skipped"] += 1
                continue

            ok, reason = apply_proposal_to_chapter(chapter_data, p)
            if not ok:
                stats["rejected"] += 1
                stats["errors"].append(f"{proposal_id}: {reason}")
                continue

            stats["applied"] += 1

            if not dry_run:
                json_path.write_text(
                    json.dumps(chapter_data, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                commit_msg = f"polish: {p['verse_ref']} ({p['issue_type']})"
                rc, _ = git("add", str(json_path.relative_to(ROOT)))
                if rc != 0:
                    stats["errors"].append(f"{proposal_id}: git add failed")
                    continue
                rc, out = git("commit", "-m", commit_msg)
                if rc != 0:
                    stats["errors"].append(f"{proposal_id}: git commit failed: {out[:200]}")

    return stats


def revert_book_commits(start_sha: str) -> tuple[bool, str]:
    """Reset to start_sha, dropping any commits made by this run."""
    rc, out = git("reset", "--hard", start_sha)
    return rc == 0, out


def apply_book(slug: str, max_chapters: int,
               approved_by_chapter: dict[int, set[str]], dry_run: bool) -> dict:
    """Apply approved proposals across a book; regression-gate; revert on failure."""
    book_stats = {"slug": slug, "applied": 0, "rejected": 0, "skipped": 0,
                  "errors": [], "regression_failed": False, "reverted": False}

    if not dry_run:
        if not in_clean_git_state():
            book_stats["errors"].append("git working tree dirty; commit or stash first")
            return book_stats

    rc, start_sha = git("rev-parse", "HEAD")
    if rc != 0:
        book_stats["errors"].append("git rev-parse HEAD failed")
        return book_stats
    start_sha = start_sha.strip()

    for ch in range(1, max_chapters + 1):
        approved_ids = approved_by_chapter.get(ch, set())
        s = apply_chapter(slug, ch, approved_ids, dry_run)
        for k in ("applied", "rejected", "skipped"):
            book_stats[k] += s[k]
        book_stats["errors"].extend(s["errors"])

    if dry_run or book_stats["applied"] == 0:
        return book_stats

    # Regression gate
    print(f"  Running regression on {slug}…")
    passed, failures = run_regression()
    if passed:
        return book_stats

    book_stats["regression_failed"] = True
    book_stats["errors"].extend(failures)
    print(f"  Regression FAILED for {slug}; reverting {book_stats['applied']} commits…")
    ok, msg = revert_book_commits(start_sha)
    book_stats["reverted"] = ok
    if not ok:
        book_stats["errors"].append(f"revert failed: {msg}")
    return book_stats


NT_MAX_CHAPTERS = {
    "matthew": 28, "mark": 16, "luke": 24, "john": 21, "acts": 28, "romans": 16,
    "1corinthians": 16, "2corinthians": 13, "galatians": 6, "ephesians": 6,
    "philippians": 4, "colossians": 4, "1thessalonians": 5, "2thessalonians": 3,
    "1timothy": 6, "2timothy": 4, "titus": 3, "philemon": 1, "hebrews": 13,
    "james": 5, "1peter": 5, "2peter": 3, "1john": 5, "2john": 1, "3john": 1,
    "jude": 1, "revelation": 22,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply approved polish-review deltas")
    parser.add_argument("--book", help="Filter to one book (e.g., john)")
    parser.add_argument("--all", action="store_true", help="All books with approvals")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be applied; no file changes, no commits")
    parser.add_argument("--summary", type=Path,
                        help="Specific summary doc (default: latest NT_V1_POLISH_SUMMARY_*.md)")
    args = parser.parse_args()

    if not (args.book or args.all):
        parser.error("must specify --book SLUG or --all")

    summary_path = args.summary or find_latest_summary()
    if not summary_path:
        print("No NT_V1_POLISH_SUMMARY_*.md found in docs/. Run polish_review + build_polish_summary first.")
        sys.exit(1)
    print(f"Reading decisions from: {summary_path.relative_to(ROOT)}")

    decisions = parse_summary_decisions(summary_path)
    approved_ids = {pid for pid, dec in decisions.items() if dec == "approve"}
    if not approved_ids:
        print("No proposals marked 'approve' in the summary doc.")
        if decisions:
            counts = defaultdict(int)
            for d in decisions.values():
                counts[d] += 1
            print("Decision breakdown: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
        return

    # Group approved ids by (slug, chapter)
    approved_by_book: dict[str, dict[int, set[str]]] = defaultdict(lambda: defaultdict(set))
    for pid in approved_ids:
        try:
            slug, chapter, _idx, _is_opt = proposal_id_to_slug_chapter(pid)
        except ValueError as exc:
            print(f"  Skipping malformed id: {pid} ({exc})")
            continue
        approved_by_book[slug][chapter].add(pid)

    if args.book:
        if args.book not in NT_MAX_CHAPTERS:
            parser.error(f"unknown book slug: {args.book}")
        approved_by_book = {args.book: approved_by_book.get(args.book, {})}

    if not any(approved_by_book.values()):
        print("No approved proposals for the requested scope.")
        return

    grand = {"applied": 0, "rejected": 0, "skipped": 0, "regression_failed": 0}
    for slug in sorted(approved_by_book.keys()):
        if slug not in NT_MAX_CHAPTERS:
            continue
        max_ch = NT_MAX_CHAPTERS[slug]
        per_chapter = approved_by_book[slug]
        if not per_chapter:
            continue
        print(f"\n=== {slug} ({sum(len(v) for v in per_chapter.values())} approved) ===")
        s = apply_book(slug, max_ch, per_chapter, args.dry_run)
        for k in ("applied", "rejected", "skipped"):
            grand[k] += s[k]
        if s.get("regression_failed"):
            grand["regression_failed"] += 1
        status = "DRY RUN" if args.dry_run else (
            "REVERTED" if s.get("reverted") else "OK"
        )
        print(f"  → {s['applied']} applied, {s['rejected']} rejected at apply. Status: {status}")
        if s["errors"]:
            print("  Errors / notes:")
            for e in s["errors"][:10]:
                print(f"    - {e}")
            if len(s["errors"]) > 10:
                print(f"    … and {len(s['errors']) - 10} more")

    print(
        f"\nTotal: applied {grand['applied']}, rejected {grand['rejected']} at apply, "
        f"regression_failed_books {grand['regression_failed']}"
    )


if __name__ == "__main__":
    main()
