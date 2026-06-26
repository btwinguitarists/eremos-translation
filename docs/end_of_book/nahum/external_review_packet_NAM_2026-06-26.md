# Nahum — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-26**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Nahum** (3 chapters, 47 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Nahum 3/3 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Nahum 1:3: the Exodus-34 attribute formula deployed in INVERSION (judgment half only), mirroring Jonah 4:2 over the same city (REVIEW)

**The situation.** Nahum 1:3 opens the book's theophany by reciting the Exodus 34:6–7 divine self-revelation formula — but it keeps **only the judgment half** and drops every mercy clause. Where Exod 34:6–7, Joel 2:13, Jonah 4:2, and Psalms 86/103/145 recite "gracious, compassionate, **slow to anger**, abounding in chesed," Nahum cites "**slow to anger** and great in power" and then immediately the Exod 34:7 reservation, "**will by no means clear the guilty**":

- **HEB (NAM 1:3):** `יְהוָה אֶרֶךְ אַפַּיִם וּגְדָל־כֹּחַ וְנַקֵּה לֹא יְנַקֶּה`
- **BSB:** "The LORD is **slow to anger** and great in power; the LORD **will by no means leave the guilty unpunished**."
- **TH (Nahum):** `องค์พระผู้เป็นเจ้า**ทรงกริ้วช้า**และทรงฤทธิ์อำนาจยิ่งใหญ่ และองค์พระผู้เป็นเจ้าจะไม่ทรงปล่อยให้ผู้กระทำผิดลอยนวลพ้นโทษเลย`
- **The locked lemma (`exod_34_attribute_formula_2026-05`):** `אֶרֶךְ אַפַּיִם` → **`ทรงกริ้วช้า`** — present and matching.

The same formula is recited **for Nineveh's mercy** at Jonah 4:2 (`אֵל־חַנּוּן וְרַחוּם אֶרֶךְ אַפַּיִם וְרַב־חֶסֶד` → `พระเจ้าผู้ทรงพระคุณและทรงพระเมตตา ทรงกริ้วช้า ทรงบริบูรณ์ด้วยความรักมั่นคง`). Nahum, a century later and over the same city, recites it **against** Nineveh's guilt. The two Nineveh books frame the formula as a mercy/judgment diptych.

**The state of the text.** The locked lemma `ทรงกริ้วช้า` is present and `check_key_term_consistency` is clean — there is **no** mechanical issue. Two smaller points sit at the editorial layer:
- The rendered reader `notes` at 1:3 name the Exod-34 echo in the translator-facing `key_decisions` but do **not** surface the **Jonah 4:2** pairing to the reader. The corpus elsewhere footnotes canonical-thread allusions of this weight.
- The illustrative Nahum 1:3 row inside `exod_34_attribute_formula_2026-05` quotes a slightly different free-rendering of the non-formulaic clauses (`…ยิ่งใหญ่ในพระเดช…ไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ`) than the shipped verse (`…ทรงฤทธิ์อำนาจยิ่งใหญ่…ไม่ทรงปล่อยให้ผู้กระทำผิดลอยนวลพ้นโทษ`). The locked lemma is unaffected; only the example-row wants syncing.

**Two questions:**
1. When a prophet recites the Exodus-34 attribute formula in **deliberate inversion** — keeping only `אֶרֶךְ אַפַּיִם` ("slow to anger") plus the `וְנַקֵּה לֹא יְנַקֶּה` reservation, and dropping the mercy clauses — should the Thai keep the **locked formula lemma** (`ทรงกริ้วช้า`) so the reader hears the Sinai echo through the inversion (current state), or render it freshly to foreground that this is *judgment*, not the familiar mercy-recitation?
2. Given that Jonah 4:2 cites the **mercy** half of the same formula over the **same city** (Nineveh), should Nahum 1:3 carry a reader-facing cross-reference footnote (Jonah 4:2 / Exod 34:6–7) marking the mercy/judgment frame, or is the translator-facing `key_decisions` note sufficient?

---

## Item B — Nahum 2:14 & 3:5: the divine challenge-formula הִנְנִי אֵלַיִךְ "Behold, I am against you" → `เราเป็นปฏิปักษ์กับเจ้า` (REVIEW)

**The situation.** Both of Nahum's verdict-oracles open with the fixed prophetic challenge-formula `הִנְנִי אֵלַיִךְ` "Behold, I am against you," spoken by YHWH-Sabaoth, and both are rendered identically:

- **HEB (NAM 2:14):** `הִנְנִי אֵלַיִךְ נְאֻם יְהוָה צְבָאוֹת`
- **HEB (NAM 3:5):** `הִנְנִי אֵלַיִךְ נְאֻם יְהוָה צְבָאוֹת`
- **BSB:** "'Behold, **I am against you**,' declares the LORD of Hosts."
- **TH (both):** `**องค์พระผู้เป็นเจ้าจอมโยธา**ตรัสว่า ดูเถิด **เราเป็นปฏิปักษ์กับเจ้า**`

`เราเป็นปฏิปักษ์กับเจ้า` is the **dominant corpus rendering** of this formula — it also carries `הִנְנִי אֵל־` at **Ezekiel 38–39** (against Gog) and **Jeremiah 50–51** (against Babylon). A **second** Thai form, `เราต่อสู้กับเจ้า`, exists but is confined to a **single Jeremiah file** (and may translate a different underlying construction such as `נִלְחַם בְּ־` "I will fight against," rather than the `הִנְנִי אֵל־` formula).

**Why it's surfaced.** Nahum's rendering is principled and internally consistent (both occurrences identical) and aligns with the majority Ezekiel/Jeremiah oracular use. But `הִנְנִי אֵל־` is a recurring prophetic-oracle leitwort that is **not yet covered by any translator-decisions doc** (`leitwort_handling_policy_2026-05` does not name it), so the existence of a second corpus form is undocumented.

**Question:**
For the fixed prophetic challenge-formula `הִנְנִי אֵל־` "Behold, I am against you" (Nah 2:14, 3:5; Ezk 38–39; Jer 50–51), is **`เราเป็นปฏิปักษ์กับเจ้า`** the right single locked rendering corpus-wide — distinct from the `เราต่อสู้กับเจ้า` "I will fight against you" form that should be reserved for `נִלְחַם בְּ־` — and is the formula worth documenting as a leitwort so the remaining prophets (and the doom-oracle sections of Ezekiel) render it uniformly?

---

## Item C — Nahum 1:1 ↔ 3:7: the prophet's name "Nahum = comfort" (נַחַם) and the book's central wordplay, glossed at the head but not surfaced at its payoff (REVIEW)

**The situation.** The prophet's name נַחוּם means "comfort/consolation" (root `נָחַם`), glossed at 1:1, and the book turns that name into a structural irony that lands at 3:7 — the same root, negated:

- **1:1 `notes`:** `นาฮูม (‘การปลอบโยน’) ชาวเมืองเอลโขช…` — "Nahum ('comfort')…"
- **1:12 (comfort embodied, to Judah):** `וְעִנִּתִךְ לֹא אֲעַנֵּךְ עוֹד` "though I afflicted you, I will afflict you **no more**" → `แม้เราได้ให้เจ้าทุกข์ใจมาแล้ว เราก็จะไม่ให้เจ้าทุกข์ใจอีกต่อไป`
- **3:7 (the payoff — no comforter, to Nineveh):** `מֵאַיִן אֲבַקֵּשׁ **מְנַחֲמִים** לָךְ` "from where shall I seek **comforters** for you?" → `เราจะหา**ผู้ปลอบโยน**เจ้าได้จากที่ไหน`

The prophet *named* "Comfort" announces that for Nineveh there is **no comforter** — while comfort flows to Judah (1:12). The 3:7 line is also the deliberate **dark inverse** of the Lamentations refrain `אֵין מְנַחֵם` "she has no comforter" (Lam 1): there, Zion has no comforter *under* judgment; here, Nineveh's lack of one *is* the oppressed nations' comfort.

**Why it's surfaced.** The wordplay is the book's theological hinge, but it is **invisible to a non-Hebrew reader**: the name "Nahum," the phrase "afflict you no more," and "no comforters" share a root that the Thai surface cannot show. It is glossed only at 1:1, with no footnote tying the name to 3:7, and `proper_noun_wordplay_2026-05` has **no Nahum entry**. (The text does not, and should not, force the pun into the rendered verse — the question is purely about apparatus.)

**Two questions:**
1. For a book whose **title-character's name** carries the central pun (Nahum = "comfort," landing on `מְנַחֲמִים` "comforters" negated at 3:7), should the Thai apparatus add a `wordplay_note` at 3:7 cross-referencing the 1:1 name-gloss — so the reader sees that "Nahum," "no more affliction" (1:12), and "no comforters" (3:7) are the same root — or is the single 1:1 gloss adequate?
2. Should that note also flag the **inverse relationship to Lamentations** (`אֵין מְנַחֵם` "no comforter" for Zion vs `מְנַחֲמִים` "no comforters" for Nineveh), given the corpus already tracks the Lamentations "no-comforter" refrain — or would that cross-book link over-load a reader footnote?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
