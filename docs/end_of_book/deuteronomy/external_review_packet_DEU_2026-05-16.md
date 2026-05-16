# Deuteronomy — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-16**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Deuteronomy** (34 chapters, 959 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation complete (not yet tagged). Deuteronomy 34/34 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — DEU 5:9-10 Sinai attribute-formula recitation drifts from `exod_34_attribute_formula_2026-05.md` (third downstream test)

**The drift:** DEU 5:9-10 is the **Decalogue-embedded** form of the Sinai attribute-formula — the same paqad-clause + chesed-clause that recur from Exod 34:6-7 (and from Num 14:18). This is the **THIRD OT recitation** of the formula in ship-order and the FIRST in a Decalogue context. The corpus-doc `docs/translator_decisions/exod_34_attribute_formula_2026-05.md` (decided 2026-05-09, Ben + cross-AI consensus) locks the canonical Thai for each component; DEU 5:9-10 drifts the same way EXO 34:6-7 (Exodus-audit Item A) and NUM 14:18 (Numbers-audit Item A) drift.

**The Hebrew at DEU 5:9-10** (the Decalogue 2nd-commandment expansion):

> אֵל קַנָּא פֹּקֵד עֲוֺן אָבוֹת עַל־בָּנִים וְעַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים לְשֹׂנְאָי׃ וְעֹשֶׂה חֶסֶד לַאֲלָפִים לְאֹהֲבַי וּלְשֹׁמְרֵי מִצְוֺתָי׃

**Component-by-component drift** (every locked vocabulary item in the paqad-clause diverges):

| Hebrew (DEU 5:9-10) | Doc-locked Thai | DEU 5:9-10 as shipped | Drift |
|---|---|---|---|
| פֹּקֵד עֲוֹן אָבוֹת עַל־בָּנִים | **ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน** | **ผู้ลงโทษความผิดของบิดาบนบุตร** | ✗ ทรง- prefix dropped (divine-volitional register slip; ผู้- agentive instead); ความชั่ว doc → ความผิด actual (moral-evil vs legal-fault); บรรพบุรุษ doc → บิดา actual (ancestors vs fathers); "ต่อ" doc → "บน" actual (preposition drift); missing หลานเหลน (great-grandchildren elision) |
| עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים | **ถึงสามชั่วและสี่ชั่วอายุคน** | **ถึงสามและสี่ชั่วอายุ** | partial drift (acceptable variant phrasing) |
| וְעֹשֶׂה חֶסֶד לַאֲלָפִים | **และทรงสำแดงความรักมั่นคงต่อหนึ่งพันชั่วอายุ** | **ทรงสำแดงความรักมั่นคงต่อหนึ่งพันชั่วอายุ** | ✓ (matches; minor — initial conjunction "และ" dropped) |

**The cross-corpus tangle.** The same paqad-clause appears at five places — EXO 20:5, DEU 5:9, EXO 34:7, NUM 14:18, plus the doc-canonical form — and each has different Thai:

- **EXO 20:5 Thai:** "ลงโทษ**ความบาป**ของบิดา**ที่ผ่านไปยัง**บุตรชั่วอายุที่สามและที่สี่ของผู้ที่เกลียดชังเรา"
- **DEU 5:9 Thai (this audit):** "**ผู้ลงโทษความผิด**ของบิดา**บน**บุตรถึงสามและสี่ชั่วอายุของผู้เกลียดเรา"
- **NUM 14:18 Thai (NUM-audit §2):** "**ทรงให้ความผิด**ของบิดา**ตกถึง**บุตรหลานจนถึงสามและสี่ชั่วอายุ"
- **EXO 34:7 Thai (EXO-audit Item A):** various component drifts
- **Doc-canonical Thai:** "**ทรงลงโทษความชั่ว**ของ**บรรพบุรุษต่อบุตรหลานและหลานเหลน** ถึงสาม**ชั่วและสี่ชั่วอายุคน**"

**Five different Thai surfaces for the same paqad-clause across the OT-pilot corpus.** This is the most concentrated single-clause cross-corpus drift in the OT-pilot to date.

**Cross-corpus context.** This is the **direct downstream test** of the Exodus-audit + Numbers-audit decisions. If EXO 34:6-7 + Num 14:18 are retroactively normalized to the doc-canonical Thai (the prior-audit recommendations), then DEU 5:9-10 **must** be normalized in lockstep. Otherwise the Decalogue context — arguably the formula's primary OT setting in Christian/Jewish liturgy — breaks the thread.

**Why this is consequential.** DEU 5 is the Second Decalogue, and DEU 5:9 is among the **most-known OT verses** in evangelical Christian usage ("the sins of the fathers visited unto the third and fourth generation"). The forward-compounding is across every Pss/Joel/Mic/Nah/Neh/2 Chr recitation of the formula. Five surfaces here translate into 8+ surfaces by the time the Twelve ship.

**Recommended retroactive normalization** (DEU 5:9-10 → doc-canonical Thai, in tandem with EXO 34 + NUM 14:18):

| | Drift Thai | Recommended Thai (matches doc + EXO/NUM normalization) |
|---|---|---|
| 5:9 | เพราะเรา องค์พระผู้เป็นเจ้าพระเจ้าของเจ้า เป็นพระเจ้าผู้ทรงหวงแหน **ผู้ลงโทษความผิดของบิดาบนบุตรถึงสามและสี่ชั่วอายุ**ของผู้เกลียดเรา | เพราะเรา องค์พระผู้เป็นเจ้าพระเจ้าของเจ้า เป็นพระเจ้าผู้ทรงหวงแหน **ทรงลงโทษความชั่วของบรรพบุรุษต่อบุตรหลานและหลานเหลน ถึงสามชั่วและสี่ชั่วอายุคน** ของผู้เกลียดเรา |
| 5:10 | **ทรงสำแดงความรักมั่นคงต่อหนึ่งพันชั่วอายุ**ของผู้ที่รักเราและรักษาบัญญัติของเรา | **และทรงสำแดงความรักมั่นคงต่อหนึ่งพันชั่วอายุ**ของผู้ที่รักเราและรักษาบัญญัติของเรา |

**Two questions:**

1. Should DEU 5:9-10 be retroactively normalized to the canonical Thai locked in `exod_34_attribute_formula_2026-05.md` before tagging `book-deuteronomy-v1`? The decision should be made in tandem with the EXO 34 (Exodus-audit Item A) + NUM 14:18 (Numbers-audit Item A) decisions; all three Pentateuchal anchors restore in one paired commit so the formula-thread is intact across the entire Torah before any downstream OT-poetry/prophets book ships.

2. The `exod_34_attribute_formula_2026-05.md` doc's current locked-recitations list does NOT yet name DEU 5:9-10. Should the doc be amended to add DEU 5:9-10 + EXO 20:5 to the locked-recitations list, so the cross-corpus thread explicitly covers the Decalogue paqad-clause recurrences (in addition to the Sinai/Spies-crisis recitations)? The Decalogue formula is the most-recited OT-corpus passage in Christian + Jewish liturgy; explicit doc-coverage protects it forward to every Pss/Prophets quotation.

---

## Item B — Decalogue parallel-text drift EXO 20 vs DEU 5 (Hebrew identical, Thai divergent)

**The drift:** The two Decalogues (Exod 20:2-17 and DEU 5:6-21) are **word-identical in MT** for most of the prohibitives. But the Thai surface drifts systematically across the two parallel passages. Most concretely:

| Cmd | Hebrew | EXO 20 Thai | DEU 5 Thai | Drift |
|---|---|---|---|---|
| Slave-house | מִבֵּית עֲבָדִים | "เรือนทาส" (20:2) | "**บ้านแห่งความเป็นทาส**" (5:6) | ✗ different idiom |
| Prohibitive frame | לֹא + verb | "**อย่า** + verb" throughout | "**เจ้าจะต้องไม่** + verb" throughout | ✗ syntactic register |
| 6th (murder) | לֹא תִּרְצָח | "อย่าฆ่าคน" (20:13) | "เจ้าจะต้องไม่ฆ่าคน" (5:17) | ✗ syntax only |
| 7th (adultery) | לֹא תִּנְאָף | "อย่าล่วงประเวณี" (20:14) | "เจ้าจะต้องไม่ล่วงประเวณี" (5:18) | ✗ syntax only |
| **8th (theft)** | לֹא תִּגְנֹב | "อย่า**ลักทรัพย์**" (20:15) | "เจ้าจะต้องไม่**ขโมย**" (5:19) | ✗ **different verb lemma for גָּנַב** |
| 9th (false witness) | לֹא תַעֲנֶה | "อย่าเป็นพยานเท็จ" (20:16) | "เจ้าจะต้องไม่เป็นพยานเท็จ" (5:20) | ✗ syntax |
| 5th honor-parents | (DEU adds "וְלמַעַן יִיטַב לָךְ") | "เพื่อวันของเจ้าจะ**ยาวนาน**" (20:12) | "เพื่อวันของเจ้าจะ**ยืนยาว**" (5:16) | ✗ Hebrew יַאֲרִכוּן same lemma; DEU 5:16 + Eph 6:2-3 match (ยืนยาว) and EXO 20:12 diverges (ยาวนาน) |
| 10th coveting order | (Hebrew DEU reorder) | order: house→wife→servants | order: **wife→house+field**→servants | ✓ correctly preserves DEU Hebrew reorder |
| Sabbath rationale | (DEU exodus-rationale) | creation (20:11) | exodus deliverance (5:15) | ✓ correctly preserves DEU Hebrew |

**The Hebrew-text variations** (Sabbath-rationale shift, coveting-order reshuffle, the DEU "well-with-you" expansion at 5:16 v 20:12) **are correctly preserved**. The drift is on the Thai surface where the Hebrew is identical. The **8th commandment lemma drift** (גָּנַב: ลักทรัพย์ EXO / ขโมย DEU) is the most concrete — a single Hebrew verb rendered as two different Thai verbs in two parallel passages within the same Pentateuch.

**Cross-corpus compound.** The NT Decalogue-quotations land at further surfaces still:
- **Rom 13:9** quotes the 7th + 6th + 8th + 10th in compressed form
- **Matt 19:18** // **Mark 10:19** // **Luke 18:20** quote 5 commandments to the rich-young-ruler
- **Eph 6:2-3** quotes the 5th honor-parents (matches DEU 5:16 ยืนยาว, not EXO 20:12 ยาวนาน — defensible since Paul quotes the DEU 5 expanded form)
- **Jas 2:11** quotes the 6th + 7th together

Each NT-side surface is independent of both OT-side surfaces. The Thai-reader cannot recognize the cross-quotation chain.

**The principled position.** Where the **Hebrew is identical, the Thai should be identical**. EXO 20 // DEU 5 is the canonical parallel-text exercise in the OT-pilot corpus.

**Recommended resolution paths:**

(a) **Normalize DEU 5 to EXO 20 surface** — change DEU 5:17, 5:18, 5:19, 5:20, 5:21 to EXO 20 syntactic frame ("อย่า + verb"); change DEU 5:19 ขโมย → ลักทรัพย์; change DEU 5:16 ยืนยาว → ยาวนาน; change DEU 5:6 "บ้านแห่งความเป็นทาส" → "เรือนทาส". Cost: ~5-8 surgical verse-edits in DEU.

(b) **Normalize EXO 20 to DEU 5 surface** — symmetric edit but in EXO. Less defensible (EXO is older corpus + ships earlier in the OT canon).

(c) **Write a corpus-doc `decalogue_parallel_text_2026-05.md`** that locks the principle for the Ten Commandments + the eight NT cross-quotations as a unified Thai-thread. Cost: doc + ~10 surgical verse-edits across EXO/DEU/NT. Strongest forward-protection.

**Two questions:**

1. Should the project normalize EXO 20 // DEU 5 Thai surface where the Hebrew is identical (path a or c)? The 8th commandment (גָּנַב: ลักทรัพย์/ขโมย) is the cleanest test case — same Hebrew verb in both Decalogues, two different Thai verbs.

2. Should the doc-lift path (c) be chosen so the Thai-lock extends to the **eight NT Decalogue-citations** (Matt 5:21+27, Matt 19:18-19 // Mark 10:19 // Luke 18:20, Rom 7:7, Rom 13:9, Eph 6:2-3, Jas 2:11) as well, protecting cross-corpus traceability before the Synoptic-quotations are reaudited?

---

## Item C — NT-cross-corpus DEU-quote drift cluster (highest forward-protection magnitude)

**The drift:** DEU is **the most-quoted OT book in the NT corpus** — Jesus quotes DEU three times in the Matt-4 temptation, the Shema is the "greatest commandment" Jesus identifies, Paul cites DEU passim in Romans, Hebrews-the-Greater-than-Moses argument rests on DEU. The cross-corpus Thai-surface drifts between DEU (OT-corpus ship) and the NT-corpus ship are widespread and systematic.

| OT (DEU) | NT echo | Thai surface drift | Severity |
|---|---|---|---|
| **DEU 18:15** "prophet like me" | Acts 3:22 / 7:37 | DEU "**ผู้พยากรณ์**" vs Acts "**ผู้เผยพระวจนะ**" — different lemma for נביא/προφήτης | **MAJOR** — affects entire Major+Minor Prophets corpus (Isa-Mal, ~16 books, ~250 chapters un-shipped) |
| **DEU 6:5** Shema love-formula | Matt 22:37 / Mark 12:30 / Luke 10:27 | DEU + Luke = สุด**จิตวิญญาณ** for ψυχή/נֶפֶשׁ; Mark + Matt = สุด**จิต** | MAJOR — affects entire psyche/nephesh anthropological-vocabulary thread |
| **DEU 11:13** (secondary Shema) | (intra-DEU) | DEU 11:13 = สุดจิต but DEU 6:5 = สุดจิตวิญญาณ — within-DEU drift on the same Shema | MEDIUM |
| **DEU 25:4** "do not muzzle ox" | 1 Cor 9:9 / 1 Tim 5:18 | DEU "อย่า**ผูกปาก**วัวขณะที่มันกำลังเหยียบนวดข้าว" / 1Cor "อย่าเอา**ผ้าผูกปาก**วัวขณะมันกำลังนวดข้าว" / 1Tim "อย่าเอา**ตะกร้อครอบปาก**วัว" | **THREE different Thai forms** — the worst single-verse cross-corpus drift in DEU's NT-quotation set |
| **DEU 32:21** "jealousy by non-nation" | Rom 10:19 | DEU "**หึง**" vs Rom "**ริษยา**" — different verb lemma for קנא/παραζηλόω | HIGH — affects divine-jealousy + Pauline-jealousy thread |
| **DEU 6:13** "fear/serve" | Matt 4:10 | DEU "เกรงกลัว…รับใช้พระองค์เท่านั้น…สาบาน" vs Matt "นมัสการ…ปรนนิบัติพระองค์แต่ผู้เดียว" | MEDIUM (Matt quotes LXX προσκυνέω form; defensible but no Layer-2 footer flags it) |
| **DEU 6:16** "do not test" | Matt 4:7 | DEU "อย่า**ทดสอบ**" vs Matt "อย่า**ทดลอง**" — verb-lemma drift on נסה/πειράζω | MEDIUM |
| **DEU 8:3** "bread alone" | Matt 4:4 | DEU "**มีชีวิตอยู่**" vs Matt "**ดำรงชีวิต**" — verb drift on חיה/ζάω | MEDIUM |
| **DEU 21:23** "hung on tree" | Gal 3:13 | DEU + Gal align except "ของพระเจ้า" qualifier omitted in Gal (matches Greek) | LOW — defensible |
| **DEU 27:26** "cursed not uphold" | Gal 3:10 | different syntactic frames (Gal quotes LXX expanded form) | LOW — principled |
| **DEU 30:12-14** "word near you" | Rom 10:6-8 | DEU "ใจ" vs Rom "**จิตใจ**" | MEDIUM |
| **DEU 32:35** "vengeance is mine" | Rom 12:19 / Heb 10:30 | DEU + Rom match (ตอบแทน); Heb 10:30 diverges (ตอบสนอง) | MEDIUM |
| **DEU 32:43** | Heb 1:6 | text-critical — see Item E | (sep) |
| **DEU 17:6 / 19:15** "2-or-3 witnesses" | Matt 18:16 / 2Cor 13:1 / 1Tim 5:19 | DEU 19:15 + NT match ("พยานสองหรือสามคน"); DEU 17:6 slightly drifts ("สองคนหรือสามคน") | LOW |

**The biggest forward-protection issue.** The נביא/προφήτης lemma split (DEU 18:15 prophet-like-Moses + the entire DEU 18:9-22 prophet-cluster uses ผู้พยากรณ์; Acts 3:22+7:37 + Heb 3 backdrop uses ผู้เผยพระวจนะ; the entire Major + Minor Prophets corpus has ~16 un-shipped books) — locking this thread NOW protects every future Prophets ship.

**Recommended resolution paths:**

(a) **Status-quo + accept drift** — each side reads with internal-corpus coherence. NOT recommended — DEU is the most-NT-quoted OT book; locking the thread here protects the largest downstream surface.

(b) **Write `ot_nt_cross_quotation_thread_2026-05.md`** that locks the OT→NT Thai-thread for the major lemma-pairs: נביא/προφήτης (the largest forward-cover surface), נֶפֶשׁ/ψυχή (Shema thread), קנא/ζῆλος (divine-jealousy thread), DEU 25:4 muzzle-ox (3-way drift). Cost: 1 new corpus-doc + ~20-30 surgical verse-edits across DEU + NT-citation verses + `check_phrase_consistency.py` extension to HARD FAIL when an OT-NT quotation-pair has divergent Thai surface for the same lemma.

(c) **Selective normalization for highest-impact drifts only** — normalize DEU 18:15 + the entire DEU 18:9-22 prophet-cluster to ผู้เผยพระวจนะ (match NT); normalize DEU 25:4 to match 1 Cor 9:9; leave the others. Cost: ~5-8 surgical verse-edits.

**Two questions:**

1. Should the project lock the OT→NT cross-quotation Thai-thread now (path b) — the most-NT-quoted OT book being shipped is the natural anchor point — or accept the as-shipped drifts and normalize lemma-by-lemma in downstream audits? The Major Prophets corpus is the largest forward-cover; locking נביא → ผู้เผยพระวจนะ uniformly at DEU 18:15 protects ~16 books.

2. The DEU 25:4 muzzle-ox quote currently has **three different Thai surface forms** across DEU + 1 Cor 9:9 + 1 Tim 5:18 — same Greek text Paul quotes twice. Which canonical Thai form should the cross-corpus thread lock onto? Recommended: the most-natural Thai-agriculture-register form "อย่าเอาผ้าผูกปากวัว" (1 Cor 9:9 form); or alternatively a more-literal "อย่าผูกปากวัว" (DEU form). The decision drives the normalization of all three verses.

---

## Item D — DEU ḥerem (חרם) 5-way Thai-surface drift; `ot_warfare_ethics_2026-05.md` needs surface-lock amendment

**The drift:** DEU is THE ḥerem book in the OT-pilot corpus — more ḥerem-density than Numbers + the future Joshua-Conquest combined. The `docs/translator_decisions/ot_warfare_ethics_2026-05.md` doc (landed per NUM-audit §17 recommendation) names the **historicist-conditioning interpretive frame** Ben endorsed but does NOT lock the Thai surface for חרם itself. DEU ships with **5 distinct Thai surface forms** for the same Hebrew lemma:

| Verse | Hebrew form | Thai surface |
|---|---|---|
| 2:34 | וַנַּחֲרֵם | "**ถวายเฮเรม**" (transliterated; "we devoted" 1cpl form) |
| 3:6 | וַנַּחֲרֵם | "**ถวายเฮเรม**" (transliterated) |
| 7:2 | הַחֲרֵם תַּחֲרִים | "**ถวายเฮเรม** … ทำลายอย่างสิ้นเชิง" (translit + gloss) |
| 7:26 | חֵרֶם | "**แยกถวายเฉพาะเพื่อการทำลาย**" (descriptive paraphrase) |
| 13:16 | הַחֲרֵם | "**ทุ่มถวายเพื่อทำลายอย่างสมบูรณ์**" |
| 13:18 | חֵרֶם | "**สิ่งที่ทุ่มถวาย**" |
| 20:17 | הַחֲרֵם תַּחֲרִימֵם | "**ทุ่มถวายพวกเขาเพื่อทำลายอย่างสมบูรณ์**" |
| 25:17-19 (Amalek) | מָחֹה (different lemma) | "**ลบความทรงจำของอามาเลค**" ✓ (principled — different Hebrew verb) |

**Layer-2 doctrinal footers:**
- **DEU 20:17 has a rich Layer-2 anchor footer** in `output/textual_variants/deuteronomy_20.json` — names the ot_warfare_ethics interpretive frame, Canaan-judgment historicism, Rahab/Gibeonites exceptions, Eph 6:12 spiritual-warfare typology, Rev 19-20 final-judgment typology. **Excellent.**
- **No ḥerem footers at chs 2-3, 7, 13, 25** — readers encounter four chs of ḥerem command before the doctrinal-frame footer at 20:17.

**The lexical question.** The five surface forms split into three categories:
- **Transliterated:** เฮเรม (preserves the Hebrew lemma as a technical-ritual term — readers learn the Hebrew word + must contextualize from surrounding gloss)
- **Volitional / "devote":** ทุ่มถวาย/แยกถวาย ("hand-over-as-offering"; preserves the ritual-offering sense — most-theologically transparent)
- **Outcome-paraphrase:** "ทำลายอย่างสิ้นเชิง" ("destroy utterly"; conveys outcome only — loses the ritual-offering sense)

**Editorial assessment.** Five surfaces is too many for a single Hebrew lemma in a single book. The DEU 20:17 anchor footer is excellent but under-supported by surface-uniformity. The doc explicitly names the historicist frame but is silent on the Thai-surface choice.

**Recommended normalization** — lock canonical Thai surface to **"ทุ่มถวายเพื่อทำลาย"** (the 13:16 / 20:17 form): most-frequent, most-theologically transparent (preserves ritual-offering register + destruction-outcome), and most-readable in narrative-prose. Optionally keep the transliterated "เฮเรม" at the FIRST DEU occurrence (2:34) with a chapter-footer naming the Hebrew lemma + the canonical Thai surface; subsequent occurrences use the canonical form only.

Cost: ~5 surgical verse-edits across chs 2-3, 7 + doc-amendment to `ot_warfare_ethics_2026-05.md` adding the Thai-surface lock section + ~4 back-pointer Layer-2 footers in chs 2-3, 7, 13 pointing to the DEU 20:17 anchor footer.

**Two questions:**

1. Should the project normalize the 5 distinct DEU ḥerem surface forms to a single canonical Thai (recommend **"ทุ่มถวายเพื่อทำลาย"**) before tagging `book-deuteronomy-v1`? And should `ot_warfare_ethics_2026-05.md` be amended to lock the canonical Thai surface alongside its existing interpretive-frame guidance?

2. Should the chs 2-3, 7, 13, 25 ḥerem cluster receive back-pointer Layer-2 footers (pointing to the rich DEU 20:17 anchor footer), or is the single anchor footer sufficient for readers who progress through the book in chapter-order?

---

## Item E — DEU 32:43 LXX/Heb 1:6 expansion: confirm asymmetric text-critical disposition

**The textual situation.** DEU 32:43 has two distinct textual witnesses:

- **MT (shorter form):** "Rejoice, O nations, with his people, for he avenges the blood of his servants and renders vengeance on his foes; he atones for his land and people."
- **LXX + 4QDeut^q (longer form):** "Let the heavens rejoice with him, and let **all the sons of God / angels of God worship him**…" — the line **Hebrews 1:6 quotes verbatim** as proof of Christ's superiority over angels.

**Eremos shipped form** (DEU 32:43): the **MT shorter form** with a Layer-2 footer in `output/textual_variants/deuteronomy_32.json` naming the LXX expansion + the Hebrews 1:6 quote.

**The cross-decision tension.** The same chapter contains the related DEU 32:8 sons-of-God textual variant. Eremos handled 32:8 by **following the DSS (4QDeut^j) + LXX reading** ("ตามจำนวนของบุตรของพระเจ้า") **rather than MT** (בני ישראל) — with a Layer-2 footer explaining the choice + the divine-council theology.

**The two adjacent text-critical decisions in DEU 32 diverge in disposition:**
- **32:8 → followed DSS/LXX** (rejected MT)
- **32:43 → followed MT** (rejected LXX/4QDeut^q expansion)

**Editorial assessment.** The asymmetry is **defensible** because the textual evidence is asymmetric:
- **32:8** has both DSS Hebrew witness (4QDeut^j) AND LXX corroboration — a strong case for following the non-MT reading.
- **32:43** has DSS Hebrew witness (4QDeut^q, later) + LXX corroboration — the witness is later and weaker.

The DEU 32:43 Layer-2 footer **currently does not name this asymmetric-witness rationale explicitly**. A reader comparing 32:8 and 32:43 footers will see two different dispositions without knowing why.

**The principled question.** Should Pentateuchal-corpus text-critical decisions consistently favor:
- (a) **MT-with-Layer-2-for-LXX-expansions** (the conservative-MT-base default + transparent Layer-2 for major NT-cited LXX divergences); 
- (b) **DSS/LXX-where-Greek-evidence-is-corroborated-by-DSS** (the eclectic-text approach);
- (c) **mixed disposition based on asymmetric witness-evidence** (current Eremos practice — 32:8 path (b), 32:43 path (a)).

Currently DEU 32 splits — confirm whether the asymmetric disposition is principled or accidental, and amend the 32:43 footer wording to name the rationale.

**Recommended:** Path (c) with footer wording-amendment. Amend the DEU 32:43 Layer-2 footer to explicitly say: "DEU 32:43 follows MT because the LXX expansion (= Heb 1:6 quotation) has only 4QDeut^q late-witness corroboration on the Hebrew side; DEU 32:8 differs because it has 4QDeut^j strong-witness corroboration." This makes the asymmetric-witness rationale visible to readers.

**Two questions:**

1. Should DEU 32:43 ship as MT-with-Layer-2 (current practice) or be lifted to the LXX/4QDeut^q expanded form (matching the Heb 1:6 NT quote)? The asymmetric-witness rationale is defensible; confirming the disposition before tagging closes the question.

2. If the asymmetric disposition stays (path c above), should the DEU 32:43 Layer-2 footer be amended to explicitly name the witness-asymmetry rationale (so a reader comparing the 32:8 + 32:43 footers sees why the two text-critical decisions diverge)?

---

## Item F — DEU within-book place-name drifts: Pisgah at 34:1 + Seven-Nations at 20:17

**Two within-DEU mechanical-fix drifts** — both single-character or single-prefix corrections that improve internal consistency. These are REVIEW-tier (not DECIDE) but consolidated here for the external review's awareness.

### F1. Pisgah פִּסְגָּה — within-DEU drift

| Verse | Thai |
|---|---|
| 3:17 | **พิ**สกาห์ |
| 3:27 | **พิ**สกาห์ |
| 4:49 | **พิ**สกาห์ |
| **34:1** | **ปิ**สกาห์ |

The same Hebrew פִּסְגָּה renders four times in DEU with one drift at the final chapter (single-character drop: **พ → ป** at the head). Cost: 1 surgical edit at DEU 34:1.

### F2. Seven-Nations ethnonym + prefix drift between DEU 7:1 and 20:17

| Position | DEU 7:1 (7-nation list) | DEU 20:17 (6-nation list) |
|---|---|---|
| Prefix | **ชาว**ฮิตไทต์ / ชาวเกอร์กาชี / ชาวอาโมไรต์ / ชาวคานาอัน / **ชาวเปริซซี** / **ชาวฮีไว** / **ชาวเยบุส** | **คน**ฮิตไทต์ / [no Girgashites] / คนอาโมไรต์ / คนคานาอัน / **คนเปริสซีต** / **คนฮีไวต์** / **คนเยบุสีต** |

The drifts: (1) Prefix "**ชาว**" (7:1) vs "**คน**" (20:17); (2) ethnonym suffix: เปริซซี/เปริสซีต, ฮีไว/ฮีไวต์, เยบุส/เยบุสีต. Both passages use the same Hebrew lemma set (פְּרִזִּי, חִוִּי, יְבוּסִי). The DEU 20:17 -ต suffix appears to be a Thai-language plural-marker that the rest of the corpus does not apply.

Recommend normalizing DEU 20:17 to match DEU 7:1's surface (ชาว- prefix; bare ethnonym).

**Two questions:**

1. Should DEU 34:1 ปิสกาห์ be normalized to พิสกาห์ to match DEU 3:17 + 3:27 + 4:49? (And as a parallel within-DEU drift category, should `glossary.json` be amended to lock the seven-nations ethnonym cluster as the corpus surface, so DEU 20:17 can be normalized to match DEU 7:1?)

2. Are there any defensible reasons to preserve the DEU 20:17 -ต suffix on the three ethnonyms (เปริสซีต / ฮีไวต์ / เยบุสีต) — e.g., as a Thai-language plural-marker for a specific narrative context — or is this a clean drift to normalize across the OT-pilot corpus?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
