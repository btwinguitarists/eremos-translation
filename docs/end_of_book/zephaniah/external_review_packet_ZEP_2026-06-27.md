# Zephaniah — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-27**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Zephaniah** (3 chapters, 53 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Zephaniah 3/3 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Zephaniah 1:7: the Adonai-YHWH compound (`אֲדֹנָי יְהוִה`) → bare `องค์พระผู้เป็นเจ้า` — the strongest witness for the open Amos question (REVIEW)

**The situation.** Zephaniah's single Adonai-YHWH compound opens the Day-of-YHWH oracle and is rendered as the **single bare title**:

- **HEB (ZEP 1:7):** `הַס מִפְּנֵי אֲדֹנָי יְהוִה כִּי קָרוֹב יוֹם יְהוָה`
- **BSB:** "Be silent in the presence of the **Lord GOD**, for the Day of the LORD is near."
- **TH (Zephaniah):** `จงเงียบสงบต่อหน้า**องค์พระผู้เป็นเจ้า** เพราะวันแห่งองค์พระผู้เป็นเจ้าใกล้เข้ามาแล้ว`
- **Lock (`divine_names_table_2026-05`):** אֲדֹנָי יְהוִה ("Lord GOD") → **`องค์พระผู้เป็นเจ้า`** — "Compound collapses to a single Thai rendering; `key_decisions` records the underlying Adonai-YHWH compound." The `key_decisions` at 1:7 does exactly this.

**Why it's surfaced (the corpus-level decision it bears on).** Zephaniah 1:7 is the **cleanest possible witness** for the still-open Amos §1 question — and it removes the one hedge that softened the earlier witnesses. The Amos audit surfaced this *exact* Hebrew string, אֲדֹנָי יְהוִה (Adonai first, then YHWH-vocalized-as-Elohim), rendered as the **expanded** `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` (20×/19 in Amos, anomalous against the entire rest of the corpus). Zephaniah renders **the identical string bare** — the form Ezekiel (217×), Isaiah (30×), Jeremiah, Obadiah (1:1), Micah (1:2), and Habakkuk (3:19) all use.

This matters because the two prior minor-prophet witnesses carried a caveat: Obadiah and Micah have the compound *standalone* (not the full pair at issue), and Habakkuk 3:19 has it in the **reversed** word order (`יְהוִה אֲדֹנָי`, the Psalter-colophon form). Zephaniah 1:7 has the **same word order as Amos** — so it is a direct apples-to-apples counter-example: the same Hebrew, the same kind of oracular context, rendered bare instead of expanded. Zephaniah thus votes **path-a (normalize the whole corpus to bare)** with no asterisk.

The English versions mark "Lord GOD" with small-caps typography; Thai script cannot render small-caps, so the project collapses the compound and records the underlying form in the footnote/`key_decisions`.

**Question:**
At Zephaniah 1:7 — "Be silent in the presence of the **Lord GOD**" (`הַס מִפְּנֵי אֲדֹנָי יְהוִה`) — is the bare collapse to a single **`องค์พระผู้เป็นเจ้า`** (with the compound recorded in the footnote) the right rendering? And given that this is the **same Hebrew word order** that Amos rendered as the expanded `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย`, should the Adonai-YHWH compound collapse uniformly to bare `องค์พระผู้เป็นเจ้า` across the whole corpus (the Ezekiel/Isaiah/Jeremiah/Obadiah/Micah/Habakkuk/Zephaniah practice), or should it carry a distinguishing expansion anywhere (the Amos practice)?

---

## Item B — Zephaniah 3:17: "he will quiet you in his love" (MT `יַחֲרִישׁ`) vs the LXX "he will renew you in his love" — a landmark verse on a one-consonant fork (REVIEW)

**The situation.** Zephaniah 3:17 is the book's tender climax and one of the best-loved verses in the Twelve. The Eremos text follows the **MT** and footnotes the famous variant:

- **HEB (ZEP 3:17, MT):** `יְהוָה אֱלֹהַיִךְ בְּקִרְבֵּךְ גִּבּוֹר יוֹשִׁיעַ יָשִׂישׂ עָלַיִךְ בְּשִׂמְחָה **יַחֲרִישׁ** בְּאַהֲבָתוֹ יָגִיל עָלַיִךְ בְּרִנָּה`
- **BSB:** "…He will **quiet you** by His love; He will rejoice over you with singing."
- **TH (Zephaniah):** `…จะ**ทรงให้เจ้าสงบนิ่ง**ด้วยความรักของพระองค์ จะทรงโห่ร้องด้วยความชื่นบานเพราะเจ้า`
- **LXX variant (footnoted):** the LXX read `יְחַדֵּשׁ` "he will **renew** you in his love" (καινιεῖ σε ἐν τῇ ἀγαπήσει αὐτοῦ) — a single-consonant difference (ר/ד) producing a quite different devotional image.

**The reasoning behind the rendering.**
- The MT `יַחֲרִישׁ` ("he will be silent / grow quiet [you]") is followed per RULES §0 (OT base = MT). The Thai `ทรงให้เจ้าสงบนิ่ง` renders the causative/transitive sense ("he will quiet *you*"), the reading BSB and most English versions adopt.
- The LXX `יְחַדֵּשׁ` "renew" — the reading behind many modern worship settings and some translations — is disclosed in the footnote (`textual_variants/zephaniah_03.json`), not retrofitted into the body.
- Third-person royal register is carried throughout the verse (`ทรงเปรมปรีดิ์`, `ทรงให้…สงบนิ่ง`, `ทรงโห่ร้อง`), consistent with the in-your-midst kingship texts of 3:5/3:15.

**Why it's surfaced.** Nothing here is mechanically wrong — the MT is followed and the variant is footnoted, exactly the project's standard discipline. It is flagged for a deliberate confirmation because 3:17 is a high-visibility, frequently-quoted verse where the MT/LXX fork yields two materially different images of God ("God grows quiet in his love" vs. "God renews you in his love"), and having Ben's explicit ratification of the MT image on record before the v1 tag is worth the line.

**Question:**
At Zephaniah 3:17 — the book's emotional climax — should the Eremos surface read the **MT** `ทรงให้เจ้าสงบนิ่งด้วยความรัก` ("he will **quiet** you in his love," with the LXX "renew" footnoted), consistent with the project's MT-base rule, or does the popularity and devotional weight of the LXX "**renew**" reading warrant elevating it (e.g. to the body with the MT footnoted, or a fuller side-by-side note)?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
