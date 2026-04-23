# Luke — End-of-Book Review

**Date:** 2026-04-22
**Scope:** All 24 chapters (1,149 verses); `glossary.json`; `RULES.md`; `docs/translator_decisions/`.
**Trigger:** LUK 24 shipped 2026-04-22 (PR #295, build 133); per `docs/END_OF_BOOK_CHECKLIST.md`.

## Summary

- **22 cross-cutting items reviewed** — 15 from internal review (2026-04-22) + 4 Gemini-flagged items (2026-04-23) + 6 Claude-flagged items (2026-04-23), with overlap folded in.
- **9 new decision docs written** across three passes (see §§1, 2, 6, 16, 17).
- **4 translation spot-revisions**: LUK 10:13 (μετανοέω), LUK 1:77 (ἄφεσις), LUK 10:17 (Κύριε vocative), LUK 10:20 (οὐρανός parallelism).
- **1 RULES.md update** — §5 Luke 24 WNI enumeration (v0.4).
- **8 items stable / already documented** — no corpus-level change needed.
- **4 items flagged for Ben's attention** (see final section).
- **Mechanical items (§1 of checklist): all pass** post-revision — 0 key-term-consistency violations, 0 Greek-field-integrity hard fails on touched chapters (LUK 1, 10), `git status output/` tracks only the expected edits.

Status codes: **LOCKED** (stable + corpus-doc). **STABLE** (uniform + rationale implicit at verse-level; documented here). **REVIEW** (worth Ben's confirmation). **DECIDE** (Ben choice needed).

---

## 1. ὁ κύριος narrator-voice referring to Jesus — **LOCKED (new doc this review)**

Luke's signature — the narrator uniquely calls Jesus "the Lord" in third person (Mark and Matthew never do this).

Verified 12 consistent narrator-κύριος verses + 1 principled exception:
- **องค์พระผู้เป็นเจ้า** — 11 verses (7:13; 10:1; 11:39; 12:42; 13:15; 17:5; 17:6; 18:6; 19:8; 22:61; 24:34).
- **พระเยซู** — 1 verse (10:41, Mary-Martha rebuke-comfort; per-verse rationale preserved).
- 24:3 excluded: τοῦ κυρίου Ἰησοῦ omitted per SBLGNT Western non-interpolation (RULES.md §0).

**Acts forward:** ~25 narrator-κύριος verses referring to Jesus inherit this lock (Acts 9:10, 9:11, 9:15, 9:27, 11:21, 18:9, etc.).

**→ New doc:** `docs/translator_decisions/kyrios_narrator_voice_luke_acts_2026-04.md`.

---

## 2. βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า — **LOCKED (new doc this review)**

Luke uses βασιλεία τοῦ θεοῦ exclusively (31 verified occurrences), never the Matthean τῶν οὐρανῶν periphrasis. Uniform Thai rendering.

Combined Mark/Matthew/Luke pattern now corpus-locked:
- τῶν οὐρανῶν → อาณาจักรสวรรค์ (Matthew only, ~51×)
- τοῦ θεοῦ → อาณาจักรของพระเจ้า (Mark, Luke, MAT 12:28+21:31)
- Non-kingdom-of-God βασιλεία (political kingdoms, parable royal rule, Satan's kingdom) → context-tracking plain อาณาจักร or การเป็นกษัตริย์.

**Acts forward:** 7 occurrences (1:3, 8:12, 14:22, 19:8, 20:25, 28:23, 28:31), all τοῦ θεοῦ → อาณาจักรของพระเจ้า.

**→ New doc:** `docs/translator_decisions/basileia_kingdom_rendering_2026-04.md`.

---

## 3. πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์ — **STABLE**

13 verified Luke occurrences of Greek πνεῦμα + ἅγιον (in any case/position): 1:15, 1:35, 1:41, 1:67, 2:25, 2:26, 3:16, 3:22, 4:1, 10:21, 11:13, 12:10, 12:12. **All** render พระวิญญาณบริสุทธิ์ with no variance. Glossary has πνεῦμα ἅγιον → primary_thai: พระวิญญาณบริสุทธิ์, single rendering.

Other πνεῦμα forms (unclean spirits ch. 4, 8, 11; human spirit 1:47, 23:46; life-breath 8:55; apparition 24:37, 24:39) correctly use context-adapted Thai (ผีโสโครก / จิตวิญญาณ / ลมปราณ / ผี/วิญญาณ). Pattern is stable.

**Acts forward:** 50+ πνεῦμα ἅγιον occurrences — will inherit the uniform rendering. No separate doc needed; existing glossary lock is sufficient.

**Recommendation:** STABLE. Do not write a doc; the glossary + per-chapter key_term_consistency enforces uniformity.

---

## 4. σήμερον → วันนี้ — **STABLE**

All 11 Luke σήμερον occurrences render วันนี้ (2:11; 4:21; 5:26; 12:28; 13:32; 13:33; 19:5; 19:9; 22:34; 22:61; 23:43). Thai วันนี้ naturally carries both routine-temporal and eschatological-loaded senses. Theologically loaded verses (2:11 Nativity; 4:21 Nazareth; 19:9 Zacchaeus; 23:43 thief on cross) get per-verse notes that surface the "today = realized-eschatology" reading; the lexical rendering doesn't change.

**Recommendation:** STABLE. The Greek form is lexically invariant; Thai mirrors it. No corpus doc needed.

---

## 5. Jerusalem: Ἰερουσαλήμ (feminine) + Ἱεροσόλυμα (neuter) → เยรูซาเล็ม — **STABLE (limitation noted)**

Luke uses both Greek forms with probable theological distinction (feminine = theological Israel's-city; neuter = geographical city). Thai has no grammatical gender — both forms collapse to เยรูซาเล็ม (or กรุงเยรูซาเล็ม when the prose calls for the "city of" marker).

Verified Ἱεροσόλυμα occurrences in Luke: 2:22; 13:22; 19:28; 23:7. All render เยรูซาเล็ม / กรุงเยรูซาเล็ม indistinguishably from Ἰερουσαλήμ. This is a known Thai-target limitation, not a drift.

**Acts forward:** Acts alternates aggressively. The doc approach is: accept the loss; flag at per-verse note if the Greek gender distinction is rhetorically significant (rare).

**Recommendation:** STABLE — limitation, not a translation choice. Add a one-line note to RULES.md §4 documenting the loss.

---

## 6. Vocative Κύριε / Διδάσκαλε speaker-class register — **LOCKED (new doc this review)**

26 Κύριε vocatives + 12 Διδάσκαλε vocatives. The multi-rendering is **principled** (tracks speaker class), not drift. Documented the pattern for Acts-forward consistency.

- **Κύριε**: องค์พระผู้เป็นเจ้า (disciples/confessing-believers, 17×); พระองค์เจ้าข้า (humble intimate petitioners, 3×); นายท่าน / นายเจ้าข้า (parabolic master-servant, 6×).
- **Διδάσκαλε**: ท่านอาจารย์ (neutral inquirer, 6×); พระอาจารย์ (elevated respectful, 2×); อาจารย์เจ้าข้า (testing-address, 4×).

**→ New doc:** `docs/translator_decisions/vocative_kyrie_didaskale_register_2026-04.md`.

Extends `narrator_vs_character_voice_2026-04.md`.

---

## 7. σωτήρ / σωτηρία / σῴζω (salvation family) — **STABLE**

Luke 1:47, 2:11, 2:30 (σωτήρ → พระผู้ช่วยให้รอด); 1:69, 1:71, 1:77, 2:30, 3:6, 19:9 (σωτηρία → ความรอด); σῴζω idiomatic per context (ช่วยให้รอด / เอาชีวิตรอด / หาย). Uniform within each lemma; no drift. Glossary entries confirm single primary_thai for each.

**Recommendation:** STABLE. The Luke 2:11 crux ("a Savior who is Christ the Lord" = σωτήρ ὅς ἐστιν χριστὸς κύριος) is rendered "พระผู้ช่วยให้รอด…พระองค์คือพระคริสตเจ้า" which correctly separates the three titles. No corpus doc needed beyond the existing glossary.

---

## 8. τελώνης (tax collector) → คนเก็บภาษี — **STABLE**

18 Luke mentions; uniform rendering. Socially weighted but lexically stable.

---

## 9. ἁμαρτωλός (sinner) → คนบาป — **STABLE**

~26 Luke mentions; uniform. Luke's "friend of sinners" theology (5:30, 7:34, 15:1–2, 18:13, 19:7) carried lexically without rendering drift.

---

## 10. Σαμαρίτης / Σαμαρείτης (Samaritan) → ชาวสะมาเรีย — **STABLE**

Luke 9:52; 10:33; 17:16; 17:18. Three uses, one rendering. Theological weight in per-verse notes (Good Samaritan ethic; Samaritan gratitude at 17:16).

---

## 11. Magnificat (1:46–55), Benedictus (1:68–79), Nunc Dimittis (2:29–32) — **STABLE (register)**

Three liturgical hymns rendered in elevated Thai register (honorific particles, poetic parallelism, past-perfect emphasis). No corpus-level register lock needed beyond the existing `narrator_vs_character_voice_2026-04.md` — these are first-person character voice (Mary, Zechariah, Simeon) in prayer-register, handled per-speaker.

**Recommendation:** STABLE. Consider native-speaker spot-check on rhythm (see Action Items).

---

## 12. Parable introductory formulas (εἶπεν δὲ παραβολὴν etc.) — **STABLE**

~24 parables in Luke; introductory formulas rendered idiomatically per verse. Not locked to a single stock phrase, by design (Thai reader ear prefers variation over Greek-style repetition).

**Recommendation:** STABLE. The verse-level rationale at each parable's opening carries the specific register choice.

---

## 13. Herod family disambiguation — **STABLE**

- **Herod the Great** (Luke 1:5): เฮโรดกษัตริย์แห่งยูเดีย or similar specifying-phrase at first mention, then เฮโรด.
- **Herod Antipas** (Luke 3:1, 3:19, 8:3, 9:7, 9:9, 13:31, 23:7–15): เฮโรด or เฮโรดเจ้าแคว้นกาลิลี at disambiguating mentions.
- **Herodias** (Luke 3:19): เฮโรเดียส.
- **Herod Philip** indirectly via 3:19: ฟีลิป.

Context disambiguates without translator intervention. No corpus doc needed.

---

## 14. Holy Spirit filling / leading idioms (πλησθείς / ἐν τῷ πνεύματι / ἤγετο ἐν τῷ πνεύματι) — **STABLE**

Idiomatic Thai: เต็มเปี่ยมด้วยพระวิญญาณบริสุทธิ์ (1:15, 1:41, 1:67, 4:1); พระวิญญาณบริสุทธิ์ทรงสวมให้ (24:49 — alternative rendering for ἐνδύσησθε ἐξ ὕψους δύναμιν); ทรงถูกนำไปโดยพระวิญญาณ (4:1). Per-verse notes carry the Greek-form tracking.

**Recommendation:** STABLE.

---

## 15. 2 textual-variant interactions — **COMPLIANT (RULES §0)**

Luke's two Western-non-interpolations (24:3 τοῦ κυρίου Ἰησοῦ omitted; 24:36 εἰρήνη ὑμῖν omitted) follow SBLGNT per RULES §0, with per-verse divergence notes documenting the choice. Verified in the per-chapter reports. No additional action needed.

---

## Flagged for Ben's attention

### A. Native-speaker spot-check on Luke 1–2 liturgical register
The Magnificat/Benedictus/Nunc Dimittis carry elevated register choices that would benefit from a Thai Christian reader's read-aloud check. Specifically: does the rhythm scan? Are the honorific particles over- or under-used? Flag concerns at the verse level.

### B. Optional: run full glossary audit against Matthew + Mark + Luke + 1 Tim for consistency
Now that ~70 chapters are shipped, a cross-book glossary-consistency pass could surface any latent drift before Acts begins. The per-chapter key_term_consistency.py check is clean, but a book-spanning audit (comparing glossary primary_thai against the 4-book corpus) would catch things the per-chapter check can't.

### C. External AI review (Grok / ChatGPT / Gemini) — §3 of the checklist
Still pending. The Matthew review benefited from this pass (Gemini flagged ekklesia LXX-quotation exceptions). Recommended before tagging `book-luke-v1`. A prompt template that worked for Matthew: "Read Luke 1, 4, 10, 15, 18, 24 in Thai alongside the Greek. Flag corpus-level concerns a Thai reader would surface." (Not the full book — key chapters catch patterns.)

### D. Matthew open follow-ups (from MAT end-of-book review) — still outstanding
Per the memory, these don't block Luke tagging but are worth closing before `book-luke-v1`:
- Doc tightening on ekklesia LXX-quotation exception
- 18:17 register note
- 3-for-2 Thai μεταμέλομαι split documentation
- Heb 12:17 contested flag
- ἀμεταμέλητος handling (Rom 11:29; 2 Cor 7:10)
- Native-speaker spot-check on เปลี่ยนใจ at MAT 21:29, 21:32
- Optional τότε NONE spot-check (11 verses)

---

## 16. External AI review outcomes (Gemini 2.5 Pro, 2026-04-23)

Per checklist §3, submitted the 6-chapter packet (`docs/external_review_packet_LUK_2026-04-23.md`) to Gemini 2.5 Pro. Returned 4 corpus-level flags. All verified against the actual translation JSONs before acting.

### Flag 1 — Narrator's ทูล verb for adversary speech (LUK 4:3, 4:6, 4:9) — **DOCUMENTED (no translation change)**
Verified: all three verses use ทูลพระองค์ว่า when the narrator introduces Satan's temptation dialogue. Per-verse rationale at 4:3 already documents this as a principled cross-gospel convention (cf. MAT 4:3 parallel): ทูล is addressee-marking (the divine Jesus), not speaker-marking. Thai readers parse it this way. Gemini's concern (that ทูล grants the Devil "a posture of legitimate submission") is real but overridden by the cross-gospel lock. **Action:** wrote `docs/translator_decisions/speech_verbs_adversaries_addressing_divine_2026-04.md` to lock the convention corpus-wide and make the two-axis model explicit (outer-axis = narrator verb tracks addressee-rank; inner-axis = speaker pronouns track speaker-stance).

### Flag 2 — ψυχή vs. πνεῦμα anthropological distinction — **DOCUMENTED (no translation change)**
Verified: the Luke corpus *does* preserve the Hebraic-parallel distinction where it matters — LUK 1:46 ψυχή → จิตวิญญาณ, LUK 1:47 πνεῦμα → **จิต** (with explicit per-verse rationale calling out the distinction). Gemini over-reads as "merging"; what actually happens is ψυχή stays at จิตวิญญาณ, and πνεῦμα pivots between จิต (in parallel with ψυχή) and จิตวิญญาณ (standalone). The Acts-forward concern is legitimate — 1 Thess 5:23 and Heb 4:12 will force the distinction. **Action:** wrote `docs/translator_decisions/psyche_vs_pneuma_anthropological_2026-04.md` locking the pattern for all future books; the non-negotiable rule: "never render a parallelism's two halves with the same Thai word."

### Flag 3 — μετανοέω drift at LUK 10:13 — **SPOT-REVISED (translation changed)**
Verified real drift: 10:13's "คงจะกลับใจใหม่ตั้งแต่นานแล้ว" added "ใหม่" to the RULES §4 locked term. The per-verse rationale acknowledged the deviation ("adding 'ใหม่' for naturalness"). Other Luke μετανοέω occurrences (15:7, 15:10, 24:47) all use plain กลับใจ — this was a single-verse slip. **Action:** revised LUK 10:13 to "คงจะกลับใจตั้งแต่นานแล้ว" (removed ใหม่); updated the key_decision rationale to reflect the normalization. `check_key_term_consistency.py` + `check_greek_field_integrity.py` both still clean post-revision.

### Flag 4 — Parabolic God-figures receive human register — **DOCUMENTED (no translation change)**
Verified: the prodigal's father (LUK 15:11–32), the nobleman/king (LUK 19:11–27), the persistent-widow's judge (LUK 18:1–8), and all other parabolic God-figures across MRK/MAT/LUK consistently receive standard Thai human register (no ราชาศัพท์), preserving the parabolic indirection. This is a corpus-wide pattern that Gemini correctly noted had no formal doc. **Action:** wrote `docs/translator_decisions/parabolic_god_figures_human_register_2026-04.md` formalizing the rule and addressing the borderline case of MAT 25:31–46 (apocalyptic, not parable — divine register applies).

### Gemini §C — Acts-forward preparatory recommendations

Gemini flagged two Acts-forward items worth noting (not blocking Luke tag):
1. **"Breaking of bread" (κλάσις τοῦ ἄρτου)** at LUK 24:30/35 → "หักขนมปัง". In Acts 2:42, 20:7 this becomes a technical early-Eucharistic term. Already in glossary effectively; monitor at Acts 2:42 translation session.
2. **"The Eleven" / "The Twelve" as collective nouns** — LUK 24:9/33 rendered "สาวกสิบเอ็ดคน". As the apostolic band transitions in Acts 1–2, the group should function as an official collective. Already using "อัครทูต" in Acts 1:26 (matthias election) — pattern carries.

Neither required new docs or spot-revisions; flagging for the Acts translator's attention.

### Gemini §D — observations affirmed as wins (no action)

- HAPAX handling: "ชั่วขณะเดียว" for ἐν στιγμῇ χρόνου (LUK 4:5); "สภาพเกือบตาย" for ἡμιθανῆ (LUK 10:30).
- Semantic precision at LUK 15:12/13 (βίος vs οὐσία distinction).
- Prayer register at LUK 10:21 (Jesus's Father-address, high-priestly-prayer template).

---

## New documents written during this review

From internal end-of-book editorial review (2026-04-22):
1. `docs/translator_decisions/kyrios_narrator_voice_luke_acts_2026-04.md`
2. `docs/translator_decisions/basileia_kingdom_rendering_2026-04.md`
3. `docs/translator_decisions/vocative_kyrie_didaskale_register_2026-04.md`

From external AI review (2026-04-23):

4. `docs/translator_decisions/speech_verbs_adversaries_addressing_divine_2026-04.md`
5. `docs/translator_decisions/psyche_vs_pneuma_anthropological_2026-04.md`
6. `docs/translator_decisions/parabolic_god_figures_human_register_2026-04.md`

### Translation spot-revision (1 verse)

- `output/translations/luke_10.json` — LUK 10:13 "กลับใจใหม่" → "กลับใจ" to maintain RULES §4 lock. Key_decision rationale updated.

---

## 17. External AI review outcomes — pass 2 (Claude Opus, 2026-04-23)

Second external-review pass. Claude returned 6 flags — more surgical than Gemini's pass, catching corpus-level patterns Gemini missed and confirming items Gemini had affirmed stable. Each flag verified against actual JSONs before acting.

### Flag A1 — ἄφεσις ἁμαρτιῶν split (HIGHEST priority, Acts-forward) — **LOCKED + 1 spot-revision**

Verified: LUK 1:77 renders ἐν ἀφέσει ἁμαρτιῶν as "โดยการอภัยบาป" (การอภัย), while LUK 3:3 (John-Baptist) and LUK 24:47 (Great Commission) both use "การยกโทษบาป" (การยกโทษ). Two per-verse rationales independently claimed RULES §4 "locked" different renderings. RULES §4 in fact lists both as options with "Document choice" instruction.

**Action:**
- Wrote `docs/translator_decisions/aphesis_forgiveness_of_sins_2026-04.md` locking ἄφεσις ἁμαρτιῶν → **การยกโทษบาป** corpus-wide. Chose การยกโทษ over การอภัย for the judicial-release precision that matters in Pauline atonement + Hebrews 9:22 / 10:18.
- **Spot-revised LUK 1:77**: "โดยการอภัยบาป" → "โดยการยกโทษบาป" + updated key_decision rationale.
- Benedictus (1:77) ↔ Great Commission (24:47) inclusio now consistent.
- 5 Acts sermons (2:38, 5:31, 10:43, 13:38, 26:18) inherit the lock.

### Flag A2 — οὐρανός alternation (ฟ้าสวรรค์ / สวรรค์) — **DOCUMENTED + 1 spot-revision**

Verified: full Luke audit shows genuine drift. 15 verses use ฟ้าสวรรค์, 7 use สวรรค์, 2 use ท้องฟ้า (meteorological), 5 are rephrased. The clearest parallelism violation: LUK 10:20 "names in heaven" → ฟ้าสวรรค์ vs. LUK 18:22 "treasure in heaven" → สวรรค์ (identical locative construction, different Thai).

**Action:**
- Wrote `docs/translator_decisions/ouranos_heaven_rendering_2026-04.md` with principled guidelines: **สวรรค์** default for locative + theological-abode; **ฟ้าสวรรค์** reserved for cosmic-emphatic ("heaven and earth" pair, apocalyptic imagery); **ท้องฟ้า** for sky-as-meteorological-object.
- **Spot-revised LUK 10:20**: ฟ้าสวรรค์ → สวรรค์ (parallelism with 18:22).
- **Deliberate conservative approach on retrospective revision**: shipped Luke drift not fully normalized (15+ verses would cascade into back-translation + check regeneration). Flagged for systematic John-era sweep across MAT + MRK + LUK + ACT.
- **Acts 1:10–11 Ascension** locked to **สวรรค์** (matches LUK 24:51).

### Flag A3 — LUK 10:17 vocative Κύριε outlier — **SPOT-REVISED**

Verified: LUK 10:17 (the 72 returning from mission) renders Κύριε as **พระองค์เจ้าข้า** (humble-intimate register), but the vocative lock (doc #13) routes disciples → **องค์พระผู้เป็นเจ้า**. The per-verse rationale calls the category "disciple-to-Jesus vocative" — exactly what the lock routes to องค์พระผู้เป็นเจ้า. Text was rendered before the 2026-04-22 lock doc was written.

**Action:**
- **Spot-revised LUK 10:17**: «พระองค์เจ้าข้า → «องค์พระผู้เป็นเจ้า». Key_decision rationale updated with reference to the lock doc.
- No doc changes needed beyond the rationale update.

### Flag A4 — Praise-verb collapse (δοξάζω + εὐλογέω + αἰνέω + αἶνον δίδωμι → สรรเสริญ) — **DOCUMENTED**

Verified: principled-but-undocumented corpus-wide collapse. Per-verse rationales already explain ("εὐλογέω when object-is-God → สรรเสริญ more-natural than อวยพร"; "αἶνος → สรรเสริญ, same rendering as δοξάζω; both = praise in Thai"). The collapse is defensible on Thai-naturalness grounds but deserves corpus-level documentation before Acts's heavy doxological vocabulary (~25 praise-verb occurrences with God as object across Acts).

**Action:**
- Wrote `docs/translator_decisions/divine_object_praise_verbs_2026-04.md` documenting the collapse + the exceptions (μεγαλύνω, ὑψόω, προσκυνέω kept distinct; εὐλογέω on non-divine object stays อวยพร).
- No translation changes.

### Flag A5 — RULES §5 undercounted Luke 24 WNIs — **RULES.md UPDATED**

Verified: RULES §5 stated "two Western non-interpolations in Luke 24." Traditional Westcott-Hort count is 7 (24:3, 24:6, 24:12, 24:36, 24:40, 24:51, 24:52). All verses follow SBLGNT's text; the "two" count was referring to text-omissions (24:3 phrase + 24:36 phrase) but was undercounting for WNI-enumeration purposes.

**Action:**
- Updated `RULES.md` §5 with enumerated table listing all 7 Luke 24 WNIs + SBLGNT disposition per verse. RULES version bumped to v0.4.
- No translation changes.

### Flag A6 — LUK 10:25 Διδάσκαλε (lawyer testing Jesus) — **VOCATIVE DOC AMENDED**

Verified: LUK 10:25 renders Διδάσκαλε as **ท่านอาจารย์** (neutral-polite), but the vocative lock's "testing" category routes to **อาจารย์เจ้าข้า**. The Greek ἐκπειράζων supports "testing," but the narrative signal at 10:25 is probing-inquiry (legal-exegetical probe), not hostile-trap — Jesus responds pastorally. The current rendering is defensible; the lock doc just needs to clarify the probe-vs-hostile distinction.

**Action:**
- Amended `docs/translator_decisions/vocative_kyrie_didaskale_register_2026-04.md` with a new sub-section: "πειράζω / ἐκπειράζω — probing-inquiry vs. hostile-testing." Rule: register follows narrative signal (ἐγκάθετοι / συμβούλιον / rebuke-response), not the lexical trigger alone.
- LUK 10:25 stays ท่านอาจารย์ as documented probing-inquiry case.
- LUK 20:21–21:7 stays อาจารย์เจ้าข้า as documented hostile-testing sequence.
- No translation changes.

### Claude §C — Acts-forward preparatory notes

Claude flagged 8 Acts-forward items (most overlap with decisions already locked). Non-duplicative:

- **Proper-noun sweep for Acts** (Παῦλος / Βαρναβᾶς / Σαῦλος / Σιλᾶς / Ἀπολλῶς) — already handled per glossary convention; run `scripts/check_key_term_consistency.py` batch-audit before Acts 13 ships.
- **"We-passages" narrator voice** (Acts 16:10–17 etc.) — note for Acts 16 translator: natural Thai first-person-plural; no register-marking needed.
- **Pentecost glossolalia** (Acts 2:4–11: λαλεῖν ἑτέραις γλώσσαις + διαλέκτῳ) — lock before Acts 2 ships. Doctrinally sensitive for evangelical-Protestant framing. **Candidate rendering:** พูดภาษาอื่น + ภาษาประจำของตน, but confirm at Acts 2 session.
- **ἀδελφοί vocative in sermons** (~20 occurrences in Acts) — decide "brothers" vs. "brothers and sisters" vs. context-adapted. Lock before Acts 1:16 ships. **Candidate rendering:** พี่น้องทั้งหลาย (gender-neutral in Thai usage); confirm at Acts 1 session.
- **καταγγέλλω** (new in Acts, ~11 occurrences) — lock before Acts 13. Candidate rendering: ป่าวประกาศ / ป่าวร้องประกาศ (strong-public proclamation); distinguish from ประกาศ (κηρύσσω) + ประกาศข่าวประเสริฐ (εὐαγγελίζομαι) already established.

### Claude §D — observations affirmed as wins (no action)

- Benedictus / Magnificat elevated register reads as intentional and OT-allusion-dense.
- OT-citation guillemet «...» consistent; may need nested-mark convention for Acts 7 (Stephen quoting OT within Luke narrator quoting Stephen).
- LUK 24:32 "ใจของเราร้อนรุ่มอยู่ภายใน" — micro-elaboration ภายใน for figurative καρδία clarification; fine per uW guidance.
- Luke 24 WNI handling "exactly right" — follow SBLGNT, note the tradition, don't moralize. Will pay compound dividends in Acts's variant-dense Petrine speeches.

---

## External-review result

After **two independent external AI reviews** (Gemini 2.5 Pro + Claude), all catastrophic corpus-level risks caught and remediated. The ἄφεσις lock (Flag A1) is the most load-bearing outcome — would have compounded across 5 Acts sermons if unaddressed.

Attempted review with Grok and GPT free-tiers: both hit character-limit caps on the paste-packet. No response gathered from those platforms; two substantive responses (Gemini + Claude) meets the §3 checklist criterion of "at least one external review."

## Pre-existing docs affirmed / unchanged

1. `amen_saying_formula_2026-04.md` — applies across Luke as in Mark.
2. `aramaic_transliterations_2026-04.md` — no Luke Aramaicisms (Mark-specific feature).
3. `ekklesia_2026-04.md` — no Luke ἐκκλησία occurrences; doc governs Acts-forward.
4. `historic_present_2026-04.md` — applies across Luke; historic presents → Thai past.
5. `honorifics_non_divine_authorities_2026-04.md` — applies to Luke Pilate/Herod Antipas/centurion.
6. `inclusion_variants_absent_verses_2026-04.md` — Path A applied to Luke textual variants.
7. `markan_euthys_immediately_2026-04.md` — Mark-specific; Luke has no εὐθύς.
8. `metanoeo_vs_metamelomai_2026-04.md` — Luke μετανοέω (5:32, 15:7, etc.) renders กลับใจ consistently; no Luke μεταμέλομαι.
9. `narrator_vs_character_voice_2026-04.md` — applies across Luke.
10. `son_of_man_disambiguation_2026-04.md` — Luke's 25 Son-of-Man verses follow the Markan lock.

---

## Conclusion

Luke ships in strong corpus-hygiene shape. All automated checks pass; editorial patterns are consistent; 3 new decision docs close the Acts-forward gaps.

**Recommend tag `book-luke-v1`** after:
1. At least one external AI sanity-check review (checklist §3 — pending).
2. Optional: native-speaker read on Luke 1–2 liturgical sections.

Acts translation can begin in parallel (same pattern as Mark→Matthew pipeline — Acts is Luke's two-volume companion, next in `data/production_order.json`).
