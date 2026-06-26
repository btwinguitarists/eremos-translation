# Obadiah — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-26**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Obadiah** (1 chapters, 21 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Obadiah 1/1 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — אֲדֹנָי יְהוִה "Lord GOD" at OBA 1:1: Obadiah renders the compound BARE, where Amos surfaces it (REVIEW)

**The situation.** Obadiah's superscription opens with the divine compound אֲדֹנָי יְהוִה ("Lord GOD"), and Obadiah renders it **bare** `องค์พระผู้เป็นเจ้า` (the Adonai dropped) — exactly the locked corpus convention. This matters because the **immediately preceding book, Amos, renders the identical compound differently** — `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` ("the LORD who is the Lord/Master"), surfacing the doubled-lord — in 20 verses, and that inconsistency is the headline DECIDE blocking Amos's v1 tag.

- **HEB (OBA 1:1):** `כֹּה־אָמַר אֲדֹנָי יְהוִה לֶאֱדוֹם … שְׁמוּעָה שָׁמַעְנוּ מֵאֵת יְהוָה`
- **BSB:** "This is what the Lord GOD says about Edom… We have heard a message from the LORD"
- **TH (Obadiah):** `องค์พระผู้เป็นเจ้าตรัสเกี่ยวกับเอโดมดังนี้ว่า … เราได้ยินข่าวจากองค์พระผู้เป็นเจ้า`
- **TH (Amos, e.g. 3:7):** `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย…` (the marked form)
- **TH (locked corpus rule — Ezekiel 217×, Isaiah ~30×, Jeremiah):** `องค์พระผู้เป็นเจ้า` (bare)

Obadiah's per-verse `key_decisions` cites the **real** locked doc (`divine_names_table_2026-05`), not the phantom `adonai_yhwh_2026-05` that Amos's KDs cite, and the chapter footnote discloses the compound collapse to the reader. So Obadiah is a **clean, conforming data point**: the bare rule applying naturally at a fresh book boundary.

**Why it's surfaced.** The corpus has shipped 217 Ezekiel + ~30 Isaiah + all Jeremiah occurrences of אֲדֹנָי יְהוִה as bare `องค์พระผู้เป็นเจ้า` per a locked decision, and Obadiah now follows suit. The only live tension is the open Amos question (normalize Amos down to bare, vs ratify Amos's marked surface and re-open the settled books). Obadiah's single occurrence is correct under "normalize to bare" and would only need changing under "ratify the marked surface."

**Two questions:**
1. For an OT translation that renders אֲדֹנָי יְהוִה as bare `องค์พระผู้เป็นเจ้า` everywhere (Ezekiel/Isaiah/Jeremiah/Obadiah) **except Amos** (marked `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย`), is the **bare collapse** the right corpus-wide surface — preserving the Adonai-YHWH distinction only in footnotes/`key_decisions` — or is there a defensible case for *surfacing* the doubled-lord compound in the rendered Thai (which would require re-opening the bare books)?
2. Is there any **theological or register** reason a Thai translation should distinguish אֲדֹנָי יְהוִה from bare יְהוָה in the visible text, or does collapsing both to `องค์พระผู้เป็นเจ้า` (distinction preserved in apparatus) lose nothing a reader needs to feel?

---

## Item B — OBA 1–9 ∥ Jeremiah 49:7–22: the two Edom oracles translated independently (REVIEW)

**The situation.** Obadiah 1–9 is a near-doublet of Jeremiah 49:7–22, the corpus's other extended oracle against Edom. Both books are translated **independently** from their own Masoretic context. This **correctly preserves genuine textual differences** between the two — but produces **incidental synonym-drift** on phrases that are word-for-word identical in Hebrew.

**Genuine MT difference, correctly preserved:**
- **OBA 1:1** `שְׁמוּעָה שָׁמַעְנוּ` ("**we** have heard," 1cp) → `**เรา**ได้ยินข่าว`
- **JER 49:14** `שְׁמוּעָה שָׁמַעְתִּי` ("**I** have heard," 1cs) → `**ข้าพเจ้า**ได้ยินข่าว`

(Harmonizing the two would erase this real distinction.)

**Incidental drift on identical Hebrew:**
- `זְדוֹן לִבְּךָ הִשִּׁיאֶךָ` (OBA 3 / JER 49:16) → Obad `ความ**เย่อหยิ่ง**ในใจของเจ้าได้หลอกลวงเจ้า` / Jer `ความ**หยิ่งยโส**ในใจของเจ้าได้หลอกลวงเจ้า`
- `שֹׁכְנִי בְחַגְוֵי־סֶלַע` (OBA 3 / JER 49:16) → Obad `ผู้อาศัยอยู่ใน**ซอกหินผา**` / Jer `ผู้อาศัยอยู่ตาม**ซอกหิน**`
- `מִשָּׁם אוֹרִידְךָ נְאֻם־יְהוָה` (OBA 4 / JER 49:16) → Obad `…องค์พระผู้เป็นเจ้า**ตรัสดังนี้**` / Jer `…องค์พระผู้เป็นเจ้า**ตรัสไว้ดังนี้**`

No automated check catches this — the passages are in different books and the phrases are not registered phrase-locks. A reader cross-referencing the two Edom oracles sees gratuitous variation where the Hebrew source is identical. The current independent-translation policy is how every doublet in the corpus has been handled (Ps 14∥53; Isa 2∥Mic 4; 2 Kgs 18–20∥Isa 36–39).

**Two questions:**
1. For two passages whose Hebrew is identical (e.g. `זְדוֹן לִבְּךָ הִשִּׁיאֶךָ`), should the Thai be **harmonized** so the reader sees the same wording in both Edom oracles — or is **independent translation per book-context** the right principle even at the cost of incidental synonym-drift, given that it also preserves the genuine `שָׁמַעְנוּ`/`שָׁמַעְתִּי` ("we"/"I") difference?
2. Where the MT genuinely differs between parallel passages (the we/I case), is preserving that difference in Thai (`เรา` vs `ข้าพเจ้า`) clearly correct — or does the risk of a reader mistaking it for translator inconsistency argue for a reader-note flagging the Obadiah∥Jeremiah-49 relationship?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
