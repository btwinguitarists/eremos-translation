# The structure layer (`data/structure/`)

A typeset **structure layer** for the Eremos Thai Bible: section headings (English +
Thai), paragraph breaks, poetry indentation, Selah, and the Psalm-119 acrostic letters.
It is what turns the reader from a verse list into something that reads and projects like a
real Bible — and it is **purely additive**: it never touches the verse translations in
`output/`.

## Provenance & license

Structure is derived from the **Berean Standard Bible** section apparatus, which is
dedicated to the **public domain** (`sources/bsb/LICENSE.md`, CC0). This derived layer is
therefore CC0 as well. We deliberately do **not** use any copyrighted heading set (e.g. the
Thai KJV is CC BY-NC-ND — NonCommercial + NoDerivatives — and must never be copied here).

The Thai heading text is **our own editorial translation** of the BSB headings, drafted
against the shipped Eremos verse text (`output/reader/`) with the project's locked divine
names and proper-noun spellings. Headings are editorial — not the inspired text — and ship
as `review_status: draft` (`headings_status: "draft"`) headed for native review, exactly
like a translation queue item.

## How it's built (reproducible)

```
scripts/extract_bsb_structure.py   # sources/bsb/download/bsb_tables.xlsx → data/structure_bsb/<book>.json (English)
                                   #   (needs openpyxl; counts match the BSB parser: 3016 hdg + 42 subhdg + 37 ihdg …)
# → Thai heading drafts land in data/structure_headings_th.json  ({English: Thai})
scripts/build_structure_layer.py   # merge EN structure + Thai + versification → data/structure/<book>.json
```

## Versification (important)

The Eremos reader is **MT-anchored** at the ~23 seams where the Hebrew and English verse
numbering diverge (e.g. Joel has 4 chapters, Malachi 3). The BSB apparatus is English-
numbered. `build_structure_layer.py` resolves every anchor into our numbering:

1. **exact** — the BSB (chapter, verse) already exists in our reader.
2. **inverse `versification_map.json`** — the map is MT-anchored (`mt_ref → bsb_ref`); we
   invert it to send a BSB ref back to our verse. (Resolves 79 anchors.)
3. **hand-verified overrides** (`OVERRIDES` in the script) — the map lacks the Leviticus
   5/6 boundary; `The Sin Offering` (BSB 6:24 "And the LORD said to Moses") is our **6:17**,
   confirmed by verse content.
4. **drop** — 8 paragraph/poetry-only marks at NT/Nehemiah chapter seams that land on a
   verse our numbering merges; dropping is invisible (the verse just continues its
   paragraph). Logged by the script, never silent. **Headings are never dropped.**

## Schema — `data/structure/<slug>.json`

```jsonc
{
  "book": "genesis",
  "en": "Genesis",
  "th": "ปฐมกาล",                    // Thai book title (from the reader H1)
  "source": "Berean Standard Bible section apparatus (CC0)",
  "headings_status": "draft",
  "versification": "eremos-reader (MT-anchored at divergent seams)",
  "structure": [                      // ordered; each entry anchors to a verse in OUR numbering
    {
      "c": 1, "v": 1,                 // chapter, verse this structure begins AT
      "heading": [                    // 0+ headings that PRECEDE this verse
        { "level": 2, "en": "The Creation", "th": "การทรงสร้าง" }
      ],
      "start": "p"                    // block that opens at this verse (see below)
    },
    { "c": 1, "v": 3, "heading": [{ "level": 3, "en": "The First Day", "th": "วันที่หนึ่ง" }], "start": "q1" }
  ]
}
```

Fields on a `structure` entry (all optional except `c`, `v`):

| Field | Meaning |
|---|---|
| `heading` | List of headings preceding this verse. `level` 2 = section, 3 = subsection. `en`/`th`. `italic:true` = speaker label (Song of Songs). `psalm:true` = psalm/book-range label. |
| `start` | The block that **opens** at this verse: `p` prose paragraph · `q1`/`q2` poetry indent level 1/2 · `li1`/`li2` list · `inscription`. A verse with no `start` continues the current block. A heading always forces a new block regardless. |
| `book_divider` | Psalms only: the five-book divider (`"I"`…`"V"`) — render as "BOOK I". |
| `acrostic` | Poetry acrostic markers (Psalm 119): `[{ "letter": "א", "name": "Aleph" }]`. |
| `selah` | `true` — a Selah falls in/after this verse; render right-aligned, muted. |

## Consumers

- **Site** (`bible.eremosapp.com`): reading view renders headings + paragraphs + poetry
  indentation + Selah; study view stays verse-by-verse.
- **Eremos app**: can read the same layer. Note the app bundle may be BSB-numbered while
  this layer is keyed to the reader (MT) — if so, consume `data/structure_bsb/` (BSB-native)
  instead, or re-run the resolver against the app's verse set.
- **Print**: headings + paragraph/poetry structure are the foundation of a typeset edition.

## Regenerating after a content change

Verse text changes don't require regenerating structure. If the reader's **versification**
changes, or headings are edited, re-run `build_structure_layer.py`. If BSB updates its
apparatus, re-run `extract_bsb_structure.py` first.
