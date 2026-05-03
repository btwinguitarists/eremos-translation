# 2 John — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-03**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **2 John** (1 chapters, 13 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged. 2 John 1/1 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

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
## Item A — ἐρχόμενον ἐν σαρκί vs ἐληλυθότα: present-participle anti-Docetic confession at 2 JN 1:7

**The pattern.** 2 John 1:7 contains a present-participle anti-Docetic Christological confession that is DISTINCT from the parallel 1 John 4:2 perfect-participle confession.

| Verse | Greek | Aspect | Thai (current) |
|---|---|---|---|
| 1 JN 4:2 | ὁμολογεῖ Ἰησοῦν Χριστὸν ἐν σαρκὶ **ἐληλυθότα** | perfect (completed-incarnation, ongoing-state) | **ที่สารภาพรับว่าพระเยซูคริสต์ได้เสด็จมาในเนื้อหนัง** |
| 2 JN 1:7 | ὁμολογοῦντες Ἰησοῦν Χριστὸν **ἐρχόμενον** ἐν σαρκί | present (ongoing OR future-coming) | **สารภาพรับว่าพระเยซูคริสต์เสด็จมาในเนื้อหนัง** |

The 1 JN rendering uses the perfective marker **ได้** ("have-already-come"); the 2 JN rendering DROPS the marker, leaving **เสด็จมา** in the bare aspectually-neutral form. The intent is to preserve Greek present-participle ambiguity (ongoing-incarnated-state vs future-coming-in-flesh) without forcing a Thai-aspect commitment.

**Three scholarly readings of the present-participle:**
1. **Ongoing-incarnated-state** (majority view): "the one who comes-and-remains-in-flesh" — anti-Docetic confession of the still-incarnated Christ; treats the aspect-shift from 1 JN 4:2 as stylistic Johannine variation.
2. **Future-coming** (minority view): present-participle as future-marking ("the one who will-come in flesh") — anti-Docetic about the *returning* Christ also-coming-in-flesh.
3. **Iterative/timeless confession**: present-participle as the ongoing-act-of-confessing-an-ongoing-Christological-reality.

The current Thai surface is compatible with all three readings (Thai has no morphological future-marking either) — but a typical Thai reader's *default* will be reading 1 (past-completed event still-relevant). Reading 2 is essentially invisible without a thai_summary or footer note.

**The verse-level KD:**

> 'Ἰησοῦν Χριστὸν ἐρχόμενον ἐν σαρκί' — present-participle (NOT perfect — distinct from 1 JN 4:2 ἐληλυθότα). Per scholarly debate: the present-participle may emphasize the ongoing-incarnated-state, OR the future-coming. Render preserves the simple 'เสด็จมาในเนื้อหนัง' (came-in-flesh, royal-prefix) — same anti-Docetic content as 1 JN 4:2.

**Two questions:**
1. Is the **ได้-dropped aspectually-neutral** Thai surface (เสด็จมาในเนื้อหนัง) the right call for the present-participle ἐρχόμενον, or should it use a future-leaning Thai construction (เช่น **กำลังเสด็จมา / จะเสด็จมา**) to preserve the future-coming reading visibly?
2. Should v.7 receive a **thai_summary** explicitly noting the aspectual difference from 1 JN 4:2 + flagging the future-coming interpretive minority view, or is this scholarly nuance better left to the verse-level note (invisible to typical readers)?

---

## Item B — ἐκλεκτῇ κυρίᾳ + ἀδελφῆς ἐκλεκτῆς: chosen-lady interpretive commitment

**The pattern.** 2 JN 1:1 + 1:13 use feminine-personification language whose interpretation is well-known: (a) literal individual-woman + her literal-children + her literal-elect-sister; (b) personified-local-church + her members + a personified-sister-church.

| Verse | Greek | Thai (current) |
|---|---|---|
| 1:1 | Ὁ πρεσβύτερος ἐκλεκτῇ κυρίᾳ καὶ τοῖς τέκνοις αὐτῆς | **ข้าพเจ้าผู้ปกครองคริสตจักร ถึงสตรีที่ทรงเลือกสรรและบุตรของนาง** |
| 1:13 | Ἀσπάζεταί σε τὰ τέκνα τῆς ἀδελφῆς σου τῆς ἐκλεκτῆς | **บุตรของน้องสาวของท่านที่ทรงเลือกสรรฝากความระลึกถึงท่าน** |

**The current surfacing strategy:** the MAIN `thai` field at both v.1 and v.13 reads **literally** (as an actual woman + actual children + actual sister); only the v.1 thai_summary surfaces the personified-church interpretation. This is the "main-field-neutral, summary-surfaces-interpretation" hybrid strategy.

**The v.1 thai_summary:**
> 'สตรีที่ทรงเลือกสรร' (ἐκλεκτῇ κυρίᾳ) มีการตีความ 2 แบบ — (1) หมายถึงสตรีจริง ๆ ที่มีศรัทธา และเด็กของนาง (2) หมายถึงคริสตจักรท้องถิ่นและสมาชิก ... นักวิชาการสมัยใหม่ส่วนใหญ่เลือกการตีความที่ 2 เนื่องจาก — (ก) ข้อ 13 'บุตรของน้องสาวของท่านที่ทรงเลือกสรร' น่าจะหมายถึงคริสตจักรอีกแห่ง (ข) ในข้อ 8 และ 10 สรรพนามเปลี่ยนเป็นรูปพหูพจน์ 'พวกท่าน' ซึ่งบ่งชี้ว่าผู้รับเป็นกลุ่มมากกว่าบุคคลเดียว

**The v.13 KD goes one step further than v.1:**

> 'ἀδελφῆς σου τῆς ἐκλεκτῆς' → น้องสาวของท่านที่ทรงเลือกสรร — confirms the v.1 personification-reading (sister-church-sending-greetings), per the scholarly consensus.

**The internal tension:** the v.1 thai_summary treats interpretation 2 as one-of-two-options ("most modern scholars choose"); the v.13 KD treats it as the project's *committed* position ("confirms the personification-reading"). The v.13 currently lacks a thai_summary — so the typical Thai reader sees only the literal-sister surface at v.13.

**The corpus precedent (`petrine_eschatological_disambiguation_2026-05.md`):** Eremos's ambiguity-preservation principle (extended in 1 JN audit to soteriology + Christology) would suggest keeping both readings on the table at v.13 — not "confirming" interpretation 2.

**Three options:**
- **Option 1 (current):** Hybrid — main-field literal, v.1 thai_summary mentions both readings, v.13 KD says "confirms" but no v.13 thai_summary. Internal tension between v.1 and v.13 framings.
- **Option 2 (commit explicitly):** Edit the main `thai` field at v.1 to read **คริสตจักรท้องถิ่นและสมาชิก** (or similar) rather than สตรีและบุตร — committing to interpretation 2. Match the v.13 surface.
- **Option 3 (preserve ambiguity uniformly):** Keep current main-field literal-surface; mirror the v.1 thai_summary at v.13; re-word the v.13 KD to drop "confirms," replace with "consistent with."

**Two questions:**
1. Is the current hybrid (Option 1) defensible, or does the internal v.1/v.13 framing tension warrant moving to Option 2 (explicit commitment) or Option 3 (uniform ambiguity-preservation)?
2. If Option 2 or 3, which is more consistent with the project's `petrine_eschatological_disambiguation_2026-05.md` ambiguity-preservation principle?

---

## Item C — προάγω → ก้าวล้ำเกินเลย at 2 JN 1:9: going-beyond-bounds metaphor

**The pattern.** 2 JN 1:9 contains the rare προάγω-as-doctrinal-progressivism warning:

> πᾶς ὁ **προάγων** καὶ μὴ μένων ἐν τῇ διδαχῇ τοῦ Χριστοῦ θεὸν οὐκ ἔχει
> ทุกคนที่**ก้าวล้ำเกินเลย**และไม่คงอยู่ในคำสอนของพระคริสต์ก็ไม่มีพระเจ้า

**The verse-level KD:**

> Per uW figs-metaphor: προάγω 'run-ahead' — preserves the ironic-progress sense (the deceivers' 'innovation' is actually 'leaving-the-faith'). Render ก้าวล้ำเกินเลย — preserves the going-beyond-bounds sense.

**The lexical question.** προάγω elsewhere in the NT (Mark 6:45; Matt 14:22; Mark 10:32; Mark 11:9; Luke 18:39; Acts 12:6; etc.) means simply "lead/go-before" without the doctrinal-progressivism overtone. 2 JN 9 is the ONLY NT case where προάγω carries the false-progressive theological warning. Modern English translations vary widely:
- ESV: "Everyone who goes on ahead and does not abide..."
- NIV: "Anyone who runs ahead and does not continue..."
- NLT: "Anyone who wanders away from this teaching..."
- NRSV: "Everyone who does not abide in the teaching of Christ, but goes beyond it..."
- CSB: "Anyone who does not remain in the teaching of Christ but goes beyond it..."

Modern Thai versions also vary: THSV "ก้าวล่วง" ("go-cross-past, transgress"); THKJV "นำหน้า" ("go in front, lead"); a Thai New Living Translation uses "ทิ้ง" ("abandon").

**The current rendering: ก้าวล้ำเกินเลย** ("step-cross-over-past") — a strong, principled rendering that captures the IRONIC-PROGRESS sense (the deceiver thinks they're advancing; in fact they're trespassing-past-the-boundary). It is a Thai-corpus-hapax: the phrase does NOT recur elsewhere in the Eremos translation.

**Alternative Thai constructions Ben asked about:**
- **ก้าวเลยขอบเขต** ("step-past-the-boundary") — more idiomatic for "transgress"; loses the IRONIC-PROGRESS sense
- **เกินไป** ("go-too-far") — common idiom; loses the directional metaphor of "running-ahead"
- **นอกแนวคำสอน** ("outside-the-line-of-teaching") — emphasizes doctrinal-departure; loses the progress-irony entirely

**Two questions:**
1. Is **ก้าวล้ำเกินเลย** the right rendering? It captures the ironic-progress (going-beyond-bounds-while-imagining-yourself-advancing) better than alternatives, but at the cost of being a Thai-corpus-hapax that may sound stilted to a typical Thai reader.
2. Should the rendering match THSV's **ก้าวล่วง** (the standard Thai-evangelical rendering for transgressive-passage) for cross-Bible Thai-readability — or is breaking with THSV's milder rendering principled here, given that 2 JN 9's προάγω is uniquely doctrinal-progressivism?

---

## Item D — μὴ λαμβάνετε αὐτὸν εἰς οἰκίαν at 2 JN 1:10: house-church platform vs private-home hospitality

**The textual question.** 2 JN 1:10 issues a strong disciplinary instruction whose interpretation is critical for modern Thai-cultural application:

> εἴ τις ἔρχεται πρὸς ὑμᾶς καὶ ταύτην τὴν διδαχὴν οὐ φέρει, **μὴ λαμβάνετε αὐτὸν εἰς οἰκίαν** καὶ χαίρειν αὐτῷ μὴ λέγετε
> ถ้าผู้ใดมาหาท่าน แต่ไม่ได้นำคำสอนนี้มา **อย่าต้อนรับเขาเข้ามาในบ้าน** และอย่าทักทายเขา

**The verse-level KD:**

> Per uW figs-explicit: 'house' here = (a) literal-private-home (refusing-hospitality) OR (b) house-church (refusing-platform). Most-commentators read (b) — the 'house' of-the-house-church should not platform false-teachers. λαμβάνω → ต้อนรับ (with-hospitality sense).

**The verse `notes` field (NOT visible to typical readers):**

> Strong-disciplinary-action against false-teachers. Per scholarly-consensus: this addresses the church-hospitality of itinerant-teachers, NOT a prohibition on all-greetings to non-Christians (which would contradict the love-of-enemies command).

**The cultural-application question.** The Thai **บ้าน** is lexically neutral — it can mean a private-home OR a meeting-place. But the *default reading* of a Thai believer encountering **อย่าต้อนรับเขาเข้ามาในบ้าน** ("don't welcome him into your house") will be the literal-private-home reading. This will potentially clash with:
- the love-of-enemies teaching (Matt 5:44; Luke 6:35) which the same Thai reader has internalized as "be hospitable to all";
- modern-Thai cultural expectation of **น้ำใจ** (warm-hearted welcome) toward visitors.

**The historical context** (which a typical Thai reader does NOT see in the bare imperative): itinerant-teacher networks where house-hospitality functioned as *doctrinal-endorsement* of the visiting teacher (the host's house was the teaching-platform — the church met there, and welcoming a teacher into the house meant providing him a pulpit). Modern Thai Christianity does not generally have this house-as-platform structure, so a literal application would over-translate the verse into a contemporary anti-hospitality teaching.

**Two surfacing options:**

**Option A (current).** Bare imperative `อย่าต้อนรับเขาเข้ามาในบ้าน`; `notes` field carries the historical-context disclaimer; no `thai_summary` flag for the typical reader.

**Option B (proposed).** Add a `thai_summary` at v.10 explaining the itinerant-teacher house-church context — something like:
> ในบริบทคริสตจักรยุคแรก ผู้สอนเร่ร่อนใช้ 'บ้าน' (คือบ้านที่คริสตจักรพบกัน) เป็นสถานที่สอน การต้อนรับครูผู้สอนเท่ากับการรับรองคำสอนของเขา คำสั่งนี้จึงห้ามการรับครูสอนเทียมเท็จเข้ามาสอนในคริสตจักร ไม่ใช่ห้ามการมีน้ำใจต่อคนทั่วไป (เปรียบเทียบ มัทธิว 5:44 — 'จงรักศัตรู').

(English gloss: "In the early-church context, itinerant-teachers used the 'house' [meaning the house-church] as the teaching place. Welcoming a teacher = endorsing his teaching. This command therefore prohibits receiving false-teachers to teach in the church, NOT prohibiting kindness to people in general — cf. Matt 5:44 'love your enemies'.")

**Three questions:**
1. Stay with Option A (current — historical-context only in `notes`, invisible to the typical reader) or move to Option B (add a v.10 thai_summary surfacing the itinerant-teacher context + explicit cross-reference to love-of-enemies)?
2. Is the practical risk of Option A — Thai believers reading this as a blanket anti-hospitality teaching that contradicts love-of-enemies — significant enough to warrant the surfacing-cost of Option B?
3. If Option B, should similar interpretive thai_summary additions cascade to other passages where modern-application risks misreading the historical-cultural context (e.g., 1 Cor 14:34-35 women-in-the-assembly; 1 Tim 2:11-12 women-not-teaching; etc.)?

---

## Item E — χαίρειν αὐτῷ μὴ λέγετε at 2 JN 1:10-11: refusing-greeting strong-disciplinary-action

**The textual question.** 2 JN 1:10-11 closes the false-teacher prohibition with the Hellenistic-greeting-formula refusal:

> καὶ **χαίρειν αὐτῷ μὴ λέγετε**· ὁ λέγων γὰρ αὐτῷ χαίρειν κοινωνεῖ τοῖς ἔργοις αὐτοῦ τοῖς πονηροῖς
> และ**อย่าทักทายเขา** เพราะผู้ที่ทักทายเขาก็ร่วมในการกระทำที่ชั่วร้ายของเขา

**The verse-level KD:**
> 'χαίρειν λέγειν' → ทักทาย (the standard-Hellenistic-greeting formula). Refusing-greeting was a strong-Jewish-cultural disassociation-from-falsehood marker.

**The verse `notes` field:**
> Hospitality-as-endorsement principle: greeting-the-deceiver participates-in his-evil-works. The cultural-context: itinerant-teacher network where hospitality = doctrinal-endorsement.

**The cultural-application question (parallel to Item D).** The bare imperative **อย่าทักทายเขา** ("don't greet him") will read to a typical Thai reader as a personal-greeting prohibition — colliding with:
- Thai cultural expectations of greeting (**สวัสดี** is mandatory courtesy);
- love-of-enemies elsewhere in the NT (Matt 5:44; Luke 6:28).

The historical-cultural specificity (refusing the formal-greeting-of-doctrinal-endorsement, a Hellenistic-Jewish marker) is INVISIBLE in the bare Thai surface. The `notes` field carries the disclaimer, but `notes` is invisible to typical readers.

**Two surfacing options (same as Item D):**

**Option A (current).** Bare imperative; `notes` carries the cultural-context disclaimer.

**Option B (proposed).** Add a `thai_summary` at v.10 OR v.11 noting that:
1. The "greeting" here is the formal-greeting-of-doctrinal-endorsement (a Hellenistic-Jewish-cultural marker), not the everyday `สวัสดี`-equivalent.
2. Refusing this greeting = refusing public-affirmation of the false-teacher's mission, NOT refusing personal-courtesy to the person.
3. This is consistent with — not a contradiction of — Matt 5:44's love-of-enemies.

**Two questions:**
1. Should Items D + E move together as a unit — both v.10 (house) and v.10-11 (greeting) get a thai_summary, OR neither?
2. If both get a thai_summary, should it be a SINGLE shared summary at v.10 covering both imperatives, or TWO separate summaries (v.10 for house, v.11 for greeting)?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
