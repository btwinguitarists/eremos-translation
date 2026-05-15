# Leviticus — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-15**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Leviticus** (27 chapters, 859 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation complete (not yet tagged). Leviticus 27/27 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — LEV-wide kipper (כִּפֵּר) drift from `sacrificial_vocabulary_2026-05.md`

**The drift:** The corpus-doc `docs/translator_decisions/sacrificial_vocabulary_2026-05.md` (LOCKED 2026-05-15; cross-AI consensus ChatGPT + Gemini + Logos AI; triggered by NUM end-of-book audit) explicitly locks the כִּפֵּר verbal-rendering at:

> | Hebrew verb | Thai (doc-locked) |
> |---|---|
> | כִּפֵּר (piel) | **ลบบาป** / **ไถ่บาป** / **ทำการลบบาป** |

**Leviticus actual rendering (across ~168 occurrences):**

| Thai phrase | Verse count | Doc-canonical? |
|---|---|---|
| **ลบมลทินบาป** | 45 verses | ✗ adds `มลทิน` (ritual-impurity) |
| **ลบมลทิน** | 45 verses | ✗ adds `มลทิน` |
| **การลบมลทิน** | 42 verses | ✗ adds `มลทิน` |
| **ทำการลบมลทินบาป** | 41 verses | ✗ adds `มลทิน` |
| **ไถ่บาป** | 14 verses | ✓ matches doc |

**The drift is universal across LEV 1-7 + 16 + 23** (the sacrificial manual + Yom Kippur + Day-of-Atonement feast). Sample verse:

> **LEV 16:6 Hebrew:** וְהִקְרִ֧יב אַהֲרֹ֛ן אֶת־פַּ֥ר הַחַטָּ֖את אֲשֶׁר־ל֑וֹ וְכִפֶּ֥ר בַּעֲד֖וֹ וּבְעַ֥ד בֵּיתֽוֹ
>
> **LEV 16:6 Thai (as shipped):** "อาโรนจะถวายวัวหนุ่มเป็นเครื่องบูชาไถ่บาปของเขา และ**ทำการลบมลทินบาป**สำหรับตัวเองและครัวเรือนของเขา"
>
> **Doc-canonical Thai would be:** "...และ**ทำการลบบาป**สำหรับตัวเองและครัวเรือนของเขา"

The Thai surface consistently adds **`มลทิน` ("ritual impurity")** to the doc-locked `ลบบาป` form. This is **arguably more faithful** to the Hebrew kipper semantic range — kipper covers BOTH moral-sin and ritual-impurity clearance in Leviticus's ritual register (cf. Milgrom *Leviticus 1-16* AB 1078-1083; Hartley *Leviticus* WBC 64-66; the kipper-as-purgation reading is the dominant scholarly view post-Milgrom). **But it diverges from the doc as written.**

**The doc was decided 2026-05-15 — the SAME DATE as this audit + LEV 27 ship.** A cross-corpus spot-check shows the same `ลบมลทินบาป` form is used in already-shipped NUM (NUM 6:11, 8:12, 15:25 — ~50 NUM occurrences). So the doc apparently locked `ลบบาป` against a NUM-and-LEV-as-shipped corpus that uses `ลบมลทินบาป`. **The doc's locked Thai is honored at 14 of ~218 cross-book occurrences (6.4% compliance).**

**Why this matters.** This is the largest single editorial-decision drift in any OT-book audit by occurrence-count (>200 verses affected). Three resolution paths:

**(a) Strict normalization** — rewrite all ~218 LEV+NUM kipper-occurrences to doc-locked `ลบบาป / ทำการลบบาป`. Cost: very high (>200 surgical edits + per-chapter check re-runs); semantic-loss (drops the `มลทิน` ritual-impurity dimension that maps the Hebrew priestly-purity register).

**(b) Doc-revision** — amend `sacrificial_vocabulary_2026-05.md` §5 to add `ลบมลทินบาป / ทำการลบมลทินบาป / การลบมลทิน` as **canonical locked Thai** in ritual-context (with `ลบบาป / ไถ่บาป` retained for moral-noun and non-ritual atonement contexts). The doc's §3 already handles the חַטָּאת polysemy split by context; this kipper extension would parallel the same split. Cost: one doc-revision + a §5 paragraph + cross-link to NUM-and-LEV-as-locking-precedent.

**(c) Leave as-is, accept doc-divergence** — worst path. The doc loses authority at the largest-volume site of the lemma.

**Cross-corpus context:** the doc's §7 also calls for `check_sacrificial_vocab.py` (script "to be written before LEV 1 ships"). The script was not written. Whichever resolution lands, the check-script should be written in tandem so future OT-book ships are auto-protected.

**Two questions:**

1. Should the project (a) retroactively normalize ~218 LEV+NUM kipper-occurrences to doc-locked `ลบบาป / ทำการลบบาป`, or (b) amend `sacrificial_vocabulary_2026-05.md` §5 to recognize the as-shipped `ลบมลทินบาป` form as canonical-in-ritual-context (with the doc's `ลบบาป` retained for moral-context occurrences)? Theologically, the ritual-`kipper`-as-purgation reading (Milgrom) supports the as-shipped `มลทิน`-including form; pragmatically, (b) is the lower-cost path with no translation-surface change.

2. Should the doc's §7 `check_sacrificial_vocab.py` script be written in tandem with the (b) doc-revision commit, so the lock is mechanically enforced for future OT-book ships? The script's pattern-checks would verify (i) the five primary offering types use the locked Thai, (ii) the kipper verbal-form uses the ritual-context form in sacrificial pericopes, (iii) the חַטָּאת polysemy split per §3 is respected.

---

## Item B — LEV 25:25 goel doc-drift + Ruth-vs-LEV cross-book divergence

**The drift:** The corpus-doc `docs/translator_decisions/goel_kinsman_redeemer_2026-05.md` (LOCKED 2026-05-15; cross-AI consensus ChatGPT + Gemini) names **`ผู้ไถ่ที่เป็นญาติ`** ("kinsman who redeems") as the canonical Thai for the property/levirate-redemption goel role:

> | Role | Hebrew context | Locked Thai |
> |---|---|---|
> | Kinsman-redeemer (property/levirate) | Lev 25; Ruth 2-4 | **ผู้ไถ่ที่เป็นญาติ** |

**Three Thai forms in actual ship (none matches the doc):**

| Source | Thai form | Verses (count) |
|---|---|---|
| Doc (decided 2026-05-15) | **ผู้ไถ่ที่เป็นญาติ** | (not in any shipped translation) |
| Ruth 3:9, 3:12, 4:1, 4:3, 4:4, 4:6, 4:14 | **ญาติผู้ไถ่** ("kinsman-redeemer" compound) | 8 |
| **LEV 25:25** (locking-precedent intro verse) | **ญาติสนิทที่สุด** ("closest kinsman") | 1 ✗ DRIFT |
| LEV 25:26, 25:48, 25:49, 25:54 | **ผู้ไถ่** alone (drops "kinsman" qualifier) | 4 |

**Sample verse:**

> **LEV 25:25 Hebrew:** כִּֽי־יָמ֣וּךְ אָחִ֔יךָ וּמָכַ֖ר מֵאֲחֻזָּת֑וֹ וּבָ֤א גֹֽאֲלוֹ֙ הַקָּרֹ֣ב אֵלָ֔יו וְגָאַ֕ל אֵ֖ת מִמְכַּ֥ר אָחִֽיו
>
> **LEV 25:25 Thai (as shipped):** "ถ้าพี่หรือน้องของเจ้ายากจนและขายที่ดินของเขา **ญาติสนิทที่สุดของเขา**อาจมาและ**ไถ่**สิ่งที่พี่หรือน้องของเขาขายไป"
>
> Verse-level KD at LEV 25:25: `{"hebrew": "גֹּאֵל", "thai": "ผู้ไถ่", "rationale": "gōʾēl — 'ผู้ไถ่/ผู้ปกป้องครอบครัว'. คำเดียวกับโบอาสในรูธ 4. NT echo: พระคริสต์ทรงเป็น gōʾēl ของเรา — รม 3:24"}` — the KD acknowledges the goel-doc cross-reference but the surface Thai loses the ไถ่ root marker (replaced with `ญาติสนิทที่สุด` = "closest kinsman").
>
> **Ruth 3:9 Thai (already shipped):** "...ขอท่านโปรดกางชายผ้าคลุมของท่านมาคลุมสาวรับใช้ของท่านด้วยเถิด เพราะท่านเป็น**ญาติผู้ไถ่**"

**Why this matters.** The goel doc's §2 explicitly states: "If Ruth's Boaz is rendered ผู้ไถ่ที่เป็นญาติ but Job 19:25's 'my Redeemer' is rendered with a different term (e.g., พระผู้ช่วย 'savior'), the typology breaks at the Thai surface." But this is already happening **across the two shipped books**:
- Ruth 3:9 reader sees `ญาติผู้ไถ่` ("kinsman-redeemer")
- LEV 25:25 reader sees `ญาติสนิทที่สุด` ("closest kinsman" — no `ไถ่` root)
- The Boaz↔LEV 25 typology breaks at the precise verse the doc was created to protect.

**The doc's locked form `ผู้ไถ่ที่เป็นญาติ` appears in neither corpus**, which suggests the doc was drafted without verifying Ruth's actual ship-form. Ruth's `ญาติผู้ไถ่` is more natural Thai compound morphology (matches Thai's left-headed compound preference: noun+attributive vs. the doc's relative-clause periphrasis).

**Three resolution paths:**

**(a) Doc-amendment + 1 LEV verse-edit (RECOMMENDED)** — amend `goel_kinsman_redeemer_2026-05.md` §1 to lock **Ruth's `ญาติผู้ไถ่`** as the canonical Thai (and `ผู้ไถ่` alone as the abbreviated in-context form). Then normalize LEV 25:25 from `ญาติสนิทที่สุดของเขา` → `ญาติผู้ไถ่ของเขา`. Cost: 1 doc-amendment + 1 verse edit. Restores the cross-book root-linkage at the locking-precedent verse.

**(b) Strict normalization to doc-canonical `ผู้ไถ่ที่เป็นญาติ`** — rewrite all 8 Ruth occurrences + LEV 25:25 to match the doc. Cost: ~9 surgical edits. Defensible only if Ben actively prefers the doc's relative-clause periphrasis over Ruth's natural compound.

**(c) Leave as-is, accept divergence** — Ruth and LEV use different surface forms; doc honored nowhere. The typology breaks at the Thai surface.

**Forward-compounding.** Job 19:25 (the divine-Redeemer locking precedent the doc §5 names: **`พระผู้ไถ่ของข้าพระองค์`** — "my Redeemer"), Isa 41:14, Isa 43:14, Isa 44:6, Isa 53 (typological), Ps 19:14 — all forthcoming. Whichever Thai is locked must propagate the `ไถ่` root marker.

**Two questions:**

1. Should the goel doc be amended to lock **`ญาติผู้ไถ่`** (Ruth's natural Thai compound form) as canonical, with **LEV 25:25's surface normalized** from `ญาติสนิทที่สุด` → `ญาติผู้ไถ่` (path a)? Or should both books be normalized to the doc's `ผู้ไถ่ที่เป็นญาติ` (path b)?

2. The doc's §5 also locks **`พระผู้ไถ่ของข้าพระองค์`** ("my Redeemer") at Job 19:25 + Isa 41-44 — should the LEV/Ruth normalization choice constrain the divine-Redeemer noun-form (i.e., should it become **`พระผู้ไถ่`** as the divine cognate of the human `ผู้ไถ่`, or remain **`พระผู้ไถ่ของข้าพระองค์`** with the explicit personal-suffix)?

---

## Item C — LEV 23:6 Unleavened Bread feast Thai-drift

**The drift:** The Hebrew חַג הַמַּצּוֹת ("Feast of Unleavened Bread") appears at **LEV 23:6** with a single-verse cross-corpus drift:

| Book | Thai | Verse count |
|---|---|---|
| Exodus | `เทศกาลขนมปังไร้เชื้อ` / `ขนมปังไร้เชื้อ` | 12 verses |
| Leviticus | `ขนมปังไร้เชื้อ` | 3 verses (2:5, 8:2, 8:26) |
| **Leviticus** | **`ขนมปังไม่มีเชื้อ`** | **1 verse (23:6) ✗ DRIFT** |
| Numbers | `ขนมปังไร้เชื้อ` | 5 verses (6:15, 6:17, 6:19) |

**Sample verse:**

> **LEV 23:6 Hebrew:** וּבַחֲמִשָּׁ֨ה עָשָׂ֥ר יוֹם֙ לַחֹ֣דֶשׁ הַזֶּ֔ה חַ֥ג הַמַּצּ֖וֹת לַיהוָ֑ה שִׁבְעַ֥ת יָמִ֛ים מַצּ֖וֹת תֹּאכֵֽלוּ
>
> **LEV 23:6 Thai (as shipped):** "ในวันที่สิบห้าของเดือนเดียวกันนี้ เป็น**เทศกาลขนมปังไม่มีเชื้อ**แด่องค์พระผู้เป็นเจ้า เจ็ดวันพวกเจ้าต้องกินขนมปังไม่มีเชื้อ"
>
> **Corpus-locked form** (EXO 12:17, 23:15, etc.): "เทศกาล**ขนมปังไร้เชื้อ**"

**Editorial assessment.** The variant `ไม่มีเชื้อ` ("having no leaven") and the corpus-locked `ไร้เชื้อ` ("without leaven") are semantically equivalent in Thai (the `ไร้` prefix and the `ไม่มี` periphrasis are register-neutral interchangeable). Both are valid Thai renderings of מַצּוֹת. But the corpus has uniformly locked `ไร้เชื้อ` since EXO 12, and LEV 23:6 is the single drift — affecting the most-frequently-read Eremos OT feast-calendar verse.

**Recommended normalization:** 1 surgical text-edit at LEV 23:6 — change `เทศกาลขนมปังไม่มีเชื้อ` → `เทศกาลขนมปังไร้เชื้อ`.

**Question:** Should LEV 23:6 be normalized to `เทศกาลขนมปังไร้เชื้อ` (matching the 20+ other corpus occurrences in EXO + LEV elsewhere + NUM) before tagging `book-leviticus-v1`? The drift is single-verse + semantically-neutral but breaks the proper-name lock at the canonical feast-calendar chapter.

---

## Item D — Yobel "Jubilee" rendering choice: `ปีจูบีลี` (English-via-Latin) vs. `ปีโยเบล` (Hebrew direct)

**The textual question:** The Hebrew יוֹבֵל ("ram's horn" → "year-of-jubilee") appears ~19 times in LEV 25:9-54 + 27:17-24. Eremos uniformly renders **`ปีจูบีลี`** (from English `jubilee` via Latin `iubilaeus`).

**Sample verse:**

> **LEV 25:10 Thai (as shipped):** "พวกเจ้าจะชำระให้บริสุทธิ์ปีที่ห้าสิบและประกาศอิสรภาพในแผ่นดินสำหรับผู้อาศัยทั้งหมด เป็น**ปีจูบีลี**ของพวกเจ้า..."
>
> **Alternative direct-Hebrew transliteration:** `ปีโยเบล`

**Editorial assessment.** Per `proper_names_and_transliteration_2026-05.md`, the project's principle is "follow established Thai-Christian-Bible precedent unless documented otherwise; for Hebrew terms, transliterate via Hebrew phonology when no precedent exists." The English-via-Latin `จูบีลี` matches modern Thai-Christian-Bible tradition (THSV-Eclectic uses `ปีจูเบลี`); the direct Hebrew transliteration `ปีโยเบล` is more-faithful to Hebrew phonology but less-familiar to Thai-Christian readers.

The trade-off compounds when the Hebrew `יוֹבֵל` recurs in Joshua 6:4-13 (the rams'-horn trumpets of Jericho — the original metonymic source) — the same Hebrew lemma there should align with the LEV transliteration choice.

**Question:** Should the project lock **`ปีจูบีลี`** (English-via-Latin transliteration; matches modern Thai-Christian-Bible usage; reader-familiar) as the going-forward canonical, or normalize to direct Hebrew **`ปีโยเบล`** (matches Hebrew phonology; preserves the rams'-horn metonymy when יוֹבֵל recurs in Joshua 6)? Either way, `proper_names_and_transliteration_2026-05.md` should be amended to document the choice + rationale.

---

## Item E — LEV 16 + LEV 17:11 NT-cross-reference Layer-2 footer gap

**The textual question:** The two most doctrinally load-bearing verses in Leviticus for NT atonement theology are LEV 16 (the Yom Kippur ritual) + LEV 17:11 (the "life is in the blood" axiom). Both currently have **only the standard YHWH first-occurrence Layer-2 footer**; neither has a Layer-2 footer cross-referencing the NT doctrine they ground.

**LEV 16 NT load-bearing nodes (no Layer-2 footer at present):**

- **LEV 16:2 kapporet `พระที่นั่งกรุณา`** — locking precedent for `kapporet_atonement_cover_2026-05.md`; direct OT-source of **Heb 9:5** (τὰ Χερουβεὶν δόξης κατασκιάζοντα τὸ ἱλαστήριον "cherubim of glory overshadowing the mercy seat") and **Rom 3:25** (ὃν προέθετο ὁ θεὸς ἱλαστήριον).
- **LEV 16:5-22 two-goats / Azazel** — OT-source of **Heb 9:28**'s "Christ once-for-all" + **Isa 53:6**'s "YHWH laid on him the iniquity of us all" + **1 Pet 2:24**'s "bore our sins in his body on the tree". The two-goats are read in church-fathers' tradition as two-aspect Christology (one slain, one bearing-iniquity-into-the-wilderness).
- **LEV 16:30 כִּפֻּרִים** — OT-source of the **Hebrews-corpus high-priestly Christology** (Heb 7-10).

**LEV 17:11 NT load-bearing (no Layer-2 footer):**

> **LEV 17:11 Thai (as shipped):** "เพราะ**ชีวิตของเนื้ออยู่ในเลือด** และเราได้ให้เลือดแก่พวกเจ้าบนแท่นบูชา**เพื่อทำการลบมลทินบาปสำหรับจิตของพวกเจ้า** เพราะเลือดเป็นสิ่งที่ทำการลบมลทินบาปด้วยชีวิต"

This is the **OT-source of Heb 9:22** (χωρὶς αἱματεκχυσίας οὐ γίνεται ἄφεσις "without shedding of blood there is no forgiveness") + **Rom 3:25** (ἐν τῷ αὐτοῦ αἵματι "in his blood"). The verse-level `notes` field references these NT echoes; the Layer-2 footer does not.

**Recommended normalization:** Write **3 Layer-2 footers** in tandem before tagging:

1. `output/textual_variants/leviticus_16.json` — add Layer-2 footer naming kapporet → Heb 9:5; two-goats → Heb 9:28 + 1 Pet 2:24 + Isa 53:6; high-priestly entry → Heb 9:7-12.
2. `output/textual_variants/leviticus_17.json` — add Layer-2 footer at v.11 naming blood-life → Heb 9:22 + Rom 3:25.
3. (Optional) `output/textual_variants/leviticus_23.json` — feast-calendar cross-reference to NT feast-fulfillment cluster (Passover→Lk 22; Firstfruits→1 Cor 15:20; Pentecost→Acts 2; Trumpets+Atonement+Booths→eschatological fulfillment).

**Cross-corpus pattern:** Genesis-audit added similar footers retroactively at Gen 3:15, Gen 22, Gen 49:10; Exodus-audit recommended at Exod 12 + Exod 24; LEV 16 is the natural next addition (the most-NT-load-bearing OT chapter in the corpus).

**Question:** Should the Eremos Layer-2 footer policy carry an NT-cross-reference at LEV 16 + LEV 17:11, naming the Hebrew→Greek atonement-theology cluster (kapporet→ἱλαστήριον, blood→αἱματεκχυσία, two-goats→Christology, Yom Kippur→Hebrews 7-10)? Without this, the Thai reader experiences the doctrinal climax of the OT priestly system at the surface without the reader-edition transparency the project's Layer-2 policy was created to provide.

---

## Item F — "I am YHWH" Holiness Code leitwort: 52 LEV occurrences without corpus-doc

**The textual question:** The **`אֲנִי יְהוָה`** ("I am YHWH") closure-formula appears **52 times in Leviticus**, concentrated in the Holiness Code (chs.18-26). It is the structural-anchor of the Holiness Code — each ethical or ritual prohibition closes with the divine self-identification.

**Sample verses (10 of 52):**

| Verse | Hebrew | Thai (current) |
|---|---|---|
| LEV 18:2 | אֲנִ֖י יְהוָ֥ה אֱלֹהֵיכֶֽם | **เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า** |
| LEV 18:6 | אֲנִ֖י יְהוָֽה | **เราคือองค์พระผู้เป็นเจ้า** |
| LEV 19:2 | אֲנִ֖י יְהוָ֥ה אֱלֹהֵיכֶֽם | **เรา องค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า** (omits `คือ` copula) |
| LEV 19:18 | אֲנִ֖י יְהוָֽה | **เราคือองค์พระผู้เป็นเจ้า** |
| LEV 19:34 | אֲנִ֖י יְהוָ֥ה אֱלֹהֵיכֶֽם | **เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า** |
| LEV 20:26 | אֲנִ֤י יְהוָה֙ קָד֔וֹשׁ | **เรา องค์พระผู้เป็นเจ้า เป็นผู้บริสุทธิ์** |

**Editorial assessment.** The Thai is uniform-up-to-minor-variations: the short form (אֲנִי יְהוָה bare) → `เราคือองค์พระผู้เป็นเจ้า`; the expanded form (אֲנִי יְהוָה אֱלֹהֵיכֶם) → `เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า`. Minor variants at LEV 19:2 + 20:26 omit the `คือ` copula — preserving the Hebrew's nominal-sentence directness. Both forms are well-formed Thai.

**Forward-compounding.** The leitwort recurs in:
- **Ezekiel ×65+** (the famous **`וִידַעְתֶּ֖ם כִּ֣י אֲנִ֣י יְהוָ֑ה`** "you/they will know that I am YHWH" — the densest divine-recognition-formula in scripture; Ezek 6, 7, 11, 13, 14, 20, 23, 24, 25, 28, 29, 30, 33, 34, 35, 36, 37, 38, 39).
- **Deuteronomy 5** (Decalogue parallel) + scattered prophetic recurrences (Isa 41:4, 43:11, 45:5+6+18+21+22).
- **NT echo:** the Johannine `ἐγὼ εἰμί` self-disclosures (Jn 8:24, 8:58, 13:19, 18:5-6) are read by NT scholars (Bauckham, *Jesus and the God of Israel*) as the Greek-translation of the Hebrew אֲנִי הוּא / אֲנִי יְהוָה — making LEV's Holiness-Code formula the OT-Christological-locus the Johannine Christ-discourse claims for himself.

**The leitwort has no corpus-doc lock.** Verse-level KDs document the rendering. No `i_am_yhwh_holiness_formula` doc exists. Recommend writing one before Ezekiel or DEUT ships.

**Question:** Should the project write a corpus-doc `docs/translator_decisions/i_am_yhwh_holiness_formula_2026-05.md` that (a) locks the bare-form `เราคือองค์พระผู้เป็นเจ้า` and expanded-form `เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า` Thai, (b) addresses the minor LEV 19:2 + 20:26 variant (omitting `คือ` copula) — either normalize them or document them as principled-stylistic-variants, and (c) forward-locks for the Ezekiel `וִידַעְתֶּם כִּי אֲנִי יְהוָה` cognate-form (65+ Ezekiel occurrences) and the Johannine `ἐγὼ εἰμί` NT-corpus echo (Jn 8:24, 8:58, etc.)?

---

## Item G — LEV 18:6-18 + 20:11-21 incest catalog: hybrid euphemism-and-explicit policy

**The textual question:** The Hebrew euphemism **`לְגַלּוֹת עֶרְוָה`** ("to uncover the nakedness" — the Pentateuch's circumlocution for sexual intercourse) appears **24 times** across LEV 18:6-18 + 20:11-21. The Thai uses a **hybrid strategy**:

| Verse | Hebrew literal | Thai (current) |
|---|---|---|
| LEV 18:6 (programmatic) | לְגַלּוֹת עֶרְוָה | **มีความสัมพันธ์ทางเพศ** (explicit) |
| LEV 18:7 (mother) | לֹא תְגַלֵּ֑ה | **ไม่เปิดเผยความเปลือยเปล่า... ไม่มีความสัมพันธ์ทางเพศกับนาง** (hybrid) |
| LEV 18:8 (stepmother) | לֹא תְגַלֵּ֑ה | **ไม่มีความสัมพันธ์ทางเพศ** (explicit) |
| LEV 18:16 (brother's wife) | לֹא תְגַלֵּ֑ה | **ไม่มีความสัมพันธ์ทางเพศ** (explicit) |
| LEV 18:18 (wife's sister) | לְגַלּ֤וֹת | **มีความสัมพันธ์ทางเพศกับนาง** (explicit) |
| LEV 20:11 (father's wife) | עֶרְוַ֥ת אָבִ֖יו | **ได้เปิดเผยความเปลือยเปล่าของบิดา** (preserves euphemism) |
| LEV 20:18 (menstruant) | הֶעֱרָ֕ה ... וְהִ֖יא גִּלְּתָ֣ה | **เปิดเผยแหล่งที่มาของการไหล** (literal preserves clinical force) |

**Editorial assessment.** The Thai strategy is **principled hybrid**:
- When the Hebrew euphemism is contextually clarified by relationship-pronoun (LEV 18:7-18 introduces each prohibition with `אֵם / אֵשֶׁת אָבִיךָ` "mother / father's wife"), the Thai prefers the explicit `มีความสัมพันธ์ทางเพศ`.
- When the Hebrew euphemism carries clinical-anatomical weight (LEV 20:18 menstruant; LEV 20:11 father's-wife with the legal-shame register), the Thai preserves the literal "uncovering" register `เปิดเผยความเปลือยเปล่า`.
- The intro verse 18:6 (programmatic for the whole catalog) uses the explicit form to set reader-expectation.

The trade-off — readability vs. lemma-preservation — is well-understood in translation: NIV / ESV / NRSV preserve "uncover the nakedness" literally throughout; NLT paraphrases to "have sexual relations"; THSV2011 uses a mixed strategy similar to Eremos. The Eremos hybrid is **not arbitrary** — it tracks Hebrew clarity vs. opacity within the same chapter.

**No corpus-doc covers this policy.** The doc `gender_passages_thai_register_2026-05.md` is scoped to Gen 1-3 + NT marriage passages (not LEV's incest / sexual-prohibition catalog). Recommend writing a short doc to lock the hybrid principle before Deuteronomy + Ezekiel ship.

**Forward-compounding:** Deut 22:30, Deut 27:20 (incest-curses), Ezek 16:8 (`כְּסוּתִי` "I spread my garment over your nakedness" — divine-marriage metaphor), Ezek 22:10 (legal-condemnation of incest), Ezek 23:18+29 (allegorical-prophetic sexual register). Also **1 Cor 5:1** (Paul invokes LEV 18:8 + 20:11 directly: γυναῖκά τινα τοῦ πατρὸς ἔχειν "to have his father's wife") — the NT-side Thai must echo the LEV-locked Thai for the Pauline citation to read as a citation.

**Question:** Should the project write a corpus-doc `docs/translator_decisions/uncover_nakedness_euphemism_2026-05.md` that (a) names the hybrid principle (explicit-in-clear-context vs. euphemism-preservation-in-anatomical-context), (b) provides verse-by-verse rationale for the LEV 18 + LEV 20 split (which Hebrew contexts cue which Thai form), and (c) forward-cover for Deuteronomy + Ezekiel + 1 Cor 5:1 NT-citation? Or should the policy be normalized — either uniformly euphemism-preserving (`เปิดเผยความเปลือยเปล่า` throughout) or uniformly explicit (`มีความสัมพันธ์ทางเพศ` throughout)?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
