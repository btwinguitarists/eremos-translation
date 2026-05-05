# Shared OT/NT proper-name normalization — Hebrew form wins

**Status:** LOCKED 2026-05-05.
**Triggered by:** Ruth 4:19 רָם / Matthew 1:3 Ἀράμ cross-corpus tension surfaced at the Ruth end-of-book audit (`docs/end_of_book/ruth/RUT_END_OF_BOOK_REVIEW_2026-05-05.md` Item C; AI review response `ai_review_response_RUT_2026-05-05.md`).
**Decided by:** Ben (2026-05-05), choosing path (c) per the audit's three options.

## The rule

For **proper names of OT figures who appear in BOTH testaments** (genealogies, the patriarchs, the kings of Judah/Israel, the major prophets cited in NT, etc.), the **Thai transliteration follows the Hebrew source form**, not the Greek source form. This holds even when the NT text uses a Hellenized spelling (prosthetic α, final μ for Hebrew final נ/ם, etc.).

## Why

Three reasons:

1. **OT-precedence** — when a person first enters the canonical narrative in an OT book (Abraham in Genesis, David in 1 Samuel, etc.), the OT establishes the Thai-name convention. The NT (writing in Greek about Hebrew figures) is a downstream witness, not the source. Honoring the Hebrew source for shared names matches the project's broader source-fidelity stance.

2. **Reader continuity** — a Thai reader cross-referencing Ruth 4:19 → Matthew 1:3 should see the same person under one name. The transparency mechanism (verse-level `key_decisions` documenting the Greek source-form) preserves scholarly traceability without splitting the surface text.

3. **Forward consistency** — Phase 6D-onward will ship OT books densely populated with figures who reappear in NT (Solomon, Elijah, Jeremiah, Daniel, Jonah, Moses, Joshua, Samuel, etc.). Without an explicit lock, every shipment risks a fresh ad-hoc decision; the lock here ensures uniformity.

## Application

### Hebrew form wins. Backfill the NT when divergence surfaces.

When the NT renders a shared figure with a Hellenized spelling that differs from the Hebrew form, **edit the NT verse to match the Hebrew form** (which the OT will or has already used). Document the source-language form in the verse's `key_decisions` so the Greek text remains scholarly-traceable.

### Per-verse `key_decisions` documents the underlying source

Every backfilled verse carries a `key_decisions` entry:

```json
{
  "greek": "Ἀράμ",
  "thai": "ราม",
  "rationale": "Matthew's Greek Ἀράμ = Heb. רָם (Ram per 1 Chr 2:9-10, Ruth 4:19). Greek prefixes a prosthetic α; English ESV/NIV/CSB/NLT all render 'Ram' per the Hebrew. Locked corpus-wide as ราม per shared_names_normalization_2026-05.md..."
}
```

This is the same Layer-1 transparency mechanism used by the Tetragrammaton lock (`divine_names_table_2026-05.md` §"Layer 1 — Per-verse `key_decisions` entry").

### Where the Hebrew form is unclear, choose the most-attested OT spelling

When a name appears in multiple OT books with slightly different Hebrew vocalizations (e.g., Hezron / Chetzron) the Thai form follows the dominant OT-genealogy form. Document the choice once in this doc; future occurrences inherit.

## Locked names (initial set, 2026-05-05)

The Davidic-line genealogy locks these at first occurrence:

| Person | Hebrew | Greek | Locked Thai | OT precedent | NT verses backfilled |
|---|---|---|---|---|---|
| Ram | רָם | Ἀράμ | **ราม** | Ruth 4:19 | Mt 1:3, Mt 1:4 |

**All other Davidic-line names** (Perez, Hezron, Amminadab, Nahshon, Salmon, Boaz, Obed, Jesse, David, Solomon, Rehoboam, the kings of Judah down to Jeconiah) **were already aligned** between Mt 1 / Lk 3 / Ruth 4 / 1 Chr 2 — no backfill needed. The audit verified this explicitly:

| Person | Hebrew form | Greek form | Thai (both) | Status |
|---|---|---|---|---|
| Perez | פֶּרֶץ | Φάρες | เปเรศ | aligned |
| Hezron | חֶצְרוֹן | Ἑσρώμ | เฮสโรน | aligned (Hebrew nun-final form already used in Mt; Greek mu-ending dropped) |
| Amminadab | עַמִּינָדָב | Ἀμιναδάβ | อัมมีนาดับ | aligned |
| Nahshon | נַחְשׁוֹן | Ναασσών | นาโชน | aligned |
| Salmon | שַׂלְמוֹן | Σαλμών | สัลโมน | aligned |
| Boaz | בֹּעַז | Βόες | โบอาส | aligned |
| Obed | עוֹבֵד | Ἰωβήδ | โอเบด | aligned (Greek prosthetic iota dropped) |
| Jesse | יִשַׁי | Ἰεσσαί | เจสซี | aligned |
| David | דָּוִד | Δαυίδ | ดาวิด | universal |

Patriarchal names (Abraham, Isaac, Jacob, Joseph, Judah, etc.) and pre-monarchy figures (Noah, Enoch, Methuselah, etc.) likewise verified aligned during the audit (Mt 1:1-2, Lk 3:34, Acts 7:2-50, Heb 11:4-33).

The Davidic-line **kings of Judah after Solomon** (Rehoboam → Jeconiah, Mt 1:7-12) all rendered consistently with their OT forms in the shipped NT. No backfill needed.

## What this rule does NOT cover

- **Proper names that exist only in one testament** (NT-only — Caiaphas, Pilate, Felix, Festus; OT-only — Methuselah, Goliath, Nebuchadnezzar, Sennacherib). These are governed by `proper_names_and_transliteration_2026-05.md` (which uses THSV11 baseline + per-name decisions). No cross-testament alignment needed because there's nothing to align against.
- **Place names** (Bethlehem, Jerusalem, Jericho, Samaria). Covered by the place-name rules in `proper_names_and_transliteration_2026-05.md`. Mostly already aligned across testaments because the place-names are stable.
- **Divine names** (YHWH, El Shaddai, Adonai). Covered by `divine_names_table_2026-05.md` — separate lock, separate transparency mechanism.
- **Textual-variant cases** (e.g., Lk 3:33 has Ἀδμίν / Ἀρνί where some manuscripts have Ἀράμ — this is a manuscript-tradition divergence, not a Hebrew/Greek transliteration drift). Honored per the SBLGNT critical-text + RULES §0.

## When to revisit

- **Phase 6D start (Former Prophets — Joshua → Kings)** — re-read this doc; the dominant kings (David, Solomon, Hezekiah, Josiah, Jehoshaphat, etc.) all reappear in Mt 1 and Acts/Heb. Any new divergence surfaced during 1 Sam-2 Kgs translation is added to the locked-names table above.
- **Phase 6F (Wisdom)** — Job 19:25 ("my Redeemer lives") + Ps 51 (David) + Ps 110 (David) trigger cross-corpus alignment with Heb 1:13, Mark 12:36, etc.
- **Phase 6G (Major Prophets)** — Isaiah / Jeremiah / Ezekiel are densely NT-cited. Verify the prophets' name-forms are aligned (Isaiah → อิสยาห์ in OT; Mt 3:3 / Lk 4:17 / Acts 8:30 use Ἠσαΐας → already อิสยาห์ via Hebrew form precedent — confirm during audit).
- **End-of-book audits forward** — every OT-book audit should include a "shared OT/NT name divergence" sweep as a small audit item.

## Reversibility

The rule is reversible. If a future Thai-reader survey indicates that the Greek-form Hellenized spellings (อารัม, ฟาเรส for Perez, etc.) read more naturally to evangelical-Thai-tradition readers, this lock can be flipped via a project-wide find-replace migration similar to the Tetragrammaton-reversibility clause in `divine_names_table_2026-05.md`. Each backfilled verse's `key_decisions` carries the underlying Greek source-form so the migration is mechanically possible.

The lock as decided 2026-05-05 prioritizes **OT-source-fidelity + cross-testament reader continuity** over surface-Hellenization-traceability. Per the audit's external AI review: ChatGPT preferred the cross-testament reader-continuity argument; Gemini preferred the policy-doc-with-divergence-preservation argument. Ben (2026-05-05) chose to combine: the Hebrew form wins (continuity), and this doc + per-verse `key_decisions` carry the transparency layer.
