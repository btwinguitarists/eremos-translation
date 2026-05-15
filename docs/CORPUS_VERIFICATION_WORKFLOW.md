# Corpus-Verification Workflow for `translator_decisions/` Docs

**Added:** 2026-05-16
**Trigger:** Leviticus end-of-book audit surfaced two doc-vs-corpus drift incidents (`sacrificial_vocabulary_2026-05.md` §5 locked `ลบบาป` while 144 occurrences of `ลบมลทินบาป` had already shipped across LEV+NUM; `goel_kinsman_redeemer_2026-05.md` locked `ผู้ไถ่ที่เป็นญาติ` while neither Ruth nor Leviticus uses that form anywhere).

---

## The rule

**No `translator_decisions/` doc graduates to `Status: LOCKED` until its proposed Thai forms have been grep-verified against the already-shipped corpus.**

The doc must include a `## Corpus-verified shipped forms` section produced by `scripts/verify_translator_decision.py`. The reviewer reads that section and decides one of:

1. **Doc matches corpus** → lock as-is.
2. **Doc differs from corpus, doc was wrong** → amend the doc to match shipped forms.
3. **Doc differs from corpus, corpus was wrong** → lock the doc, then file a corpus-revision PR that spot-edits the divergent verses before tagging the affected book(s).

Option 3 must be explicit and tracked; silent drift between doc and corpus is what this workflow exists to prevent.

---

## How to run the check

### When drafting a new doc

```bash
python3 scripts/verify_translator_decision.py \
  --form 'ผู้ไถ่' --form 'ญาติผู้ไถ่' --form 'ผู้แก้แค้นเลือด'
```

Paste the markdown table the script prints into the doc under a `## Corpus-verified shipped forms (YYYY-MM-DD)` heading. Add a one-line interpretation underneath: *"shipped corpus matches the lock"* or *"corpus uses X, doc revised to X"* or *"corpus uses X, spot-revision PR planned for verses [refs]"*.

### When amending an existing doc

```bash
python3 scripts/verify_translator_decision.py \
  --doc docs/translator_decisions/<topic>_<YYYY-MM>.md
```

The script extracts Thai forms from any markdown table in the doc whose cells contain Thai characters, then greps each one against `output/translations/*.json`. The output is the same markdown table; review it, then either update the doc tables or file the revision PR.

### Ad-hoc lookup (useful for spot-checks)

```bash
python3 scripts/verify_translator_decision.py --form 'ลบมลทินบาป' --form 'ลบบาป'
```

Counts occurrences per book, lists up to 5 sample references. No file IO beyond reading `output/translations/`.

---

## Why this matters

The Leviticus audit was the second time in 2026 that a locked doc and the shipped Thai diverged silently. The first (the Romans 16:25-27 / John 5:4 inclusion-variant gap, 2026-05-02) led to the strict `audit_inclusion_variants.py` gate. This workflow is the analogous gate for editorial-decision drift.

Per-chapter automated checks (`run_checks.py`) catch *consistency within a chapter* and *consistency with a locked rule when the rule is stored as code*. They do **not** catch:

- A doc-locked Thai form that no shipped verse uses (the doc author guessed at what's idiomatic without grepping).
- A doc-locked Thai form that the shipped majority *contradicts* (the doc was written after several books shipped, drawing on an author's mental model rather than the actual JSON).
- A cross-book divergence where Book A and Book B both render the same Hebrew differently, neither matching the doc.

The grep is cheap. The cleanup after a tag like `book-leviticus-v1` ships with a drifted lock is not cheap. Run the script before locking.

---

## Integration with `END_OF_BOOK_CHECKLIST.md`

The pre-flight grep is now part of §1 (mechanical) and §5 (lock the book). See `END_OF_BOOK_CHECKLIST.md` for the checklist hooks. The audit subagent prompt produced by `detect_book_complete.py` references this workflow when it surfaces a DECIDE-class item involving translator-decision docs.
