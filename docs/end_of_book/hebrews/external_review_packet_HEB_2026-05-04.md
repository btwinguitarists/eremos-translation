# Hebrews — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-04**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Hebrews** (13 chapters, 303 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged; Revelation complete (not yet tagged). Hebrews 13/13 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

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
## Item A — HEB 1:8 ὁ θεός vocative addressed to Christ — the most-explicit Christological-divinity citation in the NT

**The textual fact:** PSA 45:6 LXX `ὁ θρόνος σου ὁ θεὸς εἰς τὸν αἰῶνα τοῦ αἰῶνος` is cited at HEB 1:8 with the apparent **vocative ὁ θεός addressed TO THE SON** (per the v.7-9 surrounding "But to the Son He says..." framing).

**The Thai rendering takes the vocative-direct-address-to-Christ reading:**

- HEB 1:8 GK: `πρὸς δὲ τὸν υἱόν·Ὁ θρόνος σου ὁ θεὸς εἰς τὸν αἰῶνα τοῦ αἰῶνος, καὶ ἡ ῥάβδος τῆς εὐθύτητος ῥάβδος τῆς βασιλείας σου`
- TH: `แต่เกี่ยวกับพระบุตร พระเจ้าตรัสว่า "**ข้าแต่พระเจ้า** บัลลังก์ของพระองค์ดำรงอยู่ตลอดไปเป็นนิตย์ และคทาแห่งความเที่ยงธรรมเป็นคทาแห่งราชอาณาจักรของพระองค์"`

The **ข้าแต่พระเจ้า** is the standard biblical-Thai vocative-direct-address-to-God ("O God!"). Rendering this as direct-address-to-Christ is theologically deliberate.

**The 1:8 KD explicitly names the choice and rejects the alternative:**

> CRITICAL: 'ὁ θεός' here = vocative 'O-God!' addressed-TO-the-Son — explicit-Christological-divinity-citation. Translation ข้าแต่พระเจ้า preserves-vocative-direct-address. Alternative-rendering 'God-is-your-throne' (Jehovah's-Witnesses) is-grammatically-possible-but contextually-and-theologically-rejected: HEB's-argument requires-divine-address.

**The binitarian-Christology compounds at HEB 1:9:**
- GK: `ἔχρισέν σε ὁ θεός, ὁ θεός σου, ἔλαιον ἀγαλλιάσεως`
- TH: `**พระเจ้าซึ่งเป็นพระเจ้าของพระองค์** ได้ทรงเจิมพระองค์ด้วยน้ำมันแห่งความชื่นชมยินดี`

So in v.8 the Father addresses the Son as θεός; in v.9 the Father is named θεός σου ("your God") relative to the Son. **BOTH Father AND Son are addressed as θεός in two adjacent verses** — the most-explicit binitarian-Christology citation in the NT.

**Two questions:**
1. Is the vocative-direct-address-to-Son rendering (**ข้าแต่พระเจ้า**) defensible against the JW-counter-reading "God is your throne" (taking ὁ θεός as nominative subject of an implied copular clause)? The Greek is genuinely ambiguous syntactically; the contextual force ("But to the Son He says...") drives the vocative-reading. Is there contextual or grammatical evidence that would shift the choice?
2. Should a footer-note at HEB 1:8 acknowledge the JW alternative rendering for academically-engaged readers, or does naming the alternative pastorally-undermine the Christological-divinity force the verse demands? RULES §0 binds the project to evangelical-Protestant editorial alignment + mainstream-Thai reader expectation; the JW-reading is a Trinity-denying minority position. Recommendation: keep the rendering; do NOT add a footer-note that names the JW position.

---

## Item B — HEB 6:4-6 the apostasy passage — FOUR HAPAX + the most-contested NT-warning passage

**The text:**
- HEB 6:4-6 GK: `Ἀδύνατον γὰρ τοὺς ἅπαξ φωτισθέντας γευσαμένους τε τῆς δωρεᾶς τῆς ἐπουρανίου καὶ μετόχους γενηθέντας πνεύματος ἁγίου καὶ καλὸν γευσαμένους θεοῦ ῥῆμα δυνάμεις τε μέλλοντος αἰῶνος, καὶ παραπεσόντας, πάλιν ἀνακαινίζειν εἰς μετάνοιαν, ἀνασταυροῦντας ἑαυτοῖς τὸν υἱὸν τοῦ θεοῦ καὶ παραδειγματίζοντας.`

- TH: `เพราะเป็นไปไม่ได้ที่จะนำคนเหล่านั้น ผู้ซึ่งครั้งหนึ่งเคยได้รับความสว่าง ผู้ได้ลิ้มรสของประทานแห่งสวรรค์ และได้กลายเป็นผู้มีส่วนร่วมในพระวิญญาณบริสุทธิ์ และได้ลิ้มรสพระวจนะอันดีของพระเจ้า และฤทธิ์เดชแห่งยุคที่จะมาถึง และแล้วก็หลงทางไป — ที่จะนำเขาเหล่านั้นกลับมาสู่การกลับใจอีกครั้ง เพราะพวกเขาเองตรึงพระบุตรของพระเจ้าบนกางเขนซ้ำอีก และประจานพระองค์ต่อสาธารณชน`

**FOUR HAPAX** in this passage (only-here-NT vocabulary):
- **παραπίπτω** (v.6) → **หลงทางไป** ("gone-astray-from-the-path")
- **ἀνακαινίζω** (v.6) → **นำกลับมา ... อีกครั้ง** ("renew/restore")
- **ἀνασταυρόω** (v.6) → **ตรึง...บนกางเขนซ้ำอีก** ("re-crucify" / "crucify-again")
- **παραδειγματίζω** (v.6) → **ประจาน...ต่อสาธารณชน** ("publicly shame")

**Translator's policy: deliberate ambiguity.** The 6:6 KD acknowledges the three traditional interpretive streams — Calvinist (these aren't true believers), Arminian (true apostasy is possible), Hypothetical (rhetorical-impossible-condition) — and renders the Thai to **preserve the ambiguity**, allowing the Thai reader to occupy any of the three positions theologically without the translation pre-committing.

The KD on ἀνασταυρόω explicitly chose the "again" reading:
> Most-evangelical-translations follow-(1) [crucify-again] (BSB, ESV, NIV: 'crucifying-again'). Thai ตรึง...บนกางเขนซ้ำอีก preserves-the-'again'-reading.

**Two questions:**
1. Is the deliberate-ambiguity policy the right call for a CC0 Thai NT — or should the project commit explicitly to one of the three interpretive streams (Calvinist / Arminian / Hypothetical) in a footer-note? The current Thai is theologically-load-bearing in either direction (one can read the impossibility-of-renewal either as describing impostors who never had genuine faith, OR as describing real apostates who cannot be brought back, OR as rhetorical-impossible-condition the author deploys as warning). RULES §0 binds the project to evangelical-Protestant editorial alignment, but evangelical-Protestants disagree (5-point Calvinists vs Arminians vs eclectic positions).
2. Should ἀνασταυρόω be rendered with the **"again"** force (current Thai: **ซ้ำอีก** "again") or the **intensive-form** force (alternative: simply **ตรึง**...**บนกางเขน** "crucify on the cross" — emphasizing the act, not its repetition)? BSB / ESV / NIV all read "again" (HEB 6:6 NIV: "...subjecting him to public disgrace by crucifying him all over again"). The intensive-only reading is a minority position (Westcott; Bruce). Confirm the "again" reading is intentional.

---

## Item C — HEB 10:5 LXX σῶμα vs MT אזנים — the most-significant LXX/MT divergence-citation in the NT

**The textual fact:** PSA 40:6 has two divergent text-traditions:
- **LXX (Greek)**: `θυσίαν καὶ προσφορὰν οὐκ ἠθέλησας, σῶμα δὲ κατηρτίσω μοι` ("sacrifice and offering you did not want, but a **BODY** you have prepared for me")
- **MT (Hebrew)**: `זבח ומנחה לא חפצת אזנים כרית לי` ("sacrifice and offering you did not desire, **EARS** you have dug for me")

The LXX reading is a substantive translation-departure from the MT, possibly via a metonymy (open-ears → open-body for receiving) or a textual emendation. **Hebrews 10:5 cites the LXX form** — and the LXX-σῶμα is theologically essential to the author's argument: Christ's incarnation-body is what is "prepared" for sacrifice (continuing through 10:10 "sanctified through the offering of the body of Jesus Christ").

**The Thai follows LXX:**
- HEB 10:5 GK: `Θυσίαν καὶ προσφορὰν οὐκ ἠθέλησας, **σῶμα** δὲ κατηρτίσω μοι`
- TH: `"เครื่องบูชาและของถวายพระองค์ไม่ทรงประสงค์ แต่**พระกาย**พระองค์ได้ทรงเตรียมไว้สำหรับข้าพระองค์"`

The 10:5 KD acknowledges the textual-issue and follows-LXX intentionally:

> uW textual-issue: LXX-Ps-40:6 has 'σῶμα' (body); MT-Hebrew has 'ears you have dug for me' (אזנים כרית לי). The author follows LXX which is what the Spirit's-incarnation-typology requires. σῶμα → พระกาย (with-พระ-honorific for Christ's body, Christological-divine-reference).

**Editorial weight:** RULES §0 binds the project source-text to SBLGNT, NOT to MT. The Greek-text-faithful rendering in this NT-citation context is principled — the NT-author cites the LXX-form, and the project translates the NT-author's-citation as-given. But this is the clearest LXX/MT-divergence-citation in the NT, and Thai readers familiar with the OT translation tradition (which follows MT for the OT) will see the divergence.

**Two questions:**
1. Is the policy (translate-the-NT-author's-LXX-citation as-given, even where it diverges materially from the MT-OT) the right corpus default? This is the project's existing position (RULES §0), but HEB 10:5 is the test-case where the divergence is most-visible and theologically-essential. Confirm that the LXX-faithful policy continues. The alternative would be to add a footer-note acknowledging the MT-divergence — recommended? OR does footer-noting LXX/MT-divergences invite a slippery-slope of textual-criticism distractions?
2. The 10:5 σῶμα is rendered **พระกาย** (with royal pระ-prefix because the referent is Christ's incarnational-body). The MT-faithful "ears" would render as **หู** (plain, no royal). The LXX-faithful **พระกาย** is theologically-superior for the author's argument. Confirm this is the project default rendering in any future LXX/MT-divergence case (NT-author-citation-form takes priority over MT-OT-form).

---

## Item D — HEB 4:12 ψυχή / πνεῦμα crux — the second corpus exception to the locked psyche/pneuma rule

**The locked rule:** `psyche_vs_pneuma_anthropological_2026-04.md` (per `docs/CHAPTER_REVIEW_PROMPT.md` line 38):
> ψυχή → จิตวิญญาณ / ชีวิต (context); πνεῦμα (anthropological) → จิต — distinct from πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์

**HEB 4:12 — the soul/spirit doublet:**
- GK: `Ζῶν γὰρ ὁ λόγος τοῦ θεοῦ καὶ ἐνεργὴς καὶ τομώτερος ὑπὲρ πᾶσαν μάχαιραν δίστομον καὶ διϊκνούμενος ἄχρι μερισμοῦ **ψυχῆς καὶ πνεύματος**, ἁρμῶν τε καὶ μυελῶν`
- TH: `เพราะพระวจนะของพระเจ้านั้นทรงพระชนม์อยู่และมีฤทธิ์ คมยิ่งกว่าดาบสองคมใด ๆ และแทงทะลุจนถึงการแบ่ง**จิตวิญญาณและวิญญาณ** ข้อต่อและไขในกระดูก`

Renderings:
- **ψυχή → จิตวิญญาณ** (compliant with locked rule)
- **πนεῦμα → วิญญาณ** (NOT compliant: locked rule requires **จิต**)

The 4:12 KD acknowledges the choice but does not explain the departure:
> ψυχή/πνεῦμα distinguished here: จิตวิญญาณ (soul, animating-life) / วิญญาณ (spirit, divine-relating). Per-corpus-lock-pattern psyche-vs-pneuma anthropology.

**Compounds with the 1Th 5:23 tripartite-listing exception** (already flagged in 1 Thess audit §6 + §E). The two listings render with PARTIAL-OVERLAP but not-identically:

| Verse | Greek | Thai for ψυχή | Thai for πνεῦμα |
|---|---|---|---|
| 1Th 5:23 | πνεῦμα + ψυχή + σῶμα | **จิตใจ** | **วิญญาณ** |
| HEB 4:12 | ψυχή + πνεῦμα | **จิตวิญญาณ** | **วิญญาณ** |

Both depart from the locked corpus rule. The 1Th audit recommended amending the existing `psyche_vs_pneuma_anthropological_2026-04.md` doc with a 1Th 5:23 sub-section. HEB 4:12 is a parallel second exception.

**Two questions:**
1. Are the HEB 4:12 + 1Th 5:23 exceptions both principled (each fitting the verse's distinct rhetorical context — Word-piercing-discernment at HEB 4:12; trichotomy-prayer at 1Th 5:23)? If yes: the existing doc should be amended with TWO sub-sections (one per verse) and the locked-corpus-rule remains for all other contexts. If no: one or both verses need revision to enforce the corpus rule (would be costly — both are major theological verses with established renderings).
2. Cross-text consistency: should HEB 4:12 + 1Th 5:23 use the SAME Thai pairing for cross-text consistency? Currently they differ (HEB uses **จิตวิญญาณ + วิญญาณ**; 1Th uses **จิตใจ + วิญญาณ**). Recommendation: keep both as principled context-dependent exceptions, but document the divergence explicitly in the amended doc.

---

## Item E — HEB 12:14 ἁγιασμός render-or-amend — the unresolved sanctification-cluster question

**The 1 Thessalonians audit (§2) recommended a future corpus doc** `hagiasmos_hagiosune_2026-04.md` to lock:
- **ἁγιασμός (process)** → **การชำระให้บริสุทธิ์**
- **ἁγιωσύνη (state)** → **ความบริสุทธิ์**

The Greek aspectual-distinction (process-of-being-sanctified vs state-of-holiness) is theologically meaningful in Reformed sanctification-theology.

**HEB 12:14 ἁγιασμόν is rendered ความบริสุทธิ์ — NOT compliant with the proposed lock:**

- HEB 12:14 GK: `Εἰρήνην διώκετε μετὰ πάντων, καὶ τὸν **ἁγιασμόν**, οὗ χωρὶς οὐδεὶς ὄψεται τὸν κύριον`
- TH: `จงแสวงหาสันติสุขกับทุกคน และ**ความบริสุทธิ์** ซึ่งหากไม่มีสิ่งนี้ ไม่มีผู้ใดจะได้เห็นองค์พระผู้เป็นเจ้า`

The 12:14 KD does not explain the choice:
> ἁγιασμός → ความบริสุทธิ์ (cognate ἁγιάζω; here noun-form for sanctification-as-state).

The same chapter (12:10) renders ἁγιότης ("holiness"-state-noun, distinct from ἁγιασμός) as **ความบริสุทธิ์** — collapsing the two state/process distinctions.

**Two questions:**
1. Is the Greek aspectual-distinction (process ἁγιασμός vs state ἁγιωσύνη / ἁγιότης) preservable in Thai? The 1Th-recommended **การชำระให้บริสุทธิ์** ("the cleansing-to-being-pure," gerund) would be the process-rendering; the current **ความบริสุทธิ์** ("the state-of-purity," noun) is the state-rendering. The Greek is real — Paul uses both terms in adjacent contexts (1 Thess 4:3-7 vs 4:7) for principled aspectual reasons. But Thai readers might not perceive the distinction; the rendering may be over-engineered.
2. Should HEB 12:14 ἁγιασμόν be revised to **การชำระให้บริสุทธิ์** for corpus consistency with the (proposed) 1Th-anchored hagiasmos doc? OR should the proposed doc be revised to allow both **ความบริสุทธิ์** and **การชำระให้บริสุทธิ์** as context-dependent renderings? Recommendation: confirm the latter — Thai has no clean process-vs-state lexical-distinction in the bริสุทธิ์-family, and forcing one creates artificiality. The doc should document both renderings as acceptable with verse-level rationale.

---

## Item F — Forward Romans 3:25 ἱλαστήριον — the dual-sense of ἱλαστήριον HEB 9:5 (mercy-seat) ↔ Rom 3:25 (propitiation/expiation)

**HEB 9:5** (the only NT verse where ἱλαστήριον unambiguously refers to the OT mercy-seat / ark-cover):
- GK: `ὑπεράνω δὲ αὐτῆς Χερουβὶν δόξης κατασκιάζοντα τὸ **ἱλαστήριον**`
- TH: `และเหนือหีบนั้นมีเครูบแห่งพระสิริ ที่ปกคลุม**พระที่นั่งกรุณา**ด้วยปีก`

**ROM 3:25** (the cultic-instrumental sense — Christ presented as ἱλαστήριον through faith in his blood):
- GK: `ὃν προέθετο ὁ θεὸς **ἱλαστήριον** διὰ πίστεως ἐν τῷ αὐτοῦ αἵματι`

The forward Romans 3:25 ἱλαστήριον has three well-attested interpretive options:
- (a) **Mercy-seat archetype** (Calvin; T.W. Manson; Stuhlmacher) — Christ as the heavenly-mercy-seat; preserves lexical-link with HEB 9:5
- (b) **Propitiating-sacrifice** (Morris; mainstream evangelical-Reformed) — Christ as the propitiating-sacrifice that turns away divine wrath
- (c) **Expiation** (Dodd; RSV) — Christ as the means of erasing/expiating sin (not propitiating wrath)

**THSV1971 + NTV + ERV-Thai all use Option (b) เครื่องบูชาไถ่บาป** ("propitiating-sacrifice") at Rom 3:25. The HEB 9:5 KD explicitly notes the distinction:
> ἱλαστήριον in tabernacle-physical-context = the gold cover of the ark (mercy seat) → พระที่นั่งกรุณา (Thai biblical standard for the cover of the ark; distinct from ROM 3:25 propitiation-sense which uses 'เครื่องบูชาไถ่บาป').

**Question:** Confirm the corpus default for ROM 3:25 (forthcoming Romans) — Option A **พระที่นั่งกรุณา** (preserves lexical-link with HEB 9:5; Calvin/Stuhlmacher-aligned), Option B **เครื่องบูชาไถ่บาป** (matches THSV1971; mainstream evangelical Thai-reader expectation), or Option C **เครื่องลบล้างบาป** (Dodd/expiation reading)? RULES §0 evangelical-Protestant alignment + Thai-reader-expectation suggests Option B. The HEB end-of-book audit recommendation: confirm Option B explicitly so the forthcoming Romans-shipping doesn't drift on this question. The lexical-link with HEB 9:5 is intentionally lost; the Pauline cultic-instrumental sense is genuinely different from the OT-furniture sense.

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
