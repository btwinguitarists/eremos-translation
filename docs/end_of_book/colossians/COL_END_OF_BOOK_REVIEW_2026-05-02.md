# Colossians — End-of-Book Review

**Date:** 2026-05-02
**Scope:** All 4 chapters (95 verses; ~290 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (36 docs).
**Trigger:** COL 4 shipped (commit `508da29`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 4/4 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-187-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` shows only the re-ran-check artifact (`key_term_consistency_all.md`) — no COL source-file dirt.
- **Colossians is the SECOND PRISON-EPISTLE the project has shipped** (after Philippians; the Captivity-Letters cluster: PHP, Eph, Col, PHM). At 95 verses the letter is short, dense, and **uniquely-Christological** — its load-bearing centerpiece is the COL 1:15–20 cosmic-Christ-hymn (the second Christological hymn the corpus has handled, after PHP 2:5–11). The letter also introduces two new clusters with major forward-impact: the **spiritual-beings hierarchy** (θρόνοι / κυριότητες / ἀρχαί / ἐξουσίαι at 1:16, 2:10, 2:15) and the **Pauline household-code (Haustafel)** at 3:18–4:1.
- **Cross-cutting Pauline-vocabulary inheritance verified compliant** with prior locks: ἐκκλησία → คริสตจักร (1:18, 1:24, 4:15, 4:16 — LOCKED ✓), ἀπόστολος → อัครทูต (1:1 — LOCKED ✓), ἀδελφοί → พี่น้อง (1:1, 1:2, 4:7, 4:9, 4:15 — LOCKED ✓), διάκονος → ผู้รับใช้ (1:7 of Epaphras; 1:23, 1:25 of Paul; 4:7 of Tychicus — LOCKED via `diakonos_pauline_2026-05.md`), ἅγιος → ธรรมิกชน when substantive (1:2, 1:4, 1:12, 1:26 — LOCKED, matches the corpus default), ἔθνος → คนต่างชาติ (1:27 — LOCKED via `ethnos_2026-04.md`), narrator-κύριος → องค์พระผู้เป็นเจ้า (15+ uses — LOCKED), πίστις-with-clear-object → objective genitive (1:4, 2:5 — LOCKED via `pistis_christou_2026-05.md`), φρονέω → คิด (3:2 imperative — LOCKED via `phroneo_pauline_2026-05.md`), στοιχεῖα τοῦ κόσμου → หลักการพื้นฐานของโลก (2:8, 2:20 — extends GAL 4:3 precedent).
- **The single most editorially-LOAD-BEARING item is the Colossians Christ-Hymn (1:15–20):** different-lexicon and different-theological-frame than PHP 2:5–11 (no μορφή / κενόω; instead εἰκών + πρωτότοκος + πᾶν τὸ πλήρωμα + ἀποκαταλλάσσω + αἷμα τοῦ σταυροῦ). The translator's COL 1:15 KD explicitly cites `christ_hymn_kenosis_2026-05.md`'s spirit ("validate the lock without mechanically importing PHP 2 vocabulary") and renders πρωτότοκος πάσης κτίσεως with **บุตรหัวปีเหนือสิ่งที่ทรงสร้างทั้งสิ้น** (using **เหนือ** "over", not **ของ** "of") to block the Arian / JW reading. **Recommend amending** the existing kenosis doc with a COL 1:15–20 sub-section + locking the cosmic-Christ vocabulary cluster (§1).
- **8 cross-cutting Pauline patterns are STABLE-but-undocumented at corpus level** (the cosmic-Christ-hymn vocabulary; the spiritual-beings 4-tier hierarchy; the σάρξ-polysemy with explicit RULES §5 flags; the πᾶν τὸ πλήρωμα + θεότης Christological-summary at 2:9; the ἀνταναπληρῶ + ὑστερήματα τῶν θλίψεων τοῦ Χριστοῦ at 1:24; the Pauline Haustafel; the χειρόγραφον τοῖς δόγμασιν cancelled-IOU metaphor at 2:14; the ταπεινοφροσύνη false-vs-true contextual split).
- **3 items flagged REVIEW** (the spiritual-beings 4-tier hierarchy renderings; the household-code ὑποτάσσω rendering; the COL 1:24 ἀνταναπληρῶ orthodox-vs-Catholic-Mass interpretation framing).
- **3 items flagged DECIDE** (the COL 1:15 πρωτότοκος rendering as **บุตรหัวปีเหนือ...** vs alternative anti-Arian formulations; the στοιχεῖα τοῦ κόσμου basic-principles vs elemental-spirits reading at 2:8 + 2:20 — Ben deferred the GAL recommendation; the θρησκεία τῶν ἀγγέλων subjective-vs-objective genitive at 2:18 — angel-WORSHIP vs angelic-WORSHIP).
- **External AI review (§3) pending** — items doc + packet built in this branch.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. The Colossians Christ-Hymn (1:15–20) — cosmic-Christ vocabulary cluster — **STABLE (extends `christ_hymn_kenosis_2026-05.md`; recommend doc amendment + new sub-section)**

The single most theologically load-bearing passage in the book. Where PHP 2:5–11 is **kenotic-incarnational** (descent + ascent of the pre-existent Son), COL 1:15–20 is **cosmic-creational** (Christ as image-of-God + creator-of-all + head-of-the-church + reconciler-of-the-cosmos). Different lexicon, different theological frame, but the same Pauline-evangelical-Protestant orthodoxy. The verse-level KDs render every doctrinally-loaded lemma with a **principled, evangelical-Protestant orthodox** rendering and the 1:15 KD explicitly invokes the existing kenosis doc's editorial principle.

| Greek (verse) | Thai | Editorial principle |
|---|---|---|
| **εἰκὼν** τοῦ θεοῦ τοῦ ἀοράτου (1:15) | **ฉายา**ของพระเจ้าผู้ที่ตามนุษย์ไม่อาจเห็นได้ | εἰκών = perfect-revelation-image (Son perfectly reveals Father), NOT photographic-likeness or shadow-reflection. Affirms full divine-revelation. |
| **πρωτότοκος** πάσης κτίσεως (1:15) | **บุตรหัวปี*เหนือ*สิ่งที่ทรงสร้างทั้งสิ้น** | Uses **เหนือ** ("over") not **ของ** ("of") — preserves rank-comparative, blocks the Arian / JW first-created reading. **DECIDE (§3)**. |
| ἐν αὐτῷ **ἐκτίσθη τὰ πάντα** ... δι' αὐτοῦ καὶ εἰς αὐτὸν ἔκτισται (1:16) | ในพระองค์ ทุกสิ่งได้ทรงถูกสร้างขึ้น ... ทุกสิ่งได้ทรงถูกสร้างขึ้นโดยทางพระองค์และเพื่อพระองค์ | Triple-prepositional Christological frame (ἐν / διά / εἰς) preserved. Christ as sphere + agent + goal of creation. |
| αὐτός ἐστιν **πρὸ πάντων** καὶ **τὰ πάντα ἐν αὐτῷ συνέστηκεν** (1:17) | พระองค์**ทรงดำรงอยู่ก่อนสรรพสิ่ง** และในพระองค์ ทุกสิ่ง**ดำรงอยู่ด้วยกัน** | πρό = temporal pre-existence (NOT spatial-above); συνέστηκεν perfect-tense = continuing-providential-cohesion. |
| αὐτός ἐστιν ἡ **κεφαλὴ τοῦ σώματος τῆς ἐκκλησίας** (1:18a) | พระองค์ทรงเป็น**ศีรษะของกาย คือ คริสตจักร** | head-and-body metaphor for Christ-church relation; ἐκκλησία → **คริสตจักร** locked. |
| **πρωτότοκος** ἐκ τῶν νεκρῶν (1:18b) | **บุตรหัวปี**จากในหมู่ผู้ตาย | Second πρωτότοκος brackets the hymn (creation + resurrection). Identical Thai rendering preserves the structural-parallel. |
| ἵνα γένηται ἐν πᾶσιν αὐτὸς **πρωτεύων** (1:18c) | เพื่อพระองค์เองจะทรง**เป็นที่หนึ่ง**ในทุกสิ่ง | NT-HAPAX πρωτεύω → **ทรงเป็นที่หนึ่ง**. Summarizes both halves of the hymn. |
| ἐν αὐτῷ εὐδόκησεν **πᾶν τὸ πλήρωμα** κατοικῆσαι (1:19) | พระเจ้าทรงพอพระทัยที่จะให้**ความบริบูรณ์ทั้งสิ้น**สถิตอยู่ในพระองค์ | πλήρωμα → **ความบริบูรณ์ทั้งสิ้น** (vs. Colossian-heresy distributing divinity across emanations). Implied subject (God) made explicit. |
| **ἀποκαταλλάξαι τὰ πάντα** εἰς αὐτόν (1:20a) | ให้**ทุกสิ่งคืนดี**กับพระองค์เอง | Intensified-compound ἀποκαταλλάσσω → **ให้ ... คืนดี**. Cosmic scope of reconciliation preserved. |
| **εἰρηνοποιήσας διὰ τοῦ αἵματος τοῦ σταυροῦ** αὐτοῦ (1:20b) | ทรงทำให้เกิด**สันติสุขผ่านโลหิตที่หลั่งบนกางเขน**ของพระองค์ | NT-HAPAX εἰρηνοποιέω → **ทำให้เกิดสันติสุข**. Cross-blood as historical-particular means with cosmic-universal effect. |
| εἴτε τὰ ἐπὶ τῆς γῆς εἴτε τὰ ἐν τοῖς οὐρανοῖς (1:20c) | ไม่ว่าสิ่งที่อยู่บนแผ่นดินโลกหรือสิ่งที่อยู่ในสวรรค์ | Heaven/earth merism order REVERSED from v.16 (chiastic-bracket). Preserved in Thai. |

**Editorial significance:** The COL hymn-cluster is the **counterpart** to the PHP hymn-cluster — same Christological doctrine, different vocabulary register. Where PHP made the descent–ascent move with kenotic verbs (κενόω, ταπεινόω, ὑπερυψόω), COL makes the cosmic-creator-and-reconciler move with image-and-firstborn nouns (εἰκών, πρωτότοκος ×2, πλήρωμα). The translator's restraint — explicitly NOT mechanically-importing PHP 2 lemma-renderings into COL 1:15–20 — is exactly the principle the kenosis doc lays out ("validate the lock without mechanically importing PHP 2 vocabulary").

**Recommend: STABLE; amend `docs/translator_decisions/christ_hymn_kenosis_2026-05.md`** with a new **§ "Colossians 1:15–20: cosmic-Christ vocabulary"** sub-section that:
1. Locks εἰκών (Christ-as-image-of-God context) → **ฉายา**
2. Locks πρωτότοκος (Christ-as-rank-precedent context, with κτίσεως or ἐκ τῶν νεκρῶν) → **บุตรหัวปี** + the rank-marker **เหนือ** (NOT possessive **ของ**) when the genitive is comparative
3. Locks πλήρωμα (Christological-fullness context, COL 1:19, 2:9; Eph 1:23 forward) → **ความบริบูรณ์ทั้งสิ้น**
4. Locks ἀποκαταλλάσσω → **ให้คืนดี** (Pauline-cosmic-reconciliation contexts)
5. Locks εἰρηνοποιέω → **ทำให้เกิดสันติสุข**
6. Locks πρωτεύω → **ทรงเป็นที่หนึ่ง**
7. Cross-references the parallel high-Christology passages already-noted in the kenosis doc (Heb 1:1–4 ἀπαύγασμα τῆς δόξης / χαρακτὴρ τῆς ὑποστάσεως; Eph 1:20–23; 1 Pet 3:18–22; Rev 5:9–14) as still-pertinent — COL provides the SECOND Pauline locking-precedent for cosmic-high-Christology

---

## 2. πρωτότοκος (1:15, 1:18) — anti-Arian rendering with **เหนือ** — **DECIDE before tagging**

The single most-attacked verse in the book in cult-vs-orthodox debates: COL 1:15 πρωτότοκος πάσης κτίσεως. Two readings dominate:

| Reading | Claim | Translation logic |
|---|---|---|
| **(a) Rank-comparative** ("firstborn-OVER-all-creation, supreme over all created things") — *currently chosen* | πρωτότοκος is a Hebrew-Bible idiom for rank/preeminence (cf. Ps 89:27 LXX πρωτότοκον θήσομαι αὐτόν "I will make him firstborn"). Christ is the supreme-One over all creation, NOT a created being. | πάσης κτίσεως is genitive-of-comparison/rank, NOT partitive. |
| **(b) Partitive** ("firstborn-OF-all-creation, the first thing created among all creation") | The genitive is partitive: Christ is the first creature, ranking with creation. | The classic Arian / Jehovah's Witnesses NWT reading. |

**Current Thai rendering** uses **บุตรหัวปีเหนือสิ่งที่ทรงสร้างทั้งสิ้น** — explicitly **เหนือ** ("over") instead of **ของ** ("of"):

> COL 1:15 GK: ὅς ἐστιν εἰκὼν τοῦ θεοῦ τοῦ ἀοράτου, **πρωτότοκος πάσης κτίσεως**
> TH: พระบุตรทรงเป็นฉายาของพระเจ้าผู้ที่ตามนุษย์ไม่อาจเห็นได้ ทรงเป็น**บุตรหัวปีเหนือสิ่งที่ทรงสร้างทั้งสิ้น**

The 1:15 KD explicitly names the choice + cites v.16 (Christ-as-creator) as immediate confirmation that the partitive-Arian reading is incoherent. The 1:15 thai_summary further unpacks the orthodox interpretation for Thai readers.

**Editorial assessment:** The choice is doctrinally orthodox + grammatically defensible (πρωτότοκος + genitive-of-rank is well-attested in LXX). Mainstream evangelical English Bibles (NIV / ESV / CSB / BSB) all preserve the literal "firstborn of all creation" + rely on context + reader-knowledge to block the Arian reading. The Thai project's choice to encode the rank-reading lexically (with **เหนือ**) is **MORE explicit than any of the major English Bibles** — which is a defensible CC0 evangelical choice (lexically blocks cult mis-readings) but does add an interpretive step beyond the bare Greek.

**DECIDE before tagging:**
1. Confirm Ben endorses **บุตรหัวปีเหนือสิ่งที่ทรงสร้างทั้งสิ้น** (with **เหนือ**) as the corpus-default for Christ-as-πρωτότοκος contexts. The lemma recurs at COL 1:18 ἐκ τῶν νεκρῶν (locked here as **บุตรหัวปีจากในหมู่ผู้ตาย**), Rom 8:29 (πρωτότοκον ἐν πολλοῖς ἀδελφοῖς), Heb 1:6 (the πρωτότοκος brought into the world, Christ-as-firstborn-Son), Heb 12:23 (πρωτοτόκων plural — believers), and Rev 1:5 (πρωτότοκος τῶν νεκρῶν).
2. Alternative: render literal **บุตรหัวปีของสิ่งที่ทรงสร้างทั้งสิ้น** (with **ของ**, matching English "of") + add a footer-note + rely on context — which would be more lexically-bare but less anti-Arian-explicit.

**→ Recommend new doc:** `docs/translator_decisions/prototokos_pauline_2026-05.md` (brief — ~5 NT occurrences) — locks the **บุตรหัวปี + เหนือ-vs-ของ** distinction by sense (rank-comparative-of-creation: **เหนือ**; partitive-of-the-dead: **จากในหมู่**; relational-of-believers: **ในหมู่**). Cite COL 1:15 as the locking precedent + name the Arian / JW reading as the alternative considered + rejected. Important pre-Heb 1:6 + Rev 1:5.

---

## 3. στοιχεῖα τοῦ κόσμου (2:8, 2:20) — basic-principles vs elemental-spirits — **DECIDE before tagging (the long-deferred GAL question)**

The GAL audit (§4, 2026-04-30) flagged this as a corpus-priority lift recommendation: "Recommend new doc `docs/translator_decisions/stoicheia_tou_kosmou_2026-04.md` to lock หลักการ as the corpus-wide rendering ... Important pre-Col 2 handoff." The doc was **never written**. Now COL has shipped using the GAL precedent (**หลักการพื้นฐานของโลก**), and the question recurs in a context that **some commentators argue more naturally requires reading (3) "elemental spirits"**:

| Verse | Greek | Thai |
|---|---|---|
| COL 2:8 | διὰ τῆς φιλοσοφίας καὶ κενῆς ἀπάτης κατὰ τὴν παράδοσιν τῶν ἀνθρώπων, **κατὰ τὰ στοιχεῖα τοῦ κόσμου** | ด้วยปรัชญาและการล่อลวงอันว่างเปล่า ตามประเพณีของมนุษย์ **ตามหลักการพื้นฐานของโลก** |
| COL 2:20 | εἰ ἀπεθάνετε σὺν Χριστῷ **ἀπὸ τῶν στοιχείων τοῦ κόσμου** | ถ้าพวกท่านได้ตายร่วมกับพระคริสต์เพื่อพ้นจาก**หลักการพื้นฐานของโลก**แล้ว |

The 2:8 KD explicitly notes: "Per uW + Col-FRONT: ambiguous between (1) basic-elementary-principles, (2) spiritual-elemental-beings (cosmic-powers worshipped in pagan religion). The Thai rendering preserves both readings."

**Editorial assessment of the COL context:** The Christ-vs-cosmic-powers polemic in chapter 2 is densely-elemental: 2:10 (Christ is head over πάσης ἀρχῆς καὶ ἐξουσίας — every spiritual-rule-and-authority); 2:15 (Christ disarmed-and-paraded τὰς ἀρχὰς καὶ τὰς ἐξουσίας); 2:18 (the false-teachers practice θρησκείᾳ τῶν ἀγγέλων — angel-worship, see §10); 2:20 immediately after recapitulating Christ-vs-the-στοιχεῖα. The **chapter's own internal evidence** leans toward reading (3) elemental-spirits more strongly than GAL 4:3–9 did. The GAL-precedent **หลักการพื้นฐานของโลก** is preserved (corpus-consistency win) but at the price of obscuring the elemental-spirits intertext that COL 2 depends on.

**DECIDE before tagging:**
1. Confirm Ben endorses **หลักการพื้นฐานของโลก** as corpus-permanent (option 1: basic-principles; matching BSB/ESV/NIV/CSB majority). Strong pro: corpus-consistency with already-shipped GAL.
2. OR: shift to **อำนาจครอบงำของโลก** ("dominating-powers of the world") or **อำนาจฝ่ายโลก** ("worldly powers") to push COL toward reading (3) — but this would create back-incompatibility with shipped GAL 4:3, 4:9. Likely too costly to revisit.
3. EITHER WAY — finally write the deferred corpus doc `docs/translator_decisions/stoicheia_tou_kosmou_2026-05.md` (the GAL audit's recommended `2026-04.md` filename was for a doc that never landed; bumping to `2026-05.md` matches the actual write-date). Lock the chosen reading + name the alternatives + cite both GAL 4:3 and COL 2:8 as locking precedents.

---

## 4. πᾶν τὸ πλήρωμα τῆς θεότητος σωματικῶς (2:9) — the most-condensed Christological statement in the NT — **STABLE (gets locked into the kenosis-doc amendment per §1)**

COL 2:9 is the most-condensed full-divinity-and-full-humanity affirmation in the NT — packed with two NT-HAPAXES (θεότης + σωματικῶς):

> ὅτι ἐν αὐτῷ κατοικεῖ **πᾶν τὸ πλήρωμα τῆς θεότητος σωματικῶς**
> เพราะในพระคริสต์ **ความบริบูรณ์ทั้งสิ้นของพระเจ้าสถิตอยู่ในรูปกาย**

| Greek | Thai | Editorial principle |
|---|---|---|
| πᾶν τὸ **πλήρωμα** | **ความบริบูรณ์ทั้งสิ้น** | Same lemma + same Thai as 1:19. Anti-Colossian-heresy: full-divinity in Christ, NOT divided across angelic-mediators. |
| τῆς **θεότητος** (NT-HAPAX) | **ของพระเจ้า** | θεότης = "deity, godhood, the-essence-of-being-God" (distinct from cognate θειότης at Rom 1:20 = "divinity-attributes"). Rendered as the simple genitive **ของพระเจ้า** + the **ทั้งสิ้น** quantifier preserves the πᾶν-τὸ-πλήρωμα fullness-claim. |
| **σωματικῶς** (NT-HAPAX) | **ในรูปกาย** | "Bodily, in bodily form." Cognate σωματικός at LUK 3:22 → **เป็นรูปกาย**. Anti-docetic: full divinity in the historical-physical-Christ. |

The 2:9 KD names the principle: "Two HAPAX in one verse: θεότης + σωματικῶς. The most-condensed Christological-statement in the NT — full-divinity (vs Colossian-heresy distributing divinity among emanations) + full-humanity (vs docetism)."

**Editorial assessment:** The translator made a deliberate choice **not** to introduce a distinct lemma for θεότης (e.g., **ความเป็นพระเจ้า** "the-divinity-essence"), instead leaning on the contextual force of πᾶν τὸ πλήρωμα + ทั้งสิ้น to do the semantic-load. This is principled: the simpler genitive **ของพระเจ้า** reads naturally in Thai while the **ทั้งสิ้น** quantifier preserves the all-fullness claim. **STABLE.** Worth folding into the kenosis-doc amendment per §1 as a sub-bullet.

---

## 5. The spiritual-beings 4-tier hierarchy (1:16, 2:10, 2:15) — **REVIEW (high forward-impact into Eph 1:21, 6:12)**

COL 1:16 lists four classes of spiritual-beings in a polemical-cosmological context (the chapter's claim: ALL spiritual-beings are Christ's creatures, NOT co-equal-objects-of-veneration like the false-teachers' angel-worship). The translator chose **four distinct Thai terms** preserving the hierarchical-distinctions:

| Greek (1:16) | Thai | Sense |
|---|---|---|
| θρόνοι | **บัลลังก์** | thrones (literal — heavenly thrones / throne-occupying powers) |
| κυριότητες | **เทพผู้ครอง** | dominions / lordly-powers (divine-status spiritual-rulers) |
| ἀρχαί | **ทูตสวรรค์ผู้มีอำนาจ** | rulers (powerful angels — the lemma also = principalities / governing-spirits) |
| ἐξουσίαι | **ผู้ทรงสิทธิ** | authorities (those-with-rightful-power) |

The cluster recurs collapsed-to-pair at 2:10 (πάσης ἀρχῆς καὶ ἐξουσίας → **ผู้ครองและผู้ทรงอำนาจทั้งสิ้น**) and 2:15 (τὰς ἀρχὰς καὶ τὰς ἐξουσίας → **ผู้ครองและผู้ทรงอำนาจ**). The collapsed-pair renderings are slightly-different (**ผู้ครอง** "ruler" not the longer **ทูตสวรรค์ผู้มีอำนาจ**) — context determines whether the angelic-specifically (1:16) or the generic-rulership (2:10, 2:15) sense is foregrounded.

**Editorial assessment:** The 4-tier rendering at 1:16 is bold and informative — it gives Thai readers explicit-lexical-access to the angelic-hierarchy categories that the Colossian-heresy was venerating. The slight inconsistency of **ทูตสวรรค์ผู้มีอำนาจ** at 1:16 vs **ผู้ครอง** at 2:10/2:15 (same lemma ἀρχή) is principled (different polemical contexts) but worth acknowledging.

**REVIEW flag:** Confirm that:
1. The 4-tier rendering at 1:16 is the right register for Thai-evangelical readers (not too-baroque, not too-flat). Alternative: simplify to 2-pair (rule + authority) matching English "thrones or dominions or rulers or authorities" lexical-distinctness?
2. The contextual-shift between 1:16 ἀρχαί → **ทูตสวรรค์ผู้มีอำนาจ** and 2:10/2:15 ἀρχαί → **ผู้ครอง** is principled — same lemma rendered differently in different polemical contexts. Worth a verse-level cross-reference note?

**Forward-pertinent:** Eph 1:21 (πάσης ἀρχῆς καὶ ἐξουσίας καὶ δυνάμεως καὶ κυριότητος — three of the four COL terms recur + add δύναμις); Eph 3:10 (ταῖς ἀρχαῖς καὶ ταῖς ἐξουσίαις); Eph 6:12 (ἀρχάς + ἐξουσίας + κοσμοκράτορας τοῦ σκότους + πνευματικὰ τῆς πονηρίας); 1 Pet 3:22 (ἀγγέλων καὶ ἐξουσιῶν καὶ δυνάμεων); Rom 8:38–39 (ἄγγελοι + ἀρχαί + δυνάμεις). Locking the COL rendering now (or formally affirming the existing renderings as a glossary cluster) prevents drift.

**→ Recommend: optional new doc** `docs/translator_decisions/spiritual_beings_hierarchy_2026-05.md` (brief) — locks the 4-tier rendering + the 2-pair collapsed-context rendering + names the parallel passages.

---

## 6. ἀνταναπληρῶ + τὰ ὑστερήματα τῶν θλίψεων τοῦ Χριστοῦ (1:24) — **REVIEW (orthodox-vs-Catholic-Mass framing)**

Probably the most-difficult-to-translate verse in the book theologically. COL 1:24:

> Νῦν χαίρω ἐν τοῖς παθήμασιν ὑπὲρ ὑμῶν, καὶ **ἀνταναπληρῶ τὰ ὑστερήματα τῶν θλίψεων τοῦ Χριστοῦ** ἐν τῇ σαρκί μου ὑπὲρ τοῦ σώματος αὐτοῦ, ὅ ἐστιν ἡ ἐκκλησία
> บัดนี้ ข้าพเจ้าชื่นชมยินดีในความทุกข์ที่ทนเพื่อพวกท่าน และข้าพเจ้าก็**เติมเต็มในเนื้อหนังของข้าพเจ้า ในสิ่งที่ยังขาดอยู่ในความทุกข์ของพระคริสต์** เพื่อกายของพระองค์ คือ คริสตจักร

The Thai preserves the literal "fill-up what is lacking in Christ's afflictions in my flesh." The 1:24 KD names the two-readings problem explicitly: "NOT 'Christ's-atonement was insufficient' — the lack refers to 'what Christ-intentionally-left for-his-disciples-to-suffer-as-his-body.'" The 1:24 thai_summary handles the orthodox-vs-Catholic-Mass-of-merits interpretive question explicitly.

The lemma ἀνταναπληρόω is a NT-HAPAX (compound: ἀντί + ἀνά + πληρόω = "fill-up-in-turn / fill-up-on-behalf-of"). The Thai **เติมเต็ม** preserves the filling-up sense; the orthodox interpretation rides on the thai_summary disambiguation rather than on the verse-translation itself.

**Editorial assessment:** This is the project's first encounter with a Pauline statement that has been **historically used as a proof-text for Catholic merit-of-the-saints theology** (and rejected by Reformation-evangelical scholarship as misreading the lemma). The Thai translation choice is principled — render literally, disambiguate in summary. But the question of whether the Thai-reader-without-summary access could mistake the rendering for the Catholic-interpretation deserves Ben's confirmation.

**REVIEW flag:** Confirm that:
1. The literal **เติมเต็ม ... ในสิ่งที่ยังขาดอยู่ในความทุกข์ของพระคริสต์** is the right rendering for an evangelical-Protestant CC0 Thai Bible — relying on the thai_summary to block the Catholic-interpretation.
2. Alternative (more interpretive): render **เติมเต็มความทุกข์ที่พระคริสต์ทรงประทานให้ข้าพเจ้าทนเพื่อกายของพระองค์** ("fill up the sufferings Christ allotted me to endure for his body") — explicitly orthodox, but interpretively-stronger than the Greek itself.

The verse will likely surface in any external-AI review — worth surfacing it for Ben + the external-AI sanity check.

---

## 7. σάρξ polysemy with explicit RULES §5 flags — **STABLE (the COL pattern is exemplary; consider doc-extension)**

COL has **8 σάρξ occurrences across 7 verses**, with the translator explicitly tagging each with the RULES §5 polysemy flag. The pattern divides cleanly into two senses:

| Sense | Verse | Greek context | Thai |
|---|---|---|---|
| **Neutral physical-presence / earthly realm** | 2:1 | οὐχ ἑόρακαν τὸ πρόσωπόν μου ἐν σαρκί | (paraphrased — "ยังไม่เคยเห็นหน้าข้าพเจ้าด้วยตนเอง") |
| | 2:5 | τῇ σαρκὶ ἄπειμι | **ทางกาย** |
| | 2:13 | τῇ ἀκροβυστίᾳ τῆς σαρκὸς ὑμῶν | **ทางเนื้อหนัง** (literal-physical-uncircumcision) |
| | 3:22 | τοῖς κατὰ σάρκα κυρίοις | **นายของตนตามฝ่ายเนื้อหนัง** (earthly-masters distinction) |
| **Moral / sinful-nature** | 2:11 | τῇ ἀπεκδύσει τοῦ σώματος τῆς σαρκός | **ร่างกายฝ่ายเนื้อหนัง** (the sinful-nature) |
| | 2:18 | ὑπὸ τοῦ νοὸς τῆς σαρκὸς αὐτοῦ | **จิตใจฝ่ายเนื้อหนัง** (carnal-mindedness) |
| | 2:23 | πρὸς πλησμονὴν τῆς σαρκός | **การตามใจของฝ่ายเนื้อหนัง** (flesh-indulgence) |
| **Christ's earthly-physical body (distinct sub-sense)** | 1:22 | ἐν τῷ σώματι τῆς σαρκὸς αὐτοῦ | **พระวรกายฝ่ายเนื้อหนัง** (Christ's pre-resurrection physical body; royal-pระ- prefix) |

Every moral-σάρξ KD includes "POLYSEMOUS σάρξ flag (RULES §5)" — exemplary translator-discipline. The 1:22 use is distinctive (Christ's earthly-physical body, royal-prefixed **พระวรกาย** because of the divine-subject) — a third sub-sense the GAL audit (§6) didn't isolate.

**Editorial assessment:** COL's σάρξ-handling is **the strongest σάρξ polysemy-management in the corpus to date**. The translator's explicit RULES §5 flagging discipline is exactly what the GAL audit (§6) recommended could be lifted to a corpus doc. The 1:22 royal-prefixed **พระวรกายฝ่ายเนื้อหนัง** for Christ's-earthly-body is a principled extension that the existing JHN doc + GAL doc don't cover.

**Recommend: STABLE; finally lift to corpus doc** `docs/translator_decisions/sarx_pauline_2026-05.md` (the GAL audit's recommended `2026-04.md` filename was for a doc that never landed; bumping to `2026-05.md` matches the actual write-date). The doc should:
1. Lock σάρξ → **เนื้อหนัง / กาย** (single-rendering policy across all senses) per the GAL audit's analysis
2. Lock the **POLYSEMOUS σάρξ (RULES §5)** verse-level flagging discipline that COL exemplifies
3. Distinguish three sub-senses + their Thai-disambiguating qualifiers: neutral-bodily (**ทางกาย / ทางเนื้อหนัง**), moral (**ฝ่ายเนื้อหนัง**), Christ's-physical-body (**พระวรกายฝ่ายเนื้อหนัง** — royal-prefixed)
4. Cite COL 2 + GAL 5 as the locking precedents (both shipped, both compliant)
5. Forward-pertinent: Romans 7–8 will compound σάρξ density dramatically; this lock should be in place before Rom 7:5 ships

---

## 8. The Pauline household-code / Haustafel (3:18–4:1) — **REVIEW (first Pauline-Haustafel in corpus; sensitive contemporary reception)**

COL 3:18–4:1 is the project's **first Pauline-Haustafel** (household-code / Greek-Roman household-ethics-tradition Christianized). Six imperatives across six relational-pairs:

| Verse | Greek | Thai |
|---|---|---|
| 3:18 | Αἱ γυναῖκες, **ὑποτάσσεσθε** τοῖς ἀνδράσιν, ὡς ἀνῆκεν ἐν κυρίῳ | ภรรยาทั้งหลาย จง**ยอมอยู่ใต้บังคับ**สามีของตน เพราะเป็นการเหมาะสมในองค์พระผู้เป็นเจ้า |
| 3:19 | οἱ ἄνδρες, **ἀγαπᾶτε** τὰς γυναῖκας καὶ μὴ πικραίνεσθε πρὸς αὐτάς | สามีทั้งหลาย จง**รัก**ภรรยาของตน และอย่าโกรธขึ้งใส่พวกเธอ |
| 3:20 | Τὰ τέκνα, **ὑπακούετε** τοῖς γονεῦσιν κατὰ πάντα | บุตรทั้งหลาย จง**เชื่อฟัง**บิดามารดาของตนในทุกสิ่ง |
| 3:21 | οἱ πατέρες, **μὴ ἐρεθίζετε** τὰ τέκνα ὑμῶν, ἵνα μὴ ἀθυμῶσιν | บิดาทั้งหลาย อย่า**ยั่วยุ**บุตรของท่าน เพื่อพวกเขาจะไม่ท้อใจ |
| 3:22 | οἱ δοῦλοι, **ὑπακούετε** κατὰ πάντα τοῖς κατὰ σάρκα κυρίοις | ทาสทั้งหลาย จง**เชื่อฟัง**นายของตนตามฝ่ายเนื้อหนังในทุกสิ่ง |
| 4:1 | οἱ κύριοι, τὸ δίκαιον καὶ τὴν ἰσότητα τοῖς δούλοις **παρέχεσθε** | นายทั้งหลาย จง**ปฏิบัติต่อ**ทาสของท่านอย่างยุติธรรมและเสมอภาค |

The 3:18 KD names the principle: "Reciprocal-Pauline pattern: wives submit + husbands love (v.19) — both governed by 'in the Lord.' Note: the imperative is middle-voice 'submit-yourselves,' not passive 'be-submitted.'" The 3:18 thai_summary frames the genre.

**Editorial assessment:** All six renderings are principled and corpus-precedent-aligned (ὑποτάσσω → **ยอมอยู่ใต้บังคับ** matches LUK 10:17, 1Co 14:32; ὑπακούω → **เชื่อฟัง** matches Eph 6:1; the **ในองค์พระผู้เป็นเจ้า / ฝ่ายเนื้อหนัง** qualifiers preserve the Pauline-Christianizing-of-Greek-Roman-norms move). The **paternal πατήρ → บิดา** (plain register, NOT royal **พระบิดา**) at 3:21 is correct — this is a human-paternal analogy parallel to GAL 4:2's Greco-Roman household-father (per `narrator_vs_character_voice_2026-04.md` lock).

**REVIEW flag:** The Pauline-Haustafel is among the **most-debated passages in modern Christian-ethics discourse** (egalitarian-vs-complementarian debate; mutual-submission readings of Eph 5:21–33 vs hierarchical readings; reception of the slave-master code post-abolition). Modern Thai readers will bring contemporary register-expectations:
1. Confirm **ยอมอยู่ใต้บังคับ** ("submit-yourself-under-control") at 3:18 is the right register for evangelical-Thai readers — vs. softer **ยอมอยู่ในความดูแล** ("place-yourself-in-the-care-of") that some egalitarian-leaning translations might prefer. The corpus-precedent (LUK 10:17, 1Co 14:32) where ὑποτάσσω is rendered the same way is doctrinally-load-bearing — changing the COL rendering would create a corpus-inconsistency.
2. Confirm **ทาสทั้งหลาย จงเชื่อฟังนายของตน** ("slaves, obey your masters") at 3:22 is the right rendering for Thai-evangelical-historical-context (Thailand abolished slavery in 1905; modern Thai readers may read this passage with abolitionist-anachronism). Footer-note acknowledging the historical-cultural context vs the timeless-principle of "serving Christ through earthly-work" (the 3:23 thai_summary's framing)?

**Forward-pertinent:** Eph 5:22–6:9 is the EXPANDED parallel-Haustafel (especially the much-longer husbands-love-as-Christ-loved-the-church section); 1 Tim 2:8–15 + 6:1–2; Tit 2:1–10; 1 Pet 2:18–3:7 — all will recur the Haustafel-vocabulary. The COL lock + Ben's confirmation here sets the corpus-default for the entire Pauline + Petrine codes.

**→ Recommend: STABLE**, no new doc needed pre-tagging; the per-verse renderings are corpus-precedent-aligned. But Ben's confirmation here is **forward-load-bearing** (Eph 5–6 will expand the wife-husband section threefold).

---

## 9. χειρόγραφον τοῖς δόγμασιν (2:14) — cancelled-IOU metaphor — **STABLE**

COL 2:14 contains the most-vivid forensic-juridical metaphor for the cross in the NT — packed with two NT-HAPAXES (χειρόγραφον + προσηλόω):

> ἐξαλείψας **τὸ καθ' ἡμῶν χειρόγραφον τοῖς δόγμασιν** ὃ ἦν ὑπεναντίον ἡμῖν, καὶ αὐτὸ ἦρκεν ἐκ τοῦ μέσου **προσηλώσας αὐτὸ τῷ σταυρῷ**
> พระองค์ทรงลบล้าง**เอกสารหนี้ที่ปรับโทษเรา ซึ่งเป็นบัญชีที่ขัดแย้งกับเรา** และทรงเอามันออกจากระหว่างกลาง โดย**ตรึงมันไว้ที่กางเขน**

The Thai **เอกสารหนี้** ("debt-document") preserves the Greco-Roman commercial χειρόγραφον = an IOU / certificate of debt signed by the debtor. The **ตรึง ... ไว้ที่กางเขน** ("nail to the cross") preserves the προσηλόω metaphor. The 2:14 thai_summary makes the commercial-legal imagery accessible to Thai readers.

**Editorial assessment:** Both NT-HAPAXES rendered with vivid + culturally-translatable Thai. The forensic-juridical force is preserved. **STABLE** ✓ — no action.

---

## 10. θρησκεία τῶν ἀγγέλων (2:18) — subjective vs objective genitive — **DECIDE before tagging**

COL 2:18 contains a famous interpretive-crux genitive that determines the polemical-target:

> μηδεὶς ὑμᾶς καταβραβευέτω θέλων ἐν ταπεινοφροσύνῃ καὶ **θρησκείᾳ τῶν ἀγγέλων**
> อย่าให้ผู้ใดตัดสิทธิ์รางวัลของพวกท่าน ผู้ที่หลงใหลในความถ่อมใจจอมปลอมและ**การนมัสการทูตสวรรค์**

Two readings hinge on the genitive's function:

| Reading | Claim | Polemical target |
|---|---|---|
| **(a) Objective genitive** ("worship OFFERED-TO angels") — *currently chosen* | The false-teachers worship angels themselves; Paul rebukes angel-veneration. Traditional / mainstream-evangelical reading (KJV / NIV / ESV / CSB / BSB). | The Colossian-heresy includes pagan-style angel-veneration. |
| **(b) Subjective genitive** ("worship OFFERED-BY angels" — i.e., the visionary-mystic claims to join the angelic-heavenly-worship) | The false-teachers claim to participate-in / observe heavenly-worship through visionary-mystical experiences (cf. v.18 ἃ ἑόρακεν ἐμβατεύων "entering-into what he has seen"). Increasingly favored in modern scholarship (Fred Francis 1962-classic study; Lincoln; Dunn). | The Colossian-heresy is mystical-Jewish-apocalyptic visionary-piety, not pagan angel-cult. |

**Current Thai rendering** **การนมัสการทูตสวรรค์** ("the worship-of angels") is the literal objective-genitive reading. The 2:18 KD names the false-teachers' "angel-veneration" as the polemical target; this aligns with reading (a).

**Editorial assessment:** Reading (a) is the safer-evangelical-default + matches mainstream English Bibles. Reading (b) is increasingly the academic-consensus and is supported contextually by 2:18b (ἃ ἑόρακεν ἐμβατεύων + φυσιούμενος "puffed-up by his fleshly mind") + 2:23 (ἐθελοθρησκίᾳ "self-imposed-worship"). Thai **การนมัสการทูตสวรรค์** could be read either way (the Thai genitive ของ-construction is ambiguous on subjective-vs-objective just as Greek is) — but reader-default will resolve to (a) angel-worship without explicit context.

**DECIDE before tagging:**
1. Confirm Ben endorses reading (a) [angel-veneration] as the corpus-default + accepts the slight-loss of academic-consensus reading (b) [visionary-mystical-piety]. Consequence: simple Thai rendering preserved; modern Thai reader gets the traditional polemical-target.
2. OR: shift to a more-explicit visionary-mystical rendering — e.g., **การร่วมในการนมัสการของทูตสวรรค์** ("joining-in the worship-OF angels") — to reflect reading (b). Significantly-more-interpretive than the Greek itself.
3. OR: leave the Thai rendering as-is + add a footer-note acknowledging the academic-debate (most-academically-honest, but adds register-burden to the verse).

**→ Recommend: confirm reading (a)** for corpus-evangelical-default + **possible footer-note** at 2:18 acknowledging the alternative academic reading. No new corpus doc needed (single-occurrence lemma in Pauline corpus).

---

## 11. ταπεινοφροσύνη false-vs-true contextual split (2:18, 2:23 vs 3:12) — **STABLE**

COL contains the same lemma ταπεινοφροσύνη rendered with different contextual qualifiers based on negative-vs-positive valence:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 2:18 | θέλων ἐν ταπεινοφροσύνῃ καὶ θρησκείᾳ τῶν ἀγγέλων | **ความถ่อมใจจอมปลอม** | False humility (Colossian-heretics' false-virtue) |
| 2:23 | λόγον μὲν ἔχοντα σοφίας ... ταπεινοφροσύνῃ | **ความถ่อมใจจอมปลอม** | Same context (continuing the Colossian-heresy critique) |
| 3:12 | σπλάγχνα οἰκτιρμοῦ, χρηστότητα, **ταπεινοφροσύνην**, πραΰτητα, μακροθυμίαν | **ความถ่อมใจ** | True humility (Christian-virtue list) |

The 3:12 KD names the principle: "ταπεινοφροσύνη here is TRUE-humility (commanded virtue) — distinct from the same-lemma at 2:18, 23 (false-humility of the Colossian-heretics). Lemma-context-determined; same Thai rendering since the heart-quality is what matters; the false-humility is qualified 'จอมปลอม' in the relevant context."

**Editorial assessment:** This is a **principled and skillful contextual-disambiguation**. The translator correctly identifies that the SAME lemma carries OPPOSITE valences in adjacent passages and qualifies the negative-context renderings with **จอมปลอม** ("false / counterfeit") to alert the Thai reader. The PHP-2 + COL-3 corpus-Pauline-pattern of ταπεινοφροσύνη as a virtue is preserved at 3:12; the polemical-target framing at 2:18/2:23 is preserved with the qualifier. **STABLE** ✓ — no action; worth a one-line note in the kenosis doc amendment per §1 (since PHP 2:3 ταπεινοφροσύνη is the true-virtue locking-precedent).

---

## 12. πατήρ register split — **LOCKED ✓ (extends GAL + PHP pattern)**

COL has 5 πατήρ-cluster occurrences with the same principled register-split as GAL + PHP + 1TH:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:2 | ἀπὸ θεοῦ πατρὸς ἡμῶν | **จากพระเจ้าพระบิดาของเรา** | divine (royal pระ-) |
| 1:3 | τῷ θεῷ πατρὶ τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ | **พระเจ้า พระบิดาของพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** | divine (royal) |
| 1:12 | εὐχαριστοῦντες τῷ πατρί | **พระบิดา** (implied royal) | divine (royal — context: "the Father who has qualified us") |
| 3:17 | εὐχαριστοῦντες τῷ θεῷ πατρὶ δι' αὐτοῦ | **พระเจ้าพระบิดา** | divine (royal) |
| 3:21 | οἱ πατέρες, μὴ ἐρεθίζετε τὰ τέκνα ὑμῶν | **บิดาทั้งหลาย** | human-paternal Haustafel address (plain — NOT royal) |

**Editorial assessment:** Compliance with `narrator_vs_character_voice_2026-04.md` is exact. The Haustafel-address **บิดาทั้งหลาย** at 3:21 is the parallel to GAL 4:2's Greco-Roman household-father analogy (per GAL audit §5) and to 1TH 2:11's apostolic-self-portrait paternal analogy (per 1TH audit §8). **LOCKED** ✓ — third Pauline-letter confirmation of the Pauline-corpus πατήρ register-split.

---

## 13. κύριος pun — earthly-masters vs heavenly-Master (3:22, 4:1) — **STABLE (extends honorifics doc)**

COL 3:22 + 4:1 contains Paul's most-pointed κύριος-pun in the Pauline corpus: the SAME Greek lemma κύριος refers to BOTH earthly-masters (slaves' human owners) AND the divine Lord (Christ). The translator preserved the pun while disambiguating with two distinct Thai renderings:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 3:22 | τοῖς κατὰ σάρκα **κυρίοις** | **นาย**ของตนตามฝ่ายเนื้อหนัง | earthly-masters (plain register **นาย**) |
| 3:22b | φοβούμενοι τὸν **κύριον** | **องค์พระผู้เป็นเจ้า** | divine Lord (Christ; royal honorific) |
| 3:24 | τῷ **κυρίῳ** Χριστῷ δουλεύετε | **องค์พระผู้เป็นเจ้า คือ พระคริสต์** | divine Lord (royal) |
| 4:1 | οἱ **κύριοι** ... ὑμεῖς ἔχετε **κύριον** ἐν οὐρανῷ | **นายทั้งหลาย** ... **เจ้านาย**อยู่ในสวรรค์ | earthly-masters (plain **นาย / เจ้านาย**) + heavenly-master (plain **เจ้านาย** — this is the Pauline-pun: even the heavenly-Master is called by the same lemma applied to earthly-masters; preserves the rhetorical force) |

The 4:1 KD names the principle: "Pauline-paradox: the master-on-earth has a master-in-heaven. The κύριος-pun: same word for human-master AND divine-Master (Christ). Render **เจ้านาย** for the human-master sense (distinct from องค์พระผู้เป็นเจ้า which is reserved for divine-κύριος)."

**Editorial assessment:** The translator made a **deliberate exception at 4:1** — the heavenly-Master is rendered with the same plain-register **เจ้านาย** as the earthly-masters in the same verse, preserving Paul's deliberate-rhetorical-pun. This is principled and corpus-correct: the pun depends on lexical-overlap; the locked **องค์พระผู้เป็นเจ้า** rendering is reserved for divine-κύριος-as-Christ-confessional-formula contexts (e.g., 3:22b, 3:24). The 4:1 plain-register exception is the Pauline-pun-preservation move. **STABLE** ✓ — extends `honorifics_non_divine_authorities_2026-04.md` (worth a one-line cross-reference noting the Pauline-pun exception).

---

## 14. The 3:11 ethnic-collapse list (with Σκύθης) — **STABLE (distinctive expansion of GAL 3:28)**

COL 3:11 expands the Pauline ethnic-collapse formula beyond GAL 3:28's three-pair-list with two distinctive additions: **βάρβαρος + Σκύθης** (the "barbarian and Scythian" pair). Σκύθης is a NT-HAPAX:

> ὅπου οὐκ ἔνι Ἕλλην καὶ Ἰουδαῖος, περιτομὴ καὶ ἀκροβυστία, **βάρβαρος, Σκύθης**, δοῦλος, ἐλεύθερος, ἀλλὰ τὰ πάντα καὶ ἐν πᾶσιν Χριστός
> ในชีวิตใหม่นั้น ไม่มีกรีกหรือยิว ผู้เข้าสุหนัตหรือผู้ไม่ได้เข้าสุหนัต **คนต่างด้าว ชาวสกุท** ทาสหรือไท แต่พระคริสต์ทรงเป็นทุกสิ่งและในทุกคน

The 3:11 KD names the cultural force: "HAPAX in NT (Σκύθης, only here): nomadic-people-from-the-Black-Sea region; ancient stereotype-of-savagery. Render **ชาวสกุท** — Thai transliteration; the thai_summary explains the cultural-pejorative connotation." The 3:11 thai_summary unfolds the cultural context for Thai readers.

**Editorial assessment:** The βάρβαρος → **คนต่างด้าว** + Σκύθης → **ชาวสกุท** pair preserves the most-despised-cultural-other rhetorical force (the Scythian was the ancient world's stereotypical-savage). The Pauline-collapse-formula in COL goes farther than in GAL by naming the EXTREME-other category. **STABLE** ✓ — no new doc needed; the Σκύθης glossary entry suffices.

---

## 15. Nympha gender (4:15) — **STABLE (SBLGNT-feminine reading followed)**

COL 4:15 is one of the well-known **textual-variant-determines-gender** verses. SBLGNT reads αὐτῆς (her/feminine), making the accusative Νύμφαν a feminine "Nympha" hosting a house-church. Some Byzantine manuscripts read αὐτοῦ (his/masculine) — making it "Nymphas" (man); other manuscripts read αὐτῶν (their/plural). The translator followed SBLGNT-feminine:

> ἀσπάσασθε τοὺς ἐν Λαοδικείᾳ ἀδελφοὺς καὶ Νύμφαν καὶ τὴν κατ' οἶκον **αὐτῆς** ἐκκλησίαν
> จงทักทายพี่น้องในเมืองเลาดีเซีย และนิมฟา และคริสตจักรที่ประชุมที่**บ้านของนาง**

The 4:15 KD explicitly names the textual-variant + the SBLGNT/NA28 + mainstream evangelical English (BSB/ESV/NIV/CSB) all-following the feminine reading. Resolved doc at `output/textual_variants/_resolved/colossians_04_v15_nympha_gender.md` (presumed; verify path consistency with other resolved variants).

**Editorial assessment:** Compliant with project's SBLGNT-default + RULES §5b (silent-omission for word-choice variants when SBLGNT + mainstream-modern-evangelical-English consensus aligns). Important historical-data: a woman hosting a house-church confirms women's prominent leadership-role in early-churches (cf. Lydia, Phoebe, Priscilla). **STABLE** ✓ — no action.

---

## 16. Textual variants — all SBLGNT-following with `_resolved` docs — **all LOCKED ✓**

COL has **6 textual-variant decisions** flagged in the verse-level KDs, all following the SBLGNT-shorter / mainstream-critical-text consensus:

| Verse | Variant | SBLGNT reading | Resolution doc |
|---|---|---|---|
| 1:2 | καὶ κυρίου Ἰησοῦ Χριστοῦ (omitted from greeting) | shorter | `output/textual_variants/_resolved/colossians_01_v2_lord_jesus_christ.md` |
| 1:7 | ὑπὲρ ἡμῶν vs ὑπὲρ ὑμῶν | ἡμῶν (SBLGNT) | word-choice variant per RULES §5b — flagged in notes |
| 1:14 | διὰ τοῦ αἵματος αὐτοῦ (omitted from "redemption") | shorter | `output/textual_variants/_resolved/colossians_01_v14_through_his_blood.md` |
| 3:6 | ἐπὶ τοὺς υἱοὺς τῆς ἀπειθείας (verse-boundary-only question) | included; v.7 boundary | clarification-note per `465b1f1` commit |
| 4:8 | γνῶτε vs γνῷ | γνῶτε (SBLGNT) | word-choice variant per RULES §5b — flagged in notes |
| 4:15 | αὐτῆς vs αὐτοῦ vs αὐτῶν (Nympha gender) | αὐτῆς feminine (SBLGNT) | (presumed `_resolved` doc; per §15) |
| 4:18 | closing extended grace-formula (omitted) | shorter | `output/textual_variants/_resolved/colossians_04_v18_grace_benediction.md` |

**Editorial assessment:** All 6 follow the SBLGNT + mainstream-modern-evangelical-English consensus. The 3:6/3:7 verse-boundary clarification (commit `465b1f1`, just before this audit) is the COL-shipping-cycle's only mid-stream textual fix; the per-verse KD now correctly notes this is a verse-boundary placement question, not a text-omission question. **all LOCKED** ✓.

---

## 17. Inherited locks — **all compliant**

| Doc | COL evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 1:18, 1:24, 4:15, 4:16 → **คริสตจักร** uniform (Christian community); 3:18 reciprocal-marriage and 4:15 house-church preserved. | **LOCKED** |
| `ethnos_2026-04.md` | 1:27 (ἐν τοῖς ἔθνεσιν → **ในหมู่คนต่างชาติ**, Pauline-mission category — same as GAL pattern). 1 occ; compliant. | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 15+ narrator-κύριος occurrences (1:3, 1:10, 2:6, 3:13, 3:15-17, 3:22-24, 4:1, 4:7, 4:17) → **องค์พระผู้เป็นเจ้า**, all compliant. The doc's "Lukan-Acts signature" framing should be amended (per JHN + GAL + 1TH + PHP audits) to acknowledge full Pauline extension; COL is the **fifth Pauline-corpus confirmation**. | **LOCKED-with-amendment-needed** (already noted in JHN + GAL + 1TH + PHP audits) |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A — no vocative κύριε in this letter (epistolary, not narrative). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | N/A in COL — the εὐχαριστέω-cluster (1:3, 1:12, 2:7, 3:15, 3:16, 3:17, 4:2 — 7+ occurrences) uses **ขอบพระคุณ**, the Pauline-thanksgiving-formula; not the doxological-praise pattern the doc covers. Compliant. | **LOCKED (N/A)** |
| `honorifics_non_divine_authorities_2026-04.md` | The 3:22 + 4:1 κύριος-pun (earthly-masters **นาย / เจ้านาย** plain register; divine-Master **องค์พระผู้เป็นเจ้า** royal) extends the doc — see §13. The Haustafel-paternal πατήρ at 3:21 → **บิดาทั้งหลาย** (plain) extends the divine/human register-split. Co-greeter Timothy at 1:1 → **ทิโมธีพี่น้องของเรา** plain register. Compliant. | **LOCKED** (extension recommended) |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout (พระเจ้า ทรง-, the Christ-hymn 1:15-20 ทรง-prefixed verbs). Plain register for Paul (apostolic-1pl-voice ข้าพเจ้า), co-workers, the Haustafel human-figures. Compliant. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | **N/A in COL** — no Aramaic embeds in this letter (no Αββα; no Μαραναθα). | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A in COL** — no Tier 1/2/3 inclusion variants in Colossians (no `output/textual_variants/colossians*` `_unresolved` files). All 6 textual-variants are word-choice / shorter-form variants per §16, handled with `_resolved` docs + verse-level Notes per RULES §5. No inclusion-bracket policy needed. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — Colossians is a doctrinal-pastoral letter, not narrative. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in COL. The 2:14 χειρόγραφον / 2:15 Roman-triumph / 4:6 salt-and-grace metaphors are figurative-similes, not parables with transparent God-figures. Compliant. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — μετανοέω + μεταμέλομαι BOTH absent from COL (no conversion-narrative; the closest soteriological language is the 1:13 μεθίστημι "transferred-into-the-kingdom" + 2:13 συνεζωοποίησεν "made-alive-with-Christ"). | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | COL 1:14 (ἀπολύτρωσιν, **τὴν ἄφεσιν τῶν ἁμαρτιῶν** → **การไถ่ คือ การยกโทษบาปทั้งหลาย**) — Pauline-locked phrase, perfectly compliant with the doc. The articular τῶν ἁμαρτιῶν renders **บาปทั้งหลาย** (all-the-sins). | **LOCKED** |
| `pagan_deities_2026-04.md` | COL 3:5 (πλεονεξίαν ἥτις ἐστὶν εἰδωλολατρία → **ความโลภ ซึ่งเป็นการกราบไหว้รูปเคารพ**) — εἰδωλολατρία rendered with the corpus-locked **การกราบไหว้รูปเคารพ** (NOT พระเจ้า, reserved for biblical God). Compliant. | **LOCKED** |
| `roman_administrative_titles_2026-04.md` | N/A — no Roman titles in COL (no governor/centurion/proconsul). The 4:10 συναιχμάλωτος "fellow-prisoner" suggests Paul's-imprisonment but the carceral-overseers are not named. | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from COL. The Christological titles here are Son-of-the-Father (1:13 τοῦ υἱοῦ τῆς ἀγάπης αὐτοῦ → **พระบุตรที่รักของพระองค์**) + cosmic-Christ titles (1:15-20 — see §1), not Son-of-Man. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (1:8, 3:16 ψδαῖς πνευματικαῖς **ฝ่ายจิตวิญญาณ**) — only 1 explicit Holy-Spirit reference in the letter (1:8 → **ในพระวิญญาณ**). Anthropological πνεῦμα at 2:5 (Paul's "spirit being-with-them") → **จิตใจ** (matches PHP 1:27 lock + the doc-locked anthropological πνεῦμα → **จิต** when the corpus-tripartite contrast is in view; 2:5 here uses **จิตใจ** "mind/inner-self" — slight contextual variant but within the doc's flexibility). ψυχή at 3:23 (ἐκ ψυχῆς ἐργάζεσθε → **ด้วยสุดจิตวิญญาณ** "with-all-one's-soul") — Hebraistic-totality idiom. Compliant. | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | N/A — COL is Pauline, not Johannine. No ἀμήν in COL (4:18 closing benediction shorter-form per SBLGNT, no closing amen). | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply (no Jesus-direct-discourse in COL). | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries-addressing-divine in COL. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | COL 1:13 (εἰς τὴν βασιλείαν τοῦ υἱοῦ τῆς ἀγάπης αὐτοῦ → **อาณาจักรของพระบุตรที่รักของพระองค์**); COL 4:11 (συνεργοὶ εἰς τὴν βασιλείαν τοῦ θεοῦ → **เพื่ออาณาจักรของพระเจ้า**) — both compliant with the Synoptic-Acts-Pauline lock. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | COL 1:5 (ἀποκειμένην ὑμῖν ἐν τοῖς οὐρανοῖς → **เก็บไว้ให้พวกท่านในสวรรค์** — after-possessor sense **สวรรค์**); 1:16, 1:20 (τὰ ἐν τοῖς οὐρανοῖς → **ในสวรรค์** — same after-possessor); 1:23 (πάσῃ κτίσει τῇ ὑπὸ τὸν οὐρανόν → **ทุกสิ่งที่ทรงสร้างใต้ฟ้า** — meteorological **ฟ้า** for "under heaven" cosmographic idiom); 4:1 (κύριον ἐν οὐρανῷ → **เจ้านายอยู่ในสวรรค์**). All compliant per the doc's three-way rule (ฟ้าสวรรค์ / สวรรค์ / ท้องฟ้า/ฟ้า). | **LOCKED** |
| `christ_hymn_kenosis_2026-05.md` | The doc itself names COL 1:15–20 as a forward-passage "to be integrated, not pre-decided." This audit (§1) recommends amending the doc with a COL 1:15–20 cosmic-Christ-vocabulary sub-section. The translator's restraint (NOT mechanically-importing PHP 2 vocabulary) honors the doc's stated principle. | **LOCKED (extension recommended per §1)** |
| `diakonos_pauline_2026-05.md` | COL 1:7 (Epaphras as διάκονος τοῦ Χριστοῦ → **ผู้รับใช้ของพระคริสต์**); COL 1:23 (Paul as διάκονος of the gospel → **ผู้รับใช้**); COL 1:25 (Paul as διάκονος of the church → **ผู้รับใช้**); COL 4:7 (Tychicus as πιστὸς διάκονος → **ผู้รับใช้ที่สัตย์ซื่อ**). All four uses → **ผู้รับใช้** uniform (plain register, NOT royal — preserves the humility-self-attribution force per the doc). | **LOCKED** |
| `pistis_christou_2026-05.md` | COL has NO ambiguous πίστις-Χριστοῦ-genitive uses (the closest are 1:4 πίστιν ὑμῶν ἐν Χριστῷ Ἰησοῦ → **ความเชื่อของพวกท่านในพระเยซูคริสต์** unambiguously objective, with explicit ἐν preposition; and 2:5 τῆς εἰς Χριστὸν πίστεως ὑμῶν → **ความเชื่อในพระคริสต์ของพวกท่าน** unambiguously objective with εἰς preposition). The 1:4 KD explicitly cross-references the doc. Both compliant. | **LOCKED** |
| `phroneo_pauline_2026-05.md` | COL 3:2 (τὰ ἄνω **φρονεῖτε** → จง**คิด**ถึงสิ่งที่อยู่เบื้องบน) — the heavenly-orientation imperative-counterpart to PHP 3:19's negative τὰ ἐπίγεια **φρονοῦντες**. Single occurrence; perfectly compliant with the doc's cognitive-disposition branch (**คิด**). The doc explicitly named COL 3:2 as forward-pertinent; this audit confirms compliance. | **LOCKED** |
| `parousia_christou_2026-05.md` | **N/A in COL** — παρουσία absent from this letter. The Christ-eschatological-appearing language at COL 3:4 (ὅταν ὁ Χριστὸς **φανερωθῇ** → เมื่อพระคริสต์ ... **ปรากฏ**) uses φανερόω (the Pauline-corpus-standard divine-revelation lemma) rather than παρουσία. The forward-pertinent passages remain (2 Thess 2:1–9). | **LOCKED (N/A)** |
| `dikaioo_dikaiosyne_family_2026-05.md` | **N/A in COL** — δικαιόω + δικαιοσύνη family **absent from COL** (theologically-distinctive: COL's atonement-language is ἀπολύτρωσις + ἄφεσις + ἀποκαταλλάσσω, NOT δικαιόω). | **LOCKED (N/A)** |
| `nomos_pauline_2026-05.md` | **N/A in COL** — νόμος **absent from COL** (theologically-distinctive: COL's anti-Colossian-heresy critique is anti-στοιχεῖα + anti-philosophy + anti-Jewish-calendrical-observance, but NOT a νόμος-vs-grace argument). The closest analogues are 2:14 χειρόγραφον τοῖς δόγμασιν (legal-decrees → **ข้อบัญญัติ** functional-equivalent) + 2:22 ἐντάλματα τῶν ἀνθρώπων (human-commands). | **LOCKED (N/A)** |
| `huiothesia_adoption_2026-05.md` | **N/A in COL** — υἱοθεσία absent. The closest analogue is 1:13 (μετέστησεν εἰς τὴν βασιλείαν τοῦ υἱοῦ — transferred-into-the-Son's-kingdom) which is sonship-by-incorporation language but not the adoption-lemma. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | (Already noted N/A above) | **LOCKED (N/A)** |
| `proper_noun_wordplay_2026-05.md` | COL 4:9 (Onesimus the formerly-"useless" → now-faithful — Pauline-rehabilitation, parallel to PHM 11). The 4:9 KD acknowledges the PHM-back-reference. Compliant with the doc's name-meaning-disambiguation principle. | **LOCKED** |
| `telos_paidagogos_christ_2026-05.md` | N/A — COL absent of τέλος-of-νόμος language + παιδαγωγός. | **LOCKED (N/A)** |
| `porneia_vs_moicheia_DEFERRED_2026-05.md` | COL 3:5 (πορνεία at the head of the vice-list → **การล่วงประเวณี**) — uniform with prior-corpus rendering. The doc's deferred-status remains; COL adds the GAL-precedent rendering without forcing the question. Compliant. | **LOCKED (N/A; deferred per doc)** |
| `inclusion_variants_absent_verses_2026-04.md` | (Already noted above) | **LOCKED (N/A)** |
| `roman_administrative_titles_2026-04.md` | (Already noted above) | **LOCKED (N/A)** |
| `adversary_speech_register_2026-05.md` | The 2:21 quoted-prohibitions (Μὴ ἅψῃ μηδὲ γεύσῃ μηδὲ θίγῃς → ‘**อย่าจับ อย่าชิม อย่าแตะต้อง**’ in Thai-curly-quotes) are the Colossian-heretics' false-rules quoted-mockingly by Paul. Plain register (NOT royal). Compliant with the adversary-speech principle. | **LOCKED** |

---

## Mechanical (§1) — **all green**

- 4/4 chapters: `output/check_reports/colossians_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 4/4 chapters: `output/back_translations/colossians_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-187-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: only the re-ran-check artifact (`key_term_consistency_all.md` modified by my §1 verification re-run). No COL source-file dirt; no lingering `_unresolved` textual-variant files.

---

## Pre-existing docs affirmed / unchanged

All 36 docs in `docs/translator_decisions/` reviewed. Compliance summary in §17 above. The **Lukan-Acts narrator-κύριος doc** flagged for amendment (already noted in JHN + GAL + 1TH + PHP audits) — Colossians provides a fifth independent Pauline-corpus confirmation; the doc's "Lukan signature" framing should be renamed/extended to acknowledge corpus-wide narrator-κύριος usage. The **Christ-hymn kenosis doc** flagged for amendment (per §1) — COL 1:15–20 sub-section to be added.

---

## Flagged for Ben's attention

### A. Christ-Hymn (COL 1:15–20) cosmic-Christ vocabulary cluster — **STABLE; amend kenosis doc** (§1)
The COL hymn is the SECOND Christological hymn in the corpus (after PHP 2:5–11). Different lexicon (no μορφή / κενόω; instead εἰκών + πρωτότοκος + πλήρωμα + ἀποκαταλλάσσω + αἷμα τοῦ σταυροῦ). The translator's restraint (NOT mechanically-importing PHP 2 vocabulary) honors the kenosis doc's stated principle. Amend `christ_hymn_kenosis_2026-05.md` with the cosmic-Christ-vocabulary sub-section.

### B. πρωτότοκος rendering with **เหนือ** (1:15) — **DECIDE before tagging** (§2)
The choice to render πρωτότοκος πάσης κτίσεως as **บุตรหัวปีเหนือ...** (with **เหนือ** "over") rather than **บุตรหัวปีของ...** (with **ของ** "of") is doctrinally orthodox but more lexically-explicit than mainstream English Bibles. Confirm Ben endorses the **เหนือ** rendering as the corpus-default + write the recommended `prototokos_pauline_2026-05.md` brief doc. Important pre-Heb 1:6 + Rev 1:5.

### C. στοιχεῖα τοῦ κόσμου basic-principles vs elemental-spirits — **DECIDE before tagging** (§3)
The long-deferred GAL-audit recommendation. COL 2's anti-cosmic-powers polemical context (with 2:10/2:15 ἀρχαὶ καὶ ἐξουσίαι defeated + 2:18 angel-worship) leans toward reading (3) elemental-spirits more strongly than GAL did. But **หลักการพื้นฐานของโลก** preserves corpus-consistency with shipped GAL. Either way, finally write the deferred corpus doc — `stoicheia_tou_kosmou_2026-05.md`.

### D. ἀνταναπληρῶ τὰ ὑστερήματα τῶν θλίψεων τοῦ Χριστοῦ (1:24) — **REVIEW** (§6)
The most-difficult verse in the book theologically. Translator preserved literal **เติมเต็ม ... ในสิ่งที่ยังขาดอยู่ในความทุกข์ของพระคริสต์** with thai_summary disambiguation against the Catholic-Mass-of-merits interpretation. Worth Ben's confirmation that the literal-rendering + summary-disambiguation strategy is the right approach for an evangelical-Protestant CC0 Thai Bible.

### E. The spiritual-beings 4-tier hierarchy (1:16) — **REVIEW** (§5)
The 4-tier rendering at 1:16 (บัลลังก์ / เทพผู้ครอง / ทูตสวรรค์ผู้มีอำนาจ / ผู้ทรงสิทธิ) is bold + informative but distinctive. Confirm the register + the contextual-shift between 1:16 ἀρχαί → **ทูตสวรรค์ผู้มีอำนาจ** vs 2:10/2:15 ἀρχαί → **ผู้ครอง** is principled. Optional new doc `spiritual_beings_hierarchy_2026-05.md` before Eph 1:21 + 6:12.

### F. The Pauline household-code / Haustafel (3:18–4:1) — **REVIEW** (§8)
First Pauline-Haustafel in corpus. Six imperatives across six relational-pairs. Renderings are corpus-precedent-aligned (ὑποτάσσω → **ยอมอยู่ใต้บังคับ** matches LUK 10:17, 1Co 14:32; ὑπακούω → **เชื่อฟัง** matches Eph 6:1). Worth Ben's confirmation given the contemporary-reception load + the forward-pertinence to Eph 5:22–6:9 (the much-longer parallel-Haustafel) + 1 Pet 2:18–3:7.

### G. θρησκεία τῶν ἀγγέλων (2:18) subjective-vs-objective genitive — **DECIDE before tagging** (§10)
Famous interpretive crux. Translator chose reading (a) angel-veneration (mainstream evangelical) over reading (b) visionary-mystical-piety (modern academic consensus). Confirm Ben endorses (a) as the corpus-default + decide whether to add a footer-note acknowledging (b).

### H. σάρξ polysemy with explicit RULES §5 flags — **STABLE; lift to corpus doc** (§7)
COL's σάρξ-handling is the strongest in the corpus to date. Finally lift the GAL audit's recommendation to corpus doc `sarx_pauline_2026-05.md` before Romans 7-8 ships.

### I. New corpus docs to write
1. **`docs/translator_decisions/prototokos_pauline_2026-05.md`** (§2) — brief; locks **บุตรหัวปี + เหนือ-vs-ของ** distinction by sense
2. **`docs/translator_decisions/stoicheia_tou_kosmou_2026-05.md`** (§3) — finally writes the GAL-recommended doc
3. **`docs/translator_decisions/sarx_pauline_2026-05.md`** (§7) — finally writes the GAL-recommended doc + extends with COL's RULES §5 flagging discipline + Christ's-physical-body **พระวรกาย** sub-sense
4. **(Optional)** `docs/translator_decisions/spiritual_beings_hierarchy_2026-05.md` (§5) — locks the 4-tier + 2-pair renderings before Eph

### J. Existing docs to amend
- **`christ_hymn_kenosis_2026-05.md`** — add COL 1:15–20 cosmic-Christ-vocabulary sub-section (§1)
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to "Lukan-Acts + Johannine + Pauline (Galatians + 1TH + PHP + COL)." Fifth Pauline-corpus confirmation; the doc's "Lukan signature" framing should be formally renamed (already flagged across four prior audits).
- **`honorifics_non_divine_authorities_2026-04.md`** — add Pauline-pun-preservation note (the 4:1 plain-register **เจ้านาย** for the heavenly-Master is the principled exception; per §13)

### K. External AI review (§3 of checklist) — **pending**
Recommended before `book-colossians-v1` tag. Suggested 4-cluster external AI packet:
1. **COL 1:15–20** — the cosmic-Christ-hymn (πρωτότοκος / εἰκών / πλήρωμα / ἀποκαταλλάσσω cluster — DECIDE/REVIEW items A + B)
2. **COL 1:24–2:9** — Paul's apostolic-suffering + the Christ-and-fullness-cluster (REVIEW item D + STABLE item §4)
3. **COL 2:8–23** — the anti-Colossian-heresy critique (στοιχεῖα + angel-worship + asceticism — DECIDE items C + G)
4. **COL 3:18–4:1** — the Pauline-Haustafel (REVIEW item F)

Use Grok + ChatGPT in parallel per the JHN/GAL/PHP pattern.

---

## Recommendation

**Colossians ships in strong corpus-hygiene shape — and provides the cosmic-Christology counterpart to Philippians' kenotic-Christology.** The translator made consistent, principled choices on the most-significant COL-introduced patterns (the cosmic-Christ-hymn vocabulary; the spiritual-beings 4-tier hierarchy; σάρξ polysemy with explicit RULES §5 flags; the Pauline-Haustafel; the cancelled-IOU metaphor) — and none of these has a corpus-level doc yet. The finally-write-the-GAL-recommendations moment has arrived: the **stoicheia_tou_kosmou** + **sarx_pauline** docs that the GAL audit recommended for `2026-04.md` filenames were never written; COL is the natural place to formalize them as `2026-05.md`.

Tag `book-colossians-v1` after:
1. Ben's decisions on **§A + §B + §C + §G** (DECIDE items: πρωτότοκος rendering with **เหนือ**; στοιχεῖα τοῦ κόσμου basic-principles vs elemental-spirits; θρησκεία τῶν ἀγγέλων subjective-vs-objective)
2. Ben's confirmations on **§D + §E + §F + §H** (REVIEW items: ἀνταναπληρῶ Catholic-Mass framing; spiritual-beings 4-tier hierarchy; Pauline-Haustafel; σάρξ polysemy lock-lift)
3. Three new translator_decisions docs written (§I items 1–3)
4. Three existing docs amended (`christ_hymn_kenosis_2026-05.md` cosmic-Christ sub-section; `kyrios_narrator_voice_luke_acts_2026-04.md` Pauline-extension; `honorifics_non_divine_authorities_2026-04.md` Pauline-pun-exception)
5. External AI sanity-check (§K)

The remaining Pauline letters (Eph in flight; then the Pastorals: 1–2 Tim, Tit) can be queued for next book — but **`prototokos_pauline`, `stoicheia_tou_kosmou`, and `sarx_pauline`** docs should happen **before Eph 1:21 / Eph 6:12 / Rom 7:5** to avoid forward drift in the cosmic-powers + sinful-flesh vocabulary that those passages will compound.
