# Psalms — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-21**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Psalms** (150 chapters, 2,527 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah complete (not yet tagged). Psalms 150/150 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Psalms — External Review Items

Source: `docs/end_of_book/psalms/PSA_END_OF_BOOK_REVIEW_2026-05-31.md` (§2 audit). These are the REVIEW / DECIDE items where independent eyes (Greek/Hebrew + Thai) add value beyond Claude's own corpus-level self-review. Each block carries verse evidence inline; the closing **Question** becomes a YAML reviewer question.

## Item A — Exod 34:6 compassion-formula (`חַנּוּן וְרַחוּם`) lexeme consistency

The "gracious and compassionate, slow to anger, abounding in steadfast love" formula recurs across the Psalter (echoing Exod 34:6). `check_phrase_consistency.py` flags an inconsistency in how `רַחוּם` ("compassionate") is rendered:

- **Ps 103:8** `רַחוּם וְחַנּוּן יְהוָה` → "องค์พระผู้เป็นเจ้าทรงเปี่ยมด้วย**พระเมตตา**และพระคุณ ทรงกริ้วช้า…"
- **Ps 86:15** `אֵל־רַחוּם וְחַנּוּן` → "พระเจ้าผู้เปี่ยมด้วย**พระเมตตา**และพระคุณ…"
- **Ps 111:4** `חַנּוּן וְרַחוּם יְהוָה` → "ทรงเปี่ยมด้วยพระคุณและ**พระเมตตา**"
- **Ps 145:8** `חַנּוּן וְרַחוּם יְהוָה` → "ทรงเปี่ยมด้วยพระคุณและ**ความเมตตากรุณา**"  ← the outlier

`רַחוּם` = พระเมตตา in three places but **ความเมตตากรุณา** at 145:8 (chosen to avoid the honorific `พระกรุณา`/`พระกร` body-part trap, but `พระเมตตา` is itself trap-free and already the established form). The audit recommends normalizing 145:8 to `พระเมตตา`.

Two notes: (1) the **word order** legitimately varies with the MT (compassion-first `רַחוּם וְחַנּוּן` at 86:15/103:8 vs. grace-first `חַנּוּן וְרַחוּם` at 111:4/145:8) — should the Thai preserve Hebrew order, or fix one canonical order for the formula? (2) Ps 112:4 applies the same pair to the *righteous man* (plain ความเมตตา, no royal พระ-) — correct to keep distinct.

**Question:** Should `רַחוּם` be rendered uniformly as พระเมตตา across all divine occurrences of the Exod 34:6 formula (normalizing Ps 145:8 from ความเมตตากรุณา), and should the Thai preserve the Hebrew word-order variation or standardize the formula's order?

## Item B — Imprecatory-psalm footnote frame

The Psalter's imprecatory passages (137:8–9 "dashes your infants against the rocks"; 139:19–22 "do I not hate those who hate You"; 140:9–11 "burning coals"; 149:6–9 "a double-edged sword in their hands… vengeance on the nations") are rendered **faithfully and unsoftened** from the MT, each with a Tier-2 pastoral footnote using a consistent four-part frame:

> (1) faithful unsoftened rendering; (2) vengeance entrusted to God, not self-executed (Deut 32:35 / Rom 12:19); (3) lex talionis / God's righteous judgment; (4) NT trajectory — Christ's call to love enemies (Matt 5:44) + the spiritual-warfare / eschatological-judgment reading (Eph 6:17, Heb 4:12, Rev 19:15).

Example (Ps 137:9 footnote, abridged): *"…ฉบับเอเรโมสแปลตามต้นฉบับภาษาฮีบรูอย่างซื่อตรง ไม่ตัดทอน… ผู้ประพันธ์มอบการแก้แค้นไว้กับพระเจ้า ไม่ลงมือเอง… ในพระคริสต์ ผู้เชื่อได้รับการทรงเรียกให้รักศัตรู (มธ 5:44)…"*

**Question:** Is the four-part pastoral-footnote frame the right corpus-level approach for the imprecatory psalms (faithful text + theological/NT framing in the footnote), and is the Thai framing pastorally and theologically sound for a Thai Buddhist-background readership?

## Item C — Ps 145:13 missing-נun verse (MT vs. 11QPsaᵃ/LXX/Syriac)

Ps 145 is an alphabetic acrostic, but the MT **omits the נun verse** (jumps מ at v13 → ס at v14). 11QPsaᵃ (Dead Sea Scrolls Hebrew), the LXX, and the Syriac all carry it, and most modern translations supply it. The Eremos rendering keeps the **MT as base** (v13 = the מ-line only) and places the נun line in a Tier-2 footnote, quoting it:

> נֶאֱמָן יְהוָה בְּכָל־דְּבָרָיו וְחָסִיד בְּכָל־מַעֲשָׂיו → "องค์พระผู้เป็นเจ้าทรงสัตย์ซื่อในพระวจนะทั้งสิ้นของพระองค์ และทรงเปี่ยมด้วยความรักในพระราชกิจทั้งปวงของพระองค์"

`bsb_english` for v13 was truncated to the מ-line to match the MT-based Thai (the supplied line lives only in the footnote).

**Question:** For an acrostic whose structure *requires* the נun line and where Hebrew manuscript evidence (11QPsaᵃ) supplies it, is MT-base-with-footnote the right call, or should the נun line be promoted into the verse text (as a v13b) with the footnote explaining the MT omission?

## Item D — `הַלְלוּ־יָהּ` → ฮาเลลูยาห์ (transliterate vs. translate)

The frozen liturgical frame `הַלְלוּ־יָהּ` opening/closing the Hallel psalms (104, 105, 106, 111–113, 115–117, 135, 146–150) is **transliterated** to ฮาเลลูยาห์ (like เซลาห์), while mid-clause `הַלְלוּ יָהּ` ("praise YAH", e.g. 135:3) is **translated** as จงสรรเสริญองค์พระผู้เป็นเจ้า.

**Question:** Is transliterating the framing `הַלְלוּ־יָהּ` as ฮาเลลูยาห์ (a form Thai Christians may recognize liturgically) the right choice, versus translating it as จงสรรเสริญองค์พระผู้เป็นเจ้า throughout for a readership without that liturgical background?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
