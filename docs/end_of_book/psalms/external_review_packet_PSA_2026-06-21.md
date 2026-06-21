# Psalms — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-21**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Psalms** (150 chapters, 2,527 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah complete (not yet tagged). Psalms 150/150 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Psalms (PSA) — end-of-book external-review items

_Auto-derived from the book's own `key_decisions`, textual-variant footnotes, and automated check reports (150 chapters, 2,527 verses). These are evidence-based sanity-check prompts, not hand-curated maintainer concerns — review them as a corpus-level second opinion and flag anything inconsistent, mistaken, or theologically off._

## Item A — Divine-name & honorific convention (verify consistency across the whole book)


The book applies the project's locked Tetragrammaton/honorific convention. Confirm it is applied **uniformly** and correctly across every chapter, and flag any verse where the divine name, an Adonai-YHWH compound, or royal honorifics (ราชาศัพท์) read inconsistently or wrongly.

> First-occurrence convention footnote (chapter 1 / first occurrence):
>
> **องค์พระผู้เป็นเจ้า** ในบทนี้ (ปรากฏครั้งแรกที่ข้อ 2) แปลจากภาษาฮีบรู יהוה (พระนามเฉพาะของพระเจ้า ออกเสียงโดยทั่วไปว่า ‘ยาห์เวห์’). ฉบับเอเรโมสใช้ **องค์พระผู้เป็นเจ้า** ตามแบบแผนของฉบับพันธสัญญาใหม่ที่แปล κύριος ซึ่งในต้นฉบับฮีบรูตรงกับ יהוה. ดูรายละเอียดเพิ่มเติมที่ docs/translator_decisions/divine_names_table_2026-05.md.


## Item B — Textual & versification divergences (verify handling)


Key-decisions in this book that flag a textual variant, LXX/MT difference, versification realignment, or cipher. Confirm each is handled correctly and consistently:

- **Psalms 1:2** — องค์พระผู้เป็นเจ้า
  - יהוה (พระนามเฉพาะของพระเจ้า) → ‘องค์พระผู้เป็นเจ้า’ ตามแบบแผนที่ locked ใน divine_names_table_2026-05.md (เทียบ κύριος ในพันธสัญญาใหม่)
- **Psalms 1:4** — คนชั่วหาเป็นเช่นนั้นไม่
  - ‘ไม่เป็นเช่นนั้น’ อ้างถึงทั้งข้อ 1-3 — คนชั่วต่างจากผู้เป็นสุขโดยสิ้นเชิง
- **Psalms 1:6** — องค์พระผู้เป็นเจ้า
  - יהוה (พระนามเฉพาะของพระเจ้า) → ‘องค์พระผู้เป็นเจ้า’ ตามแบบแผนที่ locked ใน divine_names_table_2026-05.md (เทียบ κύριος ในพันธสัญญาใหม่)
- **Psalms 2:5** — ด้วยพระพิโรธ … ด้วยความกริ้วอันแรงกล้า
  - אַף (ตามตัวอักษร ‘จมูก’ — มานุษยรูปนิยม) → ‘พระพิโรธ’; חָרוֹן ‘ความกริ้วอันร้อนแรง’ — รักษาความเข้มของคำคู่ขนาน
- **Psalms 2:9** — เจ้าจะทำลาย
  - MT תְּרֹעֵם (ราก רעע ‘ทุบ/ทำลาย’); ฉบับ LXX อ่าน רעה ‘ปกครอง/เลี้ยงดู’ — พันธสัญญาใหม่ (วว 2:27; 12:5; 19:15) ตาม LXX ‘ปกครองด้วยคทาเหล็ก’; เราคงตาม MT ‘ทำลาย’ และบันทึกความต่างไว้ในหมายเหตุ
- **Psalms 2:12** — จงจุมพิตบุตรนั้น
  - בַר (ภาษาอาราเมอิก ‘บุตร’, เทียบ בֵּן ‘บุตร’ ในข้อ 7; บางฉบับอ่านว่า ‘ความบริสุทธิ์’ — เป็นจุดยากในเชิงข้อความ); ‘จุมพิต’ = ท่าทีแสดงความจงรักภักดี/ยอมจำนนต่อกษัตริย์; การอ่านเชิงพระคริสต์อยู่ในหมายเหตุ
- **Psalms 3:1** — บทเพลงสดุดีของดาวิด เมื่อทรงหนีจากอับซาโลมราชโอรสของพระองค์
  - คำนำ (superscription) = ข้อ 1 ใน MT; ดาวิดในฐานะกษัตริย์ → ราชาศัพท์ ‘ทรงหนี’; אַבְשָׁלוֹם בְּנוֹ ‘อับซาโลมราชโอรส’ (พระราชบุตรของดาวิด)
- **Psalms 3:3** — เซลาห์
  - เซลาห์ (ปรากฏครั้งแรกในหนังสือสดุดี) เป็นคำดนตรีฮีบรูที่ไม่ทราบความหมายแน่ชัด — ถอดเสียงไว้ตามแบบแผน (เทียบ ‘ฮาเลลูยาห์’)
- **Psalms 4:5** — จงครั่นคร้ามเถิด แต่อย่าทำบาป
  - רָגַז ‘ตัวสั่น/หวั่นไหว’ — อาจเป็นการสั่นด้วยความยำเกรง (ความหมายหลักในบริบทที่ตามด้วย ‘สงบนิ่ง’) หรือด้วยความโกรธ; เอเฟซัส 4:26 อ้างตามฉบับ LXX ว่า ‘จงโกรธ’ (ดูหมายเหตุ)
- **Psalms 6:2** — ด้วยพระพิโรธ … ด้วยความกริ้วอันแรงกล้า
  - אַף ‘พระพิโรธ’; חֵמָה ‘ความกริ้วอันร้อนแรง’ — รักษาคำคู่ขนานของความโกรธ; เป็นเสียงคร่ำครวญสำนึกผิด
- **Psalms 6:7** — ที่นอนชุ่มโชก … เตียงเปียกชุ่ม
  - ภาพเกินจริงเชิงกวี (hyperbole) — น้ำตาท่วมที่นอน; מִטָּה/עֶרֶשׂ ‘ที่นอน/เตียง’ คำคู่ขนาน
- **Psalms 8:3** — ทรงสถาปนาพลัง
  - עֹז ‘พลัง/กำลัง’ (MT); ฉบับ LXX อ่านว่า ‘คำสรรเสริญ’ และพระเยซูทรงอ้างตามฉบับ LXX ที่ มัทธิว 21:16 — เราคงตาม MT และบันทึกไว้ในหมายเหตุ
- **Psalms 8:6** — ต่ำกว่าพระเจ้าเพียงเล็กน้อย
  - אֱלֹהִים → ‘พระเจ้า’ (MT ตามตัวอักษร); ฉบับ LXX และ ฮีบรู 2:7 อ่านว่า ‘เหล่าทูตสวรรค์’ — เราคงตาม MT และบันทึกไว้ในหมายเหตุ
- **Psalms 12:8** — พระองค์จะทรงปกป้องพวกเรา
  - ฉบับเขียน (ketiv) ‘ปกป้องพวกเขา’ (คนยากไร้ในข้อ 6) ฉบับอ่าน (qere) ‘พวกเรา’ — แปลตามบริบทผู้วางใจ
- **Psalms 16:9** — จิตวิญญาณของข้าพระองค์ก็เปรมปรีดิ์
  - כְּבוֹדִי ‘เกียรติของข้าพเจ้า’ = ตัวตนภายใน/จิตวิญญาณ (MT); ฉบับ LXX/กิจการ 2:26 อ่านว่า ‘ลิ้นของข้าพเจ้า’ — เราคงตาม MT
- **Psalms 16:10** — ผู้จงรักภักดีของพระองค์ … เห็นหลุมมรณา
  - שַׁחַת ‘หลุม/หลุมมรณา’ (MT); ฉบับ LXX และ กิจการ 2:27, 13:35 อ่านว่า ‘ความเน่าเปื่อย’ — เราคงตาม MT และบันทึกไว้; חָסִיד ‘ผู้จงรักภักดี’ ซึ่งพันธสัญญาใหม่อ่านว่าหมายถึง ‘องค์บริสุทธิ์’ คือพระคริสต์ (ดูหมายเหตุ)
- **Psalms 19:15** — ศิลาและพระผู้ไถ่ของข้าพระองค์
  - גֹּאֵล (ผู้ไถ่เชิงเทววิทยา) → ‘พระผู้ไถ่’ ตาม goel_kinsman_redeemer_2026-05.md (เทียบ โยบ 19:25)
- **Psalms 20:7** — ผู้ที่พระองค์ทรงเจิมไว้
  - מָשִׁיחַ (ผู้ถูกเจิม) ในที่นี้หมายถึงกษัตริย์ที่พระเจ้าทรงเจิม — แปลตามความหมายพื้นผิวใน OT ‘ผู้ที่พระองค์ทรงเจิม’; นัยถึงพระเมสสิยาห์อธิบายในเชิงอรรถ (เทียบ ดาเนียล 9:25-26)
- **Psalms 20:8** — เราจะระลึกถึง (พระนาม)
  - נַזְכִּיר (ราก זכר, รูป hiphil) = ‘เราจะกล่าวถึง/ระลึกถึง/ร้องออกพระนาม’ — MT เน้นการร้องออกพระนามของพระเจ้าเป็นที่พึ่ง (ต่างจาก BSB ‘trust’); คำกริยาฝ่ายศัตรู (รถรบ/ม้า) ถูกละไว้ จึงเสริม ‘ไว้วางใจ’ เพื่อความชัดเจน
- **Psalms 20:10** — ขอทรงช่วยให้รอด ขอองค์กษัตริย์ทรงตอบเรา
  - ตามการแบ่งวรรค (athnach) ของ MT: ‘องค์พระผู้เป็นเจ้า ขอทรงช่วย!’ | ‘องค์กษัตริย์ (พระเจ้าผู้ทรงเป็นกษัตริย์) ทรงตอบเรา’. ฉบับ LXX/BSB อ่านว่า ‘ขอทรงช่วยกษัตริย์ (มนุษย์)’ — ฉบับเอเรโมสยึดการอ่านตาม MT
- **Psalms 22:17** — พวกเขาแทงมือและเท้าของข้าพระองค์
  - จุดที่มีปัญหาด้านตัวบทที่สำคัญที่สุดในสดุดี. MT ชี้สระเป็น כָּאֲרִי ‘เหมือนสิงโต’ (ไวยากรณ์ไม่สมบูรณ์ ต้องเสริมคำกริยา); ฉบับ LXX/ซีเรียค/วัลเกต และต้นฉบับฮีบรูบางฉบับอ่าน כָּארוּ ‘เขาเจาะ/แทง’. ฉบับเอเรโมสและฉบับแปลสมัยใหม่ส่วนใหญ่ (รวม BSB/ESV/NIV) ยึด ‘แทง’ ในเนื้อหาหลัก และระ
- **Psalms 24:6** — ผู้ที่แสวงหาพระพักตร์ของพระองค์ ข้าแต่พระเจ้าแห่งยาโคบ
  - MT มีเพียง ‘ยาโคบ’ (יַעֲקֹב); ฉบับ LXX/ซีเรียค และฉบับแปลส่วนใหญ่ (รวม BSB) เสริม ‘พระเจ้าแห่ง’ → ‘พระเจ้าแห่งยาโคบ’ ซึ่งเป็นการอ่านที่สมเหตุสมผล (ไม่ใช่การแสวงหาพระพักตร์ของยาโคบ แต่ของพระเจ้าผู้เป็นพระเจ้าของยาโคบ)
- **Psalms 25:14** — องค์พระผู้เป็นเจ้าทรงเป็นมิตรสนิท
  - סוֹד = ‘การปรึกษาลับ/มิตรภาพอันสนิทสนม’ — สื่อว่าพระเจ้าทรงไว้วางใจและเปิดเผยพระทัยแก่ผู้ยำเกรงพระองค์ (เทียบ BSB ‘confides in’)
- **Psalms 28:8** — ผู้ที่พระองค์ทรงเจิมไว้
  - מָשִׁיחַ (ผู้ถูกเจิม) ในที่นี้หมายถึงกษัตริย์ที่พระเจ้าทรงเจิม — แปลตามความหมายพื้นผิวใน OT; นัยถึงพระเมสสิยาห์อธิบายในเชิงอรรถ (เทียบ สดุดี 20:7; ดาเนียล 9:25-26)
- **Psalms 29:9** — กวางตัวเมีย
  - MT ชี้สระเป็น אַיָּלוֹת ‘กวางตัวเมีย’ (พระสุรเสียงทำให้กวางตกใจคลอดลูกก่อนกำหนด); ฉบับ BSB/บางฉบับอ่าน אֵילוֹת ‘ต้นโอ๊ก’ (เข้าคู่กับ ‘ป่า’) — ฉบับเอเรโมสยึดการชี้สระตาม MT


## Item C — Locked-term / convention applications (verify uniformity)


Renderings the translator marked as locked/by-convention. Confirm they match the project glossary and are used consistently here and against the rest of the corpus:

- **Psalms 1:2** — องค์พระผู้เป็นเจ้า
- **Psalms 3:3** — เซลาห์


## Item D — Hardest interpretive cruxes (evaluate the calls)


The key-decisions with the most reasoning attached — i.e. the book's hardest judgment calls. Evaluate whether each rendering is defensible from the source text:

- **Psalms 22:17** — พวกเขาแทงมือและเท้าของข้าพระองค์
  - จุดที่มีปัญหาด้านตัวบทที่สำคัญที่สุดในสดุดี. MT ชี้สระเป็น כָּאֲרִי ‘เหมือนสิงโต’ (ไวยากรณ์ไม่สมบูรณ์ ต้องเสริมคำกริยา); ฉบับ LXX/ซีเรียค/วัลเกต และต้นฉบับฮีบรูบางฉบับอ่าน כָּארוּ ‘เขาเจาะ/แทง’. ฉบับเอเรโมสและฉบับแปลสมัยใหม่ส่วนใหญ่ (รวม BSB/ESV/NIV) ยึด ‘แทง’ ในเนื้อหาหลัก และระบุการอ่าน MT ‘เหมือนสิงโต’ ในเชิงอรรถ
- **Psalms 19:8** — ธรรมบัญญัติ … พระโอวาท
  - คำเรียกพระวจนะของพระเจ้าหลายคำในข้อ 8-10 — ฉบับเอเรโมสล็อกการแปลให้ต่างกันและคงเส้นคงวา (เตรียมสำหรับ สดด 119). รูปรากศัพท์ (lemma): תּוֹרָה=ธรรมบัญญัติ, עֵדוּת=พระโอวาท, פִּקּוּדִים=ข้อบังคับ, מִצְוָה=พระบัญญัติ, יִרְאָה=ความยำเกรง, מִשְׁפָּטִים=ข้อตัดสิน
- **Psalms 24:6** — ผู้ที่แสวงหาพระพักตร์ของพระองค์ ข้าแต่พระเจ้าแห่งยาโคบ
  - MT มีเพียง ‘ยาโคบ’ (יַעֲקֹב); ฉบับ LXX/ซีเรียค และฉบับแปลส่วนใหญ่ (รวม BSB) เสริม ‘พระเจ้าแห่ง’ → ‘พระเจ้าแห่งยาโคบ’ ซึ่งเป็นการอ่านที่สมเหตุสมผล (ไม่ใช่การแสวงหาพระพักตร์ของยาโคบ แต่ของพระเจ้าผู้เป็นพระเจ้าของยาโคบ)
- **Psalms 20:8** — เราจะระลึกถึง (พระนาม)
  - נַזְכִּיר (ราก זכר, รูป hiphil) = ‘เราจะกล่าวถึง/ระลึกถึง/ร้องออกพระนาม’ — MT เน้นการร้องออกพระนามของพระเจ้าเป็นที่พึ่ง (ต่างจาก BSB ‘trust’); คำกริยาฝ่ายศัตรู (รถรบ/ม้า) ถูกละไว้ จึงเสริม ‘ไว้วางใจ’ เพื่อความชัดเจน
- **Psalms 2:7** — ข้าพเจ้าจะประกาศ … ตรัสกับข้าพเจ้า
  - เปลี่ยนผู้พูดเป็นกษัตริย์ (สดด 2:7 uW); กษัตริย์พูดกับ/เกี่ยวกับองค์พระผู้เป็นเจ้าในท่าทีนอบน้อม → ‘ข้าพเจ้า’ (เทียบคำอธิษฐานของซาโลมอน 1พกษ 8 ใน ot_register_policy §2.2); ส่วนพระดำรัสที่ทรงอ้างใช้ ‘เรา’ (เทวสภาพ)
- **Psalms 16:10** — ผู้จงรักภักดีของพระองค์ … เห็นหลุมมรณา
  - שַׁחַת ‘หลุม/หลุมมรณา’ (MT); ฉบับ LXX และ กิจการ 2:27, 13:35 อ่านว่า ‘ความเน่าเปื่อย’ — เราคงตาม MT และบันทึกไว้; חָסִיד ‘ผู้จงรักภักดี’ ซึ่งพันธสัญญาใหม่อ่านว่าหมายถึง ‘องค์บริสุทธิ์’ คือพระคริสต์ (ดูหมายเหตุ)
- **Psalms 8:5** — มนุษย์เป็นใครเล่า … บุตรแห่งมนุษย์
  - אֱנוֹשׁ ‘มนุษย์ (ผู้อ่อนแอ)’; בֶּן־אָדָם ที่นี่เป็นสำนวนหมายถึงมนุษย์ทั่วไป → ‘บุตรแห่งมนุษย์’ (ตาม son_of_man_disambiguation — สำนวนมนุษย์ มิใช่พระนามพระเมสสิยาห์); ฮีบรู 2:6 อ้างถึงพระคริสต์ (ดูหมายเหตุ)
- **Psalms 2:12** — จงจุมพิตบุตรนั้น
  - בַר (ภาษาอาราเมอิก ‘บุตร’, เทียบ בֵּן ‘บุตร’ ในข้อ 7; บางฉบับอ่านว่า ‘ความบริสุทธิ์’ — เป็นจุดยากในเชิงข้อความ); ‘จุมพิต’ = ท่าทีแสดงความจงรักภักดี/ยอมจำนนต่อกษัตริย์; การอ่านเชิงพระคริสต์อยู่ในหมายเหตุ


## Item E — Open corpus-level read


Beyond the items above: read for naturalness in modern Thai, theological accuracy (evangelical-Protestant), and any cross-cutting inconsistency the per-chapter automated checks would miss. Don't manufacture flags — only raise what you actually see.

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
