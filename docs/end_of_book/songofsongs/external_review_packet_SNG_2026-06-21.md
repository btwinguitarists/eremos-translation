# Song of Songs — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-21**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Song of Songs** (8 chapters, 117 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah complete (not yet tagged). Song of Songs 8/8 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Song of Songs (SNG) — end-of-book external-review items

_Auto-derived from the book's own `key_decisions`, textual-variant footnotes, and automated check reports (8 chapters, 117 verses). These are evidence-based sanity-check prompts, not hand-curated maintainer concerns — review them as a corpus-level second opinion and flag anything inconsistent, mistaken, or theologically off._

## Item A — Divine-name & honorific convention (verify consistency across the whole book)


The book applies the project's locked Tetragrammaton/honorific convention. Confirm it is applied **uniformly** and correctly across every chapter, and flag any verse where the divine name, an Adonai-YHWH compound, or royal honorifics (ราชาศัพท์) read inconsistently or wrongly.


## Item B — Textual & versification divergences (verify handling)


Key-decisions in this book that flag a textual variant, LXX/MT difference, versification realignment, or cipher. Confirm each is handled correctly and consistently:

- **Song of Songs 1:2** — ฉัน / เธอ (เสียงคู่รัก)
  - ระบบเสียงประจำเล่ม: คู่รักทั้งสองใช้ ฉัน แทนตน และ เธอ เรียกกัน (register กวีรัก ไม่ใช้ ดิฉัน/ข้าพเจ้า); ตัวบทไม่เพิ่มหัวข้อผู้พูด (MT-anchored — MT ไม่มี) ผู้พูดระบุใน thai_summary; เมื่อกล่าวถึงคนรักในภาพกษัตริย์ (1:4, 1:12) คงราชาศัพท์อ่อนตามบท persona
- **Song of Songs 2:7** — คำสาบาน-กำชับ (refrain)
  - refrain ประจำเล่ม — ซ้ำ 3:5 (verbatim), 8:4 (รูปแปร); ตรึงถ้อยคำนี้ทุกครั้ง; สาบาน ตามสูตร hebrew_oath_formulas (เทียบ Eccl 8:2)
- **Song of Songs 3:3** — พวกคนยาม
  - ซ้ำในฉากคู่ขนาน 5:7 (ที่นั่นคนยามทำร้ายเธอ) — ตรึง คนยาม ทั้งสองฉาก
- **Song of Songs 3:6** — มดยอบและกำยาน
  - ตามศัพท์เครื่องหอม corpus (มدยอบ 1:13; กำยาน — เทียบ Matt 2:11); ถิ่นทุรกันดาร ตามศัพท์ corpus
- **Song of Songs 5:8** — ฉันป่วยเพราะความรัก
  - ตรึงตาม 2:5; โครงคำสาบาน-กำชับรูปแปร (เนื้อความต่างจาก refrain 2:7/3:5 — ไม่ใช่คำเตือนปลุกรัก)
- **Song of Songs 6:10** — น่าครั่นคร้ามดั่งกองทัพชูธง
  - วลีเดียวกับ 6:4 — MT ซ้ำ; BSB 6:10 แปลแปร (‘stars in procession’) แต่ฉบับนี้ยึด MT จึงตรึงรูปเดียว
- **Song of Songs 6:12** — ราชรถแห่งชนผู้สูงศักดิ์ของฉัน
  - ข้อที่ตีความยากที่สุดของเล่ม — MT เขียนติดกัน עַמִּינָדִיב จึงอ่านได้ทั้งชื่อบุคคล ‘อัมมีนาดีบ’ และแยกคำ עַמִּי־נָדִיב ‘ชนผู้สูงศักดิ์ของฉัน’ (สาย BSB) — เลือกอย่างหลัง; รูปทับศัพท์ใน thai_literal
- **Song of Songs 8:4** — refrain คำสาบาน-กำชับ (รูปท้ายเล่ม)
  - ครั้งที่สามของ refrain — MT ตัดวรรคฝูงละมั่งออกและใช้ מַה; คงแกนถ้อยคำ verbatim ตาม 2:7/3:5 โดยสะท้อนการย่อของต้นฉบับ
- **Song of Songs 8:14** — รีบรุดมาเถิด ที่รักของฉัน
  - barach ตามตัวอักษร ‘ลี้หนี’ (ใน thai_literal) — บริบทคือเรียกให้รีบมาหาเธอ (ปิดเล่มคู่ขนาน 2:17; ภูเขาแห่งเครื่องหอม แทน ภูเขาเบเธอร์); ละมั่งหรือกวางหนุ่ม ตรึงตาม 2:9


## Item C — Locked-term / convention applications (verify uniformity)


_No explicitly locked-term key-decisions were tagged in this book._


## Item D — Hardest interpretive cruxes (evaluate the calls)


The key-decisions with the most reasoning attached — i.e. the book's hardest judgment calls. Evaluate whether each rendering is defensible from the source text:

- **Song of Songs 8:6** — เปลวเพลิงแห่งพระยาห์
  - ตัวบทที่สกัดมาเขียนแยก יָה — อ่านเป็นพระนามย่อ (Yah) ตามแนว corpus ที่คงเสียง ยาห์ (ฮาเลลูยาห์ ในเพลงสดุดี); นี่คือพระนามครั้งเดียวของทั้งเล่ม; สายอ่านขั้นสูงสุด (‘เปลวเพลิงอันเกรียงไกร’ — BSB) เก็บใน thai_literal; FLAG FOR EOB REVIEW — ทางเลือกสองสายนี้เป็นข้อตัดสินระดับเล่ม
- **Song of Songs 1:2** — ฉัน / เธอ (เสียงคู่รัก)
  - ระบบเสียงประจำเล่ม: คู่รักทั้งสองใช้ ฉัน แทนตน และ เธอ เรียกกัน (register กวีรัก ไม่ใช้ ดิฉัน/ข้าพเจ้า); ตัวบทไม่เพิ่มหัวข้อผู้พูด (MT-anchored — MT ไม่มี) ผู้พูดระบุใน thai_summary; เมื่อกล่าวถึงคนรักในภาพกษัตริย์ (1:4, 1:12) คงราชาศัพท์อ่อนตามบท persona
- **Song of Songs 7:11** — ความปรารถนาของเขาก็มีต่อฉัน
  - teshuqah คำเดียวกับ Gen 3:16 (ความปรารถนาของเจ้าจะมีต่อสามี) — ที่นี่กลับทิศ: ความปรารถนาของ ‘เขา’ มีต่อ ‘เธอ’; ตรึง ความปรารถนา ตาม Gen 3:16 เพื่อให้เสียงสะท้อน-กลับด้านได้ยินในภาษาไทย; ขั้นที่สามของสูตร 2:16/6:3
- **Song of Songs 6:12** — ราชรถแห่งชนผู้สูงศักดิ์ของฉัน
  - ข้อที่ตีความยากที่สุดของเล่ม — MT เขียนติดกัน עַמִּינָדִיב จึงอ่านได้ทั้งชื่อบุคคล ‘อัมมีนาดีบ’ และแยกคำ עַמִּי־נָדִיב ‘ชนผู้สูงศักดิ์ของฉัน’ (สาย BSB) — เลือกอย่างหลัง; รูปทับศัพท์ใน thai_literal
- **Song of Songs 2:1** — ดอกกุหลาบแห่งชาโรน / ดอกบัว
  - chavatzelet ตามสาย BSB (rose; เชิงพฤกษศาสตร์ = crocus — บันทึก; โยง Isa 35:1); שׁוֹשַׁנַּת (รูป construct ของ lemma שׁוֹשַׁנָּה) → ดอกบัว ตามคำตรึง corpus (1KI 7 งานดอกบัวของวิหาร)
- **Song of Songs 8:14** — รีบรุดมาเถิด ที่รักของฉัน
  - barach ตามตัวอักษร ‘ลี้หนี’ (ใน thai_literal) — บริบทคือเรียกให้รีบมาหาเธอ (ปิดเล่มคู่ขนาน 2:17; ภูเขาแห่งเครื่องหอม แทน ภูเขาเบเธอร์); ละมั่งหรือกวางหนุ่ม ตรึงตาม 2:9
- **Song of Songs 4:9** — น้องสาวของฉัน เจ้าสาวของฉัน
  - คู่คำเรียกรักประจำชุด 4:9-5:1 (×4+) — ‘น้องสาว’ เป็นสำนวนรักเครือญาติของกวีตะวันออกใกล้โบราณ (ไม่ใช่พี่น้องจริง; พ้องกับการเรียก น้อง ในขนบรักไทย) — ตรึงคู่คำนี้
- **Song of Songs 5:2** — คนงามพร้อมของฉัน
  - tammah = ไร้ตำหนิ/งามพร้อม (โยง מוּם 4:7) — คำเรียกที่สี่ในชุด; ตรึง (ซ้ำ 6:9); สี่คำเรียกเรียงตามต้นฉบับ: น้องสาว-ยอดรัก-นกพิราบ-คนงามพร้อม


## Item E — Open corpus-level read


Beyond the items above: read for naturalness in modern Thai, theological accuracy (evangelical-Protestant), and any cross-cutting inconsistency the per-chapter automated checks would miss. Don't manufacture flags — only raise what you actually see.

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
