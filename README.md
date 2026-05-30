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

## What's been translated (as of 2026-05-30)

**New Testament — COMPLETE.** All 27 NT books shipped (~7,950 verses across 260 chapters), tagged at the `book-<slug>-v1` level following per-book end-of-book audits. Matthew · Mark · Luke · John · Acts · Romans · 1–2 Corinthians · Galatians · Ephesians · Philippians · Colossians · 1–2 Thessalonians · 1–2 Timothy · Titus · Philemon · Hebrews · James · 1–2 Peter · 1–3 John · Jude · Revelation.

**Old Testament — 20 books shipped (494 chapters).** The full Pentateuch (Genesis · Exodus · Leviticus · Numbers · Deuteronomy), the historical books (Joshua · Judges · Ruth · 1–2 Samuel · 1–2 Kings · 1–2 Chronicles · Ezra · Nehemiah · Esther), plus Job · Daniel · Jonah are source-complete. **Job just finished; Psalms is next** as the project moves into the Writings + Prophets. Each OT book ships chapter-by-chapter to `main`, then earns its `book-<slug>-v1` tag after an end-of-book editorial audit + external-AI cross-review (several already tagged; the remainder are progressing through that gate).

**Corpus total: 754 chapters · 22,290 verses · ~63% of the full canon (1,189 chapters).**

📖 **Read it:** every shipped book has a flowing-prose reader edition at `output/reader/<book>.md`. Examples — `matthew.md`, `mark.md`, `luke.md`, `john.md`, `acts.md`, `romans.md`, `revelation.md`, `ruth.md`, `jonah.md`, `genesis.md`. The same translation also surfaces verse-by-verse with tap-to-reveal scholarly notes in the [Eremos](https://github.com/btwinguitarists/EremosVercel2) reader app (web at `eremosapp.com`; iOS via TestFlight; Android via Play Console).

All shipped chapters pass the relevant ship-gate cadence (NT-side: key-term consistency, TNBT structural, OT citation acknowledgment + DB-drift detector, synoptic parallels, back-translation, thai_summary coverage, claim-consistency / hallucination detector, Greek-field integrity, multi-word phrase consistency. OT-side: Hebrew-field integrity, divine-names lock, MT-anchored versification, Rachasap honorifics-binding, back-translation, summary coverage, and a claim-consistency / hallucination detector wired advisory-first). Currently 17 check scripts under `scripts/check_*.py`; the orchestrator (`run_checks.py`) routes by language. Optimal-equivalence polish (Claude API, Sonnet) runs as a post-checks scan and proposes idiomatic refinements without auto-applying.

Reader-facing Thai context summaries (`thai_summary` field) appear on roughly half of all verses — well above the 30–50% target in `docs/THAI_SUMMARY_STYLE.md`. NT→OT citation database at `data/nt_ot_citations.json` curates ~720 entries as of NT-v1. Every commit signed; every translation file SHA-256 fingerprinted in `HASHES.md`. End-of-book audits land an editorial review packet + external AI cross-review packet (Grok / ChatGPT / Gemini) before book-level v1 tags ship.

### Why does our Mark 1:1 differ from the BSB?

Our Greek source is the SBL Greek New Testament (SBLGNT, ed. Michael W. Holmes, 2010), licensed CC BY 4.0. At Mark 1:1, SBLGNT's main text reads `Ἀρχὴ τοῦ εὐαγγελίου Ἰησοῦ ⸀χριστοῦ.` — the `⸀` marker flags `υἱοῦ θεοῦ` ("Son of God") as a variant in its apparatus. The phrase is present in Codex Vaticanus (B), Bezae (D), Washingtonianus (W), and most Byzantine manuscripts; **absent** from Codex Sinaiticus's original hand (א\*), Theta, and citations by Origen. NA28 / UBS5 bracket it with a {C} certainty rating. Homoioteleuton (accidental drop from five consecutive `-ου` genitives) is the most commonly proposed mechanism for early omission.

The BSB — which we use only as an English reference bridge, **not** as a source — uses a different eclectic text that includes the phrase without brackets.

Our approach: **translate from SBLGNT as stated, and document every divergence from other major traditions in the verse's notes.** Our Mark 1:1 note records the manuscript evidence explicitly. This same editorial principle handles every contested passage — Mark 1:41 (ὀργισθείς vs σπλαγχνισθείς), Mark 9:29 (with-or-without "and fasting"), Mark 14:24 (with-or-without "new"), and the ⟦double-bracketed⟧ longer ending of Mark 16:9-20.

### Selected book highlights

| Book | Status | Notable features |
|------|--------|------------------|
| Mark | ✅ NT-v1 | Pilot book — corpus methodology emerged here. SBLGNT-omitted "Son of God" at 1:1 bracketed; ὀργισθείς/σπλαγχνισθείς at 1:41; ⟦double-bracketed⟧ longer ending 16:9–20 |
| Matthew | ✅ NT-v1 | Royal-register (ราชาศัพท์) consistency; Sermon on the Mount; Olivet Discourse; Passion + Resurrection. Late retag `book-matthew-v2` applied ἄφεσις-cluster phrase-lock |
| Luke | ✅ NT-v1 | Magnificat / Benedictus / Nunc Dimittis; parable-dense chs 10–19; Emmaus road; end-of-book external Gemini + Claude cross-AI review pass; Western non-interpolation table for Luke 24 |
| John | ✅ NT-v1 | I AM (ἐγώ εἰμι) discourse vocabulary lock; pericope adulterae 7:53–8:11 in ⟦double brackets⟧; high-Christological prologue treated as one register-unit |
| Acts | ✅ NT-v1 | Pentecost speech with composite OT citations (Joel 2 / Ps 16 / Ps 110); Stephen's Heilsgeschichte rehearsal; Pauline missionary speeches calibrated to Athenian/Roman audiences |
| Romans | ✅ NT-v1 | δικαιοσύνη / δίκαιος family lock per `dikaioo_dikaiosyne_family_2026-05.md`; Romans 16:25–27 doxology disposition documented |
| 1 Timothy | ✅ NT-v1 | Inaugural pilot of the optimal-equivalence rules; ὃς/Θεὸς textual variant at 3:16; γυναῖκας crux at 3:11 |
| Hebrews | ✅ NT-v1 | ἱλαστήριον disambiguation Heb-vs-Rom per `hilasterion_heb-rom_distinction_2026-05.md`; LXX-citation pattern preserved verbatim where the Greek text quotes from LXX |
| Revelation | ✅ NT-v1 | Heavenly liturgy register; Trinitarian title-cluster locks; ἔρχομαι ταχύ register-split per `erchomai_tachy_revelation_register_split_2026-05.md` |
| Ruth | ✅ OT pilot | First OT book — established חֶסֶד → ความรักมั่นคง corpus-lock; Boaz's gate-scene legal vocabulary; redeemer-kinsman thread |
| Jonah | ✅ OT pilot | Tetragrammaton convention validated in narrative + psalm + prophetic-oracle voices; MT/English versification map for ch 2 (great-fish boundary); Exod 34:6–7 attribute-formula recitation lock; sailor + Ninevite parallel-conversion arc |
| Genesis | ✅ book-v1 | Full primordial history + patriarchal narrative (50 ch); OT-narrative register and divine-name compound handling (יהוה־אלהים in the Eden narrative) established here |
| Job | ✅ shipped | Wisdom poetry (42 ch); El/Eloah/Shaddai in the dialogue vs the Tetragrammaton in the prose frame; God-as-adversary lament register (16:9, 30:21) preserved in Rachasap, not softened; chaos-monster transliterations (Rahab/Leviathan/Behemoth); MT↔English versification seams at chs 40–41; goel → พระผู้ไถ่ at 19:25 |
| Daniel | ✅ shipped | Mixed Hebrew + Aramaic sections; foreign-emperor royal register vs Hebrew-vizier plain register; apocalyptic visions; Son-of-Man at 7:13 |

Each translation lives at `output/translations/<book-slug>_<NN>.json` with full Greek/Hebrew source, BSB English reference, Thai rendering (`thai`), optional literal alternative (`thai_literal`), reader-facing Thai context summary (`thai_summary`), key decisions with rationale, and notes on textual variants / hapax legomena / OT citations / Tetragrammaton handling. OT verses additionally carry a `versification` sub-object in known-divergence zones.

---

## How it's built

**Source materials** (all open-licensed — see `ATTRIBUTIONS.md`):

- **Greek NT text:** SBL Greek New Testament (CC BY 4.0)
- **Hebrew/Aramaic OT text:** MACULA Hebrew (BHSA-derived, CC BY 4.0) — covers Genesis through Malachi with morphology + lemma + Strong's H-numbers
- **Morphology:** MACULA Greek + MACULA Hebrew linguistic datasets (CC BY 4.0) — word-by-word lemma, parsing, Louw-Nida (NT) / SDBH (OT) semantic domains
- **English reference:** Berean Standard Bible (CC0) — sanity check only, never a source to copy from
- **Scholarly notes:** unfoldingWord Translation Notes (CC-BY-SA 4.0) — read for context, never copied (would force CC-BY-SA inheritance)
- **Structural reference:** Thai New Buddhist Translation TNBT (CC-BY-SA 4.0) — used post-draft for sentence-count / length-ratio comparison only; never read during drafting (NT only — TNBT does not cover the OT)

**Translation engine:** Claude (Anthropic) — latest Opus with 1M context window and max effort/thinking, fresh chat per chapter. The check scripts call latest Sonnet for the back-translation pass at per-verse volume. See `RULES.md §11` for current model assignments.

**Pipeline** (see `docs/TRANSLATION_WORKFLOW.md`):

1. Resolve next chapter (`scripts/next_chapter.py` reads `data/production_order.json`) OR specify the book/chapter explicitly
2. Extract source-language verses + morphology (`scripts/extract_book.py` auto-routes OT codes to `extract_book_hebrew.py`)
3. Enrich with unfoldingWord scholarly notes (`scripts/enrich_with_uw.py`) — produces book-intro + per-chapter notes
4. Read `RULES.md`, the relevant translator-decision docs, and the most-recent prior chapter output for style continuity
5. Translate verse-by-verse with explicit `key_decisions` rationale
6. Save back-translation (Thai → literal English) to `output/back_translations/`
7. Run the language-routed check cadence (`scripts/run_checks.py`) — currently 15 distinct check scripts under `scripts/check_*.py`; the orchestrator picks the relevant subset for NT vs OT chapters. Iterate via `scripts/revise_chapter.py` if any check fails (max 3 passes before human review)
8. Ship the source via `scripts/ship_chapter.sh BOOK CHAPTER` — gates on green checks, regenerates `HASHES.md` + reader doc + plain-text + feedback markdown, commits to `main`, and (at end-of-book) auto-launches the editorial-review subagent + opens the audit PR
9. After end-of-book external-AI review and any revisions, lock-and-deploy with `scripts/ship_book.sh BOOK` — rebuilds the Eremos app bundle, opens + auto-merges the EremosVercel2 PR, bumps iOS `CURRENT_PROJECT_VERSION`, uploads to TestFlight via altool, and tags `book-<slug>-v1`. Android Play Console upload is a separate manual step.

---

## Confessional position

Eremos Translation is an **evangelical Protestant** Bible translation project. To be specific:

- **Source-text family**: SBLGNT (CC BY 4.0) — same Alexandrian-leaning critical text family as NA28 / UBS5, the standard scholarly base for evangelical Protestant translations (ESV, NIV, NASB, CSB, BSB).
- **Translation philosophy**: optimal equivalence (BSB family) — balancing accuracy to the Greek with natural Thai readability. Same philosophical approach as ESV, NIV, CSB.
- **Canon**: 27-book New Testament + 39-book Protestant Hebrew Old Testament (in progress). No deuterocanonical / apocryphal books.
- **Editorial decisions on contested verses match what major evangelical Protestant translations do**: e.g. Mark 16:9-20 wrapped in disputed-text brackets (matches every major modern evangelical Bible); Mark 14:24 reads "blood of the covenant" (matches ESV); Mark 1:41 "indignant / angered" (the harder reading SBLGNT prints, matching CSB and ESV-with-footnote).
- **License-driven openness, not theology-driven ecumenism**: the CC0 license means Bibles, apps, and ministries from any tradition may use the translation freely, but the **editorial decisions are evangelical Protestant** — not ecumenical-syncretist or doctrinally neutral.

If you're a Thai pastor reviewing the translation: this is meant to sit comfortably alongside THSV / NTV in your shelf — same canon, same family of source text, same translation philosophy as the modern evangelical Bibles you already trust. The differentiators are licensing (CC0) and process transparency (every decision audited in git), not theology.

---

## What makes this different from existing Thai Bible translations

Thailand already has THSV (Thai Standard Version 2011) and NTV (New Thai Version), both copyrighted. Eremos Translation is different in three specific ways:

1. **CC0 license** — no permissions, no fees, no derivative-restrictions. Anyone can use any verse anywhere, free.
2. **Full transparency** — every translation decision is documented at the verse level: which Greek word, what alternatives existed, why this Thai rendering. Reviewable in `output/translations/*.json`.
3. **AI-assisted with human-validated cadence** — produced by Claude Opus under disciplined sourcing rules, not committee discussion. Auditable via the check reports and GPG-signed git history.

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
- **Check cadence** — read RULES.md §7 and the check reports. Are the automated checks (17 language-routed scripts under `scripts/check_*.py`) the right ones? What checks are missing?
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
| `data/production_order.json` | Canonical 1,189-chapter translation order (NT complete + OT in progress) |
| `data/nt_ot_citations.json` | NT→OT citation database (curated, ~720 entries) |
| `data/synoptic_parallels.json` | Synoptic parallel-passage map for cross-gospel consistency |
| `data/versification_map.json` | OT MT-vs-English verse-numbering divergence map (Psalms superscriptions, Joel 3, Mal 3/4, Jonah 2, etc.) |
| `data/hebrew_idioms.json` | Running ledger of Hebrew idioms encountered + their Thai handling |
| `docs/TRANSLATION_WORKFLOW.md` | Step-by-step process for adding a chapter |
| `docs/translator_decisions/` | Per-decision lock docs (chesed, divine-names, register, leitwort handling, etc.) |
| `docs/end_of_book/` | Per-book end-of-book audit packets (editorial review + external AI handoff) |
| `output/translations/<slug>_<NN>.json` | Per-chapter Thai translations with rationale |
| `output/back_translations/<slug>_<NN>.json` | Thai → English back-translations for the check |
| `output/uw_notes/<slug>_FRONT.md` | unfoldingWord book-level scholarly intro |
| `output/uw_notes/<slug>_<NN>.md` | unfoldingWord per-chapter scholarly notes |
| `output/check_reports/` | Audit trail for each chapter's check cadence |
| `scripts/` | Extract, enrich, translate, check, ship pipeline |

---

## Repository status

**Public** (since 2026-04-17, when the Gospel of Mark reached first-draft completion). The CC0 license applies to all output in `output/translations/` and the curated databases under `data/`. Source material under `sources/` is git-ignored — each source has its own license and must be cloned separately from upstream (see `ATTRIBUTIONS.md`).

**NT-v1 complete; OT well underway (20 of 39 books).** All 27 NT books carry per-book `book-<slug>-v1` tags, each landed after a green ship-cadence + an end-of-book editorial-review subagent + at least one external AI cross-review pass. Human-review remains ongoing through the in-house review form (see §10b of `RULES.md`); verse-level revisions can land at any time and trigger a `book-<slug>-v2`-style retag.

On the OT side the project has moved well past the original Ruth + Jonah + Genesis bootstrap: the full Pentateuch, the historical books (Joshua through Esther), and Job · Daniel · Jonah are source-complete on `main` (494 OT chapters). Each book ships chapter-by-chapter, then earns its `book-<slug>-v1` tag after its end-of-book audit + external-AI review. Job was the most recent book completed; Psalms is next as the project enters the Writings and Prophets.

**Human-review intake:** translation reviewers can sign up at `eremosapp.com/review` — a bilingual (Thai + English) form backed by the project's question-bank (per-file YAMLs at `EremosVercel2/shared/review-questions/`). Reviewers are screened by the project lead and matched to question categories per their declared skill set (Thai naturalness / theology / biblical-language exegesis / reader comprehension / app UX).

**Companion app:** [Eremos](https://github.com/btwinguitarists/EremosVercel2) — surfaces the translation in a Thai Bible reader with a "Translation Notes" popup showing rationale + a one-tap "Flag error" feedback button. Web at `eremosapp.com`; iOS via TestFlight; Android via Play Console.

---

## Contact

Project lead: Ben VanScyoc (benvanscyoc@gmail.com) — missionary in Thailand, DMIN student.

Feedback, corrections, theological review, and Thai-native naturalness review all welcomed. Open an issue or email directly.
