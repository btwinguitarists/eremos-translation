# End-of-Book Review Checklist

**Trigger**: when the last chapter of a NT book ships (e.g., MAT 28 for Matthew, MRK 16 for Mark, LUK 24 for Luke).

**Purpose**: catch corpus-level editorial decisions and quality gaps that per-chapter checks can't see. Per-chapter automated checks catch lemma consistency and saying-level synoptic alignment, but they don't catch editorial *why* decisions. End-of-book is the natural moment to lock in choices before they compound across books (e.g., ἐκκλησία in Matthew sets the precedent for Acts + the Pauline epistles).

This checklist is informational. Nothing in the codebase enforces running it — but `MEMORY.md` has a project-memory entry pointing here, so any Claude session shipping the last chapter of a book will be reminded to check.

---

## 1. Mechanical (do these first; cheap)

- [ ] All chapters have green `output/check_reports/<slug>_NN_review.md` (per-chapter automated checks passed)
- [ ] All chapters have `output/back_translations/<slug>_NN.json` (BT done; the post-2026-04-19 ship gate enforces this, but worth confirming)
- [ ] `python3 scripts/check_key_term_consistency.py` is clean across the entire book — no undocumented lemma variance
- [ ] `git status output/` is clean (no orphaned source files; the post-2026-04-19 ship script auto-commits, but verify)

## 2. Editorial review (the substantive part)

Spawn a fresh Claude session with this prompt template:

> Eremos translation: end-of-book review for **{BOOK}**. Read all **{N}** translations + `glossary.json`. Identify cross-cutting editorial decisions worth deliberate revisit — e.g., ἐκκλησία → คริสตจักร vs. ที่ประชุม, βασιλεία → อาณาจักร, talent units, honorific patterns for non-divine figures (kings, masters, etc.), translation of culturally-loaded terms (γέεννα, σάρξ, παρουσία). For each cross-cutting choice: is the rationale documented at verse-level (key_decisions/notes) or in `docs/translator_decisions/`, or did it drift into convention? Surface findings for Ben's decision. Do NOT change any translations — assess only.

For each editorial decision flagged:
- **Rationale already documented at verse-level** → keep as-is, no action needed
- **Not documented** → write `docs/translator_decisions/{topic}_{YYYY-MM}.md` recording the choice + reasoning + alternatives considered
- **Rationale now questioned** → Ben decides whether to revise the corpus

## 3. External review (do at least one)

- [ ] At least one external AI review (Grok, ChatGPT, Gemini, etc.) — paste chapter JSONs, surface concerns, cross-check against `RULES.md`. Past pattern: external AIs frequently restate things the project already does, but occasionally surface a real corpus-level question (see MAT 18 ἐκκλησία flagging in this session).
- [ ] Native-speaker Thai review on selected chapters (per `RULES.md §7`)
- [ ] Theological reviewer review (per `RULES.md §7`)

## 4. Lock the book

When all of the above is reviewed and any decisions logged:

- [ ] Update `RULES.md` if a corpus-level decision warrants documentation in the canonical rules
- [ ] Update `glossary.json` if any term renderings were corrected
- [ ] Tag the commit: `git tag book-{slug}-v1 && git push --tags` (e.g., `book-matthew-v1`)
- [ ] If editorial-decision docs were written, ensure they're committed under `docs/translator_decisions/`

---

## Why this matters (history)

This checklist was added 2026-04-19 after an external AI review of MAT 18 surfaced ἐκκλησία → คริสตจักร as a corpus-level editorial question (MAT 16:18 + MAT 18:17 + future Acts/epistles occurrences). The verse-level rationale was documented but the corpus-level decision wasn't. Per-chapter checks couldn't catch it because both verses use the same rendering — consistency-within-corpus passes, but the editorial *whether* doesn't get reviewed.

End-of-book is the right moment to catch this kind of thing before it compounds across books.

## What to do if a decision warrants change after the book ships

If a post-ship corpus revision is decided (rare):

1. Create a feature branch on `thai-bible-ai`
2. Edit affected verses across the book (use `scripts/grep`-style search to find all occurrences)
3. Re-run all checks for affected chapters
4. Re-run `build_eremos_bundle.py`
5. Ship a "rev" commit per chapter touched
6. Update the `book-{slug}-v1` tag to `book-{slug}-v2`

Better to make these decisions BEFORE tagging v1.
