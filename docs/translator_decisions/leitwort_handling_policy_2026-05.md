# Leitwort handling — corpus-consistency vs discourse-function priority hierarchy

**Scope:** When does Hebrew lexical recurrence (Leitwort) survive in Thai translation, and when does it yield to target-language naturalness? Establishes the project's hierarchy between (a) cross-corpus lemma-consistency priorities and (b) verse-level discourse-function priorities. Triggered by the Jonah end-of-book audit cross-AI review (2026-05-09), where ChatGPT's §Z meta-observation surfaced the need for an explicit umbrella policy.

**Decided:** 2026-05-09 (Ben + cross-AI review).

**Companion docs:** `chesed_covenant_love_2026-05.md` (case study — lemma-consistency wins), `hebrew_idioms_and_metaphor_2026-05.md`, `divine_names_table_2026-05.md`.

---

## 1. The two competing priorities

Hebrew narrative and poetry frequently uses **Leitwörter** — keywords that recur deliberately across a passage, chapter, or book to carry theological/literary weight. Examples encountered already:

- **ירד** ("go down") — Jonah's descent-to-death motif (1:3 × 2 + 1:5 + 2:6).
- **טוּל** ("hurl") — Jonah 1's chain (God hurls wind v.4, sailors hurl cargo v.5, Jonah asks to be hurled v.12, sailors hurl Jonah v.15).
- **גָּדוֹל** ("great") — Jonah's "great" thread across all 4 chapters (great city, great storm, great fear, great evil, great joy).
- **מָנָה** ("appoint") — Jonah's 4-fold divine-appointment (fish 2:1, plant 4:6, worm 4:7, wind 4:8).
- **שׁוּב** ("turn, return, repent") — Jonah 3's covenant-repentance vocabulary (3:8 × 2, 3:9, 3:10).
- **רָעָה** ("evil/disaster") — Jonah's evil-thread across 4 chapters (Nineveh's evil, Ninevites' evil ways, the disaster God didn't bring, Jonah's "evil" perception).

Two project priorities pull in opposite directions when Leitwörter cross between Hebrew and Thai:

### 1.1 Lemma-consistency priority (cross-corpus traceability)

- **Goal:** Thai readers can trace the same Hebrew lemma across the corpus by recognizing identical Thai vocabulary.
- **Enforces:** Use the same Thai word/phrase for every occurrence of the Hebrew lemma (within a book, across the OT, across testaments where applicable).
- **Wins when:** the lemma is theologically loaded with cross-corpus significance (chesed, YHWH, key character names, foundational covenant-vocabulary).
- **Risk:** rigid uniformity may produce un-Thai sentences when Hebrew lemmas violate Thai semantic-collocation rules.

### 1.2 Discourse-function priority (target-language naturalness, narrative rhetoric)

- **Goal:** the Thai sentence reads naturally and conveys the verse's discourse-function (irony, ambiguity, narrative pace, rhetorical force).
- **Enforces:** Allow lexical variation when target-language collocation, idiomatic usage, or rhetorical effect demands it.
- **Wins when:** the lexical recurrence is a Hebrew-specific stylistic feature that would distract or distort in Thai.
- **Risk:** unchecked variation breaks cross-corpus lemma-traceability and obscures Hebrew literary architecture.

---

## 2. The decision hierarchy

When a Leitwort decision arises, apply these rules in order:

### Rule 1 — If the lemma is on the **corpus-lock list**, lemma-consistency wins.

The corpus-lock list (current as of 2026-05-09):

| Lemma | Thai lock | Decision doc |
|---|---|---|
| יהוה (Tetragrammaton) | องค์พระผู้เป็นเจ้า | `divine_names_table_2026-05.md` |
| אֱלֹהִים (Elohim, of true God) | พระเจ้า | `divine_names_table_2026-05.md` |
| חֶסֶד (chesed) | ความรักมั่นคง | `chesed_covenant_love_2026-05.md` |
| מָנָה (manah, divine-appointment) | ทรงจัดเตรียม | `manah_divine_appointment_2026-05.md` |
| נָחַם (nicham, divine-relenting) | ทรงเปลี่ยนพระทัย | `nicham_divine_relenting_2026-05.md` |
| Exod 34:6–7 attribute formula | (full identical phrase) | `exod_34_attribute_formula_2026-05.md` |
| ירד (yarad) — Jonah's down-motif | ลง- (preserved at every occurrence in Jonah 1–2) | (book-specific lock; book-tagged) |

**Add lemmas to this list as they emerge.** Each new entry requires a decision doc.

### Rule 2 — If the lemma is a **book-specific Leitwort** (not corpus-locked), preserve it within the book where Thai allows.

Examples:
- Jonah's טוּל ("hurl") chain — preserved as โยน in 1:5, 1:12, 1:15 (the human/sailor actions). At 1:4 (God hurls wind onto sea), Thai semantic-collocation demands ทรงบันดาลให้...พัดมา ('caused...to blow') because โยนลม would be un-Thai (wind isn't an object that can be "hurled" in Thai). The Leitwort-link is partially preserved (3 of 4 occurrences) and the 1:4 exception is documented in the verse's `key_decisions` AND in this policy doc as a worked example.
- Jonah's גָּדוֹל ("great") thread — preserved as ใหญ่ at every occurrence of "great city" (1:2, 3:2, 3:3, 4:11) and ยิ่ง / ยิ่งใหญ่ for the cognate-accusative emphatics (great fear 1:10, 16; great evil 4:1; great joy 4:6).

### Rule 3 — If the lemma is a **Hebrew rhetorical feature** that violates target-language semantic-collocation rules, discourse-function wins.

Examples:
- Hebrew cognate-accusative emphasis (verb + cognate-noun — "feared a great fear," "rejoiced a great rejoicing") → use Thai adverbial intensification (อย่างยิ่ง) instead of verb-doubling (verb-doubling sounds clumsy in Thai).
- Hebrew anthropomorphic body-part-as-emotion (אַף = "nose" = "anger") → use the Thai abstract emotion-word (พระพิโรธ) when the literal would be opaque to Thai readers.
- Hebrew personification of natural elements (ship "thinks" of breaking) → flatten to natural Thai (เกือบจะแตก) when literal would be mock-poetic.

### Rule 4 — When in doubt, **document in `key_decisions`** with both options + the rationale for the choice.

The verse's `key_decisions` rationale is the durable record. Even if the choice is later revised, the rationale captures the trade-off considered. This makes future audits transparent.

---

## 3. The Jonah audit-tested cases (2026-05-09)

The Jonah end-of-book audit (cross-AI review) tested this hierarchy on 5 cases. Outcomes:

| Case | Hebrew lemma | Decision | Rule applied |
|---|---|---|---|
| חֶסֶד (Jonah 2:9, 4:2) | חֶסֶד | LEMMA-CONSISTENCY wins → ความรักมั่นคง corpus-lock | Rule 1 |
| טוּל (Jonah 1:4) | טוּל | DISCOURSE-FUNCTION wins → ทรงบันดาลให้...พัดมา (Thai semantic-collocation) | Rule 3 |
| Captain's אֱלֹהִים (Jonah 1:6) | הָאֱלֹהִים | DISCOURSE-FUNCTION wins → เทพเจ้า (preserves 3-step conversion arc; not yet covenant-name) | Rule 3 |
| 4:11 right/left ambiguity | יָדַע בֵּין־יְמִינוֹ לִשְׂמֹאלוֹ | DISCOURSE-FUNCTION (preserve ambiguity) → literal main text + prominent footnote | Rule 3 |
| נָחַם (Jonah 3:9, 3:10, 4:2) | נָחַם | LEMMA-CONSISTENCY wins → ทรงเปลี่ยนพระทัย corpus-lock | Rule 1 |

The hierarchy is robust: when the lemma carries cross-corpus theological weight, Rule 1 wins; when the lemma's instance violates target-language naturalness or serves a discourse-specific function (irony preservation, conversion arc), Rule 3 wins.

---

## 4. Anti-patterns to avoid

### 4.1 Adjectival-expansion drift

**Anti-pattern:** Adding qualifying adjectives to a corpus-locked lemma to capture context-specific nuance, e.g., `พระเมตตาเชิงพันธสัญญา` ("covenantal mercy") instead of the locked `ความรักมั่นคง`.

**Why bad:** front-loads interpretation into the lexical choice; breaks lemma-recurrence so cross-corpus tracing fails.

**Right fix:** keep the corpus lock. If contextual nuance is needed, add to `thai_summary` or `key_decisions`, not to the main text.

### 4.2 Premature register-elevation

**Anti-pattern:** Using the highest-register Thai term (พระเจ้า, องค์พระผู้เป็นเจ้า) for a character's pre-conversion deity-reference.

**Why bad:** flattens conversion narratives; the reader misses the theological progression.

**Right fix:** Use a lower-register pre-conversion term (พระของตน, เทพเจ้า) and reserve the high-register term for the conversion-climax.

### 4.3 Lexical normalization across stylistic-emphasis constructions

**Anti-pattern:** Forcing the same Thai construction for cognate-accusative emphasis, even when the contexts vary in tone.

**Why bad:** Hebrew cognate-accusative is uniformly emphatic; Thai needs adverbial intensification that varies by context (terror vs. awe vs. joy).

**Right fix:** Preserve the emphatic-intensification semantic but allow the Thai construction to vary (อย่างยิ่ง / มาก / สุดใจ / etc.).

---

## 5. When to add a lemma to the corpus-lock list

A lemma earns corpus-lock status when ONE of:

- It is theologically foundational (divine names, covenant-words, sacrificial vocabulary).
- It appears in widely-recited liturgical/psalmic formulas (Exod 34, Aaronic blessing, Shema, etc.).
- It carries an apologetic/ecumenical sensitivity (Tetragrammaton convention, divine-anthropomorphism).
- It threads through ≥3 OT books with shared theological function.

A book-specific Leitwort (Jonah's ירד, גָּדוֹל, etc.) does **not** earn corpus-lock — it gets a book-tagged note in the relevant chapter `notes` field. The same word in another book may legitimately have a different rendering if the literary function differs.

---

## 6. Implementation: check-script discipline

`check_key_term_consistency.py` enforces Rule 1 lemma-locks. The check should:

- Fail HARD on any unauthorized variation of a corpus-locked lemma's Thai rendering.
- Allow an `lemma-contextual-variant` excuse-keyword in `key_decisions` rationale for documented exceptions (per Rule 4).
- Track each lemma-lock's Thai rendering in `data/lemma_locks.json` (canonical mapping).

`check_phrase_consistency.py` enforces multi-word phrase locks (e.g., the Exod 34 attribute formula).

---

## 7. Genesis locking-precedents sub-section (added 2026-05-12)

Added per Genesis end-of-book audit §K. Four major Leitwort-cases exercised across Genesis form locking-precedents for the policy:

### 7.1 שֶׁבַע / שָׁבוּעַ — Beersheba dual-wordplay (21:31 + 26:33)

The place-name **Beersheba** carries a dual etymology in Genesis: שֶׁבַע ("seven") in 21:28–31 (Abraham's seven ewes) + שָׁבוּעַ ("oath") in 21:23–32 + 26:33 (oath-cutting). The Hebrew text plays both senses against each other at the place-name's introduction. Eremos transliterates the name **เบเอร์เชบา** (transliteration) and surfaces the dual etymology in verse-level `key_decisions` for 21:31 + 26:33.

**Rule applied:** Rule 1 (corpus-lock the transliteration) + Rule 3 (preserve discourse-function: the dual-wordplay belongs in the KD layer, not the surface).

### 7.2 יָרַד / עָלָה — Joseph-cycle down/up trajectory

The Joseph cycle uses the lemma-pair יָרַד ("go down") + עָלָה ("go up") as a structuring leitwort across chs 37–50:
- Joseph **down** to Egypt: 37:25, 39:1
- Sons of Jacob **down** to Egypt for food: 42:2, 42:3, 43:15
- Israel **up** out of Egypt prefigured: 50:25 (Joseph's last words)

Eremos preserves the **ลงไป / ขึ้นไป** lemma-pair consistently across these verses — readers tracking the geographic-trajectory leitwort can recognize it. This anchors the Exodus theme that compounds in the Pentateuch.

**Rule applied:** Rule 1 (lemma-lock the directional verb-pair across the Joseph cycle).

### 7.3 עֵזֶר / עֶזְרָה — the "help" word-family

The עֵזֶר lemma anchors two Genesis-marker passages:
- **Gen 2:18** עֵזֶר כְּנֶגְדּוֹ ("a helper-corresponding-to-him") — the woman as Adam's matched-help
- **Gen 49:25** מֵאֵל אָבִיךָ וְיַעְזְרֶךָּ ("from the God of your father, who will help you") — Jacob's blessing on Joseph

The same lemma threads through Pss 33:20, 70:5, 121:1–2, 124:8 (forward; "our help is in the name of YHWH"). Eremos uses **ผู้ช่วย / ความช่วยเหลือ** consistently for עֵזֶר when YHWH-anchored; when Gen 2:18's woman-as-helper is rendered, the same root-lemma carries the Adam-to-divine help-trajectory.

**Rule applied:** Rule 1 (lemma-recurrence across thematic threads).

### 7.4 כֶּסֶף — silver-recursion in the Joseph cycle

The lemma כֶּסֶף ("silver") + the cognate verb **covet/desire** thread through the Joseph cycle as a moral-economy leitwort:
- 31:30 — Laban's teraphim / covet-silver (כָּסַף)
- 37:28 — Joseph sold for 20 pieces of silver
- 42:25 / 43:15 / 43:22 — silver returned in the brothers' sacks
- 44:2 — silver cup planted in Benjamin's sack

Eremos uses **เงิน** ("silver/money") consistently — readers can recognize the silver-as-moral-mirror leitwort across the cycle. The Tamar→Judah silver-payment context (38:18) also threads in.

**Rule applied:** Rule 1 (lemma-lock) + Rule 2 (preserve the moral-economy discourse-function the leitwort enables).

---

## 8. Change log

- **v0.2** (2026-05-12) — Genesis locking-precedents sub-section added per Genesis end-of-book audit §K (Beersheba dual-wordplay, Joseph down/up trajectory, ezer help-family, silver-recursion).
- **v0.1** (2026-05-09) — Initial policy, triggered by Jonah end-of-book audit cross-AI review (ChatGPT §Z meta-observation). Establishes the lemma-consistency vs discourse-function decision hierarchy as a four-rule framework.
