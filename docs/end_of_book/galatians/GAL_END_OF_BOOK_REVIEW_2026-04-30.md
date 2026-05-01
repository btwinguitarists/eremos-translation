# Galatians — End-of-Book Review

**Date:** 2026-04-30
**Scope:** All 6 chapters (149 verses; 416 verse-level `key_decisions`); `glossary.json`; existing `docs/translator_decisions/` (24 docs).
**Trigger:** GAL 6 shipped (commit `ad0138c`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 6/6 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the now-128-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks. `git status output/` shows only re-ran-check artifacts + 1TH-loop in-flight files (no GAL-source dirt).
- **Galatians is the FIRST FULL Pauline epistle the project has shipped** (after the 1TI 3 sample). The technical-vocabulary established here will propagate into Romans, 1–2 Corinthians, the Pastorals, and beyond. The translator surfaces this awareness explicitly at GAL 2:16 (`THE PIVOTAL THEOLOGICAL VERSE: this is the first Pauline statement of justification-by-faith doctrine in our corpus`).
- **9 inherited Synoptic / John / Acts locks verified compliant** in GAL (ἐκκλησία, ἔθνος, narrator-κύριος, κύριε registers, divine-object praise verbs, Aramaic-transliteration for Αββα, narrator-vs-character voice, honorifics, OT-citation flagging — see §15-16).
- **4 cross-cutting Pauline patterns are STABLE-but-undocumented at corpus level** (πίστις-Χριστοῦ genitive policy; δικαιόω forensic-declarative rendering; νόμος multi-sense uniformity; στοιχεῖα τοῦ κόσμου). All four will compound massively forward (esp. into Romans), so corpus-doc lift is recommended before Romans 1.
- **3 items flagged REVIEW** (defensible-but-worth-Ben's-confirmation: σάρξ multi-sense single-rendering; παιδαγωγός metaphor-collapse; the πατρός / πατρὸς ἡμῶν divine-Father distribution).
- **3 items flagged DECIDE** (GAL 6:16 "Israel of God" — three-way exegetical fork; GAL 5:14 πᾶς νόμος "is fulfilled" — passive vs. completed-on-our-behalf reading; the πίστις-Χριστοῦ default policy itself).
- **External AI review (§3) pending.**

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. πίστις Χριστοῦ — objective vs subjective genitive policy — **DECIDE before tagging (highest Pauline-forward priority)**

The most-debated single phrase in modern Pauline scholarship. GAL has **6 occurrences of πίστις + Χριστοῦ-genitive** (or υἱοῦ-θεοῦ-genitive), all rendered uniformly with the **OBJECTIVE-GENITIVE** Thai construction:

| Verse | Greek | Thai | Genitive choice |
|---|---|---|---|
| GAL 2:16a | διὰ πίστεως Ἰησοῦ Χριστοῦ | **โดยความเชื่อในพระเยซูคริสต์** | objective ("faith IN Christ") |
| GAL 2:16b | ἐκ πίστεως Χριστοῦ | **โดยความเชื่อในพระคริสต์** | objective |
| GAL 2:20 | ἐν πίστει ζῶ τῇ τοῦ υἱοῦ τοῦ θεοῦ | **ด้วยความเชื่อในพระบุตรของพระเจ้า** | objective |
| GAL 3:22 | ἐκ πίστεως Ἰησοῦ Χριστοῦ | **โดยทางความเชื่อในพระเยซูคริสต์** | objective |
| GAL 3:26 | διὰ τῆς πίστεως ἐν Χριστῷ Ἰησοῦ | **โดยทางความเชื่อในพระเยซูคริสต์** | objective (the ἐν here is unambiguous) |

The 2:16 KD explicitly articulates the choice:

> MAJOR INTERPRETIVE CRUX (πίστις Ἰησοῦ Χριστοῦ — the genitive): two well-attested readings: (a) OBJECTIVE GENITIVE — 'faith IN Jesus Christ' (Christ is the object of believing). The standard Reformed / Lutheran / mainstream evangelical reading. (b) SUBJECTIVE GENITIVE — 'faith/faithfulness OF Jesus Christ' (Christ's own faithfulness, his obedient self-giving on the cross, is what justifies). Increasingly favored by N.T. Wright, Richard Hays, Douglas Campbell, and the New Perspective on Paul.

**Editorial assessment:** The choice is principled, internally consistent, and explicitly aligned with RULES §0 (evangelical-Protestant alignment) — the objective-genitive is the standard NIV/ESV/CSB/THSV1971 reading. The translator is aware of the alternative and has chosen the mainstream-evangelical reading deliberately.

**DECIDE before tagging:** Confirm Ben endorses the objective-genitive default for the entire Pauline corpus going forward (will compound into Romans 3:22, 3:26; Galatians is the entry-point for the doctrine). The alternative is to add a footer-note at GAL 2:16 acknowledging the subjective-genitive position for academically-engaged readers, OR to render one or two key verses (esp. 2:20 with τοῦ υἱοῦ τοῦ θεοῦ — where subjective is grammatically more natural) ambiguously.

**→ Recommend new doc:** `docs/translator_decisions/pistis_christou_2026-04.md` — locks the objective-genitive default for Romans + the rest of the Pauline corpus before Rom 3:22 ships. Document the rationale (RULES §0 evangelical-Protestant alignment + mainstream-evangelical-Thai reader expectation), name the alternative (subjective-genitive / New Perspective), cite GAL 2:16 + Rom 3:22 as the locking precedents.

---

## 2. δικαιόω / δικαιοσύνη — forensic-declarative vs Catholic-leaning "made righteous" — **STABLE (undocumented; recommend new doc)**

The Reformation-era contested vocabulary. GAL has **9 occurrences of δικαιόω + 4 of δικαιοσύνη**, all rendered with the explicitly forensic-declarative Thai construction **ถูกประกาศว่าชอบธรรม** ("be declared righteous") rather than the older Catholic-leaning **ทำให้ชอบธรรม** ("made righteous, infused-righteousness").

| Verse | Greek | Thai | |
|---|---|---|---|
| GAL 2:16 (3×) | οὐ δικαιοῦται / δικαιωθῶμεν / οὐ δικαιωθήσεται | **ไม่ได้ถูกประกาศว่าชอบธรรม / จะถูกประกาศว่าชอบธรรม** | uniform forensic |
| GAL 2:17 | ζητοῦντες δικαιωθῆναι | **แสวงหาการถูกประกาศว่าชอบธรรม** | uniform |
| GAL 2:21 | διὰ νόμου δικαιοσύνη | **ความชอบธรรม** | δικαιοσύνη as abstract noun |
| GAL 3:6 | ἐλογίσθη...εἰς δικαιοσύνην | **ทรงนับว่าเป็นความชอบธรรม** | divine-passive accounting metaphor |
| GAL 3:8 | ἐκ πίστεως δικαιοῖ τὰ ἔθνη | **ทรงประกาศให้คนต่างชาติเป็นผู้ชอบธรรม** | active forensic with God-subject |
| GAL 3:11 | οὐδεὶς δικαιοῦται | **ไม่มีผู้ใดถูกประกาศว่าชอบธรรม** | uniform |
| GAL 3:21 | ἐκ νόμου ἂν ἦν ἡ δικαιοσύνη | **ความชอบธรรมก็ย่อมมาจาก** | abstract noun |
| GAL 3:24 | ἐκ πίστεως δικαιωθῶμεν | **ถูกประกาศว่าชอบธรรม** | uniform |
| GAL 5:4 | ἐν νόμῳ δικαιοῦσθε | **กำลังพยายามถูกประกาศว่าชอบธรรม** | conative-present preserved |
| GAL 5:5 | ἐλπίδα δικαιοσύνης | **ความหวังแห่งความชอบธรรม** | abstract noun |

The 2:16 KD explicitly names the choice and rejects the older alternative:

> FORENSIC-DECLARATIVE δικαιόω: NOT 'make righteous (in moral character)' but 'declare righteous (in courtroom verdict).' This is the foundational technical term of Pauline soteriology. Thai ถูกประกาศว่าชอบธรรม = 'be declared righteous' — captures the forensic-declarative force precisely (vs. the older Catholic-leaning ทำให้ชอบธรรม which suggests infused righteousness).

**Editorial significance:** This is a doctrinal-translation choice as load-bearing as ἐκκλησία → คริสตจักร or πίστις-Χριστοῦ-objective. The forensic-declarative rendering is **explicitly Reformational** and aligns with Protestant evangelical theology (RULES §0). It is verbose (5 syllables vs. THSV1971's typical 3-syllable นับว่าเป็นผู้ชอบธรรม) but precision-on-purpose.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/dikaioo_dikaiosune_2026-04.md` before Rom 3:21–31 (where the doctrine compounds dramatically). The doc should:
1. Lock δικαιόω → ถูกประกาศว่าชอบธรรม (passive, forensic) and active-form ทรงประกาศให้...เป็นผู้ชอบธรรม
2. Lock δικαιοσύνη → ความชอบธรรม
3. Distinguish from related Pauline lemmata: λογίζομαι εἰς δικαιοσύνην (Rom 4-style) → ทรงนับว่าเป็นความชอบธรรม; δίκαιος (adj. of righteous-person) → ผู้ชอบธรรม
4. Cite GAL 2:16 as the locking precedent
5. Reject the older Catholic-leaning ทำให้ชอบธรรม + the compressed THSV นับว่าเป็นผู้ชอบธรรม as alternatives considered

---

## 3. νόμος — multi-sense single-rendering policy — **STABLE (undocumented; recommend new doc)**

GAL has **34 occurrences of νόμος across 26 verses** — by far the densest νόμος-text in the NT. Greek νόμος in Paul carries at least 4 distinct senses:

| Sense | GAL example | Thai | Count |
|---|---|---|---|
| Mosaic Torah (the Sinai-covenant law-code) | 3:17 (νόμος ... after 430 years); 3:19 (Τί οὖν ὁ νόμος); 4:21a; 5:3 (ὅλον τὸν νόμον); 6:13 | **ธรรมบัญญัติ** | ~30 |
| Pentateuch / Torah-as-canon (the OT writing) | 4:21b (τὸν νόμον οὐκ ἀκούετε; "do you not LISTEN to the Torah?") | **ธรรมบัญญัติ** | 1 |
| Principle / governing-pattern | 6:2 (νόμον τοῦ Χριστοῦ "the LAW OF Christ") | **ธรรมบัญญัติของพระคริสต์** | 1 |
| (Implicit "principle of") in 5:23 | κατὰ τῶν τοιούτων οὐκ ἔστιν νόμος | **ธรรมบัญญัติย่อมไม่มีบทบัญญัติต่อต้าน** | 1 |

**Single Thai rendering (ธรรมบัญญัติ) across all four senses.** This is principled — it preserves the Pauline punning power of using one νόμος-word to mean different things in adjacent clauses (esp. 6:2 "law of Christ" played against 5:18 "not under law"; and 4:21's deliberate equivocation between Torah-as-rule-system and Torah-as-text). The 4:21 KD acknowledges:

> 'The law' here = the Torah/Pentateuch as a whole (which the Galatians-wanting-Torah-observance are presumably reading/hearing-recited). Paul's rhetorical thrust: the Torah ITSELF, properly heard, points BEYOND-itself to faith — as the Hagar-Sarah story illustrates.

The 6:2 "law of Christ" KD frames the principle reframing:

> νόμος τοῦ Χριστοῦ = 'the law of Christ' — striking phrase only here in Paul... The 'law of Christ' = the new-covenant-ethical-norm centered in love (cf. 5:14 'love your neighbor as yourself fulfills the whole law'). Paul reframes 'law' POSITIVELY: not the Mosaic-yoke but the Christ-pattern of self-giving love.

**Editorial assessment:** The single-rendering preserves the Pauline punning + signals to the Thai reader that all four senses are deliberately within a single semantic field. The alternative (e.g., ธรรมบัญญัติ for Mosaic / หลักการ for principle / พระคัมภีร์ for Pentateuch-as-text) would flatten Paul's rhetoric.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/nomos_pauline_2026-04.md` before Rom 7 (where νόμος-of-the-mind / νόμος-of-the-flesh / νόμος-of-Spirit-of-life / νόμος-of-sin-and-death will COMPOUND into a 5-νόμος-in-2-verses cluster at Rom 7:21–8:2). Document the single-rendering policy + the rare Pauline νόμος-of-X-genitive-construction handling.

---

## 4. στοιχεῖα τοῦ κόσμου — famously-contested phrase — **REVIEW (verse-level rationale comprehensive; corpus-doc lift recommended before Colossians)**

GAL 4:3 + 4:9 + 4:25 (the συστοιχέω cognate). Three exegetical readings:
1. **Basic principles** — elementary religious systems (Jewish-law and pagan ritual alike). BSB / ESV / NIV majority.
2. **Physical elements** — the four elements of Greek philosophy (earth, water, air, fire), to which ancient peoples assigned spiritual dignity.
3. **Elemental spirits** — personified spiritual powers (angelic beings) that governed pre-Christian humanity. Increasingly favored by N. T. Wright, Martyn, and others reading Paul apocalyptically.

Current Thai renders **หลักการ** (principle, basic-rule) — option (1):

| Verse | Greek | Thai |
|---|---|---|
| GAL 4:3 | ὑπὸ τὰ στοιχεῖα τοῦ κόσμου ... ἤμεθα δεδουλωμένοι | **ภายใต้หลักการพื้นฐานของโลก** |
| GAL 4:9 | ἐπὶ τὰ ἀσθενῆ καὶ πτωχὰ στοιχεῖα | **หลักการที่อ่อนแอและไร้ประโยชน์** |

The 4:3 KD explicitly notes:

> Three main interpretations: (a) BASIC PRINCIPLES — elementary religious systems (Jewish-law and pagan ritual alike); (b) PHYSICAL ELEMENTS — the four elements of Greek philosophy ...; (c) ELEMENTAL SPIRITS — personified spiritual powers (angelic beings) that governed pre-Christian humanity. Modern scholarly debate: BSB ESV NIV mostly favor (a); recent ... [continues]

And the 4:3 verse-level `notes` include: "This will be added to the reviewer-questions for theological-reviewer input as it is corpus-cross-cutting (recurs in Colossians)."

**Editorial assessment:** The choice of (1) is mainstream-evangelical and defensible. หลักการ is broad enough to include ritual-systems but doesn't lock in either spirits or elements. The polemical pivot at 4:9 (πτωχά "beggarly") works well with หลักการ.

**REVIEW: Confirm with Ben** that (1) is the corpus-default before Colossians 2:8 + 2:20 (where στοιχεῖα τοῦ κόσμου recurs in a Christ-vs-cosmic-powers polemical context that some commentators read more naturally with option (3) "elemental spirits"). 

**→ Recommend new doc:** `docs/translator_decisions/stoicheia_tou_kosmou_2026-04.md` to lock หลักการ as the corpus-wide rendering, document the three readings, name (1) as the chosen default, cite GAL 4:3 as the locking precedent. Important pre-Col 2 handoff.

---

## 5. πατήρ — divine vs human Father registers — **STABLE (extends existing narrator/character doc)**

GAL has 7 πατήρ-cluster occurrences:

| Verse | Greek | Thai | Sense |
|---|---|---|---|
| GAL 1:1 | θεοῦ πατρός | **พระเจ้าพระบิดา** | divine (royal πระ-) |
| GAL 1:3 | ἀπὸ θεοῦ πατρὸς ἡμῶν | **จากพระเจ้าพระบิดาของเรา** | divine (royal) |
| GAL 1:4 | τοῦ θεοῦ καὶ πατρὸς ἡμῶν | **ของพระเจ้าและพระบิดาของเรา** | divine (Granville Sharp; royal) |
| GAL 1:14 | πατρικῶν μου παραδόσεων | **บรรพบุรุษของข้าพเจ้า** | human-ancestral (plain — adj. πατρικός = "ancestral") |
| GAL 4:2 | προθεσμίας τοῦ πατρός | **เวลาที่บิดากำหนดไว้** | human-paternal (analogy — Greco-Roman household-father) |
| GAL 4:6 | Αββα ὁ πατήρ | **อับบา พระบิดา** | divine (Aramaic + royal Greek apposition; royal) |

Compliance with `narrator_vs_character_voice_2026-04.md`:
- Divine πατήρ → **พระบิดา** (royal pระ- prefix). 4 occurrences uniform.
- Human-paternal πατήρ in analogical-context (4:2 the Greco-Roman household head) → **บิดา** (plain register, no royal prefix).
- Human-ancestral πατρικός (1:14 adjective for Pharisaic ancestral tradition) → **บรรพบุรุษ** (different lemma — the noun for "ancestors"; Thai natural-equivalent of the πατρικός adjective).

**Editorial assessment:** The plain-vs-royal split tracks the divine/human reference perfectly. The 4:2 plain-register **บิดา** is correct — the analogy is to a normal Greco-Roman father setting a date in a will, not to the Father of the Trinity. The 4:6 **อับบา พระบิดา** preserves the Aramaic transliteration + royal-Greek apposition exactly per the `aramaic_transliterations_2026-04.md` lock.

**STABLE — no new doc needed.** Existing `narrator_vs_character_voice_2026-04.md` covers the principle. Worth a one-line cross-reference noting Pauline confirmation.

---

## 6. σάρξ — multi-sense single-rendering — **REVIEW (extends Johannine pattern)**

GAL has **17 σάρξ occurrences across 13 verses**, all uniformly **เนื้อหนัง**. The Johannine end-of-book audit observed an anthropological/eucharistic split for σάρξ in JHN; Galatians introduces a **third sense** (the ethical-negative "the flesh" = sinful-nature opposed to Spirit) which is the dominant Pauline use.

| Sense | GAL examples | Thai |
|---|---|---|
| **Hebraic idiom "flesh and blood"** (= human beings vs God) | 1:16 (σαρκὶ καὶ αἵματι "with flesh and blood") | **เนื้อหนังและเลือด** |
| **OT-citation echo "no flesh"** (= no human being) | 2:16 (πᾶσα σάρξ from Ps 143:2 LXX) | **เนื้อหนังใด** |
| **Anthropological-neutral "in the flesh"** (= bodily-existence) | 2:20 (νῦν ζῶ ἐν σαρκί), 4:13 (ἀσθένειαν τῆς σαρκός — Paul's bodily illness), 4:14 (ἐν τῇ σαρκί μου) | **เนื้อหนังนี้ / ทางเนื้อหนัง / สภาพ** |
| **Outward-physical sense (circumcision marker)** | 6:12 (εὐπροσωπῆσαι ἐν σαρκί), 6:13 (ἐν τῇ ὑμετέρᾳ σαρκὶ καυχήσωνται — boast in your flesh = Gentile foreskins) | **ตามเนื้อหนัง / ในเนื้อหนัง** |
| **Mode-of-birth contrast (κατὰ σάρκα vs δι' ἐπαγγελίας)** | 4:23, 4:29 | **ตามเนื้อหนัง** |
| **Ethical-negative "the flesh" (sinful nature)** | 3:3 (νῦν σαρκὶ ἐπιτελεῖσθε), 5:13 (ἀφορμὴν τῇ σαρκί), 5:16 (ἐπιθυμίαν σαρκός), 5:17 (×2 σὰρξ vs πνεῦμα antagonism), 5:19 (τὰ ἔργα τῆς σαρκός), 5:24 (τὴν σάρκα ἐσταύρωσαν), 6:8 (ὁ σπείρων εἰς τὴν σάρκα ἑαυτοῦ) | **เนื้อหนัง** |

The 2:20 KD names the principle:

> KEY-TERM CONSISTENCY: σάρξ → เนื้อหนัง (Pauline standard); the context determines which sense (anthropological vs. ethical) is in view.

The 5:13 + 5:16 KDs explicitly mark the ethical-negative shift:

> σάρξ here in ETHICAL-NEGATIVE sense (the sinful-nature's cravings). The same noun's NEUTRAL-vs-NEGATIVE Pauline distribution is FAMOUSLY-CONFUSING and Thai เนื้อหนัง must rely on context.

**Editorial assessment:** The single-rendering policy is principled (Greek itself uses the same σάρξ across all senses; flattening the lemma in Thai mirrors Paul's deliberate semantic-stretching). But the absence of a register-marker for the ethical-negative use (vs. the neutral-bodily) means **Thai readers must rely entirely on context-disambiguation** — exactly the same problem as Greek itself.

**REVIEW flag:** Confirm Ben endorses single-rendering across all 6 senses. The alternatives:
- Mark ethical-negative with intensifier — e.g., **เนื้อหนังที่ตกในบาป** (sinful flesh) — at 5:13/16/17/19/24, 6:8. Defensible; risks repetitive padding.
- Mark anthropological with body-emphasis — e.g., **กายเนื้อ** (bodily-flesh) — at 2:20, 4:13/14. Defensible; loses the Pauline punning.
- Single-rendering throughout (current). Defensible; relies on context.

**→ Recommend: STABLE; consider new doc** `docs/translator_decisions/sarx_pauline_2026-04.md` to lock the single-rendering policy + name all 6 senses + extend the JHN-only `psyche_vs_pneuma_anthropological_2026-04.md` to include the Pauline ethical-negative σάρξ. Will compound massively into Romans 7-8 (the densest σάρξ text in the NT).

---

## 7. παιδαγωγός — Greco-Roman household-disciplinarian metaphor — **STABLE (rationale at verse level; consider doc later)**

GAL 3:24 + 3:25. The single most CULTURALLY-LOADED metaphor in the chapter — the παιδαγωγός was NOT a teacher but a household slave responsible for SUPERVISING and ESCORTING a wealthy family's son to school, enforcing discipline, applying physical correction.

| Verse | Greek | Thai |
|---|---|---|
| GAL 3:24 | ὁ νόμος παιδαγωγὸς ἡμῶν γέγονεν εἰς Χριστόν | **ธรรมบัญญัติจึงได้กลายมาเป็นผู้ดูแลควบคุมของเรา จนกว่าจะถึงพระคริสต์** |
| GAL 3:25 | οὐκέτι ὑπὸ παιδαγωγόν ἐσμεν | **เราจึงไม่ได้อยู่ภายใต้การควบคุมของผู้ดูแลอีกต่อไป** |

The 3:24 KD (650+ chars) walks through the cultural background extensively. Thai uses **ผู้ดูแลควบคุม** ("supervisor-controller") at 3:24 — preserves the supervisory-disciplinary force. 3:25 uses **การควบคุมของผู้ดูแล** ("the control of the supervisor"). The two-word combination expands the single Greek noun for clarity.

**Editorial assessment:** The Thai is principled and preserves the disciplinary-not-pedagogical force. **NOT** translating as "ครู" (teacher) is critically important — the Pauline argument depends on the παιδαγωγός being a TEMPORARY-DISCIPLINARIAN (about to be displaced at the child's coming-of-age), not an educator.

**REVIEW flag — the εἰς Χριστόν "until Christ" rendering at 3:24:** The Thai **จนกว่าจะถึงพระคริสต์** ("until [the time] Christ [arrives]") preserves the temporal sense. This is principled (the salvation-historical "until Christ comes" reading) but the Greek εἰς + accusative could also be read as **directional** ("toward / leading to Christ" — the pedagogue's job was to escort the child to a destination). The 3:24 KD acknowledges:

> εἰς Χριστόν — TWO READINGS: temporal ('until Christ') vs. directional ('to Christ' — leading us to Christ).

The Thai chose temporal. Most modern English translations (NIV/ESV/CSB) also chose temporal. THSV1971 uses the older directional reading.

**Worth confirming with Ben:** is the temporal reading the corpus default? Will compound into Rom 10:4 (τέλος ... νόμου Χριστὸς) where the same temporal-vs-directional question recurs.

**→ Recommend: STABLE; consider new doc** `docs/translator_decisions/paidagogos_2026-04.md` if the metaphor recurs (1 Cor 4:15 παιδαγωγοὺς ἐν Χριστῷ — Paul as παιδαγωγός). Otherwise leave at verse-level.

---

## 8. στίγμα + μάρκα-of-Jesus (GAL 6:17) — Greco-Roman slave-branding metaphor — **STABLE**

GAL 6:17 ἐγὼ γὰρ τὰ στίγματα τοῦ Ἰησοῦ ἐν τῷ σώματί μου βαστάζω → **เพราะข้าพเจ้าแบกรอยตราของพระเยซูไว้ในกายของข้าพเจ้าแล้ว** ("for I bear the brand-marks of Jesus on my body").

The 6:17 KD names the cultural-context (slave-branding in Greco-Roman) and the polemical-twist (Paul belongs to JESUS as slave-to-master, marked by suffering-for-his-name; vs. the Judaizers who want to mark Galatians with circumcision).

**STABLE** ✓ — รอยตรา ("brand-mark") preserves the slave-branding force. 

---

## 9. καινὴ κτίσις — eschatological new-creation formula — **STABLE (recommend new doc, brief)**

GAL 6:15 ἀλλὰ καινὴ κτίσις → **มีแต่การทรงสร้างใหม่เท่านั้น** ("only the [act-of-divine] new creation matters").

The 6:15 KD:

> καινὴ κτίσις = 'new creation' (cf. 2 Cor 5:17). καινός (qualitatively-new) NOT νέος (chronologically-recent). κτίσις = creation (act-of-creating OR thing-created — both senses operative).

Thai renders **การทรงสร้างใหม่** — uses the divine-passive **ทรงสร้าง** (royal verb of creation) + the noun-suffix **การ-** + qualifier **ใหม่**. This is the **act-of-creating** sense (preserved with the divine-actor royal-verb) rather than the **thing-created** sense (which would be **สิ่งที่ทรงสร้างใหม่** "the newly-created thing/person"). Both senses are theologically present in the Greek; the Thai chose the act-emphasis.

**Editorial assessment:** Defensible. 2 Cor 5:17 (ὥστε εἴ τις ἐν Χριστῷ, καινὴ κτίσις) leans more toward the thing-created sense ("if anyone in Christ, [he is] a new creation"). The two verses may need different Thai handling depending on whether the Pauline corpus aims at Greek-mirror consistency or per-verse-context optimization.

**Recommend: STABLE; consider new doc** `docs/translator_decisions/kaine_ktisis_2026-04.md` (brief, to lock the rendering before 2 Cor 5:17 ships). Same rendering for both, OR document the 6:15-vs-2Cor5:17 act-vs-thing distinction.

---

## 10. Αββα ὁ πατήρ — Aramaic embed — **LOCKED ✓**

GAL 4:6 κρᾶζον· Αββα ὁ πατήρ → **ทรงร้องว่า 'อับบา พระบิดา'**

Per `aramaic_transliterations_2026-04.md`: Aramaic embeds preserve **transliteration AND Greek translation**. The Thai correctly preserves both: **อับบา** (Aramaic transliteration) + **พระบิδา** (Thai for ὁ πατήρ — royal divine-Father register).

The Mark 14:36 + Rom 8:15 parallels are noted in the 4:6 KD. The Greek itself preserves the bilingual formula (αββα is Aramaic; ὁ πατήρ is the Greek translator's gloss). Thai preserves the same bilingual structure.

**LOCKED** ✓ — no action.

---

## 11. ἐξαγοράζω (redeem) — slave-marketplace metaphor — **STABLE**

GAL 3:13 + 4:5. Both render **ทรงไถ่...ออกจาก / ทรงไถ่...** ("redeemed-out [royal verb]"). The 3:13 KD names the slave-marketplace background:

> ἐξαγοράζω = redeem, buy out, ransom. Compound ἐξ- (out) + ἀγοράζω (buy at the marketplace). Originally referred to BUYING-A-SLAVE-OUT-OF-BONDAGE in the ancient marketplace.

**STABLE** ✓ — ทรงไถ่ is the standard Pauline-corpus rendering (will compound into 1 Cor 6:20, 7:23; Eph 5:16; Col 4:5).

---

## 12. υἱοθεσία — adoption-as-sons — **STABLE (recommend lift to corpus doc)**

GAL 4:5 ἵνα τὴν υἱοθεσίαν ἀπολάβωμεν → **เพื่อเราจะได้รับการรับเป็นบุตร**.

The 4:5 KD:

> υἱοθεσία (5x NT — Rom 8:15, 23; 9:4; Eph 1:5; here) = adoption (literally 'son-making' or 'son-placing'). LEGAL-TECHNICAL: in Greco-Roman law, adoption granted FULL legal-status as a son, including inheritance rights, even for adoptees not born into the family.

Thai **การรับเป็นบุตร** ("the receiving-as-son [status]") preserves the legal-technical force. 

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/huiothesia_adoption_2026-04.md` (brief — 5-occurrence lemma). Will recur in Rom 8:15 (πνεῦμα υἱοθεσίας — "Spirit of adoption"), 8:23 (υἱοθεσίαν ἀπεκδεχόμενοι — "awaiting our adoption"), 9:4 (ἡ υἱοθεσία as Israel's privileges), Eph 1:5 (προορίσας ἡμᾶς εἰς υἱοθεσίαν — "predestined for adoption"). The Romans 8 cluster is theologically dense; locking GAL 4:5 as the precedent prevents drift.

---

## 13. Ἰουδαϊσμός / Ἰουδαῖος / Ἰουδαϊκῶς — Pauline ethnic-religious vocabulary — **STABLE-but-UNDOCUMENTED at corpus level (deferred to 1TH; see §13a)**

GAL has the rare lemma **Ἰουδαϊσμός** (only here in NT — 1:13, 1:14) → **ศาสนายูδาห์** ("religion of Judah / Judaism"). Plus 5 Ἰουδαῖοι/-ῷ uses (2:13, 2:14 ×3, 2:15) and the rare adverbs **ἐθνικῶς / Ἰουδαϊκῶς** at 2:14.

| Sense | Thai | Verses |
|---|---|---|
| Ἰουδαϊσμός (the religious-system) | **ศาสนายูดาห์** | 1:13, 1:14 |
| Ἰουδαῖοι (other Jewish-Christian believers in Antioch context) | **ชาวยิว** | 2:13 |
| Ἰουδαῖος (Peter as ethnic-Jew) | **ชาวยิว** | 2:14 |
| Ἰουδαϊκῶς (adverb "in a Jewish manner") | **อย่างชาวยิว** | 2:14 |
| ἐθνικῶς (adverb "in a Gentile manner") | **อย่างคนต่างชาติ** | 2:14 |
| Ἰουδαῖοι by birth (Paul + Peter + Jewish-Christians) | **ชาวยิว** | 2:15 |
| Ἰουδαῖος in the racial-theological abolition formula | **ชาวยิว** | 3:28 |

**Editorial assessment:** The split is principled. **ศาสนายูดาห์** for the comprehensive religio-cultural system (Ἰουδαϊσμός) is the standard modern Thai religious-studies term and exactly captures the rare lemma. **ชาวยิว** uniformly for Ἰουδαῖος-as-ethnic — different from the JHN four-way split (which had ผู้นำชาวยิว for the religious-political leadership). Pauline GAL Ἰουδαῖος is consistently ETHNIC-IDENTITY (vs. Johannine adversarial-leadership); the single rendering ชาวยิว is correct here.

**Cross-cutting note (from JHN audit):** The JHN end-of-book audit recommended a corpus doc `ioudaioi_johannine_2026-04.md` for the four-way split (ผู้นำชาวยิว / ชาวยิว / ยิว / [drift: พวกผู้นำยิว]). GAL's usage is RESTRICTED to **ชาวยิว** (ethnic-identity sense only) — which is itself the second category in the JHN four-way. The forward-doc should LOCK both:
- Johannine 4-way split (per JHN audit §1)
- Pauline ETHNIC-only ชาวยิว default (per this audit §13)

**→ Recommend: STABLE in GAL; defer to 1TH end-of-book** when the Pauline pattern can be confirmed across multiple letters. Then write a unified `ioudaioi_corpus_2026-04.md` covering both Johannine and Pauline distributions.

### 13a. ζηλωτής τῶν πατρικῶν παραδόσεων — Pharisaic ancestral tradition (1:14)

GAL 1:14 includes the **πατρικῶν παραδόσεων** ("ancestral traditions") phrase identical to Mark 7:3, 5, 8, 9, 13 / Matt 15:2, 3, 6 (where Jesus criticizes the Pharisaic παράδοσιν τῶν πρεσβυτέρων). The 1:14 KD explicitly cross-references the Markan/Matthean lexical pair. Thai **ธรรมเนียมของบรรพบุรุษ** ("tradition of ancestors") is consistent with the Synoptic rendering. **STABLE** ✓.

---

## 14. ἐκκλησία / ἀπόστολος / ἀδελφοί — first full Pauline epistle vocabulary — **all LOCKED ✓**

| Lemma | GAL evidence | Status |
|---|---|---|
| ἐκκλησία (3 verses, Christian community) | 1:2 (ταῖς ἐκκλησίαις τῆς Γαλατίας → **คริสตจักรทั้งหลายในแคว้นกาλาเทีย**); 1:13 (ἐδίωκον τὴν ἐκκλησίαν τοῦ θεοῦ → **ข้าพเจ้าได้ข่มเหงคริสตจักรของพระเจ้า**); 1:22 (ταῖς ἐκκλησίαις τῆς Ἰουδαίας ταῖς ἐν Χριστῷ → **คริสตจักรในแคว้นยูเดียซึ่งอยู่ในพระคริสต์**) — uniform. | **LOCKED** per `ekklesia_2026-04.md` |
| ἀπόστολος (4 verses) | 1:1 (Παῦλος ἀπόστολος → **เปาโล อัครทูต**); 1:17 (πρὸ ἐμοῦ ἀποστόλους → **อัครทูตก่อนข้าพเจ้า**); 1:19 (τῶν ἀποστόλων οὐκ εἶδον → **อัครทูตคนอื่น**); 2:8 (ἀποστολὴν τῆς περιτομῆς → **ตำแหน่งอัครทูตของคนที่เข้าสุหนัต**) — uniform **อัครทูต**. | **LOCKED** (Synoptic-Acts pattern) |
| ἀδελφοί (Pauline vocative — 11 verses) | 1:2, 1:11, 4:12, 4:28, 4:31, 5:11, 5:13, 6:1, 6:18 + 1:19 (Lord's brother), 2:4 (false brothers) — uniform **พี่น้อง**. The 1:19 + 2:4 senses (literal kinship + figurative "false brothers") use the same word but disambiguated by context, exactly like Greek. | **LOCKED** |

**LOCKED** ✓ — first-Pauline-epistle compliance with the Synoptic-Acts-Johannine corpus.

---

## 15. OT citations — Pauline density — **all LOCKED + flagged**

Galatians has **7+ formal OT citations + multiple allusions** — Paul's most density per chapter in the early chapters. All correctly flagged with **คำเขียน** ("it is written") + cross-referenced to source + added to `data/nt_ot_citations.json`:

| GAL | OT source | KD/Notes flag |
|---|---|---|
| 3:6 | Gen 15:6 | "ADDED TO NT_OT_CITATIONS: GAL 3:6 → GEN 15:6" |
| 3:8 | Gen 12:3 | citation flagged |
| 3:10 | Deut 27:26 (LXX) | "ADDED TO NT_OT_CITATIONS: GAL 3:10 → DEU 27:26" |
| 3:11 | Hab 2:4 (LXX) | "ADDED TO NT_OT_CITATIONS: GAL 3:11 → HAB 2:4" |
| 3:12 | Lev 18:5 | citation flagged |
| 3:13 | Deut 21:23 | "ADDED TO NT_OT_CITATIONS" |
| 3:16 | Gen 12:7 / 13:15 / 22:18 / 24:7 (the σπέρμα promises) | flagged with christological-singular argument |
| 4:27 | Isa 54:1 (LXX) | citation flagged |
| 4:30 | Gen 21:10 (LXX) | citation flagged |
| 5:14 | Lev 19:18 | "ADDED TO NT_OT_CITATIONS: GAL 5:14 → LEV 19:18" |

**Plus allusions:** 1:15 (Jer 1:5 + Isa 49:1 — Servant-prophet call); 2:16 (Ps 143:2 LXX — "no flesh will be justified"); 4:28 (Isaac promise echoes); 6:16 ("peace and mercy upon them" — possible Ps 125:5 + 128:6 echo).

**LOCKED** ✓ — all citations flagged + sourced. The 5:14 Lev 19:18 is also cross-referenced to Mark 12:31 + Matt 22:39 + Luke 10:27 + James 2:8 + Rom 13:9 in the verse-level rationale.

---

## 16. Inherited locks — **all compliant**

| Doc | GAL evidence | Status |
|---|---|---|
| `ekklesia_2026-04.md` | 1:2, 1:13, 1:22 → **คริสตจักร** uniform. | **LOCKED** |
| `ethnos_2026-04.md` | 9 ἔθνη verses → **คนต่างชาติ** uniform (Pauline mission contexts: 1:16, 2:2, 2:8, 2:9, 2:12, 2:14×2, 2:15, 3:14); 1 → **ประชาชาติ** at 3:8 (cosmic-Psalmic Gen 12:3 quotation: "all the **nations** will be blessed in you"); 1 → **ชนชาติ** at 1:14 (Paul's own "**people-group**" — natural-ethnic sense). All three senses present — exactly per the doc's three-way rule. The χνικῶς "in a Gentile manner" at 2:14 is rendered **อย่างคนต่างชาติ** (adverbial form preserves the Gentile-mission category). | **LOCKED** |
| `kyrios_narrator_voice_luke_acts_2026-04.md` | The doc says "Lukan-Acts signature." GAL has **5 narrator-κύριος references** (1:3, 1:19, 5:10, 6:14, 6:18) — all → **องค์พระผู้เป็นเจ้า**, perfectly compliant with the lock. The doc's Lukan-Acts framing should be **amended** to acknowledge full Pauline extension (this is now compliant in JHN per JHN audit + GAL). | **LOCKED-with-amendment-needed** (already noted in JHN audit §16) |
| `vocative_kyrie_didaskale_register_2026-04.md` | N/A in GAL — no vocative κύριε in this letter (it's a polemical-doctrinal letter, not narrative). | **LOCKED (N/A)** |
| `divine_object_praise_verbs_2026-04.md` | GAL 1:24 ἐδόξαζον ... τὸν θεόν → **ถวายพระเกียรติแด่พระเจ้า** (the narrator-doxological-formal ถวายเกียรติ rendering). Compliant per the Acts-sub-rule. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` | GAL has minimal non-divine authority figures. James is referred to with **น้องชายขององค์พระผู้เป็นเจ้า** (Lord's brother) — plain register for James himself. Peter (Cephas) — plain register throughout (vv. 2:11-14 confrontation). Compliant. | **LOCKED** |
| `narrator_vs_character_voice_2026-04.md` | Royal register on God + Christ throughout (พระเจ้า ทรง-, ตรัส-equivalent in apostolic 1pl voice). Plain register for human authorities (Peter, Barnabas, James, the Galatian agitators). GAL 1:24 ถวายพระเกียรติ for the Judean-Christians' doxological response — narrator-formal-doxological register. Compliant. | **LOCKED** |
| `aramaic_transliterations_2026-04.md` | GAL 4:6 Αββα → **อับบา** + ὁ πατήρ → **พระบิดา** (Aramaic transliteration + Greek translation, per Mark-pattern). | **LOCKED** |
| `inclusion_variants_absent_verses_2026-04.md` | **N/A in GAL** — no Tier 1/2/3 inclusion variants in Galatians (per `output/textual_variants/` absence + per my full-text scan for `[`/`⟦` markers). Several text-critical Notes (1:3 ἡμῶν position; 1:4 ὑπέρ vs. περί; 2:5 negation; 4:6 ἡμῶν vs. ὑμῶν; 4:14 ὑμῶν vs. μου) are **micro-variants** not affecting Thai meaning + handled in verse Notes per RULES §0. No inclusion-bracket policy needed. | **LOCKED (N/A)** |
| `historic_present_2026-04.md` | N/A — Galatians is a doctrinal-polemical letter, not narrative; no historic-present pattern to test. | **LOCKED (N/A)** |
| `parabolic_god_figures_human_register_2026-04.md` | N/A — no parables in GAL. The 4:1-7 heir-coming-of-age **analogy** (not parable) uses plain-register **บิดา** for the human-father analog (correct — analogical, not transparent God-figure). The 4:21-31 Hagar-Sarah **allegory** uses the historical women's names + plain-register categories (slave-girl/free woman). Compliant. | **LOCKED (N/A)** |
| `metanoeo_vs_metamelomai_2026-04.md` | **N/A** — μετανοέω absent from GAL (theologically-significant: GAL's salvation-language is justification-by-faith, not repentance-leading-to-life). | **LOCKED (N/A)** |
| `aphesis_forgiveness_of_sins_2026-04.md` | **N/A** — ἄφεσις absent from GAL (the lemma is salvific-narrative; GAL's atonement-language is δικαιόω + ἐξαγοράζω, not ἄφεσις). | **LOCKED (N/A)** |
| `pagan_deities_2026-04.md` | GAL 4:8 (φύσει μὴ οὖσι θεοῖς "by nature not gods") → **ไม่ใช่เทพเจ้า** (pagan-deity register **เทพเจ้า**, NOT พระเจ้า). Compliant per the doc — this is the only pagan-deity reference in the letter. | **LOCKED** |
| `roman_administrative_titles_2026-04.md` | N/A — no Roman titles in GAL (no governor/centurion/proconsul). | **LOCKED (N/A)** |
| `markan_euthys_immediately_2026-04.md` | N/A — Mark-specific. | **LOCKED (N/A)** |
| `son_of_man_disambiguation_2026-04.md` | N/A — υἱὸς τοῦ ἀνθρώπου absent from GAL. | **LOCKED (N/A)** |
| `psyche_vs_pneuma_anthropological_2026-04.md` | πνεῦμα ἅγιον (16 occurrences) → **พระวิญญาณ** uniform. ψυχή absent from GAL. The 6:18 "with your spirit" closing benediction uses **กับจิตวิญญาณของพวกท่าน** (the Pauline 1pl πνεύματος ὑμῶν → "your inner spiritual self"; with the standard Pauline-corpus rendering of corporate-believer-spirit). Compliant. | **LOCKED** |
| `johannine_doubled_amen_2026-04.md` | N/A — GAL is Pauline, not Johannine. The single ἀμήν at 6:18 → **อาเมน** (the standard chapter-closing acclamation). | **LOCKED (N/A)** |
| `amen_saying_formula_2026-04.md` | N/A — Synoptic-saying-formula doesn't apply (no Jesus-direct-discourse in GAL). | **LOCKED (N/A)** |
| `speech_verbs_adversaries_addressing_divine_2026-04.md` | N/A — no narrative-speech-verbs-by-adversaries-addressing-divine in GAL. | **LOCKED (N/A)** |
| `basileia_kingdom_rendering_2026-04.md` | GAL 5:21 βασιλείαν θεοῦ οὐ κληρονομήσουσιν → **อาณาจักรของพระเจ้า** (consistent with the Synoptic-Acts lock). 1 verse only; compliant. | **LOCKED** |
| `ouranos_heaven_rendering_2026-04.md` | GAL 1:8 (ἢ ἄγγελος ἐξ οὐρανοῦ "an angel from heaven"). Greek noun-with-preposition; rendering preserves the source-of force per the doc. | **LOCKED** |

---

## Mechanical (§1) — **all green**

- 6/6 chapters: `output/check_reports/galatians_NN_review.md` + `_summary.json` + per-chapter sub-reports ✓
- 6/6 chapters: `output/back_translations/galatians_NN.json` ✓
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 128-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (incl. Johannine doubled-amen, ekklesia, ouranos, etc.)
- `git status output/`: only re-ran-check artifacts (key_term_consistency_all.md + phrase_consistency.md modified by my §1 verification re-runs) + 1TH-loop in-flight files (1thessalonians_03 from another active session, NOT touched by this audit). No GAL source-file dirt.

---

## Pre-existing docs affirmed / unchanged

All 24 docs in `docs/translator_decisions/` reviewed. Compliance summary in §16 above. The **Lukan-Acts narrator-κύριος doc** flagged for amendment (already noted in JHN audit) — Galatians provides additional Pauline-corpus confirmation; the doc's "Lukan signature" framing should be renamed/extended to acknowledge corpus-wide narrator-κύριος usage in JHN + Pauline.

---

## Flagged for Ben's attention

### A. πίστις Χριστοῦ — objective-genitive default — **DECIDE before tagging** (§1)
Confirm the objective-genitive ("faith IN Christ") rendering as the corpus default for Romans + the rest of Paul. The verse-level KD at GAL 2:16 explicitly names the alternative subjective-genitive ("faith/faithfulness OF Christ") and rejects it on RULES §0 evangelical-Protestant alignment grounds. **Critical for forward-compounding into Romans 3:21–4:25.**

### B. δικαιόω forensic-declarative rendering — **STABLE, lift to corpus doc** (§2)
The ถูกประกาศว่าชอบธรรม rendering is doctrinally Reformational. Lift to corpus doc `dikaioo_dikaiosune_2026-04.md` before Rom 3 (where the doctrine compounds dramatically).

### C. νόμος multi-sense single-rendering — **STABLE, lift to corpus doc** (§3)
The single-rendering ธรรมบัญญัติ across all 4 senses preserves the Pauline punning. Lift to corpus doc before Rom 7-8 (where 5 νόμος senses compound in 2 verses).

### D. στοιχεῖα τοῦ κόσμου — **REVIEW + lift to corpus doc** (§4)
Confirm หลักการ (option 1: basic principles) as the corpus default before Col 2:8 + 2:20. Verse-level rationale at GAL 4:3 already names this for theological-reviewer attention.

### E. GAL 6:16 "Israel of God" — **DECIDE before tagging**
The 6:16 KD already extensively names the **three-way exegetical fork** (epexegetic καί identifying believers as "the Israel of God" / additive καί distinguishing them / etc.). The verse rendering keeps the Greek καί-ambiguity preserved with **และ** ("and"). **Verify Ben's preferred reading + add a footer-note for theological-reviewer-management** (this is a perennial pulpit-debate; Thai theological reviewers will flag it).

### F. σάρξ multi-sense single-rendering (เนื้อหนัง) — **REVIEW** (§6)
The single-rendering across all 6 senses (idiom, neutral-bodily, ethical-negative, etc.) follows the Pauline pattern but loses surface-distinguishability between the **neutral-bodily 2:20** and the **ethical-negative 5:13–24**. Defensible; worth Ben's confirmation before Rom 7-8 (the densest σάρξ text in NT). Consider corpus doc `sarx_pauline_2026-04.md` as a JHN-doc extension.

### G. παιδαγωγός εἰς Χριστόν — temporal vs directional (§7)
The 3:24 "until Christ" temporal reading is principled but the alternative directional ("leading to Christ") is also defensible. Confirm temporal as corpus default before Rom 10:4 (τέλος ... νόμου Χριστὸς).

### H. ἐκκλησία / ἀπόστολος / ἀδελφοί first-full-Pauline-letter compliance — **LOCKED** (§14)
All three lemmata compliant. No action.

### I. New corpus docs to write (before Romans 1)
1. **`docs/translator_decisions/pistis_christou_2026-04.md`** (§1) — locks objective-genitive default
2. **`docs/translator_decisions/dikaioo_dikaiosune_2026-04.md`** (§2) — locks forensic-declarative rendering
3. **`docs/translator_decisions/nomos_pauline_2026-04.md`** (§3) — locks multi-sense single-rendering policy
4. **`docs/translator_decisions/stoicheia_tou_kosmou_2026-04.md`** (§4) — locks หลักการ (option 1: basic principles)
5. **`docs/translator_decisions/huiothesia_adoption_2026-04.md`** (§12) — brief; locks GAL 4:5 precedent before Rom 8 cluster
6. **(Optional)** `sarx_pauline_2026-04.md` (§6) — extends JHN doc to ethical-negative Pauline sense
7. **(Optional)** `kaine_ktisis_2026-04.md` (§9) — brief; before 2 Cor 5:17

### J. Existing docs to amend
- **`kyrios_narrator_voice_luke_acts_2026-04.md`** — extend to "Lukan-Acts + Johannine + Pauline" or rename. JHN audit already flagged; GAL provides additional confirmation (5 narrator-κύριος uses, all compliant).

### K. External AI review (§3 of checklist) — **pending**
Recommended before `book-galatians-v1` tag. Suggested 4-cluster external AI packet:
1. **GAL 2:11–21** — Antioch incident + first justification-by-faith statement + πίστις Χριστοῦ first 3 occurrences + δικαιόω technical-vocab establishment
2. **GAL 3:1–14** — OT-citation density + Abraham + curse/blessing + ἔργα νόμου
3. **GAL 4:1–11** — adoption + στοιχεῖα + Αββα + sons-not-slaves climax
4. **GAL 6:11–18** — closing autograph + new creation + "Israel of God" + στίγματα

Use Grok + ChatGPT in parallel per the JHN/ACT pattern.

---

## Recommendation

**Galatians ships in strong corpus-hygiene shape — but it carries a heavier-than-usual editorial-decision load** because it is the FIRST FULL Pauline epistle in the corpus. The translator made consistent, principled choices on the four most-debated Pauline lemmata (πίστις-Χριστοῦ, δικαιόω, νόμος, στοιχεῖα) — but **none of these four has a corpus-level doc** yet. This is the moment to lock them in before Romans compounds the editorial weight.

Tag `book-galatians-v1` after:
1. Ben's decisions on **§A + §E + §G** (DECIDE items: πίστις-Χριστοῦ default; "Israel of God" reading; παιδαγωγός εἰς Χριστόν temporal-vs-directional)
2. Ben's confirmations on **§D + §F** (REVIEW items: στοιχεῖα reading; σάρξ multi-sense policy)
3. Five new translator_decisions docs written (§I items 1-5; six if §I-7 included)
4. One existing doc amended (`kyrios_narrator_voice_luke_acts_2026-04.md`)
5. External AI sanity-check (§K)

The Pauline letters (Rom, 1-2 Cor, Eph, Phil, Col, 1-2 Th, Pastorals) can be queued for next book — but writing **`pistis_christou`, `dikaioo_dikaiosune`, `nomos_pauline`, and `stoicheia_tou_kosmou`** docs should happen **before Romans 1:1** to avoid massive forward drift in the most-contested theological vocabulary in the NT.
