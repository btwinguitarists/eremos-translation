# Eremos Translation — Consolidated Reviewer Packet
**Date assembled: 2026-04-27**
**Books covered: Matthew, Mark, Luke, Acts**

This packet consolidates everything a Greek scholar, theological reviewer, or AI reviewer needs to evaluate the Matthew + Mark + Luke + Acts translation. The translation itself lives in `output/reader/<slug>.md` (full Thai text) and `output/translations/<slug>_*.json` (per-verse Greek + Thai + rationale + notes). This packet documents the decisions behind those files.

> **A note on `<slug>` and `<book>` in file paths:** `<slug>` means the lowercase no-spaces book name — `matthew` for Matthew, `mark` for Mark, `luke` for Luke, `acts` for Acts. `<BOOK>` means the three-letter uppercase book code (MAT, MRK, LUK, JHN, ACT, etc.). When a path says `output/reader/<slug>.md`, you read it as `output/reader/luke.md` for Luke, and so on.

**To give us feedback, see §11 (Reviewer Feedback Worksheet) at the end of this packet.** It's the single place to fill in your responses; you can answer at any scope (one chapter, one book, or the whole corpus).

For an external AI sanity-check (Grok / ChatGPT / Gemini scale), see the per-book `docs/end_of_book/<book>/external_review_packet_<BOOK>_*.md` files — those are scoped and sized for free-tier AI ceilings. **This packet is full-content for human reviewers.**

---

## 1. What this translation is

**Eremos Translation** is a CC0, AI-assisted Thai New Testament translated directly from the SBLGNT Greek critical text. Translation philosophy is **optimal equivalence** — faithful to Greek grammar AND natural in modern Thai. The methodology follows SIL / Wycliffe / UBS standards (Larson's meaning-based approach, Beekman & Callow's principles, Paratext's check framework), adapted for AI-assisted draft generation with extensive automated and human verification.

**Status as of this packet:**

- **Matthew**: 28 chapters — `output/reader/matthew.md` (Thai-only continuous-reading), per-chapter JSONs at `output/translations/matthew_*.json`, per-chapter check reports at `output/check_reports/matthew_*_review.md`
- **Mark**: 17 chapters — `output/reader/mark.md` (Thai-only continuous-reading), per-chapter JSONs at `output/translations/mark_*.json`, per-chapter check reports at `output/check_reports/mark_*_review.md`
- **Luke**: 24 chapters — `output/reader/luke.md` (Thai-only continuous-reading), per-chapter JSONs at `output/translations/luke_*.json`, per-chapter check reports at `output/check_reports/luke_*_review.md`
- **Acts**: 28 chapters — `output/reader/acts.md` (Thai-only continuous-reading), per-chapter JSONs at `output/translations/acts_*.json`, per-chapter check reports at `output/check_reports/acts_*_review.md`

The full repository (CC0): https://github.com/{maintainer}/thai-bible-ai (path adjust as needed for the maintainer's GitHub username).

---

## 2. Confessional position

Eremos Translation is **evangelical Protestant**. Source-text family: SBLGNT (Alexandrian-leaning critical text, same scholarly base as ESV / NIV / NASB / CSB / BSB). Canon: 27-book NT (no deuterocanonicals).

**Editorial decisions on contested verses follow what major evangelical Protestant translations do.** When manuscript evidence is split, we prefer the editorial choice that aligns with the modern evangelical critical-text consensus (NA28-aligned, where SBLGNT and NA28 agree); when SBLGNT and NA28 disagree, we follow SBLGNT but document the divergence.

**License vs. theology:** CC0 means anyone of any tradition may use the translation, but the *editorial decisions* are evangelical Protestant — not ecumenical-syncretist or doctrinally neutral. The license is open; the translator's editorial frame is not.

---

## 3. Translation philosophy (summary)

**Optimal equivalence**, BSB family. Faithful to Greek grammar, syntax, and semantic range AND natural in modern Thai. When the four pillars (Larson's accuracy / clarity / naturalness / acceptability) conflict, **accuracy wins**, with naturalness documented as a tradeoff.

What this means in practice:
- Greek tense / mood / aspect distinctions are preserved when meaningful, naturalized when not (e.g., historic-present always rendered Thai past — see `historic_present_2026-04.md`).
- Greek word order is rearranged for Thai naturalness; semantic load preserved.
- Idioms are rendered to a Thai equivalent where one exists; otherwise rendered literally with a `notes` entry explaining the original idiom.
- Aramaic embeds (Talitha cumi, Ephphatha, Abba) preserve transliteration AND Mark's own Greek translation — matching Mark's "transliterate then translate" rhetorical move.

---

## 4. Source discipline (strict)

**During translation**, the AI may read only:

- The Greek text (SBLGNT) with MACULA morphological analysis
- The Berean Standard Bible English (CC0) — sanity check ONLY, never as a source to copy
- `RULES.md` — the canonical rules
- `glossary.json` — the persistent key-term ledger
- Prior chapters of Eremos's own output (for consistency)
- unfoldingWord Book Introduction (CC-BY-SA, read-for-context-not-copy)
- unfoldingWord Translation Notes (CC-BY-SA, read-for-context-not-copy)

**Never read during translation:**

- Any copyrighted Thai translation (THSV, NTV, ERV Thai, TNCV)
- TNBT (CC-BY-SA — used post-draft for structural comparison only, never read for wording)
- Any copyrighted commentary

**Why the strictness:** this preserves the "independent creation" copyright defense. Output is produced by independent analysis of the public-domain original languages. After drafting, comparison against other translations identifies divergences to justify, never to copy.

---

## 5. Register & honorifics

- **Divine subjects** (God, Christ, Spirit) always use ราชาศัพท์ (royal register): ทรง / เสด็จ / ตรัส / ทอดพระเนตร / พระหัตถ์ / พระบาท / พระเจ้า / พระเยซู.
- **Humans addressing Christ/God** use lowest humble register: ข้าพระองค์ / พระองค์.
- **God addressing the Son** acceptably uses เจ้า (intimate Father-Son) or พระองค์ (high reverence) — documented per choice.
- **Demons / adversaries** use neutral / distancing register, never honorifics.
- **Inter-human dialogue** matches the social relationship.
- **Non-divine human authorities** (Herod, Pilate, Felix, Festus, centurions, priests) use plain Thai register, NOT ราชาศัพท์ — see `translator_decisions/honorifics_non_divine_authorities_2026-04.md`.
- **Parable characters representing God** (fathers, kings, masters, judges) use human register, never ราชาศัพท์ — see `translator_decisions/parabolic_god_figures_human_register_2026-04.md`.
- **Pagan deities** use เทพ / เทพี / เทพเจ้า — NEVER พระเจ้า, which is reserved for the biblical God.

---

## 6. Standard key-term locks

Non-negotiable (`RULES.md` §4):

| Greek | Thai | Notes |
|-------|------|-------|
| εὐαγγέλιον | ข่าวประเสริฐ | Never พระกิตติคุณ unless explicitly noted |
| χριστός | พระคริสต์ | Title, not a proper name |
| Ἰησοῦς | พระเยซู | The พระ prefix is the divine honorific |
| σατανᾶς | ซาตาน | Transliteration, standard |
| πνεῦμα ἅγιον | พระวิญญาณบริสุทธิ์ | |
| βαπτίζω / βάπτισμα | บัพติศมา | Transliteration, standard in Thai Christianity |
| ἔρημος (wilderness) | ถิ่นทุรกันดาร | "Wilderness/desert region" |
| ἔρημος τόπος | ที่เปลี่ยว | "Solitary place" |
| κύριος (= YHWH) | องค์พระผู้เป็นเจ้า | OT citations + narrator-Lord-as-Jesus in Luke-Acts |
| κύριος (Jesus / human master, vocative) | context-dependent, documented | See vocative_kyrie_didaskale doc |
| συναγωγή | ธรรมศาลา | |
| μετανοέω | กลับใจ | |
| βασιλεία τοῦ θεοῦ | อาณาจักรของพระเจ้า | Mark/Luke/Acts uniform; Matthew adds the τῶν οὐρανῶν → อาณาจักรสวรรค์ split |
| ἁμαρτία | บาป | |
| ἄφεσις (ἁμαρτιῶν) | การยกโทษ(บาป) | Locked 2026-04 |
| ἀγαπητός | ที่รัก | "Beloved" — or "ที่รักยิ่ง" for intensification |

For proper nouns (persons, places), transliteration follows established Thai Christian practice (Ἰωάννης → ยอห์น, Ἠσαΐας → อิสยาห์, etc.).

---

## 7. Locked corpus-level decisions

Each linked doc records: scope, evidence base, the rule, alternatives considered, when to revisit, and cross-references. **These decisions are LOCKED — re-litigation requires an explicit corpus revision.**

- **[ἀμὴν λέγω ὑμῖν → เราบอกความจริงแก่พวกท่าน](translator_decisions/amen_saying_formula_2026-04.md)** — Dominical solemn-pronouncement formula introduced by ἀμήν. Occurs 13× in Mark (3:28; 8:12; 9:1, 41; 10:15, 29; 11:23; 12:43; 13:30; 14:9, 18, 25, 30).
- **[ἄφεσις (ἁμαρτιῶν) → การยกโทษ(บาป)](translator_decisions/aphesis_forgiveness_of_sins_2026-04.md)** — The Greek noun ἄφεσις when it carries the theological sense of "forgiveness / remission (of sins)." This is the dominant NT sense: ~17 occurrences including the 5 Petrine-and-Pauline Acts sermons t...
- **[Aramaic transliterations in the Thai text](translator_decisions/aramaic_transliterations_2026-04.md)** — Aramaic words that Mark embeds in the Greek text for dramatic effect. Mark provides a Greek translation for each; our Thai translation preserves the transliteration AND the Thai translation, matchi...
- **[βασιλεία τοῦ θεοῦ / τῶν οὐρανῶν — kingdom-rendering lock](translator_decisions/basileia_kingdom_rendering_2026-04.md)** — The kingdom-of-God / kingdom-of-heaven word group across the Gospels + Acts + epistles. Two Greek forms carry different Synoptic conventions that the Thai corpus preserves rather than flattens.
- **[Praise verbs with divine object → สรรเสริญ (default collapse)](translator_decisions/divine_object_praise_verbs_2026-04.md)** — Greek verbs and verb-phrases of praise/worship when **God** (or the risen Christ) is the **grammatical object** of the praise-act. Four distinct lexemes collapse to a single Thai default for natura...
- **[ἐκκλησία → คริสตจักร](translator_decisions/ekklesia_2026-04.md)** — The Greek noun ἐκκλησία wherever it refers to the Christian community (gathered or institutional). Two Matthean occurrences (16:18, 18:17) set the precedent for ~110 NT occurrences in Acts, the Pau...
- **[ἔθνος — three-way contextual split](translator_decisions/ethnos_2026-04.md)** — All occurrences of ἔθνος / ἔθνη / ἐθνῶν / ἐθνικός in the NT corpus, especially the dense Acts cluster (28 verses) and the Pauline forward-pass (Romans 9–11, Galatians 2–3, Ephesians 2–3).
- **[Historic present → Thai past tense](translator_decisions/historic_present_2026-04.md)** — Greek historic-present verbs (narrative verbs in present indicative with past-time reference, e.g., λέγει "he says" mid-story) are systematically rendered in Thai past tense.
- **[Honorifics for non-divine human authorities](translator_decisions/honorifics_non_divine_authorities_2026-04.md)** — Herod Antipas, Pontius Pilate, Roman centurions, Jewish-Sanhedrin leaders, and other human rulers who appear as secondary characters in the gospel narrative.
- **[Inclusion variants — three-tier policy (LOCKED)](translator_decisions/inclusion_variants_absent_verses_2026-04.md)** — Whole-verse and large-fragment inclusion variants — readings where mainstream traditions (TR, Byz, KJV, sometimes THSV) include text that SBLGNT/NA28/UBS5 critical text omits. Distinct from word-ch...
- **[Johannine doubled-amen (`ἀμὴν ἀμὴν λέγω ὑμῖν`) → อาเมน อาเมน เราบอกแก่พวกท่านว่า](translator_decisions/johannine_doubled_amen_2026-04.md)** — The Johannine doubled-amen formula `ἀμὴν ἀμὴν λέγω ὑμῖν`. Appears 25× in John (only NT book with the doubled form): 1:51, 3:3, 3:5, 3:11, 5:19, 5:24, 5:25, 6:26, 6:32, 6:47, 6:53, 8:34, 8:51, 8:58,...
- **[ὁ κύριος (narrator voice, referring to Jesus) → องค์พระผู้เป็นเจ้า](translator_decisions/kyrios_narrator_voice_luke_acts_2026-04.md)** — Narrator-voice uses of ὁ κύριος where the referent is Jesus (not the Father, not a human master). A Lukan-Acts signature — Luke is the only evangelist who calls Jesus "the Lord" in his own narratio...
- **[Markan εὐθύς ("immediately") — context-sensitive rendering](translator_decisions/markan_euthys_immediately_2026-04.md)** — εὐθύς / εὐθέως, Mark's signature pacing adverb. Occurs 42× in Mark (more than all other NT books combined for this Markan-dominant word).
- **[μετανοέω vs. μεταμέλομαι — Thai distinction lock](translator_decisions/metanoeo_vs_metamelomai_2026-04.md)** — The two Greek "change-of-mind" verbs that the NT carefully distinguishes. μετανοέω (~34× NT) carries salvific-conversion weight; μεταμέλομαι (6× NT) is narrower — remorse, regret, reconsidering — w...
- **[Narrator vs. character voice — register for Jesus](translator_decisions/narrator_vs_character_voice_2026-04.md)** — Whether Jesus is referred to with royal register (พระองค์, พระ-, ทรง, เสด็จ, ตรัส) depends on who is speaking.
- **[οὐρανός — ฟ้าสวรรค์ / สวรรค์ / ท้องฟ้า rendering](translator_decisions/ouranos_heaven_rendering_2026-04.md)** — The Greek noun οὐρανός ("heaven / sky"), singular and plural. Common across the gospels, dense in Acts (Ascension + Pentecost + visions), and theologically loaded in Paul (ἐν τοῖς οὐρανοίς / ἐπουρά...
- **[Pagan-deity proper nouns — register and transliteration policy](translator_decisions/pagan_deities_2026-04.md)** — Greek + Hebrew/Aramaic-loanword pagan-deity names; pagan-religious vocabulary (idols, temples, priests of pagan gods); narrator-vs-character voice on "god/gods" claims.
- **[Parabolic characters that represent God — human register, not ราชาศัพท์](translator_decisions/parabolic_god_figures_human_register_2026-04.md)** — Human characters inside Jesus's parables who theologically *represent* God, Christ, or the Spirit — fathers, kings, masters, shepherds, vineyard owners, bridegrooms, judges. These figures are rende...
- **[ψυχή vs. πνεῦμα — human anthropology distinction](translator_decisions/psyche_vs_pneuma_anthropological_2026-04.md)** — The Greek words ψυχή ("soul") and πνεῦμα ("spirit") when referring to **human inner-personhood** — NOT when πνεῦμα refers to the Holy Spirit (separate glossary lock: πνεῦμα ἅγιον → พระวิญญาณบริสุทธ...
- **[Roman administrative titles — Thai rendering policy](translator_decisions/roman_administrative_titles_2026-04.md)** — All Roman political, military, and judicial titles appearing in the NT, especially the dense Acts cluster. Pauline epistles will revisit ἐξουσίαι (Romans 13:1–7), βασιλεῖς + οἱ ἐν ὑπεροχῇ (1 Tim 2:...
- **[Son of Man — บุตรมนุษย์ vs. บุตรของมนุษย์](translator_decisions/son_of_man_disambiguation_2026-04.md)** — The Christological title ὁ υἱὸς τοῦ ἀνθρώπου ("the Son of Man") vs. the generic-plural υἱοὶ τῶν ἀνθρώπων ("sons of men" = humanity).
- **[Speech verbs when adversaries address divine Jesus — ทูล convention](translator_decisions/speech_verbs_adversaries_addressing_divine_2026-04.md)** — Thai narrator-voice speech verbs (ทูล / กล่าว / พูด / ร้อง / ร้องตะโกน) used to introduce what a speaker says, when the speaker is an **adversary** (Satan, tempters, hostile Sanhedrin, Pilate, mock...
- **[Character-voice vocative address to Jesus — Κύριε, Διδάσκαλε](translator_decisions/vocative_kyrie_didaskale_register_2026-04.md)** — In-narrative character speech addressing Jesus with the vocative Κύριε ("Lord!") or Διδάσκαλε ("Teacher!"). Distinct from narrator-voice κύριος (see `kyrios_narrator_voice_luke_acts_2026-04.md`).

For a topic-organized index, see [translator_decisions/README.md](translator_decisions/README.md).

---

## 8. Per-book end-of-book audit summaries

Each completed book gets an end-of-book audit (per `END_OF_BOOK_CHECKLIST.md`) recording: mechanical-gate status, cross-cutting items reviewed, items locked / stable / under-review, and any new translator_decisions docs written.

### Matthew

Full audit: [MAT_END_OF_BOOK_REVIEW_2026-04-19.md](end_of_book/matthew/MAT_END_OF_BOOK_REVIEW_2026-04-19.md)

- **16 cross-cutting items reviewed.**
- **6 flagged** for Ben's attention: ἐκκλησία, μεταμέλομαι vs. μετανοέω, amen-formula drift, Σὺ λέγεις micro-drift, inclusion-variant treatment of 17:21/18:11, and `thai_summary` coverage variance.
- **10 items stable/locked** — no corpus-level change needed.
- **3 new decision docs recommended** (see final section).

Status codes below: **LOCKED** (stable + corpus-doc or unambiguous), **STABLE/UNDOCUMENTED** (no drift, no corpus-doc), **DRIFT** (varies without rationale), **REVIEW** (documented but Ben should confirm).

---

### Mark

Full audit: [MRK_END_OF_BOOK_REVIEW_2026-04-26.md](end_of_book/mark/MRK_END_OF_BOOK_REVIEW_2026-04-26.md)

- **12 cross-cutting items consolidated.**
- **7 decision docs originated from Mark's retrospective review** (amen_saying_formula, aramaic_transliterations, historic_present, markan_euthys_immediately, narrator_vs_character_voice, son_of_man_disambiguation, honorifics_non_divine_authorities). All seven are LOCKED.
- **5 additional decision docs that lock Mark-applicable patterns** were written during Matthew/Luke/Acts reviews and verified compliant in Mark (basileia_kingdom_rendering, metanoeo_vs_metamelomai, inclusion_variants_absent_verses, parabolic_god_figures_human_register, divine_object_praise_verbs).
- **All mechanical gates pass:** Mark is tagged `book-mark-v1`. Per-chapter check reports (`output/check_reports/mark_*_review.md`) all green; key-term consistency clean; back-translations present.
- **No outstanding items.** No DRIFT or DECIDE flags. Mark is locked.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform pattern at verse-level, no separate doc needed (rule lives in RULES.md or glossary.json).

---

### Luke

Full audit: [LUK_END_OF_BOOK_REVIEW_2026-04-22.md](end_of_book/luke/LUK_END_OF_BOOK_REVIEW_2026-04-22.md)

- **22 cross-cutting items reviewed** — 15 from internal review (2026-04-22) + 4 Gemini-flagged items (2026-04-23) + 6 Claude-flagged items (2026-04-23), with overlap folded in.
- **9 new decision docs written** across three passes (see §§1, 2, 6, 16, 17).
- **4 translation spot-revisions**: LUK 10:13 (μετανοέω), LUK 1:77 (ἄφεσις), LUK 10:17 (Κύριε vocative), LUK 10:20 (οὐρανός parallelism).
- **1 RULES.md update** — §5 Luke 24 WNI enumeration (v0.4).
- **8 items stable / already documented** — no corpus-level change needed.
- **4 items flagged for Ben's attention** (see final section).
- **Mechanical items (§1 of checklist): all pass** post-revision — 0 key-term-consistency violations, 0 Greek-field-integrity hard fails on touched chapters (LUK 1, 10), `git status output/` tracks only the expected edits.

Status codes: **LOCKED** (stable + corpus-doc). **STABLE** (uniform + rationale implicit at verse-level; documented here). **REVIEW** (worth Ben's confirmation). **DECIDE** (Ben choice needed).

---

### Acts

Full audit: [ACT_END_OF_BOOK_REVIEW_2026-04-26.md](end_of_book/acts/ACT_END_OF_BOOK_REVIEW_2026-04-26.md)

- **15 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 28/28 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `git status output/` clean; main branch up to date with origin.
- **8 inherited Luke-era locks verified compliant** in Acts (ἐκκλησία, ἄφεσις, narrator-κύριος, βασιλεία, οὐρανός-Ascension, παρρησία, divine-praise default, vocative Κύριε).
- **3 cross-cutting patterns are STABLE-but-undocumented at corpus level** (ἔθνος contextual handling, Roman administrative titles, pagan-deity proper nouns). Verse-level rationale carries the full burden; recommend lifting to `docs/translator_decisions/` before Pauline epistles.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation).
- **1 item flagged DECIDE** (Acts 21 we-passage register elevation).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---


---

## 9. How to access the translation

- **Read the full Thai text:** `output/reader/<slug>.md` (one file per book, continuous-reading format with chapter+verse markers and any chapter-footer textual-variant notes).
- **Read the per-verse rationale:** `output/translations/<slug>_NN.json` — each verse has `greek`, `bsb_english`, `translation.thai`, `translation.thai_literal`, `translation.thai_summary` (Thai context summary), `translation.key_decisions` (rationale ledger), `translation.notes` (textual-variant + scholarly notes).
- **Read the per-chapter check report:** `output/check_reports/<slug>_NN_review.md` — automated checks across 8 dimensions.
- **Read the corpus rules:** `RULES.md`.
- **Browse decisions:** `docs/translator_decisions/` (start with `README.md`).
- **Browse end-of-book audits:** `docs/end_of_book/<book>/<BOOK>_END_OF_BOOK_REVIEW_*.md`.

---

## 10. How to give feedback

The structured way: **fill in §11 (Reviewer Feedback Worksheet) below.** It's set up for any reviewer scope — one chapter, one book, or the whole corpus. Open this file in a text editor or upload to Google Docs, type under each prompt, save, send back.

For ad-hoc feedback outside the worksheet (a single verse you noticed in passing): identify the verse (book, chapter, verse), cite the Greek lemma or phrase, state the issue (mistranslation / register / theology / clarity / Thai naturalness), suggest an alternative if you have one, and cite any source supporting your alternative.

Submit via:
- The completed worksheet (preferred — single artifact, easy to process), OR
- GitHub issue on the repo (good for tracking individual verses), OR
- Direct contact with the maintainer (Ben Van Scyoc — benvanscyoc@gmail.com).

For Thai naturalness feedback specifically, native-speaker corrections are weighted heavily. The maintainer is not a native Thai speaker; the AI-generated draft may carry subtle register or idiom errors that an educated native ear catches.

For theological / editorial feedback, please indicate your tradition (evangelical Protestant / Catholic / Orthodox / academic) so the maintainer can weigh the feedback against the project's evangelical-Protestant editorial frame (§2). The license is CC0 and welcomes use in any tradition; the editorial decisions are not ecumenical and won't be adjusted for tradition-fit.

---

## 11. Reviewer Feedback Worksheet

> **How to use this section:** open this file in any text editor (TextEdit, VS Code, Notepad) or upload to Google Docs. Type your answers under each prompt — the `___` lines are placeholders. Skip any prompt you can't answer with confidence; an empty answer is more useful than a guessed one. When done, save the file (or share the doc) and send it back to the maintainer.
>
> **You don't have to answer everything.** This worksheet covers single-chapter reviewers, single-book reviewers, and multi-book reviewers. Fill in the sections that match your scope and skip the rest.

### Section A — answer if you've read at least one chapter

**Which chapter(s) did you read?**
   ___

**A1. Thai naturalness.** Where does the Thai read like a translation rather than native Thai? List specific verse references (book, chapter, verse) and what feels off.
   ___

**A2. Register fit (ราชาศัพท์).** Does the divine-vs-human register feel right where Jesus speaks, the Father is addressed, or human authorities (kings, governors, centurions) are introduced? Flag verses where it sounded off.
   ___

**A3. Clarity.** Any verses where you had to re-read to understand what was being said? List with reference.
   ___

**A4. Surprises.** Anything that struck you positively, or any rendering choice you'd want explained?
   ___

### Section B — answer if you read at least one full book

**Which book(s)?**
   ___

**B1. Cross-cutting decisions in this book.** Are there terms or patterns that seem forced or imposed where context would suggest a different rendering? Reference + reasoning.
   ___

**B2. Audit revisits.** Reading the linked end-of-book audit (§8 above), are there items where you'd push back on the verdict, or items the audit missed?
   ___

**B3. Hapax / textual variants.** Any place we made a notable choice on a hapax legomenon or a textual variant where you'd argue differently? Reference + reasoning.
   ___

**B4. Synoptic alignment** (Mark / Matthew / Luke only). Parallel passages where our renderings diverge across gospels and you think they shouldn't (or should diverge more). Reference both gospels.
   ___

### Section C — answer if you've read multiple books or the whole corpus

**C1. Cross-book consistency.** Terms or decisions that drifted across books in ways that feel unintended.
   ___

**C2. Locked corpus-level decisions** (§7 above). Any locked decision you'd revisit? Cite the doc and your reasoning.
   ___

**C3. Theological frame fit.** Does the editorial voice feel evangelical Protestant in the right way (§2), or does it tilt elsewhere?
   ___

**C4. Source discipline** (§4). Do you see places where the Thai mirrors a specific English version rather than reading from the Greek?
   ___

### Section D — about you (helps us weight your feedback)

**D1.** Tradition (evangelical Protestant / Catholic / Orthodox / academic / other):
   ___

**D2.** Greek background (none / NT survey / seminary / advanced / academic):
   ___

**D3.** Thai exposure (none / conversational / fluent non-native / native / scholarly Thai):
   ___

**D4.** Approximate hours spent on this packet:
   ___

**D5.** Would you be willing to look at later books or post-revision drafts?
   ___

### Section E — free-form

**E1.** Anything we didn't ask about that you want to flag:
   ___

**E2.** Specific encouragements (we read these, even when the rest of the feedback is negative):
   ___

**E3.** Resources you'd recommend (lexicon, commentary, prior translation we should consult):
   ___

---

**When you're done:** save this file (or your Google Doc copy) and send it to the maintainer. Reference the date at the top of this packet so we know which corpus state you reviewed against.

---

**End of packet.** This packet is regenerable from the repo at any time via `scripts/build_consolidated_reviewer_packet.py`. If something here is out of date relative to the actual repo state, the repo wins — regenerate the packet.
