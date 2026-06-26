# Hosea — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-25**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Hosea** (14 chapters, 197 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Hosea 14/14 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Divine anthropomorphism: the codified first-person-plain rule + the face-exception (DECIDE)

**The corpus lock:** `divine_anthropomorphism_thai_grammar_2026-05.md` binds God's body-parts to royal register (ราชาศัพท์) with **no person-based exception**: hand יָד → **พระหัตถ์**, eyes עֵינַי → **พระเนตร**, face פָּנִים → **พระพักตร์**, heart לֵב → **พระทัย**.

**The Hosea pattern:** first-person divine body-parts systematically drop to **plain** register, and the lapse is written into the `key_decisions` as a deliberate "narrator-vs-speaker" rule — but it is **not internally consistent** (face is kept royal):

| Ref | Hebrew (1st-person divine speech) | Thai | Register | KD note |
|---|---|---|---|---|
| 2:12 | מִיָּדִי "from my hand" | **มือ** | plain | *"rendered plain มือของเรา, not royal พระหัตถ์, per the narrator-vs-speaker distinction"* |
| 11:8 | לִבִּי "my heart" | **ใจ** | plain | *"1st-person divine heart rendered plain ใจ, per the narrator-vs-speaker rule"* |
| 13:14 | מֵעֵינָי "from my eyes" | **สายตา** | plain | (no note) |
| **5:15** | בִּקְשׁוּ פָנָי "seek my face" | **พระพักตร์** | **royal** | *"the worship-approach idiom takes the royal พระพักตร์, as in 2 Chr 7:14"* |

Third-person comparator (correct): 6:2 לְפָנָיו "before him" → royal **ต่อพระพักตร์พระองค์**.

**Cross-book:** this is the identical drift the Isaiah audit (§13, recommended reversal), the Jeremiah audit (§13, codified as a rule), and the Ezekiel audit (§10, codified across ~22 verses) all flagged — **all three still untagged and unreconciled.** Hosea adds a clean new data point: the פָּנִים "face" → royal exception that the rule needs to either absorb or reject.

**Evidence — the emotional summit, 11:8:**
- HEB: `נֶהְפַּךְ עָלַי לִבִּי יַחַד נִכְמְרוּ נִחוּמָי` → TH: `**ใจ**ของเราพลิกผันอยู่ภายในเรา ความเมตตาสงสารของเราก็ถูกจุดให้ร้อนรนขึ้น`
- The most intimate divine self-disclosure in the book renders "my heart" as the plain ใจ, not the royal พระทัย.

**Two questions:**
1. For God speaking in the **first person** about his own body-parts ("my hand," "my heart," "my eyes"), is **plain** Thai register the right call (a deliberate intimacy/self-reference effect), or should these take Rachasap uniformly with third-person divine description (พระหัตถ์ / พระทัย / พระเนตร), as the corpus anthropomorphism lock currently requires with no exception?
2. If a first-person-plain exception is adopted, how should the **5:15 "seek my face" → royal พระพักตร์** case be reconciled — is "face" a principled carve-out (a fixed worship-approach idiom), or an inconsistency that should be normalized? Critically: this must be decided **once** for the whole corpus (Isaiah, Jeremiah, Ezekiel, Hosea all show it) before the rest of the Minor Prophets ship.

---

## Item B — Hosea 6:6 חֶסֶד vs the Matthew quotation (ἔλεος): an NT-cited MT/LXX divergence with no reader footnote (REVIEW)

**The verse:** Hosea 6:6 is the book's theological heart; Jesus quotes it twice. The MT reads חֶסֶד (corpus-locked → **ความรักมั่นคง** "steadfast love"); the LXX reads ἔλεος "mercy," and that is the form quoted in Matthew (shipped → **ความเมตตา**):

- **Hos 6:6** MT: `כִּי חֶסֶד חָפַצְתִּי וְלֹא־זָבַח וְדַעַת אֱלֹהִים מֵעֹלוֹת` → TH: `เพราะเราประสงค์**ความรักมั่นคง** ไม่ใช่**เครื่องสัตวบูชา** และประสงค์ความรู้จักพระเจ้ายิ่งกว่าเครื่องเผาบูชา`
- **Matt 9:13 / 12:7** GK: `ἔλεος θέλω καὶ οὐ θυσίαν` → TH: `เราประสงค์**ความเมตตา** มิใช่**เครื่องบูชา**`

A reader cross-referencing Hos 6:6 ↔ Matt 9:13 sees ความรักมั่นคง vs ความเมตตา with **no footnote**. The 6:6 KD correctly identifies the divergence but it is KD-only (not reader-facing). The analogous 13:14 → 1 Cor 15:55 divergence **does** carry a reader-facing `reception_history` footnote.

**Question:** Should Hosea 6:6 carry a Tier-2 reader footnote disclosing the MT חֶסֶד / LXX ἔλεος split (the form Jesus quotes), modeled on the 13:14 reception-history note — i.e., does an NT-cited MT/LXX divergence on a marquee verse clear the disclosure floor? (The חֶסֶד → ความรักมั่นคง rendering itself is correct and not in question; this is purely an apparatus/footnote decision.)

---

## Item C — Hosea 14:3 "fruit of our lips": the one place the text departs from its MT base (REVIEW)

**The text base:** the project is MT-anchored (`ot_canon_and_text_base`). Hosea 14:3 is the **single verse in the book** where the translation follows a non-MT reading. The MT vocalizes פָּרִים "bulls (of our lips)"; the translation follows the LXX/Syriac פְּרִי "fruit," harmonizing with the shipped Hebrews 13:15:

- **Hos 14:3** MT: `וּנְשַׁלְּמָה פָרִים שְׂפָתֵינוּ` (lit. "we will render the *bulls* of our lips") → TH: `เพื่อเราจะถวาย**ผลแห่งริมฝีปาก**ของเราต่างเครื่องบูชา` ("fruit of our lips")
- **Heb 13:15** GK: `καρπὸν χειλέων` → TH: `**ผลแห่งริมฝีปาก**ที่ยอมรับพระนามของพระองค์` (byte-shared)

The reading is well-attested (BSB, NIV, ESV-mg "fruit"; the praise-replaces-sacrifice theology is the point) and the Heb 13:15 harmonization is a virtue — but it is a step off the stated MT base, documented only in the KD + `notes` (not reader-facing).

**Two questions:**
1. Is following the LXX/Syriac "fruit of our lips" (against the MT "bulls of our lips") the right call for an MT-anchored translation here, given the strong attestation and the Hebrews 13:15 echo — or should strict MT-priority render "bulls"?
2. Either way, should 14:3 carry a Tier-2 reader footnote noting the MT "bulls" / LXX-Syriac "fruit" divergence and the Heb 13:15 connection?

---

## Item D — Spiritual-harlotry leitwort: זָנָה → เล่นชู้ vs נָאַף → ל่วงประเวณี (STABLE; confirm + lift to a corpus doc)

**The pattern:** Hosea's controlling metaphor — Israel as YHWH's adulterous wife — is rendered with a principled two-lemma split held across all 14 chapters:

| Lemma | Sense | Thai |
|---|---|---|
| זָנָה / זְנוּנִים | "play the harlot / promiscuity" (covenant infidelity) | **เล่นชู้ / การเล่นชู้** |
| נָאַף / נַאֲפוּפִים | "commit adultery" | **ล่วงประเวณี / การล่วงประเวณี** |
| רוּחַ זְנוּנִים | "a spirit of harlotry" | **วิญญาณแห่งการเล่นชู้** |
| זֹנוֹת / קְדֵשׁוֹת | "prostitutes / cult-prostitutes" | **หญิงโสเภณี / หญิงโสเภณีประจำสถานบูชา** |

- **Hos 1:2** GK/HEB: `כִּי־זָנֹה תִזְנֶה הָאָרֶץ מֵאַחֲרֵי יְהוָה` → TH: `เพราะแผ่นดินนี้กำลัง**เล่นชู้**อย่างโจ่งแจ้งโดยหันหนีไปจากองค์พระผู้เป็นเจ้า`
- **Hos 4:13** (both lemmas in one verse): בְּנוֹתֵיכֶם תִּזְנֶינָה (זָנָה) → บุตรสาว…**เล่นชู้**; וְכַלּוֹתֵיכֶם תְּנָאַפְנָה (נָאַף) → บุตรสะใภ้…**ล่วงประเวณี**

This is the OT root-system that the already-shipped Jeremiah 2–3 and Ezekiel 16/23 elaborate, but it lives only in per-verse KDs with no corpus doc.

**Question:** Is the זָנָה → เล่นชู้ (covenant/spiritual infidelity) vs נָאַף → ล่วงประเวณี (literal adultery) split the right disambiguation for the marriage-metaphor vocabulary, and should it be lifted to a corpus doc (`spiritual_harlotry_metaphor_2026-06.md`) as the canonical reference — retro-documenting the Jeremiah/Ezekiel surface against Hosea, the metaphor's source book, and forward-protecting Nahum 3:4 / Micah 1:7?

---

## Item E — Hosea 4:7 tiqqun sopherim: MT "their glory" vs the scribal-tradition "My Glory" (REVIEW)

**The verse:** Hosea 4:7 renders the MT כְּבוֹדָם "their glory" — they exchanged their glory for shame. The `notes` records that this is one of the *tiqqunê sopherim* (the ancient reverent scribal emendations): the original may have read כְּבוֹדִי "**My** Glory" (i.e., they exchanged the LORD himself, their true Glory, for a shameful idol).

- **Hos 4:7** MT: `כְּבוֹדָם בְּקָלוֹן אָמִיר` → TH: `พวกเขาเอา**ศักดิ์ศรีของตน**ไปแลกกับสิ่งที่น่าอับอาย`

The MT surface is correctly followed and the tradition correctly noted — but only in the non-rendered `notes` field, invisible to readers. This is the only tiqqun in Hosea (others occur ahead in Zechariah 2:12, Malachi 1:13).

**Question:** Should a tiqqun-sopherim point of this kind (a reader-relevant text-critical note where the scribal tradition changes the *referent* of the glory from the people to God himself) be surfaced in a reader-facing Tier-2 footnote, or is KD/notes-only disclosure the right policy for tiqqunim across the corpus?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
