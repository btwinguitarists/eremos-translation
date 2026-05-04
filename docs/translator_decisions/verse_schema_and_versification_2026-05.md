# OT verse schema + versification anchor

**Scope:** The per-verse JSON schema used for OT translations + the policy for handling places where Hebrew (MT), Septuagint (LXX), and English-Bible-tradition versification disagree.

**Decided:** 2026-05-04.

---

## 1. Per-verse JSON schema (extension of NT schema)

OT verse files live in `output/translations/<book>_<chapter>.json` — same path convention as NT. The schema extends the NT verse object with three new fields: `language`, `hebrew`, `aramaic`, plus updates to existing fields.

```json
{
  "book": "GEN",
  "chapter": 1,
  "verse": 1,
  "language": "hebrew",
  "hebrew": "בְּרֵאשִׁ֖ית בָּרָ֣א אֱלֹהִ֑ים אֵ֥ת הַשָּׁמַ֖יִם וְאֵ֥ת הָאָֽרֶץ׃",
  "thai": "ในปฐมกาล พระเจ้าทรงสร้างฟ้าสวรรค์และแผ่นดินโลก",
  "thai_summary": "...",
  "back_translation": "In the beginning God created the heavens and the earth",
  "key_decisions": [
    "..."
  ],
  "morphology": [
    {
      "lemma": "בְּ",
      "pos": "preposition",
      "thai_gloss": "ใน",
      "strong": "H871a"
    },
    ...
  ],
  "lxx_comparator": {
    "greek": "ἐν ἀρχῇ ἐποίησεν ὁ θεὸς τὸν οὐρανὸν καὶ τὴν γῆν",
    "alignment": "verbatim",
    "divergence_note": null
  },
  "versification": {
    "mt_ref": "GEN 1:1",
    "english_ref": "Genesis 1:1",
    "bsb_ref": "Genesis 1:1",
    "lxx_ref": "Genesis 1:1",
    "diverges": false
  }
}
```

### 1.1 Field descriptions

- **`language`** — `"hebrew"` or `"aramaic"`. Default `"hebrew"`. Aramaic for Daniel 2:4b–7:28, Ezra 4:8–6:18, Ezra 7:12–26, Jeremiah 10:11, Genesis 31:47b. Drives `run_checks.py` dispatcher (per plan §9.4) to route to language-aware checks.
- **`hebrew` / `aramaic`** — the Hebrew/Aramaic source text. Mutually exclusive with each other. (Greek field reserved for NT.)
- **`thai`** — the translated text. Same as NT.
- **`thai_summary`** — natural Thai paraphrase of meaning + cross-reference + footnote-style content. Same as NT. **NT-cited OT verses must include the cross-corpus orientation per `divine_names_table_2026-05.md` §"Why this differs from the NT corpus."**
- **`back_translation`** — English back-translation of the Thai. Same as NT.
- **`key_decisions`** — array of decision rationales. **Aspect** decisions (perfect-vs-narrative-past), **versification** decisions, **DSS-vs-MT** decisions, **divine-name** confirmations, etc. all go here.
- **`morphology`** — array of word-level morphology. Each entry = lemma + pos + Thai gloss + Strong's number. Built by `extract_book_hebrew.py`.
- **`lxx_comparator`** — present when the verse is NT-cited (per `data/ot_citations_used_in_nt.json`). Contains the LXX form + alignment status + divergence note.
- **`versification`** — present when the verse is in a known divergence zone (per `data/versification_map.json`). Contains the MT reference, English-Bible reference, BSB reference, LXX reference, and a `diverges` flag. Absent when no divergence.

### 1.2 What is NOT in the OT verse schema

- **No `greek` field on OT verses.** Greek text (LXX comparator) goes in `lxx_comparator` sub-object.
- **No `aramaic` AND `hebrew` simultaneously.** A verse is one or the other.
- **No `lxx_text` field** (the LXX is consulted-only per `source_license_policy.md` §3; we don't store the LXX text in our verse files; only an alignment note). The exception: NT-cited verses where we record the LXX form for cross-corpus reference.

---

## 2. Versification: MT-anchored, with map for known divergence zones

The OT has well-known versification differences across traditions. Eremos's policy:

**Anchor on MT versification.** Every Eremos verse has its `book/chapter/verse` field aligned to the MT (BHS-base, Hebrew Bible Modern Critical Edition). When MT differs from English-Bible / LXX / Vulgate / BSB versification, the Eremos verse stays with MT; the divergence is recorded in the `versification` sub-object.

### 2.1 Known divergence zones

**Psalms** — All 116 superscripted psalms in MT have a Hebrew "title" (`לְדָוִד`, `לַמְנַצֵּחַ`, etc.) that MT counts as v.1, but English/BSB don't number. Result: MT v.2 = English v.1 for these psalms.

| MT ref | English ref (NIV/ESV/BSB) | Notes |
|---|---|---|
| Psalm 3:1 | Psalm 3:title | Superscription |
| Psalm 3:2 | Psalm 3:1 | First numbered verse in English |
| Psalm 51:1-2 | Psalm 51:title | Two-verse superscription |
| Psalm 51:3 | Psalm 51:1 | First numbered verse in English |

This applies to ~116 psalms with superscriptions. Pre-populated in `data/versification_map.json`.

**Joel** — MT chapter 3 = English chapter 2:28-32; MT chapter 4 = English chapter 3.

| MT ref | English ref | Notes |
|---|---|---|
| Joel 3:1-5 | Joel 2:28-32 | Acts 2:17-21 cites these verses; Acts uses LXX/English chapter-numbering |
| Joel 4:1-21 | Joel 3:1-21 | |

**Malachi** — MT chapter 3 = English chapter 3 + 4 (English splits Malachi 3:19+ into chapter 4).

| MT ref | English ref | Notes |
|---|---|---|
| Malachi 3:1-18 | Malachi 3:1-18 | Aligned |
| Malachi 3:19-24 | Malachi 4:1-6 | "The day is coming..." through end of book |

**Job 41 / 1 Samuel 23-24** — minor verse-numbering shifts of 1-2 verses.

**Daniel + Ezra** — Aramaic-Hebrew transitions don't always align across versions; minor shifts.

**Jeremiah** — large-scale chapter reordering between MT and LXX. MT-priority means: Eremos uses MT chapter order. Where LXX-only material exists (Letter of Jeremiah, etc.), it is excluded per `ot_canon_and_text_base_2026-05.md` (39-book canon).

### 2.2 The `data/versification_map.json` file

Build before Genesis 1. Schema:

```json
{
  "PSA-3-1": {
    "mt_book": "PSA",
    "mt_chapter": 3,
    "mt_verse": 1,
    "mt_ref": "Psalm 3:1",
    "english_ref": "Psalm 3:title",
    "bsb_ref": "Psalm 3:0",
    "lxx_ref": "Psalm 3:1",
    "has_superscription": true,
    "diverges": true
  },
  "JOL-3-1": {
    "mt_book": "JOL",
    "mt_chapter": 3,
    "mt_verse": 1,
    "mt_ref": "Joel 3:1",
    "english_ref": "Joel 2:28",
    "bsb_ref": "Joel 2:28",
    "lxx_ref": "Joel 3:1",
    "diverges": true,
    "nt_citations": ["ACT 2:17"]
  },
  "MAL-3-19": {
    "mt_book": "MAL",
    "mt_chapter": 3,
    "mt_verse": 19,
    "mt_ref": "Malachi 3:19",
    "english_ref": "Malachi 4:1",
    "bsb_ref": "Malachi 4:1",
    "lxx_ref": "Malachi 3:19",
    "diverges": true
  }
}
```

Pre-populate the known divergence zones (~150 entries: ~120 psalm superscriptions + Joel + Malachi + minor shifts elsewhere). All other verses are assumed aligned (MT verse = English verse).

### 2.3 The `check_versification_anchor.py` enforcement

Per plan §9.1 (script #4): on every chapter, the check:

1. Loads the `data/versification_map.json` entries for that chapter.
2. Verifies each verse in the chapter's `output/translations/<book>_<chapter>.json` matches the MT-anchored verse number.
3. If a verse has divergence (per the map), verifies the verse's `versification` sub-object is populated.
4. Surfaces audit warnings for any mismatch.

Default-pass for chapters with no divergence-map entries (most of the OT).

---

## 3. Ketib / Qere — Masoretic textual variants

Ketib (`כְּתִיב`) is the consonantal text "as written"; Qere (`קְרֵי`) is the marginal "as read" — the Masoretes' alternative pronunciation/reading. Frequent in the OT (~1,500 places).

**Decision (default):** Translate the **Qere** (the read tradition). This is the convention of NRSV, NIV, ESV, NASB, NLT, and most modern translations.

**Exceptions:** Translate the Ketib if (a) Qere is clearly a euphemism (especially for gender / genitalia / tetragrammaton-substitute), and the Ketib reading is what the original author wrote, OR (b) the Qere is interpretive expansion the translator judges to obscure the original.

When Ketib is chosen, document in `key_decisions` with the witness IDs (e.g., "MT Ketib `יִשְׁכְּבֶנָּה` (he shall lie with her); Qere `יִשְׁגָּלֶנָּה` (he shall ravish her). Eremos translates Ketib for euphemism-breakage. Cf. Deut 28:30").

### 3.1 The `check_ketib_qere.py` script

Per plan §9.1 (script #11): this is **warning-only** initially. Surfaces every K/Q in a chapter for translator review without blocking ship. Promote to strict after pilot.

Schema for tracking K/Q decisions in `data/ketib_qere_decisions.json` (built incrementally during translation):

```json
{
  "DEU-28-30": {
    "verse": "Deuteronomy 28:30",
    "ketib": "יִשְׁכְּבֶנָּה",
    "qere": "יִשְׁגָּלֶנָּה",
    "translated": "ketib",
    "rationale": "Translated Ketib (euphemism breaking); Qere is post-MT euphemism"
  }
}
```

---

## When to revisit

- **At pilot end** (Ruth + Jonah + Gen 1-11) — review the schema. Tighten if any field is unused or causing friction.
- **At Phase 6F (Psalms) start** — re-verify all 116 psalm-superscription divergences are in `versification_map.json`. This is a heavy concentration.
- **At Phase 6G (Jeremiah)** — re-verify the MT-LXX ordering is being handled correctly per `ot_canon_and_text_base_2026-05.md` §"When to depart from MT" exception #4.
