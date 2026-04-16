# Eremos Translation — Rules

Canonical translation rules for the Eremos Translation. Every chapter must conform to these rules; the check scripts enforce what can be enforced mechanically. Review this file before translating, and treat deviations as requiring explicit justification.

Derived from industry standards used by SIL, Wycliffe, UBS, and unfoldingWord (Larson's meaning-based translation; Beekman & Callow's principles; Paratext's check framework).

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

**Never read during translation**:

- Any copyrighted Thai translation (THSV, NTV, ERV Thai, TNCV)
- TNBT (CC-BY-SA) — see §8 for why
- Any copyrighted commentary

**Why the strictness?** This is what preserves the "independent creation" copyright defense. Our output is produced by independent analysis of the public-domain original languages. No one else's wording gets into our drafting process. After drafting, we *compare* against other translations — but only to identify divergences to justify, never to copy from.

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
- **OT citations or allusions** — identify the OT source and whether the Greek matches MT or LXX
- **Gendered/socially-contested language** — flag interpretive decisions where scholarly opinion is split (e.g., γυναῖκας in 1 Tim 3:11)
- **Technical or cultural terms** that don't have direct Thai equivalents

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
    "key_decisions": [
      { "greek": "<word or phrase>", "thai": "<Thai rendering>", "rationale": "<why this choice>" }
    ],
    "notes": "<textual variants, hapax, cross-references, interpretive calls>"
  }
}
```

Verses with no meaningful interpretive decisions may have empty `key_decisions: []` and `notes: null`, but this must be the exception, not the norm. If a verse has zero decisions, consider whether something subtle is being missed.

---

## 7. Post-draft checks (mandatory before commit)

Before any chapter is committed to `output/translations/`, the **check cadence** runs:

1. **Back-translation check** — `scripts/check_back_translation.py <book> <chapter>` — AI translates our Thai back to English, diffs against BSB, flags divergences not explained in our notes.
2. **Key-term consistency audit** — `scripts/check_key_term_consistency.py` — scans all translations, reports per-lemma rendering variance, flags undocumented divergence.
3. **TNBT structural comparison** — `scripts/check_against_tnbt.py <book> <chapter>` — verse-by-verse structural comparison against Thai TNBT (CC-BY-SA). Vocabulary differences expected (TNBT uses Buddhist register); structural differences (e.g., number of sentences, missing clauses) are the signal.
4. **OT citation check** — `scripts/check_ot_citations.py <book> <chapter>` — flags NT verses that quote OT; notes whether Greek matches LXX or MT.
5. **Parallel-passage check** — `scripts/check_parallel_passages.py` — for synoptic parallels, flags divergent renderings of the same saying across books (applicable once we have multiple gospels).

The orchestrator `scripts/run_checks.py <book> <chapter>` runs all applicable checks and produces `output/check_reports/<book>_<NN>_checks.md`.

**Ship criterion**: zero unresolved flags. A flag is "resolved" when either (a) the note is added to the verse, or (b) a decision document in `docs/translator_decisions/` records why the flag is acceptable as-is.

---

## 8. TNBT (CC-BY-SA) usage policy

The Thai New Buddhist Translation (github.com/pepa65/TNBT) is CC-BY-SA 4.0 licensed. It is a legitimate open-source Thai NT and a useful **structural reference**. But:

- **Never read during translation.** TNBT's specific Thai wording must not influence our drafting. (If we derive wording from TNBT, our output inherits CC-BY-SA and we lose CC0.)
- **Only compared after drafting**, mechanically, by the check script.
- **Vocabulary divergence is expected.** TNBT deliberately uses Buddhist register (พระศรีอาริย์ for Messiah, นิพพาน for eternal life, พิธีมุดน้ำ for baptism, พรหมวิหารสี่ for love). Our project uses standard Thai Christian vocabulary. Divergences from TNBT on vocabulary do **not** indicate an error in our translation — they indicate a deliberate choice of register.
- **Use TNBT divergences as**: a prompt to spot-check whether we've understood the passage correctly at the sentence/structural level. If TNBT's sentence count diverges from ours meaningfully, investigate. If TNBT renders a verb we rendered as a noun, investigate.

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

## 11. Change log

- **v0.1** (2026-04-16) — Initial rules drafted from Mark 1 experience + SIL/Wycliffe/UBS research synthesis. Applies going forward starting with 1 Timothy 3 pilot.

Future revisions tracked here with date + summary.
