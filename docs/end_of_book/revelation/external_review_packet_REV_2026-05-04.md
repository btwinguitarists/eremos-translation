# Revelation — External AI Sanity-Check Review Packet
**Date assembled: 2026-05-04**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Revelation** (22 chapters, 405 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** 1 Corinthians, 1 Thessalonians, 1 Timothy, 2 Corinthians, 2 Thessalonians, 2 Timothy, Acts, Colossians, Ephesians, Galatians, John, Luke, Mark, Matthew, Philemon, Philippians, Romans complete + tagged. Revelation 22/22 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

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
## Item A — REV 2:9 + 3:9 Ἰουδαῖος "synagogue of Satan" — highest-stakes Ἰουδαῖος verses in the NT

**Context:** Per the John end-of-book audit, Eremos's Johannine Ἰουδαῖος is split four ways by context: **ผู้นำชาวยิว** (leader-marked), **ชาวยิว** (ethnic-neutral), **ยิว** (compressed Passion-narrative form, chs 18–19), and a deprecated drift variant **พวกผู้นำยิว**. REV 2:9 and 3:9 are the only two occurrences of Ἰουδαῖος in Revelation, both in seven-churches polemical contexts ("synagogue of Satan / those who say they are Jews and are not"). They use the **"ยิว"** form — the compressed Passion-narrative register.

**The two verses:**

- REV 2:9 GK: `Οἶδά σου τὴν θλῖψιν καὶ τὴν πτωχείαν, ... καὶ τὴν βλασφημίαν ἐκ τῶν λεγόντων Ἰουδαίους εἶναι ἑαυτούς, καὶ οὐκ εἰσίν, ἀλλὰ συναγωγὴ τοῦ Σατανᾶ`
  TH: `เรารู้ถึงการทนทุกข์และความยากจนของเจ้า ... และเรารู้ถึงคำหมิ่นประมาทของ**พวกที่อ้างตัวเป็นยิว ซึ่งไม่ใช่ แต่เป็นธรรมศาลาของซาตาน**`

- REV 3:9 GK: `ἰδοὺ διδῶ ἐκ τῆς συναγωγῆς τοῦ Σατανᾶ, τῶν λεγόντων ἑαυτοὺς Ἰουδαίους εἶναι, καὶ οὐκ εἰσὶν ἀλλὰ ψεύδονται`
  TH: `ดูเถิด เราจะกระทำให้**บางคนจากธรรมศาลาของซาตาน ผู้ที่อ้างตัวเป็นยิวซึ่งไม่ใช่ แต่โกหก**`

**Editorial significance:** These are the two verses where modern English translations (NIV-2011, NRSVue) most often add footnotes clarifying that the rhetoric refers to a specific historical Jewish-Christian conflict in Smyrna and Sardis, not Judaism as a whole. The choice of **"ยิว"** (compressed / sharp register, matching the JHN-audit Passion-narrative form) preserves the rhetorical sharpness of the Greek polemic but is also the form most likely to read as anti-Jewish to a modern Thai reader without historical-context awareness.

**The principle would compound** into the still-unwritten `docs/translator_decisions/ioudaioi_johannine_2026-04.md` corpus doc (recommended in the JHN audit). Revelation 2:9 + 3:9 are the **highest-stakes test cases** for whichever rendering principle the corpus locks.

**Three options under consideration:**
(a) Keep **"ยิว"** — accepts the rhetorical sharpness; cite the JHN-audit four-way split as the principle.
(b) Normalize to **"ชาวยิว"** — neutralizes the rhetoric; matches NIV-2011 / NRSVue footnoting practice.
(c) Keep **"ยิว"** + add a verse-level translator's-note framing the historical-rhetorical context.

**Two questions:**
1. Is the **"ยิว"** form (compressed-pejorative register, applied here for the Smyrna / Sardis polemic) defensible as faithful-to-Greek-rhetoric, or does it impose a sharpness that exceeds the Greek?
2. For a Thai-evangelical translation aimed at a predominantly Buddhist-cultural readership without baseline historical-context awareness, is option (c) — keep the form + add a translator's-note — the right reader-management strategy? Or should the verse-level KD's existing scholarly explanation (Smyrna's Jewish-majority-city conflict, Diaspora-Judaism background) be considered sufficient?

---

## Item B — Divine self-titles cluster (the most theologically load-bearing pattern in Revelation)

**Context:** Revelation deploys **five interlocking divine self-titles** that establish the divine-eternity / divine-ultimacy axis. All five are uniformly rendered across the book and applied to **both Father and Son** at climactic moments — the strongest Christological claims in the NT.

| # | Greek formula | Thai | Verses |
|---|---|---|---|
| 1 | ὁ ὢν καὶ ὁ ἦν καὶ ὁ ἐρχόμενος (3-fold) | **ผู้ทรงดำรงอยู่ ผู้ทรงเคยดำรงอยู่ และผู้ที่จะเสด็จมา** | 1:4, 1:8, 4:8 |
| 2 | ὁ ὢν καὶ ὁ ἦν (2-fold; drops "coming" because the eschaton has arrived) | **ผู้ทรงดำรงอยู่และผู้ทรงเคยดำรงอยู่** | 11:17, 16:5 |
| 3 | Ἄλφα καὶ τὸ Ὦ | **อัลฟาและโอเมกา** (transliteration) | 1:8, 21:6, 22:13 |
| 4 | ὁ πρῶτος καὶ ὁ ἔσχατος | **เบื้องต้นและเบื้องปลาย** | 1:17, 2:8, 22:13 |
| 5 | ἡ ἀρχὴ καὶ τὸ τέλος | **ปฐมและอวสาน** | 21:6, 22:13 |
| 6 | παντοκράτωρ | **ผู้ทรงฤทธานุภาพยิ่งใหญ่** | 1:8, 4:8, 11:17, 15:3, 16:7, 16:14, 19:6, 19:15, 21:22 |

**Three theological observations:**

1. **The two-fold form at 11:17 + 16:5 deliberately drops "coming"** — both passages are post-final-trumpet / post-bowls, where the future-coming has already broken in. The Thai preserves the shift explicitly.

2. **REV 22:13 is the climactic triple-self-declaration of Christ** combining all three pairs:
   - GK: `ἐγὼ τὸ Ἄλφα καὶ τὸ Ὦ, ὁ πρῶτος καὶ ὁ ἔσχατος, ἡ ἀρχὴ καὶ τὸ τέλος`
   - TH: `เราคือ**อัลฟาและโอเมกา** เป็น**เบื้องต้นและเบื้องปลาย** เป็น**ปฐมและอวสาน**`
   - The translator uses **two distinct Thai synonym-pairs** (เบื้องต้น/เบื้องปลาย vs ปฐม/อวสาน) to prevent monotonous repetition while preserving the theological precision that πρῶτος-ἔσχατος and ἀρχή-τέλος are different ways of saying the same divine-ultimacy claim.

3. **Christ assumes the Father's titles** at 1:17 (πρῶτος-ἔσχατος, originally a YHWH title from ISA 41:4 LXX), 2:8 (ditto), and 22:13 (the triple). The Thai uses the same forms whether the speaker is Father or Son — preserving the theological equation.

**Question:** Is the synonym-pair distinction at REV 22:13 (เบื้องต้น/เบื้องปลาย for πρῶτος/ἔσχατος vs ปฐม/อวสาน for ἀρχή/τέλος) the right Thai strategy — preserving lexical-precision for the two parallel divine-ultimacy claims while preventing repetitive monotony? Or would a single Thai pair be more natural / preserve the deliberate Greek redundancy of the climactic triple-declaration? Should this pattern be locked into a corpus doc (`docs/translator_decisions/revelation_divine_self_titles_2026-05.md`) before any future eschatological material?

---

## Item C — τὸ ἀρνίον (the Lamb) → พระเมษโปดก — Christological centerpiece

**Context:** ἀρνίον is *the* Christological signature of Revelation. It occurs at 24 verses (29 lemma instances) — the slain-yet-standing paradox at 5:6, the seven-eyes / seven-horns Lamb at 5:6, the wedding-feast at 19:7–9, the throne-co-occupant at 22:1, 3, the temple-replacement at 21:22, the lamp of the New Jerusalem at 21:23.

**All 24 occurrences uniformly rendered พระเมษโปดก** (royal-prefix **พระ** + the Thai-Christian-standard "lamb" compound). Zero drift.

**Representative verses:**

- REV 5:6 GK: `καὶ εἶδον ἐν μέσῳ τοῦ θρόνου ... ἀρνίον ἑστηκὸς ὡς ἐσφαγμένον`
  TH: `และข้าพเจ้าเห็นในท่ามกลางพระบัลลังก์ ... **พระเมษโปดก**ตนหนึ่งยืนอยู่ ดุจถูกฆ่าแล้ว`

- REV 5:12 GK: `Ἄξιόν ἐστιν τὸ ἀρνίον τὸ ἐσφαγμένον λαβεῖν τὴν δύναμιν ...`
  TH: `**พระเมษโปดก**ผู้ทรงถูกฆ่านั้น สมควรได้รับฤทธานุภาพ ...`

- REV 19:7 GK: `ἦλθεν ὁ γάμος τοῦ ἀρνίου, καὶ ἡ γυνὴ αὐτοῦ ἡτοίμασεν ἑαυτήν`
  TH: `งานวิวาห์ของ**พระเมษโปดก**ได้มาถึงแล้ว และเจ้าสาวของพระองค์ก็ได้เตรียมตัวพร้อมแล้ว`

- REV 21:22 GK: `Καὶ ναὸν οὐκ εἶδον ἐν αὐτῇ, ὁ γὰρ κύριος, ὁ θεός, ὁ παντοκράτωρ, ναὸς αὐτῆς ἐστιν, καὶ τὸ ἀρνίον`
  TH: `และข้าพเจ้าไม่ได้เห็นวิหารในนคร เพราะองค์พระผู้เป็นเจ้าพระเจ้า ผู้ทรงฤทธานุภาพยิ่งใหญ่ และ**พระเมษโปดก** ทรงเป็นวิหารของนคร`

**Cross-corpus consideration:** the Eremos translation distinguishes two Lamb-of-God titles:
- **ἀρνίον** (apocalyptic-Christological, REV) → **พระเมษโปดก** (royal-prefix "lamb-of-God")
- **ἀμνός** (Paschal-Lamb metaphor, JHN 1:29 + JHN 1:36 + 1 Pet 1:19) → **ลูกแกะ** (plain "young-sheep")

Both are the established Thai-Christian standard.

**Question:** Is **พระเมษโปดก** the correct rendering for ἀρνίον across all 24 Revelation occurrences — preserving the royal-prefixed Christological apocalyptic-Lamb signature distinct from the Paschal-Lamb metaphor (ἀμνός → ลูกแกะ)? Or does the consistent rendering risk the reader missing variation in Greek register (e.g., 5:6 climactic-introduction vs 21:22 incidental-temple-replacement)?

---

## Item D — θηρίον (apocalyptic Beast) vs ζῷον (heavenly Living-Creature) — semantic-distinction preservation

**Context:** Revelation uses two animal-vocabulary lemmas for very different purposes:
- **ζῷον** (the four heavenly Living-Creatures around God's throne, 4:6ff): rendered **สิ่งมีชีวิต** ("living-being") — neutral, attendant-of-God register.
- **θηρίον** (the two apocalyptic Beasts of REV 13: sea-beast + earth-beast / false-prophet): rendered **สัตว์ร้าย** ("evil-animal" / monster register) at 30 verses uniformly.

The translator preserves the **moral / ontological gulf** between the heavenly ζῷα (faithful attendants of God) and the earthly θηρία (Satan's instruments). Flat-rendering both as **สัตว์** would have collapsed the distinction; the translator avoids this.

**Verses with θηρίον → สัตว์ร้าย (selection):**
- REV 13:1 GK: `Καὶ εἶδον ἐκ τῆς θαλάσσης θηρίον ἀναβαῖνον` → TH: `และข้าพเจ้าได้เห็น**สัตว์ร้าย**ตัวหนึ่งขึ้นมาจากทะเล`
- REV 13:11 GK: `Καὶ εἶδον ἄλλο θηρίον ἀναβαῖνον ἐκ τῆς γῆς` → TH: `และข้าพเจ้าได้เห็น**สัตว์ร้าย**อีกตัวหนึ่งขึ้นมาจากแผ่นดิน`
- REV 19:20 GK: `καὶ ἐπιάσθη τὸ θηρίον` → TH: `**สัตว์ร้าย**ก็ถูกจับ`

**Verses with ζῷον → สิ่งมีชีวิต (selection):**
- REV 4:6 GK: `τέσσαρα ζῷα γέμοντα ὀφθαλμῶν` → TH: `**สิ่งมีชีวิต**สี่ตน เต็มไปด้วยดวงตา`
- REV 5:14 GK: `καὶ τὰ τέσσαρα ζῷα ἔλεγον· Ἀμήν` → TH: `และ**สิ่งมีชีวิต**ทั้งสี่ตนกล่าวว่า "อาเมน"`

**Distinct from generic θηρίον at REV 6:8** (the "wild-animals-of-the-earth" alongside sword/famine/pestilence — natural fauna, not the apocalyptic beast). At 6:8 the Thai correctly does NOT use สัตว์ร้าย — preserving the distinction.

**Question:** Is the **สัตว์ร้าย** rendering for the apocalyptic θηρίον — distinct from **สิ่งมีชีวิต** for heavenly ζῷον and from generic-fauna **สัตว์ป่า** at 6:8 — the right Thai strategy to preserve the moral / ontological hierarchy of Revelation's animal vocabulary? Should this be locked into `docs/translator_decisions/therion_beast_apocalyptic_2026-05.md`?

---

## Item E — δράκων (the Dragon) and the Genesis-3 / Revelation-12 identification chain

**Context:** δράκων occurs 13 times across 12 verses, all rendered **มังกร** (Thai-standard apocalyptic dragon vocabulary). The translator preserves the four-fold identification chain at REV 12:9 (with verbatim repetition at REV 20:2):

- REV 12:9 GK: `καὶ ἐβλήθη ὁ δράκων ὁ μέγας, ὁ ὄφις ὁ ἀρχαῖος, ὁ καλούμενος Διάβολος καὶ ὁ Σατανᾶς, ὁ πλανῶν τὴν οἰκουμένην ὅλην`
  TH: `และ**มังกร**ใหญ่ก็ถูกเหวี่ยงลงมา คือ **งูดึกดำบรรพ์** ผู้ที่ถูกเรียกว่า**มาร**และ**ซาตาน** ผู้ล่อลวงทั่วทั้งโลก`

- REV 20:2 GK: `καὶ ἐκράτησεν τὸν δράκοντα, ὁ ὄφις ὁ ἀρχαῖος, ὅς ἐστιν Διάβολος καὶ ὁ Σατανᾶς`
  TH: `ทูตสวรรค์ได้จับ**มังกร** คือ **งูดึกดำบรรพ์** ผู้ที่เป็น**มาร**และ**ซาตาน**`

The chain locks in: **มังกร = งูดึกดำบรรพ์ (Eden-serpent, GEN 3:1, 14 echo) = มาร (Devil, Διάβολος) = ซาตาน (Satan)** — preserving the canonical bookend (Genesis-fall ↔ Revelation-binding).

**Question:** Is **มังกร** the right Thai rendering for the apocalyptic δράκων — preserving the Eden-serpent / Devil / Satan identification chain explicitly at 12:9 + 20:2? Or are there cultural connotations of **มังกร** in modern Thai (where dragons are often associated with Chinese symbolism — power, prosperity, royalty — rather than evil-monster register) that risk distorting the apocalyptic semantics?

---

## Item F — "I come quickly" formula — register-split between letters (โดยเร็ว) and epilogue (ในไม่ช้า)

**Context:** Revelation's "I am coming (quickly)" eschatological-imminence refrain occurs six times. The Thai uses **two distinct adverbials** by context:

| GK | TH | Verse | Context |
|---|---|---|---|
| ἔρχομαί σοι (no ταχύ) | **เราจะมาหาเจ้า** | 2:5 | Letter to Ephesus, warning |
| ἔρχομαί σοι ταχύ | **เราจะมาหาเจ้าโดยเร็ว** | 2:16 | Letter to Pergamum, warning |
| ἔρχομαι ταχύ | **เรากำลังมาโดยเร็ว** | 3:11 | Letter to Philadelphia, encouragement |
| ἔρχομαι ταχύ | **เราจะมาในไม่ช้า** | 22:7 | Christ's epilogue self-promise |
| ἔρχομαι ταχύ | **เราจะมาในไม่ช้า** | 22:12 | Christ's epilogue self-promise |
| ἔρχομαι ταχύ | **เราจะมาในไม่ช้า** | 22:20 | Christ's final word |

**Two readings:**
(a) **Principled register-split** — chs 2–3 letters use **โดยเร็ว** (terse, urgent-warning tone matching the chastisement-or-reward structure of the seven letters); ch 22 epilogue uses **ในไม่ช้า** (more solemn, eschatological-anticipation register matching the climactic-prophecy frame).
(b) **Drift** — the same Greek formula ἔρχομαι ταχύ should arguably get one Thai rendering for cross-Revelation uniformity. Most natural normalization: **ในไม่ช้า** in all six occurrences.

**Question:** Is the register-split (โดยเร็ว for letters / ในไม่ช้า for epilogue) defensible as principled, or is it drift that should be normalized? If kept, should the principle be documented in a corpus doc (the divine-self-titles doc, or a 22:7 KD as the locking precedent)? If normalized, what's the better single rendering — **โดยเร็ว** or **ในไม่ช้า**?

---

## Item G — REV 19:13 ὁ Λόγος τοῦ Θεοῦ → พระวาทะ — forward-inheritance from the (still-unwritten) Johannine Logos doc

**Context:** REV 19:13 uniquely names Christ at the second-coming as **ὁ Λόγος τοῦ Θεοῦ** ("the Word of God"). The Thai rendering uses **พระวาทะ** — the royal-prefixed Christological-Logos title that the Eremos John end-of-book audit (§2, 2026-04-30) recommended formalizing into `docs/translator_decisions/logos_johannine_2026-04.md`.

The JHN-audit principle: **พระวาทะ** is reserved exclusively for the Christological Logos (JHN 1:1 ×3, 1:14). REV 19:13 is the only post-John NT instance, and it **applies the JHN-locked principle**:

- REV 19:13 GK: `καὶ περιβεβλημένος ἱμάτιον βεβαμμένον αἵματι, καὶ κέκληται τὸ ὄνομα αὐτοῦ ὁ Λόγος τοῦ Θεοῦ`
  TH: `และพระองค์ทรงสวมเสื้อคลุมที่ชุ่มไปด้วยเลือด และพระองค์ทรงพระนามว่า "**พระวาทะของพระเจ้า**"`

The verse-level KD at REV 19:13 names the inheritance: "Christological-title 'ὁ Λόγος τοῦ Θεοῦ' → พระวาทะของพระเจ้า (royal-prefix divine-Word). Unique-NT-title — applies the JHN 1:1 lock."

**The doc gap:** the JHN audit's recommended `logos_johannine_2026-04.md` has NOT yet been written (as of REV's end-of-book moment, 2026-05-04). REV 19:13 is operating on an unwritten lock. This is documentary, not editorial — the rendering itself is correct.

**Question:** Is **พระวาทะ** (royal-prefixed Christological-Logos) the right Thai for REV 19:13's ὁ Λόγος τοῦ Θεοῦ — preserving the Johannine 1:1 Logos-doctrine equation across the canon? Or is REV 19:13's apocalyptic-warrior-Christ frame (blood-stained robe, ISA 63 echo) different enough from the Prologue's eternal-Logos frame to warrant a different Thai rendering (e.g., **พระวจนะ** which Eremos uses for "the word of God" written-revelation per JHN 10:35, 17:6/14/17)?

---

## Item H — The seven beatitudes — μακάριος formula split between front-form and back-form

**Context:** Revelation contains seven explicit beatitudes (1:3, 14:13, 16:15, 19:9, 20:6, 22:7, 22:14). Thai uses two principled forms of the μακάριος-blessing formula:

| Form | Position | Verses | Representative |
|---|---|---|---|
| **ความสุขมีแก่...** ("blessing-be-upon-X") — predicate-front | When the speaker pronounces a heavenly proclamation | 1:3, 14:13 | 1:3: `**ความสุขมีแก่**ผู้ที่อ่านออกเสียง` |
| **...ก็เป็นสุข** ("X-is-blessed") — predicate-back | When the beatitude qualifies the subject in narrative-flow | 16:15, 19:9, 20:6, 22:7, 22:14 | 22:7: `ผู้ที่รักษาถ้อยคำแห่งคำเผยพระวจนะของหนังสือเล่มนี้**ก็เป็นสุข**` |

Both are valid Thai for μακάριος. The split tracks the Synoptic Beatitudes precedent (MAT 5:3ff uses **ความสุขมีแก่** front-form for the formal Sermon-on-the-Mount blessings) and adapts naturally to REV's mixed usage.

**Question:** Is the syntactic-position split (front-form for heavenly proclamation / back-form for narrative-flow qualification) defensible as natural Thai rhetoric, or should the seven beatitudes share a uniform form for cross-Revelation cohesion?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
