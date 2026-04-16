# Eremos Translation

An AI-assisted, fully open-source (CC0) Thai translation of the Bible, produced directly from the original-language manuscripts via a transparent pipeline modeled on SIL/Wycliffe/UBS translation methodology. Every word choice is traceable from Greek source through morphological analysis to final Thai rendering, with explicit rationale, textual-variant notes, and an automated quality-check cadence.

**Project goal:** A reproducible, auditable, license-free (CC0) Thai NT — and eventually the full Bible — that any Thai church or app can use, modify, redistribute, or build upon without permission or fees.

---

## For reviewers

If you're a translation expert, theological reviewer, or another AI evaluating this work, **start here**:

1. **Read `RULES.md`** (15 KB) — the canonical translation rules. Sources, honorifics, key-term policy, check cadence, copyright/license discipline. Derived from Larson, Beekman & Callow, SIL training materials, and unfoldingWord standards.

2. **Read `GENRES.md`** (12 KB) — the genre-aware production plan. Lists which automated checks cover which Bible genre, what's still needed, and the recommended translation order (NT narrative → Pauline corpus → general epistles → Revelation → OT).

3. **Read a sample chapter output**, e.g.:
   - `output/translations/mark_06.json` — long narrative chapter (56 verses), good for assessing prose quality, OT-allusion handling (Ps 23 echo, Mosaic feeding-typology), and theological loadings (ἐγώ εἰμι at 6:50, eucharistic foreshadowing at 6:41)
   - `output/translations/1timothy_03.json` — epistle (16 verses), shorter, good for assessing handling of textual variants (the famous ὃς/Θεὸς at 3:16) and gendered language (γυναῖκας at 3:11)
   - `output/translations/mark_07.json` — controversy + healing (36 verses), good for OT-citation tracking (Isa 29:13 LXX-dependence at 7:6-7) and Aramaic transliteration policy (Κορβᾶν, ἐφφαθά)

4. **Read its check report** at `output/check_reports/<book>_<NN>_review.md` — the audit trail for that chapter (key-term consistency, TNBT structural diff, OT citation acknowledgment, synoptic parallels, back-translation similarity).

That's the minimum reviewer package. You can stop there or go deeper.

---

## What's been translated (as of 2026-04-16)

| Book / chapter | Verses | Notable features |
|----------------|--------|------------------|
| Mark 1 | 45 | Pilot; SBLGNT omits "Son of God" at 1:1; ὀργισθείς/σπλαγχνισθείς variant at 1:41 |
| Mark 2 | 28 | บุตรมนุษย์ for "Son of Man"; Abiathar/Ahimelech crux at 2:26 |
| Mark 3 | 35 | συλλυπέομαι hapax; Aramaic transliteration "ชาวคานาอัน" |
| Mark 4 | 41 | Isa 6:9-10 citation tracks Targum Jonathan, not LXX; cosmic-tree allusion at 4:32 |
| Mark 5 | 43 | Gerasene demoniac + Jairus/hemorrhaging-woman intercalation; Aramaic "ทาลิธา คูม" |
| Mark 6 | 56 | ἐγώ εἰμι/Exod 3:14 echo; eucharistic four-verb sequence; Pharaoh-hardening |
| Mark 7 | 36 | Isa 29:13 LXX-dependence; Decapolis healing as Isa 35 messianic restoration; "ἐφφαθά" |
| 1 Timothy 3 | 16 | ὃς/Θεὸς textual variant at 3:16; γυναῖκας crux at 3:11 |
| **Total** | **300** | of NT (260 chapters total in production order, 7/16 of Mark done) |

Each translation lives at `output/translations/<book-slug>_<NN>.json` with full Greek source, BSB English reference, Thai rendering, key decisions with rationale, and notes on textual variants / hapax legomena / OT citations.

---

## How it's built

**Source materials** (all open-licensed — see `ATTRIBUTIONS.md`):

- **Greek text:** SBL Greek New Testament (CC BY 4.0)
- **Morphology:** MACULA Greek linguistic dataset (CC BY 4.0) — word-by-word lemma, parsing, Louw-Nida semantic domains
- **English reference:** Berean Standard Bible (CC0) — sanity check only, never a source to copy from
- **Scholarly notes:** unfoldingWord Translation Notes (CC-BY-SA 4.0) — read for context, never copied (would force CC-BY-SA inheritance)
- **Structural reference:** Thai New Buddhist Translation TNBT (CC-BY-SA 4.0) — used post-draft for sentence-count / length-ratio comparison only; never read during drafting

**Translation engine:** Claude (Anthropic) — Opus 4.6 with 1M context window and max effort, fresh chat per chapter. Sonnet 4.6 for back-translation and follow-up edits.

**Pipeline** (see `docs/TRANSLATION_WORKFLOW.md`):

1. Extract Greek + morphology for the chapter (`scripts/extract_book.py`)
2. Enrich with unfoldingWord scholarly notes (`scripts/enrich_with_uw.py`)
3. Read book-level intro (`output/uw_notes/<slug>_FRONT.md`) — author, audience, themes, outline
4. Read prior chapter output for style continuity
5. Translate from Greek with verse-by-verse rationale
6. Back-translate Thai → English in-chat for self-consistency check
7. Run 5 automated checks (`scripts/run_checks.py`):
   - Key-term consistency across the whole corpus
   - TNBT structural comparison
   - OT citation acknowledgment
   - Synoptic parallel-passage check
   - Back-translation diff against BSB
8. Auto-ship via `scripts/ship_chapter.sh` — bundles, branches, PRs, auto-merges, bumps iOS, builds web, uploads TestFlight

---

## What makes this different from existing Thai Bible translations

Thailand already has THSV (Thai Standard Version 2011) and NTV (New Thai Version), both copyrighted. Eremos Translation is different in three specific ways:

1. **CC0 license** — no permissions, no fees, no derivative-restrictions. Anyone can use any verse anywhere, free.
2. **Full transparency** — every translation decision is documented at the verse level: which Greek word, what alternatives existed, why this Thai rendering. Reviewable in `output/translations/*.json`.
3. **AI-assisted with human-validated cadence** — produced by Opus 4.6 with disciplined sourcing rules, not committee discussion. Auditable via the check reports.

It is **not** a competitor to THSV/NTV; it's an alternative for use cases that require open license (apps, education, derivative works, redistribution). The translation philosophy is "optimal equivalence" — same as BSB in English.

---

## What reviewers should specifically evaluate

If you're qualified to give technical feedback, these are the dimensions that matter:

### Translation quality (Thai-native + theology required)
- **Naturalness** — does the Thai sound natural to a modern reader, or like translationese?
- **Register** — are honorifics (ราชาศัพท์) for divine subjects applied consistently? Are demons/adversaries given the right (lower) register?
- **Theological accuracy** — are the key terms (ข่าวประเสริฐ for εὐαγγέλιον, etc.) used correctly and consistently? See `glossary.json` for the corpus-wide ledger.
- **Idiomatic handling** — Hebraisms, Greek participial constructions, dense Pauline genitives — are they rendered idiomatically in Thai?

### Methodology (translation experts)
- **Source discipline** — read RULES.md §2 and §8. Are we using the right sources? Are the CC-BY-SA dependencies handled correctly to preserve our CC0 output?
- **Check cadence** — read RULES.md §7 and the check reports. Are the 5 automated checks the right ones? What checks are missing?
- **Production order** — read GENRES.md. Is the SIL/Wycliffe-influenced order (narrative → Pauline → general epistles → Revelation → OT) the right call?
- **Honorific policy** — is the ราชาศัพท์ usage policy (RULES.md §3) appropriate for Thai Christian register?

### Documentation transparency (any reviewer)
- Pick any verse from `output/translations/*.json`. Does the documented rationale make sense? Could you trace the decision back to the Greek?
- Are textual variants flagged when they should be? Are hapax legomena explained?

---

## Key files

| File | Purpose |
|------|---------|
| `RULES.md` | Canonical translation rules, sources, philosophy, check mandate |
| `GENRES.md` | Genre-aware production plan + recommended translation order |
| `ATTRIBUTIONS.md` | Source materials and their licenses (CC BY 4.0, CC-BY-SA, CC0) |
| `LICENSE` | CC0 1.0 Universal Public Domain Dedication for our output |
| `NOTICE` | One-line summary of CC0 + dependency licenses |
| `glossary.json` | Auto-maintained per-lemma rendering ledger across all translations |
| `data/production_order.json` | Canonical 260-chapter NT translation order |
| `data/nt_ot_citations.json` | NT→OT citation database (curated, growing) |
| `data/synoptic_parallels.json` | Synoptic parallel-passage map for cross-gospel consistency |
| `docs/TRANSLATION_WORKFLOW.md` | Step-by-step process for adding a chapter |
| `docs/REVIEW_TOOLS.md` | Paratext, Scripture Forge, unfoldingWord integration roadmap |
| `output/translations/<slug>_<NN>.json` | Per-chapter Thai translations with rationale |
| `output/back_translations/<slug>_<NN>.json` | Thai → English back-translations for the check |
| `output/uw_notes/<slug>_FRONT.md` | unfoldingWord book-level scholarly intro |
| `output/uw_notes/<slug>_<NN>.md` | unfoldingWord per-chapter scholarly notes |
| `output/check_reports/` | Audit trail for each chapter's 5-check cadence |
| `scripts/` | Extract, enrich, translate, check, ship pipeline |

---

## Repository status

Currently **private** (until Mark is complete — 9 chapters remaining). The CC0 license applies to all output regardless; once Mark is done the repo flips public.

Companion app: [Eremos](https://github.com/btwinguitarists/EremosVercel2) — surfaces the translation in a Thai Bible reader with a "Translation Notes" popup showing rationale and a one-tap "Flag error" feedback button.

---

## Contact

Project lead: Ben VanScyoc (benvanscyoc@gmail.com) — missionary in Thailand, DMIN student.

Feedback, corrections, theological review, and Thai-native naturalness review all welcomed. Open an issue or email directly.
