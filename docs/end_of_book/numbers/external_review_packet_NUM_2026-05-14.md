# Numbers — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-14**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Numbers** (36 chapters, 1,289 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged; Revelation complete (not yet tagged). Numbers 36/36 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Num 14:18 Sinai attribute-formula recitation drifts from `exod_34_attribute_formula_2026-05.md`

**The drift:** Num 14:18 is Moses' intercessory recitation of the Sinai attribute-formula (Exod 34:6-7), spoken during the spies-rebellion crisis. The corpus-doc `docs/translator_decisions/exod_34_attribute_formula_2026-05.md` (decided 2026-05-09, Ben + cross-AI consensus) **explicitly names Num 14:18 in its locked-recitations list** (alongside Exod 34:6-7, Ps 86:15, Ps 103:8, Ps 145:8, Joel 2:13, Jonah 4:2, Nah 1:3, Neh 9:17, 2 Chr 30:9, Mic 7:18). The Exodus end-of-book audit (2026-05-13, Exodus Item A) flagged the Exodus locking-precedent verses (Exod 34:6-7) as drifting from the doc. **Num 14:18 is the SECOND OT recitation in ship-order and drifts in the same way.**

**The Hebrew at Num 14:18** (the shorter form of the formula — omits opening רַחוּם וְחַנּוּן and the third sin-term חַטָּאָה):

> יְהוָה אֶרֶךְ אַפַּיִם וְרַב־חֶסֶד נֹשֵׂא עָוֹן וָפָשַׁע וְנַקֵּה לֹא יְנַקֶּה פֹּקֵד עֲוֹן אָבוֹת עַל־בָּנִים עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים

**Component-by-component drift** (every locked vocabulary item diverges):

| Hebrew (Num 14:18) | Doc-locked Thai | Num 14:18 as shipped | Drift |
|---|---|---|---|
| אֶרֶךְ אַפַּיִם | **ทรงกริ้วช้า** | **ทรงพระพิโรธช้า** | ✗ (different metaphor; "กริ้วช้า" Rachasap-active vs. "พระพิโรธช้า" "slow in wrath") |
| וְרַב־חֶסֶד | **ทรงบริบูรณ์ด้วยความรักมั่นคง** | **ทรงเปี่ยมด้วยความรักมั่นคง** | ✗ (เปี่ยม vs. บริบูรณ์ — synonyms; minor lexical drift) |
| נֹשֵׂא עָוֹן וָפָשַׁע | **ทรงยกโทษความชั่ว การละเมิด** | **ทรงยกโทษความผิดและการละเมิด** | ✗ (ความชั่ว doc → ความผิด actual — major drift; moral-evil register vs. legal-fault register) |
| וְנַקֵּה לֹא יְנַקֶּה | **แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ** | **แต่จะไม่ทรงปล่อยผู้ผิดให้พ้นโทษ** | ✗ (ทรงพิจารณา vs. ทรงปล่อย — legal-deliberation vs. release) |
| פֹּקֵד עֲוֹן אָבוֹת עַל־בָּנִים | **ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน** | **ทรงให้ความผิดของบิดาตกถึงบุตรหลาน** | ✗ (ทรงลงโทษ "punish" vs. ทรงให้...ตก "let fall upon"; "fathers→sons" vs. "ancestors→grandchildren-and-great-grandchildren") |
| עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים | **ถึงสามชั่วและสี่ชั่วอายุคน** | **จนถึงสามและสี่ชั่วอายุ** | partial drift (acceptable variant phrasing) |

**Cross-corpus context:** This is the **direct downstream test** of the Exodus-audit Item A decision. If Exod 34 is retroactively normalized to the doc-canonical Thai (the Exodus-audit recommendation), then Num 14:18 **must** be normalized in lockstep. Otherwise the cross-corpus recitation breaks at its first downstream witness. The remaining recitations (Ps 86:15, Ps 103:8, Ps 145:8, Joel 2:13, Nah 1:3, Neh 9:17, 2 Chr 30:9, Mic 7:18) all ship later and will follow whichever resolution lands at the Exod 34 + Num 14:18 pair.

**Why this is consequential:** The corpus-doc was created to protect the **cross-corpus lemma-thread**. The Thai reader should recognize the Sinai attribute-formula whenever it recurs. The formula is the OT's most-recited divine-self-revelation — at Sinai (Exod 34:6-7), at the spies-crisis (Num 14:18), repeated through the Psalter and the Twelve. **If the recitations diverge, the Thai reader cannot recognize the recurrence**, and the character-cluster (compassionate-gracious-slow-to-anger-rich-in-chesed-faithful-forgiving-just) becomes invisible.

**Recommended retroactive normalization** (Num 14:18 → doc-canonical Thai):

| | Drift Thai | Recommended Thai (matches Exod 34 normalization) |
|---|---|---|
| 14:18 | ‘องค์พระผู้เป็นเจ้าทรงเป็นพระเจ้าผู้ทรงพระพิโรธช้า และทรงเปี่ยมด้วยความรักมั่นคง ผู้ทรงยกโทษความผิดและการละเมิด แต่จะไม่ทรงปล่อยผู้ผิดให้พ้นโทษ ทรงให้ความผิดของบิดาตกถึงบุตรหลานจนถึงสามและสี่ชั่วอายุ’ | ‘องค์พระผู้เป็นเจ้า ทรงกริ้วช้า ทรงบริบูรณ์ด้วยความรักมั่นคง ทรงยกโทษความชั่ว และการละเมิด แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน ถึงสามชั่วและสี่ชั่วอายุคน’ |

**Two questions:**

1. Should Num 14:18 be retroactively normalized to the canonical Thai locked in `exod_34_attribute_formula_2026-05.md` before tagging `book-numbers-v1`? The decision should be made in tandem with the EXO 34 decision (Exodus-audit Item A); the two restore in one paired commit.

2. Should the doc's Implementation Checklist §3 item 2 (the `check_phrase_consistency.py` extension that HARD FAILS when 3+ formula-components co-occur but the locked Thai is missing) be written in tandem with the normalization commit? Num 14:18 is one of the verses the extension would catch. This is the structural fix that prevents the same drift recurring at Ps 86:15 / Ps 103:8 / Ps 145:8 / Joel 2:13 / Mic 7:18 / Nah 1:3 / Neh 9:17 / 2 Chr 30:9.

---

## Item B — Num 20:16 + Num 22:22-35 (11 occurrences) mal'akh-YHWH cluster drifts from `malak_yhwh_2026-05.md`

**The drift:** The mal'akh-YHWH corpus-doc `docs/translator_decisions/malak_yhwh_2026-05.md` (decided 2026-05-13, Ben + tri-AI consensus, post-Exodus audit) locks **all divine-context מַלְאָךְ → ทูตสวรรค์** uniformly across the OT corpus, matching the NT corpus's existing ทูตสวรรค์-for-ἄγγελος lock. The doc's §3 Implementation Checklist explicitly names **"Num 22 (Balaam's donkey)"** under "forward-cover" — Numbers was supposed to be the first downstream OT-book to apply the lock. **Numbers shipped before the normalization was applied. 11 occurrences drift.**

**The Hebrew lemma is uniform** across all 11 occurrences — מַלְאָךְ (with or without divine-name qualifier or pronominal suffix). The Thai uses **ทูตขององค์พระผู้เป็นเจ้า** (envoy form) instead of the doc-locked **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** (heavenly-messenger form).

| Verse | Hebrew | Thai (as shipped) | Doc-locked Thai |
|---|---|---|---|
| **20:16** | מַלְאָךְ (standalone, Israel-to-Edom diplomatic letter) | **ทูต** (no qualifier) | **ทูตสวรรค์** |
| **22:22** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:23** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:24** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:25** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:26** | מַלְאַךְ־יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:27** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:31** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:32** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:34** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |
| **22:35** | מַלְאַךְ יְהוָה | ทูตขององค์พระผู้เป็นเจ้า | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |

**The Balaam-donkey scene** (22:22-35) is the **largest mal'akh-YHWH cluster in any OT book** (more than the 6 in Exodus, more than the 11 in Judg 13 Manoah-Samson narrative). The drawn-sword angel blocking-the-way is the most-iconic mal'akh-YHWH scene in Scripture, and is the OT-NT pre-incarnate-Christ-as-mal'akh tradition's locus alongside Gen 16/22 + Judg 6/13.

**The lexical distinction in Thai.** **ทูต** alone (without สวรรค์) is plain "messenger / envoy / ambassador" — used in Thai diplomatic register without supernatural connotation (the Thai foreign-affairs ministry calls its ambassadors **ทูต**). **ทูตสวรรค์** (literally "heavenly messenger") is the NT-corpus locked rendering for ἄγγελος (across all 4 Gospels + Acts + epistles + Revelation). A Thai reader encountering 22:22 "ทูตขององค์พระผู้เป็นเจ้า" reads "envoy of the Lord" — the supernatural-marking is absent.

**Cross-corpus implications.** The decision compounds across:
- **Genesis** (Hagar 16:7-13 — `ทูต` form; Akedah 22:11/15 — `ทูตสวรรค์` form; **already inconsistent within Genesis** as flagged in earlier audits)
- **Exodus** (3:2, 14:19, 23:20, 23:23, 32:34, 33:2 — normalized in the malak_yhwh doc's 2026-05-13 commit)
- **Numbers** (this audit — 11 occurrences pending)
- **Judges** (Bochim 2:1+4, Gideon 6:11-22, Manoah 13:3-21)
- **Samuel** (2 Sam 24:16); **Kings** (1 Kgs 19:5+7, 2 Kgs 1:3+15)
- **Zechariah** (20+ occurrences in visions 1-6)
- **Malachi** (3:1 — the literary mal'akh-bookend)

**Recommended normalization** for all 11 occurrences:

> **22:22 normalized:** "แล้วพระพิโรธของพระเจ้าก็ลุกขึ้นเพราะเขากำลังเดินทาง และ**ทูตสวรรค์ขององค์พระผู้เป็นเจ้า**ยืนในทางเพื่อต่อต้านเขา…"

(Same pattern applied to 22:23, 22:24, 22:25, 22:26, 22:27, 22:31, 22:32, 22:34, 22:35; standalone **ทูตสวรรค์** at 20:16.)

**Two questions:**

1. Should the project retroactively normalize the 11 Numbers mal'akh-YHWH occurrences to **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** (or **ทูตสวรรค์** for the standalone Num 20:16) per the `malak_yhwh_2026-05.md` doc-lock before tagging `book-numbers-v1`? The doc's §3 forward-cover for Num 22 was unfulfilled at ship; this is the corrective edit.

2. Is there theological concern about identifying the Num 22 Balaam-donkey מַלְאַךְ יְהוָה (the drawn-sword angel — often read in church-tradition as a Christophany alongside Exod 3:2 and Gen 16/22) with **ทูตสวรรค์** ("heavenly messenger" = generic angel)? Or should the verse-level Layer-2 footer carry the theophanic-distinction (per the doc's §3 footnote-template) and the surface Thai stay uniform? (The doc's §2.2 explicitly endorses lexical-collapse + Layer-2 carry of the Christophanic-reading. Confirming for the Balaam-donkey case here.)

---

## Item C — Num 31:17-18 + 25:6-9 sexual-violence + zealot-execution register: doctrinal Layer-2 footer warranted?

**The textual question:** Two morally-difficult passages in close proximity:

> **25:6-9** (Phinehas spear-execution; ends a divinely-sent plague):
> "And [Phinehas] went after the man of Israel into the chamber, and pierced both of them, the man of Israel and the woman through her belly. So the plague was stopped from the children of Israel. And those who died in the plague were 24,000."
>
> **31:17-18** (Midianite war-booty distribution, following the Balaam-counsel apostasy of NUM 25):
> Hebrew: וְעַתָּה הִרְגוּ כָל־זָכָר בַּטָּף וְכָל־אִשָּׁה יֹדַעַת אִישׁ לְמִשְׁכַּב זָכָר הֲרֹגוּ׃ וְכֹל הַטַּף בַּנָּשִׁים אֲשֶׁר לֹא־יָדְעוּ מִשְׁכַּב זָכָר הַחֲיוּ לָכֶם׃
>
> Thai (as shipped): "และบัดนี้ จงฆ่าเด็กชายทุกคน และหญิงทุกคนที่ได้รู้จักชายด้วยการนอนกับชาย พวกเจ้าจงฆ่า แต่เด็กหญิงทั้งหมดที่ไม่เคยรู้จักการนอนกับชาย จงไว้ชีวิตไว้สำหรับพวกเจ้า"

**The translation surface is faithful and literal.** The Hebrew imperative-of-command (הִרְגוּ) and imperative-of-prohibition-by-exclusion (לֹא־יָדְעוּ) is preserved. The Hebrew euphemism for sexual experience (יָדְעוּ מִשְׁכַּב זָכָר "know the lying with a man") is preserved without sanitization.

**The interpretive question.** Num 31:17-18 is unique in the OT corpus for its **active divine-sanctioned-by-Moses sexual-violence target** — the explicit captive-virgin-keeping is in the same Mosaic instruction as the kill-all-non-virgin command. This is a **first-class evangelical-reader interpretive crux** — Thai-evangelical readers will encounter this and either:
- (a) read it as historically-conditioned warfare-ethics (standard evangelical-historicist reading);
- (b) read it as theological-typology (the "exterminate-Midianite-cult to prevent recurrence-of-Baal-Peor-apostasy" reading);
- (c) confront the moral question directly.

**Two analogous OT-corpus precedents** in the Eremos audit history:
- **Exod 15:11 בָּאֵלִם** (Exodus audit Item C / §14) — `ot_polytheistic_register_2026-05.md` was written to handle the Hebrew-evangelical-register tension on a single verse.
- **Gen 19, 34, 38, 39** (Genesis audit §11) — Genesis-audit STABLE-flagged the morally-difficult content register; the existing doc was deemed sufficient.

**Three resolution paths:**

(a) **Current** — leave as-is. Most-faithful to the Hebrew text's plain surface. Defensible academically; absorbs the reader-interpretive-burden as the standard.

(b) **Layer-2 doctrinal footer** — add an entry to `output/textual_variants/numbers_31.json` and `output/textual_variants/numbers_25.json` naming the **ḥerem (ban) institution in OT warfare** and the **interpretive options** in evangelical-Protestant tradition. Similar pattern to the Gen 6:1-4 Nephilim Layer-2 (preserves the surface; carries the interpretive question in a footer).

(c) **Doc-lift** — write `docs/translator_decisions/ot_warfare_ethics_2026-05.md` covering Num 21 (Sihon/Og elimination), Num 25 (Phinehas), Num 31 (Midianite war), Deut 7+20+25 (ḥerem ordinances), Josh 6-11 (Conquest narratives), 1 Sam 15 (Saul-and-Amalek). The doc names the **historicist-conditioning interpretive frame** Ben endorses, preserves textual faithfulness, and locks the Layer-2 footer practice across the OT-warfare cluster.

**Question:** Should the project write `ot_warfare_ethics_2026-05.md` to handle the entire OT-warfare-ethics cluster uniformly (option c), or limit the response to per-passage Layer-2 footers at Num 31:17-18 + 25:6-9 (option b), or leave as-is with no editorial footer (option a)? The corpus-wide doc would handle 30+ verses across the Pentateuch + Joshua + 1 Samuel forward-protectively and is the project's standard response pattern for reader-experience-protection issues. (Cost: one new corpus-doc; zero verse-edits.)

---

## Item D — Sinai = ซีนาย / สีนาย mix within Numbers + drift from Exodus's locked form

**The drift:** The Hebrew סִינַי "Sinai" renders inconsistently within Numbers AND between Numbers and Exodus.

| Book | ซีนาย | สีนาย |
|---|---|---|
| Exodus | **44×** (100% uniform) | 0× |
| Numbers | **27×** | **10×** |

**Within-NUM drift.** The same Hebrew word is rendered two different ways in the same book. Spot-check shows the 10× `สีนาย` occurrences cluster in chs.1-3, 9-10, 33; the 27× `ซีนาย` are distributed elsewhere.

**Cross-book drift.** Exodus locked `ซีนาย` (100% uniform); Numbers's 10× `สีนาย` breaks that lock at the cross-Pentateuch level.

**Editorial assessment.** Both spellings are defensible Thai transliterations of סִינַי. `สีนาย` follows the Hebrew vowel /iː/ literally; `ซีนาย` follows the conventional Thai-Christian-Bible Sinai-spelling (matches THSV-1971). Per `proper_names_and_transliteration_2026-05.md`'s "follow established Thai-Christian-Bible precedent unless documented otherwise" rule, `ซีนาย` is the corpus-canonical form.

**Recommended normalization:** Change the 10× `สีนาย` to `ซีนาย` to match Exodus + within-book consistency. Mechanical fix — locations are predominantly NUM 1:1, 1:19, 3:1, 3:4, 3:14, 9:1, 9:5, 10:12, 33:15, 33:16.

**Question:** Should the project retroactively normalize the 10× `สีนาย` occurrences to `ซีนาย` to match the Exodus-locked form, and add a `glossary.json` entry or proper-name check-script extension to lock this corpus-wide (and prevent the same drift at Deut 33:2, Judg 5:5, Ps 68:8+17, Neh 9:13)? The drift is mechanical (no semantic question); the question is whether to absorb the normalization cost now (before `book-numbers-v1` tag) or accept the within-book inconsistency.

(Related place-name drift: Succoth EXO `สุคโคท` → NUM `สุคคท` at 4 occurrences in NUM 33:5-6. Same class of drift; recommend same path.)

---

## Item E — Numbers first-occurrence YHWH-footnote wording-drift starting at ch.15

**The wording-drift:** The Layer-2 first-occurrence footnotes in `output/textual_variants/numbers_NN.json` were drafted with consistent template for chapters **1-14**:

> **องค์พระผู้เป็นเจ้า** ในบทนี้ (ปรากฏที่ข้อ X, Y, Z...) แปลจากภาษาฮีบรู יהוה (พระนามเฉพาะของพระเจ้า ออกเสียงโดยทั่วไปว่า **"ยาห์เวห์"** Yahweh)…

Starting at ch.15, the template **omits the "ยาห์เวห์ Yahweh" romanization-phrase**:

> **องค์พระผู้เป็นเจ้า** ในบทนี้ (ปรากฏที่ข้อ X, Y, Z...) แปลจากภาษาฮีบรู יהוה (พระนามเฉพาะของพระเจ้า). ฉบับเอเรโมสใช้ **องค์พระผู้เป็นเจ้า** ตามแบบแผนของฉบับพันธสัญญาใหม่ในการแปล κύριος…

**The check-script effect.** `scripts/check_divine_names.py` (line 186) detects first-occurrence footnotes by pattern-matching for `"องค์พระผู้เป็นเจ้α" + "ยาห์เวห์"` or english `"tetragrammaton" / "yhwh"` in `.lower()` form. The post-ch.14 template loses the Thai marker (ยาห์เวห์) without adding either english marker — so the script reports `[D] numbers ch.NN: contains YHWH but no first-occurrence footnote` for chs.15-36 (22 warnings).

**The footnotes ARE present and well-formed.** The check is detecting a wording-drift, not a missing-footnote. Both wordings are reader-facing-acceptable; the post-ch.14 wording is arguably more concise (references the project's own divine_names_table doc explicitly).

**Two paths:**

(a) **Restore the wording template** — add back the "ยาห์เวห์ Yahweh" romanization phrase to chs.15-36 footnotes (22 short edits). Preserves the script's current pattern-set; uniform wording across all 36 chapters.

(b) **Loosen the script's pattern** — add the post-ch.14 marker phrase ("ตามแบบแผนของฉบับพันธสัญญาใหม่") to the script's detection set. Adopt the shorter template as the going-forward standard. Avoids 22 footnote-edits; aligns with the project's pattern of evolving conventions doc-first.

**Question:** Should the project (a) retroactively restore the "ยาห์เวห์ Yahweh" romanization-phrase in the 22 chs.15-36 footnotes for uniform wording across the book, or (b) extend `check_divine_names.py`'s pattern-set to recognize the post-ch.14 marker phrase and adopt the shorter template as the going-forward OT-corpus standard?

---

## Item F — Num 14:17 standalone אֲדֹנָי vocative renders as YHWH-form rather than divine_names_table's Adonai-form

**The textual question:** Num 14:17 is in a Moses-to-YHWH prayer context — Moses uses the vocative `אֲדֹנָי` (not YHWH) to invoke the Lord's power before reciting the Sinai attribute-formula at 14:18.

> **14:17 Hebrew:** וְעַתָּה יִגְדַּל־נָא כֹּחַ אֲדֹנָי כַּאֲשֶׁר דִּבַּרְתָּ לֵאמֹר
>
> **14:17 Thai (as shipped):** บัดนี้ ขอพระอานุภาพของ**องค์พระผู้เป็นเจ้าของข้าพระองค์**ทรงสำแดงพระเกียรติยิ่งใหญ่ ตามที่พระองค์ตรัสว่า

**The doc gap:** `divine_names_table_2026-05.md` locks **standalone אֲדֹנָי → องค์เจ้านาย** as a distinct form from the YHWH-form. Num 14:17 uses neither the locked `องค์เจ้านาย` nor a transliteration — it uses **`องค์พระผู้เป็นเจ้าของข้าพระองค์`** ("my Lord", literally "the Lord-of-me") which is a paraphrase variant.

**Two readings:**

- (a) **Intentional sub-form** — Moses is addressing YHWH-as-master with the personal-possessive ("my Lord"), so the Thai's "องค์พระผู้เป็นเจ้าของข้าพระองค์" preserves the personal-vocative force even though the lexical category (Adonai) is collapsed into the YHWH-form. This is the as-shipped surface; it reads natural in Thai petitionary register.
- (b) **Drift** — the doc-lock is `องค์เจ้านาย` for standalone Adonai. Even in YHWH-context, the Adonai vocative should use that form.

**Script invisibility.** The script `check_divine_names.py` does NOT flag this verse as a [C] case because the YHWH-form `องค์พระผู้เป็นเจ้า` IS present (the script's predicate is "Thai missing BOTH Adonai-form AND YHWH-form"). The drift is therefore script-invisible.

**Cross-corpus implications.** Standalone-Adonai-in-prayer occurs throughout the Psalms (Pss 8:1+9, 16:2, 35:17+22+23, 38:9+15+22, 51:15, 54:4, 55:9, 57:9, 59:11, 62:12, 66:18, 68:11+17+19+20+22+26+32, 69:6, 71:5+16, 73:20+28, 77:2+7, 78:65, 79:12, 86:3+4+5+8+9+12+15, 89:49+50, 90:1+17, 109:21, 130:2+3+6, 140:7) and in the major Prophets (Isa 6:1+8+11; Jer's "Adonai YHWH" compound; Ezekiel passim; Dan 9:3+4+7+8+15+16+17+19). **Without normalization, the lemma-thread compounds inconsistency across the entire post-Pentateuch OT corpus.**

**Two resolution paths:**

(a) **Doc-amend** — add to `divine_names_table_2026-05.md` a sub-rule for "standalone Adonai-as-prayer-vocative within YHWH-context" that locks **องค์พระผู้เป็นเจ้าของข้าพระองค์** (as-shipped form). Num 14:17 becomes the locking precedent for the OT corpus; future Pss + Isa + Ezek + Dan recitations follow the lock. Defensible because Thai petitionary register naturally takes the personal-possessive.

(b) **Normalize Num 14:17 to องค์เจ้านาย** — match the doc strictly. The shipped Thai is "องค์พระผู้เป็นเจ้าของข้าพระองค์"; normalized would be "ขอพระอานุภาพของ**องค์เจ้านาย**ทรงสำแดงพระเกียรติยิ่งใหญ่…". Reads less petitionary in Thai (the รายาศัพท์ register collapses into address-of-master without the personal-possessive).

**Question:** Which option preserves the OT-corpus principled distinction between (i) Adonai-as-title (lock = `องค์เจ้านาย`) and (ii) Adonai-as-prayer-vocative (currently "องค์พระผู้เป็นเจ้าของข้าพระองค์")? Should `divine_names_table_2026-05.md` be amended to add a sub-rule for the prayer-vocative case (option a), with Num 14:17 as the locking precedent for the OT corpus — or should Num 14:17 be retroactively normalized to `องค์เจ้านาย` (option b) to match the doc strictly?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
