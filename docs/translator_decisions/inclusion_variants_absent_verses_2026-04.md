# Inclusion variants — three-tier policy (LOCKED)

**Status:** **LOCKED 2026-04-20** as **Path A** after end-of-book editorial review of Matthew + external AI sanity-checks (Gemini, Claude, Grok). Implements the convention canonized in `RULES.md §5`.

**Scope:** Whole-verse and large-fragment inclusion variants — readings where mainstream traditions (TR, Byz, KJV, sometimes THSV) include text that SBLGNT/NA28/UBS5 critical text omits. Distinct from word-choice variants (handled in `thai_summary` only).

---

## The locked rule

Inclusion variants are handled at three tiers, matching what BSB / ESV / NIV / CSB do for the critical-text English-Bible market:

| Tier | Variant type | Treatment | Source of truth |
|------|--------------|-----------|-----------------|
| **1** | Short phrase within an existing verse | Single brackets `[...]` in `thai` field; rationale in `thai_summary` + `key_decisions` | `output/translations/<slug>_NN.json` |
| **2** | Whole verse SBLGNT omits | Verse number absent from main flow; chapter-footer note shows TR/Byz Thai + witnesses + explanation | `output/textual_variants/<slug>_NN.json` |
| **3** | Large multi-verse block | `⟦double brackets⟧` in main text + extended verse note | `output/translations/<slug>_NN.json` (the verses themselves) |

**Reader-trust rationale carries through all three tiers:** Thai readers cross-checking with THSV/THKJV/their childhood Bible see *something* surfacing the omitted text — never a silent jump in verse numbers without explanation.

---

## Why Path A (over Options B and C considered earlier)

Three options were on the table after the end-of-book review surfaced the inconsistency at MAT 17:21 / 18:11 (silent-skip) vs. MAT 23:14 (Tier 1 single-bracket). Three external AI reviewers split:

- **Option B** (Grok): bracket-include all whole-verse variants in main text, including future Johannine Comma. **Rejected** because (a) commits us to printing the Comma in brackets in 1 John 5:7b–8a — a theological signal not supported by the project's text-critical position; (b) requires translating from a non-base-text manuscript tradition for low-attestation insertions; (c) flattens real text-critical differences between strong-MS-supported variants (23:14 Byz) and late-Byz/TR-only insertions (Comma).

- **Option C — tiered, my earlier draft** (Claude session A): bracket-include for strong-MS variants (23:14), footer-note for late-Byz/TR (17:21, 18:11), double-brackets for large blocks. **Rejected as overly complex** once the Grok-pulled BSB/ESV data showed mainstream critical-text translations don't actually make the Tier-1-strong-MS / Tier-2-late-Byz split — they uniformly footnote whole-verse variants regardless of MS weight.

- **Option A (chosen, here named "Path A")**: pure BSB/ESV/NIV/CSB pattern. Whole-verse variants → footer note, regardless of MS weight. Single-brackets reserved for inline phrase-level variants (where the verse exists). Double-brackets reserved for large-block transmissions. **Chosen** because:
  1. Matches the dominant convention in modern critical-text translations (BSB, ESV, NIV, CSB, NRSV-Updated all do this).
  2. THSV (Thai Standard Version) follows critical text — Thai readers cross-checking will recognize the convention.
  3. One unified rule per tier — no per-verse adjudication of "is this Byz weight strong enough."
  4. Doesn't pre-commit us to bracket-printing the Johannine Comma. The Comma will be Tier 2 (footer note), correctly signaling "scholarly consensus omits" without main-text appearance.
  5. Methodologically clean: we never translate from a different manuscript tradition into our main verse-by-verse text. Footer-note Thai is provided as a reader aid, clearly demarcated as TR/Byz reading.

---

## Implementation (2026-04-20)

**JSON shape (Tier 2):**

`output/textual_variants/<slug>_NN.json` — list of inclusion-variant footer entries for that chapter:

```json
[
  {
    "verse": 21,
    "type": "inclusion_variant_absent",
    "tr_byz_greek": "<Greek text from TR/Byz>",
    "tr_byz_thai": "<Thai rendering of the TR/Byz text — for footer display>",
    "bsb_english_equivalent": "<short English gloss>",
    "witnesses_include": "<MS list — e.g. TR, Byz, KJV, THKJV>",
    "witnesses_omit": "<MS list — e.g. SBLGNT, NA28, ℵ, B; ESV, NIV, BSB, THSV>",
    "explanation_thai": "<short Thai explanation of the textual situation>",
    "cross_reference": "<parallel verse where same content is undisputed, if applicable>"
  }
]
```

**Renderer (`scripts/render_reader.py`):**

After rendering all main-flow verses for a chapter, if `output/textual_variants/<slug>_NN.json` exists, append a `### หมายเหตุด้านต้นฉบับ` section with one block per absent verse: verse number, the TR/Byz Thai rendering (in blockquote), the explanation (italic), then witness lists.

**Bundle (`scripts/build_eremos_bundle.py`):**

Currently the bundle exports only verses (no footer notes). Tier 2 entries do NOT appear in the iOS app's verse popup until the app's data layer learns to consume `output/textual_variants/`. This is **acceptable lag** — the reader doc on github.com is the immediate audience for footer notes; the app surfaces notes when its UI catches up. Tracked as future work.

**Migration of MAT 23:14 (2026-04-20):**

23:14 was previously Tier 1 (bracket-include in `output/translations/matthew_23.json` per the 2026-04-18 short-phrase convention extended to whole-verse). Migrated to Tier 2 (footer note in `output/textual_variants/matthew_23.json`) under Path A. The verse no longer appears in the main verse list of `matthew_23.json` (39 → 38 verses). Bundle change ships with this commit. Net app effect: 23:14 verse-popup disappears until app learns Tier 2 rendering.

---

## Implementation status

**Locked + implemented (2026-04-20):**
- ✅ MAT 17:21 → Tier 2 footer note (`output/textual_variants/matthew_17.json`)
- ✅ MAT 18:11 → Tier 2 footer note (`output/textual_variants/matthew_18.json`)
- ✅ MAT 23:14 → migrated from Tier 1 to Tier 2 (`output/textual_variants/matthew_23.json`)
- ✅ Renderer updated (`scripts/render_reader.py`)
- ✅ `RULES.md §5` updated with the three-tier convention
- ✅ Mark 1:1, 3:14, 9:29 retained as Tier 1 (correct per new policy)
- ✅ Mark 16:9–20 retained as Tier 3 (⟦double brackets⟧, no change)

**Future work:**
- Bundle / iOS app: learn to consume `output/textual_variants/` and render footer notes in chapter view (Phase 2; not blocking this lock).
- 16:2b–3 and 21:44 (in Matthew): both currently included unmarked. Per Path A, since they ARE in our SBLGNT base, no Tier 2 treatment is needed. They sit outside the inclusion-variant policy entirely. (These would be handled at the level of *exclusion* variants — different convention, not in scope here.)
- Future Acts 8:37, 15:34, Romans 16:24 → Tier 2 footer notes when those chapters are translated.
- Future Johannine Comma (1 John 5:7b–8a) → Tier 2 footer note when 1 John is translated.
- Future John 7:53–8:11 (pericope adulterae) → Tier 3 ⟦double brackets⟧ when John is translated.

---

## Why this matters going forward

Locking Path A before Acts and the Pauline epistles avoids:
- Re-litigating each variant individually
- Drifting into bracketed-Comma territory
- Synthesizing a Greek text that doesn't exist in any single MS tradition
- Mismatching our Thai reader's expectations from THSV cross-checking

The three-tier policy gives translators a clear, unambiguous decision tree for every inclusion-variant case they'll encounter for the rest of the NT.

---

## Cross-reference

- `docs/MAT_END_OF_BOOK_REVIEW_2026-04-19.md` §14 — review that surfaced the inconsistency.
- `RULES.md §5` — the canonical rules statement.
- External-AI review feedback (Gemini, Claude session A, Grok, 2026-04-20).
- `output/textual_variants/matthew_{17,18,23}.json` — first three Tier 2 entries.
- `scripts/render_reader.py` — Tier 2 rendering implementation.
