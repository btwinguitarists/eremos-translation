# Luke metadata drift — remediation notes (2026-04-21)

This is a plain-language record of a metadata-quality issue found in the Luke 13 and Luke 14 translations, along with a couple of older artifacts in Mark and Matthew. It describes what the issue looked like, what was fixed, what didn't change, and what a human reviewer should look for.

**Nothing in the Thai translation text itself was changed.** This remediation is entirely about the structured metadata that sits alongside each verse — the `key_decisions` field in the translation JSON.

---

## What was wrong, in one paragraph

In the Luke 13 and Luke 14 translations, five entries in the `key_decisions` metadata had their `greek` field filled with Thai characters or a fabricated Greek-looking string instead of the actual Greek source word. The Thai translations of those verses were fine; the scholarly notes were fine. What broke was a structured field that's supposed to quote the Greek source of each translation decision. Three similar older artifacts existed in Mark 1, Mark 8, and Matthew 5. All eight have been corrected.

---

## What `key_decisions` is supposed to contain

For every verse in `output/translations/<book>_<chapter>.json`, the `translation.key_decisions` field is a list. Each list item documents one translation choice the translator made. It has three fields:

```
{
  "greek":     "<the Greek source phrase as it appears in the verse>",
  "thai":      "<the Thai rendering we chose>",
  "rationale": "<why we chose that rendering>"
}
```

The `greek` field is meant to hold **actual Greek text from the verse**. A reviewer reading a translation decision should be able to look at the `greek` field and find that exact string (allowing for differences in accent or capitalization) in the verse's source text shown above it.

Legitimate exceptions: when the rationale discusses a textual variant ("some manuscripts read X"), a classical usage, an LXX reading, a hapax etymology, or a morphological abbreviation ("2sg", "aor. ind."), the `greek` field may cite a word that isn't in the verse. The current automated check `scripts/check_greek_field_integrity.py` excuses entries whose rationale includes words like "variant", "mss", "manuscript", "witness", "classical", "lxx", "hapax", "morphological", etc.

---

## What was drifted in the shipped files

### Class 1 — Thai characters in the `greek` field

Examples from before the fix:

- **Mark 1:10** — `"greek": "εἶดεν + ทอดพระเนตร"` (mixed Greek and Thai; the Thai `ทอดพระเนตร` belongs in the `thai` field)
- **Mark 8:2** — `"greek": "Self-reference 'เรา'"` (Thai pronoun; no Greek at all)
- **Matthew 5:29** — `"greek": "ὁ ὀφθαλμός σου ὁ δεξιὸς σκανดαλίζει σε"` (**one** character substitution: the Thai letter `ด` U+0E14 replaced the Greek `δ` U+03B4 inside the word `σκανδαλίζει`; almost invisible to the eye)
- **Luke 13:12** — `"greek": "เจ้า"` (Thai 2nd-person pronoun)
- **Luke 13:14** — `"greek": "พวกเจ้า"`
- **Luke 13:15** — `"greek": "พวกท่าน"`
- **Luke 13:31** — `"greek": "ท่าน"`

None of these are fabricated scholarship; they're schema violations — putting Thai content into a slot reserved for Greek.

### Class 2 — Fabricated Greek-shaped strings

- **Luke 14:1** — `"greek": "ἐสδέจ"` (not a real Greek word; it's a pseudo-Greek transliteration of the Thai royal verb `เสด็จ`, with one Thai character hiding in it)

This is a genuine scholarly-metadata hallucination — the model invented a Greek source for a Thai editorial decision.

---

## What a reviewer can actually check

A human reviewer does not need to re-translate anything to do a useful review. For each chapter, skim the translation JSON and ask, for each `key_decisions` entry:

1. **Does the `greek` field look like Greek?** Not just "has some Greek letters in it" — but, is every character Greek? If you see Thai vowel marks (the little curlicues above and below letters in Thai script) or any Thai character, flag it.
2. **Does the `greek` field text actually appear in the verse's `greek` source above?** Ignoring case and accent marks (Greek has acute/grave/circumflex variants that don't change the word). If the `greek` field token isn't there, the rationale should explain why (manuscript variant, LXX reading, classical usage, cross-reference to another verse).
3. **Does the `thai` field match what's in the main `thai` translation of the verse?** If the main translation uses `พวกท่านทุกคน` but the key_decisions entry says `thai: "พวกท่านแต่ละคน"`, that's a mismatch worth flagging.
4. **Does the `rationale` say something specific to the choice?** A rationale of "Standard glossary term" is fine for truly standard words. A rationale that sounds plausible but doesn't actually explain the decision — especially with phrases that claim pipeline actions happened ("Added to nt_ot_citations.json") — should be checked against the referenced file.

**Most entries will look fine.** In 2,061 `key_decisions` entries across 14 Luke chapters, only 5 were affected. The goal of a review pass isn't to catch everything — it's to notice if there's a pattern.

---

## What was fixed, and how

Eight entries cleaned. No verse translations, summaries, or notes were edited.

| Verse | Before (broken `greek` field) | After |
|---|---|---|
| Mark 1:10 | `εἶδεν + ทอดพระเนตร` | `εἶδεν` |
| Mark 8:2 | `Self-reference 'เรา'` | (entry merged into the existing `σπλαγχνίζομαι` entry's rationale) |
| Matthew 5:29 | `…σκανดαλίζει σε` (with Thai `ด`) | `…σκανδαλίζει σε` (proper Greek `δ`) |
| Luke 13:12 | `เจ้า` | (entry merged into the existing `ἀπολέλυσαι τῆς ἀσθενείας σου` rationale) |
| Luke 13:14 | `พวกเจ้า` | (entry merged into the existing `ἐρχόμενοι θεραπεύεσθε` rationale) |
| Luke 13:15 | `พวกท่าน` | `ἕκαστος ὑμῶν` (the actual Greek 2pl pronoun in the verse) |
| Luke 13:31 | `ท่าน` | (entry merged into the `Ἡρῴδης θέλει σε ἀποκτεῖναι` rationale, since `σε` is the Greek pronoun) |
| Luke 14:1 | `ἐสδέจ` (gibberish) | `ἐλθεῖν` (the actual Greek infinitive in the verse) |

After the fixes, the check script `check_greek_field_integrity.py --all` reports zero hard fails across every translated chapter of Mark, Matthew, and Luke.

---

## How this could have happened

All eight flagged entries trace to a small set of known-bad behaviors the Claude Opus model has occasionally exhibited, especially during long, high-volume translation sessions:

1. **Character-script mixing.** The Greek letter δ (U+03B4) and the Thai letter ด (U+0E14) look similar on screen and in certain fonts are almost identical. The model sometimes silently substitutes one for the other.
2. **Fabricated "Greek roots."** When the model wants to document a Thai editorial choice (like a register decision or an honorific), and the Greek source doesn't have an explicit word to cite, the model has sometimes invented a pseudo-Greek token that looks like it justifies the decision.
3. **Schema drift under context pressure.** In long sessions with many chapters of context, the schema constraint "the `greek` field contains Greek" weakens. The model starts using the field as a general-purpose topic label (Thai pronouns, ASCII categories like "Self-reference", etc.).

The project already has one check (`check_claim_consistency.py`) targeting a related issue from the Opus 4.6→4.7 update (see `docs/CITATION_DB_REMEDIATION_2026-04-17.md`). The new `check_greek_field_integrity.py` closes the schema-drift gap that claim-consistency didn't cover.

---

## What changed in the repo

- **Fixes**: 8 `key_decisions` entries across `output/translations/mark_01.json`, `mark_08.json`, `matthew_05.json`, `luke_13.json`, `luke_14.json`.
- **New check**: `scripts/check_greek_field_integrity.py` — standalone script, also wired into `scripts/run_checks.py` as check #8/8.
- **RULES.md §5**: added a one-line rule on what may appear in `key_decisions[].greek`.
- **This doc**: the file you're reading.

## What was not changed

- No Thai translations.
- No `thai_summary` fields.
- No `notes` fields.
- No glossary entries.
- No OT citation DB entries.
- No chapter back-translations.

The cleanup is strictly at the metadata-apparatus layer.

---

## For the reviewer handoff

If you're a Thai-speaking reviewer being asked to look at one or more shipped chapters: the Thai translation is the part you're qualified to judge best. Read it aloud. Flag anything that sounds stilted, unnatural, or doctrinally off. Don't worry about the `key_decisions` metadata unless you happen to notice something — that's now covered by the automated check. Your attention is better spent on the target-language text itself.

If a native-speaker reviewer finds a problem in the Thai text, write it up as a verse reference + one-sentence description of what's wrong (e.g., `Luke 14:7 — "ทรงสังเกต" sounds like someone noticing dust, not noticing guests`). That gets entered as a GitHub issue or flagged in the next pipeline session.
