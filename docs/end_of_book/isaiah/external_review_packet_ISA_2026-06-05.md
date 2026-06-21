# Isaiah — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-05**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Isaiah** (66 chapters, 1,291 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job complete (not yet tagged). Isaiah 66/66 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Messianic committal-surface policy (and a cross-book asymmetry with Daniel)

**The pattern:** At every messianic fork, Isaiah's Thai takes the **committal evangelical-consensus reading in the main text**, while keeping **descriptive, non-endorsing notes** (Hebrew weight preserved, NT labeled as later "reception," no NT vocabulary spliced into the OT surface, the Suffering Servant kept in plain/non-royal register). This follows the project's stated policy (RULES §0: "prefer the editorial choice that aligns with the modern evangelical critical-text consensus"; "notes describe, do not pastorally endorse") and the already-shipped Genesis 3:15 protoevangelium precedent.

**7:14 — almah → "virgin" (committal), with the lexical alternative preserved:**
- HE: `הִנֵּה הָעַלְמָה הָרָה וְיֹלֶדֶת בֵּן וְקָרָאת שְׁמוֹ עִמָּנוּ אֵל`
- TH (main): `ดูเถิด หญิงพรหมจารีผู้นั้นจะตั้งครรภ์และคลอดบุตรชาย … นางจะเรียกนามของเขาว่าอิมมานูเอล` ("the virgin")
- TH (`thai_literal`): `หญิงสาวผู้นั้น [หรือ: หญิงพรหมจารีผู้นั้น]` ("young woman / virgin")
- KD documents: ʿalmâ = young woman of marriageable age; LXX → παρθένος; Matt 1:23 quotes the LXX; the MT 3fs "she will call" vs LXX/Matthew "they will call" person-difference, each faithful to its own text.

**9:5-6 — אֵל גִּבּוֹר "Mighty God," locked identical to the undisputed-divine 10:21:**
- HE 9:5: `אֵל גִּבּוֹר אֲבִי־עַד שַׂר־שָׁלוֹם` → TH: `พระเจ้าผู้ทรงฤทธิ์ พระบิดานิรันดร์ องค์สันติราช`
- HE 10:21: `אֵל גִּבּוֹר` (YHWH beyond dispute) → TH: `พระเจ้าผู้ทรงฤทธิ์` (identical surface — forcing the reader to see YHWH's own title on the child)
- The 9:6 `thai_summary` reads: `พระนามสี่ชั้นเกินกว่ากษัตริย์มนุษย์คนใดจะแบกได้ … คริสตจักรอ่านพระนามเหล่านี้สำเร็จในพระเยซูคริสต์` ("names too heavy for any human king to bear … the church reads these names fulfilled in Jesus Christ"). This is the single most doctrinally-forward summary line in the book — framed descriptively ("the church reads…"), matching the Gen 3:15 construction.

**53 — committal in substance, but the Servant kept in plain register** (where the NT uses royal honorifics for Christ, Isaiah keeps plain ปาก/มือ and documents the register difference); 53:11 follows the DSS+LXX "light" reading (`เห็นแสงสว่างแห่งชีวิต`, footnoted with 1QIsaᵃ/ᵇ + 4QIsaᵈ + LXX).

**The cross-book asymmetry:** the already-audited Daniel renders מָשִׁיחַ **generically** —
- Dan 9:25 HE `עַד־מָשִׁיחַ נָגִיד` → TH `จนถึงผู้ถูกเจิมผู้เป็นเจ้านาย` ("anointed one," not "the Messiah/Christ"), with notes that *acknowledge but do not endorse* the Christian reading.

So Isaiah commits at the surface where Daniel does not. A Thai evangelical reviewer reading Isaiah 9/53 and then Daniel 9 will see the inconsistency.

**Two questions:**
1. Is Isaiah's policy — **committal evangelical-consensus reading in the main text + rigorously descriptive (non-endorsing) notes**, with the Suffering Servant deliberately kept in plain (non-royal) register — sound and internally coherent? In particular, does the 9:6 summary line "the church reads these names fulfilled in Jesus Christ" stay within "describe, don't endorse," or does it cross into pastoral endorsement that belongs only in a footnote?
2. Given Isaiah's committal surface (and the shipped Gen 3:15 precedent), should **Daniel 9:25-26**'s generic/non-committal מָשִׁיחַ → ผู้ถูกเจิม be revisited toward the committal surface for cross-book consistency, or is there a principled reason (e.g., a near-horizon referent in Daniel's seventy-weeks frame) to treat Daniel's מָשִׁיחַ differently from Isaiah's messianic titles?

---

## Item B — Divine-anthropomorphism register drift: God's "arm" and "Spirit" in first-person divine speech

**The pattern:** The translation locks God's body-part anthropomorphisms to Thai royal register (ราชาศัพท์): the divine **arm** זְרוֹעַ → **พระกร** and the divine **Spirit** רוּחַ → **พระวิญญาณ**. Most occurrences comply, but a systematic lapse to plain register appears specifically in **first-person divine speech** ("my arm / my Spirit").

**Divine "arm" — compliant พระกร vs drift แขน:**
- 52:10 (compliant) HE `חָשַׂף יְהוָה אֶת־זְרוֹעַ קָדְשׁוֹ` → TH `องค์พระผู้เป็นเจ้าได้ทรงเปลือยพระกรอันบริสุทธิ์ของพระองค์`
- 53:1 (compliant) HE `זְרוֹעַ יְהוָה` → TH `พระกรขององค์พระผู้เป็นเจ้า`
- 59:16 (compliant) HE `וַתּוֹשַׁע לוֹ זְרֹעוֹ` → TH `พระกรของพระองค์เองจึงนำความรอดมา`
- **51:9 (drift)** HE `עוּרִי … זְרוֹעַ יְהוָה` → TH `แขนแห่งองค์พระผู้เป็นเจ้าเอ๋ย` — sits one verse-column from 52:10's พระกร, in the same "bared holy arm" thread
- **63:5 (drift)** HE `וַתּוֹשַׁע לִי זְרֹעִי` → TH `แขนของเราเองจึงนำความรอดมาให้เรา` — structurally identical to 59:16's พระกร, but plain
- **51:5 (drift)** HE `וּזְרֹעַי … וְאֶל־זְרֹעִי` → TH `แขนของเรา … หวังในแขนของเรา`

**Divine "Spirit" — compliant พระวิญญาณ vs drift วิญญาณ:**
- 11:2 (compliant) HE `וְנָחָה עָלָיו רוּחַ יְהוָה` → TH `พระวิญญาณขององค์พระผู้เป็นเจ้าจะสถิตเหนือท่าน`
- 61:1 (compliant) → TH `พระวิญญาณขององค์พระผู้เป็นเจ้าสถิตอยู่เหนือข้าพเจ้า`
- **42:1 (drift)** HE `נָתַתִּי רוּחִי עָלָיו` → TH `เราได้วางวิญญาณของเราไว้เหนือเขา` — and this is the Servant Song quoted at Matt 12:18
- **44:3 (drift)** HE `אֶצֹּק רוּחִי עַל־זַרְעֶךָ` → TH `เราจะเทวิญญาณของเราลงเหนือเชื้อสายของเจ้า`
- **59:21 (drift)** HE `רוּחִי אֲשֶׁר עָלֶיךָ` → TH `วิญญาณของเราซึ่งอยู่เหนือเจ้า`

In each drift case the referent is unambiguously God's own arm/Spirit, and the first-person possessive ("my") is the common trigger.

**Question:** Should the divine arm at 51:5 / 51:9 / 63:5 be normalized to **พระกร**, and the divine Spirit at 42:1 / 44:3 / 59:21 to **พระวิญญาณ**, to conform to the established Rachasap lock (especially given 51:9 sits beside 52:10 and 63:5 mirrors 59:16) — or is there a principled reason that first-person divine self-reference ("my arm / my Spirit") should take plain register?

---

## Item C — שָׂעִיר (goat-demon / "satyr"): demonic vs naturalized rendering in the two desert-ruin oracles

**The pattern:** The Hebrew שָׂעִיר ("hairy one," a goat-shaped desert demon in the Babylon-ruin and Edom-ruin oracles) is rendered two different ways in two parallel haunted-ruins passages.

- **13:21** (Babylon's ruins) HE `וּשְׂעִירִים יְרַקְּדוּ־שָׁם` → TH `ผีปีศาจรูปแพะจะโลดเต้นที่นั่น` ("goat-demons will dance there") — demonic register; the KD cites the Lev 17:7 goat-demon cult-ban, LXX δαιμόνια, and the haunted-Babylon echo at Rev 18:2.
- **34:14** (Edom's ruins) HE `וְשָׂעִיר עַל־רֵעֵהוּ יִקְרָא` → TH `แพะป่าตัวหนึ่งจะร้องเรียกหาเพื่อนของมัน` ("a wild goat calls to its mate") — naturalized to an ordinary "wild goat"; the KD does not flag śāʿîr at all.

Notably, 34:14 is the *more* uncanny context — the same verse introduces **Lilith** (`לִילִית` → `นางลีลิทผู้เพ่นพ่านยามราตรี`), which the translation keeps transliterated and eerie. So within one verse a demon-name is preserved (Lilith) while the goat-demon beside it is flattened to a farm animal, contradicting the demonic register chosen 21 chapters earlier and the Lev 17:7 lock.

**Question:** Should 34:14's שָׂעִיר be harmonized to the demonic rendering used at 13:21 (`ผีปีศาจรูปแพะ`), consistent with the Lev 17:7 goat-demon lock and the eerie register of the Lilith clause it sits in — or is "wild goat" defensible at 34:14 on contextual grounds (and if so, should the split be documented)?

---

## Item D — OT→NT cross-quotation: missing reader-facing footnotes for NT-cited MT/LXX divergences, plus shipped-NT retro-candidates

**The policy:** When an Isaiah verse is quoted in the NT and the NT follows the LXX against the MT, the project keeps the **MT surface** but is required to add a reader-facing `textual_variants` footnote recording the LXX reading + the NT cross-reference. This is implemented well in many places (28:16, 40:3, 52:15, 53:8, 55:3, 59:20, 61:1, 64:3 all have correct footnotes). But several NT-cited divergences are documented only in the internal `key_decisions` (invisible to readers) and lack the footnote:

- **25:8** (→ 1 Cor 15:54 "in victory") — the KD says the divergence is "documented," but the chapter's `textual_variants` file carries only the YHWH footnote: a **broken reference**.
- **11:10** HE "the nations will **seek** (דרשׁ)" vs Rom 15:12 "the Gentiles will **hope**" — no footnote.
- **9:1** vs Matt 4:15-16; **29:13-14** vs Matt 15 / 1 Cor 1:19; **42:1/42:4** vs Matt 12:18-21; **45:23** ("**swear**" vs Rom/Phil "**confess**"); **65:1-2** (LXX reordering) vs Rom 10:20-21 — all KD-only, no footnote.

**Retro-candidates (shipped OT/NT surfaces that disagree):**
- **53:1 (translator self-flagged):** Isaiah `และพระกรขององค์พระผู้เป็นเจ้า` vs shipped John 12:38 `และพระหัตถ์…` — same זְרוֹעַ/βραχίων "arm"; the NT used "hand." (Also Isaiah `เชื่อสิ่งที่เราได้ยินมา` = Rom 10:16, vs John 12:38 `เชื่อสารของเรา`.)
- **56:7:** Isaiah / Mark 11:17 / Luke 19:46 all use `นิเวศแห่งการอธิษฐาน` (Mark byte-identical), but shipped **Matthew 21:13** uses the colloquial `บ้าน` — Matthew is the outlier.

**Two questions:**
1. Should the ~7 missing `textual_variants` footnotes (for NT-cited MT/LXX divergences such as 25:8, 11:10, 45:23, 65:1-2) be added before the book is sealed, and the 25:8 broken reference fixed — or is internal `key_decisions` documentation sufficient for this class?
2. For the shipped-NT retro-candidates (53:1 พระกร/พระหัตถ์; 56:7 นิเวศ/บ้าน), should the NT side be normalized to match the OT in a staged NT re-audit (the path already used for Deuteronomy), and which surface should be canonical?

---

## Item E — אֲדֹנָי יְהוִה צְבָאוֹת ("the Lord GOD of hosts"): inconsistent Adonai-marking

**The pattern:** The triple-stack divine title אֲדֹנָי יְהוִה צְבָאוֹת appears 7× in Isaiah. The project's rule for the bare אֲדֹנָי יְהוִה compound mid-sentence is to **drop Adonai** (render only องค์พระผู้เป็นเจ้า). For the Sabaoth-stack, 5 occurrences follow that (drop Adonai) but 2 mark it:

- **Drop Adonai → องค์พระผู้เป็นเจ้าจอมโยธา:** 3:15, 10:23, 22:5, 22:12, 28:22
  - e.g. 10:23 HE `אֲדֹנָי יְהוִה צְבָאוֹת עֹשֶׂה` → TH `องค์พระผู้เป็นเจ้าจอมโยธาจะทรงกระทำ`
- **Mark Adonai → องค์เจ้านาย องค์พระผู้เป็นเจ้าจอมโยธา:** 22:14b, 22:15 (both in the Shebna oracle)
  - 22:15 HE `כֹּה אָמַר אֲדֹנָי יְהוִה צְבָאוֹת` → TH `องค์เจ้านาย องค์พระผู้เป็นเจ้าจอมโยธา ตรัสดังนี้ว่า`

(22:14 also opens with a *plain* יְהוָה צְבָאוֹת → องค์พระผู้เป็นเจ้าจอมโยธา, correctly distinguished from the Adonai-stack later in the same verse.)

**Question:** Should the two ch.22 outliers (22:14b, 22:15) be normalized to องค์พระผู้เป็นเจ้าจอมโยธา to match the other five and the mid-sentence Adonai-dropping rule — or should the Adonai be marked in all seven (normalizing the other five)?

---

## Item F — Polytheistic-register / cosmic-creature explanation: reader footnote vs internal-only

**The pattern:** Isaiah is the OT's densest idol-polemic (chs 40–48) and carries the most cosmic/mythic creatures (Leviathan 27:1, Rahab 30:7/51:9, the sea-dragon 27:1, Lilith 34:14, Bel & Nebo 46:1). The translation handles the register correctly — manufactured deities take lowercase **พระ** (never พระเจ้า); idol-worship verbs use non-divine register; cosmic creatures are transliterated/glossed and harmonized with the shipped Job/Revelation. But all of the *explanatory* orientation (why "พระ" lowercase, what a "satyr"/Lilith is, the rhetorical-incomparability of YHWH over the idols) lives only in the internal `key_decisions`, which readers never see. None of Isaiah's `textual_variants` files carry a polytheistic-register or cosmic-creature first-occurrence footnote, and ch.46 (the only named-pagan-deity scene, Bel & Nebo) has no `textual_variants` file at all (it contains no Tetragrammaton).

**Question:** Should Isaiah carry one reader-facing first-occurrence footnote for the lowercase-deity / idol-satire convention and for the cosmic-creature names (creating a `textual_variants` host file for ch.46) — or is the corpus's established practice to keep this orientation in internal notes only, in which case the "once per book" expectation should be relaxed in the policy?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
