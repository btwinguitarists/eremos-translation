# Spirit-of-YHWH empowerment — 4-way principled split by Hebrew verb

**Scope:** Every occurrence of רוּחַ יהוה / רוּחַ אֱלֹהִים where the Spirit is described as coming upon, clothing, stirring, or rushing on a human agent. Covers Judges (the densest concentration: 7 occurrences across 4 distinct Hebrew verb forms), Samuel, Kings, Chronicles, and any prophetic-empowerment passage in Isaiah / Ezekiel / Joel.

**Decided:** 2026-05-20 (Ben, post-Judges-end-of-book audit). Locked **before** 1 Samuel ships further (Saul + David Spirit-rush narratives) and **before** any Chronicler retrospective on judge-era empowerment.

**Trigger:** Judges end-of-book audit Item A + 2-way external AI review (ChatGPT + Gemini, convergent FINE-with-doc-lock verdict). The shipped JDG corpus already preserves a principled 4-way split tracking real Hebrew verb-class distinctions; this doc captures the lock so the pattern is forward-protected against well-intentioned flattening pressure (`มาเหนือ` is the easy default; without this lock a future translator would silently collapse `לָבְשָׁה` and `צָלַח` into it).

---

## The 4-way lock

| Hebrew verbal pattern | Sense | Locked Thai surface | Anchor verses |
|---|---|---|---|
| **הָיָה עַל** + רוּחַ יהוה ("the Spirit-of-YHWH was upon X") | Basic empowerment formula — Spirit settles on a person | **พระวิญญาณขององค์พระผู้เป็นเจ้า…มาเหนือ** | JDG 3:10 (Othniel), JDG 11:29 (Jephthah) |
| **לָבַשׁ** + רוּחַ יהוה ("the Spirit-of-YHWH clothed X") | Spirit *envelops* the person — uses the same verb as putting on a garment | **พระวิญญาณขององค์พระผู้เป็นเจ้า…ทรงสวมทับ** | JDG 6:34 (Gideon at trumpet-blowing); cf. 1 Chr 12:18, 2 Chr 24:20 (forward-protect) |
| **פָּעַם** + רוּחַ יהוה ("the Spirit-of-YHWH began to stir / impel X") | Inception verb — Spirit *begins to move* the person, often the first occurrence in a narrative arc | **พระวิญญาณขององค์พระผู้เป็นเจ้า…เริ่มกระตุ้น** | JDG 13:25 (Samson's first stirring); cf. PSA 77:4 (rare cognate use) |
| **צָלַח עַל** + רוּחַ יהוה ("the Spirit-of-YHWH rushed upon X with power") | Sudden, forceful descent — distinctive of the Samson cycle and reappears in 1 Sam | **พระวิญญาณขององค์พระผู้เป็นเจ้า…มาเหนือ…อย่างทรงพลัง** | JDG 14:6, 14:19, 15:14 (Samson); forward-protect 1 SAM 10:6, 10:10, 11:6, 16:13 (Saul + David) |

**Single-Thai-default rejected:** flattening everything to `มาเหนือ` would erase three meaningful Hebrew verb-class distinctions — the *enveloping* nuance of לָבַשׁ, the *inceptive* nuance of פָּעַם, and the *forceful* nuance of צָלַח. The Hebrew authors of Judges chose four distinct verbs across seven Spirit-empowerment occurrences in a 13-chapter span; that is intentional pneumatological texture, not stylistic variation, and must be preserved in the optimal-equivalence target.

---

## Why this split is sustainable

1. **Verb-by-verb principled, not surface-by-surface ad-hoc.** Each Thai surface tracks a specific Hebrew root, so the lock can be mechanically enforced by `check_key_term_consistency.py` on the Hebrew side (lemma) rather than requiring per-verse Thai lookup. Forward protection scales.
2. **Reader experience.** Thai readers comparing Gideon (`ทรงสวมทับ` — Spirit wraps him before the trumpet call) with Samson (`มาเหนือ…อย่างทรงพลัง` — Spirit rushes on him before tearing the lion) will feel the same register difference the Hebrew author created. The narrative gradient is preserved.
3. **OT/NT continuity preserved separately.** This lock concerns OT Hebrew empowerment formulas. The Pentecost/Acts pneumatology (ἐπληρώθησαν πνεύματος ἁγίου, "they were filled with the Holy Spirit") is a distinct semantic field and is not collapsed into this OT lock — see `spiritual_beings_hierarchy_2026-05.md` + the NT-side empowerment treatment.
4. **Forward-protection through 1–2 Samuel.** The two highest-stakes upcoming uses are:
    - **1 Sam 10:6, 10:10** — Saul's anointing and first Spirit-rush (צָלַח) → must render as **มาเหนือ…อย่างทรงพลัง**, matching Samson, to make the typological inversion (Saul ends as Samson does) audible.
    - **1 Sam 16:13** — David's anointing-Spirit-rush (צָלַח) → same lock.
    - **1 Sam 16:14** — Spirit *departs* from Saul (תָּסוּר) — separate idiom, separate Thai surface (likely **จากไป** / **ละทิ้ง**), not in scope of this doc.

---

## Edge cases + forward-watch

- **רוּחַ אֱלֹהִים (Elohim, not YHWH-form)** — see e.g. NUM 24:2 (Balaam). Same 4-way verb-split applies on the verb side; the divine-name side uses `พระวิญญาณของพระเจ้า` per `divine_names_table_2026-05.md` (אֱלֹהִים → พระเจ้า) rather than `พระวิญญาณขององค์พระผู้เป็นเจ้า`.
- **רוּחַ רָעָה מֵאֵת יְהוָה** (evil/troubling spirit from YHWH; 1 Sam 16:14ff.) — separate lock; do not subsume into this empowerment doc.
- **רוּחַ נְבוּאָה / רוּחַ הַחָכְמָה** (spirit of prophecy / spirit of wisdom — descriptive genitives, not the YHWH-empowerment-formula) — separate treatment; this doc does not govern.

---

## Corpus-verified shipped forms

As of 2026-05-20, the locked surfaces above match the shipped Judges corpus:

```
$ python3 -c "import json,glob; ..."
JDG 3:10  (הָיָה עַל)  → 'พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขา'
JDG 6:34  (לָבְשָׁה)    → 'พระวิญญาณขององค์พระผู้เป็นเจ้าก็ทรงสวมทับกิดเอน'
JDG 11:29 (הָיָה עַל)  → 'พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเยฟทาห์'
JDG 13:25 (לְפַעֲמוֹ)  → 'พระวิญญาณขององค์พระผู้เป็นเจ้าก็เริ่มกระตุ้นเขา'
JDG 14:6  (תִּצְלַח)   → 'พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง'
JDG 14:19 (תִּצְלַח)   → 'พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง'
JDG 15:14 (תִּצְלַח)   → 'พระวิญญาณขององค์พระผู้เป็นเจ้าก็มาเหนือเขาอย่างทรงพลัง'
```

All seven shipped surfaces conform to the lock. No retroactive verse-edits required from this audit pass.

---

## External AI verdicts (Judges audit Item A, 2026-05-20)

- **ChatGPT:** FINE — "the 4-way split is defensible because the Thai surfaces track real Hebrew verbal distinctions rather than creating stylistic variation… do not flatten everything to มาเหนือ. That would erase meaningful Hebrew verb-class differences."
- **Gemini:** FINE — "collapsing these distinct verbs into a single 'มาเหนือ' template would erase the rich pneumatological variety the MT explicitly authors… honoring the project's optimal equivalence philosophy."
- **Recommended action (both):** lock-as-is + write this corpus doc to protect the *lābash*-Spirit connection before 1 Chr 12:18 and 2 Chr 24:20 ship.

---

## Cross-references

- [[divine_names_table_2026-05]] — for the YHWH → องค์พระผู้เป็นเจ้า + אֱלֹהִים → พระเจ้า base.
- [[spiritual_beings_hierarchy_2026-05]] — for the broader pneumatology lock and the Spirit-of-God / Spirit-of-YHWH / Holy-Spirit relationship.
- [[malak_yhwh_2026-05]] — for the parallel question of how the Angel-of-YHWH ↔ YHWH ambiguity is preserved in Thai (same optimal-equivalence philosophy applied to a different divine-presence locus).
