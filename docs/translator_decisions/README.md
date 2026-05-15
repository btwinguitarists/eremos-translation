# Translator Decisions — Index

Corpus-level editorial decisions made during end-of-book reviews. Each doc contains: the rule, the evidence base, alternatives considered, and when to revisit.

**These decisions are LOCKED.** Per-chapter translation work follows them without re-litigation; if a doc's rule needs to change, that's an explicit corpus revision (see `END_OF_BOOK_CHECKLIST.md` §4 / "What to do if a decision warrants change after the book ships").

When writing a new doc, follow the existing structure: title with Greek + Thai gloss, **Scope**, **Decided**, **Evidence base**, **The rule**, alternatives considered, **When to revisit**, cross-references.

**Pre-flight grep (added 2026-05-16):** Before marking a doc `Status: LOCKED`, run `python3 scripts/verify_translator_decision.py --doc <this file>` and paste its output into a `## Corpus-verified shipped forms` section. This was added after the Leviticus audit caught `sacrificial_vocabulary §5` locking `ลบบาป` with 14 shipped occurrences vs. 144 of the unlocked variant `ลบมลทินบาป`, and `goel_kinsman_redeemer` locking `ผู้ไถ่ที่เป็นญาติ` which has 0 shipped occurrences anywhere. See `docs/CORPUS_VERIFICATION_WORKFLOW.md` for the rule.

---

## Theological key terms (what a Greek lemma renders as)

| Doc | Greek → Thai | Locked during |
|---|---|---|
| [ekklesia](ekklesia_2026-04.md) | ἐκκλησία → คริสตจักร (Christian community); ที่ประชุม (secular/OT assembly) | Matthew end-of-book |
| [aphesis_forgiveness_of_sins](aphesis_forgiveness_of_sins_2026-04.md) | ἄφεσις (ἁμαρτιῶν) → การยกโทษ(บาป); ปลดปล่อย for "release" sense (Luke 4:18) | Luke end-of-book |
| [dikaioo_dikaiosyne_family](dikaioo_dikaiosyne_family_2026-05.md) | δικαιόω (verb) + δικαίωσις/δικαίωμα-as-verdict → ทรงประกาศว่าชอบธรรม (forensic-declarative); preserves lexical distinction from λογίζομαι (นับ) | Galatians end-of-book + Romans 1-5 audit |
| [basileia_kingdom_rendering](basileia_kingdom_rendering_2026-04.md) | βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า; βασιλεία τῶν οὐρανῶν → อาณาจักรสวรรค์ (Matthew only) | Luke end-of-book |
| [ouranos_heaven_rendering](ouranos_heaven_rendering_2026-04.md) | οὐρανός → ฟ้าสวรรค์ (theological default); สวรรค์ (after a possessor); ท้องฟ้า (meteorological sky) | Luke end-of-book |
| [metanoeo_vs_metamelomai](metanoeo_vs_metamelomai_2026-04.md) | μετανοέω → กลับใจ (salvific); μεταμέλομαι → เปลี่ยนใจ (non-salvific reconsidering) | Matthew end-of-book |
| [psyche_vs_pneuma_anthropological](psyche_vs_pneuma_anthropological_2026-04.md) | ψυχή → จิตวิญญาณ (soul) / ชีวิต (life-force); πνεῦμα (anthropological) → จิต — distinct from Holy Spirit | Luke end-of-book |
| [son_of_man_disambiguation](son_of_man_disambiguation_2026-04.md) | ὁ υἱὸς τοῦ ἀνθρώπου (title) → บุตรมนุษย์; υἱοὶ τῶν ἀνθρώπων (humanity) → บุตรของมนุษย์ | Mark end-of-book |
| [ethnos](ethnos_2026-04.md) | ἔθνος three-way: ประชาชาติ (cosmic/Psalmic) / ชนชาติ (specific people-group, incl. Israel) / คนต่างชาติ (Gentiles, mission target) | Acts end-of-book |
| [pagan_deities](pagan_deities_2026-04.md) | Pagan-deity register: เทพ / เทพี / เทพเจ้า — never พระเจ้า. Personal-name deities → transliteration (Zeus → ซีอุส); abstract personifications → descriptive (Δίκη → เทพีแห่งความยุติธรรม) | Acts end-of-book |
| [roman_administrative_titles](roman_administrative_titles_2026-04.md) | χιλίαρχος → นายพัน; ἑκατοντάρχης → นายร้อย; ἡγεμών → ผู้ว่าราชการ; ἀνθύπατος → ผู้สำเร็จราชการ; πολιτάρχης → เจ้าหน้าที่ปกครองเมือง | Acts end-of-book |
| [christ_hymn_kenosis](christ_hymn_kenosis_2026-05.md) | μορφή → สภาพ (essence); σχῆμα → รูป (outward form); ἐκένωσεν → ทรงสละพระองค์เอง (NOT "emptied divinity"); ἁρπαγμός → สิ่งที่ต้องยึดไว้ (res rapta). Lock for PHP 2; validate forward against Col 1, 1 Tim 3:16, Heb 1, Eph 1:20–23, 1 Pet 3:18–22, Rev 5:9–14 | Philippians end-of-book |
| [pistis_christou](pistis_christou_2026-05.md) | πίστις Χριστοῦ → ความเชื่อในพระคริสต์ / ความเชื่อในพระเยซูคริสต์ (objective genitive default). Verse-level review preserved for Romans + future epistles, not a mechanical lock. GAL 2:16 + 3:22 already objective | Philippians end-of-book |
| [phroneo_pauline](phroneo_pauline_2026-05.md) | φρονέω three-branch split: คิด / ความคิด (cognitive disposition); จิตใจ (Christ-shaped settled disposition, PHP 2:5); ห่วงใย (active care, PHP 4:10). Forward applicability: Rom 8:5–7, 12:3, 12:16, 14:6, 15:5; Col 3:2 | Philippians end-of-book |
| [prototokos_pauline](prototokos_pauline_2026-05.md) | πρωτότοκος three-sense split: rank-comparative-of-creation = บุตรหัวปีเหนือ (COL 1:15); partitive-of-the-dead = บุตรหัวปีจากในหมู่ (COL 1:18, Rev 1:5); relational-of-believers = บุตรหัวปีในหมู่ (Rom 8:29, Heb 12:23). Includes the "go more-explicit than mainstream English" two-prong test | Colossians end-of-book |
| [stoicheia_tou_kosmou](stoicheia_tou_kosmou_2026-05.md) | στοιχεῖα τοῦ κόσμου → หลักการพื้นฐานของโลก (basic principles default). Names elemental-spirits reading explicitly so future verses can deviate when context demands. Cites GAL 4:3 + COL 2:8 as locking precedents | Colossians end-of-book (long-deferred from Galatians) |
| [spiritual_beings_hierarchy](spiritual_beings_hierarchy_2026-05.md) | Cosmic-power Pauline cosmology: θρόνοι → บัลลังก์; κυριότητες → ผู้ทρρเดชานุภาพ (NOT เทพ-prefix — collides with locked pagan-deities rule); ἀρχαί → ผู้ครอง; ἐξουσίαι → ผู้ทรงอำนาจ; δυνάμεις → ผู้ทรงสิทธิ. Two verses revised this PR (COL 1:16 + EPH 1:21) | Colossians end-of-book |
| [sarx_pauline](sarx_pauline_2026-05.md) | σάρξ four-sense polysemy: single Thai base (เนื้อหนัง / กาย) + contextual qualifiers + RULES §5 polysemy-flag discipline. Royal-prefix sub-sense for Christ's embodied flesh (พระวรกายฝ่ายเนื้อหนัง, COL 1:22). NO interpretive moral-coding. Critical before Romans 7–8 | Colossians end-of-book (long-deferred from Galatians) |

## Register & honorifics (when ราชาศัพท์ applies, when it doesn't)

| Doc | Rule | Locked during |
|---|---|---|
| [narrator_vs_character_voice](narrator_vs_character_voice_2026-04.md) | Narrator always uses ราชาศัพท์ for Jesus; character speech tracks the speaker's stance | Mark end-of-book |
| [honorifics_non_divine_authorities](honorifics_non_divine_authorities_2026-04.md) | Kings/governors/centurions/priests get plain Thai register, not ราชาศัพท์ | Mark end-of-book |
| [parabolic_god_figures_human_register](parabolic_god_figures_human_register_2026-04.md) | Parable characters representing God (fathers, kings, masters) get human register, never ราชาศัพท์ | Luke end-of-book |
| [vocative_kyrie_didaskale_register](vocative_kyrie_didaskale_register_2026-04.md) | Vocative Κύριε / Διδάσκαλε rendering varies principled-by-speaker-class (disciples vs. crowds vs. adversaries) | Luke end-of-book |
| [speech_verbs_adversaries_addressing_divine](speech_verbs_adversaries_addressing_divine_2026-04.md) | When narrator introduces adversary speech to Jesus: ทูล (preserves Jesus's divine status) regardless of speaker | Luke end-of-book |
| [adversary_speech_register](adversary_speech_register_2026-05.md) | Demon/adversary speech-introduction verbs use NEUTRAL form (กล่าว, NOT ทูล) — RULES §3 enforcement; Luke 4 corrected from corpus outlier | Luke end-of-book |
| [divine_object_praise_verbs](divine_object_praise_verbs_2026-04.md) | δοξάζω / εὐλογέω / αἰνέω / αἶνον δίδωμι (object = God) → สรรเสริญ (single Thai default) | Luke end-of-book |
| [kyrios_narrator_voice_luke_acts](kyrios_narrator_voice_luke_acts_2026-04.md) | Luke-Acts signature: narrator calls Jesus ὁ κύριος → องค์พระผู้เป็นเจ้า (Mark/Matthew don't do this) | Luke end-of-book |
| [parousia_christou](parousia_christou_2026-05.md) | παρουσία subject-driven register split: human subject → การมา / การกลับไป (plain); Christ eschatological subject → การเสด็จมา (royal); lawless one in 2 Thess 2:9 → plain (deliberate denial of royal honor). Thai grammatical requirement, not theological imposition | Philippians end-of-book |

## Narrative style & idiom (how Greek narrative-mechanical features render)

| Doc | Rule | Locked during |
|---|---|---|
| [historic_present](historic_present_2026-04.md) | Greek historic-present verbs (mid-narrative present-tense) render as Thai past tense; do not preserve present morphology | Mark end-of-book |
| [markan_euthys_immediately](markan_euthys_immediately_2026-04.md) | εὐθύς / εὐθέως: context-sensitive choice from a small consistent set (ทันใดนั้น / ในทันใด / และก็); not a single locked rendering | Mark end-of-book |
| [amen_saying_formula](amen_saying_formula_2026-04.md) | ἀμὴν λέγω ὑμῖν (Synoptic single) → "เราบอกความจริงแก่พวกท่าน(ว่า)" | Mark end-of-book |
| [johannine_doubled_amen](johannine_doubled_amen_2026-04.md) | ἀμὴν ἀμὴν λέγω ὑμῖν (Johannine doubled, 25× in John) → "อาเมน อาเมน เราบอกแก่พวกท่านว่า" — Aramaic-embed treatment | John 1 spot-review |
| [aramaic_transliterations](aramaic_transliterations_2026-04.md) | Aramaic words Mark embeds (Talitha cumi, Ephphatha, Abba, etc.) — preserve Thai-script transliteration AND Mark's own Greek translation | Mark end-of-book |

## Textual variants (how SBLGNT-omitted readings appear in the Thai text)

| Doc | Rule | Locked during |
|---|---|---|
| [inclusion_variants_absent_verses](inclusion_variants_absent_verses_2026-04.md) | Path A 3-tier policy: Tier 1 short-phrase `[...]`; Tier 2 whole-verse footer note; Tier 3 large blocks `⟦...⟧`. Matches BSB/ESV/NIV/CSB convention. | Matthew end-of-book |
| [pastoral_corpus_locks](pastoral_corpus_locks_2026-05.md) §H | Tier-2 `reading_variant` sub-type (word-substitution, not whole-verse omission). 1 Tim 3:16 Ὃς vs Θεός is the first instance. | 1 Timothy end-of-book |

## Pastoral-Epistle corpus locks (1 Tim, 2 Tim, Titus)

| Doc | Rule | Locked during |
|---|---|---|
| [pastoral_corpus_locks](pastoral_corpus_locks_2026-05.md) | Bundle of corpus-level locks for the Pastorals: πιστὸς ὁ λόγος formula (A); εὐσέβεια default ความเคร่งในพระเจ้า (B); σωτήρ for Father AND Christ + Tit 2:13 Granville-Sharp pre-decision (C); ἀρσενοκοίτης (D); women-in-worship ambiguity strategy with thai_summary guardrails (E); Phoebe-style διάκονος openness for Rom 16:1 (F); μιᾶς γυναικὸς ἄνδρα + 5:9 feminine inversion (G); 3:16 Ὃς + Tier-2 Byzantine footer (H); 2 Tim 3:16 πᾶσα γραφὴ θεόπνευστος → พระคัมภีร์ทั้งหมดเป็นลมพระโอษฐ์ของพระเจ้า (I); metaphor-flattening principle for non-determinative imagery (J); extra-canonical-tradition acknowledgment policy + Jude 9/14-15 pre-commits (K) | 1 Timothy + 2 Timothy end-of-book |
| [epiphaneia_christou](epiphaneia_christou_2026-05.md) | ἐπιφάνεια applied to Christ → การทรงปรากฏ uniformly across Pastorals (1 Tim 6:14, 2 Tim 1:10, 4:1, 4:8, Tit 2:13). Context disambiguates first-coming vs second-coming. 1 Tim 6:14 retroactively conformed 2026-05-03 from prior heavier rendering | 2 Timothy end-of-book |
| [hygiaino_sound_doctrine](hygiaino_sound_doctrine_2026-05.md) | ὑγιαίνω + cognates applied to teaching/words/doctrine → ถูกต้อง uniformly across Pastorals (1 Tim 1:10, 6:3; 2 Tim 1:13, 4:3; Tit 1:9, 13; 2:1, 2). Distinct from Gospel medical-healing usage (separate semantic field). First explicit application of metaphor-flattening principle (`pastoral_corpus_locks` §J) across a full lemma-family | 2 Timothy end-of-book (gates Titus) |

---

## How decisions get made (process)

A doc lands here when an end-of-book review (`docs/<BOOK>_END_OF_BOOK_REVIEW_*.md` per `END_OF_BOOK_CHECKLIST.md`) surfaces a corpus-level pattern that:

1. Is operating consistently across the shipped corpus, **OR** is being newly locked after spot-revision, AND
2. Will compound across future books if not documented (e.g., ekklesia compounds into Acts + Pauline + Revelation), AND
3. Has rationale that wouldn't be obvious from per-verse `key_decisions` alone.

External AI reviews (Grok / Gemini / ChatGPT — see `external_review_packet_*.md`) frequently flag candidate items for new docs.

## When to read these

- **Translating a new chapter:** scan the index; if your chapter contains any of the locked terms, follow the rule.
- **Adding a new corpus-level rule:** check no existing doc covers it; if a related doc exists, update or cross-reference rather than duplicate.
- **External reviewer / Thai scholar:** the "Locked during" column tells you which book's audit (`docs/<BOOK>_END_OF_BOOK_REVIEW_*.md`) contains the deliberation that led to each lock.

## Why this index exists

Without it, the 19 decision docs are discoverable only by directory listing or grep. The structure surfaces what's locked at-a-glance for new contributors and external reviewers.
