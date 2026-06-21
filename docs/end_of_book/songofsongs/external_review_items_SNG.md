## Item A — 8:6 שַׁלְהֶבֶתְ יָה ("flame of Yah"): the Song's only divine-name-adjacent token

**The crux:** The Song of Songs contains **no Tetragrammaton anywhere** — except a single contested token at the book's theological climax, 8:6. The extracted MT writes the final element with a space: `שַׁלְהֶבֶתְ יָה`. The final `יָה` can be read two ways:

1. **Theophoric** — the short-form divine name **Yah** (as in Hallelu-Yah). Reading: "the flame of Yah / the very flame of the LORD" (so ESV, CSB).
2. **Frozen superlative** — the `-yah` ending as an intensifying suffix. Reading: "a mighty / raging flame, the fiercest blaze of all" (so NIV, BSB).

**The current rendering takes the theophoric line in the main text, the superlative in `thai_literal`:**

- SNG 8:6 HEB: `כִּי־עַזָּה כַמָּוֶת אַהֲבָה … רְשָׁפֶיהָ רִשְׁפֵּי אֵשׁ שַׁלְהֶבֶתְ יָה`
- TH (main): `เพราะความรักเข้มแข็งดั่งความตาย … ประกายของมันคือประกายแห่งไฟ คือเปลวเพลิงแห่ง**พระยาห์**` ("…the flame of Phra-Yah")
- TH (`thai_literal`): `…คือเปลวเพลิงอันเกรียงไกร (อ่านแบบขั้นสูงสุด)` ("…a mighty flame [superlative reading]")

The verse-level decision note itself flags this: *"this is the only divine name in the whole book … FLAG FOR EOB REVIEW — this two-way choice is a book-level decision."*

**A second, internal problem if the theophoric reading stands:** the project's divine-names table locks the short form `יָהּ → ยาห์` **bare** (e.g. Pss 68:4; הַלְלוּ-יָהּ → ฮาเลลูยาห์). The current rendering uses **พระยาห์** (an honorific prefix พระ- + ยาห์) that no table row authorizes. And the automated divine-names check reports **0 YHWH chapters** for the whole book — it does not recognize שַׁלְהֶבֶתְ יָה as a divine-name occurrence — so the book currently ships with no first-occurrence footnote.

**Three questions:**
1. Is the theophoric reading ("flame of Yah / the LORD") the right editorial line for an evangelical-Protestant CC0 Thai Bible, or should the project follow the superlative line (NIV/BSB "a mighty flame") with the theophoric in a footnote? (Evangelical English translations are genuinely split: ESV/CSB theophoric, NIV/BSB superlative.)
2. If theophoric, should the surface form be the locked **ยาห์** (bare, table-conformant) rather than the unauthorized **พระยาห์** — i.e. `…เปลวเพลิงแห่งยาห์`?
3. If theophoric, does the book now owe a first-occurrence translator footnote at 8:6 explaining the Yah short-form + the superlative alternative — even though it has no full Tetragrammaton elsewhere?

---

## Item B — King-persona + Solomon: should an OT poetic book use royal honorifics (ราชาศัพท์) for human kings?

**The pattern:** Thai has a royal register (ราชาศัพท์ / "rachasap" — special verbs like ทรง-, pronouns like พระองค์, body-part nouns like พระทัย "royal heart"). The Eremos OT reserves this register for **God** by default. But the Song applies **light/full rachasap to human kings**:

| Context | Verse | Thai | Register |
|---|---|---|---|
| The male lover *figured* as a king | 1:4 | กษัตริย์**ทรง**นำฉันเข้าในห้องของ**พระองค์** | light royal |
| Solomon's wedding procession | 3:9–11 | **ทรง**สร้างพระราชยาน… **ทรง**มงกุฎซึ่ง**พระมารดา**สวมให้**พระองค์** … **พระทัย** | full royal |
| Solomon as vineyard-owner | 8:11 | ซาโลมอน**ทรง**มี… **พระองค์ทรง**ให้…เช่า | full royal |
| The king *held captive* in her hair | 7:6 | กษัตริย์ก็ตกเป็นเชลย (plain — no royal verb) | **plain** |

Note the sophisticated modulation at 7:6: the *conquered* king is **not** dignified with royal register.

**The corpus tension:** The project's narrative-book register policy (`ot_register_policy §2.2`) **grants** Hebrew kings full royal register in their public-office role. But the project's two prior poetic/wisdom books — **Psalms and Proverbs** — went the *other* way and kept human kings **non-royal**, reserving the royal register for God alone (Proverbs end-of-book audit, 2026-05-31, flagged this as the book's headline editorial decision and recommended a `human_king_register` decision doc that has not yet been written). So the corpus currently holds two opposed conventions, and the Song follows the narrative policy rather than the Psalms/Proverbs poetic practice. (Unlike Psalms/Proverbs, the Song has essentially **no divine subject**, so using พระองค์ for Solomon creates no in-book ambiguity with God.)

**Question:** For an OT poetic book, is it right to give human kings (and a king-as-lover poetic conceit) the Thai royal register, when the sibling poetic books (Psalms, Proverbs) keep human kings non-royal? Should the three poetic books be made uniform with each other, or is the Song's king-rachasap (with the 7:6 captive-king modulation) defensible as context-appropriate?

---

## Item C — Proper-noun wordplay: surface for readers, or keep in scholarly notes?

**The pattern:** The Song runs several name/sound puns. The project's policy is to keep name-etymology in scholarly notes BY DEFAULT, adding a reader-facing translator footer ONLY when the wordplay is an *active argument-engine* across multiple verses (the test that triggered a footer for Paul's Onesimus "useful" pun in Philemon). The Song's puns are currently all in the scholarly notes:

1. **Shulammite / Shalom / Solomon** — 7:1 `הַשּׁוּלַמִּית → สาวชูลัม` (the woman's only name in the book); the note records the sound-chain שׁוּלַמִּית ↔ שְׁלֹמֹה (Solomon) ↔ שָׁלוֹם (peace), which the book closes at 8:10 (`כְּמוֹצְאֵת שָׁלוֹם → ดั่งผู้นำสันติภาพมาให้`, note: "closes the Shulam–Solomon–Shalom sound-chain … which Thai cannot carry").
2. **dudaim / dodi** — 7:14 `הַדּוּדָאִים → ผลเลื่อน` (mandrakes); note records the דּוּדָאִים / דּוֹדִי ("mandrakes" / "my beloved") pun.
3. **shem / shemen** — 1:3 `שֶׁמֶן` ("oil") / `שְׁמֶךָ` ("your name") sound-play, in the note.

**Question:** The Shulammite/Shalom chain is *structural* (a 7:1 introduction resolved at 8:10) rather than an argument the reader must follow — and the translation concedes Thai can't reproduce the sound-play. By the project's three-condition footer test (active argument + multi-verse density + comprehension-dependency), these stay in the notes. Is that the right call, or should the Shulammite/Shalom inclusio get a single reader-facing footer at 8:10 so a Thai reader sees the book's closing wordplay? Do any of the three cross the threshold?

---

## Item D — Erotic body-imagery: faithful (non-euphemized) — confirm the stance

**The pattern:** The Song's three descriptive-praise poems (ch. 4, 5, 7) render the body imagery **faithfully and without euphemism**:

- 1:13 `בֵּין שָׁדַי` → **ระหว่างทรวงอกของฉัน** ("between my breasts")
- 4:5 / 7:4 breasts → **ทรวงอก**; 7:2 navel/waist → **สะดือ / ท้อง** ("navel / belly"); 7:3 thighs → **ต้นขา**
- 5:4 the door-latch scene keeps its sensual charge: **ใจของฉันก็เร่าร้อนถึงเขา**, with the literal **อวัยวะภายใน…ปั่นป่วน** in the literal field

This is the **opposite** editorial pressure from the project's Leviticus policy, which *euphemizes* the legal "uncover nakedness" sexual-prohibition formula (`uncover_nakedness_euphemism_2026-05.md`). The two are not in conflict — Leviticus euphemizes a juridical-shame register; the Song celebrates married eros and the imagery is the literary point — but the Song is the corpus's most sexually explicit text.

**Question:** For an evangelical-Protestant CC0 Thai Bible aimed partly at a Thai Buddhist-background readership, is the "keep the imagery faithful, don't euphemize" stance the right call across the Song's waṣf poems? Are there specific verses where the Thai is either too explicit or too coy for the register? Should the stance be recorded in a translator-decisions doc so it's applied consistently in future books (e.g. Ezekiel 16/23)?
