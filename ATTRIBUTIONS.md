# Attributions

The Eremos Translation's output (Thai text + rationale) is released under CC0.
But the project depends on external source materials, each with its own
license. This document enumerates them and fulfills our attribution
obligations.

---

## Sources used during translation

### SBLGNT — Society of Biblical Literature Greek New Testament

- **Used for:** The Greek New Testament source text
- **Editor:** Michael W. Holmes
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Attribution required:** Yes
- **Source:** https://github.com/LogosBible/SBLGNT
- **Citation:** Michael W. Holmes, ed., *The SBL Greek New Testament* (Atlanta: Society of Biblical Literature; Logos Bible Software, 2010).

### MACULA Greek Linguistic Dataset

- **Used for:** Word-by-word morphological analysis, syntax trees, English glosses, Louw-Nida semantic domains
- **Publisher:** Clear Bible, Inc.
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Attribution required:** Yes
- **Source:** https://github.com/Clear-Bible/macula-greek
- **Citation:** MACULA Greek Linguistic Datasets (Clear Bible, Inc., 2023).

### Berean Standard Bible (BSB)

- **Used for:** English reference translation (sanity check during drafting; not a source to copy from)
- **Publisher:** BSB Publishing
- **License:** CC0 1.0 (Public Domain Dedication)
- **Attribution required:** No (CC0), but acknowledged here as good practice
- **Source:** https://berean.bible

### unfoldingWord Translation Notes (uW TN)

- **Used for:** Scholarly reference during translation — interpretive cruxes, textual issues (at `output/uw_notes/*.md`, consulted but never copied)
- **Publisher:** unfoldingWord
- **License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- **Attribution required:** Yes
- **Reference-only use:** We consult uW TN during drafting for context but do not copy its wording. The Eremos Translation's own rationale and notes are independently composed, so our output is not a derivative work of uW TN and therefore does not inherit CC-BY-SA.
- **Source:** https://git.door43.org/unfoldingWord/en_tn

### Thai New Buddhist Translation (TNBT)

- **Used for:** Structural comparison only (post-draft check via `check_against_tnbt.py`); never read during drafting
- **Author:** Banpote Wetchgama
- **License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- **Attribution required:** Yes
- **Reference-only use:** We compare verse-level structural signals (sentence count, length ratio) against TNBT. We do not copy TNBT wording. The Eremos Translation is not a derivative work of TNBT.
- **Source:** https://github.com/pepa65/TNBT

---

## Scholarly sources consulted (general references, not copied)

- **NA28 / UBS5** — textual apparatus for manuscript variants (consulted via published editions; no text copied)
- **Louw & Nida, *Greek-English Lexicon of the New Testament: Based on Semantic Domains*** — referenced via MACULA's Louw-Nida annotations
- **BDAG (*A Greek-English Lexicon of the New Testament and Other Early Christian Literature*, 3rd ed.)** — consulted by translators for rare words; no text copied
- **HALOT (*The Hebrew and Aramaic Lexicon of the Old Testament*)** — planned for OT phase
- Critical commentaries (Nicoll, NICNT, WBC, Anchor, Expositor's, etc.) — consulted by translators for context; no text copied

---

## Our output

- **Name:** Eremos Translation (working name)
- **License:** CC0 1.0 Universal (see LICENSE)
- **Scope of CC0:** Thai translation text, rationale, notes, scripts, glossary
- **Not covered by our CC0:** Any of the above source materials — they retain their original licenses

---

## Attribution format for redistribution

If you redistribute the Eremos Translation (e.g., as part of a Bible app),
you are NOT required to include attribution for our work (it's CC0). But
if you redistribute processing dependencies or derivative tooling, please
maintain the attributions above for the source materials we depend on.

A minimal attribution line appropriate for packaged distributions of our
Thai text (e.g., in a Bible app's "about" dialog) would be:

> "Eremos Translation — public domain (CC0). Built using SBLGNT (CC BY 4.0),
> MACULA Greek (CC BY 4.0), Berean Standard Bible (CC0). Scholarly reference:
> unfoldingWord Translation Notes (CC-BY-SA 4.0). Structural reference: Thai
> New Buddhist Translation (CC-BY-SA 4.0)."
