# Jeremiah — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-21**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Jeremiah** (52 chapters, 1,364 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah complete (not yet tagged). Jeremiah 52/52 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Jeremiah (JER) — end-of-book external-review items

_Auto-derived from the book's own `key_decisions`, textual-variant footnotes, and automated check reports (52 chapters, 1,364 verses). These are evidence-based sanity-check prompts, not hand-curated maintainer concerns — review them as a corpus-level second opinion and flag anything inconsistent, mistaken, or theologically off._

## Item A — Divine-name & honorific convention (verify consistency across the whole book)


The book applies the project's locked Tetragrammaton/honorific convention. Confirm it is applied **uniformly** and correctly across every chapter, and flag any verse where the divine name, an Adonai-YHWH compound, or royal honorifics (ราชาศัพท์) read inconsistently or wrongly.

> First-occurrence convention footnote (chapter 1 / first occurrence):
>
> **องค์พระผู้เป็นเจ้า** ในบทนี้ (ปรากฏครั้งแรกที่ข้อ 2) แปลจากภาษาฮีบรู יהוה (พระนามเฉพาะของพระเจ้า ออกเสียงโดยทั่วไปว่า ‘ยาห์เวห์’). ฉบับเอเรโมสใช้ **องค์พระผู้เป็นเจ้า** ตามแบบแผนของฉบับพันธสัญญาใหม่ที่แปล κύριος ซึ่งในต้นฉบับฮีบรูตรงกับ יהוה. รูปประสม אֲדֹנָי יְהוִה (ข้อ 6) ก็แปลว่า **องค์พระผู้เป็นเจ้า** เช่นกัน โดยที่นี่อยู่ในรูปคำอุทานวิงวอนขึ้นต้นประโยค จึงแปลว่า **ข้าแต่องค์พระผู้เป็นเจ้า**; และสำนวน נְאֻם־יְהוָה (ข้อ 8, 15, 19) แปลว่า **องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้**. ดูรายละเอียดเพิ่มเติมที่ docs/translator_decisions/divine_names_table_2026-05.md.


## Item B — Textual & versification divergences (verify handling)


Key-decisions in this book that flag a textual variant, LXX/MT difference, versification realignment, or cipher. Confirm each is handled correctly and consistently:

- **Jeremiah 1:1** — ถ้อยคำของเยเรมีย์
  - divrê = 'words/acts of' — superscription head governing the whole book. יִרְמְיָהוּ → เยเรมีย์ per proper_names_and_transliteration_2026-05.md (THSV11 baseline); the prophet is referenced with plain register (no ราชาศัพท์) per ot_register_policy §2.2 — prophets are servants of Go
- **Jeremiah 2:16** — โกนกลางกระหม่อมของเจ้า
  - qodqōd (crown of the head) → กลางกระหม่อม. The verb (MT יִרְעוּךְ) read as ‘graze/shave bare’ → โกน, the Egyptian marking of slaves. An alternate reading repoints to ‘crack/break your skull’; the slave-shaving sense is followed (BSB), with the variant noted.
- **Jeremiah 2:20** — เราได้หักแอกของเจ้า และปลดโซ่ตรวนของเจ้าออก
  - ʿōl (yoke) + môsērôt (bonds/chains) → แอก + โซ่ตรวน — the exodus liberation imagery (YHWH freed Israel from Egypt's slavery). MT reads 1cs ‘I broke/tore’ (YHWH the liberator); the freed people then refuse to serve.
- **Jeremiah 2:27** — พูดกับท่อนไม้ว่า ‘ท่านเป็นบิดาของข้า’ และพูดกับก้อนหินว่า ‘เจ้าให้กำเนิดข้า’
  - ‘Tree’ and ‘stone’ = wooden and stone idols → ท่อนไม้/ก้อนหิน. The gender-reversal in MT (calling the wooden image ‘father,’ the stone ‘you bore me’) mocks idolatry's absurdity: lifeless matter addressed as life-giving parents.
- **Jeremiah 2:30** — ดาบของพวกเจ้าเองได้กลืนกินบรรดาผู้เผยพระวจนะของพวกเจ้าดั่งสิงโตที่ทำลายล้าง
  - ‘Your own sword devoured your prophets’ → the people murdered the true prophets sent to them (cf. 26:20–23; Mt 23:37). ʾaryēh mašḥît (destroying lion) → สิงโตที่ทำลายล้าง — the people's own violence as a ravening beast.
- **Jeremiah 3:5** — เจ้าพูดเช่นนี้ แต่เจ้าก็ยังทำความชั่ว
  - The pivot back to direct accusation (2fs): ‘you have spoken [thus], yet you do the evils.’ MT has a glued דִבַּרְתְּ‖וַתַּעֲשִׂי which is de-glued in the source field. Word and deed contradict — the chapter's charge of insincere repentance (cf. v. 10).
- **Jeremiah 4:3** — จงไถพรวนดินที่ยังไม่ได้ไถของพวกเจ้า และอย่าหว่านพืชลงกลางหนาม
  - nîr ‘fallow/untilled ground’ + the cognate verb (break up fallow ground) → ไถพรวนดินที่ยังไม่ได้ไถ. The farming metaphor for radical heart-renewal (cf. Hos 10:12); ‘sowing among thorns’ = repentance not rooted out (echoed at Mt 13:7, 22).
- **Jeremiah 4:18** — ช่างขมขื่นเหลือเกิน เพราะมันเสียดแทงเข้าถึงใจของเจ้า
  - mar ‘bitter’ → ขมขื่น; nāgaʿ ʿad-lēv ‘reaches/strikes to the heart’ → เสียดแทงเข้าถึงใจ. The punishment's bitterness penetrates to the core. Verse ends with the ס (setumah) marker in MT (omitted from source field).
- **Jeremiah 4:21** — อีกนานเท่าใดที่ข้าพเจ้าต้องเห็นธงสัญญาณ และได้ยินเสียงแตรเขาสัตว์
  - ʿad-mātay ‘how long’ → อีกนานเท่าใด; nēs (war-standard) + šôpār (horn) → ธงสัญญาณ / แตรเขาสัตว์ (the war-signals of vv. 5–6, 19). The prophet's weary lament-question (cf. the Psalmic ‘how long’). Verse ends with ס (setumah) marker in MT (omitted from source).
- **Jeremiah 5:7** — เราจะอภัยให้เจ้าได้อย่างไร?
  - ‘How/for what could I forgive you?’ — the answer to v. 1's offer: pardon is impossible given the persistent sin. sālaḥ → อภัย; divine first-person (เรา). The MT had a glued אֶסְלַח־לָךְבָּנַיִךְ, de-glued in the source field (אֶסְלַח־לָךְ בָּנַיִךְ).
- **Jeremiah 5:15** — ชนชาติหนึ่งจากแดนไกล … เข้มแข็งมั่นคง … มีมาแต่โบราณกาล
  - Fourfold gôy (nation) anaphora: distant (mimerḥāq) + enduring/strong (ʾêtān) + ancient (mēʿôlām) + foreign-tongued → แดนไกล / เข้มแข็งมั่นคง / โบราณกาล. The unintelligible language (cf. Deut 28:49; Isa 33:19) marks the terrifying foreignness of Babylon. The MT glued גּוֹי׀אֵיתָן 
- **Jeremiah 5:29** — เราจะไม่ลงโทษพวกเขาเพราะสิ่งเหล่านี้หรือ
  - Verbatim refrain of v. 9: פָּקַד sense (4) judgment → ลงโทษ (paqad doc); נַפְשִׁי (my soul) → จิตใจของเรา. The repeated rhetorical question frames the whole indictment (vv. 7–28). Verse ends with ס marker (omitted from source).
- **Jeremiah 6:1** — ลูกหลานของเบนยามิน … เทโคอา … เบธฮักเคเรม
  - בִּנְיָמִן Benjamin → เบนยามิน; תְּקוֹעַ Tekoa → เทโคอา; בֵּית הַכֶּרֶם Beth-haccherem → เบธฮักเคเรม (THSV11-style transliterations). The MT had two glue artifacts (paseq after הָעִזוּ; בִניָמִן glued to מִקֶּרֶב), de-glued in the source field. (Ellipsis joins the place-names.)
- **Jeremiah 6:5** — ให้เราบุกโจมตีในเวลากลางคืน และทำลายป้อมปราการของนางเสีย
  - ‘let us go up by night and destroy her citadels (ʾarmənôt)’ → บุกโจมตีในเวลากลางคืน / ทำลายป้อมปราการ. The attackers, frustrated by daylight's end (v. 4), resolve on a night assault. Verse ends with the ס (setumah) marker in MT (omitted from the source field).
- **Jeremiah 6:11** — ข้าพเจ้าเต็มไปด้วยความพิโรธขององค์พระผู้เป็นเจ้า ข้าพเจ้าเหนื่อยที่จะระงับมันไว้
  - ḥămat YHWH ‘the wrath of YHWH’ → ความพิโรธขององค์พระผู้เป็นเจ้า (Layer 1). Jeremiah's first-person (ข้าพเจ้า): he is so filled with the divine wrath he announces that he is ‘weary of holding it in’ (nilʾêtî hākîl). The MT paseq-glue (יְהוָה׀מָלֵאתִי) de-glued in the source field.
- **Jeremiah 6:14** — ‘สงบสุขแล้ว สงบสุขแล้ว’ ทั้งที่ไม่มีความสงบสุขเลย
  - šālôm → สงบสุข/สันติสุข; the doubled ‘peace, peace’ then ‘but no peace’ — the iconic false-assurance line (repeated 8:11; cf. Ezek 13:10). The MT paseq-glue (שָׁלוֹם׀שָׁלוֹם) de-glued in the source field. Rendered to keep the haunting repetition + reversal.
- **Jeremiah 6:15** — ไม่อายเลย ทั้งไม่รู้จักการกระดากหน้า
  - ‘they are not ashamed (bôš), nor know how to blush (hiklîm)’ → ไม่อาย / ไม่รู้จักการกระดากหน้า. The hardened shamelessness (cf. 3:3) over their abomination (תּוֹעֵבָה → สิ่งน่าสะอิดสะเอียน). Verse ends with ס marker (omitted from source).
- **Jeremiah 6:16** — ไต่ถามถึงทางโบราณ … ทางดี
  - Messenger-formula כֹה אָמַר יְהוָה → องค์พระผู้เป็นเจ้าตรัสดังนี้ (§5.3); Layer 1: יהוה → องค์พระผู้เป็นเจ้า ตาม divine_names_table_2026-05.md. nətîvôt ʿôlām ‘ancient paths’ → ทางโบราณ; derek haṭṭôv ‘the good way’ → ทางดี. The summons to return to the tried covenant-path of the f
- **Jeremiah 7:2** — พระนิเวศขององค์พระผู้เป็นเจ้า … พระวจนะขององค์พระผู้เป็นเจ้า … นมัสการองค์พระผู้เป็นเจ้า
  - Layer 1: יהוה → องค์พระผู้เป็นเจ้า (three occurrences). bêt YHWH ‘house of YHWH’ → พระนิเวศขององค์พระผู้เป็นเจ้า (sanctuary register, ot_register §2.3); hištaḥăwâ toward YHWH = true worship → นมัสการ (the worship-of-true-God verb). Verse ends with ס marker (omitted from source). 
- **Jeremiah 7:9** — ลักทรัพย์ ฆ่าคน ล่วงประเวณี สาบานเท็จ
  - A rapid-fire list echoing the Decalogue: gānav (steal) + rāṣaḥ (murder) + nāʾap (commit adultery) + ‘swear falsely’ → ลักทรัพย์ / ฆ่าคน / ล่วงประเวณี / สาบานเท็จ (commandments 8, 6, 7, 9/3). The MT had glue artifacts (paseq after הֲגָנֹב; נָאֹף glued to וְהִשָּׁבֵעַ), de-glued in
- **Jeremiah 7:11** — ถ้ำของโจร
  - məʿārat pārîṣîm ‘den/cave of violent ones (robbers)’ → ถ้ำของโจร — rendered to match shipped Mark 11:17 (ถ้ำของโจร), since Jesus quotes this verse at the temple-cleansing (Mk 11:17; Mt 21:13; Lk 19:46). Cross-corpus recognizability per the OT-cited-in-NT alignment principle (prop
- **Jeremiah 7:14** — สิ่งที่เราได้ทำแก่ชิโลห์ เราจะทำแก่นิเวศ … (ที่) พวกเจ้าวางใจ
  - Divine first-person (เรา): ‘as I did to Shiloh, so to this house you trust in.’ The temple's coming destruction = Shiloh's fate. The MT paseq-glue (לַבַּיִת׀אֲשֶׁר) de-glued in the source field. (Ellipsis joins the Shiloh-parallel.)
- **Jeremiah 7:15** — เชื้อสายทั้งสิ้นของเอฟราอิม
  - Ephraim (אֶפְרָיִם → เอฟราอิม) = the Northern Kingdom, already exiled by Assyria (722 BC) — ‘your brothers’ cast out, the precedent for Judah's coming exile. Verse ends with ס marker (omitted from source).
- **Jeremiah 7:16** — อย่าอธิษฐานเผื่อชนชาตินี้
  - ‘do not pray (hitpallēl) on behalf of this people’ → อย่าอธิษฐานเผื่อ. Divine first-person command to Jeremiah; the prophet's intercessory role is suspended (repeated 11:14; 14:11) — the judgment is sealed. The MT paseq-glue (תִּתְפַּלֵּל׀בְּעַד) de-glued in the source field.
- **Jeremiah 7:19** — พวกเขายั่วยุเราอย่างนั้นหรือ … จนต้องอับอายขายหน้า
  - ‘Is it Me they provoke? … is it not themselves, to the shame of their faces (bōšet pənêhem)?’ → ยั่วยุเรา / อับอายขายหน้า. Divine first-person: their idolatry harms not God but themselves. Verse ends with ס marker (omitted from source). (Ellipsis joins the rhetorical questions.)


## Item C — Locked-term / convention applications (verify uniformity)


Renderings the translator marked as locked/by-convention. Confirm they match the project glossary and are used consistently here and against the rest of the corpus:

- **Jeremiah 1:8** — องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้
- **Jeremiah 2:2** — องค์พระผู้เป็นเจ้าตรัสดังนี้ว่า
- **Jeremiah 2:2** — ความรักมั่นคงของเจ้าเมื่อครั้งยังสาว
- **Jeremiah 2:18** — น้ำแห่งแม่น้ำยูเฟรติส
- **Jeremiah 4:3** — องค์พระผู้เป็นเจ้าตรัสดังนี้
- **Jeremiah 4:4** — มิฉะนั้นความพิโรธของเราจะพลุ่งออกมาดั่งไฟ
- **Jeremiah 4:23** — ข้าพเจ้ามองดูฟ้าสวรรค์ และที่นั่นก็ไม่มีแสงสว่าง
- **Jeremiah 6:10** — หูของพวกเขาตันเสียแล้ว พวกเขาจึงฟังไม่ได้
- **Jeremiah 6:12** — เราจะเหยียดมือของเราออกต่อสู้บรรดาผู้อาศัยในแผ่นดินนี้
- **Jeremiah 12:1** — ข้าแต่องค์พระผู้เป็นเจ้า พระองค์ทรงเป็นผู้ชอบธรรม
- **Jeremiah 13:11** — องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้ … เป็นประชากร … ชื่อเสียง คำสรรเสริญ และศักดิ์ศรี
- **Jeremiah 13:13** — องค์พระผู้เป็นเจ้าตรัสดังนี้ว่า ‘ดูเถิด เราจะให้ … เมามาย’
- **Jeremiah 13:14** — เราจะไม่สงสาร ไม่ปรานี และไม่เมตตา จนต้องทำลายพวกเขาเสีย
- **Jeremiah 13:25** — นี่คือส่วนของเจ้า เป็นส่วนแบ่งที่เรากำหนดให้แก่เจ้า องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้
- **Jeremiah 14:10** — องค์พระผู้เป็นเจ้าตรัสดังนี้ว่า … พวกเขารักที่จะระเหเร่ร่อนยิ่งนัก ไม่ได้ยับยั้งเท้าของตน
- **Jeremiah 14:15** — องค์พระผู้เป็นเจ้าตรัสดังนี้ว่า เกี่ยวกับบรรดาผู้เผยพระวจนะ … จะถึงจุดจบด้วยดาบและการกันดารอาหาร
- **Jeremiah 15:2** — องค์พระผู้เป็นเจ้าตรัสดังนี้ว่า ‘ผู้ที่ถูกกำหนดให้แก่ความตาย ก็ไปสู่ความตาย …’
- **Jeremiah 15:3** — เราจะกำหนดสี่อย่างให้จัดการพวกเขา
- **Jeremiah 15:6** — เจ้าได้ทอดทิ้งเราแล้ว … เราจึงเหยียดพระหัตถ์ออกต่อสู้เจ้า และทำลายเจ้า
- **Jeremiah 15:9** — ส่วนคนที่เหลือเราจะมอบให้แก่ดาบต่อหน้าศัตรูของพวกเขา องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้
- **Jeremiah 15:19** — ถ้าเจ้าหันกลับมา เราก็จะให้เจ้ากลับคืนมา เจ้าจะได้ยืนอยู่ต่อหน้าเรา
- **Jeremiah 15:20** — เพราะเราอยู่กับเจ้าเพื่อช่วยเจ้าให้รอดและช่วยกู้เจ้า องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้
- **Jeremiah 16:3** — เพราะองค์พระผู้เป็นเจ้าตรัสดังนี้ว่า … ที่เกิดในที่แห่งนี้
- **Jeremiah 16:5** — องค์พระผู้เป็นเจ้าตรัสดังนี้ว่า อย่าเข้าไปในบ้านที่มีงานศพ
- **Jeremiah 16:5** — เราได้เอาสันติสุขของเราไป … องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้ ทั้งความรักมั่นคงและความเมตตา


## Item D — Hardest interpretive cruxes (evaluate the calls)


The key-decisions with the most reasoning attached — i.e. the book's hardest judgment calls. Evaluate whether each rendering is defensible from the source text:

- **Jeremiah 4:10** — พระองค์ได้ทรงปล่อยให้ชนชาตินี้ … ถูกลวงอย่างยิ่ง … ‘พวกเจ้าจะมีสันติสุข’
  - nāšāʾ (deceive/beguile) in the infinitive-absolute intensive (haššēʾ hiššēʾtā ‘utterly deceived’) → ลวงอย่างยิ่ง/อย่างสิ้นเชิง. The 2ms verb is addressed to God; theology (God's permissive sovereignty over false-peace prophets, cf. 1 Kgs 22:20–23; Ezek 14:9) is unpacked in thai_summary. Main text uses ‘ทรงปล่อยให้...ถู
- **Jeremiah 32:17** — ข้าแต่องค์พระผู้เป็นเจ้า ดูเถิด พระองค์ได้ทรงสร้างฟ้าสวรรค์และแผ่นดินโลกด้วยฤทธานุภาพอันยิ่งใหญ่ และด้วยพระกรที่เหยียดออกของพระองค์ ไม่มีสิ่งใดยากเกินไปสำหรับพระองค์
  - Layer 1: יהוה → องค์พระผู้เป็นเจ้า. รูปประสม אֲדֹנָי יְהוִה ที่ขึ้นต้นด้วยคำอุทาน אֲהָהּ ‘อนิจจา/โอ’ (สูตรอุทานต้นประโยค) → ข้าแต่องค์พระผู้เป็นเจ้า (divine_names sub-rule 2026-05-23: รูปประสมอุทานต้นประโยค → ข้าแต่องค์พระผู้เป็นเจ้า). zᵉrōaʿ nᵉṭûyâ ‘outstretched arm’ (ของพระเจ้า, คำทูลบุรุษที่ 2 ต่อพระเจ้า) → พระกรที่
- **Jeremiah 8:23** — (MT-anchored numbering)
  - Eremos anchors on MT versification (verse_schema §2): this verse is MT Jeremiah 8:23, but English/BSB number it 9:1 (the chapter break falls one verse earlier in English). The bsb_english field carries the BSB 9:1 text for back-translation alignment. No `versification` sub-object is added (no entry in data/versificatio
- **Jeremiah 31:22** — เพราะองค์พระผู้เป็นเจ้าได้ทรงสร้างสิ่งใหม่ขึ้นในแผ่นดิน คือผู้หญิงจะโอบล้อมผู้ชาย
  - Layer 1: יהוה → องค์พระผู้เป็นเจ้า (bārāʾ ‘create’ → ทรงสร้าง royal). nᵉqēbâ tᵉsôbēb gāber ‘a woman shall surround/encompass a man’ → ผู้หญิงจะโอบล้อมผู้ชาย — เป็นวลีที่ตีความยากและถกเถียงกันมากที่สุดวลีหนึ่งในเยเรมีย์ (ความหมายไม่แน่ชัด: การกลับด้านบทบาท/อิสราเอลปกป้อง/การตีความเชิงเมสสิยาห์ในบางจารีต); แปลตามอักษรฮีบ
- **Jeremiah 20:7** — ข้าแต่องค์พระผู้เป็นเจ้า พระองค์ทรงโน้มน้าวข้าพระองค์ ข้าพระองค์ก็ถูกโน้มน้าว พระองค์ทรงเข้มแข็งกว่าข้าพระองค์และทรงชนะ
  - Layer 1: יהוה → องค์พระผู้เป็นเจ้า (รูปอุทานเรียกหา → ข้าแต่องค์พระผู้เป็นเจ้า). pātâ (Piel) มีพิสัยความหมาย ‘ล่อลวง/ชักจูง/โน้มน้าว’ (เทียบ อพย 22:15 การเกลี้ยกล่อมหญิงสาว); คู่กับ ḥāzaq + yākōl ‘เข้มแข็งกว่าและชนะ/เอาชนะ’ บ่งว่าเป็นการ ‘เอาชนะ/บีบบังคับ’ มากกว่าการโกหก — เยเรมีย์ครวญว่าทรงโน้มน้าว/เอาชนะเขาให้รับพันธ
- **Jeremiah 1:6** — ข้าแต่องค์พระผู้เป็นเจ้า
  - אֲהָהּ אֲדֹנָי יְהוִה — the Adonai-YHWH compound in a sentence-initial interjection of dismay (אֲהָהּ ‘Ah/Alas’). Per divine_names_table_2026-05.md §sub-rule 2026-05-23, sentence-initial interjection compounds render ‘ข้าแต่องค์พระผู้เป็นเจ้า’ (Jer 1:6 is the doc's named anchor). The compound collapses to the single Th
- **Jeremiah 22:24** — เรามีชีวิตอยู่แน่ฉันใด องค์พระผู้เป็นเจ้าตรัสไว้ดังนี้ว่า แม้โคนิยาห์บุตรของเยโฮยาคิม … จะเป็นแหวนตราที่มือขวาของเรา เราก็จะถอดเจ้าออกจากที่นั่น
  - สูตรคำสาบาน ḥay-ʾānî ‘as I live’ → เรามีชีวิตอยู่แน่ฉันใด (เทียบ อสย 49:18). Layer 1: יהוה → องค์พระผู้เป็นเจ้า (נְאֻם־יְהוָה LOCKED). Coniah כָּנְיָהוּ → โคนิยาห์ (= เยโฮยาคีน/เยโคนิยาห์, 2 พกษ 24:8–15). ḥôtām ʿal-yad yᵉmînî ‘signet on my right hand’ → แหวนตราที่มือขวาของเรา — คำพูดบุรุษที่ 1 ของพระเจ้าใช้คำส่วนร่างกา
- **Jeremiah 10:12** — องค์พระผู้เป็นเจ้าผู้ทรงสร้างแผ่นดินโลก … ผู้ทรงสถาปนาพิภพ … ผู้ทรงคลี่ฟ้าสวรรค์ออก
  - Participial Creator-hymn: ʿōśeh (maker) + mēkîn (establisher) + nāṭâ (stretcher) → rendered as agentive ผู้ทรง- titles (which honorifics-binding treats as divine titles, not bound verbs), keeping the doxological flow. The subject YHWH is supplied as องค์พระผู้เป็นเจ้า (so BSB; the Hebrew continues from v. 10), with no 


## Item E — Open corpus-level read


Beyond the items above: read for naturalness in modern Thai, theological accuracy (evangelical-Protestant), and any cross-cutting inconsistency the per-chapter automated checks would miss. Don't manufacture flags — only raise what you actually see.

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
