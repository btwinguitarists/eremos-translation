# John — External AI Sanity-Check Review Packet
**Date assembled: 2026-04-30**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **John** (21 chapters, 878 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** Mark, Matthew complete + tagged; Luke, Acts complete (not yet tagged). John 21/21 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

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
## Item A — οἱ Ἰουδαῖοι four-way contextual split (the most contested editorial decision in modern Bible translation)

**The pattern:** John uses οἱ Ἰουδαῖοι 64× across narrator + dialogue. The Thai uses a four-way principled split (no other NT book required this scale of disambiguation):

| Sense | Thai | Count |
|---|---|---|
| Religious-political leadership in adversarial action (Johannine signature) | **ผู้นำชาวยิว** ("Jewish leaders") | 25 |
| Ethnic / festival / customs / believing / neutral | **ชาวยิว** ("Jews / Judeans") | 27 |
| Passion-narrative compressed form (chs 18–19) | **ยิว** ("Jews," short form) | 11 |
| **DRIFT VARIANT** — leader-marked, alternate phrase | **พวกผู้นำยิว** | 4 |

**Cleanest exegetical proof of the split — JHN 4:9 (ethnic) vs JHN 7:1 (adversary action):**
- JHN 4:9 GK: `οὐ γὰρ συγχρῶνται Ἰουδαῖοι Σαμαρίταις` → TH: `(เพราะ**ชาวยิว**ไม่คบหากับชาวสะมาเรีย)` (ethnic)
- JHN 7:1 GK: `οὐ γὰρ ἤθελεν ἐν τῇ Ἰουδαίᾳ περιπατεῖν,ὅτι ἐζήτουν αὐτὸν οἱ Ἰουδαῖοι ἀποκτεῖναι` → TH: `เพราะ**ผู้นำชาวยิว**กำลังหาทางจะฆ่าพระองค์` (leadership)

**Believing / neutral context — ชาวยิว:**
- JHN 8:31 GK: `Ἔλεγεν οὖν ὁ Ἰησοῦς πρὸς τοὺς πεπιστευκότας αὐτῷ Ἰουδαίους` → TH: `พระเยซูจึงตรัสกับ**ชาวยิว**ที่เชื่อในพระองค์`
- JHN 11:36 (mourners, sympathetic) GK: `ἔλεγον οὖν οἱ Ἰουδαῖοι·Ἴδε πῶς ἐφίλει αὐτόν` → TH: `**ชาวยิว**จึงกล่าวว่า "ดูสิ พระองค์ทรงรักเขามากเพียงใด"`

**Compressed Passion-narrative ยิว:**
- JHN 18:31 GK: `εἶπον οὖν αὐτῷ οἱ Ἰουδαῖοι·Ἡμῖν οὐκ ἔξεστιν ἀποκτεῖναι οὐδένα` → TH: `พวก**ยิว**กล่าวกับเขาว่า "พวกเราไม่มีอำนาจประหารชีวิตผู้ใด"`
- JHN 19:7 GK: `ἀπεκρίθησαν αὐτῷ οἱ Ἰουδαῖοι·Ἡμεῖς νόμον ἔχομεν` → TH: `พวก**ยิว**ตอบเขาว่า "เรามีธรรมบัญญัติ"`

**DRIFT — พวกผู้นำยิว at 5:10–18 (only block in the Gospel):**
- JHN 5:10 GK: `ἔλεγον οὖν οἱ Ἰουδαῖοι τῷ τεθεραπευμένῳ` → TH: `**พวกผู้นำยิว**กล่าวกับชายที่ได้รับการรักษาว่า`
- JHN 5:15, 5:16, 5:18: same variant in the same Bethesda-aftermath block

**Two questions:**
1. Is the four-way split (ผู้นำชาวยิว / ชาวยิว / ยิว / [drift: พวกผู้นำยิว]) defensible as anti-supersessionist editorial care that respects Johannine context-disambiguation? Or does it impose a reading not in the Greek?
2. Should the พวกผู้นำยิว variant at 5:10/15/16/18 be normalized to ผู้นำชาวยิว (1-block drift), and should the Passion-narrative ยิว vs ชาวยิว oscillation (18:31 vs 18:33; 19:7 vs 19:19/20/21) be normalized or documented as principled? Critically: this needs a `docs/translator_decisions/` doc before Romans 9–11, Galatians, Thessalonians, Revelation 2:9 + 3:9.

---

## Item B — λόγος seven-way contextual rendering (Logos doctrine + Farewell-Discourse drift question)

**The pattern:** 35 verses; seven distinct Thai renderings principled by referent class:

| Sense | Thai | Count | Verses |
|---|---|---|---|
| Christological Logos (Prologue doctrine) | **พระวาทะ** | 2 | 1:1, 1:14 |
| Father's word / scripture (royal, written-revelation) | **พระวจนะ** | 4 | 10:35, 17:6, 17:14, 17:17 |
| Jesus's spoken word in narrator-emphasis (royal, divine-utterance) | **พระดำรัส** | 4 | 2:22, 4:41, 4:50, 5:38 |
| Jesus's word / saying (plain, dominant) | **คำ** | ~20 | 4:37; 5:24; 6:60; 7:36; 8:31, 37, 43, 51, 52, 55; 12:38, 48; 14:23–24; 15:3, 20, 25; 17:20; 18:9, 32; 19:8 |
| Testimony | **คำพยาน** | 1 | 4:39 |
| Teaching | **คำสอน** | 1 | 6:60 (alongside คำ rendering) |
| Rumor (narrator-distancing) | **คำเล่าลือ** | 1 | 21:23 |

**Christological Logos — JHN 1:1, 1:14:**
- JHN 1:1 GK: `Ἐν ἀρχῇ ἦν ὁ λόγος,καὶ ὁ λόγος ἦν πρὸς τὸν θεόν,καὶ θεὸς ἦν ὁ λόγος` → TH: `ในเริ่มแรกนั้น **พระวาทะ**ทรงดำรงอยู่ และ**พระวาทะ**ทรงอยู่กับพระเจ้า และ**พระวาทะ**ทรงเป็นพระเจ้า`
- JHN 1:14 GK: `Καὶ ὁ λόγος σὰρξ ἐγένετο` → TH: `**พระวาทะ**นั้นได้ทรงรับสภาพเป็นมนุษย์`

**Father's word / scripture — พระวจนะ:**
- JHN 10:35 GK: `οὐ δύναται λυθῆναι ἡ γραφή` → TH: `และ**พระวจนะ**(ของพระเจ้า)จะลบล้างไม่ได้`
- JHN 17:17 GK: `ὁ λόγος ὁ σὸς ἀλήθειά ἐστιν` → TH: `**พระวจนะ**ของพระองค์เป็นความจริง`

**Jesus's spoken word, narrator-emphasis — พระดำรัส:**
- JHN 4:50 GK: `ἐπίστευσεν ὁ ἄνθρωπος τῷ λόγῳ ὃν εἶπεν αὐτῷ ὁ Ἰησοῦς` → TH: `ชายผู้นั้นเชื่อ**พระดำรัส**ที่พระเยซูตรัสกับเขา`
- JHN 5:38 GK: `τὸν λόγον αὐτοῦ οὐκ ἔχετε ἐν ὑμῖν μένοντα` → TH: `**พระดำรัส**ของพระองค์ก็ไม่ได้คงอยู่ในพวกท่าน`

**POSSIBLE DRIFT — Farewell Discourse (chs 14–17) systematically uses plain คำ for Jesus's word/teaching, even where the narrator-emphasis matches the พระดำรัส pattern above:**
- JHN 14:23 GK: `ἐάν τις ἀγαπᾷ με τὸν λόγον μου τηρήσει` → TH: `ถ้าผู้ใดรักเรา ผู้นั้นจะรักษา**คำ**ของเรา`
- JHN 14:24 GK: `ὁ μὴ ἀγαπῶν με τοὺς λόγους μου οὐ τηρεῖ` → TH: `ผู้ที่ไม่รักเราย่อมไม่รักษา**คำ**ของเรา`
- JHN 15:3 GK: `ἤδη ὑμεῖς καθαροί ἐστε διὰ τὸν λόγον ὃν λελάληκα ὑμῖν` → TH: `พวกท่านสะอาดแล้วเพราะ**คำ**ที่เรากล่าวกับพวกท่าน`
- JHN 17:20 GK: `οὐ περὶ τούτων δὲ ἐρωτῶ μόνον,ἀλλὰ καὶ περὶ τῶν πιστευόντων διὰ τοῦ λόγου αὐτῶν εἰς ἐμέ` → TH: `แต่ที่เราขอนั้น มิใช่เพื่อคนเหล่านี้เท่านั้น แต่เพื่อบรรดาผู้ที่จะเชื่อในเราเพราะ**คำ**ของพวกเขา`

**Two questions:**
1. Is the seven-way split (พระวาทะ Christological / พระวจนะ scripture / พระดำรัส narrator-emphasized speech / คำ general / คำพยาน testimony / คำสอน teaching / คำเล่าลือ rumor) sound for Johannine λόγος?
2. Should the Farewell-Discourse คำ at 14:23, 14:24, 15:3, 17:20 be lifted to พระดำรัส for consistency with 2:22 / 4:41 / 4:50 / 5:38 narrator-emphasis pattern? Or is the Upper-Room intimacy register (Jesus speaking to disciples, not a public crowd) a principled reason to use plain คำ? This needs a corpus doc before 1 John 1:1 ("the Word of life"), Hebrews 4:12, Revelation 19:13.

---

## Item C — JHN 3:11 ἀμὴν ἀμὴν drift (sole violation of locked formula)

**The locked rule:** `johannine_doubled_amen_2026-04.md` locks the Johannine doubled-amen formula → **อาเมน อาเมน** (Aramaic-embed treatment, Mark-pattern).

**Compliance — all other JHN occurrences (verified all 10 plural-form ὑμῖν + 2 singular-form σοι):**
- JHN 6:47, 8:51, 12:24, 13:16, 13:20, 14:12, 16:20, 16:23: all use **อาเมน อาเมว เราบอกแก่พวกท่านว่า**
- JHN 13:38 (singular σοι, to Peter): **อาเมน อาเมว เราบอกแก่เจ้าว่า**
- JHN 21:18 (singular σοι, to Peter): **อาเมน อาเมว เราบอกแก่เจ้าว่า**

**THE ONE OUTLIER — JHN 3:11:**
- JHN 3:11 GK: `ἀμὴν ἀμὴν λέγω σοι,ὃ οἴδαμεν λαλοῦμεν` → TH: `**ความจริง ความจริง เราบอกท่านว่า** เรากล่าวสิ่งที่เรารู้`

This is the only Johannine ἀμὴν ἀμὴν that uses the older Synoptic-style **ความจริง ความจริง** rendering instead of the locked **อาเมน อาเมว**. The phrase-consistency checker missed it because the singular-σοι form `ἀμὴν ἀμὴν λέγω σοι` isn't in the script's Greek-pattern variant list (the check only audits `ἀμὴν ἀμὴν λέγω ὑμῖν` plural).

**Question:** Confirm the recommended normalization: 3:11 → "อาเมน อาเมว เราบอกแก่ท่านว่า" (singular ท่าน since Nicodemus is addressed individually, mirroring the 13:38 / 21:18 σοι pattern with เจ้า). Are there contextual reasons to keep the older "ความจริง ความจริง" rendering specifically at 3:11 that I'm missing?

---

## Item D — JHN 7:8 SBLGNT οὐκ vs Thai "ยังไม่" mismatch

**The textual variant:** SBLGNT/NA28/UBS5 read `ἐγὼ οὐκ ἀναβαίνω εἰς τὴν ἑορτὴν ταύτην` ("I am NOT going up to this feast"). TR/Byz read `οὔπω` ("I am NOT YET going up"). RULES §0 binds the project to SBLGNT — the verse-level `notes` correctly explains the variant + names Porphyry's "Jesus lied" critique that motivates the οὔπω scribal smoothing.

**HOWEVER — the Thai rendering lexicalizes οὔπω, not οὐκ:**
- JHN 7:8 GK: `ὑμεῖς ἀνάβητε εἰς τὴν ἑορτήν·ἐγὼ οὐκ ἀναβαίνω εἰς τὴν ἑορτὴν ταύτην,ὅτι ὁ ἐμὸς καιρὸς οὔπω πεπλήρωται` → TH: `พวกท่านจงขึ้นไปยังเทศกาลเถิด ส่วนเรา เรา**ยังไม่**ขึ้นไปยังเทศกาลนี้ เพราะเวลาของเรา**ยังไม่**ครบกำหนด`

The Thai uses **ยังไม่** ("not yet") for both the disputed οὐκ AND the undisputed final οὔπω ("my time has not yet come"). A SBLGNT-faithful rendering would distinguish: **ไม่** ("not") for οὐκ + **ยังไม่** ("not yet") for οὔπω. The current rendering effectively translates the rejected TR/Byz reading.

**Two questions:**
1. Is this an intentional Thai-naturalness softening (preserving "ethical-coherence reading" — Jesus's "not at this moment / not in the way you expect" sense) that should be documented as a principled exception at 7:8 KD? Or is it drift from the SBLGNT lock that should be revised?
2. If revising, what's the best Thai rendering for οὐκ ἀναβαίνω that preserves naturalness without lexicalizing οὔπω? Options: (a) plain "เราไม่ขึ้นไปยังเทศกาลนี้" + reader resolves at v.10; (b) "เราไม่ขึ้นไปยังเทศกาลนี้[ในตอนนี้]" with bracketed clarifier; (c) restructure entirely.

---

## Item E — JHN 1:34 ἐκλεκτός vs υἱός — SBLGNT-strict against unanimous evangelical-Thai expectation

**The textual variant:** SBLGNT (followed here) reads `ὁ ἐκλεκτὸς τοῦ θεοῦ` ("the Chosen One of God"); NA28, TR, Byzantine majority, KJV, BSB, NIV, ESV, CSB, **and all major Thai evangelical translations (THSV1971, NTV, ERV-Thai)** read `ὁ υἱὸς τοῦ θεοῦ` ("the Son of God").

**Manuscript split:**
- ἐκλεκτός: P5 (3rd c.), ℵ* (original hand of Sinaiticus), some Old Latin, Old Syriac (early geographical-spread despite small total count)
- υἱός: P66, P75, ℵ², A, B, C, K, L, etc. (overwhelming majority)

**SBLGNT chose ἐκλεκτός on lectio-difficilior grounds (scribes harmonize "Chosen" → "Son" toward Synoptic baptismal-voice "this is my beloved Son"); NA28 sided with the majority υἱός. The project follows SBLGNT per RULES §0.**

- JHN 1:34 GK: `κἀγὼ ἑώρακα,καὶ μεμαρτύρηκα ὅτι οὗτός ἐστιν **ὁ ἐκλεκτὸς** τοῦ θεοῦ` → TH: `และข้าพเจ้าได้เห็นแล้ว และได้เป็นพยานยืนยันว่า ผู้นี้คือ**ผู้ที่พระเจ้าทรงเลือกสรร**`

**Editorial weight:** This is one of two verses in JHN where the SBLGNT reading diverges from mainstream evangelical English-Bible tradition (the other is 1:18 μονογενὴς θεός vs. μονογενὴς υἱός — pre-locked, fully documented). 1:34 is more visible because **NA28 itself** disagrees — even the standard scholarly critical text sides with υἱός.

**Three questions:**
1. Is the SBLGNT-strict choice defensible here, or does the lectio-difficilior argument fail (e.g., is there evidence the ἐκλεκτός reading is itself a scribal harmonization toward Isa 42:1 LXX — "behold my Chosen [ἐκλεκτός μου]")?
2. If keeping SBLGNT ἐκλεκτός: should a footer-note manage Thai-evangelical reader expectation (e.g., "ต้นฉบับโบราณบางฉบับ: 'พระบุตรของพระเจ้า'")?
3. Or is this the rare case where the project should depart from RULES §0 SBLGNT-strictness and follow NA28 + the unanimous mainstream?

---

## Item F — Ἐγώ εἰμι absolute (predicate-less) — four-way contextual rendering

**The pattern:** The seven famous "I am the X" sayings (with predicate) are rendered uniformly with **เราเป็น + [predicate]** (bread of life, light of world, gate, good shepherd, resurrection, way, vine — not at issue here). The **absolute / predicate-less Ἐγώ εἰμι** (echoing Exod 3:14 LXX `ἐγώ εἰμι ὁ ὤν` + Isa 43:10 LXX) is rendered four different ways by context:

| Context | Thai | Verses |
|---|---|---|
| Self-identification to terrified disciples ("It's me / Don't be afraid") | **นี่เราเอง** | 6:20 |
| Mid-dialogue self-disclosure to Samaritan woman (gloss-extended for clarity) | **เราที่กำลังพูดกับท่านอยู่นี้คือผู้นั้นเอง** | 4:26 |
| Climactic identification before arresting soldiers ("I am he") | **เราคือผู้นั้น** | 18:5, 18:6, 18:8 |
| **Climactic Christological / YHWH-echo** ("Before Abraham was, I AM") | **เราเป็น** (bare predicate) | 8:24, 8:28, 8:58, 13:19 |

**The bare-เราเป็น at 8:58 (climactic):**
- JHN 8:58 GK: `Ἀμὴν ἀμὴν λέγω ὑμῖν,πρὶν Ἀβραὰμ γενέσθαι ἐγὼ εἰμί` → TH: `อาเมน อาเมว เราบอกแก่พวกท่านว่า ก่อนที่อับราฮัมจะเกิด **เราเป็น**`

**The dialogue gloss-extended at 4:26 (Samaritan woman):**
- JHN 4:26 GK: `Ἐγώ εἰμι,ὁ λαλῶν σοι` → TH: `**เราที่กำลังพูดกับท่านอยู่นี้คือผู้นั้นเอง**`

**The arresting-scene 18:5–8:**
- JHN 18:5–6 GK: `λέγει αὐτοῖς Ἰησοῦς·Ἐγώ εἰμι ... ὡς οὖν εἶπεν αὐτοῖς·Ἐγώ εἰμι,ἀπῆλθον εἰς τὰ ὀπίσω καὶ ἔπεσαν χαμαί` → TH: `พระเยซูตรัสกับพวกเขาว่า "**เราคือผู้นั้น**" ... เมื่อพระเยซูตรัสกับพวกเขาว่า "**เราคือผู้นั้น**" พวกเขาก็ถอยหลังและล้มลงกับพื้น`

**Question:** Is the four-way contextual split principled (each rendering tracks the narrative function: recognition / dialogue-clarification / arrest-scene-self-identification / YHWH-echo-climax), or is the absolute Ἐγώ εἰμι better preserved with a single Thai form across all 8 verses to flag the deliberate Johannine theological signature? Specifically: should 4:26 + 6:20 + 18:5–8 also use bare **เราเป็น** to preserve the YHWH-echo cluster, even at the cost of dialogue naturalness?

---

## Item G — Father↔Son glorification idiom (พระสิริ-receive/transfer, distinct from human-praise default สรรเสริญ)

**The pattern:** The corpus locks **สรรเสริญ** as the default for δοξάζω + εὐλογέω + αἰνέω + αἶνον δίδωμι **when humans glorify God** (`divine_object_praise_verbs_2026-04.md`, Acts-amended with narrator-doxological **ถวายเกียรติ** sub-rule). JHN exhibits a third category not in the doc: **Father↔Son intra-Trinitarian glorification** (very dense in JHN 12 + 17), which uses **พระสิริ** (noun "glory") + receive-causative verbs:

| GK | TH | Verse |
|---|---|---|
| `δοξασθῇ ὁ υἱὸς τοῦ ἀνθρώπου` | **บุตรมนุษย์จะได้รับพระสิริ** | 12:23 |
| `δόξασόν σου τὸ ὄνομα` | **ขอทรงทำให้พระนามของพระองค์ได้รับพระสิริเถิด** | 12:28 |
| `ἐδόξασα ... δοξάσω` | **ได้ทำให้ได้รับพระสิริแล้ว ... จะทำให้ได้รับพระสิริอีก** | 12:28b |
| `ὁ θεὸς δοξάσει αὐτὸν ἐν αὑτῷ` | **พระเจ้าก็จะทรงให้พระองค์ได้รับพระสิริในพระองค์เอง** | 13:32 |
| `δόξασόν σου τὸν υἱὸν,ἵνα ὁ υἱὸς δοξάσῃ σε` | **ขอพระองค์ทรงให้พระบุตรของพระองค์ได้รับพระสิริ เพื่อพระบุตรจะถวายพระสิริแด่พระองค์** | 17:1 |
| `δόξασόν με σύ,πάτερ,παρὰ σεαυτῷ` | **ขอพระองค์ทรงให้เราได้รับพระสิริต่อพระพักตร์ของพระองค์** | 17:5 |

**Distinct from human-praise-of-God default:**
- JHN 5:41 GK: `δόξαν παρὰ ἀνθρώπων οὐ λαμβάνω` → TH: `เราไม่รับ**เกียรติ**จากมนุษย์` (here δόξα = "honor" from humans, → เกียรติ — different lemma class)
- (No JHN human-praises-God-with-δοξάζω-verb instance to test the default; the "they glorified God" Acts-pattern doesn't appear in JHN at all.)

**Question:** Is the Father↔Son glorification rendering (พระสิริ + receive-causative) the right Thai for δοξάζω when the subject AND object are both divine persons (Father/Son), as distinct from (a) human-praise-of-God default (สรรเสริญ) and (b) corporate-narrator doxological acclamation (ถวายเกียรติ)? Should `divine_object_praise_verbs_2026-04.md` be amended to add this Father↔Son sub-rule before Romans 8:30 (ἐδόξασεν), 2 Cor 3:18 (ἀπὸ δόξης εἰς δόξαν — transformative-glory), Eph 1:6/12/14 (εἰς ἔπαινον τῆς δόξης), 1 Pet 1:8, and Revelation's massive doxological-glory vocabulary?

---

## Item H — JHN 21:15–17 ἀγαπάω/φιλέω flattening to รัก

**The decision (explicit, documented at 21:15 KD):** Jesus uses **ἀγαπάω** twice (vv.15, 16) then switches to **φιλέω** in v.17; Peter answers all three with **φιλέω**. Thai renders **all six occurrences as รัก**, matching NIV/ESV/CSB (synonym-hypothesis position, widely held in modern Greek-NT scholarship). Same flattening applies corpus-wide: JHN 3:35 ἀγαπᾷ (Father loves Son) → ทรงรัก; JHN 5:20 φιλεῖ (Father loves Son) → ทรงรัก.

- JHN 21:15 GK: `ἀγαπᾷς με πλέον τούτων;... φιλῶ σε` → TH: `เจ้า**รัก**เรามากกว่าคนเหล่านี้หรือ ... ข้าพระองค์**รัก**พระองค์`
- JHN 21:17 GK: `φιλεῖς με;... φιλῶ σε` → TH: `เจ้า**รัก**เราหรือ ... ข้าพระองค์**รัก**พระองค์`

**Question:** Is the synonym-hypothesis position the right call for a CC0 Thai Bible aimed at Thai evangelicals, or should the project preserve the lexical distinction (e.g., ἀγαπάω → รัก vs. φιλέω → รักใคร่) for expository preaching that historically draws on the distinction? Should the decision be lifted from per-verse to a corpus doc?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
