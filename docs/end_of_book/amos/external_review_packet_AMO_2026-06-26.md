# Amos — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-26**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Amos** (9 chapters, 146 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Amos 9/9 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — אֲדֹנָי יְהוִה "Lord GOD": Amos surfaces the compound where the rest of the corpus collapses it (DECIDE)

**The crux.** Amos is saturated with the divine compound אֲדֹנָי יְהוִה ("Lord GOD") — 20 verses, the dominant divine title of the book, especially in the vision cycle (chs 7–9). Amos renders it **`องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย`** ("the LORD who is the Lord/Master") — *surfacing* the doubled-lord in the visible text. **The entire rest of the corpus collapses the same compound to bare `องค์พระผู้เป็นเจ้า`** (Adonai dropped), per the locked rule in `divine_names_table_2026-05`: Ezekiel renders all **217** occurrences bare, Isaiah ~30 bare, Jeremiah bare in mid-sentence appositional position.

- **HEB (3:7, plain mid-sentence compound):** `כִּי לֹא יַעֲשֶׂה אֲדֹנָי יְהוִה דָּבָר`
- **BSB:** "Surely the Lord GOD does nothing…"
- **TH (Amos):** `แท้จริง**องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย**จะไม่ทรงกระทำสิ่งใดเลย`
- **TH (locked corpus rule, e.g. Ezekiel 5:7 / Isaiah 7:7):** `องค์พระผู้เป็นเจ้า` (bare — Adonai dropped)

19 of Amos's 20 marked verses are the **plain** compound (1:8; 3:7, 8, 11; 4:2, 5; 5:3; 7:1, 2, 4, 5, 6; 8:1, 3, 9, 11; 9:5, 8 — plus 3:13/6:8 with the "of Hosts" stack), i.e. exactly the form the locked rule says to render bare. The chapter `key_decisions` justify the marking by citing a doc, **`adonai_yhwh_2026-05`, that does not exist** in the repository.

**Why it matters.** It is a visible, cross-book inconsistency on the most frequent divine title in the book: a reader comparing Amos to Ezekiel/Isaiah sees two different Thai surfaces for the identical Hebrew compound. The only other corpus occurrences of the marked form are the Jeremiah **Oracles-Against-the-Nations** "Lord GOD of hosts" triple-stack (already a flagged REVIEW item there) — never the *plain* compound that Amos marks throughout. The mechanical checks pass because divine-name *surface* forms are not enforced.

**The decision.** **(a)** Normalize Amos to the locked bare `องค์พระผู้เป็นเจ้า` (conform to Ezekiel/Isaiah/Jeremiah), or **(b)** ratify a deliberate Amos marking convention, write the real doc, and reconcile the Jeremiah split. No translation change is made pending Ben's call.

**Two questions:**
1. For an OT translation that has **already shipped 217 Ezekiel + ~30 Isaiah + all Jeremiah** occurrences of אֲדֹנָי יְהוִה as bare `องค์พระผู้เป็นเจ้า` (Adonai collapsed, per a locked decision), is Amos's marked `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` an unacceptable corpus inconsistency that should be normalized down to bare — or is there a defensible case for *surfacing* the doubled-lord compound (e.g., to preserve the Hebrew's audible weight), even at the cost of re-opening the settled books?
2. Is there any **theological or register** reason a translation might legitimately distinguish אֲדֹנָי יְהוִה (`องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย`, "the Sovereign LORD") from bare יְהוָה (`องค์พระผู้เป็นเจ้า`) in the rendered text — or does collapsing both to the same surface (with the distinction preserved only in notes) lose something a reader should be able to feel?

---

## Item B — 9:11–12 the fallen booth of David + the MT/LXX/Acts 15 fork (DECIDE)

**The crux.** Amos's turn from doom to hope is the verse James quotes (from the **LXX**) at the Jerusalem Council to authorize the Gentile mission (Acts 15:16–17). The MT and LXX diverge by a **single consonant** that changes the meaning entirely.

- **HEB (9:11–12, MT):** `אָקִים אֶת־סֻכַּת דָּוִיד הַנֹּפֶלֶת … לְמַעַן יִירְשׁוּ אֶת־שְׁאֵרִית אֱדוֹם וְכָל־הַגּוֹיִם`
- **BSB:** "I will restore the fallen tent of David … that they may possess the remnant of Edom and all the nations that bear My name."
- **TH (Amos, MT surface):** `เราจะยก**พลับพลาของดาวิดที่ล้มลง**แล้วนั้นขึ้นใหม่ … เพื่อพวกเขาจะได้**ครอบครองชนเอโดมที่เหลืออยู่** และครอบครองประชาชาติทั้งปวงที่ถูกเรียกตามนามของเรา`
- **LXX / Acts 15:17 (shipped):** "that **the remnant of mankind** (אָדָם for אֱדוֹם) may **seek** (יִדְרְשׁוּ for יִירְשׁוּ) the Lord" — *conquest of Edom* becomes *conversion of mankind*.

**The decision made.** Eremos follows the **MT surface** ("possess the remnant of Edom"), and the amos_09 KD + `notes` disclose the LXX/Acts reading explicitly (the one-letter אֱדוֹם/אָדָם + יִירְשׁוּ/יִדְרְשׁוּ difference). The messianic content — `סֻכַּת דָּוִיד` "booth of David" — is rendered as the plain fallen Davidic dynasty (`พลับพลาของดาวิด`), with the christological/Acts fulfilment in apparatus, **not** asserted in the rendered text. This is the committal-messianic-surface policy ratified at Isaiah and applied at Joel 2:23.

**Why it needs ratification.** It is the book's marquee messianic/NT-cited verse; its disposition sets precedent for the Twelve's other messianic surfaces (Micah 5:2; Zechariah). A secondary question is the `סֻכָּה` rendering: `พลับพลา` connotes a royal **pavilion/tabernacle**, while `סֻכָּה` here is a humble "booth/hut" (the KD's own gloss) — `พลับพลา` may over-elevate the deliberately lowly image.

**Two questions:**
1. For an MT-anchored translation, is following the **MT** ("possess the remnant of **Edom**") with the LXX/Acts-15 reading ("remnant of **mankind** may **seek** the Lord") in a footnote the right call — given that Acts 15 builds its entire Gentile-inclusion argument on the **LXX** text — or should the LXX/NT reading be surfaced given its doctrinal weight?
2. Is `พลับพลา` ("pavilion/tabernacle") the right rendering for `סֻכַּת דָּוִיד`, or does it over-elevate the deliberately humble "booth/hut" image (`กระท่อม`/`เพิงพัก` would be lowlier) — and does the Davidic-restoration register justify the elevation?

---

## Item C — 5:25–27 → Acts 7:42–43 (Stephen): Sakkuth/Kiyyun (MT) vs Moloch/Rephan (LXX) (REVIEW)

**The situation.** Stephen's speech (Acts 7:42–43) quotes Amos 5:25–27 from the **LXX**, which differs substantively from the MT Amos ships. Eremos translates Amos from the **MT** and Acts from the **Greek**, so the two Thai surfaces legitimately differ.

- **HEB (5:26, MT):** `וּנְשָׂאתֶם אֵת סִכּוּת מַלְכְּכֶם וְאֵת כִּיּוּן צַלְמֵיכֶם`
- **TH (Amos, MT):** `พวกเจ้ากลับแบก**สิคูท**กษัตริย์ของพวกเจ้า และ**คิยยูน**รูปเคารพของพวกเจ้า` (Sakkuth/Kiyyun — Assyrian astral deities)
- **Acts 7:43 (LXX, shipped):** "**Moloch** … **Rephan**" (LXX vocalization/substitution); and 5:27 "beyond Damascus" (MT) → "beyond **Babylon**" (Acts).

The MT surface is correctly followed; the amos_05 KD + `notes` name the LXX/Acts 7:43 citation. This is the same disclosure question raised at Joel §9 and Jeremiah §9.

**Two questions:**
1. Confirm the policy: each text translated from its own base (MT for Amos, Greek for Acts), the NT citation disclosed in a footnote, the OT surface **not** harmonized to the NT quotation.
2. Does the substantive **Sakkuth→Moloch / Kiyyun→Rephan / Damascus→Babylon** divergence — on a passage a reader may cross-reference to Acts 7 — clear the Tier-2 reader-footer floor (modeled on the Jeremiah 31:32 → Heb 8:9 case), or is the existing KD/`notes` disclosure sufficient?

---

## Item D — 7:14 לֹא־נָבִיא אָנֹכִי: "I was" or "I am" no prophet? (REVIEW)

**The crux.** Amos's reply to the priest Amaziah is a tense-ambiguous verbless Hebrew clause. The choice carries exegetical weight.

- **HEB:** `לֹא־נָבִיא אָנֹכִי וְלֹא בֶן־נָבִיא אָנֹכִי כִּי־בוֹקֵר אָנֹכִי וּבוֹלֵס שִׁקְמִים`
- **BSB (past):** "I *was* not a prophet, nor was I the son of a prophet; rather, I was a herdsman and a tender of sycamore-fig trees."
- **TH (Eremos, present):** `ข้าพเจ้า**ไม่ใช่**ผู้เผยพระวจนะ และ**ไม่ใช่**ลูกของผู้เผยพระวจนะ ข้าพเจ้าเป็นเพียงคนเลี้ยงสัตว์ และเป็นคนดูแลต้นมะเดื่อ`

**The two readings.** The **present** ("I am not a prophet") makes Amos disclaim the *professional prophet-guild* — he is a layman called directly by YHWH (v.15 `וַיִּקָּחֵנִי יְהוָה` "the LORD took me"), even while he prophesies. The **past** ("I was not… until God took me") reads it biographically. The present reading is the majority modern view and coheres with v.15.

**Two questions:**
1. For this verbless clause, is the **present-tense** reading ("I am not a [professional] prophet") the better rendering — given v.15's commissioning — or does the BSB past-tense reading ("I was not") deserve to stand or be footnoted?
2. Does the past/present ambiguity (and the denial-of-guild vs denial-of-office distinction it encodes) warrant a one-line reader note, or is the present-tense rendering self-sufficient?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
