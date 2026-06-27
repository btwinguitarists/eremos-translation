# Haggai — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-27**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Haggai** (2 chapters, 38 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Haggai 2/2 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Haggai 2:7: "the treasures of all nations" (collective חֶמְדַּת) vs. the Christological "Desire of Nations" (single figure) — the book's signature crux (DECIDE)

**The situation.** Haggai 2:7 is the book's signature interpretive fork and one of the most famous Christological cruxes in the Old Testament. The Eremos text reads the **collective-treasure** sense and footnotes the singular-messianic reading:

- **HEB (HAG 2:7):** `וְהִרְעַשְׁתִּי אֶת־כָּל־הַגּוֹיִם וּבָאוּ חֶמְדַּת כָּל־הַגּוֹיִם וּמִלֵּאתִי אֶת־הַבַּיִת הַזֶּה כָּבוֹד`
- **BSB:** "I will shake all the nations, and **they will come with all their treasures**, and I will fill this house with glory…"
- **TH (Haggai):** `เราจะเขย่าประชาชาติทั้งปวง และ**สิ่งล้ำค่าของประชาชาติทั้งหลายจะหลั่งไหลเข้ามา** และเราจะให้พระนิเวศนี้เต็มไปด้วยพระสิริ`
- **Footnoted variant:** the Vulgate (*veniet desideratus cunctis gentibus*) and KJV ("the **desire** of all nations shall come") read חֶמְדַּת as a single **Desired-One** — a messianic figure (Advent hymnody: "Come, Thou long-expected Jesus… Dear Desire of every nation").

**The reasoning behind the rendering.**
- The singular construct noun חֶמְדַּת "desire / desirable thing of" is taken **collectively** ("the treasures of…") because it governs the **plural** verb וּבָאוּ "they shall come." A plural verb fits a collective object (the nations' treasures streaming into the temple), not a single person — this is the decisive grammatical signal, and the reading BSB, NIV, ESV, and most modern versions adopt.
- The traditional singular-messianic reading ("the Desire of Nations") is **disclosed in the footnote** (`output/textual_variants/haggai_02.json`, v.7 `nt_citation_note`), not retrofitted into the body — consistent with the project's committal-messianic-surface restraint (a messianic figure is not surfaced as bare fact in the OT body).
- The same verse's opening (`I will shake the heavens…`, v.6) is quoted in **Hebrews 12:26**, and that NT link is footnoted at the same node.

**Why it's surfaced (the corpus-level decision it bears on).** The MT is itself in **grammatical tension** — singular construct noun against a plural verb — which is exactly why the versions split; this is a genuine lexical-grammatical fork, not a settled reading the project is merely disclosing. And it is among the highest-visibility Christological verses in the OT (Handel's *Messiah*, centuries of Advent devotion), so shipping the collective reading is irreversible-once-public. Corpus precedent treats the parallel as a Ben-decision: **Joel 2:23** (the rain-vs-messianic-Teacher fork, הַמּוֹרֶה לִצְדָקָה) was flagged DECIDE and ratified with the natural sense in the body and the messianic sense footnoted, precedent-setting for the Twelve. Haggai 2:7 is the same shape and warrants the same explicit ratification before the v1 tag.

**Question:**
At Haggai 2:7 — should the Eremos body read the **collective** "**the treasures of all nations** will come" (`สิ่งล้ำค่าของประชาชาติทั้งหลายจะหลั่งไหลเข้ามา`, keyed to the plural verb וּבָאוּ), with the traditional singular-messianic "**Desire of Nations**" reading footnoted — consistent with the project's MT-base + messianic-restraint discipline and with the Joel 2:23 precedent? Or does the devotional weight and long Christological tradition of "the Desire of Nations" warrant elevating the singular-messianic reading (e.g. into the body with the collective sense footnoted, or a fuller side-by-side note)?

---

## Item B — Haggai's messianic-reception surface: "latter glory" (2:9) and the Zerubbabel signet ring (2:23) — the densest reception case in the Twelve (REVIEW)

**The situation.** Beyond the 2:7 crux, Haggai carries two further texts with a strong Christian-reception reading. Both are framed in the summaries/footnotes as **reception** (what Christians see / the NT genealogy), not asserted as bare fact:

- **HAG 2:9** — `גָּדוֹל יִהְיֶה כְּבוֹד הַבַּיִת הַזֶּה הָאַחֲרוֹן מִן־הָרִאשׁוֹן` "the latter glory of this house will be greater than the former."
  - **TH body:** `พระสิริยุคหลังของพระนิเวศนี้จะยิ่งใหญ่กว่าพระสิริยุคก่อน`
  - **TH summary/footnote (reception-framed):** `คำพยากรณ์ที่**คริสตชนเห็นว่า**สำเร็จเมื่อพระเมสสิยาห์เสด็จเข้าสู่พระวิหารนี้` ("a prophecy that **Christians see as** fulfilled when the Messiah entered this temple").
- **HAG 2:23** — `וְשַׂמְתִּיךָ כַּחוֹתָם כִּי־בְךָ בָחַרְתִּי` "I will make you like my signet ring, for I have chosen you."
  - **TH body:** `เราจะทำให้เจ้าเป็นเหมือนแหวนตราของเรา เพราะเราได้เลือกเจ้าไว้แล้ว`
  - **TH summary/footnote:** notes the **reversal of Jer 22:24** (Jehoiachin plucked off "like a signet ring") and that Zerubbabel `ปรากฏในลำดับพงศ์ของพระเมสสิยาห์ (มัทธิว 1:12)` ("appears in the Messiah's genealogy, Matt 1:12") — a genealogical note, not a claim that Zerubbabel *is* the Messiah.

**The reasoning behind the rendering.**
- Both readings are surfaced at the **reception** altitude: explicitly attributed to Christian interpretation (`คริสตชนเห็นว่า`) or to the NT genealogy (Matt 1:12), never as a bare `คือพระคริสต์` ("is the Christ") assertion in the body.
- This holds the committal-messianic-surface discipline ratified at the Isaiah audit (§0) and deliberately avoids the regression the Ezekiel audit flagged (§14), where multiple summaries asserted `คือพระคริสต์` as plain fact.

**Why it's surfaced.** Nothing here is mechanically wrong — the framing is correct and footnoted. It is flagged for a deliberate confirmation because **Haggai is the densest messianic-reception book in the Twelve to date** (three messianic footnotes — 2:7, 2:9, 2:23 — in a two-chapter book), so it is the strongest single test of where the reception/assertion line sits. Having Ben's explicit ratification that the reception-framing **level** is the intended Eremos surface — neither flattening it to bare assertion nor stripping the Christian reading from the apparatus — is worth recording before the v1 tag.

**Question:**
Across Haggai's messianic-reception texts (2:9 "latter glory" → Messiah entering the temple; 2:23 signet ring → Davidic line / Matt 1:12 genealogy) — is the current **reception-framing level** (`คริสตชนเห็นว่า…` / NT-genealogy footnote, with the OT body left as a plain statement about Zerubbabel and the temple) the intended Eremos surface? Or should any of these be brought further forward (a stronger in-body messianic surface) or pulled further back (less Christian-reception apparatus) for consistency across the corpus?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
