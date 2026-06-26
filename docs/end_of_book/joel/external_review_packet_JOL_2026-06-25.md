# Joel — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-25**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Joel** (4 chapters, 73 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Joel 4/4 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — 2:23 הַמּוֹרֶה לִצְדָקָה: "early rain" vs the messianic "Teacher of Righteousness" (DECIDE)

**The crux.** Joel 2:23 contains the book's one genuine interpretive fork. The Hebrew word מוֹרֶה (môreh) is a true double-entendre meaning **both** "early/autumn rain" **and** "teacher," so the phrase הַמּוֹרֶה לִצְדָקָה reads either *"the early rain for vindication/righteousness"* or *"the Teacher of Righteousness."*

- **HEB:** `כִּי־נָתַן לָכֶם אֶת־הַמּוֹרֶה לִצְדָקָה וַיּוֹרֶד לָכֶם גֶּשֶׁם מוֹרֶה וּמַלְקוֹשׁ`
- **BSB:** "for He has given you the autumn rains for your vindication. He sends you showers, both autumn and spring rains, as before."
- **TH (Eremos, rain reading):** `เพราะพระองค์ประทาน**ฝนต้นฤดู**ให้แก่พวกเจ้า**ด้วยความชอบธรรม** พระองค์ทรงเทฝนลงมาให้พวกเจ้าอย่างบริบูรณ์ ทั้ง**ฝนต้นฤดูและฝนปลายฤดู**เหมือนแต่ก่อน`

**The decision made.** Eremos follows the **rain reading**, anchored by the same verse's second half גֶּשֶׁם מוֹרֶה וּמַלְקוֹשׁ ("downpour, early-rain, and latter-rain"), where מוֹרֶה is unambiguously precipitation. The **messianic** reading — the Qumran community's *moreh ṣedeq* ("Teacher of Righteousness") and the later christological gloss — is disclosed in a Tier-2 footnote, not baked into the rendered Thai. This matches the project's ratified policy of translating the plain-sense surface and reserving messianic/typological readings for the apparatus.

**Why it needs ratification.** It is the most contested verse in Joel, it touches messianic surfacing directly, and its disposition sets the precedent for the rest of the Minor Prophets (Amos 9:11; Micah 5; Zechariah). No translation change is proposed — this is a ratification gate.

**Two questions:**
1. For an MT-anchored, plain-sense-surface translation, is following the **"early rain for vindication"** reading (with the messianic "Teacher of Righteousness" reading in a footnote) the right call here — given that the same verse's גֶּשֶׁם מוֹרֶה וּמַלְקוֹשׁ fixes מוֹרֶה in its rain sense — or should the messianic reading be surfaced in the rendered text?
2. Is the footnote's framing of the messianic tradition (Qumran *moreh ṣedeq* + christological reading) accurate and adequately neutral, or should it say more / less?

---

## Item B — Joel 3:1–5 (MT) / 2:28–32 (Eng) → Acts 2:17–21 and Rom 10:13: an NT-cited MT/LXX surface (REVIEW)

**The situation.** Joel's Spirit-outpouring oracle is the longest OT block quoted in the New Testament — Peter preaches the whole of it at Pentecost (Acts 2:17–21), and Paul quotes its climax in Rom 10:13. Eremos translates Joel from the **MT** and Acts/Romans from the **Greek**, so the two Thai surfaces **legitimately differ** at the points where Acts follows the LXX. All three differences below are correct source-driven choices; the question is whether the apparatus should flag them more sharply for a reader who cross-references.

| Point | Joel (MT-based, this book) | Acts 2 / Rom 10 (shipped) |
|---|---|---|
| Order, Joel 3:1 / Acts 2:17 | **คนชรา…จะฝันเห็น** then **คนหนุ่ม…จะเห็นนิมิต** (old men dream → young men visions) | **คนหนุ่ม…จะเห็นนิมิต** then **คนชรา…จะฝันเห็น** (young → old) |
| "all flesh" כָּל־בָּשָׂר / πᾶσαν σάρκα | **มนุษย์ทั้งปวง** | มนุษย์ทุกคน |
| Day-epithet, Joel 3:4 / Acts 2:20 | הַנּוֹרָא "dreadful" → **น่าสะพรึงกลัว** | ἐπιφανῆ "glorious" → **รุ่งโรจน์** |
| "calls on the name… saved" | Joel 3:5: **ทุกคนที่ร้องออกพระนามขององค์พระผู้เป็นเจ้าจะรอด** | Rom 10:13: **…จะรอด** (verbatim); Acts 2:21: **…จะได้รับความรอด** |

The shared idiom **ร้องออกพระนาม…จะรอด** is consistent across all three witnesses (Joel = Rom 10:13 verbatim). The chapter already carries a Layer-2 `nt_citation_note` footnote naming the Acts 2:17–21 and Rom 10:13 citations.

**The precedent in play.** The Jeremiah audit flagged the **31:32 → Heb 8:9** MT/LXX divergence as owing a reader-facing Tier-2 footer. The sharpest Joel case is **2:31/3:4 "dreadful" (MT) vs "glorious" (Acts)** — a substantive tonal difference on a marquee verse.

**Two questions:**
1. Confirm the policy: each text is translated from its own base (MT for Joel, Greek for Acts/Romans), the NT citation is disclosed in a footnote, and the OT surface is **not** harmonized to the NT quotation. Is that the intended handling?
2. Does the **2:31 "dreadful"/"glorious" (נוֹרָא / ἐπιφανῆ)** divergence — and/or the old-men/young-men order swap — warrant its own reader-facing Tier-2 footer (modeled on the Jeremiah 31:32 → Heb 8:9 case), or is the existing combined `nt_citation_note` sufficient?

---

## Item C — יוֹם יְהוָה "Day of the LORD" leitwort: rendering + corpus-doc lift (STABLE; confirm)

**The pattern.** The "Day of the LORD" is Joel's controlling theme and the verse-cluster the rest of the Twelve and the NT build on. It is rendered **uniformly** as **วันแห่งองค์พระผู้เป็นเจ้า** across all five occurrences, matching the `glossary.json` ἡμέρα κυρίου corpus entry (so the already-shipped Acts 2:20, 1 Thess 5:2, and 2 Pet 3:10 read the same form):

- **1:15** `כִּי קָרוֹב יוֹם יְהוָה` → **เพราะวันแห่งองค์พระผู้เป็นเจ้าใกล้เข้ามาแล้ว**
- **2:1** `כִּי־בָא יוֹם־יְהוָה כִּי קָרוֹב` → **เพราะวันแห่งองค์พระผู้เป็นเจ้ากำลังมาถึง วันนั้นใกล้เข้ามาแล้ว**
- **2:11** `כִּי־גָדוֹל יוֹם־יְהוָה וְנוֹרָא מְאֹד` → **เพราะวันแห่งองค์พระผู้เป็นเจ้านั้นยิ่งใหญ่และน่าสะพรึงกลัวยิ่งนัก**
- **3:4 (Eng 2:31)** `יוֹם יְהוָה הַגָּדוֹל וְהַנּוֹרָא` → **วันแห่งองค์พระผู้เป็นเจ้าอันยิ่งใหญ่และน่าสะพรึงกลัว**
- **4:14 (Eng 3:14)** `כִּי קָרוֹב יוֹם יְהוָה בְּעֵמֶק הֶחָרוּץ` → **เพราะวันแห่งองค์พระผู้เป็นเจ้าใกล้เข้ามาแล้วในหุบเขาแห่งการตัดสิน**

The rendering is uniform and correct; it simply has **no `docs/translator_decisions/` doc** — only a glossary entry and per-verse notes. This is the project's single most cross-book-load-bearing prophetic phrase.

**Question:** Is **วันแห่งองค์พระผู้เป็นเจ้า** the right permanent rendering of יוֹם יְהוָה / ἡμέρα κυρίου across both Testaments, and should it be lifted into a corpus doc (`day_of_the_lord_leitwort_2026-06.md`) — consolidating the rendering, the anarthrous-technical rationale, and the OT↔NT consistency — to govern Amos, Obadiah, Zephaniah, and Malachi as they ship?

---

## Item D — The four-locust lexicon (1:4 / 2:25): four species or four stages? (STABLE; confirm)

**The pattern.** Joel names four Hebrew locust-words. Eremos maps each to a fixed Thai term and holds the 1:1 map across both occurrences (1:4 and 2:25), even though the Hebrew lists them in different order:

| Hebrew | Thai | sense rendered |
|---|---|---|
| גָּזָם gāzām | **ตั๊กแตนตัด** | "cutting/shearing locust" |
| אַרְבֶּה ʾarbeh | **ตั๊กแตนฝูง** | "swarming locust" (the Exod-10 plague word) |
| יֶלֶק yeleq | **ตั๊กแตนวัยกระโดด** | "hopping/young locust" |
| חָסִיל ḥāsîl | **ตั๊กแตนทำลาย** | "destroying locust" |

- **Joel 1:4:** `יֶתֶר הַגָּזָם אָכַל הָאַרְבֶּה …` → `สิ่งที่**ตั๊กแตนตัด**เหลือไว้ **ตั๊กแตนฝูง**ก็กินจนหมด … **ตั๊กแตนวัยกระโดด** … **ตั๊กแตนทำลาย**ก็กินจนหมด`
- **Joel 2:25:** `הָאַרְבֶּה הַיֶּלֶק וְהֶחָסִיל וְהַגָּזָם` → `**ตั๊กแตนฝูง ตั๊กแตนวัยกระโดด ตั๊กแตนทำลาย** และ**ตั๊กแตนตัด**`

The footnote at 1:4 discloses that scholars disagree whether these are four species or four growth-stages of one species, and notes that אַרְבֶּה is the same word as the eighth Egyptian plague (Exod 10). The 1:1 lemma→term mapping makes the 2:25 restoration ("I will repay the years the locusts ate") echo the 1:4 devastation word-for-word.

**Question:** Is rendering the four locust-words as **four distinct named kinds** (ตัด / ฝูง / วัยกระโดด / ทำลาย) — rather than collapsing them to a single "locusts/swarms" or using descriptive growth-stage glosses — the right approach for keeping the 1:4 ↔ 2:25 cascade intact, and is the four-term Thai set natural to a Thai ear? Should the map be lifted to a corpus note so Nahum 3:15–17 (אַרְבֶּה / יֶלֶק) inherits it?

---

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
