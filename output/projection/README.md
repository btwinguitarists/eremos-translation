# Eremos Translation for church projection software

Three whole-Bible files with the same text, in the formats projection programs import.
Verse numbers follow English (BSB) numbering, the numbering most Thai and English Bibles use
on screen. Psalm titles are included where the format allows (Zefania, OSIS).

| File | Format | Imports into |
|---|---|---|
| `eremos-thai.zefania.xml` | Zefania XML | OpenLP, and many other programs that read Zefania |
| `eremos-thai.osis.xml` | OSIS 2.1.1 | OpenLP, SWORD tools |
| `eremos-thai.opensong.xml` | OpenSong | OpenSong, OpenLP |

**OpenLP:** Bibles › Import Bible › choose Zefania (or OSIS / OpenSong) › select the file ›
name it "Eremos Translation (Thai)". See the OpenLP manual: https://manual.openlp.org/bibles.html

ProPresenter 7 and EasyWorship do not document a way to import a custom Bible, so no file is
provided for them yet.

This is a draft: drafted from the Hebrew and Greek, machine-checked, with Thai review beginning.
Public domain (CC0 1.0). Regenerate with `python3 scripts/export_projection.py`.
