# Hebrews — End-of-Book Review

**Date:** 2026-05-04
**Scope:** All 13 chapters (303 verses; ~580 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (~52 docs).
**Trigger:** HEB 13 shipped (commit `9ec9a94`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 13/13 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-261-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks; `audit_inclusion_variants.py --book hebrews --strict` exits 0 (zero candidates); `export_to_usfm.py --book HEB` regenerates `output/paratext/HEB.SFM` cleanly. `git status output/` — no HEB-source dirt.
- **Hebrews is the FIRST FULL homiletic-priestly NT book the project has shipped.** It is also the densest OT-LXX-citation text in the NT (~37 direct citations + ~15 allusions), and introduces the largest single-book vocabulary cluster yet locked in a single ship: the **priesthood + sacrifice + tabernacle + perfection + covenant** vocabulary that no prior corpus doc covers. The technical vocabulary established here will need to interact with Pauline (Rom 3:25 ἱλαστήριον; 1 Cor 11:25 διαθήκη; Eph 5:2 προσφορά + θυσία) and Petrine (1 Pet 1:2, 19; 2:5 sacrificial-blood + spiritual-sacrifices) language already in flight.
- **18 inherited locks verified compliant** in HEB (ekklesia, ouranos, basileia, divine-praise, honorifics, narrator-voice, aphesis, kyrios, prototokos, parepidemos, pascho, stoicheia, diakonos/leitourg-, μετάνοια, narrator-vs-character voice, OT-citation flagging, inclusion-variants N/A, arnion N/A — see §17).
- **11 cross-cutting Hebrews patterns are STABLE-but-undocumented at corpus level** — every one of them HEB-distinctive and forward-pertinent: κρείττων (the book's thesis-word ~13×); the priesthood vocabulary (ἀρχιερεύς + ἱερεύς + Μελχισέδεκ + τάξις); διαθήκη (καινή vs παλαιά covenant); αἷμα + αἱματεκχυσία (sacrificial blood); θυσία + προσφορά (sacrifice/offering doublet); σκηνή + καταπέτασμα + ἅγια + ἱλαστήριον (tabernacle vocabulary); τέλειος / τελειόω / τελείωσις (perfection cluster); προσέρχομαι (cultic drawing-near); καταπαύσις + σαββατισμός (rest); ὑπόστασις (three-way contextual split); ἀρχηγός (Christ-as-pioneer). All eleven are high-density first-occurrences in the corpus and lift cleanly to `docs/translator_decisions/`.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: HEB 4:12 ψυχή/πνεῦμα rendering — the one substantive psyche-vs-pneuma drift candidate; HEB 12:3 ταῖς ψυχαῖς paraphrase to ท้อใจ; ἱλαστήριον dual-sense at HEB 9:5 vs forward Rom 3:25).
- **4 items flagged DECIDE** (HEB 6:4-6 — apostasy-passage interpretive stance; HEB 1:8 ὁ θεός vocative addressed to Christ — the Christological-divinity anchor and the JW-counter-reading; HEB 10:5 LXX σῶμα vs MT אזנים — translator-follows-LXX departure from the Hebrew; the ἁγιασμός / ἁγιωσύνη amendment to the 1 Thessalonians 5:23 corpus doc).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. κρείττων — the book's thesis-word — **STABLE (undocumented; recommend new doc — high HEB-internal priority)**

**κρείττων ("better, superior")** is THE thesis-word of Hebrews — 13 occurrences, by far the densest in the NT (next-densest: 1 Cor 7 with 3). It frames the entire structural argument: Christ > angels > Moses > Aaron > Levitical priesthood > old-covenant sacrifices > earthly tabernacle.

| Verse | Greek | Thai | Comparative subject |
|---|---|---|---|
| 1:4 | τοσούτῳ κρείττων γενόμενος τῶν ἀγγέλων | **เป็นใหญ่กว่าทูตสวรรค์ทั้งหลาย** | Christ > angels (opening thesis) |
| 6:9 | πεπείσμεθα δὲ περὶ ὑμῶν τὰ κρείσσονα | **ดียิ่งกว่า** | "better things" of salvation |
| 7:7 | τὸ ἔλαττον ὑπὸ τοῦ κρείττονος εὐλογεῖται | **ผู้น้อยรับพรจากผู้ที่ยิ่งใหญ่กว่า** | Melchizedek > Abraham (blesser > blessed) |
| 7:19 | ἐπεισαγωγὴ δὲ κρείττονος ἐλπίδος | **ความหวังที่ดียิ่งกว่า** | new hope > Mosaic law |
| 7:22 | κρείττονος διαθήκης ἔγγυος | **พันธสัญญาที่ดียิ่งกว่า** | new covenant > old |
| 8:6 | κρείττονός ἐστιν διαθήκης μεσίτης ... κρείττοσιν ἐπαγγελίαις | **พันธสัญญาที่ดียิ่งกว่า ... พระสัญญาที่ดียิ่งกว่า** | better ministry, better covenant, better promises |
| 9:23 | κρείττοσιν θυσίαις παρὰ ταύτας | **เครื่องบูชาที่ดียิ่งกว่าเหล่านี้** | heavenly sacrifices > earthly |
| 10:34 | κρείσσονα ὕπαρξιν καὶ μένουσαν | **ทรัพย์สมบัติที่ดียิ่งกว่าและถาวร** | heavenly possession > earthly |
| 11:4 | πλείονα θυσίαν Ἅβελ παρὰ Κάϊν | (πλείονα, but cognate-thesis) — Abel's offering > Cain's |
| 11:16 | κρείττονος ὀρέγονται, τοῦτ' ἔστιν ἐπουρανίου | **ที่ดียิ่งกว่า คือดินแดนสวรรค์** | heavenly country > earthly |
| 11:35 | ἵνα κρείττονος ἀναστάσεως τύχωσιν | **การคืนชีพที่ดียิ่งกว่า** | better resurrection > release |
| 11:40 | τοῦ θεοῦ περὶ ἡμῶν κρεῖττόν τι προβλεψαμένου | **ดียิ่งกว่า** | God's better plan for us |
| 12:24 | αἵματι ῥαντισμοῦ κρεῖττον λαλοῦντι παρὰ τὸν Ἅβελ | **โลหิตประพรมที่กล่าวถึงดียิ่งกว่าโลหิตของอาเบล** | Christ's blood > Abel's |

**Editorial assessment:** Two principled Thai renderings used in clean distribution: **เป็นใหญ่กว่า** (1:4 — thesis-statement; superiority-of-position) and **ดียิ่งกว่า** (everywhere else — quality-superiority). The distribution is principled: 1:4 is the Christ-vs-angels superiority-of-rank claim that opens the book, where เป็นใหญ่ ("greater, more exalted") foregrounds the rank-superiority; the other 12 occurrences are quality-comparative (better hope, better covenant, better promises, etc.) where ดียิ่งกว่า ("better than") is the natural Thai. The 1:4 KD names this:

> κρείττων ('better / superior') → เป็นใหญ่กว่า / ดียิ่งกว่า. Hebrews-keyword recurring ~13× throughout-book ... LOCK: เป็นใหญ่กว่า in-comparative-superiority context (Christ-better-than-X). The book's-thesis-word.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/kreitton_hebrews_thesis_2026-05.md` — locks the dual rendering (เป็นใหญ่กว่า for rank-superiority, ดียิ่งกว่า for quality-comparative) and documents the structural-argument scaffold (Christ > angels > Moses > Aaron > Levitical-priesthood > old-covenant-sacrifices > earthly-tabernacle). This will preserve the rhetorical density of the comparative argument should any future revision touch a κρείττων-verse.

---

## 2. The priesthood vocabulary — ἀρχιερεύς + ἱερεύς + Μελχισέδεκ + τάξις — **STABLE (undocumented; recommend new doc — highest HEB-corpus priority)**

The single most distinctive vocabulary cluster in Hebrews. **ἀρχιερεύς ("high priest") occurs 17×** (HEB 2:17, 3:1, 4:14, 4:15, 5:1, 5:5, 5:10, 6:20, 7:26, 7:27, 7:28, 8:1, 8:3, 9:7, 9:11, 9:25, 10:11, 10:21, 13:11) — far denser than any other NT book. **ἱερεύς ("priest")** distinct: 6× (5:6 in PSA 110:4 citation; 7:1, 7:3, 7:11 of Melchizedek-and-Levi class; 7:14, 7:21, 7:23, 8:4, 9:6, 10:11, 10:21).

**Renderings (uniform):**

| Greek | Thai | Verses (representative) |
|---|---|---|
| ἀρχιερεύς (Christ, divine subject) | **มหาปุโรหิต** | 2:17, 3:1, 4:14, 5:5, 5:10, 6:20, 7:26, 7:28, 8:1, 9:11, 10:21 |
| ἀρχιερεύς (Levitical, narrative-comparative) | **มหาปุโรหิต** (same form, plain register supplied by context) | 5:1, 7:27, 9:7, 9:25, 10:11, 13:11 |
| ἱερεύς (Christ in PSA 110:4 citation) | **ปุโรหิต** | 5:6, 7:17, 7:21 |
| ἱερεύς (Melchizedek, Levitical) | **ปุโรหิต** | 7:1, 7:3, 7:11, 7:14, 7:23, 8:4, 9:6, 10:11 |
| Μελχισέδεκ | **เมลคีเซเดค** | 5:6, 5:10, 6:20, 7:1, 7:10, 7:11, 7:15, 7:17 |
| τάξις (in κατὰ τὴν τάξιν Μελχισέδεκ formula) | **ตามแบบของเมลคีเซเดค** | 5:6, 5:10, 6:20, 7:11, 7:17, 7:21 |

**Editorial assessment:** The lexical split is principled and consistent — **ปุโรหิต** for ἱερεύς (generic-priest, including Christ in the PSA 110:4 quotation context), **มหาปุโรหิต** for ἀρχιερεύς (compounded-prefix preserves the Greek ἀρχ- "chief" + ἱερεύς "priest" structure). Christ in narrator-voice receives `ทรง`-prefix on adjacent action verbs but the noun-form **มหาปุโรหิต** itself is shared between Christ-subject and Levitical-comparison contexts (correct — the noun-form has no register).

The Aramaic/Hebrew transliteration **เมลคีเซเดค** for Μελχισέδεκ uses the standard biblical-Thai consonant rendering (no royal prefix — Melchizedek is a non-divine OT figure; honorifics-non-divine lock applies). **ตามแบบของ** for κατὰ τὴν τάξιν is principled — **แบบ** ("pattern, order, type") preserves the typological-class force without committing to the more administrative Thai **ลำดับ** ("rank, sequence") that would suggest hierarchical-position.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/priesthood_vocabulary_hebrews_2026-05.md` — locks the four-element cluster (ἀρχιερεύς → มหาปุโรหิต; ἱερεύς → ปุโรหิต; Μελχισέδεκ → เมลคีเซเดค; τάξις-in-Melchizedek-formula → ตามแบบของ) and documents the rationale. Forward-pertinent for: 1 Pet 2:5, 9 (royal-priesthood — different sense, ἱεράτευμα); Rev 1:6, 5:10, 20:6 (priests-of-God-and-Christ — corporate-priesthood). The HEB-locked **ปุโรหิต** rendering is reusable; the corpus-doc should clarify that **ἱεράτευμα** ("priestly-body") will be a separate but cognate lock.

---

## 3. διαθήκη — covenant (καινή vs παλαιά) — **STABLE (undocumented; recommend new doc — highest forward-corpus priority)**

**διαθήκη ("covenant") occurs 17×** in HEB — by far the densest in the NT (the next-densest text is the Synoptic Last-Supper cluster: MAT 26:28 / MAR 14:24 / LUK 22:20 / 1 COR 11:25, 4 verses). HEB carries the covenant-renewal theology — it cites JER 31:31-34 in extenso at 8:8-12 (the longest single OT quotation in the NT — see §15) and frames the entire 8:1–10:18 argument around Christ as **κρείττονος διαθήκης μεσίτης** ("mediator of a better covenant").

| Greek | Thai | Verses |
|---|---|---|
| διαθήκη (generic / unmarked) | **พันธสัญญา** | 7:22; 8:6 (×2); 9:4 (×2); 9:15 (×2); 9:16; 9:17; 9:20; 10:29; 12:24; 13:20 |
| διαθήκη παλαιά / πρώτη ("old / first" covenant) | **พันธสัญญาเดิม** (8:13: τὴν πρώτην; 9:1: ἡ πρώτη) | 8:13; 9:1; 9:15; 9:18 |
| διαθήκη καινή ("new" covenant) | **พันธสัญญาใหม่** | 8:8 (in JER 31 citation); 9:15; 12:24 |
| διαθήκη αἰώνιος ("eternal" covenant) | **พันธสัญญานิรันดร์** | 13:20 |

**Editorial assessment:** Single-rendering **พันธสัญญา** for διαθήκη is uniform and consistent with corpus precedent (MAT 26:28; LUK 1:72; ACT 3:25; ROM 9:4; 1 COR 11:25; 2 COR 3:6, 14; GAL 3:15, 17; 4:24; EPH 2:12). The new/old/eternal modifiers are rendered transparently (**ใหม่ / เดิม / นิรันดร์**) without forcing a Thai compound. The 9:16-17 διαθήκη as "last will and testament" (only place in NT where author exploits the Greek polysemy of διαθήκη as both "covenant" and "will/testament") receives the same Thai **พันธสัญญา** with verse-level KDs explaining the polysemy — Thai cannot dual-render here without a footer-note, and the translator chose to preserve **พันธสัญญา** (covenant) as primary, which loses the testamentary-pun but preserves theological-coherence with the surrounding 9:15+ "eternal-inheritance" frame.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/diatheke_hebrews_2026-05.md` before Romans 9:4 (διαθῆκαι plural — Israel's multiple-covenants) and 1 Cor 11:25 (Lord's-Supper covenant-cup — already-rendered consistently in the Synoptics). The doc should:
1. Lock διαθήκη → **พันธสัญญา** corpus-uniform
2. Lock the modifier-pattern: παλαιά/πρώτη → เดิม; καινή → ใหม่; αἰώνιος → นิรันดร์
3. Document the 9:16-17 διαθήκη-as-testament polysemy as a verse-level exception (preserve the covenant-rendering, lose the testament-pun by design — the verse-level KD covers the rationale)
4. Cite HEB 8:6 + 8:8 + 12:24 + 13:20 as the locking precedents
5. Distinguish the related-but-distinct: μεσίτης ("mediator," 8:6, 9:15, 12:24) → **คนกลาง / ผู้กลาง**; ἔγγυος (HAPAX 7:22, "guarantor") → **ผู้ค้ำประกัน**; νόμος → **ธรรมบัญญัติ** (already corpus-locked via Pauline lock)

---

## 4. αἷμα — sacrificial blood (royal vs plain register split) — **STABLE (undocumented; recommend new doc)**

**αἷμα ("blood") occurs 21×** in HEB — densest sacrificial-blood text in the NT. The translator uses a principled REGISTER split:

| Sense | Thai | Verses |
|---|---|---|
| Christ's atoning blood (royal-honorific) | **พระโลหิต** | 9:12, 9:14, 9:25, 10:19, 10:29, 12:24, 13:12, 13:20 |
| Levitical / OT sacrificial blood (plain) | **โลหิต** | 9:7, 9:13, 9:18, 9:19, 9:21, 9:22 (×2), 10:4, 11:28, 12:4 |
| Incarnational sharing (αἵματος καὶ σαρκός — paired with σάρξ) | **เลือดและเนื้อ** (compound idiom; plain) | 2:14 |
| HAPAX αἱματεκχυσία ("blood-shedding") | **การหลั่งโลหิต** | 9:22 |

**Editorial assessment:** The royal-prefix **พระโลหิต** for Christ's atoning blood is principled and uniform — every reference to the **shed blood of Christ** in atoning-sacrificial context receives **พระโลหิต**, while every reference to the **OT-Levitical sacrificial blood** receives the plain **โลหิต**. The HEB 2:14 αἷμα + σάρξ idiom (incarnational-sharing — Christ partook of "blood and flesh" with the children) takes the doublet-form **เลือดและเนื้อ** — note the alternative **เลือด** rather than **โลหิต** here, principled because (a) the idiom is anthropological-incarnational, not sacrificial-cultic, and (b) the doublet **เลือด + เนื้อ** preserves the Greek alliterative-pair force without the cumbersome **โลหิต + เนื้อหนัง**. The HAPAX αἱματεκχυσία at 9:22 (NT-only here, "shedding-of-blood") uses **การหลั่งโลหิต** (verb-noun compound) — principled because the verse is general-axiomatic ("without shedding-of-blood there is no forgiveness"), covering both Levitical and Christological reference.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/aima_blood_register_hebrews_2026-05.md` before 1 Pet 1:2 + 1:19 (Christ's αἷμα — royal expected) and Rev 1:5; 5:9; 7:14; 12:11; 19:13 (Lamb's blood imagery — Apocalyptic-cultic). The doc should:
1. Lock the register split: αἷμα-of-Christ-sacrificial-context → **พระโลหิต**; αἷμα-of-OT-Levitical → **โลหิต**
2. Document the HEB 2:14 incarnational αἵματος καὶ σαρκός → **เลือดและเนื้อ** as the principled exception
3. Lock αἱματεκχυσία → **การหลั่งโลหิต** (HAPAX axiomatic-rendering)
4. Cross-reference the related-but-distinct ῥαντισμός ("sprinkling," 12:24; 1 Pet 1:2) → **การประพรม / โลหิตประพรม** and ἐκχέω (Last-Supper covenant blood "poured out" formula, MAT 26:28 / MAR 14:24 / LUK 22:20) — already corpus-locked

---

## 5. θυσία + προσφορά — sacrifice / offering doublet — **STABLE (undocumented; recommend doc)**

The Hebrews sacrificial-vocabulary doublet pattern. **θυσία ("sacrifice") occurs 15×**; **προσφορά ("offering") occurs 5×**; the pair recurs as a doublet at HEB 5:1, 8:3, 9:9, 10:5, 10:8.

| Greek | Thai | Notes |
|---|---|---|
| θυσία (singular, generic) | **เครื่องบูชา** | 5:1; 7:27 (×2); 8:3; 9:9, 9:23, 9:26; 10:1, 10:5, 10:8, 10:11, 10:12, 10:26; 11:4; 13:15, 13:16 |
| προσφορά | **ของถวาย** (paired-with-θυσία) / **เครื่องสักการบูชา** (Christ's body-offering, 10:10) | 10:5, 10:8 (paired); 10:10, 10:14, 10:18 (Christ's offering, distinct rendering for emphasis) |

**Editorial assessment:** The doublet θυσία + προσφορά is preserved in the Thai paired form **เครื่องบูชาและของถวาย** at 5:1, 8:3, 10:5, 10:8 — matching the LXX-formulaic translation tradition (LXX uses both terms in the PSA 40:6 quotation cited at 10:5). The standalone θυσία uniformly renders as **เครื่องบูชา**. The standalone προσφορά at 10:10 (the singular-historical Christ-body-offering) and 10:14 + 10:18 receives **เครื่องสักการบูชา** — a more elevated cult-term that distinguishes Christ's once-for-all offering from the daily-Levitical θυσία. The 13:15 θυσίαν αἰνέσεως ("sacrifice of praise") uses **เครื่องบูชาแห่งคำสรรเสริญ** — the αἰνέσεως → **คำสรรเสริญ** rendering is compliant with `divine_object_praise_verbs_2026-04.md` (see §17).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/thysia_prosphora_hebrews_2026-05.md`. Document the doublet rendering convention + the principled προσφορά-elevation to **เครื่องสักการบูชา** in the Christ-singular-offering context. Forward-pertinent for: Eph 5:2 (θυσίαν ... προσφοράν — already in flight); Rom 12:1 (παραστῆσαι τὰ σώματα ὑμῶν θυσίαν ζῶσαν — living-sacrifice imagery); 1 Pet 2:5 (πνευματικὰς θυσίας — spiritual-sacrifices).

---

## 6. The tabernacle vocabulary — σκηνή + καταπέτασμα + ἅγια + ἱλαστήριον — **STABLE (undocumented; recommend new doc)**

The HEB 8–10 tabernacle-typology cluster — the architecture-and-furniture vocabulary that frames the Day-of-Atonement-Christology argument. All HEB-distinctive in the NT.

| Greek | Thai | Verses |
|---|---|---|
| σκηνή (tabernacle/tent) | **พลับพลา** | 8:2, 8:5, 9:1, 9:2 (×2), 9:3, 9:6, 9:8, 9:11, 9:21, 10:1, 13:10 |
| καταπέτασμα (veil/curtain) | **ม่าน** (with v.6:19 elaborated **ม่านที่แยกคั่น** "veil-that-separates") | 6:19, 9:3, 10:20 |
| ἅγια / ἅγια ἁγίων (holy place / holy of holies) | **วิสุทธิสถาน** (singular for both inner and outer; 9:3 "holy of holies" → **วิสุทธิสถานชั้นสุดท้าย** / **อันสูงสุด** depending on context) | 8:2, 9:1, 9:2, 9:3, 9:8, 9:12, 9:24, 9:25, 10:19, 13:11 |
| ἱλαστήριον (mercy seat) | **พระที่นั่งกรุณา** | 9:5 |
| Χερουβίν (HAPAX) | **เครูบ** | 9:5 |
| σκεύη (vessels/articles) | **ภาชนะ** | 9:21 |

**Editorial assessment:** The vocabulary is uniform and reads naturally for a Thai-Buddhist-cultural context that has no native sanctuary-cultus vocabulary — the translator built consistently from biblical-Thai precedent. **พลับพลา** for σκηνή matches THSV1971 + ERV-Thai biblical-Thai standard (literally "ceremonial-pavilion / royal-tent"; appropriate for tabernacle). **วิสุทธิสถาน** for ἅγια is a Thai compound ("holy-place") that handles both the singular-furniture-area sense (the "Holy Place" outer-room) and the **ἅγια ἁγίων** ("Holy of Holies" inner-room) sense via context-modifiers. **ม่าน** for καταπέτασμα is plain ("curtain"); the 6:19 elaborated form **ม่านที่แยกคั่น** ("veil that separates") preserves the architectural-significance.

The **ἱλαστήριον at 9:5 → พระที่นั่งกรุณา** is the standard biblical-Thai for the OT mercy-seat (the ark cover; LXX-translation of כפרת kaporeth). This is **distinct from** the Pauline cultic-instrumental ἱλαστήριον at Rom 3:25 (Christ-as-propitiation, which most Thai translations render with the verb-phrase **เป็นเครื่องบูชาไถ่บาป** — see REVIEW item §16 below). The 9:5 KD explicitly notes this distinction:

> ἱλαστήριον in tabernacle-physical-context = the gold cover of the ark (mercy seat) → พระที่นั่งกรุณา (Thai biblical standard for the cover of the ark; distinct from ROM 3:25 propitiation-sense which uses 'เครื่องบูชาไถ่บาป').

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/tabernacle_vocabulary_hebrews_2026-05.md`. The doc should:
1. Lock σκηνή → **พลับพลา**
2. Lock καταπέτασμα → **ม่าน** (with optional **ม่านที่แยกคั่น** elaboration where architecturally-foregrounded)
3. Lock ἅγια → **วิสุทธิสถาน** (with **ชั้นสุดท้าย / อันสูงสุด** elaboration for inner-room contexts)
4. Lock ἱλαστήριον (tabernacle-furniture-context) → **พระที่นั่งกรุณา** AND flag the dual-sense distinction from the forthcoming Pauline propitiation-context (Rom 3:25) — the Thai will need a separate rendering there
5. Lock Χερουβίν → **เครูบ** (Hebrew-loanword transliteration; modern simpler form, not เครูบิม)

---

## 7. τέλειος / τελειόω / τελείωσις — perfection cluster — **STABLE (undocumented; recommend new doc)**

The Hebrews "perfection" vocabulary — central to the priestly-Christology argument (Christ "perfected through suffering," 2:10; "perfected forever" as eternal high priest, 7:28; "perfects forever those who are sanctified," 10:14). 14+ occurrences.

| Greek | Thai | Verses |
|---|---|---|
| τελειόω (verb — perfect, complete, qualify) | **ทำให้สมบูรณ์** (transitive God-subject) / **บรรลุความสมบูรณ์** (intransitive subject-perfected) | 2:10, 5:9, 7:19, 7:28, 9:9, 10:1, 10:14, 11:40, 12:23 |
| τέλειος (adj. — mature, perfect) | **ผู้ใหญ่** (mature-believer sense, 5:14) | 5:14; (9:11 use distinct — see below) |
| τελειότης (noun — maturity, completion) | **ความสมบูรณ์** (substantive form) | 6:1 |
| τελείωσις (noun — perfection, completion-state) | **ความสมบูรณ์** | 7:11 |
| τελειωτής (HAPAX 12:2) | **ผู้บรรลุความสมบูรณ์** (paired with ἀρχηγός at 12:2 — see §13) | 12:2 |

**Editorial assessment:** Single-rendering family **สมบูรณ์** (root) for the entire τελει-cluster is principled. The verb form takes either active **ทำให้สมบูรณ์** (when God/Christ is the subject perfecting) or middle/passive **บรรลุความสมบูรณ์** (when Christ or believers are the ones perfected). The 5:14 contextual-shift to **ผู้ใหญ่** ("mature ones") is principled — there τέλειος is the maturity-vs-infancy contrast (5:13–14 milk vs solid food), not the priestly-perfection sense; **ผู้ใหญ่** ("adults / mature ones") is the natural Thai. The 6:1 τελειότης ("maturity") returns to the abstract **ความสมบูรณ์** noun form, principled.

**Critical theological note:** "Perfection" in HEB is **vocational-completion** (Christ qualified-to-be-eternal-high-priest by completing the sufferings; believers brought-to-the-goal of being-with-Christ-forever), NOT moral-perfection. The Thai **สมบูรณ์** ("complete, full, total, perfect") preserves this — it is not the moral-character word **บริสุทธิ์** ("holy, pure"). The translator carefully maintains the lexical separation between **สมบูรณ์** (perfection-as-completion) and **บริสุทธิ์** (sanctification-as-purification — see §8 below) — which collapses in English "perfection" but in Greek and now Thai stays principled.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/teleios_teleioo_hebrews_2026-05.md`. Forward-pertinent for: Phil 3:12, 15 (τέλειος — Pauline-eschatological); 1 Cor 2:6 (τέλειοι — mature-Christians); James 1:4 (τέλειοι καὶ ὁλόκληροι — moral-completion sense); 1 John 4:18 (ἡ τελεία ἀγάπη — perfect-love). Each context will require principled handling that the HEB doc anchors.

---

## 8. καθαρισμός / καθαρίζω + ἁγιάζω — purification + sanctification — **STABLE (anchors HEB 12:14 amendment to 1Th 5:23 doc)**

The Hebrews dual-axis purification-and-sanctification vocabulary — connects to the existing 1 Thessalonians sanctification cluster (recommended doc: `hagiasmos_hagiosune_2026-04.md`, per `1TH_END_OF_BOOK_REVIEW_2026-04-30.md` §2; not yet written as of 2026-05-04).

| Greek | Thai | Verses |
|---|---|---|
| καθαρισμός / καθαρίζω (purify, cleanse — physical-cultic + conscience-internal) | **ชำระ / ชำระให้บริสุทธิ์** | 1:3, 9:13, 9:14, 9:22, 9:23, 10:2 |
| ἁγιάζω (sanctify, make-holy) | **ทรงชำระ ... ให้บริสุทธิ์** (Christ-subject; royal); plain **ชำระให้บริสุทธิ์** elsewhere | 2:11, 9:13, 10:10, 10:14, 10:29, 13:12 |
| ἁγιωσύνη / ἁγιότης (holiness — abstract noun) | **ความบริสุทธิ์** | 12:10 (ἁγιότης) |
| ἁγιασμός (sanctification — process noun, only 12:14) | **ความบริสุทธิ์** | 12:14 |
| καθαρότης (HAPAX, 9:13) | **บริสุทธิ์ในเนื้อหนัง** (adjectival) | 9:13 |

**Editorial assessment — coordinate with 1Th 5:23 sanctification doc:** The 1 Thess audit (§2) recommended a future corpus doc `hagiasmos_hagiosune_2026-04.md` to lock:
- ἁγιασμός (process) → **การชำระให้บริสุทธิ์**
- ἁγιωσύνη (state) → **ความบริสุทธิ์**

HEB 12:14 ἁγιασμόν → **ความบริสุทธิ์** is **NOT compliant** with the 1 Thess proposed lock (which assigned ἁγιασμός → การชำระให้บริสุทธิ์ for the process-noun, distinguished from ἁγιωσύνη → ความบริสุทธิ์ for the state-noun). HEB 12:14 collapses the two into the state-noun rendering. The 12:14 KD does not explain the choice:

> ἁγιασμός → ความบริสุทธิ์ (cognate ἁγιάζω; here noun-form for sanctification-as-state).

**This is a DECIDE item** (see §F below) — Ben needs to choose:
- Option A — Keep HEB 12:14 ἁγιασμός as **ความบริสุทธิ์** (current); amend the proposed 1Th doc to allow **ความบริสุทธิ์** for both ἁγιασμός and ἁγιωσύνη (collapse the process-vs-state distinction in Thai). Argued-for: Thai readers do not distinguish; the Greek aspectual-difference is too subtle to enforce in Thai
- Option B — Revise HEB 12:14 to **การชำระให้บริสุทธิ์** to maintain consistency with the 1Th proposed lock. Argued-for: the Greek aspectual-difference is theologically meaningful (process vs state), and a CC0 Thai NT can preserve it cleanly

The forthcoming `hagiasmos_hagiosune` corpus doc (when written) needs to take this stance explicitly with HEB 12:14 as a test-case.

**Recommend: DECIDE (§F) before tagging.** No new HEB-specific doc needed — this gets resolved within the 1 Thess-anchored sanctification doc.

---

## 9. προσέρχομαι — cultic drawing-near — **STABLE (undocumented; recommend brief doc)**

**προσέρχομαι ("draw near, approach") occurs 7×** in HEB — used in two distinct senses both well-attested in the LXX cultic vocabulary: (a) cultic-priestly approach to God (4:16, 7:25, 10:1, 10:22, 11:6); (b) eschatological approach (12:18, 12:22 — the contrasting Sinai-vs-Zion approach). All seven render as **เข้ามา** ("draw-in, come-in").

| Verse | Greek | Thai |
|---|---|---|
| 4:16 | προσερχώμεθα οὖν μετὰ παρρησίας τῷ θρόνῳ τῆς χάριτος | **ขอให้เราเข้ามาด้วยความกล้าหาญสู่บัลลังก์แห่งพระคุณ** |
| 7:25 | διὰ τοῦτο σώζειν εἰς τὸ παντελὲς δύναται τοὺς προσερχομένους | **บรรดาผู้ที่เข้ามา** |
| 10:1 | οὐδέποτε δύναται τοὺς προσερχομένους τελειῶσαι | **ผู้ที่เข้ามา** |
| 10:22 | προσερχώμεθα μετὰ ἀληθινῆς καρδίας | **ขอให้เราเข้ามาด้วยใจจริง** |
| 11:6 | πιστεῦσαι γὰρ δεῖ τὸν προσερχόμενον τῷ θεῷ | **ผู้ที่เข้ามาเฝ้าพระเจ้า** |
| 12:18 | οὐ γὰρ προσεληλύθατε [ψηλαφωμένῳ] ὄρει | **ท่านไม่ได้เข้ามาถึงภูเขาที่จับต้องได้** |
| 12:22 | ἀλλὰ προσεληλύθατε Σιὼν ὄρει | **แต่ท่านเข้ามาถึงภูเขาศิโยน** |

**Editorial assessment:** Single-rendering **เข้ามา** preserves the verb's metaphor uniformly, and naturally tracks the Hebrews-rhetorical contrast between the OT cultic-approach-to-the-throne-of-grace (4:16, 7:25, 10:1, 10:22, 11:6 — cultic, with implied-divine-object) and the eschatological-corporate-approach to the new-Sinai-Zion (12:18 negative, 12:22 positive). Worth noting: 11:6 + 4:16 use elaborated forms (**เข้ามาเฝ้า** "draw-in-to-attend," **เข้ามา ... สู่บัลลังก์** "draw-in ... to the throne") to make the divine-object explicit.

**Recommend: STABLE; consider brief doc** `docs/translator_decisions/proserchomai_cultic_2026-05.md` to lock the rendering before similar Pauline usage (Eph 2:18 προσαγωγή — different lemma but similar approach-vocabulary; 1 Pet 2:4 πρὸς ὃν προσερχόμενοι — the same lemma, parallel cultic-stone-temple imagery). Could also be folded into a broader "Hebrews tabernacle-cultus vocabulary" doc combining with §6.

---

## 10. καταπαύσις + σαββατισμός — rest cluster — **STABLE (undocumented; recommend brief doc)**

The HEB 3:7–4:13 chapter-long meditation on "rest" — the Sabbath-promised-land typology applied to the eschatological-rest-remaining-for-the-people-of-God.

| Greek | Thai | Verses |
|---|---|---|
| κατάπαυσις (LXX-Sabbath-promised-land "rest" noun) | **การพักสงบ** | 3:11 (PSA 95 citation), 3:18, 4:1, 4:3 (×2), 4:5, 4:10, 4:11 |
| καταπαύω (verb form) | **ทรงพัก / พัก** | 4:4, 4:8, 4:10 |
| σαββατισμός (HAPAX 4:9 — author-coined) | **การพักสงบสะบาโต** | 4:9 |

**Editorial assessment:** The author of HEB invents the noun **σαββατισμός** at 4:9 (NT hapax; possibly first attestation in any Greek text — the verb σαββατίζω exists in the LXX, the noun does not). The Thai **การพักสงบสะบาโต** ("the rest-and-quietness of Sabbath") preserves the author's coinage by adding the **สะบาโต** ("Sabbath") modifier to the standard κατάπαυσις rendering **การพักสงบ**. This is a well-engineered solution — Thai readers see the lexical-distinction between the generic **การพักสงบ** of vv.1–11 and the specific eschatological **การพักสงบสะบาโต** of v.9.

**Recommend: STABLE; consider brief doc** `docs/translator_decisions/katapausis_sabbatismos_2026-05.md` — locks the renderings + documents the σαββατισμός coinage. Forward-pertinent only for occasional κατάπαυσις-uses (REV 14:13 "rest from their labors" — different lemma ἀνάπαυσις); largely a HEB-internal lock. Could be folded into a broader "Hebrews-pastoral vocabulary" doc.

---

## 11. ὑπόστασις — three-way contextual rendering — **STABLE (undocumented; recommend brief doc)**

**ὑπόστασις occurs 3× in HEB** — each at a different theological pivot, with three distinct Thai renderings tracking the contextual semantic-shift:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:3 | χαρακτὴρ τῆς ὑποστάσεως αὐτοῦ | **ภาพแน่ชัดแห่งพระลักษณะของพระองค์** | "essential-being / nature" — the Father's essential-being; Christ as exact-impression of the Father's hypostasis. Theological anchor for later Nicene homoousios |
| 3:14 | τὴν ἀρχὴν τῆς ὑποστάσεως μέχρι τέλους βεβαίαν κατάσχωμεν | **ความมั่นใจในเบื้องต้นไว้ให้มั่นคงจนถึงที่สุด** | "firmness-of-confession / confidence" — believers' firmness-of-faith from the beginning to the end |
| 11:1 | Ἔστιν δὲ πίστις ἐλπιζομένων ὑπόστασις | **ความมั่นใจ (ในสิ่งที่เราหวัง)** | "substance / assurance" — faith as the ὑπόστασις of things-hoped-for |

**Editorial assessment:** The three-way contextual rendering is principled. The LSJ + BDAG entry for ὑπόστασις gives all three senses — (a) underlying essential-being (Stoic/Peripatetic philosophical-technical, anchored in 1:3); (b) firm-resolution / confidence (Polybius use, anchored in 3:14); (c) substance / reality / actual-existence (commercial-papyri use, anchored in 11:1). The translator distributes them principally:
- 1:3 = essential-being → **พระลักษณะ** ("nature, essential-character," with royal pระ-prefix because the referent is the Father's-being)
- 3:14 = firm-confidence → **ความมั่นใจ** (with elaboration **ในเบื้องต้น ... ให้มั่นคง** to capture the perseverance-context)
- 11:1 = substantiating-assurance → **ความมั่นใจ** (paired in chiastic-doublet with **ข้อพิสูจน์** for ἔλεγχος)

**Critical observation:** the 3:14 + 11:1 pair use the SAME Thai **ความมั่นใจ** for two different but adjacent ὑπόστασις senses — preserves the lexical link in Greek that an etymologically-aware reader might catch (faith as confidence; perseverance in confidence). The 1:3 alone uses the distinct **พระลักษณะ** because the philosophical-essential-being sense is genuinely different (and the παρήσιον would be obscure / wrong).

**Recommend: STABLE; lift to corpus brief doc** `docs/translator_decisions/hypostasis_three_sense_hebrews_2026-05.md` — locks the three-way distinction. Forward-pertinent for: 2 Cor 9:4, 11:17 (ὑπόστασις in financial-context "confidence/undertaking" — needs careful handling) and the patristic / theological-tradition use of ὑπόστασις (homoousios debates) that any future Greek-Christian-historical paratext might reference.

---

## 12. πίστις (faith) cluster + HEB 11 πίστει formula — **LOCKED ✓ (uniform)**

**πίστις occurs 32×** in HEB — densest in the NT alongside Romans (~40×). HEB 11 alone has the πίστει-anaphora (dative-of-means "by faith") **22× from 11:3 to 11:31**. The Thai rendering is **uniformly ความเชื่อ** across ALL grammatical cases (nominative, accusative, genitive, dative) and ALL contexts.

| Pattern | Thai | Count |
|---|---|---|
| πίστις (nom./gen./dat./acc.) → **ความเชื่อ** | uniform | ~30 |
| πίστει (dative-of-means, HEB 11 anaphora) → **โดยความเชื่อ** | 22× in HEB 11 | uniform |
| Κατὰ πίστιν (HEB 11:13) → **โดยความเชื่อ** | 1 | (variant-construction; same Thai) |

**HEB 11:1 famous definition:** Ἔστιν δὲ πίστις ἐλπιζομένων ὑπόστασις, πραγμάτων ἔλεγχος οὐ βλεπομένων → **ความเชื่อคือความมั่นใจในสิ่งที่เราหวัง และเป็นข้อพิสูจน์ในสิ่งที่เรามองไม่เห็น**. Renders the chiastic-doublet (ὑπόστασις ↔ ἔλεγχος) cleanly into Thai with the matched chiastic **ความมั่นใจ ↔ ข้อพิสูจน์** pair.

**Editorial assessment:** Locked-tight. The 22× πίστει anaphora reads cleanly in Thai as **โดยความเชื่อ X [verb]** repeating across HEB 11:3–31 — the rhetorical-cumulative force of "by faith, by faith, by faith" is preserved with full lexical-uniformity. This is what πίστις-rendering ought to look like.

**LOCKED ✓** — already corpus-uniform from prior Pauline (GAL, 1TH) + Synoptic + Johannine usage. No new doc needed; HEB confirms the corpus-wide πίστις → ความเชื่อ lock.

---

## 13. ἀρχηγός — Christ-as-Pioneer / Author / Founder — **STABLE (undocumented; recommend brief doc)**

**ἀρχηγός occurs 2× in HEB** (also at ACT 3:15 and ACT 5:31 as Christological titles) — a HEB-distinctive Christological epithet for the Christ-who-pioneers-the-way.

| Verse | Greek | Thai | Companion |
|---|---|---|---|
| 2:10 | τὸν ἀρχηγὸν τῆς σωτηρίας αὐτῶν | **องค์ผู้บุกเบิกแห่งความรอดของพวกเขา** | (alone) |
| 12:2 | τὸν τῆς πίστεως ἀρχηγὸν καὶ τελειωτὴν Ἰησοῦν | **องค์ผู้บุกเบิกและองค์ผู้บรรลุความสมบูรณ์แห่งความเชื่อ คือพระเยซู** | paired with τελειωτής (HAPAX) |

**Editorial assessment:** **ผู้บุกเบิก** ("pioneer, trailblazer, frontiersman") is a principled Thai compound that captures the Greek ἀρχηγός sense better than the corpus-prior ACT 3:15 **องค์ผู้ทรงเป็นบ่อเกิด** ("source / fountain") or ACT 5:31 **องค์ผู้นำ** ("leader"). The HEB sense is specifically the one-who-runs-ahead-and-makes-the-path — cf. 12:1-2 athletic imagery (running the race set before us, looking to Jesus as **ἀρχηγός** of our faith). The royal **องค์** prefix marks divine-Christological subject.

The 12:2 paired ἀρχηγός + τελειωτής (the HAPAX τελειωτής is the noun-form of τελειόω from §7) renders as **องค์ผู้บุกเบิก + องค์ผู้บรรลุความสมบูรณ์** — preserves the parallel-doublet with both compound-titles taking royal **องค์**.

**Recommend: STABLE; consider brief doc** `docs/translator_decisions/archegos_christ_pioneer_2026-05.md` to lock the HEB-specific **องค์ผู้บุกเบิก** rendering and acknowledge the divergence from the ACT 3:15 + 5:31 alternative renderings (which are corpus-prior and may need a sub-section noting the HEB-shift). Could be folded into the priesthood-vocabulary doc (§2) since the HEB-Christology of pioneer-and-priest is conceptually-coupled.

---

## 14. HEB 13:8 — Ἰησοῦς Χριστὸς ἐχθὲς καὶ σήμερον ὁ αὐτός — **STABLE (climactic immutability formula)**

The famous Hebrews-immutability formula at 13:8:

> Ἰησοῦς Χριστὸς ἐχθὲς καὶ σήμερον ὁ αὐτός, καὶ εἰς τοὺς αἰῶνας.
> **พระเยซูคริสต์ทรงเป็นเหมือนเดิมทั้งวันวาน วันนี้ และตลอดไปเป็นนิตย์**

**Editorial assessment:** The Thai rendering preserves all three temporal-axes (ἐχθές = วันวาน "yesterday"; σήμερον = วันนี้ "today"; εἰς τοὺς αἰῶνας = ตลอดไปเป็นนิตย์ "forever"). The royal **ทรง** prefix on **เป็นเหมือนเดิม** ("is-the-same") preserves the divine-Christ subject. Forms an **inclusio with HEB 1:12** (`σὺ δὲ ὁ αὐτὸς εἶ` → **แต่พระองค์เองยังคงเป็นพระองค์เดิม** — same Christ-immutability claim citing PSA 102:27 LXX), bracketing the entire epistle with the immutable-Christ theme.

**STABLE — no new doc needed.** Existing chapter-1 + chapter-13 inclusio is documented in the verse-level KDs.

---

## 15. OT-LXX citations — densest in the NT (~37 direct citations + ~15 allusions) — **all flagged + many LOGGED**

Hebrews is **the most OT-citation-dense text in the NT** by a wide margin — far surpassing Matthew (60+ citations across 28 chapters; HEB has 37 across 13 chapters). The translator flags every direct citation in `key_decisions` and adds `notes` cross-referencing the LXX source. A representative subset:

| HEB | OT source | Status |
|---|---|---|
| 1:5a | PSA 2:7 LXX | **LOGGED** — Davidic-coronation, reused 5:5 |
| 1:5b | 2 SAM 7:14 LXX | **LOGGED** — Davidic-covenant, reused REV 21:7 |
| 1:6 | DEU 32:43 LXX (longer/4QDeut^q) + PSA 97:7 LXX | **LOGGED** — angels-worship |
| 1:7 | PSA 104:4 LXX | **LOGGED** — angels-as-winds |
| 1:8-9 | PSA 45:6-7 LXX | **LOGGED** — Christ-addressed-as-θεός (see §15B + DECIDE item §G below) |
| 1:10-12 | PSA 102:25-27 LXX | **LOGGED** — Christ-as-creator-Lord-Yahweh |
| 1:13 | PSA 110:1 LXX | **LOGGED** — most-cited OT-text in NT |
| 2:6-8 | PSA 8:4-6 LXX | **LOGGED** — Adam-Christology dual-reference |
| 2:12 | PSA 22:22 LXX | **LOGGED** — suffering-servant Psalm |
| 2:13 | ISA 8:17-18 LXX | **LOGGED** — Christ-as-faithful-trust-er |
| 3:7-11; 3:15; 4:3, 4:5, 4:7 | PSA 95:7-11 LXX | **LOGGED** — repeated 5×; Sabbath-rest argument |
| 4:4 | GEN 2:2 LXX | **LOGGED** — creation-Sabbath |
| 5:5 | PSA 2:7 LXX (re-cited from 1:5) | **LOGGED** — applied to priestly-vocation |
| 5:6; 7:17, 7:21 | PSA 110:4 LXX | **LOGGED** — Melchizedek-priesthood |
| 6:13-14 | GEN 22:17 LXX | **LOGGED** — Abrahamic-covenant oath |
| 7:1-2 | GEN 14:17-20 (allusion-narrative) | **LOGGED** — Melchizedek narrative |
| 8:5 | EXO 25:40 LXX | **LOGGED** — heavenly-pattern of tabernacle |
| 8:8-12 | JER 31:31-34 LXX | **LOGGED** — **THE LONGEST SINGLE OT QUOTATION IN THE NT** (5 verses, 90+ Greek words) |
| 9:20 | EXO 24:8 LXX | **LOGGED** — covenant-blood formula |
| 10:5-7 | PSA 40:6-8 LXX | **LOGGED** — **σῶμα LXX vs. אזנים MT — see DECIDE item §H below** |
| 10:16-17 | JER 31:33-34 LXX (re-cited) | **LOGGED** |
| 10:30 | DEU 32:35-36 LXX | **LOGGED** |
| 10:37-38 | HAB 2:3-4 LXX | **LOGGED** — "the just shall live by faith" |
| 11:5 | GEN 5:24 LXX | **LOGGED** — Enoch translation |
| 11:18 | GEN 21:12 LXX | **LOGGED** — Isaac-as-seed-of-Abraham |
| 12:5-6 | PRO 3:11-12 LXX | **LOGGED** — divine-discipline |
| 12:20 | EXO 19:12-13 LXX | **LOGGED** — Sinai-prohibition |
| 12:21 | DEU 9:19 LXX | **LOGGED** — Moses' "I tremble with fear" |
| 12:26 | HAG 2:6 LXX | **LOGGED** — final-cosmic-shaking |
| 13:5 | DEU 31:6 LXX (or JOS 1:5) | **LOGGED** — "I will never leave you" |
| 13:6 | PSA 118:6 LXX | **LOGGED** — "the Lord is my helper" |
| 13:15 | HOS 14:3 LXX (allusion) | **LOGGED** — fruit-of-lips |
| 13:20 | ISA 63:11 LXX + ZEC 9:11 (allusion-cluster) | **LOGGED** — shepherd-of-the-sheep |

**Editorial assessment:** Every citation is flagged in the KDs; the densest cluster (HEB 1:5–13 catena of seven citations + HEB 8:8–12 JER 31:31–34 quotation + HEB 10:5–7 PSA 40 quotation + HEB 12:5–29 catena) all preserve the LXX-form rendering — including LXX/MT divergences (most importantly HEB 1:6 longer-LXX/4QDeut^q reading; HEB 10:5 σῶμα LXX vs MT אזנים). The LXX-faithful rendering is a deliberate translation choice — see DECIDE item §H below for the 10:5 case.

**Recommend (low priority):** Verify that `data/nt_ot_citations.json` has all ~37 direct citations logged (a one-time scan would confirm; many are already there per the agent inventory).

### 15A. HEB 1:8 ὁ θεός vocative addressed to Christ — Christological-divinity anchor — DECIDE item §G

The single most theologically-loaded citation-rendering in HEB. PSA 45:6 LXX `ὁ θρόνος σου ὁ θεὸς εἰς τὸν αἰῶνα τοῦ αἰῶνος` is cited at HEB 1:8 with the apparent **vocative ὁ θεός addressed TO THE SON** (not nominative "God is your throne"). The translator renders:

> **"ข้าแต่พระเจ้า บัลลังก์ของพระองค์ดำรงอยู่ตลอดไปเป็นนิตย์"**
> ("O God! Your throne endures forever and ever.")

The 1:8 KD names the choice and rejects the alternative explicitly:

> CRITICAL: 'ὁ θεός' here = vocative 'O-God!' addressed-TO-the-Son — explicit-Christological-divinity-citation. Translation ข้าแต่พระเจ้า preserves-vocative-direct-address. Alternative-rendering 'God-is-your-throne' (Jehovah's-Witnesses) is-grammatically-possible-but contextually-and-theologically-rejected: HEB's-argument requires-divine-address.

**Worth Ben's confirmation (DECIDE §G).** This is the single most-explicit direct OT-citation declaring-Christ-as-θεός in the entire NT, alongside JHN 1:1, JHN 20:28 (Thomas's confession), and Tit 2:13 (τοῦ μεγάλου θεοῦ καὶ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ). The Thai vocative **ข้าแต่พระเจ้า** is the standard biblical-Thai for direct-address-to-God; rendering this as direct-address-to-Christ is theologically deliberate and aligns with the mainstream-evangelical-Christological reading. The JW-counter-reading ("God is your throne, [O Messiah]" — taking ὁ θεός as nominative subject of an implied copular clause) is grammatically possible but theologically unmarketable in evangelical-Thai context.

---

## 16. ἱλαστήριον at HEB 9:5 (mercy-seat) vs forward Rom 3:25 (propitiation) — **REVIEW**

The HEB 9:5 ἱλαστήριον rendering **พระที่นั่งกรุณา** ("seat of grace") is the standard biblical-Thai for the OT mercy-seat (LXX-translation of MT כפרת kaporeth). This is the **furniture sense** — the gold cover of the ark.

The forward-Pauline **ROM 3:25** ἱλαστήριον (Christ "set forth as a propitiation/mercy-seat through faith in his blood") uses the **cultic-instrumental sense** — Christ as the propitiating-sacrifice or as the heavenly-mercy-seat-archetype. Most Thai translations (THSV1971, NTV, ERV-Thai) here use **เครื่องบูชาไถ่บาป** ("propitiating-sacrifice") rather than **พระที่นั่งกรุณา** — collapsing into the propitiation reading. The HEB 9:5 KD explicitly notes this distinction.

**REVIEW flag for Ben's confirmation:** When Romans ships, the ROM 3:25 ἱλαστήριον rendering will need explicit choice:
- **Option A (mercy-seat archetype reading):** Render ROM 3:25 with **พระที่นั่งกรุณา** to preserve lexical-link with HEB 9:5 + the LXX-cultic background (Calvin's reading; T.W. Manson, Stuhlmacher)
- **Option B (propitiating-sacrifice reading):** Render with **เครื่องบูชาไถ่บาป** matching THSV1971 and the Thai-evangelical reader expectation (Morris's wrath-propitiation reading; mainstream evangelical-Reformed)
- **Option C (expiation reading):** Render with **เครื่องลบล้างบาป** ("means of erasing/expiating sin") — the Dodd / RSV "expiation" position

Worth Ben's confirmation that **Option A** (lexical-link to HEB 9:5) is the project default — OR an explicit decision to differ. The doc `docs/translator_decisions/tabernacle_vocabulary_hebrews_2026-05.md` (recommended in §6) should document this as a forward-pertinent question for Romans.

---

## 17. Inherited corpus locks — **all compliant, with two qualified notes**

Comprehensive scan of the 18 active corpus locks and HEB compliance:

| Lock | HEB evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 2:12 (PSA 22:22 cite, ἐν μέσῳ ἐκκλησίας → **ในท่ามกลางคริสตจักร**) + 12:23 (ἐκκλησίᾳ πρωτοτόκων → **คริสตจักรของบรรดาบุตรหัวปี**) — uniform **คริสตจักร** despite the OT-citation context at 2:12. | **LOCKED** |
| `ethnos_2026-04.md` | **N/A in HEB** — no occurrences of ἔθνος/ἐθνικός in HEB (the closest is HEB 11:33 πατρίας ... κατηγωνίσαντο βασιλείας). | **LOCKED (N/A)** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | HEB 8:2 (ὁ κύριος ... οὐκ ἄνθρωπος → **องค์พระผู้เป็นเจ้า ... มิใช่มนุษย์**) + 12:14 (ὄψεται τὸν κύριον → **จะได้เห็นองค์พระผู้เป็นเจ้า**) + ~10 narrator + OT-citation κύριος uniformly **องค์พระผู้เป็นเจ้า**. The HEB OT-citation κύριος-as-Yahweh is collapsed with narrator-κύριος-as-Christ rendering — exegetically-defensible since HEB Christologically-applies the LXX-Yahweh-texts to Christ (1:10 etc.). | **LOCKED-with-amendment-needed** (already noted in JHN + GAL + 1TH audits — HEB is the fourth independent corpus confirmation that the doc's "Lukan-Acts" framing should be renamed/extended) |
| `vocative_kyrie_didaskale_register_2026-04.md` | **N/A in HEB** — no narrative-vocative κύριε in HEB (epistolary-homily, not narrative; the 1:10 κύριε is in OT-citation, not narrator-vocative). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | HEB 13:15 (θυσίαν αἰνέσεως → **เครื่องบูชาแห่งคำสรรเสริญ**) — αἴνεσις noun-form rendered with the locked **สรรเสริญ** family. Compliant. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | All non-divine OT figures (Abraham, Moses, Aaron, Joshua, Melchizedek, Esau, Rahab) in plain register — no royal pระ-/ทรง- on their actions. The 12:7-9 πατήρ register split (human-fathers plain, divine-Father royal) is exact. Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | HEB is homiletic; no character-voice narratives. The author addresses Christ throughout in narrator-voice with full royal register. Compliant. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | **N/A in HEB** — no Aramaic embeds (Μελχισέδεκ + Σαλήμ + Ἁβραάμ are Hebrew transliterations, not Aramaic; no αββα, μαραναθα, ταλιθα, etc.). Note: Χερουβίν at 9:5 is a HAPAX Hebrew-loanword plural — rendered **เครูบ** transliteration. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A in HEB** — `audit_inclusion_variants.py --book hebrews --strict` exits 0; zero candidates. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | **N/A** — HEB is homiletic, not narrative. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | **N/A** — no parables in HEB. The HEB 11 hall-of-faith figures are historical-narrative-summary, not parable. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | μετάνοια at 6:1 (foundational-doctrine) + 6:6 (impossible-to-renew-εἰς-μετάνοιαν) + 12:17 (Esau "found-no-place-for-μετάνοια") — uniform **การกลับใจ**. μεταμέλομαι absent from HEB. Compliant. | **LOCKED** |
| `aphesis_forgiveness_of_sins_2026-04.md` | HEB 9:22 (χωρὶς αἱματεκχυσίας οὐ γίνεται ἄφεσις → **ก็ไม่มีการยกโทษบาป**) + 10:18 (ὅπου δὲ ἄφεσις τούτων → **ที่ใดมีการยกโทษบาปเหล่านี้แล้ว**) — uniform locked **การยกโทษบาป**. | **LOCKED** |
| `pagan_deities_2026-04.md` | **N/A** — no pagan-deity references in HEB. | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` | **N/A** — no Roman titles in HEB. | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | **N/A** — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | HEB 2:6 (PSA 8 citation) ἢ υἱὸς ἀνθρώπου → **บุตรมนุษย์** — preserves the locked rendering despite the Adam-anthropology context (HEB 2:6 is the rare NT Adam-Christology dual-reference: PSA 8 cited as both about Adamic-humanity AND Messianic-Son-of-Man). The KD acknowledges the dual-reference. Compliant. | **LOCKED** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | HEB 4:12 (μερισμοῦ ψυχῆς καὶ πνεύματος → **การแบ่งจิตวิญญาณและวิญญาณ**) — see §18 below for analysis. HEB 6:19 (ψυχή → **จิตวิญญาณ**), 10:38-39 (×2 → **จิตวิญญาณ**), 12:23 (πνεύμασι → **จิตวิญญาณ**), 13:17 (ψυχῶν → **จิตวิญญาณ**) all compliant. The HEB 4:12 case is the one substantive crux — see §18. | **LOCKED-with-amendment-needed** (4:12 tripartite-adjacent exception; coordinates with the 1Th 5:23 amendment recommendation — see §F) |
| `johannine_doubled_amen_2026-04.md` | **N/A** — Johannine-specific. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | **N/A** — no Synoptic-Jesus-direct-discourse in HEB (though HEB 13:21 closes with a doxological ἀμήν → **อาเมน** corpus-standard). | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | **N/A** — no narrative-adversary-speech in HEB. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | HEB 1:8 (PSA 45 cite, βασιλείας → **ราชอาณาจักร** — compound royal-form for divine-kingdom-context) + 11:33 (κατηγωνίσαντο βασιλείας → **อาณาจักร** plural plain) + 12:28 (βασιλείαν ἀσάλευτον → **อาณาจักรที่ไม่อาจเขย่าได้** — eschatological). Per-context principled. Compliant. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | HEB 4:14 (διεληλυθότα τοὺς οὐρανούς → **ฟ้าสวรรค์** plural cosmic-scope) + 7:26 (ὑψηλότερος τῶν οὐρανῶν → **ฟ้าสวรรค์**) + 9:23-24 (3× → **สวรรค์**) + 12:23 (ἐν οὐρανοῖς → **สวรรค์**) + 12:25 (ἀπ' οὐρανῶν → **สวรรค์**) + 12:26 (γῆν ... καὶ τὸν οὐρανόν → **ฟ้าสวรรค์** cosmic-pair). Doc rule applied perfectly. Compliant. | **LOCKED** |
| `parepidemos_paroikos_sojourner_2026-05.md` | HEB 11:13 (ξένοι καὶ παρεπίδημοί → **คนต่างด้าวและผู้พำนักอาศัย** — doublet-preserved). Compliant with the Petrine-rooted lock. | **LOCKED** |
| `pascho_pathema_suffering_2026-05.md` | HEB 2:9, 2:10, 2:18, 5:8, 9:26, 13:12 — Christ-subject πάσχω uniformly takes **ทรง** royal prefix. The lock is Pauline-rooted but HEB applies it consistently across the Christ-suffering verses. Compliant. | **LOCKED** |
| `prototokos_pauline_2026-05.md` | HEB 1:6 (πρωτότοκον singular-incarnation → **บุตรหัวปี**); 11:28 (τὰ πρωτότοκα plural-Passover → **บุตรหัวปี**); 12:23 (πρωτοτόκων plural-relational-of-believers → **บรรดาบุตรหัวปี**). Compliant — the Pauline three-sense split applies to genitive-marked Pauline-Christological cases (COL 1:15-18); HEB uses simple absolute forms. | **LOCKED** |
| `arnion_amnos_lamb_disambiguation_2026-05.md` | **N/A in HEB** — HEB uses different sacrificial-victim vocabulary (μόσχος, τράγος, δάμαλις, ταῦρος) for OT-type sacrifices; no ἀρνίον or ἀμνός. | **LOCKED (N/A)** |
| `stoicheia_tou_kosmou_2026-05.md` | HEB 5:12 (τὰ στοιχεῖα τῆς ἀρχῆς → **หลักเบื้องต้น**) — different sense (basic-elementary-teachings, not cosmic-elementals). The lock allows for this contextual-shift. Compliant. | **LOCKED** |
| `revelation_divine_self_titles_2026-05.md` | **N/A** — Apocalyptic-specific. | **LOCKED (N/A)** |
| `diakonos_pauline_2026-05.md` | HEB uses cognate λειτουργ- family (1:14 λειτουργικά → **ผู้ปรนนิบัติ**; 8:2 λειτουργός → **ผู้ปรนนิบัติ**; 8:6 λειτουργίας → **ปรนนิบัติ** noun) — plain-register, not office-term. Compliant with the Pauline lock's broad "servant/minister, not institutional office" principle. | **LOCKED** |

---

## 18. The HEB 4:12 ψυχή / πνεῦμα crux — **REVIEW (the one substantive psyche-vs-pneuma exception in HEB)**

HEB 4:12 has the famous "soul-and-spirit" doublet — the one verse the translator must grapple with where ψυχή and πνεῦμα appear in immediate-coordinate-parallel-construction:

> **διϊκνούμενος ἄχρι μερισμοῦ ψυχῆς καὶ πνεύματος, ἁρμῶν τε καὶ μυελῶν**
> **แทงทะลุจนถึงการแบ่งจิตวิญญาณและวิญญาณ ข้อต่อและไขในกระดูก**

Renderings:
- **ψυχή → จิตวิญญาณ** ("soul, animating-life")
- **πνεῦμα → วิญญาณ** ("spirit, ghost")

The 4:12 KD names the choice:

> ψυχή/πνεῦμα distinguished here: จิตวิญญาณ (soul, animating-life) / วิญญาณ (spirit, divine-relating). Per-corpus-lock-pattern psyche-vs-pneuma anthropology.

**Editorial assessment — coordinate with 1Th 5:23 tripartite amendment:** The locked corpus rule (per `docs/CHAPTER_REVIEW_PROMPT.md` line 38):

> ψυχή → จิตวิญญาณ / ชีวิต (context); πνεῦμα (anthropological) → จิต — distinct from πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์

The 1 Thessalonians audit (§6 + §E) flagged the 1Th 5:23 tripartite-listing exception (where the translator used **วิญญาณ + จิตใจ + ร่างกาย** for πνεῦμα + ψυχή + σῶμα, departing from the locked **จิตวิญญาณ ↔ จิต** distinction). The 1Th audit recommended amending the existing `psyche_vs_pneuma_anthropological_2026-04.md` doc with a 1 Thess 5:23 sub-section.

**HEB 4:12 is a SECOND parallel exception** — and the only NT verse outside 1Th 5:23 where ψυχή and πνεῦμα appear in true-coordinate-parallel. The translator chose **จิตวิญญาณ + วิญญาณ** here, **inverse** to the 1Th 5:23 choice (**วิญญาณ + จิตใจ**). The two-listings render PARTIALLY-OVERLAPPING but not-identically:

| Verse | Greek | Thai for ψυχή | Thai for πνεῦμα |
|---|---|---|---|
| 1Th 5:23 | πνεῦμα + ψυχή + σῶμα | **จิตใจ** | **วิญญาณ** |
| HEB 4:12 | ψυχή + πνεῦμα | **จิตวิญญาณ** | **วิญญาณ** |

**Recommend (REVIEW + DECIDE):** This needs Ben's confirmation:
- Option A — Accept both as principled context-dependent renderings (1Th 5:23 = Pauline-trichotomy-prayer-context uses **วิญญาณ + จิตใจ + ร่างกาย**; HEB 4:12 = Word-piercing-discernment context uses **จิตวิญญาณ + วิญญาณ**). Document as two distinct sub-sections of the existing `psyche_vs_pneuma_anthropological_2026-04.md` doc. The translator's reasoning is contextual — HEB 4:12 emphasizes the pierce-to-the-deepest-spiritual-faculty, which warrants the elevated **วิญญาณ** rendering for πνεῦμα; 1Th 5:23 emphasizes the whole-person-prayer, which collapses into the inner/outer distinction
- Option B — Normalize HEB 4:12 + 1Th 5:23 to the **same Thai pairing** for cross-text consistency. The audit-recommended pairing would be **จิตวิญญาณ + วิญญาณ** (HEB 4:12 current) — which would require revising 1Th 5:23
- Option C — Restore the locked corpus rule (**ψυχή → จิตวิญญาณ** + **πνεῦμα → จิต**) at HEB 4:12, requiring a chapter-revision

**→ Recommend: Option A.** The two contexts are meaningfully different (trichotomy-prayer vs Word-discerning-piercing); two principled exceptions in the corpus is acceptable; document both sub-sections in the existing doc.

---

## Mechanical (§1) — **all green**

- 13/13 chapters: `output/check_reports/hebrews_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 13/13 chapters: `output/back_translations/hebrews_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-261-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (7943 verses across 261 chapter files)
- `python3 scripts/audit_inclusion_variants.py --book hebrews --strict`: exits 0; zero candidates
- `python3 scripts/export_to_usfm.py --book HEB`: regenerates `output/paratext/HEB.SFM` (13 chapters) cleanly
- `git status output/`: only re-ran-check artifacts and other-book in-flight files (no HEB-source dirt)

---

## Pre-existing docs affirmed / unchanged

All ~52 docs in `docs/translator_decisions/` reviewed. Compliance summary in §17 above. Two docs flagged for amendment:
1. **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to "Lukan-Acts + Johannine + Pauline (Galatians + 1TH) + Hebrews." JHN + GAL + 1TH audits already flagged this; HEB provides the fourth independent corpus confirmation. The doc's "Lukan signature" framing is now demonstrably corpus-wide.
2. **`psyche_vs_pneuma_anthropological_2026-04.md`** — add HEB 4:12 sub-section alongside the 1Th 5:23 sub-section (already recommended in 1Th audit §6). The HEB 4:12 case completes the pair: the corpus has TWO context-dependent exceptions to the corpus-locked **ψυχή / πνεῦμα → จิตวิญญาณ / จิต** rule.

---

## Flagged for Ben's attention

### A. κρείττων thesis-word lift to corpus doc — **STABLE, lift to corpus doc** (§1)
13-occurrence density makes HEB the only locking-precedent for κρείττων. Lift to corpus doc `kreitton_hebrews_thesis_2026-05.md`.

### B. Priesthood vocabulary cluster — **STABLE, lift to corpus doc** (§2)
Most-distinctive cluster in HEB. Lift to corpus doc `priesthood_vocabulary_hebrews_2026-05.md` before 1 Pet 2:5, 9 (royal-priesthood ἱεράτευμα — different lemma but cognate-cluster) + Rev 1:6, 5:10, 20:6 (priests-of-God-and-Christ).

### C. διαθήκη covenant lift to corpus doc — **STABLE, lift to corpus doc** (§3)
Densest covenant-text in NT. Lift to corpus doc `diatheke_hebrews_2026-05.md` before Rom 9:4 + 1 Cor 11:25.

### D. αἷμα + αἱματεκχυσία blood-register split — **STABLE, lift to corpus doc** (§4)
Densest sacrificial-blood-text in NT. Lift to corpus doc `aima_blood_register_hebrews_2026-05.md` before 1 Pet 1:2, 19 + Rev 1:5, 5:9, 7:14, 12:11, 19:13.

### E. θυσία + προσφορά + tabernacle vocabulary — **STABLE, lift to corpus doc(s)** (§5 + §6)
Two related corpus docs (or one combined doc): sacrifice-vocabulary (§5) + tabernacle-vocabulary (§6). The latter must address the forward Rom 3:25 ἱλαστήριον question (see §16 + REVIEW item below).

### F. ἁγιασμός / ἁγιωσύνη amendment to 1Th-anchored doc — **DECIDE before tagging** (§8)
HEB 12:14 ἁγιασμόν → **ความบริสุทธิ์** is non-compliant with the 1Th audit's proposed **ἁγιασμός → การชำระให้บริสุทธิ์** lock (process-vs-state distinction). Ben must choose: (a) revise HEB 12:14 to **การชำระให้บริสุทธิ์**; or (b) collapse the process-vs-state distinction in the not-yet-written `hagiasmos_hagiosune_2026-04.md` doc.

### G. HEB 1:8 ὁ θεός vocative addressed to Christ — **DECIDE before tagging** (§15A)
The single most-explicit Christological-divinity citation in the NT. Worth Ben's confirmation that the vocative-direct-address-to-Son rendering **ข้าแต่พระเจ้า** is the corpus default (vs the JW-counter-reading "God is your throne"). Likely confirmation; aligns with RULES §0 evangelical-Protestant alignment.

### H. HEB 10:5 σῶμα LXX vs MT אזנים — **DECIDE before tagging** (§15)
The translator follows LXX **σῶμα** ("a body you have prepared for me") rendering as **พระกาย** — necessary for the incarnation-typology (Christ's body offered as PSA 40 sacrifice). The MT-Hebrew has **אזנים כרית לי** ("ears you have dug for me"). The 10:5 KD acknowledges the textual-issue and follows-LXX. Worth Ben's confirmation: this is a deliberate departure from MT-faithful translation that aligns with NT-author usage but diverges from MT (and from the OT-translation tradition that follows MT). RULES §0 binds source-text to SBLGNT, not MT — so the LXX-faithful rendering in this NT-citation context is principled. But because this is one of the clearest LXX/MT-divergence-citations in the NT, worth confirming the policy.

### I. HEB 6:4-6 apostasy-passage — **DECIDE before tagging** (the most contested HEB passage)

The famous Hebrews-warning passage. The translator follows BSB / ESV / NIV in:
- ἀνασταυρόω (HAPAX) → **ตรึง...บนกางเขนซ้ำอีก** (the "again" reading: re-crucifixion of Christ)
- παραδειγματίζω (HAPAX) → **ประจาน...ต่อสาธารณชน** (public-shaming)
- ἀδύνατον ... πάλιν ἀνακαινίζειν εἰς μετάνοιαν → **เป็นไปไม่ได้ที่จะนำคนเหล่านั้น ... กลับมาสู่การกลับใจอีกครั้ง** (impossibility-of-renewing-to-repentance)

The 6:6 KD acknowledges the three traditional interpretive streams (Calvinist: not-true-believers; Arminian: true-apostasy-possible; Hypothetical: rhetorical-impossible-condition) and **deliberately preserves the ambiguity** in the Thai rendering — allowing the Thai reader to occupy any of the three positions theologically without the translation pre-committing.

**Worth Ben's confirmation (DECIDE §I):** The deliberate-ambiguity policy is worth explicit-affirmation in a corpus doc. Recommend new doc `docs/translator_decisions/hebrews_warning_passages_2026-05.md` to lock the deliberate-ambiguity rendering policy across all five Hebrews warning-passages (2:1-4, 3:7-4:13, 5:11-6:12, 10:26-31, 12:14-29). This protects the policy from drift in any future revision.

### J. ἱλαστήριον dual-sense before Romans — **REVIEW** (§16)
HEB 9:5 mercy-seat → **พระที่นั่งกรุณา** is correct biblical-Thai for the OT-furniture sense. ROM 3:25 propitiation will need explicit-choice between **พระที่นั่งกรุณา** (preserves lexical-link) vs **เครื่องบูชาไถ่บาป** (matches THSV1971 evangelical-Thai default). Worth deciding before Romans ships.

### K. HEB 12:3 ταῖς ψυχαῖς paraphrase — **REVIEW** (minor)
HEB 12:3 ἵνα μὴ κάμητε ταῖς ψυχαῖς ὑμῶν → **เพื่อพวกท่านจะไม่เหน็ดเหนื่อยและท้อใจ** ("lest you grow weary and discouraged"). The dative-of-respect ψυχαῖς ("in your souls") is paraphrased away into **ท้อใจ** ("become discouraged"). This is principled Thai-naturalness — the literal **เหน็ดเหนื่อยในจิตวิญญาณของท่าน** would be unnatural. Worth Ben's confirmation that the paraphrase-policy is acceptable for adverbial-dative ψυχή uses where the lexeme is structural, not theological.

### L. New corpus docs to write (before Romans ships)
1. **`docs/translator_decisions/kreitton_hebrews_thesis_2026-05.md`** (§1) — locks the dual-rendering and the structural-thesis
2. **`docs/translator_decisions/priesthood_vocabulary_hebrews_2026-05.md`** (§2) — locks the four-element cluster
3. **`docs/translator_decisions/diatheke_hebrews_2026-05.md`** (§3) — locks the covenant-rendering (highest forward-Pauline priority)
4. **`docs/translator_decisions/aima_blood_register_hebrews_2026-05.md`** (§4) — locks the royal/plain register split
5. **`docs/translator_decisions/thysia_prosphora_hebrews_2026-05.md`** (§5) — locks the sacrificial-doublet
6. **`docs/translator_decisions/tabernacle_vocabulary_hebrews_2026-05.md`** (§6 + §16) — locks σκηνή/καταπέτασμα/ἅγια/ἱλαστήριον AND the forward Rom 3:25 question
7. **`docs/translator_decisions/teleios_teleioo_hebrews_2026-05.md`** (§7) — locks the perfection cluster
8. **(Optional)** `proserchomai_cultic_2026-05.md` (§9) — brief; could fold into priesthood doc
9. **(Optional)** `katapausis_sabbatismos_2026-05.md` (§10) — brief; HEB-internal
10. **(Optional)** `hypostasis_three_sense_hebrews_2026-05.md` (§11) — brief; HEB-internal but theologically-rich
11. **(Optional)** `archegos_christ_pioneer_2026-05.md` (§13) — brief; could fold into priesthood doc
12. **(High-priority)** `hagiasmos_hagiosune_2026-04.md` (§8 + 1Th audit §2) — recommended in 1Th audit, now compounded by HEB 12:14
13. **(High-priority)** `hebrews_warning_passages_2026-05.md` (§I above) — locks the deliberate-ambiguity policy across all 5 warning passages

### M. Existing docs to amend
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to "Lukan-Acts + Johannine + Pauline + Hebrews" — fourth corpus confirmation
- **`psyche_vs_pneuma_anthropological_2026-04.md`** — add HEB 4:12 sub-section alongside the 1Th 5:23 sub-section (recommended in 1Th audit §6)

### N. External AI review (§3 of checklist) — **pending**

Recommended before `book-hebrews-v1` tag. Suggested 5-cluster external AI packet:
1. **HEB 1:1–14** — opening + Christological catena (7 OT citations) + Christ-as-θεός vocative anchor
2. **HEB 4:12 + 4:14–5:10** — the Word-piercing passage + ψυχή/πνεῦμα crux + introduction of the priestly Christology
3. **HEB 6:4–8** — the famous apostasy-passage with FOUR HAPAX (παραπίπτω + ἀνακαινίζω + ἀνασταυρόω + παραδειγματίζω)
4. **HEB 8:1–10:18** — the JER 31 new-covenant citation + PSA 40 σῶμα/MT-divergence + tabernacle vocabulary cluster
5. **HEB 11:1 + 11:13 + 12:18–24** — faith-definition + sojourner-doublet + Sinai-vs-Zion approach contrast

Use Grok + ChatGPT in parallel per the JHN/GAL/1TH pattern.

---

## Recommendation

**Hebrews ships in strong corpus-hygiene shape — and is the project's first homiletic-priestly book, introducing the densest single-book vocabulary cluster yet committed.** The translator made consistent, principled choices on the eleven HEB-distinctive lemma-clusters (κρείττων; priesthood vocabulary; διαθήκη; αἷμα; θυσία/προσφορά; tabernacle vocabulary; perfection cluster; purification/sanctification; cultic drawing-near; rest cluster; ὑπόστασις three-way split) — and **none of these eleven has a corpus-level doc** yet. This is the moment to lock them in before the Pauline corpus compounds the editorial weight: Romans will compound διαθήκη, ἱλαστήριον, sacrifice-vocabulary, and δικαιοσύνη; 1 Pet will compound priesthood + sacrificial-blood; Revelation will compound Lamb-blood + cosmic-eschatology.

Tag `book-hebrews-v1` after:
1. Ben's decisions on **§F + §G + §H + §I** (DECIDE items: 12:14 ἁγιασμός render-or-amend; 1:8 vocative ὁ θεός confirmation; 10:5 LXX/MT departure confirmation; 6:4-6 deliberate-ambiguity policy)
2. Ben's confirmation on **§J + §K** (REVIEW items: ROM 3:25 forward-policy; HEB 12:3 paraphrase-acceptable)
3. Six-to-eleven new translator_decisions docs written (§L items 1-7 minimum + 12-13; optionally 8-11)
4. Two existing docs amended (`kyrios_narrator_voice_luke_acts_2026-04.md`; `psyche_vs_pneuma_anthropological_2026-04.md`)
5. External AI sanity-check (§N)

The Pauline letters (currently in flight) and the Petrine + General + Revelation clusters can be queued for next-book — but writing **`diatheke_hebrews`, `priesthood_vocabulary_hebrews`, `aima_blood_register_hebrews`, and `tabernacle_vocabulary_hebrews`** docs should happen **before Rom 3 ships** to avoid forward drift in the sacrificial-and-cultic vocabulary that Romans will compound dramatically (Rom 3:25 ἱλαστήριον; Rom 5:9 ἐν τῷ αἵματι; Rom 8:3 περὶ ἁμαρτίας — the LXX-Day-of-Atonement formula).
