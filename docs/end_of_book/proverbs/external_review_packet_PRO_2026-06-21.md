# Proverbs — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-21**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Proverbs** (31 chapters, 915 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah complete (not yet tagged). Proverbs 31/31 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Proverbs — External Review Items

Source: `docs/end_of_book/proverbs/PRO_END_OF_BOOK_REVIEW_2026-05-31.md` (§2 audit). These are the REVIEW / DECIDE items where independent eyes (Hebrew + Thai) add value beyond Claude's own corpus-level self-review. Each block carries verse evidence inline; the closing **Question** becomes a YAML reviewer question.

## Item A — Human-king register: non-royal (the headline editorial decision)

Proverbs has many king/ruler proverbs. The Eremos rendering keeps **human kings non-royal** — reserving Thai divine-royal register (ทรง / พระองค์ / พระพิโรธ / พระพักตร์ / พอพระทัย) for God alone, so "พระองค์" is unambiguously God across the whole corpus.

- **Prov 16:14** `חֲמַת־מֶלֶךְ` → "**ความโกรธของกษัตริย์**เป็นทูตแห่งความตาย" (not พระพิโรธ)
- **Prov 16:15** `פְּנֵי־מֶלֶךְ` → "เมื่อ**สีหน้าของกษัตริย์**แจ่มใส" (not พระพักตร์)
- **Prov 25:2** `כְּבֹד אֱלֹהִים … כְּבֹד מְלָכִים` → "**พระเกียรติของพระเจ้า** … **เกียรติของกษัตริย์**" (God's glory royal, king's honor plain)
- **Prov 21:1** the king's heart is in the LORD's hand → ใจของกษัตริย์ (plain) vs. องค์พระผู้เป็นเจ้า…พระหัตถ์ (royal)

This is consistent with the Psalms precedent (Pharaoh, Davidic king rendered non-royally). The trade-off: Thai cultural norm uses ราชาศัพท์ for kings, so a Thai reader might expect light royal register in the king-proverbs.

**Question:** Should human kings in Proverbs (and the OT court narratives ahead) be rendered with plain/non-royal Thai to reserve royal register for God, or should culturally-natural Thai ราชาศัพท์ be used for human kings (accepting that "พระองค์" then becomes context-dependent)?

## Item B — `אֶרֶךְ אַפַּיִם` "slow to anger / patient" consistency

`check_phrase_consistency` flags an inconsistency in this idiom across four proverbs:

- **Prov 15:18** `אֶרֶךְ אַפַּיִם` → "ผู้ที่**โกรธช้า**ก็ระงับการทะเลาะ"
- **Prov 16:32** `אֶרֶךְ אַפַּיִם` → "ผู้ที่**โกรธช้า**ก็ดีกว่านักรบ"
- **Prov 14:29** `אֶרֶךְ אַפַּיִם` (vs. `קְצַר־רוּחַ` "quick-tempered") → "คนที่**อดทน**มีความเข้าใจอันยิ่งใหญ่ … คนใจร้อน…"
- **Prov 25:15** `אֹרֶךְ אַפַּיִם` → "ด้วย**ความอดทน** ผู้ครอบครองก็ถูกโน้มน้าวได้"

โกรธช้า (slow to anger) vs. อดทน/ความอดทน (patience) — both faithful, but inconsistent. The same idiom appears in the Exod 34:6 formula (Psalms PR #188).

**Question:** Should `אֶרֶךְ אַפַּיִם` be rendered uniformly (e.g. ผู้ที่โกรธช้า for "slow to anger"), or is it acceptable to vary between โกรธช้า and อดทน by context (e.g. retaining อดทน at 14:29 where the antonym is "quick-tempered")?

## Item C — Lady Wisdom → Christ (8:22 `קָנָנִי`; 30:4 "His Son")

Prov 8:22 (`יְהוָה קָנָנִי רֵאשִׁית דַּרְכּוֹ`) is rendered **"องค์พระผู้เป็นเจ้าทรงให้เราถือกำเนิดเป็นปฐมแห่งพระมรรคาของพระองค์"** ("brought me forth," matching the birth-language of 8:24–25), with a footnote on the קנה range (possess/acquire/beget/create), the LXX `ἔκτισέν` "created" + the Arian controversy, and the NT Wisdom→Christ link (1 Cor 1:24,30; Col 1:15–17). Prov 30:4 ("what is the name of His Son?" `בְּנוֹ`) carries a parallel footnote (John 3:13).

**Question:** Is "ทรงให้เราถือกำเนิด" (brought forth, not created) the right rendering of `קָנָנִי` at 8:22, and is the footnote framing of the Wisdom→Christ connection (8:22; 30:4) doctrinally sound and appropriate for a Thai Buddhist-background readership?

## Item D — The rod of discipline (`שֵׁבֶט`) framing

The "rod" proverbs (13:24 "he who spares the rod hates his son"; 22:15; 23:13–14; 29:15) are rendered faithfully (ไม้เรียว) with a Tier-2 footnote framing the rod as *loving discipline/correction* (מוּסָר) — explicitly not abuse — tied to God's loving discipline (3:11–12 / Heb 12:6).

**Question:** Is the pastoral footnote framing of the "rod" proverbs (loving correction, not harshness) appropriate and clear for a Thai readership, given contemporary sensitivity around corporal discipline?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
