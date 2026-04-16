# Eremos Translation — Chapter Workflow

End-to-end process for translating a new Bible chapter from original languages (Koine Greek for NT, Biblical Hebrew for OT) to Thai and surfacing it in the Eremos app.

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

Example: translating **Mark 2**.

### 1. Extract verses from MACULA

Edit `scripts/extract_mark.py` if needed (currently extracts all of Mark), then:

```bash
cd ~/thai-bible-ai
python3 scripts/extract_mark.py
```

Writes `output/mark/mark_02.json` (among others) with word-by-word morphology, BSB reference, hapax flags, Louw-Nida semantic domains.

**Extending to other books**: duplicate `extract_mark.py` → `extract_<book>.py`, change `BOOK_CODE` (e.g., `MAT`, `JHN`, `LUK`) and `BOOK_NAME_BSB`. MACULA covers the full NT.

### 2. Translate the chapter

**Option A — Claude API (fast, batched):**

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 scripts/translate_mark.py --chapter 2
```

Writes `output/translations/mark_02.json`. Each verse gets Thai rendering, literal form, key decisions, and notes.

**Option B — Manual via Claude in conversation (higher quality for pilot):**

1. Open a Claude conversation
2. Read the verse data: `python3 -c "import json; print(open('output/mark/mark_02.json').read())"`
3. Ask Claude to translate following the same pattern as `output/translations/mark_01.json`
4. Save the result to `output/translations/mark_02.json`

**Translation philosophy (consistent across all chapters):**
- Optimal equivalence (BSB-style) — faithful to Greek + natural Thai
- Translate FROM the Greek; BSB English is a sanity check, not a source
- Key term consistency: εὐαγγέλιον → ข่าวประเสริฐ, χριστός → พระคริสต์, Ἰησοῦς → พระเยซู (with honorific พระ), σατανᾶς → ซาตาน, βαπτίζω → บัพติศมา, ἔρημος → ถิ่นทุรกันดาร, κύριος (= YHWH) → องค์พระผู้เป็นเจ้า, συναγωγή → ธรรมศาลา, μετανοέω → กลับใจ
- Divine subjects get ราชาศัพท์ (royal register): ทรง + verb, เสด็จ for movement, ตรัส for speech, ทอดพระเนตร for see, พระหัตถ์ for hand
- Flag every hapax legomenon with rationale
- Flag textual variants between SBLGNT and mainstream readings (especially BSB's choices)
- Never mimic existing copyrighted Thai translations (independent creation from Greek)

### 3. Generate review markdown (optional, for human review)

```bash
python3 scripts/render_markdown.py --chapter 2
```

Writes `docs/mark_02_review.md` with parallel Greek/English/Thai + collapsible decisions. Share this with Thai-speaking reviewers.

### 4. Build the Eremos bundle

```bash
python3 scripts/build_eremos_bundle.py
```

Combines all `output/translations/mark_XX.json` files into a single `~/EremosVercel2/server/data/eremos_translation.json` — the file Eremos imports at server boot.

### 5. Ship to Eremos

```bash
cd ~/EremosVercel2
git checkout -b feat/eremos-translation-mark-2
git add server/data/eremos_translation.json
git commit -m "feat: add Mark 2 to Eremos Translation bundle"
git push -u origin feat/eremos-translation-mark-2
gh pr create --title "feat: Eremos Translation — Mark 2" --body "<summary>"
```

Vercel auto-deploys the preview. Test by tapping verses in Mark 2. Merge when happy.

**Note:** The schema never changes for new chapters — only the bundle file grows. `ensureEremosTranslationImported()` auto-detects when the bundle has new verses and upserts them on (book, chapter, verse) conflict. The unique index (migration 0005) guarantees no duplicates.

### 6. Refreshing existing content

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
| Source texts (read-only clones) | `~/thai-bible-ai/sources/` |
| Extraction scripts | `~/thai-bible-ai/scripts/extract_*.py` |
| Translation script | `~/thai-bible-ai/scripts/translate_mark.py` |
| Bundle builder | `~/thai-bible-ai/scripts/build_eremos_bundle.py` |
| Review renderer | `~/thai-bible-ai/scripts/render_markdown.py` |
| Per-verse extracted data | `~/thai-bible-ai/output/mark/mark_XX.json` |
| Per-chapter translations | `~/thai-bible-ai/output/translations/mark_XX.json` |
| Review markdown | `~/thai-bible-ai/docs/mark_XX_review.md` |
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

## Translation quality checklist

Before committing a chapter, confirm:

- [ ] All verses present (e.g., Mark 2 should have 28 verses per SBLGNT)
- [ ] Key terms consistent with prior chapters (εὐαγγέλιον always ข่าวประเสริฐ, etc.)
- [ ] Divine subjects use ราชาศัพท์ register
- [ ] Every hapax legomenon has a rationale entry in `key_decisions` or `notes`
- [ ] Any textual variants vs. BSB flagged in `notes`
- [ ] Back-translation test: paste the Thai into a separate Claude conversation, ask for English, compare against BSB — divergences should be intentional and documented
- [ ] Native-speaker review on at least the first chapter of a new book (more frequent early, less needed as patterns stabilize)

---

## Last state

- **Mark 1 complete** (45 verses) — in production via PR #165 (merged 2026-04-16)
- **Next pilot target:** Mark 2 (or whatever you pick next)
