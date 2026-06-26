# Micah — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-26**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Micah** (7 chapters, 105 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Micah 7/7 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — Micah 4:1–3 ∥ Isaiah 2:2–4: the shared vision is HARMONIZED, where Obadiah ∥ Jeremiah-49 was kept independent (DECIDE)

**The situation.** Micah 4:1–3 ("In the last days the mountain of the house of the LORD will be established…they will beat their swords into plowshares…") is a near-verbatim doublet of Isaiah 2:2–4. The Eremos edition **harmonizes** Micah to the Isaiah surface — the translator's own note says *"มีคาห์ 4:1–3 ขนานเกือบทุกคำกับ อิสยาห์ 2:2–4 ฉบับเอเรโมสแปลให้สอดคล้องกัน"* ("…translates them to match") — so the two pilgrimage-of-the-nations visions read identically in Thai.

This is the **opposite** treatment to the immediately preceding book. Obadiah 1–9 ∥ Jeremiah 49:7–22 (the two Edom oracles) were translated **independently** from each Masoretic context, which preserved a genuine MT difference (`שָׁמַעְנוּ` "we have heard," Obad → `เรา…ได้ยิน` vs `שָׁמַעְתִּי` "I have heard," Jer → `ข้าพเจ้า…ได้ยิน`) but produced incidental synonym-drift on word-for-word-identical Hebrew phrases.

- **HEB (MIC 4:3 / ISA 2:4, identical):** `וְכִתְּתוּ חַרְבֹתֵיהֶם לְאִתִּים וַחֲנִיתֹתֵיהֶם לְמַזְמֵרוֹת`
- **TH (Micah 4:3, matched to Isaiah):** `พวกเขาจะตีดาบของตนเป็นผาลไถนา และตีหอกของตนเป็นมีดลิดแขนง`
- **Contrast — HEB (OBA 3 / JER 49:16, identical):** `שֹׁכְנִי בְחַגְוֵי־סֶלַע` → Obad `ซอกหินผา` / Jer `ซอกหิน` (drifted)

A third data point: Micah 4:3 (swords → plowshares) is the deliberate **inversion** of Joel 4:10 (plowshares → swords), and the translator correctly **preserved** that inversion rather than harmonizing it away.

**Why it's surfaced (and why it's a fork, not a confirmation).** At the Obadiah audit the practice was *uniform* — every doublet had been independent — so the policy could simply be "confirmed," and that audit's §2 table even listed "Isa 2∥Mic 4" as an example of *independent* translation. Micah's actual practice contradicts that: the corpus now **harmonizes one doublet and preserves another.** A `parallel_passage_doublets` corpus doc cannot be written until the governing principle is fixed, because it would otherwise have to assert both "independent" and "harmonized" with no stated distinction. The translator's implicit principle is coherent — harmonize verbatim-identical shared vision/liturgical text; preserve independently-reworked oracles that carry real MT differences; preserve deliberate inversions — but it is undocumented and the surface contradiction is reader-visible.

**Three questions:**
1. For a doublet whose Hebrew is **word-for-word identical** and which functions as a shared liturgical/vision text (Mic 4:1–3 ∥ Isa 2:2–4), is **harmonizing** the Thai so both read identically the right principle — even though the corpus translated the Obadiah ∥ Jeremiah-49 Edom doublet **independently**?
2. Is the distinguishing principle — **harmonize** verbatim-identical shared vision-text, **preserve independence** for reworked oracles with genuine MT differences (the `שָׁמַעְנוּ`/`שָׁמַעְתִּי` case), **preserve** deliberate inversions (Mic 4:3 ∥ Joel 4:10) — the right three-way rule to lock corpus-wide for the remaining doublets (Ps 14∥53, 2 Kgs 18–20∥Isa 36–39, and others ahead in the Twelve)?
3. Where the two members of a doublet are harmonized, does the reader need a footnote flagging the parallel (Micah 4 carries one), and where they are kept independent, does the reader need a note explaining that the variation reflects the Hebrew rather than translator inconsistency?

---

## Item B — אֲדֹנָי יְהוִה "Lord GOD" at MIC 1:2: Micah renders the compound BARE, where Amos surfaces it (REVIEW)

**The situation.** Micah's cosmic-courtroom summons (1:2) carries **both** divine forms in a single verse: the compound `אֲדֹנָי יְהוִה` and, a few words later, a free-standing `אֲדֹנָי`. Micah renders the compound **bare** `องค์พระผู้เป็นเจ้า` (the Adonai dropped) and the standalone Adonai as **`องค์เจ้านาย`** — exactly the locked corpus convention. This matters because the **preceding book, Amos, renders the identical compound differently** — `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย` ("the LORD who is the Lord/Master") — in 20 verses, and that inconsistency is the headline DECIDE blocking Amos's v1 tag.

- **HEB (MIC 1:2):** `וִיהִי אֲדֹנָי יְהוִה בָּכֶם לְעֵד אֲדֹנָי מֵהֵיכַל קָדְשׁוֹ`
- **BSB:** "May the **Lord GOD** bear witness against you, the **Lord** from His holy temple."
- **TH (Micah):** `ขอ**องค์พระผู้เป็นเจ้า**ทรงเป็นพยานปรักปรำพวกท่าน คือ**องค์เจ้านาย**จากพระวิหารบริสุทธิ์ของพระองค์`
- **TH (Amos, e.g. 3:7):** `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย…` (the marked form)
- **TH (locked corpus rule — Ezekiel 217×, Isaiah ~30×, Jeremiah, Obadiah):** `องค์พระผู้เป็นเจ้า` (bare)

Micah's per-verse `key_decisions` cites the **real** locked doc (`divine_names_table_2026-05`), not the phantom `adonai_yhwh_2026-05` that Amos's KDs cite, and the chapter-1 footnote discloses the compound collapse. Micah is thus a **clean, self-consistent data point** — more informative than Obadiah, because it shows the translator distinguishing the compound (→ bare) from a standalone Adonai (→ `องค์เจ้านาย`) **in the same verse**, exactly the distinction the bare-collapse rule preserves in apparatus.

**Why it's surfaced.** The corpus has shipped 217 Ezekiel + ~30 Isaiah + all Jeremiah + Obadiah occurrences of אֲדֹנָי יְהוִה as bare `องค์พระผู้เป็นเจ้า` per a locked decision, and Micah now follows suit. The only live tension is the open Amos question (normalize Amos down to bare, vs ratify Amos's marked surface and re-open the settled books). Micah's occurrence is correct under "normalize to bare" and would only need changing under "ratify the marked surface."

**Two questions:**
1. For an OT translation that renders אֲדֹנָי יְהוִה as bare `องค์พระผู้เป็นเจ้า` everywhere (Ezekiel/Isaiah/Jeremiah/Obadiah/**Micah**) **except Amos** (marked `องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย`), is the **bare collapse** the right corpus-wide surface — preserving the Adonai-YHWH distinction only in footnotes/`key_decisions` — or is there a defensible case for *surfacing* the doubled-lord compound in the rendered Thai (which would require re-opening the bare books)?
2. Micah distinguishes, in one verse, the compound `אֲדֹנָי יְהוִה` (→ bare `องค์พระผู้เป็นเจ้า`) from a free-standing `אֲדֹנָי` (→ `องค์เจ้านาย`). Is that the right two-surface treatment — collapse the compound but render a standalone Adonai distinctly — or should both yield the same Thai?

---

## Item C — Micah 7:18–20 doxology: the Exodus-34 attribute echo, rendered freely rather than to the formula lock (REVIEW)

**The situation.** Micah's closing doxology (`מִי־אֵל כָּמוֹךָ` "Who is a God like you?" — a pun on the prophet's own name) re-uses the attribute vocabulary of the Exodus 34:6–7 divine self-revelation formula, but in fresh syntax rather than as a verbatim recitation:

- **7:18 `נֹשֵׂא עָוֺן וְעֹבֵר עַל־פֶּשַׁע`** "bearing iniquity, passing over transgression" → `ทรงยกโทษความชั่วช้า และทรงข้ามพ้นการล่วงละเมิด` (cf. Exod 34:7 `נֹשֵׂא עָוֺן וָפֶשַׁע`)
- **7:18 `לֹא־הֶחֱזִיק לָעַד אַפּוֹ`** "does not keep his anger forever" → `ไม่ทรงถือพระพิโรธไว้เป็นนิตย์` (cf. Exod 34:6 `אֶרֶךְ אַפַּיִם` "slow to anger")
- **7:18 `כִּי־חָפֵץ חֶסֶד הוּא`** "for he delights in steadfast love" → `เพราะพระองค์ทรงพอพระทัยในความรักมั่นคง` (the chesed lock)

The corpus locks the Exodus 34:6–7 formula to one **identical** Thai surface across its ~10 verbatim/near-verbatim recitations, so a reader recognizes it at every recurrence. Micah 7:18–20 is **not** one of those recitations — it is an allusive doxology — so the Eremos text renders it per local sense, **not** conformed to the formula surface. This is the same judgment the Lamentations audit made when it held chesed 3:22 **off** the Exod-34 lock.

**Why it's surfaced.** The decision (treat 7:18–20 as an independent doxology, not a formula recitation) is principled and consistent with the Lamentations precedent, but the attribute overlap with Exod 34:6–7 is strong enough that a reader could expect formula-consistent wording, and it sits at the boundary of the formula lock's scope.

**Two questions:**
1. Where a text **alludes to** the Exodus 34:6–7 attribute formula in fresh syntax (Micah 7:18–20: "bears iniquity," "does not keep anger forever," "delights in chesed") rather than reciting it verbatim, should the Thai be rendered **freely** (preserving the doxology's own poetry) or **conformed** to the locked formula surface so the reader hears the Sinai echo?
2. Is the dividing line — verbatim/near-verbatim recitation → identical locked surface; allusive re-use of the attributes → free rendering — the right rule, and does Micah 7:18–20 fall on the correct (free) side of it?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
