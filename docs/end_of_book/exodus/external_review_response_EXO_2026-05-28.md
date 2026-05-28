# Exodus external review — response + proposed actions

**Date:** 2026-05-28
**Reviewers:** Gemini + ChatGPT
**Audit packet:** `docs/end_of_book/exodus/external_review_packet_EXO_2026-05-13.md`
**Raw replies:** `docs/end_of_book/_external_inbox/EXO_raw.md`
**Status:** proposed-edits-pending (4 MAJOR CONCERNs; substantial post-lock-drift normalization required before tagging book-exodus-v1)

> **Pattern (from ChatGPT §Z):** The main issue is not random translation weakness; it is **post-lock drift** — docs created at/after ship time but not yet enforced against the shipped corpus. Priority before tagging: A → B → H → D (doc) → E → C → F → G.

## Convergence summary

| Item | Gemini | ChatGPT | Synthesized | Action |
|------|--------|---------|-------------|--------|
| A — EXO 34:6–7 Sinai attribute formula drift | **MAJOR** | **MAJOR** | NORMALIZE | **PROPOSED VERSE EDITS** — spot-revise to canonical doc Thai before tagging |
| B — EXO 33:19 חנן / רחם mapping swapped | **MAJOR** | CONCERN | NORMALIZE | **PROPOSED VERSE EDIT** — fix mapping; check Rom 9:15 alignment |
| C — EXO 15:11 "among the gods" בָּאֵלִם | CONCERN | CONCERN | LOCK + WRITE DOC | Lock ในหมู่พระทั้งหลาย; write `ot_polytheistic_register_2026-05.md` |
| D — מַלְאַךְ YHWH 4-way drift in Exodus | **MAJOR** | CONCERN | NORMALIZE | **PROPOSED VERSE EDITS** — 6 occurrences → ทูตสวรรค์ family; write `malak_yhwh_2026-05.md` |
| E — EXO 17:15 YHWH-Nissi paraphrase vs transliteration | CONCERN | CONCERN | DECIDE | Both AIs lean transliteration+gloss like GEN 22:14; amend `divine_names_table_2026-05.md` |
| F — Pharaoh heart-hardening (3 roots → single Thai) | FINE | FINE | LOCK | Write `pharaoh_heart_hardening_2026-05.md` |
| G — EXO 33:14–15 פָּנִים face/presence | CONCERN | CONCERN | SPLIT RULE | Amend `hebrew_idioms_and_metaphor_2026-05.md`; **PROPOSED EDITS at 33:20/23** |
| H — EXO 40:20 כַּפֹּרֶת within-book drift (8:1) | **MAJOR** | CONCERN | NORMALIZE | **PROPOSED VERSE EDIT** — 40:20 normalize to within-book majority |

## Items in detail

### Item A — EXO 34:6–7 Sinai attribute formula drift (MAJOR / MAJOR)
- **Gemini:** Shipped 34:6–7 strips royal ทรง- register, shifts "ความซื่อสัตย์" → "ความจริง", violating `exod_34_attribute_formula_2026-05.md`. Failing to normalize the first-occurrence recitation breaks the cross-corpus lemma thread for every subsequent OT quote (Num 14:18, Jonah 4:2, Psalms).
- **ChatGPT:** Same MAJOR. EXO 34:6–7 is the **canonical source-text location** for the locked formula. Nearly every locked component is broken: חַנּוּן, רַחוּם, אֶרֶךְ אַפַּיִם, רַב־חֶסֶד, אֱמֶת, נֹשֵׂא עָוֹן, פֹּקֵד עָוֹן. Since Jonah 4:2 has already been normalized to the doc, leaving Exodus divergent makes the corpus lock incoherent at its source.
- **Action:** **Spot-revise EXO 34:6–7 to the doc-canonical Thai before tagging book-exodus-v1.** Implement `check_phrase_consistency.py` hard-fail when 3+ formula components co-occur without locked Thai. Both AIs agree this is the #1 priority.

### Item B — EXO 33:19 חנן / רחם mapping swapped (Gemini MAJOR / ChatGPT CONCERN)
- **Gemini:** MAJOR. Current rendering contradicts both the project's locked nominal-form mapping AND the adjacent 34:6 proclamation. Wires are crossed on roots חנן and רחם.
- **ChatGPT:** CONCERN. Same. 33:19 is structurally paired with 34:6; חנן should track พระคุณ, רחม should track พระเมตตา. Sharper because Rom 9:15 quotes this verse — OT side shouldn't drift before NT cross-reference is checked.
- **Action:** Spot-revise to: `"เราจะทรงพระคุณต่อผู้ที่เราจะทรงพระคุณ และเราจะทรงพระเมตตาต่อผู้ที่เราจะทรงพระเมตตา"`. Then check Rom 9:15 alignment or document intentional NT/OT asymmetry.

### Item C — EXO 15:11 "among the gods" בָּאֵלִם
- **Gemini:** CONCERN. ในหมู่พระทั้งหลาย faithfully translates Hebrew plural but introduces theological friction for Thai-evangelical readers. Write `ot_polytheistic_register_2026-05.md`; Ben to decide between academic-equivalence (A) and theological-clarity (B).
- **ChatGPT:** CONCERN. Same. Defensible because it preserves the Hebrew poetic surface of בָּאֵלִם and the "YHWH incomparable among the gods" idiom. **Don't** flatten to เทพเจ้าใดเหมือนพระองค์ — that protects later monotheistic comfort at the cost of obscuring Hebrew rhetorical register. Doc should distinguish "preserved ancient divine-council / incomparable" idiom from idolatry-polemic contexts.
- **Action:** Lock current Hebrew-faithful approach. Write `ot_polytheistic_register_2026-05.md`. (Already exists in some form per other reviews; verify and amend.)

### Item D — מַלְאַךְ YHWH 4-way drift in Exodus (Gemini MAJOR / ChatGPT CONCERN)
- **Gemini:** MAJOR. 4 distinct Thai phrases for identical Hebrew lemma across 6 occurrences violates consistency and artificially creates ontological categories not in the source. Normalize all 6 to ทูตสวรรค์ family.
- **ChatGPT:** CONCERN. Same. False Thai category split between ทูต and ทูตสวรรค์ where Hebrew uses the same lemma-family. Specific normalizations: 3:2 → ทูตสวรรค์ขององค์พระผู้เป็นเจ้า; 14:19 → ทูตสวรรค์ของพระเจ้า; 32:34 → ทูตสวรรค์ของเรา. Don't create a separate Thai surface for possible Christophanic "angel of YHWH"; keep lexical rendering stable, let verse-level KD carry theophany distinction.
- **Action:** **Normalize all 6 Exodus occurrences to ทูตสวรรค์ family** (3:2, 14:19, 23:20, 23:23, 32:34, 33:2). Write `malak_yhwh_2026-05.md` to lock NT-aligned translation for all OT theophanies.
- **Cross-book impact:** Same lock + checker should cover NUM Item B (11 occurrences flagged MAJOR by both AIs), 1CH Item A (1 Chr 21 already clean), 1KI Item A (19:7 drift, MAJOR), 2KI Item E (human-messenger variation OK), 2CH (machine-enforce). One doc, multi-book normalization queue.

### Item E — EXO 17:15 YHWH-Nissi paraphrase vs transliteration
- **Gemini:** CONCERN. 17:15 drifts from transliteration+gloss precedent at GEN 22:14 for YHWH-compounded names without documented justification. Write/amend `divine_names_table_2026-05.md` with "YHWH-paraphrastic-self-title" sub-category. Ben to decide if 17:15 should be retroactively transliterated.
- **ChatGPT:** CONCERN. 17:15 is closer to GEN 22:14 than 15:26 / 31:13 because Moses names an altar with a YHWH-compound. Spot-revise to transliteration + gloss: `โมเสสสร้างแท่นบูชาและตั้งชื่อว่า "ยาห์เวห์นิสซี (องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า)"`. Amend table with two categories: YHWH place/altar-name compounds → transliteration + parenthetical gloss; YHWH self-attribution titles (15:26, 31:13) → paraphrase, not mandatory transliteration.
- **Action:** Both AIs lean toward transliteration+gloss at 17:15 (it's altar-naming, like GEN 22:14). Spot-revise per ChatGPT's text. Amend `divine_names_table_2026-05.md` with the two-category split.

### Item F — Pharaoh heart-hardening
- **Gemini:** FINE. Uniform "แข็งกระด้าง" safely protects the critical exegetical data (who is doing the hardening via causative vs stative syntax). Aligns with Rom 9 and John 12 NT trajectories which don't rely on the 3-root distinction.
- **ChatGPT:** FINE. Same. Single Thai idiom is defensible because subject-agency remains syntactically explicit.
- **Action:** Lock as-is. Write `pharaoh_heart_hardening_2026-05.md` documenting the three-Hebrew-roots-to-single-Thai principle + subject-agency syntactic explicitness.

### Item G — EXO 33:14–15 פָּנִים face/presence
- **Gemini:** CONCERN. Switching to "การประทับ" at 33:14–15 breaks `hebrew_idioms_and_metaphor_2026-05.md` lock; masks the intentional theological paradox. Spot-revise 33:14, 33:15, 33:20, 33:23 to พระพักตร์ (Option A).
- **ChatGPT:** CONCERN. Nuanced split: 33:14–15 (motion idiom — "my face will go") is defensible as การประทับ; but 33:20/23 (seeing/sensory verbs) **should not** use plain ใบหน้า — that undercuts the royal-register lock. Amend `hebrew_idioms_and_metaphor_2026-05.md` with sub-rule: motion idiom → การประทับ; sensory verbs for YHWH → พระพักตร์.
- **Action:** **Take ChatGPT's split rule** (preserves both natural Thai for the motion idiom and royal register for sensory verbs). **PROPOSED VERSE EDITS at 33:20 and 33:23**: ใบหน้าของเรา → พระพักตร์ของเรา. Leave 33:14–15 as การประทับ unless Thai reviewers confirm พระพักตร์ของเราจะไปกับเจ้า sounds natural.

### Item H — EXO 40:20 כַּפֹּרֶת within-book drift (Gemini MAJOR / ChatGPT CONCERN)
- **Gemini:** MAJOR. 8-to-1 split within the same book for a theologically dense tabernacle object. Anchors ROM 3:25 + HEB 9:5 propitiation theology. Ben to decide corpus-wide — Gemini recommends Option B (`ที่ลบล้างบาป` for NT ἱλαστήριον alignment); spot-revise all 9.
- **ChatGPT:** CONCERN. One-off `ที่ลบล้างบาป` in 40:20 breaks within-book consistency after 8 prior uses of `พระที่นั่งกรุณา`. **Spot-revise 40:20 to พระที่นั่งกรุณา for Exodus consistency** (the opposite direction from Gemini). Then write `kapporet_atonement_cover_2026-05.md` locking พระที่นั่งกรุณา with key-decision notes explaining the כפר / ἱλαστήριον connection.
- **⚠ Divergent direction:** Gemini wants `ที่ลบล้างบาป` everywhere (NT-aligned); ChatGPT wants `พระที่นั่งกรุณา` everywhere (within-book majority). **Ben breaks the tie.** Decision factor: which is more important — within-book consistency at the install scene (ChatGPT) or NT-typology alignment with ἱλαστήριον (Gemini)?
- **Cross-book agreement:** HEB Item F and 1JN Item B both lock HEB 9:5 = `พระที่นั่งกรุณา` (physical mercy-seat) and ROM 3:25 = `เครื่องบูชาไถ่บาป` (Pauline atonement). So the NT side actually splits — the kapporet/object sense uses พระที่นั่งกรุณา. **That argues for ChatGPT's direction here**: lock พระที่นั่งกรุณา in Exodus (the tabernacle-object book), aligning with HEB 9:5's same-sense use.

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **EXO 34:6–7** — normalize to canonical doc Thai per `exod_34_attribute_formula_2026-05.md` (Items A, both MAJOR).
2. **EXO 33:19** — fix חנן/רחם mapping to: *"เราจะทรงพระคุณต่อผู้ที่เราจะทรงพระคุณ และเราจะทรงพระเมตตาต่อผู้ที่เราจะทรงพระเมตตา"* (Item B, both flag — Gemini MAJOR).
3. **EXO 3:2, 14:19, 23:20, 23:23, 32:34, 33:2** — normalize 6 מַלְאַךְ YHWH occurrences to ทูตสวรรค์ family (Item D, Gemini MAJOR).
4. **EXO 17:15** — paraphrase → transliteration+gloss: *"ยาห์เวห์นิสซี (องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า)"* (Item E, both).
5. **EXO 33:20, 33:23** — `ใบหน้าของเรา` → `พระพักตร์ของเรา` (Item G, ChatGPT split rule preserves both AIs' concerns).
6. **EXO 40:20** — normalize to `พระที่นั่งกรุณา` (ChatGPT direction; aligned with HEB 9:5 same-sense lock). **Divergent direction — Ben confirms.**

## Proposed new / amended translator decision docs (priority-ordered)

**Highest priority — required before tagging book-exodus-v1:**
- Amend (or write) `exod_34_attribute_formula_2026-05.md` enforcement — script + verses normalized.
- **Amend (already exists): `malak_yhwh_2026-05.md`** — corpus-wide lock; multi-book normalization queue (EXO/NUM/1KI mentioned; 1CH/2CH machine scope).
- **Amend (already exists): `kapporet_atonement_cover_2026-05.md`** — lock пра that นั่งกรุณา (per HEB 9:5 alignment); explains כפר / ἱλαστήριον connection for LEV 16, ROM 3:25, HEB 9:5.
- **Amend (already exists): `ot_polytheistic_register_2026-05.md`** — distinguish preserved divine-council / incomparable-among-gods idiom from idolatry-polemic contexts.
- **Amend (already exists): `pharaoh_heart_hardening_2026-05.md`** — 3-Hebrew-roots-to-single-Thai principle.
- Amend `divine_names_table_2026-05.md` — two-category YHWH compound rule (place/altar-name → translit+gloss; self-attribution → paraphrase).
- Amend `hebrew_idioms_and_metaphor_2026-05.md` — פָּנִים sub-rule (motion idiom → การประทับ; sensory verbs for YHWH → พระพักตร์).

**Process / checker:**
- Implement `check_phrase_consistency.py` hard-fail when 3+ Sinai-formula components co-occur without locked Thai.

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/EXO_raw.md` (Cowork → Gemini + ChatGPT, 2026-05-28). All content above is the AIs' findings; no fresh analysis added. Strong convergence on A, B, F, G principle; partial divergence on H direction (NT-typology vs within-book majority — Ben to decide). ChatGPT supplied an explicit priority order in its §Z. Verse-edit proposals flagged for Ben's sign-off per the read-only-translation rule. Pattern note from ChatGPT: most of Exodus's issues are **post-lock drift** — docs created at/after ship time but not yet enforced against the corpus.
