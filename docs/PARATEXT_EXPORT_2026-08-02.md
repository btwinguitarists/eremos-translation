# Paratext / USFM export — full-Bible edition (2026-08-02)

`scripts/export_to_usfm.py` now covers all 66 books (previously the 27 NT books).
OT Thai names mirror `data/structure/<slug>.json` (`th` — the same names the app
uses); abbreviations follow the standard Thai Bible abbreviation set. Running
`--all` also emits `output/paratext/booknames.xml` (Paratext
`<book code abbr short long/>` format, 66 entries).

Validated at export time:

- 66 `.SFM` files, every file starts with `\id`, UTF-8 clean
- 1,189 chapters (PSA = 150 `\c`)
- 31,155 `\v` markers, 0 empty verses
- `booknames.xml` parses, 66 entries

`output/paratext/` is load-bearing: the eBible.org and Paratext/Scripture Forge
submissions link this folder directly, and the site's `/data` page lists it.

## Verse-count reconciliation: 31,155 (USFM/JSON) vs 31,086 (site/reader)

Both numbers count the **same text** under two numbering conventions:

- **31,155** — `output/translations/*.json` and the USFM export follow
  source numbering (MT for the OT, SBLGNT for the NT).
- **31,086** — `output/reader/*.md` and bible.eremosapp.com follow
  English-style numbering (psalm superscriptions rendered as unnumbered
  title lines; classic MT/Greek↔English verse splits and merges applied).

The 69-verse delta is fully attributed:

| Source | Count | Detail |
|---|---|---|
| Psalm superscriptions | +66 | MT counts the superscription as verse 1 — 58 psalms with a one-verse title, 4 with a two-verse title (Ps 51, 52, 54, 60); the reader renders them unnumbered |
| 1 Chr 12:41 (MT) | +1 | English 12:4 covers MT 12:4–5 |
| 1 Kgs 22:54 (MT) | +1 | English 22:43 covers MT 22:43–44 |
| 1 Sam 21:16 (MT) | +1 | MT ch. 21 numbers one ahead of English (Eng 21:1 = MT 21:2) |
| 3 John 15 (SBLGNT) | +1 | English convention merges into v. 14 |
| Num 25:19 (MT) | +1 | English folds into 26:1 |
| Rev 12:18 (SBLGNT) | +1 | English convention carries it as 13:1a |
| 2 Cor 13 | −1 | English 13:12–13 split what SBLGNT counts as one verse (Eng ch. has 14) |
| Acts 19:41 | −1 | English splits SBLGNT 19:40 |
| Isa 64:1 | −1 | English 64 has 12 verses; MT 63:19 covers Eng 63:19 + 64:1 |
| **Net** | **+69** | |

Chapter-boundary shifts (1 Chr 5/6, 1 Kgs 4/5, Num 16/17, Num 29/30,
1 Sam 23/24, Isa 8/9) move verses between chapters but are net-zero per book.

**Content equality verified 2026-08-02:** for every book named above, the
whitespace-normalized concatenation of all verse text in the JSON equals the
concatenation in the reader edition, character for character. The delta is
numbering convention only; no verse text differs between the two surfaces.

## Residual polish (non-blocking)

Some seam verses carry full `versification` sub-objects (1 Kgs 5, Isa 8,
Rev 12:18, 3 John 15) while others predate that metadata and have `null`
fields (1 Chr 5:27–41, Num 17, 1 Sam 21/24). Neither export reads those
fields, but backfilling them would make the mapping machine-checkable
end-to-end. Per `reference_versification_map`: hand-patch only — never
full-regen the versification map.
