# Zechariah — External AI Sanity-Check Review Packet
**Date assembled: 2026-06-27**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Zechariah** (14 chapters, 211 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from the Westminster Leningrad Codex (Hebrew Masoretic Text) with MACULA Hebrew morphology and discourse annotations. Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** Westminster Leningrad Codex (Hebrew MT) — same Hebrew base as ESV / NIV / NASB / CSB / NLT. MACULA Hebrew supplies word-level morphology, lemma data, and clause-discourse annotations.
- **Philosophy:** optimal equivalence — faithful to Hebrew grammar, natural in modern Thai. Aramaic sections (when present, e.g. Dan 2:4b–7:28, Ezr 4:8–6:18, Jer 10:11) are handled per the language-aware dispatcher.
- **Status:** 1 Chronicles, 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Chronicles, 2 Corinthians, 2 Kings, 2 Samuel, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Exodus, Galatians, Genesis, John, Joshua, Leviticus, Luke, Mark, Matthew, Numbers, Philemon, Philippians, Proverbs, Psalms, Romans complete + tagged; Revelation, Deuteronomy, Judges, 1 Samuel, 1 Kings, Job, Isaiah, Jeremiah, Ezekiel complete (not yet tagged). Zechariah 14/14 just shipped. Per-chapter automated checks (Hebrew-field integrity, divine-names enforcement, versification anchor against MT, honorifics-binding for Rachasap, back-translation, Thai-summary coverage) all pass.

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
## Item A — מַלְאַךְ יְהוָה rendered ทูตขององค์พระผู้เป็นเจ้า (drops สวรรค์): theophanic distinction vs corpus lock

**The pattern:** Zechariah's vision cycle (chs 1–6) and the 12:8 oracle render the **compound** מַלְאַךְ יְהוָה ("the angel of YHWH") differently from ordinary angels. The theophanic angel-of-YHWH drops the morpheme **สวรรค์** ("heaven"); ordinary/interpreting angels keep it:

| Hebrew | Thai | Verses | สวรรค์? |
|---|---|---|---|
| מַלְאַךְ יְהוָה (theophanic) | **ทูตขององค์พระผู้เป็นเจ้า** ("messenger of the LORD") | 1:11, 1:12, 3:1, 3:5, 3:6, 12:8 | NO |
| הַמַּלְאָךְ הַדֹּבֵר בִּי / standalone הַמַּלְאָךְ | **ทูตสวรรค์** ("heaven-messenger / angel") | 1:9, 1:13, 1:14, 2:2, 2:7, 4:1, 6:4, 6:5 | YES |

The 1:11 key-decision states the distinction is deliberate:
> מַלְאַךְ יְהוָה 'the angel of YHWH' = the rider among the myrtles … distinct from 'the angel speaking with me' (the interpreting angel) — both rendered ทูต…/ทูตสวรรค์, distinguished in the footnote.

In 3:1–2 this angel-of-YHWH is so closely identified with YHWH that "YHWH said to Satan" follows seamlessly; in 12:8 the house of David becomes "like God, like the angel of YHWH before them." The translator marks this near-divine figure as an **envoy of the LORD** (ทูตขององค์พระผู้เป็นเจ้า) rather than an ordinary **heaven-messenger** (ทูตสวรรค์).

**The conflict:** the corpus lock `malak_yhwh_2026-05.md` (decided 2026-05-13, tri-AI Exodus review; enforced through 2 Kings) mandates the **opposite** — the compound *keeps* สวรรค์:
> | מַלְאַךְ יהוה | **ทูตสวรรค์ขององค์พระผู้เป็นเจ้า** |

The lock exists specifically to stop the single Hebrew lemma מַלְאָךְ fragmenting into multiple Thai surfaces (it maps onto the single NT lemma ἄγγελος → ทูตสวรรค์). Zechariah drops the protected morpheme, systematically, in the corpus's most concentrated angel-of-YHWH passage. The deviation is invisible to all mechanical checks.

**Example — Zechariah 3:1:**
- Hebrew: `וַיַּרְאֵנִי אֶת־יְהוֹשֻׁעַ הַכֹּהֵן הַגָּדוֹל עֹמֵד לִפְנֵי **מַלְאַךְ יְהוָה**`
- Thai: `…โยชูวามหาปุโรหิตยืนอยู่ต่อหน้า**ทูตขององค์พระผู้เป็นเจ้า**` (note: standalone הַמַּלְאָךְ in 3:3 → **ทูตสวรรค์**)

**Two questions:**
1. Should the *theophanic* angel-of-YHWH (the figure identified with YHWH himself in Zech 3 / Gen 16 / Exod 3 / Judg 6 Christophany scenes) be surfaced **distinctly** (ทูตขององค์พระผู้เป็นเจ้า, no สวรรค์) from ordinary divine messengers (ทูตสวรรค์) — ratifying Zechariah's split and amending the lock — or kept **uniform** with สวรรค์ per the existing corpus lock, with the theophanic identification carried only by a footnote?
2. If the distinction is ratified, does it require a back-sweep of the already-shipped Christophany passages (Genesis/Exodus/Judges/2 Kings) where the compound was rendered *with* สวรรค์ — i.e. is intra-corpus consistency worth re-opening closed books, or should the carve-out apply prospectively only?

---

## Item B — Messianic / NT-citation reception at maximal density: policy ratification + the 12:10 me/him crux

**The pattern:** Zechariah is the densest NT-cited book in the OT. The translation handles every flagship messianic verse identically: **natural, non-committal Thai body text + a Layer-2 `nt_citation_note` footnote + a summary crediting the NT** (`พันธสัญญาใหม่อ้างถึง…`). No body text asserts `คือพระคริสต์` ("is Christ") as bare fact — the strongest reception-restraint witness in the corpus.

| Verse | Thai body (non-committal) | NT reception (footnoted) |
|---|---|---|
| 9:9 | กษัตริย์ของเจ้าเสด็จมา…เสด็จมาประทับบนหลังลา | Matt 21:5; John 12:15 |
| 11:12–13 | เงินสามสิบเหรียญ → ช่างปั้นหม้อ | Matt 27:9-10 |
| 13:7 | จงฟันผู้เลี้ยงแกะ และฝูงแกะจะกระจัดกระจายไป | Matt 26:31; Mark 14:27 |
| 3:8 / 6:12 | ผู้รับใช้ของเรา คือ "หน่อ" (a man, plain verbs) | Branch = Davidic-messianic title |

**The hardest test — Zechariah 12:10 (the me/him crux):**
- Hebrew (MT): `וְהִבִּיטוּ **אֵלַי** אֵת אֲשֶׁר־**דָּקָרוּ** וְסָפְדוּ **עָלָיו**` — "they will look on **ME** whom they pierced, and mourn for **HIM**" (the striking 1st→3rd person shift).
- Thai body: `และพวกเขาจะ**มองดูเรา** ผู้ที่พวกเขาได้**แทง** พวกเขาจะคร่ำครวญถึง**เขา**…` — faithfully preserves *me* (เรา) + *him* (เขา).
- Footnote (`nt_citation_note`): credits John 19:37 / Rev 1:7 (the crucified Christ "they will look on him whom they pierced") and notes the MT me/him crux.

The body does **not** resolve the crux toward Christ; the Christological reading is reception-framed in the footnote. The Branch (3:8/6:12) is likewise rendered as a *man* (ชายผู้หนึ่ง) with **plain** (non-royal-ทรง) verbs — committal restraint applied at the register level.

**Two questions:**
1. Is this reception-framing discipline — *natural body, NT credited in the footnote, never `คือพระคริสต์` in the body, plain verbs for the human/Branch figure* — the right standard for a CC0 evangelical-Protestant Thai Bible at the OT's most messianically-loaded surface? Or does the restraint under-serve Thai church readers who expect the explicit Christological identification their existing Thai Bibles supply?
2. For 12:10 specifically: is preserving the MT's literal **มองดูเรา** ("look on me", with YHWH as speaker) — rather than harmonizing to the NT's "look on him" — the correct base-text decision (RULES §0 MT-primary), given John 19:37 itself quotes the *him* form? Should anything beyond the current footnote flag the divergence?

---

## Item C — Satan article-role footnote at Zechariah 3:1 — doc-mandated note appears absent

**The pattern:** `satan_accuser_corpus_mapping_2026-05.md` (decided on the Job external review, after Gemini + ChatGPT convergently flagged that rendering הַשָּׂטָן as the proper name ซาตาน flattens the Hebrew definite-article role-sense) mandates for the **next** council scene — Zechariah 3:1–2:
> render הַשָּׂטָן → **ซาตาน**; add the Layer-2 **first-occurrence role footnote** (mirror Job 1:6) noting the article + role-sense `ผู้กล่าวหา / ปฏิปักษ์`.

**What shipped:**
- Rendering complies: 3:1 `וְהַשָּׂטָן עֹמֵד עַל־יְמִינוֹ` → `และ**ซาตาน**ยืนอยู่ข้างขวามือของท่านเพื่อกล่าวโทษท่าน`; the wordplay הַשָּׂטָן … לְשִׂטְנוֹ is kept (ซาตาน … เพื่อกล่าวโทษ).
- The ch3 footnotes carry a `nt_citation_note` at v2 for the **Jude-9 rebuke** (`ขอองค์พระผู้เป็นเจ้าทรงกำราบเจ้า`).
- But there is **no reader-facing footnote at 3:1 noting the definite article + role-sense** (`ผู้กล่าวหา / ปฏิปักษ์`) that the doc requires as the book's first-occurrence transparency note (the article-role explanation lives only in the non-reader-facing translator key-decision). This is the same mechanically-invisible missing-footnote class as Micah ch5 / Joel ch3 tetragrammaton-footnote gaps.

**Question:** Does the existing Jude-9 footnote at 3:2 adequately satisfy the `satan_accuser_corpus_mapping` requirement, or should a dedicated Layer-2 first-occurrence footnote be added at 3:1 noting that הַשָּׂטָן is article-marked ("**the** accuser/adversary", role-sense `ผู้กล่าวหา / ปฏิปักษ์`) before it is read as the proper name ซาตาน — mirroring the Job 1:6 footnote the doc points to?

---

## Item D — Zechariah 11:13 potter/treasury and 12:10 me/him: MT-primary textual choices

**The textual question:** two MT forks in the most NT-cited verses, both handled MT-primary with the alternative footnoted.

**11:13** — one-letter consonantal fork:
- MT: `הַשְׁלִיכֵהוּ אֶל־**הַיּוֹצֵר**` "throw it to the **potter**" (הַיּוֹצֵר) — some witnesses / Syriac suggest `הָאוֹצָר` "the **treasury**".
- Thai: `จงโยนเงินนั้นให้แก่**ช่างปั้นหม้อ**` (potter), MT-primary; treasury variant + Matt 27:9-10 reception (Judas's silver buying the potter's field) footnoted.

**12:10** — pronoun fork (see Item B):
- MT: `הִבִּיטוּ **אֵלַי**` "look on **me**" — vs the conjectural `אֵלָיו` "on **him**" reflected in John 19:37 and some witnesses.
- Thai: `มองดู**เรา**` (me), MT-primary; the *him* reading footnoted.

Per `mt_vs_lxx_textual_variant_handling_2026-05` §2.3 these are **non-gap** variants (no inclusion-bracket owed; the full verse is present, only the reading differs).

**Two questions:**
1. Is the MT-primary choice correct in both cases — **ช่างปั้นหม้อ** "potter" (11:13) and **มองดูเรา** "look on me" (12:10) — given that the NT citations (Matt 27 potter's field; John 19:37 "him") arguably reflect or harmonize toward the variant readings? RULES §0 binds the project to the Hebrew MT base; is the footnote the right place for the NT-reflected alternatives?
2. Should the 11:13 potter/treasury fork carry a `textual_variant`-type footnote in addition to the existing `nt_citation_note`, so the reader sees the consonantal variant explicitly (parallel to how 12:10 surfaces both the variant and the NT reception)?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
