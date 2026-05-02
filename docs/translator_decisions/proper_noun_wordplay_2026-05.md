# Proper-noun wordplay surfacing — when to add a Thai-language translator footer note

**Status:** LOCKED 2026-05-02 (after Philemon end-of-book audit external AI review)
**Trigger:** PHM 1:10-11, 1:20 (Onesimus name-wordplay)
**External review:** Gemini + ChatGPT both verdict CONCERN; both recommended a brief v.10 footer note
**See:** `docs/end_of_book/philemon/external_review_items_PHM.md` Item B; `docs/end_of_book/philemon/PHM_END_OF_BOOK_REVIEW_2026-05-02.md` §4

## The policy

Greek-name etymology stays in `thai_summary` BY DEFAULT. Add a chapter-footer translator note (`output/translator_notes/<slug>_<NN>.json` → renders as `### หมายเหตุของผู้แปล` in `output/reader/<slug>.md`) ONLY when **all three** conditions hold:

1. **Active argument:** the name's meaning is exploited in the immediate rhetorical argument — not just a static etymology decoration.
2. **Multi-verse density:** the wordplay recurs across multiple verses in the same passage (typically 2-3 verses).
3. **Reader-comprehension dependency:** without the etymology surfaced visibly, a Thai reader experiences the rhetorical hinge as disconnected from the name introduction.

When any one of these conditions fails, keep the etymology in `thai_summary` and `key_decisions[].rationale` only — do NOT add a translator-note footer.

## What this is NOT

- NOT for static name-meaning etymologies (Πέτρος "rock", Ἰησοῦς "YHWH saves", Βαρναβᾶς "son of encouragement"). These stay in `thai_summary` even when the meaning has theological weight (e.g., Matt 16:18 "on this rock"). The argument there is theological, not paronomastic.
- NOT for cultural-context notes about names (e.g., Roman-citizen vs Hebrew-name distinctions, slave-name conventions). Those stay in `notes` (English scholarly).
- NOT for textual-variant disposition (that's `output/textual_variants/` Tier 2).

## Cases that meet all three conditions

| Book | Verses | Greek | Trigger | Status |
|---|---|---|---|---|
| Philemon | 1:10-11, 1:20 | Ὀνήσιμος → ἄχρηστος/εὔχρηστος → ὀναίμην | "useful" pun is the rhetorical engine of the appeal | **IMPLEMENTED 2026-05-02** |
| 2 Timothy | 1:16-18 | Ὀνησίφορος (cognate ὀνίνημι; "useful-bringer") | Possible — same root, but check whether 2 Tim 1:16-18 has active wordplay (vs static name-mention). If only a static name-mention, the policy says NO footer note. | **DEFERRED — assess at 2 Tim end-of-book audit** |

## Schema

`output/translator_notes/<slug>_<NN>.json` — list of dicts:

```json
[
  {
    "verse": 10,
    "type": "name_etymology_active_wordplay",
    "thai_note": "ชื่อ X ในภาษากรีก ... — เปาโลเล่นสำนวนกับชื่อนี้ในข้อ Y และ Z ...",
    "rationale_en": "audit-trail explanation; not rendered to readers"
  }
]
```

Renderer: `scripts/render_reader.py` loads these alongside `output/textual_variants/` and emits a `### หมายเหตุของผู้แปล` chapter-footer section in all three render modes (reader / plain / feedback).

Bundle / Eremos app: NOT in the bundle currently (the bundle is keyed off `output/translations/<slug>_<NN>.json`'s verse-level fields). The Onesimus etymology IS reinforced in v.10's `notes` field so app users with "Show scholarly notes" toggled on still see it. If Ben later wants the translator-note footer to surface in the app's per-verse popup as a distinct apparatus, that's a separate EremosVercel2 + bundle-builder change.

## Why both AIs converged on this policy

> **Gemini:** "Proper-noun etymologies remain in thai_summary, EXCEPT when the immediate grammatical or logical argument directly depends on the wordplay for reader comprehension, warranting a Tier 2 footnote."
>
> **ChatGPT:** "Footnote proper-name etymology only when the name's meaning is actively exploited in the immediate argument across multiple verses. Do not automatically extend this to Peter/Jesus/Barnabas-type etymologies."

The two AIs converged on the same boundary condition: **active argument-bearing wordplay**, not mere etymology. This policy codifies that exact boundary.

## Implementation receipt

- `scripts/render_reader.py` — added `load_translator_notes()` + chapter-footer section
- `output/translator_notes/philemon_01.json` — first entry (Onesimus v.10)
- `output/translations/philemon_01.json` v.10 `notes` — Thai etymology sentence appended (for Eremos app's scholarly-notes toggle)
- `output/reader/philemon.md` — regenerated with the new footer section
