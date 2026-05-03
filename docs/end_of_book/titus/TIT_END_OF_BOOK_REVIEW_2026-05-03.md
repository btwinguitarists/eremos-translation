# Titus — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 3 chapters (46 verses; ~95 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (42 docs, including the two new 2026-05-03 docs `epiphaneia_christou_2026-05.md` + `hygiaino_sound_doctrine_2026-05.md` written during 2TI end-of-book + applied prospectively across TIT).
**Trigger:** TIT 3 shipped (commit `776b350`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 3/3 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the now-132-chapter corpus, with the new lemma `νηφαλίους` documented multi-rendering surfacing TIT 1:8/2:2 dual-form); `check_phrase_consistency.py` clean across all 8 audited locks; `audit_inclusion_variants.py --book titus --strict` PASSES (0 candidates — Titus is unusually clean for a Pastoral); `export_to_usfm.py --book TIT` regenerates `output/paratext/TIT.SFM` cleanly.
- **Titus is the THIRD AND FINAL PASTORAL EPISTLE** shipped. It inherits the full corpus discipline of `pastoral_corpus_locks_2026-05.md` (§A–§K) plus the two new 2026-05-03 corpus docs written during 2TI end-of-book audit response (`epiphaneia_christou_2026-05.md`; `hygiaino_sound_doctrine_2026-05.md`). **All Pastoral-distinctive lemma-clusters comply with the corpus locks.** The Pastoral pipeline is now editorially complete.
- **All five Pastoral-distinctive corpus clusters from `pastoral_corpus_locks_2026-05.md` confirmed compliant**: πιστὸς ὁ λόγος (3:8 — 5th and final Pastoral occurrence, bare-form variant), εὐσέβεια family (1:1 noun + 2:12 adverb), σωτήρ Pastoral-shift (Father at 1:3, 2:10, 3:4; Christ at 1:4, 2:13, 3:6 — corpus-balance achieved), ὑγιαίνω sound-doctrine (5 occurrences — densest single-letter cluster: 1:9, 1:13, 2:1, 2:2, 2:8 ὑγιής cognate), women-in-worship ambiguity-preservation (2:3-5 + 2:9-10 household-codes). **Plus the Granville-Sharp pre-decision at 2:13** (per §C) applied verbatim to **พระเยซูคริสต์ พระเจ้าผู้ยิ่งใหญ่และพระผู้ช่วยให้รอดของเรา**.
- **Titus introduces several NEW corpus-cross-cutting items**: (1) **πρεσβύτερος = ἐπίσκοπος terminological equivalence** at 1:5+1:7 — the Pastoral-elder-overseer interchange in densest form; (2) **ἐπιστομίζω + ἀποτόμως + γαστέρες + ἱεροπρεπής** — densest §J metaphor-flattening cluster in the corpus (4 verses in ch.1-2); (3) **1:12 Epimenides paradox citation** — 1 of only 3 NT pagan-Greek-poet citations (cf. ACT 17:28 Aratus, 1 Cor 15:33 Menander); (4) **2:11-14 + 3:4-7 doxological-hymn-pair** — two parallel ἐπεφάνη-grace-/-kindness doxologies with shared σύν-χάρις architecture; (5) **3:5 λουτροῦ παλιγγενεσίας + ἀνακαινώσεως πνεύματος ἁγίου** — the NT's most-debated baptismal-regeneration crux; (6) **2:14 περιούσιος** HAPAX with LXX-Exod 19:5 covenant-vocabulary echo; (7) **3:10 αἱρετικός** HAPAX rendered as relational-divisive (not doctrinal-heretic).
- **HAPAX density:** Titus contains **~30 HAPAX legomena** across 46 verses — the densest HAPAX-rate per verse in the NT (excluding Jude). The translator's principled metaphor-flattening discipline (§J) is exercised heavily here.
- **All inherited corpus locks compliant** (see §14): Pastoral-corpus-locks §A–§K, plus the two new 2026-05-03 docs (epiphaneia + hygiaino), plus the broader Pauline / general-corpus locks (κύριος-narrator-voice, δοῦλος, χάρις, εἰρήνη, ἔλεος, σωτηρία, δικαιοσύνη family, βασιλεία, ζωὴ αἰώνιος, μῦθοι, διάβολος, διακονία family).
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: πρεσβύτερος vs ἐπίσκοπος Thai distinct rendering at 1:5+1:7; 3:5 λουτροῦ παλιγγενεσίας single-vs-dual washing-event reading; 3:10 αἱρετικός relational-vs-doctrinal rendering).
- **2 items flagged STABLE-but-noteworthy** (1:12 Epimenides pagan-poet citation handling; 2:14 περιούσιος LXX-echo preservation).
- **0 items flagged DECIDE.** With the 2 Tim 3:16 θεόπνευστος + πᾶσα γραφή DECIDE resolved at 2TI end-of-book (now §I in `pastoral_corpus_locks_2026-05.md`) and the 2:13 Granville-Sharp pre-decided, Titus inherits a fully-ratified Pastoral corpus and presents no DECIDE blockers for the v1 tag.
- **External AI review (§3) packet pending.** 4-cluster suggested (smaller than 1TI's 8-item; smaller than 2TI's 6-item — Titus has fewer load-bearing decisions because the corpus discipline was front-loaded in 1TI + 2TI).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. πιστὸς ὁ λόγος formula at 3:8 — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §A)**

The **fifth and final** corpus occurrence of the Pastoral citation-formula (1 Tim 1:15; 3:1; 4:9; 2 Tim 2:11; Tit 3:8). Renders **ถ้อยคำนี้เชื่อถือได้** — bare-form variant matching 1 Tim 3:1 + 2 Tim 2:11 (the formula appears without the πάσης ἀποδοχῆς ἄξιος expansion).

| Verse | Greek | Thai | Reference direction |
|---|---|---|---|
| 3:8 | Πιστὸς ὁ λόγος (preceded by vv.4-7 doxology) | **ถ้อยคำนี้เชื่อถือได้** | **Backward** (the saying = the salvation-by-grace + Spirit + justification + heir doxology of vv.4-7) |

The 3:8 KD names the locking precedent + reference-direction:

> CORPUS-LOCKED Pastoral citation-formula per pastoral_corpus_locks §A — 5th and FINAL Pastoral occurrence (after 1 Tim 1:15 + 1 Tim 3:1 + 1 Tim 4:9 + 2 Tim 2:11). NO expansion (καὶ πάσης ἀποδοχῆς ἄξιος) here — render with the bare formula 'ถ้อยคำนี้เชื่อถือได้' exactly as 1 Tim 3:1 + 2 Tim 2:11 (the bare form). Per uW writing-pronouns: ὁ λόγος refers back to vv.4-7 (the salvation-by-grace-+-Spirit-+-justification-+-heir saying).

**Editorial assessment:** Compliant. The 3:8 occurrence completes the Pastoral 5-instance corpus and confirms the §A lock's reference-direction-flexibility (this is the cleanest backward-reference of the five — the formula sits immediately after a self-contained doxological saying).

**LOCKED** — no action.

---

## 2. εὐσέβεια family at 1:1 + 2:12 — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §B)**

| Verse | Greek | Thai | Form |
|---|---|---|---|
| 1:1 | ἐπίγνωσιν ἀληθείας τῆς κατ' εὐσέβειαν | **ความรู้แห่งความจริงซึ่งนำไปสู่ความเคร่งในพระเจ้า** | noun (genitive object of κατά) |
| 2:12 | σωφρόνως καὶ δικαίως καὶ εὐσεβῶς ζήσωμεν | **ดำเนินชีวิตอย่างมีสติสัมปชัญญะ อย่างชอบธรรม และด้วยความเคร่งในพระเจ้า** | adverb |

Both occurrences apply the §B lock verbatim:
- 1:1 noun → **ความเคร่งในพระเจ้า**
- 2:12 adverb → **ด้วยความเคร่งในพระเจ้า** (matching §B's verbal-form pattern at 1 Tim 4:7-8; 2 Tim 3:12)

**Editorial assessment:** Compliant. The 2:12 adverb sits inside the three-fold Christian-life pattern (oneself + neighbor + God: σωφρόνως / δικαίως / εὐσεβῶς) — one of the corpus's clearest summary-of-virtue formulations. The 1:1 noun anchors the εὐσέβεια / ἀλήθεια linkage that runs throughout the Pastorals (truth produces godliness, not vice versa).

**LOCKED** — no action.

---

## 3. σωτήρ Pastoral Christological-shift — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §C)**

Titus completes the **6 Father-Savior + 4 Christ-Savior** corpus-distribution that §C anticipates. **All 6 occurrences compliant.**

| Verse | Greek | Thai | Referent |
|---|---|---|---|
| 1:3 | κατ' ἐπιταγὴν τοῦ σωτῆρος ἡμῶν θεοῦ | **ตามพระบัญชาของพระเจ้าพระผู้ช่วยให้รอดของเรา** | Father |
| 1:4 | καὶ Χριστοῦ Ἰησοῦ τοῦ σωτῆρος ἡμῶν | **และจากพระเยซูคริสต์ พระผู้ช่วยให้รอดของเรา** | Christ |
| 2:10 | τὴν διδασκαλίαν τὴν τοῦ σωτῆρος ἡμῶν θεοῦ | **คำสอนของพระเจ้าพระผู้ช่วยให้รอดของเรา** | Father |
| 2:13 | καὶ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ | **(see §4 Granville-Sharp)** | **Christ (Granville-Sharp single-person)** |
| 3:4 | τοῦ σωτῆρος ἡμῶν θεοῦ | **พระเจ้าพระผู้ช่วยให้รอดของเรา** | Father |
| 3:6 | διὰ Ἰησοῦ Χριστοῦ τοῦ σωτῆρος ἡμῶν | **โดยทางพระเยซูคริสต์ พระผู้ช่วยให้รอดของเรา** | Christ |

**Striking observation:** Titus has the **densest σωτήρ-cluster in the NT**: 6 occurrences in 46 verses (vs. 3 in 1TI's 113 verses; 1 in 2TI's 83 verses). The Father/Christ split (3+3) is balanced — **Titus alone confirms the §C bidirectional-Christological pattern** more clearly than the rest of the Pastorals combined.

**Editorial assessment:** All 6 use the same **พระผู้ช่วยให้รอด** lemma (per §C uniform-rendering rule); only the apposition shifts (พระเจ้า vs. พระเยซูคริสต์). The 3:4 + 3:6 pair within the same doxology (Father-Savior + Christ-Savior in the same passage) is the textbook §C dual-σωτήρ pattern — both sides of the Pastoral Christological-shift in one paragraph.

**LOCKED** — no action.

---

## 4. 2:13 Granville-Sharp single-person Christological reading — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §C pre-decision)**

> 2:13 GK: τὴν μακαρίαν ἐλπίδα καὶ ἐπιφάνειαν τῆς δόξης **τοῦ μεγάλου θεοῦ καὶ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ**
> TH: ความหวังอันเปี่ยมพร และการทรงปรากฏแห่งพระสิริของ**พระเยซูคริสต์ พระเจ้าผู้ยิ่งใหญ่และพระผู้ช่วยให้รอดของเรา**

The §C pre-decision (locked at 1TI end-of-book; ratified by all three external reviewers Grok / Gemini / ChatGPT) committed to the single-person Granville-Sharp reading. The Thai construction at 2:13 applies the provisional rendering verbatim — **พระเยซูคริสต์, พระเจ้าผู้ยิ่งใหญ่และพระผู้ช่วยให้รอดของเรา**.

The 2:13 KD documents the application:

> CORPUS-LOCKED Granville-Sharp single-person reading per pastoral_corpus_locks §C pre-decision. The Greek construction (single article governing both nouns: τοῦ μεγάλου θεοῦ καὶ σωτῆρος) is widely recognized by modern evangelical scholarship as referring to a single subject — Jesus Christ as both 'our great God' AND 'our Savior.' All three external reviewers (Grok, Gemini, ChatGPT) converged at 1 Tim end-of-book review. Render 'พระเยซูคริสต์ พระเจ้าผู้ยิ่งใหญ่และพระผู้ช่วยให้รอดของเรา' — Thai apposition naturally supports the single-person reading without forced syntax.

**Editorial assessment:** This is the **highest-Christological verse in the Pastorals** and one of the strongest NT-witness verses to the deity-of-Christ. The Thai apposition (subject-name first, then descriptive titles) reads naturally in Thai sequence-of-identification without forcing the Granville-Sharp grammatical pattern onto Thai syntax. Render confirms the §C pre-decision held cleanly through to translation-time.

**LOCKED** — no action.

---

## 5. ἐπιφάνεια / ἐπιφαίνω at 2:11, 2:13, 3:4 — **LOCKED (compliant with `epiphaneia_christou_2026-05.md`)**

The new 2026-05-03 corpus doc (written during 2TI end-of-book audit response) locked ἐπιφάνεια → **การทรงปรากฏ** corpus-wide. Titus applies the lock plus the verb-cognate ἐπιφαίνω at 2:11 + 3:4:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 2:11 | Ἐπεφάνη γὰρ ἡ χάρις τοῦ θεοῦ | **เพราะพระคุณของพระเจ้าได้ทรงปรากฏแล้ว** | first-coming (Incarnation; verb-form) |
| 2:13 | ἐπιφάνειαν τῆς δόξης | **การทรงปรากฏแห่งพระสิริ** | second-coming (noun-form) |
| 3:4 | ἡ χρηστότης καὶ ἡ φιλανθρωπία ἐπεφάνη | **ความเมตตาและความรักที่ ... ได้ทรงปรากฏแล้ว** | first-coming (Incarnation; verb-form) |

**Editorial observation:** Titus exhibits the corpus's **clearest dual-sense ἐπιφάνεια application** — first-coming (2:11 + 3:4) + second-coming (2:13) within a single letter, all using the same root-rendering **ทรงปรากฏ**. This validates the new corpus-doc's central claim that one Thai lemma can carry both senses with context disambiguating. The doxological-pair structure (2:11-14 + 3:4-7) puts the two senses in deliberate parallel — both are "appearances of divine attributes" (grace + kindness/love), both initiating salvific action, both producing the same ethical-doxological response.

The corpus doc anticipated this exactly:

> ἐπιφάνεια applied to Christ → การทรงปรากฏ uniformly across the Pastorals, regardless of whether the referent is first-coming (Incarnation) or second-coming (parousia). Context disambiguates which appearing.

**LOCKED** — no action.

---

## 6. ὑγιαίνω + ὑγιής sound-doctrine cluster (1:9, 1:13, 2:1, 2:2, 2:8) — **LOCKED (compliant with `hygiaino_sound_doctrine_2026-05.md`)**

Titus contains the **densest single-letter ὑγιαίνω-family cluster in the NT** — 5 occurrences in 32 verses of chs.1-2, all rendered with **ถูกต้อง** lemma-core. The new corpus doc anticipated this exact cluster:

| Verse | Greek | Thai | Construction |
|---|---|---|---|
| 1:9 | ἐν τῇ διδασκαλίᾳ τῇ ὑγιαινούσῃ | **ด้วยคำสอนอันถูกต้อง** | "sound teaching" — apostolic content |
| 1:13 | ὑγιαίνωσιν ἐν τῇ πίστει | **มีความเชื่อที่ถูกต้อง** | verbal — sound-IN-the-faith |
| 2:1 | τῇ ὑγιαινούσῃ διδασκαλίᾳ | **คำสอนอันถูกต้อง** | "sound teaching" — Titus's mandate |
| 2:2 | ὑγιαίνοντας τῇ πίστει, τῇ ἀγάπῃ, τῇ ὑπομονῇ | **มีความถูกต้องในความเชื่อ ในความรัก และในความอดทน** | predicate — sound IN faith/love/perseverance |
| 2:8 | λόγον ὑγιῆ ἀκατάγνωστον | **คำพูดอันถูกต้องที่ไม่อาจหาที่ติได้** | ὑγιής cognate — "sound speech" |

**Editorial assessment:** The corpus doc's lemma-family lock holds **across noun + verbal + predicate-adjective + cognate-adjective forms** — a stronger test than 2TI offered (which had only 2 occurrences). The Thai construction varies syntactically (อัน + adjectival; ที่ + relative; ความ + abstract noun + ใน) but the lemma core **ถูกต้อง** is preserved in every form. This is the cleanest possible compliance.

**Notable:** 2:2's three-fold predicate construction (sound-in-faith, in-love, in-perseverance) preserves the triadic structure with **มีความถูกต้องใน ... ใน ... และใน** — the core lemma + locative repetition supplies the parallelism without forcing wooden adverbial constructions.

**LOCKED** — no action.

---

## 7. πρεσβύτερος = ἐπίσκοπος terminological equivalence at 1:5 + 1:7 — **REVIEW (Thai distinct lemma may obscure the Greek equivalence)**

This is the corpus's clearest Pastoral elder-overseer interchange:

> 1:5 GK: καὶ καταστήσῃς κατὰ πόλιν **πρεσβυτέρους** | TH: และตั้ง**ผู้ปกครอง**ในแต่ละเมือง
> 1:7 GK: δεῖ γὰρ τὸν **ἐπίσκοπον** ἀνέγκλητον εἶναι | TH: เพราะ**ผู้ปกครองดูแล**ต้องเป็นคนไม่มีข้อตำหนิ

The Greek explicitly equates the two terms: v.5 introduces πρεσβύτερος as the office; v.7 — connected by γάρ ("for") — explains the qualification using ἐπίσκοπος as the same office's functional name. The 1:7 KD names this:

> ἐπίσκοπος → ผู้ปกครองดูแล corpus-precedent 1 Tim 3:1-2 same Thai. Per uW translate-unknown: 'overseer' is alternate name for the same office Paul called πρεσβύτερος at v.5 — function-of-the-elder being-an-overseer.

**Editorial assessment:** The Thai render uses **two distinct lexical items** — **ผู้ปกครอง** (πρεσβύτερος, "ruler / one-who-presides") + **ผู้ปกครองดูแล** (ἐπίσκοπος, "ruling-overseer"). They share the same root (**ผู้ปกครอง**) so the structural equivalence is preserved through the shared-stem; the **ดูแล** ("oversee / look-after") suffix differentiates the ἐπίσκοπος-instance.

**The REVIEW question:** Is the structural-stem-shared / suffix-differentiated approach **principled enough** for a Thai reader to perceive the πρεσβύτερος = ἐπίσκοπος equivalence the Greek deliberately makes? Two alternatives:
- (a) **Identical Thai rendering** for both (e.g., **ผู้ปกครองดูแล** for both) — would force the equivalence at the cost of the Greek's lexical-pair distinctness
- (b) **thai_summary at 1:7** explicitly noting the equivalence — current 1:7 notes do mention it ("alternate name for the same office") but the **thai_summary** is not present at 1:7

The current rendering is **defensible and principled** but worth Ben's confirmation as the corpus-default for forward-Pastoral application (especially relevant for Acts 20:17+28 where Paul uses both terms of the Ephesian elders, and 1 Pet 5:1-2 πρεσβύτερος / ἐπισκοποῦντες).

**Recommend: REVIEW** — confirm with Ben. If confirmed, this should become a brief note in the deferred 1TI §L#5 doc-to-write `pastoral_offices_episkopos_presbyteros_diakonos_2026-XX.md` (see §13).

---

## 8. 1:11, 1:13, 1:12, 2:3 metaphor-flattening cluster — **LOCKED (compliant with `pastoral_corpus_locks_2026-05.md` §J)**

Titus contains the **densest §J metaphor-flattening application in the corpus** — four distinct metaphor-vehicle-flattening events in chs.1-2:

| Verse | Greek | Vehicle (literal) | Thai (target sense) | §J test |
|---|---|---|---|---|
| 1:11 | ἐπιστομίζειν | "muzzle / put-mouth-on" | **ห้ามไม่ให้พูด** ("forbid from speaking") | vehicle-fails (physical-restraint reads incongruous in Thai for human-teachers) |
| 1:13 | ἀποτόμως | "by-cutting-off" | **อย่างเคร่งครัด** ("strictly") | vehicle-fails (cutting reads as physical-violence in Thai) |
| 1:12 | γαστέρες ἀργαί | "lazy bellies" (synecdoche) | **คนตะกละและเกียจคร้าน** ("gluttonous and lazy") | vehicle-fails (belly-synecdoche reads as vulgar/cartoonish for character in Thai) |
| 2:3 | ἱεροπρεπεῖς | "sacred-fitting / priestly-suitable" | **กิริยาที่สมศักดิ์ศรี** ("dignified bearing") | vehicle-fails (clerical-frame too narrow for daily-life-comportment in Thai) |

**Editorial assessment:** Each of the four passes the §J working test (vehicle-not-determinative + no-clean-Thai-cognate-domain). The 1:11 KD explicitly cites the §J principle:

> Per pastoral_corpus_locks_2026-05.md §J metaphor-flattening principle: vehicle (muzzle-imagery) does not transfer cleanly to Thai for human-teachers; target sense (silence-from-teaching) preserved.

The **counter-example (vehicle-preserved-because-determinative)** in Titus is **3:11 ἐκστρέφομαι** ("turn-out / pervert") at v.11, rendered **ได้หันเหไปผิดทาง** ("has-turned-aside-on-wrong-path") — the path-imagery transfers cleanly to Thai and the metaphor IS determinative for the verse's argument (the divisive person has "turned" off the right way), so vehicle is preserved.

**LOCKED** — no action. The §J principle is now **stress-tested across all three Pastoral letters** with consistent application.

---

## 9. 1:12 Epimenides paradox citation — **STABLE (uniform with broader pagan-poet-citation strategy; consider future doc)**

> 1:12 GK: εἶπέν τις ἐξ αὐτῶν, ἴδιος αὐτῶν προφήτης, "**Κρῆτες ἀεὶ ψεῦσται, κακὰ θηρία, γαστέρες ἀργαί**"
> TH: มีคนหนึ่งในพวกเขาเอง ซึ่งเป็นผู้พยากรณ์ของพวกเขา ได้กล่าวว่า "**ชาวครีตเป็นคนพูดเท็จเสมอ เป็นสัตว์ร้าย เป็นคนตะกละและเกียจคร้าน**"

This is **1 of only 3 NT pagan-Greek-poet citations** (alongside Acts 17:28 Aratus *Phaenomena* + 1 Cor 15:33 Menander *Thais*). Three editorial choices made:
- (a) **προφήτης → ผู้พยากรณ์** — preserved with classical-pagan ambiguity (not narrowed to Hebrew "prophet-of-YHWH")
- (b) **ἀεί ψεῦσται preserved as hyperbole** ("เสมอ") — keeps the famous Liar's-Paradox rhetorical force
- (c) **RULES §5b direct-speech curly-quotes** applied — quoted Epimenides text in Thai "..." (Cretica fragment)

The 1:12 thai_summary **explicitly identifies Epimenides + frames the citation as cultural-self-criticism (not racist-derision)**:

> 'ผู้พยากรณ์ของพวกเขา' ที่เปาโลอ้างถึงคือ 'เอพิเมนิเดส' (Epimenides) กวีและนักปรัชญาชาวเกาะครีตในศตวรรษที่ 6 ก่อนคริสต์ศักราช ... เปาโลใช้คำพูดของเขาในเชิง 'การวิจารณ์ที่มาจากภายในของพวกเขาเอง' ไม่ใช่การดูถูกเหยียดหยามแบบเชื้อชาตินิยม

**Editorial assessment:** The thai_summary handling is **scholarly and editorially-mature** — Thai readers benefit from understanding the Cretan-cultural-critique context, the Liar's-Paradox logical-classical fame, and the editorial guard against racist-misreading. This is the **right model** for forward-pagan-citation handling (cf. ACT 17:28 Aratus and 1 Cor 15:33 Menander, both not yet shipped).

**Recommend: STABLE** — no immediate action. **Future consideration:** when ACT 17:28 + 1 Cor 15:33 ship, consider lifting the principles into a brief corpus doc `pagan_poet_citations_2026-XX.md` (3 corpus-occurrences total; closed corpus-set; low priority but principled).

---

## 10. 2:14 περιούσιος HAPAX + LXX-Exod 19:5 covenant-vocabulary echo — **STABLE (LXX-echo handling principled)**

The HAPAX περιούσιος (only here NT) carries direct lexical-echo of LXX Exod 19:5 + Deut 7:6 + Deut 14:2 + Deut 26:18 — the OT covenant-people-of-special-possession formula:

> 2:14 GK: καθαρίσῃ ἑαυτῷ **λαὸν περιούσιον**
> TH: ทรงชำระ**ประชากรเป็นของพระองค์เอง**ให้บริสุทธิ์

The 2:14 KD documents the LXX-echo:

> HAPAX περιούσιος (only here NT) — though present in LXX Exod 19:5 + Deut 7:6 + Deut 14:2 + Deut 26:18 (covenant-people-of-special-possession). Render 'ประชากรเป็นของพระองค์เอง' — preserves the possessive-special-property sense without forcing the wooden 'ทรัพย์สมบัติพิเศษ' (which would commodify-the-people image). LXX ECHO of Exod 19:5 — see notes.

The thai_summary contextualizes the covenant-extension theology:

> วลี 'ประชากรเป็นของพระองค์เอง' (กรีก λαὸς περιούσιος) ยืมจากพันธสัญญาเดิม ... การใช้คำนี้กับคริสเตียนของเปาโลที่นี่ และในเปโตรฉบับที่หนึ่ง 2:9 บ่งบอกว่าคริสตจักรเป็นผู้ที่สืบทอดพันธสัญญาของอิสราเอลในความหมายเชิงเทววิทยา — ไม่ใช่แทนที่อิสราเอล แต่ขยายชนชาติของพระเจ้าให้รวมทั้งคนต่างชาติด้วย

**Editorial assessment:** **Editorially-mature handling** — render preserves the possessive-special-property sense without forcing wooden Thai; thai_summary surfaces the OT-covenant linkage AND the supersessionism-guardrail (per RULES §0). The non-supersessionist guardrail is the right pastoral move for Thai-evangelical readers shaped by replacement-theology preaching traditions.

**Recommend: STABLE** — no new doc needed. Worth flagging at 1 Pet 2:9 ship-time (the parallel covenant-extension verse in the canonical-NT) for cross-reference handling.

---

## 11. 3:5 λουτροῦ παλιγγενεσίας + ἀνακαινώσεως πνεύματος ἁγίου — **REVIEW (single-vs-dual washing-event reading)**

The NT's most-debated baptismal-regeneration / sacramental-soteriology crux:

> 3:5 GK: ἔσωσεν ἡμᾶς διὰ **λουτροῦ παλιγγενεσίας** καὶ **ἀνακαινώσεως πνεύματος ἁγίου**
> TH: พระองค์ทรงช่วยเราให้รอด ... โดยทาง**การชำระล้างแห่งการบังเกิดใหม่** และ**การสร้างใหม่โดยพระวิญญาณบริสุทธิ์**

Two competing grammatical readings:
- (a) **One event with two characterizations**: "the washing-of-rebirth-AND-of-renewal-by-the-Spirit" — single-genitive-construction with both παλιγγενεσίας + ἀνακαινώσεως modifying λουτροῦ (sacramental-baptismal-regeneration interpretation; favored by patristic + Roman Catholic + some Reformed)
- (b) **Two events / two means**: "washing-of-rebirth AND renewal-by-the-Spirit" — two coordinate-genitives expressing distinct-yet-paired soteriological moments (most modern evangelical: justification-and-sanctification frame)

The 3:5 KD names the editorial choice + flags the construction-debate:

> The construction is debated: (1) 'washing-of-rebirth-AND-renewal-of-Spirit' (parallel datives), (2) 'washing-of-rebirth-and-of-renewal-of-Spirit' (single washing with two genitives modifying it). Render preserves both possibilities by coordinate 'การชำระล้างแห่ง... และการสร้างใหม่โดย...' leaning slightly toward (1) for natural Thai flow without forcing the reading.

**Editorial assessment:** The Thai **การชำระล้างแห่งการบังเกิดใหม่ และการสร้างใหม่โดยพระวิญญาณบริสุทธิ์** uses the conjunction **และ** ("and") to coordinate two events — leaning toward reading (b) without committing entirely. The **โดย** ("by-means-of") for ἀνακαινώσεως πνεύματος ἁγίου explicitly marks the Spirit as agent — a slight commitment to reading (b) over (a)'s single-modified-noun structure.

**The REVIEW question:** Is the slight (b)-leaning principled? Compare mainstream English:
- **BSB / NIV / CSB**: "washing of regeneration and renewal by the Holy Spirit" (similar (b)-leaning)
- **ESV**: "the washing of regeneration and renewal of the Holy Spirit" (more (a)-preserving — same construction Thai could have used)
- **NRSV**: "the water of rebirth and renewal by the Holy Spirit" (clearly (b))
- **KJV / NKJV**: "the washing of regeneration, and renewing of the Holy Ghost" (preserves single-vs-dual ambiguity)

The thai_summary explicitly embraces interpretation (a) for the **first** half ("'การชำระล้างแห่งการบังเกิดใหม่' มักถูกเข้าใจว่าหมายถึงประสบการณ์การรับบัพติศมาในฐานะสัญลักษณ์ภายนอกของการบังเกิดใหม่ภายในโดยพระวิญญาณ"). This is the **historical-mainstream-evangelical** reading (baptism-as-symbol-of-regeneration; Spirit-as-effecting-agent), but:

(1) The thai_summary commits to a baptismal-symbol-interpretation that the main text leaves grammatically open
(2) Thai-evangelical readers shaped by THSV / TNCV (which also use **การชำระล้างแห่งการบังเกิดใหม่** but typically without baptism-thai_summary commitment) may find the explicit baptismal-frame editorially-strong

**Recommend: REVIEW** — confirm with Ben on two sub-questions:
1. Is the slight (b)-leaning + **โดย-marked Spirit-agency** the right corpus-default for the construction, or should the Thai preserve a more (a)-style ambiguity (e.g., **การชำระล้างแห่งการบังเกิดใหม่และการสร้างใหม่โดยพระวิญญาณบริสุทธิ์** without the **และ** event-separator, leaning toward "the washing-of-rebirth-and-renewal-by-the-Spirit" as a single complex genitive)?
2. Should the thai_summary's baptismal-symbol commitment soften to neutral interpretation-presentation (e.g., "หลายคนเข้าใจว่า ... แต่บางคนเข้าใจว่า") to match the main text's grammatical-openness?

---

## 12. 3:10 αἱρετικός HAPAX → **คนที่ก่อให้เกิดการแตกแยก** — **REVIEW (relational-divisive vs doctrinal-heretic register)**

> 3:10 GK: **αἱρετικὸν** ἄνθρωπον μετὰ μίαν καὶ δευτέραν νουθεσίαν παραιτοῦ
> TH: จงปฏิเสธ**คนที่ก่อให้เกิดการแตกแยก** หลังจากตักเตือนเขาครั้งที่หนึ่งและครั้งที่สองแล้ว

The HAPAX αἱρετικός (only here NT) is rendered **คนที่ก่อให้เกิดการแตกแยก** ("divisive person"). The 3:10 KD names the editorial choice:

> HAPAX αἱρετικός (only here NT) — adjectival from αἵρεσις 'faction / sect.' Per uW figs-explicit: implication is divisive-in-the-church (causing-faction-formation). Render 'คนที่ก่อให้เกิดการแตกแยก' — preserves the divisive-in-community sense without forcing the modern 'heretic' register (which would import doctrinal-deviation as primary, when the early-church αἱρετικός sense is closer to 'schism-causing'). The rendering captures both the doctrinal-divergence and the relational-faction-formation aspects.

**Editorial assessment:** The Greek αἱρετικός in 1st-c. usage is closer to **schism-causing** ("forming-a-faction") than to the modern technical-theological **heretic** ("holding-condemned-doctrine"). The Eremos rendering aligns with mainstream English:
- **BSB / ESV / NIV / CSB / NASB**: "divisive person" / "factious person" (relational-frame)
- **KJV / NKJV**: "heretick" / "divisive man" (NKJV softens; KJV uses the technical-theological term)
- **NLT**: "divisive person"

**The REVIEW question:** Is **คนที่ก่อให้เกิดการแตกแยก** the right corpus-default for αἱρετικός / αἵρεσις family? Forward-applicability:
- **1 Cor 11:19 αἱρέσεις** (factions in worship) → similar relational sense
- **Gal 5:20 αἱρέσεις** (vice-list) → similar
- **2 Pet 2:1 αἱρέσεις ἀπωλείας** ("destructive heresies") → here the doctrinal-content is foregrounded; Thai may need a different rendering
- **Acts 24:14 αἵρεσις** ("the Way" called a sect by accusers) → neutral-sectarian sense

A Pauline-corpus αἵρεσις-family doc (low priority; closed-corpus across the NT) could lock the relational-default + flag 2 Pet 2:1 as the doctrinal-content exception.

**Recommend: REVIEW** — confirm with Ben as the corpus-default for the αἵρεσις-family. No new doc needed unless 2 Pet 2:1 forces re-litigation.

---

## 13. 1:5-9 elder-overseer qualification cluster — **STABLE-but-undocumented; recommend new corpus doc per 1TI §L#5**

The Titus 1:5-9 dense elder-overseer qualification list is the corpus's single longest officer-qualification passage (5 verses; 14 explicit qualities; 6 negatives + 6 positives + 2 functional). Combined with 1 Tim 3:1-13 (overseer + deacon lists) the corpus now has **4 qualification clusters** (1 Tim 3:1-7 overseer + 1 Tim 3:8-13 deacon + 1 Tim 5:9-16 widow + Tit 1:5-9 elder-overseer).

The 1TI end-of-book audit's §L#5 priority flagged this as the gating doc-to-write before Titus ships:

> `docs/translator_decisions/pastoral_offices_episkopos_presbyteros_diakonos_2026-05.md` (1TI §L#5) — Tit 1:5–9 dense overseer-elder qualification cluster makes this gating before Titus ships

**The doc-to-write was deferred.** Titus shipped without it. The translator nonetheless maintained corpus-cohesion across the three lists (corpus-precedent annotations cite 1 Tim 3 verbatim Thai for ἀνέγκλητος, μιᾶς γυναικὸς ἀνήρ, φιλόξενος, σώφρων, πάροινος, πλήκτης, αἰσχροκερδής).

**Editorial assessment:** The de-facto corpus-cohesion held. **The new corpus doc is now low-priority** (no further Pastoral letters; the corpus-set is closed at 4 clusters across 1TI + TIT). Nonetheless, a brief doc would aid:
- **Acts 14:23 + Acts 20:17, 28** — Pauline-elder-establishment narrative (Paul appointing πρεσβυτέρους + addressing them as ἐπισκόποις)
- **1 Pet 5:1-2** — πρεσβύτερος / ἐπισκοποῦντες same-office-equivalence
- **James 3:1, 5:14** — διδάσκαλος + πρεσβύτερος occurrences
- **3 John 1, 9-10** — πρεσβύτερος + Diotrephes ecclesiastical-leadership

**Recommend: STABLE; consider new corpus doc `docs/translator_decisions/pastoral_offices_episkopos_presbyteros_diakonos_2026-05.md`** at low-medium priority. The doc should:
1. Lock πρεσβύτερος → **ผู้ปกครอง** (ecclesiastical-elder office distinct from generic-older-man at 1 Tim 5:1; cf. §7 above)
2. Lock ἐπίσκοπος → **ผู้ปกครองดูแล** (alternate-name-same-office; cf. §7 above)
3. Lock διάκονος (office-sense) → **ผู้ช่วยศาสนกิจ** corpus-precedent 1 Tim 3:8 + 1 Tim 3:12
4. Document the πρεσβύτερος/ἐπίσκοπος equivalence at Tit 1:5 + 1:7 + Acts 20:17 + 28 + 1 Pet 5:1-2
5. Cross-reference §F (`pastoral_corpus_locks_2026-05.md` Phoebe-style διάκονος ambiguity) for the office-vs-general-service distinction

---

## 14. Inherited locks — **all compliant**

| Doc | Titus evidence | Status |
|---|---|---|
| `pastoral_corpus_locks_2026-05.md` §A (πιστὸς ὁ λόγος) | 3:8 — bare-form **ถ้อยคำนี้เชื่อถือได้** (5th + final Pastoral) | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §B (εὐσέβεια family) | 1:1 noun **ความเคร่งในพระเจ้า**; 2:12 adverb **ด้วยความเคร่งในพระเจ้า** | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §C (σωτήρ Pastoral-shift) | 6 occurrences (1:3, 1:4, 2:10, 2:13, 3:4, 3:6); densest σωτήρ-cluster in NT; Father+Christ balanced 3+3 | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §C (Tit 2:13 Granville-Sharp) | 2:13 → **พระเยซูคริสต์ พระเจ้าผู้ยิ่งใหญ่และพระผู้ช่วยให้รอดของเรา** (verbatim §C provisional Thai) | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §D (ἀρσενοκοίτης) | N/A in Titus | **LOCKED (N/A)** |
| `pastoral_corpus_locks_2026-05.md` §E (women-in-worship ambiguity) | 2:3-5 older-women teaching + younger-women household codes (καλοδιδάσκαλος + φίλανδρος + φιλότεκνος + ὑποτασσομένας τοῖς ἰδίοις ἀνδράσιν) — preserved per ambiguity-strategy | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §F (Phoebe-style διάκονος ambiguity) | N/A — no διάκονος (office-sense) in Titus | **LOCKED (N/A)** |
| `pastoral_corpus_locks_2026-05.md` §G (μιᾶς γυναικὸς ἀνήρ formula) | 1:6 → **เป็นสามีของภรรยาเพียงคนเดียว** (verbatim §G lock) | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §H (1 Tim 3:16 Ὃς vs Θεός variant) | N/A — variant is 1TI-specific | **LOCKED (N/A)** |
| `pastoral_corpus_locks_2026-05.md` §I (2 Tim 3:16 πᾶσα γραφή + θεόπνευστος) | N/A — verse is 2TI-specific | **LOCKED (N/A)** |
| `pastoral_corpus_locks_2026-05.md` §J (metaphor-flattening principle) | 4 applications: 1:11 ἐπιστομίζω + 1:13 ἀποτόμως + 1:12 γαστέρες + 2:3 ἱεροπρεπής (densest cluster in corpus); 1 counter-application 3:11 ἐκστρέφομαι (vehicle preserved as determinative) | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` §K (extra-canonical-tradition acknowledgment) | N/A — no extra-canonical-source citations in Titus | **LOCKED (N/A)** |
| `epiphaneia_christou_2026-05.md` | 2:11 verb-form **ทรงปรากฏ**; 2:13 noun **การทรงปรากฏ**; 3:4 verb-form **ทรงปรากฏ** — corpus-doc lock applied across noun + verbal forms | **LOCKED** |
| `hygiaino_sound_doctrine_2026-05.md` | 5 applications across noun + verbal + predicate-adjective + ὑγιής cognate (1:9, 1:13, 2:1, 2:2, 2:8) — **densest single-letter cluster in NT**; corpus-doc lock fully exercised | **LOCKED** |
| `ekklesia_2026-04.md` | N/A — no ἐκκλησία occurrences in Titus | **LOCKED (N/A)** |
| `diakonos_pauline_2026-05.md` | N/A — no διακονία family in Titus | **LOCKED (N/A)** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | Titus has minimal narrator-κύριος (epistolary; not narrative); no occurrences requiring narrator-voice handling | **LOCKED (N/A)** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — epistolary, no narrative-vocatives | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | N/A — no narrative-praise-verb-with-object passages | **LOCKED (N/A)** |
| `honorifics_non_divine_authorities_2026-04.md` | 1:7 ἐπίσκοπος → **ผู้ปกครองดูแล** (plain register); 2:9 δεσπότης → **นาย** (plain register, household-master); 3:1 ἀρχαῖς ἐξουσίαις → **ผู้ปกครองและผู้มีอำนาจ** (plain register, civil-government); 2:3 διαβόλους (adjectival) → **ใส่ร้าย** (plain); 3:3 διάβολος-derivative absent — no anomalies | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout; plain register for Paul-as-author (ข้าพเจ้า), Titus (ท่าน), human-figures (อารเทมัส, ทีคิคัส, เซนัส, อปอลโล); compliant | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | N/A — no Aramaic embeds | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | Audit script PASSES strict mode with **0 candidates**. Titus is unusually clean for a Pastoral. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — epistolary, not narrative | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in Titus | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — neither lemma in Titus (despite the church-discipline context at 3:10-11; the divisive-person framing avoids the μετάνοια vocabulary) | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | N/A — ἄφεσις absent from Titus | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | 1:12 Epimenides citation — pagan-poet but NOT pagan-deity reference (see §9); compliant by absence-of-divinity-references | **LOCKED (N/A on deities)** |
| `roman_administrative_titles_2026-04.md` | 3:1 ἀρχαῖς ἐξουσίαις generic "rulers and authorities" → **ผู้ปกครองและผู้มีอำนาจ** (not specific Roman-administrative titles like ἀνθύπατος/ἡγεμών); compliant | **LOCKED (N/A on specific titles)** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from Titus | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον at 3:5+3:6 → **พระวิญญาณบริสุทธิ์** (RULES §4 standard); no psyche/pneuma-anthropological tensions; compliant | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | N/A — Pastoral, no doxology-amen in Titus closing (Tit 3:15 has bare χάρις-blessing without ἀμήν, distinct from 2 Tim 4:18 + 1 Tim 6:21 closings); compliant | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs in Titus | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | N/A — βασιλεία absent from Titus (notable: only Pastoral letter without βασιλεία-occurrences) | **LOCKED (N/A)** |
| `ouranos_heaven_rendering_2026-04.md` | N/A — οὐρανός / ἐπουράνιος absent from Titus | **LOCKED (N/A)** |
| `parousia_christou_2026-05.md` | N/A — παρουσία noun absent from Titus; companion ἐπιφάνεια (per `epiphaneia_christou_2026-05.md`) covers the Pastoral-eschatological lemma at 2:13 | **LOCKED (N/A)** |
| `christ_hymn_kenosis_2026-05.md` | N/A — μορφή absent from Titus (no Christ-hymn-fragment-of-PHP-2-style construction; the 2:11-14 + 3:4-7 doxologies use different vocabulary) | **LOCKED (N/A)** |
| `dikaioo_dikaiosyne_family_2026-05.md` | 1:8 δίκαιον → **เที่ยงธรรม**; 2:12 δικαίως → **อย่างชอบธรรม**; 3:5 ἔργων ἐν δικαιοσύνῃ → **การกระทำที่ชอบธรรม**; 3:7 δικαιωθέντες → **ได้รับการประกาศว่าชอบธรรม** (divine-passive); corpus-locked compliance | **LOCKED** |
| `nomos_pauline_2026-05.md` | 3:9 μάχας νομικάς → **การโต้เถียงเรื่องธรรมบัญญัติ**; 3:13 νομικός (lawyer) → **นักธรรมบัญญัติ** (default to Mosaic-Law-expert per Greek-NT pattern); compliant | **LOCKED** |
| `sarx_pauline_2026-05.md` | N/A — σάρξ absent from Titus | **LOCKED (N/A)** |
| `phroneo_pauline_2026-05.md` | N/A — φρονέω family absent from Titus | **LOCKED (N/A)** |
| `pistis_christou_2026-05.md` | 1:1 πίστιν ἐκλεκτῶν θεοῦ → **ความเชื่อของผู้ที่พระเจ้าทรงเลือกสรร** (subjective-genitive); other πίστις occurrences (1:4, 1:13, 2:2, 2:10 πᾶσαν πίστιν, 3:15) all standard ความเชื่อ; no Christou-genitive ambiguity in Titus; compliant | **LOCKED** |
| `prototokos_pauline_2026-05.md` | N/A — πρωτότοκος absent from Titus | **LOCKED (N/A)** |
| `huiothesia_adoption_2026-05.md` | N/A — υἱοθεσία absent from Titus (3:7 κληρονόμοι "heirs" is the adjacent-but-distinct concept) | **LOCKED (N/A)** |
| `proper_noun_wordplay_2026-04.md` | N/A — no proper-noun wordplay in Titus | **LOCKED (N/A)** |
| `spiritual_beings_hierarchy_2026-05.md` | διάβολος as proper-noun absent from Titus; 2:3 διαβόλους (adjectival "slanderous") not the spiritual-being sense; compliant | **LOCKED (N/A on hierarchy)** |
| `stoicheia_tou_kosmou_2026-05.md` | N/A — στοιχεῖα absent from Titus | **LOCKED (N/A)** |
| `telos_paidagogos_christ_2026-05.md` | N/A — παιδαγωγός absent from Titus; 2:12 παιδεύω at v.12 ("instruct/train") is the cognate-verb (general formative-discipline; rendered ฝึก) — distinct application | **LOCKED (N/A)** |
| `adversary_speech_register_2026-05.md` | N/A — no adversary-direct-speech in Titus (the 1:12 Epimenides quote is pagan-poet quotation, not adversary-discourse — see §9) | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | Audit clean | **LOCKED** |
| `porneia_vs_moicheia_DEFERRED_2026-05.md` | N/A — neither lemma in Titus | **LOCKED (DEFERRED, N/A)** |
| Pauline locks confirmed in Titus from prior books | δόξα at 2:13 → **พระสิริ** (doxological); χάρις at 1:4 + 2:11 + 3:7 + 3:15 → **พระคุณ** (corpus-locked); εἰρήνη at 1:4 → **สันติสุข** (corpus-locked); ἔλεος at 3:5 → **พระเมตตา** (corpus-locked); σῴζω at 3:5 → **ทรงช่วย ... ให้รอด** (corpus-locked); ἁμαρτία/ἁμαρτάνω at 3:11 → **ทำบาป**; ἀνομία at 2:14 → **ความอธรรม**; ζωὴ αἰώνιος bookend at 1:2 + 3:7 → **ชีวิตนิรันดร์** (corpus-locked); μῦθος at 1:14 → **เรื่องเล่าที่ไม่จริง** (corpus-locked from 1 Tim 1:4, 4:7, 2 Tim 4:4); διάβολος adjectival at 2:3 → **ใส่ร้าย** (corpus-precedent 1 Tim 3:11); παρακαλέω at 1:9 + 2:6 + 2:15 → **หนุนใจ** (corpus-locked Pauline-Pastoral); ἐλέγχω at 1:9 + 1:13 + 2:15 → **ตักเตือน** (corpus-locked); λυτρόω at 2:14 → **ทรงไถ่** (corpus-locked); καλῶν ἔργων Pastoral-formula at 2:7, 2:14, 3:1, 3:8, 3:14 (5× — densest in NT) → **(การ)ทำดี / สิ่งดี / การกระทำดี** (contextually varied but Pastoral-formulaic); compliant | **LOCKED** ✓ |

---

## Mechanical (§1) — **all green**

- 3/3 chapters: `output/check_reports/titus_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 3/3 chapters: `output/back_translations/titus_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-132-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `python3 scripts/audit_inclusion_variants.py --book titus --strict`: **PASS (0 candidates)** — Titus is unusually clean for a Pastoral
- `python3 scripts/export_to_usfm.py --book TIT`: **PASS** — `output/paratext/TIT.SFM` regenerated cleanly (untracked; pre-existing paratext convention)
- `git status output/`: 1 modified `key_term_consistency_all.md` (regenerated by gate script with new TIT entry); plus pre-existing untracked paratext files (1CO/1TH/2CO/2TH/ACT/COL/EPH/GAL SFM stragglers from prior book-ships) — none affects translation content

---

## Pre-existing docs affirmed / unchanged

All 42 docs in `docs/translator_decisions/` reviewed. Compliance summary in §14 above.

**No doc-amendments warranted.** The two new 2026-05-03 corpus docs (`epiphaneia_christou_2026-05.md`; `hygiaino_sound_doctrine_2026-05.md`) — written during 2TI end-of-book audit response specifically to gate Titus — both held cleanly across all Titus occurrences. The 1TI §M `kyrios_narrator_voice_luke_acts_2026-04.md` framing-extension recommendation (now confirmed across **9 corpus-streams**) is unchanged; Titus contributes no narrator-κύριος (epistolary) and so doesn't add a new stream.

---

## Flagged for Ben's attention

### A. πρεσβύτερος vs ἐπίσκοπος Thai distinct-rendering at 1:5 + 1:7 — **REVIEW** (§7)
Greek explicitly equates the two terms; Thai uses two distinct lexical items (**ผู้ปกครอง** vs **ผู้ปกครองดูแล**) sharing a stem. Worth Ben's confirmation as the corpus-default for forward-Pastoral application (Acts 20:17+28; 1 Pet 5:1-2). Recommend brief thai_summary expansion at 1:7 or new corpus doc (§13) to surface the Greek equivalence.

### B. 3:5 λουτροῦ παλιγγενεσίας single-vs-dual washing-event reading — **REVIEW** (§11)
Two sub-questions:
1. Is the slight (b)-leaning **และ** + **โดย** construction (two events, Spirit as agent) the right corpus-default, or should the Thai preserve more (a)-style ambiguity?
2. Should the thai_summary's baptismal-symbol commitment soften to neutral interpretation-presentation?

### C. 3:10 αἱρετικός relational-divisive vs doctrinal-heretic rendering — **REVIEW** (§12)
**คนที่ก่อให้เกิดการแตกแยก** chosen as corpus-default; aligns with mainstream English (BSB/ESV/NIV/CSB). Worth Ben's confirmation as the αἵρεσις-family corpus-default (1 Cor 11:19; Gal 5:20; 2 Pet 2:1; Acts 24:14 forward).

### D. New corpus doc to write
1. **`docs/translator_decisions/pastoral_offices_episkopos_presbyteros_diakonos_2026-05.md`** (1TI §L#5; reaffirmed §13 above) — the deferred doc covering πρεσβύτερος = ἐπίσκοπος equivalence (TIT 1:5+1:7; Acts 20:17+28; 1 Pet 5:1-2) + διάκονος office-vs-general-service distinction (1 Tim 3:8-13; Phil 1:1; Rom 16:1). **Low-medium priority** — Pastoral-corpus is closed at 4 qualification clusters (1 Tim 3 overseer + deacon + 1 Tim 5 widow + Tit 1 elder-overseer); doc would primarily serve forward-Acts + General Epistles application. Not gating the v1 tag.

### E. Existing docs to amend
**None.** All inherited locks compliant; no amendments warranted by Titus-specific evidence.

### F. External AI review (§3 of checklist) — **pending**
Recommended before `book-titus-v1` tag. Suggested 4-cluster external AI packet (smaller than 1TI's 8-item; comparable to 2TI's 6-item — Titus has fewer load-bearing decisions because the corpus discipline was front-loaded in 1TI + 2TI):

1. **Tit 1:5-9** — πρεσβύτερος / ἐπίσκοπος equivalence + elder-overseer qualification cluster (densest in NT) + corresponding §7 + §13 questions
2. **Tit 1:11-13 + 2:3** — §J metaphor-flattening application cluster (4 verses, 4 distinct vehicles) + the 1:12 Epimenides citation handling
3. **Tit 2:11-14 + 3:4-7** — twin doxological-hymn-fragments + Granville-Sharp Christology at 2:13 + λουτροῦ παλιγγενεσίας single-vs-dual construction at 3:5
4. **Tit 2:14 περιούσιος + 3:10 αἱρετικός** — LXX-echo handling + corpus-distinctive HAPAX renderings

Use Grok + ChatGPT + Gemini (free-tier) per the JHN / GAL / 1TH / 1CO / 2CO / 1TI / 2TI pattern.

---

## Recommendation

**Titus ships in strong corpus-hygiene shape** — the strongest of any Pastoral letter so far. With the corpus discipline front-loaded into `pastoral_corpus_locks_2026-05.md` (§A–§K) and the two new 2026-05-03 corpus docs (epiphaneia + hygiaino) written specifically to gate Titus, **all corpus-level decisions held cleanly through translation-time**. The translator made consistent, principled choices on the Titus-specific clusters (1:5-9 elder-overseer cluster; 2:11-14 + 3:4-7 doxological-hymn-pair; 1:11-13 metaphor-flattening cluster; 1:12 Epimenides citation; 2:13 Granville-Sharp; 2:14 LXX-echo περιούσιος; 3:5 baptismal-regeneration crux; 3:10 relational-αἱρετικός).

**No DECIDE items.** All three REVIEW items (§A πρεσβύτερος/ἐπίσκοπος; §B 3:5 baptismal construction; §C 3:10 αἱρετικός) are **defensible-as-shipped, just worth Ben's explicit confirmation**. The 2:13 Granville-Sharp pre-decision (§C of pastoral_corpus_locks) and the 3:16 θεόπνευστος DECIDE-from-2TI (now §I of pastoral_corpus_locks) are **already ratified and N/A** in Titus — meaning Titus presents no v1-tag-blocking decisions.

**Tag `book-titus-v1` after:**
1. Ben's confirmation on **§A + §B + §C** (REVIEW items)
2. (Optional, low-priority) Decision on whether to write **§D** new corpus doc (`pastoral_offices_*`); not gating
3. External AI sanity-check (§F)

**The Pastoral pipeline is now editorially complete.** All three Pastoral letters (1TI + 2TI + TIT) have been audited end-of-book; all five Pastoral-distinctive corpus clusters from `pastoral_corpus_locks_2026-05.md` have been stress-tested + confirmed compliant; the two derivative corpus docs (epiphaneia + hygiaino) have been fully exercised. Forward-application to non-Pastoral letters (the deferred §D `pastoral_offices_*` doc; the §9 `pagan_poet_citations_2026-XX.md` candidate; the §K Jude pre-commits) is unblocked.
