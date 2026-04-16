# Eremos Translation — Genre Coverage & Production Pipeline

Maps every Bible genre to:
- What makes translation of that genre distinctive
- Which existing checks cover it
- What genre-specific checks are still needed
- Translation difficulty (affects production order)

This is the roadmap for getting from pilot (Mark 1 + 1 Tim 3) to the full Bible.

---

## Bible genres — 7 major types

| Genre | Books | Difficulty | Current status |
|-------|-------|------------|----------------|
| 1. Gospel narrative | Matt, Mark, Luke, John | Low-medium | Mark 1 ✅ |
| 2. Historical narrative (NT) | Acts | Medium | — |
| 3. Epistle | Rom–Phlm, Heb, James, 1-2 Pet, 1-3 John, Jude | Medium-high | 1 Tim 3 ✅ |
| 4. Apocalyptic (NT) | Revelation | **Very high** | — |
| 5. OT narrative | Gen 1–Deut 34 (narr. portions), Josh–Esth | Medium | phase 2 |
| 6. OT law | Torah legal portions | High (technical vocab) | phase 2 |
| 7. OT wisdom / poetry | Job, Psa, Prov, Eccl, Song | **Very high** (parallelism, meter) | phase 2 |
| 8. OT prophetic | Isa–Mal | High | phase 2 |

---

## What each genre needs

### 1. Gospel narrative (Matt/Mark/Luke/John)

**Distinctive:**
- Narrative + discourse mix
- Parables, aphorisms, miracle stories, dialogue
- Synoptic parallels (same saying across books)
- OT citations/allusions

**Covered by existing checks:**
- ✅ `check_key_term_consistency.py` — theological vocabulary
- ✅ `check_against_tnbt.py` — structural
- ✅ `check_ot_citations.py` — OT links
- ✅ `check_parallel_passages.py` — synoptic parallels
- ✅ `check_back_translation.py` — meaning preservation

**Still needed:**
- `check_parable_structure.py` — parable form (introduction, narrative, punchline)
- `check_dialogue_register.py` — who speaks to whom, matching Thai honorifics

**Translation difficulty:** Low–medium. Greek is relatively simple (especially Mark). Main challenge: consistent honorific register for Jesus.

---

### 2. Historical narrative (Acts)

**Distinctive:**
- Long speeches (Peter's Pentecost, Stephen, Paul in various cities)
- Sea voyage / travelogue vocabulary
- Roman legal/military terminology

**Covered by existing checks:**
- ✅ All the gospel-applicable checks above

**Still needed:**
- `check_speech_boundaries.py` — clear marking of where speeches start/end within narrative
- Additional technical glossary entries (Roman titles, provinces, legal terms)

**Translation difficulty:** Medium. Greek is more literary than Mark/John. Luke uses higher register.

---

### 3. Epistle (Paul + general)

**Distinctive:**
- Formulaic openings (salutation + thanksgiving) and closings (grace-benediction)
- Dense theological vocabulary (δικαιοσύνη, πίστις, χάρις, σάρξ, νόμος)
- Diatribe features (rhetorical questions, imaginary interlocutor, "by no means!")
- Paul's run-on sentences (Eph 1:3-14 is one Greek sentence)

**Covered by existing checks:**
- ✅ `check_key_term_consistency.py` — especially important for Pauline corpus coherence
- ✅ `check_against_tnbt.py`
- ✅ `check_ot_citations.py`
- ✅ `check_back_translation.py`

**Still needed:**
- `check_pauline_coherence.py` — theological key-term use across the Pauline corpus (same word in Rom, Gal, Eph, etc. — intentional divergences OK, drift not OK)
- `check_epistle_structure.py` — salutation / thanksgiving / body / closing / benediction boundaries
- Static glossary extension — salutation formulas, grace-benedictions, doxologies

**Translation difficulty:** Medium-high. Paul's theological density. Pastorals (1-2 Tim, Titus) are easier than Romans/Ephesians.

---

### 4. Apocalyptic (Revelation)

**Distinctive:**
- Visions with vivid imagery
- Heavy OT allusion (Rev has ~500 allusions, no formal citations)
- Symbolic language — numbers (7, 12, 144k), colors, beasts, lampstands
- "I saw" / "I heard" / "behold" vision-formulas throughout
- Semitic-flavored Greek (probably Semitic-original-thought in Greek garb)
- Unique hapax-density (a lot of technical apocalyptic vocabulary)

**Covered by existing checks:**
- ⚠ Current checks cover surface-level. OT-allusion density will overwhelm the curated citation list.

**Still needed:**
- `check_apocalyptic_symbols.py` — ensure symbol consistency (beast, Babylon, Lamb, throne, etc.)
- `check_ot_allusions.py` — extension of OT citation check for Revelation's allusion density (needs a deeper allusion database, possibly auto-generated from scholarly commentaries)
- `check_vision_formulas.py` — "καὶ εἶδον", "καὶ ἤκουσα", "ἰδού" markers preserved
- Static glossary — the whole apocalyptic vocabulary

**Translation difficulty:** Very high. Symbolic language + OT-density + unique vocabulary. Save for late in the NT work.

---

### 5. OT narrative (Genesis–Esther narratives)

**Distinctive:**
- Hebrew waw-consecutive chains (long strings of "and X happened")
- Toledot structure ("these are the generations of X")
- Divine name distinctions (YHWH vs Elohim — translation decision)
- Direct discourse markers (וַיֹּאמֶר)
- Etiological naming ("therefore it is called X to this day")

**Covered by existing checks:**
- Most existing checks ported to Hebrew source

**Still needed:**
- ETCBC/BHSA Hebrew morphology integration (already know the data; need extraction script `extract_book_hebrew.py`)
- `check_divine_names.py` — consistent rendering of YHWH vs Elohim vs Adonai
- `check_hebrew_idioms.py` — Hebrew idioms that need dynamic rendering (e.g., "son of Belial," "strengthen his hand")
- TNBT comparison irrelevant for OT (TNBT is NT only) — swap for another open Thai OT if one exists, or drop this check for OT

**Translation difficulty:** Medium. Hebrew narrative prose is actually straightforward syntax.

---

### 6. OT law (Torah legal material)

**Distinctive:**
- Case law formula: "כִּי־ / When / If X happens, then Y"
- Apodictic law: "לֹא תַעֲשֶׂה / You shall not..."
- Technical cultic vocabulary (קֹדֶשׁ/holy, טָהוֹר/clean, שֶׁקֶל/shekel, types of offering: עֹלָה, חַטָּאת, אָשָׁם, שְׁלָמִים, מִנְחָה)
- Legal consequences phrasing (מוֹת יוּמָת "surely be put to death")

**Still needed:**
- `check_legal_formulas.py` — case-law and apodictic-law patterns preserved
- `check_cultic_vocabulary.py` — technical terminology glossary enforcement
- Significant glossary expansion (maybe 200+ new entries for Leviticus alone)

**Translation difficulty:** High — vocabulary-dense, culturally distant, easy to mistranslate technical terms.

---

### 7. OT wisdom / poetry (Job, Psalms, Proverbs, Ecclesiastes, Song)

**Distinctive:**
- Hebrew parallelism is THE structural feature (synonymous, antithetical, synthetic, emblematic)
- Terse/compact lines (English translations typically 2-3x longer than Hebrew)
- Acrostics (Psa 9/10, 25, 34, 37, 111, 112, 119, 145; Lam 1-4; Prov 31:10-31) — can't preserve in Thai, but structural markers possible
- Wisdom vocabulary (חָכְמָה, יִרְאַת־יהוה, כְּסִיל "fool", etc.)
- Meter (can't quantify in Thai, but line-length balance can be approximated)

**Still needed:**
- `check_parallelism.py` — ensure each Hebrew line has a corresponding Thai line, balanced length, parallel structure preserved where possible
- `check_wisdom_vocabulary.py` — the technical wisdom lexicon
- `check_acrostic_markers.py` — for the acrostic psalms, note which lines correspond to which Hebrew letter (since we can't reproduce the acrostic in Thai, at least preserve the markers in notes)
- `check_strophe_boundaries.py` — stanza breaks per BHS paragraphing

**Translation difficulty:** Very high. Parallelism + terseness + acrostics + wisdom vocabulary. Psalms will take years.

---

### 8. OT prophetic (Isaiah–Malachi)

**Distinctive:**
- Oracle-formula: "thus says the LORD" (כֹּה אָמַר יהוה), "oracle of the LORD" (נְאֻם־יהוה)
- Woe-oracles (הוֹי)
- Call narratives (Isa 6, Jer 1, Ezek 1-3)
- Apocalyptic sections in later prophets (Zech, Dan, Joel)
- Mixed narrative / poetry (some books mostly poetry, some mixed)

**Still needed:**
- `check_oracle_formulas.py` — consistent rendering of the messenger formulas
- Overlap with apocalyptic checks (for Zechariah, Daniel, Joel)
- Overlap with wisdom/poetry checks (most prophetic discourse is in verse)

**Translation difficulty:** High. Combines poetic complexity with theological density.

---

## Recommended production order

This is the SIL/Wycliffe/unfoldingWord-influenced progression — complexity builds gradually, vocabulary accumulates:

```
Phase 1  ─ PILOT (complete) ─
  Mark 1                   ✅ DONE
  1 Timothy 3              ✅ DONE

Phase 2  ─ COMPLETE NT NARRATIVE ─
  Mark 2–16                (finish the gospel we started, grow the glossary)
  Matthew                  (second synoptic — parallels start activating)
  Luke + Acts              (Luke's 2-vol work)
  John                     (different register; save for later in this phase)

Phase 3  ─ PAULINE CORPUS (as a block) ─
  Galatians                (earliest; shortest)
  1-2 Thessalonians        (also early)
  1-2 Corinthians          (dense theology appears)
  Romans                   (systematic; apex)
  Ephesians / Colossians   (disputed but high-register)
  Philippians              (pastoral)
  1-2 Tim, Titus, Phm      (Pastorals — we have 1 Tim 3 already)

Phase 4  ─ GENERAL EPISTLES ─
  James                    (wisdom-epistle)
  1-2 Peter
  1-2-3 John
  Jude
  Hebrews                  (last — highest register in the corpus)

Phase 5  ─ APOCALYPTIC (Revelation) ─
  Requires new checks (symbols, vision-formulas, OT-allusion density).
  Build those before starting.

Phase 6  ─ OT (years of work ahead) ─
  Requires: Hebrew extraction (ETCBC/BHSA), Hebrew morphology, OT
  equivalents of all checks, massive glossary expansion. Start with:
    Genesis 1–11              (primeval history; simple narrative)
    Ruth / Jonah / Esther     (short narratives, pedagogically standard)
    Then build from there.

Phase 7  ─ OT POETRY + PROPHETS ─
  Psalms (start with 1, 23, 100, 150 as pilots)
  Proverbs
  Prophets (Isaiah first — most-cited in NT)
  Finish with: Job, Song of Songs, Ecclesiastes (highest-difficulty)
```

Timeline, realistically:
- Phase 2 (NT narrative): 3–6 months at 1 chapter/day cadence
- Phase 3 (Pauline): 3–4 months
- Phase 4 (general epistles): 2 months
- Phase 5 (Revelation): 2–3 months including new check development
- **Total NT: ~12 months if you translate most days**
- Phase 6 + 7 (OT): 2–5 years depending on pace

---

## Check-script roadmap

Checks already built (work across NT genres):

- ✅ `check_key_term_consistency.py`
- ✅ `check_against_tnbt.py`
- ✅ `check_ot_citations.py`
- ✅ `check_parallel_passages.py`
- ✅ `check_back_translation.py` (in-chat mode)

Checks to add before scaling beyond current pilots:

| Priority | Check | When needed |
|----------|-------|-------------|
| Medium | `check_pauline_coherence.py` | Before Romans (3rd Pauline letter) |
| Medium | `check_dialogue_register.py` | Before Matthew (heavy dialogue) |
| Low-medium | `check_speech_boundaries.py` | Before Acts |
| High | `check_apocalyptic_symbols.py` | Before Revelation |
| High | `check_vision_formulas.py` | Before Revelation |
| High | `check_ot_allusions.py` (denser) | Before Revelation |

OT-specific checks (Phase 6+):

| Check | Purpose |
|-------|---------|
| `check_divine_names.py` | YHWH / Elohim / Adonai consistency |
| `check_parallelism.py` | Hebrew poetry structure |
| `check_wisdom_vocabulary.py` | Wisdom lexicon |
| `check_oracle_formulas.py` | "thus says the LORD" markers |
| `check_cultic_vocabulary.py` | Torah legal / cultic terms |
| `check_hebrew_idioms.py` | Hebrew idiomatic patterns |
| `check_acrostic_markers.py` | Acrostic psalms |
| `check_legal_formulas.py` | Torah case/apodictic law patterns |
| `check_strophe_boundaries.py` | Poetry strophe/stanza |

---

## Bottom line

**For the NT**, we're 90% methodologically complete. A few more genre-specific checks before Revelation, and `check_pauline_coherence.py` before Romans, and we're equipped.

**For the OT**, there's meaningful additional infrastructure (Hebrew extraction, ~10 new checks, massive glossary expansion). That's phase 6+ work and worth scoping when we get there.

**For right now**, finishing Mark (Phase 2 start) is the right next move. The existing checks handle it, and each chapter grows the glossary and confirms the pattern works.
