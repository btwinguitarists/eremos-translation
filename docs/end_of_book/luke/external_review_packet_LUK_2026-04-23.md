# Luke — External AI Sanity-Check Review Packet
**Date assembled: 2026-04-23**

Paste this entire document into **one** of: Grok, ChatGPT (o3 / 4.5), Gemini 2.5 Pro. Follow the prompt at the top. Then copy the AI's response back to the Claude Code session that generated this packet.

---

## PROMPT — please read this carefully before reviewing

You are performing an **end-of-book external sanity-check review** of the Thai Gospel of Luke from a CC0, AI-assisted Bible translation project translating the Greek NT directly into Thai (no reliance on copyrighted Thai Bibles). Your output will be pasted back into the project's main Claude Code session to surface corpus-level concerns that per-chapter automated checks may have missed.

### What the project is

- **Philosophy:** optimal equivalence (BSB-family), faithful to Greek grammar AND natural in modern Thai.
- **Confessional position:** evangelical Protestant. Source: SBLGNT (same base as ESV/NIV/NASB/CSB/BSB). 27-book NT.
- **Output:** CC0 — editorial decisions are evangelical Protestant but the license is public-domain.
- **Status:** Luke 24/24 complete. 24 chapters shipped. All per-chapter automated checks passed (key-term consistency, back-translation, OT citation, parallel passages, Thai summary coverage, claim consistency, Greek-field integrity, TNBT structural comparison).
- **Corpus so far:** Mark (complete, tagged `book-mark-v1`), Matthew (complete, tagged `book-matthew-v1`), Luke (complete, not yet tagged), 1 Tim 3 pilot, Acts 1.

### What you are NOT doing

- **Do not re-evaluate the per-chapter automated checks.** They all pass.
- **Do not re-litigate corpus-level choices already locked.** Those are listed below in §B.
- **Do not suggest rewording individual verses for stylistic taste.** Thai style judgments belong to a native-speaker review, not an AI review.
- **Do not propose alternative renderings for the sake of variety.** Consistency is a feature, not a bug, for key terms.

### What you ARE doing

Read the 6 sample Luke chapters below (Luke 1, 4, 10, 15, 18, 24) alongside the Greek, cross-referenced against the RULES.md and already-locked decisions (§A and §B below). Surface **corpus-level editorial concerns** — the kind of concern that would compound across Acts and the Pauline corpus if unaddressed.

Specifically, flag:

1. **Corpus-level key-term drift** — a Greek lemma rendered differently across these 6 chapters without documented rationale. (Per-chapter check is clean; this is a cross-chapter concern.)
2. **Theological-register inconsistencies** — e.g., if the narrator's register toward Jesus shifts mid-book, or if divine honorifics (ราชาศัพท์ per RULES §3) are inconsistently applied.
3. **Undocumented corpus-level editorial choices** — choices that SHOULD have a translator_decisions doc but don't. The project already has 13 such docs (see §B); flag topics that you'd expect a 14th.
4. **Textual-variant handling concerns** — the project follows SBLGNT per RULES §0; flag any variant handling that seems inconsistent with the SBLGNT-aligned evangelical-Protestant editorial stance or the Path A inclusion-variant convention (RULES §5).
5. **Acts-forward compounding risks** — since Luke-Acts is a two-volume work by the same author, specific Lukan choices will compound into Acts. Flag high-compounding-risk items the project should lock before Acts translation gets far.
6. **Thai naturalness red flags you can detect as an LLM** — not full stylistic review (native speakers handle that), but obvious Thai idiom errors or register confusion that an educated LLM can catch.

### What a good flag looks like

- Specific Greek lemma or verse range
- The observed Thai pattern (with verse references)
- Why it matters (corpus-level compounding, not just one-verse aesthetic)
- What action you recommend (new decision doc / spot revision / nothing if it's fine)

### What a weak flag looks like (don't bother)

- "You should consider using X synonym" (stylistic taste, not corpus issue)
- "I wonder if Y would be clearer" (we have a native-speaker review step for this)
- "Greek word Z could also mean..." (we have per-chapter key_decisions for this)
- "This reading assumes [textual variant X]" (RULES §0 locks the evangelical-Protestant SBLGNT position)

### Output format

Return your response in this structure:

```
# EXTERNAL REVIEW - LUKE - {your AI name + date}

## A. Corpus-level concerns flagged (RANKED high->low priority)
1. [Flag title]
   - Evidence: [verses + Thai patterns observed]
   - Why it matters: [Acts-forward / corpus-level reasoning]
   - Recommendation: [specific action]

2. ...

## B. Items I considered but do NOT need to flag (brief rationale each)
- [topic]: [why it's fine]

## C. Acts-forward preparatory recommendations (things to lock BEFORE Acts 2+ ship)

## D. Additional observations (optional - style, naturalness detectable by LLM)
```

Keep the review ~1500-3000 words. Concrete > exhaustive. If you have no concerns, say so — confidence that the corpus is in shape is a valid outcome.

---

## §A. Compressed RULES.md context

**§0 Confessional position:** evangelical Protestant, SBLGNT-aligned, CC0 license. Follow mainstream evangelical critical-text consensus. Notes describe facts, not endorse other traditions' theology.

**§1 Philosophy:** optimal equivalence. Accuracy > naturalness when they conflict.

**§2 Sources during translation:** Greek (SBLGNT), MACULA morph, BSB English as sanity-check (never copy), RULES.md, glossary.json, prior Eremos output, unfoldingWord uW TN + book intros (read for context, never copy wording). NEVER: copyrighted Thai Bibles (THSV/NTV/ERV/TNCV), TNBT wording, copyrighted commentary.

**§3 Register:**
- Divine subjects (God, Christ, Spirit): ราชาศัพท์ always. ทรง- / เสด็จ / ตรัส / ทอดพระเนตร / พระหัตถ์ / พระบาท / พระเจ้า / พระเยซู.
- Humans addressing Christ/God: ข้าพระองค์ / พระองค์ (lowest humble).
- Demons/adversaries: neutral/distancing register, no honorifics.
- Inter-human: match social relationship.

**§4 Key-term non-negotiables:**
- εὐαγγέλιον → ข่าวประเสริฐ
- χριστός → พระคริสต์
- Ἰησοῦς → พระเยซู
- σατανᾶς → ซาตาน
- πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์
- βαπτίζω → บัพติศมา
- ἔρημος → ถิ่นทุรกันดาร (wilderness) / ที่เปลี่ยว (solitary place)
- κύριος (= YHWH) → องค์พระผู้เป็นเจ้า
- κύριος (title for Jesus/human master) → context-dependent, documented
- συναγωγή → ธรรมศาลา
- μετανοέω → กลับใจ
- βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า
- ἁμαρτία → บาป
- ἀγαπητός → ที่รัก

**§5 Inclusion-variant policy (Path A LOCKED 2026-04-20):**
- Tier 1 — short phrase: single brackets `[...]` in main text
- Tier 2 — whole verse SBLGNT omits: chapter footer note (not in main flow)
- Tier 3 — large transmitted blocks: ⟦...⟧ double brackets in main text
- Luke applies this consistently; two Western non-interpolations in Luke 24 (24:3 omits τοῦ κυρίου Ἰησοῦ; 24:36 omits εἰρήνη ὑμῖν) follow SBLGNT per RULES §0.

**§6 Verse schema:** `translation: { thai, thai_literal, thai_summary, key_decisions, notes }`. Every field required (null or [] permitted). `key_decisions[].greek` must contain actual Greek text or morphological-reference keyword.

---

## §B. Already-locked translator_decisions (do NOT re-raise these)

The project has 13 corpus-level decision docs under `docs/translator_decisions/`:

1. **amen_saying_formula_2026-04** — ἀμὴν λέγω ὑμῖν → **เราบอกความจริงแก่พวกท่าน** (Mark/Matt/Luke locked).
2. **aramaic_transliterations_2026-04** — Mark's Aramaicisms (ταλιθα κουμ, εφφαθα) transliterated + translated in Thai. (Luke has no Aramaicisms.)
3. **ekklesia_2026-04** — ἐκκλησία → **คริสตจักร** (Matt 16:18/18:17; Acts-forward ~110 occurrences). Secular/LXX uses → ที่ประชุม with note. (Luke has no ἐκκλησία.)
4. **historic_present_2026-04** — Greek historic-present verbs → Thai past tense, universal.
5. **honorifics_non_divine_authorities_2026-04** — Herod/Pilate/centurions/Sanhedrin handled per character class.
6. **inclusion_variants_absent_verses_2026-04** — Path A locked (see §A above).
7. **markan_euthys_immediately_2026-04** — Mark-specific (Luke does not use εὐθύς).
8. **metanoeo_vs_metamelomai_2026-04** — μετανοέω → กลับใจ (salvific); μεταμέλομαι → เปลี่ยนใจ / เสียใจ (non-salvific). Matthew-era lock. (Luke has μετανοέω only.)
9. **narrator_vs_character_voice_2026-04** — narrator uses royal register toward Jesus consistently; character register tracks speaker's stance.
10. **son_of_man_disambiguation_2026-04** — ὁ υἱὸς τοῦ ἀνθρώπου → **บุตรมนุษย์** (Christological title). Generic plural υἱοὶ τῶν ἀνθρώπων → บุตรของมนุษย์.

### Newly locked during this review (2026-04-22 — Luke end-of-book review, PR #28):

11. **kyrios_narrator_voice_luke_acts_2026-04** — narrator-voice ὁ κύριος referring to Jesus → **องค์พระผู้เป็นเจ้า** across Luke and forward into Acts. Luke 10:41's พระเยซู preserved as principled Mary-Martha exception (intimate rebuke-comfort register). 12 Luke narrator-κύριος verses follow the lock; 1 exception.
12. **basileia_kingdom_rendering_2026-04** — preserves Greek distinction in Thai:
   - τῶν οὐρανῶν → **อาณาจักรสวรรค์** (Matthew periphrasis only)
   - τοῦ θεοῦ → **อาณาจักรของพระเจ้า** (Mark, Luke, Matt 12:28+21:31, Acts, balance of NT)
   - Non-kingdom-of-God uses (political, parabolic, Satan's kingdom) → context-adapted plain อาณาจักร or การเป็นกษัตริย์.
13. **vocative_kyrie_didaskale_register_2026-04** — speaker-class variation for vocative Κύριε (disciples → องค์พระผู้เป็นเจ้า; humble intimates like centurion/Martha → พระองค์เจ้าข้า; parabolic servants → นายท่าน/นายเจ้าข้า) and Διδάσκαλε (neutral → ท่านอาจารย์; elevated → พระอาจารย์; testing → อาจารย์เจ้าข้า).

### Items already surveyed and **affirmed stable** during Luke end-of-book review

Do NOT flag these as corpus concerns; they've been checked and confirmed:
- **πνεῦμα ἅγιον** → **พระวิญญาณบริสุทธิ์** (all 13 Luke occurrences uniform, glossary-locked).
- **σήμερον** → **วันนี้** (all 11 Luke occurrences uniform; eschatological loading contextual, not lexical).
- **Ἰερουσαλήμ + Ἱεροσόλυμα** → **เยรูซาเล็ม / กรุงเยรูซาเล็ม** (Thai has no grammatical gender; Greek feminine/neuter distinction lost but noted as a known target-language limitation).
- **σωτήρ / σωτηρία / σῴζω** (salvation family) → พระผู้ช่วยให้รอด / ความรอด / ช่วยให้รอด (uniform by lemma).
- **τελώνης** → **คนเก็บภาษี** (uniform).
- **ἁμαρτωλός** → **คนบาป** (uniform).
- **Σαμαρίτης** → **ชาวสะมาเรีย** (uniform).
- **Magnificat / Benedictus / Nunc Dimittis** — rendered in elevated Thai register; native-speaker spot-check pending as separate action item.
- **Herod family disambiguation** — Herod the Great (1:5) / Antipas (3:1+) / Herodias / Philip — context-disambiguated per Greek source.

---

## §C. Sample chapters

Six representative Luke chapters follow, compressed format (verse reference, Greek, Thai, Thai summary if present, key decisions trimmed, notes trimmed). These are the chapters you're reviewing. The project repo has the full translations — this compression is for review efficiency, not for translation.


### Luke 1

**Luke 1:1**
- GR: Ἐπειδήπερ πολλοὶ ἐπεχείρησαν ἀνατάξασθαι διήγησιν περὶ τῶν πεπληροφορημένων ἐν ἡμῖν πραγμάτων,
- TH: ด้วยเหตุที่หลายคนได้พยายามเรียบเรียงเรื่องราวเกี่ยวกับเหตุการณ์ทั้งหลายที่ได้สำเร็จแล้วท่ามกลางพวกเรา
- TH-summary: ลูกาเริ่มต้นพระกิตติคุณด้วยอารัมภบทที่เป็นภาษากรีกแบบคลาสสิก คล้ายกับนักประวัติศาสตร์ชาวกรีก-โรมันอย่างเฮโรโดตัสและโยเซฟัส ลูกาไม่ได้อ้างว่าตนเป็นคนแรกที่เขียน แต่ยอมรับว่ามีผู้อื่นที่เขียนไว้ก่อนแล้ว เช่น พระกิตติคุณมาระโกและแหล่งข้อมูลอื่น คำว่า «ที่ได้สำเร็จแล้ว» สะท้อนว่าเหตุการณ์เกี่ยวกับพระเยซูเป็นความสำเร็จของพระสัญญาในพระคัมภีร์เดิม
- Key decisions:
  - Ἐπειδήπερ → ด้วยเหตุที่ — HAPAX in NT. Classical Greek causal conjunction, 'inasmuch as / since indeed.' The -περ suffix intensifies. This opens Luke with elevated literary register matching Hellenistic historiographical prefaces (cf. Joseph...
  - πολλοὶ ἐπεχείρησαν → หลายคนได้พยายาม — ἐπιχειρέω (NT freq 3) = 'put hand to / attempt.' Not necessarily disparaging — Luke is not criticizing prior attempts but situating his own work alongside them. Thai พยายาม preserves the 'effort/attempt' sense witho...
  - ἀνατάξασθαι διήγησιν → เรียบเรียงเรื่องราว — TWO HAPAX side-by-side. ἀνατάσσομαι = 'arrange in order / compile.' διήγησις = 'narrative account.' Technical historiographical vocabulary — marks Luke as writing within the Greco-Roman history-writing tradition. Th...
  - περὶ τῶν πεπληροφορημένων → เกี่ยวกับเหตุการณ์ทั้งหลายที่ได้สำเร็จแล้ว — πληροφορέω perfect passive ptc. = 'fully accomplished / fulfilled.' Per uW figs-activepassive: things that have happened/been fulfilled. Luke chooses a loaded verb — πληρόω-related — signaling prophetic fulfillment....
  - ἐν ἡμῖν → ท่ามกลางพวกเรา — Per uW figs-exclusive: 'us' = the Christian community including Theophilus. Thai ท่ามกลางพวกเรา = 'in the midst of us' (inclusive)
- Notes: LUKE'S PREFACE (1:1-4) is a single Greek sentence in elevated Attic/Hellenistic register — one of the most polished pieces of prose in the NT. It parallels the conventions of Greco-Roman historiographical prologues (Herodotus, Thucydides, Polybius, Josephus). THREE HAPAX in v.1 alone: ἐπειδήπερ (only here in NT, classical causal conj.), ἀνατάσ...

**Luke 1:2**
- GR: καθὼς παρέδοσαν ἡμῖν οἱ ἀπ᾽ ἀρχῆς αὐτόπται καὶ ὑπηρέται γενόμενοι τοῦ λόγου,
- TH: ตามที่ผู้ซึ่งเป็นพยานเห็นกับตาและเป็นผู้รับใช้พระวจนะตั้งแต่แรกเริ่มได้ถ่ายทอดไว้แก่พวกเรา
- TH-summary: ลูกายอมรับว่าตนไม่ได้เป็นพยานโดยตรง แต่ได้รับข้อมูลจาก «พยานเห็นกับตา» (ออโทปไตส์) — ซึ่งเป็นคำศัพท์ทางการแพทย์ที่แพทย์กรีกใช้เกี่ยวกับการสังเกตโดยตรง — ลูกาเองเป็นหมอ (โคโลสี 4:14) นี่เป็นการอ้างพื้นฐานทางประวัติศาสตร์ที่หนักแน่น
- Key decisions:
  - παρέδοσαν → ได้ถ่ายทอดไว้ — παραδίδωμι = 'hand down / transmit / deliver.' Technical term for the transmission of tradition (cf. 1 Cor 11:23, 15:3). Thai ถ่ายทอด = 'transmit / pass down' — natural for tradition-transmission
  - αὐτόπται → พยานเห็นกับตา — HAPAX in NT. αὐτόπτης = 'eyewitness' (αὐτός 'self' + ὀπ- 'see'). Technical medical/forensic term used by Greek physicians and historians for direct observation. Thai พยานเห็นกับตา = 'witness seen-with-eye' (literal ...
  - ὑπηρέται...τοῦ λόγου → ผู้รับใช้พระวจนะ — ὑπηρέτης = 'under-rower / servant / attendant' (originally from ship context). Here = 'servants of the word' (Per uW figs-metaphor/metonymy — the 'word' is the message; serving the word = serving God's message). Tha...
  - ἀπ᾽ ἀρχῆς → ตั้งแต่แรกเริ่ม — Refers to the beginning of Jesus's ministry (cf. Acts 1:22 — 'from the baptism of John' as the starting point). Thai ตั้งแต่แรกเริ่ม natural
- Notes: NT HAPAX: αὐτόπτης ('eyewitness') — a technical term from Greco-Roman historiography and Hellenistic medicine (Hippocrates, Galen). Since Luke is traditionally identified as a physician (Col 4:14), his choice of this precise medical-investigative vocabulary is characteristic. The phrase establishes Luke's historiographical method: not autopsy-...

**Luke 1:3**
- GR: ἔδοξε κἀμοὶ παρηκολουθηκότι ἄνωθεν πᾶσιν ἀκριβῶς καθεξῆς σοι γράψαι, κράτιστε Θεόφιλε,
- TH: ดังนั้น ข้าพเจ้าจึงเห็นสมควรที่จะเขียนให้ท่านตามลำดับอย่างระมัดระวัง หลังจากได้สืบค้นทุกเรื่องอย่างถี่ถ้วนมาตั้งแต่ต้น ท่านธีโอฟีลัสผู้ทรงเกียรติ
- TH-summary: ลูกาเขียนถวายแด่ «ท่านธีโอฟีลัส» — ชื่อในภาษากรีกแปลว่า «มิตรของพระเจ้า» อาจเป็นข้าราชการชั้นสูงเพราะคำว่า «ผู้ทรงเกียรติ» (กราติสเต) เป็นคำเรียกที่ใช้กับผู้ปกครองชาวโรมัน (เทียบกับกิจการ 23:26 ที่ใช้เรียกเฟลิกซ์) ลูกาเน้นความแม่นยำของงานวิจัย — เป็นเรื่องสำคัญที่จะทราบว่าพระกิตติคุณเป็นผลจากการค้นคว้าอย่างรอบคอบ ไม่ใช่ตำนาน
- Key decisions:
  - ἔδοξε κἀμοὶ → ข้าพเจ้าจึงเห็นสมควร — Impersonal ἔδοξε + dative 'it seemed-good to-me-also' (κἀμοί = καί + ἐμοί). Idiom of decision. Thai เห็นสมควร natural. First-person self-reference ข้าพเจ้า — Luke is writing humbly to a social superior
  - παρηκολουθηκότι ἄνωθεν πᾶσιν ἀκριβῶς → ได้สืบค้นทุกเรื่องอย่างถี่ถ้วนมาตั้งแต่ต้น — παρακολουθέω perfect ptc. = 'having followed closely / investigated carefully.' ἄνωθεν = 'from the beginning / from above.' ἀκριβῶς = 'precisely/accurately.' Thai สืบค้น...ถี่ถ้วน captures the investigation sense; ต...
  - καθεξῆς σοι γράψαι → ที่จะเขียนให้ท่านตามลำดับ — καθεξῆς = 'in order / successively' (NT only in Luke-Acts). Not necessarily strict chronological order — but a coherent, orderly narrative. Thai ตามลำดับ preserves the orderly-arrangement sense
  - κράτιστε Θεόφιλε → ท่านธีโอฟีลัสผู้ทรงเกียรติ — κράτιστος superlative of κρατύς = 'most excellent' — formal title used for Roman officials (Acts 23:26 Felix, 24:3, 26:25 Festus). Theophilus likely a high-status patron. Θεόφιλος = 'friend/beloved of God' — may be ...
- Notes: Luke's statement of purpose and method. The four-fold self-description of his methodology — παρηκολουθηκότι ('having closely followed'), ἄνωθεν ('from the beginning'), πᾶσιν ('everything'), ἀκριβῶς ('accurately') — is emphatic: Luke claims comprehensive, careful, original research. κράτιστε ('most excellent') is the standard form of address fo...

**Luke 1:4**
- GR: ἵνα ἐπιγνῷς περὶ ὧν κατηχήθης λόγων τὴν ἀσφάλειαν.
- TH: เพื่อท่านจะได้ทราบถึงความแน่นอนของถ้อยคำต่างๆ ที่ท่านได้รับการสั่งสอนมา
- TH-summary: คำว่า «คำสั่งสอน» (กาเตเคโท) เป็นรากศัพท์ของคำว่า «คำสอน» (catechesis) ในภาษาอังกฤษ — ธีโอฟีลัสได้เรียนรู้เรื่องพระเยซูมาแล้ว ลูกาเขียนเพื่อเสริมความมั่นใจ ไม่ใช่เพื่อประกาศข่าวแรก
- Key decisions:
  - ἐπιγνῷς → จะได้ทราบ — ἐπιγινώσκω = 'know thoroughly / fully recognize.' Intensive of γινώσκω. Here = gain deep-settled knowledge. Thai จะได้ทราบ natural for 'come to know'
  - κατηχήθης → ได้รับการสั่งสอนมา — κατηχέω aorist passive = 'was orally instructed / catechized' — source of English 'catechism.' Luke presupposes Theophilus has already received Christian instruction. Per uW figs-activepassive: people have taught yo...
  - λόγων τὴν ἀσφάλειαν → ความแน่นอนของถ้อยคำ — ἀσφάλεια = 'safety / security / certainty' — from ἀ-σφάλλω 'not-liable-to-fall.' Emphatic word-order places ἀσφάλειαν at the climactic end of the periodic sentence. Thai ความแน่นอน preserves the certainty sense. λόγ...
- Notes: The climactic word ἀσφάλεια ('certainty') stands at the end of Luke's elaborate periodic prologue — emphatic by position. Luke's stated purpose: not to persuade a non-Christian, but to reinforce the certainty of what Theophilus has already been taught. This aligns with Luke's overall apologetic-instructive purpose, providing a 'reliable' (ἀσφα...

**Luke 1:5**
- GR: Ἐγένετο ἐν ταῖς ἡμέραις Ἡρῴδου βασιλέως τῆς Ἰουδαίας ἱερεύς τις ὀνόματι Ζαχαρίας ἐξ ἐφημερίας Ἀβιά, καὶ γυνὴ αὐτῷ ἐκ τῶν θυγατέρων Ἀαρών, καὶ τὸ ὄνομα αὐτῆς Ἐλισάβετ.
- TH: ในรัชสมัยของกษัตริย์เฮโรดแห่งแคว้นยูเดีย มีปุโรหิตคนหนึ่งชื่อเศคาริยาห์ จากกลุ่มปุโรหิตอาบียาห์ ภรรยาของท่านเป็นลูกหลานของอาโรน ชื่อเอลีซาเบธ
- TH-summary: ลูกาเปลี่ยนจากภาษากรีกคลาสสิก (ข้อ 1-4) มาเป็นภาษาแบบเซปทัวจินต์ (LXX) อย่างกะทันหัน — สไตล์ภาษาเหมือนพระคัมภีร์เดิมที่แปลเป็นกรีก «ในรัชสมัย» (เอน ไตส์ เฮเมอไรส์) เป็นสำนวนภาษาฮีบรู ทำให้เรื่องราวดูเหมือนต่อเนื่องจากพระคัมภีร์เดิม เฮโรดมหาราชปกครองประมาณ 37-4 ก่อนคริสตกาล ดังนั้นเหตุการณ์นี้อยู่ประมาณ 6-5 ก่อนคริสตกาล
- Key decisions:
  - Ἐγένετο ἐν ταῖς ἡμέραις → ในรัชสมัย — Hebraic calque (LXX style) — וַיְהִי בִּימֵי 'and-it-came-to-pass in-the-days-of.' Marks the sharp stylistic shift from Hellenistic prologue (v.1-4) to Septuagintal narrative. Rather than a literal 'it came to pass ...
  - Ἡρῴδου βασιλέως τῆς Ἰουδαίας → กษัตริย์เฮโรดแห่งแคว้นยูเดีย — Herod the Great (37-4 BC). Thai เฮโรด established glossary (from MAT 2). กษัตริย์ for βασιλεύς. แคว้นยูเดีย established region-classifier. This places the annunciation in ~6-5 BC
  - ἱερεύς τις ὀνόματι Ζαχαρίας → ปุโรหิตคนหนึ่งชื่อเศคาริยาห์ — Per uW writing-participants: introduces new character. ἱερεύς = priest. Thai ปุโรหิต standard. Ζαχαρίας → เศคาริยาห์ per Thai Christian transliteration convention (zayin→s, ch→kh, etc. — standard Protestant Thai). M...
  - ἐξ ἐφημερίας Ἀβιά → จากกลุ่มปุโรหิตอาบียาห์ — ἐφημερία = priestly division (one of 24 rotating courses per 1 Chr 24:10 — Abijah is 8th). Per uW figs-explicit: this is a temple-service group. Thai กลุ่มปุโรหิต makes the priestly-rotation-group sense explicit. Ἀβ...
  - ἐκ τῶν θυγατέρων Ἀαρών → เป็นลูกหลานของอาโรน — Per uW figs-metaphor: 'daughters' = female descendants. Thai ลูกหลาน (neutral 'descendants') preserves sense without gendered awkwardness. Ἀαρών → อาโรน standard. Both Zechariah and Elizabeth are priestly-lineage — ...
  - Ἐλισάβετ → เอลีซาเบธ — From Hebrew אֱלִישֶׁבַע 'Elisheba' = 'my God is an oath.' Aaron's wife in Exod 6:23 has the same name — another priestly-continuity echo. Thai เอลีซาเบธ per Thai Christian transliteration convention
- Notes: STYLISTIC SHIFT: after the polished Hellenistic prologue of 1:1-4, Luke abruptly shifts to Septuagintal Greek — 'Ἐγένετο ἐν ταῖς ἡμέραις' mimics the Hebraic וַיְהִי בִּימֵי opening found throughout LXX narrative (Gen 14:1, Judg 1:1, 1 Sam 1:1, 2 Sam 21:1, etc.). This is Luke's deliberate literary strategy: the infancy narrative is rendered in ...

**Luke 1:6**
- GR: ἦσαν δὲ δίκαιοι ἀμφότεροι ἐναντίον τοῦ θεοῦ, πορευόμενοι ἐν πάσαις ταῖς ἐντολαῖς καὶ δικαιώμασιν τοῦ κυρίου ἄμεμπτοι.
- TH: ทั้งสองเป็นคนชอบธรรมต่อพระพักตร์พระเจ้า ดำเนินชีวิตตามพระบัญชาและกฎเกณฑ์ทั้งสิ้นขององค์พระผู้เป็นเจ้าอย่างไร้ที่ติ
- TH-summary: คำว่า «ชอบธรรม» และ «ไร้ที่ติ» ไม่ได้หมายความว่าไม่มีบาป แต่หมายถึงการรักษาพันธสัญญาอย่างซื่อสัตย์ ภายใต้กรอบของกฎของโมเสส (เทียบกับปฐมกาล 6:9 โนอาห์, โยบ 1:1, ฟีลิปปี 3:6 เปาโล) คู่สามีภรรยาเศคาริยาห์-เอลีซาเบธเป็นตัวแทนของอิสราเอลที่ซื่อสัตย์ซึ่งคอยท่าพระเมสสิยาห์
- Key decisions:
  - δίκαιοι...ἐναντίον τοῦ θεοῦ → ชอบธรรมต่อพระพักตร์พระเจ้า — Per uW figs-metaphor: ἐναντίον = 'before / in the sight of.' Thai ต่อพระพักตร์ ('before the face of,' royal-register) — preserves theophanic/judicial frame. δίκαιος → ชอบธรรม per established OT-NT glossary (MAT 1:19...
  - πορευόμενοι ἐν πάσαις ταῖς ἐντολαῖς καὶ δικαιώμασιν → ดำเนินชีวิตตามพระบัญชาและกฎเกณฑ์ทั้งสิ้น — Per uW figs-metaphor: 'walking in' = obeying. Hebrew halakh idiom preserved in LXX. Per uW figs-doublet: ἐντολαί 'commandments' + δικαιώματα 'statutes/righteous-decrees' quasi-synonymous, standard Deuteronomic pairi...
  - τοῦ κυρίου → องค์พระผู้เป็นเจ้า — κύριος here = YHWH (Deuteronomic-legal context). Per RULES.md §4 → องค์พระผู้เป็นเจ้า
  - ἄμεμπτοι → อย่างไร้ที่ติ — ἄμεμπτος = 'blameless / without-fault.' Phil 3:6 Paul uses the same word of pre-Christian righteousness 'according to the law.' Not sinless but covenantally faithful. Thai ไร้ที่ติ natural
- Notes: This verse establishes Zechariah and Elizabeth as the faithful-remnant of Israel — typologically, the righteous-waiting-ones who represent the best of Second Temple piety. The language echoes OT passages: Noah 'righteous...blameless' (Gen 6:9 LXX δίκαιος...ἄμεμπτος), Job 1:1 (ἄμεμπτος), Abraham walking before God (Gen 17:1). Their 'walking in ...

**Luke 1:7**
- GR: καὶ οὐκ ἦν αὐτοῖς τέκνον, καθότι ἦν ἡ Ἐλισάβετ στεῖρα, καὶ ἀμφότεροι προβεβηκότες ἐν ταῖς ἡμέραις αὐτῶν ἦσαν.
- TH: แต่ทั้งสองไม่มีบุตร เพราะเอลีซาเบธเป็นหมัน และทั้งคู่ก็มีอายุล่วงเข้าสู่วัยชราแล้ว
- TH-summary: ธีมของหญิงหมันที่พระเจ้าทรงเปิดครรภ์เป็นรูปแบบซ้ำในพระคัมภีร์เดิม: ซาราห์ (ปฐมกาล 11:30, 17-18), รีเบคาห์ (ปฐก 25:21), ราเชล (ปฐก 29:31, 30:22), มารดาของแซมสัน (ผู้วินิจฉัย 13), ฮันนาห์แม่ของซามูเอล (1 ซามูเอล 1-2) เอลีซาเบธเป็นผู้สืบทอดสายนี้ — การประสูติของยอห์นเป็นการอัศจรรย์ที่เตรียมทางสำหรับการอัศจรรย์ที่ใหญ่กว่าคือการประสูติของพระเยซู
- Key decisions:
  - καθότι → เพราะ — καθότι = 'because / insofar as' (Lukan preference; NT only in Luke-Acts). Per uW grammar-connect-logic-contrast: broader context implies 'but.' I render καθότι with causal เพราะ; the contrast is carried by the previ...
  - στεῖρα → เป็นหมัน — στεῖρα = 'barren/sterile.' Thai หมัน standard, same word used for Sarah in LXX (Gen 11:30). Carries OT-barrenness-theme weight
  - προβεβηκότες ἐν ταῖς ἡμέραις αὐτῶν → มีอายุล่วงเข้าสู่วัยชรา — Per uW figs-idiom: Hebraic idiom 'advanced in days' = aged. LXX-style phrasing (Gen 18:11 LXX of Abraham and Sarah — προβεβηκότες ἡμερῶν). Thai มีอายุล่วงเข้าสู่วัยชรา preserves elevated register. Echoes Gen 18:11 s...
- Notes: MAJOR OT PATTERN — the barren matriarch. This verse firmly places Zechariah and Elizabeth in the Hebrew-Bible pattern of aged-barren-couples-given-children: Abraham/Sarah (Gen 18:11 — προβεβηκότες ἡμερῶν is direct LXX echo), Isaac/Rebekah (Gen 25:21), Jacob/Rachel (Gen 29:31), Manoah/wife (Judg 13:2), Elkanah/Hannah (1 Sam 1). Each birth produ...

**Luke 1:8**
- GR: Ἐγένετο δὲ ἐν τῷ ἱερατεύειν αὐτὸν ἐν τῇ τάξει τῆς ἐφημερίας αὐτοῦ ἔναντι τοῦ θεοῦ
- TH: อยู่มาวันหนึ่ง ขณะที่เศคาริยาห์ปฏิบัติหน้าที่ปุโรหิตต่อพระพักตร์พระเจ้าในเวรของกลุ่มท่าน
- Key decisions:
  - Ἐγένετο δὲ → อยู่มาวันหนึ่ง — Per uW writing-newevent: narrative marker introducing first event. Hebraic וַיְהִי. Thai อยู่มาวันหนึ่ง standard biblical narrative formula
  - ἐν τῷ ἱερατεύειν αὐτὸν → ขณะที่เศคาริยาห์ปฏิบัติหน้าที่ปุโรหิต — HAPAX: ἱερατεύω = 'to serve as priest' (verb; cognate ἱερεύς in v.5). Used in 1 Chr 24 LXX. Thai ปฏิบัติหน้าที่ปุโรหิต natural. Name Zechariah inserted for clarity per uW writing-pronouns
  - ἐν τῇ τάξει τῆς ἐφημερίας αὐτοῦ → ในเวรของกลุ่มท่าน — τάξις = 'order/rotation.' ἐφημερία (repeated from v.5) = priestly course. Per uW writing-background: rotation schedule. Thai เวร (duty-rotation) precise for rotational service
  - ἔναντι τοῦ θεοῦ → ต่อพระพักตร์พระเจ้า — Per uW figs-metaphor: 'before God' = in God's presence, serving-in-temple. Thai ต่อพระพักตร์พระเจ้า preserves divine-presence sense with royal-register พระพักตร์
- Notes: NT HAPAX: ἱερατεύω (though common in LXX, cognate ἱερεύς frequent). The priestly division of Abijah (1 Chr 24:10) served two weeks per year. Ἐγένετο δὲ marks narrative shift from background to first event (Septuagintal idiom — LXX καὶ ἐγένετο translates וַיְהִי ~400 times).

**Luke 1:9**
- GR: κατὰ τὸ ἔθος τῆς ἱερατείας ἔλαχε τοῦ θυμιᾶσαι εἰσελθὼν εἰς τὸν ναὸν τοῦ κυρίου,
- TH: ตามธรรมเนียมของปุโรหิต ท่านได้รับเลือกโดยการจับสลากให้เข้าไปเผาเครื่องหอมในพระวิหารขององค์พระผู้เป็นเจ้า
- TH-summary: การจับสลากเป็นวิธีที่ปุโรหิตเลือกว่าใครจะทำหน้าที่สำคัญที่สุดในวันนั้น เช่น การเผาเครื่องหอมในพระวิหาร ซึ่งเป็นงานที่สามารถทำได้เพียงครั้งเดียวในชีวิต (เพราะมีปุโรหิตประมาณ 18,000 คน) นี่จึงอาจเป็นช่วงเวลาที่สำคัญที่สุดของชีวิตปุโรหิต และเป็นช่วงเวลาที่พระเจ้าทรงเลือกให้ทูตสวรรค์ปรากฏ
- Key decisions:
  - κατὰ τὸ ἔθος τῆς ἱερατείας → ตามธรรมเนียมของปุโรหิต — Per uW writing-background. ἱερατεία = 'priesthood (abstract).' Distinct from ἱερατεύω (v.8 verb) and ἱερεύς (v.5 noun-person). Thai ธรรมเนียมของปุโรหิต captures 'custom of priestly office'
  - ἔλαχε → ได้รับเลือกโดยการจับสลาก — λαγχάνω = 'obtain by lot.' Per uW translate-unknown. Thai จับสลาก natural + culturally transparent. Theologically: lots were understood as God's direct guidance (Prov 16:33)
  - τοῦ θυμιᾶσαι → เผาเครื่องหอม — HAPAX: θυμιάω = 'to burn incense' (verb). Cognate θυμίαμα (noun) in next verse. Per uW translate-unknown: priestly ritual on golden altar inside Holy Place (Exod 30:7-8, twice-daily). Thai เผาเครื่องหอม natural
  - εἰς τὸν ναὸν τοῦ κυρίου → ในพระวิหารขององค์พระผู้เป็นเจ้า — ναός = inner sanctuary (vs. ἱερόν = whole temple complex). Thai พระวิหาร conventional. κυρίου = YHWH → องค์พระผู้เป็นเจ้า
- Notes: NT HAPAX: θυμιάω (though θυμίαμα noun occurs 5x). Incense offered twice daily (Exod 30:7-8) on the golden altar inside the Holy Place. With ~18,000 priests in rotation, being chosen was a once-in-a-lifetime honor. ADDED TO NT_OT_CITATIONS: LUK 1:9 thematic_allusion to EXO 30:7-8 (daily incense offering).

**Luke 1:10**
- GR: καὶ πᾶν τὸ πλῆθος ἦν τοῦ λαοῦ προσευχόμενον ἔξω τῇ ὥρᾳ τοῦ θυμιάματος·
- TH: ในเวลาของการถวายเครื่องหอมนั้น ประชาชนทั้งหมดกำลังอธิษฐานอยู่ภายนอก
- Key decisions:
  - πᾶν τὸ πλῆθος...τοῦ λαοῦ → ประชาชนทั้งหมด — Per uW figs-hyperbole: generalization for 'large crowd.' Thai ประชาชนทั้งหมด captures emphasis without awkward double πλῆθος+λαός
  - προσευχόμενον ἔξω → กำลังอธิษฐานอยู่ภายนอก — Per uW figs-explicit: 'outside' = in court outside temple building (only priests entered ναός). Thai ภายนอก sufficient. προσεύχομαι → อธิษฐาน standard
  - τῇ ὥρᾳ τοῦ θυμιάματος → ในเวลาของการถวายเครื่องหอม — θυμίαμα noun 'incense' (cognate θυμιάω v.9). Per uW figs-metaphor: ὥρα = appointed time. Thai natural
- Notes: Zechariah alone inside the Holy Place at the golden altar, worshipers pray in outer courts during incense offering (traditional association with ~3PM afternoon service). The narrative pattern — solitary priest in sanctuary + worshiping crowd + angelic visitation — echoes Daniel 9:20-21 (Daniel prays at time of evening offering, Gabriel appears...

**Luke 1:11**
- GR: ὤφθη δὲ αὐτῷ ἄγγελος κυρίου ἑστὼς ἐκ δεξιῶν τοῦ θυσιαστηρίου τοῦ θυμιάματος.
- TH: ทันใดนั้น ทูตสวรรค์องค์หนึ่งขององค์พระผู้เป็นเจ้าปรากฏแก่เศคาริยาห์ ยืนอยู่ข้างขวาแท่นเผาเครื่องหอม
- TH-summary: ทูตสวรรค์ปรากฏที่ด้านขวาของแท่นเผาเครื่องหอม — ตำแหน่งที่ทรงเกียรติในทัศนะของชาวยิว (เทียบกับ สดุดี 110:1 «นั่งทางขวามือของเรา») แท่นเผาเครื่องหอมตั้งอยู่ในห้องบริสุทธิ์ หน้าผ้าม่านที่กั้นห้องบริสุทธิ์ที่สุด — เป็นสถานที่ใกล้ชิดพระเจ้าที่สุดที่ปุโรหิตธรรมดาจะเข้าได้
- Key decisions:
  - ὤφθη → ปรากฏ — Per uW figs-idiom: not just 'was seen in vision' — actual presence. Aorist passive of ὁράω. Thai ปรากฏ standard for theophanic appearances (cf. LUK 1:22, ACT 7:2)
  - ἄγγελος κυρίου → ทูตสวรรค์องค์หนึ่งขององค์พระผู้เป็นเจ้า — Established Matthean glossary (MAT 1:20, 2:13, 28:2). LXX-calque for מלאך יהוה. κύριος = YHWH here → องค์พระผู้เป็นเจ้า. The angel is Gabriel per v.19
  - ἑστὼς ἐκ δεξιῶν τοῦ θυσιαστηρίου τοῦ θυμιάματος → ยืนอยู่ข้างขวาแท่นเผาเครื่องหอม — ἐκ δεξιῶν = 'on the right (side).' Honorable position (Ps 110:1). θυσιαστήριον τοῦ θυμιάματος = altar of incense (Exod 30:1-6, golden altar inside Holy Place). Thai แท่นเผาเครื่องหอม
- Notes: The right side of the altar is the position of honor (Ps 110:1 'sit at my right hand'). The altar of incense was the golden altar inside the Holy Place, directly before the veil separating it from the Most Holy Place (Exod 30:1-6) — the closest sacred space ordinary priests could access. Tychonius, early church exegetes noted the parallel betw...

**Luke 1:12**
- GR: καὶ ἐταράχθη Ζαχαρίας ἰδών, καὶ φόβος ἐπέπεσεν ἐπ᾽ αὐτόν.
- TH: เมื่อเศคาริยาห์เห็นทูตสวรรค์ก็ตกใจ และความกลัวเข้าครอบงำท่าน
- Key decisions:
  - ἐταράχθη...ἰδών → เมื่อเศคาริยาห์เห็น...ก็ตกใจ — ταράσσω aor.pass. = 'was troubled/disturbed/startled.' Thai ตกใจ natural. Per uW figs-parallelism: 'troubled' + 'fear fell on him' are doublet for emphasis — I preserve both phrases rather than collapsing, per RULES...
  - φόβος ἐπέπεσεν ἐπ᾽ αὐτόν → ความกลัวเข้าครอบงำท่าน — Per uW figs-metaphor/figs-personification: 'fear fell on him' is idiomatic for overwhelming terror. Thai ความกลัวเข้าครอบงำ ('fear entered and overpowered') preserves the figurative personification
- Notes: Standard OT theophanic-response pattern — when an angel/divine figure appears, humans are overwhelmed with fear (cf. Judg 6:22-23, Dan 8:17-18, 10:7-12, Ezek 1:28). The doublet 'troubled + fear fell on him' is Hebraic-parallelism intensifying the terror. Contrast with v.13 where the angel immediately reassures 'do not be afraid' — the stereoty...

**Luke 1:13**
- GR: εἶπεν δὲ πρὸς αὐτὸν ὁ ἄγγελος· Μὴ φοβοῦ, Ζαχαρία, διότι εἰσηκούσθη ἡ δέησίς σου, καὶ ἡ γυνή σου Ἐλισάβετ γεννήσει υἱόν σοι, καὶ καλέσεις τὸ ὄνομα αὐτοῦ Ἰωάννην·
- TH: แต่ทูตสวรรค์กล่าวแก่ท่านว่า «อย่ากลัวเลย เศคาริยาห์ เพราะคำอธิษฐานของท่านได้รับการทรงสดับแล้ว เอลีซาเบธภรรยาของท่านจะให้กำเนิดบุตรชายแก่ท่าน และท่านจงตั้งชื่อเขาว่ายอห์น
- TH-summary: ชื่อ «ยอห์น» (โยฮานาน ในภาษาฮีบรู) แปลว่า «พระยาห์เวห์ทรงโปรดปราน» ชื่อนี้ไม่ได้อยู่ในครอบครัวของเศคาริยาห์ (ข้อ 61) แต่พระเจ้าทรงกำหนดชื่อนี้ล่วงหน้า — เหมือนกับที่ทรงกำหนดชื่อของอิชมาเอล (ปฐก 16:11), อิสอัค (ปฐก 17:19), และพระเยซู (ข้อ 31) เป็นสัญญาณว่าบุคคลนี้เกิดโดยพระประสงค์ของพระเจ้าเป็นพิเศษ
- Key decisions:
  - Μὴ φοβοῦ → อย่ากลัวเลย — Standard angelic-reassurance formula (cf. MAT 1:20, 28:5, LUK 1:30, 2:10). Per uW figs-imperative: not just command but encouragement. Thai อย่ากลัวเลย consistent across angelic greetings in the chapter
  - εἰσηκούσθη ἡ δέησίς σου → คำอธิษฐานของท่านได้รับการทรงสดับแล้ว — Per uW figs-activepassive: divine passive = 'God has heard.' Per uW figs-idiom: 'heard' = 'granted.' δέησις = petition/supplication (more specific than προσευχή). Thai ได้รับการทรงสดับ (royal passive 'has been heard...
  - γεννήσει υἱόν σοι → จะให้กำเนิดบุตรชายแก่ท่าน — γεννάω future of 'bear / give birth.' Thai ให้กำเนิด standard
  - καλέσεις τὸ ὄνομα αὐτοῦ Ἰωάννην → ท่านจงตั้งชื่อเขาว่ายอห์น — Per uW figs-declarative/figs-idiom: future as command 'you shall name him.' 'Call his name' = 'give name.' Ἰωάννης → ยอห์น standard Thai Christian transliteration. From Hebrew יוֹחָנָן = 'YHWH has shown favor / has ...
- Notes: NAME-THEOLOGY: Ἰωάννης (from Hebrew יוֹחָנָן Yohanan) = 'YHWH is gracious / YHWH has shown favor.' The name is prophetically given by the angel before the child's conception — a biblical marker of exceptional divine purpose (cf. Ishmael Gen 16:11, Isaac Gen 17:19, Solomon 2 Sam 12:25, Josiah 1 Kgs 13:2, Cyrus Isa 45:1; Jesus LUK 1:31). The 'pr...

**Luke 1:14**
- GR: καὶ ἔσται χαρά σοι καὶ ἀγαλλίασις, καὶ πολλοὶ ἐπὶ τῇ γενέσει αὐτοῦ χαρήσονται·
- TH: ท่านจะมีความชื่นชมและความยินดีอย่างยิ่ง และหลายคนจะชื่นชมยินดีเนื่องในการกำเนิดของเขา
- Key decisions:
  - χαρά...καὶ ἀγαλλίασις → ความชื่นชมและความยินดีอย่างยิ่ง — Per uW figs-doublet: χαρά ('joy') + ἀγαλλίασις ('exultation/great gladness') — Hebraic-parallelism doublet. Rather than collapsing (per uW suggestion), preserve as doublet in Thai to reflect the LXX-style parallelis...
  - ἐπὶ τῇ γενέσει αὐτοῦ χαρήσονται → จะชื่นชมยินดีเนื่องในการกำเนิดของเขา — Per uW grammar-connect-logic-result: ἐπί + dat = 'because of.' γένεσις = 'birth/origin.' Thai เนื่องใน...กำเนิด causal-birth phrasing
- Notes: The triple use of χαρά/χαίρω words in this verse (χαρά, ἀγαλλίασις, χαρήσονται) emphasizes the joyful nature of this birth — a thematic motif carried through Luke's infancy narrative (cf. 1:28 χαῖρε, 1:44 ἀγαλλίασις, 1:47 ἠγαλλίασεν, 1:58 συνέχαιρον, 2:10 χαράν μεγάλην, 2:13-14). The joy-motif culminates in Mary's Magnificat. OT resonance: the...

**Luke 1:15**
- GR: ἔσται γὰρ μέγας ἐνώπιον τοῦ κυρίου, καὶ οἶνον καὶ σίκερα οὐ μὴ πίῃ, καὶ πνεύματος ἁγίου πλησθήσεται ἔτι ἐκ κοιλίας μητρὸς αὐτοῦ,
- TH: เพราะเขาจะเป็นผู้ยิ่งใหญ่ในสายพระเนตรขององค์พระผู้เป็นเจ้า เขาจะไม่ดื่มเหล้าองุ่นหรือสุราเมรัยใดๆ เลย และจะเต็มเปี่ยมด้วยพระวิญญาณบริสุทธิ์ตั้งแต่อยู่ในครรภ์มารดา
- TH-summary: คำสั่งไม่ให้ดื่มเหล้าองุ่นและสุราเป็นการผูกพันแบบ «คำปฏิญาณของพวกนาศีร์» (กันดารวิถี 6:1-8) เหมือนกับแซมสัน (ผู้วินิจฉัย 13:4-7, 14) และซามูเอล (1 ซามูเอล 1:11) ยอห์นเป็นผู้ถวายตัวแด่พระเจ้าโดยสมบูรณ์ตั้งแต่ครรภ์ — เป็นผู้เผยพระวจนะรุ่นสุดท้ายของยุคเก่าและผู้บุกเบิกพระเมสสิยาห์
- Key decisions:
  - μέγας ἐνώπιον τοῦ κυρίου → ผู้ยิ่งใหญ่ในสายพระเนตรขององค์พระผู้เป็นเจ้า — Per uW figs-metaphor: 'before the Lord' = 'in God's estimation.' Thai ในสายพระเนตร (royal-register, 'in the eye-sight of') preserves divine-judgment sense. μέγας 'great' — anticipates Jesus's own assessment (LUK 7:2...
  - οἶνον καὶ σίκερα οὐ μὴ πίῃ → เขาจะไม่ดื่มเหล้าองุ่นหรือสุราเมรัยใดๆ เลย — HAPAX: σίκερα = 'strong drink / fermented liquor' (Hebrew loanword שֵׁכָר). Per uW figs-doublenegatives: οὐ μὴ + subj. = 'never.' LXX-Nazirite echo (NUM 6:3 LXX οἶνον καὶ σίκερα). Thai เหล้าองุ่น (wine) + สุราเมรัย ...
  - πνεύματος ἁγίου πλησθήσεται → เต็มเปี่ยมด้วยพระวิญญาณบริสุทธิ์ — Per uW figs-activepassive: 'Holy Spirit will fill him.' Per uW figs-metaphor: vessel-image. Thai เต็มเปี่ยมด้วย natural. πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์ established glossary
  - ἔτι ἐκ κοιλίας μητρὸς αὐτοῦ → ตั้งแต่อยู่ในครรภ์มารดา — ἔτι = 'yet/already/even.' ἐκ κοιλίας = 'from the womb.' Prenatal filling with the Spirit — cf. Jer 1:5. Thai ตั้งแต่อยู่ในครรภ์มารดา natural
- Notes: HAPAX: σίκερα ('strong drink'), a Hebraic loanword from שֵׁכָר šēkār used in LXX Numbers 6:3 (Nazirite regulations) and Judges 13:4, 7, 14 (angel to Manoah's wife about Samson). The phrase οἶνον καὶ σίκερα directly echoes the Nazirite-vow stipulations and specifically the Samson-birth-announcement (Judg 13:4 LXX is virtually identical). John i...

**Luke 1:16**
- GR: καὶ πολλοὺς τῶν υἱῶν Ἰσραὴλ ἐπιστρέψει ἐπὶ κύριον τὸν θεὸν αὐτῶν·
- TH: และเขาจะทำให้ชาวอิสราเอลจำนวนมากหันกลับมาหาองค์พระผู้เป็นเจ้าพระเจ้าของพวกเขา
- Key decisions:
  - πολλοὺς τῶν υἱῶν Ἰσραήλ → ชาวอิสราเอลจำนวนมาก — Per uW figs-metaphor: 'sons of Israel' = descendants/people of Israel. Thai ชาวอิสราเอล ('people of Israel') natural — 'sons' would be jarringly literal and exclude women
  - ἐπιστρέψει → จะทำให้...หันกลับมา — Per uW figs-metaphor: ἐπιστρέφω active 'turn back/return' = cause to repent. Thai ทำให้...หันกลับ captures causative-active sense. Note: same verb appears in v.17 — key-term consistency preserved
  - ἐπὶ κύριον τὸν θεὸν αὐτῶν → มาหาองค์พระผู้เป็นเจ้าพระเจ้าของพวกเขา — κύριον τὸν θεόν = YHWH-Elohim formula. Thai องค์พระผู้เป็นเจ้าพระเจ้า preserves dual divine-name formula (appositional). Common Deuteronomic formula
- Notes: John's mission summarized: prophetic-repentance-ministry. The ἐπιστρέφω-to-God language is classic Deuteronomic-prophetic vocabulary (Deut 30:2, 1 Kgs 8:47-48, Hos 3:5, Mal 3:7). The repentance-mission-before-the-Lord-comes theme anticipates the Elijah-typology explicitly stated in v.17, and links back to Malachi 3:1, 4:5-6. ADDED TO NT_OT_CIT...

**Luke 1:17**
- GR: καὶ αὐτὸς προελεύσεται ἐνώπιον αὐτοῦ ἐν πνεύματι καὶ δυνάμει Ἠλίου, ἐπιστρέψαι καρδίας πατέρων ἐπὶ τέκνα καὶ ἀπειθεῖς ἐν φρονήσει δικαίων, ἑτοιμάσαι κυρίῳ λαὸν κατεσκευασμένον.
- TH: เขาเองจะไปล่วงหน้าเฉพาะพระพักตร์พระองค์ด้วยพระวิญญาณและฤทธิ์เดชของเอลียาห์ เพื่อให้ใจของบรรพบุรุษหันกลับมาหาบุตรหลาน และให้คนที่ไม่เชื่อฟังหันกลับมาหาปัญญาของคนชอบธรรม เพื่อเตรียมประชากรกลุ่มหนึ่งให้พร้อมสรรพสำหรับองค์พระผู้เป็นเจ้า»
- TH-summary: ทูตสวรรค์อ้างถึงคำพยากรณ์ของมาลาคี 4:5-6 โดยตรง — «เราจะส่งเอลียาห์ผู้เผยพระวจนะมาก่อน...เขาจะทำให้ใจบิดาหันกลับมาหาบุตรของเขา» พระเจ้าส่งยอห์นในฐานะ «เอลียาห์ผู้จะมา» (เทียบ มัทธิว 17:12) เพื่อเตรียมประชากรให้พร้อมรับพระเมสสิยาห์
- Key decisions:
  - προελεύσεται ἐνώπιον αὐτοῦ → จะไปล่วงหน้าเฉพาะพระพักตร์พระองค์ — Per uW figs-idiom: 'go before' = announce/prepare the way for one who comes behind. Thai ไปล่วงหน้าเฉพาะพระพักตร์ captures the herald-before-king image. αὐτοῦ pronoun: 'him' = God (or ambiguously, the coming Messiah...
  - ἐν πνεύματι καὶ δυνάμει Ἠλίου → ด้วยพระวิญญาณและฤทธิ์เดชของเอลียาห์ — Per uW figs-doublet / figs-hendiadys: 'spirit and power' may be hendiadys ('powerful spirit') but I preserve as doublet. Refers to Malachi's Elijah-return prophecy (Mal 4:5-6). Ἠλίας → เอลียาห์ established from MAT ...
  - ἐπιστρέψαι καρδίας πατέρων ἐπὶ τέκνα → เพื่อให้ใจของบรรพบุรุษหันกลับมาหาบุตรหลาน — DIRECT QUOTATION from MAL 4:6 LXX (ἀποκαταστήσει καρδίαν πατρὸς πρὸς υἱόν — Luke's wording adapts but preserves). Per uW figs-personification/figs-synecdoche: hearts as decisive-attitude. Thai ใจ...หันกลับมาหา prese...
  - ἀπειθεῖς ἐν φρονήσει δικαίων → ให้คนที่ไม่เชื่อฟังหันกลับมาหาปัญญาของคนชอบธรรม — Per uW figs-nominaladj: adjectives used as substantives (the-disobedient, the-righteous). φρόνησις = practical wisdom. Per uW figs-explicit: 'wisdom of the righteous' = God's way. Thai คนที่ไม่เชื่อฟัง + ปัญญาของคนช...
  - ἑτοιμάσαι κυρίῳ λαὸν κατεσκευασμένον → เพื่อเตรียมประชากรกลุ่มหนึ่งให้พร้อมสรรพสำหรับองค์พระผู้เป็นเจ้า — Per uW figs-explicit: prepared-for-what = to believe the Messianic message. ἑτοιμάσαι + κατεσκευασμένον = infinitive + perf.pass.ptc. Double 'ready/prepared' intensifies. Thai เตรียม...ให้พร้อมสรรพ preserves the dou...
- Notes: MAJOR OT CITATION: this verse densely quotes MALACHI 3:1 (ὁ ἀποστελλόμενος ἄγγελός μου πρὸ προσώπου μου — 'my messenger sent before my face') and especially MALACHI 4:5-6 (ἀποκαταστήσει καρδίαν πατρὸς πρὸς υἱόν — 'he will turn the heart of the father to the son'). Luke's Greek ἐπιστρέψαι καρδίας πατέρων ἐπὶ τέκνα is a near-direct quotation ada...

**Luke 1:18**
- GR: καὶ εἶπεν Ζαχαρίας πρὸς τὸν ἄγγελον· Κατὰ τί γνώσομαι τοῦτο; ἐγὼ γάρ εἰμι πρεσβύτης καὶ ἡ γυνή μου προβεβηκυῖα ἐν ταῖς ἡμέραις αὐτῆς.
- TH: เศคาริยาห์กล่าวแก่ทูตสวรรค์ว่า «ข้าพเจ้าจะรู้ได้อย่างไรว่าเรื่องนี้เป็นจริง? เพราะข้าพเจ้าเองเป็นคนชรา และภรรยาของข้าพเจ้าก็อายุล่วงเข้าสู่วัยชราแล้ว»
- TH-summary: เศคาริยาห์ขอหมายสำคัญเพื่อเป็นหลักฐาน — คล้ายกับอับราฮัมใน ปฐมกาล 15:8 («ข้าพระองค์จะทราบได้อย่างไร?») แต่ต่างกันตรงที่อับราฮัมเชื่อแล้วเพียงขอการยืนยัน ส่วนเศคาริยาห์ดูเหมือนจะสงสัย ทูตสวรรค์จึงตอบเปรียบเทียบกับการตอบสนองของมารีย์ในข้อ 34 ซึ่งเป็นคำถามแบบ «ไว้วางใจแต่ไม่เข้าใจ» ต่างจากเศคาริยาห์ที่ «ไม่เชื่อ»
- Key decisions:
  - Κατὰ τί γνώσομαι τοῦτο → ข้าพเจ้าจะรู้ได้อย่างไรว่าเรื่องนี้เป็นจริง — Per uW figs-explicit: asking for a sign as proof. κατὰ τί = 'according to what (criterion)?' = 'how?' Thai จะรู้ได้อย่างไรว่าเรื่องนี้เป็นจริง preserves the sign-request. Echoes Abraham's κατὰ τί γνώσομαι in Gen 15:8 LXX
  - ἐγὼ γάρ εἰμι πρεσβύτης → เพราะข้าพเจ้าเองเป็นคนชรา — πρεσβύτης = 'old man.' Per uW grammar-connect-logic-result. Emphatic ἐγώ — 'I myself (and not a younger man)...' Thai ข้าพเจ้าเองเป็นคนชรา preserves emphasis. Human-to-divine register: ข้าพเจ้า humble first-person b...
  - ἡ γυνή μου προβεβηκυῖα ἐν ταῖς ἡμέραις αὐτῆς → ภรรยาของข้าพเจ้าก็อายุล่วงเข้าสู่วัยชราแล้ว — Same Hebraic idiom as v.7 (προβεβηκώς + ἡμέραι). Preserve consistent rendering — see v.7 rationale
- Notes: Zechariah's question parallels Abraham's (Gen 15:8 LXX Κύριε δέσποτα, κατὰ τί γνώσομαι ὅτι κληρονομήσω αὐτήν) but the angelic response differs sharply. Abraham's question was answered with covenant ratification; Zechariah's is rebuked with temporary muteness (v.20). The contrast with Mary's question in v.34 (πῶς ἔσται τοῦτο) is the more direct...

**Luke 1:19**
- GR: καὶ ἀποκριθεὶς ὁ ἄγγελος εἶπεν αὐτῷ· Ἐγώ εἰμι Γαβριὴλ ὁ παρεστηκὼς ἐνώπιον τοῦ θεοῦ, καὶ ἀπεστάλην λαλῆσαι πρὸς σὲ καὶ εὐαγγελίσασθαί σοι ταῦτα·
- TH: ทูตสวรรค์ตอบท่านว่า «เราคือกาเบรียล ผู้ยืนอยู่เฉพาะพระพักตร์พระเจ้า และถูกส่งมาเพื่อพูดกับท่านและประกาศข่าวประเสริฐนี้แก่ท่าน
- TH-summary: «กาเบรียล» (ในภาษาฮีบรู กัฟริเอล แปลว่า «บุรุษของพระเจ้า» หรือ «พระเจ้าคือกำลังของข้าพเจ้า») เป็นทูตสวรรค์องค์เดียวกับที่มาหาดาเนียล (ดาเนียล 8:16, 9:21) เป็นทูตสวรรค์ระดับสูงที่อยู่ใกล้ชิดพระเจ้า การที่กาเบรียลเองมาแจ้งข่าวนี้แสดงถึงความสำคัญของเหตุการณ์นี้
- Key decisions:
  - ἀποκριθεὶς...εἶπεν → ตอบท่านว่า — Per uW figs-hendiadys: 'answering said' = responded. Thai ตอบ...ว่า natural
  - Ἐγώ εἰμι Γαβριὴλ → เราคือกาเบรียล — Emphatic self-identification. Γαβριήλ → กาเบรียล standard Thai Christian transliteration (from Hebrew גַּבְרִיאֵל 'man/strength of God'). Angelic self-reference = เรา (divine-dignified first-person per RULES.md §3 f...
  - ὁ παρεστηκὼς ἐνώπιον τοῦ θεοῦ → ผู้ยืนอยู่เฉพาะพระพักตร์พระเจ้า — Per uW figs-metaphor: 'stand before' = 'serve personally.' παρίστημι perfect ptc. = 'have-been-and-still-standing' — continuous service. Thai ยืนอยู่เฉพาะพระพักตร์พระเจ้า preserves the throne-room-service image. Per...
  - ἀπεστάλην → ถูกส่งมา — Per uW figs-activepassive: God sent. Divine passive. Thai ถูกส่งมา keeps passive — angel doesn't self-send, God commissions
  - εὐαγγελίσασθαί σοι ταῦτα → ประกาศข่าวประเสริฐนี้แก่ท่าน — εὐαγγελίζω = proclaim good news. εὐαγγέλιον → ข่าวประเสริฐ is established non-negotiable glossary (RULES.md §4). Verb form preserves glossary rendering. Notable first NT occurrence of εὐαγγελίζομαι — the ANGEL annou...
- Notes: FIRST NT USE of εὐαγγελίζομαι — Gabriel announces 'gospel' concerning John-the-forerunner before Jesus's own gospel begins. Gabriel is named in OT only at Dan 8:16 and 9:21 — both in contexts of end-time revelation to Daniel. By name-dropping Gabriel, Luke places this announcement in the same eschatological-revelation register as Daniel's visi...

**Luke 1:20**
- GR: καὶ ἰδοὺ ἔσῃ σιωπῶν καὶ μὴ δυνάμενος λαλῆσαι ἄχρι ἧς ἡμέρας γένηται ταῦτα, ἀνθ᾽ ὧν οὐκ ἐπίστευσας τοῖς λόγοις μου, οἵτινες πληρωθήσονται εἰς τὸν καιρὸν αὐτῶν.
- TH: และดูเถิด ท่านจะเป็นใบ้และพูดไม่ได้จนถึงวันที่เหตุการณ์เหล่านี้จะเกิดขึ้น เพราะท่านไม่เชื่อถ้อยคำของเรา ซึ่งถ้อยคำนั้นจะสำเร็จในเวลาของมัน»
- Key decisions:
  - καὶ ἰδοὺ → และดูเถิด — Attention-marker per uW figs-metaphor. Thai ดูเถิด standard across the chapter and established across MAT translations
  - ἔσῃ σιωπῶν καὶ μὴ δυνάμενος λαλῆσαι → จะเป็นใบ้และพูดไม่ได้ — Per uW figs-doublet: 'silent and unable to speak' — doublet for emphasis. Thai เป็นใบ้ + พูดไม่ได้ preserves both phrases naturally. Per uW figs-explicit: divine judgment
  - ἀνθ᾽ ὧν οὐκ ἐπίστευσας τοῖς λόγοις μου → เพราะท่านไม่เชื่อถ้อยคำของเรา — ἀνθ᾽ ὧν = 'because / in return for which.' Per uW figs-metonymy: 'words' = message. Thai ถ้อยคำ preserves specificity of angel's words. μου 'my' — Gabriel's authoritative words, standing-in for God's
  - οἵτινες πληρωθήσονται εἰς τὸν καιρὸν αὐτῶν → ซึ่งถ้อยคำนั้นจะสำเร็จในเวลาของมัน — Per uW figs-activepassive: will happen. Per uW figs-idiom: 'at their time' = appointed/proper time. Thai จะสำเร็จในเวลาของมัน preserves the divine-timing sense. πληρόω = fulfill (same root as v.1 πεπληροφορημένων — ...
- Notes: Zechariah's punishment is also a sign — he can serve as the 'sign' for the community (v.22-23). The muteness endures until John is named (v.63-64), forming a literary-thematic bracket around the John-birth sequence. Theologically: a priest whose prayer was answered but who could not believe the answer loses his voice — his primary liturgical f...

**Luke 1:21**
- GR: Καὶ ἦν ὁ λαὸς προσδοκῶν τὸν Ζαχαρίαν, καὶ ἐθαύμαζον ἐν τῷ χρονίζειν ἐν τῷ ναῷ αὐτόν.
- TH: ในขณะนั้น ประชาชนกำลังคอยเศคาริยาห์อยู่ และประหลาดใจที่ท่านล่าช้าอยู่ในพระวิหาร
- Key decisions:
  - Καὶ → ในขณะนั้น — Per uW grammar-connect-time-simultaneous: καί here marks scene-shift from inside sanctuary to outside courtyard — simultaneous action. Thai ในขณะนั้น preserves temporal simultaneity
  - προσδοκῶν → กำลังคอย — προσδοκάω = 'wait for / expect.' Ongoing/durative. Thai กำลังคอย natural
  - ἐθαύμαζον ἐν τῷ χρονίζειν → ประหลาดใจที่ท่านล่าช้า — θαυμάζω = 'marvel / wonder.' χρονίζω = 'delay / linger.' The incense-offering itself was normally brief (~a few minutes); extended time inside would cause concern (a priest defiled might die inside the sanctuary — c...
- Notes: The crowd's perplexity has a specific religio-cultural basis: priests were expected to complete the incense offering briefly and return with the benediction (Num 6:22-27). An extended delay could mean ritual defilement or divine-strike (cf. Lev 16:13 for Yom Kippur, where the high priest's lingering would fear mortal judgment). The narrative r...

**Luke 1:22**
- GR: ἐξελθὼν δὲ οὐκ ἐδύνατο λαλῆσαι αὐτοῖς, καὶ ἐπέγνωσαν ὅτι ὀπτασίαν ἑώρακεν ἐν τῷ ναῷ· καὶ αὐτὸς ἦν διανεύων αὐτοῖς, καὶ διέμενεν κωφός.
- TH: เมื่อท่านออกมา ท่านไม่สามารถพูดกับพวกเขาได้ และพวกเขาตระหนักว่าท่านได้เห็นนิมิตในพระวิหาร ท่านทำเพียงใบ้ไปมาแก่พวกเขา แต่ยังคงพูดไม่ได้
- Key decisions:
  - ἐπέγνωσαν ὅτι ὀπτασίαν ἑώρακεν → ตระหนักว่าท่านได้เห็นนิมิต — Per uW figs-explicit: people thought it was a vision, though actually an angelic presence. ὀπτασία = 'vision / appearance' (more specific than ὅραμα). Thai นิมิต standard Christian Thai term for visionary experience
  - αὐτὸς ἦν διανεύων αὐτοῖς → ท่านทำเพียงใบ้ไปมาแก่พวกเขา — HAPAX: διανεύω = 'nod/gesture through signs' (διά 'through' + νεύω 'nod'). Thai ทำใบ้ ('make dumb signs') preserves the hand-gesture-communication sense. Periphrastic imperfect ἦν...διανεύων = ongoing-continued gesturing
  - διέμενεν κωφός → ยังคงพูดไม่ได้ — διαμένω = 'remain through (time).' κωφός = 'deaf/mute' (from muzzled-dull sense). Context clearly means 'mute' here (not deaf, though some commentators debate this — uW notes the ambiguity). Thai ยังคงพูดไม่ได้ keep...
- Notes: NT HAPAX: διανεύω (only here in NT). The crowd correctly infers a divine encounter from Zechariah's post-incense muteness — priests normally emerged with blessing (Num 6:22-27); Zechariah emerges voiceless. The ambiguity of κωφός (deaf OR mute) is discussed by uW: v.62 'they made signs to his father' might suggest he was both deaf and mute, bu...

**Luke 1:23**
- GR: καὶ ἐγένετο ὡς ἐπλήσθησαν αἱ ἡμέραι τῆς λειτουργίας αὐτοῦ, ἀπῆλθεν εἰς τὸν οἶκον αὐτοῦ.
- TH: เมื่อครบกำหนดวันปฏิบัติหน้าที่ของท่านแล้ว ท่านก็กลับไปยังบ้านของตน
- Key decisions:
  - καὶ ἐγένετο ὡς ἐπλήσθησαν αἱ ἡμέραι → เมื่อครบกำหนดวัน — Per uW writing-newevent: narrative-shift marker. πληρόω passive of 'days being fulfilled/completed' — Hebraic idiom. Thai ครบกำหนดวัน natural
  - τῆς λειτουργίας αὐτοῦ → ปฏิบัติหน้าที่ — λειτουργία = 'public service / priestly liturgical service' (from λαός+ἔργον 'people-work'). Source of 'liturgy.' Here = Zechariah's priestly-week service. Thai ปฏิบัติหน้าที่ contextually adequate; the priestly sen...
  - ἀπῆλθεν εἰς τὸν οἶκον αὐτοῦ → ท่านก็กลับไปยังบ้านของตน — Per uW figs-explicit: Zechariah's home was in the hill country of Judah (v.39-40), not Jerusalem. Thai กลับไปยังบ้านของตน natural
- Notes: The priestly week ended (Sabbath-to-Sabbath). Zechariah's home was in the 'hill country of Judah' per v.39-40 — likely a priestly village outside Jerusalem. Mute throughout his return journey, he arrives home both dumbfounded and carrying an angelic-announcement he cannot verbally share with his wife.

**Luke 1:24**
- GR: Μετὰ δὲ ταύτας τὰς ἡμέρας συνέλαβεν Ἐλισάβετ ἡ γυνὴ αὐτοῦ· καὶ περιέκρυβεν ἑαυτὴν μῆνας πέντε, λέγουσα
- TH: หลังจากวันเหล่านั้น เอลีซาเบธภรรยาของท่านก็ตั้งครรภ์ และปลีกตัวอยู่อย่างเงียบๆ เป็นเวลาห้าเดือน นางกล่าวว่า
- TH-summary: เอลีซาเบธปลีกตัวเงียบๆ ห้าเดือน น่าจะด้วยเหตุผลหลายประการ: (1) รอให้ตั้งครรภ์ชัดเจนก่อนประกาศ เพื่อหลีกเลี่ยงการหัวเราะเยาะจากเพื่อนบ้าน (2) ใช้เวลาอยู่กับพระเจ้าและขอบพระคุณ (3) ปกป้องตัวเองจากการดูแคลนว่าเป็นหญิงหมัน
- Key decisions:
  - Μετὰ δὲ ταύτας τὰς ἡμέρας → หลังจากวันเหล่านั้น — Per uW figs-idiom: 'days' = time-period (Zechariah's temple service). Per uW grammar-connect-time-sequential. Thai หลังจากวันเหล่านั้น natural
  - συνέλαβεν → ก็ตั้งครรภ์ — συλλαμβάνω = 'conceive / take-together' (womb-and-seed). Thai ตั้งครรภ์ natural
  - περιέκρυβεν ἑαυτὴν → ปลีกตัวอยู่อย่างเงียบๆ — HAPAX: περικρύβω = 'hide around / conceal completely' (περι- 'around' + κρύβω 'hide'). Per uW figs-explicit: she remained in her house. Thai ปลีกตัวอยู่อย่างเงียบๆ captures 'withdrew + hidden' without implying stric...
- Notes: NT HAPAX: περικρύβω ('seclude / hide oneself'). The five-month seclusion is not well-explained by Luke. Possibilities: (a) ancient pregnancies were often hidden until visibly evident (~5 months) to avoid 'false pregnancy' gossip; (b) Elizabeth's public shame of barrenness (v.25 ὄνειδος) motivated her to wait until the pregnancy was physically ...

**Luke 1:25**
- GR: ὅτι Οὕτως μοι πεποίηκεν κύριος ἐν ἡμέραις αἷς ἐπεῖδεν ἀφελεῖν ὄνειδός μου ἐν ἀνθρώποις.
- TH: «องค์พระผู้เป็นเจ้าทรงกระทำเช่นนี้แก่ข้าพเจ้าในวันเหล่านี้ ที่พระองค์ทอดพระเนตรมาหาข้าพเจ้าเพื่อขจัดความอับอายของข้าพเจ้าในหมู่มนุษย์»
- TH-summary: ถ้อยคำของเอลีซาเบธสะท้อนคำของราเชลใน ปฐมกาล 30:23 เมื่อนางให้กำเนิดโยเซฟว่า «พระเจ้าทรงเอาความอับอายของข้าพเจ้าไปแล้ว» ในสังคมยิวโบราณ การเป็นหมันถือเป็นความอับอายและคำสาป (เทียบ 1 ซามูเอล 1:6-7 ฮันนาห์) ลูกาจงใจให้ถ้อยคำนี้สะท้อนพระคัมภีร์เดิมเพื่อแสดงว่าเหตุการณ์นี้เป็นความต่อเนื่องของพระราชกิจของพระเจ้า
- Key decisions:
  - Οὕτως μοι πεποίηκεν κύριος → องค์พระผู้เป็นเจ้าทรงกระทำเช่นนี้แก่ข้าพเจ้า — Per uW figs-exclamations/figs-explicit: joyful exclamation referring to the pregnancy. Thai ทรงกระทำเช่นนี้ (royal verb per §3 for divine subject). κύριος = YHWH → องค์พระผู้เป็นเจ้า. Human-to-God humble first-perso...
  - ἐπεῖδεν → พระองค์ทอดพระเนตรมาหาข้าพเจ้า — Per uW figs-idiom: 'looked upon' = 'shown regard for / treated kindly.' ἐπί + ὁράω = 'look attentively upon.' Thai ทอดพระเนตร royal-register for divine seeing per §3
  - ἀφελεῖν ὄνειδός μου ἐν ἀνθρώποις → ขจัดความอับอายของข้าพเจ้าในหมู่มนุษย์ — HAPAX: ὄνειδος = 'reproach / disgrace' (only here in NT, though cognate ὀνειδίζω more frequent). Per uW figs-explicit: barrenness was socially shameful in Jewish-Second-Temple culture. Thai ความอับอาย natural. ἐν ἀν...
- Notes: NT HAPAX: ὄνειδος ('reproach'). DIRECT LXX ECHO: Elizabeth's ἀφελεῖν ὄνειδός μου directly quotes Gen 30:23 LXX, where Rachel says ἀφεῖλεν ὁ θεός μου τὸ ὄνειδος at the birth of Joseph. This places Elizabeth typologically as another matriarch-whose-barrenness-God-reversed. The plural ἐν ἀνθρώποις ('among people / in public') acknowledges the soc...

**Luke 1:26**
- GR: Ἐν δὲ τῷ μηνὶ τῷ ἕκτῳ ἀπεστάλη ὁ ἄγγελος Γαβριὴλ ἀπὸ τοῦ θεοῦ εἰς πόλιν τῆς Γαλιλαίας ᾗ ὄνομα Ναζαρὲθ
- TH: ในเดือนที่หกนั้น พระเจ้าทรงส่งทูตสวรรค์กาเบรียลไปยังเมืองหนึ่งในแคว้นกาลิลีชื่อนาซาเร็ธ
- TH-summary: «เดือนที่หก» คือเดือนที่หกของการตั้งครรภ์ของเอลีซาเบธ ไม่ใช่เดือนที่หกของปี กาเบรียล — ทูตสวรรค์องค์เดียวกับที่ไปหาเศคาริยาห์ — ถูกส่งไปอีกครั้ง แต่คราวนี้ไปยังหญิงสาวพรหมจารีในชนบทของกาลิลี แทนที่จะเป็นปุโรหิตในพระวิหารเยรูซาเล็ม นาซาเร็ธเป็นหมู่บ้านเล็กๆ ไม่มีชื่อเสียง (ยอห์น 1:46 «สิ่งดีอะไรจะออกจากนาซาเร็ธได้?»)
- Key decisions:
  - Ἐν...τῷ μηνὶ τῷ ἕκτῳ → ในเดือนที่หก — Per uW figs-explicit: sixth month of Elizabeth's pregnancy, not calendar sixth month. Per uW translate-ordinal: Thai เดือนที่หก keeps ordinal (Thai uses ordinals naturally). Context links back to five-month seclusio...
  - ἀπεστάλη ὁ ἄγγελος Γαβριήλ ἀπὸ τοῦ θεοῦ → พระเจ้าทรงส่งทูตสวรรค์กาเบรียล — Per uW figs-activepassive: I render active with 'God sent' to avoid awkward divine-passive in Thai. Royal verb ทรงส่ง per §3 for God as subject. Γαβριήλ → กาเบรียล — same angel as v.19, reinforcing parallelism betwe...
  - εἰς πόλιν τῆς Γαλιλαίας ᾗ ὄνομα Ναζαρέθ → ไปยังเมืองหนึ่งในแคว้นกาลิลีชื่อนาซาเร็ธ — Γαλιλαία → แคว้นกาลิลี established glossary. Ναζαρέθ → นาซาเร็ธ established from MAT 2:23
- Notes: Narrative parallelism with v.11-19 is deliberate: both annunciations are made by Gabriel, both contain 'do not fear,' both announce miraculous births, both identify the child's name and future role, both elicit a question — but the responses diverge (Zechariah's doubt → muteness; Mary's submission → blessing). The CONTRAST is the point: old pr...

**Luke 1:27**
- GR: πρὸς παρθένον ἐμνηστευμένην ἀνδρὶ ᾧ ὄνομα Ἰωσὴφ ἐξ οἴκου Δαυὶδ, καὶ τὸ ὄνομα τῆς παρθένου Μαριάμ.
- TH: ไปยังหญิงพรหมจารีคนหนึ่งผู้ได้หมั้นอยู่กับชายชื่อโยเซฟ ซึ่งเป็นเชื้อสายของดาวิด และหญิงพรหมจารีนั้นชื่อมารีย์
- Key decisions:
  - παρθένον → หญิงพรหมจารี — παρθένος → หญิงพรหมจารี established from MAT 1:23 (Isa 7:14 citation). Thai term literally 'woman of pure-celibate-life' — used in Thai Christian tradition for virgin. Emphatic repetition at v.27 end
  - ἐμνηστευμένην ἀνδρὶ ᾧ ὄνομα Ἰωσήφ → ได้หมั้นอยู่กับชายชื่อโยเซฟ — μνηστεύω perfect passive ptc. = 'betrothed / pledged.' Established glossary from MAT 1:18. Jewish betrothal = legally binding first stage of marriage (12-month wait); could only be dissolved by divorce. Not mere eng...
  - ἐξ οἴκου Δαυίδ → เป็นเชื้อสายของดาวิด — Per uW figs-metaphor/writing-background: 'house of David' = Davidic-lineage-descent. Per uW figs-explicit: crucial for Jesus's claim to Davidic messianic throne through adoptive-paternity (MAT 1, LUK 3 genealogies)....
  - τὸ ὄνομα τῆς παρθένου Μαριάμ → หญิงพรหมจารีนั้นชื่อมารีย์ — Μαριάμ (Hebraic form) vs Μαρία (Hellenized) — Luke varies freely. → มารีย์ established glossary. The repeat of παρθένος is significant: 'the virgin's name was Mary' places emphasis on her virginal status (key theolo...
- Notes: The emphatic repetition of παρθένος (twice in one verse) is striking — Luke is setting up the virginal-conception theme that dominates vv.34-35. Betrothal (ἐρρωσίωσις / κιδּוּשִׁין) in Second Temple Judaism was a legally-binding pre-marital stage, typically 12 months between kiddushin (betrothal, at which bride-price was paid) and nissu'in (co...

**Luke 1:28**
- GR: καὶ εἰσελθὼν πρὸς αὐτὴν εἶπεν· Χαῖρε, κεχαριτωμένη, ὁ κύριος μετὰ σοῦ.
- TH: ทูตสวรรค์เข้ามาหานางและกล่าวว่า «จงยินดีเถิด หญิงผู้ได้รับพระคุณอย่างยิ่ง องค์พระผู้เป็นเจ้าทรงสถิตกับท่าน»
- TH-summary: คำทักทาย «จงยินดีเถิด» (ไคเร) เป็นการเล่นคำกับคำว่า «ผู้ได้รับพระคุณ» (เกฮาริโตเมเน) ที่มาจากรากศัพท์เดียวกันคือ «คาริส» (พระคุณ) และสะท้อนความปิติยินดีที่เป็นธีมของลูกา 1-2 คำว่า «องค์พระผู้เป็นเจ้าทรงสถิตกับท่าน» เป็นคำอวยพรจากพระคัมภีร์เดิม (รูธ 2:4, ผู้วินิจฉัย 6:12 ต่อกิเดโอน) บ่งชี้ว่ามารีย์ถูกเรียกให้ทำภารกิจพิเศษของพระเจ้า
- Key decisions:
  - Χαῖρε → จงยินดีเถิด — Per uW figs-idiom: standard Greek greeting ('Greetings!') but literally 'rejoice!' The dual sense is intentional — a joyful announcement-greeting. Consistent with MAT 28:9 glossary rendering. The χάρις-χαίρω wordpla...
  - κεχαριτωμένη → หญิงผู้ได้รับพระคุณอย่างยิ่ง — χαριτόω perf.pass.ptc. fem. = 'graced / favored with grace.' Rare in NT (only here and Eph 1:6). Perfect tense = 'have-been-and-continue-to-be graced.' Thai ผู้ได้รับพระคุณอย่างยิ่ง preserves the perfect-aspect-with...
  - ὁ κύριος μετὰ σοῦ → องค์พระผู้เป็นเจ้าทรงสถิตกับท่าน — Per uW figs-idiom: 'the Lord is with you' = 'the Lord favors you / has chosen you for special purpose.' OT formula — same words to Gideon (Judg 6:12 LXX), Boaz-to-workers greeting (Ruth 2:4), Moses (Exod 3:12). Thai...
- Notes: The angelic greeting is a triple-layered OT allusion compressed into three Greek words. Χαῖρε echoes prophetic-joy texts like ZEP 3:14-15 and ZEC 9:9 ('Rejoice greatly, O daughter of Zion... your king comes to you'). κεχαριτωμένη is an extremely rare participle (only here and Eph 1:6 εἰς ἔπαινον δόξης τῆς χάριτος αὐτοῦ, ἧς ἐχαρίτωσεν ἡμᾶς — of...

**Luke 1:29**
- GR: ἡ δὲ ἐπὶ τῷ λόγῳ διεταράχθη καὶ διελογίζετο ποταπὸς εἴη ὁ ἀσπασμὸς οὗτος.
- TH: นางตกใจอย่างยิ่งเมื่อได้ยินถ้อยคำนั้น และครุ่นคิดว่าคำทักทายนี้มีความหมายอย่างไร
- Key decisions:
  - διεταράχθη → ตกใจอย่างยิ่ง — HAPAX: διαταράσσω (only here in NT; intensive of ταράσσω v.12 ἐταράχθη of Zechariah). διά-prefix intensifies — 'greatly troubled / thoroughly disturbed.' Thai ตกใจอย่างยิ่ง captures the heightened disturbance. Notab...
  - ἐπὶ τῷ λόγῳ → เมื่อได้ยินถ้อยคำนั้น — Per uW figs-metonymy: 'word(s)' = what Gabriel said. Thai ถ้อยคำ natural
  - διελογίζετο ποταπὸς εἴη ὁ ἀσπασμὸς οὗτος → ครุ่นคิดว่าคำทักทายนี้มีความหมายอย่างไร — διαλογίζομαι imperfect = 'was pondering / reasoning through.' ποταπός = 'what sort / of-what-kind?' (with curiosity-nuance, cf. MAT 8:27, MRK 13:1). ἀσπασμός = 'greeting.' Thai ครุ่นคิด (deeply-ponder) + มีความหมายอ...
- Notes: NT HAPAX: διαταράσσω (only here). Mary's perplexity is over the content of the greeting, not over the angel's visible presence (contrast Zechariah v.12, where the angel's appearance itself caused fear). Her response is intellectually engaged from the start — 'what kind of greeting is this?' — meaning she recognizes the extraordinary claim embe...

**Luke 1:30**
- GR: καὶ εἶπεν ὁ ἄγγελος αὐτῇ· Μὴ φοβοῦ, Μαριάμ, εὗρες γὰρ χάριν παρὰ τῷ θεῷ·
- TH: ทูตสวรรค์จึงกล่าวแก่นางว่า «อย่ากลัวเลย มารีย์ เพราะท่านได้รับพระคุณจากพระเจ้า
- Key decisions:
  - Μὴ φοβοῦ, Μαριάμ → อย่ากลัวเลย มารีย์ — Same angelic-reassurance formula as v.13 (to Zechariah). Thai อย่ากลัวเลย consistent. Direct address by name — personal-recognition moment
  - εὗρες...χάριν παρὰ τῷ θεῷ → ท่านได้รับพระคุณจากพระเจ้า — Per uW figs-activepassive: 'God is showing you grace / has given you grace.' εὗρον χάριν = 'find favor' (LXX idiom for Noah Gen 6:8, Moses Exod 33:12-17, David 2 Sam 15:25 — all major covenant-figures). Thai ได้รับพ...
- Notes: The εὗρες χάριν παρὰ τῷ θεῷ phrase is LXX idiom for the privileged-recipients of divine election: Noah (Gen 6:8 LXX), Abraham, Moses (Exod 33:12-17), David (2 Sam 15:25). Mary is placed in that salvific-elect line. The grammatical contrast with κεχαριτωμένη (perfect passive 'having-been-and-still-graced') is notable: v.28 describes her settled...

**Luke 1:31**
- GR: καὶ ἰδοὺ συλλήμψῃ ἐν γαστρὶ καὶ τέξῃ υἱόν, καὶ καλέσεις τὸ ὄνομα αὐτοῦ Ἰησοῦν.
- TH: ดูเถิด ท่านจะตั้งครรภ์และให้กำเนิดบุตรชาย ท่านจงตั้งชื่อเขาว่าเยซู
- TH-summary: ชื่อ «เยซู» (ในภาษาฮีบรู «เยชูอา» ย่อจาก «เยโฮชูอา») แปลว่า «พระยาห์เวห์ทรงช่วยให้รอด» มัทธิว 1:21 อธิบายความหมายของชื่อนี้ว่า «เพราะเขาจะช่วยประชาชนของเขาให้พ้นจากบาป» คำประกาศนี้สะท้อนคำพยากรณ์ของอิสยาห์ 7:14 เกี่ยวกับอิมมานูเอล — หญิงพรหมจารีจะตั้งครรภ์และให้กำเนิดบุตรชาย
- Key decisions:
  - καὶ ἰδοὺ → ดูเถิด — Per uW figs-metaphor: attention-marker. Thai ดูเถิด consistent
  - συλλήμψῃ ἐν γαστρὶ καὶ τέξῃ υἱόν → ท่านจะตั้งครรภ์และให้กำเนิดบุตรชาย — Per uW figs-explicitinfo: 'conceive-in-womb + bear son' — preserve both as emphasizing actual human-physical motherhood. Thai ตั้งครรภ์ + ให้กำเนิดบุตรชาย natural doublet. Near-verbatim LXX Isa 7:14 συλλήμψεται ἐν γ...
  - καλέσεις τὸ ὄνομα αὐτοῦ Ἰησοῦν → ท่านจงตั้งชื่อเขาว่าเยซู — Per uW figs-declarative/figs-idiom: future-as-command 'you shall name him.' Ἰησοῦς → เยซู — use the plain name here (NOT พระเยซู with divine prefix), because this is Gabriel addressing a human Mary about the child's...
- Notes: DIRECT LXX QUOTATION of Isa 7:14 (συλλήμψεται ἐν γαστρὶ καὶ τέξεται υἱόν), adapted to the 2nd-person. Matthew 1:23 cites this same Isaiah verse directly; Luke does it implicitly. The name-giving is given to MARY (contrast 1:13 to Zechariah, or Matthew 1:21 to Joseph — Luke emphasizes Mary's agency). The name 'Jesus' (Yeshua) shared with Joshua...

**Luke 1:32**
- GR: οὗτος ἔσται μέγας καὶ υἱὸς Ὑψίστου κληθήσεται, καὶ δώσει αὐτῷ κύριος ὁ θεὸς τὸν θρόνον Δαυὶδ τοῦ πατρὸς αὐτοῦ,
- TH: บุตรนี้จะเป็นผู้ยิ่งใหญ่ และจะได้ชื่อว่า พระบุตรขององค์ผู้สูงสุด องค์พระผู้เป็นเจ้าพระเจ้าจะประทานพระราชบัลลังก์ของดาวิดบรรพบุรุษของพระองค์แก่พระองค์
- TH-summary: คำสัญญา «พระราชบัลลังก์ของดาวิด» เป็นการทรงประกาศว่าบุตรที่มารีย์จะให้กำเนิดนั้นคือพระเมสสิยาห์ตามพันธสัญญาของพระเจ้าแก่ดาวิด (2 ซามูเอล 7:12-16) ที่ว่าเชื้อสายของดาวิดจะครองราชย์ตลอดไป คำว่า «พระบุตรขององค์ผู้สูงสุด» บ่งชี้ความเป็นพระเจ้าของบุตรนี้ — ไม่ใช่เพียงตำแหน่งกษัตริย์ แต่ทรงเป็นพระบุตรของพระเจ้าโดยธรรมชาติ
- Key decisions:
  - μέγας → ผู้ยิ่งใหญ่ — Parallel to v.15 (John 'great before the Lord') but here absolute — Jesus's greatness is not specified 'before X' because it is unconditional. Thai ผู้ยิ่งใหญ่ natural
  - υἱὸς Ὑψίστου κληθήσεται → พระบุตรขององค์ผู้สูงสุด — Per uW figs-idiom/figs-activepassive: 'will be called' = 'will be.' υἱὸς θεοῦ title with Ὕψιστος = divine epithet (cf. Gen 14:18-22 LXX Melchizedek's θεὸς ὕψιστος; Dan 4:17, 24-25 Nebuchadnezzar; common LXX for YHWH...
  - κύριος ὁ θεός → องค์พระผู้เป็นเจ้าพระเจ้า — YHWH Elohim compound divine name. Thai องค์พระผู้เป็นเจ้าพระเจ้า (double-title) for the formal LXX-compound. Royal-subject verb ประทาน per §3
  - τὸν θρόνον Δαυίδ τοῦ πατρὸς αὐτοῦ → พระราชบัลลังก์ของดาวิดบรรพบุรุษของพระองค์ — Per uW figs-metonymy/figs-metaphor: 'throne' = kingship-authority; 'father' = ancestor. Thai พระราชบัลลังก์ (royal-throne) + บรรพบุรุษ (ancestor). DIRECT CITATION of 2 Sam 7:12-13 LXX (Davidic covenant — ἀναστήσω τὸ...
- Notes: DENSE OT CITATION-CLUSTER. (1) υἱὸς Ὑψίστου directly evokes 2 Sam 7:14 LXX (ἐγὼ ἔσομαι αὐτῷ εἰς πατέρα, καὶ αὐτὸς ἔσται μοι εἰς υἱόν) — Nathan's oracle to David about his royal son. (2) θρόνον Δαυίδ echoes 2 Sam 7:12-13 (ἀνορθώσω τὸν θρόνον αὐτοῦ ἕως εἰς τὸν αἰῶνα). (3) Ὕψιστος is a major Hellenistic-Jewish divine epithet. The angel's statemen...

**Luke 1:33**
- GR: καὶ βασιλεύσει ἐπὶ τὸν οἶκον Ἰακὼβ εἰς τοὺς αἰῶνας, καὶ τῆς βασιλείας αὐτοῦ οὐκ ἔσται τέλος.
- TH: พระองค์จะทรงครองราชย์เหนือพงศ์พันธุ์ยาโคบสืบไปเป็นนิตย์ และราชอาณาจักรของพระองค์จะไม่มีที่สิ้นสุดเลย»
- Key decisions:
  - βασιλεύσει ἐπὶ τὸν οἶκον Ἰακώβ → จะทรงครองราชย์เหนือพงศ์พันธุ์ยาโคบ — Per uW figs-metaphor: 'house of Jacob' = the people of Israel. Thai พงศ์พันธุ์ยาโคบ ('clan of Jacob') preserves the dynasty-family-people sense. Royal verb ครองราชย์ per §3 for divine-royal subject. Ἰακώβ → ยาโคบ st...
  - εἰς τοὺς αἰῶνας → สืบไปเป็นนิตย์ — Per uW figs-idiom: 'into the ages' = forever. Thai สืบไปเป็นนิตย์ ('continuing onward as eternal') natural
  - τῆς βασιλείας αὐτοῦ οὐκ ἔσται τέλος → ราชอาณาจักรของพระองค์จะไม่มีที่สิ้นสุดเลย — Per uW figs-litotes/figs-abstractnouns: double-negative 'not end' = 'endlessly continue.' Per uW figs-parallelism: parallel to the 'forever' of the previous clause — Hebraic poetic repetition. Preserve both phrases....
- Notes: DIRECT verbal-echo of DANIEL 7:14 LXX (ἡ ἐξουσία αὐτοῦ ἐξουσία αἰώνιος, ἥτις οὐ παρελεύσεται, καὶ ἡ βασιλεία αὐτοῦ οὐ διαφθαρήσεται — 'his kingdom shall not be destroyed') — the Son-of-Man prophecy. Also echoes ISA 9:7 LXX (τῆς εἰρήνης αὐτοῦ οὐκ ἔστιν ὅριον — 'of his peace there is no limit' — in the Immanuel/Prince-of-Peace oracle) and 2 SAM ...

**Luke 1:34**
- GR: εἶπεν δὲ Μαριὰμ πρὸς τὸν ἄγγελον· Πῶς ἔσται τοῦτο, ἐπεὶ ἄνδρα οὐ γινώσκω;
- TH: มารีย์จึงกล่าวแก่ทูตสวรรค์ว่า «เรื่องนี้จะเป็นไปได้อย่างไร เพราะดิฉันยังไม่เคยร่วมรู้กับชายใดเลย»
- TH-summary: คำถามของมารีย์ต่างจากคำถามของเศคาริยาห์ (ข้อ 18) — มารีย์ไม่ได้สงสัยว่าพระสัญญาจะเป็นจริงหรือไม่ แต่ถามถึงวิธีการที่ไม่เข้าใจ ทูตสวรรค์ตอบนางอย่างอ่อนโยน (ข้อ 35-37) ต่างจากเศคาริยาห์ที่ถูกลงโทษให้เป็นใบ้ คำว่า «ร่วมรู้กับชายใด» (กิโนสโก อันดรา) เป็นสำนวนโบราณในพระคัมภีร์เดิมที่หมายถึงความสัมพันธ์ทางเพศ (เทียบ ปฐมกาล 4:1)
- Key decisions:
  - Πῶς ἔσται τοῦτο → เรื่องนี้จะเป็นไปได้อย่างไร — Per uW figs-explicit: Mary does not doubt (contrast Zechariah's κατὰ τί γνώσομαι seeking proof v.18). She asks about mechanism. Thai เรื่องนี้จะเป็นไปได้อย่างไร natural — 'how will this be possible?'
  - ἐπεὶ ἄνδρα οὐ γινώσκω → เพราะดิฉันยังไม่เคยร่วมรู้กับชายใดเลย — Per uW figs-euphemism: γινώσκω ἄνδρα = euphemism for 'have sexual relations with a man' (Hebrew יָדַע pattern; cf. Gen 4:1 LXX). Thai ยังไม่เคยร่วมรู้ (biblical-euphemistic 'have-not-yet known-in-union') preserves t...
- Notes: KEY CONTRAST with Zechariah (v.18): Mary asks HOW, not WHETHER — trusting the promise, only unable to picture the physical mechanism. Her betrothal-but-not-consummated status (γινώσκω ἄνδρα) means normal-conception is not yet possible. The angel's reply (v.35) bypasses the natural mechanism entirely — the Spirit will conceive. Theologically th...

**Luke 1:35**
- GR: καὶ ἀποκριθεὶς ὁ ἄγγελος εἶπεν αὐτῇ· Πνεῦμα ἅγιον ἐπελεύσεται ἐπὶ σέ, καὶ δύναμις Ὑψίστου ἐπισκιάσει σοι· διὸ καὶ τὸ γεννώμενον ἅγιον κληθήσεται, υἱὸς θεοῦ·
- TH: ทูตสวรรค์ตอบนางว่า «พระวิญญาณบริสุทธิ์จะเสด็จลงมาเหนือท่าน และฤทธิ์เดชขององค์ผู้สูงสุดจะทรงปกคลุมท่านด้วยเงา เพราะฉะนั้นองค์บริสุทธิ์ที่จะทรงประสูติมานั้นจะได้ชื่อว่า พระบุตรของพระเจ้า
- TH-summary: คำว่า «ปกคลุมด้วยเงา» (เอปิสกิอาโซ) สะท้อนภาพเมฆแห่งการประทับของพระเจ้าในพระคัมภีร์เดิม — เมฆที่ปกคลุมภูเขาซีนาย (อพยพ 24:15-16) เมฆที่ปกคลุมพลับพลา (อพยพ 40:34-35) และเมฆที่ปกคลุมพระวิหาร (1 พงศ์กษัตริย์ 8:10-11) พระวิญญาณของพระเจ้าทรงเคลื่อนไหวบนน้ำในปฐมกาล 1:2 บัดนี้ทรงกระทำพระราชกิจสร้างใหม่ในครรภ์ของมารีย์
- Key decisions:
  - Πνεῦμα ἅγιον ἐπελεύσεται ἐπὶ σέ → พระวิญญาณบริสุทธิ์จะเสด็จลงมาเหนือท่าน — Per uW figs-parallelism: this is hebraic-parallel-poetry with the next clause. ἐπέρχομαι = 'come upon.' Royal verb เสด็จ per §3 for divine-descent. πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์ established
  - δύναμις Ὑψίστου ἐπισκιάσει σοι → ฤทธิ์เดชขององค์ผู้สูงสุดจะทรงปกคลุมท่านด้วยเงา — Per uW figs-metaphor: ἐπισκιάζω = 'overshadow / cover-with-shadow' — LXX verb for shekinah-cloud (Exod 40:35 LXX ἐπεσκίαζεν ἐπ᾽ αὐτὴν ἡ νεφέλη). The shekinah-glory-cloud imagery is explicitly theophanic-creational. ...
  - τὸ γεννώμενον ἅγιον κληθήσεται, υἱὸς θεοῦ → องค์บริสุทธิ์ที่จะทรงประสูติมานั้นจะได้ชื่อว่า พระบุตรของพระเจ้า — Per uW figs-idiom/figs-activepassive: 'will be called' = 'will be.' Per uW guidelines-sonofgodprinciples: preserve divine Sonship. The ambiguity of τὸ γεννώμενον ἅγιον: could be 'the holy thing born' (neuter adj+ptc...
- Notes: THE MOST THEOLOGICALLY DENSE VERSE IN THE CHAPTER. Multiple OT echoes converge: (1) ἐπισκιάζω is the LXX-shekinah-cloud verb (Exod 40:35 of Tabernacle; Num 9:18, 22; the NT uses it again of Transfiguration Matt 17:5, Mark 9:7, Luke 9:34 — the same theophanic-cloud). (2) Creation-echo: the Spirit of God 'hovered over the waters' (Gen 1:2, Hebre...

**Luke 1:36**
- GR: καὶ ἰδοὺ Ἐλισάβετ ἡ συγγενίς σου καὶ αὐτὴ συνείληφεν υἱὸν ἐν γήρει αὐτῆς, καὶ οὗτος μὴν ἕκτος ἐστὶν αὐτῇ τῇ καλουμένῃ στείρᾳ·
- TH: และดูเถิด เอลีซาเบธญาติของท่านเองก็ได้ตั้งครรภ์บุตรชายในวัยชราของนาง บัดนี้นางที่คนเรียกว่าหญิงหมันนั้นกำลังตั้งครรภ์เป็นเดือนที่หกแล้ว
- Key decisions:
  - ἰδοὺ → ดูเถิด — Per uW figs-metaphor: attention-marker
  - Ἐλισάβετ ἡ συγγενίς σου → เอลีซาเบธญาติของท่าน — HAPAX: συγγενίς (feminine form; only here in NT, though συγγενής masc./common is frequent). 'Kinswoman / relative.' Exact relationship unknown — could be cousin, aunt, etc. Thai ญาติ (neutral 'relative') preserves t...
  - συνείληφεν υἱὸν ἐν γήρει αὐτῆς → ได้ตั้งครรภ์บุตรชายในวัยชราของนาง — HAPAX: γῆρας (only here in NT; common in LXX). 'Old age.' Thai วัยชรา natural. συλλαμβάνω perfect = has-conceived (state-perfect — she is pregnant now)
  - οὗτος μὴν ἕκτος ἐστὶν αὐτῇ τῇ καλουμένῃ στείρᾳ → บัดนี้นางที่คนเรียกว่าหญิงหมันนั้นกำลังตั้งครรภ์เป็นเดือนที่หกแล้ว — Per uW figs-idiom: τῇ καλουμένῃ στείρᾳ = 'the one (merely) called barren' — reputation undone by reality. Thai นางที่คนเรียกว่าหญิงหมัน captures the 'so-called barren' reversal
- Notes: TWO HAPAX in one verse: συγγενίς (feminine kinswoman, only here) and γῆρας ('old age,' only here in NT though common elsewhere). The angel's sign-gift to Mary — information about Elizabeth's pregnancy — is a pastoral-tender gesture: Gabriel does not merely command belief, he offers a concrete verifiable sign. Note the parallelism: Mary now kno...

**Luke 1:37**
- GR: ὅτι οὐκ ἀδυνατήσει παρὰ τοῦ θεοῦ πᾶν ῥῆμα.
- TH: เพราะไม่มีสิ่งใดเป็นไปไม่ได้สำหรับพระเจ้า»
- Key decisions:
  - οὐκ ἀδυνατήσει παρὰ τοῦ θεοῦ πᾶν ῥῆμα → ไม่มีสิ่งใดเป็นไปไม่ได้สำหรับพระเจ้า — Per uW figs-doublenegatives/figs-metonymy: double negative = strong positive. πᾶν ῥῆμα 'every word/thing' — Hebraic idiom דָּבָר davar means both 'word' and 'matter/thing.' Per uW: interpretive range (1) no-word-fro...
- Notes: DIRECT LXX QUOTATION of GENESIS 18:14 (μὴ ἀδυνατήσει παρὰ τῷ θεῷ ῥῆμα?) — the LORD's rhetorical question to Abraham after Sarah's laugh at the announced impossible-pregnancy. This intertext is the single most loaded Abraham-typology moment in the chapter: Mary's faith-response parallels Sarah's miracle-conception. Matthew 19:26 / Mark 10:27 ec...

**Luke 1:38**
- GR: εἶπεν δὲ Μαριάμ· Ἰδοὺ ἡ δούλη κυρίου· γένοιτό μοι κατὰ τὸ ῥῆμά σου. καὶ ἀπῆλθεν ἀπ᾽ αὐτῆς ὁ ἄγγελος.
- TH: มารีย์ตอบว่า «ข้าพเจ้าคือทาสหญิงขององค์พระผู้เป็นเจ้า ขอให้เป็นไปแก่ข้าพเจ้าตามถ้อยคำของท่านเถิด» แล้วทูตสวรรค์ก็จากนางไป
- TH-summary: คำตอบของมารีย์ «ขอให้เป็นไปตามถ้อยคำของท่านเถิด» (ในภาษาละติน «Fiat voluntas tua» แบบคำอธิษฐานขององค์พระผู้เป็นเจ้า) เป็นคำที่แสดงถึงความยอมจำนนและศรัทธาอย่างสมบูรณ์ นางเรียกตนเองว่า «ทาสหญิง» (ดูลี) — ใช้คำสมถะเหมือนกับฮันนาห์ (1 ซามูเอล 1:11) และนางรูธ (รูธ 3:9) เมื่อพูดกับผู้มีอำนาจเหนือนาง
- Key decisions:
  - Ἰδοὺ ἡ δούλη κυρίου → ข้าพเจ้าคือทาสหญิงขององค์พระผู้เป็นเจ้า — Per uW figs-metaphor: Mary's humble self-identification. ἰδού here = 'here I am' / 'behold-me' (self-presentation formula, cf. Isaiah 6:8 LXX ἰδοὺ ἐγώ; 1 Sam 3 Samuel's 'here I am'). δούλη feminine = female-slave/se...
  - γένοιτό μοι κατὰ τὸ ῥῆμά σου → ขอให้เป็นไปแก่ข้าพเจ้าตามถ้อยคำของท่านเถิด — γένοιτο aorist optative = 'may it happen' (wish/acceptance formula). Per uW: Mary expressing willingness. Thai ขอให้เป็นไปแก่ข้าพเจ้า preserves optative-submission. ρῆμα → ถ้อยคำ consistent with other occurrences of...
  - ἀπῆλθεν ἀπ᾽ αὐτῆς ὁ ἄγγελος → ทูตสวรรค์ก็จากนางไป — ἀπέρχομαι aor. = 'departed.' Thai จากนางไป natural closing of the annunciation scene
- Notes: Mary's γένοιτο (third-person-singular aorist optative) is liturgically significant — the Latin Vulgate's 'fiat' (translated by English 'let it be') captures the acceptance-formula. This is Mary's fiat, the moment of consent to God's initiative. The parallel to Hannah's 1 Sam 1:11 LXX 'if you will look on the humble-state of your handmaid (ταπε...

**Luke 1:39**
- GR: Ἀναστᾶσα δὲ Μαριὰμ ἐν ταῖς ἡμέραις ταύταις ἐπορεύθη εἰς τὴν ὀρεινὴν μετὰ σπουδῆς εἰς πόλιν Ἰούδα,
- TH: ในเวลานั้น มารีย์รีบลุกขึ้นเดินทางไปยังเมืองหนึ่งในแถบภูเขาของยูดาห์อย่างเร่งด่วน
- Key decisions:
  - Ἀναστᾶσα...ἐν ταῖς ἡμέραις ταύταις → ในเวลานั้น...รีบลุกขึ้น — Per uW figs-idiom/writing-newevent: 'in these days' = 'around that time' (new episode marker). ἀνίστημι aor.ptc. = 'having risen up' — idiom for 'got-up-to-do-something' (not just posture). Thai ลุกขึ้น preserves th...
  - εἰς τὴν ὀρεινὴν μετὰ σπουδῆς εἰς πόλιν Ἰούδα → ไปยังเมืองหนึ่งในแถบภูเขาของยูดาห์อย่างเร่งด่วน — ὀρεινή = 'hilly region.' Per uW figs-explicit: south of Jerusalem to Negev. μετὰ σπουδῆς = 'with haste/eagerness.' Thai แถบภูเขาของยูดาห์ (hilly-region of Judah) + อย่างเร่งด่วน. Ἰούδα → ยูดาห์ standard Thai transli...
- Notes: Mary's haste is notable. The journey from Nazareth (Galilee) to the hill country of Judah (traditionally identified as Ein Karem near Jerusalem) is ~80-100 miles — several days' walk, likely with a caravan for safety. A young engaged woman traveling alone or with minimal escort is unusual; her haste suggests both eagerness to confirm Elizabeth...

**Luke 1:40**
- GR: καὶ εἰσῆλθεν εἰς τὸν οἶκον Ζαχαρίου καὶ ἠσπάσατο τὴν Ἐλισάβετ.
- TH: นางเข้าไปในบ้านของเศคาริยาห์และทักทายเอลีซาเบธ
- Key decisions:
  - εἰσῆλθεν εἰς τὸν οἶκον Ζαχαρίου → เข้าไปในบ้านของเศคาริยาห์ — Per uW figs-explicit: Mary arrived and entered. Thai เข้าไปในบ้าน natural
  - ἠσπάσατο τὴν Ἐλισάβετ → ทักทายเอลีซาเบธ — ἀσπάζομαι = 'greet.' Aorist middle. Thai ทักทาย natural. Elizabeth's response to Mary's greeting (v.41) is the decisive moment — the voice of greeting causes the baby to leap, then Elizabeth to prophesy. The greetin...
- Notes: Note the house is identified as Zechariah's, not Elizabeth's — standard ancient-household designation. Zechariah himself is present but silent (still mute). The scene is striking: two pregnant women in an unspeaking priest's home, one matriarch-typologically (Elizabeth-as-Sarah/Hannah), one virgin-typologically (Mary-new). The meeting will pro...

**Luke 1:41**
- GR: καὶ ἐγένετο ὡς ἤκουσεν τὸν ἀσπασμὸν τῆς Μαρίας ἡ Ἐλισάβετ, ἐσκίρτησεν τὸ βρέφος ἐν τῇ κοιλίᾳ αὐτῆς, καὶ ἐπλήσθη πνεύματος ἁγίου ἡ Ἐλισάβετ,
- TH: เมื่อเอลีซาเบธได้ยินคำทักทายของมารีย์ ทารกในครรภ์ของนางก็ดิ้นไหว และเอลีซาเบธก็เต็มเปี่ยมด้วยพระวิญญาณบริสุทธิ์
- TH-summary: ทารกในครรภ์ของเอลีซาเบธ (ยอห์นผู้ให้บัพติศมา) «ดิ้นไหว» เมื่อได้ยินเสียงของมารีย์ผู้ซึ่งบัดนี้ทรงตั้งครรภ์พระเยซู คำว่า «ดิ้นไหว» (เอสกีร์เตเซน) เป็นคำเดียวกับที่ใช้ในพระคัมภีร์เดิม (ปฐมกาล 25:22) เมื่อเอซาวและยาโคบดิ้นในครรภ์ของรีเบคาห์ — สัญลักษณ์ของการทำนายชะตากรรมของทารก ยอห์นเป็นผู้เผยพระวจนะตั้งแต่ในครรภ์แล้ว (เทียบข้อ 15)
- Key decisions:
  - ἐγένετο ὡς ἤκουσεν → เมื่อ...ได้ยิน — Per uW writing-newevent: narrative marker. ἐγένετο + subordinate clause (Hebraic וַיְהִי ... כַּאֲשֶׁר). Thai เมื่อ simple temporal clause
  - ἐσκίρτησεν τὸ βρέφος ἐν τῇ κοιλίᾳ αὐτῆς → ทารกในครรภ์ของนางก็ดิ้นไหว — Per uW figs-metaphor: σκιρτάω = 'leap / skip.' Literally 'the baby leaped.' Typically used of joyful-animal-leaping (lambs). In-utero this is figurative — sudden movement. Thai ดิ้นไหว (quiver/stir) natural-physical...
  - ἐπλήσθη πνεύματος ἁγίου ἡ Ἐλισάβετ → เอลีซาเบธก็เต็มเปี่ยมด้วยพระวิญญาณบริสุทธิ์ — Per uW figs-activepassive/figs-metaphor: 'Spirit filled her' / 'vessel-filled.' Consistent with v.15 (John's prenatal Spirit-filling). Thai เต็มเปี่ยมด้วย natural
- Notes: MAJOR OT VERBAL ECHO: ἐσκίρτησεν...ἐν τῇ κοιλίᾳ (LXX σκιρτῶντα ἐν ἐμοί, Gen 25:22 of Jacob-and-Esau's in-utero struggle — announcing the older will serve the younger). The baby-in-womb recognition-and-reaction motif is Hebraically-prophetic. John, prenatal and Spirit-filled (v.15), here fulfills his forerunner-role before he can speak: his in-...

**Luke 1:42**
- GR: καὶ ἀνεφώνησεν κραυγῇ μεγάλῃ καὶ εἶπεν· Εὐλογημένη σὺ ἐν γυναιξίν, καὶ εὐλογημένος ὁ καρπὸς τῆς κοιλίας σου.
- TH: นางเปล่งเสียงดังประกาศว่า «ท่านได้รับพระพรท่ามกลางหญิงทั้งปวง และผู้ที่อยู่ในครรภ์ของท่านก็ได้รับพระพร
- TH-summary: «ท่านได้รับพระพรท่ามกลางหญิงทั้งปวง» เป็นสำนวนฮีบรูที่หมายความว่า «ท่านเป็นหญิงที่ได้รับพระพรมากที่สุด» สะท้อนถ้อยคำของเดโบราห์ถึงยาเอลใน ผู้วินิจฉัย 5:24 และถ้อยคำของอุสซียาถึงจูดิธในหนังสือจูดิธ 13:18 ทั้งสองผู้หญิงเหล่านั้นได้รับพระพรเพราะทำลายศัตรูของพระเจ้า — บัดนี้มารีย์ได้รับพระพรเพราะให้กำเนิดองค์ผู้จะทำลายศัตรูของพระเจ้าในระดับจักรวาล
- Key decisions:
  - ἀνεφώνησεν κραυγῇ μεγάλῃ → เปล่งเสียงดังประกาศ — HAPAX: ἀναφωνέω (only here in NT) = 'cry out / exclaim loudly' (ἀνα- up + φωνέω 'speak'). Per uW figs-hendiadys: 'exclaimed + said' together = 'exclaimed loudly.' Per uW figs-idiom: κραυγῇ μεγάλῃ = 'in a loud voice....
  - Εὐλογημένη σὺ ἐν γυναιξίν → ท่านได้รับพระพรท่ามกลางหญิงทั้งปวง — Per uW figs-idiom: 'blessed among women' = 'most blessed woman.' Perfect passive ptc εὐλογημένος = 'has-been-and-still-blessed.' Hebraic-superlative-idiom (cf. Judg 5:24 LXX of Jael; Judith 13:18 in Deuterocanon — s...
  - εὐλογημένος ὁ καρπὸς τῆς κοιλίας σου → ผู้ที่อยู่ในครรภ์ของท่านก็ได้รับพระพร — Per uW figs-metaphor: 'fruit of womb' = child-in-womb. Rather than literal 'fruit' (awkward for a person), Thai ผู้ที่อยู่ในครรภ์ ('the-one-who-is-in-the-womb') preserves the personal reference — still clearly in-ut...
- Notes: NT HAPAX: ἀναφωνέω (only here). OT ALLUSIONS: (1) Judg 5:24 LXX Εὐλογηθείη ἐκ γυναικῶν Ιαηλ — Deborah's song blessing Jael for killing Sisera. (2) DEUTERO-CANONICAL Judith 13:18 Εὐλογητὴ σύ θύγατερ τῷ θεῷ τῷ ὑψίστῳ παρὰ πάσας τὰς γυναῖκας — Uzziah to Judith after she killed Holofernes. Both comparisons are of women-who-broke-the-enemy. Mary st...

**Luke 1:43**
- GR: καὶ πόθεν μοι τοῦτο ἵνα ἔλθῃ ἡ μήτηρ τοῦ κυρίου μου πρὸς ἐμέ;
- TH: เหตุใดหนอข้าพเจ้าจึงได้รับเกียรตินี้ ที่มารดาขององค์พระผู้เป็นเจ้าของข้าพเจ้าเสด็จมาหาข้าพเจ้า?
- Key decisions:
  - πόθεν μοι τοῦτο → เหตุใดหนอข้าพเจ้าจึงได้รับเกียรตินี้ — Per uW figs-rquestion/figs-idiom: 'whence this to me?' = idiom for 'how wonderful and unexpected.' Not seeking information, but expressing awe. Thai เหตุใดหนอ (rhetorical-exclamatory 'why indeed') + ได้รับเกียรตินี้...
  - ἡ μήτηρ τοῦ κυρίου μου → มารดาขององค์พระผู้เป็นเจ้าของข้าพเจ้า — Per uW figs-123person: Elizabeth addresses Mary in third-person as reverent-honorific. Crucially, κύριος here refers to the in-womb Jesus. Elizabeth's Spirit-given title 'mother of my Lord' is the earliest recorded ...
  - ἔλθῃ...πρὸς ἐμέ → เสด็จมาหาข้าพเจ้า — ἔρχομαι subj. Royal verb เสด็จ per §3 — here applied to Mary's coming, because she carries the divine child (divine-by-extension honor). Though unusual for a human subject, Elizabeth's Spirit-filled speech is honori...
- Notes: CHRISTOLOGICAL PEAK: Elizabeth's 'mother of my Lord' (μήτηρ τοῦ κυρίου μου) is an astonishing early confession — an in-utero recognition that the unborn Jesus is κύριος. This is the theological ground for the Chalcedonian 'theotokos' (God-bearer) title for Mary — originally a Christological assertion (against Nestorius): if Mary is mother of t...

**Luke 1:44**
- GR: ἰδοὺ γὰρ ὡς ἐγένετο ἡ φωνὴ τοῦ ἀσπασμοῦ σου εἰς τὰ ὦτά μου, ἐσκίρτησεν ἐν ἀγαλλιάσει τὸ βρέφος ἐν τῇ κοιλίᾳ μου.
- TH: ดูเถิด เมื่อเสียงทักทายของท่านมาถึงหูของข้าพเจ้า ทารกในครรภ์ของข้าพเจ้าก็ดิ้นไหวด้วยความยินดี
- Key decisions:
  - ἰδοὺ γὰρ → ดูเถิด — Attention-marker + explanatory. Thai ดูเถิด consistent
  - ὡς ἐγένετο ἡ φωνὴ τοῦ ἀσπασμοῦ σου εἰς τὰ ὦτά μου → เมื่อเสียงทักทายของท่านมาถึงหูของข้าพเจ้า — Per uW figs-metaphor: 'sound reached ears' = 'heard your voice.' Thai เสียงทักทาย...มาถึงหู natural-poetic preserving the sensory image (rather than flattening to 'I heard')
  - ἐσκίρτησεν ἐν ἀγαλλιάσει τὸ βρέφος → ทารก...ก็ดิ้นไหวด้วยความยินดี — Per uW figs-metaphor: σκιρτάω (v.41) repeated; now with explicit-joy qualifier. ἀγαλλίασις = exultation (cognate with ἀγάλλομαι — used of Mary's spirit in v.47). Thai ดิ้นไหวด้วยความยินดี — consistent with v.41 rend...
- Notes: Elizabeth interprets the baby's-leap as prophetic-recognition — John the forerunner exulting at the Messiah's proximity. This is a key proof-text for personhood-from-conception theology (though Luke's primary intent is narrative, not bioethical). The ἀγαλλίασις (joy) motif recurs in v.47 Magnificat (ἠγαλλίασεν τὸ πνεῦμά μου) — linking Elizabet...

**Luke 1:45**
- GR: καὶ μακαρία ἡ πιστεύσασα ὅτι ἔσται τελείωσις τοῖς λελαλημένοις αὐτῇ παρὰ κυρίου.
- TH: ผู้ที่เชื่อนั้นเป็นสุข เพราะสิ่งซึ่งองค์พระผู้เป็นเจ้าตรัสแก่นางจะสำเร็จครบถ้วน»
- Key decisions:
  - μακαρία ἡ πιστεύσασα → ผู้ที่เชื่อนั้นเป็นสุข — Per uW figs-123person: Elizabeth speaks of Mary in 3rd-person as respect. μακάριος → เป็นสุข established glossary (from MAT 5 Beatitudes). Feminine ptc. 'the-one-who-has-believed' — Mary's act of faith (contrast Zec...
  - ἔσται τελείωσις → จะสำเร็จครบถ้วน — Per uW figs-activepassive: 'the Lord will accomplish.' τελείωσις = 'completion/fulfillment.' Thai สำเร็จครบถ้วน preserves the fulfillment-to-completion sense
  - τοῖς λελαλημένοις αὐτῇ παρὰ κυρίου → สิ่งซึ่งองค์พระผู้เป็นเจ้าตรัสแก่นาง — Per uW figs-explicit: 'spoken to her from the Lord' — though Gabriel spoke, the words are FROM the Lord. Royal verb ตรัส per §3. παρά 'from-beside' = source. κύριος = YHWH → องค์พระผู้เป็นเจ้า
- Notes: Elizabeth pronounces the FIRST BEATITUDE in Luke: 'Blessed is she who believed.' The contrast with Zechariah's doubt is implicit but sharp — Zechariah did not believe the angel's words (v.20), received muteness; Mary believed, receives blessing. This beatitude-of-faith anticipates Jesus's later μακάριος-sayings (6:20-22, etc.) and sets up Luke...

**Luke 1:46**
- GR: Καὶ εἶπεν Μαριάμ· Μεγαλύνει ἡ ψυχή μου τὸν κύριον,
- TH: มารีย์จึงกล่าวว่า «จิตวิญญาณของข้าพเจ้าเทิดทูนองค์พระผู้เป็นเจ้า
- TH-summary: นี่คือเริ่มต้นของเพลง «แมกนิฟิแคต» (Magnificat) — เพลงสดุดีของมารีย์ซึ่งสะท้อนเพลงของฮันนาห์ใน 1 ซามูเอล 2:1-10 เกือบจะทุกบรรทัด มารีย์เข้าใจว่าตนเองยืนอยู่ในสายของหญิงที่พระเจ้าทรงยกฐานะในประวัติศาสตร์ความรอด ฮันนาห์ที่เคยเป็นหมันได้เพลงสดุดีเมื่อให้กำเนิดซามูเอลผู้เจิมกษัตริย์ดาวิด บัดนี้มารีย์ร้องเพลงเดียวกันเมื่อตั้งครรภ์ผู้ซึ่งจะทรงครองราชย์ในฐานะพระมหากษัตริย์แห่งกษัตริย์ทั้งปวง
- Key decisions:
  - Μεγαλύνει ἡ ψυχή μου τὸν κύριον → จิตวิญญาณของข้าพเจ้าเทิดทูนองค์พระผู้เป็นเจ้า — Per uW figs-synecdoche: 'soul' = 'whole self' / 'inmost being.' μεγαλύνω = 'make great / magnify / extol.' Thai เทิดทูน ('lift-up-in-honor') captures the worshipful-exalting sense. จิตวิญญาณ ('spirit-soul') standard...
- Notes: THE MAGNIFICAT BEGINS (vv.46-55). Mary's song is nearly a pastiche of 1 Samuel 2:1-10 (Hannah's Song) and Psalm themes. Its structure: (A) Personal praise (vv.46-49) — God has done great things for me; (B) General praise (vv.50-53) — God reverses the mighty and the humble; (C) Covenantal praise (vv.54-55) — God keeps his promises to Abraham. T...

**Luke 1:47**
- GR: καὶ ἠγαλλίασεν τὸ πνεῦμά μου ἐπὶ τῷ θεῷ τῷ σωτῆρί μου·
- TH: และจิตของข้าพเจ้าปีติยินดีในพระเจ้าพระผู้ช่วยให้รอดของข้าพเจ้า
- Key decisions:
  - ἠγαλλίασεν τὸ πνεῦμά μου → จิตของข้าพเจ้าปีติยินดี — Per uW figs-synecdoche: 'spirit' parallel to 'soul' (v.46) — whole inner person. Per uW figs-idiom: aorist ἠγαλλίασεν past-tense-for-present/vivid-state. ἀγαλλιάω = 'exult / rejoice greatly' (intensive of χαίρω). Th...
  - ἐπὶ τῷ θεῷ τῷ σωτῆρί μου → ในพระเจ้าพระผู้ช่วยให้รอดของข้าพเจ้า — Per uW figs-metonymy: 'God the Savior' — God AS Savior. σωτήρ → พระผู้ช่วยให้รอด standard Thai Christian title. Direct LXX echo of Hab 3:18 (χαρήσομαι ἐπὶ τῷ θεῷ τῷ σωτῆρί μου), and theme from Ps 35:9 LXX. Mary call...
- Notes: DIRECT LXX VERBAL ECHO: Hab 3:18 LXX (ἐγὼ δὲ ἐν τῷ κυρίῳ ἀγαλλιάσομαι, χαρήσομαι ἐπὶ τῷ θεῷ τῷ σωτῆρί μου). Mary's song draws on Habakkuk's joy-in-God-despite-imminent-judgment. The parallel to 1 Sam 2:1 is also direct (ηὐφράνθην ἐν σωτηρίᾳ σου — Hannah 'rejoices in your salvation'). Theological weight: Mary identifies God as HER Savior — stan...

**Luke 1:48**
- GR: ὅτι ἐπέβλεψεν ἐπὶ τὴν ταπείνωσιν τῆς δούλης αὐτοῦ, ἰδοὺ γὰρ ἀπὸ τοῦ νῦν μακαριοῦσίν με πᾶσαι αἱ γενεαί·
- TH: เพราะพระองค์ทอดพระเนตรสถานะอันต่ำต้อยของทาสหญิงของพระองค์ ดูเถิด ตั้งแต่นี้ต่อไปคนทุกชั่วอายุจะเรียกข้าพเจ้าว่าผู้เป็นสุข
- TH-summary: มารีย์ใช้ถ้อยคำของฮันนาห์ใน 1 ซามูเอล 1:11 «ทอดพระเนตรความยากลำบากของผู้รับใช้ของพระองค์» คำว่า «ทาสหญิง» (ดูลี) แสดงถึงความสมถะของมารีย์ต่อพระพักตร์พระเจ้า การที่พระเจ้าทรงเลือกหญิงสาวบ้านนอกจากเมืองเล็กๆ อย่างนาซาเร็ธ แทนที่จะเลือกสตรีชั้นสูงในเยรูซาเล็ม เป็นการพลิกโฉมค่านิยมของโลก
- Key decisions:
  - ἐπέβλεψεν ἐπὶ τὴν ταπείνωσιν τῆς δούλης αὐτοῦ → พระองค์ทอดพระเนตรสถานะอันต่ำต้อยของทาสหญิงของพระองค์ — Per uW figs-idiom/figs-metonymy: 'looked upon' = 'shown regard for.' ταπείνωσις = 'humble/lowly condition' (not passive humility-virtue but objective-low-status). Direct verbatim echo of 1 Sam 1:11 LXX (Hannah: εἰ ἐ...
  - ἰδοὺ γὰρ ἀπὸ τοῦ νῦν μακαριοῦσίν με πᾶσαι αἱ γενεαί → ดูเถิด ตั้งแต่นี้ต่อไปคนทุกชั่วอายุจะเรียกข้าพเจ้าว่าผู้เป็นสุข — Per uW figs-metonymy: 'all generations' = all future peoples. μακαρίζω = 'call/consider blessed.' Thai ทุกชั่วอายุ (every generation) + จะเรียกข้าพเจ้าว่าผู้เป็นสุข preserves both halves (generations + blessing). Pr...
- Notes: DIRECT LXX VERBATIM ECHO: 1 Sam 1:11 LXX (Hannah's vow — ἐπὶ τὴν ταπείνωσιν τῆς δούλης σου). Mary does not simply 'allude' here — she adopts Hannah's exact language. Theologically, Hannah-typology: both women receive miraculous-child, both sing responsive songs celebrating reversal, both dedicate their child to God's purpose. Note Mary's remar...

**Luke 1:49**
- GR: ὅτι ἐποίησέν μοι μεγάλα ὁ δυνατός, καὶ ἅγιον τὸ ὄνομα αὐτοῦ,
- TH: เพราะองค์ผู้ทรงฤทธิ์ได้ทรงกระทำสิ่งยิ่งใหญ่แก่ข้าพเจ้า พระนามของพระองค์ทรงบริสุทธิ์
- Key decisions:
  - ἐποίησέν μοι μεγάλα ὁ δυνατός → องค์ผู้ทรงฤทธิ์ได้ทรงกระทำสิ่งยิ่งใหญ่แก่ข้าพเจ้า — Per uW figs-metonymy: ὁ δυνατός 'the Mighty One' — God by attribute. Thai องค์ผู้ทรงฤทธิ์ (the Mighty-powerful One, divine honorific). Royal verb ทรงกระทำ per §3. μεγάλα neuter plural = 'great things' — direct echo ...
  - ἅγιον τὸ ὄνομα αὐτοῦ → พระนามของพระองค์ทรงบริสุทธิ์ — Per uW figs-metonymy: 'name' = the person himself, his reputation. Thai พระนาม (royal name) + ทรงบริสุทธิ์ (royal + holy). Direct echo of Ps 111:9 LXX (ἅγιον καὶ φοβερὸν τὸ ὄνομα αὐτοῦ). This is one of the central O...
- Notes: MULTIPLE DIRECT OT VERBAL ECHOES: (1) Deut 10:21 LXX (ὅτι αὐτὸς ἡ καύχησίς σου καὶ αὐτὸς ὁ θεός σου, ὅστις ἐποίησέν σοι τὰ μεγάλα) — Moses's charge to Israel. (2) Ps 111:9 LXX (ἅγιον καὶ φοβερὸν τὸ ὄνομα αὐτοῦ) — 'holy is his name.' (3) Ps 71:19 LXX (τίς ὅμοιός σοι, ὁ θεός, ὁ ποιῶν μεγάλα). Mary's Magnificat is the densest OT-allusive-poetry i...

**Luke 1:50**
- GR: καὶ τὸ ἔλεος αὐτοῦ εἰς γενεὰς καὶ γενεὰς τοῖς φοβουμένοις αὐτόν.
- TH: พระเมตตาของพระองค์แผ่ไปถึงบรรดาผู้ยำเกรงพระองค์ทุกชั่วอายุ
- Key decisions:
  - τὸ ἔλεος αὐτοῦ εἰς γενεὰς καὶ γενεὰς → พระเมตตาของพระองค์แผ่ไปถึง...ทุกชั่วอายุ — Per uW figs-idiom: 'generations and generations' = every generation. ἔλεος → พระเมตตา (royal-prefix mercy) — established biblical Thai rendering. Direct echo of Ps 103:17 LXX (τὸ δὲ ἔλεος τοῦ κυρίου ἀπὸ τοῦ αἰῶνος κ...
  - τοῖς φοβουμένοις αὐτόν → บรรดาผู้ยำเกรงพระองค์ — Per uW figs-idiom: 'fearing' = reverence/awe, not terror. φοβέομαι present middle ptc. Thai ยำเกรง (reverence-awe) standard Christian Thai rendering for religious-fear. Direct echo of Ps 103:17
- Notes: DIRECT LXX VERBAL ECHO: Ps 103:17 (LXX Ps 102:17 — τὸ δὲ ἔλεος τοῦ κυρίου ἀπὸ τοῦ αἰῶνος καὶ ἕως τοῦ αἰῶνος ἐπὶ τοὺς φοβουμένους αὐτόν). The transition from personal praise (vv.46-49) to general-universal praise (vv.50-53). The 'fearing God' category links back to priestly covenantal piety (Zechariah and Elizabeth, v.6) — Mary stands in their ...

**Luke 1:51**
- GR: Ἐποίησεν κράτος ἐν βραχίονι αὐτοῦ, διεσκόρπισεν ὑπερηφάνους διανοίᾳ καρδίας αὐτῶν·
- TH: พระองค์ได้ทรงสำแดงฤทธานุภาพด้วยพระกรของพระองค์ ทรงกระจัดกระจายคนที่หยิ่งผยองในความคิดในใจของเขา
- Key decisions:
  - Ἐποίησεν κράτος ἐν βραχίονι αὐτοῦ → พระองค์ได้ทรงสำแดงฤทธานุภาพด้วยพระกรของพระองค์ — Per uW figs-metonymy: 'arm' = power. Classic OT anthropomorphism. ἐν βραχίονι αὐτοῦ = 'with his arm' (Exodus-like imagery of divine-warrior). Thai พระกร (royal arm) preserves both literal-body-part-as-honorific and ...
  - διεσκόρπισεν ὑπερηφάνους διανοίᾳ καρδίας αὐτῶν → ทรงกระจัดกระจายคนที่หยิ่งผยองในความคิดในใจของเขา — Per uW figs-metaphor: 'scattered' = defeated-dispersed. ὑπερηφάνους = 'arrogant/proud.' Per uW figs-metaphor: 'hearts' = will/affection. Thai หยิ่งผยอง (proud-arrogant) + ความคิดในใจ (thoughts-in-heart) preserves du...
- Notes: MAGNIFICAT TRANSITION TO REVERSAL-THEMES (vv.51-53). Mary now moves from personal-praise to sweeping social-apocalyptic reversal — God dethrones the proud, lifts the humble, fills the hungry, empties the rich. This is the great-reversal Lukan theme (cf. 6:20-26 Beatitudes/Woes, 14:11 exalting humble, 16:19-31 Lazarus/rich-man). ARM-OF-GOD imag...

**Luke 1:52**
- GR: καθεῖλεν δυνάστας ἀπὸ θρόνων καὶ ὕψωσεν ταπεινούς,
- TH: ทรงปลดเจ้านายจากบัลลังก์ แต่ทรงยกคนต่ำต้อยให้สูงขึ้น
- Key decisions:
  - καθεῖλεν δυνάστας ἀπὸ θρόνων → ทรงปลดเจ้านายจากบัลลังก์ — Per uW figs-metonymy: 'throne' = rulership. δυνάστης = 'ruler / potentate.' Thai เจ้านาย (ruler/noble) + บัลลังก์ (throne). Royal verb ทรงปลด per §3. Echoes 1 Sam 2:7-8 LXX (ταπεινοῖ καὶ ἀνυψοῖ — 'humbles and exalts...
  - ὕψωσεν ταπεινούς → ทรงยกคนต่ำต้อยให้สูงขึ้น — Per uW figs-metaphor/figs-nominaladj: 'exalted humble-ones.' Per uW grammar-connect-logic-contrast: καί here = 'but' (contrasting-action). Thai แต่...ทรงยก preserves the sharp reversal. Direct echo of 1 Sam 2:7-8 LX...
- Notes: DIRECT VERBAL ECHOES: (1) 1 Sam 2:7-8 LXX — Hannah's song (κύριος πτωχίζει καὶ πλουτίζει, ταπεινοῖ καὶ ἀνυψοῖ). (2) Ezek 21:26 LXX (ἐταπείνωσας τὸ ὑψηλόν...ὕψωσας τὸ ταπεινόν). (3) Ps 113:7-8 LXX (ἐγείρων ἀπὸ γῆς πτωχόν...τοῦ καθίσαι αὐτὸν μετὰ ἀρχόντων). The reversal-theme is so OT-saturated that Mary's song is effectively an anthology-repris...

**Luke 1:53**
- GR: πεινῶντας ἐνέπλησεν ἀγαθῶν καὶ πλουτοῦντας ἐξαπέστειλεν κενούς.
- TH: ทรงให้คนที่หิวอิ่มด้วยของดี แต่ทรงส่งคนร่ำรวยกลับไปมือเปล่า
- Key decisions:
  - πεινῶντας ἐνέπλησεν ἀγαθῶν → ทรงให้คนที่หิวอิ่มด้วยของดี — πεινάω pres.ptc. = 'those-who-hunger.' ἐμπίμπλημι aor. = 'filled.' ἀγαθά = 'good things.' Thai คนที่หิว + อิ่มด้วยของดี preserves the physical-hunger imagery. Royal verb ทรงให้ per §3. Direct echo of Ps 107:9 LXX (ψ...
  - πλουτοῦντας ἐξαπέστειλεν κενούς → แต่ทรงส่งคนร่ำรวยกลับไปมือเปล่า — πλουτέω pres.ptc. = 'those-who-are-rich.' ἐξαποστέλλω aor. = 'sent away.' κενούς = 'empty (handed).' Per uW grammar-connect-logic-contrast. Thai ส่ง...กลับไปมือเปล่า preserves the dismissal-empty-handed imagery. Roy...
- Notes: DIRECT VERBAL ECHO of Ps 107:9 LXX (ψυχὴν πεινῶσαν ἐνέπλησεν ἀγαθῶν). Possibly also Ps 146:7, 1 Sam 2:5 (barren bears seven, many-children-woman languishes). The rich-send-away-empty theme is distinctively Lukan in the NT — reappears in the Rich Fool (12:16-21), Dives and Lazarus (16:19-31), the rich young ruler (18:18-25). Mary's song anticip...

**Luke 1:54**
- GR: ἀντελάβετο Ἰσραὴλ παιδὸς αὐτοῦ, μνησθῆναι ἐλέους,
- TH: ทรงช่วยอิสราเอลผู้รับใช้ของพระองค์ ด้วยทรงระลึกถึงพระเมตตา
- Key decisions:
  - ἀντελάβετο Ἰσραὴλ παιδὸς αὐτοῦ → ทรงช่วยอิสราเอลผู้รับใช้ของพระองค์ — ἀντιλαμβάνομαι = 'take-hold-of to help / come to aid.' Per uW figs-metaphor: 'servant' = Israel's covenant-role. Per uW figs-personification: Israel as single person. Thai ทรงช่วยอิสราเอลผู้รับใช้ของพระองค์ preserve...
  - μνησθῆναι ἐλέους → ด้วยทรงระลึกถึงพระเมตตา — Per uW figs-idiom: 'remember mercy' = 'act in mercy.' μνησθῆναι aor.inf. = 'having-remembered / to remember.' Thai ทรงระลึกถึง (royal remember) + พระเมตตา consistent with v.50 ἔλεος rendering. Royal prefix preserved
- Notes: MAGNIFICAT CONCLUDING-MOVEMENT (vv.54-55). Mary moves from reversal-theme to covenantal-theme: the God-who-reverses is the God-who-keeps-promises-to-Abraham. Direct verbal echo of Isa 41:8-10 LXX (Israel my servant, whom I have taken-hold-of — ἀντελαβόμην). Also echoes Ps 98:3 (ἐμνήσθη τοῦ ἐλέους αὐτοῦ τῷ Ιακωβ). The παῖς = 'servant/child' ech...

**Luke 1:55**
- GR: καθὼς ἐλάλησεν πρὸς τοὺς πατέρας ἡμῶν, τῷ Ἀβραὰμ καὶ τῷ σπέρματι αὐτοῦ εἰς τὸν αἰῶνα.
- TH: ตามที่พระองค์ได้ตรัสแก่บรรพบุรุษของเรา แก่อับราฮัมและพงศ์พันธุ์ของท่านสืบไปเป็นนิตย์»
- TH-summary: เพลงของมารีย์จบลงด้วยการอ้างถึงพันธสัญญากับอับราฮัม (ปฐมกาล 12, 15, 17, 22) มารีย์เข้าใจว่าสิ่งที่กำลังจะเกิดขึ้น — การประสูติของบุตรของนาง — เป็นความสำเร็จของคำสัญญาโบราณแห่งเชื้อสายของอับราฮัมที่จะเป็นพระพรแก่ประชาชาติทั้งหลาย (ปฐก 12:3, 22:17-18)
- Key decisions:
  - καθὼς ἐλάλησεν πρὸς τοὺς πατέρας ἡμῶν → ตามที่พระองค์ได้ตรัสแก่บรรพบุรุษของเรา — Per uW figs-metaphor: 'fathers' = 'ancestors.' Royal verb ตรัส per §3. Thai บรรพบุรุษ standard
  - τῷ Ἀβραὰμ καὶ τῷ σπέρματι αὐτοῦ εἰς τὸν αἰῶνα → แก่อับราฮัมและพงศ์พันธุ์ของท่านสืบไปเป็นนิตย์ — Per uW figs-metaphor: σπέρμα = 'seed' = descendants. Thai พงศ์พันธุ์ (clan/descendants) preserves the collective-descent sense natural for Thai. εἰς τὸν αἰῶνα = 'forever' consistent with v.33. Ἀβραάμ → อับราฮัม stan...
- Notes: MAGNIFICAT CONCLUSION. Mary grounds the present-moment in the Abrahamic covenant — God's salvation-action through her child is the keeping-of-ancient-promise. ABRAHAMIC-COVENANT ECHOES: Gen 12:3 (in you all the families of earth blessed), Gen 17:7 (covenant for your seed after you), Gen 22:17-18 (seed shall bless nations), Mic 7:20 (show mercy...

**Luke 1:56**
- GR: Ἔμεινεν δὲ Μαριὰμ σὺν αὐτῇ ὡς μῆνας τρεῖς, καὶ ὑπέστρεψεν εἰς τὸν οἶκον αὐτῆς.
- TH: มารีย์พักอยู่กับเอลีซาเบธประมาณสามเดือน แล้วจึงกลับไปยังบ้านของตน
- Key decisions:
  - Ἔμεινεν...σὺν αὐτῇ ὡς μῆνας τρεῖς → มารีย์พักอยู่กับเอลีซาเบธประมาณสามเดือน — μένω = 'stay / remain.' ὡς + μῆνας τρεῖς = 'about three months.' Per uW writing-pronouns: first αὐτῇ = Elizabeth; Elizabeth's name inserted for clarity per Thai style. Mary's three-month stay brings her visit to rou...
  - ὑπέστρεψεν εἰς τὸν οἶκον αὐτῆς → แล้วจึงกลับไปยังบ้านของตน — ὑποστρέφω = 'return' — Lukan favorite verb (32x in Luke-Acts, rare elsewhere). Per uW writing-pronouns: second αὐτῆς = Mary. Thai กลับไปยังบ้านของตน — 'her own home' (tn ตน 'self' disambiguates)
- Notes: Chronological note: Elizabeth was 6 months pregnant at the time of Gabriel's annunciation to Mary (v.26, 36); Mary travels to her 'with haste' (v.39), stays 3 months (v.56), so if Mary's arrival was in Elizabeth's 6th month, Mary leaves around the time of John's birth — but Luke unusually has Mary leave BEFORE narrating the birth (v.57). This ...

**Luke 1:57**
- GR: Τῇ δὲ Ἐλισάβετ ἐπλήσθη ὁ χρόνος τοῦ τεκεῖν αὐτήν, καὶ ἐγέννησεν υἱόν.
- TH: เมื่อครบกำหนดคลอดของเอลีซาเบธแล้ว นางก็ให้กำเนิดบุตรชาย
- Key decisions:
  - ἐπλήσθη ὁ χρόνος τοῦ τεκεῖν → เมื่อครบกำหนดคลอด — Per uW figs-activepassive: 'time was fulfilled for bearing.' Hebraic idiom — same πληρόω verb as v.20 (prophecy fulfillment) and v.23 (days fulfilled). Thai ครบกำหนดคลอด natural
  - ἐγέννησεν υἱόν → ให้กำเนิดบุตรชาย — γεννάω = 'bear / give birth.' Thai ให้กำเนิดบุตรชาย natural
- Notes: Parallels Gen 25:24 (τοῦ τεκεῖν αὐτήν — Rebekah's delivery of Esau/Jacob) and 1 Sam 1:20 (Hannah bears Samuel 'when the time came'). The birth itself is narrated minimally — Luke's focus is on the community-response (v.58-66), not the biological event.

**Luke 1:58**
- GR: καὶ ἤκουσαν οἱ περίοικοι καὶ οἱ συγγενεῖς αὐτῆς ὅτι ἐμεγάλυνεν κύριος τὸ ἔλεος αὐτοῦ μετ᾽ αὐτῆς, καὶ συνέχαιρον αὐτῇ.
- TH: เพื่อนบ้านและญาติของนางได้ยินว่าองค์พระผู้เป็นเจ้าทรงสำแดงพระเมตตาอันยิ่งใหญ่แก่นาง พวกเขาจึงพลอยยินดีกับนาง
- Key decisions:
  - οἱ περίοικοι → เพื่อนบ้าน — HAPAX: περίοικος (only here in NT; cognate verb περιοικέω v.65 is also hapax). 'Those living around' = neighbors. Thai เพื่อนบ้าน natural
  - οἱ συγγενεῖς → ญาติ — συγγενής = 'relative / kinsperson.' Thai ญาติ standard
  - ἐμεγάλυνεν κύριος τὸ ἔλεος αὐτοῦ μετ᾽ αὐτῆς → องค์พระผู้เป็นเจ้าทรงสำแดงพระเมตตาอันยิ่งใหญ่แก่นาง — Per uW figs-metaphor/figs-explicit: 'magnified mercy with/toward her.' Echoes Mary's μεγαλύνει in v.46 — inclusio/theme-continuation: Mary magnifies God; God magnifies mercy. Thai ทรงสำแดงพระเมตตาอันยิ่งใหญ่ natural...
  - συνέχαιρον αὐτῇ → พวกเขาจึงพลอยยินดีกับนาง — συγχαίρω = 'rejoice-together-with.' Thai พลอยยินดี (share-in-joy) — natural rendering of the sympathetic-joy sense
- Notes: NT HAPAX: περίοικος (only here; cf. περιοικέω v.65 also hapax). The joy-theme from v.14 (the angel's promise that many would rejoice at John's birth) is now fulfilled. The echo of Mary's μεγαλύνει from v.46 is deliberate — Mary's magnification-of-God is paired with God's magnification-of-mercy.

**Luke 1:59**
- GR: Καὶ ἐγένετο ἐν τῇ ἡμέρᾳ τῇ ὀγδόῃ ἦλθον περιτεμεῖν τὸ παιδίον, καὶ ἐκάλουν αὐτὸ ἐπὶ τῷ ὀνόματι τοῦ πατρὸς αὐτοῦ Ζαχαρίαν.
- TH: อยู่มาในวันที่แปด พวกเขามาเพื่อทำพิธีเข้าสุหนัตให้เด็ก และตั้งใจจะตั้งชื่อเด็กตามชื่อบิดาว่าเศคาริยาห์
- TH-summary: การเข้าสุหนัตในวันที่แปดเป็นพระบัญญัติที่ผูกพันกับอับราฮัม (ปฐมกาล 17:12) ญาติมิตรคาดหวังว่าชื่อของเด็กจะเป็น «เศคาริยาห์จูเนียร์» ตามชื่อบิดา ซึ่งเป็นธรรมเนียมทั่วไปในครอบครัวยิว แต่พระเจ้าทรงมีแผนอื่น
- Key decisions:
  - ἐν τῇ ἡμέρᾳ τῇ ὀγδόῃ → ในวันที่แปด — Per uW translate-ordinal: eighth day of life. Thai ในวันที่แปด natural. Per uW figs-explicit: circumcision day per Gen 17:12, Lev 12:3
  - περιτεμεῖν τὸ παιδίον → ทำพิธีเข้าสุหนัตให้เด็ก — περιτέμνω = 'circumcise.' Per uW figs-explicit: covenantal ceremony. Thai พิธีเข้าสุหนัต standard Thai Christian rendering — same as used in MAT/LUK glossary for circumcision
  - ἐκάλουν αὐτὸ ἐπὶ τῷ ὀνόματι τοῦ πατρὸς αὐτοῦ Ζαχαρίαν → ตั้งใจจะตั้งชื่อเด็กตามชื่อบิดาว่าเศคาริยาห์ — Per uW figs-idiom: imperfect ἐκάλουν = 'were about to name' / 'were going to call' (conative/tendential imperfect). Per uW figs-idiom: 'calling name upon' = 'giving name.' Thai ตั้งใจจะตั้งชื่อ preserves the intent-...
- Notes: Eighth-day circumcision per Abrahamic covenant (Gen 17:12) — infant-covenant-inclusion. Naming during circumcision was not Torah-mandated but became Jewish custom. The default expectation of patronymic naming (Zechariah after Zechariah — 'junior') is a cultural setup for the surprising reversal in v.60-63 when Elizabeth insists 'No! He shall b...

**Luke 1:60**
- GR: καὶ ἀποκριθεῖσα ἡ μήτηρ αὐτοῦ εἶπεν· Οὐχί, ἀλλὰ κληθήσεται Ἰωάννης.
- TH: แต่มารดาของเด็กตอบว่า «ไม่ได้ เด็กนี้ต้องชื่อยอห์น»
- Key decisions:
  - ἀποκριθεῖσα...εἶπεν → ตอบว่า — Per uW figs-hendiadys: 'answering said' = 'responded.' Thai ตอบ...ว่า natural
  - Οὐχί → ไม่ได้ — Emphatic negative. Thai ไม่ได้ ('it-cannot-be') preserves the strong refusal
  - ἀλλὰ κληθήσεται Ἰωάννης → เด็กนี้ต้องชื่อยอห์น — Per uW figs-activepassive: future-passive = 'shall be named.' Thai ต้องชื่อ ('must be named') preserves the imperative-force. Ἰωάννης → ยอห์น consistent glossary
- Notes: Elizabeth's 'No!' is startling — we don't know how she learned the name (Zechariah couldn't speak to tell her). Possibilities: (a) Zechariah had written it on a tablet earlier; (b) Elizabeth received the name by Spirit-revelation paralleling Mary's (v.41 she was Spirit-filled); (c) signs-and-gestures communication filled the gap. The text is s...

**Luke 1:61**
- GR: καὶ εἶπαν πρὸς αὐτὴν ὅτι Οὐδείς ἐστιν ἐκ τῆς συγγενείας σου ὃς καλεῖται τῷ ὀνόματι τούτῳ.
- TH: พวกเขากล่าวแก่นางว่า «ไม่มีใครในหมู่ญาติของท่านที่มีชื่อนี้เลย»
- Key decisions:
  - Οὐδείς ἐστιν ἐκ τῆς συγγενείας σου → ไม่มีใครในหมู่ญาติของท่าน — συγγένεια = 'kinship / relatives' (collective). Thai ในหมู่ญาติ natural
  - ὃς καλεῖται τῷ ὀνόματι τούτῳ → ที่มีชื่อนี้เลย — Per uW figs-activepassive: 'who-is-called-by-this-name' = 'who has this name.' Per uW figs-explicit: 'this name' = John specifically. Thai มีชื่อนี้ (with the explicit-name context understood) natural
- Notes: The relatives' objection: patronymic-or-family-name naming was strongly expected. Breaking with that tradition was socially striking. Their objection sets up the dramatic surprise of v.63 when Zechariah confirms the unusual name, and the community realizes this is divine-revelation, not parental caprice (v.65-66 community 'awe').

**Luke 1:62**
- GR: ἐνένευον δὲ τῷ πατρὶ αὐτοῦ τὸ τί ἂν θέλοι καλεῖσθαι αὐτό.
- TH: พวกเขาจึงทำใบ้ถามบิดาของเด็กว่าจะตั้งชื่อเด็กว่าอย่างไร
- Key decisions:
  - ἐνένευον...τῷ πατρί → ทำใบ้ถามบิดา — HAPAX: ἐννεύω (only here in NT; cognate διανεύω v.22 also hapax). 'Make signs toward / gesture toward.' Thai ทำใบ้ถาม captures gesture-to-ask. Per uW figs-explicit: people assumed Zechariah couldn't hear (signing su...
  - τὸ τί ἂν θέλοι καλεῖσθαι αὐτό → จะตั้งชื่อเด็กว่าอย่างไร — Per uW figs-activepassive: 'what he wished [it] to be called.' τί ἂν θέλοι — optative of indirect deliberative question. Thai จะตั้งชื่อ...ว่าอย่างไร natural embedded-question
- Notes: NT HAPAX: ἐννεύω (only here; cf. διανεύω v.22). Two Luke-1 hapax verbs for gesturing-communication — the muteness-communication-theme is narratively important. The fact that they gestured (rather than spoke) to Zechariah supports the theory that some assumed he was also deaf, though the text does not settle this.

**Luke 1:63**
- GR: καὶ αἰτήσας πινακίδιον ἔγραψεν λέγων· Ἰωάννης ἐστὶν ὄνομα αὐτοῦ. καὶ ἐθαύμασαν πάντες.
- TH: เศคาริยาห์ขอแผ่นจารึก แล้วเขียนว่า «ชื่อของเขาคือยอห์น» ทุกคนต่างประหลาดใจ
- Key decisions:
  - αἰτήσας πινακίδιον → ขอแผ่นจารึก — HAPAX: πινακίδιον (only here in NT; diminutive of πίναξ 'board/plate'). Per uW translate-unknown: wooden writing-tablet, typically wax-covered for stylus use. Thai แผ่นจารึก ('writing-tablet/plate') captures the anc...
  - Ἰωάννης ἐστὶν ὄνομα αὐτοῦ → ชื่อของเขาคือยอห์น — Declarative — not proposing but confirming. The present-tense ἐστὶν ('is') is emphatic: not 'shall-be' but 'IS' — the name is already settled in God's decree. Thai ชื่อของเขาคือยอห์น natural
  - ἐθαύμασαν πάντες → ทุกคนต่างประหลาดใจ — θαυμάζω aorist = 'marveled.' Thai ประหลาดใจ standard. The marvel is not just the unusual name but that BOTH parents independently produced it — clear sign of divine revelation
- Notes: NT HAPAX: πινακίδιον (only here; cognate πίναξ occurs elsewhere — Matt 14:8, Luke 11:39 — but the diminutive 'little-board' is unique here). Wooden wax-tablets were standard writing-surfaces for short notes — the writer used a stylus to inscribe in the wax. Zechariah's written declaration is emphatic: 'John IS (ἐστίν) his name' — present tense...

**Luke 1:64**
- GR: ἀνεῴχθη δὲ τὸ στόμα αὐτοῦ παραχρῆμα καὶ ἡ γλῶσσα αὐτοῦ, καὶ ἐλάλει εὐλογῶν τὸν θεόν.
- TH: ในทันใดนั้น ปากและลิ้นของเศคาริยาห์ก็เปิดออก ท่านพูดได้และสรรเสริญพระเจ้า
- TH-summary: เกือบสิบเดือนผ่านไปตั้งแต่ทูตสวรรค์ลงโทษเศคาริยาห์ให้เป็นใบ้ (ข้อ 20) บัดนี้เมื่อท่านเชื่อและทำตามคำของทูตสวรรค์เรื่องชื่อของเด็ก ของประทานแห่งการพูดก็ได้รับกลับคืน คำแรกที่ท่านพูดคือการสรรเสริญพระเจ้า — ท่านไม่ได้ใช้เวลาเป็นใบ้ทั้งเก้าเดือนเปล่าประโยชน์ แต่ได้ไตร่ตรองและเตรียมคำพยากรณ์ในข้อ 67-79
- Key decisions:
  - ἀνεῴχθη δὲ τὸ στόμα αὐτοῦ παραχρῆμα καὶ ἡ γλῶσσα αὐτοῦ → ในทันใดนั้น ปากและลิ้นของเศคาริยาห์ก็เปิดออก — Per uW figs-parallelism/figs-metonymy/figs-activepassive: 'mouth opened and tongue [opened]' — Hebraic doublet-for-speech-returning. παραχρῆμα = 'immediately/at-that-moment.' Thai ปากและลิ้น...ก็เปิดออก preserves bo...
  - ἐλάλει εὐλογῶν τὸν θεόν → ท่านพูดได้และสรรเสริญพระเจ้า — ἐλάλει imperfect inchoative = 'began to speak / kept speaking.' εὐλογῶν present ptc. = 'blessing/praising.' Per uW: bless = praise in this context. Thai พูดได้และสรรเสริญ natural — the content of the speech is the B...
- Notes: The muteness that began with Zechariah's doubt (v.20) ends at the moment of Zechariah's faith-act (confirming 'John IS his name' in v.63). The narrative structure makes the discipline both real and temporary — designed to produce trust, not perpetual-silence. The first words after restoration are praise — his pent-up worship breaks forth. The ...

**Luke 1:65**
- GR: καὶ ἐγένετο ἐπὶ πάντας φόβος τοὺς περιοικοῦντας αὐτούς, καὶ ἐν ὅλῃ τῇ ὀρεινῇ τῆς Ἰουδαίας διελαλεῖτο πάντα τὰ ῥήματα ταῦτα,
- TH: ทุกคนที่อยู่รอบๆ บ้านของเขาเกิดความเกรงกลัว และเหตุการณ์ทั้งหมดนี้เป็นที่เล่าขานกันทั่วแถบภูเขาของแคว้นยูเดีย
- Key decisions:
  - ἐγένετο ἐπὶ πάντας φόβος τοὺς περιοικοῦντας αὐτούς → ทุกคนที่อยู่รอบๆ บ้านของเขาเกิดความเกรงกลัว — HAPAX: περιοικέω (only here; noun περίοικος v.58 also hapax). 'Dwell around.' Per uW figs-personification/figs-idiom: 'fear came upon' = 'they were in awe.' Per uW figs-idiom: 'fear' here = reverent awe, not terror....
  - ἐν ὅλῃ τῇ ὀρεινῇ τῆς Ἰουδαίας → ทั่วแถบภูเขาของแคว้นยูเดีย — Per uW figs-hyperbole: 'whole hill country' = 'widely throughout.' ὀρεινή = hilly/mountainous region — same as v.39. Thai แถบภูเขา + แคว้นยูเดีย
  - διελαλεῖτο πάντα τὰ ῥήματα ταῦτα → เหตุการณ์ทั้งหมดนี้เป็นที่เล่าขานกัน — Per uW figs-activepassive: 'all these matters/words were being talked about.' διαλαλέω imperfect = 'were thoroughly-talked-through.' ῥήματα here (per uW figs-metonymy parallel to v.37) = 'things / events.' Thai เหตุ...
- Notes: NT HAPAX: περιοικέω (only here). Both περίοικος (v.58, hapax) and περιοικέω (v.65, hapax) appear in the close-knit community-response around John's birth. The verbal-repetition is narratively bracketing this scene — neighbors-joy at v.58 transforms into neighbors-awe at v.65. The 'hill country of Judea' becomes the regional-rumor network — the...

**Luke 1:66**
- GR: καὶ ἔθεντο πάντες οἱ ἀκούσαντες ἐν τῇ καρδίᾳ αὐτῶν, λέγοντες· Τί ἄρα τὸ παιδίον τοῦτο ἔσται; καὶ γὰρ χεὶρ κυρίου ἦν μετ᾽ αὐτοῦ.
- TH: ทุกคนที่ได้ยินต่างก็เก็บเรื่องนี้ไว้ในใจ พลางพูดกันว่า «เด็กคนนี้จะเป็นคนเช่นใดหนอ?» เพราะว่าพระหัตถ์ขององค์พระผู้เป็นเจ้าทรงสถิตกับเขา
- Key decisions:
  - ἔθεντο πάντες οἱ ἀκούσαντες ἐν τῇ καρδίᾳ αὐτῶν → ทุกคนที่ได้ยินต่างก็เก็บเรื่องนี้ไว้ในใจ — Per uW figs-ellipsis/figs-metaphor: 'placed [these things] in their hearts' = pondered carefully, retained. Thai เก็บเรื่องนี้ไว้ในใจ ('stored this matter in heart') preserves the heart-as-storage-place metaphor
  - Τί ἄρα τὸ παιδίον τοῦτο ἔσται → เด็กคนนี้จะเป็นคนเช่นใดหนอ — Per uW figs-rquestion: rhetorical wondering, not genuine information-seeking. Thai เด็กคนนี้จะเป็นคนเช่นใดหนอ preserves the wondering-exclamation
  - χεὶρ κυρίου ἦν μετ᾽ αὐτοῦ → พระหัตถ์ขององค์พระผู้เป็นเจ้าทรงสถิตกับเขา — Per uW figs-metaphor: 'hand of the Lord' = divine power/favor. Thai พระหัตถ์ (royal hand) + ทรงสถิต (royal dwell-with). OT idiom of divine-favor/commissioning (Isa 66:14, 1 Kgs 18:46, Ezra 7:6, Neh 2:8)
- Notes: The concluding-observation of the John-birth-narrative. 'The hand of the Lord was with him' echoes OT elect-person language — used of Moses, Elijah, Ezra, Nehemiah. The community correctly discerns that this child is specially-commissioned. Their question 'what will this child become?' hangs in narrative tension — the answer begins to emerge i...

**Luke 1:67**
- GR: Καὶ Ζαχαρίας ὁ πατὴρ αὐτοῦ ἐπλήσθη πνεύματος ἁγίου καὶ ἐπροφήτευσεν λέγων·
- TH: ส่วนเศคาริยาห์บิดาของเด็ก ก็เต็มเปี่ยมด้วยพระวิญญาณบริสุทธิ์และได้เผยพระวจนะว่า
- TH-summary: นี่คือการเริ่มต้นของเพลง «เบเนดิกตัส» (Benedictus) — เพลงสรรเสริญของเศคาริยาห์ เพลงนี้แบ่งเป็นสองส่วน: ส่วนแรก (ข้อ 68-75) สรรเสริญพระเจ้าที่ทรงส่งพระผู้ช่วยให้รอดจากเชื้อสายของดาวิด ส่วนที่สอง (ข้อ 76-79) เป็นคำพยากรณ์เกี่ยวกับภารกิจของยอห์นผู้เป็นบุตรของเขา เป็นเพลงที่เต็มไปด้วยการอ้างอิงพระคัมภีร์เดิม
- Key decisions:
  - Ζαχαρίας ὁ πατὴρ αὐτοῦ ἐπλήσθη πνεύματος ἁγίου → เศคาริยาห์บิดาของเด็ก ก็เต็มเปี่ยมด้วยพระวิญญาณบริสุทธิ์ — Per uW figs-activepassive/figs-metaphor: parallel with v.41 (Elizabeth) — vessel-Spirit-filling. Consistent glossary. Zechariah joins his wife (v.41), son (v.15 prenatal), and Simeon (2:25) as Spirit-filled prophets...
  - ἐπροφήτευσεν λέγων → ได้เผยพระวจนะว่า — Per uW writing-quotations: direct-quotation-intro. προφητεύω = 'prophesy.' Thai เผยพระวจนะ standard Thai Christian rendering for prophetic-speech
- Notes: Zechariah's Benedictus begins — one of the three Spirit-inspired canticles of Luke 1-2 (Magnificat 1:46-55, Benedictus 1:68-79, Nunc Dimittis 2:29-32). Structurally the Benedictus divides: (A) vv.68-75 theocentric — praising God for Messianic-redemption coming through Davidic line; (B) vv.76-79 addressed to the newborn John — prophetic mission...

**Luke 1:68**
- GR: Εὐλογητὸς κύριος ὁ θεὸς τοῦ Ἰσραήλ, ὅτι ἐπεσκέψατο καὶ ἐποίησεν λύτρωσιν τῷ λαῷ αὐτοῦ,
- TH: «สาธุการแด่องค์พระผู้เป็นเจ้าพระเจ้าของอิสราเอล เพราะพระองค์เสด็จมาเยี่ยมเยียนและได้ทรงไถ่ประชากรของพระองค์
- Key decisions:
  - Εὐλογητὸς κύριος ὁ θεὸς τοῦ Ἰσραήλ → สาธุการแด่องค์พระผู้เป็นเจ้าพระเจ้าของอิสราเอล — Per uW figs-personification: 'God of Israel' — either 'the God whom the people of Israel worship' or collective-personified-Israel. I render literally preserving the OT-formula. εὐλογητός = 'blessed-be' (hymnic bene...
  - ἐπεσκέψατο → พระองค์เสด็จมาเยี่ยมเยียน — Per uW figs-idiom: ἐπισκέπτομαι = 'visit / look upon to help.' LXX-translates פָּקַד (visit in redemptive-sense, cf. Gen 50:24, Exod 3:16, 4:31, Ruth 1:6). Not merely 'visit' but 'visit for salvation.' Royal verb เส...
  - ἐποίησεν λύτρωσιν → ได้ทรงไถ่ — λύτρωσις = 'redemption / ransoming.' ποιέω λύτρωσιν = 'perform redemption.' Thai ทรงไถ่ standard Christian Thai verb for redemptive-action. Prophetic-aorist — redemption is already begun in the conception/coming of Jesus
- Notes: BENEDICTUS OPENING. The εὐλογητός-formula opens standard Jewish hymnic-blessings (Psalms 41:13, 72:18, 89:52, 106:48, 1 Kgs 1:48, 8:15, 1 Chr 29:10). Zechariah adopts this liturgical register to pronounce a new-salvation-act. ἐπεσκέψατο is key — this is the LXX-verb for YHWH's redemptive-visiting (Gen 50:24 Joseph's oath, Exod 3:16 God visitin...

**Luke 1:69**
- GR: καὶ ἤγειρεν κέρας σωτηρίας ἡμῖν ἐν οἴκῳ Δαυὶδ παιδὸς αὐτοῦ,
- TH: และทรงตั้งเขาแห่งความรอดขึ้นแก่เราในเชื้อสายของดาวิดผู้รับใช้ของพระองค์
- TH-summary: «เขาแห่งความรอด» เป็นสำนวนพระคัมภีร์เดิมที่หมายถึง «ผู้ช่วยให้รอดที่แข็งแกร่ง» — เขาของสัตว์เป็นสัญลักษณ์ของกำลังและการปกป้อง (สดุดี 18:2, 89:17, 132:17) «ในเชื้อสายของดาวิด» บ่งชี้ว่าพระเมสสิยาห์จะมาจากราชวงศ์ดาวิด ตามพันธสัญญาที่พระเจ้าทำกับดาวิดใน 2 ซามูเอล 7
- Key decisions:
  - ἤγειρεν κέρας σωτηρίας ἡμῖν → ทรงตั้งเขาแห่งความรอดขึ้นแก่เรา — Per uW figs-metaphor/figs-metonymy: 'raised-up a horn of salvation' — 'horn' as symbol of strength/ruler-authority (OT imagery). Not literal body-part but symbolic-power. Thai เขาแห่งความรอด preserves the OT-metapho...
  - ἐν οἴκῳ Δαυίδ παιδὸς αὐτοῦ → ในเชื้อสายของดาวิดผู้รับใช้ของพระองค์ — Per uW figs-metonymy/figs-explicit/figs-metaphor: 'house of David' = Davidic-lineage; 'servant' = David-who-served-God-faithfully-as-king. Thai เชื้อสายของดาวิด + ผู้รับใช้ preserves both concepts. Δαυίδ → ดาวิด est...
- Notes: DIRECT VERBAL ECHO: Ps 132:17 LXX (ἐκεῖ ἐξανατελῶ κέρας τῷ Δαυιδ — 'there I will make a horn to sprout for David' — the Davidic-throne promise). Also Ps 18:2 (κέρας σωτηρίας μου — 'horn of my salvation'), Ps 89:17, 24, 1 Sam 2:10 (Hannah's song — ὑψώσει κέρας χριστοῦ αὐτοῦ). The 'horn' imagery was widely used for Messianic-expectation (also Da...

**Luke 1:70**
- GR: καθὼς ἐλάλησεν διὰ στόματος τῶν ἁγίων ἀπ᾽ αἰῶνος προφητῶν αὐτοῦ,
- TH: ตามที่พระองค์ตรัสผ่านทางปากของผู้เผยพระวจนะบริสุทธิ์ของพระองค์ตั้งแต่โบราณกาล
- Key decisions:
  - ἐλάλησεν διὰ στόματος τῶν ἁγίων...προφητῶν αὐτοῦ → พระองค์ตรัสผ่านทางปากของผู้เผยพระวจนะบริสุทธิ์ของพระองค์ — Per uW figs-metonymy: 'mouth of prophets' = prophets' speech. Royal verb ตรัส per §3 — even though the speech is through-prophets, the subject-speaker is God. Thai ผู้เผยพระวจนะ standard for προφῆται + บริสุทธิ์ (ho...
  - ἀπ᾽ αἰῶνος → ตั้งแต่โบราณกาล — Per uW figs-idiom: 'from the age' = 'from ancient times / long ago.' Thai ตั้งแต่โบราณกาล natural
- Notes: The hermeneutic-key of the Benedictus: the Messianic-arrival is the fulfillment of OT prophetic-promises. Zechariah does not invent new revelation — he interprets the birth of John in light of long-standing prophetic-scripture. This explicit reference to 'the prophets from ancient times' anchors the Christian-proclamation in continuity with Is...

**Luke 1:71**
- GR: σωτηρίαν ἐξ ἐχθρῶν ἡμῶν καὶ ἐκ χειρὸς πάντων τῶν μισούντων ἡμᾶς,
- TH: คือความรอดให้พ้นจากศัตรูของเรา และพ้นจากเงื้อมมือของคนทั้งปวงที่เกลียดชังเรา
- Key decisions:
  - σωτηρίαν ἐξ ἐχθρῶν ἡμῶν → คือความรอดให้พ้นจากศัตรูของเรา — Per uW figs-abstractnouns: σωτηρία noun can be rendered by verb; I keep as noun ความรอด which is standard Thai Christian theological term. ἐχθρός → ศัตรู standard. ἐκ = 'out of / from.' Thai ให้พ้นจาก = 'to escape from'
  - ἐκ χειρὸς πάντων τῶν μισούντων ἡμᾶς → พ้นจากเงื้อมมือของคนทั้งปวงที่เกลียดชังเรา — Per uW figs-doublet: parallel with previous clause — Hebraic poetic doublet. Per uW figs-metonymy: 'hand' = power/control. Thai เงื้อมมือ ('clutches / hand-grip') preserves the hand-as-power imagery. μισέω → เกลียดช...
- Notes: Direct verbal echo of Ps 18:17 LXX and Ps 106:10 LXX (ἐλυτρώσατο αὐτοὺς ἐκ χειρὸς μισοῦντος — 'ransomed from the hand of the hater'). 'Salvation from enemies' in OT-prophetic-hope typically referred to political-military deliverance (from Assyria/Babylon/Rome). The NT reinterprets this: enemies ultimately are spiritual (sin, death, Satan), tho...

**Luke 1:72**
- GR: ποιῆσαι ἔλεος μετὰ τῶν πατέρων ἡμῶν καὶ μνησθῆναι διαθήκης ἁγίας αὐτοῦ,
- TH: เพื่อทรงสำแดงพระเมตตาต่อบรรพบุรุษของเรา และทรงระลึกถึงพันธสัญญาอันบริสุทธิ์ของพระองค์
- Key decisions:
  - ποιῆσαι ἔλεος μετὰ τῶν πατέρων ἡμῶν → เพื่อทรงสำแดงพระเมตตาต่อบรรพบุรุษของเรา — Per uW figs-metaphor/figs-explicit/figs-parallelism: 'show mercy toward the fathers' = fulfilling promises made to ancestors, which mercy flows to us as descendants. Per uW: preserve parallelism. Thai ทรงสำแดงพระเมต...
  - μνησθῆναι διαθήκης ἁγίας αὐτοῦ → ทรงระลึกถึงพันธสัญญาอันบริสุทธิ์ของพระองค์ — Per uW figs-idiom: 'remember covenant' = 'act on covenant.' διαθήκη → พันธสัญญา established theological term. ἅγιος → บริสุทธิ์ preserves holy-covenant. Royal verb ทรงระลึก per §3
- Notes: The 'holy covenant' is the Abrahamic (v.73) made explicit. The pair 'mercy' + 'covenant' is classic covenant-faithfulness-language (חֶסֶד וֶאֱמוּנָה hesed-emunah, Ps 89:2, 14, 33). Covenant-remembrance is OT theodicy — God's past-promises are the warrant for future-hope (Exod 2:24 'God remembered his covenant with Abraham'; Ps 105:8-9; 106:45)...

**Luke 1:73**
- GR: ὅρκον ὃν ὤμοσεν πρὸς Ἀβραὰμ τὸν πατέρα ἡμῶν, τοῦ δοῦναι ἡμῖν
- TH: คือคำสาบานที่ได้ทรงสาบานแก่อับราฮัมบรรพบุรุษของเรา ว่าจะทรงประทานแก่เรา
- TH-summary: อ้างถึงคำสาบานของพระเจ้าต่ออับราฮัมใน ปฐมกาล 22:16-18 หลังจากที่อับราฮัมได้เตรียมถวายอิสอัค — «เราสาบานด้วยตัวเรา...ในเชื้อสายของเจ้า ประชาชาติทั้งหลายบนแผ่นดินโลกจะได้รับพระพร» เศคาริยาห์เห็นว่าการเกิดของพระเยซูเป็นการสำเร็จของคำสาบานนี้อย่างสมบูรณ์
- Key decisions:
  - ὅρκον ὃν ὤμοσεν πρὸς Ἀβραὰμ τὸν πατέρα ἡμῶν → คำสาบานที่ได้ทรงสาบานแก่อับราฮัมบรรพบุรุษของเรา — Per uW figs-metaphor: 'father Abraham' = ancestor. ὅρκος = oath. Thai คำสาบาน + ทรงสาบาน (royal-swear verb per §3) preserves both noun and verb forms. Ἀβραάμ → อับราฮัม
  - τοῦ δοῦναι ἡμῖν → ว่าจะทรงประทานแก่เรา — Per uW figs-metaphor: τοῦ+infinitive = 'to give.' Royal verb ประทาน per §3 for divine-giving. Sets up the content-of-oath in v.74-75
- Notes: Direct reference to the Abrahamic oath of Gen 22:16-18 LXX (κατ᾽ ἐμαυτοῦ ὤμοσα) — God's solemn self-oath after Abraham's binding-of-Isaac test, promising blessings to all nations through his seed. This is a theologically-central OT text for the Christian-proclamation (quoted in Hebrews 6:13-14 of God's unchangeable purpose). Zechariah identifi...

**Luke 1:74**
- GR: ἀφόβως ἐκ χειρὸς ἐχθρῶν ῥυσθέντας λατρεύειν αὐτῷ
- TH: ว่าเมื่อทรงช่วยเราให้พ้นจากเงื้อมมือของศัตรูแล้ว เราจะได้ปรนนิบัติพระองค์โดยปราศจากความกลัว
- Key decisions:
  - ἐκ χειρὸς ἐχθρῶν ῥυσθέντας → เมื่อทรงช่วยเราให้พ้นจากเงื้อมมือของศัตรู — Per uW figs-activepassive/figs-metonymy: 'hand' = power. ῥύομαι aor.pass.ptc. = 'rescued/delivered.' Consistent with v.71 rendering เงื้อมมือของศัตรู. Royal verb ทรงช่วย per §3
  - ἀφόβως...λατρεύειν αὐτῷ → เราจะได้ปรนนิบัติพระองค์โดยปราศจากความกลัว — Per uW figs-explicit: 'without fear' = without political-enemy-threat; if enemies gone, Israel can worship freely. λατρεύω = 'serve / worship (religiously).' Thai ปรนนิบัติ standard Thai Christian term for religious...
- Notes: The purpose-clause of the Abrahamic-oath: the ultimate end of covenant-deliverance is free-worship of God. Note the theological framework: deliverance-from-enemies is not an end in itself but serves worship. This echoes Exodus 3:12, 7:16, 8:1 (the demand 'let my people go that they may serve me') — liberation-for-worship is the Exodus pattern....

**Luke 1:75**
- GR: ἐν ὁσιότητι καὶ δικαιοσύνῃ ἐνώπιον αὐτοῦ πάσαις ταῖς ἡμέραις ἡμῶν.
- TH: ในความบริสุทธิ์และความชอบธรรมเฉพาะพระพักตร์พระองค์ตลอดวันเวลาทั้งปวงของเรา
- Key decisions:
  - ἐν ὁσιότητι καὶ δικαιοσύνῃ → ในความบริสุทธิ์และความชอบธรรม — Per uW figs-abstractnouns: I keep nouns (standard Thai Christian terms). ὁσιότης = 'holiness / piety' (distinguished from ἁγιωσύνη). δικαιοσύνη = 'righteousness.' Thai ความบริสุทธิ์ + ความชอบธรรม both standard. Dire...
  - ἐνώπιον αὐτοῦ → เฉพาะพระพักตร์พระองค์ — Per uW figs-idiom: 'in his presence' = covenantal relationship. Thai เฉพาะพระพักตร์ royal-register preserves relational-theophanic sense
  - πάσαις ταῖς ἡμέραις ἡμῶν → ตลอดวันเวลาทั้งปวงของเรา — Per uW figs-idiom: 'all our days' = 'for our whole lives.' Thai ตลอดวันเวลาทั้งปวง preserves the comprehensive-lifetime-span
- Notes: The moral-character of covenant-service: holiness + righteousness. This pair is standard OT-LXX covenantal-language (Josh 24:14 LXX ἐν εὐθύτητι καὶ ἐν δικαιοσύνῃ, Wis 9:3 ἐν ὁσιότητι καὶ δικαιοσύνῃ; later Eph 4:24, 1 Thess 2:10). Zechariah articulates the ethical-end of salvation — delivered FROM sin/enemies, delivered FOR holy-living. This is...

**Luke 1:76**
- GR: καὶ σὺ δέ, παιδίον, προφήτης Ὑψίστου κληθήσῃ, προπορεύσῃ γὰρ ἐνώπιον κυρίου ἑτοιμάσαι ὁδοὺς αὐτοῦ,
- TH: ส่วนเจ้า ลูกเอ๋ย เจ้าจะได้ชื่อว่าผู้เผยพระวจนะขององค์ผู้สูงสุด เพราะเจ้าจะเดินนำหน้าเฉพาะพระพักตร์องค์พระผู้เป็นเจ้าเพื่อเตรียมมรรคาของพระองค์
- TH-summary: เศคาริยาห์ในบัดนี้พูดโดยตรงกับทารกยอห์น นี่คือบรรทัดที่โด่งดังที่สุดในเพลงของเขา อ้างถึงคำพยากรณ์ของอิสยาห์ 40:3 («เตรียมมรรคาขององค์พระผู้เป็นเจ้าในถิ่นทุรกันดาร») และมาลาคี 3:1 ยอห์นจะเป็นผู้เผยพระวจนะคนสุดท้ายของยุคเก่า ผู้บุกเบิกให้พระเมสสิยาห์
- Key decisions:
  - καὶ σὺ δέ, παιδίον → ส่วนเจ้า ลูกเอ๋ย — Per uW figs-explicit: Zechariah addresses his son directly. καὶ σὺ δέ = 'and as for you' (emphatic shift from theocentric to filiocentric). παιδίον vocative = 'little-child.' Thai เจ้า ลูกเอ๋ย (familial-intimate add...
  - προφήτης Ὑψίστου κληθήσῃ → เจ้าจะได้ชื่อว่าผู้เผยพระวจนะขององค์ผู้สูงสุด — Per uW figs-idiom/figs-activepassive: 'will be called' = 'will be.' Parallel with v.32 υἱὸς Ὑψίστου (Jesus). Ὕψιστος → องค์ผู้สูงสุด consistent. ผู้เผยพระวจนะ = prophet
  - προπορεύσῃ...ἐνώπιον κυρίου ἑτοιμάσαι ὁδοὺς αὐτοῦ → เจ้าจะเดินนำหน้าเฉพาะพระพักตร์องค์พระผู้เป็นเจ้าเพื่อเตรียมมรรคาของพระองค์ — Per uW figs-idiom/figs-metaphor: 'go before + prepare paths' — herald-imagery, direct echo of Isa 40:3 (ἑτοιμάσατε τὴν ὁδὸν κυρίου) + Mal 3:1 (ἐπιβλέψεται ὁδὸν πρὸ προσώπου μου). Thai เดินนำหน้า + เตรียมมรรคา preser...
- Notes: TRANSITION to the second half of the Benedictus — address to John. The child is called 'prophet of the Most High' — extraordinarily high prophetic-authority, parallel to Jesus's 'Son of the Most High' (v.32). DIRECT DUAL OT CITATION: (1) Isa 40:3 LXX (φωνὴ βοῶντος ἐν τῇ ἐρήμῳ· ἑτοιμάσατε τὴν ὁδὸν κυρίου — 'prepare the way of the Lord'). (2) Ma...

**Luke 1:77**
- GR: τοῦ δοῦναι γνῶσιν σωτηρίας τῷ λαῷ αὐτοῦ ἐν ἀφέσει ἁμαρτιῶν αὐτῶν,
- TH: เพื่อให้ประชากรของพระองค์รู้ถึงความรอด โดยการอภัยบาปของพวกเขา
- Key decisions:
  - τοῦ δοῦναι γνῶσιν σωτηρίας → เพื่อให้...รู้ถึงความรอด — Per uW figs-metonymy: 'give knowledge' = 'teach.' Per uW figs-abstractnouns. Thai ให้...รู้ถึงความรอด natural. σωτηρία → ความรอด established
  - ἐν ἀφέσει ἁμαρτιῶν αὐτῶν → โดยการอภัยบาปของพวกเขา — Per uW figs-abstractnouns: ἐν + dative = 'in/by.' ἄφεσις → การอภัย (per RULES.md §4 glossary, the choice is documented here — standard Thai theological term). ἁμαρτία → บาป established
- Notes: KEY THEOLOGICAL VERSE. Zechariah identifies John's mission: not merely announcing political-liberation (as v.71, 74 might suggest), but preparing-people-to-receive-the-forgiveness-of-sins in the Messiah. This reframes the salvation-hope spiritually — the ultimate enemies are sin (not Rome), and the ultimate deliverance is forgiveness (not poli...

**Luke 1:78**
- GR: διὰ σπλάγχνα ἐλέους θεοῦ ἡμῶν, ἐν οἷς ἐπισκέψεται ἡμᾶς ἀνατολὴ ἐξ ὕψους,
- TH: ด้วยพระเมตตาอันอ่อนโยนของพระเจ้าของเรา ซึ่งโดยพระเมตตานั้น ดวงรุ่งอรุณจากเบื้องสูงจะเสด็จมาเยี่ยมเยียนเรา
- TH-summary: «ดวงรุ่งอรุณ» (อะนาโทเล) เป็นภาพของพระเมสสิยาห์ที่เสด็จมาเหมือนแสงตะวันส่องผ่านความมืด ภาพนี้สะท้อนคำพยากรณ์ของมาลาคี 4:2 «ดวงอาทิตย์แห่งความชอบธรรมจะส่องขึ้น» และอิสยาห์ 9:2 «ประชาชนที่เดินในความมืดได้เห็นแสงสว่างยิ่งใหญ่»
- Key decisions:
  - διὰ σπλάγχνα ἐλέους θεοῦ ἡμῶν → ด้วยพระเมตตาอันอ่อนโยนของพระเจ้าของเรา — σπλάγχνα = 'inward parts / bowels' used figuratively for 'compassion / tenderness' (Semitic idiom — Hebrew רַחֲמִים rahamim from רֶחֶם womb). ἔλεος = mercy. σπλάγχνα ἐλέους = 'tender mercy' (hendiadys). Thai พระเมตต...
  - ἐπισκέψεται ἡμᾶς ἀνατολὴ ἐξ ὕψους → ดวงรุ่งอรุณจากเบื้องสูงจะเสด็จมาเยี่ยมเยียนเรา — Per uW figs-metaphor: ἀνατολή = 'dawn / rising (of sun/star)' — Messianic-symbol. ἐξ ὕψους = 'from on high' = from God. Per uW figs-metonymy: 'on high' = God. ἐπισκέπτομαι same verb as v.68 (redemptive-visiting). Th...
- Notes: TEXTUAL VARIANT: SBLGNT reads ἐπισκέψεται (future indicative middle, 'will visit'); some MSS read ἐπεσκέψατο (aorist, 'has visited'). SBLGNT/NA28/BSB future-tense-reading. ESV/NIV follow future. Our translation follows SBLGNT future-tense ('will visit us'). The past/future tension matches the prophetic-aorist/future interplay throughout the ca...

**Luke 1:79**
- GR: ἐπιφᾶναι τοῖς ἐν σκότει καὶ σκιᾷ θανάτου καθημένοις, τοῦ κατευθῦναι τοὺς πόδας ἡμῶν εἰς ὁδὸν εἰρήνης.
- TH: เพื่อทรงส่องสว่างแก่คนที่อาศัยอยู่ในความมืดและในเงามัจจุราช เพื่อทรงนำเท้าของเราไปสู่ทางแห่งสันติสุข»
- Key decisions:
  - ἐπιφᾶναι τοῖς ἐν σκότει καὶ σκιᾷ θανάτου καθημένοις → ทรงส่องสว่างแก่คนที่อาศัยอยู่ในความมืดและในเงามัจจุราช — Per uW figs-metaphor/figs-idiom/figs-doublet: 'darkness and shadow of death' — Hebraic doublet from Isa 9:2 / Ps 107:10. σκιὰ θανάτου = Hebrew צַלְמָוֶת tsalmavet (the 'valley of shadow' from Ps 23:4). καθημένοις 's...
  - τοῦ κατευθῦναι τοὺς πόδας ἡμῶν εἰς ὁδὸν εἰρήνης → เพื่อทรงนำเท้าของเราไปสู่ทางแห่งสันติสุข — Per uW figs-metaphor/figs-synecdoche: 'guide feet' = 'guide whole person.' I preserve 'feet' for poetic-metaphor preservation (collapse would lose imagery). ὁδὸς εἰρήνης = 'path of peace' — echoes Isa 59:8 (ὁδὸν εἰρ...
- Notes: CONCLUSION OF BENEDICTUS. Multiple OT-allusions converge: (1) Isa 9:2 LXX + Isa 42:7 LXX (opening-blind-eyes, bringing-out-of-darkness). (2) Ps 107:10, 14 LXX (καθημένους ἐν σκότει καὶ σκιᾷ θανάτου — near-verbatim); the Psalmist's account of Israel redeemed from exile. (3) Isa 59:8 LXX (οὐκ οἴδασιν ὁδὸν εἰρήνης). (4) Ps 23:4 LXX (shadow-of-dea...

**Luke 1:80**
- GR: Τὸ δὲ παιδίον ηὔξανε καὶ ἐκραταιοῦτο πνεύματι, καὶ ἦν ἐν ταῖς ἐρήμοις ἕως ἡμέρας ἀναδείξεως αὐτοῦ πρὸς τὸν Ἰσραήλ.
- TH: ส่วนทารกนั้นก็เติบใหญ่ขึ้น เข้มแข็งขึ้นในจิตวิญญาณ และอาศัยอยู่ในถิ่นทุรกันดารจนถึงวันที่เขาจะปรากฏตัวต่อสาธารณะแก่อิสราเอล
- TH-summary: บทที่ 1 จบลงด้วยบทสรุปสั้นๆ เกี่ยวกับการเติบโตของยอห์น ลูกาข้ามช่วงเวลาประมาณ 30 ปี (เปรียบเทียบกับลูกา 3:1 ที่ยอห์นเริ่มเผยพระวจนะในปีที่ 15 ของทีบีเรียส) การที่ยอห์นอาศัยอยู่ในถิ่นทุรกันดารสะท้อนภาพเอลียาห์และเป็นการเตรียมตัวด้านวิญญาณก่อนภารกิจ
- Key decisions:
  - Τὸ δὲ παιδίον ηὔξανε καὶ ἐκραταιοῦτο πνεύματι → ทารกนั้นก็เติบใหญ่ขึ้น เข้มแข็งขึ้นในจิตวิญญาณ — Per uW writing-newevent. αὐξάνω imperfect = 'was growing.' κραταιόω imperfect = 'was-being-strengthened.' Per uW: πνεύματι ambiguous — either (1) 'in spirit' (character-strength) or (2) 'by the Spirit' (Holy Spirit ...
  - ἦν ἐν ταῖς ἐρήμοις ἕως ἡμέρας ἀναδείξεως αὐτοῦ πρὸς τὸν Ἰσραήλ → อาศัยอยู่ในถิ่นทุรกันดารจนถึงวันที่เขาจะปรากฏตัวต่อสาธารณะแก่อิสราเอล — HAPAX: ἀνάδειξις (only here in NT). 'Public appearance / unveiling / installation.' Technical political-term (used of appointing officials to office). Thai ปรากฏตัวต่อสาธารณะ captures public-appearance. ἔρημος → ถิ่...
- Notes: NT HAPAX: ἀνάδειξις ('public appearance / unveiling'). Technical term used of inauguration of civic officials, military commanders. Here it marks John's public-prophetic-debut (Luke 3:1ff). The wilderness-dwelling motif parallels Elijah (1 Kgs 17, 19) — John's prophetic-Elijah-typology continues. The growth-formula ηὔξανε καὶ ἐκραταιοῦτο πνεύμ...


---

### Luke 4

**Luke 4:1**
- GR: Ἰησοῦς δὲ πλήρης πνεύματος ἁγίου ὑπέστρεψεν ἀπὸ τοῦ Ἰορδάνου, καὶ ἤγετο ἐν τῷ πνεύματι ἐν τῇ ἐρήμῳ
- TH: พระเยซูทรงบริบูรณ์ด้วยพระวิญญาณบริสุทธิ์ เสด็จกลับจากแม่น้ำจอร์แดน และพระวิญญาณทรงนำพระองค์เข้าไปในถิ่นทุรกันดาร
- TH-summary: ลูกาเชื่อมฉากนี้เข้ากับการรับบัพติศมา (3:21-22) และลำดับพงศ์พันธุ์ (3:23-38) อย่างแนบแน่น พระเยซูผู้เป็น «อาดัมคนที่สอง» (เทียบ รม 5:14; 1คร 15:45) เสด็จเข้าสู่ถิ่นทุรกันดารเพื่อถูกทดลอง ขณะที่อาดัมคนแรกล้มเหลวในสวนเอเดน พระเยซูทรงชนะในถิ่นทุรกันดาร คำว่า «บริบูรณ์ด้วยพระวิญญาณบริสุทธิ์» (πλήρης πνεύματος ἁγίου) เป็นลักษณะเฉพาะของลูกา (เทียบ กจ 6:3, 5; 7:55; 11:24) เน้นย้ำว่าพระเยซูทรงทำพันธกิจภายใต้พลังของพระวิญญาณตลอด
- Key decisions:
  - Ἰησοῦς δὲ → พระเยซู — Per uW writing-newevent: δέ transitions from genealogy (3:23-38) back to narrative. Thai leaves transition implicit (no need for «ส่วน» or «แล้ว») since flow is clear.
  - πλήρης πνεύματος ἁγίου → ทรงบริบูรณ์ด้วยพระวิญญาณบริสุทธิ์ — πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์ (RULES.md §4 non-negotiable). πλήρης = 'full' — Thai บริบูรณ์ (filled-to-fullness, spiritual sense) is the standard biblical Thai idiom, used already in LUK 1:15 (John), 1:41 (Eliza...
  - ὑπέστρεψεν ἀπὸ τοῦ Ἰορδάνου → เสด็จกลับจากแม่น้ำจอร์แดน — ὑποστρέφω is a Lukan favorite (32x in Luke-Acts, only 3x elsewhere NT). Divine subject → เสด็จกลับ (royal register for movement). Ἰορδάνης → แม่น้ำจอร์แดน (standard Thai Christian; established Mt 3:6 family).
  - ἤγετο ἐν τῷ πνεύματι ἐν τῇ ἐρήμῳ → พระวิญญาณทรงนำพระองค์เข้าไปในถิ่นทุรกันดาร — ἤγετο imperfect-passive — sustained being-led, not just a single departure. Per uW figs-activepassive: Thai actives the passive with explicit agent «พระวิญญาณทรงนำ». Contrast Mark 1:12 (ἐκβάλλει 'drives out' — force...
- Notes: Opening of Temptation Narrative (vv.1-13), synoptic parallel with Matt 4:1-11 and Mark 1:12-13. Luke's order of temptations differs from Matthew — Luke has bread → kingdoms → temple, Matthew has bread → temple → kingdoms. Most scholars (Fitzmyer, Bock, Marshall) hold Matthew preserves chronological order (ending with Satan's 'begone' dismissal...

**Luke 4:2**
- GR: ἡμέρας τεσσεράκοντα πειραζόμενος ὑπὸ τοῦ διαβόλου. καὶ οὐκ ἔφαγεν οὐδὲν ἐν ταῖς ἡμέραις ἐκείναις, καὶ συντελεσθεισῶν αὐτῶν ἐπείνασεν.
- TH: สี่สิบวัน ทรงถูกมารทดลอง ในวันเหล่านั้นพระองค์มิได้เสวยสิ่งใดเลย และเมื่อวันเหล่านั้นสิ้นสุดลง พระองค์ก็ทรงหิว
- TH-summary: สี่สิบวันสะท้อนภาพโมเสสบนภูเขาซีนาย (อพย 34:28) และเอลียาห์เดินทางสี่สิบวันสู่ภูเขาโฮเรบ (1พกษ 19:8) — ทั้งสองอดอาหารสี่สิบวันก่อนพบกับพระเจ้า พระเยซูเสด็จเข้าสู่แบบอย่างนี้ในฐานะผู้ทรงสำเร็จพันธสัญญา การไม่เสวยสิ่งใดเลยเป็นการอดอาหารเต็มรูปแบบ (ไม่ใช่แค่การละเนื้อ) ประเด็นสำคัญคือ «τεσσεράκοντα» ซึ่งทั้งอิสราเอลเดินวนในถิ่นทุรกันดารสี่สิบปีก็เพราะไม่เชื่อฟัง — พระเยซูในฐานะ «อิสราเอลที่แท้จริง» ทรงผ่านการทดสอบสี่สิบวันได้
- Key decisions:
  - ἡμέρας τεσσεράκοντα πειραζόμενος → สี่สิบวัน ทรงถูกมารทดลอง — Per uW figs-verbs: πειραζόμενος present-passive-participle indicates *continuous* testing throughout the 40 days, not just at the end. Thai «ทรงถูกมารทดลอง» (divine-subject passive) conveys the continuity; adding an...
  - διαβόλου → มาร — διάβολος (slanderer/accuser) → มาร (RULES.md §4 adjacent practice; established MAT 4:1, MRK 1:13 via σατανᾶς=ซาตาน, but Matthew uses ο διάβολος=มาร). Thai มาร = generic evil-adversary (Pali-Sanskrit loanword, also u...
  - καὶ οὐκ ἔφαγεν οὐδὲν → พระองค์มิได้เสวยสิ่งใดเลย — Per uW writing-pronouns: Greek leaves the subject implicit; English and Thai must add «พระองค์» to disambiguate (Jesus, not the devil, fasted). Divine subject → royal เสวย (eat); double-negative οὐκ...οὐδέν emphasiz...
  - συντελεσθεισῶν αὐτῶν ἐπείνασεν → เมื่อวันเหล่านั้นสิ้นสุดลง พระองค์ก็ทรงหิว — συντελέω aorist-passive-participle genitive-absolute = 'those [days] having been completed.' Thai «เมื่อวันเหล่านั้นสิ้นสุดลง» preserves the temporal clause. Divine subject hunger → ทรงหิว (royal).
- Notes: Forty days echoes Moses (Ex 34:28; Deut 9:9) and Elijah (1 Kgs 19:8), both of whom fasted 40 days in wilderness encounter with God. Forty years of Israel's wilderness wandering (Num 14:33-34) is the deeper typological backdrop — Jesus as true Israel succeeds where the nation failed. The distinction between Luke's 'tempted throughout 40 days' a...

**Luke 4:3**
- GR: εἶπεν δὲ αὐτῷ ὁ διάβολος· Εἰ υἱὸς εἶ τοῦ θεοῦ, εἰπὲ τῷ λίθῳ τούτῳ ἵνα γένηται ἄρτος.
- TH: มารจึงทูลพระองค์ว่า «ถ้าท่านเป็นพระบุตรของพระเจ้า จงสั่งหินก้อนนี้ให้กลายเป็นขนมปัง»
- TH-summary: คำทดลองแรกนี้เน้นการใช้อำนาจพระบุตรเพื่อประโยชน์ตนเอง มารเรียกพระองค์ว่า «พระบุตรของพระเจ้า» ซึ่งเป็นคำที่เสียงสวรรค์เพิ่งตรัสที่บัพติศมา (ลก 3:22) — มารไม่ได้สงสัยว่าพระเยซูเป็นพระบุตรหรือไม่ แต่ท้าทายให้พระองค์พิสูจน์โดยใช้อำนาจเพื่อแก้ความหิว แท้ที่จริงพระเยซูมีอำนาจทำเช่นนั้นได้ (ต่อมาทรงเลี้ยงห้าพัน — ลก 9:16-17) แต่ทรงปฏิเสธที่จะใช้อำนาจเพื่อหลีกเลี่ยงความทุกข์ในถิ่นทุรกันดารตามพระประสงค์ของพระบิดา
- Key decisions:
  - εἶπεν δὲ αὐτῷ ὁ διάβολος → มารจึงทูลพระองค์ว่า — Problem: does the devil 'say' with royal-deferential ทูล (addressing divine subject) or neutral พูด/กล่าว? The devil is addressing Jesus who IS divine, but as adversary. Thai Christian convention (cf. MAT 4:3 transl...
  - Εἰ υἱὸς εἶ τοῦ θεοῦ → ถ้าท่านเป็นพระบุตรของพระเจ้า — Per uW grammar-connect-condition-hypothetical + guidelines-sonofgodprinciples: εἰ + indicative = 'given that' or 'if' (real condition with doubt tinge — not pure hypothetical). υἱὸς τοῦ θεοῦ → พระบุตรของพระเจ้า (glo...
  - εἰπὲ τῷ λίθῳ τούτῳ ἵνα γένηται ἄρτος → จงสั่งหินก้อนนี้ให้กลายเป็นขนมปัง — Per uW figs-explicit: the devil points to a specific stone. Matthew's version has plural λίθοι οὗτοι 'these stones' (4:3); Luke has singular τῷ λίθῳ τούτῳ 'this stone.' Thai preserves Luke's singular — «หินก้อนนี้»....
- Notes: The first of three temptations (Lukan order). The conditional εἰ is not expressing doubt — the devil knows Jesus is Son of God (cf. 4:41 where demons confess). It's challenging: 'since you are the Son of God, prove it by exercising Son-of-God power for yourself.' This mirrors Israel's wilderness testing (Deut 8:3) where hunger became a test of...

**Luke 4:4**
- GR: καὶ ἀπεκρίθη πρὸς αὐτὸν ὁ Ἰησοῦς· Γέγραπται ὅτι Οὐκ ἐπ᾽ ἄρτῳ μόνῳ ζήσεται ὁ ἄνθρωπος.
- TH: พระเยซูตรัสตอบเขาว่า «มีคำเขียนไว้ว่า ‹มนุษย์จะดำรงชีวิตด้วยขนมปังสิ่งเดียวหามิได้›»
- TH-summary: พระเยซูทรงอ้างจากเฉลยธรรมบัญญัติ 8:3 ซึ่งเป็นพระคำที่โมเสสตรัสแก่อิสราเอลขณะย้อนมองสี่สิบปีในถิ่นทุรกันดาร — ที่ซึ่งพระเจ้าทรงให้มานาเพื่อสอนว่าชีวิตไม่ได้มาจากขนมปังเท่านั้น แต่จากพระคำของพระองค์ พระเยซูในฐานะ «อาดัมคนที่สอง» และ «อิสราเอลที่แท้จริง» ทรงตัดสินใจพึ่งพระบิดาแทนการใช้อำนาจเพื่อตนเอง พระเยซูยังคงหิว แต่ทรงเลือกพระคำมากกว่าอาหาร — ตรงข้ามกับอิสราเอลที่บ่นว่าพระเจ้าและต้องการเนื้อสัตว์ (กดว 11)
- Key decisions:
  - ἀπεκρίθη πρὸς αὐτὸν ὁ Ἰησοῦς → พระเยซูตรัสตอบเขา — Divine subject → ตรัสตอบ (royal speech). Per uW grammar-connect-logic-contrast: καί here introduces contrast (devil's challenge → Jesus's refusal) — Thai conveys the contrast via the respectful response with scriptu...
  - Γέγραπται → มีคำเขียนไว้ว่า — γέγραπται perfect-passive-indicative, standard OT-citation formula. Thai «มีคำเขียนไว้ว่า» is the established rendering (MAT 4:4, 4:7, 4:10, MRK 1:2, etc.) — perfect form conveys 'it stands written.' Per uW figs-act...
  - Οὐκ ἐπ᾽ ἄρτῳ μόνῳ ζήσεται ὁ ἄνθρωπος → มนุษย์จะดำรงชีวิตด้วยขนมปังสิ่งเดียวหามิได้ — Direct quote of DEU 8:3 LXX: οὐκ ἐπ' ἄρτῳ μόνῳ ζήσεται ὁ ἄνθρωπος. Luke (and Mark/synoptic tradition) omits Matthew's continuation «ἀλλ' ἐπὶ παντὶ ῥήματι θεοῦ». SBLGNT reads Luke with only the first half; Byzantine ...
- Notes: KEY TEXTUAL VARIANT: SBLGNT/NA28/BSB end with ὁ ἄνθρωπος. Byzantine manuscripts add «ἀλλ' ἐπὶ παντὶ ῥήματι θεοῦ» (assimilation to Matt 4:4 / Deut 8:3). We follow SBLGNT. OT CITATION: direct quote of DEU 8:3 LXX. Significance: Deut 8:3 is the lesson Moses drew from the 40-year wilderness — that Yahweh humbled Israel with hunger in order to teac...

**Luke 4:5**
- GR: Καὶ ἀναγαγὼν αὐτὸν ἔδειξεν αὐτῷ πάσας τὰς βασιλείας τῆς οἰκουμένης ἐν στιγμῇ χρόνου·
- TH: แล้วมารนำพระองค์ขึ้นไปสู่ที่สูง และชี้ให้พระองค์ทอดพระเนตรอาณาจักรทั้งหลายในแผ่นดินโลกในชั่วขณะเดียว
- TH-summary: มารให้พระเยซูทอดพระเนตรอาณาจักรทุกแห่งของโลก «ในชั่วขณะเดียว» (ἐν στιγμῇ χρόνου ซึ่งเป็น «hapax» คือปรากฏเพียงครั้งเดียวในพันธสัญญาใหม่) นี่เป็นประสบการณ์นิมิตเหนือธรรมชาติ ไม่ใช่การเดินทางจริง แผ่นดินทุกแห่งที่ปรากฏในขณะวูบเดียวสื่อถึงการที่มารอ้างว่ามีอำนาจเหนือระบบทางการเมืองของโลก — ซึ่งพระคัมภีร์ยืนยันในระดับหนึ่งว่าโลกที่ตกในบาปอยู่ใต้อิทธิพลของ «เจ้าแห่งโลก» (ยน 12:31; 14:30; 16:11; 2คร 4:4) แต่อำนาจนี้มีขีดจำกัดและกำลังจะสิ้นสุดลงในไม้กางเขน
- Key decisions:
  - ἀναγαγὼν αὐτὸν → นำพระองค์ขึ้นไปสู่ที่สูง — ἀνάγω aorist-participle = 'having led up.' Per uW figs-explicit: implication is leading up to a high-vantage place (text doesn't say what). Thai «นำพระองค์ขึ้นไปสู่ที่สูง» makes the elevation explicit since 'led him...
  - ἔδειξεν αὐτῷ πάσας τὰς βασιλείας τῆς οἰκουμένης → ชี้ให้พระองค์ทอดพระเนตรอาณาจักรทั้งหลายในแผ่นดินโลก — δείκνυμι aorist-active = show/display. Divine object (Jesus seeing) → ทอดพระเนตร (royal register for 'see'). οἰκουμένη = 'the inhabited world' — broader than κόσμος; technical term for the Roman empire's cultural-po...
  - ἐν στιγμῇ χρόνου → ในชั่วขณะเดียว — HAPAX: στιγμή (only here in NT) — 'a prick, point, moment.' From στίζω 'to prick.' Classical usage: a geometric point or a momentary instant. χρόνου (genitive) qualifies it as a 'point OF TIME.' Per uW figs-explicit...
- Notes: HAPAX: στιγμή (here only in NT). The 'instant of time' + panoramic vision marks this as a visionary/supernatural experience, not a literal mountain climb. οἰκουμένη is Luke's favored term for the civilized world (cf. 2:1 Augustus's decree «πᾶσαν τὴν οἰκουμένην»; Acts 11:28, 17:6, 24:5) — the politically-ordered Roman world-system. The devil sh...

**Luke 4:6**
- GR: καὶ εἶπεν αὐτῷ ὁ διάβολος· Σοὶ δώσω τὴν ἐξουσίαν ταύτην ἅπασαν καὶ τὴν δόξαν αὐτῶν, ὅτι ἐμοὶ παραδέδοται καὶ ᾧ ἐὰν θέλω δίδωμι αὐτήν·
- TH: แล้วมารทูลพระองค์ว่า «เราจะยกสิทธิอำนาจทั้งสิ้นและศักดิ์ศรีของอาณาจักรเหล่านี้ให้แก่ท่าน เพราะได้มอบไว้แก่เราแล้ว และเราจะยกให้ผู้ใดก็ได้ตามใจเรา
- TH-summary: มารอวดตัวว่าครอบครองอำนาจและศักดิ์ศรีของอาณาจักรทั้งปวงในโลก และสามารถยกให้ใครก็ได้ตามใจ แม้พระคัมภีร์จะยืนยันว่ามารมีอำนาจบางส่วนในระบบของโลกที่ตกในบาป แต่ข้ออ้างว่ามี «สิทธิอำนาจทั้งสิ้น» เป็นการโอ้อวด — อำนาจสูงสุดอยู่ที่พระเจ้าผู้ทรงมอบอาณาจักรทั้งปวงแก่พระบุตรในที่สุด (ดนล 7:13-14; มธ 28:18; วว 11:15) การทดลองนี้จึงเป็นการเสนอทางลัด ได้อำนาจโดยไม่ต้องผ่านไม้กางเขน
- Key decisions:
  - Σοὶ δώσω τὴν ἐξουσίαν ταύτην ἅπασαν → เราจะยกสิทธิอำนาจทั้งสิ้น...ให้แก่ท่าน — ἐξουσία → สิทธิอำนาจ (glossary-established MRK 1:22, 1:27; authority as both right and power). ἅπασαν (intensive form of πᾶσαν) → ทั้งสิ้น (emphatic totality). Devil speaks as first-person — เรา for 'I' (devil self-...
  - τὴν δόξαν αὐτῶν → ศักดิ์ศรีของอาณาจักรเหล่านี้ — δόξα here = 'glory' in the sense of visible splendor/magnificence of the kingdoms (cf. MAT 4:8 parallel τὴν δόξαν αὐτῶν). Thai ศักดิ์ศรี = honor/dignity/glory — captures the pride-of-kingdom sense. αὐτῶν (neuter plu...
  - ἐμοὶ παραδέδοται → ได้มอบไว้แก่เราแล้ว — παραδίδωμι perfect-passive-indicative = 'has been handed over [to me, now in my possession].' Per uW figs-activepassive: passive is theologically sensitive — if we name the agent («พระเจ้า»), we seem to affirm God d...
  - ᾧ ἐὰν θέλω δίδωμι αὐτήν → เราจะยกให้ผู้ใดก็ได้ตามใจเรา — ᾧ ἐὰν θέλω indefinite relative + subjunctive = 'to whomever I wish.' Thai «ผู้ใดก็ได้ตามใจเรา» captures the arbitrary-will idiom. δίδωμι present-indicative with future-reference function in this generalizing context...
- Notes: SBLGNT and Byzantine manuscripts read ἐὰν here; some mss have ἄν (classical). No semantic difference. Theological tension: the devil's claim to ultimate world-authority is at best a half-truth — cf. Ps 24:1 'the earth is the Lord's'; Dan 7:14 'dominion given to the Son of Man.' Jesus's response in v.8 (not disputing Satan's claim per se, but i...

**Luke 4:7**
- GR: σὺ οὖν ἐὰν προσκυνήσῃς ἐνώπιον ἐμοῦ, ἔσται σοῦ πᾶσα.
- TH: ฉะนั้นถ้าท่านนมัสการต่อหน้าเรา ทั้งหมดนี้จะเป็นของท่าน»
- Key decisions:
  - σὺ οὖν ἐὰν προσκυνήσῃς ἐνώπιον ἐμοῦ → ฉะนั้นถ้าท่านนมัสการต่อหน้าเรา — σύ (nominative) is emphatic 'YOU' — Thai reflects the emphasis by keeping ท่าน at the sentence's conditional position. Per uW figs-explicit: ἐνώπιον ἐμοῦ 'before me' = visible, direct act of worship; Thai «ต่อหน้าเร...
  - ἔσται σοῦ πᾶσα → ทั้งหมดนี้จะเป็นของท่าน — πᾶσα (feminine singular) refers to ἐξουσία of v.6 — Thai resolves the feminine-singular-referent to «ทั้งหมดนี้» (the whole — authority + glory collectively). ἔσται future middle = 'will become/will be.' σοῦ genitiv...
- Notes: The conditional clause makes the terms brutally clear: a single act of worship in exchange for all world-dominion. This mirrors and inverts the Deuteronomic central command (6:4-5, quoted in v.8 below). Synoptic parallel: Matt 4:9 has πεσὼν προσκυνήσῃς 'falling down worship' — more vivid prostration; Luke tones down but retains the worship demand.

**Luke 4:8**
- GR: καὶ ἀποκριθεὶς ὁ Ἰησοῦς εἶπεν αὐτῷ· Γέγραπται· Κύριον τὸν θεόν σου προσκυνήσεις καὶ αὐτῷ μόνῳ λατρεύσεις.
- TH: พระเยซูตรัสตอบเขาว่า «มีคำเขียนไว้ว่า ‹เจ้าจงนมัสการองค์พระผู้เป็นเจ้าพระเจ้าของเจ้า และปรนนิบัติพระองค์แต่ผู้เดียว›»
- TH-summary: พระเยซูทรงอ้างจากเฉลยธรรมบัญญัติ 6:13 ซึ่งเป็นส่วนหนึ่งของบริบท «เชมา» — คำสารภาพหลักของอิสราเอล (เฉลย 6:4-9) ที่เน้นว่าพระเจ้าเที่ยงแท้มีพระองค์เดียว และความจงรักภักดีของประชากรต้องเป็นของพระองค์แต่ผู้เดียว การนมัสการมารแม้เพียงครั้งเดียวจะทำลายพระบัญชาพื้นฐานสุดของพันธสัญญา พระเยซูทรงไม่เถียงเรื่องอำนาจของมาร แต่ทรงปฏิเสธเงื่อนไขโดยตรง — พระบิดาเท่านั้นที่ทรงคู่ควรการนมัสการ ไม่ว่าจะต้องแลกด้วยสิ่งใด
- Key decisions:
  - ἀποκριθεὶς ὁ Ἰησοῦς εἶπεν αὐτῷ → พระเยซูตรัสตอบเขาว่า — Per uW figs-hendiadys: ἀποκριθεὶς...εἶπεν = single act 'answered' (Aramaic-influenced Greek). Thai «ตรัสตอบ» (royal) = answered in single verb. เขา for devil.
  - Κύριον τὸν θεόν σου προσκυνήσεις → เจ้าจงนมัสการองค์พระผู้เป็นเจ้าพระเจ้าของเจ้า — Direct quote of DEU 6:13 LXX with minor rewording. MT has יהוה אלהיך תירא 'YHWH your God you shall fear'; LXX has κύριον τὸν θεόν σου φοβηθήσῃ / προσκυνήσεις depending on codex. Jesus (or Luke's LXX tradition) uses ...
  - αὐτῷ μόνῳ λατρεύσεις → ปรนนิบัติพระองค์แต่ผู้เดียว — λατρεύω → ปรนนิบัติ (glossary-consistent with MAT 4:10). Cultic-service term (distinct from διακονέω = general service). Thai «ปรนนิบัติ» covers both the priestly-worship and exclusive-allegiance senses. μόνῳ → แต่ผ...
- Notes: OT CITATION: DEU 6:13 (with LXX-based verbal adaptation: προσκυνήσεις for MT's תירא 'fear'). Part of the Shema cluster (Deut 6:4-15), the foundational monotheism declaration. Jesus's response is not philosophical (disputing Satan's claim to world-authority) but covenantal — the first commandment settles everything. The three temptation-respons...

**Luke 4:9**
- GR: Ἤγαγεν δὲ αὐτὸν εἰς Ἰερουσαλὴμ καὶ ἔστησεν ἐπὶ τὸ πτερύγιον τοῦ ἱεροῦ, καὶ εἶπεν αὐτῷ· Εἰ υἱὸς εἶ τοῦ θεοῦ, βάλε σεαυτὸν ἐντεῦθεν κάτω·
- TH: แล้วมารนำพระองค์ไปยังกรุงเยรูซาเล็ม และให้พระองค์ประทับยืนอยู่บนยอดสุดของพระวิหาร แล้วทูลพระองค์ว่า «ถ้าท่านเป็นพระบุตรของพระเจ้า จงกระโดดจากที่นี่ลงไปเถิด
- TH-summary: ลูกาเรียงลำดับให้การทดลองจบที่เยรูซาเล็ม — นครที่เป็นจุดสุดยอดของพระวรสาร (ลก 9:51; 13:33; 24:47) และเป็นที่ซึ่งพระเยซูจะทรงถูกตรึง คำว่า «πτερύγιον» (ปีกน้อย) หมายถึงยอดหรือชายคาของพระวิหาร — อาจเป็นด้านทิศตะวันออกเฉียงใต้ของลานพระวิหารที่สูงจากหุบเขาคิดโรนราว 450 ฟุต หรือเป็นยอดของพระวิหารเอง การกระโดดลงมาอย่างปลอดภัยจะเป็นการอวดอ้างต่อสาธารณะว่าพระองค์เป็นพระบุตรโดยการบังคับให้พระเจ้าช่วย — เป็นการพลิกศรัทธาเป็นการเรียกร้องสิทธิ์
- Key decisions:
  - Ἤγαγεν δὲ αὐτὸν εἰς Ἰερουσαλὴμ → แล้วมารนำพระองค์ไปยังกรุงเยรูซาเล็ม — Thai inserts «มาร» (from context) to specify subject of the Greek third-person verb — unambiguous. Ἰερουσαλήμ → กรุงเยรูซาเล็ม (glossary-established; the Hebrew-form Ἱερουσαλήμ is preferred by Luke as the sacred-cit...
  - ἔστησεν ἐπὶ τὸ πτερύγιον τοῦ ἱεροῦ → ให้พระองค์ประทับยืนอยู่บนยอดสุดของพระวิหาร — πτερύγιον (diminutive of πτέρυξ 'wing') = lit. 'little wing' → 'pinnacle, parapet, edge.' Per uW figs-explicit: exact location uncertain but implies a deadly fall. Thai «ยอดสุด» (highest point) captures the fatal-he...
  - βάλε σεαυτὸν ἐντεῦθεν κάτω → จงกระโดดจากที่นี่ลงไปเถิด — βάλλω aorist-imperative 'throw' with reflexive σεαυτόν — Thai «จงกระโดด» (jump) fits Thai idiom better than literal «โยนตัวเองลง»; the action is voluntary self-descent. ἐντεῦθεν κάτω = 'from here down.' «เถิด» = sof...
- Notes: Luke's temple-pinnacle temptation is the THIRD and climactic in Luke's order (Matthew has it second). The Lukan arrangement places the final scene at Jerusalem — thematically crucial since Luke structures his Gospel around Jerusalem as destiny-city (9:51 'he set his face'; 13:33 'a prophet cannot perish outside of Jerusalem'; 24:47 'beginning ...

**Luke 4:10**
- GR: γέγραπται γὰρ ὅτι Τοῖς ἀγγέλοις αὐτοῦ ἐντελεῖται περὶ σοῦ τοῦ διαφυλάξαι σε,
- TH: เพราะมีคำเขียนไว้ว่า ‹พระองค์จะทรงบัญชาเหล่าทูตสวรรค์ของพระองค์เกี่ยวกับเจ้า ให้คอยปกป้องเจ้า
- TH-summary: มารยกพระคำจากสดุดี 91:11-12 มาใช้ — คราวนี้ใช้พระคัมภีร์ต่อสู้พระเยซู (ตรงข้ามกับสองครั้งก่อนที่พระเยซูทรงใช้พระคัมภีร์) แต่มารยกมาแบบบิดเบือน: (1) ตัดวลี «ในทุกทาง» ของเจ้า (ἐν πάσαις ταῖς ὁδοῖς σου) ออก — วลีที่กำหนดว่าการปกป้องเป็นไปในวิถีที่พระเจ้ากำหนด ไม่ใช่ในการท้าทายพระเจ้า (2) ใช้พระสัญญาแห่งการคุ้มครองมาเป็นข้ออ้างให้พระเยซูเสี่ยงอันตรายโดยไร้เหตุ — เปลี่ยน «เชื่อวางใจ» เป็น «ทดลอง» (คำที่พระเยซูทรงชี้กลับในข้อ 12)
- Key decisions:
  - γέγραπται γὰρ → เพราะมีคำเขียนไว้ว่า — γάρ 'for' — devil uses the OT-citation formula to ground his challenge in Scripture. Irony: the devil cites what Jesus has been citing. Thai preserves γάρ as «เพราะ» since the 'for' introduces the basis of the prior...
  - Τοῖς ἀγγέλοις αὐτοῦ ἐντελεῖται περὶ σοῦ → พระองค์จะทรงบัญชาเหล่าทูตสวรรค์ของพระองค์เกี่ยวกับเจ้า — Quote of LXX Ps 90:11 (Heb 91:11). ἐντέλλομαι future middle = 'will command.' Subject (αὐτοῦ → αὐτός implicit) = God — Thai supplies «พระองค์» as subject, royal ทรงบัญชา. ἄγγελος → ทูตสวรรค์ (glossary-established). ...
  - τοῦ διαφυλάξαι σε → ให้คอยปกป้องเจ้า — HAPAX: διαφυλάσσω (only here in NT) — intensive compound of φυλάσσω = 'to guard throughout, protect carefully.' LXX Ps 90:11 has διαφυλάξαι. διά-prefix intensifies 'throughout all ways' — but devil strategically omi...
- Notes: HAPAX: διαφυλάσσω (only NT occurrence). Direct quote of PSA 91:11 (LXX 90:11). The devil's citation is DELIBERATELY PARTIAL — he omits «ἐν πάσαις ταῖς ὁδοῖς σου» ('in all your ways'), the LXX phrase that qualifies the divine protection as covering the faithful believer's ordinary paths, not a demand-test scenario. This is the classic distortio...

**Luke 4:11**
- GR: καὶ ὅτι Ἐπὶ χειρῶν ἀροῦσίν σε μήποτε προσκόψῃς πρὸς λίθον τὸν πόδα σου.
- TH: และว่า ‹พวกเขาจะประคองเจ้าไว้ด้วยมือของพวกเขา เพื่อไม่ให้เท้าของเจ้ากระทบหิน›»
- Key decisions:
  - Ἐπὶ χειρῶν ἀροῦσίν σε → พวกเขาจะประคองเจ้าไว้ด้วยมือของพวกเขา — LXX Ps 90:12a quote. αἴρω future-active = 'will lift/carry.' Thai «ประคอง» captures the tender-support sense better than «ยก» (simple lift) — angels-catching-Messiah imagery needs the protective-carrying nuance. ἐπὶ...
  - μήποτε προσκόψῃς πρὸς λίθον τὸν πόδα σου → เพื่อไม่ให้เท้าของเจ้ากระทบหิน — μήποτε + aorist-subjunctive = purpose/result negative 'lest you strike.' Per uW figs-synecdoche: 'strike your foot against a stone' = any form of harm, synecdoche for the whole body's injury. Thai preserves the conc...
- Notes: Continuation of PSA 91:12 (LXX 90:12) quote. Even the devil's truncated citation is rhetorically skilled: the imagery of supernatural protection is real (Ps 91 is genuinely a messianic psalm), but weaponized for trivial self-demonstration. ADDED TO NT_OT_CITATIONS: LUK 4:11 devil_cites_OT continuation of PSA 91:12 (part of v.10 citation).

**Luke 4:12**
- GR: καὶ ἀποκριθεὶς εἶπεν αὐτῷ ὁ Ἰησοῦς ὅτι Εἴρηται· Οὐκ ἐκπειράσεις κύριον τὸν θεόν σου.
- TH: พระเยซูตรัสตอบเขาว่า «มีคำกล่าวไว้ว่า ‹เจ้าอย่าทดลององค์พระผู้เป็นเจ้าพระเจ้าของเจ้า›»
- TH-summary: พระเยซูทรงตอบมารด้วยพระคำจากเฉลยธรรมบัญญัติ 6:16 «อย่าทดลองพระยาห์เวห์พระเจ้าของเจ้า เหมือนที่เจ้าได้ทดลองพระองค์ที่มัสสา» ซึ่งย้อนไปยังเหตุการณ์ที่อิสราเอลเรียกร้องน้ำอย่างแข็งขืนและ «ทดลองพระยาห์เวห์» (อพย 17:2-7) การที่พระเยซูทรงเสี่ยงชีวิตเพื่อบังคับพระบิดาให้ทำอัศจรรย์ช่วยจะเป็นการทำซ้ำความบาปของอิสราเอลที่มัสสา — คาดหวังการพิสูจน์แทนที่จะเชื่อวางใจ พระเยซูทรงเข้าใจความแตกต่างระหว่าง «เชื่อ» กับ «ทดลอง» อย่างชัดเจน
- Key decisions:
  - Εἴρηται → มีคำกล่าวไว้ว่า — εἴρηται perfect-passive from ἐρῶ/λέγω = 'it has been said.' Subtle contrast with earlier γέγραπται ('it has been written') — εἴρηται evokes the spoken-declaration aspect. Per uW figs-activepassive: Thai uses «มีคำกล...
  - Οὐκ ἐκπειράσεις κύριον τὸν θεόν σου → เจ้าอย่าทดลององค์พระผู้เป็นเจ้าพระเจ้าของเจ้า — Direct quote of DEU 6:16 LXX. ἐκπειράζω (compound 'test-out, test thoroughly') vs. simple πειράζω — intensive force. However Thai doesn't easily distinguish ทดลอง from «ทดลองอย่างหนัก» — we use simple «ทดลอง» since ...
- Notes: OT CITATION: DEU 6:16 LXX verbatim (οὐκ ἐκπειράσεις κύριον τὸν θεόν σου). Contextually Deut 6:16 continues «as you tested him at Massah» — referring to Ex 17:1-7 where Israel demanded water from Moses. The irony: the devil asked Jesus to duplicate Israel's wilderness testing-of-God by demanding dramatic supernatural rescue. Jesus, unlike Israe...

**Luke 4:13**
- GR: καὶ συντελέσας πάντα πειρασμὸν ὁ διάβολος ἀπέστη ἀπ᾽ αὐτοῦ ἄχρι καιροῦ.
- TH: เมื่อมารได้ทดลองทุกอย่างจบสิ้นแล้ว ก็ละพระองค์ไปจนกว่าจะถึงเวลาเหมาะ
- TH-summary: ลูกาจบฉากทดลองด้วยคำสำคัญ «ἄχρι καιροῦ» (จนกว่าจะถึงเวลาเหมาะ) — บอกใบ้ล่วงหน้าว่าการทดลองยังไม่สิ้นสุด มารจะกลับมาอีกในวันสุดท้าย เมื่อลูกา 22:3 บันทึกว่า «ซาตานเข้าสิงยูดาส» การทดลองที่สวนเกทเสมนี (22:40-46) และกางเขน (23:35-39 «ถ้าท่านเป็นพระคริสต์ จงช่วยตัวเองให้รอด») สะท้อนภาพการทดลองในถิ่นทุรกันดารโดยตรง ดังนั้นพระวรสารทั้งเล่มจึงเป็นเรื่องราวของการต่อสู้ทางวิญญาณที่ต่อเนื่อง
- Key decisions:
  - συντελέσας πάντα πειρασμὸν → มารได้ทดลองทุกอย่างจบสิ้นแล้ว — συντελέω aorist-participle 'having completed thoroughly.' Per uW figs-explicit: this does NOT mean the devil succeeded — only that he exhausted his attempts. Thai «ทดลองทุกอย่างจบสิ้นแล้ว» captures the completion-of...
  - ἀπέστη ἀπ᾽ αὐτοῦ ἄχρι καιροῦ → ก็ละพระองค์ไปจนกว่าจะถึงเวลาเหมาะ — ἀφίστημι aorist = 'departed from.' Per uW figs-explicit on καιρός: NT distinguishes χρόνος (chronological time) from καιρός (opportune/appointed moment). Thai «เวลาเหมาะ» captures καιρός's sense of right-moment bett...
- Notes: Lukan framing of the temptation as ongoing spiritual warfare, not a one-time event. The καιρός returns in 22:3 where Luke alone notes «εἰσῆλθεν δὲ Σατανᾶς εἰς Ἰούδαν» — Satan enters Judas, the prelude to the Passion. Luke's Gospel is framed between this temptation (4:1-13) and the Passion temptation (22-23) as the 'great struggle.' The phrase ...

**Luke 4:14**
- GR: Καὶ ὑπέστρεψεν ὁ Ἰησοῦς ἐν τῇ δυνάμει τοῦ πνεύματος εἰς τὴν Γαλιλαίαν. καὶ φήμη ἐξῆλθεν καθ᾽ ὅλης τῆς περιχώρου περὶ αὐτοῦ.
- TH: พระเยซูเสด็จกลับไปยังแคว้นกาลิลีด้วยฤทธิ์เดชแห่งพระวิญญาณ และกิตติศัพท์เกี่ยวกับพระองค์ก็เลื่องลือไปทั่วเขตแดนนั้น
- TH-summary: ลูกาเริ่มต้นพันธกิจกาลิลีของพระเยซูด้วยประโยคสรุปสั้น ๆ (ข้อ 14-15) ซึ่งแตกต่างจากมัทธิว 4:12-17 และมาระโก 1:14-15 ที่ให้รายละเอียดเวลา สถานที่ และเนื้อหาการประกาศ สำหรับลูกาแล้ว ฉากเยี่ยมบ้านเกิดนาซาเร็ธที่กำลังจะมาเป็นจุดเริ่มต้นทางวรรณกรรมของพันธกิจ — เป็นการเสนอโปรแกรมพันธกิจที่เป็นเอกลักษณ์ของพระเยซู (เทียบ การเปิดฉากงานประกาศในธรรมศาลาด้วยคำพยากรณ์อิสยาห์) คำว่า «ด้วยฤทธิ์เดชแห่งพระวิญญาณ» เน้นว่าการทดลองในถิ่นทุรกันดารมิได้ทำให้พระวิญญาณจากไป แต่พระเยซูทรงกลับพร้อมกับพลังของพระวิญญาณที่เต็มเปี่ยมยิ่งขึ้น
- Key decisions:
  - ὑπέστρεψεν ὁ Ἰησοῦς → พระเยซูเสด็จกลับ — Per uW writing-newevent: καί begins new episode — Thai no transition word needed since sentence-start with subject is natural episode-break. Divine subject + movement → เสด็จกลับ (royal). ὑποστρέφω Lukan favorite (3...
  - ἐν τῇ δυνάμει τοῦ πνεύματος → ด้วยฤทธิ์เดชแห่งพระวิญญาณ — Per uW figs-explicit: δύναμις + πνεῦμα combination = Spirit-empowered capability. ฤทธิ์เดช = biblical Thai for 'power/mighty-acting' (stronger than generic พลัง); standard for δύναμις in miracle-context. Note: «πνεύ...
  - φήμη ἐξῆλθεν καθ᾽ ὅλης τῆς περιχώρου → กิตติศัพท์...ก็เลื่องลือไปทั่วเขตแดนนั้น — Per uW figs-personification: φήμη (report/rumor) personified as 'going out.' Thai «เลื่องลือ» matches the organic-spread sense. φήμη → กิตติศัพท์ (standard Thai Christian; MRK 1:28 parallel uses this). περίχωρος 'su...
- Notes: Synoptic parallel: Matt 4:12-17, Mark 1:14-15 — but Luke's framing is programmatically different. Matthew and Mark time Jesus's Galilean ministry to John's arrest; Luke simply notes the Spirit-empowered return. Luke's narrative design delays detailed ministry-content to the Nazareth sermon (4:16-30), which functions as the inaugural-programmat...

**Luke 4:15**
- GR: καὶ αὐτὸς ἐδίδασκεν ἐν ταῖς συναγωγαῖς αὐτῶν, δοξαζόμενος ὑπὸ πάντων.
- TH: พระองค์ทรงสั่งสอนในธรรมศาลาของพวกเขา และทุกคนต่างก็ยกย่องพระองค์
- Key decisions:
  - αὐτὸς ἐδίδασκεν ἐν ταῖς συναγωγαῖς αὐτῶν → พระองค์ทรงสั่งสอนในธรรมศาลาของพวกเขา — Emphatic αὐτός 'he himself' — Thai renders as topicalized «พระองค์» at sentence-start (already honorific). διδάσκω imperfect = iterative/customary teaching. Divine subject + teaching → ทรงสั่งสอน (royal). συναγωγή →...
  - δοξαζόμενος ὑπὸ πάντων → ทุกคนต่างก็ยกย่องพระองค์ — Per uW figs-activepassive: present-passive participle 'being glorified.' Thai activates the passive with agent «ทุกคน» — «ต่างก็ยกย่องพระองค์». δοξάζω here = human honor/praise, not divine glorification; Thai ยกย่อง...
- Notes: Luke's summary creates narrative tension with what follows — 'glorified by all' will soon reverse to 'filled with wrath' (4:28). The synagogues mentioned here are the village synagogues throughout Galilee; Nazareth (4:16) is one specific case, Capernaum (4:31-37) another.

**Luke 4:16**
- GR: Καὶ ἦλθεν εἰς Ναζαρά, οὗ ἦν τεθραμμένος, καὶ εἰσῆλθεν κατὰ τὸ εἰωθὸς αὐτῷ ἐν τῇ ἡμέρᾳ τῶν σαββάτων εἰς τὴν συναγωγήν, καὶ ἀνέστη ἀναγνῶναι.
- TH: พระองค์เสด็จมายังเมืองนาซาเร็ธซึ่งเป็นที่ที่พระองค์ทรงเติบโตขึ้น และในวันสะบาโต พระองค์เสด็จเข้าไปในธรรมศาลาตามปกติ แล้วทรงยืนขึ้นเพื่ออ่านพระคัมภีร์
- TH-summary: เหตุการณ์ที่นาซาเร็ธนี้เป็นการเทศนาเปิดตัวของลูกา — เหมือนคำปราศรัยของเปโตรที่กรุงเยรูซาเล็ม (กจ 2) เปิดตัวกิจการของอัครทูต วลี «ตามปกติ» เผยให้เห็นว่าพระเยซูทรงเป็นผู้เคร่งในพระธรรมบัญญัติมาตั้งแต่เด็ก — ไปธรรมศาลาทุกวันสะบาโต ไม่ใช่ผู้ปฏิรูปที่ทิ้งประเพณีของชาวยิว ในธรรมศาลาช่วงแรกของวันสะบาโตจะมีการอ่านจากโตราห์ก่อน แล้วจึงอ่านจากผู้เผยพระวจนะ (ฮาฟตาราห์) โดยอ่านยืน — สอนนั่ง
- Key decisions:
  - Ναζαρά → เมืองนาซาเร็ธ — Luke's spelling Ναζαρά (vs. more common Ναζαρέθ elsewhere) may reflect older Aramaic form. Thai นาซาเร็ธ is the established transliteration (MAT 4:13, 21:11; LUK 1:26; JHN 1:45). «เมือง» prefix clarifies it's a town...
  - οὗ ἦν τεθραμμένος → ซึ่งเป็นที่ที่พระองค์ทรงเติบโตขึ้น — τρέφω perfect-passive-periphrastic 'had been raised/nurtured.' Per uW figs-activepassive: Thai actives by supplying subject «พระองค์ทรงเติบโต» — divine subject gets ทรง. The imperfect ἦν + perfect-participle = plupe...
  - κατὰ τὸ εἰωθὸς αὐτῷ → ตามปกติ — εἴωθα perfect-active-participle 'having become accustomed' → neuter-substantive 'the customary.' Thai «ตามปกติ» captures the habitual-practice sense. Alternative «ตามธรรมเนียม» would be more formal but «ตามปกติ» is ...
  - ἐν τῇ ἡμέρᾳ τῶν σαββάτων → ในวันสะบาโต — Genitive plural σαββάτων used for singular (common Hebrew/Aramaic idiom in NT Greek). Thai วันสะบาโต (transliteration) is the established form.
  - ἀνέστη ἀναγνῶναι → ทรงยืนขึ้นเพื่ออ่านพระคัมภีร์ — ἀνίστημι aorist = 'stood up.' ἀναγνῶναι aorist-infinitive 'to read.' In synagogue practice, readers stood to read (then sat to teach — v.20). Thai «อ่านพระคัมภีร์» makes the implicit object explicit (he obviously re...
- Notes: Beginning of the Nazareth sermon (vv.16-30), Luke's programmatic opening to Jesus's ministry (contrast the later, shorter accounts in Matt 13:54-58 and Mark 6:1-6 which Luke likely borrows, amplifies, and relocates). Synagogue liturgical practice: the Shema, set prayers (Shemoneh Esreh), Torah reading (parashah), Prophets reading (haftarah), s...

**Luke 4:17**
- GR: καὶ ἐπεδόθη αὐτῷ βιβλίον τοῦ προφήτου Ἠσαΐου, καὶ ἀναπτύξας τὸ βιβλίον εὗρεν τὸν τόπον οὗ ἦν γεγραμμένον·
- TH: คนนำหนังสือม้วนของอิสยาห์ผู้เผยพระวจนะมาถวายพระองค์ พระองค์ทรงคลี่ม้วนหนังสือออก พบข้อที่เขียนไว้ว่า
- TH-summary: หนังสือม้วน (βιβλίον) คือ «เซเฟอร์» แบบโบราณ — แผ่นกระดาษปาไพรัสหรือหนังสัตว์ยาวถูกม้วนเก็บและเปิดดูโดยคลี่ออก ซึ่งเป็นรูปแบบเดียวของการเก็บรักษาพระคัมภีร์ในสมัยพระเยซู (หนังสือแบบเล่ม-โคเด็กซ์เกิดขึ้นภายหลัง) ลูกาบอกเราว่าพระเยซูทรงพลิกหาข้อโดยเฉพาะ ไม่ใช่แค่อ่านตามที่ม้วนเปิดอยู่ — แสดงว่าพระองค์ทรงเลือกข้ออย่างตั้งใจ ข้อที่ทรงพบคืออิสยาห์ 61:1-2 ซึ่งเป็นคำพยากรณ์เกี่ยวกับผู้ได้รับการเจิมของพระเจ้าเพื่อประกาศข่าวประเสริฐแก่คนยากจน
- Key decisions:
  - ἐπεδόθη αὐτῷ βιβλίον τοῦ προφήτου Ἠσαΐου → คนนำหนังสือม้วนของอิสยาห์ผู้เผยพระวจนะมาถวายพระองค์ — ἐπιδίδωμι aorist-passive 'was handed over.' Per uW figs-activepassive: Thai activates with implicit subject «คน» (someone — the synagogue attendant/ὑπηρέτης of v.20). «ถวาย» (offer/hand to a superior) preserves the ...
  - ἀναπτύξας τὸ βιβλίον → พระองค์ทรงคลี่ม้วนหนังสือออก — HAPAX: ἀναπτύσσω (only here in NT) — 'to unroll, unfold.' Compound of ἀνά ('up, again') + πτύσσω ('to fold'). Note: πτύσσω also appears in v.20 as another hapax (rolling-up) — scroll-reading vocabulary clustered her...
  - εὗρεν τὸν τόπον οὗ ἦν γεγραμμένον → พบข้อที่เขียนไว้ว่า — Per uW figs-explicit: Jesus deliberately found the specific Isaiah passage — implies he requested or searched for it, not random. Thai «พบข้อ...ว่า» leads into the quotation. τόπος here = 'place, passage' (as in a b...
- Notes: HAPAX: ἀναπτύσσω (only NT occurrence; paired with πτύσσω in v.20, another hapax — scroll-opening/scroll-closing idiom). The scroll-of-Isaiah in a Galilean synagogue would have been made of sheepskin, probably containing the complete book of Isaiah (which in Dead Sea Scrolls fills a ~24-foot scroll, 1QIsaª). Jesus's selection of Isa 61:1-2 as t...

**Luke 4:18**
- GR: Πνεῦμα κυρίου ἐπ᾽ ἐμέ, οὗ εἵνεκεν ἔχρισέν με εὐαγγελίσασθαι πτωχοῖς, ἀπέσταλκέν με κηρύξαι αἰχμαλώτοις ἄφεσιν καὶ τυφλοῖς ἀνάβλεψιν, ἀποστεῖλαι τεθραυσμένους ἐν ἀφέσει,
- TH: ‹พระวิญญาณขององค์พระผู้เป็นเจ้าสถิตอยู่เหนือเรา เพราะพระองค์ทรงเจิมเราให้ประกาศข่าวประเสริฐแก่คนยากจน ทรงใช้เรามาประกาศปลดปล่อยแก่เชลยและประกาศการคืนสายตาแก่คนตาบอด ประกาศปลดปล่อยผู้ถูกกดขี่
- TH-summary: คำประกาศเปิดพันธกิจของพระเยซู — อ้างจากอิสยาห์ 61:1-2 ผสมกับอิสยาห์ 58:6 (วลี «ประกาศปลดปล่อยผู้ถูกกดขี่») เนื้อหาของอิสยาห์ 61 คือภาพของปีสะบาโตเจ็ด (ยูบิลี-เลวี 25) — ปีที่ทาสได้รับการปลดปล่อย หนี้ได้รับการยกเลิก ที่ดินกลับคืนสู่เจ้าเดิม พระเยซูทรงประกาศว่าปีแห่งพระคุณของพระเจ้า (ยูบิลีในแง่ประเสริฐสุดสูง) เริ่มต้นแล้วด้วยพันธกิจของพระองค์ «คนยากจน» «เชลย» «คนตาบอด» «ผู้ถูกกดขี่» ไม่เพียงหมายถึงสภาพทางกายภาพแต่รวมถึงความยากจนทางวิญญาณและการเป็นเชลยของบาปด้วย
- Key decisions:
  - Πνεῦμα κυρίου ἐπ᾽ ἐμέ → พระวิญญาณขององค์พระผู้เป็นเจ้าสถิตอยู่เหนือเรา — LXX Isa 61:1 opening. πνεῦμα κυρίου → พระวิญญาณขององค์พระผู้เป็นเจ้า (RULES.md §4; κύριος=YHWH → องค์พระผู้เป็นเจ้า). Per uW figs-metaphor: ἐπ᾽ ἐμέ 'upon me' = Spirit's special presence — Thai «สถิตอยู่เหนือ» captur...
  - οὗ εἵνεκεν ἔχρισέν με → เพราะพระองค์ทรงเจิมเรา — Per uW figs-metaphor: χρίω = anointing with oil, OT appointment-to-office ceremony (prophet/priest/king). χριστός ('the anointed one') derives from this verb. Jesus identifies himself with the Messiah-figure of Isa ...
  - εὐαγγελίσασθαι πτωχοῖς → ประกาศข่าวประเสริฐแก่คนยากจน — εὐαγγελίζω → ประกาศข่าวประเสริฐ (RULES.md §4 via εὐαγγέλιον = ข่าวประเสริฐ). Per uW figs-nominaladj: πτωχοῖς dative-plural of adjective used substantively = 'to the poor ones' → «คนยากจน» (people who are poor; the c...
  - κηρύξαι αἰχμαλώτοις ἄφεσιν → ประกาศปลดปล่อยแก่เชลย — HAPAX: αἰχμάλωτος (only here in NT) — literally 'captured by spear,' a war-prisoner. LXX Isa 61:1 usage. Thai «เชลย» is the standard biblical term for war-captive; works well for both literal and spiritual-captive s...
  - τυφλοῖς ἀνάβλεψιν → ประกาศการคืนสายตาแก่คนตาบอด — HAPAX: ἀνάβλεψις (only here in NT) — 'recovery of sight.' ἀνα-prefix = 'back, again' + βλέπω 'see.' LXX Isa 61:1 has this. Thai «การคืนสายตา» (restoration of sight) captures the prefix-semantics. τυφλός → คนตาบอด (b...
  - ἀποστεῖλαι τεθραυσμένους ἐν ἀφέσει → ประกาศปลดปล่อยผู้ถูกกดขี่ — HAPAX: θραύω (only here in NT as perfect-passive-participle τεθραυσμένους) — 'to break, shatter, crush.' Classical: breaking objects, shattering enemies, oppressing people. LXX use: broken/oppressed. ἀποστέλλω aoris...
- Notes: MAJOR OT CITATION: composite quotation of ISA 61:1-2a + ISA 58:6d (LXX). The composite is theologically deliberate — Isa 58:6 and Isa 61:1-2 share Jubilee-release vocabulary (ἄφεσις, ἀποστέλλω), and both are deep messianic-fulfillment texts. THREE HAPAX in this single verse: αἰχμάλωτος, ἀνάβλεψις, θραύω (all from the LXX Isaiah source, not Luk...

**Luke 4:19**
- GR: κηρύξαι ἐνιαυτὸν κυρίου δεκτόν.
- TH: ประกาศปีแห่งความโปรดปรานขององค์พระผู้เป็นเจ้า›
- TH-summary: «ปีแห่งความโปรดปรานขององค์พระผู้เป็นเจ้า» (ἐνιαυτὸν κυρίου δεκτόν) คือปีแห่งยูบิลีในเลวีนิติ 25:8-17 — ปีที่ห้าสิบ ปีแห่งการปลดปล่อย เมื่อทาสได้รับอิสรภาพ หนี้ถูกยกเลิก ที่ดินกลับสู่เจ้าของเดิม พระเยซูทรงตัดข้อความของอิสยาห์ 61:2 ตรงนี้ — ทรงไม่อ่านวลีต่อไป «และวันแห่งการแก้แค้นของพระเจ้าของเรา» (ויום נקם לאלהינו) ซึ่งเน้นการพิพากษา การจงใจตัดนี้สื่อว่าการเสด็จมาครั้งแรกของพระเยซูเป็นการประกาศพระคุณ ส่วนการพิพากษาคงอยู่สำหรับการเสด็จมาครั้งที่สอง — เปิดประตูสู่ยุคแห่งความรอด ก่อนวันพิพากษา
- Key decisions:
  - κηρύξαι ἐνιαυτὸν κυρίου δεκτόν → ประกาศปีแห่งความโปรดปรานขององค์พระผู้เป็นเจ้า — ἐνιαυτός 'year' (poetic/classical for ἔτος). Per uW figs-idiom: 'year of the Lord' = a defined period of divine activity, alluding to Jubilee (Lev 25). δεκτός 'acceptable, welcome, favorable' → «ความโปรดปราน». Thai ...
- Notes: OT CITATION: ISA 61:2a (ἐνιαυτὸν κυρίου δεκτόν, κηρύξαι). KEY THEOLOGICAL TRUNCATION: Luke records Jesus stopping mid-verse — Isa 61:2 continues «καὶ ἡμέραν ἀνταποδόσεως» ('and the day of vengeance'). This deliberate cut signals Jesus's first-advent program as proclamation-of-grace, deferring final-judgment to future eschaton. Patristic father...

**Luke 4:20**
- GR: καὶ πτύξας τὸ βιβλίον ἀποδοὺς τῷ ὑπηρέτῃ ἐκάθισεν· καὶ πάντων οἱ ὀφθαλμοὶ ἐν τῇ συναγωγῇ ἦσαν ἀτενίζοντες αὐτῷ.
- TH: แล้วพระองค์ทรงม้วนหนังสือเก็บ ส่งคืนแก่ผู้ดูแลธรรมศาลา และทรงนั่งลง สายตาของทุกคนในธรรมศาลาก็จดจ่ออยู่ที่พระองค์
- TH-summary: ในธรรมเนียมธรรมศาลา การอ่านพระคัมภีร์ทำโดยยืน แล้ว «นั่งลง» เพื่อสอน การที่พระเยซูทรงนั่งหลังอ่านจึงเป็นสัญญาณว่ากำลังจะเทศน์อธิบาย ทุกคนในธรรมศาลาจึงจับตามองพระองค์ด้วยความคาดหวัง — เพราะพระองค์ทรงเลือกข้ออิสยาห์ที่ดราม่าและเป็นข้อพยากรณ์เกี่ยวกับพระเมสสิยาห์ ผู้ดูแลธรรมศาลา (ὑπηρέτης) เป็นเจ้าหน้าที่ที่ดูแลม้วนพระคัมภีร์อันมีค่า เก็บรักษาในตู้ที่เรียกว่า «อาโรนหะกอเดช» (หีบแห่งความบริสุทธิ์)
- Key decisions:
  - πτύξας τὸ βιβλίον → พระองค์ทรงม้วนหนังสือเก็บ — HAPAX: πτύσσω (only here in NT) — 'to fold, roll up.' Counterpart to ἀναπτύσσω in v.17 (also a hapax). Thai «ม้วนหนังสือเก็บ» captures rolling-and-storing motion. Divine subject → ทรงม้วน. The two hapax bracket the ...
  - ἀποδοὺς τῷ ὑπηρέτῃ → ส่งคืนแก่ผู้ดูแลธรรมศาลา — Per uW translate-unknown: ὑπηρέτης in synagogue context = the chazzan/attendant who managed scrolls. Thai «ผู้ดูแลธรรมศาลา» (synagogue caretaker) is descriptive and clear; alternative «ผู้ปฏิบัติงาน» loses the synag...
  - ἐκάθισεν → ทรงนั่งลง — Per uW figs-explicit: in synagogue practice, sitting after reading signals 'beginning to teach' (cf. Mt 5:1 Sermon on the Mount opens with sitting). Thai «ทรงนั่งลง» (royal sitting) preserves the action; the implied...
  - πάντων οἱ ὀφθαλμοὶ ἐν τῇ συναγωγῇ ἦσαν ἀτενίζοντες αὐτῷ → สายตาของทุกคนในธรรมศาลาก็จดจ่ออยู่ที่พระองค์ — Per uW figs-synecdoche: 'the eyes' = the people themselves in the act of intent looking. Thai preserves the «สายตาของทุกคน» metonymy — natural Thai too. ἀτενίζω present-participle (with imperfect ἦσαν) = sustained i...
- Notes: HAPAX: πτύσσω (only NT occurrence; pairs with ἀναπτύσσω in v.17 — open/close-the-scroll vocabulary cluster, both hapax). The ὑπηρέτης (chazzan) was a synagogue official responsible for the Torah/Prophets scrolls and other ritual operations. The synagogue scroll-cabinet was called the aron ha-qodesh (holy ark). ἀτενίζω is a Lukan favorite (12 o...

**Luke 4:21**
- GR: ἤρξατο δὲ λέγειν πρὸς αὐτοὺς ὅτι Σήμερον πεπλήρωται ἡ γραφὴ αὕτη ἐν τοῖς ὠσὶν ὑμῶν.
- TH: พระองค์ทรงเริ่มตรัสกับพวกเขาว่า «วันนี้ พระคัมภีร์ตอนนี้สำเร็จแล้วในขณะที่ท่านทั้งหลายฟังอยู่นี้»
- TH-summary: ประโยคเดียวนี้เป็นการเทศนาเปิดพันธกิจของพระเยซู ตามที่ลูกาบันทึกไว้ — และเป็นคำประกาศที่กล้าหาญที่สุดประโยคหนึ่งในพันธสัญญาใหม่ พระเยซูทรงประกาศว่าตัวพระองค์เองคือผู้ที่อิสยาห์พยากรณ์ถึง — ผู้ได้รับการเจิมของพระเจ้า ผู้ทำให้ปีแห่งความโปรดปรานเริ่มต้น คำว่า «วันนี้» (σήμερον) เป็นคำสำคัญในพระวรสารลูกา (เทียบ ลก 2:11 «วันนี้พระผู้ช่วยให้รอดประสูติแก่ท่าน»; 19:9 «วันนี้ความรอดได้มาถึงครอบครัวนี้»; 23:43 «วันนี้เจ้าจะอยู่กับเราในเมืองบรมสุข») — บ่งชี้ว่าการสมหวังของแผนการพระเจ้าได้มาถึงในตัวพระเยซู
- Key decisions:
  - ἤρξατο δὲ λέγειν πρὸς αὐτοὺς → พระองค์ทรงเริ่มตรัสกับพวกเขาว่า — ἄρχομαι aorist + present-infinitive 'began to speak' — Lukan stylistic favorite. Divine subject + speech → ทรงเริ่มตรัส (royal). The «ἤρξατο» implies more was said than recorded — Luke gives the opening/programmatic...
  - Σήμερον πεπλήρωται ἡ γραφὴ αὕτη → วันนี้ พระคัมภีร์ตอนนี้สำเร็จแล้ว — Per uW figs-idiom on σήμερον: not a clock-time 'today' but eschatological-fulfillment 'now is the day.' Thai «วันนี้» preserves the temporal force; readers will understand the eschatological dimension from context. ...
  - ἐν τοῖς ὠσὶν ὑμῶν → ในขณะที่ท่านทั้งหลายฟังอยู่นี้ — Per uW figs-metonymy: 'in your ears' = in your hearing/while you listen. Thai idiomatizes to «ในขณะที่ท่านทั้งหลายฟังอยู่นี้» — keeps the auditory-immediacy without literal ears.
- Notes: Programmatic statement of Jesus's whole ministry. σήμερον is a Lukan keyword for fulfillment — the salvation-historical 'today' (Lk 2:11 angel to shepherds; 19:9 Zacchaeus; 23:43 cross to thief; cf. Acts 13:33). πεπλήρωται perfect signals an accomplished state continuing into the present — not just a one-time fulfillment but an inaugurated rea...

**Luke 4:22**
- GR: καὶ πάντες ἐμαρτύρουν αὐτῷ καὶ ἐθαύμαζον ἐπὶ τοῖς λόγοις τῆς χάριτος τοῖς ἐκπορευομένοις ἐκ τοῦ στόματος αὐτοῦ, καὶ ἔλεγον· Οὐχὶ υἱός ἐστιν Ἰωσὴφ οὗτος;
- TH: ทุกคนต่างก็พูดชมเชยพระองค์ และอัศจรรย์ใจในถ้อยคำแห่งพระคุณที่ออกมาจากพระโอษฐ์ของพระองค์ และพูดกันว่า «คนนี้ไม่ใช่บุตรของโยเซฟหรือ»
- TH-summary: ปฏิกิริยาแรกของชาวนาซาเร็ธคือความชื่นชมและประหลาดใจ — พูดถึงพระเยซูในแง่ดี (ἐμαρτύρουν αὐτῷ = «เป็นพยานเข้าข้างพระองค์») แต่คำถาม «คนนี้ไม่ใช่บุตรของโยเซฟหรือ» ฟังดูเป็นการเปิดเส้นทางสู่ความไม่เชื่อ — เป็นคำถามแบบการอุทาน (rhetorical question) ที่แสดงความสงสัยและถากถาง: «เด็กบ้านเดียวกันของเราที่เราเห็นโตขึ้นมา จะเป็นพระเมสสิยาห์ได้ยังไง?» พวกเขายกย่องคำพูด แต่ปฏิเสธตัวบุคคล
- Key decisions:
  - πάντες ἐμαρτύρουν αὐτῷ → ทุกคนต่างก็พูดชมเชยพระองค์ — μαρτυρέω + dative = 'bear witness in favor of' (positive testimony). Some scholars (Jeremias, Stein) read the verb as ambiguous or even hostile in this context, but the parallel ἐθαύμαζον and «λόγοις τῆς χάριτος» fr...
  - ἐθαύμαζον ἐπὶ τοῖς λόγοις τῆς χάριτος → อัศจรรย์ใจในถ้อยคำแห่งพระคุณ — Per uW figs-metonymy: λόγοι = the words spoken. χάρις = grace/charm/favor — here either 'gracious words' (charming, beautiful) or 'words of [divine] grace' (theological). Thai «ถ้อยคำแห่งพระคุณ» preserves the ambigu...
  - ἐκ τοῦ στόματος αὐτοῦ → จากพระโอษฐ์ของพระองค์ — Divine reference 'mouth of him' → พระโอษฐ์ (royal-register noun for divine mouth). Per uW figs-explicitinfo: 'words coming from his mouth' might seem redundant in some languages, but Thai «ออกมาจากพระโอษฐ์» preserve...
  - Οὐχὶ υἱός ἐστιν Ἰωσὴφ οὗτος → คนนี้ไม่ใช่บุตรของโยเซฟหรือ — Per uW figs-rquestion: rhetorical-question form expressing astonishment/dismissal — 'isn't this just Joseph's son?' Thai preserves the question form «...หรือ» since Thai readers will catch the rhetorical/dismissive ...
- Notes: Pivot point in the Nazareth episode — initial appreciation begins to crack. The question 'Joseph's son?' is not innocent inquiry but the seed of unbelief (cf. Mark 6:3 parallel where they call him 'the carpenter, son of Mary' — even more dismissive). The crowd appreciates Jesus's eloquence but cannot square it with their familiarity with his u...

**Luke 4:23**
- GR: καὶ εἶπεν πρὸς αὐτούς· Πάντως ἐρεῖτέ μοι τὴν παραβολὴν ταύτην· Ἰατρέ, θεράπευσον σεαυτόν· ὅσα ἠκούσαμεν γενόμενα εἰς τὴν Καφαρναοὺμ ποίησον καὶ ὧδε ἐν τῇ πατρίδι σου.
- TH: พระองค์ตรัสกับพวกเขาว่า «แน่นอนพวกท่านจะยกสุภาษิตนี้มากล่าวแก่เราว่า ‹หมอเอ๋ย จงรักษาตัวเองเถิด› และว่า ‹สิ่งใดที่เราได้ยินว่าท่านได้ทำในเมืองคาเปอรนาอุม จงทำที่นี่ในบ้านเกิดของท่านด้วย›»
- TH-summary: พระเยซูทรงเปิดเผยความคิดที่ซ่อนอยู่ของชาวบ้าน — พวกเขาคาดหวังว่าพระองค์จะแสดงปาฏิหาริย์ที่นี่เหมือนที่ได้แสดงที่คาเปอรนาอุม สุภาษิต «หมอเอ๋ย จงรักษาตัวเองเถิด» เป็นสำนวนที่หมายความว่า «ทำสิ่งที่อ้างได้ก่อน ก่อนจะมาสอนคนอื่น» พวกเขาต้องการให้พระเยซูพิสูจน์อำนาจของพระองค์ในบ้านเกิดด้วยการทำอัศจรรย์ตามคำสั่ง — ซึ่งเป็นการทดลองคล้ายกับที่มารทำในถิ่นทุรกันดาร (4:9-12) แต่พระเยซูทรงปฏิเสธที่จะแสดงตามความคาดหวังของฝูงชนที่ขาดศรัทธา
- Key decisions:
  - Πάντως ἐρεῖτέ μοι τὴν παραβολὴν ταύτην → แน่นอนพวกท่านจะยกสุภาษิตนี้มากล่าวแก่เรา — πάντως intensifying particle 'certainly, undoubtedly.' παραβολή here = proverb/saying (broader than gospel-parable sense). Thai «ยกสุภาษิตนี้มากล่าว» preserves the act of citing-a-proverb. ἐρεῖτέ future = predictive...
  - Ἰατρέ, θεράπευσον σεαυτόν → หมอเอ๋ย จงรักษาตัวเองเถิด — Per uW writing-proverbs: ancient Mediterranean proverb. Thai «หมอเอ๋ย» = vocative call-form (เอ๋ย is the Thai vocative particle). Aorist imperative θεράπευσον → จงรักษา. Note: Luke is the only NT author who would na...
  - ὅσα ἠκούσαμεν γενόμενα εἰς τὴν Καφαρναοὺμ → สิ่งใดที่เราได้ยินว่าท่านได้ทำในเมืองคาเปอรนาอุม — ὅσα 'whatever, however much.' γενόμενα aorist-middle-participle 'having happened' — Thai «ที่ท่านได้ทำ» activates with subject. εἰς τὴν Καφαρναούμ 'in Capernaum' (εἰς for ἐν is common in NT). Καφαρναούμ → คาเปอรนาอุ...
  - ποίησον καὶ ὧδε ἐν τῇ πατρίδι σου → จงทำที่นี่ในบ้านเกิดของท่านด้วย — Aorist imperative 'do.' πατρίς → บ้านเกิด (homeland/hometown). καί 'also' → «ด้วย» (Thai 'also' particle at end).
- Notes: Luke narrates the Capernaum miracles AFTER this Nazareth episode (4:31-41), creating chronological tension — Jesus refers to Capernaum events not yet recorded. This is Luke's intentional non-chronological arrangement to put the programmatic Nazareth speech first. The «physician heal yourself» proverb (Greek and broader Mediterranean — Euripide...

**Luke 4:24**
- GR: εἶπεν δέ· Ἀμὴν λέγω ὑμῖν ὅτι οὐδεὶς προφήτης δεκτός ἐστιν ἐν τῇ πατρίδι αὐτοῦ.
- TH: พระองค์ตรัสต่อไปว่า «เราบอกความจริงแก่ท่านทั้งหลายว่า ไม่มีผู้เผยพระวจนะคนใดเป็นที่ยอมรับในบ้านเกิดของตน
- Key decisions:
  - Ἀμὴν λέγω ὑμῖν → เราบอกความจริงแก่ท่านทั้งหลายว่า — ἀμήν (Hebrew loanword 'truly') as introductory formula = 'I am about to say something solemnly true.' Distinctive Jesus-speech-marker (76x in Synoptics). Thai «เราบอกความจริงแก่...ว่า» (RULES.md/glossary-consistent ...
  - οὐδεὶς προφήτης δεκτός ἐστιν ἐν τῇ πατρίδι αὐτοῦ → ไม่มีผู้เผยพระวจนะคนใดเป็นที่ยอมรับในบ้านเกิดของตน — Per uW writing-proverbs: condensed proverbial saying. δεκτός 'acceptable, welcome' — same word as v.19 (year-of-favor); subtle echo: Jesus proclaims acceptable Year of the Lord, but he himself is not acceptable in h...
- Notes: Synoptic parallels: Mt 13:57 («οὐκ ἔστιν προφήτης ἄτιμος εἰ μὴ ἐν τῇ πατρίδι»), Mk 6:4 (similar with added 'and in his own household'). Jn 4:44 cites the proverb but in context of Galilee vs. Judea. Each Gospel has slightly different wording — Luke's version emphasizes ACCEPTANCE (δεκτός) over honor (τίμη in Mk/Mt) — making the verbal link wit...

**Luke 4:25**
- GR: ἐπ᾽ ἀληθείας δὲ λέγω ὑμῖν, πολλαὶ χῆραι ἦσαν ἐν ταῖς ἡμέραις Ἠλίου ἐν τῷ Ἰσραήλ, ὅτε ἐκλείσθη ὁ οὐρανὸς ἐπὶ ἔτη τρία καὶ μῆνας ἕξ, ὡς ἐγένετο λιμὸς μέγας ἐπὶ πᾶσαν τὴν γῆν,
- TH: เราบอกพวกท่านตามความจริงว่า ในสมัยของเอลียาห์มีหญิงม่ายมากมายในอิสราเอล เมื่อท้องฟ้าถูกปิดอยู่สามปีหกเดือน และเกิดการกันดารอาหารใหญ่ทั่วทั้งแผ่นดิน
- TH-summary: พระเยซูทรงนำพวกเขาย้อนไปยังเรื่องราวในพันธสัญญาเดิมที่จะกระตุ้นความขุ่นเคือง — เพราะแสดงให้เห็นว่าพระเจ้าทรงสำแดงพระคุณแก่คนต่างชาติแม้ในขณะที่อิสราเอลกำลังขาดแคลน ในรัชสมัยของกษัตริย์อาหับ เอลียาห์ทรงประกาศการกันดารน้ำฝน (1 พกษ 17:1) ซึ่งกินเวลา «สามปีกับหกเดือน» (ตามที่ยากอบ 5:17 ก็ระบุ) แม้มีหญิงม่ายอิสราเอลที่ขาดแคลนอาหารหลายคน พระเจ้าทรงส่งเอลียาห์ไปให้ความช่วยเหลือแก่หญิงม่ายชาวต่างชาติคนหนึ่งที่ศาเรฟัทแห่งเขตไซดอน — แสดงพระคุณของพระเจ้าที่ก้าวข้ามเขตชาติพันธุ์
- Key decisions:
  - ἐπ᾽ ἀληθείας δὲ λέγω ὑμῖν → เราบอกพวกท่านตามความจริงว่า — ἐπ᾽ ἀληθείας 'in/upon truth' = 'truthfully, in fact.' Slightly different formula from v.24's ἀμὴν λέγω — Thai distinguishes via «ตามความจริง» (according to truth) vs. «ความจริง» (the truth).
  - ἐν ταῖς ἡμέραις Ἠλίου → ในสมัยของเอลียาห์ — Per uW figs-idiom + figs-explicit: 'days of Elijah' = period of his prophetic activity. Thai «ในสมัยของ» captures the period sense. Ἠλίας → เอลียาห์ (established standard Thai Christian transliteration; appears LUK ...
  - ὅτε ἐκλείσθη ὁ οὐρανὸς ἐπὶ ἔτη τρία καὶ μῆνας ἕξ → เมื่อท้องฟ้าถูกปิดอยู่สามปีหกเดือน — Per uW figs-activepassive + figs-metaphor: «sky was shut» = no rain — both grammatical and metaphorical. Thai «ท้องฟ้าถูกปิด» preserves both the passive and the metaphor. The 3.5 years matches Jas 5:17 (also a Lukan...
  - ὡς ἐγένετο λιμὸς μέγας ἐπὶ πᾶσαν τὴν γῆν → และเกิดการกันดารอาหารใหญ่ทั่วทั้งแผ่นดิน — Per uW translate-unknown: λιμός = famine/great-lack-of-food. Thai «การกันดารอาหาร» = standard biblical Thai for famine. ὡς here introduces co-incident result clause — Thai «และเกิด» (and there occurred). γῆ here = l...
- Notes: Reference to 1 Kings 17-18 (Elijah and the drought). The 3.5-year duration matches Jas 5:17 (likely traditional Christian-Jewish chronology). Jesus introduces the foreign-recipient theme that will enrage the audience in v.28. ADDED TO NT_OT_CITATIONS: LUK 4:25 thematic_allusion to 1KI 17:1-7 (Elijah's drought announcement) + JAS 5:17 (parallel...

**Luke 4:26**
- GR: καὶ πρὸς οὐδεμίαν αὐτῶν ἐπέμφθη Ἠλίας εἰ μὴ εἰς Σάρεπτα τῆς Σιδωνίας πρὸς γυναῖκα χήραν.
- TH: แต่พระเจ้ามิได้ทรงใช้เอลียาห์ไปยังหญิงม่ายเหล่านั้นเลย เว้นแต่ไปยังหญิงม่ายชาวต่างชาติคนหนึ่งที่เมืองศาเรฟัทแห่งเขตไซดอน
- Key decisions:
  - πρὸς οὐδεμίαν αὐτῶν ἐπέμφθη Ἠλίας → พระเจ้ามิได้ทรงใช้เอลียาห์ไปยังหญิงม่ายเหล่านั้นเลย — Per uW figs-activepassive: ἐπέμφθη aorist-passive — agent (God) supplied for clarity. Divine-action ทรงใช้ (royal). The double negative οὐδεμίαν...εἰ μή = 'not to any...except' — Per uW grammar-connect-exceptions: T...
  - εἰς Σάρεπτα τῆς Σιδωνίας πρὸς γυναῖκα χήραν → ไปยังหญิงม่ายชาวต่างชาติคนหนึ่งที่เมืองศาเรฟัทแห่งเขตไซดอน — HAPAX: Σάρεπτα (only here in NT) — Phoenician town near Sidon. Thai ศาเรฟัท (standard Thai Christian transliteration; cf. 1 Kgs 17:9 Thai OT). Σιδωνία 'region of Sidon' → เขตไซดอน. Per uW figs-explicit: hearers woul...
- Notes: HAPAX: Σάρεπτα (only NT occurrence — proper-noun hapax). Reference to 1 Kings 17:8-24. Zarephath was Phoenician (Gentile) territory. The theological scandal: God bypasses Israelite need to provide for a Gentile widow. Jesus's audience hears this as confirmation that God's grace will go to Gentiles, leaving them empty. ADDED TO NT_OT_CITATIONS:...

**Luke 4:27**
- GR: καὶ πολλοὶ λεπροὶ ἦσαν ἐν τῷ Ἰσραὴλ ἐπὶ Ἐλισαίου τοῦ προφήτου, καὶ οὐδεὶς αὐτῶν ἐκαθαρίσθη, εἰ μὴ Ναιμὰν ὁ Σύρος.
- TH: และในสมัยของเอลีชาผู้เผยพระวจนะ มีคนโรคเรื้อนมากมายในอิสราเอล แต่ไม่มีคนใดได้รับการรักษาให้สะอาด เว้นแต่นาอามานชาวซีเรีย»
- TH-summary: ตัวอย่างที่สอง — เอลีชาผู้เผยพระวจนะ ในสมัยของเอลีชามีชาวอิสราเอลโรคเรื้อนมากมาย แต่พระเจ้าทรงรักษานาอามาน — แม่ทัพชาวซีเรีย (อาราม) ผู้เป็นทั้งคนต่างชาติและศัตรูของอิสราเอล (2 พกษ 5) ภาพนี้รุนแรงยิ่งกว่ากรณีแรก — ไม่ใช่แค่หญิงม่ายต่างชาติ แต่เป็นแม่ทัพของกองทัพศัตรู ทั้งสองตัวอย่างชี้ให้เห็นว่าพระคุณของพระเจ้าไม่จำกัดด้วยพรมแดนของอิสราเอล แต่จะไหลไปสู่ผู้ที่เปิดรับด้วยความเชื่อ ไม่ว่าจะเป็นชนชาติใด — เป็นการเปิดเผยล่วงหน้าถึงพันธกิจของอัครทูตในกิจการ
- Key decisions:
  - πολλοὶ λεπροὶ ἦσαν ἐν τῷ Ἰσραὴλ ἐπὶ Ἐλισαίου → ในสมัยของเอลีชาผู้เผยพระวจนะ มีคนโรคเรื้อนมากมายในอิสราเอล — HAPAX: Ἐλισαῖος (only here in NT) — proper-noun hapax. Thai เอลีชา (standard transliteration; cf. 2 Kgs Thai OT). λεπρός → คนโรคเรื้อน (glossary-established MRK 1:40). Note: NT λέπρα covered various skin conditions,...
  - οὐδεὶς αὐτῶν ἐκαθαρίσθη → ไม่มีคนใดได้รับการรักษาให้สะอาด — Per uW figs-activepassive: ἐκαθαρίσθη aorist-passive 'was cleansed.' Per uW grammar-connect-exceptions: same exception structure as v.26. καθαρίζω in leprosy-context = ritual purification (Lev 13-14) — Thai «รักษาให...
  - εἰ μὴ Ναιμὰν ὁ Σύρος → เว้นแต่นาอามานชาวซีเรีย — TWO HAPAX: Ναιμάν (only here in NT, proper-noun) and Σύρος (only here in NT, also rare in NT generally). Naaman → นาอามาน (standard Thai transliteration; cf. 2 Kgs 5 Thai OT). Σύρος 'Syrian' → ชาวซีเรีย. Per uW figs...
- Notes: THREE HAPAX (proper nouns): Ἐλισαῖος, Ναιμάν, Σύρος. Reference to 2 Kings 5:1-14. Naaman was COMMANDER of the Syrian army — not just any Gentile but a representative of a hostile nation. The escalation from v.26: foreign widow (passive recipient) → foreign army commander (active enemy). ADDED TO NT_OT_CITATIONS: LUK 4:27 thematic_allusion to 2...

**Luke 4:28**
- GR: καὶ ἐπλήσθησαν πάντες θυμοῦ ἐν τῇ συναγωγῇ ἀκούοντες ταῦτα,
- TH: เมื่อทุกคนในธรรมศาลาได้ยินถ้อยคำเหล่านี้ ก็เต็มไปด้วยความโกรธ
- Key decisions:
  - ἐπλήσθησαν πάντες θυμοῦ → ทุกคน...ก็เต็มไปด้วยความโกรธ — Per uW figs-activepassive + figs-personification: πίμπλημι aorist-passive 'were filled.' θυμός 'wrath, rage, fury' (more intense than ὀργή) → ความโกรธ. Thai «เต็มไปด้วยความโกรธ» captures the filling-personification ...
- Notes: Per uW figs-explicit: the wrath is triggered by Jesus's two-Gentile-recipient examples (vv.25-27) which seem to confirm that God's grace will pass over the Israelite hearers in favor of outsiders. The Gentile-grace theme is core-Lukan (cf. 2:32 'a light to the Gentiles'; Acts 13-28 the Gentile mission). The Nazareth crowd's reaction prefigures...

**Luke 4:29**
- GR: καὶ ἀναστάντες ἐξέβαλον αὐτὸν ἔξω τῆς πόλεως, καὶ ἤγαγον αὐτὸν ἕως ὀφρύος τοῦ ὄρους ἐφ᾽ οὗ ἡ πόλις ᾠκοδόμητο αὐτῶν, ὥστε κατακρημνίσαι αὐτόν·
- TH: พวกเขาลุกขึ้นขับไล่พระองค์ออกไปนอกเมือง แล้วนำพระองค์ไปยังขอบหน้าผาของภูเขาที่เมืองของตนตั้งอยู่ เพื่อจะผลักพระองค์ลงไป
- TH-summary: ความโกรธของชาวบ้านพุ่งขึ้นถึงขั้นพยายามฆ่าพระเยซู — ขับออกจากเมือง นำไปยังหน้าผา (ὀφρῦς หมายตามตัวอักษรว่า «คิ้ว» = ขอบของหน้าผา ปรากฏเพียงครั้งเดียวในพันธสัญญาใหม่) เพื่อ «κατακρημνίζω» (ผลักลงเหว — hapax อีกคำหนึ่ง) นาซาเร็ธปัจจุบันมีหน้าผาทางทิศใต้ของเมืองสูงราว 30-40 ฟุต ซึ่งเชื่อกันว่าเป็นสถานที่ของเหตุการณ์นี้ ความรุนแรงของฝูงชนที่เพิ่งจะ «อัศจรรย์ใจในถ้อยคำแห่งพระคุณ» แสดงให้เห็นว่าใจมนุษย์เปลี่ยนจากความชื่นชมเป็นความเกลียดเร็วเพียงใดเมื่อความเชื่อแย้งกับอคติ
- Key decisions:
  - ἀναστάντες ἐξέβαλον αὐτὸν ἔξω τῆς πόλεως → ลุกขึ้นขับไล่พระองค์ออกไปนอกเมือง — ἀνίστημι aorist-participle 'standing up' + ἐκβάλλω aorist 'cast out, drive out' — physical force implied. Thai «ลุกขึ้นขับไล่...ออกไป» preserves the violent expulsion. Note: ἐκβάλλω is the same verb used elsewhere f...
  - ἕως ὀφρύος τοῦ ὄρους → ยังขอบหน้าผาของภูเขา — HAPAX: ὀφρῦς (only here in NT) — literally 'eyebrow' (the brow ridge); metaphorically 'edge, brink, rim' of a hill or cliff. Classical usage: brow of a hill = the projecting edge. Thai «ขอบหน้าผา» (edge of cliff) ca...
  - ἐφ᾽ οὗ ἡ πόλις ᾠκοδόμητο αὐτῶν → ที่เมืองของตนตั้งอยู่ — οἰκοδομέω pluperfect-passive 'had been built' — Per uW figs-activepassive: Thai «ตั้งอยู่» (is situated, was built) actives the passive cleanly. αὐτῶν (their) → «ของตน» (their own — reflexive), preserving the sense ...
  - ὥστε κατακρημνίσαι αὐτόν → เพื่อจะผลักพระองค์ลงไป — HAPAX: κατακρημνίζω (only here in NT) — 'to throw down headlong, hurl off a precipice.' Compound of κατά (down) + κρημνός (cliff). Per uW figs-explicit: the goal was to kill — throwing-off-cliff = stoning-substitute...
- Notes: TWO HAPAX in single verse: ὀφρῦς, κατακρημνίζω — both rare classical-Greek terms. The geography matches modern Nazareth's southern cliff edge (the so-called «Mount of the Precipice»). The attempted murder pattern foreshadows Jesus's eventual crucifixion just outside Jerusalem (Heb 13:12 «outside the gate»), echoing the broader prophet-pattern ...

**Luke 4:30**
- GR: αὐτὸς δὲ διελθὼν διὰ μέσου αὐτῶν ἐπορεύετο.
- TH: แต่พระองค์เสด็จผ่านกลางพวกเขาไป
- TH-summary: ทางออกของพระเยซูที่นี่เป็นหนึ่งในเหตุการณ์ลึกลับที่สุดของพระวรสาร — ลูกามิได้อธิบายว่า «อย่างไร» พระองค์ทรงเดินผ่านฝูงชนที่กำลังต้องการฆ่าได้ พระองค์ไม่ทำอัศจรรย์ที่ระบุชัด แต่เพียงแค่ «เสด็จผ่านกลางพวกเขาไป» — สื่อถึงอำนาจและพระประสงค์ของพระเจ้า เวลาของพระองค์ยังไม่ถึง พระเยซูจะทรงสิ้นพระชนม์ที่กรุงเยรูซาเล็มในเวลาที่พระบิดากำหนด ไม่ใช่ที่หน้าผานาซาเร็ธในมือของฝูงชนที่โกรธ (เทียบ ยน 7:30; 8:59; 10:39 — ทรงผ่านฝูงชนที่ต้องการฆ่าหลายครั้ง)
- Key decisions:
  - αὐτὸς δὲ διελθὼν διὰ μέσου αὐτῶν → แต่พระองค์เสด็จผ่านกลางพวกเขาไป — Emphatic αὐτός 'he himself' — Thai stays with «พระองค์» (sufficient honor-emphasis). διέρχομαι aorist-participle + διὰ μέσου = 'passing through middle of.' Divine subject + movement → เสด็จ. Per uW writing-implicit:...
  - ἐπορεύετο → ไป (incorporated into «เสด็จผ่านกลางพวกเขาไป») — πορεύομαι imperfect = 'was going on his way' — sustained departure. Thai integrates into the previous verb «เสด็จ...ไป» since two separate verbs would over-stage in Thai.
- Notes: Synoptic parallel ends here — Mt 13:54-58 and Mk 6:1-6 both end with the rejection theme but neither narrates an attempted lynching/escape. Luke alone records the murder attempt and miraculous passing-through. The episode prefigures John 7:30 («no one laid hands on him because his hour had not yet come»), 8:59, 10:39 (similar near-stoning esca...

**Luke 4:31**
- GR: Καὶ κατῆλθεν εἰς Καφαρναοὺμ πόλιν τῆς Γαλιλαίας. καὶ ἦν διδάσκων αὐτοὺς ἐν τοῖς σάββασιν·
- TH: พระองค์เสด็จลงไปยังเมืองคาเปอรนาอุมในแคว้นกาลิลี และทรงสั่งสอนพวกเขาในวันสะบาโต
- Key decisions:
  - κατῆλθεν εἰς Καφαρναοὺμ → เสด็จลงไปยังเมืองคาเปอรนาอุม — Per uW figs-idiom: κατέρχομαι 'go down' refers to physical elevation — Capernaum is on Sea of Galilee (~700 ft below sea level), Nazareth in the hills (~1200 ft above sea level), so going from Nazareth to Capernaum ...
  - πόλιν τῆς Γαλιλαίας → เมือง...ในแคว้นกาลิลี — Per uW figs-explicit: since Nazareth is also in Galilee, Luke specifies for non-Palestinian readers (Theophilus). Thai «ในแคว้นกาลิลี» — Galilee already established as แคว้นกาลิลี.
  - ἦν διδάσκων αὐτοὺς ἐν τοῖς σάββασιν → ทรงสั่งสอนพวกเขาในวันสะบาโต — Periphrastic imperfect (ἦν + present-participle) = 'was teaching' — sustained/customary action. Plural σάββασιν (here singular sense as in v.16). Thai «ทรงสั่งสอน» (royal teaching). σάββασιν is plural but refers to ...
- Notes: Capernaum was Jesus's adopted home base for Galilean ministry (cf. Mt 4:13 'leaving Nazareth, he came and dwelt in Capernaum'). The town sat on the northwest shore of the Sea of Galilee — economic center, fishing town, customs station. Matthew's parallel account cites a messianic-fulfillment prophecy for Jesus's Capernaum residency; Luke simpl...

**Luke 4:32**
- GR: καὶ ἐξεπλήσσοντο ἐπὶ τῇ διδαχῇ αὐτοῦ, ὅτι ἐν ἐξουσίᾳ ἦν ὁ λόγος αὐτοῦ.
- TH: พวกเขาก็พากันอัศจรรย์ใจในคำสอนของพระองค์ เพราะพระวจนะของพระองค์เปี่ยมด้วยสิทธิอำนาจ
- Key decisions:
  - ἐξεπλήσσοντο ἐπὶ τῇ διδαχῇ αὐτοῦ → พวกเขาก็พากันอัศจรรย์ใจในคำสอนของพระองค์ — Per uW figs-activepassive: ἐκπλήσσω passive 'were astonished, struck out [of normal state].' Thai «พากันอัศจรรย์ใจ» actives the passive idiomatically. διδαχή 'teaching/doctrine' → คำสอน.
  - ἐν ἐξουσίᾳ ἦν ὁ λόγος αὐτοῦ → พระวจนะของพระองค์เปี่ยมด้วยสิทธิอำนาจ — Per uW figs-metonymy: λόγος 'word' = the things-taught, his message. Divine speech → พระวจนะ (royal). ἐξουσία → สิทธิอำนาจ (glossary-consistent). Mark 1:22 parallel adds «οὐχ ὡς οἱ γραμματεῖς» (not like the scribes)...
- Notes: Synoptic parallel: Mark 1:22 (longer form). Luke truncates Mark's contrast with the scribes. The amazement at authoritative teaching is the natural reaction to a teacher who declares 'today this Scripture is fulfilled' (v.21) without appeal to other rabbinic authorities.

**Luke 4:33**
- GR: καὶ ἐν τῇ συναγωγῇ ἦν ἄνθρωπος ἔχων πνεῦμα δαιμονίου ἀκαθάρτου, καὶ ἀνέκραξεν φωνῇ μεγάλῃ·
- TH: ในธรรมศาลามีชายคนหนึ่งซึ่งมีวิญญาณผีโสโครกสิงอยู่ เขาร้องเสียงดังว่า
- Key decisions:
  - ἦν ἄνθρωπος ἔχων πνεῦμα δαιμονίου ἀκαθάρτου → มีชายคนหนึ่งซึ่งมีวิญญาณผีโสโครกสิงอยู่ — Per uW writing-participants: 'there was a man' = new-character introduction. Thai «มีชายคนหนึ่ง» = standard Thai narrative-new-participant form. πνεῦμα δαιμονίου ἀκαθάρτου = 'spirit of an unclean demon' — somewhat r...
  - ἀνέκραξεν φωνῇ μεγάλῃ → เขาร้องเสียงดังว่า — Per uW figs-idiom: ἀνακράζω + φωνῇ μεγάλῃ = 'shouted with great voice' — Thai idiom «ร้องเสียงดัง». Demon-as-subject doesn't get any honorific.
- Notes: Synoptic parallel: Mark 1:23-26 (almost verbatim). Luke's «πνεῦμα δαιμονίου ἀκαθάρτου» adds δαιμονίου to Mark's «πνεῦμα ἀκάθαρτον» — Luke is more explicit about the demonic nature (his medical-scientific-precise tendency). 1st-c. Jewish demonology held that 'unclean spirits' inhabited people, causing illness, madness, or self-destructive behavior.

**Luke 4:34**
- GR: Ἔα, τί ἡμῖν καὶ σοί, Ἰησοῦ Ναζαρηνέ; ἦλθες ἀπολέσαι ἡμᾶς; οἶδά σε τίς εἶ, ὁ ἅγιος τοῦ θεοῦ.
- TH: «โอ๊ย เรามีเรื่องอะไรกับท่าน พระเยซูชาวนาซาเร็ธ? ท่านมาเพื่อทำลายพวกเราหรือ? เรารู้ว่าท่านเป็นใคร — องค์บริสุทธิ์ของพระเจ้า!»
- TH-summary: ผีร้องตะโกนคำอุทานแบบไม่อยากพบ «Ἔα» (เป็น hapax — ปรากฏเพียงครั้งเดียวในพันธสัญญาใหม่) คำนี้เป็นคำแสดงความตกใจหรือต่อต้าน คำถาม «τί ἡμῖν καὶ σοί» เป็นสำนวนเซมิติก (เทียบ ยช 22:24; ผพ 17:18; 2 พกษ 3:13) แปลว่า «เรากับท่านมีอะไรเกี่ยวข้องกัน?» — แสดงความเป็นปรปักษ์ น่าสังเกตว่าผีคือผู้แรกในพระวรสารลูกาที่ระบุพระเยซูว่าเป็น «องค์บริสุทธิ์ของพระเจ้า» — ตำแหน่งพระเมสสิยาห์ที่ปรากฏในกูราน (ดนล 9:24 «ผู้บริสุทธิ์ที่สุด») และสดุดี 16:10 ในพระคำของเทพดาที่บัพติศมา (3:22) — ผีรู้ว่าพระเยซูคือใคร แม้กระทั่งก่อนสาวกของพระองค์
- Key decisions:
  - Ἔα → โอ๊ย — HAPAX: ἔα (only here in NT) — interjection of surprise, alarm, or dismay. Possibly originating as imperative of ἐάω 'leave alone, let be' but used as exclamation. Thai «โอ๊ย» captures the alarmed-resistance interjec...
  - τί ἡμῖν καὶ σοί → เรามีเรื่องอะไรกับท่าน — Per uW figs-idiom: Semitic idiom (Hebrew מַה־לִּי וָלָךְ) literally 'what to me and to you?' = 'what business between us?' Thai «เรามีเรื่องอะไรกับท่าน» captures the antagonistic-distancing sense. ἡμῖν plural (we — ...
  - Ἰησοῦ Ναζαρηνέ → พระเยซูชาวนาซาเร็ธ — Vocative 'Jesus of Nazareth.' Even hostile demon uses the divine-name พระเยซู — pristine fact. Ναζαρηνός → ชาวนาซาเร็ธ (established MRK 1:24, 14:67, 16:6, etc.; LUK 24:19 has ὁ Ναζωραῖος rendered same way).
  - ἦλθες ἀπολέσαι ἡμᾶς → ท่านมาเพื่อทำลายพวกเราหรือ — Per uW figs-rquestion: question-as-statement — 'you have come to destroy us, haven't you?' Thai keeps question form «หรือ» since the rhetorical-fear is preserved. ἀπόλλυμι aorist-infinitive 'destroy.' ἦλθες aorist '...
  - οἶδά σε τίς εἶ, ὁ ἅγιος τοῦ θεοῦ → เรารู้ว่าท่านเป็นใคร — องค์บริสุทธิ์ของพระเจ้า! — οἶδα perfect-with-present-meaning = 'I know.' σε...τίς εἶ = double-accusative + indirect question 'you, who you are.' Thai «เรารู้ว่าท่านเป็นใคร» preserves the structure. ὁ ἅγιος τοῦ θεοῦ = 'the Holy One of God' — T...
- Notes: HAPAX: ἔα. Synoptic parallel: Mk 1:24 (almost verbatim). Demonic recognition theme — demons consistently confess Jesus's identity in the Synoptics, but Jesus silences them (cf. v.41, Mk 1:25, 1:34, 3:11-12). The 'Holy One of God' title may echo Ps 16:10 (LXX 'τὸν ὅσιόν σου') applied messianically in Acts 2:27. Demons' superior knowledge of Jes...

**Luke 4:35**
- GR: καὶ ἐπετίμησεν αὐτῷ ὁ Ἰησοῦς λέγων· Φιμώθητι καὶ ἔξελθε ἀπ᾽ αὐτοῦ. καὶ ῥίψαν αὐτὸν τὸ δαιμόνιον εἰς τὸ μέσον ἐξῆλθεν ἀπ᾽ αὐτοῦ μηδὲν βλάψαν αὐτόν.
- TH: พระเยซูตรัสห้ามมันว่า «จงนิ่งเสีย และออกมาจากเขา!» ผีนั้นก็ผลักชายคนนั้นล้มลงตรงกลางผู้คน แล้วก็ออกมาจากเขา โดยไม่ได้ทำอันตรายเขาเลย
- Key decisions:
  - ἐπετίμησεν αὐτῷ ὁ Ἰησοῦς λέγων → พระเยซูตรัสห้ามมันว่า — ἐπιτιμάω 'rebuke, command sternly.' Divine subject + speech → ตรัสห้าม (royal authoritative-rebuke). มัน (neutral 'it') for the demon.
  - Φιμώθητι → จงนิ่งเสีย — Per uW figs-activepassive: φιμόω aorist-passive-imperative literally 'be muzzled' (μῦθος-related etymology) → 'be silent.' The muzzling-imagery is forceful in Greek; Thai «จงนิ่งเสีย» (be silent!) preserves the impe...
  - ἔξελθε ἀπ᾽ αὐτοῦ → ออกมาจากเขา — Aorist-imperative 'come out from him.' Direct command to demon. Thai «ออกมาจากเขา».
  - ῥίψαν αὐτὸν τὸ δαιμόνιον εἰς τὸ μέσον → ผีนั้นก็ผลักชายคนนั้นล้มลงตรงกลางผู้คน — ῥίπτω aorist-participle 'having thrown.' εἰς τὸ μέσον = 'into the middle' (i.e., visible to all). Thai «ผลัก...ล้มลงตรงกลางผู้คน» fills out the implicit 'in front of everyone.' Mark 1:26 parallel adds «σπαράξαν» (co...
  - ἐξῆλθεν ἀπ᾽ αὐτοῦ μηδὲν βλάψαν αὐτόν → แล้วก็ออกมาจากเขา โดยไม่ได้ทำอันตรายเขาเลย — ἐξέρχομαι aorist 'came out.' βλάπτω aorist-participle (rare classical-medical word — 'harm, injure') with μηδέν 'nothing.' Luke's medical eye notes the no-harm detail (cf. his addition vs. Mark). Thai «ไม่ได้ทำอันตร...
- Notes: Synoptic parallel: Mk 1:25-26. Luke's «μηδὲν βλάψαν αὐτόν» (without harming him) is Lukan addition — characteristic medical-author detail (Col 4:14, 'Luke the beloved physician'). The exorcism formula (rebuke + silence + expel) becomes the pattern for later Lukan exorcisms (cf. 8:29 Gerasene, 9:42 boy).

**Luke 4:36**
- GR: καὶ ἐγένετο θάμβος ἐπὶ πάντας, καὶ συνελάλουν πρὸς ἀλλήλους λέγοντες· Τίς ὁ λόγος οὗτος ὅτι ἐν ἐξουσίᾳ καὶ δυνάμει ἐπιτάσσει τοῖς ἀκαθάρτοις πνεύμασιν, καὶ ἐξέρχονται;
- TH: ความตกตะลึงเกิดขึ้นกับทุกคน พวกเขาพูดคุยกันว่า «คำสอนแบบไหนกัน? พระองค์ทรงสั่งวิญญาณโสโครกด้วยสิทธิอำนาจและฤทธิ์เดช และพวกมันก็ออกมา!»
- Key decisions:
  - ἐγένετο θάμβος ἐπὶ πάντας → ความตกตะลึงเกิดขึ้นกับทุกคน — Per uW figs-personification: θάμβος 'astonishment' personified as actively coming-upon people. Thai «ความตกตะลึงเกิดขึ้นกับ» preserves the personification-event idiomatically.
  - Τίς ὁ λόγος οὗτος → คำสอนแบบไหนกัน — Per uW figs-rquestion + figs-metonymy: λόγος here = teaching/message (as in v.32). Question-as-exclamation. Thai «คำสอนแบบไหนกัน» captures the amazed-question form.
  - ἐν ἐξουσίᾳ καὶ δυνάμει ἐπιτάσσει τοῖς ἀκαθάρτοις πνεύμασιν → พระองค์ทรงสั่งวิญญาณโสโครกด้วยสิทธิอำนาจและฤทธิ์เดช — Per uW figs-doublet: ἐξουσία + δύναμις = doublet emphasizing complete-control (right + power). Thai «สิทธิอำนาจและฤทธิ์เดช» preserves the double-emphasis (vs. Mark 1:27 simpler «κατ' ἐξουσίαν»). Divine subject + com...
- Notes: Synoptic parallel: Mark 1:27. Luke's doublet «ἐξουσίᾳ καὶ δυνάμει» (vs. Mark's single ἐξουσία) is a Lukan stylistic preference — see Lk 1:17 («πνεύματι καὶ δυνάμει Ἠλίου») and Acts 10:38 («δυνάμει καὶ Πνεύματι ἁγίῳ»). The crowd's response moves from 'authoritative teaching' (v.32) to 'authoritative power over demons' — escalating realization o...

**Luke 4:37**
- GR: καὶ ἐξεπορεύετο ἦχος περὶ αὐτοῦ εἰς πάντα τόπον τῆς περιχώρου.
- TH: ดังนั้น กิตติศัพท์เกี่ยวกับพระองค์ก็แพร่ไปทั่วทุกหนแห่งในเขตแดนนั้น
- Key decisions:
  - ἐξεπορεύετο ἦχος περὶ αὐτοῦ → กิตติศัพท์เกี่ยวกับพระองค์ก็แพร่ไป — Per uW writing-endofstory + figs-personification: ἐκπορεύομαι imperfect 'was spreading.' ἦχος 'sound, report, fame' → กิตติศัพท์ (consistent with v.14 φήμη). Thai «แพร่ไป» captures the active-spreading personification.
  - καὶ ἐξεπορεύετο → ดังนั้น...ก็แพร่ไป — Per uW grammar-connect-logic-result: καί here introduces the result. Thai «ดังนั้น...ก็» marks the cause-effect.
- Notes: End-of-pericope summary statement, parallel with v.14 (Galilean-news-spreads) — Luke uses these summary-cycles to frame his episodes. Mark 1:28 parallel uses ἀκοή 'report,' Luke uses ἦχος (more 'sound/echo'-flavored).

**Luke 4:38**
- GR: Ἀναστὰς δὲ ἀπὸ τῆς συναγωγῆς εἰσῆλθεν εἰς τὴν οἰκίαν Σίμωνος. πενθερὰ δὲ τοῦ Σίμωνος ἦν συνεχομένη πυρετῷ μεγάλῳ, καὶ ἠρώτησαν αὐτὸν περὶ αὐτῆς.
- TH: พระองค์เสด็จออกจากธรรมศาลาแล้วเข้าไปในบ้านของซีโมน แม่ยายของซีโมนนอนป่วยเป็นไข้สูง พวกเขาจึงทูลขอพระองค์ให้ทรงช่วยนาง
- Key decisions:
  - Ἀναστὰς δὲ ἀπὸ τῆς συναγωγῆς εἰσῆλθεν εἰς τὴν οἰκίαν Σίμωνος → พระองค์เสด็จออกจากธรรมศาลาแล้วเข้าไปในบ้านของซีโมน — Per uW writing-newevent: δέ marks new episode-shift. ἀνίστημι aorist-participle + εἰσέρχομαι aorist = sequential 'rose [from synagogue, ending the Sabbath visit] and entered.' Thai «เสด็จออก...แล้วเข้าไป» captures t...
  - πενθερὰ δὲ τοῦ Σίμωνος ἦν συνεχομένη πυρετῷ μεγάλῳ → แม่ยายของซีโมนนอนป่วยเป็นไข้สูง — πενθερά → แม่ยาย (mother-in-law, glossary-consistent). συνέχω present-passive-participle in periphrastic = 'was held [held-down, held-fast] by fever.' Per uW figs-idiom: «held by fever» = severely-sick idiom. πυρετὸ...
  - ἠρώτησαν αὐτὸν περὶ αὐτῆς → พวกเขาจึงทูลขอพระองค์ให้ทรงช่วยนาง — Per uW figs-explicit: ἐρωτάω + περί = 'asked about' = implicitly asked for healing. Thai «ทูลขอพระองค์ให้ทรงช่วย» makes the implicit healing-request explicit per uW guidance. ทูลขอ = honorific request to deity.
- Notes: Synoptic parallel: Mark 1:29-31, Mt 8:14-15. Luke's «πυρετῷ μεγάλῳ» (great fever) and «συνεχομένη» (gripped/held by) — medical terminology — supports the tradition of Luke as physician (Col 4:14). Galen and other Greek medical writers distinguished μέγας vs. μικρός fever as severity-grade. Simon's mother-in-law in Capernaum = Simon (future Pet...

**Luke 4:39**
- GR: καὶ ἐπιστὰς ἐπάνω αὐτῆς ἐπετίμησεν τῷ πυρετῷ, καὶ ἀφῆκεν αὐτήν· παραχρῆμα δὲ ἀναστᾶσα διηκόνει αὐτοῖς.
- TH: พระองค์เสด็จไปประทับอยู่เหนือนาง ทรงห้ามไข้ ไข้ก็ออกจากนาง ทันใดนั้นนางก็ลุกขึ้นปรนนิบัติพระองค์และคนอื่น ๆ
- TH-summary: การรักษาของพระเยซูที่นี่มีลักษณะเหมือนการขับผี — พระองค์ทรง «ห้าม» (ἐπετίμησεν คำเดียวกับที่ใช้ขับผีในข้อ 35) ไข้ ราวกับว่าโรคเป็นพลังร้ายที่ต้องขับไล่ ไม่ใช่แค่ความผิดปกติทางกาย ลูกาผู้เป็นแพทย์เห็นความเชื่อมโยงระหว่างความเจ็บป่วยกับฝ่ายมืดของโลกที่ตกในบาป (เทียบ ลก 13:11-16 ผู้หญิงคดงอ «ที่ซาตานผูกไว้สิบแปดปี») การที่นางลุกขึ้นและปรนนิบัติทันที (παραχρῆμα = ทันใดนั้น) แสดงให้เห็นว่าการรักษาเป็นจริง สมบูรณ์ ทันที ไม่ต้องพักฟื้น
- Key decisions:
  - ἐπιστὰς ἐπάνω αὐτῆς → พระองค์เสด็จไปประทับอยู่เหนือนาง — ἐφίστημι aorist-participle 'stood over.' Divine subject + standing → ประทับ (royal standing/positioning). ἐπάνω 'over, above' → เหนือ. Mark 1:31 parallel «ἤγειρεν αὐτὴν κρατήσας τῆς χειρός» (raised her by taking her...
  - ἐπετίμησεν τῷ πυρετῷ → ทรงห้ามไข้ — Same verb ἐπιτιμάω as v.35 (rebuking demon) — Luke unifies illness-and-demon under the same authority-language. Thai «ทรงห้ามไข้» (royal rebuke; ห้าม = forbid/restrain). Striking image of fever as quasi-personified ...
  - ἀφῆκεν αὐτήν → ไข้ก็ออกจากนาง — ἀφίημι aorist 'left, released.' Subject = the fever (continued from previous verb). Thai «ไข้ก็ออกจากนาง» supplies the subject for clarity (Greek leaves it implicit). Verb-choice «ออกจาก» echoes v.35 «ἔξελθε ἀπ' αὐτ...
  - παραχρῆμα δὲ ἀναστᾶσα διηκόνει αὐτοῖς → ทันใดนั้นนางก็ลุกขึ้นปรนนิบัติพระองค์และคนอื่น ๆ — παραχρῆμα 'immediately, at once' — Lukan favorite (10x Luke-Acts vs. 6x rest of NT). Thai «ทันใดนั้น». διακονέω imperfect 'began-to-serve' (ingressive) → ปรนนิบัติ. Per uW figs-idiom: 'served them' = prepared/served...
- Notes: Synoptic parallel: Mk 1:30-31; Mt 8:14-15. Luke's word-choice ἐπετίμησεν (rebuked) for the fever — paralleling demon-rebuking — is unique to him and theologically significant: Luke sees physical illness within the broader fallen-creation problem that Jesus's authority addresses. παραχρῆμα is Lukan signature vocabulary for instantaneous miracles.

**Luke 4:40**
- GR: Δύνοντος δὲ τοῦ ἡλίου ἅπαντες ὅσοι εἶχον ἀσθενοῦντας νόσοις ποικίλαις ἤγαγον αὐτοὺς πρὸς αὐτόν· ὁ δὲ ἑνὶ ἑκάστῳ αὐτῶν τὰς χεῖρας ἐπιτιθεὶς ἐθεράπευεν αὐτούς.
- TH: เมื่อดวงอาทิตย์กำลังตก คนทั้งปวงซึ่งมีคนเจ็บป่วยด้วยโรคต่าง ๆ ก็พาเขามาเฝ้าพระองค์ พระองค์ทรงวางพระหัตถ์บนตัวพวกเขาทีละคน และรักษาให้หาย
- TH-summary: วลี «เมื่อดวงอาทิตย์กำลังตก» เป็นรายละเอียดสำคัญทางวัฒนธรรม — ชาวยิวถือว่าวันสะบาโตจบลงเมื่อดวงอาทิตย์ตก หลังจากนั้นจึงสามารถ «ทำงาน» พาคนป่วยมาได้ การที่ลูการะบุเวลาแสดงถึงความเคารพต่อกฎสะบาโตของชาวเมืองคาเปอรนาอุม พวกเขาไม่ได้รอจนเช้า แต่ทันทีที่อนุญาตได้ก็พามา «ทีละคน» (ἑνὶ ἑκάστῳ) แสดงให้เห็นความเอาใจใส่ของพระเยซู ไม่ใช่การรักษาแบบเหมารวม แต่ทรงสัมผัสและรักษาแต่ละคนเป็นการเฉพาะตัว
- Key decisions:
  - Δύνοντος δὲ τοῦ ἡλίου → เมื่อดวงอาทิตย์กำลังตก — Per uW figs-explicit: sunset marked the end of the Sabbath (sunset to sunset = Jewish day). The crowd waited until Sabbath ended before bringing the sick (which would otherwise constitute 'work'). Thai «เมื่อดวงอาทิ...
  - ἅπαντες ὅσοι εἶχον ἀσθενοῦντας νόσοις ποικίλαις → คนทั้งปวงซึ่งมีคนเจ็บป่วยด้วยโรคต่าง ๆ — ἅπαντες (intensive πᾶς) 'all without exception.' ἀσθενέω present-participle 'being-sick.' νόσος ποικίλη 'various diseases' — Lukan vocabulary (cf. similar in 4:40 here, parallel Mt 4:24). Thai «คนทั้งปวง...โรคต่าง ๆ...
  - ὁ δὲ ἑνὶ ἑκάστῳ αὐτῶν τὰς χεῖρας ἐπιτιθεὶς ἐθεράπευεν αὐτούς → พระองค์ทรงวางพระหัตถ์บนตัวพวกเขาทีละคน และรักษาให้หาย — Per uW writing-implicit: ἑνὶ ἑκάστῳ 'on each one individually' — emphasizes personal attention. ἐπιτίθημι present-participle = customary/imperfect-aspect 'placing.' χείρ → พระหัตถ์ (royal hand). Thai «ทีละคน» preser...
- Notes: Synoptic parallel: Mk 1:32-34, Mt 8:16. Luke alone uses «ἑνὶ ἑκάστῳ» (each individual) — emphasizing the personal, hand-laying healing rather than mass exorcism. Mark notes Jesus 'cast out many demons' but Luke pictures methodical case-by-case healing. The hand-laying gesture becomes the church's healing pattern (Acts 6:6, 9:17, 28:8) and ordi...

**Luke 4:41**
- GR: ἐξήρχετο δὲ καὶ δαιμόνια ἀπὸ πολλῶν κραυγάζοντα καὶ λέγοντα ὅτι Σὺ εἶ ὁ υἱὸς τοῦ θεοῦ. καὶ ἐπιτιμῶν οὐκ εἴα αὐτὰ λαλεῖν, ὅτι ᾔδεισαν τὸν χριστὸν αὐτὸν εἶναι.
- TH: ผีก็ออกจากคนเป็นอันมากด้วย พลางร้องตะโกนว่า «ท่านเป็นพระบุตรของพระเจ้า» แต่พระองค์ทรงห้ามไม่ให้พวกมันพูด เพราะพวกมันรู้ว่าพระองค์ทรงเป็นพระคริสต์
- TH-summary: ผีรู้ตัวตนของพระเยซูล่วงหน้า — เรียกพระองค์ว่า «พระบุตรของพระเจ้า» (ตำแหน่งเดียวกับที่เสียงสวรรค์ตรัสที่บัพติศมา ในข้อ 3:22) แต่พระเยซูทรงห้ามไม่ให้ผีประกาศตัวตนของพระองค์ — ปรากฏการณ์ที่นักวิชาการเรียกว่า «ความลับของพระเมสสิยาห์» (Messianic Secret) เหตุผลที่เป็นไปได้: (1) คำพยานจากผีจะเป็นมลทินต่อพระวรสาร (2) ผู้คนจะคาดหวังพระเมสสิยาห์ทางการเมืองที่ผิด (3) เวลาของการเปิดเผยตามแผนของพระบิดายังไม่มาถึง — ต้องผ่านไม้กางเขนและการคืนพระชนม์ก่อน
- Key decisions:
  - ἐξήρχετο δὲ καὶ δαιμόνια ἀπὸ πολλῶν → ผีก็ออกจากคนเป็นอันมากด้วย — Per uW figs-explicit: implied that Jesus made the demons leave. Thai uses «ก็...ด้วย» (also/too) to integrate with v.40's healings — Jesus did BOTH healing AND exorcism in this evening session. δαιμόνιον → ผี (consi...
  - κραυγάζοντα καὶ λέγοντα → พลางร้องตะโกนว่า — Per uW figs-hendiadys: κραυγάζω + λέγω = single act 'shouting.' Thai «พลางร้องตะโกนว่า» merges the two into one continuous action.
  - Σὺ εἶ ὁ υἱὸς τοῦ θεοῦ → ท่านเป็นพระบุตรของพระเจ้า — Per uW guidelines-sonofgodprinciples: 'Son of God' is critical Christological title. Demons confessing this — same title used by devil at temptation (4:3, 4:9), by heavenly voice at baptism (3:22). Thai «พระบุตรของพ...
  - ἐπιτιμῶν οὐκ εἴα αὐτὰ λαλεῖν → พระองค์ทรงห้ามไม่ให้พวกมันพูด — ἐπιτιμάω present-participle (rebuking) + ἐάω imperfect (was-allowing — negated). Thai «ทรงห้ามไม่ให้» preserves both rebuke and prohibition. Divine subject → ทรงห้าม.
  - ᾔδεισαν τὸν χριστὸν αὐτὸν εἶναι → พวกมันรู้ว่าพระองค์ทรงเป็นพระคริสต์ — οἶδα pluperfect-with-imperfect-meaning 'knew.' Indirect-statement infinitive construction. χριστός → พระคริสต์ (RULES.md §4 non-negotiable). Thai preserves the indirect statement structure cleanly.
- Notes: The 'Messianic Secret' motif (Wrede's term) — Jesus consistently silences demonic confessions of his messianic identity (cf. 4:34, 8:28; Mk 1:25, 1:34, 3:11-12). Possible reasons: (1) demonic testimony is theologically tainted; (2) premature revelation could trigger political-messianic expectations; (3) the proper revelation requires the cross...

**Luke 4:42**
- GR: Γενομένης δὲ ἡμέρας ἐξελθὼν ἐπορεύθη εἰς ἔρημον τόπον· καὶ οἱ ὄχλοι ἐπεζήτουν αὐτόν, καὶ ἦλθον ἕως αὐτοῦ, καὶ κατεῖχον αὐτὸν τοῦ μὴ πορεύεσθαι ἀπ᾽ αὐτῶν.
- TH: เมื่อรุ่งสว่าง พระองค์เสด็จออกจากเมืองไปยังที่เปลี่ยวแห่งหนึ่ง ฝูงชนพากันค้นหาพระองค์ มาถึงพระองค์ และพยายามรั้งพระองค์ไว้ ไม่ให้เสด็จไปจากพวกเขา
- Key decisions:
  - Γενομένης δὲ ἡμέρας → เมื่อรุ่งสว่าง — Genitive-absolute 'day having come' = 'at daybreak.' Mark 1:35 parallel has «πρωῒ ἔννυχα λίαν» (very early while still dark) — Luke's «when day came» is a softer, dawn-arrives version. Thai «เมื่อรุ่งสว่าง» captures...
  - ἐξελθὼν ἐπορεύθη εἰς ἔρημον τόπον → พระองค์เสด็จออกจากเมืองไปยังที่เปลี่ยวแห่งหนึ่ง — ἔρημος τόπος → ที่เปลี่ยว (RULES.md §4: 'when solitary place'). Different rendering from ἔρημος alone (= ถิ่นทุรกันดาร, wilderness as region) — this is a 'deserted spot' for prayer/retreat. Thai «ออกจากเมือง» (out o...
  - οἱ ὄχλοι ἐπεζήτουν αὐτόν → ฝูงชนพากันค้นหาพระองค์ — ἐπιζητέω imperfect 'were searching for' — sustained search. Thai «พากันค้นหา» captures the collective searching.
  - κατεῖχον αὐτὸν τοῦ μὴ πορεύεσθαι ἀπ᾽ αὐτῶν → พยายามรั้งพระองค์ไว้ ไม่ให้เสด็จไปจากพวกเขา — κατέχω imperfect 'were holding back, restraining' (conative imperfect — trying to). Articular-infinitive τοῦ μὴ + present-infinitive = preventive purpose. Thai «พยายามรั้ง...ไว้ ไม่ให้» captures both conative force ...
- Notes: Synoptic parallel: Mk 1:35-37 (similar but Luke modifies). Mark has Jesus go out 'very early while still dark' for prayer; Luke shifts to 'at daybreak' and downplays the prayer (though Lukan-Jesus elsewhere prays often, cf. 5:16, 6:12, 9:18, 11:1). The crowd's attempt to detain Jesus shows their wrong-headed enthusiasm — wanting a stationary m...

**Luke 4:43**
- GR: ὁ δὲ εἶπεν πρὸς αὐτοὺς ὅτι Καὶ ταῖς ἑτέραις πόλεσιν εὐαγγελίσασθαί με δεῖ τὴν βασιλείαν τοῦ θεοῦ, ὅτι ἐπὶ τοῦτο ἀπεστάλην.
- TH: พระองค์ตรัสกับพวกเขาว่า «เราจำเป็นต้องประกาศข่าวประเสริฐแห่งอาณาจักรของพระเจ้าแก่เมืองอื่น ๆ ด้วย เพราะเราถูกส่งมาเพื่อการนี้»
- TH-summary: นี่คือคำประกาศของพระเยซูที่อธิบายภารกิจของพระองค์อย่างชัดเจน — «ประกาศข่าวประเสริฐแห่งอาณาจักรของพระเจ้า» เป็นวลีสำคัญที่ลูกาใช้สรุปเนื้อหาของคำเทศนาของพระเยซู (เทียบ ลก 8:1; 9:11; 16:16; กจ 8:12; 19:8; 28:23, 31) คำว่า δεῖ «จำเป็น» เป็นคำที่ลูกาใช้บ่อยเพื่อสะท้อนพระประสงค์ของพระเจ้า (ลก 2:49 «เรา «จำเป็น» ต้องอยู่ในพระนิเวศของพระบิดา»; 9:22 «บุตรมนุษย์ «จำเป็น» ต้องทนทุกข์»; 24:7) — บ่งชี้ว่าพระเยซูทรงทำตามแผนการของพระบิดาทุกขั้นตอน ไม่ใช่ทำตามความต้องการของฝูงชน
- Key decisions:
  - Καὶ ταῖς ἑτέραις πόλεσιν εὐαγγελίσασθαί με δεῖ → เราจำเป็นต้องประกาศข่าวประเสริฐ...แก่เมืองอื่น ๆ ด้วย — δεῖ 'it is necessary' — Lukan signature word for divine-plan necessity. Thai «จำเป็นต้อง» captures the obligation. εὐαγγελίσασθαι → ประกาศข่าวประเสริฐ (RULES.md §4 standard). καί 'also/even to other cities' → «ด้วย».
  - τὴν βασιλείαν τοῦ θεοῦ → อาณาจักรของพระเจ้า — RULES.md §4 non-negotiable. βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า. First explicit Lukan use of the kingdom-of-God phrase (cf. uW Front-matter on 'kingdom' as central Lukan concept).
  - ὅτι ἐπὶ τοῦτο ἀπεστάλην → เพราะเราถูกส่งมาเพื่อการนี้ — Per uW figs-activepassive: ἀπεστάλην aorist-passive 'I was sent.' Divine-passive (sent by the Father). Thai keeps the passive «เราถูกส่งมา» — it conveys Jesus's submission to the Father's mission. ἐπὶ τοῦτο 'for thi...
- Notes: Programmatic mission-statement. The phrase «εὐαγγελίσασθαι...τὴν βασιλείαν τοῦ θεοῦ» (preach-good-news the kingdom of God) becomes Luke's stock summary of Jesus's preaching content (8:1, 9:11; cf. 16:16) and the apostles' preaching content in Acts (8:12, 19:8, 28:23, 28:31). Mark 1:38 parallel has «ἵνα κἀκεῖ κηρύξω» (preach there too) — Luke a...

**Luke 4:44**
- GR: καὶ ἦν κηρύσσων εἰς τὰς συναγωγὰς τῆς Ἰουδαίας.
- TH: พระองค์ทรงประกาศในธรรมศาลาทั่วแคว้นยูเดีย
- TH-summary: ลูกาจบบทที่ 4 ด้วยประโยคสรุปสั้น — พระเยซูทรงประกาศในธรรมศาลาทั่ว «ยูเดีย» ซึ่งในบริบทนี้หมายถึงดินแดนของชาวยิวโดยทั่วไป (ทั้งกาลิลีและยูเดียอย่างเป็นทางการ) ไม่ใช่เพียงเขตยูเดียทางใต้ — เพราะข้อ 14, 31, 44 ทั้งหมดอยู่ในแคว้นกาลิลี การที่ลูกาใช้คำว่า «ยูเดีย» แทนคำว่า «กาลิลี» (เช่นในมาระโก 1:39) อาจสะท้อนการมองจากภายนอก (ลูกาเขียนสำหรับเทออฟิลัสซึ่งอาจเป็นชาวต่างชาติ) ที่เห็นทั้งดินแดนเป็น «ยูเดีย» ตามชื่อชาวยูดาห์
- Key decisions:
  - ἦν κηρύσσων εἰς τὰς συναγωγὰς τῆς Ἰουδαίας → พระองค์ทรงประกาศในธรรมศาลาทั่วแคว้นยูเดีย — Periphrastic imperfect (ἦν + present-participle) = 'was preaching' — sustained activity. Thai «ทรงประกาศ» (royal). κηρύσσω → ประกาศ (consistent with v.18, v.43). Per uW figs-explicit: 'Judea' here = the broader Jewi...
- Notes: End-of-pericope summary. KEY TEXTUAL ISSUE: SBLGNT/NA28/Critical text reads τῆς Ἰουδαίας (Judea); Byzantine-majority text reads τῆς Γαλιλαίας (Galilee). The harder reading is 'Judea' (since Jesus was clearly in Galilee), and most modern critical editions follow it — Luke uses Ἰουδαία in a broader sense covering Jewish territory generally (cf. ...


---

### Luke 10

**Luke 10:1**
- GR: Μετὰ δὲ ταῦτα ἀνέδειξεν ὁ κύριος καὶ ἑτέρους ἑβδομήκοντα δύο καὶ ἀπέστειλεν αὐτοὺς ἀνὰ δύο δύο πρὸ προσώπου αὐτοῦ εἰς πᾶσαν πόλιν καὶ τόπον οὗ ἤμελλεν αὐτὸς ἔρχεσθαι.
- TH: ภายหลังเหตุการณ์เหล่านี้ องค์พระผู้เป็นเจ้าทรงแต่งตั้งคนอื่นอีกเจ็ดสิบสองคน และทรงส่งพวกเขาออกไปล่วงหน้าพระองค์เป็นคู่ๆ เข้าไปในทุกเมืองและทุกแห่งที่พระองค์จะเสด็จไป
- TH-summary: ลูกาเล่าถึงการส่งสาวกรอบที่สอง คราวนี้ส่งเจ็ดสิบสองคน (บางต้นฉบับโบราณอ่านว่าเจ็ดสิบ) คู่กับการส่งสาวกสิบสองคนในบทก่อนหน้า เลขเจ็ดสิบสองสอดคล้องกับจำนวนชนชาติในโลกตามปฐมกาลบทที่ 10 ฉบับภาษากรีก อาจเป็นสัญลักษณ์ถึงพันธกิจที่จะขยายไปสู่ชนชาติทั้งปวงในอนาคต เช่นเดียวกับที่โมเสสเคยแต่งตั้งผู้ใหญ่เจ็ดสิบคนช่วยปกครองอิสราเอล (กันดารวิถี 11)
- Key decisions:
  - Μετὰ δὲ ταῦτα → ภายหลังเหตุการณ์เหล่านี้ — Per uW writing-newevent: Luke marks a new scene. Thai 'ภายหลังเหตุการณ์เหล่านี้' is the natural narrative-transition.
  - ὁ κύριος → องค์พระผู้เป็นเจ้า — Per uW: Luke refers to Jesus here by title 'the Lord' to emphasize his authority. Glossary-established κύριος → องค์พระผู้เป็นเจ้า for Lord-title. The narrator voice uses this divine title of Jesus — Lukan theologic...
  - ἀνέδειξεν → ทรงแต่งตั้ง — ἀναδείκνυμι aor-act 'appoint, commission, designate publicly.' Divine subject → ทรง-prefix (RULES §3). Thai 'แต่งตั้ง' captures the formal-designation sense.
  - ἑτέρους ἑβδομήκοντα δύο → คนอื่นอีกเจ็ดสิบสองคน — TEXTUAL VARIANT. SBLGNT/NA28 read ἑβδομήκοντα δύο (72), supported by P75, B, D. Alternative reading ἑβδομήκοντα (70) in א, A, C, W, Byzantine. We follow SBLGNT. ἕτερος 'others' = in addition to the Twelve. NEW GLOSS...
  - ἀνὰ δύο δύο → เป็นคู่ๆ — Per uW figs-idiom. ἀνά distributive; the doubled δύο δύο is emphatic Semitic-style distributive 'two by two.' Thai 'เป็นคู่ๆ' natural rendering.
  - πρὸ προσώπου αὐτοῦ → ล่วงหน้าพระองค์ — Per uW figs-metaphor: 'before his face' = 'ahead of him.' LXX idiom (Mal 3:1 πρὸ προσώπου μου) signaling forerunner-role. Thai 'ล่วงหน้า' is the natural Thai idiom.
  - οὗ ἤμελλεν αὐτὸς ἔρχεσθαι → ที่พระองค์จะเสด็จไป — μέλλω + inf 'was-about-to.' Divine-movement → เสด็จไป (RULES §3). Imperf 'was-about-to' implies imminent-future from the sending-moment.
- Notes: TEXTUAL VARIANT — '72' vs '70': SBLGNT/NA28 read ἑβδομήκοντα δύο (72) based on P75, B, D, old Latin, Syriac Sinaiticus; א A C W Θ and Byzantine read ἑβδομήκοντα (70). Critical-text consensus favors 72. The number may echo LXX Gen 10's 72 nations (vs. MT's 70) — Luke's Gentile mission-theology suits this (cf. Acts 2's 'every nation under heaven...

**Luke 10:2**
- GR: ἔλεγεν δὲ πρὸς αὐτούς·Ὁ μὲν θερισμὸς πολύς,οἱ δὲ ἐργάται ὀλίγοι·δεήθητε οὖν τοῦ κυρίου τοῦ θερισμοῦ ὅπως ἐργάτας ἐκβάλῃ εἰς τὸν θερισμὸν αὐτοῦ.
- TH: พระองค์ตรัสกับพวกเขาว่า «การเก็บเกี่ยวนั้นมีมาก แต่คนงานมีน้อย เพราะฉะนั้นจงทูลขอต่อองค์พระผู้เป็นเจ้าแห่งการเก็บเกี่ยว ให้ทรงส่งคนงานออกไปเก็บเกี่ยวของพระองค์เถิด
- TH-summary: ภาพของการเก็บเกี่ยวเป็นคำเปรียบเทียบประจำคัมภีร์เกี่ยวกับยุคสุดท้าย (โยเอล 3, อิสยาห์ 27, เยเรมีย์ 51) ที่พระเจ้าจะทรงรวบรวมผู้ที่เชื่อเข้ามาในอาณาจักรของพระองค์ พระเยซูทรงชี้ว่าผู้คนพร้อมจะเข้ามาแล้ว แต่ขาดแคลนคนงานที่จะประกาศ คำว่า «ทรงส่ง» (ἐκβάλλῃ) ในภาษากรีกเป็นคำเดียวกับที่ใช้กับการขับไล่ผี สื่อถึงความเร่งรีบของพระเจ้าในการส่งผู้รับใช้
- Key decisions:
  - ὁ θερισμὸς πολύς → การเก็บเกี่ยวนั้นมีมาก — θερισμός → การเก็บเกี่ยว (glossary-established Matt 13). μέν...δέ contrast marked with 'นั้น...แต่' in Thai. Per uW figs-metaphor: harvest = people ready for kingdom.
  - οἱ δὲ ἐργάται ὀλίγοι → แต่คนงานมีน้อย — ἐργάτης → คนงาน (laborer). Per uW figs-exmetaphor: workers = disciples who help others trust Jesus.
  - δεήθητε τοῦ κυρίου τοῦ θερισμοῦ → จงทูลขอต่อองค์พระผู้เป็นเจ้าแห่งการเก็บเกี่ยว — δέομαι aor-pass-imper 'beseech.' Humble-to-divine speech → ทูลขอ. ὁ κύριος τοῦ θερισμοῦ glossary-established phrase for 'Lord of the harvest' = God per uW figs-exmetaphor.
  - ὅπως ἐργάτας ἐκβάλῃ → ให้ทรงส่งคนงานออกไป — ἐκβάλλω aor-subj 'thrust-out' — stronger than simple 'send.' Same verb Jesus uses of exorcism (Luke 9:40). Divine-subject → ทรง-prefix. Thai 'ส่ง...ออกไป' captures the dispatching-with-urgency.
- Notes: Parallels Matt 9:37-38. Harvest-imagery stock-eschatological (Joel 3:13 LXX ἀποστείλατε δρέπανα, ὅτι παρέστηκεν τρύγητος; Isa 27:12, Jer 51:33, Hos 6:11). ἐκβάλλω 'thrust-out' — the same verb used of exorcism (Luke 9:40, 11:14) and Jesus' cleansing of the Temple (Matt 21:12). Not a gentle sending — the Lord must urgently dispatch. The metaphor...

**Luke 10:3**
- GR: ὑπάγετε·ἰδοὺ ἀποστέλλω ὑμᾶς ὡς ἄρνας ἐν μέσῳ λύκων.
- TH: จงไปเถิด ดูเถิด เราส่งพวกท่านออกไปเหมือนลูกแกะท่ามกลางหมาป่า
- Key decisions:
  - ὑπάγετε → จงไปเถิด — ὑπάγω pres-act-imper 'go forth.' Thai 'จงไปเถิด' polite-imperative.
  - ἰδοὺ → ดูเถิด — Attention-marker per uW figs-metaphor: 'Listen carefully now.' Thai 'ดูเถิด' standard rendering for ἰδού.
  - ἀποστέλλω ὑμᾶς → เราส่งพวกท่านออกไป — ἀποστέλλω pres-act 'I am sending.' Jesus-speaker, self-reference as dispatcher.
  - ὡς ἄρνας → เหมือนลูกแกะ — HAPAX ἀρήν — classical/Homeric Greek for young-lamb (Iliad 4.158; Hes. Op. 786). Distinct from ἀμνός (sacrificial-lamb) and πρόβατον (generic-sheep). LXX Isa 40:11 uses ἀρήν for gathered-Israel's young. Thai 'ลูกแกะ...
  - ἐν μέσῳ λύκων → ท่ามกลางหมาป่า — λύκος → หมาป่า. Per uW figs-simile + translate-unknown: wolves prey on lambs; the simile warns of hostile receivers. Alt gloss: 'predators among us' — but Thai 'หมาป่า' preserves the specific-image and is standard T...
- Notes: HAPAX ἀρήν — only NT use (ἀρνίον 'little lamb' is separate lexeme, 30x Revelation). Classical Greek pastoral vocabulary preserved here. LXX usage (Isa 40:11, 65:25) frames young-lambs as gathered-Israel-imagery — subtle continuity: Jesus sends his young-of-Israel into a hostile pagan-flock. Cf. fuller version Matt 10:16 (sheep-among-wolves + b...

**Luke 10:4**
- GR: μὴ βαστάζετε βαλλάντιον,μὴ πήραν,μὴ ὑποδήματα,καὶ μηδένα κατὰ τὴν ὁδὸν ἀσπάσησθε.
- TH: อย่านำถุงเงิน ย่าม หรือรองเท้าสำรองไป และอย่าทักทายผู้ใดตามระหว่างทาง
- Key decisions:
  - βαλλάντιον → ถุงเงิน — βαλλάντιον 'money-bag/purse.' Per uW figs-metonymy: represents the money it contains. Thai 'ถุงเงิน' literal+cultural fit.
  - πήραν → ย่าม — πήρα → ย่าม (glossary-established Luke 9:3). Traveler's shoulder-bag for provisions. Per uW figs-metonymy: represents the provisions.
  - ὑποδήματα → รองเท้าสำรอง — ὑπόδημα 'sandal.' Per uW figs-metonymy: the sandals stand for extra-equipment-beyond-essentials. Jesus isn't saying disciples go barefoot — Mark 6:9 'wear sandals.' Thai 'รองเท้าสำรอง' makes the spare/extra sense ex...
  - μηδένα κατὰ τὴν ὁδὸν ἀσπάσησθε → อย่าทักทายผู้ใดตามระหว่างทาง — Per uW figs-hyperbole: hyperbolic instruction for travel-urgency, not rudeness. Near-Eastern greetings were elaborate time-consuming rituals. Cf. 2 Kings 4:29 Elisha's similar instruction to Gehazi.
- Notes: Stricter than Luke 9:3 mission-charge (no staff, bag, bread, money, second tunic). Here: no money-bag, no traveler's-bag, no extra-sandals. The three items form a metonymic cluster for self-sufficient travel — disciples must depend on host-hospitality (developed in vv.5-8). The no-greetings-on-road has parallel in 2 Kgs 4:29 (Elisha sends Geha...

**Luke 10:5**
- GR: εἰς ἣν δ’ἂν εἰσέλθητε οἰκίαν πρῶτον λέγετε·Εἰρήνη τῷ οἴκῳ τούτῳ.
- TH: เมื่อพวกท่านเข้าไปในบ้านหลังใด จงพูดก่อนว่า «สันติสุขจงมีแก่ครัวเรือนนี้เถิด»
- Key decisions:
  - πρῶτον λέγετε → จงพูดก่อนว่า — πρῶτον 'first' — the greeting should be the first thing said. Thai 'จงพูดก่อน' natural.
  - Εἰρήνη τῷ οἴκῳ τούτῳ → สันติสุขจงมีแก่ครัวเรือนนี้เถิด — Per uW figs-idiom: Hebraic greeting based on shalom (שָׁלוֹם לַבַּיִת הַזֶּה). Functions both as greeting and blessing. Per uW figs-metonymy: οἶκος = household members. εἰρήνη → สันติสุข (glossary-established). Thai...
- Notes: The shalom-formula (cf. 1 Sam 25:6 שָׁלוֹם אָתָּה וְשָׁלוֹם בֵּיתֶךָ). In Jewish culture, this was simultaneously a greeting AND an invocation of divine blessing. Parallels Matt 10:12-13 (simpler form). Per uW figs-quotesinquotes: Jesus quoting what he wants disciples to say — Thai retains the direct-quotation format using guillemets.

**Luke 10:6**
- GR: καὶ ἐὰν ᾖ ἐκεῖ υἱὸς εἰρήνης,ἐπαναπαήσεται ἐπ’αὐτὸν ἡ εἰρήνη ὑμῶν·εἰ δὲ μήγε,ἐφ’ὑμᾶς ἀνακάμψει.
- TH: ถ้ามีผู้รักสันติสุขอยู่ที่นั่น สันติสุขของพวกท่านจะอยู่เหนือเขา แต่ถ้าไม่มี สันติสุขนั้นจะกลับคืนมาสู่พวกท่าน
- TH-summary: สำนวน «ผู้รักสันติสุข» (แปลตรงตัวจากภาษากรีกคือ «บุตรแห่งสันติสุข») เป็นรูปแบบภาษาฮีบรูและอาราเมคที่ใช้ระบุคนที่มีลักษณะหนึ่ง (เช่น «บุตรแห่งความสว่าง» «บุตรแห่งฟ้าร้อง») พระเยซูทรงหมายถึงผู้ที่เปิดใจรับข่าวประเสริฐและสภาพของอาณาจักรพระเจ้า พรแห่ง «สันติสุข» ถูกมองว่าเป็นของจริงที่ลงไปอยู่ที่ผู้เปิดรับ หรือสะท้อนกลับมาหากไม่มีใครต้อนรับ
- Key decisions:
  - υἱὸς εἰρήνης → ผู้รักสันติสุข — Per uW figs-idiom: Hebraic-Aramaic 'son of peace' = one characterized by peace. Per uW alt: 'a person who wants peace with God and with people.' Literal Thai 'บุตรแห่งสันติสุข' preserves idiom but obscures for Thai ...
  - ἐπαναπαήσεται ἐπ’ αὐτὸν ἡ εἰρήνη → สันติสุข...จะอยู่เหนือเขา — ἐπαναπαύω fut-pass 'will rest upon.' Per uW figs-metaphor: spatial metaphor = experience-in-lasting-way. Thai 'จะอยู่เหนือเขา' preserves the spatial-metaphor.
  - εἰ δὲ μήγε → แต่ถ้าไม่มี — Per uW figs-ellipsis: 'if not, [there is no such son of peace].' Thai 'แต่ถ้าไม่มี' supplies the implied referent.
  - ἐφ’ ὑμᾶς ἀνακάμψει → สันติสุขนั้นจะกลับคืนมาสู่พวกท่าน — Per uW figs-personification: peace described as a living-thing that could choose to leave and return. ἀνακάμπτω fut-act 'will return.' Thai 'กลับคืนมาสู่' preserves personification.
- Notes: The 'son of X' idiom is thoroughly Semitic — Hebrew ben-X, Aramaic bar-X (cf. Mark 3:17 'Boanerges' = sons-of-thunder; Luke 16:8 'sons of light' vs. 'sons of this age'; Eph 2:2 'sons of disobedience'). Not biological descent — identifying-characteristic. The peace-blessing is treated almost tangibly: it 'rests' on the receptive host or 'return...

**Luke 10:7**
- GR: ἐν αὐτῇ δὲ τῇ οἰκίᾳ μένετε,ἐσθίοντες καὶ πίνοντες τὰ παρ’αὐτῶν,ἄξιος γὰρ ὁ ἐργάτης τοῦ μισθοῦ αὐτοῦ.μὴ μεταβαίνετε ἐξ οἰκίας εἰς οἰκίαν.
- TH: จงพักอยู่ในบ้านเดียวกันนั้น กินและดื่มสิ่งที่เจ้าของบ้านจัดหาให้ เพราะว่าคนงานย่อมสมควรได้รับค่าจ้างของตน อย่าย้ายจากบ้านหลังหนึ่งไปอีกหลังหนึ่ง
- TH-summary: คำตรัสของพระเยซู «คนงานย่อมสมควรได้รับค่าจ้าง» ปรากฏในจดหมายเปาโลถึงทิโมธีฉบับที่ 1 บทที่ 5 ว่าเป็น «พระคัมภีร์» โดยอ้างคู่กับบัญญัติในเฉลยธรรมบัญญัติ 25:4 เกี่ยวกับวัวที่นวดข้าว เป็นหลักฐานยุคแรกๆ ของการที่คำตรัสของพระเยซูได้รับสถานะเทียบเท่าพระคัมภีร์ในคริสตจักรยุคเริ่มต้น หลักการนี้รองรับว่าผู้รับใช้พระเจ้าสมควรได้รับการอุปถัมภ์ด้านวัตถุจากชุมชนที่พวกเขารับใช้
- Key decisions:
  - ἐν αὐτῇ τῇ οἰκίᾳ μένετε → จงพักอยู่ในบ้านเดียวกันนั้น — μένω pres-act-imper 'stay.' Per uW: not 'stay there constantly' but 'make it your base.' Thai 'พักอยู่...เดียวกันนั้น' captures the single-lodging-base sense.
  - τὰ παρ’ αὐτῶν → สิ่งที่เจ้าของบ้านจัดหาให้ — Per uW figs-idiom: 'the things from them' = food/drink they provide. Thai makes the referent explicit.
  - ἄξιος γὰρ ὁ ἐργάτης τοῦ μισθοῦ αὐτοῦ → เพราะว่าคนงานย่อมสมควรได้รับค่าจ้างของตน — Per uW writing-proverbs. Proverbial statement. Cited in 1 Tim 5:18 as γραφή alongside Deut 25:4. ἐργάτης → คนงาน; μισθός → ค่าจ้าง. Present-generic 'ย่อม' marks the universal-truth register.
  - μὴ μεταβαίνετε ἐξ οἰκίας εἰς οἰκίαν → อย่าย้ายจากบ้านหลังหนึ่งไปอีกหลังหนึ่ง — μεταβαίνω pres-act-imper 'move/change-place.' Per uW: repeats earlier 'stay' for emphasis — don't shop-around for better accommodations. Protects host's honor.
- Notes: Proverbial wisdom-statement quoted by Paul in 1 Tim 5:18 as γραφή ('For the Scripture says') alongside Deut 25:4 on not muzzling the threshing-ox. This is one of the earliest NT-within-NT scripture-citations of Jesus' words — significant for the reception-history of Jesus-logia as authoritative. The principle legitimates apostolic-support: min...

**Luke 10:8**
- GR: καὶ εἰς ἣν ἂν πόλιν εἰσέρχησθε καὶ δέχωνται ὑμᾶς,ἐσθίετε τὰ παρατιθέμενα ὑμῖν,
- TH: ในเมืองใดที่พวกท่านเข้าไปและมีคนต้อนรับพวกท่าน จงกินสิ่งที่เขาจัดมาวางตรงหน้าพวกท่าน
- Key decisions:
  - δέχωνται ὑμᾶς → มีคนต้อนรับพวกท่าน — Per uW writing-pronouns: 'they' = people-of-the-city. δέχομαι → ต้อนรับ (welcome, glossary-standard for hospitality-sense).
  - ἐσθίετε τὰ παρατιθέμενα ὑμῖν → จงกินสิ่งที่เขาจัดมาวางตรงหน้าพวกท่าน — παρατίθημι pres-pass-ptc 'set before.' Per uW figs-activepassive: could state 'the people serve you.' Thai 'จัดมาวางตรงหน้า' preserves the set-before-you image.
- Notes: Parallel to v.7's 'eat whatever they offer' but now at town-level (not just one house). Anticipates the Gentile-mission issue: eating what-is-served implies not imposing strict Jewish kosher-laws on hosts. Cf. Acts 10:13-15 Peter's vision; 1 Cor 10:27 Paul's similar instruction to Corinthians (if unbeliever invites you, eat what is set before ...

**Luke 10:9**
- GR: καὶ θεραπεύετε τοὺς ἐν αὐτῇ ἀσθενεῖς,καὶ λέγετε αὐτοῖς·Ἤγγικεν ἐφ’ὑμᾶς ἡ βασιλεία τοῦ θεοῦ.
- TH: จงรักษาคนเจ็บป่วยในเมืองนั้น และบอกพวกเขาว่า «อาณาจักรของพระเจ้ามาใกล้พวกท่านแล้ว»
- Key decisions:
  - θεραπεύετε τοὺς...ἀσθενεῖς → จงรักษาคนเจ็บป่วย — θεραπεύω → รักษา (glossary-standard). Per uW figs-nominaladj: ἀσθενής substantival 'the sick-ones' → คนเจ็บป่วย (glossary Luke 9:2 precedent).
  - Ἤγγικεν ἐφ’ ὑμᾶς ἡ βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้ามาใกล้พวกท่านแล้ว — ἐγγίζω perf-act 'has-drawn-near.' βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า (RULES §4 non-negotiable). Per uW figs-abstractnouns: could reformulate as 'God is ruling in this area' or 'God will soon begin to rule' — but...
- Notes: The 72-mission mirrors the Twelve (Luke 9:1-2): proclaim-and-heal. ἤγγικεν (perf) is a present-reality-emphasis: the kingdom has drawn-near and-is-now-near. Same verb in Luke 10:11 and Mark 1:15 — Jesus' programmatic kingdom-announcement. Per uW: the phrase can mean spatially-close (its activities are happening nearby) or temporally-close (soo...

**Luke 10:10**
- GR: εἰς ἣν δ’ἂν πόλιν εἰσέλθητε καὶ μὴ δέχωνται ὑμᾶς,ἐξελθόντες εἰς τὰς πλατείας αὐτῆς εἴπατε·
- TH: แต่ในเมืองใดที่พวกท่านเข้าไปและไม่มีคนต้อนรับพวกท่าน จงออกไปที่ถนนของเมืองนั้นและประกาศว่า
- Key decisions:
  - μὴ δέχωνται ὑμᾶς → ไม่มีคนต้อนรับพวกท่าน — Direct contrast with v.8 per uW. Negated present-subjunctive of δέχομαι.
  - εἰς τὰς πλατείας αὐτῆς → ที่ถนนของเมืองนั้น — πλατεῖα 'broad-street, plaza' — the public-space where the rejection would be witnessed. Thai 'ถนน' adequate.
- Notes: Sets up the dust-shaking pronouncement in v.11. The public street/plaza location is deliberate — the judgment-declaration must be witnessed by the community.

**Luke 10:11**
- GR: Καὶ τὸν κονιορτὸν τὸν κολληθέντα ἡμῖν ἐκ τῆς πόλεως ὑμῶν εἰς τοὺς πόδας ἀπομασσόμεθα ὑμῖν·πλὴν τοῦτο γινώσκετε ὅτι ἤγγικεν ἡ βασιλεία τοῦ θεοῦ.
- TH: «แม้แต่ฝุ่นจากเมืองของพวกท่านที่ติดเท้าของเรา เราก็ขอเช็ดออกต่อหน้าพวกท่าน อย่างไรก็ตาม จงทราบว่าอาณาจักรของพระเจ้าได้มาใกล้แล้ว»
- TH-summary: การ «เช็ดฝุ่นออกจากเท้า» เป็นการกระทำเชิงสัญลักษณ์ในวัฒนธรรมยิว เมื่อชาวยิวกลับจากดินแดนต่างชาติจะสะบัดฝุ่นออกเสียก่อนเข้าดินแดนบริสุทธิ์ พระเยซูทรงสอนให้สาวกใช้ภาพนี้ประกาศว่าเมืองที่ปฏิเสธข่าวประเสริฐได้กลายเป็นดินแดนนอกอาณาจักรของพระเจ้า แม้จะปฏิเสธแล้ว คำประกาศ «อาณาจักรของพระเจ้ามาใกล้แล้ว» ยังคงให้ไว้เป็นคำเตือน — พระคุณของพระเจ้าถูกเสนอก่อนการพิพากษา
- Key decisions:
  - κονιορτὸν τὸν κολληθέντα → ฝุ่น...ที่ติดเท้า — κονιορτός → ฝุ่น (dust). κολλάω aor-pass-ptc 'been-stuck-to.' Thai 'ที่ติดเท้า' natural.
  - ἀπομασσόμεθα ὑμῖν → เราขอเช็ดออกต่อหน้าพวกท่าน — HAPAX ἀπομάσσομαι — classical/Hellenistic 'wipe-off.' Per uW translate-symaction: symbolic-act of disassociation. Thai 'เช็ด...ออก' captures the wiping-gesture. 'ต่อหน้าพวกท่าน' preserves the ὑμῖν dative-of-disadvan...
  - πλὴν τοῦτο γινώσκετε → อย่างไรก็ตาม จงทราบว่า — Per uW figs-idiom: introduces a warning. Thai 'อย่างไรก็ตาม จงทราบ' natural warning-introducer.
  - ἤγγικεν ἡ βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้าได้มาใกล้แล้ว — Same perf-form as v.9 — consistency maintained. The kingdom-announcement is unchanged whether-accepted-or-rejected; the reception changes.
- Notes: HAPAX ἀπομάσσομαι — only NT use. Classical/Hellenistic 'to wipe off.' Parallel gestures use different verbs: Mark 6:11 and Matt 10:14 use ἐκτινάσσω 'shake off'; Acts 13:51 (Paul and Barnabas at Pisidian Antioch) also ἐκτινάσσω. Luke here uses the rarer ἀπομάσσομαι — possibly to avoid repeat with the later Acts narrative, or literary-variation....

**Luke 10:12**
- GR: λέγω ὑμῖν ὅτι Σοδόμοις ἐν τῇ ἡμέρᾳ ἐκείνῃ ἀνεκτότερον ἔσται ἢ τῇ πόλει ἐκείνῃ.
- TH: เราบอกพวกท่านว่า ในวันนั้น โสโดมจะทนรับโทษได้มากกว่าเมืองนั้นเสียอีก
- Key decisions:
  - ἐν τῇ ἡμέρᾳ ἐκείνῃ → ในวันนั้น — Per uW figs-idiom + figs-explicit: eschatological 'that day' = final judgment. Thai 'วันนั้น' preserves the Semitic-idiom pattern of referring to judgment day (cf. Isa 2:12, Joel 2:31). The context makes the referen...
  - Σοδόμοις...ἀνεκτότερον ἔσται ἢ τῇ πόλει ἐκείνῃ → โสโดมจะทนรับโทษได้มากกว่าเมืองนั้นเสียอีก — ἀνεκτότερον compar 'more-bearable.' Σόδομα → โสโดม. Per uW figs-metonymy + figs-explicit: Sodom = its people + paradigm for severe-judgment (Gen 19). Thai 'ทนรับโทษได้มากกว่า...เสียอีก' preserves the comparative-jud...
- Notes: Sodom is the OT paradigm for exemplary-divine-judgment (Gen 19; cited Deut 29:23, Isa 1:9, Jer 49:18, Lam 4:6, Amos 4:11, 2 Pet 2:6, Jude 7). The eschatological 'day' = final judgment (Mal 4:1 'the day is coming, burning like an oven'). The rhetorical logic: reject the kingdom-messengers = worse than Sodom's famous wickedness. This is theologi...

**Luke 10:13**
- GR: Οὐαί σοι,Χοραζίν·οὐαί σοι,Βηθσαϊδά·ὅτι εἰ ἐν Τύρῳ καὶ Σιδῶνι ἐγενήθησαν αἱ δυνάμεις αἱ γενόμεναι ἐν ὑμῖν,πάλαι ἂν ἐν σάκκῳ καὶ σποδῷ καθήμενοι μετενόησαν.
- TH: วิบัติแก่เจ้า โคราซิน วิบัติแก่เจ้า เบธไซดา เพราะหากการอัศจรรย์ทั้งหลายที่ได้กระทำในเจ้าได้กระทำในเมืองไทระและไซดอน ชาวเมืองนั้นคงจะกลับใจใหม่ตั้งแต่นานแล้ว นั่งในผ้ากระสอบและขี้เถ้า
- Key decisions:
  - Οὐαί σοι → วิบัติแก่เจ้า — Per uW figs-apostrophe + figs-idiom: woe-oracle addressed to cities as if they could hear. Thai 'วิบัติแก่เจ้า' standard Thai Christian prophetic-idiom. Per uW figs-metonymy: city-name = its inhabitants. σοι singula...
  - Χοραζίν...Βηθσαϊδά → โคราซิน...เบธไซดา — Proper nouns — glossary-established (Βηθσαϊδά at Luke 9:10; Χοραζίν from Matt 11:21 glossary).
  - δυνάμεις → การอัศจรรย์ทั้งหลาย — δύναμις in plural = 'mighty-works, miracles' (standard Synoptic-usage for Jesus' miracle-deeds). Thai 'การอัศจรรย์' standard.
  - Τύρῳ καὶ Σιδῶνι → เมืองไทระและไซดอน — Glossary-established (Luke 6:17 precedent; glossary ไทระและไซดอน).
  - πάλαι ἂν ἐν σάκκῳ καὶ σποδῷ καθήμενοι μετενόησαν → ชาวเมืองนั้นคงจะกลับใจใหม่ตั้งแต่นานแล้ว นั่งในผ้ากระสอบและขี้เถ้า — Per uW figs-hypo: counterfactual-past conditional. πάλαι 'long ago.' μετανοέω → กลับใจ (RULES §4 non-negotiable); adding 'ใหม่' for naturalness. Per uW translate-symaction: σάκκος καὶ σποδός = repentance gesture. Th...
- Notes: Parallels Matt 11:21-22 (Q-material). Chorazin + Bethsaida were Galilean towns where Jesus performed miracles (Chorazin not elsewhere attested in NT despite miracle-implication here; Bethsaida home of Peter/Andrew/Philip per John 1:44). Tyre + Sidon = Phoenician Gentile-cities notorious for wickedness (Isa 23; Ezek 26-28; Amos 1:9-10 denunciat...

**Luke 10:14**
- GR: πλὴν Τύρῳ καὶ Σιδῶνι ἀνεκτότερον ἔσται ἐν τῇ κρίσει ἢ ὑμῖν.
- TH: อย่างไรก็ตาม ในการพิพากษา ไทระและไซดอนจะทนรับโทษได้มากกว่าพวกเจ้า
- Key decisions:
  - ἐν τῇ κρίσει → ในการพิพากษา — Per uW figs-explicit: eschatological 'the judgment' = final assize. κρίσις → การพิพากษา (standard).
  - ἀνεκτότερον ἔσται...ἢ ὑμῖν → จะทนรับโทษได้มากกว่าพวกเจ้า — Parallels v.12 — matching rendering consistency. ὑμῖν dative — now plural since Chorazin+Bethsaida are addressed together. Per uW figs-youdual: dual 'you.'
- Notes: Parallels Matt 11:22. The judgment-logic is cumulative: revelation received + rejection = graver accountability. Rabbinic principle: greater light, greater responsibility (cf. Amos 3:2 'you only have I known of all the families of the earth, therefore I will punish you'). Luke consistently drives the measure-for-measure principle.

**Luke 10:15**
- GR: καὶ σύ,Καφαρναούμ,μὴ ἕως οὐρανοῦ ὑψωθήσῃ;ἕως τοῦ ᾅδου καταβιβασθήσῃ.
- TH: และเจ้า คาเปอร์นาอูม เจ้าจะถูกยกขึ้นถึงฟ้าสวรรค์หรือ? เจ้าจะถูกดิ่งลงไปถึงแดนคนตายต่างหาก
- TH-summary: พระเยซูทรงยืมคำพยากรณ์ของอิสยาห์ 14:13-15 ที่กล่าวแก่กษัตริย์บาบิโลน «เราจะขึ้นไปถึงฟ้าสวรรค์... แต่เจ้าจะถูกนำลงไปถึงแดนคนตาย» มาประยุกต์ใช้กับคาเปอร์นาอูม ซึ่งเป็นเมืองที่พระองค์ทรงใช้เป็นฐานในระหว่างการปฏิบัติพันธกิจในแคว้นกาลิลี (ลูกา 4:31) การนำคำพยากรณ์ที่พูดกับศัตรูของพระเจ้ามาใช้กับเมืองของตัวเองเป็นเรื่องหนักหน่วง — คาเปอร์นาอูมได้เห็นการอัศจรรย์มากกว่าเมืองใดๆ แต่ไม่ยอมกลับใจ
- Key decisions:
  - σύ, Καφαρναούμ → เจ้า คาเปอร์นาอูม — Per uW figs-apostrophe + figs-metonymy: city-address by name = the people. Καφαρναούμ → คาเปอร์นาอูม (standard Thai; note Thai Bibles variably render as คาเปอรนาอุม/คาเปอร์นาอูม — using คาเปอร์นาอูม). Per uW figs-yo...
  - μὴ ἕως οὐρανοῦ ὑψωθήσῃ → เจ้าจะถูกยกขึ้นถึงฟ้าสวรรค์หรือ? — Per uW figs-doublenegatives + figs-rquestion + figs-metaphor: μή + fut-pass = question expecting no-answer. Per uW: 'to be exalted' = spatial-metaphor for divine-honor. Thai 'เจ้าจะถูกยกขึ้น...หรือ?' preserves the i...
  - ἕως τοῦ ᾅδου καταβιβασθήσῃ → เจ้าจะถูกดิ่งลงไปถึงแดนคนตายต่างหาก — Per uW figs-metaphor + figs-activepassive: spatial-metaphor for punishment-and-dishonor; fut-pass. ᾅδης → แดนคนตาย (standard Thai for Hades/Sheol). 'ต่างหาก' supplies the rhetorical-contrast answer.
- Notes: **OT ALLUSION TO ISA 14:13-15 LXX** — Babylonian-king's taunt-song: 'I will ascend into heaven... I will sit on the mount of assembly... I will ascend above the heights of the clouds... But you will be brought down to Sheol, to the depths of the Pit' (Isa 14:13-15). Greek LXX: εἰς τὸν οὐρανὸν ἀναβήσομαι... εἰς ᾅδου καταβιβασθήσῃ (same verb κατ...

**Luke 10:16**
- GR: Ὁ ἀκούων ὑμῶν ἐμοῦ ἀκούει,καὶ ὁ ἀθετῶν ὑμᾶς ἐμὲ ἀθετεῖ·ὁ δὲ ἐμὲ ἀθετῶν ἀθετεῖ τὸν ἀποστείλαντά με.
- TH: ผู้ที่ฟังพวกท่านก็ฟังเรา และผู้ที่ปฏิเสธพวกท่านก็ปฏิเสธเรา ส่วนผู้ที่ปฏิเสธเรา ก็ปฏิเสธพระองค์ผู้ทรงใช้เรามา»
- Key decisions:
  - Ὁ ἀκούων ὑμῶν → ผู้ที่ฟังพวกท่าน — ἀκούω + gen 'hear, listen-to.' Per uW figs-metaphor: listening-to-disciples = listening-to-Jesus (representative-agency).
  - ὁ ἀθετῶν → ผู้ที่ปฏิเสธ — ἀθετέω 'reject, set-aside, treat-as-void.' Thai 'ปฏิเสธ' standard.
  - τὸν ἀποστείλαντά με → พระองค์ผู้ทรงใช้เรามา — Per uW figs-explicit: 'the-one-who-sent-me' = God the Father. Thai 'พระองค์ผู้ทรงใช้เรามา' preserves the indirect-reference (God is implicit). Divine subject → ทรง-prefix on ใช้. Aor-act-ptc substantival.
- Notes: Principle of shaliah-agency (Jewish legal doctrine): 'a man's agent is as himself' (m. Berakhot 5:5). Authorized messenger carries sender's authority. Four-tier chain: hearer ← disciple ← Jesus ← Father. Parallels Matt 10:40, John 13:20, 5:23. The theological weight: the 72's mission is not merely Jesus' delegated-project but a direct-particip...

**Luke 10:17**
- GR: Ὑπέστρεψαν δὲ οἱ ἑβδομήκοντα δύο μετὰ χαρᾶς λέγοντες·Κύριε,καὶ τὰ δαιμόνια ὑποτάσσεται ἡμῖν ἐν τῷ ὀνόματί σου.
- TH: สาวกเจ็ดสิบสองคนกลับมาด้วยความยินดี และทูลว่า «พระองค์เจ้าข้า แม้แต่ผีก็ยังยอมอยู่ใต้บังคับของพวกข้าพระองค์ โดยพระนามของพระองค์»
- Key decisions:
  - οἱ ἑβδομήκοντα δύο → สาวกเจ็ดสิบสองคน — Matches v.1 textual-variant decision. Per uW translate-textvariants: same number as in v.1. Thai 'สาวก' added for narrative-clarity ('the seventy-two disciples').
  - Κύριε → พระองค์เจ้าข้า — Vocative address to Jesus from disciples — humble-to-divine register (RULES §3). Thai 'พระองค์เจ้าข้า' is the most common disciple-to-Jesus vocative in Thai NT. Note: could also use 'องค์พระผู้เป็นเจ้า' but vocative...
  - τὰ δαιμόνια ὑποτάσσεται ἡμῖν → ผีก็ยังยอมอยู่ใต้บังคับของพวกข้าพระองค์ — δαιμόνιον → ผี (glossary-established Mark). ὑποτάσσομαι pres-pass 'submit.' Per uW figs-activepassive: alt 'demons obey us.' Thai 'ยอมอยู่ใต้บังคับ' natural.
  - ἐν τῷ ὀνόματί σου → โดยพระนามของพระองค์ — Per uW figs-metonymy: name = power-and-authority. ὄνομα → พระนาม (royal register for divine name). Thai 'โดยพระนาม' = 'by/through your name' instrumental sense.
- Notes: The 72's delight mirrors Luke 9:10 (the Twelve's report). Exorcism as sign-of-kingdom. 'In your name' = by your delegated-authority — the shaliah-principle in action. The 72 are surprised: even power-over-demons was not explicitly in their commission (vv.2-11 mentioned healing but not exorcism), but it flows from kingdom-proclamation. This set...

**Luke 10:18**
- GR: εἶπεν δὲ αὐτοῖς·Ἐθεώρουν τὸν Σατανᾶν ὡς ἀστραπὴν ἐκ τοῦ οὐρανοῦ πεσόντα.
- TH: พระองค์ตรัสกับพวกเขาว่า «เราได้เห็นซาตานตกลงมาจากฟ้าสวรรค์ดุจฟ้าแลบ
- TH-summary: พระดำรัสของพระเยซูอาจสะท้อนคำพยากรณ์ในอิสยาห์ 14:12 ที่กล่าวถึง «ดาวแห่งรุ่งอรุณ» ตกลงจากฟ้าสวรรค์ ซึ่งประเพณียิวโบราณตีความว่าเชื่อมโยงกับการล้มลงของซาตาน การที่สาวกเจ็ดสิบสองคนขับไล่ผีได้ ไม่ใช่เพียงเรื่องเฉพาะหน้า แต่เป็นส่วนหนึ่งของสงครามจักรวาลที่กำลังเกิดขึ้น ที่อาณาจักรของพระเจ้ากำลังเอาชนะอำนาจแห่งความมืด
- Key decisions:
  - Ἐθεώρουν → เราได้เห็น — θεωρέω imperf-act 'was-watching, perceived.' Imperfect could suggest ongoing-vision or concurrent-observation (while disciples ministered). Per uW figs-metaphor: Jesus may have had literal vision — Thai 'ได้เห็น' pr...
  - τὸν Σατανᾶν → ซาตาน — Σατανᾶς → ซาตาน (RULES §4 non-negotiable; transliteration standard).
  - ὡς ἀστραπὴν → ดุจฟ้าแลบ — Per uW figs-simile: lightning-simile for suddenness-and-visibility. ἀστραπή → ฟ้าแลบ (standard Thai). 'ดุจ' literary-style simile-marker.
  - ἐκ τοῦ οὐρανοῦ πεσόντα → ตกลงมาจากฟ้าสวรรค์ — πίπτω aor-act-ptc 'having-fallen.' οὐρανός → ฟ้าสวรรค์ (standard in Thai Christian vocabulary for 'heaven' = divine-realm).
- Notes: **OT/JEWISH TRADITION ECHO — ISA 14:12 LXX and Jewish apocalyptic.** The lightning-fall imagery evokes Isa 14:12 LXX (πῶς ἐξέπεσεν ἐκ τοῦ οὐρανοῦ ὁ Ἑωσφόρος ὁ πρωὶ ἀνατέλλων — 'How has fallen from heaven the morning-star, the early-rising one'), traditionally interpreted (from at least 2nd-century CE) as Satan's primordial-fall. Cf. Rev 12:7-9...

**Luke 10:19**
- GR: ἰδοὺ δέδωκα ὑμῖν τὴν ἐξουσίαν τοῦ πατεῖν ἐπάνω ὄφεων καὶ σκορπίων,καὶ ἐπὶ πᾶσαν τὴν δύναμιν τοῦ ἐχθροῦ,καὶ οὐδὲν ὑμᾶς οὐ μὴ ἀδικήσῃ.
- TH: ดูเถิด เราได้ให้สิทธิอำนาจแก่พวกท่านที่จะเหยียบงูและแมงป่อง และเหนือฤทธิ์อำนาจทั้งหมดของศัตรู ไม่มีสิ่งใดจะทำร้ายพวกท่านได้เลย
- TH-summary: ภาพของ «งูและแมงป่อง» เป็นการผสมผสานระหว่างสัญลักษณ์ของภัยในถิ่นทุรกันดาร (ดู กันดารวิถี 21:6 ภัยในทะเลทราย) และอำนาจของมาร (ปฐมกาล 3 งูในสวนเอเดน) พระเยซูทรงอ้างถึงเพลงสดุดีบทที่ 91 ข้อ 13 ที่ว่า «ท่านจะเหยียบสิงโตและงูเห่า ท่านจะย่ำสิงโตหนุ่มและมังกร» สัญญาการปกป้องที่พระเจ้าทรงให้แก่ผู้เชื่อของพระองค์ พระเยซูทรงขยายคำสัญญานี้ให้ครอบคลุมพันธกิจของสาวกในการต่อสู้กับอำนาจของซาตาน
- Key decisions:
  - ἰδοὺ → ดูเถิด — Per uW figs-metaphor: attention-marker 'Listen carefully now.' Thai 'ดูเถิด' standard.
  - δέδωκα ὑμῖν τὴν ἐξουσίαν → เราได้ให้สิทธิอำนาจแก่พวกท่าน — δίδωμι perf-act 'have-given' (lasting-state). ἐξουσία → สิทธิอำนาจ (glossary-established Luke 9:1 precedent).
  - πατεῖν ἐπάνω ὄφεων καὶ σκορπίων → เหยียบงูและแมงป่อง — πατέω pres-act-inf 'tread.' ὄφις → งู (glossary-established). σκορπίος → แมงป่อง (standard Thai). Per uW figs-metaphor: could be literal (Num 21:6 serpent-plague; wilderness dangers) or figurative (evil spirits). Th...
  - πᾶσαν τὴν δύναμιν τοῦ ἐχθροῦ → ฤทธิ์อำนาจทั้งหมดของศัตรู — Per uW figs-explicit: the-enemy = Satan (from v.18). δύναμις → ฤทธิ์อำนาจ. ἐχθρός → ศัตรู (glossary-established).
  - οὐδὲν ὑμᾶς οὐ μὴ ἀδικήσῃ → ไม่มีสิ่งใดจะทำร้ายพวกท่านได้เลย — Per uW figs-doublenegatives: emphatic double-negative 'nothing in no way.' Thai 'ไม่มี...ได้เลย' preserves the absolute-denial emphasis.
- Notes: **OT ECHO — PS 91:13 LXX** (Psalm 90:13 LXX numbering): ἐπ᾽ ἀσπίδα καὶ βασιλίσκον ἐπιβήσῃ, καὶ καταπατήσεις λέοντα καὶ δράκοντα — 'you will tread on asp and basilisk, trample lion and dragon.' Jesus extends the psalmist's promise-of-protection to his missionaries. The Ps 91-intertext is significant because Luke 4:9-11 earlier has Satan quote P...

**Luke 10:20**
- GR: πλὴν ἐν τούτῳ μὴ χαίρετε ὅτι τὰ πνεύματα ὑμῖν ὑποτάσσεται,χαίρετε δὲ ὅτι τὰ ὀνόματα ὑμῶν ἐγγέγραπται ἐν τοῖς οὐρανοῖς.
- TH: อย่างไรก็ตาม อย่ายินดีเพียงเพราะผีอยู่ใต้บังคับของพวกท่าน แต่จงยินดีที่ชื่อของพวกท่านได้รับการจารึกไว้ในฟ้าสวรรค์
- TH-summary: พระเยซูทรงเปลี่ยนทิศทางความยินดีของสาวก ไม่ให้เน้นฤทธานุภาพในการรับใช้ แต่ให้เน้นความรอดนิรันดร์ของตนเอง ภาพ «ชื่อที่ถูกจารึกในฟ้าสวรรค์» มีรากมาจากพระคัมภีร์เดิม (อพยพ 32:32, ดาเนียล 12:1, มาลาคี 3:16) ที่พระเจ้าทรงมีบันทึกของผู้ที่เป็นของพระองค์ ภาพนี้ปรากฏเด่นในพระธรรมวิวรณ์ในรูปของ «หนังสือแห่งชีวิต»
- Key decisions:
  - ἐν τούτῳ μὴ χαίρετε...χαίρετε δὲ → อย่ายินดีเพียงเพราะ...แต่จงยินดีที่ — Per uW figs-hyperbole: not literal 'don't rejoice at all' but 'rejoice more at the other.' Thai 'อย่า...เพียงเพราะ...แต่จงยินดีที่' softens to comparative-contrast.
  - τὰ πνεύματα ὑμῖν ὑποτάσσεται → ผีอยู่ใต้บังคับของพวกท่าน — Per uW figs-activepassive: alt 'the demons must obey you.' Here τὰ πνεύματα = τὰ δαιμόνια from v.17 (shorthand, interchangeable in Lukan-usage). Thai retains 'ผี' for consistency.
  - τὰ ὀνόματα ὑμῶν ἐγγέγραπται ἐν τοῖς οὐρανοῖς → ชื่อของพวกท่านได้รับการจารึกไว้ในฟ้าสวรรค์ — ἐγγράφω perf-pass 'have-been-written' (lasting-state). Per uW figs-activepassive + figs-explicit: God has written down names; = 'God knows you belong to him.' Thai 'ได้รับการจารึก' preserves passive-with-agent-impli...
- Notes: **OT ECHO — BOOK-OF-LIFE TRADITION.** Exod 32:32 (Moses: 'blot me out of your book'); Ps 69:28 ('blotted out of the book of the living'); Dan 12:1 ('everyone whose name is found written in the book'); Mal 3:16 ('a book of remembrance was written before him'); Rev 3:5, 13:8, 20:12-15, 21:27 (the-Lamb's book-of-life); Phil 4:3 ('names are in the...

**Luke 10:21**
- GR: Ἐν αὐτῇ τῇ ὥρᾳ ἠγαλλιάσατο τῷ πνεύματι τῷ ἁγίῳ καὶ εἶπεν·Ἐξομολογοῦμαί σοι,πάτερ κύριε τοῦ οὐρανοῦ καὶ τῆς γῆς,ὅτι ἀπέκρυψας ταῦτα ἀπὸ σοφῶν καὶ συνετῶν,καὶ ἀπεκάλυψας αὐτὰ νηπίοις·ναί,ὁ πατήρ,ὅτι οὕτως εὐδοκία ἐγένετο ἔμπροσθέν σου.
- TH: ในเวลานั้น พระเยซูทรงเปรมปรีดิ์ในพระวิญญาณบริสุทธิ์และตรัสว่า «ข้าแต่พระบิดา องค์พระผู้เป็นเจ้าแห่งฟ้าสวรรค์และแผ่นดินโลก ข้าพระองค์ขอสรรเสริญพระองค์ที่ทรงปิดซ่อนสิ่งเหล่านี้ไว้จากผู้มีปัญญาและผู้เฉียบแหลม และได้ทรงเปิดเผยแก่บรรดาเด็กเล็กๆ ใช่แล้ว พระบิดา เพราะนี่เป็นที่พอพระทัยของพระองค์
- TH-summary: พระเยซูทรงอธิษฐานขอบพระคุณพระบิดาที่ทรงเปิดเผยความจริงของอาณาจักรพระเจ้าไม่ใช่แก่ผู้ที่ถือว่าตนมีปัญญา (เช่น ธรรมาจารย์ ฟาริสี) แต่แก่ผู้ที่ต้อนรับด้วยใจอย่างเด็กเล็กๆ คำตรัสนี้สะท้อนคำสอนของพระเยซูที่ให้ต้อนรับอาณาจักรพระเจ้าเหมือนเด็กเล็ก (ลูกา 18:17) การที่พระเยซูทรงเรียกพระบิดาว่า «องค์พระผู้เป็นเจ้าแห่งฟ้าสวรรค์และแผ่นดินโลก» เป็นการยืนยันพระเจ้าผู้ครอบครองทั้งจักรวาล
- Key decisions:
  - ἐν αὐτῇ τῇ ὥρᾳ → ในเวลานั้น — Per uW figs-idiom: 'at that hour' = 'at that same time.'
  - ἠγαλλιάσατο τῷ πνεύματι τῷ ἁγίῳ → ทรงเปรมปรีดิ์ในพระวิญญาณบริสุทธิ์ — ἀγαλλιάω aor-mid 'greatly rejoice, exult.' Divine subject → ทรง. πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์ (RULES §4 non-negotiable). Lukan theme: Jesus' joy is Spirit-inspired (4:1, 4:14, 4:18).
  - Ἐξομολογοῦμαί σοι → ข้าพระองค์ขอสรรเสริญพระองค์ — ἐξομολογέω pres-mid 'confess, acknowledge, praise.' Here the sense is thanksgiving-praise (LXX Ps 9:1, 137:1). Jesus-to-Father → humble-register 'ข้าพระองค์ขอ...พระองค์.' Per uW figs-youformal: careful address choic...
  - πάτερ κύριε τοῦ οὐρανοῦ καὶ τῆς γῆς → ข้าแต่พระบิดา องค์พระผู้เป็นเจ้าแห่งฟ้าสวรรค์และแผ่นดินโลก — Per uW guidelines-sonofgodprinciples: πατήρ → พระบิดา (important title). Per uW figs-merism: heaven+earth = all that exists. Glossary-established phrase κύριος τοῦ οὐρανοῦ καὶ τῆς γῆς → องค์พระผู้เป็นเจ้าแห่งฟ้าสวรร...
  - ἀπέκρυψας...ἀπεκάλυψας → ทรงปิดซ่อน...ทรงเปิดเผย — ἀποκρύπτω/ἀποκαλύπτω contrastive-pair 'hide/reveal.' Aor-act 'you hid... you revealed.' Divine subject (Father) → ทรง-prefix. Thai pair preserves the contrastive-parallelism.
  - σοφῶν καὶ συνετῶν → ผู้มีปัญญาและผู้เฉียบแหลม — Per uW figs-nominaladj + figs-doublet + figs-irony: adjectives-as-nouns 'people who are wise and intelligent'; doublet-for-emphasis; irony — they think they are wise but actually miss revelation. σοφός → ผู้มีปัญญา;...
  - νηπίοις → บรรดาเด็กเล็กๆ — Per uW figs-metaphor: 'little children' = people willing to trust and receive. νήπιος → เด็กเล็กๆ (standard Thai); 'บรรดา' for plural-collective force.
  - οὕτως εὐδοκία ἐγένετο ἔμπροσθέν σου → นี่เป็นที่พอพระทัยของพระองค์ — εὐδοκία 'good-pleasure.' Per uW figs-metaphor: ἔμπροσθέν σου 'before you' = 'in your sight/judgment.' Thai 'เป็นที่พอพระทัย' idiomatic for 'well-pleasing to God' (royal register).
- Notes: Parallel to Matt 11:25-26 (Q-material). One of the strongest Johannine-Synoptic parallels (sometimes called the 'bolt-from-the-Johannine-blue' in the Synoptic tradition). Jesus' Father-Son prayer-intimacy here anticipates John 11:41-42, 17:1-26. Lukan Spirit-theme: Jesus' joy is Spirit-produced (cf. 4:1, 4:14). The paradox — God hides from the...

**Luke 10:22**
- GR: πάντα μοι παρεδόθη ὑπὸ τοῦ πατρός μου,καὶ οὐδεὶς γινώσκει τίς ἐστιν ὁ υἱὸς εἰ μὴ ὁ πατήρ,καὶ τίς ἐστιν ὁ πατὴρ εἰ μὴ ὁ υἱὸς καὶ ᾧ ἐὰν βούληται ὁ υἱὸς ἀποκαλύψαι.
- TH: ทุกสิ่งได้ทรงมอบไว้แก่เราโดยพระบิดาของเรา ไม่มีผู้ใดรู้ว่าพระบุตรเป็นใครนอกจากพระบิดา และไม่มีผู้ใดรู้ว่าพระบิดาเป็นใครนอกจากพระบุตร และผู้ที่พระบุตรทรงประสงค์จะเปิดเผยให้แก่เขา»
- TH-summary: คำตรัสของพระเยซูในข้อนี้มักถูกเรียกว่า «สายฟ้าจากฟ้าของยอห์น» เพราะมีเนื้อหาใกล้เคียงกับพระวรสารยอห์นมาก (เทียบ ยอห์น 3:35, 5:19-27, 10:15) ที่อธิบายความสัมพันธ์พิเศษระหว่างพระบิดากับพระบุตร การรู้จักพระบิดาไม่ใช่เรื่องที่มนุษย์จะค้นพบเองได้ด้วยสติปัญญา แต่เป็นเรื่องที่พระบุตรทรงเปิดเผยแก่ผู้ที่พระองค์ทรงเลือก
- Key decisions:
  - πάντα μοι παρεδόθη ὑπὸ τοῦ πατρός μου → ทุกสิ่งได้ทรงมอบไว้แก่เราโดยพระบิดาของเรา — παραδίδωμι aor-pass 'was-handed-over.' Per uW figs-activepassive: alt 'Father has handed everything over to me.' Thai passive with 'ทรง' on the act ('ได้ทรงมอบไว้') preserves divine-agency and passive form.
  - οὐδεὶς γινώσκει τίς ἐστιν ὁ υἱὸς εἰ μὴ ὁ πατήρ → ไม่มีผู้ใดรู้ว่าพระบุตรเป็นใครนอกจากพระบิดา — Per uW grammar-connect-exceptions: alt 'only the Father knows who the Son is.' Kept exception-clause form for strict-Greek-syntax. Per uW: γινώσκω here = know-from-personal-experience. ὁ υἱὸς/ὁ πατὴρ → พระบุตร/พระบิ...
  - ᾧ ἐὰν βούληται ὁ υἱὸς ἀποκαλύψαι → ผู้ที่พระบุตรทรงประสงค์จะเปิดเผยให้แก่เขา — βούλομαι pres-mid-subj 'wills, wishes.' ἀποκαλύπτω aor-inf 'reveal.' Divine subject → ทรง. Thai 'ทรงประสงค์จะเปิดเผยให้แก่เขา' preserves the Son's sovereign-election in revelation.
- Notes: The 'great Synoptic bolt from the Johannine blue' (B.F. Westcott's famous phrase). Mutual-exclusive Father-Son knowledge reflects unique-eternal relationship — parallels John 1:18, 3:35, 5:19-27, 10:15, 17:25. Son acts as sole-mediator of knowledge of Father. Theological implication: saving knowledge of God comes through Son's free revelation,...

**Luke 10:23**
- GR: Καὶ στραφεὶς πρὸς τοὺς μαθητὰς κατ’ἰδίαν εἶπεν·Μακάριοι οἱ ὀφθαλμοὶ οἱ βλέποντες ἃ βλέπετε.
- TH: แล้วพระองค์ทรงหันไปหาเหล่าสาวกเป็นการส่วนตัว และตรัสว่า «ดวงตาที่เห็นสิ่งที่พวกท่านเห็นอยู่ก็เป็นสุข
- Key decisions:
  - στραφεὶς πρὸς τοὺς μαθητὰς κατ’ ἰδίαν → ทรงหันไปหาเหล่าสาวกเป็นการส่วนตัว — στρέφω aor-pass-ptc 'having-turned.' Divine subject → ทรง-prefix. Per uW figs-explicit: crowd presumably present; Jesus now addresses disciples privately. κατ’ ἰδίαν → เป็นการส่วนตัว (glossary-established).
  - Μακάριοι οἱ ὀφθαλμοὶ οἱ βλέποντες ἃ βλέπετε → ดวงตาที่เห็นสิ่งที่พวกท่านเห็นอยู่ก็เป็นสุข — Per uW figs-synecdoche: ὀφθαλμοί 'eyes' = the-disciples-who-witness. Per uW figs-explicit: 'what you see' = Jesus' miracles and ministry. μακάριος → เป็นสุข (glossary-standard beatitude-form). Thai 'ดวงตา...ก็เป็นสุ...
- Notes: Beatitude form (μακάριοι). 'Eyes that see' = Lukan shorthand for witnessing Jesus' ministry + understanding its significance. Parallels Matt 13:16-17 — but Matthew adds 'and ears that hear' at both position. Luke separates the hearing beatitude into v.24. The privacy marker (κατ’ ἰδίαν) sets this apart from the public teaching to the crowd — i...

**Luke 10:24**
- GR: λέγω γὰρ ὑμῖν ὅτι πολλοὶ προφῆται καὶ βασιλεῖς ἠθέλησαν ἰδεῖν ἃ ὑμεῖς βλέπετε καὶ οὐκ εἶδαν,καὶ ἀκοῦσαι ἃ ἀκούετε καὶ οὐκ ἤκουσαν.
- TH: เพราะเราบอกพวกท่านว่า ผู้พยากรณ์และกษัตริย์เป็นอันมากได้ปรารถนาจะเห็นสิ่งที่พวกท่านเห็น แต่ไม่ได้เห็น และปรารถนาจะฟังสิ่งที่พวกท่านฟังอยู่ แต่ไม่ได้ฟัง»
- Key decisions:
  - πολλοὶ προφῆται καὶ βασιλεῖς → ผู้พยากรณ์และกษัตริย์เป็นอันมาก — προφήτης → ผู้พยากรณ์ (glossary). βασιλεύς → กษัตริย์ (standard). Matthew parallel has 'prophets and righteous-persons'; Luke's 'kings' likely thinks of David's messianic-anticipation (Ps 16; Acts 2:25-31 quotes Dav...
  - καὶ οὐκ εἶδαν...καὶ οὐκ ἤκουσαν → แต่ไม่ได้เห็น...แต่ไม่ได้ฟัง — Per uW figs-explicit: the OT prophets/kings lived before this time — they desired but did not live to see/hear the messianic fulfillment. Aor-act 'did not see/hear.'
- Notes: Parallels Matt 13:17 (with 'righteous men' instead of 'kings'). Luke's 'kings' likely evokes David (Acts 2:25-31 David's foresight of resurrection; 1 Pet 1:10-12 prophets foretelling but not seeing). The eschatological privilege: the disciples witness what the OT greats longed-for-but-did-not-live-to-see. Not merit but timing — God's revelatio...

**Luke 10:25**
- GR: Καὶ ἰδοὺ νομικός τις ἀνέστη ἐκπειράζων αὐτὸν λέγων·Διδάσκαλε,τί ποιήσας ζωὴν αἰώνιον κληρονομήσω;
- TH: ดูเถิด มีผู้เชี่ยวชาญทางบัญญัติคนหนึ่งลุกขึ้นทดสอบพระองค์ ทูลว่า «ท่านอาจารย์ ข้าพเจ้าต้องทำประการใดจึงจะได้รับชีวิตนิรันดร์เป็นมรดก?»
- Key decisions:
  - ἰδοὺ νομικός τις → ดูเถิด มีผู้เชี่ยวชาญทางบัญญัติคนหนึ่ง — Per uW writing-participants + figs-metaphor: ἰδού introduces new character. νομικός → ผู้เชี่ยวชาญทางบัญญัติ (glossary-established Luke 7:30 precedent).
  - ἀνέστη → ลุกขึ้น — Per uW translate-symaction: standing-up indicates intention to ask question (formal address-posture). Thai 'ลุกขึ้น' preserves the specific action.
  - ἐκπειράζων αὐτὸν → ทดสอบพระองค์ — ἐκπειράζω pres-act-ptc 'put-to-the-test.' Per uW alt: 'seeing how well he would answer.' Thai 'ทดสอบ' captures the testing-intent (neutral; the text doesn't specify malicious vs. legitimate-inquiry — though v.29 cla...
  - Διδάσκαλε → ท่านอาจารย์ — Per uW: respectful title. Thai 'ท่านอาจารย์' standard respectful human-to-Jesus form (not divine-register yet — this is a legal-scholar testing Jesus).
  - τί ποιήσας ζωὴν αἰώνιον κληρονομήσω → ข้าพเจ้าต้องทำประการใดจึงจะได้รับชีวิตนิรันดร์เป็นมรดก? — Per uW figs-metaphor: κληρονομέω 'inherit' figuratively = 'come-to-possess.' Per uW figs-verbs: aor-act-ptc 'having-done' may suggest single-deed (but more likely aspectual — completed action of doing). ζωὴν αἰώνιον...
- Notes: Same question asked by the rich ruler (Luke 18:18) — recurring Lukan-setup for teaching on eternal-life / kingdom-entrance. νομικός (law-expert) = skilled interpreter of Mosaic Torah; often synonymous with γραμματεύς (scribe) in Luke. The 'test' posture is classical for rabbi-disputation — legitimate-but-probing, not necessarily hostile. Jesus...

**Luke 10:26**
- GR: ὁ δὲ εἶπεν πρὸς αὐτόν·Ἐν τῷ νόμῳ τί γέγραπται;πῶς ἀναγινώσκεις;
- TH: พระองค์ตรัสกับเขาว่า «ในพระบัญญัติเขียนไว้อย่างไร? ท่านอ่านเข้าใจอย่างไร?»
- Key decisions:
  - Ἐν τῷ νόμῳ τί γέγραπται → ในพระบัญญัติเขียนไว้อย่างไร — ὁ νόμος → พระบัญญัติ (the-Law, Torah). γέγραπται perf-pass 'has-been-written.' Per uW figs-rquestion + figs-parallelism: Jesus uses two questions as a rhetorical unit 'what is written + how do you read.' Thai preser...
  - πῶς ἀναγινώσκεις → ท่านอ่านเข้าใจอย่างไร — Per uW figs-idiom: 'how do you read?' = 'how do you understand it?' ἀναγινώσκω 'read (aloud),' but idiom = 'interpret.' Thai 'อ่านเข้าใจ' preserves the read-and-understand sense.
- Notes: Classic rabbinic Socratic-counter-question: Jesus answers the test with a teacher-like turn. The 'what is written + how do you read' pair is rabbinic standard-formulation (m. Avot 5:22, 'Turn it and turn it, for everything is in it'). Jesus doesn't answer but redirects to Torah — establishing common ground before pressing home the meaning.

**Luke 10:27**
- GR: ὁ δὲ ἀποκριθεὶς εἶπεν·Ἀγαπήσεις κύριον τὸν θεόν σου ἐξ ὅλης τῆς καρδίας σου καὶ ἐν ὅλῃ τῇ ψυχῇ σου καὶ ἐν ὅλῃ τῇ ἰσχύϊ σου καὶ ἐν ὅλῃ τῇ διανοίᾳ σου,καὶ τὸν πλησίον σου ὡς σεαυτόν.
- TH: เขาตอบว่า «‹จงรักองค์พระผู้เป็นเจ้าของเจ้าด้วยสุดใจของเจ้า สุดจิตวิญญาณของเจ้า สุดกำลังของเจ้า และสุดความคิดของเจ้า› และ ‹จงรักเพื่อนบ้านของเจ้าเหมือนรักตนเอง›»
- TH-summary: คำตอบของผู้เชี่ยวชาญทางบัญญัติรวมข้อพระคัมภีร์สองข้อเข้าด้วยกัน — เฉลยธรรมบัญญัติ 6:5 (พระบัญญัติชีมาที่ชาวยิวท่องทุกวัน) กับเลวีนิติ 19:18 (จงรักเพื่อนบ้านเหมือนรักตนเอง) พระเยซูเองทรงสอนในที่อื่นว่าสองข้อนี้คือบทสรุปของธรรมบัญญัติทั้งหมด (มาระโก 12:29-31, มัทธิว 22:37-40) รูปข้อเฉลยธรรมบัญญัติ 6:5 ในฉบับภาษากรีกของลูกามีสี่ส่วน (ใจ จิตวิญญาณ กำลัง ความคิด) ขณะที่ต้นฉบับภาษาฮีบรูมีสามส่วน (ใจ จิตวิญญาณ กำลัง)
- Key decisions:
  - ἀποκριθεὶς εἶπεν → ตอบว่า — Per uW figs-hendiadys: 'answering and said' = 'responded.'
  - Ἀγαπήσεις κύριον τὸν θεόν σου → จงรักองค์พระผู้เป็นเจ้าของเจ้า — **OT CITATION — DEUT 6:5 (Shema).** Per uW figs-youcrowd: singular 'you' retained (each individual obeys). Per uW figs-declarative: future-indicative used for command 'you-will-love' = 'you-must-love.' κύριον here =...
  - ἐξ ὅλης τῆς καρδίας...ψυχῇ...ἰσχύϊ...διανοίᾳ → ด้วยสุดใจ...จิตวิญญาณ...กำลัง...ความคิด — Per uW figs-merism: four-part comprehensive-self devotion. Luke's four-element form (heart+soul+strength+mind) matches certain LXX Deut 6:5 witnesses (some LXX MSS have καρδία and διάνοια interchangeable or added). ...
  - τὸν πλησίον σου ὡς σεαυτόν → จงรักเพื่อนบ้านของเจ้าเหมือนรักตนเอง — **OT CITATION — LEV 19:18.** Per uW figs-ellipsis: 'love' verb carried forward from first citation. πλησίον → เพื่อนบ้าน (glossary-established). Thai brackets inner-quotation using ‹ › for the two scripture-citations.
- Notes: **OT CITATION — COMPOSITE: DEUT 6:5 + LEV 19:18.** The dual-summary of Torah. Jesus himself teaches the same composite in Mark 12:29-31 and Matt 22:37-40 (with different word-combinations for the Deut 6:5 elements). Luke's four-element form (καρδία+ψυχή+ἰσχύς+διάνοια) matches certain LXX Deut 6:5 witnesses — MT Hebrew has three (לבב/לב, נפש, מ...

**Luke 10:28**
- GR: εἶπεν δὲ αὐτῷ·Ὀρθῶς ἀπεκρίθης·τοῦτο ποίει καὶ ζήσῃ.
- TH: พระองค์จึงตรัสกับเขาว่า «ท่านตอบถูกต้องแล้ว จงทำเช่นนี้เถิด แล้วท่านจะมีชีวิต»
- Key decisions:
  - Ὀρθῶς ἀπεκρίθης → ท่านตอบถูกต้องแล้ว — ὀρθῶς adverb 'correctly, rightly.' Thai 'ถูกต้องแล้ว' natural approval-statement.
  - τοῦτο ποίει καὶ ζήσῃ → จงทำเช่นนี้เถิด แล้วท่านจะมีชีวิต — Per uW grammar-connect-condition-hypothetical: conditional-form. ποίει pres-act-imper continuous 'keep-doing.' ζήσῃ fut-mid 'will-live' = eternal-life implied. Thai 'จงทำ...แล้วท่านจะมีชีวิต' preserves conditional-f...
- Notes: **OT ECHO — LEV 18:5** (καὶ ποιήσας αὐτὰ ἄνθρωπος ζήσεται ἐν αὐτοῖς — 'the one who does these things will live by them'), which Paul cites in Rom 10:5 and Gal 3:12 as the principle of law-righteousness. Jesus agrees with the lawyer's content; the question is whether one can actually DO it (setting up the Samaritan parable as existential-test o...

**Luke 10:29**
- GR: Ὁ δὲ θέλων δικαιῶσαι ἑαυτὸν εἶπεν πρὸς τὸν Ἰησοῦν·Καὶ τίς ἐστίν μου πλησίον;
- TH: แต่เขาต้องการแสดงว่าตนเองเป็นผู้ชอบธรรม จึงทูลถามพระเยซูว่า «แล้วใครเป็นเพื่อนบ้านของข้าพเจ้า?»
- Key decisions:
  - θέλων δικαιῶσαι ἑαυτὸν → ต้องการแสดงว่าตนเองเป็นผู้ชอบธรรม — δικαιόω 'justify, vindicate, prove-righteous.' Per uW alt: 'prove that he had done what he needed to do.' Thai 'แสดงว่าตนเองเป็นผู้ชอบธรรม' captures the self-vindication attempt.
  - Καὶ τίς ἐστίν μου πλησίον → แล้วใครเป็นเพื่อนบ้านของข้าพเจ้า? — Per uW figs-explicit: implied 'whom should I consider neighbor, i.e., someone I must love.' Thai 'แล้ว...ของข้าพเจ้า' natural follow-up question.
- Notes: The follow-up question reveals the lawyer's strategy: he seeks a narrow-definition to limit his obligations. Jewish legal-discussion of the time debated the scope of 'neighbor': Sir 12:1-7 distinguishes the pious from the ungodly; Qumran's Community Rule (1QS 1:9-10) commands loving sons-of-light and hating sons-of-darkness; rabbinic tradition...

**Luke 10:30**
- GR: ὑπολαβὼν δὲ ὁ Ἰησοῦς εἶπεν·Ἄνθρωπός τις κατέβαινεν ἀπὸ Ἰερουσαλὴμ εἰς Ἰεριχὼ καὶ λῃσταῖς περιέπεσεν,οἳ καὶ ἐκδύσαντες αὐτὸν καὶ πληγὰς ἐπιθέντες ἀπῆλθον ἀφέντες ἡμιθανῆ.
- TH: พระเยซูทรงรับคำถามและตรัสว่า «ชายคนหนึ่งกำลังเดินทางลงจากเยรูซาเล็มไปยังเมืองเยรีโค เขาตกไปอยู่ในมือของพวกโจร พวกโจรถอดเสื้อผ้าของเขาออก ทุบตีเขา แล้วจากไป ทิ้งให้เขาอยู่ในสภาพเกือบตาย
- TH-summary: ทางจากเยรูซาเล็มลงไปเมืองเยรีโค ยาวประมาณ 27 กิโลเมตร ลดระดับ 1,100 เมตรผ่านหุบเขาถิ่นทุรกันดาร เป็นเส้นทางที่โจรชอบดักปล้น ชาวยิวในสมัยพระเยซูรู้จักเส้นทางนี้ดีว่าอันตรายมาก นักประวัติศาสตร์ยิวโจเซฟัสยืนยันเรื่องโจรในภูมิภาคนี้ การที่พระเยซูทรงเลือกฉากนี้ทำให้ผู้ฟังเห็นภาพชัดเจนและรับรู้อันตรายในทันที
- Key decisions:
  - ὑπολαβὼν → ทรงรับคำถาม — Per uW figs-hendiadys + figs-parables: ὑπολαμβάνω 'take-up (the question), reply.' Divine subject → ทรง. Introduces parable-as-response.
  - Ἄνθρωπός τις → ชายคนหนึ่ง — Per uW writing-participants: indefinite-introduction of character. Thai 'ชายคนหนึ่ง' natural narrative-opener.
  - κατέβαινεν ἀπὸ Ἰερουσαλὴμ εἰς Ἰεριχώ → กำลังเดินทางลงจากเยรูซาเล็มไปยังเมืองเยรีโค — Per uW figs-idiom: 'going down' = literal-down-in-elevation (Jerusalem ~780m → Jericho ~-260m = ~1040m drop over ~27km). Ἰερουσαλήμ → เยรูซาเล็ม (standard). Ἰεριχώ → เมืองเยรีโค (glossary-established).
  - λῃσταῖς περιέπεσεν → ตกไปอยู่ในมือของพวกโจร — Per uW figs-idiom: περιπίπτω 'fall-into (midst-of)' — not literal-fall but encounter-as-victim. λῃστής → โจร (glossary). Thai 'ตกไปอยู่ในมือ' idiomatic for become-victim.
  - ἐκδύσαντες αὐτὸν → ถอดเสื้อผ้าของเขาออก — Per uW figs-idiom: ἐκδύω here = 'strip (of belongings + clothes).' Thai specifies clothes for the visual image; belongings implicit.
  - πληγὰς ἐπιθέντες → ทุบตีเขา — Per uW figs-idiom: 'laying on blows' = 'beat.' Thai 'ทุบตี' captures the repeated-violence.
  - ἀφέντες ἡμιθανῆ → ทิ้งให้เขาอยู่ในสภาพเกือบตาย — HAPAX ἡμιθανής 'half-dead' — per uW figs-idiom 'almost dead.' Thai 'เกือบตาย' natural. NEW GLOSSARY: ἡμιθανής → เกือบตาย.
- Notes: HAPAX ἡμιθανής — only NT use. Compound ἡμι- (half) + θνῄσκω (die). Road from Jerusalem to Jericho ~17 miles, ~3600-foot descent through desolate Judean-wilderness terrain. Traditional name 'Ma'aleh Adummim' (Ascent of Blood, Josh 15:7, 18:17) reflected the road's dangerous reputation. Josephus (War 4.451-75) confirms Roman-era banditry in the ...

**Luke 10:31**
- GR: κατὰ συγκυρίαν δὲ ἱερεύς τις κατέβαινεν ἐν τῇ ὁδῷ ἐκείνῃ,καὶ ἰδὼν αὐτὸν ἀντιπαρῆλθεν·
- TH: บังเอิญว่ามีปุโรหิตคนหนึ่งเดินทางลงมาในทางเดียวกันนั้น แต่เมื่อเขาเห็นชายผู้นั้น เขาก็เดินผ่านไปอีกฟากหนึ่ง
- Key decisions:
  - κατὰ συγκυρίαν → บังเอิญว่า — HAPAX συγκυρία 'chance, coincidence.' Classical Greek (Polybius, Plutarch). Thai 'บังเอิญ' standard. Per uW alt: 'it just so happened that.' NEW GLOSSARY: συγκυρία → บังเอิญ.
  - ἱερεύς τις → ปุโรหิตคนหนึ่ง — Per uW writing-participants + figs-explicit: new character; implicit cultural-knowledge that priest = religious-leader. ἱερεύς → ปุโรหิต (glossary-established).
  - ἰδὼν αὐτὸν ἀντιπαρῆλθεν → เมื่อเขาเห็นชายผู้นั้น เขาก็เดินผ่านไปอีกฟากหนึ่ง — Per uW grammar-connect-logic-contrast + figs-explicit: introduced with contrastive 'but' since religious-leader would be expected to help. ἀντιπαρέρχομαι 'pass-by-on-opposite-side.' Thai 'เดินผ่านไปอีกฟากหนึ่ง' lite...
- Notes: HAPAX συγκυρία — only NT use. The priest's avoidance may reflect ritual-purity concern (Num 19:11-13: touching a corpse makes a priest unclean for 7 days; priests must not defile themselves for the dead except for immediate family — Lev 21:1-4). But the text says only 'half-dead' — not dead. Jewish tradition (Pirke Avot 1:12; b. Yoma 85a-b) em...

**Luke 10:32**
- GR: ὁμοίως δὲ καὶ Λευίτης κατὰ τὸν τόπον ἐλθὼν καὶ ἰδὼν ἀντιπαρῆλθεν.
- TH: เช่นเดียวกัน คนเลวีคนหนึ่งมาถึงที่นั้น เมื่อเห็นชายผู้นั้น ก็เดินผ่านไปอีกฟากหนึ่งด้วย
- Key decisions:
  - ὁμοίως δὲ καὶ → เช่นเดียวกัน — Per uW grammar-connect-logic-contrast: again expected-to-help but did-not.
  - Λευίτης → คนเลวี — Per uW figs-explicit: Levite = Temple-servant. Λευίτης → คนเลวี (standard Thai).
  - κατὰ τὸν τόπον ἐλθὼν → มาถึงที่นั้น — κατὰ τὸν τόπον 'at the place.' Some MSS insert 'the place' vs 'to the place' — Thai 'มาถึงที่นั้น' natural.
- Notes: Levites served in the Temple (Num 3:6-9) and had purity-concerns similar to priests (though slightly less strict per Ezek 44:25-27). The priest+Levite pair = representative-of-Temple-establishment. Both walked past. The parable builds via triadic-pattern: listeners anticipate the third figure would be a lay-Israelite (completing the priestly-L...

**Luke 10:33**
- GR: Σαμαρίτης δέ τις ὁδεύων ἦλθεν κατ’αὐτὸν καὶ ἰδὼν ἐσπλαγχνίσθη,
- TH: แต่ชาวสะมาเรียคนหนึ่งซึ่งกำลังเดินทางมาถึงที่ชายนั้นอยู่ เมื่อเห็นเขา ก็มีใจเมตตาสงสาร
- TH-summary: ชาวยิวกับชาวสะมาเรียเป็นศัตรูกันมายาวนาน (ดู ยอห์น 4:9) ตั้งแต่หลังการถูกกวาดต้อนไปบาบิโลน ชาวสะมาเรียสืบเชื้อสายจากชาวอิสราเอลเหนือผสมกับผู้ถูกย้ายมาโดยอัสซีเรีย มีพระคัมภีร์ของตนเอง (เพนทาทุกของสะมาเรีย) และนมัสการที่ภูเขาเกริซิม ไม่ใช่กรุงเยรูซาเล็ม การที่พระเยซูทรงใช้ชาวสะมาเรียเป็นตัวเอกของอุปมาเป็นการท้าทายผู้ฟังชาวยิวอย่างแรง — คนที่พวกเขาดูถูกกลับเป็นผู้ปฏิบัติตามพระบัญญัติของพระเจ้า
- Key decisions:
  - Σαμαρίτης δέ τις → แต่ชาวสะมาเรียคนหนึ่ง — Per uW writing-participants + figs-explicit + grammar-connect-logic-contrast: strong contrastive 'but.' Σαμαρίτης → ชาวสะมาเรีย (glossary-established). Audience would expect a lay-Israelite as third figure; Samarita...
  - ὁδεύων → ซึ่งกำลังเดินทาง — HAPAX ὁδεύω 'travel on road' — only NT use. Classical vocabulary for ordinary journeying. Thai 'กำลังเดินทาง' natural. NEW GLOSSARY: ὁδεύω → เดินทาง.
  - ἦλθεν κατ’ αὐτὸν → มาถึงที่ชายนั้นอยู่ — κατά + acc 'at, to, upon.' Thai 'มาถึงที่...อยู่' natural.
  - ἐσπλαγχνίσθη → ก็มีใจเมตตาสงสาร — σπλαγχνίζομαι aor-pass 'was-moved-with-compassion (in the entrails).' Glossary-established 'มีความเมตตาสงสาร' (Luke 7:13 precedent); Thai 'มีใจเมตตาสงสาร' variant preserving the gut-level compassion.
- Notes: HAPAX ὁδεύω — only NT use. Samaritans-and-Jews were bitter enemies (John 4:9 'Jews have no dealings with Samaritans'; Josephus Ant. 20.118-136 records a Samaritan-Jew incident in Galilee; Luke 9:52-55 Samaritan-village rejection of Jesus). Samaritans: descendants of northern-kingdom Israelites mixed with Assyrian-imperial settlers (2 Kings 17:...

**Luke 10:34**
- GR: καὶ προσελθὼν κατέδησεν τὰ τραύματα αὐτοῦ ἐπιχέων ἔλαιον καὶ οἶνον,ἐπιβιβάσας δὲ αὐτὸν ἐπὶ τὸ ἴδιον κτῆνος ἤγαγεν αὐτὸν εἰς πανδοχεῖον καὶ ἐπεμελήθη αὐτοῦ.
- TH: เขาเข้ามาใกล้ เทน้ำมันและเหล้าองุ่นลงบนบาดแผลของชายคนนั้นและพันแผลให้ ยกเขาขึ้นใส่หลังสัตว์พาหนะของตน พาไปที่โรงแรมและดูแลรักษาเขา
- TH-summary: น้ำมันและเหล้าองุ่นเป็นยาแผนโบราณที่ใช้กับบาดแผล — น้ำมันทำให้บาดแผลชุ่มชื้นและเบาเจ็บ เหล้าองุ่นมีฤทธิ์ฆ่าเชื้อโรค (อิสยาห์ 1:6 ใช้ภาพเดียวกันในเชิงเปรียบเทียบ) การที่ชาวสะมาเรียดูแลละเอียดเช่นนี้ แล้วยังยอมสละความสะดวกสบายของตนด้วยการให้ชายเจ็บขี่สัตว์ของตนในขณะที่ตนเองเดินไป แสดงถึงความรักที่ลงมือจริง ไม่ใช่แค่คำพูด
- Key decisions:
  - κατέδησεν τὰ τραύματα αὐτοῦ → พันแผลให้ — HAPAX καταδέω 'bind up.' HAPAX τραῦμα 'wound.' Both only-NT-uses. Thai 'พันแผล' for καταδέω, 'บาดแผล' for τραῦμα. Per uW figs-events: oil+wine poured FIRST, then binding — Greek aor-ptc sequence. Thai reflects actua...
  - ἐπιχέων ἔλαιον καὶ οἶνον → เทน้ำมันและเหล้าองุ่นลงบน... — HAPAX ἐπιχέω 'pour on.' ἔλαιον → น้ำมัน (glossary). οἶνος → เหล้าองุ่น (standard Thai). Per uW figs-explicit: wine-for-cleansing, oil-for-healing/soothing. NEW GLOSSARY: ἐπιχέω → เท...ลงบน.
  - ἐπιβιβάσας δὲ αὐτὸν ἐπὶ τὸ ἴδιον κτῆνος → ยกเขาขึ้นใส่หลังสัตว์พาหนะของตน — ἐπιβιβάζω aor-act-ptc 'mount, put-on (an animal).' Per uW translate-unknown: κτῆνος = pack-animal, probably-donkey. Thai 'สัตว์พาหนะ' general-term preserves the ride-animal sense without over-specifying.
  - ἤγαγεν αὐτὸν εἰς πανδοχεῖον → พาไปที่โรงแรม — HAPAX πανδοχεῖον 'inn, lodging-place.' Thai 'โรงแรม' adequate (classical-Thai would be 'โรงเตี๊ยม' for ancient-inn; modern 'โรงแรม' works for readability). NEW GLOSSARY: πανδοχεῖον → โรงแรม.
  - ἐπεμελήθη αὐτοῦ → ดูแลรักษาเขา — ἐπιμελέομαι aor-pass 'take-care-of.' Thai 'ดูแลรักษา' combines care-and-nurse sense.
- Notes: **FOUR HAPAX LEGOMENA in one verse** (καταδέω, τραῦμα, ἐπιχέω, πανδοχεῖον) — striking concentration of Luke's rich-literary vocabulary, likely reflecting his educated background (traditionally identified as a physician, Col 4:14). Oil-and-wine = standard ancient-wound-treatment: oil soothes and moisturizes; wine's alcohol disinfects (cf. Isa 1...

**Luke 10:35**
- GR: καὶ ἐπὶ τὴν αὔριον ἐκβαλὼν δύο δηνάρια ἔδωκεν τῷ πανδοχεῖ καὶ εἶπεν·Ἐπιμελήθητι αὐτοῦ,καὶ ὅ τι ἂν προσδαπανήσῃς ἐγὼ ἐν τῷ ἐπανέρχεσθαί με ἀποδώσω σοι.
- TH: วันรุ่งขึ้น เขาเอาเงินเดนาริอัสสองเหรียญออกมา มอบให้เจ้าของโรงแรม และสั่งว่า «จงดูแลเขาเถิด ท่านจะใช้จ่ายเพิ่มเท่าไรก็ตาม เมื่อข้าพเจ้ากลับมา ข้าพเจ้าจะชดใช้คืนให้»
- Key decisions:
  - δύο δηνάρια → เงินเดนาริอัสสองเหรียญ — Per uW translate-bmoney: δηνάριον = Roman silver coin ≈ day's wage for a laborer (Matt 20:2). Thai 'เงินเดนาริอัสสองเหรียญ' transliteration+classifier preserves the specific-currency reference.
  - τῷ πανδοχεῖ → เจ้าของโรงแรม — HAPAX πανδοχεύς 'innkeeper.' Per uW alt: 'the person in charge of the inn.' NEW GLOSSARY: πανδοχεύς → เจ้าของโรงแรม.
  - Ἐπιμελήθητι αὐτοῦ → จงดูแลเขาเถิด — ἐπιμελέομαι aor-pass-imper matching v.34.
  - ὅ τι ἂν προσδαπανήσῃς...ἀποδώσω σοι → ท่านจะใช้จ่ายเพิ่มเท่าไรก็ตาม...ข้าพเจ้าจะชดใช้คืนให้ — HAPAX προσδαπανάω 'spend-in-addition.' Per uW figs-hypo: hypothetical-conditional 'whatever-if.' ἀποδίδωμι fut 'will-repay.' Thai 'จะใช้จ่ายเพิ่มเท่าไรก็ตาม...จะชดใช้คืน' natural. NEW GLOSSARY: προσδαπανάω → ใช้จ่าย...
- Notes: HAPAX πανδοχεύς, προσδαπανάω — only NT uses. Two denarii ≈ two days' wages for a laborer. Sufficient to cover several-days lodging at ancient-inn-rates (estimated based on Roman-era inn-prices). The open-ended 'whatever-more-you-spend-I-will-repay' demonstrates extravagant-commitment, not minimum-obligation fulfillment. The Samaritan leaves wi...

**Luke 10:36**
- GR: τίς τούτων τῶν τριῶν πλησίον δοκεῖ σοι γεγονέναι τοῦ ἐμπεσόντος εἰς τοὺς λῃστάς;
- TH: ในสามคนนี้ ท่านคิดว่าผู้ใดเป็นเพื่อนบ้านของคนที่ถูกพวกโจรปล้น?»
- Key decisions:
  - τίς τούτων τῶν τριῶν πλησίον δοκεῖ σοι γεγονέναι → ในสามคนนี้ ท่านคิดว่าผู้ใดเป็นเพื่อนบ้าน — Per uW: Jesus reframes the lawyer's question. Lawyer asked 'who IS my neighbor?' (limiting); Jesus asks 'who BECAME a neighbor?' (expanding via action). πλησίον...γεγονέναι 'to have-become neighbor.' Thai 'เป็นเพื่อ...
  - τοῦ ἐμπεσόντος εἰς τοὺς λῃστάς → ของคนที่ถูกพวกโจรปล้น — Per uW figs-idiom: 'fell among robbers' = 'was attacked by robbers' (not literal-fall). Thai 'ถูก...ปล้น' captures the victimization.
- Notes: Jesus' decisive reframing: the lawyer asked 'who qualifies as my neighbor' (seeking boundaries); Jesus asks 'who proved to be neighbor through action.' Neighbor-love is thus redefined from a category-membership question to an action-character question. The grammar is telling: γίνομαι (become) + πλησίον — neighbor-status is something one BECOME...

**Luke 10:37**
- GR: ὁ δὲ εἶπεν·Ὁ ποιήσας τὸ ἔλεος μετ’αὐτοῦ.εἶπεν δὲ αὐτῷ ὁ Ἰησοῦς·Πορεύου καὶ σὺ ποίει ὁμοίως.
- TH: เขาตอบว่า «คนที่แสดงความเมตตาต่อเขา» พระเยซูจึงตรัสกับเขาว่า «จงไปเถิด และท่านจงทำเช่นเดียวกัน»
- Key decisions:
  - Ὁ ποιήσας τὸ ἔλεος μετ’ αὐτοῦ → คนที่แสดงความเมตตาต่อเขา — ἔλεος → ความเมตตา (human-level mercy, not divine พระเมตตา). Note: the lawyer avoids naming 'the Samaritan' — the hostility runs that deep. Thai preserves this by matching the circumlocution.
  - Πορεύου καὶ σὺ ποίει ὁμοίως → จงไปเถิด และท่านจงทำเช่นเดียวกัน — Per uW figs-explicit: alt 'you are right; be a neighbor to those who need your help.' Thai 'จงไป...จงทำเช่นเดียวกัน' preserves the dual-imperative. Echoes v.28 τοῦτο ποίει — neighbor-love as ongoing-practice.
- Notes: The lawyer CANNOT bring himself to name 'the Samaritan' directly — the cultural-religious animosity is so deeply rooted. He must describe the Samaritan functionally: 'the one who showed mercy.' Jesus' closing command (πορεύου καὶ σὺ ποίει ὁμοίως) deliberately echoes v.28 (τοῦτο ποίει καὶ ζήσῃ) — neighbor-love is the way of LIFE, not just a ver...

**Luke 10:38**
- GR: Ἐν δὲ τῷ πορεύεσθαι αὐτοὺς αὐτὸς εἰσῆλθεν εἰς κώμην τινά·γυνὴ δέ τις ὀνόματι Μάρθα ὑπεδέξατο αὐτὸν.
- TH: ขณะที่พระเยซูและเหล่าสาวกเดินทางไป พระองค์เสด็จเข้าไปในหมู่บ้านแห่งหนึ่ง หญิงคนหนึ่งชื่อมารธาได้ต้อนรับพระองค์ไว้ในบ้านของนาง
- Key decisions:
  - Ἐν δὲ τῷ πορεύεσθαι αὐτοὺς → ขณะที่พระเยซูและเหล่าสาวกเดินทางไป — Per uW writing-newevent: temporal-articular-infinitive marks new event. Per uW figs-synecdoche: αὐτόν 'he entered' = group of Jesus-and-disciples. Thai makes the group-reference explicit.
  - εἰσῆλθεν εἰς κώμην τινά → พระองค์เสด็จเข้าไปในหมู่บ้านแห่งหนึ่ง — Divine-movement → เสด็จ. Unnamed village here; John 11:1, 12:1-3 identifies as Bethany.
  - γυνὴ δέ τις ὀνόματι Μάρθα → หญิงคนหนึ่งชื่อมารธา — Per uW writing-participants: new character introduction. Μάρθα → มารธา (standard Thai). Aramaic name meaning 'mistress/lady.'
  - ὑπεδέξατο αὐτὸν → ได้ต้อนรับพระองค์ไว้ในบ้านของนาง — ὑποδέχομαι aor-mid 'receive-as-guest (in one's house).' Thai adds 'ไว้ในบ้านของนาง' to make the hospitality-location explicit, matching the fuller-implication of the Greek verb.
- Notes: Luke's 'travel-narrative' (9:51-19:27) arc continues; unnamed village here, identified as Bethany in John 11:1, 12:1-3. Martha (Aramaic מָרְתָא 'mistress, lady') is named as household-head — suggests she is the owner or at least the responsible-hostess. Luke's portrayal here and John's portrayal (Lazarus's sisters, John 11) are consistent: Mar...

**Luke 10:39**
- GR: καὶ τῇδε ἦν ἀδελφὴ καλουμένη Μαριάμ,ἣ καὶ παρακαθεσθεῖσα πρὸς τοὺς πόδας τοῦ Ἰησοῦ ἤκουεν τὸν λόγον αὐτοῦ.
- TH: นางมีน้องสาวคนหนึ่งชื่อมารีย์ ซึ่งนั่งอยู่แทบพระบาทของพระเยซู คอยฟังพระดำรัสของพระองค์
- TH-summary: การที่มารีย์ «นั่งแทบพระบาทของพระเยซู» ไม่ใช่การนั่งรับใช้ แต่เป็นท่าทีของ «สาวก» — ผู้เรียนรู้จากอาจารย์ (เปรียบเทียบ กิจการ 22:3 ที่เปาโลกล่าวว่าได้เรียนรู้ «ใต้เท้าของกามาลิเอล») ในวัฒนธรรมยิวสมัยนั้น ผู้หญิงไม่นิยมเป็นลูกศิษย์ของรับบี การที่พระเยซูทรงยอมรับมารีย์ในฐานะสาวกจึงเป็นการยกสถานะผู้หญิงเป็นการปฏิวัติวัฒนธรรม
- Key decisions:
  - ἀδελφὴ καλουμένη Μαριάμ → น้องสาวคนหนึ่งชื่อมารีย์ — Per uW writing-participants + figs-activepassive: introduces Mary. Μαριάμ → มารีย์ (glossary-established).
  - παρακαθεσθεῖσα πρὸς τοὺς πόδας τοῦ Ἰησοῦ → นั่งอยู่แทบพระบาทของพระเยซู — HAPAX παρακαθέζομαι 'sit beside' — only NT use. Per uW figs-explicit: customary disciple-posture. πούς (divine) → พระบาท (royal register). Thai 'นั่งอยู่แทบพระบาท' matches idiom for disciple-at-feet. NEW GLOSSARY: π...
  - τοῦ Ἰησοῦ → ของพระเยซู — TEXTUAL VARIANT — SBLGNT, P75, B read τοῦ Ἰησοῦ 'of Jesus'; א, A, C^c, D read τοῦ κυρίου 'of the Lord.' Following SBLGNT.
  - ἤκουεν τὸν λόγον αὐτοῦ → คอยฟังพระดำรัสของพระองค์ — ἀκούω imperf 'kept-hearing.' Per uW figs-metonymy: λόγος = 'what he said.' Divine speech → พระดำรัส. Thai 'คอยฟัง' preserves the sustained-listening.
- Notes: HAPAX παρακαθέζομαι — only NT use. **TEXTUAL VARIANT:** τοῦ Ἰησοῦ (SBLGNT, P75, B, Vulgate, Syriac) vs. τοῦ κυρίου (א, A, C^c, D, most later MSS). SBLGNT prefers the harder-reading 'Jesus' (since 'Lord' is the more-common Lukan-narrator reference in this context). Modern critical-texts uniformly follow SBLGNT here. Sitting at a rabbi's feet wa...

**Luke 10:40**
- GR: ἡ δὲ Μάρθα περιεσπᾶτο περὶ πολλὴν διακονίαν·ἐπιστᾶσα δὲ εἶπεν·Κύριε,οὐ μέλει σοι ὅτι ἡ ἀδελφή μου μόνην με κατέλειπεν διακονεῖν;εἰπὲ οὖν αὐτῇ ἵνα μοι συναντιλάβηται.
- TH: ฝ่ายมารธากลับวอกแวกอยู่กับงานปรนนิบัติมากมาย นางเข้ามาทูลว่า «พระองค์เจ้าข้า พระองค์ไม่ทรงสนพระทัยหรือที่น้องสาวของข้าพเจ้าปล่อยให้ข้าพเจ้าปรนนิบัติแต่ลำพัง? ขอตรัสสั่งให้นางมาช่วยข้าพเจ้าเถิด»
- Key decisions:
  - περιεσπᾶτο περὶ πολλὴν διακονίαν → วอกแวกอยู่กับงานปรนนิบัติมากมาย — HAPAX περισπάω 'drag-away, distract' — only NT use. Imperf-pass 'was-being-distracted.' Per uW figs-activepassive: alt 'all Martha could think about was the big meal.' διακονία → งานปรนนิบัติ (glossary-aligned for s...
  - ἐπιστᾶσα δὲ εἶπεν → นางเข้ามาทูลว่า — ἐφίστημι aor-act-ptc 'come-up-to, stand-over.' Disciple-to-divine → ทูล (humble-speech).
  - Κύριε → พระองค์เจ้าข้า — Vocative κύριε from Martha to Jesus. Humble-to-divine address → พระองค์เจ้าข้า.
  - οὐ μέλει σοι → พระองค์ไม่ทรงสนพระทัยหรือ — Per uW figs-rquestion: rhetorical question 'does it not concern you?' Thai 'ไม่ทรงสนพระทัยหรือ' preserves politeness while expressing the complaint. Divine → ทรง.
  - ἵνα μοι συναντιλάβηται → ให้นางมาช่วยข้าพเจ้าเถิด — συναντιλαμβάνομαι aor-mid-subj 'help alongside.' Thai 'มาช่วย' captures the bear-burden-together sense.
- Notes: HAPAX περισπάω — only NT use (though related περίσπασμος etc.). The imperfect indicates ongoing-distraction. Per uW figs-rquestion: Martha's complaint is framed rhetorically for politeness — she respects Jesus enough not to directly command, but uses rhetorical-question to voice grievance. Note cultural-gender-dynamic: Martha doesn't directly ...

**Luke 10:41**
- GR: ἀποκριθεὶς δὲ εἶπεν αὐτῇ ὁ κύριος·Μάρθα Μάρθα,μεριμνᾷς καὶ θορυβάζῃ περὶ πολλά,
- TH: พระเยซูตรัสตอบนางว่า «มารธา มารธาเอ๋ย เจ้ากังวลและกลัดกลุ้มใจเรื่องมากมาย
- Key decisions:
  - ὁ κύριος → พระเยซู — Per uW: Luke refers to Jesus as 'the Lord' in narration. Thai narrative-convention prefers names for clarity — rendering as 'พระเยซู' in narrative-voice keeps flow natural; the divine-register comes through ตรัส.
  - Μάρθα Μάρθα → มารธา มารธาเอ๋ย — Per uW figs-reduplication: name-doubling for emphasis/tender-address. Thai 'เอ๋ย' vocative-particle captures the tender-urgent tone (used on the second occurrence).
  - μεριμνᾷς καὶ θορυβάζῃ περὶ πολλά → เจ้ากังวลและกลัดกลุ้มใจเรื่องมากมาย — Per uW figs-doublet: μεριμνάω + θορυβάζω 'anxious + troubled' = doublet-for-emphasis. HAPAX θορυβάζω 'be-agitated' — only NT use. Thai 'กังวล + กลัดกลุ้มใจ' matches the doublet-pair. 'เจ้า' intimate-address (teacher...
- Notes: HAPAX θορυβάζω — only NT use. The name-doubling 'Martha, Martha' is a tender-urgent address-pattern used elsewhere: 'Simon, Simon' (Luke 22:31), 'Saul, Saul' (Acts 9:4), 'Jerusalem, Jerusalem' (Matt 23:37, Luke 13:34). The doublet μεριμνάω+θορυβάζω (internal-worry+external-agitation) emphasizes Martha's distress. Jesus' response is NOT a rebuk...

**Luke 10:42**
- GR: ὀλίγων δέ ἐστιν χρεία ἢ ἑνός·Μαριὰμ γὰρ τὴν ἀγαθὴν μερίδα ἐξελέξατο ἥτις οὐκ ἀφαιρεθήσεται αὐτῆς.
- TH: แต่มีเพียงไม่กี่สิ่งเท่านั้นที่จำเป็น หรือแท้จริงเพียงสิ่งเดียวเท่านั้น เพราะว่ามารีย์ได้เลือกส่วนที่ดีนั้นแล้ว ซึ่งจะไม่ถูกเอาไปจากนาง»
- TH-summary: ข้อนี้มีความแปรปรวนในต้นฉบับภาษากรีก ต้นฉบับเก่าแก่ที่สุดบางฉบับอ่านว่า «มีไม่กี่สิ่งที่จำเป็น หรือเพียงสิ่งเดียว» ขณะที่ต้นฉบับอื่นๆ อ่านเพียงว่า «มีเพียงสิ่งเดียวที่จำเป็น» การแปลของเราตามต้นฉบับที่เก่าที่สุด «สิ่งเดียว» ที่พระเยซูทรงหมายถึงคือการนั่งฟังคำสอนของพระองค์เหมือนที่มารีย์ได้เลือก ไม่ใช่การเตรียมอาหารที่มารธากำลังวุ่นวายอยู่
- Key decisions:
  - ὀλίγων δέ ἐστιν χρεία ἢ ἑνός → แต่มีเพียงไม่กี่สิ่งเท่านั้นที่จำเป็น หรือแท้จริงเพียงสิ่งเดียวเท่านั้น — **TEXTUAL VARIANT.** SBLGNT reads 'ὀλίγων δέ ἐστιν χρεία ἢ ἑνός' (few things are needed, or one) — conflation of two traditions; supported by P75, P45, B, C^2. NA28 and majority of modern ETs read 'ἑνός δέ ἐστιν χρε...
  - τὴν ἀγαθὴν μερίδα ἐξελέξατο → ได้เลือกส่วนที่ดีนั้นแล้ว — μερίς → ส่วน (portion). ἐκλέγομαι aor-mid 'chose-for-oneself.' Thai 'ได้เลือก...แล้ว' completed-choice preserved. Per uW alt: 'better activity.' The definite-article ('THE good portion') implies the right-choice fro...
  - οὐκ ἀφαιρεθήσεται αὐτῆς → จะไม่ถูกเอาไปจากนาง — ἀφαιρέω fut-pass 'will-not-be-taken-away.' Per uW figs-activepassive: alt (1) 'I will not take that opportunity away from her' OR (2) 'God will not let her lose what she has gained.' Thai passive preserves the neutr...
- Notes: **TEXTUAL VARIANT:** SBLGNT reads ὀλίγων δέ ἐστιν χρεία ἢ ἑνός 'few things are needed, or one' — conflation of two earlier traditions. NA28 and most modern ETs read ἑνός δέ ἐστιν χρεία 'one thing is needed' (supported by P3, A, C, W, Byzantine majority). A third tradition reads ὀλίγων δέ ἐστιν χρεία 'few things are needed' without ἢ ἑνός. SBLG...


---

### Luke 15

**Luke 15:1**
- GR: Ἦσαν δὲ αὐτῷ ἐγγίζοντες πάντες οἱ τελῶναι καὶ οἱ ἁμαρτωλοὶ ἀκούειν αὐτοῦ.
- TH: ครั้งนั้น บรรดาคนเก็บภาษีและคนบาปพากันเข้ามาใกล้พระองค์เพื่อฟังพระองค์
- TH-summary: พระกิตติคุณลูกาแสดงภาพที่ขัดต่อความคาดหมายของสังคมสมัยนั้น — ผู้ที่ถูกมองว่า «ไม่บริสุทธิ์» กลับเป็นกลุ่มที่แสวงหาพระเยซู ฉากนี้ตั้งเวทีสำหรับคำอุปมาสามเรื่องที่จะตามมาในบทนี้ ซึ่งทั้งหมดเป็นคำตอบต่อการบ่นของพวกฟาริสีในข้อ 2
- Key decisions:
  - Ἦσαν & ἐγγίζοντες → พากันเข้ามาใกล้ — Periphrastic imperfect (εἰμί + present participle) = durative 'they kept drawing near' (uW writing-participants). Thai 'พากันเข้ามาใกล้' preserves the ongoing, communal nature of the gathering.
  - πάντες → บรรดา — Per uW figs-hyperbole: 'all' is an overstatement for emphasis ('many'). Thai 'บรรดา' (a great many/the collective) captures the hyperbolic collective without literalizing to 'every single tax collector.'
  - οἱ τελῶναι καὶ οἱ ἁμαρτωλοὶ → คนเก็บภาษีและคนบาป — Glossary-established Lukan pairing (cf. 5:30, 7:34, 19:7). 'คนเก็บภาษีและคนบาป' is the stereotyped Lukan phrase — kept consistent across chapters.
  - ἀκούειν αὐτοῦ → เพื่อฟังพระองค์ — Present infinitive of purpose 'to hear him.' 'ฟัง' + royal pronoun 'พระองค์' (Jesus as divine addressee). Non-divine persons 'ฟัง' without royal marking; the object-honorific here is via pronoun.
- Notes: Lukan scene-setting for the three lost/found parables (vv.4-7, 8-10, 11-32). The periphrastic imperfect signals ongoing, scene-establishing action — 'tax collectors and sinners' had become habitual listeners at this point of Luke's travel narrative. The 'tax collectors and sinners' phrase is stereotyped throughout Luke (cf. 5:30, 7:34, 19:7) a...

**Luke 15:2**
- GR: καὶ διεγόγγυζον οἵ τε Φαρισαῖοι καὶ οἱ γραμματεῖς λέγοντες ὅτι Οὗτος ἁμαρτωλοὺς προσδέχεται καὶ συνεσθίει αὐτοῖς.
- TH: พวกฟาริสีและพวกธรรมาจารย์ก็บ่นกันว่า «ชายผู้นี้ต้อนรับคนบาป และรับประทานอาหารร่วมกับพวกเขา»
- TH-summary: ในวัฒนธรรมยิวสมัยนั้น การร่วมโต๊ะอาหารเป็นสัญลักษณ์ของการยอมรับและความสนิทสนม พวกฟาริสียึดถือกฎแห่งความบริสุทธิ์อย่างเคร่งครัดและหลีกเลี่ยงการกินกับ «คนบาป» เพราะถือเป็นการปนเปื้อน การที่พระเยซูทรงนั่งรับประทานกับพวกเขา จึงเป็นการประกาศว่าพระเจ้าทรงรับพวกเขา — และเป็นสาเหตุของการบ่นว่าของพวกฟาริสีเสมอมา (เปรียบกับลูกา 5:30, 7:34, 19:7)
- Key decisions:
  - διεγόγγυζον → บ่นกัน — Imperfect of διαγογγύζω 'grumble/murmur throughout (a group).' The δια- prefix intensifies + conveys communal spread of the grumbling (uW grammar-connect-logic-result). Same verb at Luke 19:7. 'บ่นกัน' captures the ...
  - οἵ τε Φαρισαῖοι καὶ οἱ γραμματεῖς → พวกฟาริสีและพวกธรรมาจารย์ — Standard Lukan pairing (uW writing-participants: reintroducing this character-group from 5:17-30 onward). 'พวกฟาริสี/พวกธรรมาจารย์' — established glossary renderings. τε...καί binds them as one grumbling unit.
  - Οὗτος → ชายผู้นี้ — Demonstrative pronoun used pejoratively (uW figs-explicit: means Jesus but dismissive). 'ชายผู้นี้' captures the distancing tone — not naming him, treating him as a specimen. Preserves the contemptuous register of t...
  - προσδέχεται → ต้อนรับ — Present of προσδέχομαι 'receive/welcome.' Stronger than mere toleration — it is active reception. 'ต้อนรับ' carries the welcoming-hospitality sense (glossary-established from prior Luke). The present tense is habitu...
  - συνεσθίει αὐτοῖς → รับประทานอาหารร่วมกับพวกเขา — Present of συνεσθίω 'eat-together-with.' Table-fellowship was a high-significance boundary marker in Second-Temple Judaism. 'รับประทานอาหารร่วมกับ' echoes Luke 5:30 ('รับประทานและดื่มร่วมกับคนเก็บภาษีและคนบาป') for ...
- Notes: The Pharisees' grumble is the catalyst for the three parables. Table fellowship (συνεσθίω) in the Jewish cultural context implied solidarity — to eat with someone was to accept them into one's circle. Pharisees built elaborate halakhah around whom one could eat with; the Qumran Community Rule (1QS 6.16-17) shows how serious this was. Jesus's w...

**Luke 15:3**
- GR: εἶπεν δὲ πρὸς αὐτοὺς τὴν παραβολὴν ταύτην λέγων·
- TH: พระเยซูจึงตรัสคำอุปมานี้แก่พวกเขาว่า
- Key decisions:
  - εἶπεν δὲ → จึงตรัส — Per uW grammar-connect-logic-result: δέ introduces Jesus's response to the grumbling. ราชาศัพท์ 'ตรัส' (royal speech-verb) for Jesus as speaker (RULES §3).
  - τὴν παραβολὴν ταύτην → คำอุปมานี้ — 'This parable' (singular, per Greek) introduces what will in fact be a trilogy — but Luke treats it narratively as one teaching-unit answering the grumble. 'คำอุปมา' — glossary-established (cf. Luke 5:36, 8:4ff, 12:...
- Notes: The singular τὴν παραβολήν is noteworthy: what follows is three distinct parables (sheep, coin, sons), but Luke framed them as one unified response. The literary structure is deliberate: each parable escalates in detail (~4 verses → 3 verses → 22 verses) and intensifies the personal stake (animal → object → human son). All three share the patt...

**Luke 15:4**
- GR: Τίς ἄνθρωπος ἐξ ὑμῶν ἔχων ἑκατὸν πρόβατα καὶ ἀπολέσας ἐξ αὐτῶν ἓν οὐ καταλείπει τὰ ἐνενήκοντα ἐννέα ἐν τῇ ἐρήμῳ καὶ πορεύεται ἐπὶ τὸ ἀπολωλὸς ἕως εὕρῃ αὐτό;
- TH: «ในพวกท่านคนใดที่มีแกะหนึ่งร้อยตัว แล้วตัวหนึ่งหายไป จะไม่ละแกะเก้าสิบเก้าตัวไว้ในถิ่นทุรกันดาร และออกไปตามหาแกะตัวที่หายนั้นจนกว่าจะพบหรือ?
- TH-summary: ในพระคัมภีร์เดิม พระเจ้าเองทรงเป็น «ผู้เลี้ยงแกะ» ของอิสราเอล (สดุดี 23; เอเสเคียล 34) เอเสเคียล 34 ตำหนิผู้เลี้ยงที่ไม่แสวงหาแกะที่หลง และพยากรณ์ว่าพระเจ้าเองจะทรงเป็นผู้เลี้ยงที่ไปตามหา พระเยซูทรงนำภาพนี้มาใช้เพื่อแสดงว่าการที่พระองค์ต้อนรับ «คนบาป» นั้นเป็นการกระทำของพระเจ้าผู้แสวงหาแกะที่หายไป ไม่ใช่การละเมิดธรรมบัญญัติ
- Key decisions:
  - Τίς ἄνθρωπος ἐξ ὑμῶν → ในพวกท่านคนใด — Rhetorical question opener (uW figs-rquestion + figs-hypo). Jesus invites the audience to place themselves in the shepherd's position. 'ในพวกท่านคนใด' preserves the rhetorical-inclusive form; keeps the scenario-as-h...
  - ἀπολέσας & τὸ ἀπολωλὸς → หายไป & ที่หาย — ἀπόλλυμι aorist-active-participle 'having lost' + perfect-passive-participle 'the one having been lost' (substantival). Thai 'หาย' (be lost/missing) carries both active-cause and passive-state senses naturally; usin...
  - ἐν τῇ ἐρήμῳ → ในถิ่นทุรกันดาร — RULES §4 glossary: ἔρημος → ถิ่นทุรกันดาร. Though BSB renders 'pasture' (fitting the shepherd-grazing context of semi-arid hill-country), the underlying Greek is the same word Luke uses for John's wilderness (1:80, ...
  - οὐ καταλείπει & πορεύεται → จะไม่ละ & และออกไปตามหา — Present indicatives framed by rhetorical-question negation 'does he not leave...and go?' The question expects 'yes, of course he does.' 'จะไม่ละ...และออกไปตามหาหรือ?' preserves the affirmative-by-rhetorical-negation.
  - ἕως εὕρῃ αὐτό → จนกว่าจะพบ — Aorist-subjunctive 'until he finds it.' 'จนกว่าจะพบ' — the persistence of searching is emphasized. Same phrase echoes in v.8 (woman searching the coin).
- Notes: First parable. The question-form (uW figs-rquestion) is designed to elicit the audience's own assent to the shepherd's behavior before they realize its implication (that God behaves the same toward 'sinners'). The 99-vs-1 math is meant to emphasize: even a small proportional loss moves a shepherd to exhaustive search. ἔρημος here denotes Judea...

**Luke 15:5**
- GR: καὶ εὑρὼν ἐπιτίθησιν ἐπὶ τοὺς ὤμους αὐτοῦ χαίρων,
- TH: และเมื่อพบแล้ว ก็ยกแกะตัวนั้นวางบนบ่าด้วยความยินดี
- Key decisions:
  - εὑρὼν → เมื่อพบแล้ว — Aorist-active-participle of εὑρίσκω 'having found.' The temporal relation to the main verb is antecedent. 'เมื่อพบแล้ว' captures the 'once found' sense.
  - ἐπιτίθησιν ἐπὶ τοὺς ὤμους αὐτοῦ → ยกแกะตัวนั้นวางบนบ่า — Present of ἐπιτίθημι 'place upon.' Per uW figs-explicit: this is the standard way a shepherd carries a sheep for the return trip — legs draped over both shoulders for stability. 'ยก...วางบนบ่า' conveys the lifting-a...
  - χαίρων → ด้วยความยินดี — Present-active-participle of χαίρω 'rejoicing.' Adverbial modification of the main verb — the carrying IS joyful. 'ด้วยความยินดี' (with joy) captures the manner. The χαρά root recurs in the refrain (vv.6, 7, 9, 10, ...
- Notes: The carrying-on-shoulders was iconic in ancient shepherd-art and later became the 'Good Shepherd' icon in early Christian imagery. Physically, tired or injured sheep were carried home across the shoulders with front legs held in one hand and hind legs in the other (see uW figs-explicit note). The joyfulness (χαίρων) is the interpretive key — t...

**Luke 15:6**
- GR: καὶ ἐλθὼν εἰς τὸν οἶκον συγκαλεῖ τοὺς φίλους καὶ τοὺς γείτονας,λέγων αὐτοῖς·Συγχάρητέ μοι ὅτι εὗρον τὸ πρόβατόν μου τὸ ἀπολωλός.
- TH: เมื่อกลับถึงบ้าน ก็เรียกมิตรสหายและเพื่อนบ้านมาพร้อมกัน กล่าวแก่พวกเขาว่า ‹จงร่วมยินดีกับข้าพเจ้าเถิด เพราะข้าพเจ้าพบแกะของข้าพเจ้าที่หายไปแล้ว›
- Key decisions:
  - συγκαλεῖ → เรียก...มาพร้อมกัน — Present of συγκαλέω 'call together.' The συν-prefix is load-bearing — the recovery is not private joy but communal celebration. 'เรียก...มาพร้อมกัน' preserves the gathering sense. Same verb at v.9 (woman calling nei...
  - τοὺς φίλους καὶ τοὺς γείτονας → มิตรสหายและเพื่อนบ้าน — φίλος 'friend' + γείτων 'neighbor.' Same pairing at v.9 (but feminine forms there). 'มิตรสหาย' (close companions) + 'เพื่อนบ้าน' (neighbors) — the natural Thai pair for this social circle.
  - Συγχάρητέ μοι → จงร่วมยินดีกับข้าพเจ้าเถิด — Aorist-passive imperative of συγχαίρω 'rejoice-together-with.' Direct quotation of shepherd's invitation. 'จงร่วมยินดี' carries the 'rejoice together' sense; 'เถิด' softens to invitation-register (not harsh command)...
  - ὅτι εὗρον τὸ πρόβατόν μου τὸ ἀπολωλός → เพราะข้าพเจ้าพบแกะของข้าพเจ้าที่หายไปแล้ว — Causal ὅτι 'because/that.' Aorist εὗρον 'I have found.' τὸ ἀπολωλός = perfect-passive-participle 'the lost one' (attributive). Thai preserves the attributive structure 'แกะของข้าพเจ้าที่หายไป' (my-sheep that-was-lost).
- Notes: The συν- prefix dominates this verse (συγκαλεῖ 'call-together' + συγχάρητε 'rejoice-together') — setting up a communal-joy motif that will recur in each of the three parables. The shepherd's joy is not private; it demands community. This anticipates the theological punch of v.7: heaven itself is the community that rejoices. The call-together-n...

**Luke 15:7**
- GR: λέγω ὑμῖν ὅτι οὕτως χαρὰ ἐν τῷ οὐρανῷ ἔσται ἐπὶ ἑνὶ ἁμαρτωλῷ μετανοοῦντι ἢ ἐπὶ ἐνενήκοντα ἐννέα δικαίοις οἵτινες οὐ χρείαν ἔχουσιν μετανοίας.
- TH: เราบอกพวกท่านว่า ในทำนองเดียวกัน จะมีความยินดีในสวรรค์เพราะคนบาปคนเดียวที่กลับใจ มากกว่าเพราะคนชอบธรรมเก้าสิบเก้าคนที่ไม่จำเป็นต้องกลับใจ
- TH-summary: ประโยคว่า «คนชอบธรรมเก้าสิบเก้าคนที่ไม่จำเป็นต้องกลับใจ» เป็นคำเสียดสี พระเยซูไม่ได้หมายความว่ามีคนบนโลกที่ไม่จำเป็นต้องกลับใจจริง ๆ แต่กำลังใช้ภาษาของพวกฟาริสีเองที่คิดว่าตนเองชอบธรรมอยู่แล้ว เพื่อชี้ว่าพระเจ้าทรงยินดีมากกว่ากับคนที่ยอมกลับใจ ไม่ใช่กับคนที่คิดว่าตนเองไม่ต้องการการกลับใจ (เปรียบกับลูกา 5:31-32)
- Key decisions:
  - λέγω ὑμῖν → เราบอกพวกท่านว่า — Jesus-speech emphatic-formula (uW: 'I can assure you'). Jesus as divine-teaching-authority but in parable-teaching mode — 'เรา' (royal first-person) + 'บอก' (teaching verb). Standard Lukan rendering pattern for λέγω...
  - οὕτως → ในทำนองเดียวกัน — Per uW figs-explicit: implicit meaning is 'just as the shepherd rejoiced.' 'ในทำนองเดียวกัน' (in-the-same-manner) makes the analogy explicit without over-expanding.
  - χαρὰ ἐν τῷ οὐρανῷ ἔσται → จะมีความยินดีในสวรรค์ — Per uW figs-metonymy: 'heaven' = 'the inhabitants of heaven' (i.e., God and his court). 'ในสวรรค์' preserves the metonymic idiom without flattening to 'พระเจ้าทรงยินดี' (which would lose the heavenly-court imagery t...
  - ἐπὶ ἑνὶ ἁμαρτωλῷ μετανοοῦντι → เพราะคนบาปคนเดียวที่กลับใจ — ἐπί + dative 'over/because of.' μετανοοῦντι present-active-participle 'who is repenting' — ongoing orientation, not point-act. Thai 'ที่กลับใจ' (who-repents) natural relative-clause; 'กลับใจ' = glossary-established ...
  - δικαίοις οἵτινες οὐ χρείαν ἔχουσιν μετανοίας → คนชอบธรรม...ที่ไม่จำเป็นต้องกลับใจ — Per uW figs-nominaladj: δίκαιος used substantivally 'righteous ones.' Rhetorically ironic — the phrase describes the Pharisees' self-image (they see themselves as not-needing-repentance). Luke 5:32 parallel: 'I have...
- Notes: Theological punch-line of the sheep parable. The analogical pattern: shepherd → God/heaven; lost sheep → sinner; community of neighbors → inhabitants of heaven. The rhetorical force lies in the 99-vs-1 contrast: heaven's joy over a single repentant sinner outweighs joy over the 99 'righteous.' The phrase 'who have no need of repentance' is alm...

**Luke 15:8**
- GR: Ἢ τίς γυνὴ δραχμὰς ἔχουσα δέκα,ἐὰν ἀπολέσῃ δραχμὴν μίαν,οὐχὶ ἅπτει λύχνον καὶ σαροῖ τὴν οἰκίαν καὶ ζητεῖ ἐπιμελῶς ἕως οὗ εὕρῃ;
- TH: หรือหญิงคนใดที่มีเหรียญเงินสิบเหรียญ แล้วทำตกหายไปเหรียญหนึ่ง จะไม่จุดตะเกียง กวาดบ้าน และค้นหาอย่างละเอียดรอบคอบ จนกว่าจะพบหรือ?
- TH-summary: เหรียญดรัคมา (δραχμή) มีค่าเท่ากับค่าแรงหนึ่งวันของคนงาน หญิงที่มีสิบเหรียญจึงเก็บทรัพย์ของครอบครัวไว้ทั้งหมด บางคนเชื่อว่าเหรียญสิบเหรียญเป็นผ้าคาดศีรษะแต่งงาน (คล้ายแหวนแต่งงาน) การทำหายเหรียญหนึ่งเหมือนการเสียส่วนหนึ่งของสิ่งศักดิ์สิทธิ์ บ้านของชาวปาเลสไตน์มืดมัว มีหน้าต่างเล็ก พื้นดิน จึงต้องจุดตะเกียงและกวาดเพื่อให้เหรียญกลิ้งออกมา
- Key decisions:
  - Ἢ τίς γυνὴ → หรือหญิงคนใด — Ἤ 'or' connects to previous parable (parallelism of scenario). Jesus pairs a male-centered with a female-centered parable — uW chapter intro notes this may be deliberate paired-genders for comprehensive teaching. 'ห...
  - δραχμὰς & δραχμὴν → เหรียญเงิน & เหรียญ — δραχμή = Greek silver coin worth ~one day's wage (uW translate-bmoney; avoid anachronistic modern currency). 'เหรียญเงิน' (silver coin) captures the material; second occurrence 'เหรียญ' abbreviated since context est...
  - ἐπιμελῶς → อย่างละเอียดรอบคอบ — HAPAX LEGOMENON — ἐπιμελῶς (only NT occurrence; adv. form of ἐπιμελής 'careful/painstaking'; cf. 2 Macc 2:25 LXX for careful composition; Diosc. Mat. Med. for careful preparation). Classical Greek: 'with careful att...
  - ἅπτει λύχνον καὶ σαροῖ τὴν οἰκίαν → จุดตะเกียง กวาดบ้าน — Present indicatives framed by rhetorical-question negation (uW figs-rquestion + figs-hypo). λύχνος = oil-lamp (house-light); σαρόω = sweep. Per uW figs-synecdoche: σαροῖ τὴν οἰκίαν = sweep the floor (whole-for-part)...
- Notes: HAPAX: ἐπιμελῶς. Second parable in the lost-and-found trilogy, structurally parallel to vv.4-7 but with a female protagonist — uW chapter intro suggests Jesus may be using a man + a woman as paired examples for comprehensive teaching of his audience. The 10 drachmas: scholarly consensus is divided on whether these were household savings or a w...

**Luke 15:9**
- GR: καὶ εὑροῦσα συγκαλεῖ τὰς φίλας καὶ γείτονας λέγουσα·Συγχάρητέ μοι ὅτι εὗρον τὴν δραχμὴν ἣν ἀπώλεσα.
- TH: และเมื่อพบแล้ว นางก็เรียกเพื่อนผู้หญิงและเพื่อนบ้านมาพร้อมกัน กล่าวว่า ‹จงร่วมยินดีกับข้าพเจ้าเถิด เพราะข้าพเจ้าพบเหรียญที่ข้าพเจ้าทำหายไปแล้ว›
- Key decisions:
  - τὰς φίλας καὶ γείτονας → เพื่อนผู้หญิงและเพื่อนบ้าน — Feminine forms φίλας (fem. plural of φίλη) + γείτονας (either-gender; context-feminine). The feminine-specific friends = women friends (social circles were often gender-segregated). 'เพื่อนผู้หญิง' explicitly marks ...
  - Συγχάρητέ μοι ὅτι εὗρον τὴν δραχμὴν ἣν ἀπώλεσα → จงร่วมยินดีกับข้าพเจ้าเถิด เพราะข้าพเจ้าพบเหรียญที่ข้าพเจ้าทำหายไปแล้ว — Exact verbal parallel to v.6 (shepherd's call), with δραχμή replacing πρόβατον. Translation preserves the exact structural parallelism intentional in the Greek. ἀπώλεσα aorist 'I had-lost' — prior to finding (indire...
- Notes: Structural parallel to v.6 — the communal-celebration refrain is verbally intentional. The woman's gathering of a female social circle matches the shepherd's male one; Jesus presents divine rejoicing as gender-comprehensive, not gender-specific. Mark the small difference: the woman says 'I had lost' (indicating finding-closure) while the sheph...

**Luke 15:10**
- GR: οὕτως,λέγω ὑμῖν,γίνεται χαρὰ ἐνώπιον τῶν ἀγγέλων τοῦ θεοῦ ἐπὶ ἑνὶ ἁμαρτωλῷ μετανοοῦντι.
- TH: เราบอกพวกท่านว่า ในทำนองเดียวกัน ย่อมมีความยินดีต่อหน้าเหล่าทูตสวรรค์ของพระเจ้า เพราะคนบาปคนเดียวที่กลับใจ»
- TH-summary: ที่ว่า «ต่อหน้าเหล่าทูตสวรรค์ของพระเจ้า» เป็นการอ้อมคำเพื่อไม่เอ่ยพระนามของพระเจ้าโดยตรง (ตามประเพณียิว) หมายความว่า พระเจ้าเองทรงยินดี และทูตสวรรค์ผู้อยู่ต่อหน้าพระองค์ก็ยินดีด้วย ภาพเปรียบเทียบ: พระเจ้าเหมือนเจ้าภาพในงานเลี้ยงฉลองที่มีทูตสวรรค์เป็นแขกผู้ร่วมยินดี
- Key decisions:
  - ἐνώπιον τῶν ἀγγέλων τοῦ θεοῦ → ต่อหน้าเหล่าทูตสวรรค์ของพระเจ้า — Per uW figs-metaphor: ἐνώπιον = 'in the presence of.' 'ต่อหน้า' (lit. before-face-of) captures the presence-sense. The phrase is a periphrasis avoiding direct mention of God's joy — both his heavenly court rejoices ...
  - γίνεται → ย่อมมี — Present of γίνομαι 'comes-to-be/happens.' Not the future ἔσται of v.7 — v.10 uses present-gnomic 'there occurs/there is.' 'ย่อมมี' (habitually-there-is) captures the gnomic-present generalization.
  - οὕτως & λέγω ὑμῖν → เราบอกพวกท่านว่า ในทำนองเดียวกัน — Word-order flipped from Greek (οὕτως first, then parenthetical 'I tell you') for Thai naturalness. Same formula as v.7; consistent rendering.
- Notes: Second parable's punch-line, closing the coin pericope. The slight variation from v.7 ('joy in heaven' → 'joy before the angels of God') amplifies: where v.7 uses heaven-as-location metonymy, v.10 names the angelic court explicitly. This anticipates 12:8-9 (confession 'before the angels of God') and 16:22 (angels escorting Lazarus). The joy-ov...

**Luke 15:11**
- GR: Εἶπεν δέ·Ἄνθρωπός τις εἶχεν δύο υἱούς.
- TH: พระองค์ตรัสอีกว่า «ชายคนหนึ่งมีบุตรชายสองคน
- Key decisions:
  - Εἶπεν δέ → พระองค์ตรัสอีกว่า — Per uW figs-parables: transition to a further parable. 'ตรัสอีกว่า' — royal-speech-verb (continuing from v.3) + 'อีก' (again/further) marks the next-in-series relationship. The three parables are narratively linked ...
  - Ἄνθρωπός τις εἶχεν δύο υἱούς → ชายคนหนึ่งมีบุตรชายสองคน — Per uW writing-participants: standard parable-opener formula. 'ชายคนหนึ่ง' = 'a certain man' (indefinite-specific). Note: this is a parable-internal human character, so no ราชาศัพท์ (royal register) for the 'father'...
- Notes: Opening of the longest parable in Luke (22 verses). The two-sons setup signals a common Lukan device (two responses to the same situation) also at 7:41-47 (two debtors) and 18:9-14 (Pharisee and tax collector). Structural: the parable divides into prodigal-recovery (vv.11-24) and older-son-reaction (vv.25-32). Cultural note on naming: the sons...

**Luke 15:12**
- GR: καὶ εἶπεν ὁ νεώτερος αὐτῶν τῷ πατρί·Πάτερ,δός μοι τὸ ἐπιβάλλον μέρος τῆς οὐσίας·ὁ δὲ διεῖλεν αὐτοῖς τὸν βίον.
- TH: บุตรคนเล็กพูดกับบิดาว่า ‹บิดาเจ้าข้า ขอมอบทรัพย์ส่วนที่ข้าพเจ้าจะได้รับเป็นมรดกแก่ข้าพเจ้าเถิด› บิดาก็แบ่งทรัพย์สินให้แก่ทั้งสองคน
- TH-summary: ในวัฒนธรรมปาเลสไตน์สมัยโบราณ การขอมรดกในขณะที่บิดายังมีชีวิตอยู่เป็นเรื่องที่ไม่เคารพอย่างร้ายแรง เกือบเท่ากับปรารถนาให้บิดาตาย ตามธรรมบัญญัติ (เฉลยธรรมบัญญัติ 21:17) บุตรหัวปีได้รับส่วนสองเท่า ดังนั้นบุตรคนเล็กจะได้ประมาณหนึ่งในสามของทรัพย์สินทั้งหมด การที่บิดายอมให้ แสดงถึงความรักที่ยอมเสียศักดิ์ศรีเพื่อเคารพเจตจำนงเสรีของบุตร
- Key decisions:
  - Πάτερ,δός μοι → บิดาเจ้าข้า ขอมอบ...แก่ข้าพเจ้าเถิด — Per uW figs-imperative: δός is aorist imperative expressing immediate/urgent request. Thai 'ขอ...เถิด' (please...would-you) is a request-imperative softening appropriate for son-to-father address within the parable....
  - τὸ ἐπιβάλλον μέρος τῆς οὐσίας → ทรัพย์ส่วนที่ข้าพเจ้าจะได้รับเป็นมรดก — Per uW figs-idiom: 'the portion that falls-to (one)' = 'the share of inheritance that would come to me.' ἐπιβάλλω neuter-participle substantivized = 'the portion falling (to me).' Thai expansion 'ทรัพย์ส่วนที่ข้าพเจ...
  - διεῖλεν αὐτοῖς τὸν βίον → แบ่งทรัพย์สินให้แก่ทั้งสองคน — διαιρέω 'divide/apportion.' βίος = 'means of life, property' (different sense from ζωή 'life itself'). Per uW 'he divided his wealth between his two sons.' 'แบ่งทรัพย์สินให้แก่ทั้งสองคน' — the βίος-as-wealth sense m...
- Notes: The scandal embedded in the younger son's request: in Mediterranean patrilineal culture, asking for inheritance while the father lived was tantamount to declaring the father dead to him (see K. Bailey, Poet & Peasant; Jerome's comm. ad loc.). The father's compliance — 'he divided' (διεῖλεν) — is culturally shocking. He does not rebuke or withh...

**Luke 15:13**
- GR: καὶ μετ’οὐ πολλὰς ἡμέρας συναγαγὼν πάντα ὁ νεώτερος υἱὸς ἀπεδήμησεν εἰς χώραν μακράν,καὶ ἐκεῖ διεσκόρπισεν τὴν οὐσίαν αὐτοῦ ζῶν ἀσώτως.
- TH: ไม่กี่วันต่อมา บุตรคนเล็กก็รวบรวมทุกสิ่งที่ตนมี ออกเดินทางไปยังแดนไกล และที่นั่นเขาได้ผลาญทรัพย์สินของตนด้วยการใช้ชีวิตอย่างสุรุ่ยสุร่าย
- TH-summary: «แดนไกล» (χώρα μακρά) บ่งบอกว่าเป็นดินแดนของคนต่างชาติ (ไม่ใช่ยิว) การที่บุตรคนเล็กไปอยู่ไกลบ้าน คือการตัดสัมพันธ์กับชุมชนแห่งพันธสัญญา และต่อมาการไปเลี้ยงสุกร (ข้อ 15) ก็ยืนยันว่าเขาอยู่ในดินแดนของคนต่างชาติ
- Key decisions:
  - μετ’ οὐ πολλὰς ἡμέρας → ไม่กี่วันต่อมา — Per uW figs-litotes: 'not many days' = 'few days' (positive-meaning-via-negative-negation). 'ไม่กี่วันต่อมา' (a-few-days-later) — Thai natural idiom; the speed of departure emphasizes eagerness to leave, not practic...
  - συναγαγὼν πάντα → รวบรวมทุกสิ่งที่ตนมี — Per uW: 'having packed all of his things' (συνάγω = collect/gather). 'รวบรวมทุกสิ่งที่ตนมี' (gathered-up everything he-owned) natural Thai; 'ที่ตนมี' clarifies the possessive range.
  - ἀπεδήμησεν εἰς χώραν μακράν → ออกเดินทางไปยังแดนไกล — ἀποδημέω = 'go abroad (as an expatriate).' The ἀπο- prefix emphasizes leaving-for-good. 'ออกเดินทางไปยัง' captures the emigration-sense. 'แดนไกล' — deliberately Gentile-associated (distant-land) rather than generic ...
  - διεσκόρπισεν τὴν οὐσίαν αὐτοῦ → ผลาญทรัพย์สินของตน — διασκορπίζω = 'scatter abroad, dissipate.' Strong metaphor of wealth being blown in all directions. 'ผลาญ' (burn-through/consume) is the standard Thai verb for wasteful-spending and captures the scattering-away sense.
  - ζῶν ἀσώτως → ใช้ชีวิตอย่างสุรุ่ยสุร่าย — HAPAX LEGOMENON — ἀσώτως (only NT occurrence; cf. ἄσωτος 'dissolute' at Eph 5:18). Classical Greek: from α-privative + σῴζω = 'without-saving/without-thinking-of-preservation.' Per uW: 'without thinking about the co...
- Notes: HAPAX: ἀσώτως. The ἀσώτως adverb is the etymological root of the traditional title 'Prodigal Son' (Latin prodigus = wasteful). The word's classical force: 'in a manner tending toward self-destruction' — not merely 'extravagant' but 'without regard for one's own preservation.' The Greek suggests not just financial mismanagement but moral self-d...

**Luke 15:14**
- GR: δαπανήσαντος δὲ αὐτοῦ πάντα ἐγένετο λιμὸς ἰσχυρὰ κατὰ τὴν χώραν ἐκείνην,καὶ αὐτὸς ἤρξατο ὑστερεῖσθαι.
- TH: เมื่อเขาใช้จ่ายจนหมดสิ้นทุกสิ่งแล้ว ก็เกิดการกันดารอาหารอย่างร้ายแรงทั่วแดนนั้น และเขาก็เริ่มขัดสน
- Key decisions:
  - δαπανήσαντος δὲ αὐτοῦ πάντα → เมื่อเขาใช้จ่ายจนหมดสิ้นทุกสิ่งแล้ว — Genitive-absolute construction (aorist-active-participle + pronoun in genitive) = temporal 'after he had spent all.' δαπανάω = 'spend/consume.' 'ใช้จ่ายจนหมดสิ้นทุกสิ่ง' — temporal subordination via 'เมื่อ...แล้ว' p...
  - λιμὸς ἰσχυρὰ → การกันดารอาหารอย่างร้ายแรง — λιμός 'famine' + ἰσχυρά 'strong/severe' (adj.-feminine agreeing with λιμός — Koine gender-variation for this noun; attic-normally-masc). 'การกันดารอาหาร' = established Thai biblical term for famine; 'อย่างร้ายแรง' (...
  - ὑστερεῖσθαι → ขัดสน — Per uW: 'to lack what he needed' / 'not to have enough to live on.' Present middle-infinitive of ὑστερέω 'fall-short/be-in-lack.' ἤρξατο + infinitive = 'began to.' 'เริ่มขัดสน' (began to be in need) captures the inc...
- Notes: Narrative turning point — the external circumstance (famine) combines with the internal state (depleted funds) to push the younger son toward the parable's crisis. The ἰσχυρά intensifier emphasizes severity. Famines in Greco-Roman antiquity could last years and devastated entire regions; the younger son's exile-land is simultaneously hit by ec...

**Luke 15:15**
- GR: καὶ πορευθεὶς ἐκολλήθη ἑνὶ τῶν πολιτῶν τῆς χώρας ἐκείνης,καὶ ἔπεμψεν αὐτὸν εἰς τοὺς ἀγροὺς αὐτοῦ βόσκειν χοίρους·
- TH: เขาจึงไปอาศัยทำงานกับชาวเมืองคนหนึ่งในแดนนั้น ซึ่งก็ส่งเขาออกไปในทุ่งนาของตนเพื่อเลี้ยงสุกร
- TH-summary: สำหรับชาวยิว สุกรเป็นสัตว์ที่ไม่สะอาดอย่างยิ่ง (เลวีนิติ 11:7) การเลี้ยงสุกรเท่ากับการอยู่ในสภาพที่ต่ำที่สุดที่ชาวยิวจินตนาการได้ ผู้ฟังของพระเยซูจะสัมผัสถึงความเสื่อมสุดขั้วของบุตรคนเล็ก — จากบุตรชายของคนมั่งคั่ง กลายเป็นคนรับใช้ที่ทำงานที่ไม่สะอาดที่สุดในดินแดนของคนต่างชาติ
- Key decisions:
  - πορευθεὶς ἐκολλήθη → ไปอาศัยทำงานกับ — Per uW figs-idiom: ἐκολλήθη (aorist-passive of κολλάω 'glue-to') = 'attached himself to' = 'began to work for.' Literal 'glued-to' conveys desperation-of-attachment (not choice; adherence-to-whoever-would-take-him)....
  - ἑνὶ τῶν πολιτῶν τῆς χώρας ἐκείνης → ชาวเมืองคนหนึ่งในแดนนั้น — πολίτης = 'citizen/countryman.' Implicitly Gentile (given the pigs). 'ชาวเมืองในแดนนั้น' preserves the Gentile-country distancing.
  - βόσκειν χοίρους → เพื่อเลี้ยงสุกร — βόσκω 'feed (animals).' χοίρος 'pig/swine' (ritually unclean per Lev 11:7; Deut 14:8). 'เลี้ยงสุกร' — 'สุกร' is the standard Thai biblical term for pig (cf. Mark 5:11-16; Matt 7:6). For Jewish reader/hearer, feeding...
- Notes: The cultural depth: for a Jew, pig-feeding was not merely undignified labor but actively forbidden. The Mishnah (b. B. Qamma 82b) preserves the saying 'Cursed is the man who raises swine.' That the younger son takes this job is the final proof of his complete detachment from his covenant identity — geographic exile (v.13) + economic exile (v.1...

**Luke 15:16**
- GR: καὶ ἐπεθύμει γεμίσαι τὴν κοιλίαν αὐτοῦ ἀπὸ τῶν κερατίων ὧν ἤσθιον οἱ χοῖροι,καὶ οὐδεὶς ἐδίδου αὐτῷ.
- TH: เขาปรารถนาจะเอาฝักถั่วที่สุกรกินนั้นมากินให้อิ่มท้อง แต่ไม่มีใครให้อะไรแก่เขาเลย
- Key decisions:
  - ἐπεθύμει → ปรารถนา — Imperfect of ἐπιθυμέω 'desire strongly/crave.' Durative-imperfect = ongoing hunger. 'ปรารถนา' (earnestly-desire) captures the craving-state. The Greek word often has moral overtones (covetousness), but here is plain...
  - κερατίων → ฝักถั่ว — HAPAX LEGOMENON — κεράτιον (only NT occurrence; diminutive of κέρας 'horn,' referring to the horn-shaped pods of the carob tree / St. John's bread-tree, Ceratonia siliqua). Per uW translate-unknown: 'husks of beans ...
  - γεμίσαι τὴν κοιλίαν αὐτοῦ → มากินให้อิ่มท้อง — γεμίζω 'fill up'; κοιλία 'belly/stomach.' Aorist-active-infinitive 'to fill (his) belly.' 'กินให้อิ่มท้อง' (eat-until-full-belly) is natural Thai idiom for hunger-satisfaction; literal 'เติมท้องของตน' would sound st...
  - οὐδεὶς ἐδίδου αὐτῷ → ไม่มีใครให้อะไรแก่เขาเลย — Per uW: the phrase is ambiguous — either 'no one was giving him anything (else) to eat' (so he desperately wished even for pig-food) OR 'his master would not allow him to eat even those pods' (so even the pig-pods w...
- Notes: HAPAX: κεράτιον (carob pods). The κεράτιον ('little horn') is the fruit of the carob tree (Ceratonia siliqua), native to the eastern Mediterranean. Pods are hard, sweet when dry, commonly fed to livestock; humans ate them only in extreme hunger. A rabbinic tradition (Lev. Rabba 35.6) holds that 'when the Israelites are in need of carobs, they ...

**Luke 15:17**
- GR: εἰς ἑαυτὸν δὲ ἐλθὼν ἔφη·Πόσοι μίσθιοι τοῦ πατρός μου περισσεύονται ἄρτων,ἐγὼ δὲ λιμῷ ὧδε ἀπόλλυμαι·
- TH: แต่เมื่อเขาได้สติรู้ตัว ก็รำพึงว่า ‹ลูกจ้างของบิดาเรามีอาหารกินเหลือเฟือสักเท่าไร แต่เราอยู่ที่นี่ กำลังจะตายเพราะความหิวโหย
- TH-summary: คำว่า «ได้สติรู้ตัว» (εἰς ἑαυτὸν ἐλθών) เป็นสำนวนกรีกโบราณ หมายถึงการกลับมารู้ตัว เหมือนคนตื่นจากความเพ้อฝัน เป็นจุดเปลี่ยนสำคัญของคำอุปมา — ก่อนหน้านี้เขาไม่ได้คิดถึงบิดา แต่เมื่อ «ได้สติ» เขาจึงนึกถึงบ้านและพระคุณของบิดาเป็นครั้งแรก
- Key decisions:
  - εἰς ἑαυτὸν & ἐλθὼν → ได้สติรู้ตัว — Per uW figs-idiom: 'came into himself' = 'became able to understand his situation clearly / realized he had made a terrible mistake.' Classical Greek idiom (cf. Epictetus, Plutarch) for regaining lucid self-awarenes...
  - Πόσοι μίσθιοι τοῦ πατρός μου περισσεύονται ἄρτων → ลูกจ้างของบิดาเรามีอาหารกินเหลือเฟือสักเท่าไร — Per uW figs-exclamations: this is an exclamation, not a question, despite πόσοι-interrogative form. 'สักเท่าไร' (how-much/so-many) preserves both the exclamatory force and the enumerative sense. μίσθιος = 'day-labor...
  - ἐγὼ δὲ λιμῷ ὧδε ἀπόλλυμαι → แต่เราอยู่ที่นี่ กำลังจะตายเพราะความหิวโหย — Per uW figs-hyperbole: could be literal starvation OR figurative overstatement. 'กำลังจะตาย' (about-to-die) preserves the dramatic present/imminence of ἀπόλλυμαι (present-middle 'I-am-perishing'). Left ambiguous — a...
- Notes: IDIOM: εἰς ἑαυτὸν ἐλθών — 'coming to oneself,' classical Greek for regaining lucidity. The hinge moment of the parable. Before this, the younger son is portrayed as in a kind of self-induced delirium; now he recovers clarity. Commentators ancient (Chrysostom, Ambrose) and modern (Bailey, Capon) treat this as the repentance-dawning — though not...

**Luke 15:18**
- GR: ἀναστὰς πορεύσομαι πρὸς τὸν πατέρα μου καὶ ἐρῶ αὐτῷ·Πάτερ,ἥμαρτον εἰς τὸν οὐρανὸν καὶ ἐνώπιόν σου,
- TH: เราจะลุกขึ้นกลับไปหาบิดาของเรา และจะกล่าวแก่ท่านว่า "บิดาเจ้าข้า ข้าพเจ้าได้ทำบาปต่อฟ้าสวรรค์และต่อท่าน
- TH-summary: การพูดว่า «บาปต่อฟ้าสวรรค์» เป็นการอ้อมคำของยิวที่ไม่เอ่ยพระนามพระเจ้าโดยตรง (เพื่อเคารพบัญญัติข้อที่สาม) แปลตรง ๆ ว่า «ข้าพเจ้าทำบาปต่อพระเจ้าและต่อท่าน» บุตรตระหนักว่าบาปที่แท้จริงไม่ได้เป็นแค่ต่อบิดา แต่เป็นต่อพระเจ้าเอง
- Key decisions:
  - ἀναστὰς → ลุกขึ้น — Per uW figs-idiom: 'having-arisen' = 'I-will-leave-this-place.' Aorist-active-participle of ἀνίστημι. 'ลุกขึ้น' literally 'rise-up' preserves the physical-movement + departure idiom; same Thai verb pattern as v.20 (...
  - ἥμαρτον εἰς τὸν οὐρανὸν καὶ ἐνώπιόν σου → ได้ทำบาปต่อฟ้าสวรรค์และต่อท่าน — Per uW figs-euphemism: τὸν οὐρανόν = 'God' (Jewish reverence-for-the-Name periphrasis). 'ฟ้าสวรรค์' preserves the Jewish idiom (literally 'heaven/sky'); the euphemism is explained in thai_summary rather than flatten...
  - πορεύσομαι & ἐρῶ → จะกลับไปหา...และจะกล่าวแก่ท่านว่า — Future indicatives 'I will go...and say.' This is internal monologue (planned speech) — the son rehearses what he will say. Level-3 quote conventions: the inner-quote introducing his planned words uses double-quote ...
- Notes: EUPHEMISM: εἰς τὸν οὐρανὸν for God — Jewish reverence periphrasis (cf. m. Avot 1:3; Rab. 'kingdom of heaven' in Matthew; Luke 15:21 parallel). Per uW: Jews 'often avoided saying the word God and used heaven instead.' The son's confession is a rehearsed three-clause speech: (1) Father-address, (2) I-have-sinned (two-direction), (3) I-am-not-wor...

**Luke 15:19**
- GR: οὐκέτι εἰμὶ ἄξιος κληθῆναι υἱός σου·ποίησόν με ὡς ἕνα τῶν μισθίων σου.
- TH: ข้าพเจ้าไม่สมควรที่จะได้ชื่อว่าเป็นบุตรของท่านอีกต่อไป ขอท่านทำให้ข้าพเจ้าเป็นเหมือนลูกจ้างคนหนึ่งของท่านเถิด"›
- Key decisions:
  - οὐκέτι εἰμὶ ἄξιος κληθῆναι υἱός σου → ข้าพเจ้าไม่สมควรที่จะได้ชื่อว่าเป็นบุตรของท่านอีกต่อไป — Per uW figs-activepassive: κληθῆναι aorist-passive-infinitive 'to be called' — the agent is the father (or God). Thai 'ได้ชื่อว่าเป็น' (to-be-named-as) carries the naming-relation without requiring explicit agent. P...
  - ποίησόν με ὡς ἕνα τῶν μισθίων σου → ขอท่านทำให้ข้าพเจ้าเป็นเหมือนลูกจ้างคนหนึ่งของท่านเถิด — Per uW figs-imperative: ποίησον aorist-imperative, but functioning as request (not command). 'ขอท่าน...เถิด' (please...would-you) softens appropriately — son requesting, not demanding. 'ลูกจ้างคนหนึ่ง' = 'one of the...
- Notes: The son's plan: to abdicate sonship and petition for menial wage-labor. Crucial detail — he asks for μίσθιος (hired day-laborer), the lowest free-status position, lower than household slaves (who at least had room and board secure). This is the humility-maximization rehearsal. What the father will do (v.22 — robe, ring, sandals) goes in precis...

**Luke 15:20**
- GR: καὶ ἀναστὰς ἦλθεν πρὸς τὸν πατέρα ἑαυτοῦ.ἔτι δὲ αὐτοῦ μακρὰν ἀπέχοντος εἶδεν αὐτὸν ὁ πατὴρ αὐτοῦ καὶ ἐσπλαγχνίσθη καὶ δραμὼν ἐπέπεσεν ἐπὶ τὸν τράχηλον αὐτοῦ καὶ κατεφίλησεν αὐτόν.
- TH: เขาจึงลุกขึ้นกลับไปหาบิดาของตน ขณะที่เขายังอยู่ห่างไกล บิดาเห็นเขาก็มีใจเมตตาสงสาร วิ่งเข้าไปกอดคอเขาและจูบเขาด้วยความรัก
- TH-summary: การวิ่งไปหาบุตรเป็นการกระทำที่ปฏิวัติในวัฒนธรรมตะวันออกกลางโบราณ ชายสูงวัยที่มีศักดิ์ศรีไม่วิ่ง การวิ่งต้องเปิดเสื้อคลุมยาวออกและเผยขา ซึ่งถือเป็นการเสียศักดิ์ศรีอย่างยิ่ง การที่บิดายอมสละศักดิ์ศรีตนเอง เพื่อไปพบและปกป้องบุตรก่อนที่ชาวเมืองจะประชาทัณฑ์ คือภาพของพระคุณพระเจ้าที่ยอมเสียสละเพื่อคืนดีกับคนบาป
- Key decisions:
  - ἀναστὰς ἦλθεν → ลุกขึ้นกลับไป — Per uW figs-idiom: ἀναστάς here = 'leaving that place' (same idiom as v.18 planning-speech, now enacted). The narrative echo v.18→v.20 emphasizes that the son literally does what he rehearsed. 'ลุกขึ้นกลับไป' mirror...
  - ἔτι & αὐτοῦ μακρὰν ἀπέχοντος → ขณะที่เขายังอยู่ห่างไกล — Per uW: 'while he was still at a great distance from his father's house' (not 'still in the other country'). Genitive-absolute temporal 'while he was still being-distant.' 'ขณะที่เขายังอยู่ห่างไกล' captures the stil...
  - ἐσπλαγχνίσθη → มีใจเมตตาสงสาร — Aorist-passive of σπλαγχνίζομαι 'be-moved-with-visceral-compassion' (σπλάγχνα 'inward-parts/bowels' as the seat of emotion). Glossary-established 'ความเมตตาสงสาร' (Luke 7:13, 10:33). 'มีใจเมตตาสงสาร' matches Luke 10...
  - δραμὼν ἐπέπεσεν ἐπὶ τὸν τράχηλον αὐτοῦ → วิ่งเข้าไปกอดคอเขา — δραμών aorist-participle of τρέχω 'run.' ἐπέπεσεν ἐπὶ τὸν τράχηλον — per uW figs-idiom: 'fell-upon-the-neck' = 'gave him a hug / hugged him tightly.' The running is culturally loaded (dignified Middle-Eastern men di...
  - κατεφίλησεν αὐτόν → จูบเขาด้วยความรัก — Aorist of καταφιλέω 'kiss-down-emphatically' — the κατα- prefix intensifies beyond simple φιλέω 'kiss.' The verb is used for earnest, repeated kisses of welcome/reconciliation (cf. Acts 20:37 Paul and Ephesian elder...
- Notes: The parable's emotional climax. Three cultural facts make this scene shocking to Jesus's original audience: (1) The father sees at great distance — suggests watching/waiting. (2) The running — Kenneth Bailey's scholarship documents that Middle Eastern men of dignity did not run; running required hiking up long robes and exposing bare legs, a s...

**Luke 15:21**
- GR: εἶπεν δὲ ὁ υἱὸς αὐτῷ·Πάτερ,ἥμαρτον εἰς τὸν οὐρανὸν καὶ ἐνώπιόν σου,οὐκέτι εἰμὶ ἄξιος κληθῆναι υἱός σου.
- TH: บุตรจึงกล่าวแก่บิดาว่า ‹บิดาเจ้าข้า ข้าพเจ้าได้ทำบาปต่อฟ้าสวรรค์และต่อท่าน ข้าพเจ้าไม่สมควรที่จะได้ชื่อว่าเป็นบุตรของท่านอีกต่อไป›
- TH-summary: บุตรกล่าวคำสารภาพที่เขาเตรียมไว้ในข้อ 18-19 แต่สังเกตว่า เขาไม่ได้พูดประโยคสุดท้าย «ขอให้ข้าพเจ้าเป็นลูกจ้างของท่าน» บิดาขัดจังหวะเขาก่อน (ข้อ 22) ด้วยคำสั่งให้คนรับใช้เอาเสื้อคลุม แหวน และรองเท้ามา — สัญลักษณ์ของการคืนฐานะเป็นบุตร ไม่ใช่ลูกจ้าง
- Key decisions:
  - ἥμαρτον εἰς τὸν οὐρανὸν καὶ ἐνώπιόν σου,οὐκέτι εἰμὶ ἄξιος κληθῆναι υἱός σου → ได้ทำบาปต่อฟ้าสวรรค์และต่อท่าน ข้าพเจ้าไม่สมควรที่จะได้ชื่อว่าเป็นบุตรของท่านอีกต่อไป — Verbatim repetition of v.18-19 first-two-clauses (same euphemism, same formal petitioning structure). Thai preserves exact verbal match to v.18-19 for the recognizable-echo effect. NOTICE: the third clause of the pl...
- Notes: INCOMPLETE SPEECH: the son delivers the first two clauses of his rehearsed confession (v.18b-19a) but does NOT say 'make me as one of your hired servants' (v.19b). This is almost certainly intentional on Luke's part — the father's welcome preempts the request. Some later manuscripts (A, D, Byzantine) DO add 'make me as one of your hired servan...

**Luke 15:22**
- GR: εἶπεν δὲ ὁ πατὴρ πρὸς τοὺς δούλους αὐτοῦ·Ταχὺ ἐξενέγκατε στολὴν τὴν πρώτην καὶ ἐνδύσατε αὐτόν,καὶ δότε δακτύλιον εἰς τὴν χεῖρα αὐτοῦ καὶ ὑποδήματα εἰς τοὺς πόδας,
- TH: แต่บิดาสั่งเหล่าบ่าวของตนว่า ‹จงรีบเอาเสื้อคลุมตัวดีที่สุดมาสวมให้เขา และเอาแหวนมาสวมที่นิ้วของเขา เอารองเท้ามาสวมที่เท้าของเขา
- TH-summary: สัญลักษณ์สามอย่างในข้อนี้เป็นการคืนฐานะบุตรอย่างสมบูรณ์: (1) «เสื้อคลุมตัวดีที่สุด» เป็นเสื้อของบิดาเอง — บ่งบอกว่าเขาได้รับเกียรติในครอบครัว (2) «แหวน» น่าจะเป็นแหวนตราประทับ แสดงอำนาจในการทำธุรกรรมแทนครอบครัว (3) «รองเท้า» เป็นสิ่งที่ไพร่หรือทาสไม่สวม แสดงว่าเขาเป็นคนเสรีและเป็นเจ้านาย — ไม่ใช่ลูกจ้างตามที่เขาเตรียมจะขอ
- Key decisions:
  - Ταχὺ → จงรีบ — Adverb 'quickly.' Emphasizes the urgency of the father's restorative action — no time for deliberation. 'จงรีบ' (hasten!) carries the imperative-urgency.
  - στολὴν τὴν πρώτην → เสื้อคลุมตัวดีที่สุด — Per uW figs-metaphor: 'first' here = 'best' (cf. 14:7 πρωτοκλισία 'first-place' = 'place of honor'). στολή 'long robe' — ceremonial outer garment, distinct from mere χιτών (tunic). 'เสื้อคลุมตัวดีที่สุด' captures bo...
  - δακτύλιον εἰς τὴν χεῖρα αὐτοῦ → แหวนมาสวมที่นิ้วของเขา — HAPAX LEGOMENON — δακτύλιος (only NT occurrence; cf. LXX Gen 41:42 Pharaoh's-signet-ring-to-Joseph). Per uW figs-synecdoche: χεῖρα ('hand') stands for 'finger' — Thai 'นิ้ว' (finger) makes the synecdoche explicit pe...
  - ὑποδήματα εἰς τοὺς πόδας → รองเท้ามาสวมที่เท้าของเขา — Per uW translate-unknown: 'sandals' — type of open footwear, typically leather. In this culture, poorer people (slaves, beggars) went barefoot; more affluent wore sandals. 'รองเท้า' (footwear, generic) captures the ...
- Notes: HAPAX: δακτύλιος (ring). The three items — robe, ring, sandals — are together per uW translate-symaction 'signs of status, authority, and privilege.' Each symbolically restores a dimension of sonship: robe (public honor, perhaps the father's own), signet-ring (household authority to transact on the family's behalf), sandals (free-person vs. ba...

**Luke 15:23**
- GR: καὶ φέρετε τὸν μόσχον τὸν σιτευτόν,θύσατε,καὶ φαγόντες εὐφρανθῶμεν,
- TH: และจงนำลูกโคอ้วนที่ขุนไว้มาฆ่า ให้เรากินเลี้ยงฉลองกัน
- Key decisions:
  - τὸν μόσχον τὸν σιτευτόν → ลูกโคอ้วนที่ขุนไว้ — Per uW translate-unknown: a μόσχος σιτευτός is a young cow (calf) specially fattened for a feast. Reserved for major occasions (weddings, festivals, important guests) — not an everyday meal. 'ลูกโคอ้วน' (fattened ca...
  - θύσατε → มาฆ่า — Per uW figs-explicit: θύω 'slaughter-and-prepare-as-food.' The implicit is 'butcher and cook.' 'ฆ่า' captures the slaughter; the cooking is context-implicit as in Greek (no need to expand to 'ฆ่าและปรุง').
  - φαγόντες εὐφρανθῶμεν → กินเลี้ยงฉลองกัน — Per uW figs-hendiadys: 'eat and celebrate' = one idea ('celebrate by feasting'). Aorist-participle + aorist-subjunctive (hortatory). Per uW figs-exclusive: εὐφρανθῶμεν = 'let us all rejoice' — inclusive 'us' (includ...
- Notes: The fattened calf (מַרְבֵּק / ἀμνοὶ σιτευτοί in LXX) appears at 1 Sam 28:24 (spec. provision) and Jer 46:21 (Egypt's mercenaries in luxury). This was reserved-for-feast livestock — kept specifically for high-honor occasions. Its slaughter commits the household to a large, loud, communal celebration (the meat must be eaten same-day pre-refriger...

**Luke 15:24**
- GR: ὅτι οὗτος ὁ υἱός μου νεκρὸς ἦν καὶ ἀνέζησεν,ἦν ἀπολωλὼς καὶ εὑρέθη.καὶ ἤρξαντο εὐφραίνεσθαι.
- TH: เพราะบุตรคนนี้ของเราตายแล้วแต่กลับเป็นขึ้นมา เขาหายไปแล้วและพบอีก› แล้วพวกเขาก็เริ่มเลี้ยงฉลองกัน
- TH-summary: ภาษาของการคืนชีพ «ตายแล้วแต่กลับเป็นขึ้นมา» (νεκρὸς ἦν καὶ ἀνέζησεν) ใช้เชิงอุปมา ไม่ใช่ว่าบุตรตายจริง ๆ แต่บิดามองว่าการที่บุตรอยู่ในแดนไกลท่ามกลางคนต่างชาติ เหมือนสูญเสียเขาไปเป็นศพ และการที่เขากลับมา เหมือนการคืนชีพ ภาษานี้สะท้อนแก่นสำคัญของลูกา — พระเยซู «บุตรมนุษย์มาเพื่อจะแสวงหาและช่วยสิ่งที่หายไป» (ลูกา 19:10)
- Key decisions:
  - οὗτος ὁ υἱός μου → บุตรคนนี้ของเรา — Demonstrative-articular 'this-son-of-mine.' Ostentatively claiming sonship — directly opposite to the son's own 'I am not worthy to be called your son' (v.21). The father overrides the son's self-disqualification wi...
  - νεκρὸς ἦν καὶ ἀνέζησεν → ตายแล้วแต่กลับเป็นขึ้นมา — Per uW figs-metaphor: death/resurrection used metaphorically. ἀνέζησεν (aorist of ἀναζάω 'live-again') literally 'came-back-to-life.' The father is NOT saying the son literally died; the absence-to-Gentile-land was ...
  - ἦν ἀπολωλὼς καὶ εὑρέθη → หายไปแล้วและพบอีก — Per uW figs-metaphor: lost/found metaphorical parallel to death/resurrection. ἀπολωλώς perfect-participle 'having-been-in-a-lost-state'; εὑρέθη aorist-passive 'was-found' (divine-passive intimated — who found him? t...
  - ἤρξαντο εὐφραίνεσθαι → เริ่มเลี้ยงฉลองกัน — Per uW grammar-connect-logic-result: 'the servants prepared the feast, and the household then began to enjoy it.' Inchoative-aorist 'began to celebrate.' 'เริ่มเลี้ยงฉลองกัน' matches the εὐφραίνω-verb theme recurrin...
- Notes: Pivot verse of the parable. The father's declaration uses DOUBLE-METAPHOR (death/life + lost/found) to fuse the vocabulary of the two prior parables (sheep-found, coin-found) with the theological climax of resurrection-language. Cf. Luke 19:10: 'The Son of Man came to seek and to save the lost (ἀπολωλός)' — same perfect-participle; this parabl...

**Luke 15:25**
- GR: Ἦν δὲ ὁ υἱὸς αὐτοῦ ὁ πρεσβύτερος ἐν ἀγρῷ·καὶ ὡς ἐρχόμενος ἤγγισεν τῇ οἰκίᾳ,ἤκουσεν συμφωνίας καὶ χορῶν,
- TH: ขณะนั้น บุตรคนโตของท่านอยู่ที่ทุ่งนา และเมื่อกลับมาใกล้บ้าน ก็ได้ยินเสียงดนตรีและเสียงเต้นรำ
- TH-summary: บทที่สองของคำอุปมา: บุตรคนโตเข้ามาในฉาก เป็นภาพของพวกฟาริสีและธรรมาจารย์ (ในข้อ 2) — คนที่ทำงานหนักในบ้านของบิดา ไม่เคยหนีไปไหน แต่กลับไม่สามารถร่วมยินดีในการที่พระเจ้าทรงต้อนรับคนบาปกลับมา
- Key decisions:
  - ἐν ἀγρῷ → ที่ทุ่งนา — Per uW figs-explicit: implicit 'out working in the field.' 'ทุ่งนา' (rice-field/agricultural field) — Thai cultural equivalent to the working-field-land context; the working-implication is carried by context.
  - ὡς ἐρχόμενος ἤγγισεν → เมื่อกลับมาใกล้บ้าน — Per uW figs-explicit: 'as he came back home from the field.' Temporal ὡς + present-participle 'as coming-back' + aorist ἤγγισεν 'he-drew-near.' 'เมื่อกลับมาใกล้' preserves the approach-trajectory.
  - συμφωνίας καὶ χορῶν → เสียงดนตรีและเสียงเต้นรำ — HAPAX — both συμφωνία 'music/sound-together' (lit. 'sound-with-agreement'; cf. English 'symphony') and χορός 'dance/chorus' (group-dance) are NT-hapax. Per uW figs-metonymy: 'heard dancing' — the older son could not...
- Notes: DOUBLE HAPAX: συμφωνία + χορός (both only NT occurrences, though both are common in classical/LXX Greek). συμφωνία = instrumental music ensemble (cf. Dan 3:5 LXX 'the sound of the horn, pipe...συμφωνία'); χορός = group-dance with music, standard ANE feast mode. The two together signal a full, formal celebration — not a modest family meal. The ...

**Luke 15:26**
- GR: καὶ προσκαλεσάμενος ἕνα τῶν παίδων ἐπυνθάνετο τί ἂν εἴη ταῦτα·
- TH: เขาจึงเรียกเด็กรับใช้คนหนึ่งมาถามว่าเรื่องอะไรกัน
- Key decisions:
  - προσκαλεσάμενος → เรียก...มา — Aorist-middle-participle of προσκαλέω 'call-to-oneself.' Middle voice shows self-interest (call-to-me). The older son approaches from outside and stops to inquire — he has not yet entered the house. 'เรียก...มา' cap...
  - ἕνα τῶν παίδων → เด็กรับใช้คนหนึ่ง — Per uW figs-explicit: παῖς 'boy/youth/servant' — here probably young-servant (not adult δοῦλος). 'เด็กรับใช้' (child-servant/young-servant) preserves both the youth and the servant-status. The παῖς-vs-δοῦλος distinc...
  - ἐπυνθάνετο τί ἂν εἴη ταῦτα → ถามว่าเรื่องอะไรกัน — πυνθάνομαι 'inquire'; imperfect iterative 'kept-inquiring' (persistent asking). Indirect-question with potential-optative 'what-these-things-might-be.' Per uW: 'what was happening.' 'ถามว่าเรื่องอะไรกัน' preserves t...
- Notes: The older son does not enter the house to find out — he stops at the edge and inquires through an intermediary (a young servant). This is already symptomatic: he is relationally distant even in approach. The young-servant-messenger pattern highlights that NO ONE had specifically told him about his brother's return — a detail that feeds his lat...

**Luke 15:27**
- GR: ὁ δὲ εἶπεν αὐτῷ ὅτι Ὁ ἀδελφός σου ἥκει,καὶ ἔθυσεν ὁ πατήρ σου τὸν μόσχον τὸν σιτευτόν,ὅτι ὑγιαίνοντα αὐτὸν ἀπέλαβεν.
- TH: เด็กนั้นตอบเขาว่า ‹น้องชายของท่านกลับมาแล้ว และบิดาของท่านได้สั่งให้ฆ่าลูกโคอ้วนที่ขุนไว้ เพราะท่านได้น้องกลับมาอย่างปลอดภัย›
- Key decisions:
  - Ὁ ἀδελφός σου → น้องชายของท่าน — The servant-boy frames the relationship as brotherhood ('your brother'). This is the preserved family-category. The older son's upcoming refusal of this category (v.30: 'this son of yours,' not 'my brother') will be...
  - ἔθυσεν ὁ πατήρ σου τὸν μόσχον τὸν σιτευτόν → บิดาของท่านได้สั่งให้ฆ่าลูกโคอ้วนที่ขุนไว้ — Per uW figs-metonymy: 'the father killed' — he did not do it personally; he ordered it done. 'บิดา...ได้สั่งให้ฆ่า' makes the commanding-to-kill explicit in Thai, matching uW figs-metonymy alternate translation. Cal...
  - ὅτι ὑγιαίνοντα αὐτὸν ἀπέλαβεν → เพราะท่านได้น้องกลับมาอย่างปลอดภัย — Per uW: 'because his son has come home safely.' ὑγιαίνοντα present-participle 'being-in-good-health.' ἀπέλαβεν aorist of ἀπολαμβάνω 'receive-back/get-back.' 'ได้น้องกลับมาอย่างปลอดภัย' — note the shift from 'your-br...
- Notes: The servant-boy's report is entirely positive — no hint of the father's 'dead/alive' metaphor (v.24). He reports simple facts: the brother came, the calf was killed, the brother is in good health. The moral freight added by the older son's reaction (next verses) comes not from the servant's report but from the older son's own interpretive lens...

**Luke 15:28**
- GR: ὠργίσθη δὲ καὶ οὐκ ἤθελεν εἰσελθεῖν.ὁ δὲ πατὴρ αὐτοῦ ἐξελθὼν παρεκάλει αὐτόν.
- TH: บุตรคนโตก็โกรธ และไม่ยอมเข้าไปในบ้าน บิดาจึงออกมาอ้อนวอนเขา
- TH-summary: บิดาออกมาหาบุตรคนโต เช่นเดียวกับที่วิ่งออกไปหาบุตรคนเล็ก (ข้อ 20) ทั้งสองฉากใช้คำกรีกเดียวกัน «ออกไป» (ἐξέρχομαι) บิดาจึงแสดงพระคุณเหมือนกันต่อบุตรทั้งสอง — ออกจากบ้านเพื่อไปพบทั้งคู่ คนหนึ่งด้วยการวิ่ง อีกคนด้วยการอ้อนวอน
- Key decisions:
  - ὠργίσθη → โกรธ — Aorist-passive of ὀργίζω 'be-angry.' Passive in form, active in sense (as often with emotion-verbs). Standard Greek anger-verb. 'โกรธ' plain-Thai for anger — no ราชาศัพท์ (human parable-character).
  - οὐκ ἤθελεν εἰσελθεῖν → ไม่ยอมเข้าไปในบ้าน — Imperfect θέλω 'he kept-not-willing' + aorist infinitive 'to go in.' The refusal is sustained, not a single moment. 'ไม่ยอม' (refuse-consistently) matches the continued-willful-refusal; 'เข้าไปในบ้าน' makes the hous...
  - ὁ δὲ πατὴρ αὐτοῦ ἐξελθὼν παρεκάλει αὐτόν → บิดาจึงออกมาอ้อนวอนเขา — Per uW grammar-connect-logic-result: 'so his father came outside and pleaded with him.' ἐξελθών aorist-participle 'coming-out' — SAME verbal root as the father's running-out to the younger son (δραμών + ἐπέπεσεν are...
- Notes: STRUCTURAL PARALLEL to v.20 — the father's second 'going-out.' The elder son refuses to go in just as the younger son had refused to stay home. The father goes out to seek BOTH. Ancient Mediterranean patriarchal dignity: a father with guests at a feast does not leave the head-table to go outside; the son's refusal to enter is a public affront ...

**Luke 15:29**
- GR: ὁ δὲ ἀποκριθεὶς εἶπεν τῷ πατρὶ αὐτοῦ·Ἰδοὺ τοσαῦτα ἔτη δουλεύω σοι καὶ οὐδέποτε ἐντολήν σου παρῆλθον,καὶ ἐμοὶ οὐδέποτε ἔδωκας ἔριφον ἵνα μετὰ τῶν φίλων μου εὐφρανθῶ·
- TH: เขาตอบบิดาว่า ‹ดูเถิด ตลอดหลายปีมานี้ ข้าพเจ้าได้ปรนนิบัติท่านเหมือนทาส และไม่เคยขัดคำสั่งของท่านเลย แต่ท่านก็ไม่เคยให้แม้แต่ลูกแพะแก่ข้าพเจ้าสักตัวหนึ่ง เพื่อที่ข้าพเจ้าจะได้ฉลองกับเพื่อน ๆ ของข้าพเจ้า
- TH-summary: คำพูดของบุตรคนโตเผยให้เห็นหัวใจที่มองตนเองเป็นทาส ไม่ใช่บุตร เขาใช้คำ «ปรนนิบัติเหมือนทาส» (δουλεύω) ทั้ง ๆ ที่เป็นบุตรที่ชอบธรรม ความขมขื่นของเขาคือความขมขื่นของคนทำตามธรรมบัญญัติอย่างเคร่งครัด แต่ไม่เข้าใจความรักของบิดา — ภาพเดียวกับพวกฟาริสีในข้อ 2
- Key decisions:
  - Ἰδοὺ → ดูเถิด — Per uW figs-metaphor: attention-getter 'Now listen.' Glossary-established 'ดูเถิด' for ἰδού; signals the older son demanding the father's attention to the grievance-argument about to unfold.
  - τοσαῦτα ἔτη δουλεύω σοι → ตลอดหลายปีมานี้ ข้าพเจ้าได้ปรนนิบัติท่านเหมือนทาส — Per uW figs-metaphor: δουλεύω 'I-slave-for-you' — the older son describes himself as a slave to emphasize how hard he has worked. Jesus-reader sees the irony (he is a son, not a slave; the self-demotion is self-accu...
  - οὐδέποτε ἐντολήν σου παρῆλθον → ไม่เคยขัดคำสั่งของท่านเลย — Per uW figs-doublenegatives + figs-hyperbole: 'never-violated-command' — uses double-negative + never-hyperbole. Could be rendered positively 'always obeyed' but preserved as negative for emphasis. Thai 'ไม่เคย...เล...
  - ἔριφον → ลูกแพะ...สักตัวหนึ่ง — Per uW figs-explicit: ἔριφος 'kid-goat' was much smaller/cheaper than a fatted-calf — the older son deliberately contrasts 'even a young goat' (minimal gift) with the calf the father killed for the younger son. 'ลูก...
- Notes: The older son's speech reveals his theological error: he frames his sonship as contractual slavery. 'I slave for you...and you never gave me even a kid-goat' — the logic of earned payment, not familial love. The Pharisees-in-the-parable mirror: religious rule-keeping experienced as slavery-for-reward rather than sonship-in-joy. The kid-vs-calf...

**Luke 15:30**
- GR: ὅτε δὲ ὁ υἱός σου οὗτος ὁ καταφαγών σου τὸν βίον μετὰ πορνῶν ἦλθεν,ἔθυσας αὐτῷ τὸν σιτευτὸν μόσχον.
- TH: แต่พอลูกคนนี้ของท่าน ผู้ที่ผลาญทรัพย์สินของท่านกับพวกหญิงแพศยากลับมา ท่านก็สั่งฆ่าลูกโคอ้วนให้เขา›
- TH-summary: บุตรคนโตปฏิเสธความเป็นพี่น้อง เขาเรียกน้องว่า «ลูกคนนี้ของท่าน» — ไม่ใช่ «น้องชายของข้าพเจ้า» (สังเกตว่าบิดาตอบในข้อ 32 ด้วยคำว่า «น้องคนนี้ของเจ้า» เพื่อคืนความสัมพันธ์พี่น้อง) นอกจากนี้ คำว่า «พวกหญิงแพศยา» เป็นการกล่าวหาที่บุตรคนโตแต่งเติมเอง — ข้อความเดิมในข้อ 13 กล่าวเพียงว่า «ใช้ชีวิตอย่างสุรุ่ยสุร่าย» โดยไม่ระบุว่ากับใคร
- Key decisions:
  - ὁ υἱός σου οὗτος → ลูกคนนี้ของท่าน — Per uW: the older son refers to his brother as 'this son of yours' — refuses to name him 'my brother' (pointed kinship-refusal). 'ลูกคนนี้ของท่าน' matches the distancing possessive + demonstrative. Thai reader-sensi...
  - ὁ καταφαγών σου τὸν βίον → ผู้ที่ผลาญทรัพย์สินของท่าน — Per uW figs-metaphor: κατεσθίω 'eat-down' = 'devour/consume' (aorist-participle 'the-one-having-consumed-your-wealth'). Metaphor of eating-up-wealth-until-nothing-left. 'ผลาญทรัพย์สิน' (squander-wealth) — same verb-...
  - μετὰ πορνῶν → กับพวกหญิงแพศยา — Per uW figs-synecdoche: πόρνη 'prostitute' — the older son's accusation. NOTE: the narrator in v.13 only said ἀσώτως (wastefully); 'with prostitutes' is the older son's interpretation, likely imaginary/unverifiable....
  - ἔθυσας αὐτῷ τὸν σιτευτὸν μόσχον → ท่านก็สั่งฆ่าลูกโคอ้วนให้เขา — Per uW figs-metonymy + figs-explicit: the father did not personally kill; he ordered it. Implicit purpose: 'to hold a celebration.' Thai 'สั่งฆ่า' (order-to-kill) matches the metonymic alternate; the celebration-pur...
- Notes: The older son's speech climaxes with two rhetorical moves: (1) refusal-of-kinship — 'this son of yours' instead of 'my brother'; (2) lurid-slander — 'with prostitutes,' an accusation the narrative has NOT established (v.13 said only ἀσώτως). The older son paints the darkest possible picture to maximize his grievance's moral weight. Per uW: the...

**Luke 15:31**
- GR: ὁ δὲ εἶπεν αὐτῷ·Τέκνον,σὺ πάντοτε μετ’ἐμοῦ εἶ,καὶ πάντα τὰ ἐμὰ σά ἐστιν·
- TH: บิดาจึงกล่าวแก่เขาว่า ‹ลูกเอ๋ย เจ้าอยู่กับเราเสมอมา และทุกสิ่งที่เป็นของเราก็เป็นของเจ้า
- Key decisions:
  - Τέκνον → ลูกเอ๋ย — Per uW: τέκνον here is term of affection ('My dear son/child'). Thai 'ลูกเอ๋ย' is established Lukan vocative for τέκνον (cf. Luke 2:48 Mary-to-Jesus, 16:25 Abraham-to-rich-man; comparable at 8:54). Non-distancing, w...
  - σὺ πάντοτε μετ’ ἐμοῦ εἶ → เจ้าอยู่กับเราเสมอมา — Per uW: 'I appreciate the way you have stayed here and helped me.' Emphatic σύ fronts the subject — YOU are the one always-with-me. πάντοτε 'always/at-all-times.' 'เจ้าอยู่กับเราเสมอมา' (you have always been with me...
  - πάντα τὰ ἐμὰ σά ἐστιν → ทุกสิ่งที่เป็นของเราก็เป็นของเจ้า — 'All mine is yours' — the double-portion inheritance already set aside in v.12 when βίος was divided 'to them' (αὐτοῖς). Legally, the older son has held his 2/3 throughout. Reassurance that nothing-of-his is taken-b...
- Notes: The father's response-clause-1 answers the older son's grievance with two claims: (1) constant-presence ('you are always with me' — a claim the older son cannot honestly refute); (2) unbroken-inheritance ('all mine is yours' — reminds him that the calf-for-brother has not cost him his 2/3 share). Cultural-legal footnote: after the division in ...

**Luke 15:32**
- GR: εὐφρανθῆναι δὲ καὶ χαρῆναι ἔδει,ὅτι ὁ ἀδελφός σου οὗτος νεκρὸς ἦν καὶ ἔζησεν,καὶ ἀπολωλὼς καὶ εὑρέθη.
- TH: แต่สมควรที่จะฉลองและยินดี เพราะน้องคนนี้ของเจ้าตายแล้วแต่กลับเป็นขึ้นมา เขาหายไปแล้วและพบอีก›»
- TH-summary: บิดาแก้ไขคำของบุตรคนโต — เขาเรียกน้องว่า «ลูกคนนี้ของท่าน» (ข้อ 30) บิดากลับเรียกว่า «น้องคนนี้ของเจ้า» คืนความสัมพันธ์พี่น้อง คำอุปมาจบแบบเปิด เราไม่ทราบว่าบุตรคนโตจะเข้าไปในงานเลี้ยงหรือไม่ — เป็นคำถามที่พระเยซูทิ้งไว้ให้พวกฟาริสีและธรรมาจารย์ตอบเอง (ข้อ 2)
- Key decisions:
  - εὐφρανθῆναι & καὶ χαρῆναι ἔδει → สมควรที่จะฉลองและยินดี — Per uW figs-hendiadys: 'celebrate and rejoice' expresses a single idea ('celebrate joyfully'). ἔδει imperfect of δεῖ 'it-was-necessary/fitting.' 'สมควรที่จะฉลองและยินดี' preserves both the moral-necessity and the pa...
  - ὁ ἀδελφός σου οὗτος → น้องคนนี้ของเจ้า — Per uW: the father's POINTED correction of the older son's 'this son of yours' (v.30). 'น้องคนนี้ของเจ้า' is the inverse-parallel to v.30's 'ลูกคนนี้ของท่าน' — the father reasserts the brotherhood-tie the older son ...
  - νεκρὸς ἦν καὶ ἔζησεν,καὶ ἀπολωλὼς καὶ εὑρέθη → ตายแล้วแต่กลับเป็นขึ้นมา เขาหายไปแล้วและพบอีก — Per uW figs-metaphor: 'See how you translated this figurative expression in v.24.' VERBATIM VERBAL ECHO of v.24 (dead/alive + lost/found) — Thai rendering matches v.24 exactly. Note slight Greek difference: v.24 use...
- Notes: Open ending. The parable terminates with the father's argument but not with the older son's response. We do not know if the older son goes in. This is deliberate: Jesus leaves the ending for the Pharisees-in-the-audience (v.2) to write with their own lives. Will they come in to the feast of God's welcoming sinners, or will they remain outside ...


---

### Luke 18

**Luke 18:1**
- GR: Ἔλεγεν δὲ παραβολὴν αὐτοῖς πρὸς τὸ δεῖν πάντοτε προσεύχεσθαι αὐτοὺς καὶ μὴ ἐγκακεῖν,
- TH: แล้วพระเยซูตรัสคำอุปมาเรื่องหนึ่งแก่พวกเขา เพื่อสอนว่าพวกเขาควรอธิษฐานอยู่เสมอและไม่ย่อท้อ
- Key decisions:
  - ἔλεγεν → พระเยซูตรัส — Imperfect 'was saying/kept saying' but in narrative introduction functions as simple past. Divine subject → ตรัส (royal register per RULES.md §3). Subject made explicit (พระเยซู) for clarity since the previous chapt...
  - ἐγκακεῖν → ไม่ย่อท้อ — ἐγκακέω 'lose heart / grow weary in doing' (6× NT; Luke's only use). Thai ย่อท้อ captures compound sense of losing spirit + giving up in prayer, standard Thai Christian register.
  - πρὸς τὸ δεῖν πάντοτε προσεύχεσθαι → เพื่อสอนว่าพวกเขาควรอธิษฐานอยู่เสมอ — πρὸς τὸ + articular-infinitive δεῖν 'in view of the necessity to...' — Luke's purpose-clause framing. Thai เพื่อสอนว่า...ควร captures the didactic purpose. πάντοτε 'always/continually' → อยู่เสมอ emphasizes persever...
- Notes: Luke 18 opens with its most distinctive structural feature — Luke alone among the Synoptics frames this parable with an explicit purpose-statement (πρὸς τὸ δεῖν). The framing verses 1 and 8 form an inclusio: the parable teaches persistent prayer, and v.8 asks whether the Son of Man will find such persevering faith on earth. ἐγκακέω picks up Pa...

**Luke 18:2**
- GR: λέγων·Κριτής τις ἦν ἔν τινι πόλει τὸν θεὸν μὴ φοβούμενος καὶ ἄνθρωπον μὴ ἐντρεπόμενος.
- TH: พระองค์ตรัสว่า «ในเมืองหนึ่ง มีผู้พิพากษาคนหนึ่งซึ่งไม่ยำเกรงพระเจ้าและไม่เกรงใจมนุษย์เลย
- Key decisions:
  - Κριτής → ผู้พิพากษา — κριτής in civil/legal-court sense → ผู้พิพากษา (consistent with LUK 12:14, 12:58 where Jesus uses κριτής in legal-court contexts). ผู้ตัดสิน reserved for non-court metaphorical judgment (LUK 11:19 exorcism context, ...
  - τὸν θεὸν μὴ φοβούμενος → ไม่ยำเกรงพระเจ้า — φοβέομαι of reverent fear toward God → ยำเกรง (glossary-established LUK 1:50, 12:5). Distinguished from φοβέομαι as fear-of-harm (กลัว).
  - ἄνθρωπον μὴ ἐντρεπόμενος → ไม่เกรงใจมนุษย์ — ἐντρέπω 'turn-toward, give-regard-to' → ไม่เกรงใจ captures 'having no regard for.' Per uW figs-gendernotations ἄνθρωπον is generic 'people' → มนุษย์ (Thai generic noun).
- Notes: Introduces the unjust-judge character. The double negative (neither God-fearing nor man-respecting) is a legal-character caricature of the worst-possible judge — no vertical accountability (θεόν) and no horizontal accountability (ἄνθρωπον). Jewish legal expectation (Deut 16:18-20; 2 Chr 19:6-7) was that a judge must fear God and respect the pa...

**Luke 18:3**
- GR: χήρα δὲ ἦν ἐν τῇ πόλει ἐκείνῃ καὶ ἤρχετο πρὸς αὐτὸν λέγουσα·Ἐκδίκησόν με ἀπὸ τοῦ ἀντιδίκου μου.
- TH: ในเมืองนั้นมีหญิงม่ายคนหนึ่ง นางมาหาเขาเรื่อย ๆ วิงวอนว่า ‹ขอโปรดให้ความยุติธรรมแก่ข้าพเจ้าต่อคู่ความของข้าพเจ้าเถิด›
- TH-summary: หญิงม่ายในสังคมศตวรรษที่หนึ่งไม่มีสามีปกป้องและไม่มีอำนาจในศาล จึงเป็นภาพของผู้อ่อนแอที่สุดซึ่งธรรมบัญญัติของโมเสสสั่งให้ปกป้อง (อพย 22:22; ฉธบ 10:18) ความเสียเปรียบของนางทำให้ความจำเป็นในการยืนหยัดต่อผู้พิพากษาที่ไม่ยำเกรงพระเจ้าเป็นภาพของคำอธิษฐานที่ไม่ย่อท้อของผู้เชื่อในโลกที่ไม่เป็นธรรม
- Key decisions:
  - χήρα → หญิงม่าย — χήρα → หญิงม่าย (glossary-established LUK 2:37, 4:25-26, 7:12, 20:47, 21:2-3, MRK 12:40-43, MAT 23:14).
  - ἤρχετο → มาหาเขาเรื่อย ๆ — Imperfect indicates repeated/continual action per uW note ('she kept coming'). Thai เรื่อย ๆ captures the iterative aspect crucial to the parable's point about persistence.
  - Ἐκδίκησόν με → ขอโปรดให้ความยุติธรรมแก่ข้าพเจ้า — ἐκδικέω aor-imp 2sg 'vindicate / give-justice-to' in legal context. Per uW figs-imperative: widow not in position to command, render as polite petition. Thai ขอโปรด + ข้าพเจ้า + ...เถิด triple-marks humility.
  - ἀντιδίκου → คู่ความ — ἀντίδικος = legal adversary / opposing-party-in-lawsuit. Per LUK 12:58 glossary-established คู่ความ (legal opponent in court proceedings). Preserves specifically-legal vs. general-enemy sense.
- Notes: Widow as paradigmatic vulnerable-plaintiff. Torah background: widows, orphans, and foreigners are the three categories protected by Mosaic law (Ex 22:22-24; Deut 10:18, 24:17-21; Isa 1:17). The judge's refusal to hear her case violates Torah (Deut 1:17 — judges must not favor the strong over the weak). ἤρχετο imperfect = kept coming — the repe...

**Luke 18:4**
- GR: καὶ οὐκ ἤθελεν ἐπὶ χρόνον,μετὰ ταῦτα δὲ εἶπεν ἐν ἑαυτῷ·Εἰ καὶ τὸν θεὸν οὐ φοβοῦμαι οὐδὲ ἄνθρωπον ἐντρέπομαι,
- TH: เขาไม่ยอมทำตามอยู่ชั่วระยะหนึ่ง แต่ภายหลังเขาคิดในใจว่า ‹แม้ข้าไม่ยำเกรงพระเจ้าและไม่เกรงใจมนุษย์ก็ตาม
- Key decisions:
  - οὐκ ἤθελεν ἐπὶ χρόνον → ไม่ยอมทำตามอยู่ชั่วระยะหนึ่ง — ἤθελεν imperfect 'was not willing' over an extended period. Thai ไม่ยอม + ชั่วระยะหนึ่ง captures sustained unwillingness.
  - εἶπεν ἐν ἑαυτῷ → คิดในใจว่า — Hebraism / Septuagintism 'said within himself' = internal deliberation. Thai คิดในใจ is the natural equivalent (cf. LUK 7:39 ὁ Φαρισαῖος... εἶπεν ἐν ἑαυτῷ).
  - Εἰ καὶ → แม้...ก็ตาม — Per uW grammar-connect-condition-fact: concessive not hypothetical — judge states real fact about himself. Thai แม้...ก็ตาม preserves concessive force.
- Notes: The judge's self-admission that he neither fears God nor respects people confirms v.2's narrator-characterization. Internal monologue structure mirrors LUK 12:17, 16:3 — a Lucan signature technique for revealing character-motive in parables.

**Luke 18:5**
- GR: διά γε τὸ παρέχειν μοι κόπον τὴν χήραν ταύτην ἐκδικήσω αὐτήν ἵνα μὴ εἰς τέλος ἐρχομένη ὑπωπιάζῃ με.
- TH: แต่เพราะหญิงม่ายผู้นี้รบกวนข้า ข้าจะให้ความยุติธรรมแก่นาง เพื่อนางจะไม่มากวนข้าอยู่ร่ำไปจนทำให้ข้าหมดแรง›»
- Key decisions:
  - τὸ παρέχειν μοι κόπον → รบกวนข้า — παρέχω + κόπος 'cause trouble / weariness to' (idiom). Thai รบกวน captures 'trouble/bother' register. Natural colloquial Thai without forcing lexical equivalence.
  - εἰς τέλος → อยู่ร่ำไป — Per uW figs-idiom: εἰς τέλος = 'perpetually / forever' (idiom). Thai อยู่ร่ำไป = 'continually/endlessly' matches the 'incessantly/forever' idiom.
  - ὑπωπιάζῃ με → ทำให้ข้าหมดแรง — Per uW figs-metaphor: ὑπωπιάζω (lit. 'strike under the eye' / give a black eye) used metaphorically 'wear out / beat down.' The literal pugilistic sense (boxing term — to bruise) is rare outside 1 Cor 9:27. Thai ทำใ...
  - ἐκδικήσω αὐτήν → ข้าจะให้ความยุติธรรมแก่นาง — ἐκδικέω fut-ind-1sg 'I will vindicate / give justice to.' Consistent with v.3's ἐκδίκησον rendering — 'ให้ความยุติธรรม' throughout vv.3, 5, 7, 8 for lemma consistency.
- Notes: Non-honorific register throughout judge's speech — ข้า (not ข้าพเจ้า) for self-reference, consistent with his own self-description as godless and disrespectful. ὑπωπιάζω is suggestively comedic — the powerful judge imagines the widow literally punching him in the face. Paul uses the same verb 1 Cor 9:27 of disciplining one's body. Hapax-adjace...

**Luke 18:6**
- GR: εἶπεν δὲ ὁ κύριος·Ἀκούσατε τί ὁ κριτὴς τῆς ἀδικίας λέγει·
- TH: แล้วองค์พระผู้เป็นเจ้าตรัสว่า «จงฟังคำที่ผู้พิพากษาอธรรมได้กล่าวนั้น
- Key decisions:
  - ὁ κύριος → องค์พระผู้เป็นเจ้า — Per uW note: Luke refers to Jesus as ὁ κύριος. Thai องค์พระผู้เป็นเจ้า (glossary-established from RULES.md §4 κύριος for divine title). Luke uses this absolute ὁ κύριος 24× of Jesus — a deliberate narrative confessi...
  - Ἀκούσατε → จงฟัง — Per uW figs-idiom: ἀκούω here = 'think about / reflect on' (not new report). But retained imperative as 'จงฟัง' since Thai จงฟังคำที่... naturally means 'consider what [he] said' in context.
  - ὁ κριτὴς τῆς ἀδικίας → ผู้พิพากษาอธรรม — Hebrew-style genitive of quality: 'judge of injustice' = unjust judge. ἀδικία → อธรรม (Thai compound 'non-righteousness'), more natural than literal 'ผู้พิพากษาของความไม่ชอบธรรม.' Standard Thai Christian rendering f...
- Notes: Jesus' transition from parable to application. The qal-vahomer (lesser-to-greater) argument: if even the unjust judge eventually acts, how much more will the righteous God answer his elect?

**Luke 18:7**
- GR: ὁ δὲ θεὸς οὐ μὴ ποιήσῃ τὴν ἐκδίκησιν τῶν ἐκλεκτῶν αὐτοῦ τῶν βοώντων αὐτῷ ἡμέρας καὶ νυκτός,καὶ μακροθυμεῖ ἐπ’αὐτοῖς;
- TH: แล้วพระเจ้าจะไม่ทรงให้ความยุติธรรมแก่ผู้ที่ทรงเลือกสรรไว้ของพระองค์ ซึ่งร้องทูลพระองค์ทั้งกลางวันและกลางคืนหรือ? พระองค์จะทรงผัดผ่อนต่อเขาทั้งหลายหรือ?
- TH-summary: «ผู้ที่ทรงเลือกสรร» หมายถึงประชากรของพระเจ้าที่พระองค์เรียกให้มาเป็นของพระองค์ ภาพของผู้ร้องทุกข์ «ทั้งกลางวันและกลางคืน» เป็นการเปรียบเทียบจากเพลงสดุดี (สดด 22:2; 88:1) ที่บรรยายถึงผู้ทุกข์ใจวิงวอนพระเจ้าอย่างต่อเนื่อง คำสอนคือพระเจ้าทรงฟังและจะทรงตอบ — แม้การตอบอาจช้าในสายตาของมนุษย์ แต่ในความเป็นจริงพระองค์มิได้ทรงเพิกเฉย
- Key decisions:
  - ὁ δὲ θεὸς οὐ μὴ ποιήσῃ τὴν ἐκδίκησιν → แล้วพระเจ้าจะไม่ทรงให้ความยุติธรรม...หรือ? — Per uW figs-rquestion: rhetorical question expecting 'yes, he certainly will.' Thai จะไม่...หรือ? preserves the expected-positive rhetorical form. ทรง-prefix on ทรงให้ for divine subject (RULES.md §3). ποιεῖν τὴν ἐκ...
  - τῶν ἐκλεκτῶν αὐτοῦ → ผู้ที่ทรงเลือกสรรไว้ของพระองค์ — ἐκλεκτός = chosen/elect — per LUK 9:35 ὁ ἐκλελεγμένος 'ผู้ที่เราทรงเลือกสรรไว้' (of the Son) and standard NT usage of 'the elect.' Per uW figs-nominaladj: adjective-as-noun → noun phrase ผู้ที่ทรงเลือกสรรไว้. NEW: ο...
  - βοώντων αὐτῷ ἡμέρας καὶ νυκτός → ร้องทูลพระองค์ทั้งกลางวันและกลางคืน — Per uW figs-merism: 'day and night' = all the time. Thai ทั้งกลางวันและกลางคืน preserves the merism idiom (Thai readers will understand the 'continuously' sense). βοάω pres-act-ptc 'cry out' → ร้องทูล (speech-act to...
  - καὶ μακροθυμεῖ ἐπ’αὐτοῖς → พระองค์จะทรงผัดผ่อนต่อเขาทั้งหลายหรือ? — Difficult crux. Per uW figs-idiom: καὶ may be idiomatic 'even if' OR continuation-of-rhetorical-question. Following BSB/ESV evangelical mainstream: render as second rhetorical question continuing the first (expectin...
- Notes: CONTESTED SYNTAX: καὶ μακροθυμεῖ ἐπ’ αὐτοῖς can be read as (a) continuing rhetorical question ('will he delay?' — BSB, ESV); (b) contrastive independent clause ('though he delays...' — NRSV); (c) concessive subordinate ('even if he takes long' — NIV). We follow (a) per BSB/evangelical-mainstream. The textual challenge is real — Greek syntax ad...

**Luke 18:8**
- GR: λέγω ὑμῖν ὅτι ποιήσει τὴν ἐκδίκησιν αὐτῶν ἐν τάχει.πλὴν ὁ υἱὸς τοῦ ἀνθρώπου ἐλθὼν ἆρα εὑρήσει τὴν πίστιν ἐπὶ τῆς γῆς;
- TH: เราบอกพวกท่านว่า พระองค์จะทรงให้ความยุติธรรมแก่เขาทั้งหลายโดยเร็ว แต่กระนั้น เมื่อบุตรมนุษย์เสด็จมา พระองค์จะพบความเชื่อบนแผ่นดินโลกหรือ?»
- TH-summary: คำถามสุดท้ายของคำอุปมาพลิกน้ำหนักจากพระเจ้าที่ซื่อสัตย์ไปสู่ความไม่แน่นอนของมนุษย์ — พระเจ้าจะทรงตอบอย่างแน่นอน แต่เมื่อบุตรมนุษย์เสด็จกลับมา จะทรงพบมนุษย์ที่ยังคงอธิษฐานด้วยความเชื่อต่อไปหรือไม่ ประเด็นคำถามไม่ได้อยู่ที่ความเชื่อถือได้ของพระเจ้า แต่อยู่ที่ความอดทนยืนหยัดของผู้เชื่อในช่วงที่พระองค์ดูเหมือนเงียบ
- Key decisions:
  - ἐν τάχει → โดยเร็ว — 'Swiftly / soon.' Per uW figs-explicit: apparent tension with the parable's 'persist-because-delay' theme; implication is God begins acting immediately even if results take time. Thai โดยเร็ว preserves the literal s...
  - πλὴν → แต่กระนั้น — πλήν adversative 'nevertheless/however' — Per uW figs-explicit: marks a turn from God's faithfulness to the human-side uncertainty. Thai แต่กระนั้น preserves the contrastive-pivot force.
  - ὁ υἱὸς τοῦ ἀνθρώπου → บุตรมนุษย์ — Son of Man title — glossary-established บุตรมนุษย์ (LUK 5:24, 6:5, 9:22, 9:26, 9:44, 9:58, 11:30, 12:8, 12:10, 12:40, 17:22, 17:24, 17:26, 17:30 + MRK/MAT corpus).
  - ἆρα εὑρήσει τὴν πίστιν → พระองค์จะพบความเชื่อ...หรือ? — Per uW figs-rquestion: ἆρα + question = anticipates negative answer ('will he, really?' implying doubt). Thai จะ...หรือ? preserves the dubious-rhetorical tone without forcing a negative English gloss.
- Notes: Parable's closing tension — God is faithful (certainly answers), but will humans be faithful? ἐν τάχει ('swiftly/soon') + the Son-of-Man return creates eschatological horizon. πίστις here is per uW figs-explicit = 'the persevering trust that keeps praying when answer delays' (contextual sense, connecting back to v.1's μὴ ἐγκακεῖν). This is the...

**Luke 18:9**
- GR: Εἶπεν δὲ καὶ πρός τινας τοὺς πεποιθότας ἐφ’ἑαυτοῖς ὅτι εἰσὶν δίκαιοι καὶ ἐξουθενοῦντας τοὺς λοιποὺς τὴν παραβολὴν ταύτην·
- TH: พระองค์ยังตรัสคำอุปมาเรื่องนี้แก่บางคนที่มั่นใจในตนเองว่าเป็นคนชอบธรรมและดูหมิ่นผู้อื่นว่า
- Key decisions:
  - πεποιθότας ἐφ’ἑαυτοῖς → มั่นใจในตนเอง — πείθω perf-act-ptc + ἐπί 'having put-trust in' → มั่นใจใน (established Thai 'confident-in / trust-in'). Reflexive ἑαυτοῖς → ตนเอง.
  - δίκαιοι → คนชอบธรรม — δίκαιος → ชอบธรรม (glossary-established, used throughout corpus).
  - ἐξουθενοῦντας τοὺς λοιποὺς → ดูหมิ่นผู้อื่น — ἐξουθενέω 'despise / treat with contempt' (11× NT). Thai ดูหมิ่น is the standard 'despise' verb, captures the social-contempt register. τοὺς λοιπούς = 'the rest / others' → ผู้อื่น.
- Notes: Per uW writing-participants: τινας introduces new unspecified addressees — likely Pharisees (the story's anti-model is a Pharisee). Luke positions this parable as pastoral correction rather than public teaching. ἐξουθενέω appears 6× in Luke-Acts (more than any other NT corpus) — Luke's signature word for social-religious contempt.

**Luke 18:10**
- GR: Ἄνθρωποι δύο ἀνέβησαν εἰς τὸ ἱερὸν προσεύξασθαι,ὁ εἷς Φαρισαῖος καὶ ὁ ἕτερος τελώνης.
- TH: «ชายสองคนขึ้นไปยังพระวิหารเพื่ออธิษฐาน คนหนึ่งเป็นฟาริสีและอีกคนหนึ่งเป็นคนเก็บภาษี
- Key decisions:
  - ἀνέβησαν εἰς τὸ ἱερὸν → ขึ้นไปยังพระวิหาร — Per uW figs-idiom: ἀναβαίνω of traveling to Jerusalem (elevation-idiom because city is on a mountain). Thai ขึ้นไปยัง preserves the up-going sense. ἱερόν here = temple-courtyard (per uW figs-synecdoche); Thai พระวิห...
  - Φαρισαῖος → ฟาริสี — Φαρισαῖος → ฟาริสี (glossary-established throughout corpus — MRK 2:16, MAT 3:7, LUK 5:17 etc.).
  - τελώνης → คนเก็บภาษี — τελώνης → คนเก็บภาษี (glossary-established Matt 5:46, MRK 2:15-16, LUK 3:12, 5:27-29 etc.).
- Notes: The parable's paired-opposition setup: Pharisee (religious-elite insider) vs. tax collector (socially-reviled Roman collaborator). Jewish expectation would have been that the Pharisee's prayer is heard and the tax collector's is not — the parable's inversion is the entire rhetorical payload.

**Luke 18:11**
- GR: ὁ Φαρισαῖος σταθεὶς πρὸς ἑαυτὸν ταῦτα προσηύχετο·Ὁ θεός,εὐχαριστῶ σοι ὅτι οὐκ εἰμὶ ὥσπερ οἱ λοιποὶ τῶν ἀνθρώπων,ἅρπαγες,ἄδικοι,μοιχοί,ἢ καὶ ὡς οὗτος ὁ τελώνης·
- TH: ฟาริสีผู้นั้นยืนขึ้นอธิษฐานในใจตนเองว่า ‹ข้าแต่พระเจ้า ข้าพระองค์ขอบพระคุณพระองค์ที่ข้าพระองค์ไม่เหมือนคนอื่น ๆ ซึ่งเป็นพวกฉ้อฉน ผู้อยุติธรรม คนเล่นชู้ หรือแม้แต่เหมือนคนเก็บภาษีผู้นี้
- TH-summary: คำอธิษฐานของฟาริสีเปิดเผยความผิดพลาดหลัก — เขา «ขอบพระคุณ» พระเจ้า แต่ใจทั้งหมดของคำอธิษฐานเป็นเรื่องของตนเองและการเปรียบเทียบกับผู้อื่น เขาอธิษฐาน «ในใจตนเอง» (πρὸς ἑαυτὸν) ซึ่งบ่งบอกว่าคำอธิษฐานนี้ไปไม่ถึงพระเจ้าจริง ๆ แต่เป็นเพียงการยกย่องตนเองโดยใช้ภาษาแห่งการอธิษฐาน
- Key decisions:
  - σταθεὶς πρὸς ἑαυτὸν → ยืนขึ้นอธิษฐานในใจตนเอง — Ambiguous syntax: πρὸς ἑαυτόν can modify σταθείς ('stood by himself') OR προσηύχετο ('prayed to himself / inwardly'). Most modern translators (including BSB, NIV) take the latter — praying to/about himself. Thai ในใ...
  - Ὁ θεός → ข้าแต่พระเจ้า — Vocative/nominative-for-vocative 'O God.' Thai ข้าแต่พระเจ้า is the standard Thai Christian prayer-opening.
  - εὐχαριστῶ σοι → ข้าพระองค์ขอบพระคุณพระองค์ — εὐχαριστέω pres-act-1sg 'I-give-thanks' — Thai ขอบพระคุณ + ข้าพระองค์/พระองค์ (highest humble register, human addressing God per RULES.md §3).
  - ἅρπαγες, ἄδικοι, μοιχοί → พวกฉ้อฉน ผู้อยุติธรรม คนเล่นชู้ — Three-term vice list. ἅρπαξ 'robber/extortioner' (per uW translate-unknown 'bandits') → ฉ้อฉน 'cheat/defraud.' ἄδικος 'unrighteous' → ผู้อยุติธรรม (non-righteous one). μοιχός 'adulterer' → คนเล่นชู้ (glossary-standa...
- Notes: The Pharisee's prayer structure — thanksgiving that masks self-praise — is ironic. Per uW note: πρὸς ἑαυτόν ambiguous ('stood by himself' vs 'prayed to/about himself'). Both readings converge on isolation theme. The vice-list (ἅρπαγες, ἄδικοι, μοιχοί) is not the standard Pauline type but a caricature-list — the Pharisee names the 'obvious sinn...

**Luke 18:12**
- GR: νηστεύω δὶς τοῦ σαββάτου,ἀποδεκατῶ πάντα ὅσα κτῶμαι.
- TH: ข้าพระองค์อดอาหารสัปดาห์ละสองวัน ข้าพระองค์ถวายสิบชักหนึ่งของทุกสิ่งที่ข้าพระองค์หามาได้›
- Key decisions:
  - νηστεύω δὶς τοῦ σαββάτου → ข้าพระองค์อดอาหารสัปดาห์ละสองวัน — σάββατον here = 'week' (common Semitism, cf. LUK 24:1 μία τῶν σαββάτων 'first day of the week'). Thai สัปดาห์ละสองวัน = 'two days per week.' The Pharisee's extra-Torah piety — Torah requires only Yom Kippur fasting;...
  - ἀποδεκατῶ → ถวายสิบชักหนึ่ง — ἀποδεκατόω 'pay tithes of' → ถวายสิบชักหนึ่ง (glossary-established LUK 11:42; MAT 23:23).
  - ὅσα κτῶμαι → ของทุกสิ่งที่ข้าพระองค์หามาได้ — κτάομαι 'acquire, gain, earn' → หามาได้ (natural Thai 'get/earn'). The boast extends beyond Torah requirement (tithing all income, not just the produce-categories Torah specifies).
- Notes: The Pharisee lists supererogatory practices (beyond-Torah piety): fasting twice weekly (not Torah-required) and tithing ALL income (Torah required tithing of produce, firstborn, firstfruits — not universal income). His prayer moves from negative 'I am not like...' to positive 'I do...' — both forms self-congratulatory. No OT-citation entry nee...

**Luke 18:13**
- GR: ὁ δὲ τελώνης μακρόθεν ἑστὼς οὐκ ἤθελεν οὐδὲ τοὺς ὀφθαλμοὺς ἐπᾶραι εἰς τὸν οὐρανόν,ἀλλ’ἔτυπτε τὸ στῆθος αὐτοῦ λέγων·Ὁ θεός,ἱλάσθητί μοι τῷ ἁμαρτωλῷ.
- TH: ส่วนคนเก็บภาษียืนอยู่ห่าง ๆ ไม่กล้าแม้แต่จะเงยหน้าขึ้นดูฟ้าสวรรค์ แต่ตีอกของตนแล้วกล่าวว่า ‹ข้าแต่พระเจ้า ขอทรงพระเมตตาต่อข้าพระองค์ผู้เป็นคนบาปด้วยเถิด›
- TH-summary: ท่าทางทั้งสามของคนเก็บภาษี — ยืนห่าง ๆ ไม่กล้าเงยหน้า และตีอก — เป็นสัญลักษณ์ของการถ่อมใจและการกลับใจในวัฒนธรรมยิวศตวรรษที่หนึ่ง การตีอกเป็นท่าทางของความเสียใจอย่างสุดซึ้งต่อบาปของตน คำอธิษฐานของเขา «ขอทรงพระเมตตาต่อข้าพระองค์ผู้เป็นคนบาป» ใช้คำเฉพาะที่หมายถึง «ทรงลบล้างบาป» ซึ่งเป็นคำของพิธีกรรมในพระวิหาร — เขาขอความรอดไม่ใช่จากความดีของตน แต่จากพระคุณของพระเจ้า
- Key decisions:
  - μακρόθεν ἑστὼς → ยืนอยู่ห่าง ๆ — Per uW translate-symaction: sign of humility — did not feel worthy to be near the Pharisee. Thai ยืนอยู่ห่าง ๆ captures the distanced-positioning.
  - οὐκ ἤθελεν οὐδὲ τοὺς ὀφθαλμοὺς ἐπᾶραι → ไม่กล้าแม้แต่จะเงยหน้าขึ้นดู — Per uW figs-idiom: 'lift up eyes' = 'look at.' Thai เงยหน้าขึ้นดู is the natural idiom for 'raise face to look up.' ἤθελεν + negation → ไม่กล้า (was not willing + humility-inflection).
  - ἔτυπτε τὸ στῆθος αὐτοῦ → ตีอกของตน — Per uW translate-symaction: physical expression of sorrow, demonstrating repentance/humility. Thai ตีอก is the established Thai idiom for this gesture (used in funeral/repentance contexts).
  - ἱλάσθητί μοι τῷ ἁμαρτωλῷ → ขอทรงพระเมตตาต่อข้าพระองค์ผู้เป็นคนบาปด้วยเถิด — ἱλάσκομαι aor-imp-pass 'be propitiated / show mercy (toward).' Significant lexical choice: not generic ἐλέησον (which the blind man later uses, v.38) but the temple-sacrifice-related term for propitiation/atonement ...
  - ἁμαρτωλῷ → คนบาป — ἁμαρτωλός → คนบาป (RULES.md §4 non-negotiable, glossary-established).
- Notes: Three symbolic actions (distance, downcast eyes, breast-beating) each mark humility/repentance in first-century Jewish culture. LEXICAL CRUX: ἱλάσθητι (from ἱλάσκομαι) is not the common ἐλέησον — it carries temple-atonement overtones ('be propitiated toward me'). This is the same word-family as ἱλαστήριον (Rom 3:25 mercy-seat), evoking the Day...

**Luke 18:14**
- GR: λέγω ὑμῖν,κατέβη οὗτος δεδικαιωμένος εἰς τὸν οἶκον αὐτοῦ παρ’ἐκεῖνον·ὅτι πᾶς ὁ ὑψῶν ἑαυτὸν ταπεινωθήσεται,ὁ δὲ ταπεινῶν ἑαυτὸν ὑψωθήσεται.
- TH: เราบอกพวกท่านว่า ชายผู้นี้กลับไปยังบ้านของตนโดยที่พระเจ้าทรงชำระเขาให้เป็นผู้ชอบธรรม ไม่ใช่ฟาริสีผู้นั้น เพราะทุกคนที่ยกตนเองขึ้นจะถูกทำให้ต่ำลง แต่คนที่ถ่อมตนลงจะได้รับการยกขึ้น»
- TH-summary: «ทรงชำระให้เป็นผู้ชอบธรรม» (ดิไคโอโอ) เป็นคำที่เปาโลใช้ในจดหมายของท่านเพื่ออธิบายพระคุณของพระเจ้า — การที่พระเจ้าทรงประกาศผู้ที่เชื่อให้เป็นผู้ไร้ข้อกล่าวหา ที่สำคัญคือคนเก็บภาษีไม่ได้ทำอะไรเลยเพื่อให้ชอบธรรม นอกจากยอมรับความผิดของตนและขอพระเมตตา นี่คือหลักการพื้นฐานของข่าวประเสริฐ: ความชอบธรรมเป็นของขวัญจากพระเจ้า ไม่ใช่รางวัลของการปฏิบัติ
- Key decisions:
  - κατέβη εἰς τὸν οἶκον αὐτοῦ → กลับไปยังบ้านของตน — Per uW figs-idiom: 'went down' = returned home from Jerusalem (descent-idiom because Jerusalem is on a mountain). Thai กลับไปยังบ้าน captures the return-home sense; the elevation aspect is implicit.
  - δεδικαιωμένος → โดยที่พระเจ้าทรงชำระเขาให้เป็นผู้ชอบธรรม — δικαιόω perf-pass-ptc 'having been declared-righteous.' Per uW figs-activepassive: divine passive — God is the implied agent. Thai makes this explicit: พระเจ้าทรงชำระ (God cleanses/justifies). This Pauline/Lukan key...
  - παρ’ἐκεῖνον → ไม่ใช่ฟาริสีผู้นั้น — παρά + acc in comparative sense = 'rather than / in contrast to.' ἐκεῖνος 'that one' (distant demonstrative) — refers back to the Pharisee. Per uW figs-explicit: implication is the Pharisee was NOT justified; Thai ไ...
  - ὑψῶν ἑαυτὸν ταπεινωθήσεται → ยกตนเองขึ้นจะถูกทำให้ต่ำลง — Per uW figs-metaphor + figs-activepassive: spatial metaphor for honor (high) vs humiliation (low); divine passive — God will humble/exalt. Thai ยกตนเองขึ้น vs ทำให้ต่ำลง preserves the vertical metaphor. ὑψωθήσεται →...
- Notes: CORE LUKAN THEOLOGY: The justification-by-humility principle echoes across Luke — cf. 1:52 (Magnificat), 14:11 (parable of chief seats). The reversal theme is Lukan signature. THEOLOGICAL KEY TERM: δικαιόω in passive here is one of only a handful of Lucan uses of this Pauline-central verb — Luke typically uses it of human self-justification (1...

**Luke 18:15**
- GR: Προσέφερον δὲ αὐτῷ καὶ τὰ βρέφη ἵνα αὐτῶν ἅπτηται·ἰδόντες δὲ οἱ μαθηταὶ ἐπετίμων αὐτοῖς.
- TH: ประชาชนยังนำทารกของตนมาเฝ้าพระองค์ เพื่อให้พระองค์ทรงสัมผัสเด็กเหล่านั้น แต่เมื่อเหล่าสาวกเห็นเช่นนั้นก็ตำหนิพวกเขา
- Key decisions:
  - τὰ βρέφη → ทารก — βρέφος → ทารก (glossary-established LUK 1:41,44 - in-utero; 2:12,16 - newborn Jesus; 1 Pet 2:2). Luke's specific choice of βρέφη (infants) rather than synoptic παιδία (children, MRK 10:13) emphasizes the very-young age.
  - ἅπτηται → ทรงสัมผัส — ἅπτω mid 'touch.' Per uW translate-symaction: touching babies conveys God's blessing. Thai ทรงสัมผัส (royal register for divine subject, RULES.md §3).
  - ἐπετίμων → ตำหนิ — ἐπιτιμάω impf 'rebuke, scold.' Per uW figs-explicit: disciples tried to stop the parents. Thai ตำหนิ (scold/reproach) captures the disciples' gatekeeping stance.
- Notes: PARALLEL: MRK 10:13-16 || MAT 19:13-15. Luke's βρέφη (babies/infants) is distinctive vs. Mark's παιδία (children). This specifies very young — emphasizing Luke's point about dependent helplessness as entry to kingdom. ἐπιτιμάω is the same verb used of rebuking demons (LUK 4:35,41, 9:42) — disciples apply demon-silencing authority to children, ...

**Luke 18:16**
- GR: ὁ δὲ Ἰησοῦς προσεκαλέσατο αὐτὰ λέγων·Ἄφετε τὰ παιδία ἔρχεσθαι πρός με καὶ μὴ κωλύετε αὐτά,τῶν γὰρ τοιούτων ἐστὶν ἡ βασιλεία τοῦ θεοῦ.
- TH: แต่พระเยซูทรงเรียกเด็กเหล่านั้นมาและตรัสว่า «จงยอมให้เด็กเล็ก ๆ มาหาเราเถิด อย่าห้ามพวกเขาเลย เพราะอาณาจักรของพระเจ้าเป็นของคนเช่นนี้แหละ
- Key decisions:
  - προσεκαλέσατο αὐτὰ → ทรงเรียกเด็กเหล่านั้นมา — προσκαλέομαι aor-mid 'call-to-oneself.' Per uW writing-pronouns: αὐτά refers to the children — but per the ambiguity, the calling may be addressed to the disciples (telling them to allow the children). Thai ทรงเรียก...
  - Ἄφετε τὰ παιδία → จงยอมให้เด็กเล็ก ๆ มาหาเราเถิด — ἀφίημι aor-imp 'permit/let.' Per uW figs-verbs: the first verb indicates one-time-action ('allow'), second indicates ongoing ('never forbid'). Thai จงยอมให้...มา preserves the permissive imperative.
  - τὰ παιδία → เด็กเล็ก ๆ — παιδίον diminutive 'little child' (distinct from v.15's βρέφος 'infant'). Thai เด็กเล็ก ๆ (reduplication for smallness/endearment). Jesus' generic term covers both babies (v.15) and older children.
  - τῶν γὰρ τοιούτων ἐστὶν ἡ βασιλεία τοῦ θεοῦ → เพราะอาณาจักรของพระเจ้าเป็นของคนเช่นนี้แหละ — βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า (RULES.md §4). τῶν τοιούτων 'of such-kind-ones' — per uW figs-simile: v.17 makes explicit this is simile ('whoever does not receive AS a child'). Thai คนเช่นนี้แหละ ('those-of-...
- Notes: PARALLEL: MRK 10:14 || MAT 19:14. Lexical shift within the episode: Luke uses βρέφη (v.15, infants) → παιδία (vv.16-17, children) — Jesus generalizes from babies to all children in the kingdom-saying. The kingdom belongs not to children per se but to those like-children in trust/dependence (made explicit v.17).

**Luke 18:17**
- GR: ἀμὴν λέγω ὑμῖν,ὃς ἂν μὴ δέξηται τὴν βασιλείαν τοῦ θεοῦ ὡς παιδίον,οὐ μὴ εἰσέλθῃ εἰς αὐτήν.
- TH: เราบอกความจริงแก่พวกท่านว่า ผู้ใดไม่รับอาณาจักรของพระเจ้าเหมือนอย่างเด็กเล็ก ๆ ผู้นั้นจะไม่มีวันเข้าในอาณาจักรนั้นเลย»
- TH-summary: การ «รับอาณาจักร» เหมือนเด็กไม่ได้หมายถึงไร้เดียงสา แต่หมายถึงท่าทีของการยอมรับของขวัญโดยไม่เรียกร้องสิทธิ์ เด็กในวัฒนธรรมปาเลสไตน์โบราณไม่มีอำนาจต่อรอง ไม่มีสถานะ และพึ่งพาผู้อื่นอย่างสิ้นเชิง — นี่คือท่าทีที่พระเยซูทรงสอนว่าเป็นประตูเข้าสู่อาณาจักรของพระเจ้า ซึ่งตรงกันข้ามกับความมั่นใจในตนเองของฟาริสีในคำอุปมาก่อนหน้า
- Key decisions:
  - ἀμὴν λέγω ὑμῖν → เราบอกความจริงแก่พวกท่านว่า — Jesus' solemn-asseveration formula. ἀμὴν 'truly' transliterated from Hebrew אָמֵן. Thai 'เราบอกความจริง' is glossary-established (LUK 4:24, 12:37, 18:29 etc.; MRK 10:15 parallel).
  - ὡς παιδίον → เหมือนอย่างเด็กเล็ก ๆ — Per uW figs-simile: the comparison can be drawn out explicitly (cf. LUK 18:17 UST 'with trust and humility as a child'). Thai เหมือนอย่างเด็กเล็ก ๆ preserves the simile without exegetical expansion (the point is mad...
  - οὐ μὴ εἰσέλθῃ → จะไม่มีวันเข้า...เลย — οὐ μή + aor-subj = emphatic future negation 'will certainly not.' Thai จะไม่มีวัน...เลย triple-marks the emphatic negation.
- Notes: PARALLEL: MRK 10:15. The kingdom-entry-as-reception principle flips the expected religious-achievement model (which the rich ruler in vv.18-23 will embody). Children receive without presuming to deserve — the same structure as the tax collector's reception (v.14).

**Luke 18:18**
- GR: Καὶ ἐπηρώτησέν τις αὐτὸν ἄρχων λέγων·Διδάσκαλε ἀγαθέ,τί ποιήσας ζωὴν αἰώνιον κληρονομήσω;
- TH: ขุนนางผู้หนึ่งทูลถามพระองค์ว่า «ท่านอาจารย์ผู้ประเสริฐ ข้าพเจ้าจะต้องทำสิ่งใดจึงจะได้รับชีวิตนิรันดร์เป็นมรดก?»
- TH-summary: คำถามของขุนนางคล้ายคำถามของผู้เชี่ยวชาญทางบัญญัติใน ลก 10:25 — แต่ขุนนางผู้นี้เป็นผู้ปกครองทางศาสนาในยิว ซึ่งมีอำนาจในการตัดสินศาสนา คำว่า «ได้รับเป็นมรดก» เป็นภาษาของพันธสัญญาเดิมเกี่ยวกับแผ่นดินคานาอัน (ฉธบ 1:38-39) — ขุนนางคิดว่าชีวิตนิรันดร์เป็นสิ่งที่ได้มาด้วยการกระทำ เช่นเดียวกับแผ่นดินคานาอันที่ได้มาโดยการสืบทอด
- Key decisions:
  - ἄρχων → ขุนนาง — ἄρχων 'ruler, chief' — here a Jewish leader per uW writing-participants. Thai ขุนนาง ('noble/aristocrat') captures the social rank without over-specifying as synagogue-ruler or Sanhedrin-member (the Greek leaves thi...
  - Διδάσκαλε ἀγαθέ → ท่านอาจารย์ผู้ประเสริฐ — Vocative address. Thai ท่านอาจารย์ (respectful teacher) + ผู้ประเสริฐ (excellent/good). Matches MRK 10:17 'ท่านอาจารย์ผู้ประเสริฐ.' ἀγαθός here carries the special sense the next verse will interrogate.
  - ζωὴν αἰώνιον κληρονομήσω → ได้รับชีวิตนิรันดร์เป็นมรดก — ζωὴ αἰώνιος → ชีวิตนิรันดร์ (glossary-established LUK 10:25). Per uW figs-metaphor: κληρονομέω 'inherit' used figuratively for 'obtain/acquire.' Thai ได้รับ...เป็นมรดก preserves the inheritance-language that carries...
- Notes: PARALLEL: MRK 10:17 || MAT 19:16. Luke alone calls him ἄρχων; Matthew calls him 'young,' Mark has no title — they likely harmonize to 'rich young ruler' in popular imagination. Connection to vv.15-17: immediately after teaching that the kingdom belongs to those who receive-like-children, Luke presents a ruler who assumes kingdom-entry is earne...

**Luke 18:19**
- GR: εἶπεν δὲ αὐτῷ ὁ Ἰησοῦς·Τί με λέγεις ἀγαθόν;οὐδεὶς ἀγαθὸς εἰ μὴ εἷς ὁ θεός.
- TH: พระเยซูตรัสกับเขาว่า «เหตุใดท่านจึงเรียกเราว่าผู้ประเสริฐ? ไม่มีใครประเสริฐเลย นอกจากพระเจ้าองค์เดียว
- TH-summary: พระเยซูทรงไม่ได้ปฏิเสธว่าพระองค์เป็นพระเจ้า แต่ทรงใช้คำถามให้ขุนนางได้คิดใหม่ว่าเขาใช้คำว่า «ประเสริฐ» อย่างไร ในพระคัมภีร์เดิม «ดี» คือคุณลักษณะเฉพาะของพระเจ้า (สดด 34:8; 118:1) — ถ้าขุนนางยอมรับว่าพระเยซูทรงเป็นผู้ประเสริฐจริง ๆ เขาต้องยอมรับว่าพระองค์ทรงเป็นมากกว่ามนุษย์
- Key decisions:
  - Τί με λέγεις ἀγαθόν → เหตุใดท่านจึงเรียกเราว่าผู้ประเสริฐ? — Per uW figs-rquestion: Jesus uses question-form as teaching tool — not denying his goodness but challenging the ruler's casual use of the term. Thai เหตุใด...จึง...? preserves the rhetorical-probing tone.
  - οὐδεὶς ἀγαθὸς εἰ μὴ εἷς ὁ θεός → ไม่มีใครประเสริฐเลย นอกจากพระเจ้าองค์เดียว — Absolute statement. εἷς 'one' here intensifies = 'God alone / one and only.' Thai พระเจ้าองค์เดียว captures the 'God alone' sense. ἀγαθός → ประเสริฐ (matches v.18's Διδάσκαλε ἀγαθέ).
- Notes: PARALLEL: MRK 10:18 || MAT 19:17 (MAT rephrases). The saying has two standard interpretive paths: (1) Jesus distances himself from the 'good' descriptor to redirect attention to God (humility); (2) Jesus is inviting the ruler to think through the implication — if Jesus is indeed 'good' and only God is good, therefore... The uW note explicitly ...

**Luke 18:20**
- GR: τὰς ἐντολὰς οἶδας·Μὴ μοιχεύσῃς,Μὴ φονεύσῃς,Μὴ κλέψῃς,Μὴ ψευδομαρτυρήσῃς,Τίμα τὸν πατέρα σου καὶ τὴν μητέρα.
- TH: ท่านรู้จักพระบัญญัติทั้งหลายอยู่แล้ว คือ ‹อย่าล่วงประเวณี อย่าฆ่าคน อย่าลักทรัพย์ อย่าเป็นพยานเท็จ จงให้เกียรติบิดาและมารดาของเจ้า›
- TH-summary: OT CITATION: พระเยซูทรงอ้างพระบัญญัติสิบประการ (อพย 20:12-16; ฉธบ 5:16-20) แต่ทรงยกเพียงครึ่งหลังที่เกี่ยวข้องกับความสัมพันธ์ระหว่างมนุษย์ — ไม่ใช่ครึ่งแรกที่เกี่ยวกับการนับถือพระเจ้า น่าสังเกตคือลำดับของพระเยซูต่างจากฉบับฮีบรูเล็กน้อย (ล่วงประเวณีมาก่อนฆ่าคน) ซึ่งตรงกับฉบับ LXX ในบางต้นฉบับ และพระองค์ไม่ได้ยกข้อ «อย่าโลภ» — เรื่องที่จะกลายเป็นหัวใจของการสนทนาต่อไป
- Key decisions:
  - τὰς ἐντολὰς → พระบัญญัติทั้งหลาย — ἐντολή → พระบัญญัติ (glossary-established for Decalogue/Torah commandments; the พระ-prefix marks divine origin).
  - Μὴ μοιχεύσῃς → อย่าล่วงประเวณี — μοιχεύω → ล่วงประเวณี (glossary-established MRK 10:19, MAT 19:18 — Thai Christian standard for 'commit adultery' in Decalogue context).
  - Μὴ φονεύσῃς → อย่าฆ่าคน — φονεύω → ฆ่าคน (glossary-established MRK 10:19, MAT 19:18, MAT 5:21).
  - Μὴ κλέψῃς → อย่าลักทรัพย์ — κλέπτω → ลักทรัพย์ (glossary-established MRK 10:19, MAT 19:18).
  - Μὴ ψευδομαρτυρήσῃς → อย่าเป็นพยานเท็จ — ψευδομαρτυρέω → เป็นพยานเท็จ (glossary-established MRK 10:19, MAT 19:18).
  - Τίμα τὸν πατέρα σου καὶ τὴν μητέρα → จงให้เกียรติบิดาและมารดาของเจ้า — τιμάω → ให้เกียรติ (glossary-established MRK 10:19 and MAT 15:4 for parent-honor context). σου singular per uW figs-youcrowd — preserve singular เจ้า since Moses addressed Israelites individually.
- Notes: OT CITATION: Exodus 20:12-16 || Deuteronomy 5:16-20 — the second-table Decalogue (human-horizontal commandments). Significant selection: Jesus quotes only the second table (commandments 6-9 + commandment 5 at the end), omitting the first-table commandments about God-relationship AND crucially omitting commandment 10 (οὐκ ἐπιθυμήσεις — 'do not ...

**Luke 18:21**
- GR: ὁ δὲ εἶπεν·Ταῦτα πάντα ἐφύλαξα ἐκ νεότητος μου.
- TH: แต่เขาทูลว่า «ทั้งหมดนี้ข้าพเจ้าได้ถือรักษามาตั้งแต่เยาว์วัย»
- Key decisions:
  - ἐφύλαξα → ได้ถือรักษา — φυλάσσω aor 'keep, guard, observe (laws).' Thai ถือรักษา (hold+maintain) is the standard Thai Christian rendering for law-keeping (matches MRK 10:20 'ได้ถือรักษา').
  - ἐκ νεότητος μου → ตั้งแต่เยาว์วัย — νεότης 'youth' — Per uW figs-abstractnouns: abstract-noun renderable as adjective. Thai เยาว์วัย (classical/formal register for 'young age') matches the ruler's formal self-presentation.
- Notes: The ruler's self-assessment is confident but partial — as Jesus' selection of commandments in v.20 implied, he's being tested only on the second-table Decalogue. His confidence about keeping these since youth sets up the trap Jesus will spring in v.22.

**Luke 18:22**
- GR: ἀκούσας δὲ ὁ Ἰησοῦς εἶπεν αὐτῷ·Ἔτι ἕν σοι λείπει·πάντα ὅσα ἔχεις πώλησον καὶ διάδος πτωχοῖς,καὶ ἕξεις θησαυρὸν ἐν οὐρανοῖς,καὶ δεῦρο ἀκολούθει μοι.
- TH: เมื่อพระเยซูทรงได้ยินเช่นนั้น ตรัสกับเขาว่า «ท่านยังขาดสิ่งหนึ่ง จงไปขายทุกสิ่งที่ท่านมีและแจกจ่ายแก่คนยากจน แล้วท่านจะมีทรัพย์สมบัติในสวรรค์ จากนั้นจงมาติดตามเรา»
- Key decisions:
  - Ἔτι ἕν σοι λείπει → ท่านยังขาดสิ่งหนึ่ง — λείπω pres 'lack, be missing.' Thai ยังขาด + สิ่งหนึ่ง preserves the 'still missing one thing' force. Matches MRK 10:21 'ท่านยังขาดอยู่สิ่งหนึ่ง.'
  - πάντα ὅσα ἔχεις πώλησον → จงไปขายทุกสิ่งที่ท่านมี — πωλέω aor-imp 'sell.' πάντα ὅσα ἔχεις 'all-that you-have' → ทุกสิ่งที่ท่านมี. Matches MRK 10:21 'จงไปขายทุกสิ่งที่ท่านมี' exactly for synoptic consistency.
  - διάδος πτωχοῖς → แจกจ่ายแก่คนยากจน — διαδίδωμι aor-imp 'distribute.' πτωχός → คนยากจน (glossary-established LUK 4:18, 6:20, 14:13, 21:3, MRK 10:21 pattern).
  - θησαυρὸν ἐν οὐρανοῖς → ทรัพย์สมบัติในสวรรค์ — θησαυρός → ทรัพย์สมบัติ (glossary-established LUK 12:33, 12:34; matches MRK 10:21 'ทรัพย์สมบัติในสวรรค์'). The plural οὐρανοῖς is Semitic idiom → singular สวรรค์ in Thai.
  - δεῦρο ἀκολούθει μοι → จงมาติดตามเรา — Per uW figs-metaphor: ἀκολουθέω of discipleship 'follow as disciple' (LUK 5:27 precedent). Thai จงมาติดตามเรา — discipleship-call formula throughout corpus.
- Notes: PARALLEL: MRK 10:21 || MAT 19:21. Mark adds ἠγάπησεν αὐτόν ('he loved him') which Luke and Matthew both omit — Luke's version is spare/direct. The call has three parts: (1) divest (sell+give), (2) invest (heavenly treasure), (3) apprentice (follow). The sequence is theological — discipleship is preceded by de-possession.

**Luke 18:23**
- GR: ὁ δὲ ἀκούσας ταῦτα περίλυπος ἐγενήθη,ἦν γὰρ πλούσιος σφόδρα.
- TH: แต่เมื่อเขาได้ยินเช่นนั้น ก็เป็นทุกข์อย่างยิ่ง เพราะเขาเป็นคนมั่งมีมาก
- Key decisions:
  - περίλυπος ἐγενήθη → เป็นทุกข์อย่างยิ่ง — περίλυπος 'very-sorrowful' (compound περί + λύπη intensifying). Thai เป็นทุกข์อย่างยิ่ง captures 'deeply-sorrowful.' Same word used of Jesus at Gethsemane (MRK 14:34 / MAT 26:38) — the intensity matters.
  - πλούσιος σφόδρα → คนมั่งมีมาก — πλούσιος → คนมั่งมี (glossary-established LUK 6:24, 16:1, 16:19, 21:1; matches MRK 10:22 'ทรัพย์สมบัติมากมาย' pattern but Luke uses πλούσιος adjective). σφόδρα 'exceedingly' → มาก.
- Notes: Luke's ἐγενήθη (became) vs MRK's aorist-middle ἀπῆλθεν λυπούμενος ('went away grieving') + MAT's aorist-pass ἀπῆλθεν λυπούμενος. Luke is unique in that he doesn't explicitly say the ruler 'went away' — leaving the scene unfinished. This is a Lukan signature — the ruler's response is paused mid-sadness, and Jesus' commentary to the disciples (v...

**Luke 18:24**
- GR: Ἰδὼν δὲ αὐτὸν ὁ Ἰησοῦς εἶπεν·Πῶς δυσκόλως οἱ τὰ χρήματα ἔχοντες εἰς τὴν βασιλείαν τοῦ θεοῦ εἰσπορεύονται·
- TH: พระเยซูทอดพระเนตรเห็นเขาแล้วตรัสว่า «คนที่มีทรัพย์สมบัติจะเข้าในอาณาจักรของพระเจ้ายากเย็นเพียงใด!
- Key decisions:
  - Ἰδὼν δὲ αὐτὸν ὁ Ἰησοῦς → พระเยซูทอดพระเนตรเห็นเขา — TEXTUAL VARIANT: Per uW translate-textvariants: many manuscripts add περίλυπον γενόμενον ('having-become-sad') here → 'seeing him having become sad.' SBLGNT omits (following א B L). BSB 'Seeing the man's sadness' tr...
  - Πῶς δυσκόλως ... εἰσπορεύονται → จะเข้า...ยากเย็นเพียงใด! — Per uW figs-exclamations: πῶς δυσκόλως = exclamation not question ('how-difficultly!'). Thai ยากเย็นเพียงใด! preserves the exclamatory intensity. Matches MRK 10:23 style.
  - οἱ τὰ χρήματα ἔχοντες → คนที่มีทรัพย์สมบัติ — χρήματα 'money/possessions/wealth' (plural substantive). Thai ทรัพย์สมบัติ consistent with v.22 θησαυρόν rendering and with MRK 10:23 'คนมั่งมี' pattern.
- Notes: TEXTUAL VARIANT: SBLGNT omits περίλυπον γενόμενον (Byz/some Alex add); we follow SBLGNT. This is not a translation-meaning-affecting variant (the sadness is already in v.23) but worth flagging. PARALLEL: MRK 10:23 || MAT 19:23. Jesus' commentary picks up the earlier reversal-principle (v.14) in concrete form: wealth creates entry-barrier to ki...

**Luke 18:25**
- GR: εὐκοπώτερον γάρ ἐστιν κάμηλον διὰ τρήματος βελόνης εἰσελθεῖν ἢ πλούσιον εἰς τὴν βασιλείαν τοῦ θεοῦ εἰσελθεῖν.
- TH: เพราะอูฐลอดรูเข็มก็ยังง่ายกว่าที่คนมั่งมีจะเข้าในอาณาจักรของพระเจ้า»
- TH-summary: คำพูดนี้เป็นการพูดเกินจริง (ไฮเปอร์โบเล) ในรูปแบบของแรบไบ เพื่อเน้นความเป็นไปไม่ได้อย่างสิ้นเชิง ไม่ใช่คำอธิบายเกี่ยวกับประตูเล็กในกรุงเยรูซาเล็มที่เรียกว่า «ประตูเข็ม» (นั่นเป็นเรื่องเล่าที่สร้างขึ้นในยุคกลาง ไม่มีหลักฐานในศตวรรษที่หนึ่ง) ประเด็นคือ: ด้วยตัวของคนรวยเอง การเข้าอาณาจักรพระเจ้าเป็นไปไม่ได้ — เหมือนอูฐลอดรูเข็มจริง ๆ
- Key decisions:
  - κάμηλον → อูฐ — κάμηλος → อูฐ (glossary-established MRK 10:25, MAT 19:24, MAT 23:24; camel hyperbole-image). Per uW translate-unknown: if audience unfamiliar, substitute large-beast-of-burden — but Thai readers know อูฐ.
  - τρήματος βελόνης → รูเข็ม — HAPAX-DOUBLE: τρῆμα (NT hapax, Luke only) + βελόνη (NT hapax — Luke's medical term; MRK/MAT use rarer ῥαφίς). Thai รูเข็ม ('hole of needle') glossary-established MRK 10:25, MAT 19:24. The hapax doubling is Luke's di...
  - εὐκοπώτερον γάρ ἐστιν → เพราะ...ก็ยังง่ายกว่า — εὐκοπώτερον comparative of εὔκοπος 'easy.' Per uW figs-hyperbole: extreme comparison. Thai ก็ยังง่ายกว่า preserves the comparative hyperbole.
- Notes: HAPAX-DOUBLE: τρῆμα + βελόνη are both NT-hapax, specific to Luke's version. τρῆμα 'hole/perforation' from τιτράω 'to bore.' βελόνη 'needle' = medical/surgical-needle (Luke's physician vocabulary) vs MRK/MAT ῥαφίς 'sewing-needle.' PARALLEL: MRK 10:25 || MAT 19:24. The medieval 'Needle Gate in Jerusalem' etymology (a small gate camels must stoop...

**Luke 18:26**
- GR: Εἶπαν δὲ οἱ ἀκούσαντες·Καὶ τίς δύναται σωθῆναι;
- TH: ผู้ที่ได้ยินจึงถามว่า «ถ้าเช่นนั้น ใครจะรอดได้?»
- Key decisions:
  - Καὶ τίς δύναται σωθῆναι → ถ้าเช่นนั้น ใครจะรอดได้? — Per uW figs-rquestion: likely rhetorical-exclamation expressing surprise rather than genuine question. Thai ถ้าเช่นนั้น...? captures the 'in-that-case-who-possibly?' force. Matches MRK 10:26 'ถ้าเช่นนั้นใครจะรอดได้....
- Notes: PARALLEL: MRK 10:26 || MAT 19:25. The disciples' surprise reflects the Jewish cultural assumption that wealth = divine blessing (Deut 28). If even the blessed-rich can't enter, who can? — the question exposes the works-based framework that Jesus is dismantling.

**Luke 18:27**
- GR: ὁ δὲ εἶπεν·Τὰ ἀδύνατα παρὰ ἀνθρώποις δυνατὰ παρὰ τῷ θεῷ ἐστιν.
- TH: พระองค์ตรัสว่า «สิ่งที่เป็นไปไม่ได้สำหรับมนุษย์นั้น เป็นไปได้สำหรับพระเจ้า»
- TH-summary: พระเยซูทรงสรุปว่าความรอดไม่ใช่ผลของความพยายามของมนุษย์ — ไม่ว่าจะเป็นการรักษาพระบัญญัติ การบริจาค หรือการถวายตัว ความรอดเป็นพระราชกิจของพระเจ้าเพียงผู้เดียว การที่คนมั่งมีจะละทิ้งทรัพย์สมบัติและเข้าอาณาจักรเป็นเรื่องเป็นไปไม่ได้หากพิจารณาจากธรรมชาติมนุษย์ แต่เมื่อพระเจ้าทรงทำงานในใจของผู้คน สิ่งที่ดูเป็นไปไม่ได้ก็เกิดขึ้นได้
- Key decisions:
  - Τὰ ἀδύνατα παρὰ ἀνθρώποις → สิ่งที่เป็นไปไม่ได้สำหรับมนุษย์ — Per uW figs-nominaladj: ἀδύνατα 'impossible-things' (neuter plural substantive). Thai สิ่งที่เป็นไปไม่ได้ preserves the substantive-adjectival force. παρά + dat 'with/for/in the view of' → สำหรับ.
  - δυνατὰ παρὰ τῷ θεῷ → เป็นไปได้สำหรับพระเจ้า — Parallel structure to first clause. Thai maintains parallelism. Matches MRK 10:27 'เป็นไปได้สำหรับพระเจ้า' pattern.
- Notes: PARALLEL: MRK 10:27 || MAT 19:26. The aphorism connects back to the Annunciation (LUK 1:37 'οὐκ ἀδυνατήσει παρὰ τοῦ θεοῦ πᾶν ῥῆμα' — nothing will be impossible with God). Luke's theological inclusio: what God did at Incarnation (impossible-virgin-birth) he does at salvation (impossible-rich-entering-kingdom). OT background possibly: Gen 18:14 ...

**Luke 18:28**
- GR: Εἶπεν δὲ ὁ Πέτρος·Ἰδοὺ ἡμεῖς ἀφέντες τὰ ἴδια ἠκολουθήσαμέν σοι.
- TH: เปโตรทูลว่า «ดูเถิด พวกข้าพระองค์ได้ละทิ้งสิ่งของของตนและได้ติดตามพระองค์»
- Key decisions:
  - Ἰδοὺ → ดูเถิด — Per uW figs-metaphor: ἰδού 'behold!' attention-getter. Thai ดูเถิด (glossary-standard for ἰδού).
  - ἡμεῖς ἀφέντες τὰ ἴδια → พวกข้าพระองค์ได้ละทิ้งสิ่งของของตน — TEXTUAL VARIANT: SBLGNT/NA28 read τὰ ἴδια ('one's own [things]'); Byzantine/TR read πάντα ('everything') — ULT follows the πάντα reading with footnote. BSB renders 'all we had' (reading-ambiguous, but defensible for...
  - ἠκολουθήσαμέν σοι → ได้ติดตามพระองค์ — Per uW figs-metaphor: follow = become disciple. Thai ได้ติดตามพระองค์ (glossary-standard for ἀκολουθέω-as-discipleship).
- Notes: PARALLEL: MRK 10:28 || MAT 19:27. TEXTUAL VARIANT: SBLGNT τὰ ἴδια vs Byz πάντα. We follow SBLGNT/NA28 shorter reading. The difference is theological-pragmatic: τὰ ἴδια ('our own') emphasizes that they left what was theirs — personally and individually — while πάντα ('everything') is more absolute. Both preserve the sacrificial-abandonment poin...

**Luke 18:29**
- GR: ὁ δὲ εἶπεν αὐτοῖς·Ἀμὴν λέγω ὑμῖν ὅτι οὐδείς ἐστιν ὃς ἀφῆκεν οἰκίαν ἢ γυναῖκα ἢ ἀδελφοὺς ἢ γονεῖς ἢ τέκνα ἕνεκεν τῆς βασιλείας τοῦ θεοῦ,
- TH: พระองค์ตรัสกับพวกเขาว่า «เราบอกความจริงแก่พวกท่านว่า ไม่มีผู้ใดที่ได้ละทิ้งบ้านเรือน ภรรยา พี่น้อง บิดามารดา หรือบุตร เพราะเห็นแก่อาณาจักรของพระเจ้า
- Key decisions:
  - οὐδείς ἐστιν ὃς ἀφῆκεν → ไม่มีผู้ใดที่ได้ละทิ้ง — Per uW figs-doublenegatives: double-negative statement spanning v.29-30. We render in Thai as negative + positive-conclusion form (ไม่มี ... ที่จะไม่ได้รับ = 'there is no one ... who will not receive'), preserving t...
  - οἰκίαν ἢ γυναῖκα ἢ ἀδελφοὺς ἢ γονεῖς ἢ τέκνα → บ้านเรือน ภรรยา พี่น้อง บิดามารดา หรือบุตร — List of abandoned attachments. Luke's list distinctive: includes γυναῖκα (wife, absent in MRK 10:29, MAT 19:29) + γονεῖς 'parents' (MRK/MAT split to πατέρα/μητέρα). Thai preserves the exact Lucan list. Note: Matt 19...
  - ἕνεκεν τῆς βασιλείας τοῦ θεοῦ → เพราะเห็นแก่อาณาจักรของพระเจ้า — ἕνεκεν + gen 'for the sake of.' Luke: 'kingdom of God' motive; MRK: 'for my-sake and the gospel's' (MRK 10:29); MAT: 'for my name's sake' (MAT 19:29). Each evangelist's phrasing marks their Christology. Thai เพราะเห...
- Notes: PARALLEL: MRK 10:29 || MAT 19:29. Luke's list-variations: (a) includes γυναῖκα (wife) uniquely — controversial; some harmonize with 1 Cor 9:5's 'right to take along a sister-wife'; others read it as Luke's emphasis on discipleship-overriding-marriage (cf. LUK 14:26); (b) uses γονεῖς (parents) compressed. Luke's 'kingdom of God' motivation vs M...

**Luke 18:30**
- GR: ὃς οὐχὶ μὴ ἀπολάβῃ πολλαπλασίονα ἐν τῷ καιρῷ τούτῳ καὶ ἐν τῷ αἰῶνι τῷ ἐρχομένῳ ζωὴν αἰώνιον.
- TH: ที่จะไม่ได้รับมากหลายเท่าในยุคนี้ และในยุคที่จะมาถึงจะได้รับชีวิตนิรันดร์»
- TH-summary: คำสอนของพระเยซูเกี่ยวกับรางวัลของผู้ติดตามพระองค์นำเสนอสองมิติ — «ยุคนี้» (ปัจจุบัน) และ «ยุคที่จะมาถึง» (อนาคต) เมื่อพระเจ้าทรงครอบครอง การได้รับ «มากหลายเท่า» ในยุคนี้หมายถึงการมีครอบครัวฝ่ายจิตวิญญาณ — ชุมชนของผู้เชื่อที่เข้ามาแทนครอบครัวทางเนื้อหนังที่ละทิ้ง ไม่ใช่ทรัพย์สมบัติเนื้อหนังที่เพิ่มพูนขึ้น
- Key decisions:
  - ὃς οὐχὶ μὴ ἀπολάβῃ → ที่จะไม่ได้รับ — Per uW figs-doublenegatives: completion of the double-negative from v.29. οὐχὶ μή + aor-subj emphatic-negation — but the whole sentence (v.29 negative + v.30 negative) yields positive meaning ('everyone who leaves ....
  - πολλαπλασίονα → มากหลายเท่า — HAPAX: πολλαπλασίων (NT-hapax, Luke only) 'many-times-over / manifold.' MRK 10:30 uses ἑκατονταπλασίονα ('hundredfold'), MAT 19:29 uses πολλαπλασίονα (also, some manuscripts ἑκατονταπλασίονα). Luke's word is the les...
  - ἐν τῷ καιρῷ τούτῳ ... ἐν τῷ αἰῶνι τῷ ἐρχομένῳ → ในยุคนี้ ... ในยุคที่จะมาถึง — Per uW figs-metonymy: both καιρός and αἰών here = 'age / world-period.' Thai ยุค covers both without over-distinguishing. The two-ages scheme is classic Jewish apocalyptic (העוֹלָם הַזֶּה vs הָעוֹלָם הַבָּא).
  - ζωὴν αἰώνιον → ชีวิตนิรันดร์ — ζωὴ αἰώνιος → ชีวิตนิรันดร์ (glossary-established, matches v.18's rendering).
- Notes: HAPAX: πολλαπλασίων is NT-hapax (only here). PARALLEL: MRK 10:30 || MAT 19:29. Luke's πολλαπλασίων 'manifold' avoids MRK's specific ἑκατονταπλασίονα 'hundredfold' — softer, less specific. MRK 10:30 unique mention of 'with persecutions' (Luke/Matt omit). Two-ages scheme: καιρός τούτος / αἰὼν ὁ ἐρχόμενος (cf. LUK 16:8 discussion of αἰών; LUK 20:...

**Luke 18:31**
- GR: Παραλαβὼν δὲ τοὺς δώδεκα εἶπεν πρὸς αὐτούς·Ἰδοὺ ἀναβαίνομεν εἰς Ἰερουσαλήμ,καὶ τελεσθήσεται πάντα τὰ γεγραμμένα διὰ τῶν προφητῶν τῷ υἱῷ τοῦ ἀνθρώπου·
- TH: พระเยซูทรงนำสาวกทั้งสิบสองไปข้างเดียวและตรัสกับพวกเขาว่า «ดูเถิด พวกเรากำลังขึ้นไปยังกรุงเยรูซาเล็ม และทุกสิ่งที่พวกผู้เผยพระวจนะได้เขียนเกี่ยวกับบุตรมนุษย์จะสำเร็จ
- TH-summary: นี่คือคำทำนายความทุกข์ทรมานครั้งที่สามของพระเยซู (ดู ลก 9:22; 9:44) แต่ครั้งนี้ชัดเจนและรายละเอียดที่สุด พระองค์ทรงเน้นว่าความตายของพระองค์ไม่ใช่เหตุการณ์ที่บังเอิญ แต่เป็นการสำเร็จของคำทำนายในพันธสัญญาเดิม (เช่น อสย 53; สดด 22; เศค 12:10) กรุงเยรูซาเล็มกลายเป็นเป้าหมายของการเดินทางยาวของพระองค์จาก ลก 9:51
- Key decisions:
  - Παραλαβὼν τοὺς δώδεκα → ทรงนำสาวกทั้งสิบสองไปข้างเดียว — παραλαμβάνω 'take aside.' Per uW alt-translation: 'took to a place away from other people where they would be alone.' τοὺς δώδεκα = the-Twelve — Per uW figs-nominaladj: substantive-adjective for apostolic group. Tha...
  - Ἰδοὺ ἀναβαίνομεν εἰς Ἰερουσαλήμ → ดูเถิด พวกเรากำลังขึ้นไปยังกรุงเยรูซาเล็ม — ἀναβαίνω 'go up' — elevation idiom (Jerusalem is on mountain). Ἰερουσαλήμ → กรุงเยรูซาเล็ม (glossary-established). The ἀναβαίνομεν (present-indicative 1pl) marks the imminent arrival — Luke's travel narrative climax.
  - τελεσθήσεται πάντα τὰ γεγραμμένα διὰ τῶν προφητῶν → ทุกสิ่งที่พวกผู้เผยพระวจนะได้เขียน ... จะสำเร็จ — Per uW figs-activepassive: both passives (τελεσθήσεται + γεγραμμένα). τελέω fut-pass 'be-fulfilled/completed.' Thai สำเร็จ standard for prophetic-fulfillment. προφήτης → ผู้เผยพระวจนะ (glossary-established). γέγραπτ...
- Notes: THIRD PASSION PREDICTION (Luke): following LUK 9:22 (first, general) and LUK 9:44 (second, brief), now the most detailed. Luke 9:51 began the travel narrative to Jerusalem; here, at ch.18, the destination becomes explicit and imminent. PROPHETIC FULFILLMENT: 'everything written by the prophets' — OT texts typically invoked: Isa 53 (suffering s...

**Luke 18:32**
- GR: παραδοθήσεται γὰρ τοῖς ἔθνεσιν καὶ ἐμπαιχθήσεται καὶ ὑβρισθήσεται καὶ ἐμπτυσθήσεται,
- TH: เพราะพระองค์จะทรงถูกมอบไว้กับคนต่างชาติ จะถูกเยาะเย้ย ถูกดูหมิ่น และถูกถ่มน้ำลายรด
- Key decisions:
  - παραδοθήσεται τοῖς ἔθνεσιν → จะทรงถูกมอบไว้กับคนต่างชาติ — Per uW figs-activepassive: passive of παραδίδωμι 'hand over / deliver over' — established LUK 9:44 'จะต้องถูกมอบไว้ในมือมนุษย์' pattern. Per uW figs-metonymy: ἔθνεσιν = Roman authorities (Gentile court). Thai คนต่าง...
  - ἐμπαιχθήσεται → ถูกเยาะเย้ย — ἐμπαίζω fut-pass 'be mocked.' Thai ถูกเยาะเย้ย (glossary-established MRK 10:34, 15:20).
  - ὑβρισθήσεται → ถูกดูหมิ่น — ὑβρίζω fut-pass 'be insulted/treated with contempt.' Thai ถูกดูหมิ่น distinguished from ถูกเยาะเย้ย — different act (contempt-treatment vs. mocking-speech). Luke-distinctive: MRK 10:34 omits ὑβρισθήσεται.
  - ἐμπτυσθήσεται → ถูกถ่มน้ำลายรด — ἐμπτύω fut-pass 'be spat upon.' Thai ถูกถ่มน้ำลายรด (glossary-established MRK 10:34, 14:65, 15:19).
- Notes: Luke-distinctive inclusion of ὑβρισθήσεται (MRK omits). Luke's triplet (mock-insult-spit) emphasizes the public-shaming aspect of the passion — shame-honor culture dimension. PARALLEL: MRK 10:33-34 || MAT 20:18-19.

**Luke 18:33**
- GR: καὶ μαστιγώσαντες ἀποκτενοῦσιν αὐτόν,καὶ τῇ ἡμέρᾳ τῇ τρίτῃ ἀναστήσεται.
- TH: พวกเขาจะโบยพระองค์แล้วฆ่าพระองค์ และในวันที่สามพระองค์จะทรงเป็นขึ้นมาใหม่»
- Key decisions:
  - μαστιγώσαντες → โบย — μαστιγόω aor-ptc 'scourge/flog.' Thai โบย (glossary-established MRK 10:34, MAT 20:19).
  - ἀποκτενοῦσιν αὐτόν → ฆ่าพระองค์ — ἀποκτείνω fut 'kill.' Thai ฆ่า (standard). ทรง- not applied to the object of killing (pronoun αὐτόν = Him — the honorific is marked by 'พระองค์' itself).
  - τῇ ἡμέρᾳ τῇ τρίτῃ ἀναστήσεται → ในวันที่สามพระองค์จะทรงเป็นขึ้นมาใหม่ — Per uW figs-metonymy: ἀνίστημι 'rise up' = come back to life. Thai ทรงเป็นขึ้นมาใหม่ (divine subject + resurrection idiom; glossary-established MRK 10:34, LUK 9:22).
- Notes: PARALLEL: MRK 10:34 || MAT 20:19. Luke preserves the Semitic idiom 'on the third day' (inclusive counting: Friday-Saturday-Sunday = three days per first-century Jewish reckoning). Per uW translate-ordinal: some languages may need cardinal adaptation — Thai วันที่สาม preserves ordinal without ambiguity.

**Luke 18:34**
- GR: καὶ αὐτοὶ οὐδὲν τούτων συνῆκαν,καὶ ἦν τὸ ῥῆμα τοῦτο κεκρυμμένον ἀπ’αὐτῶν,καὶ οὐκ ἐγίνωσκον τὰ λεγόμενα.
- TH: แต่พวกเขาไม่เข้าใจสิ่งเหล่านี้เลย คำนี้ถูกซ่อนไว้จากพวกเขา และเขาทั้งหลายไม่รู้ความหมายของสิ่งที่พระองค์ตรัส
- Key decisions:
  - οὐδὲν τούτων συνῆκαν → ไม่เข้าใจสิ่งเหล่านี้เลย — συνίημι aor 'understand, comprehend.' Double negation structure (οὐδέν + neg-reinforcement). Thai ไม่เข้าใจ...เลย triple-marks total lack of comprehension.
  - ἦν τὸ ῥῆμα τοῦτο κεκρυμμένον ἀπ’αὐτῶν → คำนี้ถูกซ่อนไว้จากพวกเขา — Per uW figs-activepassive: passive (divine-passive implied — God as hiding-agent). Thai ถูกซ่อนไว้ preserves passive voice; the divine-agent is contextually inferred but not made explicit (following Luke's narrative...
  - τὸ ῥῆμα τοῦτο → คำนี้ — Per uW note: ῥῆμα here = 'saying, utterance' (specific sense). Thai คำ captures the saying-sense.
  - τὰ λεγόμενα → ความหมายของสิ่งที่พระองค์ตรัส — Per uW figs-activepassive: τὰ λεγόμενα 'the things being said' (pres-pass-ptc-substantive). Thai expanded to สิ่งที่พระองค์ตรัส + ความหมาย (what was said + meaning-thereof) to preserve the 'not comprehending the mea...
- Notes: Triple restatement (did not understand + hidden + did not comprehend) emphasizes the disciples' total failure of comprehension. Luke-distinctive: MRK omits this, MAT 20:17-19 is briefer. The disciples' incomprehension is a Lucan theme (cf. LUK 9:45 same trope after second prediction). The divine-passive κεκρυμμένον suggests intentional-divine-...

**Luke 18:35**
- GR: Ἐγένετο δὲ ἐν τῷ ἐγγίζειν αὐτὸν εἰς Ἰεριχὼ τυφλός τις ἐκάθητο παρὰ τὴν ὁδὸν ἐπαιτῶν.
- TH: เมื่อพระเยซูเสด็จเข้าใกล้เมืองเยรีโค มีชายตาบอดคนหนึ่งนั่งขอทานอยู่ริมทาง
- Key decisions:
  - Ἐγένετο δὲ ἐν τῷ ἐγγίζειν αὐτὸν → เมื่อพระเยซูเสด็จเข้าใกล้ — Classic Lucan ἐγένετο-in-articular-inf construction (Septuagintism, Luke's narrative signature). Per uW writing-newevent: event-introducer. Thai เมื่อ + เสด็จ (divine-subject motion verb). Named subject (พระเยซู) fo...
  - Ἰεριχὼ → เมืองเยรีโค — Ἰεριχώ → เมืองเยรีโค (glossary-established LUK 10:30, MRK 10:46).
  - τυφλός τις → ชายตาบอดคนหนึ่ง — Per uW writing-participants: introduces new character. τυφλός → ตาบอด (glossary-established throughout corpus). τις indefinite → คนหนึ่ง.
  - ἐπαιτῶν → ขอทาน — ἐπαιτέω 'beg' — rare (LUK 18:35; 16:3). Thai ขอทาน (natural Thai for begging).
- Notes: PARALLEL: MRK 10:46 || MAT 20:29-34 (Matthew doubles to two blind men). LOCATION DISCREPANCY: Luke says 'as Jesus drew near to Jericho'; Mark/Matthew say 'as they were leaving Jericho.' Classic Synoptic crux — possible resolutions: (1) Old-Jericho + New-Jericho (two nearby sites); (2) Luke telescopes narrative (healing on approach, healing sum...

**Luke 18:36**
- GR: ἀκούσας δὲ ὄχλου διαπορευομένου ἐπυνθάνετο τί εἴη τοῦτο·
- TH: เมื่อเขาได้ยินเสียงฝูงชนเดินผ่านมา เขาจึงถามว่าเกิดอะไรขึ้น
- Key decisions:
  - ὄχλου διαπορευομένου → เสียงฝูงชนเดินผ่านมา — ὄχλος → ฝูงชน (glossary-standard). διαπορεύομαι 'pass through/by' → เดินผ่านมา. Added เสียง (sound) since the blind man perceives the crowd by ear, implicit but helpful for Thai readers.
  - ἐπυνθάνετο τί εἴη τοῦτο → เขาจึงถามว่าเกิดอะไรขึ้น — Per uW alt: 'what was happening.' πυνθάνομαι 'inquire' → ถาม. Optative εἴη in indirect question preserved in Thai as naturally-phrased question-embedded statement.
- Notes: The blind man's awareness of crowd-commotion by ear (sensorium reversal — he cannot see but can hear) is the narrative setup for his faith-through-hearing response.

**Luke 18:37**
- GR: ἀπήγγειλαν δὲ αὐτῷ ὅτι Ἰησοῦς ὁ Ναζωραῖος παρέρχεται.
- TH: พวกเขาบอกเขาว่า «พระเยซูชาวนาซาเร็ธกำลังเสด็จผ่านมา»
- Key decisions:
  - Ἰησοῦς ὁ Ναζωραῖος → พระเยซูชาวนาซาเร็ธ — Ναζωραῖος → ชาวนาซาเร็ธ (glossary-established LUK 4:34, MRK 10:47 — Thai Christian standard for Nazarene epithet). Per uW translate-names.
  - παρέρχεται → กำลังเสด็จผ่านมา — παρέρχομαι pres 'pass by.' เสด็จ (divine motion) per RULES.md §3.
- Notes: Ναζωραῖος vs Ναζαρηνός: Luke uses both (Ναζαρηνός at LUK 4:34, 24:19; Ναζωραῖος here at 18:37). Most scholarly analysis treats them as variant adjective-forms with the same referent (from Nazareth), though some argue Ναζωραῖος may carry messianic-nazir overtones (cf. Matt 2:23 citation debate). Thai ชาวนาซาเร็ธ covers both forms.

**Luke 18:38**
- GR: καὶ ἐβόησεν λέγων·Ἰησοῦ υἱὲ Δαυίδ,ἐλέησόν με.
- TH: เขาจึงร้องขึ้นว่า «พระเยซู บุตรดาวิด ขอทรงพระเมตตาข้าพระองค์เถิด»
- TH-summary: «บุตรดาวิด» เป็นตำแหน่งของพระเมสสิยาห์ตามพันธสัญญาของพระเจ้าที่ให้แก่ดาวิด (2 ซมอ 7:12-16; อสย 11:1; ยรม 23:5) — พระเจ้าทรงสัญญาว่าจะมีเชื้อสายของดาวิดที่จะปกครองตลอดไป ชายตาบอดผู้นี้ แม้จะมองไม่เห็นด้วยตาเนื้อ แต่มองเห็นพระเยซูด้วยตาใจว่าทรงเป็นพระเมสสิยาห์ ซึ่งเป็นเรื่องน่าขัดแย้งกับขุนนางผู้มั่งมี (ข้อ 18-23) ที่มีตาแต่มองไม่เห็น
- Key decisions:
  - υἱὲ Δαυίδ → บุตรดาวิด — Per uW figs-metaphor: υἱός here = 'descendant' of David. Per uW figs-explicit: implicit messianic title (God promised a son-of-David who would be the Messiah). Thai บุตรดาวิด (glossary-established MRK 10:47, MAT 9:2...
  - ἐλέησόν με → ขอทรงพระเมตตาข้าพระองค์เถิด — ἐλεέω aor-imp 'have mercy.' Per uW figs-imperative: render as polite request (ขอ... เถิด). Per uW figs-explicit: implicitly requesting healing. Thai ขอทรงพระเมตตา + ข้าพระองค์ (humble-register addressing divine-auth...
- Notes: FIRST MESSIANIC CONFESSION in Luke's narrative by a non-disciple. The blind man's Christological insight — calling Jesus υἱὲ Δαυίδ — contrasts ironically with both (a) the sighted disciples who don't understand (v.34), and (b) the rich ruler who had moral-vision-without-spiritual-vision (vv.18-23). The blind man's physical blindness and spirit...

**Luke 18:39**
- GR: καὶ οἱ προάγοντες ἐπετίμων αὐτῷ ἵνα σιγήσῃ·αὐτὸς δὲ πολλῷ μᾶλλον ἔκραζεν·Υἱὲ Δαυίδ,ἐλέησόν με.
- TH: ผู้ที่เดินนำหน้าห้ามเขาให้เงียบ แต่เขายิ่งร้องเสียงดังขึ้นอีกว่า «บุตรดาวิด ขอทรงพระเมตตาข้าพระองค์เถิด»
- Key decisions:
  - οἱ προάγοντες → ผู้ที่เดินนำหน้า — προάγω pres-ptc 'go ahead of.' Thai ผู้ที่เดินนำหน้า captures 'those walking ahead.'
  - ἐπετίμων αὐτῷ ἵνα σιγήσῃ → ห้ามเขาให้เงียบ — Per uW alt: 'kept telling him not to shout.' ἐπιτιμάω impf 'rebuked' + ἵνα + aor-subj purpose 'so that he would be silent.' Thai ห้าม...ให้เงียบ.
  - πολλῷ μᾶλλον ἔκραζεν → ยิ่งร้องเสียงดังขึ้นอีก — Per uW: could be (1) 'shouted louder' (2) 'called more persistently.' Thai ยิ่ง...ขึ้นอีก captures the intensifying response without forcing a single interpretation — volume + persistence both implied.
- Notes: The crowd's silencing is another instance of Lukan ἐπιτιμάω-gatekeeping (cf. v.15 — disciples rebuking those bringing children). In both cases, Jesus overrides the gatekeepers.

**Luke 18:40**
- GR: σταθεὶς δὲ ὁ Ἰησοῦς ἐκέλευσεν αὐτὸν ἀχθῆναι πρὸς αὐτόν.ἐγγίσαντος δὲ αὐτοῦ ἐπηρώτησεν αὐτόν·
- TH: พระเยซูทรงหยุดและตรัสสั่งให้พาชายนั้นมาหาพระองค์ เมื่อเขาเข้ามาใกล้แล้ว พระองค์ตรัสถามเขาว่า
- Key decisions:
  - σταθεὶς → ทรงหยุด — ἵστημι aor-pass-ptc 'having stopped/stood.' Thai ทรงหยุด (royal-register motion verb).
  - ἐκέλευσεν αὐτὸν ἀχθῆναι πρὸς αὐτόν → ตรัสสั่งให้พาชายนั้นมาหาพระองค์ — κελεύω aor + aor-pass-inf (passive construction: 'commanded him to be brought'). Per uW figs-activepassive: can render active 'people to bring him.' Thai ตรัสสั่งให้พา...มา natural Thai handling of causative-command.
- Notes: Jesus' σταθείς (stopped) in the middle of a forward-moving crowd is dramatically weighted — the travel narrative pauses for this encounter. The Jerusalem-bound Messiah stops for one blind beggar.

**Luke 18:41**
- GR: Τί σοι θέλεις ποιήσω;ὁ δὲ εἶπεν·Κύριε,ἵνα ἀναβλέψω.
- TH: «เจ้าต้องการให้เราทำสิ่งใดให้เจ้า?» ชายนั้นทูลว่า «องค์พระผู้เป็นเจ้า ขอให้ข้าพระองค์กลับมองเห็นเถิด»
- Key decisions:
  - Τί σοι θέλεις ποιήσω → เจ้าต้องการให้เราทำสิ่งใดให้เจ้า? — Jesus-to-human register (เจ้า for singular human addressee). ποιήσω subjunctive 'should-I-do.' Thai ให้เราทำ preserves the causative 'for-me-to-do-for-you' structure.
  - Κύριε → องค์พระผู้เป็นเจ้า — κύριε vocative of κύριος — RULES.md §4 κύριος of Jesus → องค์พระผู้เป็นเจ้า. The blind man's address elevates from v.38's 'Son of David' to κύριε (Lord) — a confessional intensification.
  - ἵνα ἀναβλέψω → ขอให้ข้าพระองค์กลับมองเห็นเถิด — Per uW alt: 'I want to be able to see again' / 'I want you to restore my sight.' ἀναβλέπω 'look up/regain sight' — ἀνά prefix carries 'again' for previously-sighted. Per uW background: either he was born blind or lo...
- Notes: PARALLEL: MRK 10:51 (ῥαββουνι 'Rabboni'), MAT 20:33 ('Lord, that our eyes be opened'). Each gospel has a different vocative — Luke's Κύριε is highest confession. The ἀνα- in ἀναβλέψω suggests prior sight (loss-restoration) more than congenital blindness.

**Luke 18:42**
- GR: καὶ ὁ Ἰησοῦς εἶπεν αὐτῷ·Ἀνάβλεψον·ἡ πίστις σου σέσωκέν σε.
- TH: พระเยซูตรัสกับเขาว่า «จงมองเห็นเถิด ความเชื่อของเจ้าได้ช่วยเจ้าให้รอดแล้ว»
- TH-summary: คำว่า «ได้ช่วยเจ้าให้รอดแล้ว» (เซโซเคน) ใช้คำเดียวกับ «ได้รับความรอด» ในแง่ของวิญญาณ — การรักษาของพระเยซูไม่ใช่เพียงการคืนสายตาทางกายภาพ แต่เป็นการเผยให้เห็นถึงความรอดที่ใหญ่กว่าที่มาพร้อมกับการมาของพระเมสสิยาห์ ความเชื่อของชายตาบอด — ที่กล้าร้องเรียกพระเยซูว่าบุตรดาวิดและไม่ยอมเงียบ — เป็นช่องทางที่พระเจ้าทรงประทานทั้งการรักษาและความรอดให้
- Key decisions:
  - Ἀνάβλεψον → จงมองเห็นเถิด — Per uW figs-imperative: not a command the man could obey, but performative-command that accomplishes itself. Thai จงมองเห็นเถิด preserves the imperative-form; context makes clear this is a healing-word not a request.
  - ἡ πίστις σου σέσωκέν σε → ความเชื่อของเจ้าได้ช่วยเจ้าให้รอดแล้ว — Per uW figs-abstractnouns + personification: πίστις (faith) 'actively saved you' — theological language. Per uW: σῴζω here = 'healed,' but with theological overtones of salvation-through-faith. Thai ได้ช่วยเจ้าให้รอ...
- Notes: PARALLEL: MRK 10:52 (identical Greek) || MAT 20:34 (Matthew doesn't include the faith-saved formula — just compassion-touch-healing). Luke's retention of the faith-saved formula ties this healing to the larger Lucan theme (cf. LUK 7:50 of the sinful woman, 8:48 of the hemorrhaging woman, 17:19 of the Samaritan leper). σέσωκεν (perfect) marks a...

**Luke 18:43**
- GR: καὶ παραχρῆμα ἀνέβλεψεν,καὶ ἠκολούθει αὐτῷ δοξάζων τὸν θεόν.καὶ πᾶς ὁ λαὸς ἰδὼν ἔδωκεν αἶνον τῷ θεῷ.
- TH: ทันใดนั้นเขาก็กลับมองเห็น และเขาติดตามพระองค์ไปพร้อมกับสรรเสริญพระเจ้า และประชาชนทั้งหมดที่เห็นเหตุการณ์นั้นก็ร่วมกันสรรเสริญพระเจ้าด้วย
- Key decisions:
  - παραχρῆμα → ทันใดนั้น — παραχρῆμα 'immediately/at-once' — Luke's signature adverb (10× Luke-Acts out of 18× NT). Thai ทันใดนั้น (glossary-established LUK 1:64, 4:39, 5:25, 8:44, 47, 13:13, 19:11, 22:60).
  - ἠκολούθει αὐτῷ δοξάζων τὸν θεόν → เขาติดตามพระองค์ไปพร้อมกับสรรเสริญพระเจ้า — Per uW note: here ἀκολουθέω may carry literal 'following-in-road' sense more than discipleship-metaphor — but the concurrent δοξάζων (glorifying) reads as discipleship-behavior. Thai preserves both readings. δοξάζω ...
  - πᾶς ὁ λαὸς ἰδὼν ἔδωκεν αἶνον → ประชาชนทั้งหมดที่เห็นเหตุการณ์นั้นก็ร่วมกันสรรเสริญ — λαός 'people' (in Luke often = God's people Israel) → ประชาชน. αἶνος 'praise' → สรรเสริญ. δίδωμι + αἶνον 'give praise' — Thai ร่วมกันสรรเสริญ captures the communal response. NEW: αἶνος → สรรเสริญ (same rendering as ...
- Notes: PARALLEL: MRK 10:52 || MAT 20:34. Luke-distinctive: (a) λαός rather than ὄχλος for the witnessing-crowd — Luke's theological-Israel terminology; (b) explicit mention of crowd-response praising God. The chapter closes with a praise-inclusio matching the chapter's opening command to prayer (v.1). παραχρῆμα mirrors LUK 5:25 (paralytic) and 17:14 ...


---

### Luke 24

**Luke 24:1**
- GR: τῇ δὲ μιᾷ τῶν σαββάτων ὄρθρου βαθέως ἐπὶ τὸ μνῆμα ἦλθον φέρουσαι ἃ ἡτοίμασαν ἀρώματα.
- TH: เช้าตรู่ของวันต้นสัปดาห์ พวกผู้หญิงก็นำเครื่องหอมที่เตรียมไว้ไปยังอุโมงค์
- TH-summary: «วันต้นสัปดาห์» คือวันอาทิตย์ นับเป็นวันที่สามหลังจากวันศุกร์ที่พระเยซูสิ้นพระชนม์ — พวกผู้หญิงต้องรอให้วันสะบาโตผ่านไป (ลูกา 23:56) จึงสามารถออกมาชโลมพระศพได้ตามธรรมเนียมยิว
- Key decisions:
  - τῇ & μιᾷ τῶν σαββάτων → วันต้นสัปดาห์ — uW figs-explicit + translate-ordinal: μιᾷ is cardinal 'one' but functions as ordinal 'first.' σάββατον in this construction means 'week' (metonymy for the week-ending Sabbath). Thai วันต้นสัปดาห์ natural for 'first ...
  - ὄρθρου βαθέως → เช้าตรู่ — uW figs-idiom: 'deep of dawn' = first light. Thai เช้าตรู่ preserves the 'before sunrise' nuance naturally.
  - ἐπὶ τὸ μνῆμα ἦλθον → ไปยังอุโมงค์ — Subject 'they' implicit per uW writing-pronouns — refers to women at 23:55-56. μνῆμα = tomb-chamber (synonym of μνημεῖον, alternates freely in the chapter). Thai อุโมงค์ matches the LUK 23:53/55 precedent — the same...
  - φέρουσαι ἃ ἡτοίμασαν ἀρώματα → นำเครื่องหอมที่เตรียมไว้ — ἀρώματα = aromatic-spices for anointing. Thai เครื่องหอม standard (LUK 23:56 precedent). ἡτοίμασαν aor — preparation done Friday evening (per 23:56), action completed before Sabbath-rest.
- Notes: OPENING OF RESURRECTION NARRATIVE. The women are those named in v.10 (Mary Magdalene, Joanna, Mary of James, + others). They carry aromatic-spices prepared before the Sabbath (23:56) — Jewish burial-custom of washing + anointing. SYNOPTIC PARALLEL: MAT 28:1, MRK 16:1-2, JHN 20:1. Each gospel emphasizes different details; Luke stresses the time...

**Luke 24:2**
- GR: εὗρον δὲ τὸν λίθον ἀποκεκυλισμένον ἀπὸ τοῦ μνημείου,
- TH: พวกเธอพบว่าหินถูกกลิ้งออกจากอุโมงค์แล้ว
- Key decisions:
  - τὸν λίθον ἀποκεκυλισμένον → หินถูกกลิ้งออก — uW figs-explicit: the λίθος is the large round rolling-stone sealing the tomb-entrance. uW figs-activepassive: divine-passive — implied actor is God/angel. Thai ถูกกลิ้งออก preserves the passive + rolling-action. λί...
  - ἀπὸ τοῦ μνημείου → จากอุโมงค์ — μνημεῖον = tomb (variant of μνῆμα at v.1). Thai อุโมงค์ consistent — same referent.
- Notes: DIVINE-PASSIVE implied: the stone did not roll-itself; God/angel removed it (per MAT 28:2 where an angel descends and rolls it back). Luke's ἀποκεκυλισμένον perfect-passive-participle captures the resultant state — stone-stays-rolled, tomb-stays-open. The size of the stone (per uW note at v.2 on LUK) required multiple people to move — women wo...

**Luke 24:3**
- GR: εἰσελθοῦσαι δὲ οὐχ εὗρον τὸ σῶμα.
- TH: เมื่อเข้าไปแล้ว พวกเธอก็ไม่พบพระศพ
- TH-summary: SBLGNT ไม่มีวลี «ขององค์พระเยซูเจ้า» ที่ปรากฏในฉบับ NA28/BSB/KJV/THSV ฉบับเอเรมอสเลือกตามต้นฉบับวิจารณ์ SBLGNT (สำนวนสั้น) พบในพยานตระกูลตะวันตก Codex Bezae (D) และฉบับลาตินโบราณบางฉบับ — เป็นหนึ่งใน «Western non-interpolations» ที่นักวิชาการโต้แย้งกันมา
- Key decisions:
  - εἰσελθοῦσαι & οὐχ εὗρον τὸ σῶμα → เมื่อเข้าไปแล้ว พวกเธอก็ไม่พบพระศพ — uW figs-explicit: body-not-there because Jesus has risen. Thai พระศพ retains divine-register honorific (LUK 23:52/53/55 precedent). Note the SHORT reading per SBLGNT — see notes for textual divergence.
- Notes: TEXTUAL VARIANT (SBLGNT vs NA28): SBLGNT main text ends the verse at τὸ σῶμα with no genitive qualifier. NA28 reads τὸ σῶμα [τοῦ κυρίου Ἰησοῦ] in single brackets ('the body [of the Lord Jesus]'). BSB, ESV, NIV, CSB, KJV, THSV all include 'of the Lord Jesus.' Witnesses-omit include Codex Bezae (D), Old Latin (a b d e ff² l r¹), some Syriac; wit...

**Luke 24:4**
- GR: καὶ ἐγένετο ἐν τῷ ἀπορεῖσθαι αὐτὰς περὶ τούτου,καὶ ἰδοὺ ἄνδρες δύο ἐπέστησαν αὐταῖς ἐν ἐσθῆτι ἀστραπτούσῃ.
- TH: ขณะที่พวกเธอกำลังงุนงงเรื่องนี้อยู่ ดูเถิด มีชายสองคนสวมเสื้อผ้าที่ส่องประกายมายืนอยู่ข้างพวกเธอ
- TH-summary: ลูกาเรียกพวกเขาว่า «ชาย» (ἄνδρες) — ต่อมาใน ข้อ 23 กล่าวว่าเป็น «ทูตสวรรค์» ยอห์น 20:12 เรียกว่าเป็น «ทูตสวรรค์สององค์» เช่นเดียวกัน การที่ลูกาใช้คำว่า «ชาย» สะท้อนว่าทูตสวรรค์ปรากฏในรูปมนุษย์ — ประเพณีการบันทึกเรื่องการเทพพบในพันธสัญญาเดิม (เช่น ปฐมกาล 18 เมื่ออับราฮัมต้อนรับ «ชายสามคน» ที่กลายเป็นพระเจ้ากับทูตสวรรค์)
- Key decisions:
  - ἐν τῷ ἀπορεῖσθαι αὐτὰς → ขณะที่พวกเธอกำลังงุนงง — ἀπορέω 'be at a loss, puzzled, perplexed' middle voice = mental distress. Thai งุนงง captures the confused-state naturally.
  - καὶ ἰδοὺ → ดูเถิด — uW writing-newevent: Luke's καὶ ἰδού marks a sudden-dramatic-reveal. Thai ดูเถิด glossary-standard (cf. LUK 23:50).
  - ἄνδρες δύο → ชายสองคน — Luke says ἄνδρες 'men' — not ἄγγελοι (yet — v.23 reports them as angels). uW explains: angels appearing in human-form. Thai ชายสองคน matches Luke's surface-choice; the angelic-nature is disclosed at v.23.
  - ἐν ἐσθῆτι ἀστραπτούσῃ → สวมเสื้อผ้าที่ส่องประกาย — ἀστράπτω 'flash like lightning' — same root as ἀστραπή. Thai ส่องประกาย 'shine/glisten' captures the lightning-flash shimmer naturally. The dazzling-attire is a standard-biblical angelophany marker (Dan 10:5-6; MAT ...
- Notes: ANGELOPHANY: Luke presents the messengers as ἄνδρες 'men' (surface-appearance), but v.23 retrospectively calls them ἀγγέλων. SYNOPTIC DIVERGENCE: MAT 28:2-3 has one-angel rolling-stone; MRK 16:5 has one-young-man inside; LUK 24:4 + JHN 20:12 have two-angels. uW chapter-intro (§'Two men in bright shining robes') counsels against harmonizing. Th...

**Luke 24:5**
- GR: ἐμφόβων δὲ γενομένων αὐτῶν καὶ κλινουσῶν τὰ πρόσωπα εἰς τὴν γῆν,εἶπαν πρὸς αὐτάς·Τί ζητεῖτε τὸν ζῶντα μετὰ τῶν νεκρῶν;
- TH: เมื่อพวกเธอตกใจกลัวและก้มหน้าลงถึงดิน พวกเขาก็กล่าวแก่พวกเธอว่า «เหตุใดพวกเจ้ามาหาผู้ทรงพระชนม์อยู่ในหมู่คนตายเล่า?»
- TH-summary: คำถามนี้เป็นคำถามเชิงวาทศิลป์ (ไม่ได้ถามเพื่อรอคำตอบ) แต่เป็นการประกาศว่าพระเยซูทรงพระชนม์ คำว่า «ผู้ทรงพระชนม์» (τὸν ζῶντα) เป็นการเน้นว่าพระองค์เป็นผู้ทรงชีวิตอยู่ ไม่ใช่คนตาย
- Key decisions:
  - ἐμφόβων & γενομένων αὐτῶν → พวกเธอตกใจกลัว — ἔμφοβος 'terrified.' Participial-genitive-absolute with γίνομαι. Thai ตกใจกลัว natural rendering.
  - κλινουσῶν τὰ πρόσωπα εἰς τὴν γῆν → ก้มหน้าลงถึงดิน — uW translate-symaction: respectful-bowing gesture before divine-messengers. Thai ก้มหน้าลงถึงดิน preserves the physical prostration posture naturally.
  - Τί ζητεῖτε τὸν ζῶντα μετὰ τῶν νεκρῶν → เหตุใดพวกเจ้ามาหาผู้ทรงพระชนม์อยู่ในหมู่คนตาย — uW figs-rquestion: rhetorical-question = announcement, not information-request. Thai เหตุใด...เล่า preserves the question-form but signals the rhetorical-register. τὸν ζῶντα 'the living-one' is a christological-titl...
- Notes: RHETORICAL-QUESTION-AS-PROCLAMATION: the angels use the question-form to announce Jesus's resurrection. τὸν ζῶντα 'the Living One' foreshadows his post-resurrection title (cf. Rev 1:18 ὁ ζῶν). The honorific divine-register in Thai (ผู้ทรงพระชนม์) marks Jesus's identity throughout the chapter. THEOLOGICAL: 'living among the dead' inverts the wo...

**Luke 24:6**
- GR: οὐκ ἔστιν ὧδε,ἀλλὰ ἠγέρθη.μνήσθητε ὡς ἐλάλησεν ὑμῖν ἔτι ὢν ἐν τῇ Γαλιλαίᾳ,
- TH: พระองค์ไม่ได้อยู่ที่นี่ แต่ทรงเป็นขึ้นมาแล้ว จงระลึกถึงที่พระองค์ตรัสกับพวกเจ้าไว้ เมื่อพระองค์ยังอยู่ในแคว้นกาลิลี
- TH-summary: คำประกาศการคืนพระชนม์ครั้งแรกในพระคัมภีร์ — «ทรงเป็นขึ้นมาแล้ว» (ἠγέρθη) เป็นรูปกรรมวาจก (divine passive) หมายความว่า พระเจ้าพระบิดาทรงทำให้พระเยซูเป็นขึ้นมา ทูตสวรรค์เตือนให้ระลึกถึงคำพยากรณ์ที่พระเยซูได้ตรัสไว้สามครั้งในแคว้นกาลิลี (ลูกา 9:22, 9:44, 18:31-33)
- Key decisions:
  - οὐκ ἔστιν ὧδε, ἀλλὰ ἠγέρθη → พระองค์ไม่ได้อยู่ที่นี่ แต่ทรงเป็นขึ้นมาแล้ว — ἠγέρθη aor-pass 'was raised' per uW figs-idiom + figs-activepassive — implied actor is God (divine-passive). Thai ทรงเป็นขึ้นมาแล้ว preserves divine-register ทรง- and captures the resurrection-action. เป็นขึ้น match...
  - μνήσθητε → จงระลึกถึง — μιμνήσκομαι aor-imp 'remember!' — direct command from the angels. Thai จงระลึกถึง natural imperative.
  - ἐν τῇ Γαλιλαίᾳ → ในแคว้นกาลิลี — Γαλιλαία → แคว้นกาลิลี standard (LUK 23:49/55 precedent).
- Notes: FIRST-RESURRECTION-PROCLAMATION: the empty-tomb is revealed as resurrection via angelic-declaration. ἠγέρθη divine-passive implicit-agent = God — Paul uses the same formula at 1Co 15:4. Luke uniquely has the angels reference Jesus's Galilean-passion-predictions (cf. MRK 16:7 which points FORWARD to Galilee; Luke points BACKWARD — the crucifixi...

**Luke 24:7**
- GR: λέγων ὅτι Δεῖ τὸν υἱὸν τοῦ ἀνθρώπου παραδοθῆναι εἰς χεῖρας ἀνθρώπων ἁμαρτωλῶν,καὶ σταυρωθῆναι,καὶ τῇ τρίτῃ ἡμέρᾳ ἀναστῆναι.
- TH: โดยตรัสว่า ‹บุตรมนุษย์จะต้องถูกมอบไว้ในเงื้อมมือคนบาป ต้องถูกตรึงบนกางเขน และในวันที่สามจะทรงเป็นขึ้นมา›
- TH-summary: คำพยากรณ์ที่พระเยซูตรัสไว้ในแคว้นกาลิลีมีสามจังหวะ — ถูกมอบ ถูกตรึง เป็นขึ้นมา — ซึ่งเกิดขึ้นจริงครบถ้วนแล้ว ทูตสวรรค์กำลังช่วยให้พวกผู้หญิงเชื่อมโยงเหตุการณ์ที่เพิ่งเห็นกับถ้อยคำที่เคยได้ยิน «บุตรมนุษย์» เป็นคำที่พระเยซูใช้เรียกพระองค์เอง มีรากจากพระธรรมดาเนียล 7:13
- Key decisions:
  - Δεῖ τὸν υἱὸν τοῦ ἀνθρώπου παραδοθῆναι → บุตรมนุษย์จะต้องถูกมอบไว้ — δεῖ 'it-is-necessary' — divine-necessity of the passion-plan. Thai จะต้อง captures the must-ness. υἱὸς τοῦ ἀνθρώπου → บุตรมนุษย์ standard (LUK 21:27/36, 22:22/48/69 precedent). παραδίδωμι aor-pass-inf 'to-be-handed-...
  - εἰς χεῖρας ἀνθρώπων ἁμαρτωλῶν → ในเงื้อมมือคนบาป — uW figs-metonymy: χεῖρας 'hands' = power/control. Thai เงื้อมมือ preserves the figurative hand-control idiom naturally. ἁμαρτωλός → คนบาป glossary-standard.
  - σταυρωθῆναι → ถูกตรึงบนกางเขน — σταυρόω aor-pass-inf 'to-be-crucified.' Thai ถูกตรึงบนกางเขน standard (LUK 23:33 precedent).
  - τῇ τρίτῃ ἡμέρᾳ ἀναστῆναι → ในวันที่สามจะทรงเป็นขึ้นมา — ἀνίστημι aor-act-inf 'to-rise.' Thai ทรงเป็นขึ้นมา — divine-register ทรง- prefix required for divine-subject-raising-himself. τρίτῃ ἡμέρᾳ 'third day' — Friday-death, Saturday-in-tomb, Sunday-raised by inclusive-reck...
- Notes: INDIRECT-QUOTATION: the angels report Jesus's prior-Galilean-prediction. This matches LUK 9:22 (δεῖ + παθεῖν + ἀποδοκιμασθῆναι + ἀποκτανθῆναι + ἐγερθῆναι) + LUK 9:44 (παραδίδοσθαι εἰς χεῖρας ἀνθρώπων) + LUK 18:31-33 (σταυρωθῆναι + ἀναστήσεται). THIRD-DAY-IDIOM: per uW chapter-intro, 'first/second/third day' reckoning: Friday=day-one, Saturday=...

**Luke 24:8**
- GR: καὶ ἐμνήσθησαν τῶν ῥημάτων αὐτοῦ,
- TH: พวกเธอจึงระลึกถึงพระดำรัสของพระองค์ได้
- Key decisions:
  - ἐμνήσθησαν τῶν ῥημάτων αὐτοῦ → พวกเธอจึงระลึกถึงพระดำรัสของพระองค์ได้ — μιμνήσκομαι aor-pass-3pl 'they-remembered.' uW figs-metonymy: ῥήματα 'words' = what-he-said using-words. Thai พระดำรัส divine-register for divine-speech. จึง...ได้ captures the enabling-realization.
- Notes: REVERSAL-OF-COMPREHENSION: the angels' reminder unlocks the women's memory. In LUK 9:45 and 18:34, the disciples had their understanding 'hidden' from them about these same prophecies; here the women break through into understanding. Luke tracks this comprehension-arc deliberately.

**Luke 24:9**
- GR: καὶ ὑποστρέψασαι ἀπὸ τοῦ μνημείου ἀπήγγειλαν ταῦτα πάντα τοῖς ἕνδεκα καὶ πᾶσιν τοῖς λοιποῖς.
- TH: เมื่อกลับจากอุโมงค์แล้ว พวกเธอก็ไปรายงานเรื่องทั้งหมดนี้แก่สาวกสิบเอ็ดคนและคนอื่น ๆ ทั้งหมด
- Key decisions:
  - τοῖς ἕνδεκα → สาวกสิบเอ็ดคน — uW figs-nominaladj: 'the Eleven' = the twelve-minus-Judas after Iscariot's defection. Thai สาวกสิบเอ็ดคน (disciples-eleven) matches the MAT 28:16 + MRK 16:14 precedent — adding สาวก makes the referent-clear (not 'el...
  - καὶ πᾶσιν τοῖς λοιποῖς → และคนอื่น ๆ ทั้งหมด — uW figs-explicit: all-other-disciples present with the Eleven. Thai คนอื่น ๆ ทั้งหมด natural. λοιποί 'rest' → คนอื่น ๆ.
- Notes: 'THE ELEVEN' (τοῖς ἕνδεκα): first-NT-usage of this collective-title — the apostolic-core post-Judas. Will recur at v.33 (assembled-group), Acts 1:26 (pre-Matthias-election), Acts 2:14 (Peter-with-the-Eleven at Pentecost). Luke tracks the group-identity through the transition. NARRATIVE-FUNCTION: the women become the first-evangelists of the re...

**Luke 24:10**
- GR: ἦσαν δὲ ἡ Μαγδαληνὴ Μαρία καὶ Ἰωάννα καὶ Μαρία ἡ Ἰακώβου καὶ αἱ λοιπαὶ σὺν αὐταῖς·ἔλεγον πρὸς τοὺς ἀποστόλους ταῦτα.
- TH: หญิงเหล่านั้นคือมารีย์ชาวมักดาลา โยอันนา มารีย์มารดาของยากอบ และหญิงอื่น ๆ ที่อยู่กับพวกเธอ ซึ่งบอกเล่าเรื่องเหล่านี้แก่เหล่าอัครทูต
- Key decisions:
  - ἡ Μαγδαληνὴ Μαρία → มารีย์ชาวมักดาลา — Μαρία Μαγδαληνή — 'Mary of Magdala.' Thai มารีย์ชาวมักดาลา standard Thai Christian transliteration. First-named because she was first-to-see the risen Jesus (JHN 20:14-18) — Luke lists her first as well per importan...
  - Ἰωάννα → โยอันนา — uW translate-names: Joanna — wife of Chuza (Herod's steward, LUK 8:3). Thai โยอันนา standard transliteration.
  - Μαρία ἡ Ἰακώβου → มารีย์มารดาของยากอบ — uW translate-names: 'Mary of James' = Mary the mother of James (the Less/Little, cf. MRK 15:40). Thai adds มารดา 'mother' explicitly per Thai-syntax requirement. ยากอบ standard transliteration.
  - τοὺς ἀποστόλους → เหล่าอัครทูต — ἀπόστολος → อัครทูต standard. Eremos-glossary precedent (cf. Mark 3:14, 6:30). This is the first-NT-use of 'apostles' in the resurrection-narrative — Luke signals the official-transmission of the gospel-news from th...
- Notes: NAMED-WITNESSES: the specific naming of women-witnesses is a historiographical-marker — ancient historians named witnesses to signal 'you can verify this with them.' Mary Magdalene appears at the tomb in all four gospels (LUK 8:2 had already introduced her as one from whom seven demons were cast). Joanna (unique to Luke) was named at 8:3 — wea...

**Luke 24:11**
- GR: καὶ ἐφάνησαν ἐνώπιον αὐτῶν ὡσεὶ λῆρος τὰ ῥήματα ταῦτα,καὶ ἠπίστουν αὐταῖς.
- TH: แต่ถ้อยคำเหล่านี้กลับดูเหมือนเรื่องเพ้อเจ้อในสายตาของพวกเขา พวกเขาจึงไม่เชื่อพวกเธอ
- TH-summary: คำว่า «เรื่องเพ้อเจ้อ» (λῆρος) เป็นคำที่พบครั้งเดียวในพันธสัญญาใหม่ ในภาษากรีกคลาสสิกใช้หมายถึงคำพูดเลื่อนลอยไร้สาระ — เหล่าอัครทูตไม่เชื่อพวกผู้หญิงในตอนแรก ลูกาบันทึกข้อนี้เพื่อแสดงความซื่อสัตย์ในการเล่าเรื่อง ไม่ได้ปกปิดว่าสาวกเองก็ต้องใช้เวลาในการเชื่อ
- Key decisions:
  - ἐφάνησαν ἐνώπιον αὐτῶν → ดูเหมือน...ในสายตาของพวกเขา — uW figs-metaphor: ἐνώπιον 'in-front-of' = in-their-view/opinion. Thai ในสายตาของ preserves the perceptual-framing naturally.
  - ὡσεὶ λῆρος → เหมือนเรื่องเพ้อเจ้อ — HAPAX: λῆρος 'idle-talk, nonsense, trifle' — classical usage (LSJ) denotes hollow, silly, frivolous-chatter. In medical-Greek it can mean delirious-raving. Thai เรื่องเพ้อเจ้อ captures the rambling-nonsense nuance —...
  - ἠπίστουν αὐταῖς → พวกเขาจึงไม่เชื่อพวกเธอ — ἀπιστέω imperfect 'were-not-believing' — ongoing-disbelief. Thai ไม่เชื่อ direct. จึง captures the result-connective (uW grammar-connect-logic-result).
- Notes: HAPAX: λῆρος 'nonsense, idle-tale' — unique in NT. Classical parallels include Plato Gorgias (where λῆρος denotes philosophical-triviality) and 4 Maccabees 5:11 (mocking-dismissal). The medical-Greek sense 'delirium' (from a physician-author per uW) adds pointed-irony: the apostles dismiss as 'delirium' what turned out to be reality. HISTORICA...

**Luke 24:12**
- GR: Ὁ δὲ Πέτρος ἀναστὰς ἔδραμεν ἐπὶ τὸ μνημεῖον·καὶ παρακύψας βλέπει τὰ ὀθόνια μόνα·καὶ ἀπῆλθεν πρὸς αὑτὸν θαυμάζων τὸ γεγονός.
- TH: แต่เปโตรลุกขึ้นแล้ววิ่งไปที่อุโมงค์ เมื่อก้มลงมอง ก็เห็นแต่ผ้าป่านกองอยู่ตามลำพัง เขาจึงกลับไปโดยประหลาดใจในสิ่งที่เกิดขึ้น
- TH-summary: เปโตรแม้จะไม่เชื่อในตอนแรก (ข้อ 11) แต่ยังวิ่งไปตรวจสอบด้วยตนเอง — เป็นท่าทีของคนที่ต้องการหลักฐาน ไม่ใช่เชื่อลม ๆ แล้ง ๆ ยอห์น 20:3-10 เล่ารายละเอียดว่าเปโตรไปพร้อมกับยอห์น ลูกาเน้นเปโตรเพียงคนเดียวเพื่อความกระชับ
- Key decisions:
  - Πέτρος ἀναστὰς ἔδραμεν → เปโตรลุกขึ้นแล้ววิ่งไป — uW figs-idiom: ἀναστάς 'having-risen' = taking-initiative (not necessarily from sitting). But the literal standing-up-to-run is also fine here since it fits natural action. Thai ลุกขึ้นแล้ววิ่งไป preserves the simpl...
  - παρακύψας βλέπει τὰ ὀθόνια μόνα → เมื่อก้มลงมอง ก็เห็นแต่ผ้าป่านกองอยู่ตามลำพัง — παρακύπτω 'stoop-down-to-look' — necessary because rock-cut tombs had low entrances (uW figs-explicit). Thai ก้มลงมอง captures the bending-action. ὀθόνια 'linen-strips' for burial-wrapping. Thai ผ้าป่าน standard. μό...
  - ἀπῆλθεν πρὸς αὑτὸν θαυμάζων τὸ γεγονός → เขาจึงกลับไปโดยประหลาดใจในสิ่งที่เกิดขึ้น — uW explicit: dual-reading — 'went-away to-himself wondering' (= wondering-to-himself) OR 'went-away to-his-own-home wondering.' ULT/BSB follow the first reading; so do we. Thai ประหลาดใจในสิ่งที่เกิดขึ้น natural. We...
- Notes: TEXTUAL-NOTE: v.12 is another Western-non-interpolation candidate. Codex Bezae (D), Old Latin a b d e l r¹ OMIT this entire verse. SBLGNT, NA28, Byzantine, and all Alexandrian uncials INCLUDE. Since SBLGNT prints the verse, we render it — no textual-footnote required here (SBLGNT + NA28 + BSB all agree on inclusion). HARMONIZATION with JHN 20:...

**Luke 24:13**
- GR: Καὶ ἰδοὺ δύο ἐξ αὐτῶν ἐν αὐτῇ τῇ ἡμέρᾳ ἦσαν πορευόμενοι εἰς κώμην ἀπέχουσαν σταδίους ἑξήκοντα ἀπὸ Ἰερουσαλήμ,ᾗ ὄνομα Ἐμμαοῦς,
- TH: ดูเถิด ในวันเดียวกันนั้น สาวกสองคนกำลังเดินทางไปหมู่บ้านแห่งหนึ่งชื่อเอมมาอูส ซึ่งห่างจากกรุงเยรูซาเล็มประมาณสิบเอ็ดกิโลเมตร
- TH-summary: เรื่องราว «ถนนสู่เอมมาอูส» เป็นหนึ่งในเรื่องเล่าที่เป็นที่รักในพระกิตติคุณของลูกา — สาวกสองคนเดินกลับบ้านในบ่ายวันอาทิตย์โดยคิดว่าทุกอย่างจบสิ้นแล้ว แต่พระเยซูผู้ทรงเป็นขึ้นมาเสด็จเดินเคียงข้างพวกเขาโดยที่พวกเขายังจำไม่ได้ ตลอดการเดินทางนี้ พระองค์จะทรงอธิบายจากพระคัมภีร์เดิมว่าทุกสิ่งที่เกิดขึ้นกับพระเมสสิยาห์นั้นเป็นไปตามที่พยากรณ์ไว้
- Key decisions:
  - ἰδοὺ → ดูเถิด — uW writing-newevent: signals new-episode. Thai ดูเถิด glossary-standard.
  - δύο ἐξ αὐτῶν → สาวกสองคน — uW writing-pronouns: 'two of them' = two-disciples (not specifically apostles, per v.33 return). Thai สาวกสองคน — explicit-identification for clarity.
  - κώμην & ᾗ ὄνομα Ἐμμαοῦς → หมู่บ้านแห่งหนึ่งชื่อเอมมาอูส — HAPAX: Ἐμμαοῦς — proper-name, village-location uncertain (several candidates: el-Qubeibeh, Abu Ghosh, Amwas). Thai เอมมาอูส standard transliteration. κώμη → หมู่บ้าน standard.
  - σταδίους ἑξήκοντα → ประมาณสิบเอ็ดกิโลเมตร — uW translate-bdistance: 60 stadia ≈ 11 km. Thai converts to modern-metric per uW precedent and Thai reader-expectation. (Some textual variants read 160 stadia for a different Emmaus candidate; SBLGNT + all major-mss...
- Notes: HAPAX: Ἐμμαοῦς — proper-name (village-identity-disputed). Village-location candidates: (1) el-Qubeibeh (Crusader-tradition) 11 km NW of Jerusalem, matches 60-stadia; (2) Abu Ghosh 13 km W; (3) Amwas/Emmaus-Nicopolis 30 km NW, matches the 160-stadia-variant. No consensus. NARRATIVE-INTRODUCTION: the Emmaus-episode is unique to Luke (not in MAT/...

**Luke 24:14**
- GR: καὶ αὐτοὶ ὡμίλουν πρὸς ἀλλήλους περὶ πάντων τῶν συμβεβηκότων τούτων.
- TH: พวกเขาสนทนากันเรื่องเหตุการณ์ทั้งหมดที่เกิดขึ้น
- Key decisions:
  - ὡμίλουν πρὸς ἀλλήλους → สนทนากัน — ὁμιλέω imperfect 'were-conversing.' Thai สนทนากัน natural. ἀλλήλων 'one-another' absorbed into reciprocal-particle กัน.
  - περὶ πάντων τῶν συμβεβηκότων τούτων → เรื่องเหตุการณ์ทั้งหมดที่เกิดขึ้น — συμβαίνω perf-ptc 'having-happened.' uW figs-explicit: 'these things' = Jesus's arrest, crucifixion, women-at-tomb-report. Thai เหตุการณ์ทั้งหมด preserves the 'all things' scope naturally.
- Notes: SCENE-SETTING: the two disciples are processing the weekend's traumatic-and-puzzling events. Luke will develop this 'talking-about' into the dramatic-ironic encounter where the very-subject of their discussion is walking with them.

**Luke 24:15**
- GR: καὶ ἐγένετο ἐν τῷ ὁμιλεῖν αὐτοὺς καὶ συζητεῖν,καὶ αὐτὸς Ἰησοῦς ἐγγίσας συνεπορεύετο αὐτοῖς,
- TH: ขณะที่พวกเขากำลังสนทนาและถกเถียงกันอยู่นั้น พระเยซูเองก็เสด็จเข้ามาใกล้ ทรงดำเนินไปด้วยกันกับพวกเขา
- Key decisions:
  - συζητεῖν → ถกเถียงกัน — συζητέω 'discuss, deliberate, dispute.' Thai ถกเถียงกัน captures the back-and-forth deliberation. Together ὁμιλεῖν + συζητεῖν is a hendiadys-intensification: talking-and-debating, wrestling-with-the-meaning.
  - αὐτὸς Ἰησοῦς ἐγγίσας → พระเยซูเองก็เสด็จเข้ามาใกล้ — uW writing-pronouns: αὐτός intensifier emphasizes 'Jesus-himself' actually-there, not a vision. Thai พระเยซูเอง. Divine-register: เสด็จ required for Jesus-movement per RULES §3. ἐγγίζω aor-ptc 'having-drawn-near' → ...
  - συνεπορεύετο αὐτοῖς → ทรงดำเนินไปด้วยกันกับพวกเขา — συμπορεύομαι imperfect 'was-traveling-together-with.' Divine-register ทรง- prefix. ดำเนินไปด้วยกัน natural Thai for fellow-walking.
- Notes: αὐτὸς ΙΗΣΟῦΣ: Luke's emphatic 'Jesus himself' per uW writing-pronouns — corporeal, visible, audible, not an apparition. The walking-together is the hermeneutical-set-piece: the risen-Lord as fellow-pilgrim. Foreshadows Acts's traveling-companion motif ('we-passages').

**Luke 24:16**
- GR: οἱ δὲ ὀφθαλμοὶ αὐτῶν ἐκρατοῦντο τοῦ μὴ ἐπιγνῶναι αὐτόν.
- TH: แต่ตาของพวกเขาถูกปิดไว้ไม่ให้จำพระองค์ได้
- TH-summary: การที่พระเจ้าทรงปิดตาของพวกเขา เป็นการบอกใบ้ว่าการจดจำพระเยซูต้องเกิดจากการทรงเปิดเผยของพระเจ้าเอง ไม่ใช่จากการใช้ตาเห็นเท่านั้น — ข้อ 31 จะกล่าวถึงตรงข้าม คือ «ตาของพวกเขาสว่างขึ้น» เมื่อพระเยซูหักขนมปัง
- Key decisions:
  - οἱ & ὀφθαλμοὶ αὐτῶν ἐκρατοῦντο → ตาของพวกเขาถูกปิดไว้ — uW figs-synecdoche + figs-metaphor + figs-activepassive: 'eyes were-held' = God prevented recognition. κρατέω impf-pass 'were-being-restrained.' Thai ถูกปิดไว้ preserves the divine-passive restraint. ตา (eyes) standard.
  - τοῦ μὴ ἐπιγνῶναι αὐτόν → ไม่ให้จำพระองค์ได้ — ἐπιγινώσκω aor-inf 'to-recognize fully.' Thai จำได้ natural for recognition. Purpose-clause articular-infinitive-of-negation → ไม่ให้...ได้.
- Notes: DIVINE-PASSIVE: ἐκρατοῦντο imperfect-passive with implied-divine-actor. God prevented-recognition — intentional, pedagogical. The recognition later at v.31 is also divine-gift (διηνοίχθησαν οἱ ὀφθαλμοί). Luke frames resurrection-recognition as REVELATION, not observation — the same man is seen but not-recognized-until-God-opens. This prefigure...

**Luke 24:17**
- GR: εἶπεν δὲ πρὸς αὐτούς·Τίνες οἱ λόγοι οὗτοι οὓς ἀντιβάλλετε πρὸς ἀλλήλους περιπατοῦντες;καὶ ἐστάθησαν σκυθρωποί.
- TH: พระองค์ตรัสกับพวกเขาว่า «เรื่องอะไรที่พวกท่านโต้ตอบกันขณะเดินทางอยู่?» พวกเขาก็หยุดยืน หน้าตาเศร้าหมอง
- Key decisions:
  - Τίνες οἱ λόγοι οὗτοι οὓς ἀντιβάλλετε → เรื่องอะไรที่พวกท่านโต้ตอบกัน — HAPAX: ἀντιβάλλω 'throw-back-and-forth' — classical sense = exchange-words, dispute, debate. Thai โต้ตอบ captures the back-and-forth exchange naturally. uW figs-metonymy: λόγοι = what-they-have-been-saying. Thai เรื...
  - ἐστάθησαν σκυθρωποί → พวกเขาก็หยุดยืน หน้าตาเศร้าหมอง — σκυθρωπός 'gloomy, sad-faced' — adjective-nominative-plural modifying the two men. Thai หน้าตาเศร้าหมอง preserves the sad-countenance idiom. ἐστάθησαν aor-pass 'they-stood' — stopped-walking. Thai หยุดยืน.
- Notes: HAPAX: ἀντιβάλλω — NT-unique, though classical-common (Thucydides, Xenophon for 'exchange' words/blows). LSJ: 'cast against, answer, match, compare' — the men are deeply-debating, not casually-chatting. Luke's word-choice signals intensity. HONORIFIC: Jesus addresses the two disciples — Thai พวกท่าน (neutral-respectful 2PL) fits a stranger add...

**Luke 24:18**
- GR: ἀποκριθεὶς δὲ εἷς ὀνόματι Κλεοπᾶς εἶπεν πρὸς αὐτόν·Σὺ μόνος παροικεῖς Ἰερουσαλὴμ καὶ οὐκ ἔγνως τὰ γενόμενα ἐν αὐτῇ ἐν ταῖς ἡμέραις ταύταις;
- TH: คนหนึ่งในพวกเขาชื่อคลีโอปัสตอบพระองค์ว่า «ท่านเป็นผู้เดียวหรือที่พักอาศัยในกรุงเยรูซาเล็มแต่ไม่รู้เรื่องราวที่เกิดขึ้นในกรุงนี้ในช่วงหลายวันมานี้?»
- Key decisions:
  - ὀνόματι Κλεοπᾶς → ชื่อคลีโอปัส — HAPAX: Κλεοπᾶς — proper-name, NT-unique. May be same as Κλωπᾶς at JHN 19:25 (husband of one Mary) or distinct. Thai คลีโอปัส standard transliteration.
  - Σὺ μόνος παροικεῖς Ἰερουσαλὴμ → ท่านเป็นผู้เดียวหรือที่พักอาศัยในกรุงเยรูซาเล็ม — uW figs-rquestion: rhetorical-question expressing surprise. παροικέω 'reside-as-stranger, sojourn' — Cleopas assumes Jesus is a visitor-to-Jerusalem for Passover. Thai พักอาศัย natural. Ἰερουσαλήμ → กรุงเยรูซาเล็ม g...
  - τὰ γενόμενα ἐν αὐτῇ ἐν ταῖς ἡμέραις ταύταις → เรื่องราวที่เกิดขึ้นในกรุงนี้ในช่วงหลายวันมานี้ — uW figs-idiom: 'these days' = recently. Thai ในช่วงหลายวันมานี้ natural for 'recent-days.' αὐτῇ refers to Jerusalem (feminine-pronoun per Greek convention — uW writing-pronouns).
- Notes: HAPAX: Κλεοπᾶς — only-here in NT. Possible-identity: (1) same-as Κλωπᾶς of JHN 19:25, husband of Mary-wife-of-Clopas (who stood at the cross) — if so, then the OTHER-unnamed disciple may be this Mary; (2) distinct-person. Scholarship is split; Luke leaves unnamed companion anonymous. RHETORICAL-QUESTION: uW figs-rquestion — Cleopas is incredul...

**Luke 24:19**
- GR: καὶ εἶπεν αὐτοῖς·Ποῖα;οἱ δὲ εἶπαν αὐτῷ·Τὰ περὶ Ἰησοῦ τοῦ Ναζαρηνοῦ,ὃς ἐγένετο ἀνὴρ προφήτης δυνατὸς ἐν ἔργῳ καὶ λόγῳ ἐναντίον τοῦ θεοῦ καὶ παντὸς τοῦ λαοῦ·
- TH: พระองค์ตรัสถามว่า «เรื่องอะไร?» พวกเขาทูลว่า «เรื่องของพระเยซูชาวนาซาเร็ธ ผู้เป็นผู้เผยพระวจนะทรงฤทธิ์ทั้งในด้านการกระทำและถ้อยคำต่อพระพักตร์พระเจ้าและต่อหน้าประชาชนทั้งปวง
- Key decisions:
  - Ποῖα → เรื่องอะไร — uW figs-explicit: Ποῖα 'what-kind' (not just Τί 'what') acknowledges significance. Thai เรื่องอะไร natural follow-up-question.
  - Ἰησοῦ τοῦ Ναζαρηνοῦ → พระเยซูชาวนาซาเร็ธ — uW translate-names: Ναζαρηνός 'Nazarene' = from-Nazareth. Thai ชาวนาซาเร็ธ standard (LUK 4:34 + 18:37 precedent). Divine-honorific พระ- prefix retained for Jesus-proper-noun per glossary, even though the disciples h...
  - ἀνὴρ προφήτης δυνατὸς ἐν ἔργῳ καὶ λόγῳ → ผู้เผยพระวจนะทรงฤทธิ์ทั้งในด้านการกระทำและถ้อยคำ — uW figs-idiom: ἀνὴρ προφήτης = 'distinguished prophet.' uW figs-metonymy: ἔργῳ καὶ λόγῳ = deeds-and-words. προφήτης → ผู้เผยพระวจนะ glossary-standard (LUK 20:6 precedent). δυνατός → ทรงฤทธิ์ — Thai captures the powe...
  - ἐναντίον τοῦ θεοῦ καὶ παντὸς τοῦ λαοῦ → ต่อพระพักตร์พระเจ้าและต่อหน้าประชาชนทั้งปวง — uW figs-metaphor: ἐναντίον 'before' = 'in-the-sight-of' — God empowered + the people witnessed. Thai ต่อพระพักตร์ (divine-register 'before-God-face') + ต่อหน้า (human 'before-face-of'). Split the preposition to pres...
- Notes: CLEOPAS'S CHRISTOLOGY: at this point the two disciples view Jesus as 'prophet, mighty in work and word' — Moses-like or Elijah-like category (cf. Deut 18:15, 1 Ki 17:24). This is short-of-the-full-confession-of-Messiah-risen-from-dead, yet accurate-as-far-as-it-goes. Luke's narrative-method: let characters speak from their limited-perspective,...

**Luke 24:20**
- GR: ὅπως τε παρέδωκαν αὐτὸν οἱ ἀρχιερεῖς καὶ οἱ ἄρχοντες ἡμῶν εἰς κρίμα θανάτου καὶ ἐσταύρωσαν αὐτόν.
- TH: และพวกหัวหน้าปุโรหิตและผู้ปกครองของเราได้มอบพระองค์ไว้ให้ถูกพิพากษาประหาร และตรึงพระองค์บนกางเขนอย่างไร
- Key decisions:
  - οἱ ἀρχιερεῖς καὶ οἱ ἄρχοντες ἡμῶν → พวกหัวหน้าปุโรหิตและผู้ปกครองของเรา — uW figs-exclusive: ἡμῶν 'our' = fellow-Jews (Cleopas identifying self + companion as Jewish). ἀρχιερεύς → หัวหน้าปุโรหิต glossary-standard (LUK 22:52/66 precedent). ἄρχων → ผู้ปกครอง standard.
  - παρέδωκαν & εἰς κρίμα θανάτου → ได้มอบพระองค์ไว้ให้ถูกพิพากษาประหาร — uW figs-metonymy: 'judgment of death' = death-sentence from the Romans. παραδίδωμι 'hand-over' — the same verb used for Judas's betrayal, now for the Sanhedrin's handing-to-Pilate. Thai มอบไว้ให้ถูกพิพากษาประหาร pre...
  - ἐσταύρωσαν αὐτόν → ตรึงพระองค์บนกางเขน — uW figs-synecdoche: 'they crucified' — Jewish leaders named as agents even though Romans performed the execution (they set-in-motion). Thai ตรึงพระองค์บนกางเขน matches LUK 23:33 precedent.
- Notes: CLEOPAS'S NARRATIVE: compresses LUK 22:54-23:49 into a single-sentence — Sanhedrin-delivery → Roman-sentencing → crucifixion. The 'our' (ἡμῶν) confessional-marker: Cleopas takes collective-responsibility on behalf of Israel even though specific actors were the leaders. THEOLOGICAL-ECHO: Peter will say nearly-the-same-thing at Acts 2:23 + 3:15 ...

**Luke 24:21**
- GR: ἡμεῖς δὲ ἠλπίζομεν ὅτι αὐτός ἐστιν ὁ μέλλων λυτροῦσθαι τὸν Ἰσραήλ·ἀλλά γε καὶ σὺν πᾶσιν τούτοις τρίτην ταύτην ἡμέραν ἄγει ἀφ’ οὗ ταῦτα ἐγένετο.
- TH: แต่พวกเราเคยหวังว่าพระองค์คือผู้ที่จะไถ่อิสราเอล ยิ่งกว่านั้น วันนี้ก็เป็นวันที่สามแล้วตั้งแต่เหตุการณ์เหล่านี้เกิดขึ้น
- TH-summary: คำว่า «เคยหวัง» (ἠλπίζομεν — รูปอดีตกาลไม่สมบูรณ์) สะท้อนความหวังที่ดับไปแล้ว พวกเขาคาดหมายว่าพระเมสสิยาห์จะปลดแอกชนชาติอิสราเอลจากจักรวรรดิโรมัน แต่พอเห็นพระองค์สิ้นพระชนม์บนกางเขน ความหวังของพวกเขาก็ดับลง ทั้งที่พระเยซูเคยสอนไว้ชัดว่าพระเมสสิยาห์ต้องทนทุกข์ก่อนแล้วจึงเข้าสู่พระสิริ (เทียบ ข้อ 26)
- Key decisions:
  - ἡμεῖς & ἠλπίζομεν → พวกเราเคยหวัง — uW figs-exclusive: 'we' = Cleopas + companion + fellow-disciples (excluding Jesus-addressed). ἐλπίζω imperfect 'were-hoping' — imperfect captures ongoing-then-dashed hope. Thai เคยหวัง preserves the past-but-no-long...
  - ὁ μέλλων λυτροῦσθαι τὸν Ἰσραήλ → ผู้ที่จะไถ่อิสราเอล — uW figs-metaphor: λυτρόω 'ransom, redeem, buy-back' — from slavery-metaphor. In Jewish-messianic-expectation: political-liberation from Rome + spiritual-restoration. Thai ไถ่ captures the ransom-redeem sense standar...
  - τρίτην ταύτην ἡμέραν ἄγει → วันนี้ก็เป็นวันที่สามแล้ว — uW figs-explicit + translate-ordinal: 'this third day' — Jewish reckoning, Friday-to-Sunday inclusive. The disciples note-the-day as implicit-challenge — three-days-dead-is-permanent-in-their-experience. Thai วันที่...
- Notes: MESSIANIC-EXPECTATION: the disciples hoped for political-liberation (cf. Acts 1:6 'restore the kingdom to Israel'). Their hope-dashed-by-crucifixion is Luke's narrative-truth: they had the right Messiah but the wrong expectation. The imperfect-tense ἠλπίζομεν 'we-were-hoping' signals past-tense hope — they no-longer-hope. THREE-DAYS-ALREADY: C...

**Luke 24:22**
- GR: ἀλλὰ καὶ γυναῖκές τινες ἐξ ἡμῶν ἐξέστησαν ἡμᾶς·γενόμεναι ὀρθριναὶ ἐπὶ τὸ μνημεῖον,
- TH: ยิ่งกว่านั้น พวกผู้หญิงบางคนในกลุ่มของเราก็ทำให้พวกเราประหลาดใจ เพราะพวกเธอได้ไปที่อุโมงค์แต่เช้ามืด
- Key decisions:
  - γυναῖκές τινες ἐξ ἡμῶν → พวกผู้หญิงบางคนในกลุ่มของเรา — 'Some women of-us' = women-disciples in the broader Jesus-following group. Thai พวกผู้หญิงบางคนในกลุ่มของเรา preserves the community-membership sense.
  - ἐξέστησαν ἡμᾶς → ทำให้พวกเราประหลาดใจ — ἐξίστημι aor 'astonish, astound.' Thai ทำให้ประหลาดใจ natural for causative-amazement.
  - γενόμεναι ὀρθριναὶ ἐπὶ τὸ μνημεῖον → พวกเธอได้ไปที่อุโมงค์แต่เช้ามืด — HAPAX: ὀρθρινός 'early-morning' adjective — NT-unique. Cognate of ὄρθρος (v.1). Thai เช้ามืด preserves the pre-dawn timing. μνημεῖον → อุโมงค์ consistent within-chapter.
- Notes: HAPAX: ὀρθρινός — NT-unique adjective, from ὄρθρος-root (cf. v.1 ὄρθρου βαθέως). Classical attestation (Homer, later-Koine) for early-rising or pre-dawn. Cleopas repeats-by-reference the same-morning-event — narrative-confirmation that the women's report was circulating. COMMUNITY-COMPOSITION: ἐξ ἡμῶν 'of our-group' shows that the disciple-com...

**Luke 24:23**
- GR: καὶ μὴ εὑροῦσαι τὸ σῶμα αὐτοῦ,ἦλθον λέγουσαι καὶ ὀπτασίαν ἀγγέλων ἑωρακέναι,οἳ λέγουσιν αὐτὸν ζῆν.
- TH: เมื่อไม่พบพระศพของพระองค์แล้ว ก็มาเล่าว่าพวกเธอได้เห็นนิมิตของทูตสวรรค์ ซึ่งกล่าวว่าพระองค์ทรงพระชนม์อยู่
- Key decisions:
  - ὀπτασίαν ἀγγέλων → นิมิตของทูตสวรรค์ — ὀπτασία 'vision' — a divine-seeing. ἄγγελος → ทูตสวรรค์ glossary-standard (LUK 1:11/26, 2:9/13 precedent). The word ἀγγέλων clarifies what v.4 called ἄνδρες 'men' — from the women's now-interpreted perspective, they...
  - οἳ λέγουσιν αὐτὸν ζῆν → ซึ่งกล่าวว่าพระองค์ทรงพระชนม์อยู่ — ζῶν 'living' present-active-ptc. Divine-register ทรง- prefix for divine-subject alive-state. Thai ทรงพระชนม์อยู่ preserves the honorific 'hold-royal-life' construction standard for divine-subjects (cf. LUK 20:38 pre...
- Notes: ANGELS-NAMED: Cleopas uses ἀγγέλων 'angels' where Luke at v.4 called them ἄνδρες 'men.' The women's report has categorized them as angels (consistent with their dazzling-apparel and post-facto recognition). Luke preserves both framings — ἄνδρες from the narrator's what-was-seen, ἀγγέλων from the disciples' what-was-understood. No contradiction...

**Luke 24:24**
- GR: καὶ ἀπῆλθόν τινες τῶν σὺν ἡμῖν ἐπὶ τὸ μνημεῖον,καὶ εὗρον οὕτως καθὼς καὶ αἱ γυναῖκες εἶπον,αὐτὸν δὲ οὐκ εἶδον.
- TH: บางคนในพวกเราได้ไปที่อุโมงค์ และพบเป็นอย่างที่พวกผู้หญิงบอก แต่ไม่ได้เห็นพระองค์»
- Key decisions:
  - τινες τῶν σὺν ἡμῖν → บางคนในพวกเรา — uW figs-explicit: 'some of those with us' = fellow-male-disciples, confirming v.12 (Peter) and parallel to JHN 20:3 (Peter + beloved-disciple). Thai บางคนในพวกเรา.
  - εὗρον οὕτως καθὼς καὶ αἱ γυναῖκες εἶπον → พบเป็นอย่างที่พวกผู้หญิงบอก — uW figs-explicit: confirmed the women's report — empty-tomb found-as-described. Thai เป็นอย่างที่...บอก natural confirmation-formula.
  - αὐτὸν & οὐκ εἶδον → แต่ไม่ได้เห็นพระองค์ — uW writing-pronouns: αὐτόν = Jesus. The disciples-who-went saw the empty-tomb but not Jesus himself (they preceded the Emmaus-encounter). Thai แต่ไม่ได้เห็นพระองค์. Honorific พระองค์ retained even in negative-constr...
- Notes: CORROBORATING-WITNESSES: Cleopas's narrative-conclusion — the apostles confirmed the empty-tomb but saw no-risen-Jesus. This matches v.12 (Peter alone) + JHN 20:3-10 (Peter + beloved-disciple). Luke's Cleopas-plural reconciles: 'some went,' not just Peter. The final 'but him-they-did-not-see' is the narrative-hinge — and Luke's dramatic-irony:...

**Luke 24:25**
- GR: καὶ αὐτὸς εἶπεν πρὸς αὐτούς·Ὦ ἀνόητοι καὶ βραδεῖς τῇ καρδίᾳ τοῦ πιστεύειν ἐπὶ πᾶσιν οἷς ἐλάλησαν οἱ προφῆται·
- TH: พระองค์ตรัสกับพวกเขาว่า «โอ คนโง่เขลาและเชื่อช้าในใจต่อทุกสิ่งที่พวกผู้เผยพระวจนะได้กล่าวเอ๋ย
- Key decisions:
  - Ὦ ἀνόητοι → โอ คนโง่เขลา — uW figs-nominaladj: ἀνόητος 'without-understanding' used as noun. Thai คนโง่เขลา captures the foolish-without-understanding category. Ὦ vocative-exclamation → โอ. The rebuke is affectionate-stern, not contemptuous.
  - βραδεῖς τῇ καρδίᾳ τοῦ πιστεύειν → เชื่อช้าในใจ — uW figs-metaphor + figs-metonymy: καρδία = mind/inner-self; βραδύς 'slow.' Thai เชื่อช้าในใจ preserves the slow-of-heart Hebraism — idiomatic-translation retains the biblical-rhetoric.
  - ἐπὶ πᾶσιν οἷς ἐλάλησαν οἱ προφῆται → ต่อทุกสิ่งที่พวกผู้เผยพระวจนะได้กล่าว — προφήτης → ผู้เผยพระวจนะ glossary-standard (LUK 1:70, 7:16, 20:6 precedent). Thai ต่อทุกสิ่งที่...ได้กล่าว natural for scope-of-prophetic-speech.
- Notes: JESUS'S REBUKE: the first-post-resurrection-teaching is a correction of hermeneutical-blindness. The disciples failed to connect the Messianic-suffering-prophecies (Isa 53, Psa 22, etc.) with the Messianic-glory-prophecies (Isa 9, Psa 110, etc.). Their category-error was to expect the second without the first. SLOW-OF-HEART is a Hebraism (cf. ...

**Luke 24:26**
- GR: οὐχὶ ταῦτα ἔδει παθεῖν τὸν χριστὸν καὶ εἰσελθεῖν εἰς τὴν δόξαν αὐτοῦ;
- TH: พระคริสต์จำเป็นต้องทนทุกข์เช่นนี้ก่อนจะเข้าสู่พระสิริของพระองค์ มิใช่หรือ?»
- TH-summary: นี่เป็นการเปิดเผยครั้งสำคัญในพันธสัญญาใหม่ว่า «การทนทุกข์ก่อนพระสิริ» เป็นแบบแผนที่พระเจ้าทรงกำหนดไว้ล่วงหน้าสำหรับพระเมสสิยาห์ — การสิ้นพระชนม์บนกางเขนไม่ได้เป็นความพ่ายแพ้แต่เป็นเส้นทางจำเป็นสู่พระสิริ เปาโลจะขยายความเรื่องนี้ในฟีลิปปี 2:6-11 ว่าการถ่อมพระองค์ลงสู่ความตายนำไปสู่การที่พระเจ้าทรงยกพระองค์ขึ้น
- Key decisions:
  - οὐχὶ & ἔδει παθεῖν τὸν χριστὸν → พระคริสต์จำเป็นต้องทนทุกข์ & มิใช่หรือ — uW figs-rquestion: rhetorical question = statement. δεῖ 'it-was-necessary' — divine-necessity. πάσχω 'suffer' → ทนทุกข์ natural. χριστός → พระคริสต์ glossary-standard. Thai จำเป็นต้อง...มิใช่หรือ preserves the quest...
  - καὶ εἰσελθεῖν εἰς τὴν δόξαν αὐτοῦ → ก่อนจะเข้าสู่พระสิริของพระองค์ — uW grammar-connect-logic-result: 'enter glory' is the result-goal of the suffering. Thai ก่อนจะเข้าสู่ makes the sequence temporal-logical explicit for Thai-reader comprehension. δόξα → พระสิริ glossary-standard (LU...
- Notes: THE CHRISTOLOGICAL-KEY: the suffering-then-glory pattern is the hermeneutical-lens for reading the OT about the Messiah. Luke returns to this at v.46; Peter uses the same formula at Acts 3:18; Paul at Phil 2:6-11; the author of Hebrews at Heb 12:2. This verse is the single-most-load-bearing statement about OT Christology in the NT — Jesus hims...

**Luke 24:27**
- GR: καὶ ἀρξάμενος ἀπὸ Μωϋσέως καὶ ἀπὸ πάντων τῶν προφητῶν διερμήνευσεν αὐτοῖς ἐν πάσαις ταῖς γραφαῖς τὰ περὶ ἑαυτοῦ.
- TH: แล้วพระองค์ทรงเริ่มอธิบายให้พวกเขาฟังตั้งแต่งานเขียนของโมเสสและผู้เผยพระวจนะทั้งปวง ทรงอธิบายข้อความเกี่ยวกับพระองค์ในพระคัมภีร์ทั้งสิ้น
- TH-summary: พระเยซูทรงอธิบายว่าพระคัมภีร์เดิมทั้งหมด — ทั้งพระบัญญัติ (ของโมเสส) และหนังสือผู้เผยพระวจนะ — ชี้ถึงพระองค์ทั้งสิ้น นี่เป็นบทเรียนเฮอร์เมนิวติกส์ครั้งแรกของคริสเตียน ที่พระเยซูเองทรงสอน: พระคัมภีร์เดิมต้องอ่านในแสงสว่างของพระคริสต์
- Key decisions:
  - ἀρξάμενος ἀπὸ Μωϋσέως καὶ ἀπὸ πάντων τῶν προφητῶν → ทรงเริ่ม...ตั้งแต่งานเขียนของโมเสสและผู้เผยพระวจนะทั้งปวง — uW figs-metonymy: 'Moses' = Pentateuch; 'the prophets' = Prophets section of Hebrew canon. Thai งานเขียนของ (writings-of) makes the metonymy-of-author-for-writings explicit for Thai readers. Μωϋσῆς → โมเสส standard ...
  - διερμήνευσεν αὐτοῖς ἐν πάσαις ταῖς γραφαῖς τὰ περὶ ἑαυτοῦ → ทรงอธิบายข้อความเกี่ยวกับพระองค์ในพระคัมภีร์ทั้งสิ้น — διερμηνεύω 'interpret, explain thoroughly' — διά-intensive. Thai ทรงอธิบาย divine-register. γραφαί → พระคัมภีร์ standard. τὰ περὶ ἑαυτοῦ 'the things concerning himself' → ข้อความเกี่ยวกับพระองค์. Thai reflexive beco...
- Notes: COMPREHENSIVE-CHRISTOLOGICAL-HERMENEUTIC: Jesus interprets the whole-OT christologically — Moses (Pentateuch) + Prophets (Former + Latter Prophets) + by extension all-Scriptures. This verse is foundational for understanding NT-use-of-OT. Specific passages Jesus likely walked through on the seven-mile road include (typical candidates): Gen 3:15...

**Luke 24:28**
- GR: Καὶ ἤγγισαν εἰς τὴν κώμην οὗ ἐπορεύοντο,καὶ αὐτὸς προσεποιήσατο πορρώτερον πορεύεσθαι.
- TH: เมื่อพวกเขาเข้าใกล้หมู่บ้านที่จะไปนั้น พระองค์ทรงทำทีว่าจะเสด็จต่อไปอีก
- Key decisions:
  - ἤγγισαν εἰς τὴν κώμην οὗ ἐπορεύοντο → พวกเขาเข้าใกล้หมู่บ้านที่จะไปนั้น — uW figs-verbs: the first 'they' is Jesus + two, the second 'they' is the two-disciples-only — they-were-going. Thai smoothes this ambiguity by treating both as the-group.
  - αὐτὸς προσεποιήσατο πορρώτερον πορεύεσθαι → พระองค์ทรงทำทีว่าจะเสด็จต่อไปอีก — DOUBLE-HAPAX: προσποιέομαι 'pretend, make-as-if' + πορρώτερον 'further-on' (comparative-adv of πόρρω). uW figs-explicit: Jesus acted-as-if continuing, not verbal-deception — he kept walking when they turned off. Tha...
- Notes: DOUBLE-HAPAX: προσποιέομαι + πορρώτερον — both NT-unique, both found here. προσποιέομαι (LSJ: 'lay-claim, feign, pretend') has a slight 'acting-as-if' sense without necessarily-full-deception. πορρώτερον is the comparative-adverb 'further' (from πόρρω). Jesus 'made-as-if' continuing — not deceiving-with-words, but by-continuing-to-walk when th...

**Luke 24:29**
- GR: καὶ παρεβιάσαντο αὐτὸν λέγοντες·Μεῖνον μεθ’ ἡμῶν,ὅτι πρὸς ἑσπέραν ἐστὶν καὶ κέκλικεν ἤδη ἡ ἡμέρα.καὶ εἰσῆλθεν τοῦ μεῖναι σὺν αὐτοῖς.
- TH: แต่พวกเขาทูลเชิญพระองค์อย่างจริงจังว่า «เชิญพักกับพวกเราเถิด เพราะใกล้ค่ำแล้ว วันกำลังจะหมด» พระองค์จึงเสด็จเข้าไปพักกับพวกเขา
- Key decisions:
  - παρεβιάσαντο αὐτὸν → ทูลเชิญพระองค์อย่างจริงจัง — παραβιάζομαι 'urge strongly, constrain.' uW figs-ellipsis: urge-to-do-what = stay-overnight. Thai ทูลเชิญ...อย่างจริงจัง preserves honorific-speech-to-Jesus + intensity-of-request.
  - Μεῖνον μεθ’ ἡμῶν → เชิญพักกับพวกเราเถิด — μένω aor-imp 'remain.' uW figs-exclusive: ἡμῶν 'us' excludes Jesus (the-two-speaking-to-Jesus-about-themselves). Thai เชิญ polite-invitation + พัก 'stay-lodge' + เถิด polite-imperative-softener.
  - πρὸς ἑσπέραν ἐστὶν καὶ κέκλικεν ἤδη ἡ ἡμέρα → ใกล้ค่ำแล้ว วันกำลังจะหมด — uW figs-parallelism + figs-metonymy: two phrases = same-meaning (evening-arriving + day-declining). κλίνω 'bend-down' = sun-setting. uW figs-explicit: implies safety-concern (night-travel dangerous). Thai preserves ...
  - εἰσῆλθεν τοῦ μεῖναι σὺν αὐτοῖς → พระองค์จึงเสด็จเข้าไปพักกับพวกเขา — Divine-register เสด็จ for Jesus-movement. Purpose-articular-infinitive → เพื่อพัก (pared to พัก).
- Notes: HOSPITALITY-TEST-PASSED: the disciples' insistence is the Mediterranean-hospitality-norm (cf. Gen 19:3 Lot-Sodom, Gen 18:3 Abraham-oaks-of-Mamre). Without pressing, the stranger would have moved-on. Luke's narrative-theology: fellowship-with-risen-Jesus requires-invitation — hospitality-as-faith-evidence. This will matter again when the meal d...

**Luke 24:30**
- GR: καὶ ἐγένετο ἐν τῷ κατακλιθῆναι αὐτὸν μετ’αὐτῶν λαβὼν τὸν ἄρτον εὐλόγησεν καὶ κλάσας ἐπεδίδου αὐτοῖς·
- TH: ขณะที่พระองค์ทรงเอนพระกายเสวยกับพวกเขา พระองค์ทรงหยิบขนมปัง ทรงอวยพร ทรงหัก แล้วประทานให้พวกเขา
- TH-summary: ท่าทีสี่อย่าง — หยิบ อวยพร หัก ประทาน — เป็นแบบเดียวกับที่พระเยซูทรงทำในการเลี้ยงห้าพันคน (ลูกา 9:16) และในพิธีมหาสนิท (ลูกา 22:19) ท่าทีนี้เองที่ทำให้สาวกจำพระองค์ได้ — แสดงว่าพระเยซูทรงเผยพระองค์ในพิธีกรรมที่คริสเตียนจะทำเพื่อระลึกถึงพระองค์
- Key decisions:
  - ἐν τῷ κατακλιθῆναι αὐτὸν μετ’ αὐτῶν → ขณะที่พระองค์ทรงเอนพระกายเสวยกับพวกเขา — uW translate-unknown: κατακλίνω 'recline' — Mediterranean banqueting-posture on couches. Thai ทรงเอนพระกาย divine-register + เสวย (royal-eating verb) preserves the meal-taking honorific. The pair ทรงเอนพระกายเสวย is...
  - λαβὼν τὸν ἄρτον εὐλόγησεν καὶ κλάσας ἐπεδίδου αὐτοῖς → พระองค์ทรงหยิบขนมปัง ทรงอวยพร ทรงหัก แล้วประทานให้พวกเขา — FOUR-STEP EUCHARISTIC-FORMULA: λαβών (took) + εὐλόγησεν (blessed) + κλάσας (broke) + ἐπεδίδου (was-giving). Deliberately-parallel to LUK 9:16 (feeding-5000) and LUK 22:19 (last supper). Divine-register ทรง- on each ...
- Notes: EUCHARISTIC-ECHO: the four-step-formula (λαβών + εὐλόγησεν + κλάσας + ἐπεδίδου) deliberately-echoes LUK 9:16 (feeding-of-5000) and LUK 22:19 (institution of the Lord's Supper). Luke is signaling that the risen-Jesus is revealed in the breaking-of-bread — the eucharistic-recognition-pattern. The four-actions are the shape-of-Christian-worship a...

**Luke 24:31**
- GR: αὐτῶν δὲ διηνοίχθησαν οἱ ὀφθαλμοί,καὶ ἐπέγνωσαν αὐτόν·καὶ αὐτὸς ἄφαντος ἐγένετο ἀπ’αὐτῶν.
- TH: แล้วตาของพวกเขาก็สว่างขึ้น พวกเขาจำพระองค์ได้ แต่พระองค์ทรงหายจากสายตาของพวกเขา
- TH-summary: เหตุการณ์นี้เป็นภาพสะท้อนของ ข้อ 16 ที่ «ตาของพวกเขาถูกปิดไว้» — ตอนนี้ตาของพวกเขาถูกเปิดออก การเปิดเผยนี้ทำโดยพระเจ้า ไม่ใช่โดยความพยายามของมนุษย์ พระเยซูทรงหายจากสายตาหลังจากที่พวกเขาจำได้ แสดงว่าภารกิจของพระองค์กับทั้งสองสิ้นสุดแล้ว — แต่การประทับอยู่ของพระองค์ในการหักขนมปังนั้นคงอยู่สำหรับคริสตจักรในทุกยุค
- Key decisions:
  - αὐτῶν & διηνοίχθησαν οἱ ὀφθαλμοί → ตาของพวกเขาก็สว่างขึ้น — uW figs-metonymy + figs-activepassive: διανοίγω aor-pass 'were-opened' — divine-passive, God-opens. ὀφθαλμοί = understanding (per uW). Thai ตา...สว่างขึ้น preserves the metaphor: eyes-become-bright = recognition-daw...
  - ἐπέγνωσαν αὐτόν → พวกเขาจำพระองค์ได้ — ἐπιγινώσκω aor 'recognized fully.' Thai จำได้ (recognize) standard. Paired-reversal with v.16 οὐκ ἐπιγνῶναι.
  - αὐτὸς ἄφαντος ἐγένετο ἀπ’ αὐτῶν → พระองค์ทรงหายจากสายตาของพวกเขา — HAPAX: ἄφαντος 'invisible, vanishing.' uW figs-idiom: not 'remained-invisible-in-room' but 'suddenly-no-longer-there.' Divine-register ทรง-. Thai หายจากสายตา natural for sudden-vanishing.
- Notes: HAPAX: ἄφαντος — NT-unique. Classical: unseen, out-of-sight. NOT the same as invisible-but-present; Jesus left suddenly. RECOGNITION-STRUCTURE: Luke pairs v.16 (eyes-held-from-recognition) ↔ v.31 (eyes-opened + disappearance). The narrative-symmetry confirms divine-orchestration of the encounter. THEOLOGICAL-SIGNIFICANCE: recognition comes at ...

**Luke 24:32**
- GR: καὶ εἶπαν πρὸς ἀλλήλους·Οὐχὶ ἡ καρδία ἡμῶν καιομένη ἦν ὡς ἐλάλει ἡμῖν ἐν τῇ ὁδῷ,ὡς διήνοιγεν ἡμῖν τὰς γραφάς;
- TH: พวกเขาพูดกันว่า «ใจของเราร้อนรุ่มอยู่ภายในไม่ใช่หรือ ขณะที่พระองค์ตรัสกับเราตามทาง และทรงเปิดพระคัมภีร์ให้เรา?»
- Key decisions:
  - Οὐχὶ ἡ καρδία ἡμῶν καιομένη ἦν → ใจของเราร้อนรุ่มอยู่ภายในไม่ใช่หรือ — uW figs-rquestion + figs-metaphor: 'was-not-our-heart burning' = was-not-excitement-burning-within-us. uW figs-possession: singular-heart-shared retained as collective-metaphor. Thai ใจของเราร้อนรุ่ม preserves the h...
  - ὡς ἐλάλει ἡμῖν ἐν τῇ ὁδῷ → ขณะที่พระองค์ตรัสกับเราตามทาง — Divine-register ตรัส for Jesus-speech. Thai ตามทาง natural for 'on-the-road.'
  - ὡς διήνοιγεν ἡμῖν τὰς γραφάς → และทรงเปิดพระคัมภีร์ให้เรา — uW figs-metaphor: διανοίγω 'open' used metaphorically for 'explain.' Thai ทรงเปิด preserves the metaphor and is consistent Thai-Christian usage (cf. 'เปิดใจ' open-heart, 'เปิดตา' open-eyes). γραφή → พระคัมภีร์ gloss...
- Notes: RETROSPECTIVE-RECOGNITION: the two disciples realize in-hindsight that Jesus's Scripture-opening was itself the sign they missed. The heart-burning is the ongoing spiritual-confirmation that they ignored while their eyes-were-held. Luke's lesson: the Spirit's-inward-witness + the Scripture's-outward-witness work together — Emmaus-Road is the p...

**Luke 24:33**
- GR: καὶ ἀναστάντες αὐτῇ τῇ ὥρᾳ ὑπέστρεψαν εἰς Ἰερουσαλήμ,καὶ εὗρον ἠθροισμένους τοὺς ἕνδεκα καὶ τοὺς σὺν αὐτοῖς,
- TH: ในชั่วโมงนั้นเอง พวกเขาก็ลุกขึ้นกลับไปยังกรุงเยรูซาเล็ม พบว่าสาวกสิบเอ็ดคนกับพวกที่อยู่กับพวกเขาชุมนุมกันอยู่
- Key decisions:
  - αὐτῇ τῇ ὥρᾳ → ในชั่วโมงนั้นเอง — uW figs-idiom: 'at-the-same hour' = at-once. Thai ในชั่วโมงนั้นเอง preserves the immediacy. Despite evening-already-falling (v.29), they leave immediately — the news cannot wait.
  - ἀναστάντες → ลุกขึ้น — uW figs-idiom: taking-initiative. Thai ลุกขึ้น here signals the physical + resolve combination.
  - εὗρον ἠθροισμένους τοὺς ἕνδεκα → พบว่าสาวกสิบเอ็ดคน...ชุมนุมกันอยู่ — HAPAX: ἀθροίζω 'gather, assemble' — NT-unique. Thai ชุมนุมกัน captures the gathering. Perf-pass-ptc 'having-been-gathered' — they-stayed-together. τοὺς ἕνδεκα → สาวกสิบเอ็ดคน consistent with v.9.
- Notes: HAPAX: ἀθροίζω — NT-unique (though cognate ἀθρόος and later ἀθροισμός are attested in Koine). The Eleven are assembled in defensive-fellowship after the trauma. The Emmaus-travelers break into this gathered-community with their news. NARRATIVE-TIMING: 11 km/night-travel + evening-already-falling means the Emmaus-pair walk back in darkness, on ...

**Luke 24:34**
- GR: λέγοντας ὅτι ὄντως ἠγέρθη ὁ κύριος καὶ ὤφθη Σίμωνι.
- TH: ที่กำลังพูดกันว่า «องค์พระผู้เป็นเจ้าทรงเป็นขึ้นแล้วจริง ๆ และทรงปรากฏแก่ซีโมนด้วย»
- TH-summary: การปรากฏพระองค์แก่ซีโมน (เปโตร) เป็นเหตุการณ์ที่เปาโลกล่าวถึงใน 1 โครินธ์ 15:5 ด้วย ว่าพระเยซูทรงปรากฏแก่ «เคฟาส» (ซีโมนในภาษาอาราเมค) ก่อนอัครทูตสิบสอง — เป็นการปรากฏที่ไม่มีรายละเอียดในพระกิตติคุณเล่มใด แต่ถูกอ้างอิงเพื่อยืนยันว่าเปโตรเป็นพยานเห็นพระองค์โดยตรง
- Key decisions:
  - ὄντως ἠγέρθη ὁ κύριος → องค์พระผู้เป็นเจ้าทรงเป็นขึ้นแล้วจริง ๆ — uW figs-activepassive: divine-passive ἠγέρθη. ὁ κύριος used by the-disciples for Jesus — post-resurrection-title emerging. Thai องค์พระผู้เป็นเจ้า matches glossary-standard for κύριος when divine-title (RULES §4 pre...
  - ὤφθη Σίμωνι → ทรงปรากฏแก่ซีโมน — ὁράω aor-pass 'was-seen' = appeared-to (idiomatic-Christophany). Thai ทรงปรากฏแก่ divine-register standard. Σίμων → ซีโมน standard (LUK 4:38 + 5:3-10 + 7:40-44 + 22:31 precedent).
- Notes: FIRST APPEARANCE TO PETER: mentioned here + at 1 Cor 15:5 ('appeared-to Cephas'). No details recorded in any gospel — private-appearance perhaps to restore Peter after the denial. This appearance preceded the Emmaus-appearance but is reported by the assembled-group AFTER the Emmaus-pair arrive — signaling Peter's-encounter was already common-k...

**Luke 24:35**
- GR: καὶ αὐτοὶ ἐξηγοῦντο τὰ ἐν τῇ ὁδῷ,καὶ ὡς ἐγνώσθη αὐτοῖς ἐν τῇ κλάσει τοῦ ἄρτου.
- TH: สาวกสองคนนั้นจึงเล่าเหตุการณ์ที่เกิดขึ้นระหว่างทาง และเล่าว่าพวกเขาจำพระองค์ได้อย่างไรในตอนที่ทรงหักขนมปัง
- Key decisions:
  - αὐτοὶ ἐξηγοῦντο τὰ ἐν τῇ ὁδῷ → สาวกสองคนนั้นจึงเล่าเหตุการณ์ที่เกิดขึ้นระหว่างทาง — uW figs-ellipsis: 'the things on-the-road' = what-happened-during-the-journey. ἐξηγέομαι 'narrate, describe in detail' — root of 'exegesis.' Thai เล่าเหตุการณ์ natural.
  - ὡς ἐγνώσθη αὐτοῖς ἐν τῇ κλάσει τοῦ ἄρτου → พวกเขาจำพระองค์ได้อย่างไรในตอนที่ทรงหักขนมปัง — uW figs-activepassive + figs-metonymy: divine-passive + metonymic 'breaking-of-the-bread' for the-bread-breaking-moment-as-act-of-recognition. Thai ในตอนที่ทรงหักขนมปัง makes the revealing-moment specific. จำได้ rec...
- Notes: FORMULA 'THE BREAKING OF THE BREAD': κλάσις τοῦ ἄρτου becomes the early-Christian-technical-term for the eucharist (cf. Acts 2:42 τῇ κλάσει τοῦ ἄρτου; Acts 20:7 κλάσαι ἄρτον). Luke's first-use-here creates the expression. The Emmaus-episode thus BECOMES the paradigm for what the Church will do: gather, hear Scripture opened, break bread, recog...

**Luke 24:36**
- GR: Ταῦτα δὲ αὐτῶν λαλούντων αὐτὸς ἔστη ἐν μέσῳ αὐτῶν.
- TH: ขณะที่พวกเขากำลังเล่าเรื่องเหล่านี้อยู่ พระองค์เองก็เสด็จมาประทับยืนอยู่ท่ามกลางพวกเขา
- TH-summary: SBLGNT ไม่มีวลี «ทรงตรัสแก่พวกเขาว่า ‹สันติสุขจงมีแก่พวกท่าน›» ซึ่งปรากฏในฉบับ NA28/BSB/KJV/THSV ฉบับเอเรมอสเลือกตามต้นฉบับวิจารณ์ SBLGNT (สำนวนสั้น) พบในพยาน Codex Bezae (D) และฉบับลาตินโบราณ — เป็นหนึ่งใน «Western non-interpolations» ที่มีการโต้แย้งกันมาหลายศตวรรษ
- Key decisions:
  - Ταῦτα δὲ αὐτῶν λαλούντων → ขณะที่พวกเขากำลังเล่าเรื่องเหล่านี้อยู่ — Genitive-absolute temporal-ptc. Thai ขณะที่...กำลัง...อยู่ natural continuous-action.
  - αὐτὸς ἔστη ἐν μέσῳ αὐτῶν → พระองค์เองก็เสด็จมาประทับยืนอยู่ท่ามกลางพวกเขา — uW figs-rpronouns: αὐτός emphatic 'he-himself.' Thai พระองค์เอง. ἵστημι aor-act 'stood.' Divine-register เสด็จมา + ประทับยืน (honorific standing). ἐν μέσῳ 'in the midst' → ท่ามกลาง glossary-standard.
- Notes: TEXTUAL VARIANT (SBLGNT vs NA28): SBLGNT ends this verse at αὐτῶν with no peace-greeting. NA28 reads αὐτὸς ἔστη ἐν μέσῳ αὐτῶν [καὶ λέγει αὐτοῖς· Εἰρήνη ὑμῖν] — 'and he said to them, Peace be with you' — in single brackets. BSB, ESV, NIV, CSB, KJV, THSV all include the peace-greeting. Witnesses-omit include Codex Bezae (D), Old Latin (a b d e f...

**Luke 24:37**
- GR: πτοηθέντες δὲ καὶ ἔμφοβοι γενόμενοι ἐδόκουν πνεῦμα θεωρεῖν.
- TH: พวกเขาตกใจและหวาดกลัว คิดว่าเห็นวิญญาณ
- Key decisions:
  - πτοηθέντες & καὶ ἔμφοβοι γενόμενοι → ตกใจและหวาดกลัว — uW figs-doublet: πτοέω 'startle' + ἔμφοβος γίνομαι 'become-terrified' — near-synonym doublet for intensification. Thai ตกใจและหวาดกลัว preserves both with natural-Thai pair.
  - ἐδόκουν πνεῦμα θεωρεῖν → คิดว่าเห็นวิญญาณ — uW figs-explicit + note: πνεῦμα in this context = 'ghost/spirit-of-dead-person,' not Holy Spirit. Thai วิญญาณ appropriate for ghost-sense (disambiguated from พระวิญญาณ Holy Spirit). They thought they saw-a-disembodi...
- Notes: πνεῦμα = GHOST: Thai disambiguates cleanly — วิญญาณ (disembodied-spirit / ghost) vs. พระวิญญาณ (divine-Spirit, always-with-phra-honorific). No confusion with pneumatology here. BACKGROUND: popular-1st-century Jewish-belief in post-mortem-appearances (cf. LUK 9:19 Jesus-as-Elijah/prophet-returned) — the disciples' category-error is treating the...

**Luke 24:38**
- GR: καὶ εἶπεν αὐτοῖς·Τί τεταραγμένοι ἐστέ,καὶ διὰ τί διαλογισμοὶ ἀναβαίνουσιν ἐν τῇ καρδίᾳ ὑμῶν;
- TH: พระองค์ตรัสกับพวกเขาว่า «เหตุใดพวกท่านจึงตระหนกใจ? และเหตุใดความสงสัยจึงเกิดขึ้นในใจของพวกท่าน?
- Key decisions:
  - Τί τεταραγμένοι ἐστέ → เหตุใดพวกท่านจึงตระหนกใจ — uW figs-rquestion: rhetorical 'why-troubled' = challenge-and-reassure. ταράσσω perf-pass-ptc 'have-been-troubled.' Thai ตระหนกใจ preserves the startled-anxiety register.
  - διὰ τί διαλογισμοὶ ἀναβαίνουσιν ἐν τῇ καρδίᾳ ὑμῶν → เหตุใดความสงสัยจึงเกิดขึ้นในใจของพวกท่าน — uW figs-metaphor + figs-explicit: διαλογισμοί 'reasonings, doubts' — in this context = doubts-about-resurrection. ἀναβαίνω 'come up, arise' — metaphor of thoughts surfacing. καρδία = mind. Thai ความสงสัย (doubts) + ...
- Notes: JESUS'S PASTORAL-DIAGNOSTIC: before proving bodily-resurrection, he names the disciples' inner-state — troubled-hearts + surfacing-doubts. Not dismissive (the fears are natural response to ghost-hypothesis) but redirective — the evidence will follow (vv.39-43). Note Thai ใจ (mind/heart) serves double-duty like Greek καρδία.

**Luke 24:39**
- GR: ἴδετε τὰς χεῖράς μου καὶ τοὺς πόδας μου,ὅτι ἐγώ εἰμι αὐτός·ψηλαφήσατέ με καὶ ἴδετε,ὅτι πνεῦμα σάρκα καὶ ὀστέα οὐκ ἔχει καθὼς ἐμὲ θεωρεῖτε ἔχοντα.
- TH: จงดูมือและเท้าของเราเถิด ว่าเป็นเราเอง จงจับตัวเราและพิจารณาดูเถิด เพราะวิญญาณไม่มีเนื้อและกระดูกอย่างที่พวกท่านเห็นว่าเรามี»
- TH-summary: พระเยซูทรงเสนอหลักฐานสองอย่างเพื่อพิสูจน์ว่าพระองค์ไม่ใช่วิญญาณ — การมองเห็นรอยตะปูที่มือและเท้า และการสัมผัสตรวจด้วยมือ นี่เป็นข้อพระคัมภีร์หลักที่สอนว่าการคืนพระชนม์ของพระเยซูเป็นการคืนพระชนม์ทางกาย (physical/bodily resurrection) ไม่ใช่เพียงจิตวิญญาณอย่างที่ลัทธิอื่น ๆ บางลัทธิสอน
- Key decisions:
  - ἴδετε τὰς χεῖράς μου καὶ τοὺς πόδας μου → จงดูมือและเท้าของเราเถิด — uW figs-metonymy: hands + feet = nail-mark-locations from crucifixion. Thai มือและเท้า direct. NOTE: divine-register-dilemma — normally divine-subjects-body-parts use พระหัตถ์ (royal-hand) + พระบาท (royal-foot), but...
  - ἐγώ εἰμι αὐτός → ว่าเป็นเราเอง — uW figs-rpronouns: αὐτός emphatic 'myself.' Thai เราเอง preserves the self-affirmation. NOT the ἐγώ εἰμι absolute-self-designation (Yahweh-echo) as in JHN 8:58; here the αὐτός clarifies it is predicative-I-myself.
  - ψηλαφήσατέ με → จงจับตัวเรา — ψηλαφάω 'touch, handle, feel' — tactile-examination. Thai จับตัว natural imperative for bodily-touch.
  - πνεῦμα σάρκα καὶ ὀστέα οὐκ ἔχει → วิญญาณไม่มีเนื้อและกระดูก — uW figs-merism: σάρξ + ὀστέον 'flesh + bones' = the-physical-body-as-whole, merism. Thai เนื้อ (flesh) + กระดูก (bones) standard pair. Note: bones (ὀστέα) not standard 'blood' — Jesus chooses bones deliberately. σάρ...
- Notes: HAPAX: ὀστέα — nominative-accusative plural of ὀστέον 'bone' — NT-unique in this form (related forms attested but this exact morphology is unique here). BODILY-RESURRECTION DOCTRINE: this verse is the foundational-text for Christian teaching that Jesus's resurrection was physical-bodily, NOT spiritual-only. Later heresies (Gnosticism, Docetism...

**Luke 24:40**
- GR: καὶ τοῦτο εἰπὼν ἔδειξεν αὐτοῖς τὰς χεῖρας καὶ τοὺς πόδας.
- TH: เมื่อตรัสดังนั้นแล้ว พระองค์ก็ทรงสำแดงมือและเท้าให้พวกเขาดู
- Key decisions:
  - τοῦτο εἰπὼν → เมื่อตรัสดังนั้นแล้ว — Divine-register ตรัส for Jesus-speech. Aor-ptc → เมื่อ...แล้ว natural.
  - ἔδειξεν αὐτοῖς τὰς χεῖρας καὶ τοὺς πόδας → พระองค์ก็ทรงสำแดงมือและเท้าให้พวกเขาดู — δείκνυμι 'show, display.' Divine-register ทรงสำแดง. Thai สำแดง standard for divine-showing/revealing-display. มือ + เท้า plain-form consistent with v.39 (physical-proof context).
- Notes: TEXTUAL-NOTE: v.40 is a third Western-non-interpolation candidate. Codex Bezae (D) + Old Latin omit. SBLGNT, NA28, and majority of uncials INCLUDE. Our project renders per SBLGNT's inclusion — no separate-footnote needed since SBLGNT + NA28 + BSB agree. Compare JHN 20:20 for parallel-display to the apostolic-group (JHN also adds 'his side' whe...

**Luke 24:41**
- GR: ἔτι δὲ ἀπιστούντων αὐτῶν ἀπὸ τῆς χαρᾶς καὶ θαυμαζόντων,εἶπεν αὐτοῖς·Ἔχετέ τι βρώσιμον ἐνθάδε;
- TH: ขณะที่พวกเขายังไม่เชื่อเพราะความยินดีและความอัศจรรย์ใจ พระองค์ตรัสกับพวกเขาว่า «ที่นี่พวกท่านมีอะไรรับประทานบ้างไหม?»
- Key decisions:
  - ἔτι & ἀπιστούντων αὐτῶν ἀπὸ τῆς χαρᾶς καὶ θαυμαζόντων → ขณะที่พวกเขายังไม่เชื่อเพราะความยินดีและความอัศจรรย์ใจ — uW figs-doublet + figs-explicit: ἀπιστούντες + θαυμάζοντες = disbelief-from-too-good-to-believe overlap. ἀπὸ τῆς χαρᾶς 'from joy' = because-of-the-joy. Thai ยังไม่เชื่อเพราะความยินดีและความอัศจรรย์ใจ preserves all t...
  - Ἔχετέ τι βρώσιμον ἐνθάδε → ที่นี่พวกท่านมีอะไรรับประทานบ้างไหม — HAPAX: βρώσιμος 'eatable, edible.' uW alternate: 'anything to eat.' Thai อะไรรับประทานบ้าง natural. ἐνθάδε 'here' → ที่นี่. Question-form ไหม natural polite-inquiry.
- Notes: HAPAX: βρώσιμος — NT-unique adjective from βρῶσις-root. Ordinary-Koine usage = edible-food. JOY-THAT-MAKES-IT-HARD-TO-BELIEVE: an emotionally-true observation — the news-too-good-to-be-true triggers initial-skepticism. Jesus responds with the most-mundane-demonstration possible: eating. Ghosts don't eat. PHYSICALITY-PROOF-#2: after showing-mar...

**Luke 24:42**
- GR: οἱ δὲ ἐπέδωκαν αὐτῷ ἰχθύος ὀπτοῦ μέρος·
- TH: พวกเขาก็ถวายปลาย่างชิ้นหนึ่งแด่พระองค์
- Key decisions:
  - ἐπέδωκαν αὐτῷ → พวกเขาก็ถวาย...แด่พระองค์ — ἐπιδίδωμι 'hand-over, give-to.' Thai ถวาย (royal-give) + แด่พระองค์ divine-register — disciples handing-something to divine-person.
  - ἰχθύος ὀπτοῦ μέρος → ปลาย่างชิ้นหนึ่ง — HAPAX: ὀπτός 'roasted, broiled.' ἰχθύς → ปลา standard (LUK 5:6/9, 9:13/16, 11:11 precedent). Thai ปลาย่าง (fish-roasted) natural pair. μέρος 'part, piece' → ชิ้นหนึ่ง.
- Notes: HAPAX: ὀπτός — NT-unique adjective, classical-Greek for roasted/broiled over fire. The specific-detail (not just 'fish' but 'broiled fish' — ready-to-eat, cooked) signals concrete-reality — a historical-detail embedded in the narrative, not generic. TEXTUAL-NOTE: Byzantine mss add καὶ ἀπὸ μελισσίου κηρίου 'and some honey-comb' here — SBLGNT/NA...

**Luke 24:43**
- GR: καὶ λαβὼν ἐνώπιον αὐτῶν ἔφαγεν.
- TH: พระองค์ทรงรับ และเสวยต่อหน้าพวกเขา
- Key decisions:
  - λαβὼν & ἔφαγεν → ทรงรับ และเสวย — Divine-register throughout: ทรงรับ (royal-receive) + เสวย (royal-eat). uW figs-explicit: the eating-in-their-sight proves physical-body. ἐσθίω aor-3sg 'ate.'
  - ἐνώπιον αὐτῶν → ต่อหน้าพวกเขา — uW figs-metaphor: 'in-front-of-them' = 'where-they-could-see.' Thai ต่อหน้า standard.
- Notes: PHYSICAL-PROOF-CAPSTONE: eating-before-witnesses — the strongest-proof-of-bodily-nature imaginable. Luke's narrative-argument is complete: see (marks) + touch (flesh/bones) + observe (eating) = not-a-ghost. This passage remains foundational for Christian doctrine of bodily-resurrection (cf. Acts 10:41 'us-who-ate-and-drank with-him after-he-rose').

**Luke 24:44**
- GR: εἶπεν δὲ πρὸς αὐτούς·Οὗτοι οἱ λόγοι μου οὓς ἐλάλησα πρὸς ὑμᾶς ἔτι ὢν σὺν ὑμῖν,ὅτι δεῖ πληρωθῆναι πάντα τὰ γεγραμμένα ἐν τῷ νόμῳ Μωϋσέως καὶ τοῖς προφήταις καὶ ψαλμοῖς περὶ ἐμοῦ.
- TH: พระองค์ตรัสกับพวกเขาว่า «นี่คือถ้อยคำที่เราได้กล่าวแก่พวกท่านเมื่อเรายังอยู่กับพวกท่าน ว่าทุกสิ่งที่เขียนไว้เกี่ยวกับเราในธรรมบัญญัติของโมเสส ในหนังสือผู้เผยพระวจนะ และในสดุดี จะต้องสำเร็จ»
- TH-summary: พระเยซูทรงอ้างถึงโครงสร้างสามส่วนของพระคัมภีร์ฮีบรู — ธรรมบัญญัติ (โทราห์ของโมเสส), ผู้เผยพระวจนะ (เนวิอิม), และหนังสือเขียน (เคทูวิม ซึ่งพระองค์ทรงใช้ชื่อหนังสือเล่มใหญ่ที่สุดคือ «สดุดี» แทนทั้งส่วน) — ซึ่งทั้งหมดชี้ถึงพระองค์ นี่คือครั้งแรกในพันธสัญญาใหม่ที่มีการอ้างถึงโครงสร้างสามส่วนนี้อย่างชัดเจน
- Key decisions:
  - Οὗτοι οἱ λόγοι μου → นี่คือถ้อยคำที่เราได้กล่าว — uW figs-metonymy: 'my words' = what-I-said. Thai นี่คือถ้อยคำที่...ได้กล่าว natural. Note ราชาศัพท์ suspended because Jesus is speaking-about-himself (first-person — we use plain self-designation เรา with ทรง-form r...
  - ἔτι ὢν σὺν ὑμῖν → เมื่อเรายังอยู่กับพวกท่าน — uW alternate: 'when-I-was-with-you before.' Thai เมื่อเรายังอยู่กับพวกท่าน natural — the 'before' implicit-in the stil-with contrast with now-risen.
  - δεῖ πληρωθῆναι πάντα τὰ γεγραμμένα → ทุกสิ่งที่เขียนไว้...จะต้องสำเร็จ — uW figs-activepassive + figs-abstractnouns: δεῖ + aor-pass-inf 'must-be-fulfilled.' Thai จะต้องสำเร็จ preserves necessity + fulfillment. γέγραπται → เขียนไว้ standard.
  - ἐν τῷ νόμῳ Μωϋσέως καὶ τοῖς προφήταις καὶ ψαλμοῖς → ในธรรมบัญญัติของโมเสส ในหนังสือผู้เผยพระวจนะ และในสดุดี — uW figs-merism + figs-synecdoche: 'Law + Prophets + Psalms' = whole-Hebrew-Bible (Torah + Nevi'im + Ketuvim, with Psalms representing Writings). First-NT-three-fold-reference to the Hebrew canon-structure. Thai ธรรม...
- Notes: FIRST EXPLICIT THREE-FOLD CANON REFERENCE: Law (Torah = Genesis-Deuteronomy) + Prophets (Nevi'im = Joshua-Malachi minus Daniel) + Psalms (representing Ketuvim = Writings). This is the earliest-NT-evidence of the three-fold-structure of the Hebrew Bible, a structure attested in Prologue to Sirach (c. 132 BC) and 4QMMT (Qumran). Jesus confirms t...

**Luke 24:45**
- GR: τότε διήνοιξεν αὐτῶν τὸν νοῦν τοῦ συνιέναι τὰς γραφάς,
- TH: แล้วพระองค์ทรงเปิดความคิดของพวกเขาให้เข้าใจพระคัมภีร์
- Key decisions:
  - διήνοιξεν αὐτῶν τὸν νοῦν → พระองค์ทรงเปิดความคิดของพวกเขา — uW figs-idiom: διανοίγω 'open' — enable-understanding. Thai ทรงเปิด divine-register. νοῦς 'mind, understanding' → ความคิด natural (cf. 'เปิดใจ/เปิดความคิด' idiomatic). Same verb (διήνοιξεν) used at v.32 for opening-...
  - τοῦ συνιέναι τὰς γραφάς → ให้เข้าใจพระคัมภีร์ — συνίημι 'understand, comprehend.' Articular-infinitive-of-purpose → ให้เข้าใจ. γραφαί → พระคัมภีร์ standard.
- Notes: THREE-FOLD OPENING: v.31 ὀφθαλμοί (eyes-opened for recognition) + v.32 γραφαί (scriptures-opened for explanation) + v.45 νοῦς (mind-opened for understanding). Luke's deliberate-triad: physical-seeing + textual-discernment + cognitive-grasp are all-divinely-enabled. This is Luke's pneumatology-in-embryo — what-will-become the Spirit-opening-eye...

**Luke 24:46**
- GR: καὶ εἶπεν αὐτοῖς ὅτι οὕτως γέγραπται παθεῖν τὸν χριστὸν καὶ ἀναστῆναι ἐκ νεκρῶν τῇ τρίτῃ ἡμέρᾳ,
- TH: พระองค์ตรัสกับพวกเขาว่า «ตามที่เขียนไว้ พระคริสต์จะต้องทนทุกข์และทรงเป็นขึ้นมาจากตายในวันที่สาม
- TH-summary: พระเยซูทรงสรุปแก่นของพยากรณ์เกี่ยวกับพระเมสสิยาห์ที่กระจายอยู่ในพระคัมภีร์เดิม — ทนทุกข์ (สะท้อนอิสยาห์ 53, สดุดี 22) แล้วคืนพระชนม์ในวันที่สาม (สะท้อนโฮเชยา 6:2, สดุดี 16:10) นี่ไม่ใช่การอ้างข้อพระคัมภีร์ข้อใดข้อหนึ่งโดยเฉพาะ แต่เป็นการสรุปเส้นของคำพยากรณ์หลายข้อที่ประกอบกัน
- Key decisions:
  - οὕτως γέγραπται → ตามที่เขียนไว้ — uW figs-activepassive: γράφω perf-pass 'it-is-written.' Thai ตามที่เขียนไว้ standard formula for scripture-reference.
  - παθεῖν τὸν χριστὸν → พระคริสต์จะต้องทนทุกข์ — uW figs-synecdoche: πάσχω here summarizes the full-passion (betrayal + suffering + death). Thai ทนทุกข์ glossary-standard (LUK 22:15, 24:26 precedent). χριστός → พระคริสต์ standard.
  - ἀναστῆναι ἐκ νεκρῶν τῇ τρίτῃ ἡμέρᾳ → ทรงเป็นขึ้นมาจากตายในวันที่สาม — ἀνίστημι aor-inf 'rise.' Thai ทรงเป็นขึ้นมา divine-register + จากตาย (from-dead). uW figs-nominaladj: τῶν νεκρῶν 'the-dead' as noun group. τρίτῃ ἡμέρᾳ per v.7 pattern.
- Notes: META-PROPHETIC-SUMMARY: Jesus is not quoting a specific OT text but summarizing-the-composite-witness of Moses + Prophets + Psalms on suffering + resurrection. The composite-reading assembles: Isa 52:13-53:12 (suffering-servant), Psa 22 (crucifixion-details), Psa 16:10 (not-left-in-Sheol), Hos 6:2 (third-day-resurrection), Jonah 1:17 (three-da...

**Luke 24:47**
- GR: καὶ κηρυχθῆναι ἐπὶ τῷ ὀνόματι αὐτοῦ μετάνοιαν εἰς ἄφεσιν ἁμαρτιῶν εἰς πάντα τὰ ἔθνη—ἀρξάμενοι ἀπὸ Ἰερουσαλήμ·
- TH: และจะมีการประกาศในพระนามของพระองค์ เรื่องการกลับใจเพื่อการยกโทษบาปแก่ชนทุกชาติ โดยเริ่มต้นจากกรุงเยรูซาเล็ม
- TH-summary: ข้อนี้เป็นคำสั่งมอบภารกิจ (Great Commission) ฉบับลูกา — ที่จะขยายต่อไปในกิจการของอัครทูต โครงสร้างการแผ่ขยายคือ «เริ่มจากเยรูซาเล็ม — ยูเดีย — สะมาเรีย — สุดปลายแผ่นดินโลก» (กิจการ 1:8) การกลับใจ (การเปลี่ยนความคิด หันกลับจากบาป) และการยกโทษบาปเป็นข่าวประเสริฐที่ต้องประกาศในพระนามของพระเยซู
- Key decisions:
  - κηρυχθῆναι → จะมีการประกาศ — uW figs-activepassive: κηρύσσω aor-pass-inf 'be-proclaimed.' Thai จะมีการประกาศ preserves passive-impersonal form.
  - ἐπὶ τῷ ὀνόματι αὐτοῦ → ในพระนามของพระองค์ — uW figs-metonymy: 'in his name' = on-his-authority. Thai ในพระนามของพระองค์ divine-register standard.
  - μετάνοιαν εἰς ἄφεσιν ἁμαρτιῶν → การกลับใจเพื่อการยกโทษบาป — RULES §4 glossary-required: μετάνοια → การกลับใจ; ἄφεσις → การยกโทษ (not การอภัย; though aliased interchangeably per glossary). Thai เพื่อ preserves the εἰς-purpose (for-the-purpose-of). ἁμαρτία → บาป glossary-stand...
  - εἰς πάντα τὰ ἔθνη → แก่ชนทุกชาติ — uW figs-metonymy: ἔθνη = ethnic-groups, nations. Thai ชนทุกชาติ standard for all-nations. Matches Eremos MAT 28:19 precedent (Great Commission). ชน (people) + ชาติ (ethnic-group/nation) pair.
  - ἀρξάμενοι ἀπὸ Ἰερουσαλήμ → โดยเริ่มต้นจากกรุงเยรูซาเล็ม — uW figs-explicit: plural-participle ἀρξάμενοι refers to disciples (implicit-imperative). Thai โดยเริ่มต้นจาก natural sequential-connector. Ἰερουσαλήμ → กรุงเยรูซาเล็ม standard.
- Notes: GREAT-COMMISSION-LUKAN-FORM: Luke's version of the Great Commission — different accent than MAT 28:19-20 (baptize + disciple) or MRK 16:15 (preach gospel) or JHN 20:21-23 (sending + Spirit + forgiving). Luke's distinctive: μετάνοια + ἄφεσις ἁμαρτιῶν as gospel-content, ἔθνη as scope, Ἰερουσαλήμ as starting-point. These three parameters PERFECTL...

**Luke 24:48**
- GR: ὑμεῖς μάρτυρες τούτων.
- TH: พวกท่านเป็นพยานของสิ่งเหล่านี้
- Key decisions:
  - ὑμεῖς μάρτυρες τούτων → พวกท่านเป็นพยานของสิ่งเหล่านี้ — μάρτυς → พยาน standard. uW figs-explicit: 'witnesses of these things' = firsthand-experience + commissioned-testifiers. Emphatic ὑμεῖς pronoun → พวกท่าน (fronted).
- Notes: WITNESS-THEME: μάρτυς is foundational for Luke-Acts — the disciples are authorized-witnesses, not interpreters. Acts 1:8 echoes: 'you-shall-be-my-witnesses' (ἔσεσθε μου μάρτυρες). Acts 1:21-22 sets witness-criterion for Matthias: someone present-from-John's-baptism-to-the-ascension, witness-to-the-resurrection. The apostolic-foundation is eyew...

**Luke 24:49**
- GR: καὶ ἰδοὺ ἐγὼ ἐξαποστέλλω τὴν ἐπαγγελίαν τοῦ πατρός μου ἐφ’ὑμᾶς·ὑμεῖς δὲ καθίσατε ἐν τῇ πόλει ἕως οὗ ἐνδύσησθε ἐξ ὕψους δύναμιν.
- TH: ดูเถิด เราจะส่งพระสัญญาของพระบิดาของเรามาเหนือพวกท่าน แต่พวกท่านจงคอยอยู่ในกรุงนี้ก่อน จนกว่าจะได้รับฤทธิ์เดชจากเบื้องบนสวมทับตัว
- TH-summary: «พระสัญญาของพระบิดา» หมายถึงพระวิญญาณบริสุทธิ์ที่พระเจ้าทรงสัญญาไว้ในพันธสัญญาเดิม (เช่น โยเอล 2:28-32 ที่เปโตรจะอ้างในเทศนาวันเพ็นเทคอสต์ — กิจการ 2:17-21) คำว่า «สวมทับ» เป็นภาพเปรียบเสื้อผ้า — ฤทธิ์เดชของพระเจ้าจะห่อหุ้มตัวสาวกดุจเสื้อผ้า เหตุการณ์นี้จะเกิดขึ้นในวันเพ็นเทคอสต์สิบวันหลังจากการเสด็จขึ้นสู่สวรรค์
- Key decisions:
  - ἰδοὺ ἐγὼ ἐξαποστέλλω → ดูเถิด เราจะส่ง — uW: ἰδού = attention-marker. ἐξαποστέλλω 'send-out-from' — intensive. Present-futuristic 'I-am-sending.' Thai ดูเถิด เราจะส่ง natural. Emphatic ἐγώ fronted.
  - τὴν ἐπαγγελίαν τοῦ πατρός μου → พระสัญญาของพระบิดาของเรา — uW figs-explicit: 'promise of the Father' = Holy Spirit. Thai พระสัญญาของพระบิดา — divine-register พระ-prefix on both nouns. πατήρ → พระบิดา glossary-standard (LUK 22:29 precedent).
  - καθίσατε ἐν τῇ πόλει → พวกท่านจงคอยอยู่ในกรุงนี้ก่อน — uW figs-imperative + figs-explicit: καθίζω aor-imp-emphatic 'stay-seated' = remain. Thai จงคอยอยู่...ก่อน preserves imperative + emphatic-stay-first. ἡ πόλις = Jerusalem (per v.47) → กรุงนี้ (this-city-referring-bac...
  - ἕως οὗ ἐνδύσησθε & δύναμιν → จนกว่าจะได้รับฤทธิ์เดชจากเบื้องบนสวมทับตัว — uW figs-metaphor: ἐνδύω 'clothe' — power-as-garment metaphor. Thai ได้รับ...สวมทับตัว preserves the clothing-putting-on metaphor naturally. δύναμις → ฤทธิ์เดช glossary-standard (LUK 1:17, 4:14, 21:27 precedent).
  - ἐξ ὕψους → จากเบื้องบน — uW figs-metonymy: 'from-on-high' = from-heaven/God. Thai จากเบื้องบน (from-above) preserves the spatial-heavenly metaphor without flattening to 'from-God.' This matches later-NT language and Thai Christian usage.
- Notes: PRELUDE TO ACTS: this verse is the pivot from Luke's gospel to Acts — the same promise appears at Acts 1:4 + 1:8 (ἐπαγγελίαν τοῦ πατρός + δύναμιν + Holy-Spirit). Pentecost is the fulfillment (Acts 2). 'Clothed with power from on high' — metaphor of empowerment as garment (cf. Isa 61:10, Rom 13:14 Paul's 'put-on Christ'). THEOLOGICAL: Jesus is ...

**Luke 24:50**
- GR: Ἐξήγαγεν δὲ αὐτοὺς ἕως πρὸς Βηθανίαν,καὶ ἐπάρας τὰς χεῖρας αὐτοῦ εὐλόγησεν αὐτούς.
- TH: พระองค์ทรงนำพวกเขาออกไปจนถึงหมู่บ้านเบธานี แล้วทรงยกพระหัตถ์อวยพรพวกเขา
- TH-summary: การยกมืออวยพรเป็นท่าทีของปุโรหิตในพันธสัญญาเดิม — พระเยซูในฐานะมหาปุโรหิตองค์สุดท้าย (ฮีบรู 7) ทรงจบพันธกิจภาคพื้นโลกด้วยการอวยพรประชาชนของพระเจ้า ดุจเดียวกับอาโรนที่อวยพรอิสราเอลด้วยท่าทีเดียวกัน (กันดารวิถี 6:22-27)
- Key decisions:
  - Ἐξήγαγεν & αὐτοὺς ἕως πρὸς Βηθανίαν → พระองค์ทรงนำพวกเขาออกไปจนถึงหมู่บ้านเบธานี — ἐξάγω aor-act-3sg 'led-out.' Divine-register ทรงนำ. Βηθανία → หมู่บ้านเบธานี (with หมู่บ้าน村 for clarity — cf. LUK 19:29, MRK 11:1, MAT 21:17 precedent).
  - ἐπάρας τὰς χεῖρας αὐτοῦ εὐλόγησεν αὐτούς → ทรงยกพระหัตถ์อวยพรพวกเขา — uW translate-symaction: ἐπαίρω + χεῖρας = priestly-blessing-gesture (cf. Num 6:23-27 Aaronic benediction). Divine-register ทรงยกพระหัตถ์ (royal-hand honorific — appropriate here because blessing-gesture is royal-pri...
- Notes: PRIESTLY-BLESSING-GESTURE: raising-hands-to-bless matches Aaronic-practice (Lev 9:22, Num 6:23-27). Jesus fulfills-the-priestly-role as he departs. Luke is framing the ascension as a temple-closing: the high-priest emerges from the holy-place to bless the people. See Heb 7 (Jesus as priest-forever after the order of Melchizedek). Bethany-locat...

**Luke 24:51**
- GR: καὶ ἐγένετο ἐν τῷ εὐλογεῖν αὐτὸν αὐτοὺς διέστη ἀπ’αὐτῶν καὶ ἀνεφέρετο εἰς τὸν οὐρανόν.
- TH: ขณะที่ทรงอวยพรพวกเขาอยู่นั้น พระองค์ก็ทรงแยกจากพวกเขา และถูกรับขึ้นสู่สวรรค์
- TH-summary: การเสด็จขึ้นสู่สวรรค์ (Ascension) เป็นเหตุการณ์ที่ลูกาบันทึกในที่เดียวของพระกิตติคุณทั้งสี่ ลูกาจะเล่าเหตุการณ์นี้อีกครั้งในกิจการ 1:9-11 โดยขยายรายละเอียดเกี่ยวกับทูตสวรรค์ที่ประกาศว่า «พระเยซูจะเสด็จกลับมาในลักษณะเดียวกัน» คำว่า «ถูกรับขึ้น» (รูปกรรมวาจก) แสดงว่าพระเจ้าพระบิดาทรงเป็นผู้ทรงยกพระองค์ขึ้น
- Key decisions:
  - ἐν τῷ εὐλογεῖν αὐτὸν αὐτοὺς → ขณะที่ทรงอวยพรพวกเขาอยู่นั้น — Present-articular-infinitive temporal 'while-he-was-blessing.' Divine-register ทรงอวยพร continues from v.50. Thai ขณะที่...อยู่นั้น natural contemporaneous.
  - διέστη ἀπ’ αὐτῶν → พระองค์ก็ทรงแยกจากพวกเขา — διΐστημι aor 'stand-apart, separate.' Divine-register ทรงแยก. Thai แยกจาก natural separation.
  - ἀνεφέρετο εἰς τὸν οὐρανόν → และถูกรับขึ้นสู่สวรรค์ — uW figs-activepassive: ἀναφέρω impf-pass 'was-being-carried-up' — divine-passive (God takes up). Thai ถูกรับขึ้น preserves passive-voice + divine-agency-implied. οὐρανός → สวรรค์ standard.
- Notes: TEXTUAL-NOTE: v.51 is a fourth Western-non-interpolation candidate — Codex Bezae (D), Sinaitic-Syriac (sy^s), Old Latin (a, b, d, e, ff², l) OMIT the clause καὶ ἀνεφέρετο εἰς τὸν οὐρανόν 'and was carried up into heaven.' SBLGNT + NA28 + BSB all INCLUDE. Our project renders per SBLGNT. The Western-omission may reflect harmonization-concern (why...

**Luke 24:52**
- GR: καὶ αὐτοὶ προσκυνήσαντες αὐτὸν ὑπέστρεψαν εἰς Ἰερουσαλὴμ μετὰ χαρᾶς μεγάλης,
- TH: พวกเขากราบนมัสการพระองค์ แล้วกลับไปยังกรุงเยรูซาเล็มด้วยความยินดีอย่างยิ่ง
- TH-summary: การนมัสการพระเยซูหลังการเสด็จขึ้นสู่สวรรค์เป็นการแสดงความเชื่อที่พัฒนาอย่างชัดเจน — ก่อนหน้านี้สาวกเคยเรียกพระเยซูว่า «อาจารย์» หรือ «พระเมสสิยาห์» แต่บัดนี้พวกเขากราบนมัสการพระองค์ในฐานะพระเจ้า
- Key decisions:
  - αὐτοὶ προσκυνήσαντες αὐτὸν → พวกเขากราบนมัสการพระองค์ — προσκυνέω → นมัสการ glossary-standard (LUK 4:7/8 precedent). Thai กราบนมัสการ adds the kneeling-prostration dimension natural for divine-worship-Thai. Object αὐτόν → พระองค์ divine-register pronoun.
  - ὑπέστρεψαν εἰς Ἰερουσαλὴμ μετὰ χαρᾶς μεγάλης → แล้วกลับไปยังกรุงเยรูซาเล็มด้วยความยินดีอย่างยิ่ง — ὑποστρέφω aor 'returned.' Thai กลับไปยัง natural. uW figs-abstractnouns: μετὰ χαρᾶς μεγάλης 'with great joy.' Thai ด้วยความยินดีอย่างยิ่ง preserves the intensity.
- Notes: PROSKYNESIS of CHRIST: the disciples now worship Jesus explicitly (προσκυνέω — typically reserved-for-God in biblical-Greek). This is an implicit-high-Christology in Luke's conclusion. The same disciples who at LUK 9:19 categorized Jesus as 'prophet like Elijah' now worship him. The Lukan narrative-arc completes with apostolic-worship-of-Chris...

**Luke 24:53**
- GR: καὶ ἦσαν διὰ παντὸς ἐν τῷ ἱερῷ εὐλογοῦντες τὸν θεόν.
- TH: และเขาทั้งหลายอยู่ในพระวิหารตลอดเวลา พลางสรรเสริญพระเจ้า
- TH-summary: พระกิตติคุณลูกาทั้งเล่มเริ่มต้นที่พระวิหารเมื่อทูตสวรรค์ประกาศแก่เศคาริยาห์ (ลูกา 1:5-23) และจบลงที่พระวิหารเมื่อเหล่าสาวกสรรเสริญพระเจ้าที่นั่น — เป็นโครงสร้างที่เรียกว่า «อินคลูซิโอ» (inclusion) ที่แสดงความสมบูรณ์ของเรื่องเล่า จากนี้ลูกาจะต่อด้วยกิจการของอัครทูต ที่เล่าต่อจากการเสด็จขึ้นสู่สวรรค์
- Key decisions:
  - ἦσαν διὰ παντὸς ἐν τῷ ἱερῷ → อยู่ในพระวิหารตลอดเวลา — uW figs-ellipsis + figs-hyperbole: διὰ παντός 'through-all' = continuously / regularly (hyperbolic-for-emphasis; they were at the temple every-day when-open, not-literally-24/7). uW figs-synecdoche: ἱερόν = whole-te...
  - εὐλογοῦντες τὸν θεόν → พลางสรรเสริญพระเจ้า — uW alternate: 'worshiping God.' εὐλογέω when object-is-God → สรรเสริญ (praise-God) more-natural than อวยพร (bless, which makes less-sense with God-as-object in Thai). Matches Luke 23:47 สรรเสริญพระเจ้า precedent (ce...
- Notes: LUKE'S INCLUSIO: the gospel opens (1:5-23) with Zechariah at the temple; it closes (24:53) with the disciples at the temple. The temple frames the whole-narrative. The disciples remain in Jerusalem (per Jesus's v.49 instruction) awaiting Pentecost — continuing-temple-worship until the Spirit comes and expands their sphere to the ends-of-the-ea...


---


## §D. When you're done

Paste your response back as-is — it will feed into Ben's Claude Code session that produced this packet. Thanks for the review.

---
*Packet generated by Claude Code during Luke end-of-book review (2026-04-23). Project: https://github.com/btwinguitarists/eremos-translation. Checklist: docs/END_OF_BOOK_CHECKLIST.md section 3.*
