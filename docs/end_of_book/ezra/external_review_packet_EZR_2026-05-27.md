# Ezra — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-27**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Ezra** (10 chapters, 280 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings complete (not yet tagged). Ezra 10/10 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — How should a foreign (Persian) monarch be honored in Thai? Ezra ships a two-tier register split, deliberately deferred to this review

**The pattern:** Thai has a royal honorific register (ราชาศัพท์) — `ทรง` before verbs, `พระองค์` / `เสด็จ` / `พระ-` noun-elevation — that the Eremos translation reserves, per `ot_register_policy_2026-05.md` §2.2 + `honorifics_non_divine_authorities_2026-04.md`, for God and for legitimate (Davidic/covenant) kings. Ezra is the corpus's **first sustained encounter with a sympathetic *Gentile* emperor** (Cyrus, Darius, Artaxerxes), and the translation **explicitly parked the register question for this end-of-book review.** The Ezra 1:2 translator note says so verbatim (translated): *"Cyrus, a foreign king, is rendered in commoner register (`กล่าว`, 'said') to match the already-shipped parallel 2 Chr 36:23; whether to elevate foreign emperors to full royal honorifics per `ot_register_policy` §2.2 is a corpus-level decision affecting Ezra–Nehemiah–Esther–Daniel, to be considered at the Ezra end-of-book review."*

**What shipped — a coherent but surface-mixed two-tier split:**

| Tier | Rule | Evidence |
|---|---|---|
| **Narrator voice** | Persian king gets **no `ทรง`-led verb** (polite nouns/pronouns OK) | **1:7** `กษัตริย์ไซรัสได้นำเครื่องใช้…ออกมา` ("King Cyrus brought out the vessels" — plain `ได้นำ…ออกมา`, no `ทรง`); **6:1** `กษัตริย์ดาริอัสจึงสั่งให้ค้น` ("King Darius ordered a search" — plain `สั่ง`); **3:7** `ให้` not `ประทาน` |
| **Inside the reported letters/decrees** | King gets **in-world deferential forms** | **4:11** `(สำเนาจดหมาย…) ขอกราบทูลกษัตริย์อารทาเซอร์ซีส จากบรรดาผู้รับใช้ของพระองค์` ("To King Artaxerxes, from your servants" — `กราบทูล` humble-address verb, `พระองค์` royal pronoun); **4:14** `เสื่อมเสียพระเกียรติ` (royal "honor"); **4:15** `พระองค์จะทรงพบและทราบ` ("you will find and know" — uses `ทรง`, noted as deferential courtly address) |

**Sample verses:**
- **1:7 HEB:** `וְהַמֶּלֶךְ כּוֹרֶשׁ הוֹצִיא אֶת־כְּלֵי בֵית־יְהוָה` → **TH:** "**กษัตริย์ไซรัสยังได้นำ**เครื่องใช้แห่งพระนิเวศขององค์พระผู้เป็นเจ้า**ออกมา**…" (narrator, no `ทรง`)
- **4:15 ARAM:** `דִּי יְבַקַּר בִּסְפַר־דָּכְרָנַיָּא דִּי אֲבָהָתָךְ וּתְהַשְׁכַּח` → **TH:** "…แล้วในบันทึกนั้น**พระองค์จะทรงพบ**และ**ทราบ**ว่า…" (inside the officials' letter, deferential `ทรง`)

**Editorial context:** the split is principled — it mirrors the project's narrator-vs-character-voice distinction (the in-letter forms are the *officials'* deference to their sovereign, not the translation's theological endorsement) and tracks 2 Chr 36's already-shipped commoner-register choice for Cyrus. But (a) it is **undocumented at corpus level** — no `docs/translator_decisions/` doc states the rule, so Nehemiah (next), then Esther and Daniel — where Persian kings are *central* characters — have only Ezra's scattered verse notes to inherit; (b) a reader scanning Ezra sees Persian kings sometimes with `ทรง`/`พระองค์` and sometimes without, which *looks* inconsistent without the rule stated; (c) it is exactly the precedent-setting editorial *whether* the end-of-book checklist exists to catch.

**Forward-compounds to:** Nehemiah (Artaxerxes throughout), Esther (Ahasuerus as the central royal figure), Daniel (Nebuchadnezzar, Belshazzar, Darius, Cyrus) — the entire Persian/Babylonian-court block of the OT.

**Two questions:** (1) Is the two-tier convention — **narrator voice withholds `ทรง` from Gentile emperors; reported in-court speech grants them deferential `พระองค์`/`ทรง` as the speakers' courtesy** — the right corpus rule, or should foreign legitimate monarchs receive *full* royal honorifics everywhere (treating sovereignty, not covenant status, as the trigger), or *none* (plain register even inside letters)? (2) Whichever rule is chosen, should it be written into a corpus doc (`foreign_monarch_register_2026-05.md` or an `ot_register_policy` §2.2 amendment) now, so Nehemiah/Esther/Daniel inherit it explicitly?

---

## Item B — Ezra 10:3: is אֲדֹנָי "my lord" (= Ezra, human) or "the Lord" (divine)? The MT points it as the divine form

**The pattern:** The Eremos translation reserves the Thai divine honorific `องค์เจ้านาย` for the divine title אֲדֹנָי ("the Lord"), and renders the *human* "my lord/master" with ordinary words (`นาย`, `เจ้านาย` without `องค์`). The disambiguation is normally driven by the Hebrew vocalization: divine **אֲדֹנָי** (qamats under the nun) vs human **אֲדֹנִי** (hiriq, "my lord").

**The verse:** Shecaniah's proposal to Ezra to send away the foreign wives —
- **10:3 HEB (MT):** `וְעַתָּה נִכְרָת־בְּרִית לֵאלֹהֵינוּ לְהוֹצִיא כָל־נָשִׁים … בַּעֲצַת אֲדֹנָי וְהַחֲרֵדִים בְּמִצְוַת אֱלֹהֵינוּ` — "…let us make a covenant with our God to put away all these wives … according to the counsel of **אֲדֹנָי** and of those who tremble at the commandment of our God."
- **10:3 TH (shipped):** read as **human** "my lord" (= Ezra); `องค์เจ้านาย` (the divine form) is **not** used.
- **`key_decision` (shipped, translated):** *"Here אֲדֹנָי means 'my lord/master' = Ezra (human), not God, per BSB/ESV/NIV (cf. v4 'Arise, this matter is your responsibility'); so `องค์เจ้านาย`, reserved for God, is not used — note: the divine-names checker may raise a C-soft warning, a false positive here."*

**The tension:** The reading is well-supported — **BSB, ESV, NIV** all render "my lord," and the immediate context (v4: "Arise, for this matter is your responsibility, and we are with you") addresses Ezra directly. **But the MT vocalizes אֲדֹנָי — the form normally reserved for the divine title** — rather than the expected human אֲדֹנִי. The Masoretic pointing is therefore (weak but real) evidence for a divine reading ("the counsel of *the Lord*"), and it is exactly why the project's automated divine-names checker flags 10:3 with a C-soft warning.

**Editorial context:** the translation documents its choice and pre-empts the checker warning as a false positive, which is the right discipline. This item is *not* a defect or a tag blocker — it is a request for a Hebrew-competent confirmation that the human reading is correct despite the divine pointing.

**Question:** At Ezra 10:3, is אֲדֹנָי better read as the **human** "my lord" (= Ezra/the leader, with BSB/ESV/NIV) — in which case the shipped rendering and the "false positive" classification are correct — or does the **MT's divine vocalization** argue for "the counsel of *the Lord*" (taking `องค์เจ้านาย` / a divine rendering)? Is there a consensus, or is this a genuine crux the translation should footnote either way?

---

## Item C — Ezra and 1 Esdras: does the divergent Greek recension need any disclosure under the MT-anchored policy?

**The pattern:** The Eremos OT is **MT-anchored** (`ot_canon_and_text_base_2026-05.md`). For verse-level MT-vs-LXX divergence, `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3 sets a *disclosure floor*: a book with no macro-structural / canonically-visible / materially-reader-affecting divergence is COMPLIANT with zero `textual_variant` entries. Ezra's `textual_variants` files are all YHWH-footnote-only, and `audit_inclusion_variants.py --book ezra --strict` returns 0 candidates — correct for *verse-level* variants.

**The Ezra-specific feature:** Ezra's distinctive textual situation is not verse-level variants but the existence of **two Greek forms**:
- **Esdras B** (LXX Ezra–Nehemiah) — a fairly literal Greek translation, close to MT.
- **1 Esdras / Esdras A** — a **divergent recension**: it reorders the Ezra material (it runs 2 Chr 35–36 → Ezra → parts of Nehemiah), omits/relocates blocks, and **adds the famous "contest of the three guardsmen / the strength of truth and women and wine"** (1 Esd 3:1–5:6), a passage with **no Hebrew/Aramaic counterpart** in MT Ezra. 1 Esdras is canonically present in the Orthodox tradition (and appended in the Vulgate as 3 Esdras).

**Editorial context:** because 1 Esdras is a *separate recension* rather than a set of variants *to* MT Ezra, the most defensible position is that it needs no per-verse disclosure — the project translates MT Ezra, and 1 Esdras is simply a different book-form. But §2.3 specifically asks that *macro-structural / canonically-visible* divergences be **disposed of explicitly** rather than silently, and 1 Esdras is exactly that kind of high-visibility parallel (a reader who encounters "1 Esdras" in an Orthodox Bible or a study reference will ask why it differs). The audit's recommendation is a one-line disposition in the MT/LXX doc, not any surface change.

**Question:** Under the project's MT-anchored policy, does the existence of the **1 Esdras (Esdras A) recension** — with its reordering and its non-MT "three guardsmen" episode — warrant any disclosure for Ezra (e.g., a single book-level note recording "MT Ezra is the base; 1 Esdras is a separate Greek recension, not a textual variant of MT, so no per-verse disclosure is owed"), or is silence fully appropriate because 1 Esdras is a distinct composition rather than a witness to the MT text the project translates?

---

## Item D — "God of heaven" (אֱלֹהֵי הַשָּׁמַיִם / Aramaic אֱלָהּ שְׁמַיָּא) → `พระเจ้าแห่งฟ้าสวรรค์`: right rendering for the Persian-period title?

**The pattern:** In the Persian period, Israel's God is repeatedly named — by Gentile kings and by Jews addressing Gentile authorities — as **"the God of heaven"** (Hebrew אֱלֹהֵי הַשָּׁמַיִם; Aramaic אֱלָהּ שְׁמַיָּא). It is the era's signature divine self-presentation in the imperial-diplomatic register. Ezra renders it **uniformly `พระเจ้าแห่งฟ้าสวรรค์`** ("God of the sky/heaven") across **both** languages:

| Ref | Lang | Source | Thai |
|---|---|---|---|
| 1:2 | Heb | אֱלֹהֵי הַשָּׁמַיִם (Cyrus' proclamation) | `พระเจ้าแห่งฟ้าสวรรค์` |
| 5:11–12 | Aram | אֱלָהּ שְׁמַיָּא (elders to Tattenai) | `พระเจ้าแห่งฟ้าสวรรค์` |
| 6:9–10 | Aram | אֱלָהּ שְׁמַיָּא (Darius' decree) | `พระเจ้าแห่งฟ้าสวรรค์` |
| 7:12, 21, 23 | Aram | אֱלָהּ שְׁמַיָּא (Artaxerxes' rescript) | `พระเจ้าแห่งฟ้าสวรรค์` |

**Sample:** **1:2 TH:** "องค์พระผู้เป็นเจ้า**พระเจ้าแห่งฟ้าสวรรค์**ได้ประทานราชอาณาจักรทั้งสิ้นในแผ่นดินโลกแก่เรา…"

**Editorial context:** `ฟ้าสวรรค์` is the standard Thai compound for "heaven/sky" (it also appears in `ทูตสวรรค์` "angel" and the heaven-rendering doc `ouranos_heaven_rendering_2026-04.md`). The rendering is uniform and natural, but it is **undocumented at corpus level** and recurs ~7× in Nehemiah and dominates Daniel (2:18–19, 2:37, 2:44; 5:23) — the audit recommends locking it in a `god_of_heaven_persian_title_2026-05.md` doc before it compounds.

**Question:** Is **`พระเจ้าแห่งฟ้าสวรรค์`** the best Thai rendering of the Persian-period title "the God of heaven" (אֱלֹהֵי הַשָּׁמַיִם / אֱלָהּ שְׁמַיָּא) — capturing the intended sense (the transcendent God who rules from / over heaven, presented to a polytheistic imperial audience) — or would an alternative (e.g. `พระเจ้าแห่งสวรรค์`, or a form making the "Most High / sovereign over all" nuance explicit) read more naturally and accurately for a Thai audience? Should it be locked as the corpus form for all of Ezra–Nehemiah–Daniel?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
