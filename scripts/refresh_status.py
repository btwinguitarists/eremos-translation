#!/usr/bin/env python3
"""
Regenerate STATUS.md at the repo root — the daily-glance file.

Pulls live state from the repo and writes one human-readable summary so the
maintainer doesn't have to remember which command surfaces which fact.

Sources:
  - scripts/next_chapter.py --json   (next chapter + per-book progress)
  - git log on output/translations/  (last shipped chapter + date)
  - output/check_reports/            (most recent check report)
  - ~/Desktop/eremos-translation-pending-decisions.md   (if present)

Usage:
  python3 scripts/refresh_status.py
"""
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
CHECK_REPORTS = ROOT / "output" / "check_reports"
STATUS_FILE = ROOT / "STATUS.md"
DESKTOP_PENDING = Path.home() / "Desktop" / "eremos-translation-pending-decisions.md"
DESKTOP_PENDING_TH = Path.home() / "Desktop" / "eremos-translation-pending-decisions-TH.md"

BOOK_NAMES = {
    # NT
    "MAT": "Matthew", "MRK": "Mark", "LUK": "Luke", "JHN": "John", "ACT": "Acts",
    "ROM": "Romans", "1CO": "1 Corinthians", "2CO": "2 Corinthians",
    "GAL": "Galatians", "EPH": "Ephesians", "PHP": "Philippians", "COL": "Colossians",
    "1TH": "1 Thessalonians", "2TH": "2 Thessalonians",
    "1TI": "1 Timothy", "2TI": "2 Timothy", "TIT": "Titus", "PHM": "Philemon",
    "HEB": "Hebrews", "JAS": "James", "1PE": "1 Peter", "2PE": "2 Peter",
    "1JN": "1 John", "2JN": "2 John", "3JN": "3 John", "JUD": "Jude", "REV": "Revelation",
    # OT
    "GEN": "Genesis", "EXO": "Exodus", "LEV": "Leviticus", "NUM": "Numbers",
    "DEU": "Deuteronomy", "JOS": "Joshua", "JDG": "Judges", "RUT": "Ruth",
    "1SA": "1 Samuel", "2SA": "2 Samuel", "1KI": "1 Kings", "2KI": "2 Kings",
    "1CH": "1 Chronicles", "2CH": "2 Chronicles", "EZR": "Ezra", "NEH": "Nehemiah",
    "EST": "Esther", "JOB": "Job", "PSA": "Psalms", "PRO": "Proverbs",
    "ECC": "Ecclesiastes", "SNG": "Song of Songs", "ISA": "Isaiah", "JER": "Jeremiah",
    "LAM": "Lamentations", "EZK": "Ezekiel", "DAN": "Daniel", "HOS": "Hosea",
    "JOL": "Joel", "AMO": "Amos", "OBA": "Obadiah", "JON": "Jonah",
    "MIC": "Micah", "NAM": "Nahum", "HAB": "Habakkuk", "ZEP": "Zephaniah",
    "HAG": "Haggai", "ZEC": "Zechariah", "MAL": "Malachi",
}


def run(cmd, cwd=ROOT):
    try:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, check=False
        )
        return result.stdout.strip()
    except FileNotFoundError:
        return ""


def get_next_chapter_status():
    """Run scripts/next_chapter.py --json and return the parsed payload."""
    raw = run([sys.executable, "scripts/next_chapter.py", "--json"])
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def get_progress_summary():
    """Run scripts/next_chapter.py --status and return the human summary."""
    return run([sys.executable, "scripts/next_chapter.py", "--status"])


def get_last_shipped():
    """Most recent commit touching output/translations/, with date + subject."""
    log = run([
        "git", "log", "-1", "--format=%h | %ad | %s",
        "--date=short", "--", "output/translations/",
    ])
    return log or "(no commits on output/translations/ yet)"


def get_recent_check_reports(n=3):
    """Most recently modified check reports."""
    if not CHECK_REPORTS.is_dir():
        return []
    reports = sorted(
        CHECK_REPORTS.glob("*_review.md"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return reports[:n]


def count_pending_sections(path):
    """Count `## ` sections in a pending-decisions file."""
    if not path.is_file():
        return None
    text = path.read_text()
    return len(re.findall(r"^##\s", text, re.MULTILINE))


def render_status():
    today = date.today().isoformat()
    next_status = get_next_chapter_status()
    progress = get_progress_summary()
    last_shipped = get_last_shipped()
    recent_reports = get_recent_check_reports()
    en_pending = count_pending_sections(DESKTOP_PENDING)
    th_pending = count_pending_sections(DESKTOP_PENDING_TH)

    if next_status:
        book_code = next_status.get("book", "?")
        next_book = BOOK_NAMES.get(book_code, book_code)
        next_chapter = next_status.get("chapter", "?")
        next_phase = next_status.get("phase", "?")
        next_line = f"**{next_book} {next_chapter}** ({next_phase}) — code `{book_code}`"
    else:
        next_line = "(could not resolve next chapter — run `python3 scripts/next_chapter.py --status` directly)"

    # Language-aware extract command. OT books use extract_book_hebrew.py
    # (Hebrew/Aramaic source from MACULA Hebrew); NT books use extract_book.py
    # (Greek source from MACULA Greek + SBLGNT).
    OT_CODES = {
        "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT",
        "1SA", "2SA", "1KI", "2KI", "1CH", "2CH", "EZR", "NEH",
        "EST", "JOB", "PSA", "PRO", "ECC", "SNG", "ISA", "JER",
        "LAM", "EZK", "DAN", "HOS", "JOL", "AMO", "OBA", "JON",
        "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL",
    }
    next_book_code = next_status.get("book", "") if next_status else ""
    is_ot = next_book_code in OT_CODES
    extract_script = "extract_book_hebrew.py" if is_ot else "extract_book.py"
    language_note = (
        f"_Note: `{next_book_code}` is an OT book — uses `extract_book_hebrew.py` "
        f"(Hebrew/Aramaic source from MACULA Hebrew). For NT books use `extract_book.py`._"
        if is_ot else
        f"_Note: `{next_book_code}` is an NT book — uses `extract_book.py` "
        f"(Greek source from MACULA Greek + SBLGNT). For OT books use `extract_book_hebrew.py`._"
    )

    recent_lines = []
    for p in recent_reports:
        rel = p.relative_to(ROOT)
        mtime = date.fromtimestamp(p.stat().st_mtime).isoformat()
        recent_lines.append(f"- `{rel}` ({mtime})")
    recent_block = "\n".join(recent_lines) if recent_lines else "(none yet)"

    pending_lines = []
    if en_pending is not None:
        pending_lines.append(
            f"- `~/Desktop/eremos-translation-pending-decisions.md` — **{en_pending} sections**"
        )
    if th_pending is not None:
        pending_lines.append(
            f"- `~/Desktop/eremos-translation-pending-decisions-TH.md` — **{th_pending} sections**"
        )
    pending_block = "\n".join(pending_lines) if pending_lines else "(no Desktop pending-decisions files found)"

    return f"""# STATUS — Eremos Translation

> Auto-generated by `scripts/refresh_status.py`. Re-run that to refresh.
> **Last updated:** {today}

## Next chapter to translate

{next_line}

To start translating, use the trigger phrase **"Eremos Translation: next"** in a Claude session, or run manually:

```bash
python3 scripts/{extract_script} --book <BOOK> --chapter <N>
python3 scripts/enrich_with_uw.py --book <BOOK> --chapter <N>
```

{language_note}

## Progress

```
{progress}
```

## Last shipped

{last_shipped}

## Most recent check reports

{recent_block}

## Pending decisions for translator review

{pending_block}

These rolling artifacts on Desktop are the working buffer between the maintainer and Claude per the translation rhythm. They are **not** for sharing with reviewers — the reviewer-facing files are `docs/reviewer_packet_en_*.md` and `docs/reviewer_packet_th_*.md`.

## Where things live

| Audience | File you send |
|---|---|
| **Per-verse review by a Thai reader / scholar / pastor** (each verse has a `> ___` block to type comments into; bilingual TH/EN instructions at the top) | `output/feedback/<slug>.md` |
| Verses-only edition for impressionistic / scholarly reading (no comment blocks) | `output/plain/<slug>.md` |
| Annotated reading edition (verses + AI-generated บริบท commentary, for end users / app readers) | `output/reader/<slug>.md` |
| External AI, per-chapter spot-check | `docs/CHAPTER_REVIEW_PROMPT.md` + paste chapter JSON |
| External AI, end-of-book review | `docs/end_of_book/<book>/external_review_packet_<BOOK>_*.md` |
| English-speaking Greek / theological scholar (project context + locked decisions + worksheet) | `docs/reviewer_packet_en_*.md` (latest) |
| Thai native-speaker reader / theological reviewer (project context FAQ) | `docs/reviewer_packet_th_*.md` (latest, **needs editorial pass first**) |

## Quick commands

| Want to... | Run |
|---|---|
| Confirm next chapter | `python3 scripts/next_chapter.py --status` |
| Run all checks on a chapter | `python3 scripts/run_checks.py --book <BOOK> --chapter <N>` |
| Ship a chapter (full pipeline) | `bash scripts/ship_chapter.sh <BOOK> <N>` |
| Web-only ship (skip TestFlight) | `bash scripts/ship_chapter.sh <BOOK> <N> --skip-testflight` |
| Refresh this STATUS.md | `python3 scripts/refresh_status.py` |
| Regenerate reader + plain + feedback markdown (all books, all modes) | `python3 scripts/render_reader.py` |
| Regenerate one mode for one book | `python3 scripts/render_reader.py --book <BOOK> --mode <plain\\|feedback\\|reader>` |
| Build reviewer packet (EN) | `python3 scripts/build_consolidated_reviewer_packet.py MAT MRK LUK ACT --lang en` |
| Build reviewer packet (TH) | `python3 scripts/build_consolidated_reviewer_packet.py MAT MRK LUK ACT --lang th` |
| Build per-book external AI packet | `python3 scripts/build_external_review_packet.py <BOOK> --items docs/end_of_book/<book>/external_review_items_<BOOK>.md` |
| End-of-book review walkthrough | See `docs/END_OF_BOOK_CHECKLIST.md` |

## Repo layout (post-reorg)

```
docs/
├── (live working docs at top level)
├── translator_decisions/   ← locked corpus-level rules (sacred)
├── end_of_book/<book>/     ← per-book audit + external-review packet + items
└── archive/                ← one-off historical docs (not in flow)

scripts/
├── (live pipeline scripts at top level)
└── backfills/              ← one-time data fixers, kept for traceability
```
"""


def main():
    text = render_status()
    STATUS_FILE.write_text(text)
    print(f"Wrote {STATUS_FILE}")
    print(f"  {len(text):,} chars / {text.count(chr(10)) + 1:,} lines")


if __name__ == "__main__":
    main()
