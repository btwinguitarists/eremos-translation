# Acts — External AI Sanity-Check Review Packet
**Date assembled: 2026-04-26**

**Paste this entire document into one of:** Grok (free), ChatGPT (free or paid), Gemini 2.5 Pro, Claude. **Then copy the AI's response back to the project's main session.**

---

## PROMPT — read carefully before reviewing

You are performing an **end-of-book external sanity-check** on **Acts** (28 chapters, 1,002 verses) from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes to the project's main session to surface corpus-level concerns that per-chapter automated checks may have missed.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar, natural in modern Thai.
- **Status:** Mark, Matthew complete + tagged; Luke complete (not yet tagged). Acts 28/28 just shipped. Per-chapter automated checks (key-term consistency, back-translation, OT-citation, Greek-field integrity, TNBT structural diff, claim consistency, synoptic alignment, Thai-summary coverage) all pass.

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
- ἀμὴν λέγω ὑμῖν → เราบอกความจริงแก่พวกท่าน(ว่า) — uniform across all dominical solemn pronouncements
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
## Item A — Acts 21 we-passage register elevation

**The pattern:** Luke's four "we-passages" in Acts use Greek 1pl markers (ἡμᾶς / ἡμῶν / ἡμεῖς / ἡμῖν + 1pl verbs). Three of the four blocks render with natural-register Thai 1pl **พวกเรา / เรา**. **Block 3 (Acts 21:1–18) elevates to literary-formal register ข้าพเจ้าทั้งหลาย** in 7 of 7 verses. The verse-level rationale at 21:1 doesn't document the elevation. Within Acts 21:5 the register also mixes ข้าพเจ้าทั้งหลาย and พวกเรา in a single sentence.

**Block 1 (16:10–17) — natural register:**
- Acts 16:10 GK: `ὡς δὲ τὸ ὅραμα εἶδεν, εὐθέως ἐζητήσαμεν ἐξελθεῖν εἰς Μακεδονίαν, συμβιβάζοντες ὅτι προσκέκληται ἡμᾶς ὁ θεὸς εὐαγγελίσασθαι αὐτούς.`
- TH: `เมื่อเปาโลเห็นนิมิตนั้นแล้ว ในทันใดเราก็พยายามที่จะเดินทางไปยังแคว้นมาซิโดเนีย โดยสรุปว่าพระเจ้าทรงเรียกเราให้ประกาศข่าวประเสริฐแก่พวกเขา`

**Block 2 (20:5–15) — natural register:**
- Acts 20:6 GK: `ἡμεῖς δὲ ἐξεπλεύσαμεν μετὰ τὰς ἡμέρας τῶν ἀζύμων ἀπὸ Φιλίππων`
- TH: `ส่วนพวกเรา หลังจากเทศกาลขนมปังไร้เชื้อแล้ว เราก็แล่นเรือออกจากเมืองฟีลิปปี`

**Block 3 (21:1–18) — formal-literary register:**
- Acts 21:1 GK: `Ὡς δὲ ἐγένετο ἀναχθῆναι ἡμᾶς ἀποσπασθέντας ἀπ’αὐτῶν`
- TH: `เมื่อข้าพเจ้าทั้งหลายแยกจากพวกเขาแล้วและออกเรือไป`
- Acts 21:5 GK: `ὅτε δὲ ἐγένετο ἐξαρτίσαι ἡμᾶς τὰς ἡμέρας ... καὶ θέντες τὰ γόνατα ἐπὶ τὸν αἰγιαλὸν`
- TH: `เมื่อข้าพเจ้าทั้งหลายพักอยู่ครบจำนวนวันแล้ว ... แล้วพวกเราคุกเข่าลงที่ชายหาดอธิษฐานร่วมกัน` ← **inner mix**
- Acts 21:11 GK: `καὶ ἐλθὼν πρὸς ἡμᾶς`
- TH: `ท่านเข้ามาหาข้าพเจ้าทั้งหลาย`
- Acts 21:17 GK: `Γενομένων δὲ ἡμῶν εἰς Ἱεροσόλυμα ἀσμένως ἀπεδέξαντο ἡμᾶς οἱ ἀδελφοί.`
- TH: `เมื่อข้าพเจ้าทั้งหลายมาถึงกรุงเยรูซาเล็ม พวกพี่น้องที่นั่นก็ต้อนรับด้วยความยินดี`

**Block 4 (27:1–28:16) — natural register:**
- Acts 27:1 GK: `Ὡς δὲ ἐκρίθη τοῦ ἀποπλεῖν ἡμᾶς εἰς τὴν Ἰταλίαν`
- TH: `เมื่อเป็นอันตัดสินกันแล้วว่าพวกเราจะแล่นเรือไปยังประเทศอิตาลี`
- Acts 28:14 GK: `οὗ εὑρόντες ἀδελφοὺς παρεκλήθημεν παρ’αὐτοῖς ἐπιμεῖναι ἡμέρας ἑπτά·καὶ οὕτως εἰς τὴν Ῥώμην ἤλθαμεν.`
- TH: `ที่นั่นพวกเราพบพี่น้องผู้เชื่อ พวกเขาขอร้องให้พวกเราพักอยู่ด้วยเป็นเวลาเจ็ดวัน แล้วโดยอย่างนั้น พวกเราจึงมาถึงกรุงโรม`

**Question:** Is the Acts 21 elevation defensible (chapter 21 is the most theologically/dramatically charged we-block — prophecy, tearful farewell, formal arrival in Jerusalem, audience with James)? Or is it unmarked register drift to be normalized to พวกเรา? The within-21:5 mix tilts toward "drift."

---

## Item B — ἔθνος three-way contextual split

**The pattern:** 28 occurrences in Acts, principled three-way split:
- **ประชาชาติ** = "nations" cosmic/Psalmic universal scope
- **ชนชาติ** = "nation" as specific people-group (incl. Israel)
- **คนต่างชาติ** = "Gentiles" (Pauline mission target, non-Jews)

**Cleanest example — Acts 26:23 (uses both senses contrastively):**
- GK: `εἰ πρῶτος ἐξ ἀναστάσεως νεκρῶν φῶς μέλλει καταγγέλλειν τῷ τε λαῷ καὶ τοῖς ἔθνεσιν.`
- TH: `และเมื่อทรงเป็นผู้แรกที่ฟื้นจากความตาย พระองค์จะทรงประกาศแสงสว่างแก่ชนชาติของเราและแก่บรรดาคนต่างชาติ»` (λαός→ชนชาติ "the people [of Israel]" vs. ἔθνεσιν→คนต่างชาติ "Gentiles")

**Geopolitical / Psalmic — ประชาชาติ:**
- Acts 4:25 GK: `Ἱνατί ἐφρύαξαν ἔθνη` (Psalm 2 quotation) → TH: `เหตุใดบรรดาประชาชาติจึงเดือดดาลเกรี้ยวกราด`
- Acts 17:26 GK: `ἐποίησέν τε ἐξ ἑνὸς πᾶν ἔθνος ἀνθρώπων` → TH: `จากบุรุษคนเดียว พระองค์ทรงสร้างทุกประชาชาติของมนุษย์`

**Pauline-mission Gentiles — คนต่างชาติ (16 verses, e.g.):**
- Acts 13:46 GK: `ἰδοὺ στρεφόμεθα εἰς τὰ ἔθνη` → TH: `ดูเถิด เราจะหันไปหาคนต่างชาติแล้ว`
- Acts 28:28 GK: `τοῖς ἔθνεσιν ἀπεστάλη τοῦτο τὸ σωτήριον τοῦ θεοῦ` → TH: `ความรอดของพระเจ้านี้ได้ถูกส่งไปยังคนต่างชาติแล้ว`

**ANOMALY — ชนต่างชาติ (literary variant) at 2 verses:**
- Acts 4:27 GK: `σὺν ἔθνεσιν καὶ λαοῖς Ἰσραήλ` → TH: `พร้อมด้วย**ชนต่างชาติ**และประชาชนอิสราเอล` (corporate prayer register)
- Acts 14:27 GK: `ἤνοιξεν τοῖς ἔθνεσιν θύραν πίστεως` → TH: `ทรงเปิดประตูแห่งความเชื่อแก่**ชนต่างชาติ**` (church report register)

**Question:** Is ชนต่างชาติ at 4:27 + 14:27 (vs. คนต่างชาติ at 16 mission-context verses) a defensible literary-elevation in formal-public-prayer + church-report contexts? Or is it unmarked drift to be normalized? Critically: does the three-way split (ประชาชาติ / ชนชาติ / คนต่างชาติ) need a dedicated `docs/translator_decisions/` doc before Pauline epistles (Romans 9–11 will compound)?

---

## Item C — Roman administrative titles (ἀνθύπατος drift)

**The pattern:** Acts is the NT's densest Roman-administrative-vocabulary book. Most titles are uniform. **ἀνθύπατος ("proconsul") has two Thai renderings.** Other titles for reference:

- χιλίαρχος (tribune) → **นายพัน** (12× uniform); e.g., Acts 21:33 GK: `τότε ἐγγίσας ὁ χιλίαρχος ἐπελάβετο αὐτοῦ` → TH: `ครั้นนายพันเข้ามาใกล้ก็จับตัวเปาโล`
- ἑκατοντάρχης (centurion) → **นายร้อย** (11× uniform)
- ἡγεμών (governor — Felix/Festus) → **ผู้ว่าราชการ** (6× uniform); Acts 23:24 → `ผู้ว่าราชการเฟลิกซ์`
- Καῖσαρ (throne-name) → **ซีซาร์** (9× uniform)
- Σεβαστός (Augustus title) → **องค์จักรพรรดิ** (2× uniform); Acts 25:21 GK: `εἰς τὴν τοῦ Σεβαστοῦ διάγνωσιν` → TH: `รอการวินิจฉัยขององค์จักรพรรดิ`
- πρῶτος τῆς νήσου (Publius, Malta) → **หัวหน้าของเกาะ**

**ἀνθύπατος drift (3 occurrences, 2 renderings):**
- Acts 13:8 (Cyprus, Sergius Paulus) GK: `ζητῶν διαστρέψαι τὸν ἀνθύπατον ἀπὸ τῆς πίστεως` → TH: `พยายามจะชักจูง**ผู้สำเร็จราชการ**ให้หันจากความเชื่อ`
- Acts 13:12 GK: `τότε ἰδὼν ὁ ἀνθύπατος τὸ γεγονὸς ἐπίστευσεν` → TH: `เมื่อ**ผู้สำเร็จราชการ**เห็นเหตุการณ์ที่เกิดขึ้นก็เชื่อ`
- Acts 19:38 GK: `ἀγοραῖοι ἄγονται καὶ ἀνθύπατοί εἰσιν` → TH: `ศาลก็เปิดและมี**ผู้ว่าการ**อยู่`

**Question:** ผู้ว่าการ at 19:38 is one syllable shy of ผู้ว่าราชการ (used for ἡγεμών = governor). This may confuse Thai readers between two distinct Roman ranks (proconsul of Cyprus = senatorial-province-governor; governor of Judea = imperial-province-governor; not the same office). Is the specific-vs-generic split (named Sergius Paulus = ผู้สำเร็จราชการ, abstract reference = ผู้ว่าการ) defensible, or should both occurrences normalize to ผู้สำเร็จราชการ?

---

## Item D — Pagan-deity proper-noun policy

**The pattern (already operating, not yet documented at corpus level):**

1. **Pagan-deity register: เทพ / เทพี / เทพเจ้า / เหล่าทวยเทพ** — explicitly NOT พระเจ้า (which is reserved for the biblical God). Crowd at 12:22 (Herod's death) and Maltese natives at 28:6 (Paul not dying from snakebite) say เทพเจ้า — Luke's narrator-theology then corrects in third person.
2. **Transliteration vs. descriptive:** Personal proper-name deities (Zeus, Hermes, Artemis, Castor/Pollux, Moloch, Rephan) get **transliteration**. Abstract/personified-attribute deities (Δίκη "Justice") get **descriptive translation** (เทพีแห่งความยุติธรรม).

**Sample evidence:**
- Acts 12:22 (Herod's death) GK: `Θεοῦ φωνὴ καὶ οὐκ ἀνθρώπου` → TH: `นี่เป็นเสียงของ**เทพเจ้า** ไม่ใช่ของมนุษย์`
- Acts 14:11 (Lystra crowd) GK: `Οἱ θεοὶ ὁμοιωθέντες ἀνθρώποις κατέβησαν πρὸς ἡμᾶς` → TH: `เหล่าทวยเทพได้แปลงกายเป็นมนุษย์และลงมาหาพวกเราแล้ว`
- Acts 14:13 (Zeus priest) GK: `ὅ τε ἱερεὺς τοῦ Διὸς` → TH: `ปุโรหิตของวิหาร**ซีอุส**` (Zeus → ซีอุส transliteration)
- Acts 17:23 (unknown god altar) GK: `βωμὸν ἐν ᾧ ἐπεγέγραπτο·Ἀγνώστῳ θεῷ` → TH: `แท่นบูชาแห่งหนึ่ง ซึ่งจารึกไว้ว่า «**แด่พระเจ้าที่ไม่รู้จัก**»` (NB: this is the inscription's own claim — Paul appropriates it to point to the biblical God; "พระเจ้า" register is the inscription's, not Luke's)
- Acts 19:24 GK: `ποιῶν ναοὺς ἀργυροῦς Ἀρτέμιδος` → TH: `ทำศาลเจ้าเงินรูปของ**เทพีอารเทมิส**`
- Acts 19:27 GK: `τῆς μεγάλης θεᾶς Ἀρτέμιδος` → TH: `**เทพี**อารเทมิสผู้ยิ่งใหญ่` (θεά→เทพี feminine pagan)
- Acts 28:4 (Maltese on Paul) GK: `ἡ δίκη ζῆν οὐκ εἴασεν` → TH: `**เทพีแห่งความยุติธรรม**ก็ไม่ยอมให้เขามีชีวิตอยู่` (Δίκη → descriptive translation)
- Acts 28:6 GK: `μεταβαλόμενοι ἔλεγον αὐτὸν εἶναι θεόν` → TH: `พากันพูดว่าท่านเป็น**เทพเจ้าองค์หนึ่ง**` (a god, polytheistic register)
- Acts 28:11 GK: `Ἀλεξανδρίνῳ,παρασήμῳ Διοσκούροις` → TH: `เป็นเรือจากเมืองอเล็กซานเดรีย มีรูป**ฝาแฝดดิออสคูรี**เป็นเครื่องหมายที่หัวเรือ` (Διόσκουροι → Greek-source transliteration "Dioscuri", NOT Latin Castor/Pollux)

**Two questions:** (1) Is the register (เทพ/เทพี/เทพเจ้า) + transliteration-vs-descriptive split sound? (2) For Acts 28:11 specifically: is keeping the Greek Διόσκουροι→ดิออสคูรี the right call, or should the Thai pivot toward the more-recognizable Latin pair-name "Castor and Pollux" → คาสเตอร์และพอลลักซ์ (which Thai readers may know better through general mythology)?

The corpus has 19 corpus-level decision docs but none for pagan-deity policy. Pauline epistles will compound (1 Cor 8:5–6, 1 Cor 10:14–21, Rom 1:18–25, Gal 4:8–9). Should this become doc #20?

---

## Item E — Praise-verb sub-rule (δοξάζω narrator drift)

**The locked rule:** δοξάζω + εὐλογέω + αἰνέω + αἶνον δίδωμι all default to **สรรเสริญ** when God is the object.

**Compliance examples:**
- Acts 2:47 GK: `αἰνοῦντες τὸν θεὸν` → TH: `**สรรเสริญพระเจ้า**`
- Acts 3:8 GK: `αἰνῶν τὸν θεόν` → TH: `**สรรเสริญพระเจ้า**`

**Sub-pattern (3 verses, all "they glorified God" narrator-context):**
- Acts 4:21 GK: `πάντες ἐδόξαζον τὸν θεὸν ἐπὶ τῷ γεγονότι` → TH: `ทุกคนต่าง**ถวายพระเกียรติแด่พระเจ้า**สำหรับสิ่งที่ได้เกิดขึ้น`
- Acts 11:18 GK: `ἡσύχασαν καὶ ἐδόξασαν τὸν θεὸν` → TH: `เงียบลงและ**ถวายเกียรติแด่พระเจ้า**`
- Acts 21:20 GK: `οἱ δὲ ἀκούσαντες ἐδόξαζον τὸν θεόν` → TH: `เมื่อพวกเขาได้ยินก็**ถวายเกียรติแด่พระเจ้า**`

**Outliers:**
- Acts 13:48 GK: `ἐδόξαζον τὸν λόγον τοῦ κυρίου` → TH: `**เทิดทูน**พระวจนะขององค์พระผู้เป็นเจ้า` (object is "the word," not "God" — defensible)

**Question:** Is δοξάζω → ถวายเกียรติ in narrator-context "they glorified God" a principled doxological-formal sub-rule (the doc allows ถวายพระเกียรติ for "doxological-formal contexts"), or is it inconsistency to be normalized to สรรเสริญ?

---

## Item F — σωτήριον τοῦ θεοῦ Lukan two-volume inclusio

**Verify the Luke-Acts bookend lands cleanly:**
- LUK 2:30 (Simeon) GK: `εἶδον οἱ ὀφθαλμοί μου τὸ σωτήριόν σου` → TH: `นัยน์ตาของข้าพระองค์ได้เห็น**ความรอดของพระองค์**`
- LUK 3:6 (Baptist citing Isa 40:5) GK: `ὄψεται πᾶσα σὰρξ τὸ σωτήριον τοῦ θεοῦ` → TH: `มนุษย์ทุกคนจะเห็น**ความรอดของพระเจ้า**`
- ACT 28:28 (Paul to Roman Jews) GK: `τοῖς ἔθνεσιν ἀπεστάλη τοῦτο τὸ σωτήριον τοῦ θεοῦ` → TH: `**ความรอดของพระเจ้า**นี้ได้ถูกส่งไปยังคนต่างชาติแล้ว`

The verse-level rationale at Acts 28:28 already cross-references Luke 2:30 + 3:6 and explicitly names the inclusio.

**Question:** Does the Thai render preserve the two-volume bookend you'd expect from Luke's Greek? Or is anything lost / would a Thai reader miss the connection?

---

## §Z — Anything else?

If you spot a corpus-level concern outside the items above, flag it briefly. Don't manufacture flags; only mention if you actually see something. **Skip §Z if the items above are your full read.**

---

**End of packet. Output format reminder:** items × {Verdict / Reasoning / Recommended action} + optional §Z.
