# Song of Songs — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-03**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Song of Songs** (8 chapters, 117 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job complete (not yet tagged). Song of Songs 8/8 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — 8:6 שַׁלְהֶבֶתְ יָה ("flame of Yah"): the Song's only divine-name-adjacent token

**The crux:** The Song of Songs contains **no Tetragrammaton anywhere** — except a single contested token at the book's theological climax, 8:6. The extracted MT writes the final element with a space: `שַׁלְהֶבֶתְ יָה`. The final `יָה` can be read two ways:

1. **Theophoric** — the short-form divine name **Yah** (as in Hallelu-Yah). Reading: "the flame of Yah / the very flame of the LORD" (so ESV, CSB).
2. **Frozen superlative** — the `-yah` ending as an intensifying suffix. Reading: "a mighty / raging flame, the fiercest blaze of all" (so NIV, BSB).

**The current rendering takes the theophoric line in the main text, the superlative in `thai_literal`:**

- SNG 8:6 HEB: `כִּי־עַזָּה כַמָּוֶת אַהֲבָה … רְשָׁפֶיהָ רִשְׁפֵּי אֵשׁ שַׁלְהֶבֶתְ יָה`
- TH (main): `เพราะความรักเข้มแข็งดั่งความตาย … ประกายของมันคือประกายแห่งไฟ คือเปลวเพลิงแห่ง**พระยาห์**` ("…the flame of Phra-Yah")
- TH (`thai_literal`): `…คือเปลวเพลิงอันเกรียงไกร (อ่านแบบขั้นสูงสุด)` ("…a mighty flame [superlative reading]")

The verse-level decision note itself flags this: *"this is the only divine name in the whole book … FLAG FOR EOB REVIEW — this two-way choice is a book-level decision."*

**A second, internal problem if the theophoric reading stands:** the project's divine-names table locks the short form `יָהּ → ยาห์` **bare** (e.g. Pss 68:4; הַלְלוּ-יָהּ → ฮาเลลูยาห์). The current rendering uses **พระยาห์** (an honorific prefix พระ- + ยาห์) that no table row authorizes. And the automated divine-names check reports **0 YHWH chapters** for the whole book — it does not recognize שַׁלְהֶבֶתְ יָה as a divine-name occurrence — so the book currently ships with no first-occurrence footnote.

**Three questions:**
1. Is the theophoric reading ("flame of Yah / the LORD") the right editorial line for an evangelical-Protestant CC0 Thai Bible, or should the project follow the superlative line (NIV/BSB "a mighty flame") with the theophoric in a footnote? (Evangelical English translations are genuinely split: ESV/CSB theophoric, NIV/BSB superlative.)
2. If theophoric, should the surface form be the locked **ยาห์** (bare, table-conformant) rather than the unauthorized **พระยาห์** — i.e. `…เปลวเพลิงแห่งยาห์`?
3. If theophoric, does the book now owe a first-occurrence translator footnote at 8:6 explaining the Yah short-form + the superlative alternative — even though it has no full Tetragrammaton elsewhere?

---

## Item B — King-persona + Solomon: should an OT poetic book use royal honorifics (ราชาศัพท์) for human kings?

**The pattern:** Thai has a royal register (ราชาศัพท์ / "rachasap" — special verbs like ทรง-, pronouns like พระองค์, body-part nouns like พระทัย "royal heart"). The Eremos OT reserves this register for **God** by default. But the Song applies **light/full rachasap to human kings**:

| Context | Verse | Thai | Register |
|---|---|---|---|
| The male lover *figured* as a king | 1:4 | กษัตริย์**ทรง**นำฉันเข้าในห้องของ**พระองค์** | light royal |
| Solomon's wedding procession | 3:9–11 | **ทรง**สร้างพระราชยาน… **ทรง**มงกุฎซึ่ง**พระมารดา**สวมให้**พระองค์** … **พระทัย** | full royal |
| Solomon as vineyard-owner | 8:11 | ซาโลมอน**ทรง**มี… **พระองค์ทรง**ให้…เช่า | full royal |
| The king *held captive* in her hair | 7:6 | กษัตริย์ก็ตกเป็นเชลย (plain — no royal verb) | **plain** |

Note the sophisticated modulation at 7:6: the *conquered* king is **not** dignified with royal register.

**The corpus tension:** The project's narrative-book register policy (`ot_register_policy §2.2`) **grants** Hebrew kings full royal register in their public-office role. But the project's two prior poetic/wisdom books — **Psalms and Proverbs** — went the *other* way and kept human kings **non-royal**, reserving the royal register for God alone (Proverbs end-of-book audit, 2026-05-31, flagged this as the book's headline editorial decision and recommended a `human_king_register` decision doc that has not yet been written). So the corpus currently holds two opposed conventions, and the Song follows the narrative policy rather than the Psalms/Proverbs poetic practice. (Unlike Psalms/Proverbs, the Song has essentially **no divine subject**, so using พระองค์ for Solomon creates no in-book ambiguity with God.)

**Question:** For an OT poetic book, is it right to give human kings (and a king-as-lover poetic conceit) the Thai royal register, when the sibling poetic books (Psalms, Proverbs) keep human kings non-royal? Should the three poetic books be made uniform with each other, or is the Song's king-rachasap (with the 7:6 captive-king modulation) defensible as context-appropriate?

---

## Item C — Proper-noun wordplay: surface for readers, or keep in scholarly notes?

**The pattern:** The Song runs several name/sound puns. The project's policy is to keep name-etymology in scholarly notes BY DEFAULT, adding a reader-facing translator footer ONLY when the wordplay is an *active argument-engine* across multiple verses (the test that triggered a footer for Paul's Onesimus "useful" pun in Philemon). The Song's puns are currently all in the scholarly notes:

1. **Shulammite / Shalom / Solomon** — 7:1 `הַשּׁוּלַמִּית → สาวชูลัม` (the woman's only name in the book); the note records the sound-chain שׁוּלַמִּית ↔ שְׁלֹמֹה (Solomon) ↔ שָׁלוֹם (peace), which the book closes at 8:10 (`כְּמוֹצְאֵת שָׁלוֹם → ดั่งผู้นำสันติภาพมาให้`, note: "closes the Shulam–Solomon–Shalom sound-chain … which Thai cannot carry").
2. **dudaim / dodi** — 7:14 `הַדּוּדָאִים → ผลเลื่อน` (mandrakes); note records the דּוּדָאִים / דּוֹדִי ("mandrakes" / "my beloved") pun.
3. **shem / shemen** — 1:3 `שֶׁמֶן` ("oil") / `שְׁמֶךָ` ("your name") sound-play, in the note.

**Question:** The Shulammite/Shalom chain is *structural* (a 7:1 introduction resolved at 8:10) rather than an argument the reader must follow — and the translation concedes Thai can't reproduce the sound-play. By the project's three-condition footer test (active argument + multi-verse density + comprehension-dependency), these stay in the notes. Is that the right call, or should the Shulammite/Shalom inclusio get a single reader-facing footer at 8:10 so a Thai reader sees the book's closing wordplay? Do any of the three cross the threshold?

---

## Item D — Erotic body-imagery: faithful (non-euphemized) — confirm the stance

**The pattern:** The Song's three descriptive-praise poems (ch. 4, 5, 7) render the body imagery **faithfully and without euphemism**:

- 1:13 `בֵּין שָׁדַי` → **ระหว่างทรวงอกของฉัน** ("between my breasts")
- 4:5 / 7:4 breasts → **ทรวงอก**; 7:2 navel/waist → **สะดือ / ท้อง** ("navel / belly"); 7:3 thighs → **ต้นขา**
- 5:4 the door-latch scene keeps its sensual charge: **ใจของฉันก็เร่าร้อนถึงเขา**, with the literal **อวัยวะภายใน…ปั่นป่วน** in the literal field

This is the **opposite** editorial pressure from the project's Leviticus policy, which *euphemizes* the legal "uncover nakedness" sexual-prohibition formula (`uncover_nakedness_euphemism_2026-05.md`). The two are not in conflict — Leviticus euphemizes a juridical-shame register; the Song celebrates married eros and the imagery is the literary point — but the Song is the corpus's most sexually explicit text.

**Question:** For an evangelical-Protestant CC0 Thai Bible aimed partly at a Thai Buddhist-background readership, is the "keep the imagery faithful, don't euphemize" stance the right call across the Song's waṣf poems? Are there specific verses where the Thai is either too explicit or too coy for the register? Should the stance be recorded in a translator-decisions doc so it's applied consistently in future books (e.g. Ezekiel 16/23)?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
