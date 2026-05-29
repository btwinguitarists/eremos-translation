# Nehemiah — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-29**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Nehemiah** (13 chapters, 405 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings complete (not yet tagged). Nehemiah 13/13 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — How should a foreign (Persian) monarch be honored in Thai? Ezra and Nehemiah, two adjacent shipped books, now render the SAME king two different ways

**The pattern:** Thai has a royal honorific register (ราชาศัพท์) — `ทรง` before verbs, `พระองค์` / `เสด็จ` / `พระ-` noun-elevation, `ตรัส` (royal "say") — that the Eremos translation reserves, per `ot_register_policy_2026-05.md`, for God and for legitimate kings. The book of Ezra (already shipped) **deliberately deferred** the question of whether a sympathetic *Gentile* emperor (Cyrus, Darius, Artaxerxes) should receive this register, parking it for a corpus decision spanning "Ezra–Nehemiah–Esther–Daniel." As shipped, **Ezra withholds `ทรง` from the Persian king in narrator voice** (commoner register, to match the already-shipped 2 Chr 36:23). **Nehemiah — the very next book — grants the same king full ราชาศัพท์ in narrator voice**, citing `ot_register_policy §2.2` ("foreign emperors get ราชาศัพท์") at nearly every verse. Both books are shipped; neither is tagged; the conflicting king is **Artaxerxes**, who commissions Ezra (Ezra 7) and Nehemiah (Nehemiah 2).

**Ezra (no `ทรง` for the king — narrator voice):**
- EZR 1:7 HEB: `וְהַמֶּלֶךְ כּוֹרֶשׁ הוֹצִיא אֶת־כְּלֵי בֵית־יְהוָה` → TH: `กษัตริย์ไซรัสยังได้นำเครื่องใช้แห่งพระนิเวศขององค์พระผู้เป็นเจ้าออกมา` (plain `ได้นำ…ออกมา`, no `ทรง`)
- EZR 6:1 → TH: `กษัตริย์ดาริอัสจึงสั่งให้ค้น…` (plain `สั่ง`)

**Nehemiah (full `ทรง`/`พระ-` for the king — narrator voice):**
- NEH 2:2 HEB: `וַיֹּאמֶר לִי הַמֶּלֶךְ` → TH: `กษัตริย์**ตรัส**กับข้าพเจ้า` (royal speech verb; likewise 2:4, 2:6)
- NEH 2:9 HEB: `וַיִּשְׁלַח עִמִּי הַמֶּלֶךְ` → TH: `กษัตริย์**ทรงส่ง**บรรดานายทหาร…` (explicit `ทรงส่ง`)
- NEH 5:14 HEB: `אֲשֶׁר־צִוָּה אֹתִי…אַרְתַּחְשַׁסְתְּא` → TH: `กษัตริย์อารทาเซอร์ซีส**ทรงแต่งตั้ง**ให้ข้าพเจ้าเป็นเจ้าเมือง`
- NEH 2:1/2:5/2:6 royal nouns: `พระพักตร์` (the king's presence), `พระทัย` (the king's pleasure), `พระเนตร`, `พระกรรณ` (6:7), `พระมเหสี…ประทับ` (the queen, 2:6)

**The policy tension:** `ot_register_policy §2.2`'s table actually *prescribes* Nehemiah's choice — its row reads "Foreign emperors (Pharaoh, Nebuchadnezzar, Cyrus, Darius, Xerxes) → ราชาศัพท์ (ทรง)… even if villainous." So Nehemiah follows the written rule and **Ezra is the outlier** — but Ezra's commoner-register choice (matching 2 Chr 36:23) was the one the project deferred for ratification, and that ratification never happened. Separately and consistently in **both** books, the *Hebrew* court-servant (Ezra; Nehemiah-the-cupbearer/governor) is held in **plain** register per the §2.5 Joseph-vizier sub-rule — that part is not in question; only the *emperor's* register is.

**Forward-compounds to:** Esther (Ahasuerus, the central royal figure) and Daniel (Nebuchadnezzar, Belshazzar, Darius, Cyrus) — the rest of the OT's Persian/Babylonian court.

**Two questions:** (1) Should a sympathetic foreign emperor receive **full Thai royal honorifics in narrator voice** (the Nehemiah / written-`§2.2` approach — sovereignty, not covenant status, triggers ราชาศัพท์), or should Gentile emperors be held in **commoner register** in narrator voice (the Ezra / 2 Chr 36:23 approach), reserving deference for in-court reported speech only? (2) Whichever rule is chosen, it must be applied to **both** Ezra and Nehemiah (and written into a corpus doc before Esther/Daniel) so the same king is not honored two different ways across a book boundary — which book should be normalized to match the other?

---

## Item B — Nehemiah 9:17 drifts from the locked Exodus-34 "gracious and merciful, slow to anger, abounding in steadfast love" formula

**The locked rule:** `exod_34_attribute_formula_2026-05.md` locks the Sinai self-revelation formula (Exod 34:6) to a single canonical Thai surface across all its OT occurrences "so the Decalogue formula and the Sinai-revelation formula read as the same canonical text-thread." Its table **explicitly lists Nehemiah 9:17** with the locked form. The locked component renderings are: `חַנּוּן` → **ทรงพระคุณ**; `רַחוּם` → **ทรงพระเมตตา**; `אֶרֶךְ אַפַּיִם` → **ทรงกริ้วช้า**; `רַב־חֶסֶד` → **ทรงบริบูรณ์ด้วยความรักมั่นคง** (the chesed lock per `chesed_covenant_love_2026-05.md`).

**The verse — the climax of Nehemiah's penitential prayer (the longest prayer in the OT):**
- NEH 9:17 HEB: `…וְאַתָּה אֱלוֹהַּ סְלִיחוֹת חַנּוּן וְרַחוּם אֶרֶךְ אַפַּיִם וְרַב־חֶסֶד וְלֹא עֲזַבְתָּם`
- **Locked (per the doc):** `พระเจ้าผู้ทรงประทานการอภัย ทรงพระคุณและทรงพระเมตตา ทรงกริ้วช้า ทรงบริบูรณ์ด้วยความรักมั่นคง`
- **Shipped:** `…แต่พระองค์ทรงเป็นพระเจ้าผู้อภัย ผู้ทรงพระคุณและทรงเมตตา ทรงพระพิโรธช้า และเปี่ยมด้วยความรักมั่นคง พระองค์มิได้ทรงทอดทิ้งพวกเขา`

| Component | Hebrew | Locked | Shipped | Match? |
|---|---|---|---|---|
| God of forgiveness | אֱלוֹהַּ סְלִיחוֹת | พระเจ้าผู้ทรงประทานการอภัย | พระเจ้าผู้อภัย | ✗ |
| gracious | חַנּוּן | ทรงพระคุณ | ทรงพระคุณ | ✓ |
| compassionate | רַחוּם | ทรงพระเมตตา | ทรงเมตตา | ✗ (missing พระ) |
| slow to anger | אֶרֶךְ אַפַּיִם | **ทรงกริ้วช้า** | **ทรงพระพิโรธช้า** | ✗ |
| abounding in chesed | רַב־חֶסֶד | **ทรงบริบูรณ์ด้วยความรักมั่นคง** | **เปี่ยมด้วยความรักมั่นคง** | ✗ (chesed token kept; frame changed) |

**The short-form echo also drifts:** NEH 9:31 HEB `אֵל־חַנּוּן וְרַחוּם אָתָּה` → shipped `เพราะพระองค์ทรงเป็นพระเจ้าผู้ทรงพระคุณและทรงเมตตา` (again `ทรงเมตตา`, not the locked `ทรงพระเมตตา`).

**Why the automated checks passed it:** `check_phrase_consistency.py` audits the embedded chesed token `ความรักมั่นคง` (present and correct here) but **not** the full Exod-34 attribute-formula string, so the `ทรงกริ้วช้า`→`ทรงพระพิโรธช้า` and `ทรงบริบูรณ์ด้วย`→`เปี่ยมด้วย` deviations are invisible to it. This is the same class of drift the Jonah 4:2 `רַב־חֶסֶד` rendering caused (flagged MAJOR CONCERN by external AI in 2026-05, then normalized).

**Two questions:** (1) Is the shipped NEH 9:17 (`ทรงพระพิโรธช้า` / `เปี่ยมด้วยความรักมั่นคง` / `พระเจ้าผู้อภัย`) an acceptable variant, or should it be normalized to the locked canonical surface (`ทรงกริ้วช้า` / `ทรงบริบูรณ์ด้วยความรักมั่นคง` / `พระเจ้าผู้ทรงประทานการอภัย`) so the Exod-34 leitwort reads identically here and at Exod 34:6, Num 14:18, Pss 86/103/145, Joel 2:13, Jonah 4:2, 2 Chr 30:9? (2) Is `ทรงกริ้วช้า` or `ทรงพระพิโรธช้า` the better Thai for `אֶרֶךְ אַפַּיִם` ("slow to anger / long of nostrils") in a high register addressed to God — and does the distinction matter enough to enforce corpus-wide?

---

## Item C — Persian governor-title is rendered three ways in Nehemiah and diverges from Ezra

**The pattern:** Nehemiah is the governor (Hebrew `פֶּחָה`; Persian title `תִּרְשָׁתָא`, Tirshatha) of the sub-province of Judah within the Trans-Euphrates satrapy. The translation renders the gubernatorial title inconsistently:

| Hebrew | Thai | Refs | Who |
|---|---|---|---|
| פֶּחָה | **เจ้าเมือง** ("city/town lord") | NEH 5:14, 5:18, 2:7, 2:9, 3:7 | Nehemiah / regional governors |
| פֶּחָה | **ผู้ว่าราชการ** ("provincial governor") | NEH 12:26 | Nehemiah |
| תִּרְשָׁתָא | **ผู้ว่าราชการ** | NEH 7:65, 7:69, 8:9, 10:2 | Nehemiah |
| פֶּחָה | **ผู้ว่าราชการแคว้น** ("satrapy governor") | EZR 5:3, 5:6, 6:6, 6:13 | Tattenai (the satrap, in Ezra) |

**Sample verses:**
- NEH 5:14 HEB: `אֹתִי לִהְיוֹת פֶּחָם בְּאֶרֶץ יְהוּדָה` → TH: `…ทรงแต่งตั้งให้ข้าพเจ้าเป็น**เจ้าเมือง**ในแคว้นยูดาห์`
- NEH 12:26 HEB: `נְחֶמְיָה הַפֶּחָה` → TH: `เนหะมีย์**ผู้ว่าราชการ**`
- NEH 8:9 HEB: `נְחֶמְיָה הוּא הַתִּרְשָׁתָא` → TH: `เนหะมีย์**ผู้ว่าราชการ**`
- EZR 5:3 (Tattenai the satrap) → TH: `…**ผู้ว่าราชการแคว้น**ฟากตะวันตกของแม่น้ำ`

There may be a defensible tier (`เจ้าเมือง` = governor of the small Judah province; `ผู้ว่าราชการแคว้น` = satrap of the whole region) — in which case Nehemiah's default `เจ้าเมือง` is right and Ezra's Tattenai correctly sits a level up. But **NEH 12:26 calls Nehemiah `ผู้ว่าราชการ`, not `เจ้าเมือง`**, breaking even the internal pattern, and `תִּרְשָׁתָא` (a distinct Persian loanword-title) is silently collapsed into `ผู้ว่าราชการ` with no rationale recorded. (The mechanical key-term checker is clean because `פֶּחָה`/`תִּרְשָׁתָא` are not registered key terms.) "Beyond the River" itself is uniform and matches Ezra: `(แคว้น)ฟากตะวันตกของแม่น้ำยูเฟรติส` (NEH 2:7, 2:9, 3:7).

**Question:** Is there a principled tier the rendering should follow — e.g. `เจ้าเมือง` for the sub-provincial `פֶּחָה`/Tirshatha (Nehemiah, governor of Judah) vs `ผู้ว่าราชการแคว้น` for the satrap-level `פֶּחָה` (Tattenai) — and if so, should NEH 12:26 (and the Tirshatha occurrences) be normalized to it? Or should all Persian-period `פֶּחָה`/`תִּרְשָׁתָא` collapse to one Thai surface across Ezra–Nehemiah–Esther–Daniel? Should `תִּרְשָׁתָא` be transliterated (e.g. `เทอร์ชาธา`) to preserve the distinct Persian title, or is translating it as `ผู้ว่าราชการ` the right reader-first call?

---

## Item D — Nehemiah and the Greek tradition (Esdras B / 1 Esdras): does the MT-anchored policy owe any disclosure?

**The pattern:** The Eremos OT is **MT-anchored** (`ot_canon_and_text_base_2026-05.md`). For verse-level MT-vs-LXX divergence, `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3 sets a *disclosure floor*: a book with no macro-structural / canonically-visible / materially-reader-affecting divergence is COMPLIANT with zero textual-variant entries. Nehemiah's `textual_variants` files (chapters 1, 5, 8, 9) are all YHWH-footnote-only; there are no inclusion-variant entries. The single MT-vs-parallel decision — the **"horses 736 + mules 245" line of Ezra 2:66 is absent from MT Nehemiah 7** (MT NEH 7 = 72 verses; English/BSB re-adds it as 7:69 to reach 73) — is documented **inline** in the NEH 7:68 translator note ("ฉบับเอเรโมสยึดตาม MT"), not as a textual-variant entry.

**The Greek situation:** Greek Nehemiah is **Esdras B** (= LXX Ezra–Nehemiah), a fairly literal rendering close to MT. The divergent recension **1 Esdras (Esdras A)** — famous for reordering the Ezra material and adding the "contest of the three guardsmen" — carries only a slice of Nehemiah (NEH 7:73–8:12, the Ezra-reads-the-Law assembly), grafted into its Ezra-centred narrative. So for Nehemiah the Greek divergence is minor and structural, not verse-level — below the §2.3 floor, the same disposition Ezra reached.

**Question:** Under the project's MT-anchored policy, does Nehemiah owe any disclosure for its Greek-tradition situation — e.g. a single book-level note recording "MT Nehemiah is the base; Esdras B is the close Greek translation and 1 Esdras is a separate recension carrying only NEH 7:73–8:12, so no per-verse disclosure is owed" — or is silence fully appropriate (as for Ezra), with the one MT/English versification difference at 7:68 already handled inline?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
