# OT canon, text base, and source hierarchy

**Scope:** Which Old Testament canon Eremos translates, which Hebrew/Aramaic text serves as the translation base, and which other ancient witnesses serve as comparators.

**Decided:** 2026-05-04 (Ben + plan §4).
**Companion doc:** `docs/source_license_policy.md` (Gate 0 — license roles).

---

## Canon: 39-book Protestant OT

Eremos translates the **39-book Protestant Old Testament canon**, in the conventional Christian-Bible book order:

**Pentateuch (5):** Genesis, Exodus, Leviticus, Numbers, Deuteronomy.
**Historical (12):** Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther.
**Poetry/Wisdom (5):** Job, Psalms, Proverbs, Ecclesiastes, Song of Songs.
**Major Prophets (5):** Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel.
**Minor Prophets (12):** Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi.

**Not in scope:** Apocrypha / Deuterocanonical books (Tobit, Judith, Wisdom, Sirach, Baruch, 1–2 Maccabees, etc.). Eremos is an evangelical-Protestant project; including Apocrypha would overstep scope. If a future maintainer wants to translate them, that's a separate project.

---

## Text base: Masoretic Text (MT) — primary

The translation base for the OT is the **Masoretic Text**, instantiated via:

- **Westminster Leningrad Codex (WLC)** — the published electronic text matching the *Biblia Hebraica Stuttgartensia* (BHS) base. Source: `sources/morphhb/` (CC BY 4.0; underlying WLC is public domain).
- **OSHB lemma + WHM morphology** layers in `sources/morphhb/`.
- **MACULA Hebrew** clausal/syntactic annotations in `sources/macula-hebrew/` (CC BY 4.0).

The MT is "primary" in the strong sense: when MT and other ancient witnesses disagree, the **default is to follow the MT** unless one of the documented exceptions in the source-hierarchy table below applies.

---

## Source hierarchy

The OT translation pipeline draws from four tiers of textual witness, plus paratextual aids.

### Tier 1 — Primary translation base

| Source | License | Use |
|---|---|---|
| WLC (via morphhb) | PD; CC BY 4.0 distribution | Hebrew/Aramaic source text — the base everything else compares against |

### Tier 2 — Morphological / syntactic aids (use when translating)

| Source | License | Use |
|---|---|---|
| WHM morphology (in morphhb) | CC BY 4.0 | Per-word morphology codes |
| OSHB lemma layer (in morphhb) | CC BY 4.0 | Lemma identification, Strong's-Hebrew numbers |
| MACULA Hebrew | CC BY 4.0 | Clause-level syntax trees, semantic-domain hints (SDBH-derived; treat semantic-domain fields with curator care per `source_license_policy.md` §2.2 caveat), inline LXX equivalents at the lemma level |

### Tier 3 — Ancient version comparators (consult when MT is disputed or NT cites)

| Source | License | Use |
|---|---|---|
| Septuagint (Rahlfs / Göttingen) | proprietary_reference (Logos consult only — see `source_license_policy.md` §3) | (a) NT-citation alignment when an OT verse is cited in already-shipped Thai NT (`check_nt_quotation_alignment.py` flags); (b) major MT-LXX divergence zones (Jeremiah short text, 1 Samuel 17 differences, Esther additions, Daniel 3) |
| MACULA Hebrew inline `greek=` field | CC BY 4.0 | Word-level LXX equivalent at every Hebrew lemma — covers the load-bearing case without needing a separate LXX text clone |
| Targums (Onkelos, Pseudo-Jonathan, Neofiti, Jonathan) | varies by edition; consult_only | Aramaic interpretive expansion; useful for understanding ancient Jewish reception of difficult passages; never the primary witness |
| Vulgate (Jerome) | varies by edition; consult_only | Western Christian interpretive tradition; useful where Latin was the primary Bible of the translator-traditions Eremos draws from (Beekman/Callow/Larson/Nida) |
| Peshitta (Syriac) | varies by edition; consult_only | Eastern witness; sometimes preserves a non-MT Hebrew text; valuable for Isaiah, Genesis, Psalms |
| Samaritan Pentateuch | mixed; consult_only | Helpful for Pentateuchal text-criticism; differs from MT in ~6,000 places |

### Tier 4 — Dead Sea Scrolls (active comparator for select books)

Per Ben's 2026-05-04 lock (plan §10): **DSS is elevated from Tier 4 to active comparator** for the following books:

- **1–2 Samuel** — DSS witness 4QSamᵃ preserves a longer, Sept-aligned text in many places where MT has suffered haplography. Modern translations (NRSV, NIV, ESV, NLT) frequently follow 4QSamᵃ over MT for Samuel.
- **Isaiah** — 1QIsaᵃ (the Great Isaiah Scroll) is a complete-book DSS witness, ~1000 years older than the Aleppo Codex. Many modern translations adopt 1QIsaᵃ readings in disputed places.
- **Pentateuch** — 4QpaleoExodᵐ, 4QGenᵉ, and other Pentateuchal DSS witnesses sometimes preserve readings that align with the LXX or Samaritan Pentateuch against the MT.

For these three corpora, the policy is:
- Translate from MT by default.
- When a DSS variant has scholarly weight (cited by NRSV/NIV/ESV apparatus, recommended by Tov, Würthwein, or DSS-aware commentaries), document the variant in `key_decisions` with the witness ID + the basis for adopting (or not adopting) it.
- Use DSS adopted readings where MT is clearly corrupted or missing text, with a verse-level footer note ([Tier 2] per RULES.md) when the divergence is theologically significant.

For all other OT books, DSS remains a **specialist consult** — recordable in `key_decisions` if a DSS reading is materially relevant, but not routinely adopted over MT.

### Tier 5 — Proprietary reference (consult only via Logos)

| Source | Role |
|---|---|
| HALOT (*Hebrew and Aramaic Lexicon of the Old Testament*) | Primary modern Hebrew/Aramaic lexicon; consult for any contested word |
| DCH (*Dictionary of Classical Hebrew*, Clines) | Comprehensive modern Hebrew lexicon |
| TDOT (*Theological Dictionary of the Old Testament*, Botterweck/Ringgren) | Word-study depth |
| BHS / BHQ apparatus | Critical-edition apparatus for textual decisions |
| UBS Translator's Handbooks (per book) | SIL/UBS translator's reference |
| WBC, NICOT, NAC, Tyndale OT, AB | Mainstream evangelical-scholarly commentaries |

Translator may consult these in Logos. **Phrasing not copied** into Eremos files. Cite by short reference in translator notes.

### Tier 6 — Open-license English bridges (consult only; not source)

| Source | License | Use |
|---|---|---|
| BSB OT (already on disk) | CC0 | English sanity-check during drafting; same role as for NT |
| BDB (1906 ed.) | PD | One PD Hebrew lexicon; gloss text usable in English notes if paraphrased |
| JPS 1917 Tanakh | PD | English bridge translation; consult, don't copy |
| Brenton's English LXX | PD | When wanting to read the LXX in English without going to Logos |

---

## When to depart from MT (the four exception triggers)

The MT-primary rule has four documented exceptions where another witness should be considered:

1. **Obvious copyist error preserved by MT.** Cases where MT's reading is grammatically impossible, semantically nonsensical, or contradicts itself within a few verses, and another ancient witness preserves a clean reading. Example: 1 Sam 13:1 ("Saul was [BLANK] years old when he began to reign, and he reigned [BLANK + 2] years over Israel" — MT has lost the numbers; LXX-Lucianic + 4QSamᵃ have alternative readings).
2. **NT citation alignment requires LXX form.** When the NT Greek author quotes an OT passage in its LXX form (Heb 1:6 quoting Deut 32:43 LXX-form, etc.), the OT translation should at minimum *acknowledge* the LXX form even while translating MT. Document the divergence.
3. **DSS elevated-comparator findings (Sam, Isa, Pent.).** Per the elevation above. DSS overrides MT only when the case is well-attested in modern apparatus.
4. **Major MT-LXX divergence zones (Jer, 1 Sam 17, Esther, Daniel 3).** Where MT and LXX differ at scale (Jeremiah is ~1/8 shorter in LXX; 1 Sam 17 has whole verses missing in LXX; Esther LXX has six "Greek additions"; Daniel 3 LXX-Theodotion has the Song of the Three additions): translate **MT only**; document the LXX-only material in a Tier 3 footer note with witness IDs (`output/textual_variants/<book>_<chapter>.json`); do **not** include the LXX-only material in the main text.

For (1), (2), (3): the divergence is recorded in the verse's `key_decisions` field plus a `[Tier 2] verse-level footer note` per RULES.md §5b. The translator decides per-verse based on the witness strength.

For (4): document at chapter-level via the `output/textual_variants/<book>_<chapter>.json` file, with separate audit-flagging in `audit_inclusion_variants.py`.

---

## What this does NOT mean

- **Eremos is not a critical text.** We do not produce a textual apparatus. We produce a translation of the MT with documented exceptions. Readers wanting full apparatus consult NA28-equivalent OT critical editions (BHS/BHQ, Hebrew University Bible Project).
- **Eremos is not LXX-primary.** Some traditions translate from LXX (Eastern Orthodox, much of patristic-era reception). Eremos translates from MT. This is consistent with NRSV/NIV/ESV/NASB/NLT modern Protestant tradition.
- **Eremos is not "majority text" / "received text" Hebrew.** We use the WLC (BHS-base), not a Ben Asher / Aleppo or Aleppo-reconstructed text per se. The WLC is the standard published electronic text and aligns with BHS / BHQ critical apparatus expectations.

---

## When to revisit

- **At every major phase boundary** (6A → 6B, etc.) re-confirm the source-hierarchy table is intact and that no new sources have crept in undocumented.
- **If a DSS-edited apparatus changes** (e.g., a new DJD volume releases) — re-check for any newly-published readings affecting Sam/Isa/Pent.
- **If a CC0-friendly digital LXX appears** — promote LXX from `proprietary_reference` to `primary_text` and clone it; this would close the §3-deferral in `source_license_policy.md`.
- **If a downstream user reports a reading that doesn't match BHS** — verify the WLC-base electronic text has not drifted at upstream `morphhb` and re-pin the commit hash if needed.
