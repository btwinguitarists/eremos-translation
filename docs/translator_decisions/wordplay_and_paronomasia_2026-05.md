# Wordplay, paronomasia, and onomatopoeia in the OT

**Scope:** The technique of preserving Hebrew sound-play, name-etymology, alliteration, and other phonologically-motivated rhetoric in Thai translation. Not all wordplay is preserved — the policy distinguishes when to footnote vs. when the meaning hinges on the play and demands a creative Thai rendering.

**Decided:** 2026-05-04.
**Pattern reference:** NT side already has `johannine_doubled_amen_2026-04.md` and the various Aramaic-transliteration patterns; OT extends the same philosophy.

---

## 1. The four wordplay strata

OT wordplay falls into four strata, each with a different translation policy.

### Stratum 1 — Etymological name-play (the meaning of a name is the rhetorical point)

Examples:
- **Adam / earth** — `אָדָם` ↔ `אֲדָמָה` (Gen 2:7, 3:19)
- **Eve / living** — `חַוָּה` ↔ `חַי` (Gen 3:20)
- **Cain / acquired** — `קַיִן` ↔ `קָנִיתִי` (Gen 4:1)
- **Babel / confused** — `בָּבֶל` ↔ `בָּלַל` (Gen 11:9)
- **Abraham / father of multitudes** — `אַבְרָהָם` from `אַב-הֲמוֹן` (Gen 17:5)
- **Isaac / he laughs** — `יִצְחָק` from `צָחַק` (Gen 17:17, 18:12, 21:6)
- **Jacob / heel-grasper / supplanter** — `יַעֲקֹב` from `עָקֵב` (Gen 25:26, 27:36)
- **Israel / wrestles with God** — `יִשְׂרָאֵל` from `שָׂרָה אֶל / עִם־אֱלֹהִים` (Gen 32:28)
- **Moses / drawn out** — `מֹשֶׁה` from `מְשִׁיתִהוּ` (Ex 2:10)
- **Esau / hairy / Edom / red** — `עֵשָׂו` ↔ `שֵׂעָר`, ↔ `אֲדֹם` (Gen 25:25, 30; 36:1)
- **Bethel / house of God** — `בֵּית־אֵל` (Gen 28:19)
- **Beer-lahai-roi / well of the Living-One who sees me** — `בְּאֵר־לַחַי־רֹאִי` (Gen 16:14)
- **Naomi / Mara** — `נָעֳמִי` ("pleasant") → `מָרָא` ("bitter") (Ruth 1:20)
- **Ben-oni / Benjamin** — Rachel's death-naming vs. Jacob's renaming (Gen 35:18)
- **Onesimus** — only NT but parallel pattern (Philemon)

**Policy: preserve via footnote.** Thai readers cannot recover the Hebrew etymology from transliterated names. The verse's `key_decisions` entry + `thai_summary` cross-reference explains the wordplay.

Default rendering pattern:
- Main text: transliterate the name per `proper_names_and_transliteration_2026-05.md`.
- `thai_summary`: capture the wordplay in plain language.

**Sample for Gen 3:20** (`חַוָּה` / "living"):
- Main: **อาดามจึงเรียกชื่อภรรยาของเขาว่าเอวา เพราะนางเป็นมารดาของผู้มีชีวิตทั้งปวง**
- `thai_summary`: "ชื่อ 'เอวา' (חַוָּה) ในภาษาฮีบรูเชื่อมโยงกับคำว่า 'ผู้มีชีวิต' (חַי) — เป็นการเล่นเสียงและความหมายเพื่อสื่อถึงบทบาทของนางในฐานะมารดาของมนุษยชาติ"

**Sample for Ruth 1:20** (Naomi → Mara):
- Main: **อย่าเรียกข้าพเจ้านาโอมีเลย แต่จงเรียกข้าพเจ้ามารา เพราะองค์ผู้ทรงมหิทธิฤทธิ์ทรงทำให้ข้าพเจ้าขมขื่นยิ่งนัก**
- `thai_summary` (or footer note): "นาโอมี (נָעֳמִי) แปลว่า 'หวานชื่น' มารา (מָרָא) แปลว่า 'ขมขื่น' — นางเปลี่ยนชื่อตนเองเพื่อสะท้อนความเศร้าโศก"

### Stratum 2 — Alliteration / sound-rhetoric within a verse

Examples:
- `תֹּהוּ וָבֹהוּ` (Gen 1:2) — formless + empty, paired by sound (tohu wa-bohu)
- `שֹׁאוֹן וְשׁוֹאָה` (Zeph 1:15) — devastation and desolation
- `בְּעֲבוּר אֱלֹהֵיכֶם` (Isa 53:8) — Isaiah's heavy alliteration in the Servant Songs
- `מִשְׁפַּח / מִשְׂפָּח` (Isa 5:7) — "justice" expected, "bloodshed" found

**Policy: capture if naturally Thai-renderable; footnote otherwise.** Don't force unnatural Thai for the sake of preserving the sound. Where Thai already has a natural alliterative pair (e.g., **ว่างเปล่าเปลี่ยวเหงา** for tohu-wa-bohu), use it. Where Thai requires unnatural construction, render literally + footnote the Hebrew sound-rhetoric.

Sample Gen 1:2:
- Main option A (preserve sound-pair): **ส่วนแผ่นดินโลกนั้นว่างเปล่าและเปลี่ยวเหงา**
- Main option B (literal, footnote): **ส่วนแผ่นดินโลกนั้นไร้รูปและว่างเปล่า** + footnote about Hebrew tohu-wa-bohu doubled-noun construction

Translator's choice per-verse.

### Stratum 3 — Polyptoton / cognate-noun-with-cognate-verb (intensifying)

The most common Hebrew rhetorical figure: a noun and its cognate verb together for emphasis.

Examples:
- `מוֹת תָּמוּת` (Gen 2:17) — "dying you shall die" → **เจ้าจะต้องตายแน่ ๆ** (intensifier rendered via แน่ ๆ / อย่างแน่นอน)
- `שָׁמוֹעַ תִּשְׁמַע` — "hearing you shall hear" → **เจ้าจะฟังอย่างตั้งใจ** OR **เจ้าจะได้ยินแน่นอน**
- `שָׁמַר תִּשְׁמְרוּן` — "guarding you shall guard" → **เจ้าทั้งหลายจงรักษาให้ดี / รักษาอย่างเคร่งครัด**
- `הָלֹךְ יֵלֵכוּ` — "going they shall go" → **พวกเขาจะเดินไปอย่างต่อเนื่อง / พวกเขาจะเดินไปเรื่อย ๆ**

**Policy: render as Thai intensifier or duration-marker.** Don't try to preserve the doubled verb in Thai (Thai grammar doesn't tolerate doubled cognate verbs the way Hebrew does). Use Thai adverbials (`แน่นอน, อย่างแน่นอน, แน่ ๆ, อย่างยิ่ง, อย่างต่อเนื่อง, เรื่อย ๆ, อย่างเคร่งครัด`) to capture the intensification.

When the intensification is theologically loaded (Gen 2:17 — the death-warning), the `key_decisions` notes the polyptoton specifically.

### Stratum 4 — Phonetic puns on similar-sounding Hebrew roots

Examples:
- **Hebrews 5:8** quoting Hebrew rhetorical pattern — `ἔμαθεν ἀφ' ὧν ἔπαθεν` ("learned from what he suffered") preserves Greek pun, but the underlying Hebrew thought-pattern is older. NT-side handling is established.
- **Isaiah 5:7** — `מִשְׁפָּט / מִשְׂפָּח` (justice/bloodshed) and `צְדָקָה / צְעָקָה` (righteousness/cry) — TWO consecutive paronomasia
- **Jeremiah 1:11-12** — `שָׁקֵד / שֹׁקֵד` (almond-tree / watching) — God watching over his word

**Policy: preserve in main text where possible; footnote when not.** The Isaiah 5:7 case is essentially impossible to fully render in Thai while preserving both pun-pairs. Render the meaning; footnote the original sound-play in `thai_summary`.

Sample Isaiah 5:7:
- Main: **พระองค์ทรงคาดหวังความยุติธรรม แต่กลับเห็นการนองเลือด ทรงคาดหวังความชอบธรรม แต่กลับได้ยินเสียงร้องคร่ำครวญ**
- `thai_summary`: "ภาษาฮีบรูใช้คู่คำเสียงคล้ายกันสองคู่ (มิชพัต/มิชพาห, ตเศดาคา/ตเซอาคา) เพื่อเน้นความขัดแย้งระหว่างความคาดหวังของพระเจ้ากับสิ่งที่ทรงพบในชนชาติของพระองค์"

---

## 2. Specific cross-cutting wordplay categories

### 2.1 Place-name + meaning binding

Many OT places are named with theological meaning. Per `proper_names_and_transliteration_2026-05.md` Override #4: transliterate the compound + footnote the meaning.

| Place | Meaning footnoted |
|---|---|
| `יהוה־יִרְאֶה` (Gen 22:14) | "พระยาห์เวห์ทรงจัดเตรียม" |
| `מַחֲנַיִם` (Gen 32:2) | "สองค่าย" (Jacob seeing two camps of angels) |
| `פְּנוּאֵל` (Gen 32:30) | "พระพักตร์ของพระเจ้า" (where Jacob saw God face-to-face) |
| `מְרִיבָה` (Ex 17:7) | "การโต้แย้ง" |
| `מַסָּה` (Ex 17:7) | "การทดสอบ" |
| `גִּלְגָּל` (Josh 5:9) | "การกลิ้งออกไป" (rolling away of Egypt's reproach) |
| `אַכוֹר / אִיכָבוֹד` | "ความปั่นป่วน / ปราศจากเกียรติ" (Ichabod, 1 Sam 4:21) |
| `יִזְרְעֶאל` | "พระเจ้าทรงหว่าน" (Hosea's son's name) |

### 2.2 Theological-name wordplay

When the divine name itself participates in the wordplay (Exodus 3:14 — `אֶהְיֶה אֲשֶׁר אֶהְיֶה`), this gets a separate doc (`exodus_3_14_divine_self_naming_2026-05.md`, planned). Reference here for completeness; do not duplicate.

### 2.3 Numerical wordplay (gematria-like)

Rare but present. The most common case is **alphabetic acrostics** (Psalm 119, etc.) per `ot_register_policy_2026-05.md` §5. Other numerical-wordplay (e.g., the 14 generations in Matt 1's structure echoing David's gematria of 14) is NT-side and out of scope here.

---

## 3. Translation principle: meaning > sound when forced to choose

When the wordplay cannot be preserved in Thai without sacrificing meaning, **prioritize meaning**. Footnote the original sound. The Thai reader gets the semantic content; the Hebrew-reader scholar can recover the sound from the footnote.

When the wordplay can be preserved in Thai naturally (e.g., a Thai sound-pair already exists for the Hebrew sound-pair), preserve it. Document the choice in `key_decisions`.

---

## 4. The verse-level checking mechanism

Plan §9.3 lists `check_paronomasia.py` as one of the 6 specialized scripts. Implementation:

1. Read the chapter's source `hebrew` field.
2. Look up known wordplay sites in `data/known_paronomasia.json` (built incrementally from the catalog above + new findings).
3. For each known site in the chapter, verify the verse's `key_decisions` mentions the wordplay (either "preserved in Thai" or "footnoted in thai_summary").
4. Flag missing decisions for translator review.

This is a soft-check (warning, not fail). Translator may legitimately decide a wordplay is too minor to mark; the check just surfaces it.

---

## When to revisit

- **At Genesis pilot end** — Genesis is dense with name-etymology wordplay. After the pilot ships, review the `data/known_paronomasia.json` catalog for completeness on Gen 1-11; extend to Gen 12-50 progressively.
- **At Phase 6F (Wisdom/Poetry) start** — Job, Proverbs, Psalms have heavy alliteration and parallelism interactions; re-read this doc.
- **At Phase 6G (Prophets) start** — Isaiah, Jeremiah, the Twelve are paronomasia-heavy. Catalog will grow most here.
- **If a wordplay surfaces during translation that this doc doesn't address** — log in `key_decisions`, add to `data/known_paronomasia.json`, append a row to the relevant section above.
