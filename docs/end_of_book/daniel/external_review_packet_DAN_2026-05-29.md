# Daniel — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-29**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Daniel** (12 chapters, 357 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings complete (not yet tagged). Daniel 12/12 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Foreign-monarch register: full ราชาศัพท์ for four Gentile emperors (the fourth and final book of the deferred Ezra–Nehemiah–Esther–Daniel decision)

**The pattern:** Eremos's OT register policy (`ot_register_policy_2026-05.md §2.2`) grants foreign emperors full Thai royal honorifics (ราชาศัพท์ — `ทรง`-prefixed verbs, `เสด็จ` for movement, `ตรัส` for speech, royal-prefixed body nouns, `บรรทม` for royal sleep) in the narrator's voice "even if villainous," with a downshift only for grave moral failure. The companion sub-rule §2.5 holds Hebrew court-officials (Joseph, Daniel, Mordecai, Nehemiah — Daniel is named explicitly) in plain register regardless of office. Daniel exercises both halves harder than any prior book: four emperors and the named vizier himself.

**All four emperors get full ราชาศัพท์ in narrator voice:**
- DAN 1:1 HEB: `בָּא נְבוּכַדְנֶאצַּר מֶלֶךְ־בָּבֶל יְרוּשָׁלִַם וַיָּצַר עָלֶיהָ` → TH: `เนบูคัดเนสซาร์กษัตริย์แห่งบาบิโลน**ทรง**ยกทัพมายังกรุงเยรูซาเล็มและ**ทรง**ล้อมเมืองไว้` (KD: "§2.2, ตารางระบุ 'เนบูคัดเนสซาร์' โดยตรง")
- DAN 5:1 ARAM: `בֵּלְשַׁאצַּר מַלְכָּא עֲבַד לְחֶם רַב` → TH: `กษัตริย์เบลชัสซาร์**ทรง**จัดงานเลี้ยงใหญ่` — register **kept royal straight through the temple-vessel sacrilege** (5:2–4)
- DAN 6:1 ARAM: `דָּרְיָוֶשׁ … קַבֵּל מַלְכוּתָא` → TH: `ดาริอัสชาวมีเดีย**ทรง**รับราชอาณาจักร`; 6:18/6:20 → `**บรรทม**ไม่หลับ … **ทรง**ตื่นบรรทม…รีบ**เสด็จ**ไปยังถ้ำสิงโต`
- Cyrus appears only as a regnal dating anchor (1:21, 6:28, 10:1) — no narrated action.

**The named vizier is held plain (§2.5):**
- DAN 2:16 → TH: `ดาเนียลเข้าเฝ้า…**ข้าพระบาท**` (KD: "ดาเนียล(ชาวฮีบรู)…ใช้ภาษาสามัญ/นอบน้อม §2.5 — ไม่รับราชาศัพท์")
- DAN 6:1–4 → "ใช้ภาษาสามัญ §2.5 แม้ดำรงตำแหน่งสูง"; the three friends are likewise plain in their bold address to the king (3:16–18).

**The cross-book conflict:** the same policy is applied four ways. Nehemiah and Esther both grant their Persian king full `ทรง` (Esther cites the Nehemiah precedent explicitly); Daniel does the same for all four kings. **Ezra alone** renders its Persian kings in commoner register — including Ahasuerus/Xerxes at Ezra 4:6, the *same king* Esther renders with full `ทรง` for ten chapters. All four books are shipped and untagged. Daniel is the last book of the very block ("Ezra–Nehemiah–Esther–Daniel") to which Ezra deferred the decision.

**Two questions:**
1. Is granting full Thai royal register (ราชาศัพท์) to Gentile emperors like Nebuchadnezzar and Belshazzar in the *narrator's* voice — including through Belshazzar's sacrilege with the temple vessels — the right editorial stance for an evangelical-Protestant Thai Bible? Or should villainous/sacrilegious foreign kings be down-registered? (Note the contrast: Nebuchadnezzar's register *is* downshifted during his beast-madness at MT 4:30, but on a "divine humiliation" trigger, while Belshazzar's sacrilege keeps royal register.)
2. Given that three of four court-block books (Nehemiah, Esther, Daniel) plus the written policy already grant foreign emperors full ราชาศัพท์, should the project ratify that rule corpus-wide, normalize Ezra's Persian kings to match, and tag all four books together? Is there any reason to prefer the Ezra commoner-register treatment instead?

---

## Item B — "One like a son of man" (7:13) gets light divine register, while the "man clothed in linen" (10:5–6) is kept deliberately plain

**The pattern:** Daniel contains two exalted heavenly figures, and the translation gives them *different* Thai registers on purpose.

**7:13 — the "one like a son of man" receives light royal register (ราชาศัพท์เบา ๆ):**
- DAN 7:13 ARAM: `וַאֲרוּ עִם־עֲנָנֵי שְׁמַיָּא כְּבַר אֱנָשׁ אָתֵה הֲוָה … וְעַד־עַתִּיק יוֹמַיָּא מְטָה` → TH: `มีผู้หนึ่งเหมือน**บุตรมนุษย์**เสด็จมาพร้อมกับเมฆแห่งฟ้าสวรรค์ **พระองค์เสด็จ**เข้าไปเฝ้าผู้เจริญด้วยวัยวุฒิ และ**ทรง**ถูกนำเข้ามาต่อ**พระพักตร์**ของพระองค์`
- KD: "כְּבַר אֱנָשׁ → 'บุตรมนุษย์' (รูปคำตำแหน่ง ไม่มี 'ของ' ตาม son_of_man_disambiguation ซึ่งระบุว่า ดนล 7:13 เป็นต้นกำเนิดของตำแหน่งนี้)" and "บุตรมนุษย์ได้รับราชาศัพท์เบา ๆ (เสด็จมา/ทรง) ในฐานะผู้ครองนิรันดร์ที่ได้รับมอบอำนาจ"
- 7:14 then gives him `อำนาจการปกครอง พระเกียรติ และราชอาณาจักร` — everlasting dominion. The lexical title `บุตรมนุษย์` is the locked NT "Son of Man" surface; the generic-human sense is kept distinct (8:17, Daniel himself, → `บุตรแห่งมนุษย์` *with* `แห่ง`).

**10:5–6 — the "man clothed in linen" is kept plain, ambiguity preserved:**
- DAN 10:5–6 HEB: `אִישׁ־אֶחָד לָבוּשׁ בַּדִּים … גְּוִיָּתוֹ כְתַרְשִׁישׁ וּפָנָיו כְּמַרְאֵה בָרָק` → TH: `มีชายผู้หนึ่งสวมเสื้อผ้าป่าน กายดุจพลอยทารชิช ใบหน้าดุจสายฟ้าแลบ` — theophanic *imagery* but **no `ทรง`**.
- Note: "สงวนความกำกวมไว้ ไม่ระบุชัดว่าเป็นพระเจ้าหรือทูตสวรรค์ … บางธรรมเนียมอ่านว่าเป็นพระคริสต์ก่อนทรงรับสภาพมนุษย์ บางธรรมเนียมว่าเป็นทูตสวรรค์ชั้นสูง — ฉบับนี้คงความกำกวมไว้."

**Two questions:**
1. Is it sound to give the Danielic "one like a son of man" (7:13–14) light divine/royal register (`เสด็จ`/`ทรง`/`พระพักตร์`) — effectively reading the figure as the divine Messiah the Christian canon identifies — while keeping the equally-glorious "man clothed in linen" (10:5–6) in plain register to preserve the christophany-vs-angelophany ambiguity? Is the enthronement + everlasting-dominion of 7:14 sufficient warrant for the asymmetry, or should both figures be treated the same way?
2. The title `บุตรมนุษย์` (the NT "Son of Man" surface) is applied to the 7:13 figure, while Daniel-as-human at 8:17 gets the distinct `บุตรแห่งมนุษย์`. Is that lexical disambiguation the right way to mark "this is the messianic title, that is the generic 'mortal'" in Thai?

---

## Item C — The seventy weeks: מָשִׁיחַ rendered generically as "ผู้ถูกเจิม" (anointed one), not "พระเมสสิยาห์/พระคริสต์"

**The pattern:** Daniel 9:24–27 (the "seventy weeks") is the most contested messianic prophecy in the OT. Eremos renders `מָשִׁיחַ` with the **generic** Thai `ผู้ถูกเจิม` ("one who is anointed"), not the messianic title `พระเมสสิยาห์` / `พระคริสต์`, and the notes acknowledge but do not endorse the christological reading.

- DAN 9:25 HEB: `עַד־מָשִׁיחַ נָגִיד` → TH: `จนถึง**ผู้ถูกเจิม**ผู้เป็นเจ้านาย` (KD: "מָשִׁיחַ 'ผู้ถูกเจิม' → 'ผู้ถูกเจิม' ตามตัวอักษร; ธรรมเนียมคริสต์อ่านว่าหมายถึงพระเมสสิยาห์/พระคริสต์ ดูหมายเหตุ")
- DAN 9:26 HEB: `יִכָּרֵת מָשִׁיחַ וְאֵין לוֹ` → TH: `**ผู้ถูกเจิม**จะถูกตัดขาดและจะไม่มีอะไรเหลือ` (note: "ธรรมเนียมคริสต์อ่านว่าหมายถึงการสิ้นพระชนม์ของพระคริสต์")

This matches the project's RULES §0 stance that the verse *surface* follows the Hebrew while the *notes* describe rather than pastorally endorse a tradition's reading (the same descriptive stance used at JHN 1:34). But it is the verse a Thai evangelical reader will check first, and the project elsewhere (Item B, 7:13) does pre-commit a figure toward the divine/messianic reading via register.

**Question:** For an evangelical-Protestant CC0 Thai Bible, is the generic `ผู้ถูกเจิม` (with a note acknowledging-but-not-endorsing the christological reading) the right call for `מָשִׁיחַ` in Daniel 9:25–26 — or should the high-visibility messianic crux use `พระเมสสิยาห์`/`พระคริสต์`, or carry a fuller reader-facing note? Is the project being consistently descriptive (vs. the more committal register given the 7:13 Son-of-Man figure)?

---

## Item D — The Greek-version Additions to Daniel (Prayer of Azariah / Song of the Three, Susanna, Bel and the Dragon) are excluded with no reader-facing note

**The pattern:** The Greek versions of Daniel (Old Greek and Theodotion) contain three blocks absent from the Masoretic Hebrew/Aramaic text: the **Prayer of Azariah + Song of the Three Young Men** (inserted between MT 3:23 and 3:24, ~67 verses), **Susanna** (Greek ch.13), and **Bel and the Dragon** (Greek ch.14). Catholic and Orthodox Bibles include them; Protestant canons do not. Eremos translates **MT Daniel only** (per RULES §0 and `ot_canon_and_text_base_2026-05.md`), which is correct — but, unlike Esther (which records its parallel "Additions to Esther" exclusion in a single note at Esther 1:1), **Daniel carries no reader-facing note anywhere** documenting the exclusion, not at 1:1 and not at the 3:23/3:24 seam where the Greek inserts the ~67 verses.

- DAN 3:23 → 3:24 in Eremos: the MT narrative runs straight through (the three are thrown in at 3:23; Nebuchadnezzar is astonished at 3:24) with **no annotation** that the Greek tradition inserts the Prayer of Azariah and the Song of the Three (the liturgical *Benedicite*) at exactly this gap.
- Under `mt_vs_lxx_textual_variant_handling_2026-05.md §2.3` this is a separate-recension / canonical-block question, not a per-verse MT variant → a documented "non-gap." But Daniel's additions are *more* reader-visible than Esther's (the Song of the Three is a famous liturgical canticle; Susanna and Bel are complete narratives printed as Daniel 13–14 in Catholic Bibles).

**Question:** Should Daniel carry a single reader-facing disposition note (mirroring Esther 1:1, and/or a Tier-3 footer at the 3:23 seam) stating that Eremos follows the Masoretic text and excludes the Prayer of Azariah/Song of the Three, Susanna, and Bel and the Dragon per RULES §0 — plus a note that the MT base is followed over the Greek (Theodotion/OG) text-form? Or is silent exclusion (with only the central policy doc recording it) sufficient for these well-known additions?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
