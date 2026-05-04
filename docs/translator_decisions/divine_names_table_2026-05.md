# Divine names — table of OT renderings (Tetragrammaton + family)

**Scope:** Every form of the divine name and divine epithet that appears in the Hebrew Old Testament, plus a few Aramaic equivalents in Daniel/Ezra. Includes the Tetragrammaton (יהוה), the Adonai-YHWH compound (אֲדֹנָי יְהוִה), the title-clusters (יְהוָה צְבָאוֹת etc.), and the El-compound names (אֵל שַׁדַּי, אֵל עֶלְיוֹן, etc.).

**Decided:** 2026-05-04 (Ben).
**Approach:** **THSV11 "Historical" — transliterate the Tetragrammaton.**
**Reversibility clause:** Ben explicitly noted "if we need to come back later and change the yahweh/LORD debate historical vs similarity, we will." A project-wide find-replace migration is permitted if reader feedback warrants. Until then, the renderings below are locked.

**Evidence base for the lock:**
- THSV11 (Thai Standard Version 2011) renders יהוה as `พระยาห์เวห์`. Modern Thai scholarly translation precedent.
- Hebrew direct-transliteration approach matches NRSV/NJPS scholarly tradition, prioritizes OT historical accuracy over visual canonical unity with the NT.
- The trade-off (visual disconnect with the already-shipped Eremos NT, which uses `องค์พระผู้เป็นเจ้า` for κύριος-as-YHWH) is **explicitly accepted** by Ben, with documentation mitigations in `RULES.md §B18` and the per-verse `check_nt_quotation_alignment.py` flag.

---

## The full table (locked)

| Hebrew | Transliteration | Default Thai | Where this rendering applies |
|---|---|---|---|
| יהוה (Tetragrammaton) | YHWH / Yahweh | **พระยาห์เวห์** | Project-wide; the cornerstone lock |
| אֲדֹנָי יְהוִה (Adonai YHWH; "Lord GOD") | Adonai Yahweh | **พระยาห์เวห์องค์เจ้านาย** | Genesis 15:2, Ezekiel-frequent, Amos. Avoids the awkward "Lord Lord" double-honorific |
| יְהוָה צְבָאוֹת (YHWH Tsebaoth; "of hosts") | Yahweh Tsebaoth | **พระยาห์เวห์จอมโยธา** | Isaiah, Jeremiah, Zechariah heavy. **Note:** the already-shipped Eremos NT renders κύριος Σαβαώθ at James 5:4 as `องค์พระผู้เป็นเจ้าจอมโยธา`. The OT rendering here intentionally diverges — the second word `จอมโยธา` ("of hosts") is identical, only the first word differs |
| יָהּ (Yah; short form) | Yah | **ยาห์** | Psalms 68:4, 77:11; הַלְלוּ-יָהּ "Hallelu-Yah" closing formula in Pss 113–118, 146–150 |
| אֱלֹהִים (Elohim) | Elohim | **พระเจ้า** | Most-frequent name; matches NT θεός |
| אֱלוֹהַּ (Eloah, sg. of Elohim) | Eloah | **พระเจ้า** | Job-frequent (~41×); Hab, Deut, Pss; Aramaic Job & Daniel parallel אֱלָהּ |
| אֵל (El, standalone) | El | **พระเจ้า** | Standalone; in compound names below, transliterate as **เอล-** |
| אֲדֹנָי (Adonai, standalone, of God) | Adonai | **องค์เจ้านาย** | Aligns with Adonai-YHWH compound; matches NT δεσπότης pattern (e.g., 2 Pet 2:1) |
| שַׁדַּי (Shaddai) | Shaddai | **ผู้ทรงมหิทธิฤทธิ์** ("Almighty") | Genesis-patriarchal, Job |
| אֵל שַׁדַּי (El Shaddai) | El Shaddai | **พระเจ้าผู้ทรงมหิทธิฤทธิ์** | Genesis 17:1, 28:3, 35:11, 43:14, 48:3, 49:25; Exodus 6:3 |
| אֵל עֶלְיוֹן (El Elyon) | El Elyon | **พระเจ้าผู้สูงสุด** | Genesis 14:18–22 (Melchizedek scene) |
| אֵל עוֹלָם (El Olam) | El Olam | **พระเจ้านิรันดร์** | Genesis 21:33 |
| אֵל רֳאִי (El Ro'i) | El Ro'i | **เอลโรอี** + footnote ("พระเจ้าผู้ทรงเห็นข้าพเจ้า") | Genesis 16:13 (Hagar-specific). Transliterate; gloss the meaning in footnote because Hagar's wordplay is the point |
| יהוה־יִרְאֶה (YHWH-Yireh) | Yahweh-Yireh | **ยาห์เวห์ยีเรห์** + footnote ("พระยาห์เวห์ทรงจัดเตรียม") | Genesis 22:14. Place-name compound; transliterate the proper-name form (note: short form יהוה here in the place-name, not the full พระ-prefixed Tetragrammaton — keeps it readable as a place rather than a divine title) |
| יהוה־נִסִּי (YHWH-Nissi) | Yahweh-Nissi | **ยาห์เวห์นิสซี** + footnote | Exodus 17:15 |
| יהוה־שָׁלוֹם (YHWH-Shalom) | Yahweh-Shalom | **ยาห์เวห์ชาโลม** + footnote | Judges 6:24 |
| יהוה־צִדְקֵנוּ (YHWH-Tsidkenu) | Yahweh-Tsidkenu | **ยาห์เวห์ซิดเคนู** + footnote | Jeremiah 23:6, 33:16 |
| יהוה רֹעִי (YHWH ro'i) | YHWH my shepherd | **พระยาห์เวห์ผู้เลี้ยงดูข้าพเจ้า** | Psalm 23:1. Not a place-name, so the full พระ-prefixed Tetragrammaton applies |
| יהוה־שָׁמָּה (YHWH-Shammah) | Yahweh-Shammah | **ยาห์เวห์ชัมมาห์** + footnote | Ezekiel 48:35 |
| אֶהְיֶה אֲשֶׁר אֶהְיֶה (Ehyeh Asher Ehyeh) | "I AM WHO I AM" | **(separate decision doc)** | Exodus 3:14. The cardinal divine self-disclosure; needs its own treatment because it is not a name in the table-of-names sense — it is the verb-formula that grounds the Tetragrammaton |

### Aramaic equivalents (for Daniel + Ezra)

| Aramaic | Default Thai | Notes |
|---|---|---|
| אֱלָהּ (elah; sg.) | **พระเจ้า** | Equivalent of Hebrew אֱלוֹהַּ |
| אֱלָהָא (elaha; emphatic) | **พระเจ้า** | |
| מָרֵא־מַלְכִין / מָרֵא־שְׁמַיָּא (Mare-Malkin / Mare-Shemayya) | **องค์เจ้านายแห่งกษัตริย์ทั้งหลาย** / **องค์เจ้านายแห่งฟ้าสวรรค์** | Daniel 2:47, 5:23; "Lord of kings" / "Lord of heaven" titles |
| עִלָּאָה (Illaya; "the Most High") | **ผู้สูงสุด** | Daniel 4–7 frequent |

---

## Why "พระ" prefix on the Tetragrammaton (พระยาห์เวห์) but not on place-name compounds (ยาห์เวห์ยีเรห์)

Two registers are at play:

- **Direct address / divine reference** — full deferential prefix. `พระยาห์เวห์` reads as "Lord Yahweh" with the พระ honorific prefix. This is how a Thai reader would expect a divine name to feel in formal scripture.
- **Place-name** — transliterate as a phonetic name, no prefix. `ยาห์เวห์ยีเรห์` reads as a proper place name, like an English reader would read "Yahweh-Yireh." The honorific would feel out of place ("Lord Yahweh-Yireh" doesn't make sense — it's the place's name, not a deferential reference to the deity).

This distinction is preserved across all compound names: when YHWH compounds with a verb/noun *as a place-name or memorial* (יהוה־יִרְאֶה, etc.), the prefix is dropped. When YHWH appears *as the divine subject* of a verb (יהוה רֹעִי, "YHWH my shepherd" in Ps 23:1), the prefix is retained.

---

## Why this differs from the NT corpus (and why that's OK)

The Eremos NT — already shipped through ~92% of the canon — renders `κύριος` (when it stands for YHWH in OT quotations or in Hebraic constructions) as `องค์พระผู้เป็นเจ้า`. This was the right call for the NT because:

1. The NT Greek author wrote `κύριος`, not the Tetragrammaton. We translate the Greek author's *word choice*, not the underlying Hebrew that may or may not have stood behind it.
2. The κύριος-tradition (Septuagint / NT) was deliberately constructed as a *titular* rendering, not a transliteration. Honoring that titular tradition for the NT is faithful to the NT's own translation move.

The OT will use `พระยาห์เวห์`. This **is** a visual disconnect from the NT corpus when the NT cites the OT. Examples:

- **Psalm 110:1** — OT renders: `พระยาห์เวห์ตรัสกับองค์เจ้านายของข้าพเจ้า`. NT-cited at Mark 12:36 / Heb 1:13 already shipped as: `องค์พระผู้เป็นเจ้าตรัสกับองค์เจ้านายของข้าพเจ้า`.
- **Joel 2:28–32 / Acts 2:17–21** — OT will render `יהוה` as `พระยาห์เวห์`. NT shipped as `องค์พระผู้เป็นเจ้า`.
- **Habakkuk 2:4 / Romans 1:17** — OT will render `יהוה` references as `พระยาห์เวห์`; NT shipped as `องค์พระผู้เป็นเจ้า`.

**This is intentional.** Three mitigations make it survivable:

1. **`check_nt_quotation_alignment.py`** flags every NT-cited OT verse and requires a `key_decisions` entry confirming the historical-transliteration choice was applied. This makes the divergence visible in audit and prevents accidental drift in either direction.
2. **`thai_summary` cross-references** for major NT-quoted OT passages explicitly call out the cross-corpus connection — e.g., for Ps 110:1: "พระยาห์เวห์ตรัสกับองค์เจ้านายของข้าพเจ้า — ข้อนี้พระเยซูทรงอ้างถึงในมาระโก 12:36 ที่นั่นใช้คำว่า 'องค์พระผู้เป็นเจ้า' ตามแบบแผนของฉบับพันธสัญญาใหม่."
3. **Reversibility clause.** If reader feedback turns sharply against the disconnect, the migration is one project-wide find-replace PR. This is documented in `RULES.md §B1` so the curator (Ben or future maintainer) knows the path.

---

## Adonai-YHWH compound — handling the "Lord GOD" double-honorific

Hebrew `אֲדֹנָי יְהוִה` is a fixed compound that appears most often in Genesis 15:2, the prophets (especially Ezekiel — ~217×), Amos, and the prayer of Moses in Deuteronomy 9:26. The Masoretes vocalized it specifically with the `Elohim` vowels (אֲדֹנָי יְהוִה) so that readers who already say `Adonai` for the Tetragrammaton would pronounce the compound as `Adonai Elohim` instead of saying `Adonai` twice.

English translations have the same problem and resolve it three ways:

- **Doubled small-caps:** "Sovereign LORD" (NIV), "Lord GOD" (NASB, ESV) — keeps the double form, lets typography distinguish.
- **Single rendering:** "the Sovereign LORD" treating the compound as one title.
- **Direct doubled rendering:** awkward and rare in modern English.

**Decision for Eremos OT:** `พระยาห์เวห์องค์เจ้านาย`. Order chosen for two reasons:

1. **Tetragrammaton first.** The compound is "Adonai *YHWH*" — YHWH is the operative divine name; Adonai is the deferential gloss prefix. Putting `พระยาห์เวห์` first keeps the Tetragrammaton's prominence.
2. **Adonai = องค์เจ้านาย.** This matches the standalone Adonai rendering and matches the NT corpus's δεσπότης rendering (e.g., 2 Pet 2:1, Jude 4 already shipped). So the second position is a known Eremos-corpus title, not a novel coinage.

The result reads naturally as "Lord Yahweh, the sovereign master." Avoids the double-honorific awkwardness without losing either component.

---

## Vocative direct address (when speaking to YHWH)

When the Hebrew has `יהוה` in second-person address (vocative) — most frequent in Psalms — the rendering is:

> **ข้าแต่พระยาห์เวห์**

The `ข้าแต่` is the standard Thai deferential vocative particle (matching NT's `ข้าแต่องค์พระผู้เป็นเจ้า` for κύριε in vocative).

For psalms that combine vocative + epithet:

- `יהוה אֱלֹהַי` (YHWH my God) → **ข้าแต่พระยาห์เวห์ พระเจ้าของข้าพเจ้า**
- `יהוה רֹעִי` (YHWH my shepherd) → not vocative in Ps 23:1; declarative — **พระยาห์เวห์ผู้เลี้ยงดูข้าพเจ้า**

---

## Hallelujah / הַלְלוּ-יָהּ formula

The closing-formula in Pss 113–118 + 146–150 reads `הַלְלוּ-יָהּ`. This is "Praise-Yah!" — short-form Tetragrammaton + plural imperative.

**Decision:**
- **Render:** **ฮาเลลูยาห์** (Thai-script transliteration of the full liturgical formula).
- **Why not break it apart** ("Praise Yah" / "จงสรรเสริญพระยาห์เวห์"): the formula is a fixed liturgical unit in both Jewish + Christian traditions, and Thai church readers already know `ฮาเลลูยาห์` as a worship-word. Translating it would feel pedantic.
- This is consistent with how Eremos NT renders the same word in Revelation 19:1, 3, 4, 6 (`ฮาเลลูยาห์`).

---

## Wordplay involving the divine name (small set of cases)

A few OT scenes turn on the meaning of the divine name itself, not just its phonetic form. These need verse-level treatment:

- **Exodus 3:13–15** — Moses asks for the divine name; God responds `אֶהְיֶה אֲשֶׁר אֶהְיֶה`, then `אֶהְיֶה`, then `יהוה`. The wordplay relies on the verb `הָיָה` (to be) phonetically connecting the verb-form `אֶהְיֶה` to the proper name `יהוה`. **Action:** separate decision doc (`exodus_3_14_divine_self_naming_2026-05.md`); cannot be auto-resolved by this table.
- **Ruth 1:20–21** — Naomi puns on `שַׁדַּי` (Shaddai) using רוּת homophonic plays. **Action:** verse-level handling in `key_decisions`; reference this table for the base rendering.
- **Numbers 6:24–26** (Aaronic blessing) — three uses of `יהוה` in liturgical structure. **Action:** standard `พระยาห์เวห์` rendering throughout; preserve the threefold structure visually if possible.

---

## What's NOT in scope for this doc

This doc covers **the divine name table only**. The following are separate:

- **Anthropomorphism policy** — see `hebrew_idioms_and_metaphor_2026-05.md` (planned)
- **Cultic/sanctuary register** — see `ot_register_policy_2026-05.md` (planned)
- **Rachasap policy** — see `ot_register_policy_2026-05.md` §B12.5
- **Wordplay on divine names** — see verse-level handling in `key_decisions`; this doc gives the base name only
- **Christological identification of OT YHWH passages with NT Christ** — see end-of-book Hebrews audit + `nt_quotation_alignment_2026-05.md`

---

## When to revisit

- **Reader feedback at end of pilot.** When Ruth → Jonah → Genesis 1–11 ship and Ben/Benz get reader response, if the disconnect from the NT corpus is judged too disruptive, run the find-replace migration. The flags are already in place via `check_nt_quotation_alignment.py`.
- **Specific compound that doesn't pattern.** If a divine-name compound surfaces during translation that this table doesn't anticipate, document it in `key_decisions` and append to this doc. Don't make ad-hoc renderings without recording them here.
- **NT regression.** If the OT Tetragrammaton rendering somehow leaks into NT translation work (unlikely — OT pipeline is feature-flagged), fix immediately and audit.
