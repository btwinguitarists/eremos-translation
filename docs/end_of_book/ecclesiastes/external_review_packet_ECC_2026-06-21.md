# Ecclesiastes — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-21**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Ecclesiastes** (12 chapters, 222 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah complete (not yet tagged). Ecclesiastes 12/12 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Ecclesiastes (ECC) — end-of-book external-review items

_Auto-derived from the book's own `key_decisions`, textual-variant footnotes, and automated check reports (12 chapters, 222 verses). These are evidence-based sanity-check prompts, not hand-curated maintainer concerns — review them as a corpus-level second opinion and flag anything inconsistent, mistaken, or theologically off._

## Item A — Divine-name & honorific convention (verify consistency across the whole book)


The book applies the project's locked Tetragrammaton/honorific convention. Confirm it is applied **uniformly** and correctly across every chapter, and flag any verse where the divine name, an Adonai-YHWH compound, or royal honorifics (ราชาศัพท์) read inconsistently or wrongly.


## Item B — Textual & versification divergences (verify handling)


Key-decisions in this book that flag a textual variant, LXX/MT difference, versification realignment, or cipher. Confirm each is handled correctly and consistently:

- **Ecclesiastes 2:25** — นอกเหนือไปจากข้าพเจ้า
  - ยึดตัวบท MT (מִמֶּנִּי ‘จากข้าพเจ้า’) ตามนโยบาย MT-anchored; LXX/เปชิตตาอ่าน מִמֶּנּוּ ‘นอกจากพระองค์’ (BSB ตามสายนี้) — บันทึกเป็น textual note
- **Ecclesiastes 3:14** — เพื่อมนุษย์จะยำเกรงพระองค์
  - ยำเกรง ตามศัพท์ corpus (เทียบ Prov 1:7 ความยำเกรง); รูปตามตัวอักษร ‘ต่อพระพักตร์’ เก็บใน thai_literal เพื่อเลี่ยง divine body-part ติดกริยา ทรง- ในตัวบทหลัก
- **Ecclesiastes 4:17** — MT 4:17 = English 5:1
  - จุดแบ่งบทต่างกัน: MT จบบท 4 ที่นี่ แต่ฉบับอังกฤษขึ้นบท 5 — ลงทะเบียนใน versification_map (ECC-4-17) และโซน MT 5:1-19 = Eng 5:2-20
- **Ecclesiastes 6:3** — ทารกที่ตายตั้งแต่เกิด
  - nefel = stillborn — ใช้รูปบรรยายตรง (เทียบ Job 3:16 / Ps 58)
- **Ecclesiastes 7:15** — ในวันคืนอันไร้แก่นสารของข้าพเจ้า
  - hevel รูป genitive ส่วนตัว (วันแห่ง hevel ของข้าพเจ้า) — คงคำตรึง เทียบ 6:12
- **Ecclesiastes 8:10** — ถูกลืม
  - ยึดตัวบท MT (שכח ‘ถูกลืม’) ตามนโยบาย MT-anchored; BSB ตามสายแปร יִשְׁתַּבְּחוּ ‘ได้รับการสรรเสริญ’ — บันทึก textual note (เทียบ 2:25)
- **Ecclesiastes 9:9** — ชีวิตอันไร้แก่นสารของเจ้า
  - hevel genitive บุรุษที่สอง (×2 ในข้อ) — คงคำตรึง เทียบ 6:12 / 7:15; ข้อนี้เป็นคู่ตรงข้ามเชิงบวกของภาพหญิงบ่วงแร้ว 7:26
- **Ecclesiastes 9:11** — วาระและเหตุไม่คาดฝัน
  - עֵת → วาระ ตามคำตรึง 3:1; פֶגַע = เหตุบังเอิญ/ไม่คาดฝัน — คู่ขนานกับ miqreh
- **Ecclesiastes 11:5** — ลม
  - ruach กำกวม ลม/วิญญาณ (คู่กับครรภ์มารดาอ่านได้สองชั้น) — เลือก ‘ลม’ ขนาน 11:4; บันทึกชั้นความหมาย


## Item C — Locked-term / convention applications (verify uniformity)


Renderings the translator marked as locked/by-convention. Confirm they match the project glossary and are used consistently here and against the rest of the corpus:

- **Ecclesiastes 1:1** — ปัญญาจารย์


## Item D — Hardest interpretive cruxes (evaluate the calls)


The key-decisions with the most reasoning attached — i.e. the book's hardest judgment calls. Evaluate whether each rendering is defensible from the source text:

- **Ecclesiastes 1:2** — ไร้แก่นสาร
  - hevel leitwort (~38x ทั้งเล่ม) — เลือกคำเดียวคงที่เพื่อรักษา refrain; ไร้แก่นสาร = ‘ไม่มีแก่นสารถาวร’ ตรง uW gloss ‘vapor that disappears, no lasting value’; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus (33 ข้อก่อนหน้าไม่เคยใช้). PROVISIONAL — รอคำยืนยันจากผู้อ่านไทยสองท่านของ Ben (2026-06-03); หากเปลี่ยนเป็น อนิจจัง ต้อง 
- **Ecclesiastes 1:14** — ไร้แก่นสาร
  - hevel leitwort (~38x ทั้งเล่ม) — เลือกคำเดียวคงที่เพื่อรักษา refrain; ไร้แก่นสาร = ‘ไม่มีแก่นสารถาวร’ ตรง uW gloss ‘vapor that disappears, no lasting value’; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus (33 ข้อก่อนหน้าไม่เคยใช้). PROVISIONAL — รอคำยืนยันจากผู้อ่านไทยสองท่านของ Ben (2026-06-03); หากเปลี่ยนเป็น อนิจจัง ต้อง 
- **Ecclesiastes 2:1** — ไร้แก่นสาร
  - hevel leitwort — คำเดียวคงที่ทั้งเล่มเพื่อรักษา refrain; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus. PROVISIONAL — รอคำยืนยันจากผู้อ่านไทยของ Ben (2026-06-03)
- **Ecclesiastes 2:11** — ไร้แก่นสาร
  - hevel leitwort — คำเดียวคงที่ทั้งเล่มเพื่อรักษา refrain; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus. PROVISIONAL — รอคำยืนยันจากผู้อ่านไทยของ Ben (2026-06-03)
- **Ecclesiastes 2:15** — ไร้แก่นสาร
  - hevel leitwort — คำเดียวคงที่ทั้งเล่มเพื่อรักษา refrain; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus. PROVISIONAL — รอคำยืนยันจากผู้อ่านไทยของ Ben (2026-06-03)
- **Ecclesiastes 2:17** — ไร้แก่นสาร
  - hevel leitwort — คำเดียวคงที่ทั้งเล่มเพื่อรักษา refrain; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus. PROVISIONAL — รอคำยืนยันจากผู้อ่านไทยของ Ben (2026-06-03)
- **Ecclesiastes 2:19** — ไร้แก่นสาร
  - hevel leitwort — คำเดียวคงที่ทั้งเล่มเพื่อรักษา refrain; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus. PROVISIONAL — รอคำยืนยันจากผู้อ่านไทยของ Ben (2026-06-03)
- **Ecclesiastes 2:21** — ไร้แก่นสาร
  - hevel leitwort — คำเดียวคงที่ทั้งเล่มเพื่อรักษา refrain; เลี่ยงศัพท์พุทธ อนิจจัง ตามแนวทาง corpus. PROVISIONAL — รอคำยืนยันจากผู้อ่านไทยของ Ben (2026-06-03)


## Item E — Open corpus-level read


Beyond the items above: read for naturalness in modern Thai, theological accuracy (evangelical-Protestant), and any cross-cutting inconsistency the per-chapter automated checks would miss. Don't manufacture flags — only raise what you actually see.

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
