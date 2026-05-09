# Jonah — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-09**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Jonah** (4 chapters, 48 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged; Revelation complete (not yet tagged). Jonah 4/4 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — JON 4:2 + JON 2:9 חֶסֶד (chesed) cross-corpus drift vs Ruth's lock

**The cross-corpus pattern (and the first-OT-book-to-second-OT-book consistency question):** Ruth shipped חֶסֶד uniformly as **ความรักมั่นคง** ("steadfast love") at all 3 occurrences (RUT 1:8, 2:20, 3:10). Jonah is the second OT book in the corpus to exercise the lemma — and **Jonah uses two new renderings, neither matching Ruth**. No corpus-doc lock exists yet (the Ruth audit recommended writing one before Pss; the doc was not written before Jonah shipped).

| Verse | Hebrew | Thai (current Jonah) |
|---|---|---|
| RUT 1:8 (already shipped) | יַעַשׂ יְהוָה ... חֶסֶד | **ขอองค์พระผู้เป็นเจ้าทรงสำแดงความรักมั่นคง** |
| RUT 2:20 (already shipped) | (אֲשֶׁר) לֹא־עָזַב חַסְדּוֹ | **ผู้ไม่ทรงละทิ้งความรักมั่นคงของพระองค์** |
| RUT 3:10 (already shipped) | חַסְדֵּךְ הָאַחֲרוֹן מִן־הָרִאשׁוֹן | **ความรักมั่นคงของเจ้าในครั้งหลังนี้ยิ่งใหญ่กว่าครั้งก่อน** |
| **JON 2:9** | חַסְדָּם יַעֲזֹבוּ | **ทอดทิ้งพระเมตตาที่พวกเขาควรได้รับ** ← lemma flattened to plain "mercy"; "their" suffix unpacked into a relative clause |
| **JON 4:2** | וְרַב־חֶסֶד | **ทรงบริบูรณ์ด้วยพระเมตตาเชิงพันธสัญญา** ← compound rendering; "covenant-dimension" qualifier inserted to mark the technical sense within the Exod-34 attribute formula |

The 2:9 KD names the ambiguous-suffix exegetical-crux (option 1: "the chesed they could have received from YHWH" — BSB/ESV/NIV; option 2: "their own loyalty that they abandon"). Eremos resolves to option 1 and **flattens the Hebrew lemma into plain พระเมตตา + a relative clause** to surface the resolution.

The 4:2 KD names the Exod 34:6–7 echo + Jonah-specific addendum (וְנִחָם עַל־הָרָעָה), with the chesed-component lifted into a 9-syllable compound **พระเมตตาเชิงพันธสัญญา** ("mercy-of-covenant-dimension") to flag the technical covenant-loyalty sense.

**Why this matters forward:** The Exod-34 attribute formula recurs verbatim or near-verbatim at **Ps 86:15, Ps 103:8, Ps 145:8, Joel 2:13, Nah 1:3, Neh 9:17, 2 Chr 30:9** (and is alluded to in many more Psalms). חֶסֶד occurs **~245 times in the OT** including ~127 in the Psalms alone. Each future occurrence will need to map cleanly back to the same Thai lemma — and the current 3-way split (ความรักมั่นคง / พระเมตตา / พระเมตตาเชิงพันธสัญญา) breaks that mapping.

**Two questions:**
1. Should JON 2:9 + 4:2 be re-translated to align with Ruth's **ความรักมั่นคง** lock for cross-corpus consistency? Specifically:
   - JON 2:9: **ทอดทิ้งความรักมั่นคงที่พวกเขาควรได้รับ** (preserves the suffix-resolution + locks to Ruth's lemma)
   - JON 4:2: **ทรงบริบูรณ์ด้วยความรักมั่นคง** (drops the "เชิงพันธสัญญา" qualifier; trusts that future Pss/Joel/Nah readings will compound the covenant-sense via repetition)
2. Is the trade-off worth it? **Ruth-lock-wins** preserves the lemma-recurrence for Thai readers across 245 future occurrences but loses Jonah's contextual qualifier. **Jonah-context-preserved** keeps the 4:2 attribute-formula's covenant-emphasis but creates a 3-way Thai split that maps poorly back to the single Hebrew lemma.

The decision compounds critically into the new corpus doc `chesed_covenant_love_2026-05.md` (recommended by both the Ruth and Jonah audits) and into the related `exod_34_attribute_formula_2026-05.md` doc that will lock the 6-component formula's Thai before its 7+ canonical recurrences.

---

## Item B — JON 4:11 right-hand/left-hand interpretive crux: book's closing climactic line

**The textual question:** The book of Jonah ends on a rhetorical question whose force depends on a famously-debated phrase:

- GK / Hebrew: `אֲשֶׁר לֹא־יָדַע בֵּין־יְמִינוֹ לִשְׂמֹאלוֹ` ("who do not know between their right hand and their left")
- TH (current): `**ผู้ไม่รู้จักแยกแยะมือขวาจากมือซ้ายของตน**` (literal "do not know how to distinguish their right hand from their left")

Two well-attested readings:

| Reading | Implication for Jonah's theology |
|---|---|
| (1) **Children too young to distinguish left from right** (≈ ages 3–4) | The 120,000 are small children; total Nineveh population ~600,000+. YHWH's mercy is for the genuinely-innocent. Matches archaeological greater-Nineveh estimates. |
| (2) **Morally ignorant** (do not know good from evil in the ethical sense) | The 120,000 are the entire morally-undiscerning Ninevite adult population. YHWH's mercy is for the genuinely-guilty. The book's protest reads as "God shows mercy to those who don't deserve it." |

**The current Eremos approach:** Surface-literal Thai + a Layer-2 reader-edition footnote in `output/textual_variants/jonah_04.json` that explicitly names BOTH readings (`type: interpretive_crux_footnote`):
> "ฉบับเอเรโมสรักษาความเป็นสองนัยของต้นฉบับฮีบรูไว้โดยแปลตรง ผู้อ่านสามารถพิจารณาเลือกความหมายได้เอง — ทั้งสองความหมายสนับสนุนข้อโต้แย้งของพระเจ้าเรื่องพระเมตตาที่กว้างขวาง" ("Eremos preserves the dual-sense of the Hebrew by direct translation; the reader may choose between the meanings — both readings support God's argument about wide-reaching mercy.")

**Editorial concern:** A typical Thai reader of the surface text alone will read **"ผู้ไม่รู้จักแยกแยะมือขวาจากมือซ้าย"** as a description of small children (the surface Thai is unambiguously physical-spatial; "ไม่รู้จักแยกแยะมือขวาซ้าย" is the Thai idiom for "naive / can't tell their right from left," which colloquially means small children). The moral-ignorance reading is accessible only through the reader-edition footnote — and only if the Eremos rendering layer surfaces the footnote prominently.

**Three resolution paths:**

(a) **Current** — surface-literal Thai + reader-edition footnote covering both readings. Lowest-risk; preserves the Hebrew dual-sense; but defaults the surface meaning to children-reading for typical Thai readers.

(b) **Lift the moral-ignorance reading into the main text** — e.g., **ผู้ที่ไม่รู้ผิดชอบดีชั่ว** ("who do not know right-from-wrong"). Locks the moral-ignorance reading; loses the surface dual-sense; commits the climactic line to one interpretation.

(c) **Surface-literal main text + an inline parenthetical** — e.g., `ผู้ไม่รู้จักแยกแยะมือขวาจากมือซ้ายของตน (หมายถึงเด็กเล็ก หรือผู้เขลาทางศีลธรรม)` ("...meaning either small children or the morally-ignorant"). Surfaces the ambiguity directly to the reader without requiring them to find the footnote. Slight prose-flow cost.

**Two questions:**
1. Is the dual-sense preservation strategy (option a) theologically adequate, given that the climactic-line is the book's closing rhetorical force? Or does the closing line warrant an inline mechanism (option c) that doesn't depend on the footnote-rendering layer?
2. Independent of the rendering choice: should the textual_variants reader-edition footnote be elevated in the Eremos rendering layer (e.g., presented as an inline-superscript-marker in the Thai prose, not just as an end-of-chapter note) for the book's climactic verse specifically?

---

## Item C — JON 1:4 טוּל "hurl" Leitmotiv — verb-divergence at the divine-action-occurrence

**The chapter-spanning verbal echo (which the Hebrew narrator deliberately constructs across vv.4–15):**

| Verse | Subject | Object | Hebrew | Thai (current) |
|---|---|---|---|---|
| JON 1:4 | YHWH | רוּחַ גְּדוֹלָה (great wind) | הֵטִיל | **ทรงบันดาลให้...พัดมา** ("caused to blow") |
| JON 1:5 | sailors | כֵּלִים (cargo) | וַיָּטִלוּ | **โยน** ("throw") |
| JON 1:12 | Jonah → sailors (imperative) | אֹתִי / נַפְשִׁי | הֲטִילֻנִי | **จับ...โยน** ("seize and throw") |
| JON 1:15 | sailors | יוֹנָה | וַיָּטִלוּ | **โยน** ("throw") |

**The narrative-design point:** The Hebrew narrator reuses טוּל across all four verbs — God hurls wind → sailors hurl cargo → Jonah asks to be hurled → sailors hurl Jonah. The thematic force: God's action initiates a chain that ends with the sailors hurling Jonah; the prophet becomes the cargo. The verbal echo is the chapter's theological hinge.

**The Thai breaks the verbal echo at v.4** because the modern Thai verb โยน (lit. "throw a discrete object") does not naturally apply to wind. The 1:4 KD names the trade-off explicitly:

> "The Thai rendering ทรงบันดาลให้...พัดมา preserves the divine causation while reading naturally; the harsher 'ทรงโยน' would sound non-Thai-idiomatic for wind."

The thai_literal field at 1:4 already preserves the literal hurling-reading (`ทรงโยนลมใหญ่ลงสู่ทะเล`) — the verbal echo lives in the literal-layer but not in the prose-layer.

**Three options:**

(a) **Current** — ทรงบันดาลให้ลม...พัดมา at 1:4; โยน at 1:5/12/15. Verbal echo broken at the divine-occurrence; Thai natural.

(b) **Force the echo** — render 1:4 as **ทรงโยนลมพายุใหญ่ลงสู่ทะเล** (literal "hurled a wind into the sea"). Preserves the four-fold verbal echo at the cost of Thai naturalness; modern Thai readers may pause on "hurl-a-wind" as un-idiomatic.

(c) **Compromise** — keep 1:4 as ทรงบันดาล + add a chapter-level reader-edition note (output/textual_variants/jonah_01.json) that names the four-fold hurling-chain in Hebrew. Verbal echo not surface-preserved but reader awareness restored.

**Compounds forward:** Future leitwort decisions of similar shape will recur in Genesis 12 (לֵךְ-לְךָ to Abram + לֵךְ-לְךָ to Isaac in Gen 22 — same verb same imperative same theological pivot) and in many Pss-Lamentations cognate-accusative patterns. Establishing a **leitwort handling policy doc** (`docs/translator_decisions/leitwort_handling_policy_2026-05.md`) now would lock the trade-off principle for forward decisions.

**Two questions:**
1. Is option (a) — the current rendering — the right call? The Thai-naturalness argument is principled; the cost is the lost verbal-design at the chapter's narrative pivot.
2. Should the project adopt a meta-doc on leitwort handling that formalizes when Hebrew lexical-recurrence yields to Thai naturalness (and when it doesn't — see §JON-5 the four-fold ทรงจัดเตรียม leitmotiv where Thai DOES tolerate the verbal echo)?

---

## Item D — JON 4:6 קִיקָיוֹן (qiqayon plant) botanical-identity reader-edition note

**The textual question:** The plant Jonah sits under at JON 4:6 (and that the worm destroys at 4:7) is **קִיקָיוֹן** — a Hebrew lemma occurring ONLY in Jonah 4 (5×, vv.6/7/9/10). Its botanical identity has been debated for ~2400 years:

| Tradition | Identification | Notes |
|---|---|---|
| LXX (3rd c. BCE) | κολοκύνθη ("gourd") | Standard Greek tradition; influenced Latin & European versions |
| Jerome / Vulgate (4th–5th c. CE) | hedera ("ivy") | Sparked the famous Augustine-Jerome dispute (Augustine objected to Jerome changing the LXX gourd) |
| Modern Hebrew lexicons (BDB, HALOT) | castor-bean (Ricinus communis) | Botanical match: rapid growth + large palmate leaves casting shade |
| Some modern English translations | "vine" / "leafy plant" / "bush" | Avoids the species-specificity question |

**Current Thai:** **ต้นน้ำเต้า** ("gourd plant"), uniform across all 5 occurrences. Aligns with the LXX tradition.

The 4:6 KD names the LXX precedent + the botanical reasons for choosing gourd (rapid overnight growth per v.10 "son-of-night-begotten plant"; toxic-pod problem with castor; ต้นน้ำเต้า is a familiar Thai plant).

**The reader-edition footnote at JON 4:6 in `output/textual_variants/jonah_04.json` does NOT currently mention the botanical-crux** (it covers the divine-name compound יהוה־אלהים and the Eden-Genesis-2 echo, not the plant identity).

**Question:** Should the reader-edition footnote at JON 4:6 add a botanical-crux note (LXX-gourd vs Jerome-ivy vs modern-castor-bean)? Adds scholarly transparency without changing the main-text rendering. The footnote could read approximately:

> "**ต้นน้ำเต้า** (קִיקָיוֹน, qiqayon) — เป็นพืชเฉพาะที่ปรากฏเพียงครั้งเดียวในพระคัมภีร์ฮีบรู (โยนาห์ 4 บทเดียว) นักวิชาการได้ถกเถียงถึงพืชชนิดนี้มากว่า 2,400 ปี ฉบับ LXX (กรีก) แปลว่า 'น้ำเต้า' (κολοκύνθη); เซนต์เจอโรม (ละติน) แปลว่า 'ไม้เลื้อย' (hedera) ซึ่งทำให้เกิดข้อโต้แย้งกับเซนต์ออกัสติน นักวิชาการสมัยใหม่ส่วนหนึ่งระบุว่าน่าจะเป็น 'ต้นละหุ่ง' (Ricinus communis) ฉบับเอเรโมสใช้ 'ต้นน้ำเต้า' ตามฉบับ LXX ซึ่งเป็นฉบับเก่าแก่ที่สุด"

This is a **footnote-only decision** (no main-text translation change). Confirm whether to add.

---

## Item E — JON 1:6 captain's אֱלֹהִים → พระเจ้า: pre-conversion register-elevation

**The textual question:** The Phoenician ship-captain at JON 1:6 says:

- GK/Hebrew: `אוּלַי יִתְעַשֵּׁת **הָאֱלֹהִים** לָנוּ וְלֹא נֹאבֵד` ("perhaps **the God** will consider us and we will not perish")
- TH (current): `บางที**พระเจ้า**จะทรงคำนึงถึงเรา และเราจะไม่พินาศ`

**The register choice:** Thai **พระเจ้า** is the corpus's reserved-for-YHWH form (per `pagan_deities_2026-04.md` extended into the OT). In adjacent JON 1:5, the same sailors' polytheistic prayer to "his god" (אֱלֹהָיו) is rendered with the plain pagan register **พระของตน** (no royal pre-fix). At JON 1:6, the captain — same character-group, no time-elapsed conversion-event — speaks the elevated **พระเจ้า**.

**The exegetical question on the Hebrew:** הָאֱלֹהִים here is articular ("the deity-in-question") but does not commit the captain to monotheism. Most modern English translations preserve the ambiguity:
- BSB: "this God"
- ESV: "the god"
- NIV: "the god"
- NRSV: "the god"

The 1:6 KD frames the captain's language as **"unconscious deferential elevation — the captain is ascending from polytheistic frame toward monotheistic recognition"** (fully realized at 1:14 when the sailors call YHWH by covenant-name + 1:16 when they sacrifice to YHWH). The current Thai rendering anticipates the conversion arc by elevating the captain's speech-act now.

**Three options:**

(a) **Current** — พระเจ้า at 1:6, framing the captain as unconsciously-elevating. Reader-friendly + theologically loaded (the captain unwittingly invokes YHWH; the irony serves the sailor-conversion narrative arc).

(b) **Match 1:5 plain register** — render 1:6 as **บางทีพระจะทรง...** (plain พระ-, no พระเจ้า) to align with the same character-group's same-frame pagan-prayer at 1:5. The 1:14/1:16 conversion-arc still works without 1:6's pre-emptive elevation.

(c) **Use the pagan-deity register lemma** — เทพเจ้า ("deity," per `pagan_deities_2026-04.md`) at 1:6 for the captain's speech. Distinguishes from 1:5's individual pagan-gods (พระของตน) and from 1:14's covenant-name (องค์พระผู้เป็นเจ้า) — three-step register progression.

**Question:** Which option best serves the Thai reader's theological-narrative awareness of the sailors' three-stage conversion arc (1:5 polytheistic → 1:6 deferential → 1:14/1:16 YHWH-by-covenant-name)? The rendering compounds into similar pre-conversion register-decisions in Acts 17:23 ("to an unknown god" — Paul to the Athenians) and the Cornelius narrative (Acts 10).

---

## Item F — JON 4:2 + 3:9 + 3:10 נִחַם divine-relenting: anthropomorphism + apparent-paradox

**The pattern:** Three occurrences of נִחַם (Niph'al, "be sorry, relent, change-mind") with God as subject, all rendered uniformly **ทรงเปลี่ยนพระทัย** ("change [royal] mind"):

| Verse | Hebrew | Thai | Speaker / register |
|---|---|---|---|
| JON 3:9 | יָשׁוּב וְנִחַם הָאֱלֹהִים | **พระเจ้าอาจจะทรงหันและเปลี่ยนพระทัย** | Ninevite king (cautious-hope conditional) |
| JON 3:10 | וַיִּנָּחֶם הָאֱלֹהִים עַל־הָרָעָה | **พระเจ้าจึงทรงเปลี่ยนพระทัยเรื่องเหตุร้าย** | Narrator (factive — God actually relented) |
| JON 4:2 | וְנִחָם עַל־הָרָעָה | **ทรงเปลี่ยนพระทัยจากการลงโทษ** | Jonah (citing Exod 34 + adding the relenting-clause as protest-rhetoric) |

**The literal-rendering policy** preserves the OT anthropomorphism per `hebrew_idioms_and_metaphor_2026-05.md` §1.4 (body-part-as-object-of-divine-verb takes royal-Thai noun + ทรง-on-verb — the implicit Ruth-1:13 rule). Thai readers face the same theological tension as Hebrew readers face vs:
- **Num 23:19** לֹא אִישׁ אֵל וִיכַזֵּב וּבֶן־אָדָם וְיִתְנֶחָם ("God is not a man that he should change his mind")
- **1 Sam 15:29** וְגַם נֵצַח יִשְׂרָאֵל לֹא יְשַׁקֵּר וְלֹא יִנָּחֵם ("the Glory of Israel will not lie or change his mind")

PR #133 added a Layer-2 textual_variants note ("divine-anthropomorphism note") at JON 3 explicitly acknowledging the נִחַם anthropomorphism for reader-edition consumption.

**Mainstream evangelical resolution** (per Jer 18:7–10): God's character is unchanging, but his responsive-judgment to human repentance is itself a stable covenant-feature. Jeremiah 18 makes this explicit: God's word to a nation about either weal or woe is conditional on that nation's turning.

**Two questions:**
1. Is the literal-rendering policy (ทรงเปลี่ยนพระทัย at all 3 occurrences) the right corpus-default for divine נִחַם? Or should the rendering be flexed contextually (e.g., "ทรงโปรดเปลี่ยน" / "ทรงทรงเลิก" at the factive 3:10 to avoid the surface-paradox)? Compounds into Joel 2:13–14, Amos 7:3+6, Jer 18:8/10, 26:3+13+19, 42:10 (~10 more divine-נִחַם occurrences in the prophetic corpus).
2. Should the project write a corpus doc `docs/translator_decisions/nicham_divine_relenting_2026-05.md` that names BOTH the literal-rendering policy AND the Num 23:19 / 1 Sam 15:29 counter-formulae, so the reader-edition has a single referenced location for the theological-paradox + the Jer 18:7–10 resolution? The doc would lock ทรงเปลี่ยนพระทัย as the corpus-default before the prophetic-relenting cluster ships.

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
