# Leviticus external review — response + proposed actions

**Date:** 2026-05-28
**Reviewers:** Gemini + ChatGPT
**Audit packet:** `docs/end_of_book/leviticus/external_review_packet_LEV_2026-05-15.md`
**Raw replies:** `docs/end_of_book/_external_inbox/LEV_raw.md`
**Status:** proposed-edits-pending (one within-book proper-name fix at 23:6; one cross-book GOEL doc-vs-Ruth divergence; LEV 16/17 Layer-2 cross-ref footer additions)

> **Important meta-observation (ChatGPT §Z):** "Doc authority is becoming the main failure point, not translation quality." Items A and B both show docs created after or alongside shipped text but not verified against shipped corpus. **Before tagging LEV: run a doc-lock audit pass** — every newly locked Thai form should be grep-checked against Ruth/Exodus/Numbers/Leviticus actual output before the doc becomes authoritative.

## Convergence summary

| Item | Gemini | ChatGPT | Synthesized | Action |
|------|--------|---------|-------------|--------|
| A — LEV-wide kipper drift from doc (200+ verses) | **MAJOR** | CONCERN | DOC-AMEND, NOT VERSE EDIT | Amend `sacrificial_vocabulary_2026-05.md` §5 to *recognize* ลบมลทินบาป for ritual contexts (the shipped form is **exegetically superior** — fix the doc, not the verses) |
| B — LEV 25:25 goel doc-vs-Ruth divergence | **MAJOR** | CONCERN | **PROPOSED VERSE EDIT** + DOC-AMEND | LEV 25:25 ญาติสนิทที่สุด → ญาติผู้ไถ่ (match Ruth's already-shipped natural form); amend doc |
| C — LEV 23:6 Unleavened Bread drift | CONCERN | CONCERN | **PROPOSED VERSE EDIT** | LEV 23:6 ไม่มีเชื้อ → ไร้เชื้อ (proper-noun feast-name alignment) |
| D — Yobel "Jubilee" rendering | CONCERN | FINE | LOCK + DOCUMENT | Lock ปีจูบีลี; doc the LEV/Joshua-yobel split |
| E — LEV 16 + 17:11 NT cross-reference footer gap | CONCERN | CONCERN | ADD LAYER-2 FOOTERS | Add LEV 16 + LEV 17 Layer-2 footers (LEV 23 optional) before tagging |
| F — "I am YHWH" Holiness Code formula | CONCERN | CONCERN | WRITE LOCK DOC | Write `i_am_yhwh_holiness_formula_2026-05.md` before Ezekiel/John 8 echoes |
| G — Uncover-nakedness hybrid policy | FINE | FINE | LOCK | Write `uncover_nakedness_euphemism_2026-05.md` documenting the hybrid; covers Deut 22:30, 27:20, Ezek 16/22/23, 1 Cor 5:1 |

## Items in detail

### Item A — LEV-wide kipper drift (Gemini MAJOR / ChatGPT CONCERN)
- **Gemini:** MAJOR. The drift affects 200+ verses and directly contradicts a doc drafted on the same date. **But — the shipped Thai (ลบมลทินบาป) is exegetically superior** for Leviticus (e.g. LEV 16:6): it captures the dual moral-ritual purgation framework that ลบบาป alone misses. Path (b): amend the doc, not the verses.
- **ChatGPT:** CONCERN. Same — **"The shipped LEV/NUM surface is not the problem; the doc is."** In Leviticus ritual contexts, כִּפֵּר regularly covers purgation/cleansing of sanctuary/altar/persons/impurity, not only moral "sin-forgiveness." LEV 16:6 ทำการลบมลทินบาป is defensible and likely better than flattening every occurrence to ทำการลบบาป.
- **Action:** **Amend the doc, not the verses.** Update `sacrificial_vocabulary_2026-05.md` §5 to recognize ลบมลทินบาป / การลบมลทิน / ทำการลบมลทินบาป as canonical for ritual-purgation contexts, retaining ลบบาป / ไถ่บาป for moral/non-ritual atonement. Write `check_sacrificial_vocab.py` in the same commit to enforce the programmatic split for future OT books.

### Item B — LEV 25:25 goel doc-vs-Ruth divergence (Gemini MAJOR / ChatGPT CONCERN)
- **Gemini:** MAJOR. Typological linkage between LEV 25:25 (foundational legal text), Ruth 3–4 (primary narrative application), and future theological echoes is broken at the Thai surface. The documented lock (ผู้ไถ่ที่เป็นญาติ) is clunky periphrasis that isn't actually used in either shipped book; Ruth's ญาติผู้ไถ่ is much more natural Thai compound morphology. Path (a): amend doc to lock Ruth's form; spot-revise LEV 25:25.
- **ChatGPT:** CONCERN. Same. LEV 25:25 is the legal foundation for Ruth's Boaz role, so rendering גֹּאֵל as ญาติสนิทที่สุด loses the ไถ่ root precisely where the corpus needs it. **Ruth's ญาติผู้ไถ่ is already better Thai and better corpus precedent than the doc's unused ผู้ไถ่ที่เป็นญาติ.** For Job 19:25 + Isaiah: don't force the exact human compound; preserve root linkage with พระผู้ไถ่; keep suffix where Hebrew has it (Job 19:25 stays פระผู้ไถ่ของข้าพระองค์).
- **Action:** **Spot-revise LEV 25:25 ญาติสนิทที่สุดของเขา → ญาติผู้ไถ่ของเขา.** Amend the goel doc to lock ญาติผู้ไถ่ as canonical human property/levirate form; ผู้ไถ่ allowed as abbreviated in-context form; พระผู้ไถ่ retained for divine Redeemer (Job 19:25 anchor).

### Item C — LEV 23:6 Unleavened Bread feast Thai-drift
- **Gemini:** CONCERN. Single-verse drift in the most important liturgical calendar chapter of the Torah breaks exact-match searchability for a major biblical feast. Consistency in proper nouns + institutional titles is baseline.
- **ChatGPT:** CONCERN. Same. ขนมปังไม่มีเชื้อ is semantically fine but this is a **proper feast-name slot** and the corpus has already standardized `เทศกาลขนมปังไร้เชื้อ`. Drift more visible than incidental food references. Also change the second phrase in the same verse to ขนมปังไร้เชื้อ unless there's a specific reason to leave intra-verse variation.
- **Action:** Spot-revise LEV 23:6: `เทศกาลขนมปังไม่มีเชื้อ` → `เทศกาลขนมปังไร้เชื้อ`; check second phrase in same verse.

### Item D — Yobel "Jubilee" rendering (Gemini CONCERN / ChatGPT FINE)
- **Gemini:** CONCERN. Stated transliteration principle justifies the culturally established ปีจูบีลี (LEV 25:10), but undocumented decision creates a landmine for Joshua 6 (where same lemma yobel = literal "ram's horn"). Lock ปีจูบีลี; amend `proper_names_and_transliteration_2026-05.md` to document the English-via-Latin exception + dictate metonymic/literal yobel handling in Joshua.
- **ChatGPT:** FINE. ปีจูบีลี is reader-familiar + aligns with Thai-Christian Bible usage. In a reader-facing Thai Bible, established ecclesial comprehension should usually override phonological reconstruction unless the Hebrew form is the teaching point. Lock ปีจูบีลี; doc as accepted traditional/theological term. For Joshua 6, handle יוֹבֵל as a related lexical note if needed; **do not force ปีโยเบล into Leviticus.**
- **Action:** Lock ปีจูบีลี (both AIs agree on the lock direction; only the CONCERN/FINE labels differ). Amend `proper_names_and_transliteration_2026-05.md` with the doc note + Joshua-yobel handling instructions.

### Item E — LEV 16 + 17:11 NT cross-reference footer gap
- **Gemini:** CONCERN. LEV 16 and 17:11 are the epicenter of OT atonement theology providing the theological vocabulary for Hebrews 7–10 and ROM 3:25. Failing to explicitly map these via Layer-2 footers breaks the precedent set in GEN/EXO audits.
- **ChatGPT:** CONCERN. Same. **Not marginal cross-reference candidates; central infrastructure for Hebrews, Romans 3:25, and NT blood/atonement language.** If GEN 3:15, 22, EXO 12, 24 receive Layer-2 reader transparency, LEV 16 + 17:11 should as well. Specific mappings: kapporet/mercy seat → Heb 9:5/Rom 3:25; Day of Atonement → Heb 9:7–12; blood-life at LEV 17:11 → Heb 9:22/Rom 3:25. **Treat LEV 23 as optional** (add later only if there's a broader feast-fulfillment note policy).
- **Action:** Write Layer-2 footers for `leviticus_16.json` + `leviticus_17.json` (concise, reader-edition oriented) before tagging. Defer LEV 23 footer.

### Item F — "I am YHWH" Holiness Code formula
- **Gemini:** CONCERN. 52-occurrence structural formula undocumented is reckless; risks massive drift hitting Ezekiel's 65+ + threatens NT linkage to Johannine ego eimi.
- **ChatGPT:** CONCERN. Same. Minor `คือ` omission at LEV 19:2, 20:26 not a translation error but shouldn't remain accidental. Lock bare → `เราคือองค์พระผู้เป็นเจ้า`, expanded → `เราคือองค์พระผู้เป็นเจ้าพระเจ้าของพวกเจ้า`. **Normalize LEV 19:2 to include คือ.** LEV 20:26 can remain structurally different (adds קָדוֹשׁ).
- **Action:** Write `i_am_yhwh_holiness_formula_2026-05.md` locking the bare + expanded forms and Ezekiel's `וִידַעְתֶּם כִּי אֲנִי יְהוָה` recognition formula. **Spot-revise LEV 19:2 to include `คือ`**; document 20:26's principled structural difference.

### Item G — Uncover-nakedness hybrid policy
- **Gemini:** FINE. Hybrid strategy intelligently handles Hebrew register shifts: explicit Thai (มีความสัมพันธ์ทางเพศ) where Hebrew uses relationship pronouns (LEV 18:7); literal anatomical opacity (เปิดเผยความเปลือยเปล่า) where context demands clinical/legal weight (LEV 20:11, 20:18). Draft `uncover_nakedness_euphemism_2026-05.md` to formalize.
- **ChatGPT:** FINE. Hybrid policy is legitimate. **Don't** normalize uniformly to either euphemism-only or explicit-only. Doc should explicitly cover Deut 22:30, Deut 27:20, Ezek 16/22/23, and 1 Cor 5:1 so the LEV → Paul citation path remains visible.
- **Action:** Lock hybrid as-is. Write `uncover_nakedness_euphemism_2026-05.md` with explicit coverage of the downstream verses (per ChatGPT).

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **LEV 25:25** — `ญาติสนิทที่สุดของเขา` → `ญาติผู้ไถ่ของเขา` (Item B; align with Ruth's already-shipped natural form; preserves the ไถ่ root for Boaz typology).
2. **LEV 23:6** — `เทศกาลขนมปังไม่มีเชื้อ` → `เทศกาลขนมปังไร้เชื้อ` (Item C; proper feast-name standardization); check second phrase in same verse.
3. **LEV 19:2** — add `คือ` if currently omitted (Item F).
4. **LEV 16 + LEV 17 Layer-2 footers** — add (Item E; not main-text edits but new metadata files in `output/textual_variants/`).

## Proposed new / amended translator decision docs

- **Amend `sacrificial_vocabulary_2026-05.md` §5** — recognize ลบมลทินบาป as canonical for ritual-purgation contexts; retain ลบบาป/ไถ่บาป for moral. Write `check_sacrificial_vocab.py`.
- **Amend the goel doc** — lock `ญาติผู้ไถ่` as canonical human; abbreviated ผู้ไถ่ allowed; พระผู้ไถ่ for divine (Job 19:25, Isaiah anchors).
- **Amend `proper_names_and_transliteration_2026-05.md`** — document ปีจูบีลี as accepted traditional Thai-Christian term + Joshua-yobel split (literal "ram's horn" treatment).
- **Amend (already exists): `i_am_yhwh_holiness_formula_2026-05.md`** — lock bare + expanded forms + Ezekiel recognition formula + John 8 ego eimi forward-link.
- **Amend (already exists): `uncover_nakedness_euphemism_2026-05.md`** — explicit hybrid policy covering Deut 22:30, 27:20, Ezek 16/22/23, 1 Cor 5:1.

## Process discipline (ChatGPT §Z — important pattern across the backlog)

**"Doc authority is becoming the main failure point, not translation quality."** Before tagging book-leviticus-v1:
- **Doc-lock audit pass** — every newly locked Thai form should be grep-checked against Ruth/Exodus/Numbers/Leviticus actual output before the doc becomes authoritative.
- This same discipline should apply to all the proposed docs across the 19-book backlog. Many "drifts" being flagged are actually shipped Thai diverging from docs written *after* the shipped Thai existed.

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/LEV_raw.md` (Cowork → Gemini + ChatGPT, 2026-05-28). All content above is the AIs' findings; no fresh analysis added. Strong convergence across all 7 items; the most notable finding is the meta-observation about doc-vs-corpus drift (Items A + B; ChatGPT §Z). Verse-edit proposals flagged for Ben's sign-off per the read-only-translation rule.
