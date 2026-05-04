# Hebrew grammar transfer to Thai (verbal aspect, construct chains, waw-consecutive)

**Scope:** The three Hebrew grammatical phenomena that don't translate cleanly into Thai and need a project-wide policy: (1) verbal aspect (perfect / imperfect / wayyiqtol / weqatal), (2) construct chains (smikhut / chained genitive), and (3) waw-consecutive narrative chains.

**Decided:** 2026-05-04.
**Reference grammars:** Joüon-Muraoka *Grammar of Biblical Hebrew*; Waltke-O'Connor *Introduction to Biblical Hebrew Syntax*; Van der Merwe-Naudé-Kroeze (BHRG) *Biblical Hebrew Reference Grammar*; Runge & Westbury, *Lexham Discourse Hebrew Bible*. (All consult-only via Logos library.)

---

## 1. Hebrew verbal aspect — translation policy

Hebrew verbs are **aspectual**, not strictly tensed. The two finite stems (qatal / yiqtol) plus the four converted forms (wayyiqtol, weqatal, weyiqtol, ptcl + perfect) carry meaning that English/Thai must approximate via tense + adverbial cues.

### 1.1 The basic mapping

| Hebrew form | Default Thai rendering | When this applies |
|---|---|---|
| **Perfect (qatal)** in narrative past — "he killed" | Plain past Thai: **ฆ่า / ได้ฆ่า / ฆ่าแล้ว** | Foreground completed events in narrative; result-state perfects |
| **Imperfect (yiqtol)** in future / habitual — "he will kill / he kills" | **จะฆ่า / ฆ่า** + adverbial as needed | Future, habitual, modal, jussive (depending on context) |
| **Wayyiqtol (וַיִּקְטֹל)** narrative past chain — "and he killed / then he killed" | Plain past Thai: **ก็ฆ่า / และฆ่า / จากนั้นฆ่า** (see §3 below) | Foreground narrative event chain; the workhorse of Hebrew narrative prose |
| **Weqatal (וְקָטַל)** prophetic future / habitual chain — "and he will kill / and he kills" | **และจะฆ่า / และฆ่า** | Prophetic-future chains, habitual chains, instructional chains in Pentateuch law |
| **Imperative** — "kill!" | Plain Thai imperative: **จงฆ่า / ฆ่าเสีย** | |
| **Jussive** (yiqtol with subtle distinction) — "let him kill / may he kill" | **ขอให้ฆ่า / ให้เขาฆ่า / ให้ฆ่า** | Often morphologically identical to imperfect; context decides |
| **Cohortative** (1st-person imperfect with -ah ending) — "let me kill / let us kill" | **ขอให้ฆ่า / ให้ข้าพเจ้าฆ่า / ให้พวกเราฆ่า** | |
| **Infinitive absolute** (intensifying) — "you shall surely die" | **จะตายแน่นอน / ต้องตายแน่ ๆ** + intensifying particle | The intensifier is captured via adverbial/modal Thai, not by doubling the verb |
| **Infinitive construct** in temporal / purpose — "when he killed / in order to kill" | **เมื่อ.../เพื่อ...** + plain verb | Treat as English participle/infinitive |
| **Participle** (active/passive present-state) — "killing / killed" | **กำลังฆ่า / ผู้ฆ่า / ที่ถูกฆ่า** | Often translates as "the one who...", "the X-ing one" |

### 1.2 Aspect not tense — the pitfall

Avoid mechanical mapping "qatal=past, yiqtol=future." Hebrew narrative routinely uses **qatal** for past events that English/Thai would render with present-tense (background description), and uses **yiqtol** for habitual past ("he used to kill" — `יִקְטֹל` with a past-time framing).

The translator's task is to identify the **aspectual function in context**, then choose the Thai tense+adverbial that captures the function — not to produce a mechanical morphology-to-tense match.

### 1.3 Discourse function trumps morphology

Per Runge / BHRG, the Hebrew verbal forms also carry discourse function:

- **Wayyiqtol** → mainline foregrounded narrative event
- **Qatal in non-wayyiqtol position** → background, dischronologized, contrastive
- **Yiqtol in poetry** → often "gnomic" / habitual / general-truth aspect, not future
- **Participle in narrative** → ongoing/coincident action
- **Verbless clause** → identification, classification, location

This drives the connective + subordinator choice in Thai, not just the tense:

- Mainline event → **ก็ / และ / แล้ว** (forward-flowing connective)
- Background → **ตอนนั้น / ส่วน / ในเวลานั้น** (backgrounding adverbial)
- Contrastive → **แต่ / ส่วน** (contrast marker)
- Result → **ดังนั้น / จึง** (result-marker)

### 1.4 Recording aspect in `key_decisions`

When a verse turns on aspectual choice (e.g., Gen 2:5 "had not yet rained" — qatal in pre-action background; Gen 1:2 `הָיְתָה` debated as "was" vs "had become"), document the aspectual reading in the verse's `key_decisions` array.

---

## 2. Construct chains (smikhut / chained genitive)

Hebrew construct chains link nouns in possessive/relational sequences without `of`. Examples:

- `דְּבַר־יהוה` — "word-of-YHWH" → **พระวจนะของพระยาห์เวห์** (default genitive `ของ`) or **พระดำรัสแห่งพระยาห์เวห์** (formal-register `แห่ง`)
- `אִישׁ אֱלֹהִים` — "man-of-God" → **คนของพระเจ้า** (plain) or **บุรุษแห่งพระเจ้า** (elevated)
- `בֵּית אָבִיו` — "house-of-his-father" → **บ้านบิดาของเขา / บ้านของบิดา**

### 2.1 Connective choice

Thai has two main genitive connectives:

- **ของ** — plain possessive; works for everyday relational/possessive constructs.
- **แห่ง** — formal/elevated; works for titular phrases, institutional/divine relations, and where Hebrew construct carries technical-formula weight.

**Default:** `ของ` for plain narrative, biographical, and most everyday constructs. Switch to `แห่ง` when:

- The phrase is a **fixed title** (e.g., `יְהוָה צְבָאוֹת` "YHWH of hosts" → already renders as compound `พระยาห์เวห์จอมโยธา` so the construct is absorbed).
- The phrase is a **liturgical/cultic formula** ("the day of the LORD" — `יוֹם יְהוָה` → already locked at NT side as `วันแห่งองค์พระผู้เป็นเจ้า`; OT will use `วันแห่งพระยาห์เวห์`).
- The phrase introduces an **abstract genitive** ("the holiness of God" — `קְדוּשַׁת אֱלֹהִים` → **ความบริสุทธิ์แห่งพระเจ้า**).

Either is acceptable in most cases; the translator chooses by ear.

### 2.2 Long chains (3+ nouns)

Hebrew can chain 3-4 nouns: `כְּלִי בֵית יהוה` — "vessels-of-house-of-YHWH" → **ภาชนะของพระวิหารของพระยาห์เวห์**. In Thai, repeated `ของ` is acceptable; consider breaking the chain with structure:

- **ภาชนะแห่งพระวิหารของพระยาห์เวห์** (mix `แห่ง` + `ของ` to vary register)
- **ภาชนะที่อยู่ในพระวิหารของพระยาห์เวห์** (paraphrase with a relative clause)

Decision per-verse based on Thai naturalness.

### 2.3 Special construct: superlative (`קֹדֶשׁ הַקֳּדָשִׁים`)

The "X of X-es" form encodes the superlative ("Holy of Holies"). Render as:

- `קֹדֶשׁ הַקֳּדָשִׁים` → **ที่บริสุทธิ์ที่สุด** (superlative-explicit) or **อภิบริสุทธิ์สถาน** (cultic technical term, used in Thai Bible tradition)
- `שִׁיר הַשִּׁירִים` → **บทเพลงแห่งบทเพลง** (preserve the title-form; readers know this as "Song of Songs")

Decide per-construct based on whether the Thai-Bible-reader-tradition has an established term.

---

## 3. Waw-consecutive narrative chains

Hebrew narrative is built on **wayyiqtol** verb-chains: a sequence of `וַיִּקְטֹל` verbs that drive the narrative forward. A typical Hebrew narrative paragraph has 5-15 wayyiqtol verbs in a row.

### 3.1 The translation challenge

Mechanical word-for-word renders this as `และ.../และ.../และ.../และ...` ad infinitum, which is **not natural Thai narrative.** Thai narrative prefers:

- Connective **variation** — mix `และ`, `ก็`, `แล้ว`, `จากนั้น`, `เมื่อ-...ก็`, omitted-connective
- **Asyndeton** — drop the connective in some places where Hebrew uses `ו` (the Hebrew waw is a default narrative continuer; Thai doesn't need a continuer for every verb)
- **Subordination** — convert some Hebrew wayyiqtol forms to Thai temporal subordinate clauses (`เมื่อ...` "when..."), especially when one event is logically the setup for the next

### 3.2 Default rendering policy for wayyiqtol chains

For a typical narrative paragraph:

1. **First wayyiqtol of a paragraph** → fronted Thai connective (`แล้ว / จากนั้น / และ`) or no connective if the previous sentence already established the temporal frame.
2. **Subsequent wayyiqtol verbs** → mix:
   - **`ก็`** (default sequential connective; the closest Thai analog to wayyiqtol's narrative continuer)
   - **`และ`** (when joining two roughly-parallel actions)
   - **No connective** (when the previous sentence's flow is strong enough)
   - **`แล้ว`** (for a new beat/event, signaling step-change)
3. **Wayyiqtol verbs that are *logical setup* for the next event** → consider Thai subordination (`เมื่อ X ทำ ... Y ก็ ...`) to avoid flat parataxis.

The rule of thumb: **don't translate every `ו` with `และ`.** Vary, omit, subordinate. Read the paragraph as Thai prose, not as a 1:1 morphology mirror.

### 3.3 When to keep the chain flat (resist the urge to subordinate)

Some Hebrew narrative deliberately uses repetitive flat parataxis as a stylistic feature (Genesis 1's seven-day structure; the ritual-instruction chains of Leviticus 8-9; Joshua's tribal-allotment chapters). For these:

- Preserve the parallelism. Use **`ก็`** repeatedly. Don't subordinate.
- This *is* what Hebrew is doing rhetorically; flattening it into varied Thai loses the rhetoric.

The translator's judgment per-paragraph.

### 3.4 The opposite trap: weqatal in prophecy

Prophetic literature uses **weqatal** chains (`וְקָטַל` future-perfective sequences) the same way narrative uses wayyiqtol — a connective + verb chain driving prophetic-future events forward. Same translation policy: vary connectives, mix `และ` / `ก็` / `แล้ว` / no-connective, occasionally subordinate.

### 3.5 The infinitive absolute as a chain-anchor

In Pentateuch law and prophecy, an **infinitive absolute** sometimes serves as a stylistic anchor for a chain: `דַּבֵּר אֶל־בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ` "speak to the sons of Israel and (you shall) say." Render the infinitive-absolute + finite-verb pair as a single instructional unit:

- **จงพูดกับวงศ์วานอิสราเอลว่า** ("speak to the family of Israel saying") — coalesces into one Thai imperative-with-introduction.

---

## 4. Stative verbs vs fientive (action) verbs

Hebrew distinguishes:

- **Fientive (action) verbs** — describe an event: `ק־ט־ל` (kill), `ר־א־ה` (see), `ה־ל־ך` (walk).
- **Stative verbs** — describe a state: `ז־ק־ן` (be old), `כ־ב־ד` (be heavy/honored), `ק־ד־שׁ` (be holy).

Stative verbs in Hebrew often translate to **adjective + copula** in Thai:

- `זָקֵן` (he was old) → **เขาแก่ชรา / เขาเป็นชรา**
- `כְּבוֹד יהוה כָּבֵד` (the glory of YHWH was heavy) → **พระสิริของพระยาห์เวห์หนักมาก** (use Thai adjectival construction)
- `קָדוֹשׁ אַתָּה` (you are holy) → **พระองค์ทรงบริสุทธิ์**

Don't force stative Hebrew verbs into Thai action-verb constructions; this misreads the aspectual force.

---

## 5. The verb `הָיָה` (to be)

`הָיָה` is the Hebrew "be" verb. Often translates to Thai zero-copula construction (Thai doesn't always need a copula). Sometimes translates to Thai `เป็น / อยู่ / มี`.

- `וַתְּהִי הָאָרֶץ` (Gen 1:2) — "and the earth was..." → **และโลกก็เป็น...** (with `เป็น` to clarify the predicate state) OR **และโลก...** (zero-copula, with a Thai adjective directly attached: "และโลกร้างว่างเปล่า").

Per-verse judgment based on the predicate type.

The Genesis 1:2 case specifically (`וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ`) has an additional aspectual dimension — `הָיְתָה` here may be aspect-perfective ("was" — describing the state) or have a "had become" force (which would feed gap-theory readings). The pure aspectual reading is "the earth was formless and empty"; document any divergence in `key_decisions` for Gen 1:2 specifically.

---

## 6. Negation

| Hebrew | Use | Thai |
|---|---|---|
| `לֹא` | indicative negation | **ไม่ / ไม่ได้** |
| `אַל` | jussive/prohibitive ("don't!") | **อย่า** |
| `אֵין` | existential negation ("there is no") | **ไม่มี / ปราศจาก** |
| `בְּלִי / בִּלְתִּי` | "without / except" | **เว้นแต่ / ปราศจาก / โดยไม่มี** |

---

## 7. Pronouns + suffixes

Hebrew pronominal suffixes attach to verbs, nouns, and prepositions: `אֲדוֹנִי` (my-Lord), `בְּיָדוֹ` (in-his-hand), `שְׁמַרְתִּיךָ` (I-kept-you).

Thai has no morphological suffix, so each becomes a separate possessive phrase:

- `אֲדוֹנִי` → **องค์เจ้านายของข้าพเจ้า**
- `בְּיָדוֹ` → **ในมือของพระองค์** (if divine subject) or **ในมือของเขา** (human subject)
- `שְׁמַרְתִּיךָ` → **เราได้รักษาเจ้าไว้ / เราดูแลเจ้า** (1st-person verb + 2nd-person object pronoun)

Use the appropriate Thai pronoun register (deferential / royal / plain / contemptuous) based on subject-object relation per `ot_register_policy_2026-05.md`.

---

## When to revisit

- **Phase 6F (Psalms / Job / Wisdom)** — re-read this doc focusing on poetry's distinctive yiqtol-as-gnomic and parallelism interactions with aspect.
- **Phase 6G (Prophets)** — re-read focusing on weqatal-chain handling in prophetic-future material.
- **If a Hebrew construction surfaces during translation that this doc doesn't address** — document in `key_decisions`, then append to this doc when the pattern repeats.
