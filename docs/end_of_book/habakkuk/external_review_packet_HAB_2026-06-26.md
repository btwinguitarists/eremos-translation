# Habakkuk — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-26**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Habakkuk** (3 chapters, 56 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Habakkuk 3/3 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Habakkuk 2:4: "the righteous shall live by his faith" (אֱמוּנָה) → `ความเชื่ออันมั่นคง` "steadfast faith" — the corpus's most NT-cited OT verse (DECIDE)

**The situation.** Habakkuk 2:4b is the theological heart of the book and the single most NT-cited OT verse in the corpus — quoted at Romans 1:17, Galatians 3:11, and Hebrews 10:38, and the textual cornerstone of the Reformation. The Eremos text translates the **MT** and discloses the NT/LXX reception in a footnote:

- **HEB (HAB 2:4b):** `וְצַדִּיק בֶּאֱמוּנָתוֹ יִחְיֶה`
- **BSB:** "but the righteous will live by **his faith**"
- **TH (Habakkuk):** `ส่วนคนชอบธรรมจะดำรงชีวิตอยู่ด้วย**ความเชื่ออันมั่นคง**ของเขา` ("…will live by **his steadfast faith**")
- **LXX (the form the NT cites):** `ὁ δίκαιος ἐκ πίστεώς [μου] ζήσεται` — renders אֱמוּנָה as πίστις and, in the Pauline quotation, **drops the possessive suffix** ("the righteous shall live **by faith**").

**The reasoning behind the rendering.**
- אֱמוּנָה holds two senses — "faithfulness / steadfastness" (covenant loyalty) and "faith / trust." `ความเชื่ออันมั่นคง` ("steadfast/firm faith") was chosen to carry **both**: the firmness of the root *and* the trust dimension.
- The MT suffix בֶּאֱמוּנָתוֹ = "by **his** [own] faithfulness" — the righteous person's steadfast trust, **not** God's faithfulness. The Thai preserves the possessive (`…ของเขา`). This is the correct MT reading per RULES §0 (OT base = MT).
- The footnote (`habakkuk_02.json` v4) discloses the MT/LXX/NT divergence: the NT reads the verse "in the dimension of justifying faith," the MT context "emphasizes living with steadfast faithfulness amid crisis," and notes the verse's three NT citations.

**Why it's surfaced (the corpus-level *whether*).** Every mechanical and verse-level box is checked — the issue is cross-testament consistency. A Thai reader who cross-references Habakkuk 2:4 against its three NT citations (rendered in the Eremos NT) will read **`ความเชื่ออันมั่นคง`** ("steadfast faith") in the OT and **`โดยความเชื่อ`** (plain "by faith") in the NT. This is the kind of forward-compounding editorial choice (cf. the MAT 18 ἐκκλησία precedent that motivated the end-of-book checklist) that should be ratified deliberately before the book is locked.

The 2:3 verse forms a citation cluster with 2:4: Hebrews 10:37–38 quotes them together. Habakkuk 2:3 (`כִּי בֹא יָבֹא לֹא יְאַחֵר`) is likewise translated on the **MT** (an impersonal subject — the *vision* will come, `เพราะมันจะมาถึงอย่างแน่นอน และจะไม่ชักช้า`), with the LXX personal-subject reading ("the coming one will come," the form Heb 10:37 cites toward Christ) recorded in the footnote, not retrofitted into the body.

**Two questions:**
1. For Habakkuk 2:4 — the corpus's landmark OT→NT bridge verse — is **`ความเชื่ออันมั่นคง`** ("steadfast faith," carrying both the faithfulness and trust senses of אֱמוּנָה, faithful to the MT possessive) the right rendering even though it differs visually from the plain **`โดยความเชื่อ`** that the three NT citations (Rom 1:17; Gal 3:11; Heb 10:38) use — or should the OT verse be rendered with the plainer `ความเชื่อ` so the four occurrences read uniformly across the testaments?
2. Is the project's MT-in-the-body / NT-reception-in-the-footnote discipline (applied here to both 2:3's LXX personalization → Heb 10:37 and 2:4's possessive → the suffix-dropping NT citation) the right policy for a verse of this theological prominence, or does this pericope warrant a heavier reader-facing apparatus that lays the MT and NT readings side by side?

---

## Item B — Habakkuk 3:19: the lone Adonai-YHWH compound (`יְהוִה אֲדֹנָי`) at the closing colophon → bare `องค์พระผู้เป็นเจ้า` (REVIEW)

**The situation.** Habakkuk's single Adonai-YHWH compound closes the book, in the reversed word order (YHWH-vocalized-as-Elohim *then* Adonai — the form standard in the Psalter colophons, e.g. Ps 68:21, 109:21, 140:8, 141:8), and is rendered as the **single bare title**:

- **HEB (HAB 3:19):** `יְהוִה אֲדֹנָי חֵילִי`
- **BSB:** "**GOD the Lord** is my strength"
- **TH (Habakkuk):** `**องค์พระผู้เป็นเจ้า**ทรงเป็นกำลังของข้าพเจ้า`
- **Lock (`divine_names_table_2026-05` line 22):** אֲדֹנָי יְהוִה (Adonai-YHWH; "Lord GOD") → **`องค์พระผู้เป็นเจ้า`** — "Compound collapses to single Thai rendering; `key_decisions` records the underlying Adonai-YHWH compound." The `key_decisions` at 3:19 does exactly this.

**Why it's surfaced.** This is a clean witness for the **bare-rendering path of the still-open Amos §1 question**. Amos surfaced the *same family* of compound (its word order אֲדֹנָי יְהוִה) rendered as the **expanded** `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` (20×/19 in Amos, anomalous against the rest of the corpus). Habakkuk — like Obadiah (1:1) and Micah (1:2) before it — renders the compound **bare**, the form Ezekiel (217×), Isaiah, and Jeremiah all use. Habakkuk 3:19 thus votes **path-a (normalize to bare)**. The English versions mark the distinction typographically ("GOD the Lord" / "Lord GOD" with small-caps); Thai script cannot render small-caps, so the project collapses the compound and records it in the footnote/`key_decisions`.

**Question:**
At the climactic colophon of Habakkuk — "**GOD the Lord** is my strength" (`יְהוִה אֲדֹנָי חֵילִי`) — is the bare collapse to a single **`องค์พระผู้เป็นเจ้า`** (with the compound recorded in the footnote) the right rendering, even though the doubled Hebrew title arguably carries extra solemnity at the book's resolution? More broadly: should the Adonai-YHWH compound (both word orders — אֲדֹנָי יְהוִה and the reversed יְהוִה אֲדֹנָי) collapse uniformly to bare `องค์พระผู้เป็นเจ้า` corpus-wide (the Ezekiel/Isaiah/Jeremiah/Obadiah/Micah/Habakkuk practice), or should it carry a distinguishing expansion at any point (the Amos practice)?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
