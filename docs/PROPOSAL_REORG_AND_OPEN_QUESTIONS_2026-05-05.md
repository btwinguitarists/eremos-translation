# Eremos — RUT 1 post-merge proposals + open questions

**Date:** 2026-05-05
**Context:** RUT 1 merged (#116). External AI reviews (Gemini + ChatGPT) processed. This doc proposes the folder-reorganization, lists system gaps surfaced by the OT pilot, and captures the open questions for the Thai-language reviewer to answer at end-of-Ruth review.

---

## A. Open questions for the Thai-language reviewer (NOT blocking Ruth 2)

These are register/word-choice judgment calls that a Thai native speaker should validate. All are already logged in the corresponding `key_decisions` rationale fields, so the reviewer will see them when reviewing the chapter. Listed here for visibility:

| Verse | Hebrew | Current Thai | Alternative considered | Why this matters |
|---|---|---|---|---|
| 1:6 | פָּקַד | ทรงเยี่ยมเยียน | ทรงเหลียวแล (look upon with care) | paqad recurs throughout OT in pastoral-care contexts; needs a corpus-wide lock |
| 1:8 | חֶסֶד | ความรักมั่นคง | ความเมตตาที่ภักดี / ความรักภักดี | **OT-corpus key-term lock** — chesed appears 246× in OT |
| 1:9 | מְנוּחָה | ความสงบมั่นคง | ที่พักพิง / ที่พักสงบ | menuchah is the covenant-rest term — also Heb 4 in NT |
| 1:14 | דָּבַק | ยึดมั่นแนบแน่น | ผูกพัน / กอดรัด | davaq = Gen 2:24 marriage-covenant verb; recurs |
| 1:19 | הוּם | แตกตื่น | ฮือฮา / ตื่นเต้น | hum = collective vocal-stir; needs to NOT lean happy-excitement |
| 1:20-21 | שַׁדַּי | องค์ผู้ทรงมหิทธิฤทธิ์ | (per divine_names_table lock) | Shaddai recurs ~48× in OT; lock is in place but worth confirming feel |

**My recommendation:** treat these as end-of-Ruth review items for the Thai reviewer. Continue translating Ruth 2-4 with the current locks (consistency matters more than perfection at the per-chapter level). Adjust at book-boundary based on reviewer feedback.

**No questions block Ruth 2.** I'm ready to proceed when you say go.

---

## B. System gaps surfaced by the OT pilot

### B.1 — Verbless equational clauses (Gemini)

Hebrew has many verbless equational clauses (`X is Y`) — e.g., Ruth 1:16 `עַמֵּךְ עַמִּי` ("your people [are] my people"). These get a Thai copula inserted (`จะเป็น`).

**Issue:** if a future automated syntax checker scans for "every Hebrew clause has a verb" it would flag every verbless clause as broken.

**Proposed fix:** when we add such a checker (none exists yet), build it with a verbless-clause whitelist. Document the convention in `docs/translator_decisions/` so future contributors don't trip on it.

**Priority:** low — no checker exists yet to flag false positives.

### B.2 — `lexical_lock` tag for major term locks (Gemini)

Major OT-corpus key-term decisions (chesed → ความรักมั่นคง, Shaddai → ผู้ทรงมหิทธิฤทธิ์, etc.) are buried inside `key_decisions[].rationale` text. A script can't easily aggregate them into a master glossary.

**Proposed fix:** add an optional `lexical_lock: true` boolean field to `key_decisions[]` entries that introduce or apply a corpus-wide lock. A script (`build_glossary.py` extension) walks all chapters, picks up locked entries, and emits `output/glossary_locks.md` — the master ledger of "every term locked across the corpus, where it was first locked, and the rationale."

**Priority:** medium — useful for coherence audits, especially as we ship more OT chapters. Worth doing before Ruth 2 ships, so Ruth 1's chesed entry is the first to carry the tag.

### B.3 — Honorifics-binding check (Gemini)

ราชาศัพท์ (royal Thai — `ทรง-` verbal prefix, `พระ-` body-part prefix) should bind ONLY to divine subjects. The Ruth 1:13 fix (dropping ทรง- from "ได้ยื่นออกมาต่อสู้" because the subject is `พระหัตถ์`, a body-part, not YHWH directly) is exactly the kind of slip a check could catch.

**Proposed fix:** new check `scripts/check_honorifics_binding.py` that walks Thai translation text and flags any `ทรง-` verb whose grammatical subject (per surrounding noun analysis) is not in a known-divine-subject list. Hard fail on undocumented violations.

**Priority:** medium — would have caught the Ruth 1:13 slip mechanically. Worth building before more OT chapters ship.

### B.4 — OT pipeline gaps already closed in #116

Documented for completeness:
- `check_divine_names.py` + `check_hebrew_field_integrity.py` now read nested `translation.thai` / `translation.key_decisions` (was reading flat — let any OT translation through with no real validation)
- `render_reader.py` now imports OT BOOKS from `extract_book_hebrew` (#115) + handles `tetragrammaton_convention_first_occurrence` textual_variants type (#116)
- 39 OT Thai book titles added to `THAI_BOOK_TITLES`

---

## C. Folder reorganization — proposed two-phase approach

**The ask:** organize `output/` and `docs/` so files are findable. Currently:
- `output/translations/` has 262 flat files (one per chapter, NT books all mixed in alphabetical order)
- `output/check_reports/` has 2,051 files
- `output/back_translations/` has 366 files
- `docs/` root has ~15 ad-hoc files mixed with `translator_decisions/`, `end_of_book/`, `archive/`

**The cost:** 24 scripts hardcode the flat paths (92 path references total). Moving files breaks every script unless they're updated in lockstep.

### Phase 1 — Add Thai+English book-title docs (no script changes; do now)

Add `output/by-book/README.md` with a single table that maps every flat file to its testament + Thai book name + English book name + chapter, so anyone scanning the repo can find what they want by Thai name. Two minutes of work, zero risk.

Same for `docs/README.md` — a top-level index of what's in `docs/` and where to look.

### Phase 2 — Symlink hierarchy (no file moves; presents hierarchical view; do as separate PR)

Create:
```
output/by-book/
  ├── พันธสัญญาเดิม-Old-Testament/
  │   └── 08-นางรูธ-Ruth/
  │       ├── chapter-01/
  │       │   ├── translation.json -> ../../../../translations/ruth_01.json
  │       │   ├── back_translation.json -> ../../../../back_translations/ruth_01.json
  │       │   ├── check_review.md -> ../../../../check_reports/ruth_01_review.md
  │       │   └── ...
  │       └── reader.md -> ../../../reader/ruth.md
  └── พันธสัญญาใหม่-New-Testament/
      └── 41-มาระโก-Mark/
          └── ...
```

Symlinks let scripts continue using flat paths while humans navigate hierarchically. Generated by a script (`scripts/build_book_index.py`), regenerated on every `ship_chapter.sh`.

**Why symlinks not moves:** moving 262+2051+366 files would require lockstep updates to 24 scripts. Symlinks let me ship Phase 2 in one PR with zero risk to the existing pipeline.

### Phase 3 — Consider true file moves (months out, only if Phase 2 isn't enough)

If symlinks feel hacky or git-on-Mac mishandles them, we can do the real move later. But Phase 2 should cover 95% of the "I want to find Ruth chapter 1's translation" use case.

### docs/ proposal

Reorganize `docs/` root into:
```
docs/
  ├── README.md (NEW — top-level index)
  ├── workflows/        (TRANSLATION_WORKFLOW.md, END_OF_BOOK_CHECKLIST.md, REVIEW_TOOLS.md)
  ├── style_guides/     (CHAPTER_REVIEW_PROMPT.md, THAI_SUMMARY_STYLE.md, source_license_policy.md)
  ├── audits/           (NT_V1_FULL_AUDIT_2026-05-04.md, NT_V1_POLISH_SUMMARY_2026-05-04.md, 1tim_03_pilot_assessment_2026-05-02.md, end_of_book/, archive/)
  ├── reviewer_packets/ (reviewer_packet_en_2026-04-27.md, reviewer_packet_th_2026-04-27.md, future per-book packets)
  ├── translator_decisions/ (existing — keep as-is)
  └── proposals/        (this doc, future proposals)
```

This needs `git mv` for ~10 files + a one-line update to anywhere that links into `docs/` from outside (CLAUDE.md memory references the path `~/thai-bible-ai/docs/`, will keep working since most references are to `docs/translator_decisions/` which doesn't move).

**Priority:** low — `docs/` is small enough (~15 root files) that it's findable today. But if you do a lot of work in `docs/` (per your message), doing this once is worth a 1-PR upfront cost.

---

## D. My recommended next moves

**Immediate (no user action needed):**
- Ship Ruth 2 using current locks. Continue logging Thai-reviewer questions in `key_decisions`.

**Soon (need your go-ahead):**
- B.2 lexical_lock tag (1 PR, ~30 min, useful for end-of-book aggregation)
- B.3 honorifics-binding check (1 PR, ~1 hour, would have caught the v.13 slip)
- C Phase 1 README files (1 PR, ~15 min, zero risk)
- C Phase 2 symlink hierarchy (1 PR, ~1 hour, zero risk to scripts)
- C docs/ reorganization (1 PR, ~30 min, low risk — git mv with 1-line link updates)

**Defer:**
- C Phase 3 true file moves (only if symlinks prove insufficient)

**My read:** ship Ruth 2 first (validates the post-fix pipeline end-to-end on a fresh chapter), then do C Phase 1 + 2 + docs/ reorg as a single "infra cleanup" PR before Ruth 3. lexical_lock + honorifics-binding can wait until end-of-Ruth.
