# Esther — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-29**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Esther** (10 chapters, 167 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings complete (not yet tagged). Esther 10/10 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — How should a foreign (Persian) monarch be honored in Thai? Esther is the third book of the Persian-court block, and now the SAME king (Ahasuerus/Xerxes) is rendered two different ways across Ezra and Esther

**The pattern:** Thai has a royal honorific register (ราชาศัพท์) — `ทรง` before verbs, `พระองค์` / `เสด็จ` / `พระ-` noun-elevation, `ตรัส` (royal "say") — that the Eremos translation reserves, per `ot_register_policy_2026-05.md`, for God and for kings. The book of Ezra (shipped) **deliberately deferred** the question of whether a *Gentile* emperor (Cyrus, Darius, Artaxerxes, Ahasuerus) should receive this register, parking it for a corpus decision spanning "Ezra–Nehemiah–Esther–Daniel." As shipped, **Ezra withholds `ทรง` from the Persian king in narrator voice** (commoner register, to match 2 Chr 36:23). **Nehemiah grants the same king full ราชาศัพท์ in narrator voice**, citing `ot_register_policy §2.2`. **Esther — where Ahasuerus/Xerxes is the central figure for all 10 chapters — does the same as Nehemiah**, and explicitly cites the Nehemiah precedent. All three books are shipped; none is tagged.

**Esther (full `ทรง`/`พระ-` for the king — narrator voice):**
- EST 1:1 HEB: `הַמֹּלֵךְ` → TH: `ผู้**ทรง**ครอบครอง` (KD: "จักรพรรดิต่างชาติ… ได้รับ ทรง- ในเสียงผู้เล่า แม้เป็นคนนอกพันธสัญญา… ตาม ot_register_policy §2.2")
- EST 1:3 HEB: `עָשָׂה מִשְׁתֶּה` → TH: `**ทรง**จัดงานเลี้ยง`
- EST 7:7 HEB: `קָם… בַּחֲמָתוֹ` → TH: `**ทรง**ลุกขึ้นด้วย**พระพิโรธ** … **เสด็จ**จากงานเลี้ยง`
- EST 8:2 HEB: `וַיָּסַר הַמֶּלֶךְ אֶת־טַבַּעְתּוֹ` → TH: `**ทรง**ถอด**พระธำมรงค์** … **พระราชทาน**`
- EST 10:2 HEB: `גִּדְּלוֹ הַמֶּלֶךְ` → TH: `กษัตริย์**ทรง**เลื่อนยศ`
- **EST 1:10** (the satirical drunk scene — register explicitly NOT downshifted) KD: "แม้ฉากนี้ออกเชิงเสียดสี (ทรงมึนเมา) ก็ยังคงราชาศัพท์ของจักรพรรดิตาม §2.2 'แม้เป็นตัวร้าย' — สงวนการลดทอนไว้สำหรับความผิดศีลธรรมร้ายแรง (เทียบดาวิด 2 ซมอ 11)… **สอดคล้องกับการคงราชาศัพท์ให้อารทาเซอร์ซีสในเนหะมีย์**"

**Ezra (no `ทรง` for the king — narrator voice), incl. the SAME king as Esther:**
- EZR 1:7 → TH: `กษัตริย์ไซรัส**ได้นำ**…ออกมา` (plain)
- EZR 6:1 → TH: `กษัตริย์ดาริอัสจึง**สั่ง**ให้ค้น` (plain)
- EZR 4:6 mentions **Ahasuerus/Xerxes** (`אֲחַשְׁוֵרוֹשׁ`) in narrator voice in the same commoner register — the very king Esther renders with full `ทรง` for 10 chapters.

**The policy tension:** `ot_register_policy §2.2`'s table *prescribes* the Nehemiah/Esther choice — its row reads "Foreign emperors (Pharaoh, Nebuchadnezzar, Cyrus, Darius, **Xerxes**) → ราชาศัพท์ (ทรง)… even if villainous." So Nehemiah and Esther follow the written rule and **Ezra is the outlier** — but Ezra's commoner-register choice (matching 2 Chr 36:23) was the one parked for ratification, and that ratification never happened. Separately and consistently in all three books, the *Hebrew* court-servant (Ezra; Nehemiah; **Mordecai**, who at 10:3 is "second to the king" yet held in plain register, the KD calling it "กรณีสุดยอดของหลัก §2.5") is plain per the §2.5 Joseph-vizier sub-rule — that part is not in question; only the *emperor's* register is.

**Forward-compounds to:** Daniel (Nebuchadnezzar, Belshazzar, Darius, Cyrus) — the last major Persian/Babylonian-court book.

**Two questions:** (1) Should a foreign emperor receive **full Thai royal honorifics in narrator voice** (the Nehemiah + Esther + written-`§2.2` approach — sovereignty, not covenant status, triggers ราชาศัพท์), or be held in **commoner register** in narrator voice (the Ezra / 2 Chr 36:23 approach), reserving deference for in-court reported speech only? (2) Whichever rule is chosen, it must be applied to **all three** shipped books (Ezra, Nehemiah, Esther) and written into a corpus doc before Daniel — so the same king (Ahasuerus, Artaxerxes) is not honored two different ways across a book boundary. Given that two of three books and the written policy already grant full ราชาศัพท์, should Ezra be the book normalized?

---

## Item B — The Persian "law/decree" word דָּת — the engine of Esther's plot — is rendered five ways, and the "irrevocable law of the Medes and Persians" motif is worded two ways

**The pattern:** `דָּת` (a Persian loanword, ~20× in Esther) drives the whole plot: the irrevocable royal edict that condemns the Jews, and the counter-edict that saves them. The translation renders it across a wide range:

| Thai | Refs | Apparent role |
|---|---|---|
| `พระราชโองการ` (royal ordinance) | 1:8 | king's standing order |
| `กฎหมาย` (law) | 1:15, 1:19, 8:13 | general statute / "the law" |
| `พระบัญชา` + `พระราชกำหนด` | 2:8 | royal command + regulation |
| `ระเบียบ` (regulation) | 2:12 | the women's beauty-regimen rule |
| `พระราชสาส์น` (royal letter/edict) | 3:12–13, 8:9 | a specific written, sealed edict |
| `พระราชกฤษฎีกา` (royal decree) | 9:1 | the decree taking effect |

**The irrevocability motif — a structural hinge of the book (the king cannot revoke Haman's decree, only counter it) — is itself worded two ways:**
- EST 1:19 HEB: `וְיִכָּתֵב בְּדָתֵי פָרַס־וּמָדַי וְלֹא יַעֲבוֹר` → TH: `…ในกฎหมายของชาวเปอร์เซียและมีเดียเพื่อจะ**เปลี่ยนแปลงไม่ได้**`
- EST 8:8 HEB: `כִּי־כְתָב אֲשֶׁר־נִכְתָּב בְּשֵׁם־הַמֶּלֶךְ… אֵין לְהָשִׁיב` → TH: `…หนังสือที่เขียนในนามของกษัตริย์… จะ**เพิกถอนไม่ได้**` (KD cross-refs: "กฎเปอร์เซีย เทียบ 1:19")

The tiering may be principled — `กฎหมาย` for an abstract statute, `พระราชสาส์น`/`พระราชโองการ` for a specific issued edict, `ระเบียบ` for a court regulation. The mechanical key-term checker is clean because `דָּת` is not a registered key term (so the variance is invisible to it, exactly like Nehemiah's `פֶּחָה` governor-title).

**Two questions:** (1) Is the contextual tiering of `דָּת` intended and correct (general statute vs specific issued edict vs court regulation), or should it collapse toward a smaller, more consistent set? (2) Should the "cannot be repealed" motif (`เปลี่ยนแปลงไม่ได้` at 1:19 / `เพิกถอนไม่ได้` at 8:8) be harmonized to a single wording so the irrevocable-law-of-the-Medes-and-Persians thread reads as one motif across the book?

---

## Item C — Esther and the Greek tradition: the six "Additions to Esther" supply the God the Hebrew omits — does the MT-anchored policy owe any disclosure?

**The pattern:** The Eremos OT is **MT-anchored** (`ot_canon_and_text_base_2026-05.md`); deuterocanonical material is excluded per `RULES §0`. Esther's textual situation is the most prominent deuterocanonical-expansion case the corpus has shipped: the **LXX Esther carries six large Additions (A–F, ~107 verses)** — Mordecai's apocalyptic dream, the texts of the two royal decrees, the prayers of Mordecai and Esther, Esther's unsummoned audience, and the dream's interpretation + a Purim colophon. The theological point: **the Additions insert explicit prayer and divine-name language that the Hebrew pointedly withholds** (the Hebrew Esther never names God — see Item D), and Catholic/Orthodox canons include them.

Eremos translates **MT Esther only**. The exclusion is documented in a single note at **1:1**: "ฐานต้นฉบับ: MT (เอสเธอร์ภาษาฮีบรู) — ไม่รวม 'ส่วนเพิ่มเติมของเอสเธอร์' ในฉบับ LXX ซึ่งเป็นหนังสือนอกสารบบของนิกายโปรเตสแตนต์ (ตาม RULES §0)." For verse-level MT-vs-LXX divergence the disposition is clean: `audit_inclusion_variants.py --book esther --strict` = 0 candidates; no textual-variant files (and none owed — the book has no Tetragrammaton, so no YHWH footnote). Under `mt_vs_lxx_textual_variant_handling_2026-05.md §2.3`, the Additions are a **separate recension / canonical-block question**, not a per-verse MT variant — the same disposition Ezra reached for 1 Esdras and Nehemiah for Esdras B (→ non-gap). But the Additions are *more* canonically visible than 1 Esdras and bear directly on the book's defining feature.

**Question:** Under the project's MT-anchored policy, does Esther owe any disclosure for the six LXX Additions — e.g. a single book-level note recording "MT Esther is the base; the LXX Additions A–F (~107 verses, incl. the prayers that name God) are deuterocanonical expansions excluded per RULES §0, not MT textual variants, so no per-verse disclosure is owed" — or is the single 1:1 note sufficient, given the verse-level inclusion audit is already clean?

---

## Item D — The Hebrew Esther never names God — yet hides the divine name in four acrostics. Should the Thai reader be told?

**The pattern:** Esther is the only book in the Hebrew Bible that never mentions God: no Tetragrammaton, no Elohim, no Adonai. The Eremos translation faithfully preserves the silence — a whole-book search of the rendered Thai text finds **zero** divine-name occurrences (the only mentions of `พระเจ้า` are in translator commentary at 1:1 and 10:3, never in Scripture). The providence hinges are rendered without naming a deliverer:
- EST 4:14 HEB: `יַעֲמוֹד… מִמָּקוֹם אַחֵר` → TH: `ความบรรเทาและการช่วยกู้สำหรับชาวยิวก็จะมาจากที่อื่น` (KD: "'จากที่อื่น'… เป็นการพาดพิงอย่างอ้อม ๆ โดยไม่ระบุชัดว่าผู้ใดจะช่วยกู้ — คงความกำกวมไว้ตามต้นฉบับ")
- EST 4:16 HEB: `וְכַאֲשֶׁר אָבַדְתִּי אָבָדְתִּי` → TH: `หากข้าพเจ้าจะต้องพินาศ ข้าพเจ้าก็ยอมพินาศ`
- EST 9:1 HEB: `נַהֲפוֹךְ הוּא` → TH: `กลับพลิกผัน` (the reversal that organizes the book)

**The hidden name:** the MT of Esther famously **encodes the Tetragrammaton in four acrostics** — the initial or final letters of four consecutive words spell יהוה at **1:20, 5:4, 5:13, 7:7** — and the divine self-designation אהיה ("I AM") once at **7:5**. Several MT manuscripts mark these with enlarged/majuscule letters: the one place the Hebrew "smuggles in" the name the book refuses to speak. The Eremos translation **does not mention this anywhere** in its 10 chapters of notes. The acrostic is untranslatable into Thai (it is a property of the Hebrew letter-sequence), and most English versions are likewise silent — but Esther's no-divine-name silence is itself an editorially significant feature, and the acrostics are the scribal tradition's own commentary on it ("the name is present though unspoken").

**Question:** Given that the book's never-naming-God silence is a deliberately-preserved feature, should the Thai edition carry a **single reader-facing note** (e.g. at 1:20 or in a book introduction) acknowledging the Masoretic acrostic tradition that hides יהוה at 1:20 / 5:4 / 5:13 / 7:7 (and אהיה at 7:5) — or is deliberate silence the better call, consistent with the book's own reticence and with the project's MT-faithful, reader-first practice?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
