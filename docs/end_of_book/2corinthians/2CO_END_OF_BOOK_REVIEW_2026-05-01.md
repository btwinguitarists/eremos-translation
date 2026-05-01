# 2 Corinthians — End-of-Book Review

**Date:** 2026-05-01
**Scope:** All 13 chapters (256 verses); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** 2CO 13 shipped (commit `ff8cd50` thai-bible-ai); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2) + handwritten External AI items packet (§3 — ready for Gemini/Grok/ChatGPT cross-review). No translation changes prescribed; surface only.

## Summary

- **12 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 13/13 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 violations) across the 162-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status` clean (only re-ran-check artifacts).
- **2 Corinthians is the FIFTH FULL Pauline epistle the project has shipped** (after Galatians, 1 Thess, 2 Thess, 1 Cor; all between 2026-04-30 and 2026-05-01). At 13 chapters it is the second-largest Pauline letter shipped to date. It is also the most autobiographical-rhetorical Pauline letter — the corpus's first dense exposure to:
  - **Comfort / consolation cluster** (chs 1, 7): παράκλησις / παρακαλέω in the densest distribution in the NT (1:3–7 alone has 10 occurrences of the family). The translator splits the Thai by sense — **การหนุนใจ** (comfort) vs **วิงวอน / ขอร้อง** (appeal/urge).
  - **Reconciliation cluster** (5:18–20): καταλλαγή / καταλλάσσω → **คืนดี**. The first dense NT καταλλαγή cluster, lead-in to Rom 5:10–11; 11:15; Eph 2:16; Col 1:20–22.
  - **Old-vs-New-covenant exposition** (3:6–18): διαθήκη + γράμμα/πνεῦμα + Mosaic-veil typology. The first dense διαθήκη theological-cluster, lead-in to Hebrews.
  - **Pneumatic-deposit / sealing** (1:21–22; 5:5): ἀρραβών τοῦ πνεύματος → **มัดจำ**. First-occurring corpus-cross-cutting key term (recurs Eph 1:14).
  - **Pauline diatribe / fool's-speech rhetoric** (chs 10–12): καυχάομαι / καύχησις in the densest concentration in the NT (~29 occurrences across 4 chapters), juxtaposed with sarcastic embedded-quotation of opponents' self-styling (ὑπερλίαν ἀπόστολοι "super-apostles" at 11:5, 12:11; ψευδαπόστολοι at 11:13).
  - **Cosmic-dualism vocabulary**: ὁ θεὸς τοῦ αἰῶνος τούτου (4:4) — Satan-as-"god"; Βελιάρ (6:15) — the first NT Belial-occurrence; Σατανᾶς (2:11; 11:14; 12:7) — densely woven as the diabolic counterpart.
  - **Visionary-experience vocabulary** (12:1–7): ὀπτασίαι, ἀποκαλύψεις κυρίου, τρίτος οὐρανός, παράδεισος, σκόλοψ τῇ σαρκί. The most personal-mystical passage in Paul.
- **Inherited locks verified compliant** across 2 Cor: ἐκκλησία (1:1, 8:1, 8:18, 8:19, 8:23, 8:24, 11:8, 11:28, 12:13 → คริสตจักร); narrator-κύριος (densely throughout → องค์พระผู้เป็นเจ้า); οὐρανός (5:1; 12:2 "ฟ้าสวรรค์ชั้นที่สาม" preserves the locked theological-default after possessor); μετανοέω/μεταμέλομαι split (7:8 ไม่เสียใจ / 7:9 การกลับใจ — the locus classicus of the 2026-04 lock, cleanly handled); Roman-titles (11:32 ἐθνάρχης Ἁρέτα → ผู้สำเร็จราชการ — extension to a non-Roman client-king's official); ἔθνος three-way (11:26 ἐξ ἐθνῶν → คนต่างชาติ); εἰδώλον (6:16 → รูปเคารพ — locked from 1 Cor); pagan-deities (4:4 ὁ θεὸς τοῦ αἰῶνος τούτου → **เทพเจ้าแห่งยุคนี้** — striking application of the "พระเจ้า reserved for biblical God only" rule to the Satan-as-metaphorical-god reference).
- **No major textual variants in 2 Corinthians.** SBLGNT followed throughout. No Tier 1/2/3 inclusion variants flagged for 2 Cor (no `output/textual_variants/2corinthians*` files). No chapter-footer notes attached.
- **External AI cross-review (§3) PENDING.** Items doc + packet ready: paste `docs/end_of_book/2corinthians/external_review_packet_2CO_2026-05-01.md` into Gemini / Grok / ChatGPT / Claude.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — defensible, worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. παράκλησις / παρακαλέω cluster (1:3–7; 7:4–13) — **STABLE (undocumented; recommend new doc — high Pauline-forward priority)**

The παράκλησις family is **densest in 2 Cor of any NT book** (~30 occurrences across the family). Translator splits by Thai sense:

| Sense | Greek | Thai | Examples |
|---|---|---|---|
| comfort / consolation | παράκλησις, παρακαλέω | **การหนุนใจ / หนุนใจ** | 1:3 πάσης παρακλήσεως → **การหนุนใจทั้งสิ้น**; 1:4 παρακαλῶν ἡμᾶς → **ทรงหนุนใจเรา**; 7:4 πεπλήρωμαι τῇ παρακλήσει → **ได้รับการหนุนใจอย่างเต็มที่** |
| appeal / urge | παρακαλέω | **วิงวอน / ขอร้อง / ร้องวิงวอน** | 5:20 ὡς τοῦ θεοῦ παρακαλοῦντος δι' ἡμῶν → **ราวกับว่าพระเจ้าทรงร้องวิงวอนผ่านทางเรา**; 6:1 παρακαλοῦμεν → **เราจึงวิงวอน**; 8:6 παρακαλέσαι ἡμᾶς Τίτον → **เราจึงได้ขอร้องทิตัส** |

The 1:3–7 ten-fold echo (παρακλήσεως × 5 + παρακαλέω × 4 + παρακαλούμεθα × 1 in 5 verses) is preserved as a **rhythmic Thai echo** with the same root **หนุนใจ** repeated — the Greek wordplay is reproducible because Thai also tolerates lexical anaphora at this density.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/paraklesis_paraklao_2026-05.md` before Romans (12:1, 15:30 παρακαλέω-appeal cluster) and the Pastorals. The doc should:
1. Lock comfort-sense παράκλησις / παρακαλέω → **การหนุนใจ / หนุนใจ**
2. Lock appeal-sense παρακαλέω → **วิงวอน / ขอร้อง / ร้องวิงวอน** (context-dependent)
3. Cite 2 Cor 1:3–7 as the locking precedent for comfort-sense; 5:20 + 6:1 for appeal-sense
4. Cross-reference 1 Thess 4:1, 4:18, 5:11 (early Pauline appeal-uses; rendered consistently)

---

## 2. καταλλαγή / καταλλάσσω — reconciliation cluster (5:18–20) — **STABLE (undocumented; recommend new doc — high Pauline-forward priority)**

The 5:18–20 cluster is the FIRST DENSE NT καταλλαγή occurrence:

| Verse | Greek | Thai |
|---|---|---|
| 5:18 | τοῦ καταλλάξαντος ἡμᾶς ἑαυτῷ διὰ Χριστοῦ καὶ δόντος ἡμῖν τὴν διακονίαν τῆς καταλλαγῆς | **ผู้ทรงให้เราคืนดีกับพระองค์โดยทางพระคริสต์ และทรงประทานพันธกิจแห่งการคืนดีให้แก่เรา** |
| 5:19 | θεὸς ἦν ἐν Χριστῷ κόσμον καταλλάσσων ἑαυτῷ ... τὸν λόγον τῆς καταλλαγῆς | **พระเจ้าได้ทรงให้โลกคืนดีกับพระองค์ในพระคริสต์ ... ถ้อยคำแห่งการคืนดี** |
| 5:20 | καταλλάγητε τῷ θεῷ | **จงคืนดีกับพระเจ้าเถิด** |

Verb form → **คืนดี** ("be reconciled; restore relationship"); noun form → **การคืนดี** ("the [act of] reconciliation"). Theologically rich and Thai-natural — **คืนดี** is the everyday Thai idiom for "make peace / restore" between estranged parties. The active-vs-passive force of καταλλάσσω is preserved by Thai voice constructions (ทรงให้... คืนดี = "cause to be reconciled" — divine-active subject).

**Editorial assessment:** The principled active-vs-passive split (God καταλλάσσει the world; the world is to καταλλάγητε / be-reconciled) reads cleanly in Thai. The companion λόγος τῆς καταλλαγῆς (5:19) → **ถ้อยคำแห่งการคืนดี** preserves the Pauline gospel-as-message-of-reconciliation framing.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/katallage_reconciliation_2026-05.md` before Rom 5:10–11 (the next-densest cluster) and Eph 2:16; Col 1:20–22. The doc should:
1. Lock καταλλαγή → **การคืนดี**; καταλλάσσω → **คืนดี / ทรงให้คืนดี**
2. Cite 2 Cor 5:18–20 as the locking precedent
3. Note the cognate ἀποκαταλλάσσω (Col 1:20, Eph 2:16) — confirm whether intensified prefix needs a Thai marker (e.g., **ทรงให้คืนดีอย่างสมบูรณ์**) or stays uniform

---

## 3. καυχάομαι / καύχησις / καύχημα — pride/boast cluster (chs 10–12) — **REVIEW**

2 Cor has **the densest καυχάομαι-family concentration in the NT** (~29 occurrences across chs 10–12, the so-called "fool's speech"). Translator uniformly renders the family with **ภาคภูมิใจ** / **ความภาคภูมิใจ** ("be proud, take pride / pride"):

| Verse | Greek | Thai |
|---|---|---|
| 1:14 | καύχημα ὑμῶν ἐσμεν | **เราเป็นเหตุที่พวกท่านภูมิใจ** |
| 10:8 | περισσότερόν τι καυχήσωμαι περὶ τῆς ἐξουσίας ἡμῶν | **ข้าพเจ้าจะภาคภูมิใจเกินไปในเรื่องสิทธิอำนาจของเรา** |
| 10:17 | Ὁ δὲ καυχώμενος ἐν κυρίῳ καυχάσθω | **'แต่ผู้ที่ภาคภูมิใจ ก็ให้เขาภาคภูมิใจในองค์พระผู้เป็นเจ้าเถิด'** (OT-citation, Jer 9:24) |
| 11:18 | πολλοὶ καυχῶνται κατὰ σάρκα, κἀγὼ καυχήσομαι | **คนเป็นจำนวนมากภาคภูมิใจตามเนื้อหนัง ข้าพเจ้าก็จะภาคภูมิใจเช่นกัน** |
| 11:30 | τὰ τῆς ἀσθενείας μου καυχήσομαι | **ข้าพเจ้าก็จะภาคภูมิใจในสิ่งที่แสดงความอ่อนแอของข้าพเจ้า** |
| 12:9 | καυχήσομαι ἐν ταῖς ἀσθενείαις μου | **ข้าพเจ้าจะภาคภูมิใจในความอ่อนแอของข้าพเจ้า** |

**The interpretive crux:** καυχάομαι in Paul carries a **double valence** — pejorative when subject is opponents/flesh (10:12; 11:12, 18; "boast" in the bad sense), redeemed when subject is "in the Lord" or "in weakness" (10:17; 11:30; 12:9). Thai **ภาคภูมิใจ** is **uniformly positive** ("take pride, be proud") and may UNDER-COMMUNICATE the pejorative force in 11:18 ("many boast according to the flesh" reads in Thai as "many take-pride-according-to-the-flesh"), where a pejorative **อวด** ("show off, brag, vaunt") would land harder.

The translator's choice — uniform **ภาคภูมิใจ** — is principled (preserves the Pauline rhetorical inversion, where the same verb is *both* the disease and the cure across the fool's speech) but reads as more even-keeled than the Greek polemic. See **Item A** in items doc.

---

## 4. 2 Cor 4:4 — ὁ θεὸς τοῦ αἰῶνος τούτου → **เทพเจ้าแห่งยุคนี้** — **DECIDE**

2 Cor 4:4 is the only NT verse where **ὁ θεός** (with the standard biblical-divine article-construction) is used of **Satan**:

- 4:4 GK: ἐν οἷς **ὁ θεὸς τοῦ αἰῶνος τούτου** ἐτύφλωσεν τὰ νοήματα τῶν ἀπίστων
- 4:4 TH: ในพวกเขานั้น **เทพเจ้าแห่งยุคนี้**ได้ทำให้ความคิดของผู้ที่ไม่เชื่อตาบอด

The translator applies the locked `pagan_deities_2026-04.md` rule ("พระเจ้า reserved for biblical God only; pagan/non-biblical-god references → เทพเจ้า") to the metaphorical "god of this age" reference. **เทพเจ้า** here functionally marks the same Christian/pagan boundary — the verse-internal contrast with v.6 ὁ θεὸς ὁ εἰπών (Gen 1:3 echo) → **พระเจ้าผู้ตรัสว่า** is preserved cleanly.

**Why this is DECIDE-worthy:** The pagan-deities doc is written for *literal* pagan deities (Acts 14 Zeus/Hermes; Acts 17 Athenian "gods"; Acts 19 Artemis). It does not explicitly cover NT *polemical / metaphorical* "god" references where Greek uses ὁ θεός of a non-biblical referent — Satan (2 Cor 4:4); the belly (Phil 3:19 ὧν ὁ θεὸς ἡ κοιλία); the antichrist (2 Thess 2:4 ὁ ἀντικείμενος καὶ ὑπεραιρόμενος ἐπὶ πάντα λεγόμενον θεόν). The translator extended the principle correctly, but the corpus-doc needs amendment to make the extension explicit. Most published Thai translations preserve **พระเจ้า** at 2 Cor 4:4 (e.g., THSV, TNCV) — Eremos's choice is a *minority but principled* reading. Worth Ben's confirmation + extension of the doc. See **Item B** in items doc.

---

## 5. 2 Cor 12:4 — παράδεισος → **เมืองบรมสุข** — **REVIEW**

2 Cor 12:4 is one of three NT παράδεισος occurrences (Luke 23:43; 2 Cor 12:4; Rev 2:7). Translator's renderings:

- 12:4 GK: ὅτι ἡρπάγη εἰς τὸν παράδεισον
- 12:4 TH: ว่าเขาถูกฉวยขึ้นไปยัง**เมืองบรมสุข**

Cross-corpus check at Luke 23:43 (already shipped):
- Luke 23:43 TH: วันนี้เจ้าจะอยู่กับเราใน**เมืองบรมสุขเกษม**

Both renderings use **บรมสุข** ("supreme bliss") — the key Buddhist-resonant element. **บรมสุข / สุขาวดี** is in Thai-Buddhist-cultural register the standard term for the Pure Land / heavenly destination, with strong Mahāyāna-Buddhist Amitābha-Pure-Land associations.

**The cultural-resonance question:** **เมืองบรมสุข** is theologically-correct AND culturally-engaged — Paul's third-heaven mystical experience lands in a Thai context where "supreme-bliss-realm" is a living religious category. But it imports a Buddhist eschatological referent into the Pauline text. Alternatives considered would be:
- **สวรรค์** (heaven; Christian-marked but generic)
- **สถานที่บรมสุข** (place-of-supreme-bliss; descriptive)
- **อุทยาน** (garden/park; literal, preserves the Greek παράδεισος = "walled garden, royal park" Persian-loanword sense)
- transliteration **พาราดีซัส**

The corpus is internally consistent (Luke 23:43 + 2 Cor 12:4 use the same root). Will recur Rev 2:7 (τοῦ παραδείσου τοῦ θεοῦ) — cross-corpus consistency required. See **Item C** in items doc.

---

## 6. ὑπερλίαν ἀπόστολοι at 11:5, 12:11 — sarcastic curly-quote — **REVIEW**

Paul's sarcastic-honorific reference to his opponents in Corinth — translator marks the sarcasm with **curly quotes**:

- 11:5 GK: μηδὲν ὑστερηκέναι τῶν ὑπερλίαν ἀποστόλων
- 11:5 TH: ข้าพเจ้าไม่ได้ด้อยกว่า **'อัครทูตชั้นยอด'** เหล่านั้นเลยแม้แต่น้อย
- 12:11 GK: οὐδὲν γὰρ ὑστέρησα τῶν ὑπερλίαν ἀποστόλων
- 12:11 TH: ข้าพเจ้าไม่ได้ด้อยกว่า **'อัครทูตชั้นยอด'** เหล่านั้นเลยแม้แต่น้อย

This **parallels the 1 Cor "Corinthian-slogan" curly-quote convention** (1 Cor 7:1, 8:4, 10:23 — see 1 Cor audit Item C). Both books mark *sarcastic Pauline embedded-quotation of the opponents' self-styling* with curly quotes — a consistent corpus convention worth formalizing into the doc that the 1 Cor audit recommended (`docs/translator_decisions/corinthian_slogan_quotemarks_2026-05.md`). The 2 Cor "super-apostles" is a stronger case because the **ὑπερλίαν** modifier itself is unambiguously sarcastic in Pauline usage. See **Item D** in items doc.

---

## 7. ἀρραβών τοῦ πνεύματος (1:22, 5:5) — **STABLE (undocumented; recommend brief new doc)**

ἀρραβών ("earnest, deposit, down-payment") is a Pauline distinctive — it occurs only in 2 Cor 1:22, 5:5 + Eph 1:14 in the NT:

| Verse | Greek | Thai |
|---|---|---|
| 1:22 | καὶ δοὺς τὸν ἀρραβῶνα τοῦ πνεύματος ἐν ταῖς καρδίαις ἡμῶν | **และทรงประทานพระวิญญาณเป็น**มัดจำ**ในใจของเรา** |
| 5:5 | ὁ δοὺς ἡμῖν τὸν ἀρραβῶνα τοῦ πνεύματος | **พระองค์ทรงเป็นผู้ประทานพระวิญญาณเป็น**มัดจำ**ให้แก่เรา** |

**มัดจำ** ("deposit, earnest, down-payment") is the Thai commercial idiom — exactly the Greek metaphor's source register (originally a Hebrew/Phoenician commercial-loanword in Greek). Lands precisely.

**Recommend: STABLE; brief new doc** `docs/translator_decisions/arrabon_deposit_2026-05.md` before Eph 1:14 (the third and final NT occurrence) — locks the rendering and notes the commercial-register fidelity.

---

## 8. διαθήκη παλαιά / καινή (3:6–18) — **STABLE (undocumented; recommend new doc — pre-Hebrews priority)**

2 Cor 3 is the densest NT διαθήκη theological-cluster outside Hebrews:

| Verse | Greek | Thai |
|---|---|---|
| 3:6 | διακόνους **καινῆς διαθήκης** | **ผู้รับใช้แห่ง**พันธสัญญาใหม่ |
| 3:14 | ἐπὶ τῇ ἀναγνώσει **τῆς παλαιᾶς διαθήκης** | **ในขณะอ่าน**พันธสัญญาเดิม |

**พันธสัญญา** ("bond / covenant") is the standard Thai Bible-tradition rendering. Cross-corpus consistent with Galatians 4:24 (δύο διαθῆκαι → **พันธสัญญาสองแบบ**). Note that **พันธสัญญาเดิม / ใหม่** are also the canonical Thai *names* for the Old/New Testament — translator preserves the deliberate Pauline pun (the Old/New Covenant theology IS the Old/New Testament canon-naming).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/diatheke_covenant_2026-05.md` before Hebrews (where διαθήκη occurs ~17×). The doc should:
1. Lock διαθήκη → **พันธสัญญา** (covenant)
2. Note παλαιά / καινή → **เดิม / ใหม่** (preserves the Old/New Testament canon-naming pun)
3. Lock μεσίτης διαθήκης → **คนกลางแห่งพันธสัญญา** (forward to Heb 8:6, 9:15, 12:24)
4. Cite 2 Cor 3:6, 14; Gal 4:24 as the locking precedents

---

## 9. διακονία / διάκονος cluster — **STABLE (split context-driven; recommend brief new doc)**

διακονία occurs ~12× in 2 Cor with a context-driven split:

| Sense | Thai | Examples |
|---|---|---|
| theological "ministry" (apostolic-vocation) | **พันธกิจ** | 3:7 ἡ διακονία τοῦ θανάτου → **พันธกิจแห่งความตาย**; 3:8 ἡ διακονία τοῦ πνεύματος → **พันธกิจแห่งพระวิญญาณ**; 4:1 τὴν διακονίαν ταύτην → **พันธกิจนี้**; 5:18 διακονίαν τῆς καταλλαγῆς → **พันธกิจแห่งการคืนดี** |
| concrete "service / aid" (collection-related) | **การรับใช้** | 8:4 τὴν κοινωνίαν τῆς διακονίας τῆς εἰς τοὺς ἁγίους → **การมีส่วนร่วมในการรับใช้ธรรมิกชน**; 9:1, 9:12, 9:13 διακονία (collection-context) → **การรับใช้** |
| concrete "serving" (verb / participle) | **ปรนนิบัติ** | 3:3 διακονηθεῖσα ὑφ' ἡμῶν → **ซึ่งเราได้ปรนนิบัติให้สำเร็จ** |

διάκονος → **ผู้รับใช้** uniformly (3:6, 6:4, 11:15, 11:23). The split is principled: theological-vocational sense (chs 3–6, where ministry = the Pauline apostolic vocation) gets **พันธกิจ**; concrete relief-service sense (chs 8–9, where it's the Jerusalem collection) gets **การรับใช้**. Reads cleanly.

**Recommend: STABLE; brief new doc** `docs/translator_decisions/diakonia_split_2026-05.md` before Romans 11:13, 12:7, 15:25, 15:31 (where the same split recurs — apostolic-vocation vs Jerusalem-collection-service) and the Pastorals (where διάκονος is the office-specific term). Should also note the still-untreated διάκονος-as-office question (deacon-office reading at Rom 16:1 Phoebe; Phil 1:1; 1 Tim 3:8, 12) — likely a future-Pastorals lock.

---

## 10. σκόλοψ τῇ σαρκί (12:7) — "thorn in the flesh" — **STABLE**

The iconic 12:7 phrase — translator preserves the literal Greek metaphor:

- 12:7 GK: ἐδόθη μοι σκόλοψ τῇ σαρκί, ἄγγελος Σατανᾶ, ἵνα με κολαφίζῃ
- 12:7 TH: จึงได้มี**หนาม**เข้ามาในเนื้อหนังของข้าพเจ้า เป็นทูตของซาตานเพื่อทรมานข้าพเจ้า

**หนาม** ("thorn / spike") preserves the Greek σκόλοψ literal-physical force (KJV/ESV/NIV "thorn"; some scholars argue "stake" given σκόλοψ's range). Theologically-neutral on the chronic-illness-vs-opposition-vs-Satan-attack interpretive question. Reads naturally in Thai.

**STABLE — no new doc needed.** Verse-level KD captures the rationale; iconic-phrase preservation aligns with 1 Cor's similarly-iconic preservations (e.g., σπείρεται σῶμα ψυχικόν / πνευματικόν).

---

## 11. Βελιάρ (6:15) — **STABLE (proper-name transliteration; first NT occurrence)**

2 Cor 6:15 is **the only NT occurrence of Βελιάρ** (= Belial, an OT/Second-Temple Jewish-literature title for Satan):

- 6:15 GK: τίς δὲ συμφώνησις Χριστοῦ πρὸς **Βελιάρ**
- 6:15 TH: พระคริสต์จะมีความสอดคล้องกับ**เบลีอัล**อย่างไร?

**เบลีอัล** is a clean transliteration following the proper-name principle (per `pagan_deities_2026-04.md` Rule 2, extended). The OT-Hebrew בְּלִיַּעַל ("worthlessness") source is preserved in name-form rather than translated. Aligns with Thai-Bible-tradition (THSV: เบลีอัล).

**STABLE — no new doc needed.** First and only NT occurrence; cross-corpus consistency not at risk. Worth a brief mention in the next aramaic_transliterations or proper-names amendment doc as a confirming case.

---

## 12. 5:21 "made him to be sin" — **STABLE (literal preservation of theologically-loaded phrase)**

2 Cor 5:21 is one of the most theologically-dense single verses in Paul. Translator preserves the literal Greek:

- 5:21 GK: τὸν μὴ γνόντα ἁμαρτίαν ὑπὲρ ἡμῶν ἁμαρτίαν ἐποίησεν, ἵνα ἡμεῖς γενώμεθα δικαιοσύνη θεοῦ ἐν αὐτῷ
- 5:21 TH: พระเจ้าทรงให้พระองค์ผู้ไม่ทรงรู้จักบาป**กลายเป็นบาป**เพื่อเรา เพื่อให้เราได้**กลายเป็นความชอบธรรมของพระเจ้า**ในพระองค์

**กลายเป็นบาป** ("become sin") is the literal Greek, NOT a softened "sin-offering" reading (which the Hebraic-idiom interpretation would produce). The chiasm "made-sin / become-righteousness-of-God" is preserved with parallel **กลายเป็น** verbs. Theologically-neutral on penal-substitutionary-vs-Hebraic-idiom-vs-mystical-exchange interpretive options — the Thai reader sees the Greek scandal of the chiasm without translator-embedded resolution.

**STABLE — no new doc needed.** Aligns with the project's Greek-fidelity philosophy; matches BSB/ESV/CSB. Worth flagging in any forward soteriological-vocabulary doc as a corpus-precedent for "preserve the Pauline theological-paradox without translator-resolution."

---

## 13. Inherited locks — **all compliant**

| Doc | 2CO evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 1:1, 8:1, 8:18, 8:19, 8:23, 8:24, 11:8, 11:28, 12:13 → **คริสตจักร** uniform. | **LOCKED** |
| `ethnos_2026-04.md` | 11:26 ἐξ ἐθνῶν → **คนต่างชาติ** (Gentile-mission category, correct). | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | Densely throughout 2 Cor → **องค์พระผู้เป็นเจ้า**, perfectly compliant — **fifth Pauline confirmation** that the doc's "Lukan signature" framing should be amended (already noted in JHN/GAL/1TH/1CO audits). | **LOCKED-with-amendment-needed** |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — no vocative κύριε in 2 Cor. | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | 9:13 δοξάζοντες τὸν θεὸν → **ถวายเกียรติแด่พระเจ้า** (uses ถวายเกียรติ instead of สรรเสริญ). The doc locks **สรรเสริญ** as the *single* Thai default for the praise-verb cluster (δοξάζω / εὐλογέω / αἰνέω) when the object is God. **Worth a quick check** — context here is participial "glorifying God *for* the obedience of your confession", which may license the variant ถวายเกียรติ ("ascribe glory to") rather than สรรเสริญ ("praise [vocally]"). Other 2 Cor δόξα-praise occurrences (1:20 πρὸς δόξαν → **เพื่อพระเกียรติสิริ**; 4:15 εἰς τὴν δόξαν → **เพื่อพระเกียรติของพระเจ้า**) use **พระเกียรติ** for the noun-form, which is consistent. | **LOCKED-with-spot-check** (9:13 ถวายเกียรติ vs สรรเสริญ — see Item E) |
| `honorifics_non_divine_authorities_2026-04.md` | 11:32 ἐθνάρχης Ἁρέτα τοῦ βασιλέως → **ผู้สำเร็จราชการของกษัตริย์อาเรทัส**. ἐθνάρχης not previously locked but rendered consistently with ἀνθύπατος/ἡγεμών pattern (plain register: ผู้สำเร็จราชการ). กษัτรย์ for βασιλεύς (ราชาศัพท์) — Aretas IV gets the king-honorific consistent with Herod/Agrippa lock. Compliant. | **LOCKED + minor extension** (ἐθνάρχης → ผู้สำเร็จราชการ) |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout (densely; παρακαλέω-of-God constructions all ทรง-prefixed); plain register for Σατανᾶς (2:11; 11:14; 12:7), Βελιάρ (6:15), opponents (11:13–15 ψευδαπόστολοι, διάκονοι αὐτοῦ — plain). Compliant. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | 1:20 ἀμήν → **อาเมน** (transliteration; OT-context Pauline doxology, not a Synoptic-saying-formula occurrence). Consistent with the 25× ἀμήν ἀμήν Johannine-transliteration policy at the lemma-level. | **LOCKED** |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A** — no Tier 1/2/3 inclusion variants in 2 Cor (no `output/textual_variants/2corinthians*` files; full text-scan confirmed). | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — 2 Cor is epistolary-rhetorical, not narrative; no historic-present pattern. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in 2 Cor (the 11:2 παρθένος-bride image is a brief simile, not a parable with a God-figure). | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | **THE LOCUS CLASSICUS** of the lock. 7:8 ἐλύπησα ... οὐ μεταμέλομαι → **ข้าพเจ้าก็ไม่เสียใจ**; 7:8 εἰ καὶ μετεμελόμην → **แม้ข้าพเจ้าจะเคยเสียใจมาก่อน**; 7:9 ἐλυπήθητε εἰς μετάνοιαν → **ความโศกใจได้นำพวกท่านสู่การกลับใจ**; 7:10 μετάνοιαν εἰς σωτηρίαν → **การกลับใจสู่ความรอด**; 12:21 μὴ μετανοησάντων → **ไม่ได้กลับใจ**. **The 7:8–10 contrast PRESERVES the lexical distinction in Thai** exactly as the doc anticipated (μεταμέλομαι → เสียใจ; μετάνοια → การกลับใจ). | **LOCKED — locus classicus confirmation** |
| `aphesis_forgiveness_of_sins_2026-04.md` | N/A — ἄφεσις absent from 2 Cor. (2:7 χαρίσασθαι "forgive" → **ให้อภัย**; 2:10 χαρίζομαι → **ให้อภัย** — distinct Pauline forgiveness-vocabulary, not the Synoptic ἄφεσις family.) | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | 4:4 ὁ θεὸς τοῦ αἰῶνος τούτου → **เทπเจ้าแห่งยุคนี้** (LOCK-EXTENSION; see §4 above + Item B); 6:16 εἰδώλων → **รูปเคารพ** (idol; locked from 1 Cor); 6:15 Βελιάρ → **เบลีอัล** (proper-name transliteration; see §11). | **LOCKED-with-extension-needed** (metaphorical-θεός case) |
| `roman_administrative_titles_2026-04.md` | 11:32 ἐθνάρχης Ἁρέτα → **ผู้สำเร็จราชการของกษัตริย์อาเรทัส** — extension from Roman-imperial to a client-king's appointee (Nabataean Aretas IV). Plain register preserved. Consistent. | **LOCKED + minor extension** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from 2 Cor. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (6:6, 13:13) → **พระวิญญาณบริสุทธิ์** uniform. Anthropological πνεῦμα (2:13 τῷ πνεύματί μου → **ในจิตวิญญาณของข้าพเจ้า**; 7:1 σαρκὸς καὶ πνεύματος → **เนื้อหนังและจิตวิญญาณ**; 7:13 τὸ πνεῦμα αὐτοῦ → **จิตวิญญาณของเขา**; 12:18 τῷ αὐτῷ πνεύματι → **จิตวิญญาณเดียวกัน**) all → **จิตวิญญาณ**. ψυχή at 1:23 + 12:15 → **ชีวิต** (sense (b), per locked rule). 4:16 ὁ ἔξω/ἔσω ἄνθρωπος ("outer / inner person") → **มนุษย์ภายนอก / ภายใน** — distinct Pauline anthropology (NOT a ψυχή/πνεῦμα contrast); compliant. | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | N/A — Pauline. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — no Jesus-direct-discourse in 2 Cor. (12:9 Christ's Ἀρκεῖ σοι ἡ χάρις μου ... → **'พระคุณของเราเพียงพอสำหรับเจ้า ...'** — quoted from a vision, single-occurrence; rendered with curly quotes + first-person divine-speech preserved.) | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries in 2 Cor. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | N/A — βασιλεία absent from 2 Cor. (5:20 πρεσβεύομεν "we are ambassadors" is a related metaphor but not the βασιλεία noun.) | **LOCKED (N/A)** |
| `ouranos_heaven_rendering_2026-04.md` | 5:1 ἐν τοῖς οὐρανοῖς → **ในฟ้าสวรรค์** (theological-default); 5:2 τὸ ἐξ οὐρανοῦ → **ที่อยู่ของเราซึ่งมาจากฟ้าสวรรค์**; 12:2 ἕως τρίτου οὐρανοῦ → **ฟ้าสวรรค์ชั้นที่สาม** (theological-default with ordinal); 12:5 (no οὐρανός; the third-heaven referent inherits 12:2's lock). All compliant. | **LOCKED** |
| `parousia_christou_2026-04.md` (proposed at 1TH audit; not yet written) | 2 Cor's παρουσία occurrences are **non-Christ-subject** (7:6, 7:7 of Titus → **การมาถึงของทิตัส**; 10:10 παρουσία τοῦ σώματος "bodily presence" → **การปรากฏตัวของเขาทางกาย**) — the corpus-internal split (Christ-เสด็จมา / non-Christ-มาถึง) is **already operational in 2 Cor** ahead of the corpus-doc being written. Compliant with proposed-but-unwritten lock. | **STABLE-pre-doc** (compliance ahead of doc-write) |
| `hagiasmos_hagiosune_2026-04.md` (proposed at 1TH audit; not yet written) | 7:1 ἁγιωσύνην → **ความบริสุทธิ์** (state-of-holiness, exactly per the proposed lock); 7:1 παντὸς μολυσμοῦ → **ทุกสิ่งที่ทำให้เป็นมลทิน** (impurity-binary-opposite). 1 Cor 1:30 / 6:11 ἁγιασμός already-locked-stably. Compliant. | **STABLE-pre-doc** |

---

## TODO — corpus decision docs (non-blocking; JIT before relevant downstream books)

Carrying forward from prior audits, plus new from 2 Corinthians:

1. `docs/translator_decisions/parousia_register_2026-04.md` — Christ-เสด็จมา / non-Christ-มาถึง split. **Confirmed by 2 Cor 7:6, 7:7, 10:10.** (Carried over.)
2. `docs/translator_decisions/anomia_lawlessness_2026-04.md` — ความอธรรม / คนอธรรม. (Carried over from 2TH.)
3. `docs/translator_decisions/aparche_firstfruits_2026-04.md` — ผลแรก. (Carried over from 1CO.)
4. `docs/translator_decisions/paradosis_synoptic_pauline_split_2026-04.md` — Synoptic ธรรมเนียม / Pauline คำสอนที่ส่งทอดมา + Col 2:8 caveat. (Carried over.)
5. `docs/translator_decisions/semeion_three_senses_2026-04.md` — miracle / authentication-mark / signal. **Confirmed by 2 Cor 12:12 (σημεῖα τοῦ ἀποστόλου = หมายสำคัญแห่งอัครทูต — apostolic-authentication sense locked; alongside σημεῖα + τέρατα + δυνάμεις cluster).** (Carried over.)
6. `docs/translator_decisions/glossolalia_languages_2026-05.md` — γλῶσσαι → ภาษา / ภาษาต่างๆ. (Carried over from 1CO.)
7. `docs/translator_decisions/eidolothyta_idol_meat_2026-05.md` — εἰδωλόθυτος → อาหารที่ถวายแก่รูปเคารพ. (Carried over from 1CO.)
8. `docs/translator_decisions/corinthian_slogan_quotemarks_2026-05.md` — convention for marking Pauline-quotation of opponents. **Confirmed and reinforced by 2 Cor 11:5, 12:11 ὑπερλίαν ἀπόστολοι → 'อัครทูตชั้นยอด' with curly quotes** (see §6 + Item D). (Carried over from 1CO; ready to write.)
9. `docs/translator_decisions/anastasis_resurrection_cluster_2026-05.md` — resurrection vocabulary. (Carried over from 1CO.)
10. **NEW** `docs/translator_decisions/paraklesis_paraklao_2026-05.md` — comfort/appeal split. **Trigger book:** Romans (12:1, 15:30 appeal cluster); Pastorals.
11. **NEW** `docs/translator_decisions/katallage_reconciliation_2026-05.md` — คืนดี for the καταλλαγή cluster. **Trigger book:** Romans 5:10–11; Eph 2:16; Col 1:20–22.
12. **NEW** `docs/translator_decisions/diatheke_covenant_2026-05.md` — พันธสัญญา + Old/New Testament canon-naming pun. **Trigger book:** Hebrews (~17 occurrences; high priority).
13. **NEW** `docs/translator_decisions/arrabon_deposit_2026-05.md` — มัดจำ for the πνεύματος-deposit metaphor. **Trigger book:** Ephesians 1:14.
14. **NEW** `docs/translator_decisions/diakonia_split_2026-05.md` — พันธกิจ (apostolic-vocation) / การรับใช้ (concrete service) split. **Trigger book:** Romans 15:25, 31; Pastorals (διάκονος-as-office question).

---

## Pre-existing docs to amend

- **`pagan_deities_2026-04.md`** — extend to cover NT polemical/metaphorical "god" references where Greek uses ὁ θεός of a non-biblical referent (Satan at 2 Cor 4:4; the belly at Phil 3:19; the antichrist at 2 Thess 2:4). **Rule extension to lock:** ὁ θεὸς-of-non-biblical-referent in NT polemical/metaphorical use → **เทพเจ้า** (preserves the "พระเจ้า reserved for biblical God only" boundary). See §4 + Item B.
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to "Lukan-Acts + Johannine + Pauline (Galatians + 1TH + 2TH + 1CO + 2CO)." Fifth-Pauline confirmation; the "Lukan-Acts signature" framing has fully outgrown its scope label.
- **`metanoeo_vs_metamelomai_2026-04.md`** — add 2 Cor 7:8–10 as the **locus-classicus-confirmation cite** (the doc was written anticipating this verse; 2 Cor's translation honored the lock exactly).

---

## Tagging eligibility

§1 mechanical gates clean. §2 internal review complete. §3 external AI review **PENDING** (packet ready for paste). §4 native-speaker / theological reviewer feedback **PENDING** (Items B + C are the strongest YAML candidates — they touch theology AND Thai cultural register).

**Tag `book-2corinthians-v1` is gated on:**

1. Ben's decision on **§4 / Item B** (DECIDE: extend `pagan_deities_2026-04.md` to cover Satan-as-θεός at 4:4; or revise the 4:4 rendering to **พระเจ้า**)
2. Ben's confirmation on **§5 / Item C** (REVIEW: παράδεισος → เมืองบรมสุข Thai-Buddhist-resonance — should it stand cross-corpus, or shift toward สวรรค์/อุทยาน)
3. Ben's confirmation on **§3 / Item A** (REVIEW: καυχάομαι universal **ภาคภูมิใจ** vs context-dependent **อวด** for pejorative passages)
4. Ben's confirmation on **§6 / Item D** (REVIEW: curly-quote convention for sarcastic embedded-quotation; confirms the 1 Cor-proposed `corinthian_slogan_quotemarks_2026-05.md`)
5. (Optional) Ben's spot-check on §13's δοξάζω at 9:13 (ถวายเกียรติ vs locked สรรเสริญ — Item E)
6. External AI sanity-check (§3) returned + reviewed
7. Five new translator_decisions docs (§§1, 2, 7, 8, 9 above — paraklesis, katallage, diatheke, arrabon, diakonia) considered for write before Romans / Hebrews / Eph compounds the editorial weight

The Pauline letters ahead (Romans next, then Eph, Phil, Col, 1–2 Tim, Tit, Phm) will compound the παράκλησις, καταλλαγή, διαθήκη, ἀρραβών, διακονία clusters quickly — writing those five docs **before Romans 5** will prevent forward drift in the most theologically-load-bearing Pauline vocabulary.
