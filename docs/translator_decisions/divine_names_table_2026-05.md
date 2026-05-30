# Divine names — table of OT renderings (Tetragrammaton + family)

**Scope:** Every form of the divine name and divine epithet that appears in the Hebrew Old Testament, plus a few Aramaic equivalents in Daniel/Ezra. Includes the Tetragrammaton (יהוה), the Adonai-YHWH compound (אֲדֹנָי יְהוִה), the title-clusters (יְהוָה צְבָאוֹת etc.), and the El-compound names (אֵל שַׁדַּי, אֵל עֶלְיוֹן, etc.).

**Decided:** 2026-05-04 (Ben). **Third-revision flip — locked before any OT chapter shipped.**
**Approach:** **NT-aligned with Hebrew-form transparency.** `יהוה → องค์พระผู้เป็นเจ้า`, identical to the NT corpus. Per-chapter footnote at first YHWH occurrence + per-verse `key_decisions` records the underlying Hebrew form so the Hebrew-form distinctness is preserved as transparency rather than as visual difference in vocabulary.

**Reversibility clause:** Ben explicitly noted "if we need to come back later and change the yahweh/LORD debate historical vs similarity, we will." A project-wide find-replace migration to `พระยาห์เวห์` is permitted if Thai reader feedback later prefers the historical-transliteration form. Until then, the renderings below are locked.

**Evidence base for the lock:**
- ~22 NT books shipped have been rendering κύριος-as-YHWH consistently as `องค์พระผู้เป็นเจ้า` (`κύριος Σαβαώθ → องค์พระผู้เป็นเจ้าจอมโยธα` Jas 5:4; `ἡμέρα κυρίου → วันแห่งองค์พระผู้เป็นเจ้α` 1 Th 5:2; `πνεῦμα κυρίου → พระวิญญาณขององค์พระผู้เป็นเจ้α` Lk/Acts pattern). The OT inherits this lock.
- Mainstream English translations (ESV, NIV, CSB, NLT) handle the Adonai/YHWH distinction via typographic small-caps ("LORD" vs "Lord"), layered over consistent vocabulary. Eremos's per-chapter-footnote + `key_decisions` mechanism is the equivalent in Thai (Thai script doesn't easily render small-caps).
- The earlier (2026-05-04 afternoon) `พระยาห์เวห์` lock was reversed before any OT chapter shipped, eliminating any migration cost.

---

## The full table (locked)

| Hebrew | Default Thai | Where this rendering applies |
|---|---|---|
| יהוה (Tetragrammaton) | **องค์พระผู้เป็นเจ้า** | Project-wide; matches NT corpus exactly |
| אֲדֹנָי יְהוִה (Adonai YHWH; "Lord GOD") | **องค์พระผู้เป็นเจ้า** | Compound collapses to single Thai rendering; `key_decisions` records the underlying Adonai-YHWH compound |
| יְהוָה צְבָאוֹת (YHWH Tsebaoth; "of hosts") | **องค์พระผู้เป็นเจ้าจอมโยธา** | **Identical** to already-shipped Jas 5:4. Visual unity preserved across testaments |
| יָהּ (Yah; short form) | **ยาห์** | Pss 68:4, 77:11; הַלְלוּ-יָהּ "Hallelu-Yah" closing-formula in Pss 113–118, 146–150. Transliterated because it's a phonetic short-form |
| אֱלֹהִים (Elohim) | **พระเจ้า** | Most-frequent name; matches NT θεός |
| אֱלוֹהַּ (Eloah, sg. of Elohim) | **พระเจ้า** | Job-frequent (~41×); Hab, Deut, Pss; Aramaic Job & Daniel parallel אֱלָהּ |
| אֵל (El, standalone) | **พระเจ้า** | Standalone; in compound names below, transliterate as **เอล-** |
| אֲדֹנָי (Adonai, standalone, of God — without YHWH compound) | **องค์เจ้านาย** | Distinct from `องค์พระผู้เป็นเจ้า` (which now covers YHWH). Matches NT δεσπότης pattern (e.g., 2 Pet 2:1). When standalone Adonai appears WITHOUT YHWH, this is the rendering — distinguishable in `key_decisions` from compound Adonai-YHWH |
| שַׁדַּי (Shaddai, **standalone divine title**) | **องค์ผู้ทรงมหิทธิฤทธิ์** ("the Almighty") | Job-frequent (esp. the dialogue cycles), Genesis-patriarchal. The **องค์-** prefix marks it as a standalone divine *title* — parallel to องค์พระผู้เป็นเจ้า and องค์เจ้านาย. **Standalone-title form locked 2026-05-30** per JOB external review (Gemini + ChatGPT, convergent CONCERN on standalone-title drift): when שַׁדַּי stands alone as a divine title it takes the องค์- prefix. Job's 6 early bare occurrences (5:17, 6:4, 6:14, 8:3, 8:5, 11:7) were normalized to **องค์ผู้ทรงมหิทธิฤทธิ์** for internal consistency with the 25 later occurrences. The bare **ผู้ทรงมหิทธิฤทธิ์** form is reserved for the **attributive/embedded** use inside compounds (next row), where the head noun already carries the divine classifier. |
| אֵל שַׁדַּי (El Shaddai) | **พระเจ้าผู้ทรงมหิทธิฤทธิ์** | Genesis 17:1, 28:3, 35:11, 43:14, 48:3, 49:25; Exodus 6:3. Here ผู้ทรงมหิทธิฤทธิ์ is **embedded/attributive** on พระเจ้า (no องค์- prefix — the พระเจ้า supplies the divine classifier). Contrast the standalone-title row above. |
| אֵל עֶלְיוֹן (El Elyon) | **พระเจ้าผู้สูงสุด** | Genesis 14:18–22 (Melchizedek scene) |
| אֵל עוֹלָם (El Olam) | **พระเจ้านิรันดร์** | Genesis 21:33 |
| אֵל רֳאִי (El Ro'i) | **เอลโรอี** + footnote ("พระเจ้าผู้ทรงเห็นข้าพเจ้า") | Genesis 16:13 (Hagar-specific). Transliterate; gloss the meaning in footnote because Hagar's wordplay is the point |
| יהוה־יִרְאֶה (YHWH-Yireh) | **ยาห์เวห์ยีเรห์** + footnote ("องค์พระผู้เป็นเจ้าทรงจัดเตรียม") | Genesis 22:14. Place-name compound; transliterate the proper-name form. Place-name compounds RETAIN the historical-transliteration `ยาห์เวห์` form because they are proper memorial-place names, not direct references to the deity |
| יהוה־נִסִּי (YHWH-Nissi) | **ยาห์เวห์นิสซี (องค์พระผู้เป็นเจ้าทรงเป็นธงชัยของข้า)** | Exodus 17:15. Altar-name. Per audit 2026-05-13: transliterate + gloss inline (parenthetical) so the altar's name reads as a Hebrew memorial-name. Distinguish from YHWH-paraphrastic-self-titles (see row immediately below). |
| **YHWH-paraphrastic-self-titles** (compound divine self-attributions, NOT memorial-place/altar names) | **paraphrase to Thai meaning** (do NOT transliterate) | Examples: Exod 15:26 יהוה רֹפְאֶךָ → "องค์พระผู้เป็นเจ้าผู้ทรงรักษาเจ้า" (YHWH-your-Healer); Exod 17:16 כֵּס יָהּ → "พระที่นั่งของยาห์" (the kes-Yah compound); Exod 31:13 יהוה מְקַדִּשְׁכֶם → "องค์พระผู้เป็นเจ้าผู้ทรงชำระเจ้าให้บริสุทธิ์" (YHWH-who-sanctifies-you). These are grammatically participial self-attributions embedded in YHWH-speech, NOT fixed memorial-name compounds. Per audit 2026-05-13. |
| יהוה־שָׁלוֹם (YHWH-Shalom) | **ยาห์เวห์ชาโลม** + footnote | Judges 6:24 |
| יהוה־צִדְקֵנוּ (YHWH-Tsidkenu) | **ยาห์เวห์ซิดเคนู** + footnote | Jeremiah 23:6, 33:16 |
| יהוה רֹעִי (YHWH ro'i) | **องค์พระผู้เป็นเจ้าทรงเป็นผู้เลี้ยงดูข้าพเจ้า** | Psalm 23:1. Not a place-name; YHWH is the divine subject of a verb, so the standard `องค์พระผู้เป็นเจ้า` rendering applies |
| יהוה־שָׁמָּה (YHWH-Shammah) | **ยาห์เวห์ชัมมาห์** + footnote | Ezekiel 48:35 |
| אֶהְיֶה אֲשֶׁר אֶהְיֶה (Ehyeh Asher Ehyeh) | **(separate decision doc)** | Exodus 3:14. The cardinal divine self-disclosure; needs its own treatment because it is not a name in the table-of-names sense — it is the verb-formula that grounds the Tetragrammaton |

### Aramaic equivalents (for Daniel + Ezra)

| Aramaic | Default Thai | Notes |
|---|---|---|
| אֱלָהּ (elah; sg.) | **พระเจ้า** | Equivalent of Hebrew אֱלוֹהַּ |
| אֱלָהָא (elaha; emphatic) | **พระเจ้า** | |
| מָרֵא־מַלְכִין / מָרֵא־שְׁמַיָּא (Mare-Malkin / Mare-Shemayya) | **องค์เจ้านายแห่งกษัตริย์ทั้งหลาย** / **องค์เจ้านายแห่งฟ้าสวรรค์** | Daniel 2:47, 5:23; "Lord of kings" / "Lord of heaven" titles |
| עִלָּאָה (Illaya; "the Most High") | **ผู้สูงสุด** | Daniel 4–7 frequent |

---

## Why the "place-name compounds" are the only place `ยาห์เวห์` survives

Two registers are at play in YHWH-bearing constructions:

- **Direct address / divine reference** — `יהוה` referring to the deity → **องค์พระผู้เป็นเจ้า** (matches NT corpus).
- **Place-name compound** — `יהוה־יִרְאֶה` etc. as a proper memorial-place name → transliterate as **ยาห์เวห์-X** + footnote translation.

This distinction is preserved across all compound names: when YHWH compounds with a verb/noun *as a place-name or memorial* (יהוה־יִרְאֶה, יהוה־נִסִּי, יהוה־שָׁלוֹם, יהוה־צִדְקֵנוּ, יהוה־שָׁמָּה), it is transliterated. When YHWH appears *as the divine subject* of a verb (יהוה רֹעִי, "YHWH my shepherd" in Ps 23:1), the standard `องค์พระผู้เป็นเจ้า` rendering applies.

The Thai reader's experience: place names that include "ยาห์เวห์" feel like Hebrew memorial-site names, similar to how an English reader experiences "Yahweh-Yireh" — clearly a transliterated proper name, not a translation of the deity-reference.

---

## Hebrew-form transparency mechanism

Because the Thai output collapses three distinct Hebrew forms (`יהוה`, `אֲדֹנָי יְהוִה`, `אֲדֹנָי` standalone, plus titular compounds like `יְהוָה צְבָאוֹת`) into the same Thai rendering family centered on `องค์พระผู้เป็นเจ้า`, the Hebrew-form distinctness is preserved via three layered mechanisms:

### Layer 1 — Per-verse `key_decisions` entry

Every verse where a YHWH-family form appears records the underlying Hebrew. Format examples:

- **Gen 2:4** (compound `יהוה אֱלֹהִים`):
  > "ในข้อนี้ 'องค์พระผู้เป็นเจ้าพระเจ้า' เป็นสำนวนแปลของ יהוה אֱלֹהִים (YHWH Elohim, the Tetragrammaton + Elohim compound). 'יהוה' (YHWH) แปลเป็น 'องค์พระผู้เป็นเจ้า' ตามแบบแผนของฉบับพันธสัญญาใหม่ — ดู translator_decisions/divine_names_table_2026-05.md"

- **Gen 15:2** (compound `אֲדֹנָי יְהוִה`):
  > "ในข้อนี้ 'องค์พระผู้เป็นเจ้า' เป็นสำนวนแปลของ אֲדֹנָי יְהוִה (Adonai-YHWH compound, "Lord GOD"). ฉบับเอเรโมสยุบสองคำให้เป็นรูปเดียวเพื่อหลีกเลี่ยงการซ้ำคำ ('Lord Lord'); แต่บันทึกไว้ที่นี่ว่าต้นฉบับฮีบรูเป็นรูปประสม"

- **Pss 110:1** (Adonai standalone, addressing Christ-figure):
  > "ในข้อนี้ 'องค์พระผู้เป็นเจ้าตรัสกับองค์เจ้านายของข้าพเจ้า' แปลจาก יהוה ל אֲדֹנִי. 'องค์พระผู้เป็นเจ้า' = יהוה; 'องค์เจ้านาย' = אֲדֹנִי (Adonai, here a title for the Davidic king / Christ-figure, distinct from the standalone Adonai-as-divine usage)"

### Layer 2 — Per-chapter first-occurrence footnote

The first verse of every OT chapter where YHWH appears carries a Tier 2 footer note (`output/textual_variants/<book>_<chapter>.json`):

> **องค์พระผู้เป็นเจ้า** ในบทนี้แปลจากภาษาฮีบรู יהוה (พระนามเฉพาะของพระเจ้า ออกเสียงโดยทั่วไปว่า "ยาห์เวห์") ฉบับเอเรโมสใช้ **องค์พระผู้เป็นเจ้า** ตามแบบแผนของฉบับพันธสัญญาใหม่ในการแปล κύριος ซึ่งในต้นฉบับฮีบรูตรงกับ יהוה. เมื่อข้อความฮีบรูใช้คำว่า אֲדֹנָי (อาโดนาย, "องค์เจ้านาย") โดยไม่มี יהוה ฉบับเอเรโมสจะแปลว่า "องค์เจ้านาย" เพื่อให้ผู้อ่านสามารถแยกแยะรูปแบบฮีบรูได้

### Layer 3 — Reader-edition front-matter

A single one-page convention note in the OT reader-edition front-matter explains the project's Tetragrammaton policy once for the whole OT, replacing per-chapter repetition. Once the reader-edition exists, the chapter-level footnote (Layer 2) is shortened to a brief reference to the front-matter.

This three-layer mechanism preserves Hebrew-form transparency without footnote-bloat in the running text. A scholar reading for the underlying Hebrew gets the answer; a devotional reader gets unobstructed Thai.

---

## Vocative direct address (when speaking to YHWH)

When the Hebrew has `יהוה` in second-person address (vocative) — most frequent in Psalms — the rendering matches the NT vocative pattern:

> **ข้าแต่องค์พระผู้เป็นเจ้า**

The `ข้าแต่` is the standard Thai deferential vocative particle (matching NT's `ข้าแต่องค์พระผู้เป็นเจ้า` for κύριε in vocative).

For psalms that combine vocative + epithet:

- `יהוה אֱלֹהַי` (YHWH my God) → **ข้าแต่องค์พระผู้เป็นเจ้า พระเจ้าของข้าพเจ้า**
- `יהוה רֹעִי` (YHWH my shepherd) → not vocative in Ps 23:1; declarative — **องค์พระผู้เป็นเจ้าทรงเป็นผู้เลี้ยงดูข้าพเจ้า**

---

## Hallelujah / הַלְלוּ-יָהּ formula

The closing-formula in Pss 113–118 + 146–150 reads `הַלְלוּ-יָהּ`. This is "Praise-Yah!" — short-form Tetragrammaton + plural imperative.

**Decision:**
- **Render:** **ฮาเลลูยาห์** (Thai-script transliteration of the full liturgical formula).
- **Why not break it apart** ("Praise Yah" / "จงสรรเสริญองค์พระผู้เป็นเจ้α"): the formula is a fixed liturgical unit in both Jewish + Christian traditions, and Thai church readers already know `ฮาเลลูยาห์` as a worship-word.
- This is consistent with how Eremos NT renders the same word in Revelation 19:1, 3, 4, 6 (`ฮาเลลูยาห์`).

---

## Wordplay involving the divine name (small set of cases)

A few OT scenes turn on the meaning of the divine name itself, not just its phonetic form. These need verse-level treatment:

- **Exodus 3:13–15** — Moses asks for the divine name; God responds `אֶהְיֶה אֲשֶׁר אֶהְיֶה`, then `אֶהְיֶה`, then `יהוה`. The wordplay relies on the verb `הָיָה` (to be) phonetically connecting the verb-form `אֶהְיֶה` to the proper name `יהוה`. **Action:** separate decision doc (`exodus_3_14_divine_self_naming_2026-05.md`); cannot be auto-resolved by this table. The fact that `יהוה → องค์พระผู้เป็นเจ้า` (vocabulary-level rendering) doesn't carry the verb-form phonetic connection means the Exodus 3 wordplay needs explicit verse-level handling with footnote.
- **Ruth 1:20–21** — Naomi puns on `שַׁדַּי` (Shaddai). **Action:** verse-level handling in `key_decisions`; reference this table for the base rendering.
- **Numbers 6:24–26** (Aaronic blessing) — three uses of `יהוה` in liturgical structure. **Action:** standard `องค์พระผู้เป็นเจ้า` rendering throughout; preserve the threefold structure visually if possible.

---

## What's NOT in scope for this doc

This doc covers **the divine name table only**. The following are separate:

- **Anthropomorphism policy** — see `hebrew_idioms_and_metaphor_2026-05.md`
- **Cultic/sanctuary register** — see `ot_register_policy_2026-05.md`
- **Rachasap policy** — see `ot_register_policy_2026-05.md` §B12.5
- **Wordplay on divine names** — see verse-level handling in `key_decisions`; this doc gives the base name only
- **NT-citation alignment with OT** — see plan §12 + the (now-simplified, mostly-alignment-as-default) `check_nt_quotation_alignment.py`

---

## When to revisit

- **Reader feedback at end of pilot.** When Ruth → Jonah → Genesis 1–11 ship and the maintainer + the Thai-language reviewer get reader response, if the per-chapter footnote convention is judged too intrusive or insufficiently transparent, adjust the mechanism (placement, brevity, frequency). The vocabulary lock is harder to revisit, but the find-replace migration to `พระยาห์เวห์` remains a clean one-PR option.
- **Specific compound that doesn't pattern.** If a divine-name compound surfaces during translation that this table doesn't anticipate, document it in `key_decisions` and append to this doc. Don't make ad-hoc renderings without recording them here.
- **NT regression.** If somehow the OT divine-name lock causes regression in NT rendering (extremely unlikely — both testaments use the same vocabulary now), fix immediately and audit.


---

## Sub-rule (2026-05-15): Standalone אֲדֹנָי as prayer-vocative

**Decision:** When אֲדֹנָי (Adonay, plural-of-majesty) appears **standalone** in a **direct prayer-vocative** to God (i.e., not in the compound אֲדֹנָי יְהוִה, and not as a third-person title), render as **`องค์พระผู้เป็นเจ้าของข้าพระองค์`** ("my Lord").

**Canonical precedent:** Num 14:17 — Moses' intercession after the spies-rebellion: וְעַתָּה יִגְדַּל־נָא כֹּחַ אֲדֹנָי → "ขอพระอานุภาพ**ขององค์พระผู้เป็นเจ้าของข้าพระองค์**ทรงสำแดงพระเกียรติยิ่งใหญ่".

**Rationale:** The Adonay morphology (-ay ending) is read by morphology-sensitive translations (LEB, etc.) as honorific-possessive ("my Lord"). In direct prayer-vocative contexts, the warmer possessive Thai matches the intimate register Hebrew preserves. Confirmed by external AI cross-check (ChatGPT/Gemini/Logos 2026-05-15) — Logos AI explicitly cited LEB's morphology-sensitive treatment.

**What this does NOT cover:**
- אֲדֹנָי יְהוִה compound → separate locked compound form (see main table).
- אֲדֹנָי used as third-person title in narrative → `องค์เจ้านาย` (master/Lord-title).
- אֲדֹנִי (single-yodh, "my lord" addressed to humans like Moses or kings) → `เจ้านายของข้าพเจ้า` / context-appropriate.

**Forward protection:** This rule will govern standalone Adonai prayer-vocatives throughout Psalms, Isaiah, Ezekiel, Daniel. Documented as part of NUM end-of-book audit (item F) before any Psalter chapter ships.

---

## Sub-rule (2026-05-18): Adonai 4-way distinction — JOS 7:7–8 anchor

**Triggered by:** JOS audit Item E + 3-way external AI review (Grok / Gemini / ChatGPT). The shipped JOS 7:7-8 prayer demonstrates a principled within-prayer distinction that the 2026-05-15 sub-rule above did not fully cover: a *direct vocative interjection* `בִּי אֲדֹנָי` ("please, my Lord!") was rendered **`ข้าแต่องค์เจ้านาย`**, while the compound `אֲדֹנָי יְהוִה` in the same prayer was rendered **`ข้าแต่องค์พระผู้เป็นเจ้า`**. The 2026-05-15 sub-rule's surface (`องค์พระผู้เป็นเจ้าของข้าพระองค์`) was anchored on NUM 14:17, which is *possessive* Adonai (`כֹּחַ אֲדֹנָי` = "the power of my Lord") — a different syntactic position from JOS 7:8's vocative interjection.

**The 4-way distinction (LOCK as of 2026-05-18):**

| Hebrew form | Syntactic context | Locked Thai | Anchor |
|---|---|---|---|
| **אֲדֹנָי יְהוִה** (compound) | Any (prayer or narrative) | **องค์พระผู้เป็นเจ้า** (vocative: **ข้าแต่องค์พระผู้เป็นเจ้า**) | JOS 7:7 / Gen 15:2 |
| **אֲדֹנָי** standalone, **direct vocative interjection** in prayer | בִּי אֲדֹנָי, אֲהָהּ אֲדֹנָי, אָנָּא אֲדֹנָי | **ข้าแต่องค์เจ้านาย** | **JOS 7:8** (locking precedent) |
| **אֲדֹנָי** standalone, **possessive / genitive within a prayer** | כֹּחַ אֲדֹנָי and similar | **องค์พระผู้เป็นเจ้าของข้าพระองค์** (per 2026-05-15 sub-rule) | NUM 14:17 |
| **אֲדֹנָי / אֲדֹנֵי** title, **third-person reference** (not in prayer-address) | Narrative use, "the Lord said" | **องค์เจ้านาย / องค์เจ้านายของบรรดาเจ้านาย** | Gen 18:27, Deut 10:17 |
| **אֲדֹנִי** (single-yodh, addressing humans/angels) | "my lord" to Moses, kings, angels | **เจ้านายของข้าพเจ้า** / context-appropriate | Gen 24:12, Num 32:25 |

**Why this distinction matters:** within a single prayer, Hebrew alternates between the compound אֲדֹנָי יְהוִה (rare, weighty) and standalone אֲדֹנָי (common, intimate vocative). The Thai must preserve that alternation so the reader feels the same register shift the Hebrew preserves. JOS 7:7-8 is the cleanest single-prayer example in the OT and is therefore the locking anchor.

**Boundary with the 2026-05-15 sub-rule:** the 2026-05-15 rule applies to *possessive* standalone Adonai inside prayer (`כֹּחַ אֲדֹנָי` and similar genitive constructions); this 2026-05-18 rule applies to *direct vocative interjections* (`בִּי אֲדֹנָי`, `אֲהָהּ אֲדֹנָי`, `אָנָּא אֲדֹנָי`). The two rules are complementary, not contradictory.

**Forward protection:** Psalms (frequent `אֲדֹנָי` vocatives in laments), Daniel 9 (Daniel's prayer — multiple Adonai vocatives), Lamentations, Ezra 9 (penitential prayer). Translators ship-working those books default to the 4-way distinction above; the JOS 7:7-8 surface is the precedent.

---

## Sub-rule (2026-05-20): Recognition-arc principle — JDG 6:15 → 6:22 anchor

**Triggered by:** JDG audit Item B + 2-way external AI review (ChatGPT + Gemini, convergent MAJOR-CONCERN verdict on Adonai-in-prayer 5-form drift across JOS + JDG). The Judges audit applied the JOS 7:7–8 4-way distinction under pressure and surfaced an additional principle the JOS audit did not name: the *same Hebrew form* (אֲדֹנִי vs אֲדֹנָי) can correspond to two distinct Thai surfaces depending on whether the human speaker has yet recognized the divine identity of the figure being addressed.

**The recognition-arc:**

| Stage | Hebrew form | Sense | Thai surface | Anchor |
|---|---|---|---|---|
| **Pre-recognition** — speaker addresses figure as "my lord" not yet knowing it is divine | **אֲדֹנִי** (single-yodh; possessive "my lord") | Human / angelic address; speaker treats figure as an angel-courier or distinguished stranger | **เจ้านายของข้าพเจ้า** / **ท่านนายของข้าพเจ้า** | **JDG 6:15** (Gideon to the angel-of-YHWH, before recognition) |
| **Post-recognition** — speaker realizes figure is divine and switches to the formal compound vocative | **אֲדֹנָי יְהוִה** (compound) | Formal divine address; speaker now knows the encounter is theophanic / angelophanic with divine identification | **ข้าแต่องค์พระผู้เป็นเจ้า** | **JDG 6:22** (Gideon's response after recognition: "Alas, Lord GOD! I have seen the angel of YHWH face to face!") |

**Rationale:** the JDG 6:15 → 6:22 pericope is the single cleanest **within-pericope register-shift anchor** in the OT. Gideon's pre-recognition אֲדֹנִי at v.15 and his post-recognition אֲדֹנָי יְהוִה at v.22 are separated by only 7 verses and involve the same speaker addressing the same figure — making the register-shift unambiguously diagnostic of *speaker awareness*, not of Hebrew form alone. Translating both with the same Thai surface (or worse, treating v.15 as if Gideon already knew it was divine) would flatten the narrative arc the Hebrew author explicitly constructed.

**Forward protection for analogous theophany / angelophany scenes:**

1. **GEN 18:1–33** (Abraham at Mamre) — Abraham initially addresses the three visitors as `אֲדֹנָי` ("my lords" / "my lord" — singular MT, plural some witnesses) at v.3 without certainty whether they are divine; by v.22 the narrative makes clear at least one of them is YHWH. Apply the recognition-arc principle: v.3 = pre-recognition `ข้าแต่ท่านนาย` (singular, registering Abraham's hospitality-host stance to apparent travelers); subsequent address shifts to post-recognition forms as the narrative develops.

2. **GEN 32:23–33** (Jacob at Peniel) — Jacob wrestles with "a man" (אִישׁ, v.25), then realizes "I have seen God face-to-face" (v.31). The man is never called אֲדֹנִי / אֲדֹנָי in dialogue, but the recognition-arc structure (man → divine figure) is parallel.

3. **JOS 5:13–15** (Joshua and the Commander of YHWH's host) — Joshua initially asks "are you for us or for our adversaries?" (v.13, pre-recognition, addressing as `אֲדֹנִי` is implicit but the speech is direct interrogation, not vocative); by v.14 he falls on his face and worships, recognition complete. The JOS 5:15 holy-ground formula (`שַׁל־נַעַלְךָ`) verbally matches EXO 3:5 and signals divine identity. See [[captain_of_yhwh_host_2026-05]] for the parallel register handling.

4. **JDG 13:1–22** (Manoah and the angel of YHWH) — Manoah's pre-recognition address at v.11 ("Are you the man…?" — not vocative) and his post-recognition fear at v.22 ("We shall surely die, for we have seen God!") — but note that v.8 (`בִּי אֲדוֹנָי`) is **already post-Annunciation** (the angel has already revealed to Manoah's wife in vv.3–5), so it falls under the 2026-05-18 sub-rule (standalone vocative-interjection prayer → `ข้าแต่องค์เจ้านาย`), not the pre-recognition category. The recognition-arc principle and the 4-way Adonai sub-rule are complementary, not overlapping.

5. **2 KGS 6:15–17** (Elisha's servant and the chariots of fire) — pre-/post-recognition of the angelic host. Use the recognition-arc principle.

**Boundary with the 4-way Adonai sub-rule (2026-05-18):** the 4-way distinction governs the *form-to-Thai mapping* once the speaker's recognition-stage is known. The recognition-arc principle (this sub-rule) governs *which stage the speaker is in* when the Hebrew uses formally ambiguous אֲדֹנִי. The two rules compose: first determine recognition-stage from the narrative arc (this sub-rule), then apply the 4-way mapping (2026-05-18 sub-rule) within that stage.

**No retroactive verse edits required from JDG audit Item B beyond the 3 already applied (JDG 6:22, 13:8, 16:28).** JDG 6:15 was already shipped with the correct pre-recognition Thai (`ข้าแต่ท่านนายของข้าพเจ้า`); this sub-rule documents the principle it embodies so future theophany / angelophany scenes inherit the pattern.

---

## Sub-rule (2026-05-23): Adonai-YHWH compound vocative — sentence position determines particle

**Triggered by:** 2 SA audit Item B + 2-way external AI review (ChatGPT + Gemini, convergent FINE verdict on 2 Sam 7:18–29 — confirming the bare `องค์พระผู้เป็นเจ้า` is correct in mid-sentence appositional prayer-address). The 2026-05-18 4-way Adonai sub-rule did not explicitly distinguish *sentence-initial interjection* compound vocatives from *mid-sentence appositional* compound vocatives. 2 Sam 7's "David's covenant prayer" is the cleanest mid-sentence anchor in the OT for the appositional form (אֲדֹנָי יְהוִה repeated 7 times in vv.18–29, all mid-sentence, none after `אֲהָהּ`/`בִּי`/`אָנָּא`).

**The position-determines-particle distinction:**

| Compound vocative environment | Hebrew shape | Thai surface | Anchor |
|---|---|---|---|
| **Sentence-initial interjection / plea** | `אֲהָהּ אֲדֹנָי יְהוִה` / `בִּי אֲדֹנָי יְהוִה` / `אָנָּא אֲדֹנָי יְהוִה` | **`ข้าแต่องค์พระผู้เป็นเจ้า`** | JOS 7:7 (Joshua's lament after Ai) |
| **Mid-sentence appositional prayer address** | `אֲדֹנָי יְהוִה` (without preceding interjection particle) | **`องค์พระผู้เป็นเจ้า`** (bare) | **2 SA 7:18–29** (David's covenant prayer) |

**Rationale:** Thai `ข้าแต่` is a sentence-initial deferential vocative particle. Forcing it into mid-sentence appositional environments produces unnatural Thai repetition — and over-formalizes the prayer in places where Hebrew itself uses the bare compound without an interjection particle. 2 SA 7:18–29 demonstrates this clearly: David alternates between sustained address ("you, O Lord GOD" — appositional) and direct statement ("therefore you are great, O Lord GOD" — also appositional), and across 7 occurrences in 12 verses, none use the interjection-particle preface. Treating all of them as `ข้าแต่` would corrupt the natural flow of the Thai prayer and obscure the deliberate Hebrew distinction between formal plea (interjection-particle + vocative) and sustained covenant address (bare vocative).

**Composition with prior Adonai sub-rules:**

- **2026-05-15 sub-rule** (possessive standalone Adonai in prayer → `องค์พระผู้เป็นเจ้าของข้าพระองค์`): governs **possessive/genitive** position of standalone אֲדֹנָי.
- **2026-05-18 sub-rule** (4-way distinction): governs the form-to-Thai mapping for standalone אֲדֹנָי vocatives and the compound אֲדֹנָי יְהוִה default (`ข้าแต่องค์พระผู้เป็นเจ้า`).
- **2026-05-20 sub-rule** (recognition-arc): governs *which stage* the speaker is in for formally ambiguous אֲדֹנִי addresses.
- **2026-05-23 sub-rule** (this rule): refines the 2026-05-18 default — `ข้าแต่` applies to **sentence-initial interjection** compounds; bare `องค์พระผู้เป็นเจ้า` applies to **mid-sentence appositional** compounds.

The 4 sub-rules compose without overlap: position (this rule) → recognition-stage (2026-05-20) → form-to-Thai (2026-05-18) → possessive special-case (2026-05-15).

**Forward protection:**

1. **Psalms 71:5; 109:21; 140:7** — `כִּי־אַתָּה תִקְוָתִי אֲדֹנָי יְהוִה` and similar appositional address constructions: apply bare `องค์พระผู้เป็นเจ้า`.

2. **Isaiah 25:8; 28:16; 30:15; 40:10; 48:16; 49:22; 50:4–9; 52:4; 56:8; 61:1, 11; 65:13, 15** — Isaiah is the OT book with the highest density of compound אֲדֹנָי יְהוִה (~30 occurrences). Most are **mid-sentence appositional** (e.g., `כֹּה אָמַר אֲדֹנָי יְהוִה` — "thus says the Lord GOD"). Apply bare `องค์พระผู้เป็นเจ้า` for these prophetic-formula appositions; reserve `ข้าแต่องค์พระผู้เป็นเจ้า` for sentence-initial interjection prayer-vocatives (e.g., Jer 1:6; 4:10; 14:13; 32:17, 25; Ezek 4:14; 9:8; 11:13; 20:49 — Jeremiah and Ezekiel both have `אֲהָהּ אֲדֹנָי יְהוִה` as a prophet's lament-interjection).

3. **Amos 1:8; 3:7–8, 11, 13; 4:2, 5; etc.** — heavy use of `אֲדֹנָי יְהוִה צְבָאוֹת` ("Lord GOD of hosts") in prophetic formulas: apply `องค์พระผู้เป็นเจ้าจอมโยธา` (mid-sentence appositional).

**No retroactive verse edits required for 2 SA 7:18–29** — already shipped with the correct bare `องค์พระผู้เป็นเจ้า` for each compound occurrence. This sub-rule documents the principle that 2 SA 7 embodies so future Psalms / Isaiah / Jeremiah / Ezekiel / Amos compound-vocative scenes inherit the pattern.
