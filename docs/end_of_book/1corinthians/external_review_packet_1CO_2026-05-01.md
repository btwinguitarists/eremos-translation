# 1 Corinthians — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-01**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **1 Corinthians** (16 chapters, 437 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** Mark, Matthew complete + tagged; Luke, John, Acts complete (not yet tagged). 1 Corinthians 16/16 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

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

### What we want from you

The internal end-of-book review surfaced the items below. For each, tell us either (a) "fine as-is, here's why" or (b) "here's a real concern, here's the action." Where you disagree, give specific verse-level reasoning grounded in the Greek + Thai shown.

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
## Item A — γλῶσσαι (chs 12–14): "tongues" rendered as ภาษาต่างๆ ("languages")

**The pattern:** 1 Corinthians 12–14 is THE densest spiritual-gifts + glossolalia passage in the NT. The translator rendered γλῶσσαι uniformly as **ภาษา / ภาษาต่างๆ** ("languages / various languages") — preserving the literal Greek-Hebrew *language*-sense rather than committing to "ecstatic tongues" interpretation:

| Verse | Greek | Thai |
|---|---|---|
| 12:10 | γένη **γλωσσῶν** ... ἑρμηνεία **γλωσσῶν** | การพูด**ภาษา**ต่างๆ ... การแปล**ภาษา**ต่างๆ |
| 13:1 | ταῖς **γλώσσαις** τῶν ἀνθρώπων ... καὶ τῶν ἀγγέλων | **ภาษา**ของมนุษย์ ... และของทูตสวรรค์ |
| 14:2 | ὁ γὰρ λαλῶν **γλώσσῃ** οὐκ ἀνθρώποις λαλεῖ ἀλλὰ θεῷ | ผู้ที่พูด**ภาษา**ต่างๆ ไม่ได้พูดกับมนุษย์ แต่พูดกับพระเจ้า |

The choice keeps the translation theologically-neutral on the cessationist-vs-continuationist + xenoglossy-vs-ecstatic-utterance debates — both readings are accommodated by **ภาษา**.

**Question:** Is the **ภาษา / ภาษาต่างๆ** rendering right for the Pauline-corpus (will recur at Acts 2's Pentecost rendering, already locked)? Alternative: a more-distinctive **ภาษาแปลกๆ** ("strange/unfamiliar languages") to preserve the eschatological-strangeness of the gift, OR transliteration **กลอสซาเลีย / ลิ้น** to avoid pre-committing on linguistic-vs-ecstatic. Should the corpus lock the current literal-language reading?

---

## Item B — σῶμα ψυχικόν / σῶμα πνευματικόν at 15:44 + ψυχή/πνεῦμα collapse at 15:45

**The pattern:** 15:44–46 contrasts two body-types using the Greek ψυχή / πνεῦμα adjectival pair:

- 15:44 GK: σπείρεται **σῶμα ψυχικόν**, ἐγείρεται **σῶμα πνευματικόν**
- 15:44 TH: ถูกหว่านเป็น**กายตามธรรมชาติ** ถูกทำให้เป็นขึ้นเป็น**กายฝ่ายวิญญาณ**

ψυχικόν → "ตามธรรมชาติ" (natural) and πνευματικόν → "ฝ่ายวิญญาณ" (spiritual / pertaining to spirit). The Greek's ψυχή-anthropological-substrate vs πνεῦμα-anthropological-substrate distinction is rendered as natural-vs-spiritual — closer to BSB/ESV/NIV than literal "soulish/spiritual."

**The COLLAPSE at 15:45:**
- 15:45 GK: ὁ πρῶτος ἄνθρωπος Ἀδὰμ εἰς **ψυχὴν** ζῶσαν · ὁ ἔσχατος Ἀδὰμ εἰς **πνεῦμα** ζωοποιοῦν
- 15:45 TH: อาดัมคนแรกได้กลายเป็น**วิญญาณ**ที่มีชีวิต ... อาดัมคนสุดท้ายเป็น**วิญญาณ**ที่ให้ชีวิต

**The PROBLEM:** Both ψυχή AND πνεῦμα → **วิญญาณ** at 15:45. This COLLAPSES the very ψυχή/πνεῦμα distinction that v.44 just established with ψυχικόν/πνευματικόν. The 1 Thess 5:23 tripartite anthropology rule (πνεῦμα = วิญญาณ; ψυχή = จิตใจ; σῶμα = ร่างกาย) is locally-set-aside here — and the asymmetry is jarring.

**Two questions:**
1. Is the v.45 ψυχή = วิญญาณ rendering acceptable, or should it shift to **จิตใจ** (per the 1 Thess 5:23 tripartite lock) so the ψυχή/πνεῦμα contrast is visible? E.g., "อาดัมคนแรกได้กลายเป็น**จิตใจ**ที่มีชีวิต ... อาดัมคนสุดท้ายเป็น**วิญญาณ**ที่ให้ชีวิต"?
2. Is the v.44 "natural / spiritual" pair (ตามธรรมชาติ / ฝ่ายวิญญาณ) right, or should it preserve more of the ψυχή-stem with **กายของจิตใจ / กายของวิญญาณ**?

---

## Item C — Corinthian-slogan quotation marks at 7:1, 8:4, 10:23 (interpretive extra-data)

**The pattern:** Modern scholarship widely reads several Pauline assertions in 1 Cor as Paul *quoting Corinthian-letter slogans* before refuting them. The translator made these quotations EXPLICIT in Thai using curly quotes:

- 7:1 GK: καλὸν ἀνθρώπῳ γυναικὸς μὴ ἅπτεσθαι
- 7:1 TH: "**เป็นการดีที่ผู้ชายจะไม่แตะต้องผู้หญิง**" (Corinthian-slogan; Paul will refute in vv.2-7)

- 8:4 GK: οὐδὲν εἴδωλον ἐν κόσμῳ, καὶ ... οὐδεὶς θεὸς εἰ μὴ εἷς
- 8:4 TH: "**รูปเคารพไม่ใช่อะไรเลยในโลกนี้**" และว่า "**ไม่มีพระเจ้าอื่นใดเลย นอกจากพระเจ้าองค์เดียว**" (slogans Paul affirms in v.6 but qualifies in v.7)

This INTERPRETIVE-DECISION (Paul-quoting-Corinthians) is held by ESV/NIV/BSB at 7:1 and 6:12 / 10:23 and is increasingly mainstream. It crosses from translation into light commentary.

**Question:** Is the explicit-quotation-marking right — or does it cross the line from translation into exegesis? RULES §0 says we follow modern evangelical-Protestant critical-text consensus; modern translations DO mark these (sometimes as footnotes, sometimes inline). Should the corpus formalize the rule "mark Corinthian slogans with curly quotes when modern critical consensus reads them as quotations" so future books are consistent?

---

## Item D — Last Supper at 11:24: textual variant + ἀνάμνησις

**The pattern:** 1 Cor 11:24 has a major textual variant — TR/Byz/KJV add **κλώμενον** ("broken") to "this is my body broken for you"; SBLGNT/NA28 omit. Translator follows SBLGNT:

- 11:24 GK (SBLGNT): Τοῦτό μού ἐστιν τὸ σῶμα τὸ ὑπὲρ ὑμῶν
- 11:24 TH: นี่คือ**กาย**ของเรา ซึ่ง**ให้ไว้**เพื่อพวกท่าน

**ἀνάμνησις at 11:24, 25** → "เพื่อ**ระลึกถึง**เรา" (in remembrance of me). Standard.

**The σῶμα rendering note:** Christ's body at the Lord's Supper = **กาย** (royal-noun for divine-physical-body). Same word as the sociological "body of Christ" at 12:27 — preserves the Pauline intertextual link.

**Question:** Both choices align with mainstream BSB/ESV/NIV. Is the SBLGNT-following + standard ἀνάμνησις rendering corpus-stable, or does the absence of the "broken" word need a footer-note for Thai readers familiar with KJV-tradition Eucharistic liturgy?

---

## Item E — Women in 1 Cor: 11:5 prophesying + 14:34–35 silent (apparent tension + textual variant)

**The pattern:** 1 Cor presents an APPARENT-CONTRADICTION:

- 11:5: women MAY pray and prophesy in church (rendered straight: ผู้หญิงทุกคนที่อธิษฐานหรือพยากรณ์)
- 14:34: women are to be SILENT in churches (rendered straight: ให้พวกผู้หญิงนิ่งเงียบในคริสตจักร)

**Major textual variant at 14:34-35:** Some Western MSS (D, F, G + Old Latin + Ambrosiaster) DISPLACE these verses to AFTER 14:40 — suggesting they may be a later marginal-gloss-interpolation that scribes inserted at different points. Modern scholarship is split: most evangelical critical-text editors (NA28, SBLGNT) retain in-place; some (Fee, Payne) argue for interpolation.

**Translation has NEITHER footer note NOR Tier-1/2 bracket marking** at 14:34-35 — the verses are translated as-is, in-place, with no apparent acknowledgment of either (a) the textual-variant problem or (b) the apparent tension with 11:5.

**Two questions:**
1. Should 1 Cor 14:34-35 receive a Tier-2-style chapter-footer note explaining the Western-MSS displacement? (Project's Tier-2 system is for whole-verse-omission variants; this is a whole-verse-displacement variant — different but adjacent.)
2. Should 11:5 vs 14:34-35 receive cross-reference notes (verse-level `notes` field) acknowledging the apparent tension and the major interpretive options (different settings; different roles; interpolation; cultural-decorum-only)? Or is silence preferable?

---

## Item F — εἰδωλόθυτα chs 8–10: "food sacrificed to idols" rendering

**The pattern:** Translator: **อาหารที่ถวายแก่รูปเคารพ** ("food offered to idols") for εἰδωλόθυτος / εἰδωλόθυτα. εἴδωλον → **รูปเคารพ** ("idol" — image-of-worship).

- 8:1, 4, 7, 10; 10:19, 28: consistent rendering across the chs 8-10 cluster

**The Thai-cultural resonance:** "รูปเคารพ" ("image-of-respect/worship") activates Thai-Buddhist cultural categories around Buddha-images. The translation is theologically-correct and culturally-engaged — Paul's polemic against pagan-idol-meat lands harder in a Thai context where idol-ceremony is a living-cultural-form.

**Question:** Is **อาหารที่ถวายแก่รูปเคารพ** the right corpus default for εἰδωλόθυτος? Will recur at Rev 2:14, 20 + Acts 15:29 + Acts 21:25. Cross-corpus consistency required.

---

## Item G — πορνεία / πόρνος rendering — corpus consistency check

**The pattern:** 1 Cor 5–6 has the densest πορνεία-cluster in Paul (5:1, 9, 10, 11; 6:9, 13, 15, 16, 18; 7:2). Translator's renderings:

- πόρνος → **คนล่วงประเวณี** ("person who commits adultery / fornication")
- πορνεία → **การล่วงประเวณี** ("adultery / fornication / sexual immorality")

**Cross-corpus consistency:** Mark 7:21, Matt 5:32 / 19:9, Acts 15:20, 29 / 21:25 — same family. Eremos's prior corpus uses **การล่วงประเวณี** consistently.

**Question:** Is the conflation of πορνεία (general sexual immorality, broader than μοιχεία = adultery) with **การล่วงประเวณี** (which Thai readers may parse as "adultery specifically") problematic? Greek distinguishes πορνεία (broader) from μοιχεία (married-adultery); Thai **การล่วงประเวณี** is closer to μοιχεία. Should πορνεία get a more-general rendering like **ความผิดทางเพศ** ("sexual sin/immorality") to preserve the Greek-distinction? Or is the corpus-locked choice acceptable on naturalness grounds?

---

## Item H — Marana tha at 16:22: Aramaic-embed treatment with parenthetical Thai gloss

**The pattern:** 1 Cor 16:22 closes with the famous Aramaic prayer:

- 16:22 GK: Μαράνα θά
- 16:22 TH: "**มาราน-อาธา**" (องค์พระผู้เป็นเจ้าของเราเอ๋ย ขอเสด็จมาเถิด)

The translator preserves the Aramaic transliteration AND provides the Thai gloss in parenthetical translation — the standard Eremos Aramaic-embed treatment (cf. Mark's talitha cumi, ephphatha, abba). The vocative Aramaic "Lord, come!" is rendered with the royal **เสด็จมา** divine-coming verb consistent with the παρουσία corpus-lock.

**Question:** The rendering preserves the Aramaic (per RULES §10b liturgical-formula treatment) AND provides Thai-reader access via gloss. Is the parenthetical-gloss form the right Eremos-pattern for Aramaic-formulae across the NT corpus (vs. inline-translation OR translation-only-no-Aramaic)? Will recur for marana-tha-related material in Didache + early-liturgical-tradition references downstream.

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
