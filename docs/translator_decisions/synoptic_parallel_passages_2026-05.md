# Synoptic / parallel-passage corpus policy

**Scope:** When two or more OT books contain parallel narrative or poetry (Samuel↔Chronicles, Kings↔Chronicles, 2 Sam 22 ≈ Ps 18, Isa 36–39 ≈ 2 Kgs 18–20, Jer 52 ≈ 2 Kgs 25, Mic 4:1–3 ≈ Isa 2:2–4, etc.), how does the project translate each passage and what does the reader see at Layer 1 vs Layer 2?

**Decided:** 2026-05-23 (Ben + ChatGPT + Gemini convergent CONCERN verdict on 2 SA audit Item C — first major OT-side precedent for parallel-passage handling).

**Triggered by:** 2 Samuel created the first large-scale OT parallel-passage corpus. 2 Sam 22 ≈ Ps 18 (51 verses of poetry with stylistic variants) and 2 Sam 5–24 ≈ 1 Chr 11–21 (the Davidic narrative). Ad-hoc handling in 2 Samuel was sound but unsustainable as the corpus scales into Kings, Chronicles, Psalms, Isaiah, and Jeremiah.

**Companion docs:** `divine_names_table_2026-05.md`, `verse_schema_and_versification_2026-05.md`, `ot_canon_and_text_base_2026-05.md`, `hebrew_idioms_and_metaphor_2026-05.md`.

---

## 1. Translate each passage from its own MT context

**Lock:** parallel passages are **not** automatically harmonized. Each book's received MT wording controls that book's translation unless the canon/text-base policy (`ot_canon_and_text_base_2026-05.md`) independently justifies emendation for that specific verse.

**Examples:**

- **2 Sam 22 ≈ Ps 18** — 2 Sam 22 follows 2 Samuel's MT form, even where Psalm 18 differs. Psalm 18 (when translated) will follow the Psalter's MT form, even where 2 Sam 22 differs.
- **Samuel ↔ Chronicles** — translated independently. 2 Sam 24:1 ("YHWH incited David") and 1 Chr 21:1 ("Satan incited David") are both translated faithfully from their own MT.
- **2 Kings 18–20 ≈ Isaiah 36–39** — Kings follows Kings' MT; Isaiah follows Isaiah's MT.
- **Jer 52 ≈ 2 Kgs 25** — same principle.
- **Mic 4:1–3 ≈ Isa 2:2–4** — same.

**Rationale:** the received MT of each book is the project's text-base for that book. Harmonizing across books would impose an editorial layer the MT itself does not impose. Variant readings preserved in the canon are theologically meaningful in their own right — they show what each biblical author was inspired to record about the same event or oracle.

**Exception:** when MT of one book contains an obvious copyist error AND the parallel book preserves the original reading AND the canon/text-base policy's Trigger-1 criteria apply (contextual contradiction + strong external witnesses), the MT-anchored emendation per `ot_canon_and_text_base_2026-05.md` overrides. The 2 SA 21:19 / 1 Chr 20:5 case is an example where the project considered but did NOT emend — see §3 below for the disposition logic.

---

## 2. Layer-1 documentation (per-verse `key_decisions` / `notes`)

Per-verse documentation should identify major parallel witnesses when:

- **Wording differs materially** (more than stylistic; affects meaning or emphasis).
- **Names or numbers differ** (e.g., 2 Sam 24:9 census totals vs 1 Chr 21:5; 2 Sam 8:4 vs 1 Chr 18:4 chariot numbers).
- **Agency differs** (e.g., 2 Sam 24:1 YHWH vs 1 Chr 21:1 Satan).
- **A later biblical author cites or reuses the text** (e.g., NT citations of OT, OT inner-biblical citation).
- **The difference affects interpretation** (theological, apologetic, or historical).

**Format:** include the parallel reference + the parallel reading + the project's chosen text. Example:

```json
{
  "hebrew": "וַיֹּסֶף אַף־יְהוָה",
  "rendering": "พระพิโรธขององค์พระผู้เป็นเจ้าเดือดดาลต่ออิสราเอลอีกครั้ง",
  "rationale": "**Samuel↔Chronicles divergence**: 2 ซมอ 24:1 'พระเจ้าทรงยุยง' vs 1 พศด 21:1 'ซาตานยุยง.' ทั้งสองเป็นพระวจนะของพระเจ้า — ไม่ขัดแย้งกันในกรอบเทววิทยา (พระเจ้าทรงครอบครอง + ทรงอนุญาตให้ซาตานทำงานตามแผนของพระองค์ — เปรียบ โยบ 1-2). ฉบับเอเรโมสรักษาการอ่านของ MT 2 ซมอ."
}
```

Layer-1 documentation is for translators, reviewers, scholars, and AI evaluators. It defends the methodology + records the parallel.

---

## 3. Layer-2 reader-facing footers

Reader-facing chapter-footer notes (`output/textual_variants/<book>_<chapter>.json` entries with `type: synoptic_variant_*` or `type: trigger_1_mt_departure_footer`) should be used when:

- **The translation departs from MT** in favor of the parallel reading (Trigger-1; mandated by `ot_canon_and_text_base_2026-05`).
- **The parallel difference is famous, apologetically prominent, or theologically weighty** (e.g., Samuel↔Chronicles 24:1 YHWH vs Satan; 21:19 Elhanan vs Goliath).
- **The difference is likely to confuse readers** familiar with the parallel book (e.g., 2 Sam 24:9 census totals).
- **The parallel gives a substantially different name, number, or agent** for the same event.

**Format examples** (from 2 SA 21 + 24 audit-followup):

- **Trigger-1 MT-departure footer** (mandated): "ต้นฉบับฮีบรู (MT) อ่านว่า X. ฉบับเอเรโมสแปลตามการอ่านของ LXX/Syriac/Vulgate/etc. ว่า Y. เหตุผลของการเปลี่ยน: ..."

- **Synoptic variant disclosure footer** (MT-faithful, but high-profile): "ต้นฉบับฮีบรู (MT) ของ 2 ซมอ N อ่านว่า X. 1 พศด/Ps/Isa อ่านว่า Y. ทั้งสองเป็นพระวจนะของพระเจ้า — ฉบับเอเรโมสรักษาการอ่านของ MT [book] ตามนโยบาย MT-anchored. คำอธิบายของนักวิชาการ: ..."

**Standard phrasing templates:**

1. **Departure from MT** (Trigger-1):
   > "ต้นฉบับฮีบรู (MT) อ่านว่า **[X]**. ฉบับเอเรโมสแปลตามการอ่านของ [LXX/Syriac/Vulgate/Josephus/etc.] ว่า **[Y]**. เหตุผลของการเปลี่ยน: [contextual contradiction explanation]. นโยบาย: docs/translator_decisions/ot_canon_and_text_base_2026-05.md."

2. **Samuel↔Chronicles (MT-faithful)**:
   > "**[Verse summary]** (Samuel↔Chronicles): 2 ซมอ N:M อ่านว่า **[X]**. 1 พศด P:Q อ่านว่า **[Y]**. ทั้งสองเป็นพระวจนะของพระเจ้า — ฉบับเอเรโมสรักษาการอ่านของ MT 2 ซมอ ตามนโยบาย MT-anchored. คำอธิบาย: [scholarly note]."

3. **Psalter parallel (e.g., 2 Sam 22 ≈ Ps 18)**:
   > "**[Verse]** สดด 18 มีรูปแบบที่แตกต่างเล็กน้อย: **[difference]**. ฉบับเอเรโมสแปลตามต้นฉบับ 2 ซมอ ในที่นี้ + จะนำมาใช้กับ สดด 18 เมื่อแปลถึงในอนาคต."

4. **Prophets parallel (e.g., Isa 36–39 ≈ 2 Kgs 18–20)** — same format as Samuel↔Chronicles.

---

## 4. Disposition logic — when to emend vs preserve

When MT of one book diverges from a parallel book and the project must decide whether to preserve MT or follow the parallel:

| Situation | Decision | Anchor |
|---|---|---|
| MT creates contextual contradiction + strong external witnesses (LXX/Syriac/Vulgate/parallel) preserve the original reading | **Emend** to the parallel reading + Trigger-1 Layer-2 footer mandated | 2 SA 15:7 (forty → four) |
| MT is grammatically/contextually coherent + the parallel has a different reading | **Preserve MT** + Layer-2 synoptic-variant footer (if difference is famous or material) | 2 SA 24:13 (seven years vs three); 2 SA 21:19 (Elhanan/Goliath); 2 SA 24:1, 24:9 |
| MT and parallel reflect different but equally valid editorial traditions (independent witnesses) | **Preserve MT** + Layer-1 note (no Layer-2 unless famous) | Many minor Samuel↔Chronicles stylistic differences |
| MT and parallel are stylistic variants of the same content (no meaning difference) | **Preserve MT** + no special note required | Most 2 Sam 22 ≈ Ps 18 minor word-order differences |

**Key principle:** the project does not "fix" MT just because Chronicles or LXX reads differently. Emendation requires both (a) contextual problem in MT AND (b) strong external support. Without both, MT stands and the variant is disclosed.

---

## 5. Application to 2 Samuel (already applied 2026-05-23)

The 2 SA audit-followup (this doc's triggering audit) applied the policy as follows:

| Verse | MT reading | Parallel reading | Disposition | Layer-2 footer |
|---|---|---|---|---|
| **15:7** | "forty years" (אַרְבָּעִים) | LXX/Syriac/Vulgate "four years" (אַרְבַּע) | **Emend** to "four" (contextual contradiction) | **Trigger-1 footer** (mandated) |
| **21:19** | "Elhanan killed Goliath" | 1 Chr 20:5 "Elhanan killed Lahmi brother of Goliath" | **Preserve MT** | **Synoptic-variant footer** |
| **24:1** | "YHWH incited David" | 1 Chr 21:1 "Satan incited David" | **Preserve MT** | **Synoptic-variant footer** |
| **24:9** | Israel 800K + Judah 500K | 1 Chr 21:5 Israel 1.1M + Judah 470K | **Preserve MT** | **Synoptic-variant footer** |
| **24:13** | "seven years famine" | 1 Chr 21:12 + LXX "three years" | **Preserve MT** | **Synoptic-variant footer** |

All 5 footers added in PR `end-of-book-audit-followup-2samuel-2026-05-23`.

---

## 6. Forward application — what's coming

**Psalter (~2026-Q4 / 2027-Q1):**

- **Ps 18 ≈ 2 Sam 22** — translate Ps 18 from its own MT; disclose 2 Sam 22 stylistic variants where material.
- **Ps 14 ≈ Ps 53** — translate each from its own MT (Ps 14 in Book I, Ps 53 in Book II; the Elohistic Psalter changes God→Elohim).
- **Ps 40:13–17 ≈ Ps 70** — same; the duplicate-psalm doublets are independent.
- **Ps 105 ≈ 1 Chr 16:8–22** + **Ps 96 ≈ 1 Chr 16:23–33** + **Ps 106:1, 47–48 ≈ 1 Chr 16:34–36** — translate the Chronicles-embedded version from Chronicles' MT when translating Chronicles; translate the Psalter version from the Psalter's MT when translating Psalms; disclose the cross-reference at Layer 2.

**Kings ↔ Chronicles (~2026-Q4 / 2027-Q2):**

- The bulk of 1–2 Chronicles narrative parallels 1–2 Samuel + 1–2 Kings. Apply the same principle: each book's MT controls that book's translation; document parallel divergences at Layer 1; Layer-2 footer for famous or material differences.

**Major Prophets parallel sets:**

- **Isaiah 36–39 ≈ 2 Kings 18–20** — translate each from its own MT.
- **Jeremiah 52 ≈ 2 Kings 25** — same.
- **Mic 4:1–3 ≈ Isa 2:2–4** — same; the "swords into plowshares" oracle appears in both with minor differences.

**NT-citation cluster** (out of scope for this doc, see plan §12):
- NT-cited OT verses use a `lxx_comparator` sub-object per `verse_schema_and_versification_2026-05.md` to record the LXX form + alignment status. This is orthogonal to the synoptic-parallel policy here (which governs OT↔OT parallels).

---

## 7. Mechanical enforcement (future work)

A future check script `check_synoptic_parallel_coverage.py` could:

- Load a parallel-passage map (e.g., `data/synoptic_parallels_ot.json` — to be created).
- For each verse in the map, verify the verse's Layer-1 documentation references the parallel.
- For high-profile parallels (per a curated list), verify Layer-2 footer exists.

This is **not blocking** for the 2 SA tag — the script can be built later as the corpus scales. The current policy is enforced by the end-of-book audit subagent (which catches missing Layer-2 footers, as it did for 2 SA 15:7 / 21:19 / 24:1 / 24:9 / 24:13).

---

## 8. Change log

- **v0.1** (2026-05-23) — Initial policy, triggered by 2 SA end-of-book audit Item C + ChatGPT/Gemini convergent CONCERN verdict. Locks the independent-MT principle + Layer-1/Layer-2 disclosure rules + standard footer phrasing. Applied retroactively to 2 SA 15:7 / 21:19 / 24:1 / 24:9 / 24:13.
