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

### Open Scriptures Hebrew Bible (OSHB / morphhb)

- **Used for:** Hebrew Old Testament source text (Westminster Leningrad Codex base) + Westminster Hebrew Morphology layer
- **Publisher:** Open Scriptures
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0); the underlying Westminster Leningrad Codex text is itself in the public domain
- **Attribution required:** Yes — "Original work of the Open Scriptures Hebrew Bible available at https://github.com/openscriptures/morphhb"
- **Source:** https://github.com/openscriptures/morphhb (clone @ commit `3d15126fb1ef`, acquired 2026-05-04)
- **Role per `docs/source_license_policy.md`:** WLC base text = `primary_text`; WHM morphology layer = `morphology_data`

### MACULA Hebrew Linguistic Datasets

- **Used for:** Word-by-word Hebrew morphology, clausal syntax trees, lexical IDs, Strong's-Hebrew numbers (inline), English/Mandarin glosses, semantic domain tags, LXX Greek equivalents at lemma level
- **Publisher:** Biblica, Inc. / Clear Bible
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Attribution required:** Yes
- **Source:** https://github.com/Clear-Bible/macula-hebrew (clone @ commit `47db250bd55d`, acquired 2026-05-04)
- **Role per `docs/source_license_policy.md`:** `morphology_data`
- **Bundled-source caveat:** MACULA Hebrew incorporates Westminster Hebrew Syntax (J. Alan Groves Center, CC BY 4.0), OSHB (CC BY 4.0), Cherith glosses (CC BY 4.0), and Semantic Dictionary of Biblical Hebrew (©2000-2021 United Bible Societies, "Used with permission"). MACULA's overall CC-BY 4.0 license governs the bundled distribution, but the SDBH-derived `@sdbh` / `@lexdomain` / `@coredomain` / `@contextualdomain` fields retain their UBS-permission nature. Direct verbatim republication of SDBH-flavored fields outside the MACULA bundle is **`consult_only` in spirit**: use the semantic-domain tags as a key into our own glossary work, do not republish them as standalone data.
- **Citation:** MACULA Hebrew Linguistic Datasets (Biblica, Inc. / Clear Bible, 2022–2024).

### unfoldingWord Translation Notes — Old Testament books (uW TN OT)

- **Used for:** Scholarly reference during OT translation — interpretive cruxes, textual issues (at `sources/en_tn/`, consulted but never copied)
- **Publisher:** unfoldingWord
- **License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- **Attribution required:** Yes
- **Reference-only use:** We consult uW TN during drafting for context but do not copy its wording. The Eremos Translation's own rationale and notes are independently composed; our output is not a derivative work of uW TN and therefore does not inherit CC-BY-SA.
- **Source:** https://git.door43.org/unfoldingWord/en_tn

### unfoldingWord Translation Words — Old Testament (uW TW OT)

- **Used for:** Cross-reference for biblical-term concepts during OT translation (at `sources/en_tw/`, consulted but never copied)
- **Publisher:** unfoldingWord
- **License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- **Attribution required:** Yes
- **Reference-only use:** Same hard rule as uW TN — consult only; do not copy phrasing.
- **Source:** https://git.door43.org/unfoldingWord/en_tw

### unfoldingWord Hebrew Bible (uW UHB)

- **Status:** **Not cloned for the Eremos pipeline.** uW publishes their UHB under CC BY-SA 4.0; the underlying Hebrew text is the WLC (public domain), but the published distribution carries ShareAlike. We use the WLC directly via `morphhb` (CC BY 4.0) instead, which avoids inheriting CC BY-SA via the uW UHB distribution.
- **If consulted:** Reference-only; treat as `consult_only` per `docs/source_license_policy.md`.

---

## Scholarly sources consulted (general references, not copied)

- **NA28 / UBS5** — textual apparatus for manuscript variants (consulted via published editions; no text copied)
- **Louw & Nida, *Greek-English Lexicon of the New Testament: Based on Semantic Domains*** — referenced via MACULA's Louw-Nida annotations
- **BDAG (*A Greek-English Lexicon of the New Testament and Other Early Christian Literature*, 3rd ed.)** — consulted by translators for rare words; no text copied
- **BDB (*A Hebrew and English Lexicon of the Old Testament*, 1906 ed.)** — public domain Hebrew lexicon; consulted during OT translation
- **HALOT (*The Hebrew and Aramaic Lexicon of the Old Testament*)** — `proprietary_reference`; consulted via Logos library
- **DCH (*Dictionary of Classical Hebrew*, Clines)** — `proprietary_reference`; consulted via Logos library
- **TDOT (*Theological Dictionary of the Old Testament*, Botterweck/Ringgren)** — `proprietary_reference`; consulted via Logos library
- **BHS / BHQ (*Biblia Hebraica Stuttgartensia / Quinta*)** — textual apparatus consulted via published editions / Logos library
- **Septuagint (Rahlfs / Göttingen)** — `proprietary_reference`; consulted via published editions / Logos library; LXX text NOT cloned into Eremos repo (no clean PD digital encoding readily available — see `docs/source_license_policy.md` §3)
- **Dead Sea Scrolls (Tov / Abegg / Lim editions)** — `consult_only`, elevated to active comparator for 1–2 Samuel, Isaiah, Pentateuch per plan
- **Targums, Vulgate, Peshitta, Samaritan Pentateuch** — ancient versional witnesses; consulted via published editions / Logos library; case-by-case role assignment
- Critical commentaries (Nicoll, NICNT, WBC, Anchor, Expositor's, NICOT, NAC, Tyndale OT, etc.) — consulted by translators for context; no text copied

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
> MACULA Greek + MACULA Hebrew (CC BY 4.0), Open Scriptures Hebrew Bible /
> morphhb (CC BY 4.0), Berean Standard Bible (CC0). Scholarly reference:
> unfoldingWord Translation Notes / Words (CC-BY-SA 4.0). Structural
> reference: Thai New Buddhist Translation (CC-BY-SA 4.0)."
