# Song of Songs — End-of-Book Review

**Date:** 2026-06-04
**Scope:** All 8 chapters (117 MT verses; `output/translations/songofsongs_01.json` … `songofsongs_08.json`); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** SNG 8 shipped (commit `85c5e22b`); per `docs/END_OF_BOOK_CHECKLIST.md` §2 + §3, fired by `scripts/detect_book_complete.py`.
**Mandate:** Internal editorial review (§2). Surface only — **no translation changes made.**

## Summary

- **14 cross-cutting items reviewed.** Mechanical gates (§1) pass: 8/8 chapters have green per-chapter 7-check reports + back-translations (BT verse-counts match source: 17/17/11/16/16/12/14/14); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean (0 violations across 38 audited locks). `git status` SNG source clean — the only dirty file is `output/check_reports/divine_names.md` (a re-run global report artifact, **not SNG-scoped**, left unstaged).
- **5 items LOCKED** — flora/fauna/spice/gem/wood corpus-consistency; versification divergence zone (SNG 7 = English 6:13 + 7:1-13); honorifics-binding + Hebrew-field integrity; inclusion / MT-LXX textual-variant scope (N/A — no SBLGNT, no YHWH); divine-name *absence* (no first-occurrence footnote owed, per the Ecclesiastes/Esther precedent — **modulo item 1**).
- **6 items STABLE** — the lyric-voice register (ฉัน/เธอ + the דּוֹדִי / רַעְיָתִי distinction); the no-speaker-headers (MT-anchored) policy; the adjuration refrain + gazelle-oath divine-name-avoidance pun; the mutual-possession formula + the 7:11 teshuqah→Gen 3:16 echo; the faithful (non-euphemized) erotic body-imagery; the book-specific recurring-phrase leitwort locks.
- **2 items REVIEW** — the **king-persona + Solomon rachasap** (item 4, the headline editorial decision — SNG follows the *written* OT register policy §2.2 but diverges from the Psalms/Proverbs poetic-book non-royal practice); the proper-noun wordplay footer question (item 10).
- **1 item DECIDE** — item 1, **8:6 שַׁלְהֶבֶתְ יָה** ("flame of Yah") — the book's only divine-name-adjacent token; the verse-level KD itself flags it `FLAG FOR EOB REVIEW`. Blocks a clean `book-songofsongs-v1` tag.
- **External AI review (§3) items prepared** (see `external_review_items_SNG.md`).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — defensible-but-worth-Ben's-confirmation. **DECIDE** — Ben choice needed before tagging `book-songofsongs-v1`.

---

## 1. 8:6 שַׁלְהֶבֶתְ יָה ("flame of Yah") + the divine-name absence — **DECIDE** (the one blocker)

Song of Songs is, with Esther and Ecclesiastes, one of the OT books with **no Tetragrammaton anywhere** — except for a single contested token at the book's theological summit, **8:6**:

- **SNG 8:6** GK/HEB: `…רְשָׁפֶיהָ רִשְׁפֵּי אֵשׁ שַׁלְהֶבֶתְ יָה` → TH: `…ประกายของมันคือประกายแห่งไฟ คือเปลวเพลิงแห่ง**พระยาห์**`
  - `thai_literal`: `…คือเปลวเพลิงอันเกรียงไกร (อ่านแบบขั้นสูงสุด)`

The extracted MT writes the final element with a space (`שַׁלְהֶבֶתְ יָה`), and the translator read `יָה` as the short-form divine name **Yah**, rendering **เปลวเพลิงแห่งพระยาห์** ("flame of Yah") and parking the alternative superlative reading ("the fiercest blaze of all," BSB) in `thai_literal`. The 8:6 KD explicitly says: *"นี่คือพระนามครั้งเดียวของทั้งเล่ม … FLAG FOR EOB REVIEW — ทางเลือกสองสายนี้เป็นข้อตัดสินระดับเล่ม."*

**Three coupled decisions Ben must make:**

1. **Divine-name reading vs. superlative.** Is שַׁלְהֶבֶתְ יָה a genuine theophoric (the only divine-name in the Song, rendered as a name) or a frozen superlative (`-yah` as an intensifying suffix → "a mighty/raging flame")? The major evangelical translations split: ESV "the very flame of the LORD" (with footnote "a most vehement flame"), NIV "like a mighty flame," CSB "the LORD's own flame," BSB "the fiercest blaze of all." Per RULES §0, the project follows the modern evangelical critical consensus where one exists — and here it is genuinely split. The current rendering takes the theophoric line in the main text and the superlative in `thai_literal`. **Confirm or flip.**

2. **If theophoric: surface form.** The current rendering is **พระยาห์** (honorific พระ- + ยาห์). But `divine_names_table_2026-05.md` locks the short-form `יָהּ → ยาห์` **bare** (e.g. Pss 68:4; the הַלְלוּ-יָהּ → ฮาเลลูยาห์ formula). No table row authorizes a **พระยาห์** form. Either (a) normalize 8:6 to the locked **ยาห์** (`…เปลวเพลิงแห่งยาห์`), or (b) add a sub-rule to the divine-names table authorizing **พระยาห์** for the standalone-reverential context (vs. the liturgical-formula bare ยาห์). **This is a divine-names-table drift that must be resolved either way.**

3. **If theophoric: does SNG 8 now owe a first-occurrence footnote?** The book currently ships with **no `output/textual_variants/songofsongs_*.json` file** and the `divine_names.md` check reports **0 chapters-with-YHWH / 0 first-occurrence-footnotes** — i.e. the automated divine-names check does **not** recognize שַׁלְהֶבֶתְ יָה as a divine-name occurrence (the token is the short form Yah embedded in a construct, and the check scans for full YHWH). So *as shipped*, SNG conforms to the Ecclesiastes/Esther "no-YHWH → no footnote owed" precedent. But **if** 8:6 is affirmed as a divine name, the `divine_names_table_2026-05.md` Layer-2 mechanism would arguably owe a Tier-2 first-occurrence footnote at 8:6 (`output/textual_variants/songofsongs_08.json`) explaining the Yah short-form + the superlative-vs-theophoric reading. **Decide whether 8:6 triggers the footnote mechanism or stays a verse-level KD note.**

**Recommendation:** keep the theophoric reading in the main text (it is the harder, more defensible line and preserves the only divine spark in the book's climax), **normalize พระยาห์ → ยาห์** to the locked table form (or formally authorize พระยาห์ via a one-line table sub-rule), and **add a single Tier-2 footnote at 8:6** that does double duty — naming the Yah short-form *and* the superlative alternative. This is the cleanest resolution and the only item blocking `book-songofsongs-v1`.

**Also note (8:6, second KD):** `קִנְאָה` rendered **ความหวงแหน** ("ardor/jealous-love"), deliberately distinguished from the negative-envy sense (Eccl-style อิจฉา). Defensible and well-reasoned; no action. `שְׁאוֹל → แดนคนตาย` conforms to the corpus lock (Eccl 9:10).

---

## 2. Lyric-voice register — ฉัน / เธอ + the דּוֹדִי / רַעְיָתִי distinction — **STABLE** (recommend doc-lift)

The book's foundational voice decision, documented at the 1:2 KD: both lovers self-refer as **ฉัน** and address each other as **เธอ** — the intimate lyric register, deliberately **not** the ดิฉัน/ข้าพเจ้า of formal prose. Layered on top is a strict gendered endearment split:

| Hebrew | Speaker→addressee | Thai lock | Count | Representative |
|---|---|---|---|---|
| **דּוֹדִי** | she → him ("my beloved") | **ที่รักของฉัน** | ~26× | 1:13, 1:14, 2:3, 2:8–10, 2:16–17, 4:16, 5:2–8, 5:10–16, 6:1–3, 7:10–14, 8:14 |
| **רַעְיָתִי** | he → her ("my darling") | **ยอดรักของฉัน** | ~9× | 1:9, 1:15, 2:2, 2:10, 2:13, 4:1, 4:7, 5:2, 6:4 |
| **רֵעִי** (masc. of רַעְיָתִי) | she → him ("my friend") | **สหายของฉัน** | 1× | 5:16 |

The two are kept lexically distinct so a Thai reader can hear *who is speaking* without rubrics (see item 3). The split is principled and 100% uniform. **STABLE — recommend `docs/translator_decisions/songofsongs_lyric_voice_register_2026-06.md`** locking: (a) the ฉัน/เธอ lyric register; (b) the דּוֹדִי→ที่รักของฉัน / רַעְיָתִי→ยอดรักของฉัน distinction; (c) the additional fixed endearments — יוֹנָתִי→นกพิราบของฉัน (2:14, 5:2, 6:9), תַמָּתִי→คนงามพร้อมของฉัน (5:2, 6:9), אֲחֹתִי כַלָּה→น้องสาวของฉัน เจ้าสาวของฉัน (the kin-endearment, 4:9–5:1 ×4). Book-specific (no forward-compounding), but it is the book's spine and deserves a durable record beyond the 1:2 KD.

---

## 3. No speaker headers (MT-anchored) — **STABLE**

The Song is a dialogue with no MT speaker-rubrics; many modern English editions *insert* them (ESV/NIV/CSB add "He / She / Others" / "Bride / Bridegroom / Friends"). Eremos follows the MT — **no inserted headers in the verse text** — and identifies the speaker in `thai_summary` instead (e.g. 2:2 "ชายหนุ่มตอบ…", 6:1 "บุตรสาวเยรูซาเล็มอาสา…"). This is consistent with the project's general MT-anchoring principle and with the no-paraphrase-into-the-text discipline. Uniform across all 8 chapters. **STABLE.** (Worth confirming as an editorial stance, since some Thai readers accustomed to THSV-style rubrics may find the un-headed dialogue harder to follow — but the `thai_summary` layer carries the speaker-identification, which is the project's designed mechanism.)

---

## 4. King-persona + Solomon rachasap — **REVIEW** (the headline editorial decision)

The Song deploys light **ราชาศัพท์ (royal Thai)** in three king-related registers, and the handling is intelligently modulated:

| Context | Verse | Rendering | Register |
|---|---|---|---|
| The male lover *figured* as a king ("the king brings me to his chambers") | 1:4 | **กษัตริย์ทรงนำฉันเข้าในห้องของพระองค์** | light rachasap (ทรงนำ / พระองค์) |
| The king at his table | 1:12 | **กษัตริย์ประทับที่โต๊ะเสวยของพระองค์** | light rachasap (ประทับ / เสวย) |
| Solomon's procession (palanquin, crown, wedding) | 3:7–11 | **พระวอ** (mittah), **พระราชยาน** (appiryon), **ทรงสร้าง**, **ทรงมงกุฎ**, **พระมารดา**, **อภิเษกสมรส**, **พระทัย** | full rachasap |
| Solomon as vineyard-owner | 8:11–12 | **ซาโลมอนทรงมี… พระองค์ทรงให้… เช่า** | full rachasap |
| The king *held captive* in her tresses | 7:6 | **กษัตริย์ก็ตกเป็นเชลยอยู่ในปอยผมนั้น** | **plain** (not a rachasap-subject — the captive king is the object, not the dignified office-actor) |

**The cross-cutting tension.** `ot_register_policy_2026-05.md` §2.2 explicitly grants **Hebrew kings (incl. Solomon) full ราชาศัพท์ in public-office context** ("Narrator dignifies the office"). By that *written* policy, SNG's Solomon-rachasap is **correct**. But the **Proverbs and Psalms** practice goes the other way: those books keep human kings **non-royal** and reserve ทรง/พระองค์ for God alone (Proverbs audit 2026-05-31, item 2 — flagged REVIEW, recommending a pending `human_king_register_2026-05.md` doc that is **not yet written**). So the corpus currently holds **two opposed king-register conventions**: narrative-book policy (kings get ทรง) vs. wisdom/poetic-book practice (kings non-royal).

SNG sits in the poetic camp but follows the narrative-book policy. The usual rationale for the poetic-book non-royal choice — keep พระองค์ unambiguously = God — **does not create internal ambiguity in SNG**, because God is essentially absent from the book (item 1). So SNG's choice is defensible on its own terms. The 7:6 plain-king modulation is a genuinely sophisticated touch (the conquered-king is *not* dignified). But the corpus inconsistency is real and will recur in every poetic book.

**REVIEW — confirm SNG's king-rachasap, and resolve the corpus tension.** Recommend Ben (a) decide whether the poetic books should be uniform with each other or with the narrative policy, and (b) write the pending `docs/translator_decisions/human_king_register_2026-05.md` (owed since the Proverbs audit) with an explicit **Song-of-Songs persona-king sub-rule**: lover-as-king and Solomon-proper take light/full rachasap; the captive-king (7:6) stays plain. If Ben decides the poetic books must be non-royal-uniform, SNG would need a corpus-revision pass (≈8 verses) — hence this borders on DECIDE; it is flagged REVIEW because SNG *complies with the written policy as it stands*.

---

## 5. The adjuration refrain + gazelle-oath divine-name-avoidance pun — **STABLE** (recommend documenting under `hebrew_oath_formulas`)

The "daughters of Jerusalem, I adjure you" refrain recurs with controlled variation:

- **2:7 = 3:5** (verbatim): `הִשְׁבַּעְתִּי אֶתְכֶם בְּנוֹת יְרוּשָׁלִַם בִּצְבָאוֹת אוֹ בְּאַיְלוֹת הַשָּׂדֶה אִם־תָּעִירוּ…` → **ฉันขอให้พวกเธอสาบานโดยอ้างฝูงละมั่งและกวางตัวเมียแห่งท้องทุ่ง … จนกว่าความรักจะพอใจเอง** (identical both times — `check_phrase_consistency` clean).
- **8:4** (MT abbreviates — drops the gazelle clause, uses מַה for אִם): rendered with the same core (`ฉันขอให้พวกเธอสาบานว่า…`), the abbreviation mirrored. KD documents it.
- **5:8** (a *different* adjuration — "if you find my beloved, tell him I am sick with love"): correctly treated as a **variant, not the refrain** — KD flags it explicitly.

The 2:7 `notes` capture the famous euphemism: `בִּצְבָאוֹת אוֹ בְּאַיְלוֹת` ("by the gazelles / by the does") **puns on the avoided divine titles** `(יהוה) צְבָאוֹת` ("LORD of hosts") and `(אֵל) שַׁדַּי` — the lovers swear by gazelles *instead of* by the divine name, in keeping with the book's God-absent style. This is a real intersection with `divine_names_table` (a deliberate divine-name *non*-occurrence) and with `hebrew_oath_formulas_2026-05.md`.

**STABLE.** The `hebrew_oath_formulas` doc catalogs four oath-types but **not** the `הִשְׁבַּעְתִּי אֶתְכֶם` "adjure-you" type or the gazelle-substitution pun. **Recommend a short addition to `hebrew_oath_formulas_2026-05.md`** documenting the Song's adjuration-refrain Thai lock (`ฉันขอให้พวกเธอสาบาน…`) and the divine-title-avoidance pun, so the oath-formula catalog is complete.

---

## 6. The mutual-possession formula + the 7:11 teshuqah→Gen 3:16 echo — **STABLE**

The book's structural refrain of belonging develops in three steps, all locked:

- **2:16** `דּוֹדִי לִי וַאֲנִי לוֹ` → **ที่รักของฉันเป็นของฉัน และฉันก็เป็นของเขา** (he-first)
- **6:3** `אֲנִי לְדוֹדִי וְדוֹדִי לִי` → **ฉันเป็นของที่รักของฉัน และที่รักของฉันก็เป็นของฉัน** (inverted, I-first)
- **7:11** `אֲנִי לְדוֹדִי וְעָלַי תְּשׁוּקָתוֹ` → **ฉันเป็นของที่รักของฉัน และความปรารถนาของเขาก็มีต่อฉัน**

The 7:11 KD makes the cross-corpus catch: `תְּשׁוּקָה` ("desire") is the **same lemma as Gen 3:16** ("your desire shall be for your husband"), and the Song *reverses the direction* — there the woman's desire is toward the man under the curse; here **the man's** desire is toward the woman. The translator locked **ความปรารถนา** specifically so the Gen 3:16 reversal is audible in Thai. This is exactly the leitwort-handling-policy Rule 1/Rule 2 ideal (preserve the lemma where it carries cross-corpus theological weight). **STABLE — no action;** optionally note the תְּשׁוּקָה↔Gen 3:16 thread in the leitwort doc's cross-corpus list if Genesis 3:16's Thai is confirmed to use ความปรารถนา (worth a one-line consistency check).

---

## 7. Erotic body-imagery: faithful, non-euphemized — **STABLE** (recommend a note)

The three waṣf (descriptive-praise) poems (ch. 4 he→her, ch. 5 she→him, ch. 7 he→her) render the body imagery **faithfully and without euphemism**: 1:13 `בֵּין שָׁדַי` → **ระหว่างทรวงอกของฉัน**; 4:5 / 7:4 breasts → **ทรวงอก**; 7:2 navel/waist → **สะดือ / ท้อง**; 7:3 thighs → **ต้นขา**; 5:4 the door-latch scene kept its sensual charge (`ใจของฉันก็เร่าร้อนถึงเขา`, with the literal `อวัยวะภายใน…ปั่นป่วน` in `thai_literal`). The 4:7 `מוּם → ตำหนิ` deliberately echoes the Levitical "without blemish" sacrificial register; 4:12 / 8:6 `ประทับตรา` (seal) threads.

This is the **opposite editorial pressure** from `uncover_nakedness_euphemism_2026-05.md` (which *euphemizes* Leviticus's legal sexual-prohibition formula). The two are not in conflict — Leviticus euphemizes a *juridical-shame* register; the Song *celebrates* married eros and the imagery is the point — but SNG is the corpus's most eros-explicit text, and the "keep it faithful, don't euphemize" stance is a real editorial decision worth a durable note (especially given Thai Buddhist-background readers and the project's evangelical framing). **STABLE — recommend a short note** (either a `songofsongs_body_imagery_2026-06.md` or a §in the lyric-voice doc of item 2) recording the non-euphemism stance + the deliberate contrast with the Levitical euphemism policy. Also a good **external-review item** (see §3 Item).

---

## 8. Flora / fauna / spice / gem / wood corpus-consistency — **LOCKED**

The Song is the OT's densest catalog of named plants, perfumes, and gems; every one is anchored to an existing corpus rendering:

- **Perfumes/spices:** נֵרְדְּ → **นารดา** (NT lock, Mark 14:3 / John 12:3); מוֹר → **มดยอบ**; מוֹר עֹבֵר → **มดยอบเหลว** (Exod 30:23); לְבוֹנָה → **กำยาน**; כֹּפֶר → **เทียนกิ่ง** (henna); אֲהָלוֹת → **กฤษณา** (Prov 7:17); כַּרְכֹּם → **หญ้าฝรั่น**; קָנֶה/קִנָּמוֹן → **อ้อหอม/อบเชย** (Exod 30:23).
- **Flowers/trees:** שׁוֹשַׁנָּה → **ดอกบัว** (1 Kings 7 temple-lily lock); תַּפּוּחַ → **แอปเปิล**; פַּרְדֵּס → **อุทยาน** (Eccl 2:5); אֲרָזִים/בְּרוֹתִים → **สนสีดาร์/ไซเปรส** (1 Kings temple woods); תָּמָר → **อินทผลัม**; דּוּדָאִים → **เลื่อน** (mandrake, Gen 30:14).
- **Gems/metals:** תַּרְשִׁישׁ → **บุษน้ำเงิน** (Exod 28:20); סַפִּיר → **ไพลิน** (Exod 24:10); אַרְגָּמָן → **ผ้าสีม่วง** (tabernacle).

All consistent with `proper_names_and_transliteration_2026-05.md` and the prior-book corpus. `check_key_term_consistency.py` confirms 0 undocumented multi-renderings. **LOCKED.**

---

## 9. Recurring-phrase leitwort locks — **STABLE** (book-specific, per `leitwort_handling_policy` Rule 2)

Beyond the endearments (item 2) and formulas (items 5–6), the book's repeated phrases are uniformly locked:

- `שֶׁאָהֲבָה נַפְשִׁי` → **ผู้ที่ใจฉันรัก** (1:7; 3:1–4 ×4)
- `הַיָּפָה בַּנָּשִׁים` → **ผู้งามเลิศในหมู่หญิง** (1:8, 5:9, 6:1)
- `כִּשְׁנֵי עֳפָרִים … צְבִיָּה` → **ดั่งลูกละมั่ง … แม่ละมั่ง** (4:5 = 7:4)
- `לִצְבִי אוֹ לְעֹפֶר הָאַיָּלִים` → **ดั่งละมั่งหรือกวางหนุ่ม** (2:9, 2:17, 8:14)
- `קוּמִי לָךְ … וּלְכִי־לָךְ` → **ลุกขึ้นเถิด … มากับฉันเถิด** (2:10 = 2:13)
- `שְׂמֹאלוֹ … וִימִינוֹ` → **แขนซ้าย … แขนขวา** (2:6 = 8:3)
- `הַשֹּׁמְרִים` → **คนยาม** (3:3 helpful / 5:7 dark-mirror — same word, opposite outcome, lock preserved)
- `מִי זֹאת עֹלָה מִן־הַמִּדְבָּר` → **นั่นใครกันที่ขึ้นมาจากถิ่นทุรกันดาร** (3:6 = 8:5; cf. 6:10)
- `אֲיֻמָּה כַּנִּדְגָּלוֹת` → **น่าครั่นคร้ามดั่งกองทัพชูธง** (6:4 = 6:10, where MT repeats but BSB diverges to "stars" — the project held the MT repeat)
- `נֹטְרִים / כֶּרֶם שֶׁלִּי` → the 1:6 "my own vineyard I did not keep" → 8:12 "my vineyard is mine" inclusio, lock preserved

These are book-specific Leitwörter (not corpus-locked) and correctly handled as book-tagged consistency per `leitwort_handling_policy_2026-05.md` Rule 2. `check_phrase_consistency.py` clean. **STABLE.**

---

## 10. Proper-noun wordplay — **REVIEW** (footer-note question)

The book runs several name/sound puns, all currently kept in `key_decisions` / `notes` (no reader-facing footer):

- **Shulammite / Shalom / Solomon** — `הַשּׁוּלַמִּית → สาวชูลัม` (7:1, the only naming of the woman); the KD notes the שׁוּלַמִּית ↔ שְׁלֹמֹה ↔ שָׁלוֹם sound-chain, which 8:10 closes (`כְּמוֹצְאֵת שָׁלוֹם → ดั่งผู้นำสันติภาพมาให้`, KD: "ปิดสายเสียงพ้อง ชูลัม-ซาโลมอน-ชาโลม … ภาษาไทยคงไม่ได้").
- **dudaim / dodi** — 7:14 `הַדּוּדָאִים → ผลเลื่อน` (mandrakes), KD notes the דּוּדָאִים/דּוֹדִי ("mandrakes"/"my beloved") pun.
- **shem / shemen** — 1:3 `שֶׁמֶן`/`שְׁמֶךָ` ("oil"/"your name") sound-play, in `notes` (cf. Eccl 7:1).

Per `proper_noun_wordplay_2026-05.md`, a reader-facing translator-note footer is added **only** when all three conditions hold (active argument-bearing wordplay + multi-verse density + reader-comprehension dependency). The Shulammite/Shalom chain is *structural* (7:1 introduction → 8:10 resolution) rather than argument-bearing, and the KD itself concedes Thai can't carry it. By the strict three-condition test, these correctly stay in KD/notes. **REVIEW — confirm** that none of the SNG puns crosses the footer threshold (recommend: they do not — they are framing/atmospheric, not argument-engines like the Philemon Onesimus pun). If Ben wants the Shulammite/Shalom inclusio surfaced for readers, a single 8:10 translator-note footer is the place; otherwise leave as KD.

---

## 11. Versification divergence zone (SNG 7 = English 6:13 + 7:1-13) — **LOCKED**

Chapter 7 carries a `versification` block on **all 14 MT verses** (MT 7:1 = English/BSB 6:13; MT 7:2-14 = English 7:1-13; LXX tracks MT). The 14 `SNG-7-*` entries are registered in `data/versification_map.json` (confirmed present; the divergence zone was registered at commit `6478f45a`, and an earlier SNG divergence was registered for Song-of-Songs MT/English at `6478f45a`/start-memory). `check_versification` clean on all chapters. **LOCKED.**

**Process caveat (carry-forward):** per the `versification_map ship gotcha` (auto-memory), `ship_chapter.sh` does **not** stage `versification_map.json` — map edits in divergence chapters are committed manually. Confirm the SNG-7 map entries are committed on `main` before tagging (they appear present in the working tree; verify they are not an uncommitted local edit).

---

## 12. Honorifics-binding + Hebrew-field integrity — **LOCKED**

All 8 chapters cleared `check_honorifics_binding.py` and the Hebrew-field-integrity check (0 hard fails). Two SNG-specific techniques carried the rachasap cleanly:

- **Clause-final body-part with no trailing ทรง-verb** — e.g. 3:11 `พระทัย` placed clause-final (KD: "พระทัย อยู่ท้ายประโยค ไม่มีกริยา ทรง- ตามหลัง (เลี่ยง checker)"). This is the documented `…-splice trap` avoidance from the Kings-era memory.
- **Surface-form Hebrew citation in KDs** — the chapter-6 ship hit and fixed the integrity gotcha (KD `hebrew` field must cite the verse's *surface* form, not the lemma — e.g. 6:12 must cite MT's one-word `עַמִּינָדִיב`, since the word-division IS the crux; 2:1 `שׁוֹשַׁנַּת` not the lemma `שׁוֹשַׁנָּה`). All KDs now cite surface forms. **LOCKED.**

---

## 13. Inclusion / MT-LXX textual-variant scope — **N/A / LOCKED-by-precedent**

SNG is a Hebrew (MT) text with no SBLGNT scope, so `audit_inclusion_variants.py` (NT/SBLGNT-scoped) is N/A — the same disposition recorded for Proverbs/Psalms. There are no MT/LXX inclusion-gap candidates that rise above the §2.3 "non-gap" floor (the MT/LXX differences in the Song are word-level, not whole-verse inclusion variants). With no Tetragrammaton (item 1 modulo 8:6), **no `output/textual_variants/songofsongs_*.json` files are owed** — matching the Ecclesiastes (first no-YHWH OT book) and Esther precedents. **N/A — modulo the item-1 DECIDE** (if 8:6 is affirmed theophoric and Ben elects the Tier-2 footnote, one `songofsongs_08.json` would be created).

---

## 14. 6:12 Amminadib crux — **STABLE** (MT word-division crux, handled in KD)

The Song's most notorious textual crux, `מַרְכְּבוֹת עַמִּינָדִיב` (6:12), is rendered along the BSB line — **ราชรถแห่งชนผู้สูงศักดิ์ของฉัน** (reading עַמִּי־נָדִיב "my noble people") — with the proper-name reading ("Amminadib") preserved in `thai_literal` and the `notes`. The MT one-word surface form is correctly cited in the KD (the word-division *is* the crux). The נָדִיב thread is carried into 7:2 (`בַּת־נָדִיב → บุตรสาวแห่งผู้สูงศักดิ์`). Defensible, well-documented, BSB-aligned. **STABLE — no action.**

---

## Mechanical (§1) — all green (one tooling caveat)

- 8/8 chapters: `output/check_reports/songofsongs_NN_review.md` all 7 checks ✅
- 8/8 chapters: `output/back_translations/songofsongs_NN.json` present, verse-counts match source ✅
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** ✅
- `check_phrase_consistency.py`: **0 violations across 38 audited locks** ✅
- `git status output/`: only `output/check_reports/divine_names.md` dirty (re-ran global report; 0-YHWH-chapter recount — **not SNG-scoped**, left unstaged) ✅
- **Tooling caveat:** per the `EOB book-code registration gotcha` (auto-memory) and the Proverbs/Psalms note, the packet/USFM/YAML scripts' slug tables can lag for newly-completed OT codes. `build_external_review_packet.py SNG` resolves the SNG code (it looked for the items file rather than erroring); `audit_items_to_yaml.py SNG` and `export_to_usfm.py SNG` should be smoke-tested — register the SNG code first if either errors. Not a tag blocker.

---

## Flagged for Ben's attention

### A. 8:6 שַׁלְהֶבֶתְ יָה — **DECIDE before tagging** (§1)
Three coupled choices: (1) theophoric "flame of Yah" vs. superlative "raging flame"; (2) if theophoric, normalize **พระยาห์ → ยาห์** (locked table form) or authorize พระยาห์ via a table sub-rule; (3) if theophoric, whether SNG 8 owes a Tier-2 first-occurrence footnote. **Recommend:** keep theophoric, normalize to ยาห์, add one Tier-2 footnote doing double duty (Yah short-form + superlative alternative). **Only item blocking `book-songofsongs-v1`.**

### B. King-persona + Solomon rachasap — **REVIEW + owed doc** (§4)
SNG follows the *written* OT register policy §2.2 (Hebrew kings get ทรง) but diverges from the Psalms/Proverbs poetic-book non-royal practice. Confirm SNG's choice, and write the pending `human_king_register_2026-05.md` (owed since the Proverbs audit) with an explicit Song-of-Songs persona-king sub-rule (lover-as-king + Solomon = rachasap; captive-king 7:6 = plain). If Ben mandates poetic-book non-royal uniformity, ≈8 SNG verses need revision (then this becomes DECIDE).

### C. Proper-noun wordplay footer — **REVIEW** (§10)
Confirm none of the Song's puns (Shulammite/Shalom/Solomon 7:1+8:10; dudaim/dodi 7:14; shem/shemen 1:3) crosses the `proper_noun_wordplay` three-condition footer threshold. Recommend: leave in KD/notes (they are framing, not argument-engines). Optional single 8:10 footer if Ben wants the inclusio surfaced.

### D. Non-euphemized erotic body-imagery — **REVIEW / confirm stance** (§7)
Confirm the "keep the imagery faithful, don't euphemize" stance for the corpus's most eros-explicit text (contrast with the Levitical `uncover_nakedness` euphemism policy). Good external-review item for a Thai Buddhist-background readership sanity check.

### E. New / owed translator_decisions docs
1. `songofsongs_lyric_voice_register_2026-06.md` (§2) — lock ฉัน/เธอ + the דּוֹדִי/רַעְיָתִי endearment split + the fixed endearment set. **Recommended.**
2. `human_king_register_2026-05.md` (§4) — **owed since Proverbs**; add the SNG persona-king sub-rule. **Recommended.**
3. Short addition to `hebrew_oath_formulas_2026-05.md` (§5) — the `הִשְׁבַּעְתִּי אֶתְכֶם` adjuration-refrain lock + the gazelle-substitution divine-name-avoidance pun. **Recommended.**
4. Optional: a body-imagery non-euphemism note (§7) — standalone `songofsongs_body_imagery_2026-06.md` or a §in doc #1.

### F. External AI review (§3) — **pending**
Items prepared in `external_review_items_SNG.md`. Suggested focus: 8:6 Yah (A), king-persona rachasap (B), proper-noun wordplay footer (C), body-imagery stance (D).

---

## Recommendation

**Song of Songs ships in clean corpus-hygiene shape** — all mechanical gates green, all flora/fauna/spice/gem renderings corpus-anchored, the lyric-voice and leitwort architecture uniform and principled, the versification divergence properly registered. The one genuine blocker is **8:6 שַׁלְהֶבֶתְ יָה** (item 1 / §A), which the translator already self-flagged for this audit. The king-register decision (§B) is defensible-as-shipped but should be resolved at the corpus level (it's a Psalms/Proverbs-vs-SNG inconsistency, not an SNG error).

Tag `book-songofsongs-v1` after:
1. Ben's decision on §A (the 8:6 DECIDE) + any resulting normalization (พระยาห์→ยาห์) / footnote.
2. Ben's decisions on §B–D (king register, wordplay footer, body-imagery stance).
3. External AI sanity-check (§F).
4. The 1–3 recommended docs written (lyric-voice; the owed human-king doc; the oath-formula addition).
5. Re-run checks clean + `bash scripts/ship_book.sh SNG` (after confirming the SNG-7 versification-map entries are committed on `main`).
