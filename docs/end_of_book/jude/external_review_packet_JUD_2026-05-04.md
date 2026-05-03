# Jude — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-04**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Jude** (1 chapters, 25 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged. Jude 1/1 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

### Already-locked corpus decisions — DO NOT re-litigate

- ἐκκλησία (Christian community) → คริสตจักร; secular/OT assembly → ที่ประชุม
- βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า; βασιλεία τῶν οὐρανῶν → อาณาจักรสวรรค์ (Matthew only)
- ἄφεσις ἁμαρτιῶν → การยกโทษบาป; ἄφεσις (release) at LUK 4:18 → ปลดปล่อย
- narrator-voice ὁ κύριος (= Jesus) → องค์พระผู้เป็นเจ้า (Luke-Acts signature)
- vocative Κύριε from disciples/believers → องค์พระผู้เป็นเจ้า; from outsiders → context
- παρρησιάζομαι → อย่างกล้าหาญ
- δοξάζω / εὐλογέω / αἰνέω / αἶνον δίδωμι (object = God) → สรรเสริญ (single Thai default)
- honorifics ราชาศัพท์ for divine subjects + kings (Herod, Agrippa); plain register for governors (Felix, Festus) + non-divine human authorities
- pagan deities → เทพ / เทพี / เทพเจ้า (NEVER พระเจ้า, reserved for the biblical God)
- μετανοέω → กลับใจ (salvific); μεταμέλομαι → เปลี่ยนใจ (non-salvific reconsidering)
- οὐρανός → ฟ้าสวรรค์ (theological default); สวรรค์ (after possessor); ท้องฟ้า (meteorological)
- ψυχή → จิตวิญญาณ / ชีวิต (context); πνεῦμα (anthropological) → จิต — distinct from πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์
- ὁ υἱὸς τοῦ ἀνθρώπου (Christological title) → บุตรมนุษย์; υἱοὶ τῶν ἀνθρώπων (humanity) → บุตรของมนุษย์
- Greek historic-present verbs → Thai past tense (do not preserve present morphology)
- ἀμὴν λέγω ὑμῖν (Synoptic single) → เราบอกความจริงแก่พวกท่าน(ว่า)
- ἀμὴν ἀμὴν λέγω ὑμῖν (Johannine doubled, 25× in John) → อาเมน อาเมน เราบอกแก่พวกท่านว่า — Aramaic-embed treatment
- μονογενὴς θεὸς (JHN 1:18) → พระบุตรองค์เดียวผู้ทรงเป็นพระเจ้าด้วย — exception to standard μονογενής → องค์เดียว lock for the compound
- Aramaic embeds (Talitha cumi, Ephphatha, Abba, etc.) → preserve Thai-script transliteration AND Mark's own Greek translation
- Inclusion-variant Path A (LOCKED): Tier 1 short-phrase `[...]`; Tier 2 whole-verse footer note; Tier 3 large blocks `⟦...⟧` — matches BSB/ESV/NIV/CSB
- Parable characters representing God (fathers, kings, masters, judges) → human register, never ราชาศัพท์
- Narrator introducing adversary speech to Jesus → ทูล (preserves Jesus's divine status regardless of speaker)
- ἔθνος three-way: ประชาชาติ (cosmic/Psalmic) / ชนชาติ (specific people-group, incl. Israel) / คนต่างชาติ (Gentiles, mission target)
- Roman titles: χιλίαρχος → นายพัน; ἑκατοντάρχης → นายร้อย; ἡγεμών → ผู้ว่าราชการ; ἀνθύπατος → ผู้สำเร็จราชการ
- Pagan-deity personal names → transliteration (Zeus → ซีอุส); abstract personifications → descriptive (Δίκη → เทพีแห่งความยุติธรรม)

### What we want from you

The internal end-of-book review surfaced the items below. For each, tell us either (a) "fine as-is, here's why" or (b) "here's a real concern, here's the action." Where you disagree, give specific verse-level reasoning grounded in the Greek + Thai shown.

### What we are NOT asking for

- Don't propose stylistic alternatives "for variety." Consistency in key terms is a feature.
- Don't flag things from the locked-decisions list above. Those are settled.
- Don't suggest re-rendering specific verses for taste. Native Thai reviewers handle stylistic feedback.
- Don't comment on per-chapter automated-check coverage — those all pass.

### Output format

For each item below, return:

```
## [Item letter]: [Short title]
**Verdict:** FINE / CONCERN / MAJOR CONCERN
**Reasoning:** [1-3 sentences citing verses]
**Recommended action:** [specific — "lock as-is", "spot-revise verse X", "write doc Y", or "Ben to decide"]
```

Then a brief **§Z: Anything else?** section if you spot a corpus-level concern outside these items.

---
## Item A — Pseudepigrapha-citation surfacing strategy at JUD 1:9 + JUD 1:14–15: corpus-doc formalization

**The pattern.** Jude is the ONLY NT book that makes direct citations of NON-CANONICAL Jewish pseudepigrapha:

| Verse | Greek | Citation source | Thai_summary present? |
|---|---|---|---|
| **1:9** | `οὐκ ἐτόλμησεν κρίσιν ἐπενεγκεῖν βλασφημίας, ἀλλὰ εἶπεν· Ἐπιτιμήσαι σοι κύριος` | **Assumption of Moses** (also: *Testament of Moses*; lost in full) — Michael-disputing-with-the-devil-over-Moses's-body tradition | ✓ (substantial) |
| **1:14–15** | `Προεφήτευσεν δὲ καὶ τούτοις ἕβδομος ἀπὸ Ἀδὰμ Ἑνὼχ λέγων· Ἰδοὺ ἦλθεν κύριος ἐν ἁγίαις μυριάσιν αὐτοῦ ...` | **1 Enoch 1:9** — direct verbatim quotation introduced with prophetic-formula | ✓ (substantial) |

Both citations also include OT-DB cross-references (the v.9 Michael-rebuke `Ἐπιτιμήσαι σοι κύριος` echoes ZEC 3:2 LXX; recorded in `data/nt_ot_citations.json`).

**The current surfacing strategy:**

For v.9 (`thai_summary` excerpt, English gloss):
> "This verse references a Jewish tradition from the 'Assumption of Moses' (or *Testament of Moses*), an extra-canonical document that recounts the archangel Michael disputing with the devil over Moses's body... Jude does not endorse this document as Scripture, but cites it as an example his Jewish readers would recognize, to point out that even the archangel respects authority in the spiritual realm — so how dare false teachers slander the glorious ones?"

For v.14 (`thai_summary` excerpt, English gloss):
> "Jude cites Enoch's prophecy (Genesis 5:18-24) as it appears in 1 Enoch 1:9. This book is a Jewish pseudepigrapha (3rd-1st c. BC) — not in the Jewish or Protestant Christian canon. Jude's citation does not mean Jude accepts the entire book as Scripture, but means this specific prophecy aligns with God's revelation — like Paul citing Greek poets (Acts 17:28; Titus 1:12). Most Protestant Christians understand this prophecy as true while not regarding all of 1 Enoch as Scripture."

**The interpretive-bound is critical for Thai-Protestant readers.** Without the surfacing, a typical Thai reader could:

- **Misuse direction A:** Assume Jude's citation entails the canonical-status of 1 Enoch / Assumption-of-Moses (the "if it's quoted in Scripture it must be Scripture" inference).
- **Misuse direction B:** Treat the citation as evidence Jude is sub-canonical himself ("Jude quotes apocryphal books, so Jude shouldn't be in the NT"). This was a real concern in early-church canon-debates and remains a concern in some Thai-Christian contexts where Jude's canonicity has been questioned.
- **Misuse direction C:** Confuse Jude's citation-formula `Προεφήτευσεν` ("prophesied") at v.14 as endorsement of 1 Enoch's full prophetic-status.

The current thai_summary entries bound (A) and (C) explicitly via the Pauline-poets-citation parallel (ACT 17:28 + TIT 1:12) and the "specific prophecy aligns with God's revelation" framing.

**The corpus-doc question.** The two-verse-level thai_summary entries handle the surfacing well at the verse-level. The DECIDE question is whether to formalize the strategy as a NEW corpus doc `docs/translator_decisions/pseudepigrapha_citations_2026-05.md` to:

1. Document the pseudepigrapha-citation surfacing-strategy as a project-wide standard;
2. Specify the Protestant interpretive frame (citation ≠ canonical-status; analogous to Pauline-poet-citation);
3. Cross-reference the existing handling of 2 PET 2:4 fallen-angels-tradition allusion (1 Enoch 6–21 stream — same-tradition, treated more allusively at 2 PET 2:4 + JUD 1:6) for cross-corpus harmonization;
4. Specify that future analogous cases (none in NT outside Jude + 2 Peter) should follow the same Protestant frame.

The corpus doc would close the NT corpus on this question — no further test cases (Revelation does not cite pseudepigrapha).

**Two surfacing options:**

**Option A (status quo).** Keep verse-level thai_summary entries; treat as STABLE per-verse handling.

**Option B (proposed).** Create `pseudepigrapha_citations_2026-05.md` formalizing the strategy. Single-author, ~1 hour. Closes the corpus.

**Editorial assessment.** Option B has the upside of giving the project a referenceable standard if external reviewers raise the canonical-status question, harmonizing JUD 9 + JUD 14–15 + JUD 6 (allusive) + 2 PET 2:4 (allusive) into a single principled documentation, and signaling-clearly to Thai-Protestant readers that the project has thought-through the canonical-status question rather than leaving it implicit.

**Three questions:**
1. Is the current per-verse thai_summary surfacing adequate (Option A — status quo), or should the project formalize a NEW corpus doc to lift the surfacing-strategy to project-wide standard (Option B)?
2. If Option B, should the corpus doc cross-reference the JUD 1:6 + 2 PET 2:4 fallen-angels-allusions to the SAME 1 Enoch tradition stream, treating the citation-vs-allusion distinction as the principled differentiation?
3. Is the Pauline-poet-citation parallel (ACT 17:28 Aratus + TIT 1:12 Epimenides) the right frame for the Protestant interpretive-bound, or is there a stronger frame (e.g., the early-church distinction between *citation-of-truth* vs *endorsement-of-source*) that the corpus doc should adopt?

---

## Item B — Doxology v.25 Christological-mediation surfacing: `μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ`

**The textual question.** JUD 1:25 contains the famous closing doxology of Jude:

> **μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ τοῦ κυρίου ἡμῶν** δόξα μεγαλωσύνη κράτος καὶ ἐξουσία πρὸ παντὸς τοῦ αἰῶνος καὶ νῦν καὶ εἰς πάντας τοὺς αἰῶνας· ἀμήν.
> **แด่พระเจ้าผู้ทรงเป็นพระผู้ช่วยให้รอดของเราแต่องค์เดียว โดยทางพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** ขอพระสิริ พระบารมี ฤทธานุภาพ และสิทธิอำนาจ จงมีแด่พระองค์ก่อนกาลทั้งสิ้น ทั้งบัดนี้และตลอดทุกยุคทุกสมัย อาเมน

**The interpretive question.** The phrase admits two readings:

| Reading | Construal | Theological consequence |
|---|---|---|
| **Trinitarian-mediation (Eremos current)** | "the only God [the Father, the] Savior of-us, [acting] through Jesus Christ our Lord" | God-the-Father is Savior; salvation-mediated through Christ |
| **Subordinationist-flat** (rejected) | "the only God [is] our Savior; [we know him] through Jesus Christ our Lord" | (compatible with #1; some early-modern critics read this as flat-monotheist anti-Christ-divinity, but mainstream Protestant reads it #1) |

**The KD already disambiguates against the subordinationist-flat reading:**
> Per uW: 'the only God' here = the Father (the qualifier emphasizes monotheism while preserving the Christological-mediation 'through Jesus Christ'). σωτήρ-of-Father → พระผู้ช่วยให้รอด (matches 1 TIM 1:1, 2:3, 4:10 'God-our-Savior' context — distinct from Granville-Sharp Christological-σωτήρ at 2 PET 1:1 + 1:11 + TIT 2:13).

**The translation surface.** The Thai uses the ordinary structure **แด่พระเจ้า ผู้ทรงเป็นพระผู้ช่วยให้รอดของเราแต่องค์เดียว โดยทางพระเยซูคริสต์องค์พระผู้เป็นเจ้าของเรา** ("to God, who is our Savior alone, through-the-way-of Jesus Christ our Lord"). The **โดยทาง** ("through-the-way-of," instrumental-mediation) preserves the Christological-mediation reading clearly. The **แต่องค์เดียว** ("alone, only one") preserves the monotheism-emphasis (μόνῳ).

**The deliberate-contrast with 2 PET 1:1 + TIT 2:13.** Jude's syntax DELIBERATELY avoids the Granville-Sharp pattern that 2 PET 1:1, 1:11 + TIT 2:13 use. Compare:

| Verse | Greek | Both-titles-apply-to | Thai (Eremos) |
|---|---|---|---|
| **2 PET 1:1** | `τοῦ θεοῦ ἡμῶν καὶ σωτῆρος Ἰησοῦ Χριστοῦ` | Christ (Granville-Sharp) | (renders Christ-as-both-titles) |
| **TIT 2:13** | `τοῦ μεγάλου θεοῦ καὶ σωτῆρος ἡμῶν Ἰησοῦ Χριστοῦ` | Christ (Granville-Sharp) | (renders Christ-as-both-titles) |
| **JUD 1:25** | `μόνῳ θεῷ σωτῆρι ἡμῶν διὰ Ἰησοῦ Χριστοῦ` | Father (with Christological-mediation) | "to God-our-Savior alone, through Christ" |

The cross-corpus distinction is theologically-substantive: 2 PET 1:1 + TIT 2:13 affirm Christ-is-θεός (Christ-divinity); JUD 1:25 affirms Father-is-σωτήρ (with Christological-mediation). Both are orthodox; the structural-distinction matters for trinitarian-grammar.

**The interpretive surface.** A typical Thai-Protestant reader who encounters the Eremos `แด่พระเจ้า ... โดยทางพระเยซูคริสต์` will likely read it correctly (the **โดยทาง** mediation-marker is unambiguous), BUT will not see the deliberate-contrast with the Granville-Sharp pattern unless the thai_summary names it. The KD carries the analysis but is invisible to typical readers.

**Two surfacing options:**

**Option A (current).** Bare doxology; verse-level KD carries the analysis; no thai_summary at v.25.

**Option B (proposed).** Add a `thai_summary` at v.25 noting:

> "พระเจ้า" ในข้อนี้หมายถึงพระบิดา; "พระผู้ช่วยให้รอด" คือบทบาทของพระบิดา; "โดยทางพระเยซูคริสต์" หมายถึงบทบาทของพระบุตรในการเป็นสื่อกลางแห่งการช่วยให้รอด โครงสร้างนี้แตกต่างจาก 2 เปโตร 1:1 และ ทิตัส 2:13 ที่ทั้ง "พระเจ้า" และ "พระผู้ช่วยให้รอด" ระบุถึงพระคริสต์ (Granville-Sharp) คำสรรเสริญสี่องค์ประกอบ (พระสิริ + พระบารมี + ฤทธานุภาพ + สิทธิอำนาจ) ครอบคลุมกาลเวลาสามมิติ (ก่อนกาลทั้งสิ้น + บัดนี้ + ตลอดทุกยุคทุกสมัย)

(English gloss: "'God' here = the Father; 'Savior' is the Father's role; 'through Jesus Christ' is the Son's role as mediator-of-salvation. This structure differs from 2 Peter 1:1 and Titus 2:13 where both 'God' and 'Savior' identify Christ (Granville-Sharp). The four-fold doxological attributes (glory + majesty + power + authority) span three temporal dimensions (before all time + now + forever).")

**Editorial assessment of options.** Option B has higher upside than Item A (pseudepigrapha) because:
- The doxology is the climax of the letter and the single most-frequently-quoted Jude passage in liturgical contexts (Thai-Protestant benediction-usage is widespread);
- The trinitarian-mediation construal preserves Christ's divinity AND the monotheism-emphasis simultaneously — a thai_summary that names this bounds the subordinationist-flat misreading;
- The deliberate-contrast with 2 PET 1:1 + TIT 2:13 is structurally-significant for trinitarian-grammar; surfacing it allows the cross-corpus reading.

**Three questions:**
1. Stay with Option A (current — historical-context only in KD, invisible to typical readers) or move to Option B (add v.25 thai_summary surfacing the trinitarian-mediation construal + the deliberate-contrast with 2 PET 1:1 + TIT 2:13)?
2. Is the practical risk of Option A — Thai-Protestant liturgical-readers reading the doxology subordinationist-flat (treating the Father-Savior reading as anti-Christ-divinity) — significant enough to warrant the surfacing-cost of Option B?
3. If Option B, should the thai_summary cascade to 2 PET 1:1 + TIT 2:13 (the Granville-Sharp counterparts) so the three passages have parallel surfacing of the trinitarian-grammar distinction?

---

## Item C — ἐπαγωνίζομαι at JUD 1:3 → ต่อสู้อย่างเข้มแข็ง: Jude's programmatic statement

**The pattern.** JUD 1:3 contains the famous programmatic statement of the entire letter — the verse-of-record for the project's standard of "the faith once-for-all delivered":

> Ἀγαπητοί, πᾶσαν σπουδὴν ποιούμενος γράφειν ὑμῖν περὶ τῆς κοινῆς ἡμῶν σωτηρίας ἀνάγκην ἔσχον γράψαι ὑμῖν παρακαλῶν **ἐπαγωνίζεσθαι** τῇ ἅπαξ παραδοθείσῃ τοῖς ἁγίοις πίστει.
> ท่านที่รัก เมื่อข้าพเจ้าได้พยายามอย่างเต็มที่ที่จะเขียนถึงท่านเรื่องความรอดที่เรามีร่วมกัน ข้าพเจ้าเห็นว่าจำเป็นต้องเขียนถึงท่าน เพื่อขอวิงวอนท่านให้**ต่อสู้อย่างเข้มแข็ง**เพื่อความเชื่อที่ทรงมอบแก่ธรรมิกชนทั้งหลายครั้งเดียวสำหรับทุกยุคทุกสมัย

The 1:3 KD names the agonistic-imagery:

> HAPAX ἐπαγωνίζομαι (only here NT, 'contend-strenuously' — intensified ἀγωνίζομαι) → ต่อสู้อย่างเข้มแข็ง. The agonistic-imagery (cf. 1 TIM 6:12 ἀγωνίζου τὸν καλὸν ἀγῶνα same lemma).

**The lexical question.** The lemma is a rare-Koine intensified-form of ἀγωνίζομαι. The simple form appears at:
- 1 COR 9:25 — ἀγωνιζόμενος (athletic-training)
- COL 1:29; 4:12 — Paul's striving in prayer/proclamation
- 1 TIM 6:12 — `ἀγωνίζου τὸν καλὸν ἀγῶνα τῆς πίστεως` ("fight the good fight of faith") — the most-direct conceptual parallel
- 2 TIM 4:7 — `τὸν καλὸν ἀγῶνα ἠγώνισμαι` (Paul's farewell)

The intensified ἐπ-prefix marks an "additional" or "for-something" sense — *contend on-behalf-of* rather than just "struggle." Jude's grammatical structure (`ἐπαγωνίζεσθαι τῇ ... πίστει`, dative-of-cause-or-defense) makes the on-behalf-of sense explicit: contend FOR the faith.

**Modern translations vary:**
- ESV / NASB: "contend earnestly for the faith"
- NIV: "contend for the faith"
- CSB / NLT: "contend for the faith" / "defend the faith"
- KJV: "earnestly contend for the faith"

**Modern Thai versions:**
- THSV: **ต่อสู้เพื่อความเชื่อ** ("fight for the faith" — adverb dropped)
- THKJV: **ต่อสู้เพื่อความเชื่อ** (same simplification)

**The current rendering: ต่อสู้อย่างเข้มแข็ง** ("strive-fight strongly") preserves the intensifier (อย่างเข้มแข็ง), which simpler Thai versions drop. This is principled — the ἐπ-prefix is morphologically marked in Greek; preserving an adverbial-marker in Thai is the natural-equivalent strategy.

**Alternative Thai constructions:**
- **ต่อสู้อย่างเข้มแข็ง** (current) — "strongly" / vigorous register
- **ต่อสู้อย่างหนักแน่น** — "steadfastly" — more theologically-loaded
- **ต่อสู้อย่างไม่ลดละ** — "unrelentingly" — matches the agonistic-Pauline register more closely
- **ต่อสู้สุดกำลัง** — "with-all-strength" — colloquial-elevated

**Two questions:**
1. Is **ต่อสู้อย่างเข้มแข็ง** the right rendering for the active-loving-pursuit force of ἐπ-prefix at JUD 1:3 ("contend earnestly for the faith once-for-all delivered"), or should it match the THSV simpler **ต่อสู้** (dropping the adverb) for cross-Bible Thai-readability at the cost of softening the intensifier-nuance?
2. If the intensifier is preserved, is **อย่างเข้มแข็ง** ("strongly") the right adverb, or should it be elevated to **อย่างหนักแน่น** (steadfast, more theological-register) or **อย่างไม่ลดละ** (unrelenting, matches the agonistic-Pauline imagery at 2 TIM 4:7) to mark this as Jude's programmatic-statement rather than a generic "struggle"?

---

## Item D — Pastoral triage at JUD 1:22–23: three-fold mercy + ZEC 3 / LEV 13 priestly-defilement imagery

**The pattern.** JUD 1:22–23 closes the letter's body with a three-fold pastoral-triage of-doubting-believers:

| Category | Greek | Thai (current) |
|---|---|---|
| (a) doubting-mercy | οὓς μὲν ἐλεᾶτε διακρινομένους | จงเมตตาบางคนที่ยังไม่แน่ใจ |
| (b) fire-rescue | οὓς δὲ σῴζετε ἐκ πυρὸς ἁρπάζοντες | จงช่วยบางคนให้รอดโดยฉุดเขาออกจากไฟ |
| (c) fearful-mercy with-clothing-hatred | οὓς δὲ ἐλεᾶτε ἐν φόβῳ, μισοῦντες καὶ τὸν ἀπὸ τῆς σαρκὸς ἐσπιλωμένον χιτῶνα | จงเมตตาบางคนด้วยความเกรงกลัว เกลียดชังแม้แต่เสื้อผ้าที่เปื้อนด้วยเนื้อหนัง |

**The three-fold structure.** SBLGNT prints the three-fold reading; some-mss collapse to two clauses. Eremos correctly follows SBLGNT (RULES §0).

**The OT-imagery layer.** Two OT-imagery threads run through the passage:

- **ZEC 3:2** ("a brand-plucked-from-the-fire") — same Joshua-the-high-priest scene as the JUD 1:9 Michael-rebuke citation (`Ἐπιτιμήσαι σοι κύριος`). The (b) fire-rescue clause echoes ZEC 3:2 thematically; corpus-internal-link with v.9's ZEC-citation.
- **ZEC 3:3–4 + LEV 13:47** — the priestly-defilement clothing-hatred imagery. The "stained-tunic" (`χιτῶνα ἐσπιλωμένον ἀπὸ τῆς σαρκός`) recalls Joshua's filthy-garments in Zechariah 3 + the leprous-cloth contagion-purity laws in Leviticus 13.

The (c) clause's σπίλος cognate (`ἐσπιλωμένον`) shares root-family with 2 PET 2:13 σπίλοι ("blots/stains") — corpus-internal-link.

**Editorial assessment of the current rendering.** The Thai preserves the three-fold structure cleanly. The **ฉุดเขาออกจากไฟ** ("snatch-them-out-of-fire") preserves the urgent-rescue imagery. The **เสื้อผ้าที่เปื้อนด้วยเนื้อหนัง** ("garment stained-by-flesh") preserves the priestly-defilement imagery literally; this is a deliberately-startling Thai phrasing that mirrors the deliberately-startling Greek.

**The interpretive surface.** A typical Thai reader encountering **เสื้อผ้าที่เปื้อนด้วยเนื้อหนัง** at v.23 may not immediately decode the priestly-defilement reference (ZEC 3:3–4 + LEV 13:47). The verse `notes` carries the analysis but is invisible to typical readers. The Thai preserves the literal-imagery faithfully, but the OT-imagery-load is heavy and possibly cryptic without the cross-references.

**Two surfacing options:**

**Option A (current).** Bare three-fold-narrative; verse-level `notes` carries the analysis; no thai_summary at v.22 or v.23.

**Option B (proposed).** Add a `thai_summary` at v.23 (the verse with the heaviest OT-imagery-load) noting:
1. The three-fold pastoral-triage structure (doubting-mercy + fire-rescue + fearful-mercy);
2. The ZEC 3:2 "brand-plucked-from-the-fire" cross-reference for the (b) fire-rescue clause;
3. The ZEC 3:3–4 + LEV 13:47 priestly-defilement imagery for the (c) clothing-hatred clause;
4. The σπίλος cognate cross-corpus link with 2 PET 2:13.

**Editorial assessment of options.** Option B has moderate upside:
- The OT-imagery-load is concentrated in the (c) clause, which is the most-startling phrasing in the entire letter;
- The ZEC 3 + LEV 13 cross-references are not common-knowledge for Thai-Protestant readers;
- The cross-corpus-link with v.9 (ZEC 3:2 Michael-rebuke citation) is structurally-significant — vv. 22–23 close the letter's body with the same ZEC-3-imagery that opens the false-teacher-polemic section at v.9; surfacing this allows the inclusio-reading.

**Two questions:**
1. Stay with Option A (current — bare imagery, KD-only analysis) or move to Option B (add v.23 thai_summary surfacing the three-fold structure + the ZEC 3:3–4 / LEV 13:47 priestly-defilement imagery + the σπίλος cross-corpus link)?
2. If Option B, should the thai_summary also note the inclusio-reading (vv. 22–23 ZEC 3 imagery closes the letter's body that opened with the v.9 ZEC 3 Michael-rebuke citation), or is the per-verse OT-imagery surfacing sufficient?

---

## Item E — Catholic-Epistle πληθυνθείη greeting verb cross-corpus split

**The pattern.** The optative-passive `πληθυνθείη` ("may-X-be-multiplied") is the distinctive Catholic-Epistle opening-greeting verb. It appears in three NT openings:

| Verse | Greek | Thai (current) |
|---|---|---|
| 1 PET 1:2 | χάρις ὑμῖν καὶ εἰρήνη **πληθυνθείη** | ขอพระคุณและสันติสุขจง**ทวียิ่งขึ้น**แก่ท่านทั้งหลาย |
| 2 PET 1:2 | χάρις ὑμῖν καὶ εἰρήνη **πληθυνθείη** ἐν ἐπιγνώσει ... | ขอพระคุณและสันติสุขจง**ทวีคูณ**แก่ท่านทั้งหลาย |
| JUD 1:2 | ἔλεος ὑμῖν καὶ εἰρήνη καὶ ἀγάπη **πληθυνθείη** | ขอพระเมตตา สันติสุข และความรัก จง**ทวีคูณ**แก่ท่านทั้งหลาย |

**The cross-corpus inconsistency.** 1 PET 1:2 uses **ทวียิ่งขึ้น** ("be more abundant" / "increase further"); 2 PET 1:2 + JUD 1:2 use **ทวีคูณ** ("multiply"). Both are valid Thai renderings of πληθυνθείη; the verb does not have a fixed Thai-corpus lock per `glossary.json` or any existing translator-decisions doc, and the phrase-consistency check tolerates this split (it is not a phrase-lock).

**The KD-level signal.** The 2 PET 1:2 KD claims formula-identity with 1 PET ("Same opening-formula as 1 PET 1:2 (πληθυνθείη → จงทวีคูณ)") but renders differently from the actual 1 PET. The JUD 1:2 KD names the corpus-internal-link with 1 PET 1:2 + 2 PET 1:2 ("Catholic-Epistle-openers") and uses ทวีคูณ. The split is therefore a verse-level-rendering artifact, not a principled distinction.

**Lexical analysis:**
- **ทวียิ่งขึ้น** ("[increase] more-and-more") — comparative-incremental sense; preserves the optative "may-it-grow-further" nuance
- **ทวีคูณ** ("multiply") — multiplicative sense; preserves the πληθυνθείη "may-be-multiplied" force more directly

The Greek aorist-optative-passive third-person πληθυνθείη is mood-of-wish + multiplicative-passive — the more direct rendering is **ทวีคูณ**.

**Two harmonization options:**

**Option A.** Harmonize: change 1 PET 1:2 to **ทวีคูณ** to match 2 PET + JUD. (Two-thirds-of-the-corpus already uses **ทวีคูณ**; this is the smaller change.)

**Option B.** Harmonize the other direction: change 2 PET + JUD to **ทวียิ่งขึ้น** to match 1 PET. (One-third already uses; this is the larger change.)

**Option C.** Leave as-is (current state). Both are defensible Thai-equivalents; the split has no semantic consequence.

**Two questions:**
1. Should the Catholic-Epistle πληθυνθείη greeting verb be harmonized across 1 PET + 2 PET + JUD, or left as-is (Option C)? If harmonized, which direction (Option A → all-ทวีคูณ; Option B → all-ทวียิ่งขึ้น)?
2. Is **ทวีคูณ** ("multiply") or **ทวียิ่งขึ้น** ("increase further") the better Thai rendering for the aorist-optative-passive πληθυνθείη force ("may-X-be-multiplied")? The multiplicative-passive lexicon favors ทวีคูณ; the comparative-incremental nuance favors ทวียิ่งขึ้น.

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
