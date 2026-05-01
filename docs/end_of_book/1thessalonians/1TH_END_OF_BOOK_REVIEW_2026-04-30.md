# 1 Thessalonians — End-of-Book Review

**Date:** 2026-04-30
**Scope:** All 5 chapters (89 verses; 203 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (24 docs).
**Trigger:** 1TH 5 shipped (commit `8066641`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **12 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 5/5 chapters have green per-chapter reports + back-translations (chs 1–4 reside on the `end-of-book-review-galatians` loop branch; ch 5 on `end-of-book-review-galatians-audit`; both are reachable from this audit branch's parent); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-119-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status` clean.
- **1 Thessalonians is the SECOND FULL Pauline epistle the project has shipped** (after Galatians; both 2026-04-30). At 89 verses it is also Paul's earliest extant letter (ca. AD 50–51). The technical-vocabulary established here will propagate into 2 Thess (already in flight), the Pastorals, and beyond. The audit confirms strong CONTINUITY with GAL on the inherited Pauline-vocabulary set (ἐκκλησία, ἀπόστολος, ἀδελφοί, πατήρ register split, εὐχαριστέω, ἁγιασμός — first introduced here, glossary-locked) and **introduces a major NEW corpus-cross-cutting cluster: Pauline ESCHATOLOGY-VOCABULARY** (παρουσία, ἁρπάζω, σάλπιγξ θεοῦ, ἀρχάγγελος, ἡμέρα κυρίου, ὀργὴ ἐρχομένη). 1 Thess 4:13–5:11 is the densest eschatological passage in the corpus to date and the first significant exposure for Eremos.
- **15 inherited Synoptic / John / Acts / Galatians locks verified compliant** in 1TH (ἐκκλησία, ἔθνος, narrator-κύριος, divine-object praise verbs implicitly N/A, narrator-vs-character voice, Aramaic-transliteration N/A, honorifics, OT-citation flagging — see §11–12).
- **5 cross-cutting Pauline patterns are STABLE-but-undocumented at corpus level** (παρουσία; ἁγιασμός / ἁγιωσύνη / ἀκαθαρσία cluster; ἁρπάζω-rapture verb; ἡμέρα κυρίου; tripartite anthropology at 5:23). All five are first-occurring or first-densely-occurring here, so corpus-doc lift is recommended before 2 Thess 1:7–10 (the day-of-the-Lord cluster) and Romans (sanctification + wrath density).
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: σκεῦος "vessel" = body vs wife at 4:4; ἀπό in "from-the-presence" 2 Thess-style ἀπό questions absent here but adjacent; tripartite-anthropology rendering at 5:23).
- **3 items flagged DECIDE** (1 Thess 2:14–16 anti-Jewish-polemic / interpolation question + Thai handling; 1 Thess 4:4 σκεῦος = body-vs-wife; the πάντων τῶν ἁγίων αὐτοῦ at 3:13 = angels-vs-saints crux).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. παρουσία — Christ's eschatological coming (the Pauline-corpus entry-point) — **STABLE (undocumented; recommend new doc — high Pauline-forward priority)**

Παρουσία occurs **4× in 1TH** (2:19; 3:13; 4:15; 5:23) — the densest distribution of this lemma per chapter in the entire NT. Every occurrence renders **การเสด็จมา** ("the coming, the arrival") with the prepositional phrase **ในการเสด็จมาของ...** ("in/at the coming of..."):

| Verse | Greek | Thai |
|---|---|---|
| 2:19 | ἔμπροσθεν τοῦ κυρίου ἡμῶν Ἰησοῦ ἐν τῇ αὐτοῦ παρουσίᾳ | **ต่อพระพักตร์พระเยซูองค์พระผู้เป็นเจ้าของเรา ในการเสด็จมาของพระองค์** |
| 3:13 | ἐν τῇ παρουσίᾳ τοῦ κυρίου ἡμῶν Ἰησοῦ μετὰ πάντων τῶν ἁγίων αὐτοῦ | **ในการเสด็จมาของพระเยซูองค์พระผู้เป็นเจ้าของเรา พร้อมกับวิสุทธิชนทุกคนของพระองค์** |
| 4:15 | εἰς τὴν παρουσίαν τοῦ κυρίου | **จนถึงการเสด็จมาขององค์พระผู้เป็นเจ้า** |
| 5:23 | ἐν τῇ παρουσίᾳ τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ | **ในการเสด็จมาของพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** |

The 5:23 KD names the principle:

> παρουσία consistent rendering. The TEMPORAL-FRAME of the prayer = the parousia-event.

**Editorial assessment:** **การเสด็จมา** is principled — it preserves the royal-divine action (เสด็จ = royal verb of motion) AND the simple "coming/arrival" semantic. The single-rendering policy across all 4 occurrences is uniform and tracks the Pauline-technical use (παρουσία as Christ's eschatological return, NOT the secular Hellenistic sense of a king's civic-arrival, which is the etymological source). 1TH effectively LOCKS this rendering for the Pauline corpus.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/parousia_christou_2026-04.md` before 2 Thess 2:1–9 (the densest παρουσία-cluster in the NT, including the παρουσία τοῦ ἀνόμου "the parousia of the lawless one" — distinctively non-Christ use). The doc should:
1. Lock παρουσία (Christ-eschatological subject) → **การเสด็จมา**
2. Note the 2 Thess 2:9 παρουσία (lawless-one subject) needs careful handling to preserve the Pauline-rhetorical pun (NOT royal-เสด็จ for the antichrist; will need plain register)
3. Cite 1 Thess 4:15 as the locking precedent
4. Cross-reference the related Synoptic eschatological-coming language (Matt 24 ἔρχομαι constructions, NOT the παρουσία noun) for distinction

---

## 2. ἁγιασμός / ἁγιωσύνη / ἀκαθαρσία — sanctification cluster (Pauline ethics first-establishment) — **STABLE (undocumented; recommend new doc — high Pauline-forward priority)**

1TH 4:1–8 is the FIRST DENSE Pauline-sanctification passage in the corpus. The cluster spans:

| Greek | Thai | Verses |
|---|---|---|
| ἁγιασμός (the PROCESS of being-set-apart-and-purified) | **การชำระให้บริสุทธิ์** | 4:3, 4:4, 4:7 |
| ἁγιωσύνη (the STATE of holiness) | **ความบริสุทธิ์** | 3:13 |
| ἀκαθαρσία (impurity, the binary-opposite) | **ความไม่บริสุทธิ์** | 4:7 |
| ἁγιάζω (verb — sanctify) | **ทรงชำระ ... ให้บริสุทธิ์** | 5:23 |
| ἅγιοι (substantival adj. — holy ones / saints) | **วิสุทธิชน** | 3:13 |
| ἅγιον (adj. modifying φίλημα — "holy kiss") | **อันบริสุทธิ์** | 5:26 |
| ἅγιον (adj. modifying πνεῦμα) | **บริสุทธิ์** | 1:5, 1:6, 4:8 |

The 4:3 KD names the principle:

> ἁγιασμός = the PROCESS of being-set-apart-and-purified (cognate with ἅγιος 'holy'; cf. Rom 6:19, 22; 1 Tim 2:15; Heb 12:14; 1 Pet 1:2). DISTINGUISHED FROM ἁγιωσύνη ('the state-of-holiness') — ἁγιασμός is the active-process. KEY-TERM ESTABLISHED: ἁγιασμός → การชำระให้บริสุทธิ์ (Pauline-corpus standard for the process of being-made-holy).

**Editorial significance:** The principled lexical split between **ἁγιασμός = การชำระให้บริสุทธิ์ (process)** and **ἁγιωσύνη = ความบริสุทธิ์ (state)** is theologically rich — it preserves the Greek-aspectual contrast that English collapses into "sanctification" / "holiness" indistinguishably. The 4:7 binary contrast (ἀκαθαρσίᾳ ↔ ἁγιασμῷ → **ความไม่บริสุทธิ์ ↔ การชำระให้บริสุทธิ์**) reads cleanly in Thai. The verbal form ἁγιάζω at 5:23 uses **ทรงชำระ ... ให้บริสุทธิ์** (royal-verb construction with God as subject — divine sanctifying-action).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/hagiasmos_hagiosune_2026-04.md` before Rom 6:19, 22 (the next-densest ἁγιασμός cluster) and Heb 12:14 (ἁγιωσύνη in covenant-pursuit context). The doc should:
1. Lock ἁγιασμός (process) → **การชำระให้บริสุทธิ์**
2. Lock ἁγιωσύνη (state) → **ความบริสุทธิ์**
3. Lock ἁγιάζω (transitive verb, God-subject) → **ทรงชำระ ... ให้บริสุทธิ์**
4. Lock ἀκαθαρσία (binary-opposite of ἁγιασμός) → **ความไม่บริสุทธิ์**
5. Note the differentiation from ἅγιος (substantive "saints/holy-ones") → **วิสุทธิชน**
6. Note the differentiation from related-but-distinct Pauline ethics-vocab: πορνεία → **การล่วงประเวณี** (locked from GAL 5:19); τιμή ("honor" alongside ἁγιασμός at 4:4) → **เกียรติ**
7. Cite 1 Thess 4:3–8 as the locking precedent (densest first-occurrence cluster)

---

## 3. ἁρπάζω + the rapture-passage vocabulary — **STABLE (undocumented; recommend brief new doc)**

The famous 1 Thess 4:17 verse — Latin Vulgate `rapio`, source of the English term "rapture":

> ἔπειτα ἡμεῖς οἱ ζῶντες οἱ περιλειπόμενοι ἅμα σὺν αὐτοῖς **ἁρπαγησόμεθα** ἐν νεφέλαις εἰς ἀπάντησιν τοῦ κυρίου εἰς ἀέρα

Thai: **เราทั้งหลายที่ยังเป็นอยู่และเหลืออยู่ จะถูกรับขึ้นไปพร้อมกับพวกเขาในเมฆ เพื่อพบกับองค์พระผู้เป็นเจ้าในฟากฟ้า** ("we who are still living and remaining will be **received-up [passive]** together with them in clouds, to meet the Lord in the air").

The 4:17 KD names the source-language history:

> ἁρπάζω future passive = 'will be snatched up, will be caught up.' The Latin VULGATE translates with rapio, source of English 'rapture.' ἅμα σὺν αὐτοῖς = 'together with them' = simultaneous-united with the just-resurrected dead-believers. ถูกรับขึ้นไปพร้อมกับพวกเขา = 'will be taken up together with them' (preserves the ἁρπάζω + ἅμα σύν simultaneous-uplift force).

**Editorial assessment:** **ถูกรับขึ้นไป** is a measured and theologically-neutral rendering. It preserves the divine-passive (the believers are taken-up BY God / Christ; not "snatched/grabbed" violently per non-passive ἁρπάζω uses) and avoids importing the **dispensationalist English "rapture" framing** by name into the Thai. Thai readers unfamiliar with the term "rapture" will read this as the Pauline-eschatological "uplift to meet the Lord" event without any pre-trib / mid-trib / post-trib commitment. The verse-level Notes acknowledge:

> THE FAMOUS 'RAPTURE' VERSE. ἁρπάζω → Latin rapio → English 'rapture.' The verse is foundational for various-Christian-eschatological-systems (pre-trib rapture, mid-trib, post-trib, amillennial, etc.); the Greek text DOES NOT specify which system is correct — it specifies the EVENT (resurrection + rapture + meeting in the air) but not its placement-within-eschatological-timeline.

The accompanying eschatological-vocabulary cluster in 4:16:
- **κέλευσμα** (NT hapax — "shout, military-command") → **เสียงคำสั่ง**
- **ἀρχάγγελος** ("archangel") → **หัวหน้าทูตสวรรค์**
- **σάλπιγξ θεοῦ** ("trumpet of God") → **เสียงแตรของพระเจ้า**
- **νεφέλαι** ("clouds") → **เมฆ** (cf. Dan 7:13 / Mark 13:26 cloud-imagery)
- **ἀπάντησις** (technical Hellenistic civic-reception term) → **พบกับ** ("meet with")
- **ἀέρ** ("air") → **ฟากฟ้า** ("the firmament / atmospheric region")

**Recommend: STABLE; consider brief new doc** `docs/translator_decisions/rapture_event_vocabulary_2026-04.md` to lock the 4:17 ἁρπάζω → **ถูกรับขึ้นไป** rendering (theologically-neutral, divine-passive) and document the surrounding 4:16 cluster as a unit. Important pre-1 Cor 15:51–52 (the parallel rapture-passage with σαλπίσει + ἀλλαγησόμεθα) and 2 Cor 12:2–4 (Paul's own ἁρπαγέντα ἕως τρίτου οὐρανοῦ "caught up to the third heaven" — same lemma, different referent).

---

## 4. ἡμέρα κυρίου — Day of the Lord (OT-prophetic technical term) — **STABLE (undocumented; recommend new doc)**

1 Thess 5:2 introduces the Pauline rendering of the OT-prophetic technical term **יוֹם יְהוָה / ἡμέρα κυρίου**:

> αὐτοὶ γὰρ ἀκριβῶς οἴδατε ὅτι **ἡμέρα κυρίου** ὡς κλέπτης ἐν νυκτὶ οὕτως ἔρχεται.
> เพราะพวกท่านเองทราบดีอยู่แล้วว่า **วันแห่งองค์พระผู้เป็นเจ้า**นั้นจะมาถึงเหมือนขโมยที่มาในเวลากลางคืน

The 5:2 KD names the principle:

> OT-PROPHETIC TECHNICAL TERM: 'the Day of YHWH' (Joel 1:15; 2:1, 11, 31; Amos 5:18-20; Obad 15; Zeph 1:7-18; etc.) = the eschatological-day-of-divine-judgment. In NT-application, the 'Lord' = CHRIST — the Day-of-the-Lord becomes the Christ-parousia + judgment + cosmic-renewal. Pauline-corpus-standard rendering: วันแห่งองค์พระผู้เป็นเจ้า (royal-noun construction; consistent with prior-corpus-renderings of יוֹם יְהוָה / ἡμέρα κυρίου).

The associated 5:4 ἡ ἡμέρα (anaphoric "that day") → **วันนั้น** (preserves the anaphoric reference). The 5:5 υἱοὶ ἡμέρας ("sons of day") → **บุตรแห่งวัน** (preserves the Hebraic "sons of X" idiom + the contrast with υἱοὶ φωτός / νυκτός / σκότους).

**Editorial assessment:** **วันแห่งองค์พระผู้เป็นเจ้า** is perfectly compliant with the locked narrator-κύριος rendering (`kyrios_narrator_voice_luke_acts_2026-04.md`). The royal-pระ-prefixed construction preserves the divine-eschatological force of the OT-prophetic technical term. Note: **κυρίου** in this OT-citation-style construction refers to **CHRIST** in NT-application (per Pauline pattern), not the Tetragrammaton — but the rendering is stable across both readings since องค์พระผู้เป็นเจ้า covers both YHWH-translation and Christ-honorific in the NT corpus.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/hemera_kyriou_2026-04.md` before 2 Thess 1:10 + 2:2 (where the τοῦ κυρίου (or τοῦ Χριστοῦ) ἡμέρα recurs in a heavily-eschatological context with the famous 2:2 textual variant κυρίου / Χριστοῦ). The doc should:
1. Lock ἡμέρα κυρίου → **วันแห่งองค์พระผู้เป็นเจ้า**
2. Lock anaphoric ἡ ἡμέρα → **วันนั้น**
3. Note the related-but-distinct: ἡμέρα Χριστοῦ → **วันแห่งพระคริสต์** (Phil 1:6, 1:10; 2:16); ἡμέρα ... κρίσεως → **วันพิพากษา** (separate lock — judgment-day construction)
4. Cite 1 Thess 5:2 as the locking precedent
5. Cross-reference the OT echoes (Joel, Amos, Zeph) for theological-context noted in glossary

---

## 5. ὀργή — divine wrath in eschatological context — **STABLE (undocumented; consider doc later)**

1TH has **3 occurrences of ὀργή**, all rendered **พระพิโรธ** ("divine wrath" — royal-pระ-prefixed):

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:10 | τὸν ῥυόμενον ἡμᾶς ἐκ τῆς ὀργῆς τῆς ἐρχομένης | **ผู้ทรงช่วยเราให้พ้นจากพระพิโรธที่จะมาถึง** | future-eschatological wrath (parousia-deliverance) |
| 2:16 | ἔφθασεν δὲ ἐπ’ αὐτοὺς ἡ ὀργή | **และพระพิโรธก็ได้มาถึงพวกเขา** | aorist-realized wrath (divine-vengeance-already-upon) |
| 5:9 | οὐκ ἔθετο ἡμᾶς ὁ θεὸς εἰς ὀργήν | **พระเจ้ามิได้ทรงตั้งเราไว้สำหรับพระพิโรธ** | divine-appointment-NOT-toward-wrath |

The 5:9 KD names the principle:

> πรรพิโรธ = 'wrath' (consistent with 1:10, 2:16 — divine-eschatological-judgment). The CONNECTION TO CH.4 PAROUSIA-DOCTRINE: at the parousia, believers are NOT-recipients-of-wrath but recipients-of-salvation.

**Editorial assessment:** Single-rendering **พระพิโรธ** across all three uses is principled — the royal-pระ- prefix preserves the divine-eschatological force; and the same Thai rendering ties together the Pauline rhetorical-pivot (1:10 future-wrath-believers-rescued-from ↔ 2:16 already-arriving-wrath-on-persecutors ↔ 5:9 not-appointed-to-wrath-believers). 

**Recommend: STABLE; consider new doc later** (after Romans ships, where ὀργή is densest in the corpus — Rom 1:18; 2:5, 8; 3:5; 4:15; 5:9; 9:22; 12:19; 13:4–5). For now, verse-level rationale at 5:9 is comprehensive enough.

---

## 6. πνεῦμα + ψυχή + σῶμα tripartite anthropology (5:23) — **REVIEW (rationale comprehensive at verse level)**

1 Thess 5:23 contains the **only canonical NT verse** that lists πνεῦμα + ψυχή + σῶμα together as components of the human person:

> καὶ **ὁλόκληρον** ὑμῶν τὸ **πνεῦμα** καὶ ἡ **ψυχή** καὶ τὸ **σῶμα** ἀμέμπτως ... τηρηθείη
> และขอให้**วิญญาณ** **จิตใจ** และ**ร่างกาย**ของพวกท่านถูกสงวนรักษาไว้ครบถ้วนทุกส่วนอย่างไม่มีตำหนิ

Renderings:
- **πνεῦμα → วิญญาณ** (literal "spirit"; uses anthropological vs `psyche_vs_pneuma_anthropological_2026-04.md` lock)
- **ψυχή → จิตใจ** ("mind / inner-self / heart")
- **σῶμα → ร่างกาย** ("body")

The 5:23 KD names the interpretive crux:

> FAMOUS TRIPARTITE-ANTHROPOLOGY VERSE: πνεῦμα 'spirit' + ψυχή 'soul' + σῶμα 'body.' The TRIPARTITE-vs-DICHOTOMOUS-anthropology-debate: (a) TRIPARTITE — humans have THREE distinct components (spirit + soul + body) — supported here + Heb 4:12; (b) DICHOTOMOUS — humans have TWO components (inner: combined-spirit/soul; outer: body) — Paul's other-letters often pair just-two terms. The MAJORITY-MODERN view: this is a RHETORICAL-INCLUSIVE listing for emphasis on the WHOLE-PERSON, not a precise-anthropological-tripartite-claim.

**Editorial assessment — CHECK WITH `psyche_vs_pneuma_anthropological_2026-04.md`:** The locked corpus rule (per `docs/CHAPTER_REVIEW_PROMPT.md` line 38):

> ψυχή → จิตวิญญาณ / ชีวิต (context); πνεῦμα (anthropological) → จิต — distinct from πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์

But at 1 Thess 5:23 the renderings are:
- **ψυχή → จิตใจ** (NOT จิตวิญญาณ / ชีวิต)
- **πνεῦμα → วิญญาณ** (NOT จิต)

The 5:23 case is unique because the doc-locked **ψυχή → จิตวิญญาณ** + **πνεῦμα → จิต** would COLLAPSE in this verse since จิต + จิตวิญญาณ overlap in Thai. The translator had to use a different tripartite Thai pairing (**วิญญาณ + จิตใจ + ร่างกาย**) to keep the three components LEXICALLY DISTINCT in Thai. The 5:23 KD acknowledges this implicit-departure but does not explicitly cross-reference the corpus doc.

**Other 1TH ψυχή / πνεῦμα uses:**
- 1TH 2:8 ψυχή ("our [own] lives" — apostles giving themselves) → **ชีวิต** (per locked rule, sense (b))
- 1TH 5:14 ὀλιγόψυχος ("small-souled, faint-hearted") → **ใจฝ่อ** (compound — Thai-natural for "shrunken-spirit"; preserves ψυχή as ใจ "heart/mind")
- 1TH 5:19 πνεῦμα ("the Spirit" — divine-Spirit, contextual) → **พระวิญญาณ** (royal-prefixed; per `pneuma hagion` lock-by-implication)
- 1TH 1:5, 1:6, 4:8 πνεῦμα ἅγιον → **พระวิญญาณบริสุทธิ์** (uniform; locked)

**REVIEW flag: Confirm with Ben** that the 5:23 tripartite-rendering exception (**วิญญาณ + จิตใจ + ร่างกาย**) is principled and should be amended into the existing `psyche_vs_pneuma_anthropological_2026-04.md` doc as the **single-occurrence-tripartite-listing exception**. This will recur in:
- Heb 4:12 (μερισμοῦ ψυχῆς καὶ πνεύματος "division of soul and spirit") — different context (a SEPARATING action distinguishing 2 components, NOT a 3-component rhetorical-listing)
- 1 Cor 15:44–46 (σῶμα ψυχικόν vs σῶμα πνευματικόν) — adjectival contrast, different referent

**→ Recommend: amend** `psyche_vs_pneuma_anthropological_2026-04.md` with a 1 Thess 5:23 sub-section + cite the rendering rationale + flag the rare 3-listing-exception.

---

## 7. εὐχαριστέω — Pauline thanksgiving cycles — **STABLE (extends Synoptic Lord's-Supper lock)**

1TH has **3 explicit εὐχαριστέω-cluster occurrences** — Paul's first-letter thanksgiving cycles:

| Verse | Greek | Thai |
|---|---|---|
| 1:2 | Εὐχαριστοῦμεν τῷ θεῷ πάντοτε περὶ πάντων ὑμῶν | **เราทั้งหลายขอบพระคุณพระเจ้าเสมอเพราะพวกท่านทุกคน** |
| 2:13 | καὶ ἡμεῖς εὐχαριστοῦμεν τῷ θεῷ ἀδιαλείπτως | **พวกเราจึงขอบพระคุณพระเจ้าอย่างไม่หยุดยั้ง** |
| 3:9 | τίνα εὐχαριστίαν δυνάμεθα τῷ θεῷ ἀνταποδοῦναι | **เราจะขอบพระคุณพระเจ้าได้อย่างไรเพื่อพวกท่าน** |
| 5:18 | ἐν παντὶ εὐχαριστεῖτε | **จงขอบพระคุณในทุกสถานการณ์** |

Uniform rendering **ขอบพระคุณ** ("thank — humble register") + the noun **ความขอบคุณ** at 3:9. This matches the Synoptic Lord's-Supper εὐχαριστέω → **ขอบพระคุณ / โมทนาพระคุณ** pattern (glossary auto-indexed) but here in the **Pauline-epistolary-thanksgiving** rather than the Lord's-Supper liturgical context.

**Editorial assessment:** Single-rendering **ขอบพระคุณ** (with God as object) is uniform and uses the Thai humble-register suitable for the human apostolic-1pl-voice addressing God. The 3:9 noun-form **εὐχαριστία** is rendered with the verb (ขอบพระคุณ) rather than the noun (ความขอบคุณ) — this is principled because Greek εὐχαριστία in the dative-object position with ἀνταποδίδωμι is rhetorical "what thanks can we render?" — Thai turns it into "how can we thank?" naturally.

**STABLE — no new doc needed.** Existing Synoptic Lord's-Supper εὐχαριστέω rendering is consistent with Pauline epistolary thanksgiving. Worth a one-line cross-reference noting Pauline confirmation.

---

## 8. πατήρ — divine vs human-paternal-analogy register split — **STABLE (extends GAL pattern)**

1TH has 4 πατήρ-cluster occurrences with the same principled register split as GAL:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:1 | ἐν θεῷ πατρί | **ในพระเจ้าพระบิดา** | divine (royal pระ-) |
| 1:3 | ἔμπροσθεν τοῦ θεοῦ καὶ πατρὸς ἡμῶν | **ต่อพระพักตร์พระเจ้าและพระบิดาของเรา** | divine (royal) |
| 2:11 | ὡς πατὴρ τέκνα ἑαυτοῦ | **ดุจบิดาที่ปฏิบัติต่อลูกของตน** | human-paternal analogy (plain — apostle-as-father metaphor) |
| 3:11 | ὁ θεὸς καὶ πατὴρ ἡμῶν | **พระเจ้าและพระบิδาของเราเอง** | divine (royal) |
| 3:13 | ἔμπροσθεν τοῦ θεοῦ καὶ πατρὸς ἡμῶν | **ต่อพระพักตร์พระเจ้าและพระบิดาของเรา** | divine (royal) |

**Editorial assessment:** Compliance with `narrator_vs_character_voice_2026-04.md` is exact:
- Divine πατήρ → **พระบิδา** (royal pระ- prefix). 4 occurrences uniform.
- Human-paternal πατήρ in apostolic-self-portrait analogy (2:11) → **บิδา** (plain register, no royal prefix).

The 2:11 analogy is the parallel to GAL 4:2's Greco-Roman household-father analogy — both use the plain Thai **บิดา** correctly (see GAL audit §5). The 1TH 2:7–12 paternal-imagery cluster is **especially distinctive** — Paul juxtaposes a **maternal** image (2:7 τροφός θάλπῃ τὰ ἑαυτῆς τέκνα → **แม่ที่กำลังเลี้ยงดูลูกของตนด้วยความทะนุถนอม**) with the **paternal** image (2:11 ὡς πατὴρ τέκνα ἑαυτοῦ → **ดุจบิδาที่ปฏิบัติต่อลูกของตน**) — both plain register since both are apostolic-self-portrait analogies, NOT divine-Father references. Compliant.

**STABLE — no new doc needed.** GAL audit §5 already covers the principle. 1TH provides confirmation across a second Pauline letter.

---

## 9. ἐκκλησία / ἀπόστολος / ἀδελφοί — Pauline epistolary vocabulary — **all LOCKED ✓**

| Lemma | 1TH evidence | Status |
|---|---|---|
| ἐκκλησία (2 verses, Christian community) | 1:1 (τῇ ἐκκλησίᾳ Θεσσαλονικέων → **คริสตจักรของชาวเธสะโลนิกา**); 2:14 (τῶν ἐκκλησιῶν τοῦ θεοῦ τῶν οὐσῶν ἐν τῇ Ἰουδαίᾳ → **คริสตจักรทั้งหลายของพระเจ้าในแคว้นยูเดีย**) — uniform. **Note:** This is the FIRST PAULINE NARRATIVE USE of "the church of [city name]" formula — distinctive of the Pauline-epistolary-greeting tradition. | **LOCKED** per `ekklesia_2026-04.md` |
| ἀπόστολος (1 verse) | 2:7 (ὡς Χριστοῦ ἀπόστολοι → **ในฐานะอัครทูตของพระคริสต์**) — uniform with GAL. | **LOCKED** (Synoptic-Acts-GAL pattern) |
| ἀδελφοί (Pauline vocative — 17 verses) | 1:4, 2:1, 2:9, 2:14, 2:17, 3:2, 3:7, 4:1, 4:6 (sense-shift = "fellow-believer at issue, not vocative"), 4:10 (×2), 4:13, 5:1, 5:4, 5:12, 5:14, 5:25, 5:26, 5:27 — uniform **พี่น้อง / พี่น้องทั้งหลาย**. **Note:** 1TH uses the vocative **ἀδελφοί** with the highest density per chapter in the Pauline corpus (avg ~3.4 per chapter; 17 / 5). The Thai rendering preserves the warm-pastoral force. | **LOCKED** |

**LOCKED** ✓ — second-Pauline-epistle compliance with the GAL-Synoptic-Acts-Johannine corpus.

---

## 10. εἰρήνη — Pauline peace formula + ὁ θεὸς τῆς εἰρήνης — **STABLE (extends GAL pattern)**

1TH has the salutation εἰρήνη at 1:1 and the closing "God of peace" formula at 5:23:

| Verse | Greek | Thai |
|---|---|---|
| 1:1 | χάρις ὑμῖν καὶ εἰρήνη | **ขอพระคุณและสันติสุขจงดำรงอยู่กับท่านทั้งหลาย** |
| 5:3 | ὅταν λέγωσιν· Εἰρήνη καὶ ἀσφάλεια | **ขณะที่ผู้คนกำลังพูดว่า ‘สันติสุขและความปลอดภัย’** (false-peace, world-context) |
| 5:13 | εἰρηνεύετε ἐν ἑαυτοῖς | **จงอยู่อย่างสันติสุขท่ามกลางกันและกัน** (verbal-form, intramural-peace imperative) |
| 5:23 | ὁ θεὸς τῆς εἰρήνης | **พระเจ้าแห่งสันติสุข** |

**Editorial assessment:** Single-rendering **สันติสุข** ("peace + happiness") for εἰρήνη across all four uses is principled and matches the GAL salutation rendering. The 5:23 ὁ θεὸς τῆς εἰρήνης → **พระเจ้าแห่งสันติสุข** is a Pauline formula that recurs (Rom 15:33; 16:20; Phil 4:9; 2 Thess 3:16; Heb 13:20) — locking this rendering here is forward-pertinent.

**STABLE — no new doc needed.** Glossary index for σαντι- terms covers the rendering. Worth a one-line cross-reference in any future Pauline-formulae doc.

---

## 11. OT echoes / allusions — Pauline density — **all flagged + 1 LOGGED**

1TH has **1 explicit OT-allusion logged** in `data/nt_ot_citations.json`:

| 1TH | OT source | Status |
|---|---|---|
| 5:8 | Isa 59:17 (LXX divine-warrior armor adapted) | **LOGGED** — Note explains Pauline-modification (Isaiah's breastplate-of-righteousness becomes faith-and-love; Isaiah's helmet-of-salvation becomes hope-of-salvation) |

**Additional unflagged echoes (allusions, not formal citations):**

| 1TH | Echoed text | Notes |
|---|---|---|
| 4:5 | Ps 79:6 / Jer 10:25 (LXX echo: ἔθνη τὰ μὴ εἰδότα τὸν θεόν "Gentiles who do not know God") | Verse-level rendering preserves the LXX formula faithfully (**คนต่างชาติที่ไม่รู้จักพระเจ้า**); not formally cited |
| 5:2 | Joel + Amos + Zeph "Day of YHWH" formula | Recognized as OT-prophetic technical term in 5:2 KD; not a single-source citation |
| 4:16 | Dan 7:13 cloud + descent imagery; Ex 19:13 trumpet | Eschatological-cloud-imagery noted in 4:17 KD |
| 2:16 | Dan 8:23 / Gen 15:16 "iniquity-filling-up-to-judgment" pattern | Acknowledged in 2:16 KD ("OT-PROPHETIC: a measure of sin filling-up to its capacity, after which divine-judgment falls") |
| 4:6 | Deut 32:35 / Ps 94:1 LXX divine-vengeance language | Acknowledged in 4:6 KD (ἔκδικος κύριος = "avenger of these things") |

**Recommend (low priority):** Add 4:5 (Ps 79:6 / Jer 10:25 echo) and 5:2 (Day-of-YHWH composite) to `data/nt_ot_citations.json` as `type: "allusion"` or `type: "thematic_echo"` entries. Not blocking; verse-level KDs already capture the rationale.

---

## 12. Inherited locks — **all compliant**

| Doc | 1TH evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 1:1, 2:14 → **คริสตจักร** uniform. | **LOCKED** |
| `ethnos_2026-04.md` | 2:16 (κωλυόντων ἡμᾶς τοῖς ἔθνεσιν → **คนต่างชาติ**, Pauline-mission category); 4:5 (καθάπερ καὶ τὰ ἔθνη τὰ μὴ εἰδότα τὸν θεόν → **คนต่างชาติที่ไม่รู้จักพระเจ้า**, Gentile-pagan-religious category — same rendering, different sense). Both compliant per the doc's three-way rule (ประชาชาติ / ชนชาติ / คนต่างชาติ). | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 1TH has **6+ narrator-κύριος references** (1:1, 1:3, 1:6, 1:8, 2:15, 3:11, 3:12, 4:6, 4:15, 4:16, 4:17, 5:2, 5:9, 5:12, 5:23, 5:27, 5:28) — all → **องค์พระผู้เป็นเจ้า**, perfectly compliant with the lock. The narrative-non-applicability concern of the doc's "Lukan-Acts signature" framing is now further-confirmed-Pauline; **amendment-needed** as already noted in JHN audit + GAL audit. | **LOCKED-with-amendment-needed** (already noted in JHN + GAL audits) |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A in 1TH — no vocative κύριε in this letter (epistolary, not narrative). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | N/A in 1TH — no doxological praise-verb-with-God-object constructions in this letter. | **LOCKED (N/A)** |
| `honorifics_non_divine_authorities_2026-04.md` | N/A in 1TH — minimal non-divine-authority figures. Σιλουανός / Τιμόθεος in 1:1 are co-senders (plain register, no royal). Σατανᾶς in 2:18 is plain register **ซาตาน** (correct — adversary not honored). | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout; plain register for human authorities + co-senders + the human-paternal analogy at 2:11 (per §8 above). Compliant. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | **N/A in 1TH** — no Aramaic embeds in this letter (no Αββα; no Μαραναθα — 1 Cor 16:22 is the locked occurrence ahead). | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A in 1TH** — no Tier 1/2/3 inclusion variants in 1 Thessalonians (no `output/textual_variants/1thessalonians*` files; no `[`/`⟦` markers in the Greek; full text-scan confirmed). Two verse-level **micro-variants** flagged in KDs (2:7 ἤπιοι vs νήπιοι; 3:2 συνεργὸν τοῦ θεοῦ vs διάκονον τοῦ θεοῦ vs combined). Both followed SBLGNT per RULES §0; flagged in verse Notes; not requiring inclusion-bracket policy. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — 1 Thess is a doctrinal-pastoral letter, not narrative; no historic-present pattern to test. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in 1TH. The 5:2 "thief in the night" image is a SIMILE for the parousia's surprise-arrival, not a parable with a transparent God-figure (the thief-image is NOT a divine-actor analogy; it is a surprise-arrival simile). Compliant. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — μετανοέω + μεταμέλομαι BOTH absent from 1TH (the conversion-vocabulary at 1:9 ἐπεστρέψατε πρὸς τὸν θεὸν ἀπὸ τῶν εἰδώλων → **กลับใจจากรูปเคารพหันมาหาพระเจ้า** uses ἐπιστρέφω "turn / convert," correctly rendered with the **กลับใจ ... หันมา** locked combination). | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | **N/A** — ἄφεσις absent from 1TH (the lemma is salvific-narrative; 1TH's atonement-language is δι' Ἰησοῦ at 4:14, διὰ τοῦ κυρίου ἡμῶν Ἰησοῦ Χριστοῦ at 5:9, not ἄφεσις). | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | 1TH 1:9 (ἀπὸ τῶν εἰδώλων δουλεύειν θεῷ ζῶντι καὶ ἀληθινῷ → **กลับใจจากรูปเคารพหันมาหาพระเจ้าเพื่อรับใช้พระเจ้าผู้ทรงพระชนม์**). The pagan idols are rendered **รูปเคารพ** ("idolatrous-images") — NOT พระเจ้า (reserved for the biblical God). The contrasting "living and true God" preserves the Hellenistic-pagan-vs-Christian-God polemic. Compliant. | **LOCKED** |
| `roman_administrative_titles_2026-04.md` | N/A — no Roman titles in 1TH (no governor/centurion/proconsul). | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from 1TH (the closest Christological title here is Ἰησοῦν τὸν υἱὸν αὐτοῦ at 1:10 → **พระบุตรของพระองค์**; "Son of God / Son of the Father," not Son-of-Man). | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (3 occurrences: 1:5, 1:6, 4:8) → **พระวิญญาณบริสุทธิ์** uniform. Anthropological πνεῦμα (5:19 + 5:23) → see §6 — the 5:23 tripartite-listing exception flagged for doc-amendment. ψυχή (2:8 self-giving lives → **ชีวิต**; 5:23 tripartite → **จิตใจ**; 5:14 ὀλιγόψυχος compound → **ใจฝ่อ**) — see §6. | **LOCKED-with-amendment-needed** (5:23 tripartite-exception) |
| `johannine_doubled_amen_2026-04.md` | N/A — 1TH is Pauline, not Johannine. No ἀμήν in 1TH. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply (no Jesus-direct-discourse in 1TH). | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries-addressing-divine in 1TH. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | 1TH 2:12 (εἰς τὴν ἑαυτοῦ βασιλείαν καὶ δόξαν → **อาณาจักรและพระสิริของพระองค์**) — consistent with the Synoptic-Acts-GAL lock. 1 verse only; compliant. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | 1TH 1:10 (τὸν υἱὸν αὐτοῦ ἐκ τῶν οὐρανῶν → **พระบุตรของพระองค์จากฟ้าสวรรค์**) — theological-default ฟ้าสวรรค์; 4:16 (καταβήσεται ἀπ' οὐρανοῦ → **เสด็จลงมาจากสวรรค์**) — after-possessor sense รค์ (truncated form). Both compliant per the doc. | **LOCKED** |

---

## Mechanical (§1) — **all green**

- 5/5 chapters: `output/check_reports/1thessalonians_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓ (chs 1–4 on `end-of-book-review-galatians` loop branch; ch 5 on `end-of-book-review-galatians-audit`; both reachable from this audit branch's parent commit chain)
- 5/5 chapters: `output/back_translations/1thessalonians_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-119-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: only re-ran-check artifacts (key_term_consistency_all.md + phrase_consistency.md modified by my §1 verification re-runs). No 1TH source-file dirt.

---

## Pre-existing docs affirmed / unchanged

All 24 docs in `docs/translator_decisions/` reviewed. Compliance summary in §12 above. The **Lukan-Acts narrator-κύριος doc** flagged for amendment (already noted in JHN + GAL audits) — 1 Thessalonians provides a third independent Pauline-corpus confirmation; the doc's "Lukan signature" framing should be renamed/extended to acknowledge corpus-wide narrator-κύριος usage in JHN + GAL + 1TH (and forward-Pauline). The **psyche_vs_pneuma_anthropological doc** flagged for sub-section amendment to handle the 1 Thess 5:23 tripartite-listing exception (see §6).

---

## Flagged for Ben's attention

### A. παρουσία rendering (การเสด็จมา) lift to corpus doc — **STABLE, lift to corpus doc** (§1)
The 4-occurrence-per-5-chapter density makes 1TH the locking-precedent for the Pauline-corpus παρουσία. Lift to corpus doc `parousia_christou_2026-04.md` before 2 Thess 2:1–9 (where παρουσία recurs in the densest cluster + the polemical παρουσία τοῦ ἀνόμου non-Christ use).

### B. ἁγιασμός / ἁγιωσύνη / ἀκαθαρσία cluster — **STABLE, lift to corpus doc** (§2)
The principled Greek-aspectual split (process vs state vs binary-opposite) is doctrinally rich. Lift to corpus doc `hagiasmos_hagiosune_2026-04.md` before Rom 6:19, 22 (densest ἁγιασμός cluster) and Heb 12:14.

### C. ἁρπάζω + 1 Thess 4:16–17 rapture-vocabulary cluster — **STABLE, consider brief doc** (§3)
The theologically-neutral ถูกรับขึ้นไป rendering avoids importing the dispensationalist English "rapture" framing. Brief corpus doc would lock the rendering before 1 Cor 15:51–52 (the parallel rapture-passage with σαλπίσει + ἀλλαγησόμεθα).

### D. ἡμέρα κυρίου lift to corpus doc — **STABLE, lift to corpus doc** (§4)
The OT-prophetic technical-term rendering วันแห่งองค์พระผู้เป็นเจ้า is locked. Lift to corpus doc `hemera_kyriou_2026-04.md` before 2 Thess 1:10 + 2:2 (the 2:2 κυρίου / Χριστοῦ textual variant).

### E. πνεῦμα + ψυχή + σῶμα tripartite at 5:23 — **REVIEW** (§6)
The single-occurrence tripartite-listing necessitates a different Thai-pairing (วิญญาณ + จิตใจ + ร่างกาย) than the corpus-locked psyche/pneuma split (จิตวิญญาณ / จิต). Worth Ben's confirmation + amendment to existing `psyche_vs_pneuma_anthropological_2026-04.md` doc.

### F. σκεῦος "vessel" at 4:4 — **DECIDE** (§ below; see external review item)
1 Thess 4:4 σκεῦος has two well-attested readings: (a) BODY ("control your own body") — modern majority + current Thai (**ครอบครองร่างกายของตนเอง**); (b) WIFE ("acquire a wife in honor") — older view, supported by κτάομαι semantic + 1 Pet 3:7. Verse-level KD acknowledges both. Worth Ben's confirmation that (a) is the corpus-default.

### G. πάντων τῶν ἁγίων αὐτοῦ at 3:13 — **DECIDE** (angels vs saints crux)
The 3:13 KD names three readings: (a) ANGELS (cf. Matt 25:31); (b) DEPARTED BELIEVERS (most modern commentators); (c) BOTH. Current Thai **วิสุทธิชนทุกคน** ("all his holy ones / saints") leans toward (b) but preserves angelic-reading-possibility through the inclusive **ทุกคน**. Worth Ben's confirmation, especially given Jude 14 παρουσία ἁγίαις μυριάσιν echo (where angels are clearly in view).

### H. 1 Thess 2:14–16 anti-Jewish-polemic / interpolation question — **DECIDE** (textual-historical question)
1 Thess 2:14–16 is one of the most contested passages in Pauline studies for the proposal that vv. 14–16 are a **post-AD-70 interpolation** (the "wrath has come upon them εἰς τέλος" reading naturally as the AD-70 destruction of Jerusalem, which post-dates Paul). The translator follows SBLGNT (which retains the verses as authentic) and renders εἰς τέλος → **ในขั้นสุด** ("to the final / utmost extent") — the verse-level KD acknowledges the interpolation-debate but does not flag it for the reader. Worth Ben's confirmation that the SBLGNT-text-as-authentic stance is the corpus-default + whether a footer-note acknowledging the academic interpolation-debate should be added (likely no, per RULES §0 evangelical-Protestant alignment + SBLGNT default).

### I. New corpus docs to write (before 2 Thessalonians 1:7–10 + Romans)
1. **`docs/translator_decisions/parousia_christou_2026-04.md`** (§1) — locks **การเสด็จมา** rendering
2. **`docs/translator_decisions/hagiasmos_hagiosune_2026-04.md`** (§2) — locks the sanctification cluster
3. **`docs/translator_decisions/hemera_kyriou_2026-04.md`** (§4) — locks **วันแห่งองค์พระผู้เป็นเจ้า** rendering
4. **(Optional)** `rapture_event_vocabulary_2026-04.md` (§3) — brief; before 1 Cor 15:51–52
5. **(Optional)** `parousia_anthropomorphic_imagery_2026-04.md` — brief; covers 4:16 cluster (κέλευσμα + ἀρχάγγελος + σάλπιγξ θεοῦ + νεφέλαι + ἀπάντησις + ἀέρ) before 1 Cor 15 + Rev 8–11 trumpets
6. **(Optional)** `pater_pauline_register_2026-04.md` — Pauline-confirmation extension of the existing narrator-vs-character doc

### J. Existing docs to amend
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to "Lukan-Acts + Johannine + Pauline (Galatians + 1TH)." JHN + GAL audits already flagged; 1TH provides the third independent Pauline confirmation.
- **`psyche_vs_pneuma_anthropological_2026-04.md`** — add 1 Thess 5:23 tripartite-listing-exception sub-section (§6).

### K. External AI review (§3 of checklist) — **pending**
Recommended before `book-1thessalonians-v1` tag. Suggested 4-cluster external AI packet:
1. **1TH 1:1–10** — opening + thanksgiving + gospel-spread + parousia-anticipation (1:10 wrath-deliverance + Son-from-heaven)
2. **1TH 4:1–8** — sanctification cluster + πορνεία + σκεῦος-crux + Spirit-rejection-warning
3. **1TH 4:13–18** — the rapture-passage + παρουσία + ἁρπάζω + κέλευσμα/ἀρχάγγελος/σάλπιγξ cluster
4. **1TH 5:1–11 + 5:23** — Day of the Lord + sons-of-day + armor-of-Isaiah + tripartite-anthropology benediction

Use Grok + ChatGPT in parallel per the JHN/GAL pattern.

---

## Recommendation

**1 Thessalonians ships in strong corpus-hygiene shape — and provides the Pauline-eschatology-vocabulary entry-point for the corpus.** The translator made consistent, principled choices on the five most-significant 1TH-introduced lemma-clusters (παρουσία; ἁγιασμός cluster; ἁρπάζω; ἡμέρα κυρίου; tripartite anthropology) — and **none of these five has a corpus-level doc** yet. This is the moment to lock them in before 2 Thessalonians compounds the editorial weight (esp. the 2 Thess 2:1–9 παρουσία-cluster + 2 Thess 1:7–10 ἀπό-question + 2 Thess 2:13 ἁγιασμός recurrence).

Tag `book-1thessalonians-v1` after:
1. Ben's decisions on **§F + §G + §H** (DECIDE items: σκεῦος body-vs-wife at 4:4; ἁγιοι angels-vs-saints at 3:13; 2:14–16 interpolation handling)
2. Ben's confirmation on **§E** (REVIEW item: 5:23 tripartite-listing rendering exception)
3. Three-to-five new translator_decisions docs written (§I items 1–3 minimum; optionally 4–6)
4. Two existing docs amended (`kyrios_narrator_voice_luke_acts_2026-04.md`; `psyche_vs_pneuma_anthropological_2026-04.md`)
5. External AI sanity-check (§K)

The Pauline letters (2 Thess in flight, then Rom, 1–2 Cor, Eph, Phil, Col, Pastorals) can be queued for next book — but writing **`parousia_christou`, `hagiasmos_hagiosune`, and `hemera_kyriou`** docs should happen **before 2 Thess 1:7** to avoid forward drift in the eschatology-vocabulary that 2 Thess will compound dramatically.
