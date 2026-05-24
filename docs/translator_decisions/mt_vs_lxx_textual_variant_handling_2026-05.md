# MT-vs-LXX textual-variant handling — OT-side policy

**Scope:** How the Eremos OT translation handles places where the Masoretic Text (MT) and Septuagint (LXX) preserve materially different readings — and how those differences are surfaced (or not) in the Thai surface text vs. the Layer-2 footer apparatus.

**Decided:** 2026-05-12 (Genesis end-of-book audit §F + external AI cross-review). Genesis-locking-precedents at 4:8 / 46:27 / 47:31. **CRITICAL** before Joshua / Samuel / Jeremiah / Esther / Ezra-Nehemiah ship, since each of those books carries major MT-vs-LXX divergences that this policy must anchor.

**Companion docs:** `inclusion_variants_absent_verses_2026-04.md` (NT-side policy; this is the OT companion), `divine_names_table_2026-05.md` (Tetragrammaton + LXX κύριος mapping).

---

## 1. Three Genesis-locking-precedents

Three of the most-cited MT-vs-LXX divergences in Hebrew Bible scholarship occur in Genesis. Each was handled differently in pre-policy drafting; this doc codifies the principle behind the choices.

### 1.1 Gen 4:8 — LXX gap-fill (Cain's words to Abel)

**MT:** וַיֹּאמֶר קַיִן אֶל־הֶבֶל אָחִיו וַיְהִי בִּהְיוֹתָם בַּשָּׂדֶה ("And Cain said to Abel his brother, and it came to pass while they were in the field...") — MT has a **silent gap** between "Cain said" and "in the field." Cain's words are not preserved.

**LXX + SP (Samaritan Pentateuch) + Syriac + Vulgate + Targums:** all four ancient versions agree in supplying εἴπωμεν εἰς τὸ πεδίον ("Let us go out to the field"). The gap-fill is **broadly attested across four independent textual traditions** — the only major textual case in Genesis where the LXX divergence has cross-versional support of this breadth.

**Eremos surface text (updated 2026-05-12):** includes the addition **inline without brackets**, matching Berean Standard Bible (BSB) — the project's foundational translation philosophy:

> คาอินพูดกับอาเบลน้องชายว่า **"ให้เราออกไปที่ทุ่งนากัน"** เมื่อพวกเขาอยู่ในทุ่งนา...

(BSB Gen 4:8: *"Then Cain said to his brother Abel, 'Let us go out to the field.' And while they were in the field..."* — no brackets, no footnote-marker on the surface.)

**Layer-2 footer** at `output/textual_variants/genesis_04.json` (type `textual_variant_lxx_addition`) documents the manuscript evidence + the five cross-versional witnesses (LXX + SP + Syriac + Vulgate + Targum Pseudo-Jonathan).

**Category:** **Broadly-attested gap-fill** — the rare case where multiple independent ancient versions converge on the same supplement to an MT-silent reading. Surface inline (no bracket) per BSB-alignment + the Category-A high bar (≥3 cross-versional witnesses required — Gen 4:8 has 5).

### 1.2 Gen 46:27 — MT 70 vs. LXX 75 persons

**MT:** 70 persons descended into Egypt (Jacob + 69 descendants).
**LXX:** 75 persons (adds 5 descendants of Joseph via Ephraim and Manasseh).
**NT echo:** Acts 7:14 (Stephen's speech) cites the LXX number — "Joseph sent and called Jacob his father and all his relatives, seventy-five persons in all."

**Eremos surface text:** uses **เจ็ดสิบคน** (MT 70).

**Layer-2 footer** at `output/textual_variants/genesis_46.json` (type `lxx_variant`) documents the LXX number + the Acts 7:14 NT cross-reference.

**Category:** **Competing textual tradition** — MT and LXX preserve different but internally-coherent numerical traditions. Eremos surfaces MT (the primary base text) and documents LXX in the apparatus.

### 1.3 Gen 47:31 — MT "head of bed" vs. LXX "top of staff"

**MT:** וַיִּשְׁתַּחוּ יִשְׂרָאֵל עַל־רֹאשׁ הַמִּטָּה ("Israel bowed at the head of the **bed**") — vocalization מִטָּה *miṭṭāh*.
**LXX:** ἐπὶ τὸ ἄκρον τῆς ῥάβδου ("upon the head of his **staff**") — same consonants (מטה) revocalized as **maṭṭeh** ("staff").
**NT echo:** Heb 11:21 cites LXX — "By faith Jacob, as he was dying, blessed each of Joseph's sons, and worshiped, **leaning on the top of his staff**."

**Eremos surface text:** uses **บนหัวเตียง** (MT "head of bed").

**Layer-2 footer** at `output/textual_variants/genesis_47.json` (type `lxx_variant`) documents the LXX vocalization + the Heb 11:21 NT cross-reference.

**Category:** **Competing textual tradition** — same consonants, different vocalizations preserved by the MT (Masoretes) vs. the LXX (which translated 3rd c. BCE pre-Masoretic).

---

## 2. The three categories — explicit policy

| Category | Description | Surface-text policy | Footer policy |
|---|---|---|---|
| **A. Broadly-attested gap-fill** | MT has a silent gap (omission, lacuna); LXX + ≥2 other independent ancient versions (SP, Syriac, Vulgate, Targums) converge on the same supplement | **Include the addition inline, no brackets** (matches BSB style — the project's foundational philosophy) | Required (manuscript evidence + cross-versional witness list) |
| **B. Competing textual tradition** | MT and LXX preserve different readings with similar internal coherence (number-counts; vocalization variants; lexical substitutions) | **Surface = MT only**; Layer-2 footer | Required (LXX reading + NT cross-reference if cited) |
| **C. LXX expansion / paraphrase / theological-edit** | LXX adds, paraphrases, or theologically-edits beyond MT, without cross-versional support | **Surface = MT only**; no inline-bracket | Optional footer (use if the LXX expansion has lasting theological/historical importance) |

**Hard threshold for Category A:** the cross-versional evidence must include **at least three** of {LXX, SP, Syriac (Peshitta), Vulgate, Targums (Onkelos / Pseudo-Jonathan)}, AND the variant must fill a genuine MT-text-state lacuna (not merely paraphrase a present-text). The 4:8 case meets this. **Future translators should treat Category A as the rare exception, not the default.**

**Default behavior** is Category B / C: surface = MT only, LXX divergence documented in the footer apparatus.

## 2.1 Resolved 2026-05-12 — BSB-alignment

The original draft of this doc presented Gen 4:8 with square brackets and flagged a ChatGPT-vs-Gemini divergence on whether to strip them. Ben asked **"what does BSB do here?"** — BSB Gen 4:8 includes the LXX gap-fill inline without brackets or footnote-markers (just as natural English text). Since the Eremos project is explicitly BSB-style ("Optimal equivalence — Berean Standard Bible style" per `scripts/translate_mark.py`), the policy resolved to **no bracket** at the surface + cross-versional manuscript evidence in the Layer-2 footer.

The Category-A high bar (≥3 cross-versional witnesses + a genuine MT lacuna) is intentionally narrow to prevent inline-addition becoming a general license for LXX imports. The 5-witness threshold at Gen 4:8 (LXX + SP + Syriac + Vulgate + Targum Pseudo-Jonathan) far exceeds the bar.

**Forward-look:** at Joshua 21:36–37 (missing-MT-verses with LXX + Vulgate support), the Category-A bar will be tested. If Joshua 21 has ≥3 cross-versional witnesses, the addition gets included inline (matching the Gen 4:8 precedent). If not, it's a Category-B (footer-only).

---

## 2.2 Macro-structural divergence subcategory (added 2026-05-24, 1 Kings EOB)

Categories A/B/C above handle **verse-level** minuses/pluses/competing-readings. They do **not** fit whole-narrative reordering, large transposed blocks, or alternate parallel accounts. 1 Kings / 3 Reigns is the largest such case in the OT so far (LXX reorders the Solomon material; inserts the two **Miscellanies** at 3 Rgns 2:35a–o and 2:46a–l; carries an **alternate Jeroboam account** at 12:24a–z; and **swaps MT chs. 20↔21**). Forcing this into scattered verse footers would obscure the scale.

**Decision (Ben, 2026-05-24, confirming ChatGPT over Gemini's "Tier 4"):** keep the A/B/C tier scheme intact and add a **subcategory**, not a competing fourth tier:

- **`macro_structural_mt_lxx_divergence`** — whole-narrative reordering / transposed blocks / alternate parallel accounts. Surface = **MT only** (as always). Disclosure = a **book-level prefatory note** (primary; the issue is structural, not phrase-level) + optional Tier-2 **chapter-footer anchors** at the affected chapters.

**1 Kings book-level prefatory note — canonical text (Thai), to surface at the head of 1 Kings:**

> **หมายเหตุเรื่องตัวบท (MT/LXX):** ฉบับเอเรโมสแปลพระธรรม 1 พงศ์กษัตริย์จากต้นฉบับภาษาฮีบรู (MT) เป็นหลัก. ฉบับกรีก (Septuagint / 3 Reigns) มีโครงสร้างต่างจาก MT อย่างมีนัยสำคัญ ได้แก่ การจัดลำดับเรื่องของซาโลมอนใหม่, ส่วนเพิ่ม "Miscellanies" สองตอน (3 รก. 2:35ก–ฯ และ 2:46ก–ฯ), เรื่องเล่าทางเลือกเกี่ยวกับเยโรโบอัม (12:24ก–ฮ), และการสลับลำดับบทที่ 20 กับ 21. ฉบับเอเรโมสยึดลำดับและตัวบทตาม MT; ความแตกต่างเชิงโครงสร้างเหล่านี้บันทึกไว้เพื่อความโปร่งใส มิได้กระทบเนื้อหาที่แปล.

**Chapter-footer anchors (Tier-2, to add at):** ch. 2 + 11 (Solomon material + Miscellanies), ch. 12 (alternate Jeroboam narrative), ch. 20–21 (MT/LXX chapter-order swap). *Implementation status (2026-05-24): subcategory + book-note text locked here; reader-facing book-note (1kings_01 textual_variants) + the four chapter footers + re-ship are a pre-`ship_book.sh` follow-up.*

---

## 3. Forward applicability — OT books where this policy compounds

The MT-vs-LXX question scales massively beyond Genesis:

| Book | Major divergences | Category |
|---|---|---|
| **Joshua** | 21:36–37 missing in MT, present in LXX + Vulgate (Reubenite Levitical cities) | A or B (case-by-case) |
| **1 Samuel** | 13:1 numerical gap; ch. 17 (David vs. Goliath) — LXX is ~50% shorter | C (LXX truncation; surface = MT) |
| **2 Samuel** | 5:6–9; 8:7–8; multiple smaller divergences | Mostly B |
| **1–2 Kings** | verse-level: many smaller divergences (B/C). **Macro-structural** (1 Kings): Solomon reordering, the two Miscellanies (2:35a–o, 2:46a–l), alternate Jeroboam account (12:24a–z), MT 20↔21 swap | `macro_structural_mt_lxx_divergence` (§2.2) — MT surface + book-level note |
| **Jeremiah** | the **LXX is ~13% shorter than MT** and arranges material differently (the oracles against nations come earlier in LXX) — this is the largest MT-vs-LXX divergence in the OT | The whole book's text-form is the question; document a per-book policy decision |
| **Esther** | LXX has 6 long additions ("Additions to Esther" in the Apocrypha — Mordecai's dream, Esther's prayer, etc.); Catholic OT includes them, Protestant OT excludes them | C with strong NT-Apocrypha-policy implications |
| **Daniel** | LXX (Theodotion) has 3 additions: Prayer of Azariah / Song of the Three Holy Children (between 3:23 and 3:24); Susanna; Bel and the Dragon | C with strong NT-Apocrypha-policy implications |
| **Ezra-Nehemiah** | textual divisions differ; some passages have parallel LXX form (1 Esdras) | B / C |

**This doc must land before Joshua / Samuel / Jeremiah / Esther / Ezra-Nehemiah ship.** For each book at audit-time, the audit doc should explicitly classify the major MT-vs-LXX divergences into Categories A/B/C and confirm the policy compliance.

---

## 4. The Tetragrammaton-LXX-edge-case

`divine_names_table_2026-05.md` already locks the YHWH ↔ κύριος mapping for NT-quotes-of-OT. This doc does not duplicate that; refer to the divine-names table for any case where MT יהוה corresponds to LXX κύριος (or vice versa). The Tetragrammaton place-name compounds (יהוה־יִרְאֶה Gen 22:14; יהוה־נִסִּי Ex 17:15; יהוה־שָׁלוֹם Judg 6:24) are NOT MT-vs-LXX-variant cases — they are MT place-names that LXX often paraphrases (e.g., Gen 22:14 LXX Κύριος εἶδεν "the Lord saw").

---

## 5. Implementation checklist

- [ ] Run `audit_inclusion_variants --strict` at each book-boundary to flag any MT-LXX-cohort verses not classified A/B/C
- [ ] At each book end-of-book audit: include an explicit MT-vs-LXX section that lists the divergences + classifies each into A/B/C + confirms surface vs footer treatment
- [ ] At Joshua 21:36–37 audit time: explicitly decide whether the MT-missing-verses are Category A (inline-bracket like Gen 4:8) or Category B (footer-only). Cross-versional witness count is the decisive factor
- [ ] At Jeremiah audit time: decide whether the entire book uses MT-form, LXX-form, or hybrid — this is a book-level policy decision that compounds across 52 chapters

---

## 6. Change log

- **v0.3** (2026-05-24, 1 Kings EOB) — Added §2.2 `macro_structural_mt_lxx_divergence` subcategory + the canonical 1 Kings book-level prefatory note text. Resolves the 1 Kings audit "MT/LXX inclusion-variant gap" (DECIDE #2, carried from 1 Samuel §17). Ben chose subcategory-not-Tier-4 (ChatGPT over Gemini). Reader-facing book-note + ch.2/11/12/20–21 footers are a pre-`ship_book.sh` follow-up.
- **v0.2** (2026-05-12, later same day) — Gen 4:8 brackets STRIPPED per Ben's BSB-alignment decision. Category A redefined as "inline without brackets, matching BSB" rather than the original "inline-with-square-brackets." Cross-versional manuscript evidence remains in Layer-2 footer. Resolves the ChatGPT-vs-Gemini divergence by adopting BSB's actual rendering style.
- **v0.1** (2026-05-12) — Initial policy, triggered by Genesis end-of-book audit §F + external AI cross-review (ChatGPT + Gemini both MAJOR CONCERN). Genesis-locking-precedents at 4:8 (Category A) + 46:27 + 47:31 (Category B). Originally flagged Ben decision pending on 4:8 bracket; resolved in v0.2 (above).
