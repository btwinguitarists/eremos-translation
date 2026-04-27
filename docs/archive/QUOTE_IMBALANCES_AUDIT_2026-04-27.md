# Quote-mark imbalances — audit recorded 2026-04-27

**Status**: pre-existing bug surface — these chapters have unbalanced quotation
marks in the `translation.thai` field. Documented here for the follow-up PR
that will hand-fix each one.

**Context**: discovered while doing the corpus-wide guillemet → curly conversion
(PR #51). The conversion was purely mechanical and preserved the imbalance
count — these are not new bugs, they existed in the original guillemet form
too.

**Why these matter**: a reader of `output/plain/<slug>.md` (or the Eremos app
verse popup) currently sees speech that opens but never closes, or closes
without opening. This is the "detrimental" scenario the maintainer flagged.

**How to fix each**: read the chapter's BSB English alongside the Thai, locate
where the quote should open or close per BSB structure, and add the missing
punctuation in the corresponding Thai verse. For each fix, update HASHES.md
and re-render with `scripts/render_reader.py --book <BOOK>`.

---

## Chapters with imbalances after PR #51 (curly chars)

30 chapters. The diff column shows missing/extra count: `+N` means N more
opens than closes (unclosed opens at chapter end); `-N` means N more closes
than opens (stray closes earlier in chapter).

| Chapter | `“`/`”` diff | `‘`/`’` diff | Likely fix |
|---|---:|---:|---|
| acts_01 | -1 | 0 | Stray `”` somewhere v22–v25 region — the apostle-replacement speeches |
| acts_08 | 0 | -1 | Stray `’` at v33 — Isaiah quote close |
| acts_10 | +1 | 0 | Unclosed `“` at v4 — angel's speech to Cornelius continues silently to v6 |
| acts_13 | +2 | 0 | Two unclosed `“` — Paul's synagogue speech (v16–v41) and Paul/Barnabas's response (v46–v47) |
| acts_20 | +1 | 0 | Unclosed `“` at v18 — Paul's Miletus farewell speech |
| acts_28 | -1 | -1 | Stray `”` and `’` v27–v28 — Isaiah quote nested in Paul's final speech |
| luke_03 | 0 | -1 | Stray `’` at v6 — Isaiah quote close (v4 prematurely closed) |
| luke_04 | 0 | +1 | Unclosed `‘` at v23 — synagogue scene |
| luke_08 | -1 | 0 | Stray `”` at v18 |
| luke_09 | -1 | 0 | Stray `”` at v5/v27/v40 region |
| luke_10 | +1 | 0 | Unclosed `“` at v41 — Mary/Martha scene |
| luke_18 | +1 | 0 | Unclosed `“` at v42 — blind man healing |
| luke_20 | +1 | 0 | Unclosed `“` at v46 — Pharisee warning |
| luke_21 | +3 | 0 | Three unclosed `“` at v34+ — Olivet discourse |
| luke_22 | +2 | 0 | Two unclosed `“` at v71 — Sanhedrin trial |
| luke_24 | +1 | 0 | Unclosed `“` at v46 — post-resurrection teaching |
| mark_04 | +1 | 0 | Unclosed (Mark detected `'` as outer for this chapter) |
| mark_07 | +1 | 0 | Unclosed (Mark `'` outer chapter) |
| mark_08 | 0 | +1 | Unclosed (Mark `"` outer chapter from here forward) |
| mark_11 | 0 | +1 | Unclosed |
| mark_13 | 0 | +1 | Unclosed |
| mark_16 | 0 | +1 | Unclosed |
| matthew_02 | +1 | 0 | Unclosed `“` at v23 |
| matthew_03 | +1 | 0 | Unclosed `“` at v17 — voice from heaven |
| matthew_12 | -1 | +1 | Stray `”` at v50, unclosed `‘` at v49 (Isaiah quote) |
| matthew_13 | +1 | 0 | Unclosed `“` at v57 — parables of the kingdom |
| matthew_17 | +1 | 0 | Unclosed `“` at v26 — temple-tax dialog |
| matthew_21 | -1 | 0 | Stray `”` at v40/v44 — Pharisee dialog |
| matthew_24 | +1 | 0 | Unclosed `“` at v4 — Olivet discourse |
| matthew_25 | -1 | 0 | Stray `”` at v46 — eternal-life pronouncement |

## How to work this list

1. Pick a chapter. Open both `output/translations/<slug>_<NN>.json` and the
   verses' BSB English (already in the JSON `bsb_english` field).
2. Walk verses with quote chars, tracking running balance of `“` minus `”`
   (and `‘` minus `’` for nested).
3. The verse where balance first goes wrong tells you where the missing
   punctuation belongs:
   - Balance goes negative → stray close. Either remove the stray, or find
     the verse earlier where speech should open and add `“` (cross-check
     with BSB).
   - Balance is +N at chapter end → N opens never closed. Find the verse
     where speech should end (per BSB), add `”` there.
4. After each chapter fix, re-run the diagnostic to confirm balance is 0.
5. After all 30 chapters, regenerate: `python3 scripts/render_reader.py`
   and `python3 scripts/update_hashes.py`. Rebuild the bundle:
   `python3 scripts/build_eremos_bundle.py`.

## Source diagnostic

The original diagnostic that surfaced these (run on the pre-conversion guillemet
text): `/tmp/imbalance_context.txt` from the PR #51 working session — this
listed each problem verse with surrounding BSB+Thai context. To regenerate
under the new curly characters, swap the chars in the diagnostic script
accordingly.

## Related PRs

- **PR #51** (this fix): mechanical curly-quote conversion. Preserved
  imbalances as-is.
- **PR #52** (planned): hand-fix each of these 30 chapters using the BSB
  cross-check approach above.
