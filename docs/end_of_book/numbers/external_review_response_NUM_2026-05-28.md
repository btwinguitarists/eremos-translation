# Numbers external review — response + proposed actions

**Date:** 2026-05-28
**Reviewers:** Gemini + ChatGPT
**Audit packet:** `docs/end_of_book/numbers/external_review_packet_NUM_2026-05-14.md`
**Raw replies:** `docs/end_of_book/_external_inbox/NUM_raw.md`
**Status:** proposed-edits-pending (3 MAJOR CONCERNs both AIs — Items A, B, D are blocking before book-numbers-v1 tag)

> **Both AIs converge on the pre-tag blocker set:** Items A (Sinai formula recitation), B (mal'akh-YHWH 11-verse cluster), and D (Sinai transliteration). C and F are policy/doc decisions. E is template/script hygiene.

## Convergence summary

| Item | Gemini | ChatGPT | Synthesized | Action |
|------|--------|---------|-------------|--------|
| A — NUM 14:18 Sinai attribute-formula drift | **MAJOR** | **MAJOR** | **PROPOSED VERSE EDIT** — normalize to doc-canonical Thai in tandem with EXO 34 commit |
| B — NUM 20:16 + 22:22–35 mal'akh-YHWH cluster (11 verses) | **MAJOR** | **MAJOR** | **PROPOSED VERSE EDITS** — all 11 → ทูตสวรรค์ family |
| C — NUM 25 + 31 warfare/sexual-violence reader crux | CONCERN | CONCERN | KEEP SURFACE + LAYER-2 FOOTERS | Write `ot_warfare_ethics_2026-05.md`; add Layer-2 at NUM 25 + NUM 31 |
| D — Sinai ซีนาย/สีนาย mix within NUM + drift from EXO | CONCERN | CONCERN | **PROPOSED VERSE EDITS** | 10× สีนาย → ซีนาย; also normalize Succoth in NUM 33:5–6 to สุคโคท (ChatGPT) |
| E — Numbers YHWH first-occurrence footnote template drift (ch.15+) | FINE | CONCERN | **DIVERGENT DIRECTION** | Gemini: loosen script; ChatGPT: restore the canonical template in NUM 15–36 |
| F — NUM 14:17 standalone אֲדֹנָי vocative | CONCERN | CONCERN | DOC-AMEND | Add sub-rule in `divine_names_table_2026-05.md`; NUM 14:17 as locking precedent |

## Items in detail

### Item A — NUM 14:18 Sinai attribute-formula drift (MAJOR / MAJOR)
- **Gemini:** MAJOR. Sinai attribute-formula is a foundational OT divine self-revelation; preserving the cross-corpus lemma-thread is exactly why `exod_34_attribute_formula_2026-05.md` was created. Current NUM 14:18 diverges on every locked vocabulary item (e.g. "ความผิด" instead of "ความชั่ว"), breaking reader recognition of this vital cross-book recurrence.
- **ChatGPT:** MAJOR. Not merely similar to Exod 34:6–7 — it is a **direct shortened recitation** of the same formula. Since the project already locked this recitation family, the shipped Thai breaks the recognition-thread at the first downstream witness.
- **Action:** **Spot-revise NUM 14:18 to the doc-canonical Thai in tandem with the EXO 34 normalization** (Items pair with EXO Item A). Write `check_phrase_consistency.py` extension with hard-fail when 3+ formula components co-occur without locked Thai. Strong both-AI convergence.

### Item B — NUM 20:16 + 22:22–35 mal'akh-YHWH cluster (MAJOR / MAJOR)
- **Gemini:** MAJOR. Rendering mal'akh YHWH as just `ทูต` (envoy) strips the supernatural/heavenly marker from one of OT's most iconic narratives (Balaam's donkey). `malak_yhwh_2026-05.md` mandates ทูตสวรรค์ to align with NT angelos lock; specifically targeted NUM 22 for forward-cover.
- **ChatGPT:** MAJOR. Same. NUM 22:22–35 is a dense, repeated cluster; current `ทูตขององค์พระผู้เป็นเจ้า` loses the supernatural/angelic marking carried by the locked `ทูตสวรรค์` form. NUM 20:16 belongs in the same divine-deliverance category unless explicitly classified as human envoy (context doesn't require that).
- **Action:** **Normalize all 11 occurrences to ทูตสวรรค์ family.** Specific:
  - NUM 20:16 → ทูตสวรรค์
  - NUM 22:22, 23, 24, 25, 26, 27, 31, 32, 34, 35 → ทูตสวรรค์ขององค์พระผู้เป็นเจ้า
  Surface Thai stays lexically uniform; theophanic/Christophanic distinction goes in Layer 2, not a separate surface rendering.
- **Cross-book lock:** Same `malak_yhwh_2026-05.md` covers EXO Item D (6 verses), 1KI Item A (19:7), 2CH check-script scope. Multi-book normalization in one doc + script pass.

### Item C — NUM 25 + 31 warfare / sexual-violence reader crux
- **Gemini:** CONCERN. Severe interpretive crux for evangelical readers; literal Thai must remain faithful (currently is). Leaving without an interpretive framework abandons readers and invites compounding friction in Deuteronomy + Joshua. Write `ot_warfare_ethics_2026-05.md`; Layer-2 footers for NUM 31 + NUM 25.
- **ChatGPT:** CONCERN. Same. Shipped Thai for NUM 31:17–18 is textually faithful and shouldn't be softened. **Don't revise the verse surface.** Doc establishes forward policy for Deut 7/20/25, Joshua 6–11, 1 Sam 15, related ḥerem/warfare texts.
- **Action:** Write `ot_warfare_ethics_2026-05.md` (may already exist per other reviews — verify and amend if so). Add Layer-2 footers at NUM 25 + NUM 31. Verse surface unchanged.

### Item D — Sinai ซีนาย/สีนาย mix
- **Gemini:** CONCERN. Internal book inconsistency (10 vs 27 occurrences) + cross-book drift from Exodus (100% ซีนาย) violates proper-noun consistency rules. ซีนาย aligns with THSV-1971 precedent.
- **ChatGPT:** CONCERN. Mechanical proper-name consistency, not semantic debate. **Also normalize Succoth in NUM 33:5–6 to the Exodus form `สุคโคท`** (extra catch). Add both to `glossary.json` / proper-name checker.
- **Action:** **Spot-revise 10× สีนาย → ซีนาย in Numbers.** **Also normalize Succoth in NUM 33:5–6 → สุคโคท** (ChatGPT). Extend glossary + proper-name check-script to lock corpus-wide; prevent drift in Deuteronomy / Judges / Psalms.

### Item E — NUM YHWH first-occurrence footnote template drift (Gemini FINE / ChatGPT CONCERN — ⚠ divergent direction)
- **Gemini:** FINE. The post-chapter-14 template is well-formed, concise, accurately references the project's NT-aligned standard. **Loosen the script** (Option b) by adding "ตามแบบแผนของฉบับพันธสัญญาใหม่" to `check_divine_names.py`'s detection set. Adopt the shorter template as the going-forward standard to avoid 22 manual edits.
- **ChatGPT:** CONCERN. Footnotes are present and reader-acceptable; problem is **template drift plus false-positive script warnings**. Canonical per-chapter convention; inconsistent wording inside one tagged book is undesirable. **Restore the `ยาห์เวห์` Yahweh phrase in NUM 15–36** for this tagged book, then separately decide whether the shorter template becomes future standard.
- **Action: ⚠ Ben to decide direction.** Gemini: loosen the script + adopt shorter template (less work, accepts the drift). ChatGPT: restore the canonical template in 22 chapters (more work, preserves the existing convention). Compromise: ChatGPT explicitly suggests extending the check script to recognize both templates so future convention changes don't create false positives — that lowers the risk of either choice. Both AIs would accept a "doc both templates, normalize at next tag" path.

### Item F — NUM 14:17 standalone אֲדֹנָי vocative
- **Gemini:** CONCERN. Current `องค์พระผู้เป็นเจ้าของข้าพระองค์` captures the personal petitionary vocative force which the flatter title lock (`องค์เจ้านาย`) lacks. Prayer-vocative pattern will appear hundreds of times in Psalms + Prophets; must be codified, not left as script-invisible exception. Amend `divine_names_table_2026-05.md` with sub-rule; NUM 14:17 as OT locking precedent.
- **ChatGPT:** CONCERN. Same. Strictly rendering all standalone אֲדֹנָי as องค์เจ้านาย preserves the table but will sound wooden in vocative prayer contexts. Sub-rule: standalone אֲדֹנָי as prayer-vocative within direct address to YHWH may render as `องค์พระผู้เป็นเจ้าของข้าพระองค์`. NUM 14:17 as locking precedent. **Don't normalize this verse** to `องค์เจ้านาย` unless Ben decides the lexical distinction must override Thai prayer-register naturalness.
- **Action:** Amend `divine_names_table_2026-05.md` with the sub-rule. Lock NUM 14:17 as precedent. Strong both-AI convergence on keeping the current verse + documenting.
- **Cross-book agreement:** JOS Item E and JDG Item B both propose a 4-way Adonai distinction that incorporates this. **Coordinate as one doc-amendment.**

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **NUM 14:18** — normalize Sinai-formula recitation to doc-canonical Thai per `exod_34_attribute_formula_2026-05.md` (Item A, both MAJOR). **Pair with EXO 34:6–7 in the same commit.**
2. **NUM 20:16 + NUM 22:22, 23, 24, 25, 26, 27, 31, 32, 34, 35** — 11 mal'akh-YHWH occurrences → ทูตสวรรค์ family (Item B, both MAJOR). Pair with the malak_yhwh corpus-wide lock + check-script.
3. **NUM 10× สีนาย → ซีนาย** — proper-noun normalization to match Exodus (Item D).
4. **NUM 33:5–6 — Succoth → สุคโคท** — additional ChatGPT catch in the same proper-noun pass (Item D).
5. **Optional (DIVERGENT): NUM 15–36 YHWH first-occurrence footnotes** — restore canonical template (ChatGPT direction) OR loosen the script (Gemini direction). Ben decides.

## Proposed new / amended translator decision docs

**Highest priority (paired with EXO normalization):**
- Enforce `exod_34_attribute_formula_2026-05.md` corpus-wide via `check_phrase_consistency.py` extension.
- **New: `malak_yhwh_2026-05.md`** — unified lock covering EXO/NUM/1KI/2CH normalizations + 1CH/2KI documented variation.

**Before Deuteronomy / Joshua tagging:**
- **New: `ot_warfare_ethics_2026-05.md`** — forward policy for ḥerem/warfare/sexual-violence texts. Layer-2 footers at NUM 25 + NUM 31.

**Coordinated with JOS Item E + JDG Item B:**
- **Amend `divine_names_table_2026-05.md`** with the 4-way Adonai distinction (standalone prayer-vocative = `องค์พระผู้เป็นเจ้าของข้าพระองค์`; NUM 14:17 anchor).

**Process / checker:**
- Add Sinai + Succoth to `glossary.json` / proper-name check-script for corpus-wide lock.
- Extend `check_divine_names.py` to recognize multiple footnote templates (ChatGPT) so future convention changes don't create false positives.

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/NUM_raw.md` (Cowork → Gemini + ChatGPT, 2026-05-28). All content above is the AIs' findings; no fresh analysis added. Very strong convergence on the blocker set (A, B, D — both MAJOR); minor direction divergence at Item E (script vs verse restoration). Pre-tag blockers per both AIs: A, B, D. C and F are doc/policy decisions. Verse-edit proposals flagged for Ben's sign-off per the read-only-translation rule.

Also: there's a pre-existing `DECISIONS_NEEDED_NUM_2026-05-15.md` in this book's folder which should be cross-checked against these proposals to ensure nothing here contradicts already-pending decisions.
