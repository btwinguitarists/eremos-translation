# Eremos Translation — Rules

Canonical translation rules for the Eremos Translation. Every chapter must conform to these rules; the check scripts enforce what can be enforced mechanically. Review this file before translating, and treat deviations as requiring explicit justification.

Derived from industry standards used by SIL, Wycliffe, UBS, and unfoldingWord (Larson's meaning-based translation; Beekman & Callow's principles; Paratext's check framework).

---

## 0. Confessional position

Eremos Translation is **evangelical Protestant**. Source-text family: SBLGNT (Alexandrian-leaning critical text, same scholarly base as ESV / NIV / NASB / CSB / BSB). Translation philosophy: optimal equivalence (BSB family). Canon: 27-book NT (no deuterocanonicals).

**Editorial decisions on contested verses follow what major evangelical Protestant translations do.** When manuscript evidence is split, we prefer the editorial choice that aligns with the modern evangelical critical-text consensus (NA28-aligned, where SBLGNT and NA28 agree); when SBLGNT and NA28 disagree, we follow SBLGNT but document the divergence.

**License vs. theology**: CC0 means anyone of any tradition may use the translation, but **the editorial decisions are evangelical Protestant** — not ecumenical-syncretist or doctrinally neutral. Do not let the openness of the license drift into doctrinally relativistic note-writing. Notes should describe textual / linguistic / cultural facts, not pastorally endorse the doctrinal frameworks of other traditions. (If a passage is genuinely compatible with multiple traditions' theological readings, that observation belongs in scholarly footnotes, not in the verse-level note. Or rephrase descriptively: "preserves the Greek metaphor" rather than "permits multiple Eucharistic theologies.")

---

## 1. Translation philosophy

**Optimal equivalence.** Faithful to Greek grammar, syntax, and semantic range AND natural in modern Thai. Not formal equivalence (slavish word-for-word), not pure dynamic equivalence (loose paraphrase). Match BSB's approach in English.

The **four pillars** (SIL / Larson):

- **Accuracy** — faithful to the meaning of the source text
- **Clarity** — readable by the target audience
- **Naturalness** — sounds like native Thai, not translationese
- **Acceptability** — respectful register appropriate for Scripture in Thai

When pillars conflict, **accuracy wins**, with naturalness documented as a tradeoff.

---

## 2. Sources (strict — do not violate)

**During translation**, the AI may read only:

- The Greek text (SBLGNT) with MACULA morphological analysis
- The Berean Standard Bible English (CC0) as a sanity check — NEVER as a source to copy from
- This RULES.md
- `glossary.json` — our persistent key-term ledger
- Prior chapters of our own Eremos Translation output (for consistency)
- **unfoldingWord Book Introduction** (CC-BY-SA) at `output/uw_notes/<slug>_FRONT.md` — **MUST be read FIRST** before any chapter of a book. Provides author, audience, date, themes, outline, and book-specific translation issues. SIL/Wycliffe pro practice.
- **unfoldingWord Translation Notes** (CC-BY-SA) at `output/uw_notes/<slug>_<NN>.md` — chapter-level scholarly reference (interpretive cruxes, textual issues). Read AFTER the book intro. **Read for context, never copy wording.** See §8 for license handling.

**Never read during translation**:

- Any copyrighted Thai translation (THSV, NTV, ERV Thai, TNCV)
- TNBT (CC-BY-SA) — see §8 for why
- Any copyrighted commentary
- unfoldingWord TW wording (CC-BY-SA) — reference permitted, but any paraphrase must be in Claude's own words (see §8)

**Why the strictness?** This is what preserves the "independent creation" copyright defense. Our output is produced by independent analysis of the public-domain original languages. No one else's wording gets into our drafting process. After drafting, we *compare* against other translations — but only to identify divergences to justify, never to copy from.

### Sources evaluated and deferred

- **CNTR Universal Apparatus** (Center for New Testament Restoration, https://greekcntr.org/) — evaluated 2026-04 for potential use as a programmatic textual-variant audit source. **Deferred**: the Universal Apparatus is not yet distributed as a machine-readable dataset (only as a PDF with the 2022 printed SRGNT), and the variant cases our translation notes already catch (Mark 1:1, 1:41, 2:26, 9:29, 14:24, 16:9-20) cover the translation-affecting surface. CNTR's `SR.tsv` base-text data is CC BY 4.0 and could be adopted later. CNTR's `transcriptions` repo is CC BY-SA 4.0 and **must not be mixed with our CC0 output**. Full spike notes at `docs/CNTR_SPIKE_2026-04.md`. Revisit in ~6 months.

---

## 3. Register & honorifics

- **Divine subjects** (God, Christ, Spirit) always use ราชาศัพท์ (royal register):
  - `ทรง` prefixes verbs of action (ทรงสอน, ทรงรักษา)
  - `เสด็จ` for movement (เสด็จมา, เสด็จไป)
  - `ตรัส` for speech (ตรัสว่า)
  - `ทอดพระเนตร` for "see"
  - `พระหัตถ์` for "hand", `พระบาท` for "foot"
  - `พระเจ้า` for God; `พระเยซู` for Jesus (พระ-prefix is the honorific)

- **Humans addressing Christ/God** use the lowest humble register:
  - `ข้าพระองค์` or `ข้า` for "I"
  - `พระองค์` for "you" (divine addressee)

- **God addressing the Son**: `เจ้า` is acceptable (intimate Father-Son); may use `พระองค์` for high reverence. Document the choice.

- **Demons or adversaries** use neutral/distancing register, never honorifics.

- **Inter-human dialogue**: match the social relationship. Peasants to rabbi → respectful; peers → casual; master to servant → direct.

---

## 4. Key-term consistency

Every meaningful Greek lemma gets one canonical Thai rendering recorded in `glossary.json`. If a later verse warrants a different rendering (because the Greek word carries a different sense in context), that's permitted but must be:

1. Documented in the verse's `key_decisions` or `notes`
2. Added as a *contextual variant* to the glossary entry

The **default Thai rendering** for a lemma, once established, should not drift. The key-term consistency check (`scripts/check_key_term_consistency.py`) flags any lemma whose renderings vary without documented rationale.

Non-negotiable standard terms (established from Mark 1):

| Greek | Thai | Notes |
|-------|------|-------|
| εὐαγγέλιον | ข่าวประเสริฐ | Never "พระกิตติคุณ" unless explicitly noted |
| χριστός | พระคริสต์ | Title, not a proper name |
| Ἰησοῦς | พระเยซู | The พระ prefix is the divine honorific |
| σατανᾶς | ซาตาน | Transliteration, standard |
| πνεῦμα ἅγιον | พระวิญญาณบริสุทธิ์ | |
| βαπτίζω / βάπτισμα | บัพติศมา | Transliteration, standard in Thai Christianity |
| ἔρημος | ถิ่นทุรกันดาร | When "wilderness/desert region" |
| ἔρημος τόπος | ที่เปลี่ยว | When "solitary place" |
| κύριος (= YHWH in OT citations) | องค์พระผู้เป็นเจ้า | |
| κύριος (as a title for Jesus/human master) | render per context, document |
| συναγωγή | ธรรมศาลา | |
| μετανοέω / μετάνοια | กลับใจ / การกลับใจ | |
| βασιλεία τοῦ θεοῦ | อาณาจักรของพระเจ้า | |
| ἁμαρτία | บาป | |
| ἄφεσις | การยกโทษ / การอภัย | Document choice |
| ἀγαπητός | ที่รัก | "Beloved" — or "ที่รักยิ่ง" for intensification |

For proper nouns (persons, places), transliteration follows established Thai Christian practice. Maintain a `glossary.json` proper-noun section to avoid drift (Ἰωάννης → ยอห์น, Ἠσαΐας → อิสยาห์, etc.).

---

## 5. What must always be flagged

Every verse translation must include explicit entries for:

- **Hapax legomena** — words appearing only once in the NT. Rationale must draw on classical/LXX usage, context, etymology. Mark in `notes` with the word.
- **Textual variants** where SBLGNT diverges from the Byzantine majority text or BSB's choice. Name the variant, name our decision, state why.
- **Polysemous Greek words** whose choice of sense affects translation (e.g., σάρξ as "flesh" vs "human nature" vs "physical body")
- **OT citations or allusions** — identify the OT source and whether the Greek matches MT or LXX. For each intertextual claim the verse-note asserts, a corresponding entry MUST be added to `data/nt_ot_citations.json` in the same editing pass. The drift-detector in `check_ot_citations.py` will block ship if notes claim a citation that is not recorded in the DB.
- **Gendered/socially-contested language** — flag interpretive decisions where scholarly opinion is split (e.g., γυναῖκας in 1 Tim 3:11)
- **Technical or cultural terms** that don't have direct Thai equivalents

### Bracket convention for inclusion variants (added 2026-04-18)

When SBLGNT's apparatus flags an **inclusion variant** — words SBLGNT's main text omits but mainstream traditions (NA28, BSB, NIV, ESV, THSV) include — render the words in **single Thai brackets `[...]`** in the `thai` field, and explain the convention in the verse's `thai_summary`.

Reader-trust rationale: if Thai readers expect the words from THSV / NTV / their childhood Bible and we silently omit, they read the omission as our editorial overreach. Brackets honestly signal "these words appear in many manuscripts and translations; our base text doesn't print them in the main line." This is the NA28 / NRSV-Updated / NET convention.

**Scope:**
- Applies only to inclusion variants (we omit, mainstream includes), not to word-choice variants (we picked word A, mainstream picked word B — those go in `thai_summary` only).
- Not for cases where modern critical-text consensus matches our practice (e.g. Mark 7:16, 9:44, 9:46, 9:49 longer reading — modern evangelical Bibles all skip these too; no reader confusion).
- Not for the longer ending of Mark 16:9-20, which uses ⟦double-brackets⟧ as a larger-block stylistic distinction.

**Currently bracketed (Mark first-pass audit, 2026-04-18):**
- Mark 1:1 — `[พระบุตรของพระเจ้า]`
- Mark 3:14 — `[ซึ่งพระองค์ทรงเรียกว่าอัครทูตด้วย]`
- Mark 9:29 — `[และการอดอาหาร]`

**For future books:** run `scripts/audit_inclusion_variants.py` on each new book to surface candidate verses; apply brackets only after confirming each one is an inclusion variant (not word-choice) and that mainstream traditions do include the words.

---

## 6. Verse-level output shape

Every verse in `output/translations/<book>_<NN>.json` must have:

```json
{
  "reference": "1 Timothy 3:1",
  "chapter": 3,
  "verse": 1,
  "greek": "<Greek text>",
  "bsb_english": "<BSB text>",
  "translation": {
    "thai": "<natural Thai rendering>",
    "thai_literal": "<optional literal alternative if it differs meaningfully>",
    "thai_summary": "<optional 1-2 sentence Thai-language explanation for the average reader — see docs/THAI_SUMMARY_STYLE.md>",
    "key_decisions": [
      { "greek": "<word or phrase>", "thai": "<Thai rendering>", "rationale": "<why this choice>" }
    ],
    "notes": "<textual variants, hapax, cross-references, interpretive calls>"
  }
}
```

Verses with no meaningful interpretive decisions may have empty `key_decisions: []` and `notes: null`, but this must be the exception, not the norm. If a verse has zero decisions, consider whether something subtle is being missed.

**Schema requirement (strict):** every verse's `translation` object MUST contain the keys `thai`, `thai_literal`, `thai_summary`, `key_decisions`, and `notes`. If a field has no content, write the explicit null (`"notes": null`, `"thai_literal": null`, `"thai_summary": null`) or empty list (`"key_decisions": []`). **Never omit the key itself.** Check scripts use `.get()` defensively, but an absent key still signals schema drift and will be backfilled by `scripts/backfill_notes_null.py` at the next audit. This rule was tightened on 2026-04-17 after Gemini's cross-AI review flagged 69 verses missing the `notes` key.

### `thai_summary` — reader-facing layer (added 2026-04-17)

The `thai_summary` field serves a **different audience** from `key_decisions` and `notes`:

- **`key_decisions` + `notes`** (English) → for translators, reviewers, scholars, AI evaluators. Defends and documents the methodology. Belongs in the GitHub repo and admin views; appears in the Eremos app behind a "Show scholarly notes" toggle.
- **`thai_summary`** (Thai, optional, 1-2 sentences) → for the average Thai Christian reading the verse. Surfaces an OT echo, cultural context, or theological motif in plain modern Thai. Appears prominently in the Eremos app popup above the scholarly notes.

**Not every verse needs a summary.** Roughly 30-50% of verses warrant one. Skip simple narrative without interpretive payload. See `docs/THAI_SUMMARY_STYLE.md` for the full editorial spec including length, register, content priorities, and verse-type guide.

The `thai_summary` field is OPTIONAL. Backward-compatibility: chapters translated before this field existed (Mark 1-8, 1 Tim 3 as of 2026-04-17) will not have it. New chapters from Mark 9+ are expected to include it where warranted.

---

## 7. Post-draft checks (mandatory before commit)

Before any chapter is committed to `output/translations/`, the **check cadence** runs:

1. **Back-translation check** — `scripts/check_back_translation.py <book> <chapter>` — AI translates our Thai back to English, diffs against BSB, flags divergences not explained in our notes.
2. **Key-term consistency audit** — `scripts/check_key_term_consistency.py` — scans all translations, reports per-lemma rendering variance, flags undocumented divergence.
3. **TNBT structural comparison** — `scripts/check_against_tnbt.py <book> <chapter>` — verse-by-verse structural comparison against Thai TNBT (CC-BY-SA). Vocabulary differences expected (TNBT uses Buddhist register); structural differences (e.g., number of sentences, missing clauses) are the signal.
4. **OT citation check** — `scripts/check_ot_citations.py <book> <chapter>` — flags NT verses that quote OT; notes whether Greek matches LXX or MT. Also detects **DB drift**: when a verse's notes claim an OT citation (via phrases like "OT CITATION", "composite citation", "ADDED TO NT_OT_CITATIONS", "FULFILLMENT:") co-located with an OT book reference, the check fails if no entry exists in `data/nt_ot_citations.json` for that verse. This closes the silent-drop failure mode identified on 2026-04-17, when chapters 11/13/14/15 shipped with zero DB entries despite rich OT intertextual notes. **The translator must add a DB entry at the time the note is written — not as a post-hoc curation.**
5. **Parallel-passage check** — `scripts/check_parallel_passages.py` — for synoptic parallels, flags divergent renderings of the same saying across books (applicable once we have multiple gospels).

The orchestrator `scripts/run_checks.py <book> <chapter>` runs all applicable checks and produces `output/check_reports/<book>_<NN>_checks.md`.

**Ship criterion**: zero unresolved flags. A flag is "resolved" when either (a) the note is added to the verse, or (b) a decision document in `docs/translator_decisions/` records why the flag is acceptable as-is.

**Enforcement (Levels 1-3):**

- **Level 1 — audit trail.** Git history records every revision committed to `output/translations/`. Each chapter's `output/check_reports/<slug>_<NN>_iterations.txt` tracks how many revision passes happened before ship.
- **Level 2 — ship gate.** `scripts/ship_chapter.sh` runs `run_checks.py` as a pre-flight and refuses to proceed on non-zero exit. No more "trust the chat" — the gate is mechanical.
- **Level 3 — revision loop.** When checks fail, run `scripts/revise_chapter.py --book <CODE> --chapter <N>`. It reads the per-check exit codes and writes `output/check_reports/<slug>_<NN>_REVISIONS_NEEDED.md` — a structured prompt listing each flagged verse with the failure reason. Claude in the same chat reads this, edits the translation JSON, re-runs `run_checks.py`. If still failing after 3 iterations, the script flags the chapter for human review (theological consultant or native-speaker reviewer).

This addresses the formal-feedback-loop gap noted in cross-AI evaluation. Informational warnings (e.g., TNBT structural divergences, which are EXPECTED because TNBT uses Buddhist register) do NOT trigger revision — only checks that exit non-zero do.

---

## 8. CC-BY-SA source policy (TNBT, unfoldingWord)

### TNBT (Thai New Buddhist Translation)

The TNBT (github.com/pepa65/TNBT) is CC-BY-SA 4.0. It is a legitimate open-source Thai NT and a useful **structural reference**. But:

- **Never read during translation.** TNBT's Thai wording must not influence our drafting.
- **Only compared after drafting**, mechanically, by `check_against_tnbt.py`.
- **Vocabulary divergence is expected.** TNBT deliberately uses Buddhist register (พระศรีอาริย์ for Messiah, นิพพาน for eternal life, พิธีมุดน้ำ for baptism). Our project uses standard Thai Christian vocabulary. Divergences from TNBT on vocabulary do **not** indicate an error — they indicate a deliberate choice of register.
- **Use TNBT divergences as**: a prompt to spot-check structural-level understanding. Different sentence count, different verb/noun handling → investigate.

### unfoldingWord Translation Notes & Translation Words

unfoldingWord materials (Translation Notes, Translation Words, Translation Questions) are CC-BY-SA 4.0. They are **permitted reference material during translation** — unlike TNBT, which is target-language wording we must avoid, uW TN is English scholarly commentary that safely informs exegesis without polluting the target-language output.

- **Reading uW TN during translation**: ✅ permitted and encouraged. Claude should consume `output/uw_notes/<slug>_<NN>.md` as part of chapter preparation.
- **Copying uW TN wording into our rationale**: ❌ never. Paraphrase in Claude's own words. (Direct quotations would force our rationale text to inherit CC-BY-SA, complicating the CC0 license on our Thai translation output.)
- **Our Thai translation itself**: is Claude's own work from Greek. uW TN explains what the Greek means; it does not tell us how to render it in Thai.

### CC0 protection

Our output remains CC0 if and only if:
1. We never copy wording verbatim from any CC-BY-SA source (TNBT, uW TN, uW TW)
2. Every derivation is independently re-expressed
3. We do not embed CC-BY-SA text in the translation output files

These rules are enforceable mechanically to a limited degree (key-term consistency check can catch some uW TW drift; see §11 future-enhancements). Primary discipline is at the drafting step.

---

## 9. Things not automated (still required)

These steps are social, not mechanical, and cannot be built into scripts:

- **Native-speaker naturalness review** — at least one Thai-speaking reviewer reads the chapter aloud and flags anything that sounds stilted or unclear
- **Theological review** — at least one Thai-speaking pastor/theologian reads for doctrinal accuracy
- **Community comprehension testing** — eventually, small groups of target-audience readers answer comprehension questions

For the pilot phase, Ben is the de facto native-speaker + theological reviewer. As more chapters land, add reviewers per chapter.

---

## 10. Copyright boundary (hard limits)

- Our translation is **CC0** (public domain). Anyone can use it, reprint it, modify it, commercialize it.
- We NEVER read or reference copyrighted Thai translations during drafting. Post-draft comparison against copyrighted translations (e.g., "is our Mark 1:1 wildly different from THSV's?") would be standard scholarly practice but is **currently out of scope** for this pipeline because we lack legal access to automated copies. If someone has legitimate access to THSV, they can do manual spot-checks for egregious divergences — but this is not part of the automated pipeline.
- TNBT (CC-BY-SA) is used for structural-only comparison per §8. We do not copy TNBT wording, so we do not inherit CC-BY-SA.
- unfoldingWord resources (CC-BY-SA) can be referenced as a scholarly aid (key-term definitions, translation notes in English). Same rule: don't copy wording; use for understanding.
- Scholarly commentaries (for exegesis) may be consulted but their wording is never copied.

---

## 10b. Review infrastructure (manual / community)

Not everything can be automated. For native-speaker review, theological review, and community comprehension testing, the industry-standard tools are:

- **Paratext** (SIL) — desktop standard for formal translation teams. Free for qualified missionaries via sponsorship. See `docs/REVIEW_TOOLS.md §1`.
- **Scripture Forge** (SIL) — free web-based community review. Integrates with Paratext. `docs/REVIEW_TOOLS.md §2`.
- **unfoldingWord Translation Questions** — comprehension testing for community review. Already integrated source-side (`sources/en_tn/`).

These are **post-draft** tools, not translation aids. They handle the social steps (§9) of the check cadence. See `docs/REVIEW_TOOLS.md` for the full integration roadmap.

---

## 11. Model recommendations

Requirements are version-agnostic — what matters is the tier + context + effort, not the specific version number. Pick the latest available model in each tier.

| Task | Tier & settings | Rationale |
|------|-----------------|-----------|
| Translation (main chat that produces the draft) | **Latest Opus**, 1M context, max effort/thinking | Translation is the highest-stakes step. Hapax legomena, textual variants, theological nuance all benefit from the deepest reasoning. |
| Back-translation check (API calls from `check_back_translation.py`) | **Latest Sonnet** | Simpler task (Thai → English, literal). Sonnet handles it well and saves API spend at per-verse volume. |
| Follow-up review, code edits, running the check scripts | **Latest Sonnet or Haiku** | Faster, cheaper. No reason to burn Opus once the draft is done. |
| Code-only checks (key-term consistency, TNBT structural, OT citation, parallel passages) | No LLM | Pure Python. |

**Claude Code CLI notes (as of 2026-04):**
- Default is Opus 4.7 — fine for translation. Runs with max effort by default unless you drop the effort level.
- `/fast` toggles to Opus 4.6 inside Claude Code: faster output, meaningfully cheaper per token, still Opus-tier reasoning. Use when budget matters and turnaround time is tight. Quality difference vs. 4.7 is small for translation work.
- CLI doesn't support arbitrary model pinning, so "use the latest Opus" is effectively "accept the default."
- Scripts that hit the API directly (e.g., `check_back_translation.py`) should specify the model explicitly — currently `claude-sonnet-4-6` for cost at per-verse volume, bump when a newer Sonnet lands.

**New chat per chapter?** Yes — each chapter gets a fresh Opus chat so:
- The kickoff memory and RULES.md load cleanly
- No context drift from the previous chapter's translation
- The full 1M context is fresh for the new chapter's exegesis
- Parallelizable (you can translate multiple chapters on different days in different chats)

Exception: if rapidly translating sequential chapters in one sitting (e.g., Mark 2–5), staying in the same chat is fine — the glossary.json will have just been written, and Claude's continuity helps with the unfolding narrative.

## 12. Change log

- **v0.1** (2026-04-16) — Initial rules drafted from Mark 1 experience + SIL/Wycliffe/UBS research synthesis. Applies going forward starting with 1 Timothy 3 pilot.
- **v0.2** (2026-04-17) — §11 model recommendations made version-agnostic ("latest Opus / Sonnet" instead of "4.6"). Added Claude Code CLI notes: default is 4.7, `/fast` toggles to 4.6 for budget-sensitive runs.

Future revisions tracked here with date + summary.
