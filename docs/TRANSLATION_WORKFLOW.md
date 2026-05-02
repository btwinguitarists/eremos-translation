# Eremos Translation — Chapter Workflow

End-to-end process for translating a new Bible chapter from original languages (Koine Greek for NT, Biblical Hebrew for OT) to Thai and surfacing it in the Eremos app.

**Before translating anything, read [RULES.md](../RULES.md)** — the canonical translation rules (derived from SIL/Wycliffe/UBS standards). Every chapter must conform; the check scripts below enforce what can be enforced mechanically.

Companion doc in the Eremos repo: `~/EremosVercel2/docs/eremos-translation-workflow.md`

---

## Two-repo architecture

```
~/thai-bible-ai/                     ~/EremosVercel2/
┌──────────────────────┐             ┌──────────────────────┐
│ SBLGNT + MACULA TSV  │             │ server/data/         │
│ BSB reference        │    bundle   │   eremos_translation │
│                      │   ────────▶ │   .json              │
│ extract_mark.py      │             │                      │
│ translate_mark.py    │             │ ensureEremos         │
│ build_eremos_bundle  │             │   TranslationImported│
│ render_markdown.py   │             │ → Supabase           │
└──────────────────────┘             └──────────────────────┘
     AI translation                        Eremos app
     pipeline (private)                    (public, per-verse popup)
```

---

## One-time setup

Already done, but for reference:

1. Source repos cloned in `~/thai-bible-ai/sources/`:
   - `SBLGNT/` — Greek NT with morphological tagging (CC BY 4.0)
   - `macula-greek/` — syntax + semantic annotations (CC BY 4.0)
   - `bsb-text/bsb.txt` — Berean Standard Bible plain text (CC0)
2. Supabase tables `eremos_translation_verses` and `translation_feedback` already exist (migration 0004).
3. Python deps: `pip3 install anthropic --break-system-packages` (only needed when using API mode).

---

## Translating a new chapter — step by step

You can either specify the chapter or let the pipeline pick the next one in production order:

```bash
# specific chapter
python3 scripts/extract_book.py --book MRK --chapter 6

# OR — resolve the next chapter automatically based on production order
python3 scripts/next_chapter.py
# → "MRK 6"
```

`next_chapter.py` reads `data/production_order.json` (260 NT chapters in SIL-style order) and returns the first one not yet in `output/translations/`. Run with `--status` for a full progress report, `--pretty` for human-readable, or `--json` for the structured entry.

The trigger phrase **"Eremos Translation: next"** uses this resolver automatically.

Example: translating **Mark 2**.

### 1. Extract verses from MACULA + enrich with uW Translation Notes

```bash
cd ~/thai-bible-ai
python3 scripts/extract_book.py --book 1TI --chapter 3        # single chapter
python3 scripts/enrich_with_uw.py --book 1TI --chapter 3      # scholarly context
```

The first script writes `output/<book-slug>/<slug>_<NN>.json` with word-by-word morphology, BSB reference, hapax flags, Louw-Nida semantic domains.

The second fetches CC-BY-SA unfoldingWord Translation Notes for the chapter and writes TWO files:

- `output/uw_notes/<slug>_FRONT.md` — book-level introduction (author, audience, date, themes, outline, translation issues). **Read this FIRST before any chapter of a book.** SIL/Wycliffe pro practice — translators always start with the book overview before chapter-specific work.
- `output/uw_notes/<slug>_<NN>.md` — chapter-level verse-by-verse scholarly commentary. Read AFTER the book intro for chapter-specific cruxes.

Both are CC-BY-SA reference material — read for context, never copy wording into our output (would inherit CC-BY-SA, breaking our CC0 license). See RULES.md §8.

### 2. Translate the chapter

Full philosophy and rules live in [RULES.md](../RULES.md). Quick summary:
- Optimal equivalence (BSB-style) — faithful to Greek + natural Thai
- Translate FROM the Greek; BSB English is a sanity check, not a source
- Never read any Thai translation (including TNBT) during drafting
- Divine subjects use ราชาศัพท์; key terms follow the RULES.md §4 glossary
- Flag every hapax, textual variant, OT citation, and interpretive decision

**Option A — Manual via Claude in conversation (higher quality, current default):**

1. Open a Claude conversation
2. Claude reads RULES.md and the extracted verse data for the chapter
3. Claude reads the nearest prior chapter's output for style consistency
4. Claude produces Thai for all verses in the pattern of `output/translations/mark_01.json`
5. Save the result to `output/translations/<slug>_<NN>.json`

**Option B — Claude API (batched, faster for scaling up):**

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 scripts/translate_mark.py --chapter 2
```

(Script currently tied to Mark — generalize to `translate_book.py` once API mode becomes the default.)

### 3. Run the check cadence (MANDATORY before shipping)

```bash
python3 scripts/run_checks.py --book 1TI --chapter 3
```

Runs all five checks in sequence and produces an aggregate report at `output/check_reports/<slug>_<NN>_review.md`:

1. **Key-term consistency** (`check_key_term_consistency.py`) — scans all translations, per-lemma rendering report, flags RULES.md §4 violations and undocumented multi-renderings
2. **TNBT structural comparison** (`check_against_tnbt.py`) — verse-by-verse length/sentence-count signals against open-licensed Thai NT. Vocabulary divergence expected (TNBT uses Buddhist register); structural divergence is the signal.
3. **OT citation acknowledgment** (`check_ot_citations.py`) — for known NT-quotes-OT verses, confirms we've noted the OT source and LXX/MT relation
4. **Synoptic parallel check** (`check_parallel_passages.py`) — flags divergent renderings of the same saying across synoptic gospels (activates once 2+ gospels are in)
5. **Back-translation check** (`check_back_translation.py`) — Claude API translates our Thai back to English, diffs against BSB, flags undocumented divergence. **Requires `ANTHROPIC_API_KEY`.** Gracefully skipped if unset.

**Ship criterion:** no flagged checks. Flagged items must be resolved by editing the chapter's notes/decisions, or documented as acceptable.

### 4. Generate review markdown (optional, for human review)

```bash
python3 scripts/render_markdown.py --chapter 3
```

Writes `docs/<slug>_<NN>_review.md` with parallel Greek/English/Thai + collapsible decisions. Share with Thai-speaking reviewers.

### 5. Build the Eremos bundle

```bash
python3 scripts/build_eremos_bundle.py
```

Combines all `output/translations/mark_XX.json` files into a single `~/EremosVercel2/server/data/eremos_translation.json` — the file Eremos imports at server boot.

### 6. Ship — split: per-chapter source-only + per-book lock-and-deploy (refactored 2026-05-02)

The ship pipeline is split into two stages so that bundle / Vercel / iOS / Android updates land at the **book boundary** rather than per-chapter. Rationale: with no active per-chapter reviewers (Ben + AI lead the work, human review is async), per-chapter native-app builds were producing ~16 PRs + ~16 iOS bumps per Romans-sized book and silently exhausting the TestFlight cap (iris-code 90382). The book-boundary ship consolidates this into 1 of each per book and makes "what users see in the app" atomic with the audited + tagged book content.

#### 6a. `ship_chapter.sh` — source-only per-chapter

```bash
bash scripts/ship_chapter.sh MRK 5
bash scripts/ship_chapter.sh PHM 1 --skip-audit   # at end-of-book, defer audit
```

What it does, in order, without intermediate confirmation:

1. **Gates** — runs `run_checks.py` (all 9 checks must pass) + verifies thai-bible-ai is on `main`
2. **Regenerates** `HASHES.md` + `output/reader/<book>.md`
3. **Commits source** to thai-bible-ai/main: translation JSON, back-translations, check reports, uW notes, glossary growth, OT-citation registry, regenerated reader/plain/feedback markdown
4. **Asserts** the source commit reached origin/main (PR #60/#61 incident guard)
5. **Detects book completion** via `detect_book_complete.py`. If this is the last chapter of the book:
   - **Auto-launches** `run_end_of_book_audit.sh BOOK_CODE --print` — spawns a fresh Claude session via `claude --print` that runs §1 mechanical gate + §2 editorial review + §3 external AI packet, opening an audit PR for review.
   - Halts /loop (exit 1) so Ben can do the external AI review and decide on revisions.
   - Pass `--skip-audit` to defer the auto-audit (rare; manual `bash scripts/run_end_of_book_audit.sh BOOK_CODE` later).

What it does **NOT** do (deferred to `ship_book.sh`): bundle rebuild, EremosVercel2 PR, Vercel deploy, iOS bump, TestFlight upload, Android Play upload, `book-<slug>-v1` tag. The compatibility no-ops `--skip-testflight` and `--skip-merge` are accepted but print a one-line note (legacy /loop wrappers stay backward-compatible).

Total runtime: ~5-15 sec for non-end-of-book chapters; +5-15 min when the auto-audit fires.

#### 6b. `ship_book.sh` — book-boundary lock-and-deploy

```bash
bash scripts/ship_book.sh PHM
bash scripts/ship_book.sh ROM --skip-testflight   # bundle/Vercel only
bash scripts/ship_book.sh ROM --skip-tag          # ship without v1 tag (revisions pending)
```

Run this after:
1. All chapters of the book have shipped to thai-bible-ai/main via `ship_chapter.sh`
2. End-of-book audit PR has merged
3. Any AI-review revisions have landed

What it does:

1. **Gates** — verifies all chapters of BOOK_CODE are translated, runs `audit_inclusion_variants --strict`, verifies thai-bible-ai is on main
2. **Pulls latest main** in `~/EremosVercel2/`
3. **Rebuilds bundle** (`build_eremos_bundle.py` — book-agnostic, picks up every translated chapter currently in the corpus)
4. If bundle changed: branches `feat/book-ship-<slug>`, commits, pushes, opens PR, **auto-merges**
5. **Bumps** `CURRENT_PROJECT_VERSION` (last value + 1)
6. `npm run build && npx cap sync ios`
7. `xcodebuild archive → exportArchive → xcrun altool --upload-app`
8. **Tags** `book-<slug>-v1` in thai-bible-ai + pushes tag

Total runtime: ~6-10 min including TestFlight upload. ~1 min with `--skip-testflight`.

**Android** (Play Console upload) is a separate manual step — see `reference_eremos_ship_recipe.md` (auto-memory) for the `gradle bundleRelease` + `play_upload.py` sequence. The script lives in `~/.appstoreconnect/`, not in this repo.

**Note:** The schema never changes for new chapters — only the bundle file grows. `ensureEremosTranslationImported()` auto-detects when the bundle has new verses and upserts them on (book, chapter, verse) conflict. The unique index (migration 0005) guarantees no duplicates.

### 7. Refreshing existing content

When you **add** a chapter, the import auto-syncs on next server boot (bundle length > DB count triggers upsert).

When you **edit** an already-imported verse (fix a typo, refine wording) without changing the verse count, the import's count-based heuristic treats it as in-sync and skips. To force a refresh:

1. Open Supabase Studio → SQL editor
2. Run `TRUNCATE eremos_translation_verses;`
3. Trigger a server restart (push a no-op commit or hit the Vercel redeploy button)

Next boot will repopulate from the current bundle. Safe operation — the translation data lives in the bundle file, not the DB.

---

## Reference: File paths

| What | Path |
|------|------|
| **Rules (read before translating)** | `~/thai-bible-ai/RULES.md` |
| Source texts (read-only clones) | `~/thai-bible-ai/sources/` (SBLGNT, macula-greek, bsb-text, TNBT) |
| Extraction (all books) | `~/thai-bible-ai/scripts/extract_book.py` |
| Translation script (Mark only, legacy) | `~/thai-bible-ai/scripts/translate_mark.py` |
| **Check orchestrator** | `~/thai-bible-ai/scripts/run_checks.py` |
| Individual checks | `~/thai-bible-ai/scripts/check_*.py` |
| Glossary builder | `~/thai-bible-ai/scripts/build_glossary.py` |
| Bundle builder | `~/thai-bible-ai/scripts/build_eremos_bundle.py` |
| Review renderer | `~/thai-bible-ai/scripts/render_markdown.py` |
| Key-term glossary (generated) | `~/thai-bible-ai/glossary.json` |
| OT citation database | `~/thai-bible-ai/data/nt_ot_citations.json` |
| Synoptic parallel database | `~/thai-bible-ai/data/synoptic_parallels.json` |
| Per-verse extracted data | `~/thai-bible-ai/output/<slug>/<slug>_<NN>.json` |
| Per-chapter translations | `~/thai-bible-ai/output/translations/<slug>_<NN>.json` |
| Check reports | `~/thai-bible-ai/output/check_reports/` |
| Review markdown | `~/thai-bible-ai/docs/<slug>_<NN>_review.md` |
| Eremos bundle (target) | `~/EremosVercel2/server/data/eremos_translation.json` |
| Eremos schema | `~/EremosVercel2/shared/models/eremos.ts` (tables: `eremosTranslationVerses`, `translationFeedback`) |
| Eremos import fn | `~/EremosVercel2/server/bible-import.ts` → `ensureEremosTranslationImported()` |
| Eremos API routes | `~/EremosVercel2/server/routes.ts` (search: `/api/eremos-translation`) |
| Eremos popup UI | `~/EremosVercel2/client/src/components/ChapterReader.tsx` (search: `translationSheet.eremos`) |
| Eremos admin feedback panel | `~/EremosVercel2/client/src/pages/Admin.tsx` (search: `TranslationFeedbackPanel`) |

---

## Book code reference (NT)

Eremos uses standard 3-letter uppercase codes. Same codes are used in the bundle JSON and in MACULA's `ref` field.

| Book | Code | Chapters |
|------|------|----------|
| Matthew | MAT | 28 |
| Mark | MRK | 16 |
| Luke | LUK | 24 |
| John | JHN | 21 |
| Acts | ACT | 28 |
| Romans | ROM | 16 |
| 1 Corinthians | 1CO | 16 |
| 2 Corinthians | 2CO | 13 |
| Galatians | GAL | 6 |
| Ephesians | EPH | 6 |
| Philippians | PHP | 4 |
| Colossians | COL | 4 |
| 1 Thessalonians | 1TH | 5 |
| 2 Thessalonians | 2TH | 3 |
| 1 Timothy | 1TI | 6 |
| 2 Timothy | 2TI | 4 |
| Titus | TIT | 3 |
| Philemon | PHM | 1 |
| Hebrews | HEB | 13 |
| James | JAS | 5 |
| 1 Peter | 1PE | 5 |
| 2 Peter | 2PE | 3 |
| 1 John | 1JN | 5 |
| 2 John | 2JN | 1 |
| 3 John | 3JN | 1 |
| Jude | JUD | 1 |
| Revelation | REV | 22 |

For OT: will need to add ETCBC/BHSA Hebrew data and MACULA Hebrew when we get there.

---

## Output JSON shape (reference)

Each verse in `output/translations/mark_XX.json` and in the Eremos bundle:

```json
{
  "reference": "Mark 1:1",
  "chapter": 1,
  "verse": 1,
  "greek": "Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ χριστοῦ.",
  "bsb_english": "This is the beginning of the gospel of Jesus Christ, the Son of God.",
  "translation": {
    "thai": "จุดเริ่มต้นของข่าวประเสริฐเรื่องพระเยซูคริสต์",
    "thai_literal": "...",
    "key_decisions": [
      { "greek": "...", "thai": "...", "rationale": "..." }
    ],
    "notes": "TEXTUAL VARIANT: ..."
  }
}
```

The Eremos bundle strips this down to:

```json
{
  "book": "MRK",
  "chapter": 1,
  "verse": 1,
  "thai": "...",
  "thai_literal": "...",
  "key_decisions": [...],
  "notes": "..."
}
```

---

## TestFlight is now part of `ship_chapter.sh`

TestFlight upload is integrated into the ship pipeline (step 7 above). Per the updated `reference_appstoreconnect.md`, **per-chapter TestFlight is allowed** for Eremos Translation chapters because each ships meaningful new content. The "confirm before TestFlight" rule still applies to non-translation features.

If you want to ship multiple chapters before one TestFlight upload, use `--skip-testflight` on each chapter except the last.

---

## Pre-ship checklist

Manual confirmation before committing the chapter (automated checks cover most of this):

- [ ] `python3 scripts/run_checks.py --book <CODE> --chapter <N>` returns no flags
- [ ] All verses present for the chapter (matches SBLGNT verse count)
- [ ] Divine subjects use ราชาศัพท์ register throughout
- [ ] Every hapax legomenon has a rationale entry
- [ ] Every textual variant vs. BSB is flagged in `notes`
- [ ] Every OT citation/allusion is acknowledged (automated)
- [ ] Native-speaker review (Ben or designated reviewer) for naturalness — **manual**
- [ ] Theological review for doctrinal accuracy — **manual**

---

## Last state

- **Mark 1 complete** (45 verses) — in production via PR #165 (merged 2026-04-16)
- **Check infrastructure complete** (2026-04-16) — RULES.md, 5 automated checks, orchestrator, glossary builder
- **Next pilot target:** 1 Timothy 3 (16 verses, 5 hapax, famous v16 textual variant) — a real stress test for our rules
