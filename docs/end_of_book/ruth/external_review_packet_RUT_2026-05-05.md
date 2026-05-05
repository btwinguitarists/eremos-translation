# Ruth — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-05**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Ruth** (4 chapters, 85 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged; Revelation complete (not yet tagged). Ruth 4/4 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
- Tetragrammaton יהוה → องค์พระผู้เป็นเจ้า (NT-aligned per divine_names_table_2026-05.md); אֱלֹהִים → พระเจ้า; שַׁדַּי → ผู้ทรงมหิทธิฤทธิ์
- First-occurrence-per-chapter Tetragrammaton convention footer note in output/textual_variants/<book>_<chapter>.json (Layer 2)
- OT register: ราชาศัพท์ ทรง- on verbs whose subject is the divine person; plain verb when subject is a divine body part (e.g., יַד יהוה)
- Pagan deities (foreign אֱלֹהִים, plural-of-Moabite-gods, Baal/Asherah/etc.) → พระทั้งหลาย / เทพ — NEVER พระเจ้า (reserved for YHWH/true God)
- חֶסֶด (covenant loyal-love, Ruth 1:8 lock) → ความรักมั่นคง
- גֹּאֵל (kinsman-redeemer) → ญาติผู้ไถ่; גָּאַל / גְּאֻלָּה family verbs → ไถ่ / สิทธิ์ในการไถ่
- Hebrew oath formulas: כֹּה יַעֲשֶׂה יהוה ... וְכֹה יֹסִיף → ขอองค์พระผู้เป็นเจ้าทรงลงโทษ ... และให้หนักยิ่งกว่านั้นอีก; חַי־יהוה → ตราบใดที่องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่
- Hebrew anthropomorphism for YHWH's body parts: royal-Thai พระหัตถ์ / พระเนตร / พระโอษฐ์ / พระบาท (matches Rachasap when divine possessor)
- אֵשֶׁת חַיִל / אִישׁ גִּבּוֹר חַיִל (Ruth 2:1 + 3:11 mirrored pair) → ชายผู้มีฐานะมั่งคั่งและทรงเกียรติ / หญิงผู้ทรงคุณธรรมและทรงเกียรติ
- Hebrew jussive prayer-blessings (יְבָרֶכְךָ יהוה, יִתֵּן יהוה, etc.) → Thai ขอ-...ทรง- + verb (royal-honorific for divine subject)
- Hebrew narrative-opening וַיְהִי → idiomatic Thai (drop or use temporal-marker like 'วันหนึ่ง'); waw-consecutive chains do not require mechanical และ rendering

### What we want from you

The internal end-of-book review surfaced the items below. For each, tell us either (a) "fine as-is, here's why" or (b) "here's a real concern, here's the action." Where you disagree, give specific verse-level reasoning grounded in the Hebrew + Thai shown.

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
## Item A — RUT 1:13 יַד־יְהוָה anthropomorphism — ทรง- prefix-on-body-part rule

**The pattern (and the first-OT-book policy decision):** Ruth 1:13 has Naomi's lament `יָצְאָה בִי יַד־יְהוָה` ("the hand of YHWH has gone out against me"). The Thai renders the body-part with royal-Thai prefix (พระหัตถ์, not plain มือ) but **the verb itself is plain** — no ทรง- prefix — because the grammatical subject of the verb is `พระหัตถ์` (the hand), not YHWH directly.

- RUT 1:13 GK: `יָצְאָה בִי יַד־יְהוָה` → TH: `**พระหัตถ์**ขององค์พระผู้เป็นเจ้า**ได้ยื่นออกมาต่อสู้**กับฉัน` (royal-Thai noun + plain verb — no ทรง-)

**Compare the YHWH-as-direct-subject pattern (full ทรง- + verb):**

- RUT 1:6 GK: `פָקַד יְהוָה אֶת־עַמּוֹ` → TH: `องค์พระผู้เป็นเจ้า**ทรงเยี่ยมเยียน**ประชากรของพระองค์` (verb takes ทรง-, divine subject)
- RUT 4:13 GK: `וַיִּתֵּן יְהוָה לָהּ הֵרָיוֹן` → TH: `องค์พระผู้เป็นเจ้า**ทรงประทาน**ให้นางตั้งครรภ์` (verb takes ทรง-)

**The 1:13 KD makes the rule explicit (per ChatGPT review 2026-05-05):**
> "**Grammatical fix:** dropped ทรง- royal-verb prefix because the grammatical subject of the action is `พระหัตถ์` (the hand), not YHWH directly — ทรง- attaches to verbs whose subject is the divine person, not to verbs whose subject is a body-part of the divine person."

**Why this matters forward:** OT-Hebrew has ~30+ "hand of YHWH" references (mighty-act and hostile-touch), ~50+ "mouth of YHWH" (the prophetic mouth-of-the-LORD-spoke formula), ~140+ "face of YHWH" (the seek-the-face-of-YHWH idiom in Psalms), 20+ "eyes of YHWH" (providence). The same ทรง-or-not question recurs constantly. The Ruth 1:13 lock is implicit at the verse level only — no corpus doc yet declares the rule.

**Question:** Is the principle correct as Thai grammar — that ทรง- attaches to verbs whose subject is the divine person, but NOT to verbs whose subject is a divine body-part (where the body-part already carries royal-Thai marking via the พระ- noun-prefix)? And: should this be lifted from a verse-level KD to a corpus doc (`docs/translator_decisions/divine_anthropomorphism_thai_grammar_2026-05.md`) before Exod 7 + Deut 9 + Pss 33:18 / 34:15 / Isa 40:5 — where the construction multiplies?

---

## Item B — RUT 3:9 כָּנָף wordplay flatness — wing/cloak verbal-echo across 2:12 → 3:9

**The chapter 2-3 verbal echo (which Hebrew preserves with ONE noun and Thai cannot match without strain):**

- RUT 2:12 (Boaz prays for Ruth) GK: `אֲשֶׁר־בָּאת לַחֲסוֹת תַּחַת־**כְּנָפָיו**` ("under whose **wings** [of YHWH] you have come to take refuge") → TH: `เจ้ามาลี้ภัยอยู่ใต้**ปีก**ของพระองค์`
- RUT 3:9 (Ruth proposes to Boaz) GK: `וּפָרַשְׂתָּ **כְנָפֶךָ** עַל־אֲמָתְךָ` ("spread your **wing/corner-of-cloak** over your handmaid") → TH: `ขอท่านโปรดกาง**ชายผ้าคลุม**ของท่านมาคลุมสาวรับใช้ของท่านด้วยเถิด`

**The literary-theological pivot:** Hebrew uses the same noun כָּנָף at both points. Boaz prays Ruth will take refuge under **YHWH's wings** (2:12) — Ruth then asks Boaz to spread **his wing** (= corner of cloak) over her (3:9). The verbal echo says: Boaz becomes the human instrument by which YHWH answers Boaz's own prayer.

The Thai loses the verbal echo because Thai lacks a single noun spanning both senses. ปีก = bird-wing only; ชายผ้าคลุม = corner-of-cloak only. The 3:9 thai_summary unpacks the wordplay:

> "การ ‘กางชายผ้าคลุม’ (וּפָרַשְׂתָּ כְנָפֶךָ עַל / pārastā kənāpekā ʿal) เป็นสำนวนทางวัฒนธรรมที่หมายถึง ‘โปรดสมรสกับฉัน’ — ถ้อยคำที่รูธใช้สะท้อนคำพูดของโบอาสในรูธ 2:12 ที่กล่าวว่ารูธ ‘เข้าลี้ภัยใต้ปีก’ ของพระเจ้า — รากศัพท์เดียวกัน כָּנָף (kānāp) แปลว่าทั้ง ‘ปีก’ และ ‘ชายผ้าหรือมุมของผ้าคลุม’ รูธกำลังขอให้โบอาสตอบคำอวยพรของเขาเอง"

**Three options for handling the echo:**

(a) **Surface preservation (current):** ปีก at 2:12, ชายผ้าคลุม at 3:9; verbal echo unpacked in 3:9 thai_summary only. Thai naturalness is preserved; the wordplay is scholarly footnote.

(b) **Force the echo at 3:9:** render 3:9 as `กาง**ปีกแห่งผ้าคลุม**ของท่าน` (lit. "spread the wing-of-your-cloak"). Preserves verbal echo; adds Thai awkwardness — ปีก does not naturally apply to a garment in modern Thai.

(c) **Force the echo at 2:12:** render 2:12 as `ใต้**ชายของปีก**ของพระองค์` (lit. "under the corner-of-the-wing of him") with footnote. Unusual Thai but makes 3:9 echo visible without stretching ปีก-as-cloak.

**Compounds forward:** Ps 17:8, Ps 36:7, Ps 57:1, Ps 91:4 ("under the shadow of YHWH's wings"), Mt 23:37 / Lk 13:34 (NT echo: Christ as hen-gathering-chicks πτέρυγας).

**Two questions:**
1. Is the Ruth 2:12-3:9 wordplay theologically load-bearing enough to warrant Thai naturalness compromise? (Hebrew Bible scholars consistently flag the כָּנָף-pivot as deliberate; but evangelical-Thai readers may not need the lemma-level echo if the thai_summary unpacking is sufficient.)
2. If preserving the echo is the priority, which of (b) / (c) is least-bad Thai? Or is there a fourth option (e.g., a Thai compound combining ปีก and ชายผ้า in a way that reads naturally)?

---

## Item C — RUT 4:19 רָם vs MAT 1:3-4 อารัม — cross-corpus name-form normalization

**The divergence:** The same OT figure (Hezron's son, Amminadab's father, in the Davidic line) appears in two corpus locations with two Thai forms:

- **RUT 4:19** (Hebrew רָם → THSV11 OT-baseline): **ราม**
- **MAT 1:3-4** (Greek Ἀράμ with prosthetic alpha → already-shipped NT): **อารัม**

The 4:19 KD documents the divergence and recommends "future polish-pass." The same person in the same Davidic genealogy is now spelled two ways in the corpus.

**Other Ruth-4 names verified as cross-corpus-locked-and-consistent** (per `proper_names_and_transliteration_2026-05.md` THSV11 baseline):
- פֶּרֶץ → เปเรศ (Ruth 4:18 + Mt 1:3) ✓
- חֶצְרוֹן → เฮศרอน / เฮสโรน (slight Thai-orthographic variance) — Ruth 4:18 + Mt 1:3
- עַמִּינָדָב → อัมมีนาดับ (Ruth 4:19 + Mt 1:4) ✓
- נַחְשׁוֹן → นาโชน (Ruth 4:20 + Mt 1:4) ✓
- שַׂלְמָה / שַׂלְמוֹן → สัลโมน / ซัลโมน (Hebrew form-variance harmonized; Mt 1:4 alignment)
- בֹּעַז → โบอาส (Mt 1:5) ✓
- עוֹבֵד → โอเบด (Mt 1:5) ✓
- יִשַׁי → เจสซี (Mt 1:5-6) ✓
- דָּוִד → ดาวิด ✓

**The Ram instance is the one drift** — and it's a generalizable issue. Hebrew→Greek transliteration sometimes adds prosthetic alpha or other small adjustments; cross-corpus consistency policy is undecided.

**Three resolution paths:**

(a) **OT Hebrew form wins corpus-wide** (ราม). Normalize Mt 1:3-4 in a future NT polish-pass. Argument: Hebrew-text fidelity; matches THSV11.

(b) **NT Greek form wins corpus-wide** (อารัม). Normalize Ruth 4:19 to อารัม. Argument: cross-corpus consistency; aligns with already-shipped NT; matches mainstream evangelical Thai (NTV/THSV-Plus/ESV-Thai all carry over the Greek prosthetic).

(c) **Tolerate the divergence with an explicit doc.** Both forms valid; readers see the same person in two transliterations.

**Compounds forward:** Many OT-Hebrew/NT-Greek transliteration pairs will recur in Phase 6D (Former Prophets — Joshua/Judges/Samuel/Kings) and the Pss superscriptions. Examples that the rule will govern: שְׁלֹמֹה / Σολομών (Solomon), אִיזֶבֶל / Ἰεζάβελ (Jezebel), אֵלִיָּהוּ / Ἠλίας (Elijah), נֹחַ / Νῶε (Noah), עָכָן / Ἀχάν (Achan), and many more.

**Question:** Which resolution (a/b/c) — and what's the deciding principle (Hebrew-source-fidelity vs already-shipped-NT-consistency vs reader-experience-of-recognizing-the-same-person)? The Ruth 4:19 / Mt 1:3-4 divergence is the first concrete trigger; the chosen rule will govern dozens of OT-Hebrew/NT-Greek shared-name normalization decisions in coming books.

---

## Item D — RUT 1:6 פָּקַד pastoral-care rendering vs other senses

**The rendering (per RUT 1:6 KD, 2026-05-05 ChatGPT-review):**

- RUT 1:6 GK: `כִּי־פָקַד יְהוָה אֶת־עַמּוֹ לָתֵת לָהֶם לָחֶם` → TH: `องค์พระผู้เป็นเจ้า**ทรงเยี่ยมเยียน**ประชากรของพระองค์ โดยประทานอาหารให้พวกเขา`

The 1:6 KD documents the open question:
> "Adopted 2026-05-05 per ChatGPT review feedback to soften from earlier 'เสด็จมาเยี่ยมเยียน' which read as overly heavy royal-physical-visit register. **Open question for the Thai-language reviewer: is ทรงเยี่ยมเยียน too plain, or is ทรงเหลียวแล (look upon with care) more natural for paqad in pastoral-care contexts?**"

**Why this is more than a Ruth-1:6 question:** The Hebrew lemma פָּקַד is one of the OT's most frequent + contextually-ranged divine-action verbs (~300× OT). Senses:

1. **Pastoral-care visit** — Gen 21:1, Ex 4:31, 1 Sam 2:21, Ruth 1:6, Lk 1:68 NT-echo (ἐπεσκέψατο). Current Ruth lock: ทรงเยี่ยมเยียน.
2. **Numbering / mustering** — Num 1:3+19 (military census). Likely Thai: ทรงทำสำมะโน.
3. **Appointment / commission** — Num 27:16, Jer 1:10. Likely Thai: ทรงแต่งตั้ง.
4. **Judgment-visitation** — Ex 32:34, Hos 4:9, Amos 3:14, Jer 5:9. Likely Thai: ทรงลงโทษ.

The Ruth-1:6 single-verse lock alone is insufficient; one Thai verb cannot serve all four contexts.

**Two questions:**
1. For sense (1) pastoral-care — is **ทรงเยี่ยมเยียน** the right Thai, or is **ทรงเหลียวแล** (look upon with care) more idiomatic-natural?
2. Should the OT corpus get a four-sense paqad table (locked Thai per sense + representative OT loci) before 1 Samuel 2 ships? Forward-load: Sam-Kgs alone has ~40 occurrences across all four senses.

---

## Item E — RUT 1:9 מְנוּחָה vs RUT 3:1 מָנוֹחַ — gendered-form contextual rendering split

**The same root, two contextual senses, two Thai forms:**

- RUT 1:9 GK: `יִתֵּן יְהוָה לָכֶם וּמְצֶאןָ **מְנוּחָה** אִשָּׁה בֵּית אִישָׁהּ` ("may YHWH grant you that you find **rest**, each in the house of her husband") → TH: `ขอองค์พระผู้เป็นเจ้าทรงโปรดให้พวกเจ้าได้พบ**ความสงบมั่นคง**`
- RUT 3:1 GK: `הֲלֹא אֲבַקֶּשׁ־לָךְ **מָנוֹחַ** אֲשֶׁר יִיטַב־לָךְ` ("should I not seek **a resting place** for you that it may be well with you?") → TH: `ฉันควรจะหา**ที่พักพิง**ให้เจ้า`

**The KD-documented split principle:** the morphological feminine form **מְנוּחָה** carries the **abstract security/peace** sense (rendered ความสงบมั่นคง — settled-peace); the masculine **מָנוֹחַ** carries the **concrete future-home/place** sense per Naomi's 3:1 imagery (rendered ที่พักพิง — shelter/refuge-place).

The 1:9 KD documents the 2026-05-05 ChatGPT-review revision: from earlier `ที่พักพิง` (refuge/shelter — too physical-shelter-leaning) to `ความสงบมั่นคง` (settled-peace — better captures security-in-marriage nuance). Open for Thai-language reviewer validation.

**Why this matters forward:** the same root spans Pss 95:11 (מְנוּחָתִי "my rest") + Heb 4:1ff (the Hebrews' canonical rest theme citing LXX κατάπαυσις from this Hebrew root) — the rest-of-God theology is a major OT/NT thread. Locking the Ruth-1:9-vs-3:1 split principle now governs how Thai handles "rest-as-state-of-being" vs "rest-as-place" everywhere downstream.

**Two questions:**
1. Is the gendered-form principle (feminine מְנוּחָה → abstract; masculine מָנוֹחַ → concrete) a sound translator's rule, or is it an over-fit pattern that breaks down outside Ruth? (Some OT grammarians treat the two forms as essentially synonymous; the contextual reading is the actual disambiguator.)
2. For the Ruth-1:9 abstract-sense rendering specifically — is **ความสงบมั่นคง** (settled-peace) the right Thai for the marital-security context, or is something closer to **ที่พึ่งพาอาศัย** (place-of-reliance) or **ความปลอดภัยในชีวิต** (security in life) more natural? Confirming Thai-language-reviewer voice critical.

---

## Item F — RUT 1:19 הוּם → แตกตื่น vs ฮือฮา — Thai naturalness of the village-stir verb

**The translator's open question (RUT 1:19 KD):**

- RUT 1:19 GK: `וַתֵּהֹם כָּל־הָעִיר עֲלֵיהֶן וַתֹּאמַרְנָה הֲזֹאת נָעֳמִי` ("and the whole city was stirred / buzzing about them, and they said: 'Is this Naomi?'") → TH: `ทั้งเมืองก็**แตกตื่น**เพราะพวกนาง พวกผู้หญิงต่างพูดกันว่า "นี่นาโอมีหรือ?"`

The 1:19 KD documents:
> "הוּם 'be in commotion, be stirred, buzzing.' Per ChatGPT review 2026-05-05: revised from earlier 'เกิดการตื่นเต้น' (which leans toward happy-excitement) to 'แตกตื่น' (be-startled/stirred-up) — captures the disturbed-reaction sense (the women's amazement is at how Naomi has been transformed by tragedy, not delighted excitement). **Open question for the Thai-language reviewer: is แตกตื่น appropriate here, or would ฮือฮา (buzzing/talking-up) be more natural Thai for the collective-vocal-stir?**"

**Two Thai candidates with subtly different connotations:**
- **แตกตื่น** (current) — disturbed, agitated, alarmed; matches the negative-amazement tone (Naomi's tragedy-changed appearance)
- **ฮือฮา** — collective-buzzing, "everyone is talking about it," more colloquial/positive-or-neutral

The Hebrew הוּם itself can carry either valence — the verse's force is the women's collective vocalization that Naomi's transformed condition has occasioned, which then triggers Naomi's renaming-lament in vv.20-21. The choice between แตกตื่น and ฮือฮา shifts the village's-emotional-tone.

**Question:** Which Thai best captures the Hebrew הוּם in this context — the disturbed-amazement of **แตกตื่น** or the collective-buzzing of **ฮือฮา**? Or is there a third option (e.g., **ลือกัน** "they spread word among themselves" or **โกลาหล** "be in commotion") that captures both the verb's force and the village's tone better?

---

## Item G — RUT 4 levirate-redemption legal-vocabulary cluster — **first-OT-book corpus-doc readiness**

**The cluster:** Ruth chapter 4 establishes the OT corpus's first major encounter with kinsman-redeemer + levirate-marriage Mosaic-law vocabulary. All renderings uniform; no corpus doc yet.

| Hebrew | Thai | Sense |
|---|---|---|
| גֹּאֵל | ญาติผู้ไถ่ | The kinsman-redeemer (~9× chs.3-4) |
| גָּאַל (verb) | ไถ่ | To redeem (the act, ~5×) |
| גְּאֻלָּה (noun) | สิทธิ์ในการไถ่ | The redemption-right (4:6, 4:7) |
| לְהָקִים שֵׁם־הַמֵּת עַל־נַחֲלָתוֹ | สืบทอดชื่อของผู้ล่วงลับในมรดกของเขา | Levirate-purpose formula (4:5, 4:10) |
| נָעַל (sandal-removal) | ถอดรองเท้า | Legal-validation ceremony (4:7-8) |

**Sample verse (the chapter's legal pivot):**

- RUT 4:10 GK: `וְגַם אֶת־רוּת הַמֹּאֲבִיָּה אֵשֶׁת מַחְלוֹן קָנִיתִי לִי לְאִשָּׁה לְהָקִים שֵׁם־הַמֵּת עַל־נַחֲלָתוֹ` → TH: `ฉันได้รับ**รูธหญิงโมอับ ภริยาของมาห์โลน เป็นภริยาของฉัน เพื่อสืบทอดชื่อของผู้ล่วงลับ**ในมรดกของเขา`

**The unnamed closer-kinsman at 4:1** is addressed as `פְּלֹנִי אַלְמֹנִי` ("so-and-so") → `สหายเอ๋ย` ("o friend"), preserving the Hebrew deliberate-anonymity (the kinsman who refuses redemption is forgotten by name; Boaz who accepts is preserved in the closing genealogy).

**Forward-load:** Lev 25:25-28 + Deut 25:5-10 (Mosaic-law texts), Job 19:25 (`גֹּאֲלִי` "my Redeemer"), Isa 41:14 + 43:1 + 43:14 + 44:6+24 + 47:4 + 48:17 + 49:7+26 + 54:5+8 + 59:20 + 60:16 + 63:9 (YHWH-as-Redeemer concentration in Deutero-Isaiah), Pss 19:14 + 78:35, Prov 23:11. NT Christological cross-references: Tit 2:14, Heb 9:12 (αἰωνίαν λύτρωσιν), Eph 1:7 (ἀπολύτρωσις), 1 Pet 1:18.

**Two questions:**
1. Is the OT-Ruth legal-vocabulary set (ญาติผู้ไถ่ / ไถ่ / สิทธิ์ในการไถ่ / สืบทอดชื่อ-ในมรดก / ถอดรองเท้า) ready to be locked into a corpus doc (`docs/translator_decisions/goel_kinsman_redeemer_2026-05.md`) as the canonical OT-rendering set before Job 19 + Deutero-Isaiah?
2. Does the ญาติผู้ไถ่ Thai compound carry the right semantic load for the Christological-typological NT cross-references (Christ-as-redeemer in Heb 9, Eph 1:7 ἀπολύτρωσις, Rev 5:9 ἠγόρασας)? Or does it favor too narrowly the legal-kinship sense and lose the broader theological-redemption sense Christ enacts?

---

## Item H — RUT 1:6 + 4:13 divine-action attribution + Ruth 1cs pronoun escalation — register coherence

**Two related register questions at narrative-pivot moments.**

### H1. Divine-action verbs at 1:6 + 4:13

YHWH appears as direct narrative-subject only twice — at the famine-ends frame (1:6) and the conception frame (4:13):

- RUT 1:6 GK: `כִּי־פָקַד יְהוָה אֶת־עַמּוֹ לָתֵת לָהֶם לָחֶם` → TH: `องค์พระผู้เป็นเจ้า**ทรงเยี่ยมเยียน**ประชากรของพระองค์ โดย**ประทานอาหาร**ให้พวกเขา`
- RUT 4:13 GK: `וַיִּתֵּן יְהוָה לָהּ הֵרָיוֹן` → TH: `องค์พระผู้เป็นเจ้า**ทรงประทาน**ให้นางตั้งครรภ์`

Between 1:6 and 4:13, YHWH never appears as direct narrative-subject — providence works quietly through human actions (Ruth's "chance" arrival at Boaz's field 2:3; threshing-floor encounter; closer-kinsman's reversal). The Thai preserves this narrator-restraint pattern by varying the ทรง-prefixed verbs (ทรงเยี่ยมเยียน at 1:6; ทรงประทาน at 4:13).

### H2. Ruth's 1cs pronoun escalation: ดิฉัน vs ข้าพเจ้า

Ruth uses **ดิฉัน** (humble feminine 1sg) in ordinary dialogue with Naomi (2:2) + Boaz (2:10, 2:13, 3:9). She elevates to **ข้าพเจ้า** (formal 1sg) for the 1:16-17 covenant-oath only:

- RUT 1:16: `שׁוּב מֵאַחֲרָיִךְ ... עַמֵּךְ עַמִּי וֵאלֹהַיִךְ אֱלֹהָי` → TH: `**ข้าพเจ้า**จะไปที่นั่น ... พระเจ้าของท่านจะเป็นพระเจ้าของ**ข้าพเจ้า**`
- RUT 3:9 (still ดิฉัน): `אָנֹכִי רוּת אֲמָתֶךָ` → TH: `**ดิฉัน**คือรูธ สาวรับใช้ของท่าน`

The 1:16 KD anchors the policy: "Ruth elevates her pronoun register here for the covenant oath ... matching NT covenant-prayer register."

**Two questions:**
1. Is the divine-action ทรง-pattern at 1:6 + 4:13 (varying the verb across narrative pivots) the right Thai for capturing the narrator's structural-restraint, or is the variety diluting the narrator's deliberate-rare-divine-subject-marking?
2. Is Ruth's two-tier pronoun policy (ดิฉัน for ordinary dialogue / ข้าพเจ้า for the 1:16-17 covenant-oath only) the right register-pattern? Should the 3:9 marriage-proposal — which re-affirms the 1:16 covenant — also escalate to ข้าพเจ้า? Or is the humble-petitioner ดิฉัน at 3:9 the deliberately-submissive register that fits אֲמָה ("handmaid") self-positioning?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
