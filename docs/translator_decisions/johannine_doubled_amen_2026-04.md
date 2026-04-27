# Johannine doubled-amen (`ἀμὴν ἀμὴν λέγω ὑμῖν`) → อาเมน อาเมน เราบอกแก่พวกท่านว่า

**Scope:** The Johannine doubled-amen formula `ἀμὴν ἀμὴν λέγω ὑμῖν`. Appears 25× in John (only NT book with the doubled form): 1:51, 3:3, 3:5, 3:11, 5:19, 5:24, 5:25, 6:26, 6:32, 6:47, 6:53, 8:34, 8:51, 8:58, 10:1, 10:7, 12:24, 13:16, 13:20, 13:21, 13:38, 14:12, 16:20, 16:23, 21:18.

**Decided:** 2026-04-27 during John 1 spot-review. Flagged by Gemini 2.5 Pro external review (per `docs/CHAPTER_REVIEW_PROMPT.md` workflow): the prior draft `เราบอกความจริง ความจริงแก่พวกท่านว่า` literally repeats the abstract noun `ความจริง` back-to-back, which reads as a stutter or typographical error in Thai (unlike English "truly, truly" which works as solemn emphasis).

**Evidence base:** John 1:51 (first occurrence) — the lock is set at this verse to prevent drift across the remaining 24 occurrences.

---

## The rule

**`ἀμὴν ἀμὴν λέγω ὑμῖν` → "อาเมน อาเมน เราบอกแก่พวกท่านว่า"** — uniform across all 25 Johannine occurrences.

Treat `ἀμήν` as an **Aramaic embed**, consistent with the existing Aramaic-embed policy in `aramaic_transliterations_2026-04.md` (Talitha cumi, Ephphatha, Abba, etc.). The Greek `ἀμήν` is already a preserved Hebrew/Aramaic word (`אָמֵן`) — Mark/Matthew/Luke/John didn't translate it into Greek; they preserved the Semitic word. We do the same in Thai.

## Why "อาเมน อาเมน" and not literal Thai repetition

**Argument for "อาเมน อาเมน" (chosen):**

- **Consistent with existing Aramaic-embed policy.** `aramaic_transliterations_2026-04.md` already establishes that Aramaic words Mark embeds get Thai-script transliteration AND a Greek translation alongside. ἀμήν is the same kind of Semitic-word-preserved-by-the-evangelist; the same policy applies.
- **Preserves the doubling visually.** The reader sees that Jesus is using a marked formula, the same way English readers see "truly, truly."
- **"อาเมน" is already a recognizable word in Thai Christianity.** Thai Christians say it after prayer; the word is liturgically familiar and carries the same solemn-affirmation weight it does in Greek/Hebrew.
- **Scales gracefully across all 25 verses.** Once the reader sees the formula at 1:51, every subsequent occurrence reads as "this is John's signature solemn-pronouncement marker," not as a stutter.
- **Most exegetically faithful.** John (and Greek tradition before him) preserved the Hebrew/Aramaic word rather than translating it precisely because the *liturgical force* survives transliteration where it would be lost in translation. We preserve the same trade-off.

**Counter-argument (literal Thai repetition `เราบอกความจริง ความจริง...`):**

- Visually preserves the doubling without introducing a foreign word.
- BSB / ESV / KJV English do this ("truly, truly").
- **But:** Thai abstract nouns don't intensify by repetition the way Hebrew nouns or English emphatic adverbs do. `ความจริง ความจริง` reads as a stutter — Gemini's flag at 1:51 is correct. This is a Thai-target language constraint that English translations don't share.

**Why not the NIV-style adverbial collapse (`เราบอกความจริงอย่างแน่แท้แก่พวกท่านว่า`)?**

- Loses the visual doubling that distinguishes Johannine-doubled from Synoptic-single. Across 25 verses, the reader never sees that John has a different solemn-pronouncement formula from Mark/Matthew/Luke. Flattens a Johannine signature.

**Why not the bridge form (`เราบอกความจริง ความจริงก็คือว่า ...`)?**

- Better than literal repetition but still uses `ความจริง` twice in sequence. Cleaner Thai but still slightly awkward; loses the marker-like quality the Aramaic embed provides.

## Distinction from the Synoptic single-amen lock

| Greek | Thai | Locked in |
|---|---|---|
| ἀμὴν λέγω ὑμῖν (single, Mark/Matthew/Luke) | เราบอกความจริงแก่พวกท่าน(ว่า) | `amen_saying_formula_2026-04.md` |
| ἀμὴν ἀμὴν λέγω ὑμῖν (doubled, John only) | อาเมน อาเมน เราบอกแก่พวกท่านว่า | this doc |

The two locks are deliberately distinct. The Synoptic single-amen is rendered with `ความจริง` because the single-occurrence solemn-marker doesn't trip the Thai-stutter problem. The Johannine doubled-amen requires a different strategy because Thai abstract-noun repetition fails as an intensifier.

## Forward implications

This lock determines all 24 remaining doubled-amens in John (1:51 already shipped at v.51 of John 1; 3:3 next when John 3 ships).

## Alternatives considered

- **Literal repetition** (`เราบอกความจริง ความจริงแก่พวกท่านว่า`) — rejected: reads as stutter in Thai.
- **Adverbial collapse, NIV-style** (`เราบอกความจริงอย่างแน่แท้แก่พวกท่านว่า`) — rejected: flattens the Johannine signature.
- **Bridge form** (`เราบอกความจริง ความจริงก็คือว่า ...`) — rejected: still uses `ความจริง` twice; not as clean as the Aramaic embed.
- **Doubled certainty marker** (`เราบอกความจริงแท้จริงแก่พวกท่านว่า`) — rejected: blends two Thai certainty words; loses the visual doubling.
- **Aramaic embed** (`อาเมน อาเมน เราบอกแก่พวกท่านว่า`) — chosen.

## When to revisit

- If native-Thai-speaker review at John end-of-book reports that "อาเมน อาเมน" reads as foreign or breaks reading flow more than expected. (Anticipated outcome: it reads as deliberately marked, which is the intent.)
- If the Synoptic and Johannine forms ever appear together in a citation context (e.g., a NT-OT citation that quotes a Synoptic amen-saying inside a Johannine document) — handle that singular case at the verse level.

## Cross-reference

- `docs/translator_decisions/amen_saying_formula_2026-04.md` — Synoptic single-amen lock (the pair this distinguishes from).
- `docs/translator_decisions/aramaic_transliterations_2026-04.md` — the Aramaic-embed policy this lock is consistent with.
- John 1:51 — first occurrence; v.51 of `output/translations/john_01.json` is the first verse to apply this lock.
- Original flag: Gemini 2.5 Pro external review of John 1, 2026-04-27 (per `docs/CHAPTER_REVIEW_PROMPT.md` workflow).
