# 1 Peter — End-of-Book Review

**Date:** 2026-05-03
**Scope:** All 5 chapters (105 verses; verse-level `key_decisions` across the corpus); `glossary.json`; existing `docs/translator_decisions/` (44 docs).
**Trigger:** 1PE 5 shipped (commit `2204c75` for source/checks/reader; inclusion-variant resolution for 1:22 in `953f313`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 5/5 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status` shows only un-tracked Paratext exports (untouched by this audit).
- **1 Peter is the FIRST FULL Petrine epistle the project has shipped** and the second Catholic-Epistle (after James). It introduces a major **NEW corpus-cross-cutting cluster: Petrine SUFFERING-AND-EXILE THEOLOGY** (πάσχω / πάθημα — densest in NT; παρεπίδημος / πάροικος / διασπορά / παροικία sojourner-frame) — anchored to a thoroughly OT-saturated ecclesiology (1 Pet 2:4-10's stone-cluster Isa 28:16 + Ps 118:22 + Isa 8:14 mosaic, plus the four-fold Sinai/Israel formula at 2:9 from Isa 43:20-21 + Exod 19:6).
- **The most theologically-contested passages in the entire NT cluster here**: 3:18-22 (Christ's preaching to the spirits in prison + flood-as-baptism-typology) and 4:6 (gospel-preached-to-the-dead). Translator chose **lexical-ambiguity-preservation** at 3:19 (multiple interpretations stay open in Thai as in Greek) and **explicit disambiguation** at 4:6 (added "ผู้ที่บัดนี้ตายไปแล้ว" = "those who are now dead" to rule out a postmortem-evangelism reading). These are opposite editorial strategies in adjacent passages — worth Ben's confirmation.
- **20 inherited locks verified compliant** in 1PE (ekklesia-by-implication, ethnos, narrator-κύριος, psyche/pneuma, ἁγιασμός, divine-object praise verbs, narrator-vs-character voice, pagan deities, pastoral_corpus_locks ambiguity-preservation, aphesis N/A, etc. — see §17).
- **5 cross-cutting Petrine patterns are STABLE-but-undocumented at corpus level** (πάσχω/πάθημα suffering cluster; παρεπίδημος-πάροικος sojourner-frame; ἀναστροφή signature ethic; ποιμήν/ἀρχιποίμην shepherd Christology; ἀναγεννάω new-birth). Lifting these to corpus docs is recommended before 2 Peter and Hebrews ship.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: 2:9 βασίλειον ἱεράτευμα single-concept "royal priesthood" rendering; 3:7 σκεῦος → "ภาชนะ" wife-as-vessel — different from the 1TH 4:4 σκεῦος-as-body reading; 5:13 Βαβυλών as transliteration with Rome-metaphor only in summary).
- **3 items flagged DECIDE** (1 Pet 3:19 spirits-in-prison interpretation; 1 Pet 4:6 dead-evangelism explicit disambiguation; 1 Pet 3:21 baptism ἀντίτυπον + ἐπερώτημα framing).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. πάσχω / πάθημα — Petrine suffering theology (NT-densest cluster) — **STABLE (undocumented; recommend new doc — high Catholic-Epistles-forward priority)**

1 Peter contains the **densest πάσχω + πάθημα cluster per chapter in the entire NT** — the lemma-pair occurs **15× across 5 chapters** (πάσχω 8×, πάθημα 7×). The translator implements a uniform two-pronged rendering:

| Greek lemma | Thai | Subject | Verses |
|---|---|---|---|
| πάσχω (verb, Christ-subject) | **ทรงทนทุกข์** (royal-prefix passive of suffering) | Christ | 2:21, 2:23, 3:18, 4:1 |
| πάσχω (verb, believers-subject) | **ทนทุกข์** (plain register) | believers | 2:19, 2:20, 3:14, 3:17, 4:19 |
| πάθημα (noun, "suffering / passion") | **การทนทุกข์** | both | 1:11, 4:13, 5:1, 5:9 |
| πάσχω (subst. participle, "the one who suffered") | **ผู้ที่ได้ทนทุกข์** | believer-paradigm | 4:1b |
| πάσχω (aorist, generic past) | **ทนทุกข์เพียงชั่วครู่** | believer-eschatological | 5:10 |

The 2:21 KD names the principle:

> πάσχω → ทรงทนทุกข์ (royal-prefix). The substitutionary-paradigm (Χριστός ἔπαθεν ὑπὲρ ὑμῶν 'Christ suffered for you') sets the suffering-Christology that the entire letter develops.

**Editorial assessment:** The **register-split between divine-Christ-suffering (royal ทรงทนทุกข์) and human-believer-suffering (plain ทนทุกข์)** is principled and theologically rich. It preserves the Petrine-Christological-paradigm: Christ's suffering is *paradigmatic* (royal-divine-act) and believers' suffering is *participatory* in his (plain register, sharing-in not equating-to). The 4:13 κοινωνεῖτε τοῖς τοῦ Χριστοῦ παθήμασιν ("you share in the sufferings of Christ") binds the two registers together at the κοινωνία level — the believers' plain-register **ทนทุกข์** is *participation* in the royal-register **ทรงทนทุกข์**.

The 1:11 KD anchors the OT-rooting:

> The suffering-then-glory pattern of Christ's passion is the NT-rereading of ISA 53 + LUK 24:26 same suffering-glory sequence.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/pascho_pathema_suffering_2026-05.md` before:
- **2 Peter** (where ἀπώλεια / κρίσις / σωτηρία dominate but Christ's παθήματα recur)
- **Hebrews** (Heb 2:10, 5:8, 9:26 — Christ's sufferings; Heb 13:12 — outside-the-camp suffering)
- **Acts** (already shipped — but the corpus-Pauline ἔπαθεν renderings would benefit from cross-reference)

The doc should:
1. Lock πάσχω (Christ-subject) → **ทรงทนทุกข์** (royal-divine-passive)
2. Lock πάσχω (believer-subject) → **ทนทุกข์** (plain-participatory)
3. Lock πάθημα → **การทนทุกข์** (process-noun, both subjects)
4. Note the participatory-paradigm at 4:13 (κοινωνεῖτε ... παθήμασιν)
5. Cite 1 Pet 2:21 + 4:13 + 5:1 as the locking precedents
6. Cross-reference Pauline-corpus παθήματα (Rom 8:18; 2 Cor 1:5-7; Phil 3:10; Col 1:24)

---

## 2. παρεπίδημος / πάροικος / διασπορά / παροικία — Petrine sojourner-exile identity-frame — **STABLE (undocumented; recommend new doc)**

The Petrine sojourner-cluster runs **5×** across the letter, framing the entire epistle as written to "exiles":

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 1:1 | ἐκλεκτοῖς παρεπιδήμοις διασπορᾶς | **ผู้ที่ทรงเลือกสรรและเป็นคนต่างถิ่นกระจัดกระจายอยู่** | letter-opening identity (sojourners-in-dispersion) |
| 1:17 | τὸν τῆς παροικίας ὑμῶν χρόνον | **ตลอดเวลาที่ท่านพำนักอยู่ในต่างถิ่น** | the time of your sojourning |
| 2:11 | παροίκους καὶ παρεπιδήμους | **คนต่างถิ่นและคนพำนักชั่วคราว** | strangers and temporary residents |
| 5:13 | ἡ ἐν Βαβυλῶνι συνεκλεκτή | **คริสตจักรที่อยู่ในบาบิโลน ผู้ที่ทรงเลือกสรรร่วมกับท่านทั้งหลาย** | Babylon = sojourner-Rome metaphor |

The 1:1 KD names the principle:

> Per uW figs-metaphor: παρεπίδημος 'sojourning-foreigner' → คนต่างถิ่น (resident-aliens). διασπορά → กระจัดกระจาย corpus-precedent JAS 1:1 same lemma same Thai-pattern. Render preserves the dual-identity (chosen + sojourners-in-dispersion) — ecclesiological-metaphor that frames the entire letter.

**Editorial assessment:** The Thai consistently distinguishes:
- **παρεπίδημος** (the *passing-through* sojourner — Heb. גֵּר־וְתוֹשָׁב Gen 23:4 LXX) → **คนต่างถิ่น** (foreigner-from-elsewhere)
- **πάροικος** (the *resident-alien with limited rights*) → **คนพำนักชั่วคราว** (temporary-resident) at 2:11; subsumed into the broader **คนต่างถิ่น** at 1:1
- **διασπορά** (the dispersion as a place / collective) → **กระจัดกระจายอยู่** (scattered)
- **παροικία** (abstract "sojourning-time") → **เวลาที่ท่านพำนักอยู่ในต่างถิ่น** (the time you stay as foreigners)

**The Petrine-distinctive theological move** — Peter applies the OT-Israel diaspora-sojourner identity to **Gentile-Christians** (per uW FRONT note at 1:1) — is preserved in the Thai. The five-province addressee-list (1:1) confirms this is *not* a literal Jewish-diaspora letter but an ecclesiological reframing.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/parepidēmos_paroikos_sojourner_2026-05.md` before Hebrews 11:13 (the great sojourners-passage: ξένοι καὶ παρεπίδημοι) + Hebrews 13:14 (οὐ γὰρ ἔχομεν ὧδε μένουσαν πόλιν). The doc should:
1. Lock παρεπίδημος → **คนต่างถิ่น**
2. Lock πάροικος → **คนพำนักชั่วคราว** (or **คนต่างถิ่น** when paired-and-collapsed)
3. Lock διασπορά → **กระจัดกระจาย** (matching JAS 1:1 corpus precedent)
4. Lock παροικία (abstract noun) → **เวลาที่ ... พำนักอยู่ในต่างถิ่น** (verbal-paraphrase)
5. Cross-reference JAS 1:1 (twelve-tribes-in-διασπορά) and Heb 11:13 (the patriarchs-as-sojourners)
6. Cite 1 Pet 1:1 as the locking precedent

---

## 3. ἀναστροφή — Petrine "conduct / way-of-life" signature ethic — **STABLE (undocumented; consider doc)**

ἀναστροφή occurs **6× in 1 Peter** (1:15, 1:18, 2:12, 3:1, 3:2, 3:16) — more than in any other NT book. Uniform rendering **ความประพฤติ** (noun) / **ประพฤติ** (verbal) across all six:

| Verse | Greek | Thai |
|---|---|---|
| 1:15 | ἐν πάσῃ ἀναστροφῇ γενήθητε | **ในความประพฤติทุกประการ** |
| 1:17 | τὸν τῆς παροικίας ὑμῶν χρόνον ἀναστράφητε | **จงประพฤติด้วยความยำเกรง** (verbal form) |
| 1:18 | ἐλυτρώθητε ἐκ τῆς ματαίας ὑμῶν ἀναστροφῆς πατροπαραδότου | **จากความประพฤติที่ไร้ค่าซึ่งสืบทอดมาจากบรรพบุรุษ** |
| 2:12 | τὴν ἀναστροφὴν ὑμῶν ἐν τοῖς ἔθνεσιν ἔχοντες καλήν | **จงประพฤติอย่างดีในหมู่คนต่างชาติ** |
| 3:1 | διὰ τῆς τῶν γυναικῶν ἀναστροφῆς ἄνευ λόγου | **โดยความประพฤติของภรรยา โดยไม่ต้องใช้คำพูด** |
| 3:2 | τὴν ἐν φόβῳ ἁγνὴν ἀναστροφὴν ὑμῶν | **ความประพฤติอันบริสุทธิ์ด้วยความยำเกรงของท่าน** |
| 3:16 | τὴν ἀγαθὴν ... ἀναστροφήν | **ความประพฤติดี** |

**Editorial assessment:** The single-rendering **ความประพฤติ** is uniform and pivots cleanly between contexts (holy / pre-conversion-pagan / among-Gentiles / wifely / godly). Petrine ethical-rhetoric is built on this lemma; the Thai preserves the through-line.

**Recommend: STABLE — verse-level rationale comprehensive.** No new corpus-doc strictly needed; Pauline-corpus already uses the same Thai-rendering at Gal 1:13 (`ἐν τῷ Ἰουδαϊσμῷ → ความประพฤติของข้าพเจ้าในศาสนายูดาย`) and Eph 4:22 / 1 Tim 4:12 (parallel ἀναστροφή renderings). A one-line cross-reference in any future Pauline-ethics-formulae doc would suffice.

---

## 4. 1 Pet 2:9 — γένος ἐκλεκτόν / βασίλειον ἱεράτευμα / ἔθνος ἅγιον / λαὸς εἰς περιποίησιν — **REVIEW (the four-fold Sinai/Israel formula applied to the Church)**

The strongest NT-Petrine ecclesiology — Exod 19:6 LXX + Isa 43:20-21 LXX composite citation:

> Ὑμεῖς δὲ **γένος ἐκλεκτόν**, **βασίλειον ἱεράτευμα**, **ἔθνος ἅγιον**, **λαὸς εἰς περιποίησιν**

> แต่ท่านทั้งหลายเป็น "**ชนชาติที่ทรงเลือกสรร** เป็น**ปุโรหิตหลวง** เป็น**ชนชาติบริสุทธิ์** เป็น**ประชากรเป็นของพระองค์เอง**"

The 2:9 KD names the interpretive crux:

> HAPAX βασίλειον (only here NT, neuter-noun 'royal-something') — per uW: either (1) royal-priesthood as appositional (Exod 19:6 LXX βασίλειον ἱεράτευμα), or (2) two distinct titles 'a royal-realm + priesthood.' Render 'ปุโรหิตหลวง' — preserves the royal-priesthood single-concept reading (mainstream evangelical).

**Editorial assessment — REVIEW** the **βασίλειον ἱεράτευμα → ปุโรหิตหลวง** single-concept choice:
- (a) **Single-concept "royal priesthood"** — *current Thai*. Reads βασίλειον adjectivally. Mainstream English (NIV/ESV/CSB/NASB).
- (b) **Two distinct titles "royal house, priesthood"** — Reads βασίλειον as a substantive (a "royal-house / royal-realm" — cf. βασίλειον in classical Greek for "palace"). NRSV's earlier choice; some Catholic tradition.
- The translator chose (a) consistent with mainstream-evangelical alignment per RULES §0. Worth Ben's confirmation.

The other three titles read uniformly:
- **γένος ἐκλεκτόν** → **ชนชาติที่ทรงเลือกสรร** (same root as 1:1 ἐκλεκτοῖς; corpus-internal-link)
- **ἔθνος ἅγιον** → **ชนชาติบริสุทธิ์** (NB: same Thai **ชนชาติ** for both γένος and ἔθνος — flattens the lexical distinction; ethnos_2026-04.md doc context-dependent rendering)
- **λαὸς εἰς περιποίησιν** → **ประชากรเป็นของพระองค์เอง** (same Thai-pattern as Tit 2:14 περιούσιος; corpus-internal-link)

The **γένος / ἔθνος → ชนชาติ collapse** is principled (the Thai language doesn't easily distinguish "race" from "nation/people-group" at this register), but worth noting for the audit.

**Recommend: REVIEW the βασίλειον single-vs-dual rendering.** Either way, a brief corpus-doc `docs/translator_decisions/petrine_priesthood_2_9_2026-05.md` would lock the choice before any Revelation 1:6 / 5:10 / 20:6 renderings of ἐποίησεν αὐτοὺς ... βασιλείαν, ἱερεῖς (where the SAME Exod 19:6 root is reused with different syntax — βασιλείαν as accusative-noun, ἱερεῖς as plural — making the priesthood-as-realm reading explicit there).

---

## 5. 1 Pet 2:4-8 stone-cluster OT mosaic — **all LOCKED ✓**

The Petrine application of three OT stone-texts (Isa 28:16 + Ps 118:22 + Isa 8:14) to Christ + Church:

| Verse | OT source | Thai | Status |
|---|---|---|---|
| 2:6 | Isa 28:16 LXX (cornerstone in Zion) | **"ดูเถิด เราวางศิลาก้อนหนึ่งไว้ในศิโยน เป็นศิลามุมเอกที่ทรงเลือกและล้ำค่า"** | **LOGGED** — same Thai-pattern as ROM 9:33 + ROM 10:11 (corpus-internal-link) |
| 2:7 | Ps 118:22 LXX (rejected stone → cornerstone) | **"ศิลาที่ช่างก่อสร้างได้ทอดทิ้ง ได้กลายเป็นศิลามุมเอก"** | **LOGGED** — same Thai-pattern as MAT 21:42 / MAR 12:10 / LUK 20:17 / ACT 4:11 (Synoptic-Acts corpus-internal-link) |
| 2:8 | Isa 8:14 LXX (stumbling-stone) | **"ศิลาแห่งการสะดุดและหินแห่งเหตุสะดุด"** | **LOGGED** — same Thai-pattern as ROM 9:32 (corpus-internal-link) |

**Editorial assessment:** The translator preserves **distinct Thai-words for distinct Greek-lexemes within the parallel pair λίθος προσκόμματος + πέτρα σκανδάλου** (**ศิลา-การสะดุด** + **หิน-เหตุสะดุด**) — Thai readers experience the parallelism rhythm without lexical-collapse. The cornerstone-Christology threads cleanly across all three citations using the consistent **ศิลามุมเอก** rendering for both ἀκρογωνιαῖος (2:6) and κεφαλὴν γωνίας (2:7) — preserving the **conceptual** equivalence while acknowledging the Greek-lexical distinction (ἀκρογωνιαῖος = the *foundation-cornerstone*; κεφαλὴ γωνίας = the *capstone / head-of-corner*; both are translated by the same Thai because the *Christological-fulfillment* is the same regardless of architectural-positioning, and the Petrine argument requires the equivalence).

**LOCKED** ✓ — DB entries recorded in `data/nt_ot_citations.json`. Strong corpus-internal cross-linkage.

---

## 6. 1 Pet 3:18-22 — Christ's preaching to the spirits in prison + flood-baptism typology — **DECIDE (the most contested NT passage)**

This is the **single most-contested passage in the entire NT** for interpretation. 1 Peter 3:19 has at least three mainstream readings (per BDAG, Davids, Achtemeier, Schreiner, Jobes commentaries):

> 3:18-19 GK: `... θανατωθεὶς μὲν σαρκὶ ζῳοποιηθεὶς δὲ πνεύματι· ἐν ᾧ καὶ τοῖς ἐν φυλακῇ πνεύμασιν πορευθεὶς ἐκήρυξεν,`

> 3:18-19 TH: `... ทรงถูกประหารในเนื้อหนัง แต่ทรงได้ชีวิตในพระวิญญาณ ในพระวิญญาณนั้น พระองค์ได้เสด็จไปประกาศแก่บรรดาวิญญาณที่อยู่ในที่กักขัง`

The 3:19 KD names the three readings:

> 3 interpretations: (1) **fallen-angels** preached-to between death-and-resurrection (the "Augustinian" reading-of-Calvin / Kelly / Achtemeier; cf. 2 Pet 2:4 + Jude 6 + 1 Enoch 6-21) — Christ proclaims-judgment over the Genesis-6 "sons-of-God" demonic-spirits; (2) **dead-humans-from-flood** preached-to between death-and-resurrection (the "patristic" reading; postmortem-evangelism); (3) **pre-incarnate-Christ-preached-through-Noah** to Noah's contemporaries while the ark was being built (the Augustinian-classical-Reformed reading — Wayne Grudem's preferred reading).

**Editorial strategy chosen — LEXICAL-AMBIGUITY-PRESERVATION:** The translator deliberately renders Greek-grammar-faithfully with no interpretive narrowing:
- **ἐν ᾧ** ("in which" / "in [the Spirit] in whom") → **ในพระวิญญาณนั้น** ("in that Spirit") — preserves the antecedent ambiguity (πνεύματι 3:18b OR ζῳοποιηθεὶς 3:18b)
- **πορευθεὶς ἐκήρυξεν** ("having gone, he proclaimed") → **ได้เสด็จไปประกาศ** (royal-prefix; preserves the *journey-and-proclaim* sequence without specifying the *where*)
- **τοῖς ἐν φυλακῇ πνεύμασιν** ("to the spirits in prison") → **บรรดาวิญญาณที่อยู่ในที่กักขัง** (plural-spirits-in-prison; preserves the spirits=angels-vs-spirits=human-souls ambiguity)

This is the **opposite** strategy from 4:6 (next item) — where the translator *did* narrow the interpretive ambiguity.

**The 3:21 follow-up — baptism is NOT-regenerative:**
> ἀντίτυπον (HAPAX-here, "antitype / corresponding-figure") → **ภาพแทน** ("image-substitute"). The 3:21 KD: "Peter is NOT teaching baptismal-regeneration — the explicit 'not removal-of-dirt-from-flesh' qualifier + the 'through-resurrection-of-Christ' basis make clear that faith-in-Christ-confessed-at-baptism saves, not the rite itself."

> ἐπερώτημα (HAPAX-here, "appeal / pledge / inquiry") → **คำสัญญา** ("formal-promise") — the translator chose the **pledge** reading consistent with mainstream-evangelical interpretation (NIV/ESV-compatible).

**DECIDE — three sub-decisions:**

**§A — confirm the 3:19 lexical-ambiguity-preservation strategy** (do NOT narrow to one of the three interpretations; let Thai readers receive the same options Greek readers receive).

**§B — confirm the 3:21 ἐπερώτημα → คำสัญญา (pledge) reading** vs the alternative **คำขอวิงวอน** ("appeal / petition" — older NRSV reading). The pledge-reading is mainstream-evangelical but theologically-loaded (turns baptism into a *credal-act* rather than *interrogative-vow*).

**§C — confirm the 3:21 ἀντίτυπον → ภาพแทน rendering** (preserves "corresponding-figure" + the negation-clause that explicitly disclaims regenerative-physical-cleansing). Worth a footer-note?

**Recommend: STABLE-with-DECIDE on §A + §B + §C.** Per RULES §0 evangelical-Protestant alignment, the lexical-ambiguity preservation strategy at 3:19 is the right default for a CC0 Thai Bible — Thai pastors can pursue further study. But the contrast with 4:6 (next item) is striking and worth Ben's explicit confirmation.

---

## 7. 1 Pet 4:6 — gospel preached to "the dead" — **DECIDE (the second-most-contested NT passage; opposite editorial strategy from 3:19)**

Adjacent in the letter to the spirits-in-prison passage, but the **translator chose explicit disambiguation** here, in deliberate contrast to 3:19's ambiguity-preservation:

> 4:6 GK: `εἰς τοῦτο γὰρ καὶ νεκροῖς εὐηγγελίσθη ἵνα κριθῶσι μὲν κατὰ ἀνθρώπους σαρκὶ ζῶσι δὲ κατὰ θεὸν πνεύματι.`

> 4:6 TH: `เพราะเหตุนี้เอง ข่าวประเสริฐจึงได้ถูกประกาศแก่**ผู้ที่บัดนี้ตายไปแล้ว**ด้วย เพื่อพวกเขาจะถูกพิพากษาตามมนุษย์ในเนื้อหนัง แต่จะมีชีวิตตามพระเจ้าในวิญญาณ`

The 4:6 KD names the disambiguation:

> Per uW figs-explicit: 'dead-ones' refers to those-who-heard-the-gospel-while-alive but have-since-died. Render with explicit 'ผู้ที่บัดนี้ตายไปแล้ว' — disambiguates from a postmortem-evangelism reading (which would contradict HEB 9:27).

**Editorial assessment:** The translator inserted "**บัดนี้**" ("now") into the Thai to convert what reads in Greek as ambiguous (νεκροῖς = "to the dead" — *when?* could be: postmortem-preaching OR preaching-to-now-dead-people-while-they-were-alive) into an explicit "those-who-are-now-dead" reading. This is **interpretive narrowing** — it commits to the mainstream-evangelical reading consistent with HEB 9:27 ("it is appointed for men to die once, then comes judgment" — which forecloses postmortem-evangelism).

**Why this is striking:** The translator's editorial strategy at 3:19 (preserve ambiguity) and at 4:6 (narrow to mainstream-evangelical reading) are **opposite**. Both are defensible — but consistency would either preserve-ambiguity at both (let Thai readers wrestle with both passages exegetically) or disambiguate at both (commit to mainstream-evangelical readings throughout). The current mixed strategy is the most-common evangelical-translation choice (NIV/ESV/CSB all do this) but worth Ben's confirmation that this is the corpus-default.

**DECIDE:** Should the corpus default be:
- (a) **mixed-strategy** (current): preserve ambiguity at 3:19 (where the three readings are exegetically irreducible) + disambiguate at 4:6 (where one reading is theologically incompatible per HEB 9:27)?
- (b) **uniform-ambiguity-preservation**: render 4:6 as bare "ข่าวประเสริฐได้ถูกประกาศแก่ผู้ตาย" without the "บัดนี้" insertion?
- (c) **uniform-disambiguation**: render 3:19 with one of the three interpretations made explicit (e.g., "ในยุคของโนอาห์" pre-incarnate-Christ-through-Noah reading)?

**Recommend: confirm option (a) is the corpus-default.** It matches mainstream-evangelical English translations and the project's RULES §0 alignment. But the inconsistency of strategy is worth a corpus-doc `docs/translator_decisions/petrine_eschatological_disambiguation_2026-05.md` that names the principle: *preserve ambiguity when multiple-readings are exegetically-defensible; disambiguate when one-reading is theologically-incompatible-with-the-rest-of-Scripture*.

---

## 8. ποιμήν / ἀρχιποίμην / ποίμνη / ἐπίσκοπος — Petrine shepherd Christology + ecclesiology — **STABLE (undocumented; recommend doc)**

1 Peter has the corpus's **densest shepherd-imagery cluster** outside John 10. The cluster bridges Christological (2:25) and ecclesiological (5:1-4) uses:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 2:25 | τὸν ποιμένα καὶ ἐπίσκοπον τῶν ψυχῶν ὑμῶν | **ผู้เลี้ยงและผู้ดูแลจิตวิญญาณของท่านทั้งหลาย** | Christological — Christ as Shepherd-Overseer-of-souls |
| 5:2 | ποιμάνατε τὸ ἐν ὑμῖν ποίμνιον τοῦ θεοῦ | **จงเลี้ยงดูฝูงแกะของพระเจ้าที่อยู่ในหมู่พวกท่าน** | ecclesiological — elders shepherding the flock |
| 5:2 | ἐπισκοποῦντες | **ดูแลพวกเขา** | ecclesiological — overseeing (verb) |
| 5:4 | τοῦ ἀρχιποίμενος | **พระผู้เลี้ยงใหญ่** | Christological — Christ as Chief-Shepherd at parousia |

The 2:25 KD names the principle:

> ποιμήν → ผู้เลี้ยง — corpus-precedent JHN 10:2 (slightly-shortened from ผู้เลี้ยงแกะ to fit the dual-title context with 'ผู้ดูแล'). ἐπίσκοπος → ผู้ดูแล — DIVINE-application context (Christ-as-Overseer-of-souls), distinct from the ecclesiastical-office sense at 1 Tim 3:2 ('ผู้ปกครองดูแล'). Render bare 'ผู้ดูแล' for the Christological-divine title; alternative ผู้ปกครองดูแล considered but here the ecclesiastical-office sense doesn't fit (Christ is THE overseer-of-souls, not a church-office).

**Editorial assessment — the principled lexical-split:**

| Greek | Christological-divine context | Ecclesiastical-office context |
|---|---|---|
| ποιμήν | **ผู้เลี้ยง** (1 Pet 2:25; cf. JHN 10:2) | **ผู้เลี้ยง** (1 Pet 5:2 verbal-form ποιμαίνω → เลี้ยงดู) |
| ἐπίσκοπος | **ผู้ดูแล** (1 Pet 2:25 — bare, Christological) | **ผู้ปกครองดูแล** (1 Tim 3:2 — compound, office-title) |
| ἀρχιποίμην | **พระผู้เลี้ยงใหญ่** (1 Pet 5:4 — royal-prefix + comparative, eschatological-Christ-title) | N/A — only Christological |

The **register-split** is principled and defensible. **พระ-** prefix preserved for the Christological-eschatological ἀρχιποίμην (5:4); plain register for the ecclesiastical-office uses. The 2:25 ἐπίσκοπος ψυχῶν is a *Christological divine-title* (Christ-as-Overseer-of-souls), which differs from the ecclesiastical-office ἐπίσκοπος of the Pastorals.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/poimēn_episkopos_register_split_2026-05.md` before:
- **2 Peter** (no shepherd-imagery, but elder-language likely)
- **Hebrews 13:20** (the great Petrine-echo: "ὁ ποιμὴν τῶν προβάτων ὁ μέγας" → **ผู้เลี้ยงแกะใหญ่**)
- **Revelation 7:17** (Christ-as-Shepherd vision: "τὸ ἀρνίον ... ποιμανεῖ αὐτούς")

The doc should:
1. Lock ποιμήν (Christ-subject) → **ผู้เลี้ยง** (or **ผู้เลี้ยงแกะ** when the sheep-context is explicit)
2. Lock ἀρχιποίμην → **พระผู้เลี้ยงใหญ่** (royal + comparative)
3. Lock ἐπίσκοπος (Christological-divine context) → **ผู้ดูแล** (bare)
4. Distinguish from ἐπίσκοπος (ecclesiastical-office, Pastorals) → **ผู้ปกครองดูแล** (compound)
5. Lock ποίμνη / ποίμνιον → **ฝูงแกะ**
6. Cite 1 Pet 2:25 + 5:2 + 5:4 as the locking precedents

---

## 9. πρεσβύτερος / νεώτερος / ταπεινοφροσύνη — 1 Pet 5:1-7 elder/young/humility code — **STABLE (extends Pastoral Epistles pattern)**

The 5:1-7 elders-and-young pastoral instruction:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| 5:1 | Πρεσβυτέρους | **ผู้ปกครองคริสตจักร** | ecclesiastical-office |
| 5:1 | συμπρεσβύτερος (HAPAX) | **ผู้ปกครองคริสตจักรเพื่อนร่วมงาน** | Peter's pastoral self-designation |
| 5:5 | νεώτεροι | **คนหนุ่ม** | younger-men in the church |
| 5:5 | ὑποτάγητε | **จงยอมจำนน** | submit (same Thai-pattern as 2:13, 2:18, 3:1) |
| 5:5 | ταπεινοφροσύνη | **ความถ่อมใจ** | humility |
| 5:5 | ἐγκομβώσασθε (HAPAX) | **สวมใส่** | clothe-yourselves |
| 5:5b | DIRECT OT CITATION Prov 3:34 LXX | **"พระเจ้าทรงต่อต้านคนเย่อหยิ่ง แต่ทรงประทานพระคุณแก่คนถ่อมใจ"** | OT citation (also at JAS 4:6 — corpus-internal-link) |

**Editorial assessment:** Compliance with `pastoral_corpus_locks_2026-05.md` is exact:
- πρεσβύτερος (ecclesiastical-office) → **ผู้ปกครองคริสตจักร** (compound, distinguishes from generic "older-men")
- ταπεινοφροσύνη → **ความถ่อมใจ** (corpus-precedent Phil 2:3, Col 3:12)
- συμπρεσβύτερος (HAPAX) — the principled rendering preserves "fellow-elder-with-the-addressees" — Peter's humble pastoral self-designation rather than apostolic-authoritative one. Theologically loaded: Peter does NOT claim apostolic primacy here.

The **PROV 3:34 LXX citation at 5:5b** uses identical Thai to JAS 4:6 (corpus-internal-link) — both Peter and James appear to draw from a shared early-Christian-tradition citing this proverb. The same Thai rendering preserves the inter-textual-link for Thai readers.

**STABLE — no new doc needed.** Pastoral-corpus-locks doc covers the ecclesiastical-office vocabulary. Worth a one-line cross-reference noting Catholic-Epistles confirmation of the lock.

---

## 10. 1 Pet 3:1-7 household codes — wives/husbands + Sarah-exemplar + σκεῦος (vessel-as-wife) — **REVIEW**

The Petrine household-code at 3:1-7:

| Verse | Greek | Thai |
|---|---|---|
| 3:1 | γυναῖκες ὑποτασσόμεναι τοῖς ἰδίοις ἀνδράσιν | **ภรรยาทั้งหลาย จงยอมจำนนต่อสามีของตน** |
| 3:6 | ὡς Σάρρα ὑπήκουσεν τῷ Ἀβραάμ, κύριον αὐτὸν καλοῦσα | **เช่นเดียวกับซาราห์ที่เชื่อฟังอับราฮัม โดยเรียกท่านว่านาย** |
| 3:7 | συνοικοῦντες κατὰ γνῶσιν, ὡς ἀσθενεστέρῳ σκεύει τῷ γυναικείῳ ἀπονέμοντες τιμήν | **จงอยู่กินกับภรรยาของท่านอย่างเข้าใจ โดยให้เกียรติแก่นางในฐานะภาชนะที่อ่อนแอกว่า** |
| 3:7b | ὡς καὶ συγκληρονόμοις χάριτος ζωῆς | **และในฐานะผู้รับมรดกร่วมแห่งพระคุณคือชีวิต** |

**Three editorial choices flagged for review:**

**§A — 1 Pet 3:6 κύριος (Sarah-to-Abraham) → นาย (master), NOT divine-κύριος:** The translator correctly uses **นาย** ("master / sir") rather than **องค์พระผู้เป็นเจ้า** (the locked divine-κύριος rendering) — Sarah addressing Abraham is a *human-honorific* per the OT-Genesis-18:12 LXX context. This is fully compliant with `vocative_kyrie_didaskale_register_2026-04.md` (the doc's category for non-divine-κύριος contexts). **STABLE.**

**§B — 1 Pet 3:7 σκεῦος → ภาชนะ (vessel) referring to the WIFE:** The translator renders σκεῦος as **ภาชนะ** ("vessel / container") preserving the Pauline-Petrine metaphor (cf. ACT 9:15 + 1 TH 4:4 + 2 Tim 2:20-21).
   - **The contrast with the 1TH 4:4 σκεῦος DECIDE-flag is striking.** At 1 Thess 4:4 the audit flagged σκεῦος as having two readings (BODY vs WIFE) — the translator chose BODY for that verse (**ครอบครองร่างกายของตนเอง**). At 1 Pet 3:7 the σκεῦος unambiguously refers to the wife (γυναικεῖος = "of-the-female") — and is rendered **ภาชนะ** (vessel). The two passages use the **same Greek lemma** in **opposite referent-roles** (1TH 4:4 σκεῦος = body-of-the-person; 1PE 3:7 σκεῦος = wife-as-the-weaker-vessel-of-the-husband). The Thai correctly distinguishes the two — but consistency-checking against the 1TH-4:4 pending DECIDE is worth noting.
   - **REVIEW:** Worth Ben's confirmation that the **wife = ภาชนะที่อ่อนแอกว่า** rendering reads naturally in Thai (the Greek is already cross-culturally awkward in modern English; preserving the metaphor in Thai adds another layer).

**§C — 1 Pet 3:1 ὑποτάσσω + pastoral_corpus_locks §E ambiguity-preservation:** Per the May 2026 pastoral-corpus-locks doc, the household-code's structural form is preserved without forcing modern complementarian-or-egalitarian interpretation. The Thai **จงยอมจำนน** is principled — "submit-yourselves-to" with no register-shift. **STABLE.** The 3:7 close with **συγκληρονόμοις χάριτος ζωῆς** ("fellow-heirs of the grace which is life") balances the wife-instruction by elevating wives to *spiritual-equality*; the Thai **ผู้รับมรดกร่วมแห่งพระคุณคือชีวิต** preserves this balance.

**Recommend: STABLE on §A + §C; REVIEW on §B (1 Pet 3:7 σκεῦος = ภาชนะ rendering for wife-as-vessel — confirm naturalness in Thai).**

---

## 11. ἀναγεννάω + σπορά + λόγος ζῶν — Petrine new-birth-by-imperishable-seed — **STABLE (undocumented; consider doc)**

The new-birth cluster at 1:3 and 1:23:

| Verse | Greek | Thai |
|---|---|---|
| 1:3 | ὁ ... ἀναγεννήσας ἡμᾶς εἰς ἐλπίδα ζῶσαν | **ผู้ทรงบังเกิดเราใหม่ ... ให้เข้าสู่ความหวังอันมีชีวิต** |
| 1:23 | ἀναγεγεννημένοι οὐκ ἐκ σπορᾶς φθαρτῆς ἀλλὰ ἀφθάρτου, διὰ λόγου ζῶντος θεοῦ καὶ μένοντος | **เพราะท่านได้รับการบังเกิดใหม่ ไม่ใช่จากเมล็ดพันธุ์ที่จะเสื่อมสูญ แต่จากที่ไม่เน่าเปื่อย โดยทางพระวจนะของพระเจ้าผู้ทรงพระชนม์และดำรงอยู่** |

**Editorial assessment:**
- **ἀναγεννάω (NT-2× hapax-as-pair, only 1 Pet 1:3 + 1:23)** → **ทรงบังเกิด ... ใหม่** / **ได้รับการบังเกิดใหม่** — preserves the divine-causative regenerative-act sense + the passive-recipient sense.
- **σπορά (NT-hapax, "sowing / seed")** → **เมล็ดพันธุ์** — preserves the agricultural-sown-seed metaphor.
- **λόγος ζῶν θεοῦ καὶ μένων** ("the living and abiding word of God") → **พระวจนะของพระเจ้าผู้ทรงพระชนม์และดำรงอยู่** — preserves both possible Greek-grammar attachments (ζῶντος + μένοντος may modify either λόγος OR θεοῦ; the Thai reads with the participles modifying θεοῦ, the more-natural-Greek-grammar reading).

The 1:23 KD anchors the Petrine-Johannine-Synoptic cross-link:

> The seed-and-word imagery echoes JESUS-PARABLE-OF-SOWER + JHN 1:13 (born-not-of-blood-but-of-God).

**Recommend: STABLE — consider brief doc** `docs/translator_decisions/anagennaō_new_birth_2026-05.md` to lock the rendering before Titus 3:5 (παλιγγενεσίας → **การฟื้นบังเกิดใหม่**, already shipped — different lemma, same theological-concept) and JHN 3:3 (γεννηθῇ ἄνωθεν → **บังเกิดใหม่**, already shipped). Petrine ἀναγεννάω is the *uniquely-strong* lemma (the αν- prefix making the regeneration-causative explicit), so a brief doc would be helpful.

---

## 12. 1 Pet 5:8 διάβολος ὡς λέων ὠρυόμενος — distinctive imagery — **STABLE**

> 5:8 GK: `ὁ ἀντίδικος ὑμῶν διάβολος ὡς λέων ὠρυόμενος περιπατεῖ ζητῶν τινα καταπιεῖν`

> 5:8 TH: `ปฏิปักษ์ของท่านคือมาร เดินวนเวียนไปมาดุจสิงโตคำราม เสาะหาผู้ที่จะกลืนกิน`

**Editorial assessment:**
- **ἀντίδικος** ("legal-adversary, opponent-in-court") → **ปฏิปักษ์** (corpus-precedent; "opponent / adversary"). Per `adversary_speech_register_2026-05.md` and `spiritual_beings_hierarchy_2026-05.md`, the devil-as-legal-prosecutor metaphor (cf. Job 1:6-12 / Zech 3:1-2) is preserved.
- **διάβολος** → **มาร** (corpus-locked Thai-Christian standard for the Devil; distinct from **ซาตาน** = transliterated "Satan" in adversary-cosmic context).
- **λέων ὠρυόμενος** → **สิงโตคำราม** ("roaring lion") — preserves the Petrine-imagery faithfully. Echoes Ps 22:13 LXX (ὡς λέων ὁ ἁρπάζων) + Ps 7:2 LXX (lion-rendering metaphor for the wicked-pursuer).

**STABLE — full compliance** with `adversary_speech_register_2026-05.md` and `spiritual_beings_hierarchy_2026-05.md` (διάβολος → มาร = personal-devil; not a generic-evil-power).

---

## 13. 1 Pet 5:13 Βαβυλών — Rome metaphor preserved as transliteration — **REVIEW**

> 5:13 GK: `ἀσπάζεται ὑμᾶς ἡ ἐν Βαβυλῶνι συνεκλεκτὴ καὶ Μᾶρκος ὁ υἱός μου.`

> 5:13 TH: `**คริสตจักรที่อยู่ในบาบิโลน** ผู้ที่ทรงเลือกสรรร่วมกับท่านทั้งหลาย ฝากความระลึกถึงท่าน และมาระโกบุตรของข้าพเจ้าก็เช่นกัน`

The 5:13 KD names the metaphor:

> Per uW figs-metaphor: Babylon = Rome (NT-coded-language, also REV 14:8 + 17:5 + 18:2). thai_summary explains the Babylon-Rome metaphor for Thai readers.

**Editorial assessment:** The translator preserves **Βαβυλών → บาบิโลน** as a *transliteration-of-the-text* and explains the Rome-metaphor in `thai_summary`. This matches the project's standard for OT-coded-NT-language (cf. the προσήλυτος / Ἑλληνιστής Acts-renderings, where the transliteration is preserved + cultural-summary explains).

**Two questions worth confirmation:**
- **§A — Should Babylon = Rome be made explicit in the main text?** Some modern English translations footnote "Babylon" with "i.e., Rome" (NIV/CSB main-text uses Babylon; ESV footnotes "Rome"). Current Thai uses bare **บาบิโลน** + summary — preserves authorial-intent (Peter wrote "Babylon" as code-language, not "Rome") but may obscure the metaphor for Thai-readers unfamiliar with NT-coded-language.
- **§B — συνεκλεκτή (HAPAX, "the [feminine] co-elect-one")** → **คริสตจักร ... ผู้ที่ทรงเลือกสรรร่วมกับท่านทั้งหลาย** — the translator inserted **คริสตจักร** ("the church") as the implicit subject of the feminine-singular συνεκλεκτή. This is interpretive: the alternative reading is that συνεκλεκτή refers to **Peter's wife** ("she who is in Babylon, co-elect with you"; cf. 1 Cor 9:5 indicating Peter had a wife — "Cephas and the brothers of the Lord"). The mainstream reading (the Roman-church) is preserved with **คริสตจักร**, but worth Ben's confirmation that the church-reading is the corpus-default.

**Recommend: REVIEW §A + §B.** Both are mainstream-evangelical readings; the explicit insertions (**บาบิโลน** transliterated + **คริสตจักร** as implicit-subject) may benefit from a brief footer-note pointer in the chapter-summary.

---

## 14. 1 Pet 4:16 Χριστιανός — early-Christian self-designation — **STABLE**

> 4:16 GK: `εἰ δὲ ὡς Χριστιανός, μὴ αἰσχυνέσθω, δοξαζέτω δὲ τὸν θεὸν ἐν τῷ ὀνόματι τούτῳ.`

> 4:16 TH: `แต่ถ้าทนทุกข์ในฐานะ**คริสเตียน** อย่าให้ผู้นั้นอาย แต่ให้ถวายเกียรติแด่พระเจ้าในนามนั้น`

**Editorial assessment:** **Χριστιανός → คริสเตียน** (corpus-Thai-Christian-standard transliteration). The lemma occurs only **3× in the entire NT** (Acts 11:26 — Antioch-coining; Acts 26:28 — Agrippa's "almost a Christian"; 1 Pet 4:16 — Petrine self-designation under persecution). The Thai uses the standard Thai-Christian transliteration **คริสเตียน** consistently.

**STABLE — no new doc needed.** The corpus already has 3 verses worth of consistent rendering. The Petrine 4:16 ratifies the pattern.

---

## 15. OT citations / allusions — Petrine density — **all flagged + LOGGED**

1 Peter has **8+ explicit OT citations** + numerous allusions logged:

| 1PE | OT source | Status |
|---|---|---|
| 1:16 | Lev 11:44, 19:2 | **LOGGED** — "Be holy because I am holy" |
| 1:24-25 | Isa 40:6-8 | **LOGGED** — grass + flower of grass + word-of-the-Lord-endures |
| 2:6 | Isa 28:16 LXX | **LOGGED** — cornerstone-in-Zion |
| 2:7 | Ps 118:22 LXX | **LOGGED** — stone-rejected-cornerstone |
| 2:8 | Isa 8:14 LXX | **LOGGED** — stumbling-stone |
| 2:9 | Exod 19:6 + Isa 43:20-21 LXX | **LOGGED** — composite four-fold formula |
| 2:22 | Isa 53:9 | **LOGGED** — "no deceit in his mouth" |
| 2:24 | Isa 53:5, 12 | **LOGGED** — bore-our-sins + by-his-wounds-healed |
| 3:10-12 | Ps 34:12-16 LXX | **LOGGED** — long-citation block |
| 4:18 | Prov 11:31 LXX | **LOGGED** — "if righteous-scarcely-saved..." |
| 5:5 | Prov 3:34 LXX | **LOGGED** — God-resists-proud (also at JAS 4:6) |

**Additional unflagged echoes (allusions, not formal citations):**
- 1:2 — Exod 24:8 LXX (Sinai-blood-sprinkling); 2:25 — Isa 53:6 LXX (sheep-going-astray); 3:6 — Gen 18:12 LXX (Sarah-calling-Abraham-"my-lord"); 3:14 — Isa 8:12 LXX (don't-fear-what-they-fear); 3:20 — Gen 6-8 (Noah-flood); 4:8 — Prov 10:12 LXX (love-covers-sins, also at JAS 5:20); 4:14 — Isa 11:2 LXX (Spirit-of-glory-resting-upon); 4:17 — Ezek 9:6 + Jer 25:29 (judgment-begins-at-house-of-God); 5:7 — Ps 55:23 LXX (cast-anxiety-upon-Yahweh); 5:9 — Job 1:6-12 / 2:1-7 LXX (resist-the-adversary); 5:14 — Gen 23:6 / various OT (kiss-of-greeting).

**Editorial assessment:** 1 Peter is among the **most OT-saturated NT books per verse-count** (>20 explicit + allusive OT-references in 105 verses). All are flagged via verse-level KD-rationales; explicit-citations get DB entries in `data/nt_ot_citations.json`. Per RULES §5b, direct-speech curly Thai-quotes mark the explicit-citations.

**STABLE — all compliant.** Worth ensuring `data/nt_ot_citations.json` is fully up-to-date with the 8 explicit-citations listed above.

---

## 16. 1 Pet 1:22 — inclusion-variant resolution (the recent commit) — **LOCKED ✓**

Per commit `953f313` ("Resolve 1PE 1:22 inclusion-variant for end-of-book audit gate"):

> 1:22 GK (SBLGNT): `Τὰς ψυχὰς ὑμῶν ἡγνικότες ἐν τῇ ὑπακοῇ τῆς ἀληθείας εἰς φιλαδελφίαν ἀνυπόκριτον ἐκ καρδίας ἀλλήλους ἀγαπήσατε ἐκτενῶς`

The 1:22 KD names the textual decision:

> Per uW textual-issues note: SBLGNT omits 'δια πνεύματος' ('through-the-Spirit') which appears in some-mss; we follow SBLGNT (modern critical-text). Note SBLGNT prints 'ἐκ καρδίας' — 'from heart' rather than the variant 'ἐκ καθαρᾶς καρδίας' ('from pure heart'); render preserves the SBLGNT reading + supplies natural 'ที่บริสุทธิ์'

**LOCKED ✓** — fully compliant with RULES §0 SBLGNT-strictness. The inclusion-variant gap audit (per `docs/end_of_book/inclusion_variant_gap_2026-05-02.md`) has been satisfied.

---

## 17. Inherited locks — **all compliant**

| Doc | 1PE evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | **N/A directly** — ἐκκλησία does NOT occur in 1 Peter. Peter uses **ἀδελφότης** ("brotherhood") at 2:17 + 5:9 → **หมู่พี่น้อง** for the Christian-community concept. The 5:13 συνεκλεκτή is rendered with explicit insertion of **คริสตจักร** (the implicit-feminine-noun referent). | **LOCKED (N/A)** for direct lemma; **คริสตจักร** insertion at 5:13 ratifies the Pauline-corpus rendering |
| `ethnos_2026-04.md` | 2:9 (ἔθνος ἅγιον → **ชนชาติบริสุทธิ์**, identity-positive); 2:12 (ἐν τοῖς ἔθνεσιν → **ในหมู่คนต่างชาติ**, Gentile-pagan); 4:3 (τὸ βούλημα τῶν ἐθνῶν → **ใจปรารถนาของคนต่างชาติ**, Gentile-pagan-religious). All compliant with the doc's three-way rule (ประชาชาติ / ชนชาติ / คนต่างชาติ). | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | 1PE has **8+ narrator-κύριος references** (1:3 ὁ θεὸς καὶ πατὴρ τοῦ κυρίου; 2:3 ὁ κύριος; 2:13 διὰ τὸν κύριον; 3:6 κύριον (Sarah-to-Abraham, NON-divine — see §10A); 3:12 ὀφθαλμοὶ κυρίου ... πρόσωπον δὲ κυρίου (Ps 34:15-16 LXX citation); 3:15 κύριον δὲ τὸν Χριστὸν ἁγιάσατε). All divine uses → **องค์พระผู้เป็นเจ้า**, perfectly compliant; the 3:6 non-divine-κύριος → **นาย** is also compliant. | **LOCKED** (Catholic-Epistles ratifies) |
| `vocative_kyrie_didaskale_register_2026-04.md` | The 3:6 κύριον (Sarah-to-Abraham, non-divine) → **นาย** uses the doc's principled non-divine-κύριος rendering. No vocative κύριε in 1PE (epistolary, not narrative). | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | 4:11 closing-doxology (`ᾧ ἐστιν ἡ δόξα καὶ τὸ κράτος εἰς τοὺς αἰῶνας τῶν αἰώνων· ἀμήν`) → **ขอพระสิริและฤทธานุภาพจงมีแด่พระองค์สืบ ๆ ไปเป็นนิตย์ อาเมน** — compliant. 5:11 mid-letter-doxology (`αὐτῷ τὸ κράτος εἰς τοὺς αἰῶνας· ἀμήν`) → **ขอฤทธานุภาพจงมีแด่พระองค์สืบ ๆ ไปเป็นนิตย์ อาเมน** — compliant. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | 2:13 (βασιλεῖ → **กษัตริย์**); 2:14 (ἡγεμόσιν → **เจ้าเมือง**); 2:17 (τὸν βασιλέα τιμᾶτε → **จงให้เกียรติแก่กษัตริย์**); 5:13 (Σιλουανός → **สิลวานัส**); 5:13 (Μᾶρκος → **มาระโก**). All compliant with plain-register for non-divine-authorities. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout; plain register for non-divine human authorities (kings, governors, masters, husbands-as-such, Sarah-Abraham, devil); plain register for Christian-community authorities (elders, fellow-elders). The 5:8 διάβολος ὡς λέων → **มาร ... ดุจสิงโต** plain register correctly avoids royal-prefixing the adversary. Compliant. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | **N/A in 1PE** — no Aramaic embeds in this letter. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A directly** — 1PE has no Tier 1/2/3 inclusion variants. The 1:22 micro-variant flagged in KDs followed SBLGNT per RULES §0; resolution-commit `953f313` closes the audit-gap. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — 1 Peter is a doctrinal-pastoral letter, not narrative; no historic-present pattern to test. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in 1PE. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | N/A — μετανοέω + μεταμέλομαι BOTH absent from 1PE. | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | **N/A** — ἄφεσις absent from 1PE (the Petrine atonement-language uses **ἔπαθεν περὶ ἁμαρτιῶν** at 3:18 + **τὰς ἁμαρτίας ἡμῶν αὐτὸς ἀνήνεγκεν** at 2:24, not ἄφεσις). | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | 4:3 (ἀθεμίτοις εἰδωλολατρίαις → **การกราบไหว้รูปเคารพอันชั่วร้าย**) — pagan idols are rendered **รูปเคารพ** (idolatrous-images) — NOT พระเจ้า (reserved for the biblical God). Compliant. | **LOCKED** |
| `roman_administrative_titles_2026-04.md` | 2:13-14 (βασιλεῖ → **กษัตริย์**; ἡγεμόσιν → **เจ้าเมือง**) — compliant with the doc's Roman-administrative-title renderings. | **LOCKED** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from 1PE. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (1:12 — **พระวิญญาณบริสุทธิ์**); πνεῦμα Χριστοῦ (1:11 — **พระวิญญาณของพระคริสต์**); ψυχή (1:9 — **จิตวิญญาณ**, salvation-of-souls; 1:22 — **จิตวิญญาณ**, purify-souls; 2:11 — **จิตวิญญาณ**, war-against-souls; 2:25 — **จิตวิญญาณ**, Shepherd-of-souls; 3:20 — **คน** = ψυχαί, "eight-souls" in Genesis-flood = "eight-people"; 4:19 — **จิตวิญญาณ**, entrust-souls). Doc-locked **ψυχή → จิตวิญญาณ** uniformly applied except at 3:20 where ψυχαί = "souls" in the Hebraic sense of "persons" → **คน** is the natural Thai. πνεῦμα anthropological at 3:18-19 (Christ's spirit / spirits-in-prison) — see §6 above. | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | N/A — 1PE is Petrine. The 4:11 + 5:11 single-ἀμήν doxologies are NOT the Johannine-doubled-amen pattern. | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply (no Jesus-direct-discourse in 1PE). The 4:11 + 5:11 ἀμήν are doxology-closes, not saying-formulas. | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries-addressing-divine in 1PE. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | N/A — βασιλεία absent from 1PE. The 2:9 βασίλειον (HAPAX) is a different lemma — see §4. | **LOCKED (N/A)** |
| `ouranos_heaven_rendering_2026-04.md` | 1:4 (κληρονομίαν ... τετηρημένην ἐν οὐρανοῖς ὑμᾶς → **มรดกที่ ... ทรงเก็บรักษาไว้ในสวรรค์เพื่อท่าน**) — compliant per the doc. 1:12 + 3:22 (οὐρανός heaven-as-location-of-Christ-enthroned) → **สวรรค์** — compliant. | **LOCKED** |
| `pastoral_corpus_locks_2026-05.md` | 5:1-7 elder/young/humility code (πρεσβύτερος → **ผู้ปกครองคริสตจักร**; ταπεινοφροσύνη → **ความถ่อมใจ**; συμπρεσβύτερος → **ผู้ปกครองคริสตจักรเพื่อนร่วมงาน**) — compliant. 3:1-7 wives/husbands code §E ambiguity-preservation — compliant. | **LOCKED** |
| `adversary_speech_register_2026-05.md` | 5:8 (ὁ ἀντίδικος ὑμῶν διάβολος → **ปฏิปักษ์ของท่านคือมาร**); 5:9 (ᾧ ἀντίστητε → **จงต่อสู้มัน**) — compliant. The plain register on the adversary correctly avoids royal-prefixing. | **LOCKED** |
| `spiritual_beings_hierarchy_2026-05.md` | 1:12 (εἰς ἃ ἐπιθυμοῦσιν ἄγγελοι παρακύψαι → **เป็นสิ่งที่บรรดาทูตสวรรค์ปรารถนาจะมองดู**, **ทูตสวรรค์** = angels, plain register); 3:22 (ἀγγέλων καὶ ἐξουσιῶν καὶ δυνάμεων → **เหล่าทูตสวรรค์ ผู้มีอำนาจ และฤทธิ์เดช**, hierarchy-of-spiritual-beings); 5:8 (διάβολος → **มาร**); 3:19 (πνεύματα ἐν φυλακῇ → **บรรดาวิญญาณที่อยู่ในที่กักขัง**, ambiguous-spirits) — all compliant. | **LOCKED** |
| `christ_hymn_kenosis_2026-05.md` | **N/A directly** — 1 Pet has no Christ-hymn in the Phil 2:6-11 / Col 1:15-20 mode. The 2:21-25 Christological-paradigm passage is a *suffering-servant typology* (Isa 53 echo), not a kenotic-incarnational-hymn. | **LOCKED (N/A)** |
| `parousia_christou_2026-05.md` | 1:7 (ἐν ἀποκαλύψει Ἰησοῦ Χριστοῦ → **ในการสำแดงของพระเยซูคริสต์**); 1:13 (ἐν ἀποκαλύψει Ἰησοῦ Χριστοῦ → same); 4:13 (ἐν τῇ ἀποκαλύψει τῆς δόξης αὐτοῦ → **ในการสำแดงพระสิริของพระองค์**); 5:1 (τῆς μελλούσης ἀποκαλύπτεσθαι δόξης → **พระสิริที่จะทรงสำแดง**); 5:4 (φανερωθέντος τοῦ ἀρχιποίμενος → **เมื่อพระผู้เลี้ยงใหญ่ทรงสำแดงพระองค์**). **Note:** 1 Peter does NOT use παρουσία — it uses **ἀποκάλυψις** (revelation / unveiling) and **φανερόω** (manifest) for the eschatological-coming. The Thai uniformly renders both with **การสำแดง / ทรงสำแดง** (revelation-of-Christ at parousia). This is a **lexical-distinction the parousia_christou doc should acknowledge**: Pauline = παρουσία = **การเสด็จมา**; Petrine = ἀποκάλυψις/φανέρωσις = **การสำแดง**. Worth a doc-amendment. | **LOCKED-with-amendment-needed** |
| `huiothesia_adoption_2026-05.md` | **N/A directly** — υἱοθεσία absent from 1PE. The 1:14 (ὡς τέκνα ὑπακοῆς → **ดุจดังบุตรที่เชื่อฟัง**) + 1:17 (πατέρα ἐπικαλεῖσθε → **ทูลเรียกพระบิดา**) family-language is *Father-children* (Pauline-Synoptic-Johannine intersection), not the Pauline-technical υἱοθεσία lemma. | **LOCKED (N/A)** |

---

## Mechanical (§1) — **all green**

- 5/5 chapters: `output/check_reports/1peter_NN_review.md` ✓
- 5/5 chapters: `output/back_translations/1peter_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the now-220-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks**
- `git status output/`: only un-tracked Paratext-export files (`output/paratext/{1CO,1TH,2CO,2TH,ACT,COL,EPH,GAL,TIT}.SFM`) — pre-existing, untouched by this audit. No 1PE source-file dirt.

---

## Pre-existing docs affirmed / unchanged

All 44 docs in `docs/translator_decisions/` reviewed. Compliance summary in §17 above. Two amendments recommended:

1. **`parousia_christou_2026-05.md`** — extend with a **§Petrine-ἀποκάλυψις** sub-section noting that 1 Peter uses ἀποκάλυψις/φανέρωσις (rendered **การสำแดง**) for the same eschatological-Christ-coming event that Paul calls παρουσία (rendered **การเสด็จมา**). Cross-reference 1 Pet 1:7, 1:13, 4:13, 5:1, 5:4.

2. **`narrator_vs_character_voice_2026-04.md`** — affirmed (no amendment needed) for the 1 Pet 3:6 Sarah-to-Abraham κύριος → นาย (non-divine-κύριος) compliance.

---

## Flagged for Ben's attention

### A. πάσχω + πάθημα suffering-cluster lift to corpus doc — **STABLE, lift to corpus doc** (§1)
1 Peter is the densest πάσχω + πάθημα cluster per chapter in NT. Lift to corpus doc `pascho_pathema_suffering_2026-05.md` before 2 Pet + Hebrews. The principled register-split (Christ-royal-ทรงทนทุกข์ vs believer-plain-ทนทุกข์) is theologically rich and worth locking.

### B. παρεπίδημος / πάροικος / διασπορά / παροικία sojourner-cluster lift to corpus doc — **STABLE, lift to corpus doc** (§2)
Petrine ecclesiology built on this lemma-cluster. Lift to corpus doc `parepidēmos_paroikos_sojourner_2026-05.md` before Hebrews 11:13 + 13:14. Cross-references to JAS 1:1 (διασπορά).

### C. ποιμήν / ἀρχιποίμην / ἐπίσκοπος Christological-vs-ecclesiastical register-split lift to corpus doc — **STABLE, lift to corpus doc** (§8)
The principled register-split (Christological-divine ผู้ดูแล / พระผู้เลี้ยงใหญ่ vs ecclesiastical-office ผู้ปกครองดูแล / ผู้ปกครองคริสตจักร) is doctrinally important. Lift to corpus doc `poimēn_episkopos_register_split_2026-05.md` before Hebrews 13:20 + Revelation 7:17.

### D. ἀναγεννάω + σπορά + λόγος ζῶν new-birth cluster — **STABLE, consider brief doc** (§11)
The Petrine ἀναγεννάω lemma (only 1 Pet 1:3, 1:23 in NT) is the strongest regenerative-causative form. Brief corpus doc would lock the rendering before Tit 3:5 (already shipped — confirm consistency) and JHN 3:3 references in any future Pauline-Catholic-Epistles cross-references.

### E. 1 Pet 2:9 βασίλειον ἱεράτευμα → ปุโรหิตหลวง single-concept rendering — **REVIEW** (§4)
The translator chose (a) single-concept "royal priesthood" over (b) two-distinct-titles "royal-realm + priesthood." Mainstream-evangelical alignment per RULES §0 supports (a). Worth Ben's confirmation before Revelation 1:6 / 5:10 / 20:6 (where Exod 19:6 is reused with explicit dual-construction).

### F. 1 Pet 3:7 σκεῦος → ภาชนะ wife-as-vessel — **REVIEW** (§10§B)
The Greek metaphor (wife-as-weaker-vessel) is preserved in Thai as ภาชนะ. Pending DECIDE on 1TH 4:4 σκεῦος (BODY vs WIFE) suggests cross-checking these two Petrine-vs-Pauline σκεῦος-uses. Worth Ben's confirmation that ภาชนะ reads naturally in Thai for the wife-context.

### G. 1 Pet 5:13 Βαβυλών = Rome metaphor (transliteration vs explicitation) — **REVIEW** (§13§A)
Translator preserved บาบิโลน transliteration + summary-explanation. Worth Ben's confirmation: keep authorial-coded-language (current), or footnote with **(หมายถึงโรม)** = "(refers to Rome)" in main-text? Also the συνεκλεκτή → คริสตจักร insertion (§13§B) — confirm the church-reading vs Peter's-wife-reading.

### H. 1 Pet 3:19 spirits-in-prison interpretation — **DECIDE** (§6)
Three mainstream readings (fallen-angels / dead-humans-from-flood / pre-incarnate-Christ-through-Noah). Translator chose **lexical-ambiguity-preservation**. Confirm this is the corpus-default for irreducibly-multi-interpretable passages.

### I. 1 Pet 4:6 dead-evangelism explicit disambiguation — **DECIDE** (§7)
Translator inserted "**บัดนี้**" ("now") to convert ambiguous Greek into explicit "those-who-are-now-dead" reading (rules out postmortem-evangelism per HEB 9:27). Opposite strategy from 3:19 (preserve-ambiguity). Confirm the mixed strategy is the corpus-default *(preserve ambiguity when irreducible; disambiguate when one reading is theologically-incompatible)*. Could be locked into a corpus doc `petrine_eschatological_disambiguation_2026-05.md`.

### J. 1 Pet 3:21 baptism ἀντίτυπον + ἐπερώτημα framing — **DECIDE** (§6§B + §6§C)
- ἐπερώτημα → **คำสัญญา** (pledge-reading; mainstream-evangelical) vs alternative **คำขอวิงวอน** (appeal/petition; older NRSV)
- ἀντίτυπον → **ภาพแทน** (image-substitute) — preserves "corresponding-figure" + the negation-clause that explicitly disclaims regenerative-physical-cleansing
- Confirm both renderings; brief corpus doc `petrine_baptism_typology_2026-05.md` could lock these before 2 Pet ships (where baptism doesn't recur, but the same flood-typology-of-judgment recurs at 2 Pet 2:5 + 3:5-7).

### K. New corpus docs to write (before 2 Peter and Hebrews ship)
1. **`docs/translator_decisions/pascho_pathema_suffering_2026-05.md`** (§1) — locks the Christ-royal vs believer-plain register split
2. **`docs/translator_decisions/parepidēmos_paroikos_sojourner_2026-05.md`** (§2) — locks the sojourner-cluster
3. **`docs/translator_decisions/poimēn_episkopos_register_split_2026-05.md`** (§8) — locks the Christological-vs-ecclesiastical shepherd-overseer register split
4. **(Optional)** `anagennaō_new_birth_2026-05.md` (§11) — brief; locks the regenerative-new-birth cluster
5. **(Optional)** `petrine_eschatological_disambiguation_2026-05.md` (§7) — names the principle: preserve ambiguity when irreducible; disambiguate when one reading is theologically-incompatible
6. **(Optional)** `petrine_baptism_typology_2026-05.md` (§6§B-§C) — locks 3:21 ἀντίτυπον + ἐπερώτημα

### L. Existing docs to amend
- **`parousia_christou_2026-05.md`** — extend with §Petrine-ἀποκάλυψις sub-section noting 1 Peter uses ἀποκάλυψις/φανέρωσις rendered **การสำแดง** for the eschatological-Christ-coming.

### M. External AI review (§3 of checklist) — **pending**
Recommended before `book-1peter-v1` tag. Suggested 4-cluster external AI packet:
1. **1PE 1:1–12** — opening + sojourner-identity + Trinitarian election + Petrine-eschatology (ἀποκάλυψις)
2. **1PE 2:4–10** — stone-cluster OT mosaic + four-fold Sinai/Israel formula (the strongest NT-Petrine ecclesiology)
3. **1PE 3:18–22** — Christ's death + spirits-in-prison + flood-baptism typology (the most-debated NT passage)
4. **1PE 4:1–11 + 4:12–19** — suffering theology + 4:6 dead-evangelism explicit disambiguation + 4:11 doxology + Christ-name-bearing persecution

Use Grok + ChatGPT in parallel per the JHN/GAL/1TH pattern.

---

## Recommendation

**1 Peter ships in strong corpus-hygiene shape — and provides the Petrine-suffering-and-exile-theology entry-point for the corpus.** The translator made consistent, principled choices on the four most-significant 1PE-introduced lemma-clusters (πάσχω/πάθημα; παρεπίδημος/πάροικος; ποιμήν/ἀρχιποίμην; ἀναγεννάω) — and **none of these has a corpus-level doc** yet. This is the moment to lock them in before 2 Peter and Hebrews compound the editorial weight (esp. Heb 11:13 + 13:14 sojourner-density; Heb 13:20 ποιμὴν τῶν προβάτων ὁ μέγας; 2 Pet 1-3 πάθημα + suffering recurrences).

The most distinctive editorial choices in 1 Peter — the **3:19 lexical-ambiguity-preservation** vs **4:6 explicit-disambiguation** strategy contrast, and the **3:21 baptism-typology framing** — are the highest-priority items for Ben's confirmation before tagging.

Tag `book-1peter-v1` after:
1. Ben's decisions on **§H + §I + §J** (DECIDE items: 3:19 ambiguity-preservation; 4:6 explicit-disambiguation; 3:21 baptism-typology framing)
2. Ben's confirmation on **§E + §F + §G** (REVIEW items: 2:9 βασίλειον single-concept; 3:7 σκεῦος-as-wife; 5:13 Βαβυλών transliteration + συνεκλεκτή church-reading)
3. Three core new translator_decisions docs written (§K items 1–3 minimum; optionally 4–6)
4. One existing doc amended (`parousia_christou_2026-05.md` with Petrine-ἀποκάλυψις sub-section)
5. External AI sanity-check (§M)

The Catholic-Epistles corpus is now half-shipped (James + 1 Peter complete; 2 Peter + 1-3 John + Jude pending). The Petrine-suffering-theology vocabulary established here will propagate into 2 Peter (already in flight) and the eschatological-judgment material in 2 Pet 2-3.
