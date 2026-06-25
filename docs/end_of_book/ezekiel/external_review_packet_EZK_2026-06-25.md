# Ezekiel — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-25**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Ezekiel** (48 chapters, 1,273 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah complete (not yet tagged). Ezekiel 48/48 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
# Ezekiel (EZK) — end-of-book external-review items

_Hand-curated from the EZK end-of-book editorial review (`EZK_END_OF_BOOK_REVIEW_2026-06-25.md`). One block per REVIEW/DECIDE item worth an independent second opinion. The project follows the **Masoretic Text** surface, renders the Tetragrammaton יהוה → **องค์พระผู้เป็นเจ้า** and the Ezekiel-signature compound אֲדֹנָי יְהוִה ("Lord GOD," 217×) → **องค์พระผู้เป็นเจ้า**, uses Thai royal register (**ราชาศัพท์**, the ทรง/พระ- prefixes) for divine and royal referents, and per RULES §0 takes the evangelical-consensus reading in the main verse text while keeping interpretive notes descriptive (reporting a reading, not pastorally endorsing it)._

---

## Item A — A *codified, scaled-up* first-person-plain rule for God's body-parts (hand / eye / face)

**The pattern:** The translation locks God's body-part anthropomorphisms to Thai royal register: divine hand יָד → **พระหัตถ์**, divine eye עֵינַי → **พระเนตร**, divine face פָּנִים → **พระพักตร์**, divine arm זְרוֹעַ → **พระกร** (the doc `divine_anthropomorphism_thai_grammar_2026-05.md` states *no person-based exception*). In Ezekiel — the most anthropomorphism-dense book in the corpus — **first-person divine speech ("my hand / my eye / my face") systematically drops to plain register** (มือ / ตา / หน้า), and the rule is **operationalized at scale** in the `key_decisions` with a self-cross-referencing lock chain:

**Hand — same idiom, two registers, split on grammatical person:**
- 1:3 / 3:14 / 8:1 / 37:1 / 40:1 (3rd-person narration, "the hand of YHWH") → **พระหัตถ์** ✓ royal (7×)
- **6:14 (1st-person, drift)** HE `וְנָטִיתִי אֶת־יָדִי` → TH `เราจะเหยียด**มือ**ของเราออกต่อสู้` — KD: *"God's OWN hand in 1st-person speech → PLAIN มือ … contrast the narrator-voice royal พระหัตถ์ at 1:3."*
- **14:9, 14:13, 16:27, 25:7/13/16, 35:3** (1st-person) → all **มือ**.

**Eye — Ezekiel's signature refrain "my eye will not pity," all plain ตา, named "5:11 lock":**
- **5:11** HE `וְלֹא־תָחוֹס עֵינִי` → TH `**ตา**ของเราจะไม่เมตตา` — KD: *"God's OWN eye in 1st-person speech → PLAIN ตา (not royal พระเนตร)."* Also 7:4, 7:9 ("consistent with 5:11"), 8:18 (+ "my ears" → plain หู), 9:10 ("lock, 5:11"), 20:17.

**Face — all plain หน้า, codified:** 14:8 `וְנָתַתִּי פָנַי` → `เราจะหัน**หน้า**ของเรา` (KD: "1st-person convention"); 15:7 ("as 14:8").

**Two named exceptions create a second, finer split.** The fixed **Exodus power-formula** keeps royal even in 1st-person speech — 20:33–34 `בְּיָד חֲזָקָה וּבִזְרוֹעַ נְטוּיָה` → **พระหัตถ์**อันแข็งแกร่ง **พระกร**ที่เหยียดออก (KD: "lexicalized epithet keeps Rachasap"). So **within chapter 20**: "I withheld my **มือ**" (20:22) vs "with strong **พระหัตถ์** and outstretched **พระกร**" (20:33) — identical lemma יָד, same speaker, eleven verses apart. (The hedged vision-body-part "the form of a hand," 8:3, is a third, plain, exception.)

**Tally: ~22 first-person divine body-part verses render plain by stated rule; 0 render royal.** This is the same drift the Isaiah audit (§13, recommended reversal) and the Jeremiah audit (§13, a DECIDE item) flagged — now the largest, most rigorously-codified instance in the corpus, and invisible to mechanical checks (the KDs cite each other, so internal consistency is perfect).

**Two questions:**
1. Should God's first-person self-reference to his own hand/eye/face ("my hand / my eye / my face") take **plain** Thai register, or the **royal** register (ราชาศัพท์) the corpus locks for divine body-parts? Is there a sound Thai-grammar or theological basis for a *grammatical-person* exception (1st-person plain; 2nd/3rd-person royal), or does that produce an incoherent surface (the พระหัตถ์/มือ split for the identical "stretch out the hand" idiom within chapter 20)?
2. If a first-person-plain rule is ratified, are the two named carve-outs principled — the fixed **Exodus "mighty hand and outstretched arm" epithet** keeping royal (20:33–34), and the **hedged vision-body-part** ("what looked like a hand," 8:3) staying plain — and should the rule be applied retroactively to Isaiah and Jeremiah so all three major prophets are consistent before Daniel?

---

## Item B — Foreign-monarch register: every ruler is plain (a Latter-Prophets vs Writings genre split)

**The pattern:** The project's policy (`ot_register_policy §2.2`) gives foreign emperors full Thai royal register (ราชาศัพท์: ทรง/พระองค์/เสด็จ/ตรัส) **even if villainous**, and §2.6 extends ทรง even to narrator-voice emperor-action verbs; the already-audited **Daniel applies this to all four of its foreign emperors**. **Ezekiel renders every foreign and human ruler in plain register** — a full-book scan for ทรง/พระองค์/เสด็จ on ruler verses returns **zero hits**, including narrator-voice siege verbs:
- 26:8–9 (Nebuchadnezzar besieging Tyre) TH `เขาจะ**ฆ่า** … **ตั้ง**เครื่องล้อม … **ก่อ**เชิงเทิน` — all plain, the exact category §2.6 upgraded to ทรง for the Ezra block.
- 28:2 (king of Tyre, who claims "I am a god") → plain เจ้านาย/เจ้า, rebuked `เจ้าเป็นเพียงมนุษย์ ไม่ใช่พระเจ้า`.
- 29:3 (Pharaoh) → plain เจ้า + the mocking image สัตว์ร้ายมหึมา "the great monster."

The same king **Nebuchadnezzar is plain in Ezekiel and Jeremiah but royal (ทรง) in Daniel.** Ezekiel's choice is internally consistent and *considered* (12:12 reasons to plain via the royal-shame downshift; 38:3/39:1 keep Gog plain via the §3 adversary rule), and is rhetorically defensible — granting ราชาศัพท์ to the self-deifying king of Tyre or the "great monster" Pharaoh would undercut the judgment oracles. But it is **not what §2.2/§2.6 as written require.** As the third data point (after Jeremiah and Daniel), Ezekiel tips the corpus into a genre-level pattern: *Latter-Prophets judgment oracles flatten foreign rulers; Writings court-narratives dignify them.* The governing `foreign_monarch_register` doc has been owed since the Ezra audit and **still does not exist.**

**Two questions:**
1. Should a hostile, condemned foreign ruler in **prophetic judgment-oracle voice** (Nebuchadnezzar, Pharaoh, the king of Tyre in Ezekiel) receive full Thai royal register matching Daniel and §2.2's "even if villainous" rule — or is a documented **genre exception** (plain register for condemned rulers in oracle voice; royal only in court-narrative voice) the right resolution, given that Jeremiah and Ezekiel now agree against Daniel on the *same king*?
2. Is it theologically coherent to give the **king of Tyre** royal honorifics (ราชาศัพท์) in the very oracle that condemns him for claiming divinity (28:2) — i.e., does withholding royal register from a self-deifying or "monster"-figured ruler serve the text, or does consistency with the foreign-emperor policy outweigh the local rhetoric?

---

## Item C — Messianic/Davidic notes assert "is the Christ" as fact (a step past Isaiah and Jeremiah)

**The pattern:** Per RULES §0 the project takes the evangelical-consensus reading in the **verse text** but keeps interpretive **notes descriptive** — reporting a reading or what the NT does, not asserting fulfillment as fact in the translator's own voice. The Jeremiah audit judged its most-forward note (31:31, *"cited in Hebrews 8/10 as fulfilled in Christ"*) §0-compliant precisely because it **reports what Hebrews does** (a citation-fact), and praised Jeremiah as "§0-cleaner than Isaiah." **Ezekiel's reader-facing `thai_summary` notes regress past that bar** — several state the identification as bare fact:

- **34:23** (the one-shepherd / "my servant David" oracle) summary: *"…หมายถึงเชื้อสายของดาวิด **คือพระคริสต์** ผู้เลี้ยงแกะที่ดี (ยอห์น 10:11)"* — "means the seed of David, **who is the Christ**, the Good Shepherd (John 10:11)."
- **34:1** summary: *"…เป็นภาพล่วงหน้าของพระเยซู ผู้เลี้ยงแกะที่ดี"* — "a foreshadowing of Jesus" (stated as fact).
- **17:22** (the tender cedar-shoot) summary: *"กษัตริย์ในวงศ์ดาวิดที่แท้จริง**คือพระคริสต์**"* — "the true Davidic king **is the Christ**."
- **21:32** ("until he comes whose right it is," echoing Gen 49:10): *"…จะได้รับการสถาปนาใหม่**ในพระคริสต์** ผู้ทรงเป็นกษัตริย์โดยชอบธรรม"* — "re-established **in Christ**."

The **verse text itself is clean** everywhere (e.g. 34:23 main text = `ผู้เลี้ยงแกะคนเดียว … คือดาวิดผู้รับใช้ของเรา`, no Christ-identification), and "my servant David" carries correct plain register (future, not-yet-reigning figure). A **report-form template already exists in the same book** and is §0-correct: 47:1 *"ภาพนี้สำเร็จในวิวรณ์ 22:1"* ("this image is fulfilled in Rev 22:1"), 17:23b *"พระเยซูทรงนำภาพนี้ไปใช้ใน…มัทธิว 13:32"* ("Jesus applies this image in Matt 13:32"). Both report *what the NT text does* rather than asserting the OT verse's referent.

**Question:** Should the assertive messianic clauses (34:23, 34:1, 17:22, 21:32 — "is the Christ / a foreshadowing of Jesus / re-established in Christ") be down-toned to the report-form the same book already uses elsewhere (e.g. "in Christian interpretation this is read as the Davidic Messiah" / "the New Testament applies this to Christ in John 10:11") to stay within RULES §0 — or is a Davidic-messianic identification stated as fact acceptable in a reader note for these particular oracles? (The verse text needs no change; this is purely a note-layer register question, and it sets the precedent for Daniel 7 and Zechariah.)

---

## Item D — MT/LXX temple-vision measurements: incomplete, structurally-fragile disclosure

**The pattern:** Ezekiel is the OT's densest cluster of measurement-textual cruxes (the temple vision, chs. 40–48), where the Masoretic Text and the Septuagint (often followed by modern English versions like the BSB) give different dimensions. The project correctly translates the **MT** surface. But disclosure to the reader is thin and fragile: every chapter carries exactly one reader-facing `textual_variants` footnote — the Tetragrammaton first-occurrence note — and **the few measurement notes that exist are bundled *inside* that divine-name footnote**, so a reader who doesn't open the YHWH footnote never sees them. Only **3 of 9** temple chapters disclose anything:
- ch. 40 (v. 49): MT "eleven cubits" / no steps vs LXX "twelve cubits" + "ten steps."
- ch. 42 (v. 4, 16–20): MT אַמָּה אֶחָת "one cubit" (likely a scribal slip for מֵאָה "hundred") vs LXX/BSB "hundred cubits"; v. 16–20 MT "500 reeds" vs BSB "500 cubits."
- ch. 45 (v. 1): MT "ten thousand" vs LXX/BSB "twenty thousand."

Chapters **41, 43, 44, 46, 47, 48 disclose nothing**; further cruxes (40:14, 42:16 reeds-vs-cubits, 45:12 the 60-shekel mina) live only in internal `key_decisions`, which are never rendered to readers. There is **no book-level or temple-section disclosure note.** (By contrast, ch. 7's footnote *does* reader-facingly disclose the MT/LXX verse-order difference at 7:3–9 — the model to follow.) The corpus policy `mt_vs_lxx_textual_variant_handling §2.3` sets a disclosure floor for reader-affecting divergences, and the Jeremiah audit (§9) made the analogous macro-divergence disclosure a decision item.

**Question:** For a book whose defining textual feature is the temple-vision measurements, is a single **temple-section (40–48) disclosure note** warranted — e.g. "Eremos follows the Masoretic measurements throughout the temple vision; the Septuagint and English versions differ in places (40:49, 42:4/16–20, 45:1, …)" — and should measurement cruxes be moved out of the Tetragrammaton footnote into a **separate, non-divine-name textual footer** so they aren't dependent on the reader opening the divine-name note? Or is the current bundled, partial disclosure acceptable for dimensional (non-doctrinal) variants?

---

## Item E — "son of man" (בֶּן־אָדָם) — a three-way Thai system the policy doc doesn't yet sanction

**The pattern:** God addresses Ezekiel as בֶּן־אָדָם ("son of man" = mortal/human one) **93 times**, all rendered uniformly **บุตรแห่งมนุษย์เอ๋ย** (with the connector **แห่ง** + vocative particle **เอ๋ย**). This is deliberately **distinct** from the Christological title ὁ υἱὸς τοῦ ἀνθρώπου / Danielic בַּר אֱנָשׁ, which the project renders **บุตรมนุษย์** (no connector; Dan 7:13, the Gospels). The OT *mortal*-sense แห่ง-form is also used at Dan 8:17 (the angel addressing Daniel) and Ps 8:4 (generic humanity) — so the project effectively runs a three-way system: title **บุตรมนุษย์** / generic-plural **บุตรของมนุษย์** / mortal-address **บุตรแห่งมนุษย์**. The execution is flawless and internally consistent. **However**, the governing doc `son_of_man_disambiguation_2026-04.md` is NT-scoped and its "alternatives considered" section **explicitly rejected the แห่ง form** ("the established Thai Christian pattern is บุตรมนุษย์ without แห่ง") — a rejection aimed at the *NT title*, but on its face the shipped Ezekiel mortal-address is the very form the doc rejects.

**Question:** Is the three-way distinction — reserving **บุตรมนุษย์** (no connector) for the Christological title, **บุตรแห่งมนุษย์** (with แห่ง) for the OT prophetic mortal-address (Ezekiel ×93, Dan 8:17, Ps 8:4), and **บุตรของมนุษย์** for the generic plural — a sound and natural disambiguation in Thai, such that the policy doc should be amended to register and authorize it? Or does the แห่ง form risk being heard as the messianic title by Thai readers, arguing for a different mortal-address rendering?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
