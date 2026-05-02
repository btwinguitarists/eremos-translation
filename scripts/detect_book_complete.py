#!/usr/bin/env python3
"""
End-of-book detection for ship_chapter.sh.

Reads data/production_order.json. If the just-shipped chapter is the LAST
chapter for its book:
  - prints a loud BOOK COMPLETE banner
  - writes output/.book_complete_signal with book code + timestamp
  - writes output/.book_complete_audit_prompt.md with a self-contained
    end-of-book audit prompt the user (or scripts/run_end_of_book_audit.sh)
    can pipe into a fresh Claude session
  - exits 1 so the calling shell halts (and any /loop wrapper detects failure)

The chapter has already been fully shipped (PR merged, TestFlight uploaded)
by the time this runs at the END of ship_chapter.sh — exit 1 only signals
"don't continue to next chapter; run end-of-book audit first."

Usage:
    python3 scripts/detect_book_complete.py <BOOK_CODE> <CHAPTER>

Exit codes:
    0 — not the last chapter; loop can continue
    1 — BOOK COMPLETE; loop must halt for end-of-book audit
    2 — invalid arguments
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BOOK_NAMES = {
    "MAT": "Matthew", "MRK": "Mark", "LUK": "Luke", "JHN": "John",
    "ACT": "Acts", "ROM": "Romans", "1CO": "1 Corinthians", "2CO": "2 Corinthians",
    "GAL": "Galatians", "EPH": "Ephesians", "PHP": "Philippians", "COL": "Colossians",
    "1TH": "1 Thessalonians", "2TH": "2 Thessalonians", "1TI": "1 Timothy",
    "2TI": "2 Timothy", "TIT": "Titus", "PHM": "Philemon", "HEB": "Hebrews",
    "JAS": "James", "1PE": "1 Peter", "2PE": "2 Peter", "1JN": "1 John",
    "2JN": "2 John", "3JN": "3 John", "JUD": "Jude", "REV": "Revelation",
}

BOOK_SLUGS = {
    "MAT": "matthew", "MRK": "mark", "LUK": "luke", "JHN": "john",
    "ACT": "acts", "ROM": "romans", "1CO": "1corinthians", "2CO": "2corinthians",
    "GAL": "galatians", "EPH": "ephesians", "PHP": "philippians", "COL": "colossians",
    "1TH": "1thessalonians", "2TH": "2thessalonians", "1TI": "1timothy",
    "2TI": "2timothy", "TIT": "titus", "PHM": "philemon", "HEB": "hebrews",
    "JAS": "james", "1PE": "1peter", "2PE": "2peter", "1JN": "1john",
    "2JN": "2john", "3JN": "3john", "JUD": "jude", "REV": "revelation",
}


_AUDIT_PROMPT_TEMPLATE = """# Eremos translation — end-of-book audit for __BOOK_NAME__ (__BOOK__)

You are spawned by `scripts/detect_book_complete.py` immediately after the last
chapter of __BOOK_NAME__ (__BOOK__ __TOTAL__) shipped via `scripts/ship_chapter.sh`.
Your job is the §2 (Editorial review) and §3 (External AI packet) steps from
`docs/END_OF_BOOK_CHECKLIST.md`. Do NOT change any translations — assess only.

## Working directory

You will be invoked from `~/thai-bible-ai`. All paths below are relative to it.

## Inputs to read

- `output/translations/__SLUG___*.json` — all __TOTAL__ translated chapters of __BOOK_NAME__
- `glossary.json` — running term registry
- `docs/translator_decisions/` — locked corpus decisions (READ-ONLY; do not rewrite)
- `RULES.md` §0 (SBLGNT-strictness) and §7 (review gates)
- `docs/END_OF_BOOK_CHECKLIST.md` — your charter
- Existing audits under `docs/end_of_book/` (matthew, mark, luke, acts, john, galatians, 1thessalonians)
  — use these as templates for shape and tone

## Mechanical gate (do these first)

Run before drafting:
- `python3 scripts/check_key_term_consistency.py` — must be clean across __BOOK_NAME__
- `python3 scripts/check_phrase_consistency.py` — must be clean across __BOOK_NAME__
- Verify every __BOOK__ chapter has a green per-chapter `output/check_reports/__SLUG___NN_review.md`
- Verify every __BOOK__ chapter has `output/back_translations/__SLUG___NN.json`
- `git status output/` — should be clean (post-2026-04-19 ship script auto-commits)

If the mechanical gate fails, STOP and report — do not draft the audit until the
maintainer clears the blocker.

## Outputs you must produce

### 1. `docs/end_of_book/__SLUG__/__BOOK___END_OF_BOOK_REVIEW___TODAY__.md`

Structured audit doc following the shape of:
- `docs/end_of_book/john/JHN_END_OF_BOOK_REVIEW_2026-04-30.md`
- `docs/end_of_book/galatians/GAL_END_OF_BOOK_REVIEW_2026-04-30.md`
- `docs/end_of_book/1thessalonians/1TH_END_OF_BOOK_REVIEW_2026-04-30.md`

Required structure:
- Title line `# __BOOK_NAME__ — End-of-Book Review`
- Date / Scope / Trigger / Mandate header
- `## Summary` with a bullet count of items reviewed and counts per status code
- One numbered section per cross-cutting item, each with a status tag in its
  heading: `**LOCKED**` / `**STABLE**` / `**REVIEW**` / `**DECIDE**`
- For STABLE-but-undocumented items, recommend a new
  `docs/translator_decisions/{topic}_{YYYY-MM}.md` doc
- For LOCKED items, list the verses that comply and any drift candidates

Status code legend:
- **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`
- **STABLE** — uniform/principled + rationale at verse-level (no corpus doc)
- **REVIEW** — defensible-but-worth-Ben's-confirmation
- **DECIDE** — Ben choice needed before tagging `book-__SLUG__-v1`

### 2. `docs/end_of_book/__SLUG__/external_review_items___BOOK__.md`

The handwritten items section the external AI packet builder consumes.
One `## Item A — ...` block per REVIEW or DECIDE item, with verse evidence
inline (Greek + Thai + English gloss as appropriate). Follow the shape of
`docs/end_of_book/john/external_review_items_JHN.md`. End each block with a
`**Question:**` or `**Two questions:**` block — these become the YAML
review questions auto-generated by `scripts/audit_items_to_yaml.py`.

### 3. External review packet

Run: `python3 scripts/build_external_review_packet.py __BOOK__ --items docs/end_of_book/__SLUG__/external_review_items___BOOK__.md`

This produces `docs/end_of_book/__SLUG__/external_review_packet___BOOK_____TODAY__.md`
sized for free-tier AI ceilings (~20K chars). Verify it built; do not commit
the packet if the items doc is empty.

### 4. YAML reviewer-question PR

After the items doc is finalized:

```
python3 scripts/audit_items_to_yaml.py __BOOK__
```

Emits one `output/review_questions___SLUG__/<id>.yml` per item, matching the
schema EremosVercel2's `shared/review-questions/` consumes. Every Thai field
is `__TODO_TH__` — fill those in (translate topic / question / text_prompt /
body to Thai) before copying to EremosVercel2.

Then in `~/EremosVercel2`:

```
git checkout main && git pull
git checkout -b feat/review-questions-__SLUG__-audit
cp ~/thai-bible-ai/output/review_questions___SLUG__/*.yml shared/review-questions/
git add shared/review-questions/
git commit -m "feat: add review questions from __BOOK__ end-of-book audit"
git push -u origin feat/review-questions-__SLUG__-audit
gh pr create --title "feat: add review questions from __BOOK__ end-of-book audit"
```

The PR body should list each new question id + tier + topic. The build-time
generator (`script/build-review-questions.ts`) regenerates
`shared/review-questions-generated.ts` on `npm run check` / `npm run build`.

## Branch + PR convention

1. `git checkout -b end-of-book-review-__SLUG__-audit` (note the `-audit` suffix —
   keeps it distinct from any chapter-ship branches)
2. `git add docs/end_of_book/__SLUG__/`
3. `git commit -m "docs(__BOOK__): end-of-book editorial review + external AI packet"`
4. `git push -u origin end-of-book-review-__SLUG__-audit`
5. `gh pr create --title "docs(__BOOK__): end-of-book editorial review" --body "..."`
   — include in the body: status-code counts, list of REVIEW/DECIDE items,
   pointer to the items doc, and a checklist for Ben to confirm + tag
   `book-__SLUG__-v1` after merge

## Hand-off

When you finish:
- Print the PR URL
- Print a one-paragraph summary: counts per status code, list of items
  flagged DECIDE (these block the v1 tag), list of new translator_decisions
  docs you recommend
- Exit cleanly. Do NOT resume the translation loop — `book-__SLUG__-v1`
  tagging is Ben's manual step after he reviews this audit.

## Constraints

- Do NOT modify any translation JSON files
- Do NOT rewrite `docs/TRANSLATION_WORKFLOW.md`, `docs/END_OF_BOOK_CHECKLIST.md`,
  or `RULES.md` (they are stable contracts — see auto-memory
  `feedback_translation_instructions_readonly.md`)
- DO append to `docs/translator_decisions/` if a DECIDE item resolves into
  a new lock — but only if the audit document explicitly recommends it
- Always create a PR; never push directly to main (per
  `feedback_pr_creation.md`)
"""


def write_audit_prompt(book: str, book_name: str, total: int) -> Path:
    """Render the end-of-book audit prompt for `book` and write it next to
    the .book_complete_signal file. The prompt is self-contained — pipe it
    into `claude` (interactive or `--print`) to spawn the audit agent.
    """
    slug = BOOK_SLUGS.get(book, book.lower())
    today = date_today_iso()
    prompt = (
        _AUDIT_PROMPT_TEMPLATE
        .replace("__BOOK_NAME__", book_name)
        .replace("__BOOK__", book)
        .replace("__SLUG__", slug)
        .replace("__TOTAL__", str(total))
        .replace("__TODAY__", today)
    )
    out = ROOT / "output" / ".book_complete_audit_prompt.md"
    out.write_text(prompt, encoding="utf-8")
    return out


def date_today_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def main() -> None:
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <BOOK_CODE> <CHAPTER>", file=sys.stderr)
        sys.exit(2)
    book = sys.argv[1].upper()
    try:
        chapter = int(sys.argv[2])
    except ValueError:
        print(f"chapter must be integer, got: {sys.argv[2]}", file=sys.stderr)
        sys.exit(2)

    order_path = ROOT / "data" / "production_order.json"
    if not order_path.exists():
        print(f"[detect_book_complete] {order_path} missing — skipping check", file=sys.stderr)
        sys.exit(0)

    order = json.loads(order_path.read_text())
    chapters_in_book = [e["chapter"] for e in order["order"] if e["book"] == book]
    if not chapters_in_book:
        print(f"[detect_book_complete] {book} not in production_order.json — skipping check", file=sys.stderr)
        sys.exit(0)

    max_chapter = max(chapters_in_book)
    if chapter < max_chapter:
        # not last — loop continues
        sys.exit(0)

    # BOOK COMPLETE
    book_name = BOOK_NAMES.get(book, book)
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

    signal_path = ROOT / "output" / ".book_complete_signal"
    signal_path.write_text(
        f"book={book}\nname={book_name}\nchapter={chapter}\ntotal={max_chapter}\nts={timestamp}\n"
    )
    audit_prompt_path = write_audit_prompt(book, book_name, max_chapter)

    bar = "=" * 72
    print()
    print(bar)
    print(f"    \U0001f4d6  BOOK COMPLETE  —  {book_name} ({book})  —  all {max_chapter} chapters shipped (source)")
    print(bar)
    print("  Source committed to thai-bible-ai/main.")
    print("  Bundle / Vercel / iOS deferred to ship_book.sh at end of audit cycle.")
    print()
    print("  Next steps (most are automatic — ship_chapter.sh orchestrates):")
    print()
    print("    §1  Mechanical    — auto-runs in run_end_of_book_audit.sh (gates the audit)")
    print("    §2  Editorial     — auto-launched: claude --print < audit_prompt.md")
    print("                      (subagent writes docs/end_of_book/<book>/*_REVIEW_*.md)")
    print("    §3  External AI   — packet auto-built; Ben pastes into Grok + 1 other AI")
    print("    §4  Revisions     — Ben implements + lands a small PR if needed")
    print(f"    §5  Lock the book — `bash scripts/ship_book.sh {book}`")
    print(f"                      (bundle PR + iOS bump + tag book-{BOOK_SLUGS.get(book, book.lower())}-v1)")
    print()
    print(f"  Marker written: {signal_path.relative_to(ROOT)}")
    print(f"  Audit prompt:   {audit_prompt_path.relative_to(ROOT)}")
    print()
    print(f"  ship_chapter.sh will now auto-launch the audit unless --skip-audit was set.")
    print(f"  /loop halts after the audit so Ben can do external AI review + decide revisions.")
    print(bar)
    sys.exit(1)


if __name__ == "__main__":
    main()
