# Hebrew proper names and place-names — transliteration policy

**Scope:** All Hebrew/Aramaic proper nouns in the OT — personal names, place names, tribal/clan names, river/mountain names, foreign king names, ethnic groups. Plus the policy for adopting THSV11 / TNCV name conventions as the baseline.

**Decided:** 2026-05-04 (per plan §6 + Gemini #5 recommendation).

---

## Core policy: THSV11/TNCV baseline + override only when needed

The OT contains **thousands** of proper names — every patriarch, every clan member, every place, every foreign king. Transliterating each from Hebrew first-principles for every chapter would (a) consume enormous translator time, (b) produce inconsistencies as different transliteration choices accumulate, (c) confuse Thai Bible readers who already know names from THSV11 / TNCV.

**Decision:** Adopt the THSV11 (Thai Standard Version 2011) + TNCV (Thai New Contemporary Version) transliteration baseline as the **default** for all OT proper names. Override the default only when:

1. The default name introduces a **factual error** (e.g., conflates two distinct biblical figures with the same name).
2. The default contradicts **Hebrew phonology** in a way that misleads readers about the underlying name (rare — THSV11 is generally faithful).
3. **Theological wordplay** in the verse turns on the name's etymology, and the THSV11 form obscures it (rare; document the override in `key_decisions`).
4. The name is **transliterated inconsistently** across THSV11 itself, and Eremos must pick one form for canonical consistency.

Default transliteration data: `data/proper_names_thsv11_baseline.json` (to be built; see §5 below for build process).

---

## Why baseline-adoption rather than first-principles transliteration

- **Reader recognition.** Thai Bible readers already know Abraham as `อับราฮัม`, David as `ดาวิด`, Jerusalem as `กรุงเยรูซาเล็ม`. Reinventing these would alienate readers.
- **Eremos NT precedent.** The NT translation has used THSV11-aligned forms for the major Old-Testament-mentioned names (Abraham, Moses, David, Solomon, Elijah, etc.). Adopting THSV11 baseline keeps the OT-NT name continuity consistent within Eremos itself.
- **Translator time.** ~2,000+ proper names in the OT. First-principles transliteration on each = months of work. Baseline + override = days.
- **Consistency mechanism.** A single baseline file eliminates the "Asaph in 2 Chr was rendered as อาสาฟ but in Pss as อาซัฟ" failure mode.

---

## Specific cases that need explicit decision

### Patriarchs and matriarchs

| Hebrew | THSV11 baseline | Notes |
|---|---|---|
| אַבְרָהָם | **อับราฮัม** | Use throughout. Pre-renaming אַבְרָם → **อับราม** (Genesis 11–17) |
| יִצְחָק | **อิสอัค** | |
| יַעֲקֹב | **ยาโคบ** | The Israel rename: יִשְׂרָאֵל → **อิสราเอล** (Genesis 32–35) |
| שָׂרָה | **ซาราห์** | Pre-renaming שָׂרַי → **ซาราย** |
| רִבְקָה | **เรเบคาห์** | |
| לֵאָה | **เลอาห์** | |
| רָחֵל | **ราเชล** | |
| יוֹסֵף | **โยเซฟ** | |
| יְהוּדָה | **ยูดาห์** | |

### Major prophets

| Hebrew | THSV11 baseline | Notes |
|---|---|---|
| מֹשֶׁה | **โมเสส** | Adopt THSV11. (Note: NT corpus already uses Greek-form **โมเสส** = Μωυσῆς in Acts/Heb; matches OT) |
| אַהֲרֹן | **อาโรน** | |
| יְהוֹשֻׁעַ | **โยชูวา** | The Yeshua/Joshua name. Pre-renaming הוֹשֵׁעַ → **โฮเชยา** (Numbers 13:8, 16) |
| שְׁמוּאֵל | **ซามูเอล** | |
| אֵלִיָּהוּ | **เอลียาห์** | (NT corpus: same — Ἠλίας, Mark 9:4, James 5:17) |
| אֱלִישָׁע | **เอลีชา** | |
| יְשַׁעְיָהוּ | **อิสยาห์** | |
| יִרְמְיָהוּ | **เยเรมีย์** | |
| יְחֶזְקֵאל | **เอเสเคียล** | |
| דָּנִיֵּאל | **ดาเนียล** | |

### Minor prophets

| Hebrew | THSV11 baseline |
|---|---|
| הוֹשֵׁעַ | **โฮเชยา** |
| יוֹאֵל | **โยเอล** |
| עָמוֹס | **อาโมส** |
| עֹבַדְיָה | **โอบาดีห์** |
| יוֹנָה | **โยนาห์** |
| מִיכָה | **มีคาห์** |
| נַחוּם | **นาฮูม** |
| חֲבַקּוּק | **ฮาบากุก** |
| צְפַנְיָה | **เศฟันยาห์** |
| חַגַּי | **ฮักกัย** |
| זְכַרְיָה | **เศคาริยาห์** |
| מַלְאָכִי | **มาลาคี** |

### Kings of Israel + Judah

The two-kingdom history has ~40 kings; THSV11 baseline applies. The full king-list will be loaded into `data/proper_names_thsv11_baseline.json`. Spot-check:

- דָּוִד → **ดาวิด**
- שְׁלֹמֹה → **ซาโลมอน**
- חִזְקִיָּהוּ → **เฮเซคียาห์**
- יֹאשִׁיָּהוּ → **โยสิยาห์**
- אַחְאָב → **อาฮับ**
- יָרָבְעָם → **เยโรโบอัม**

### Foreign kings (Egyptian, Babylonian, Persian)

| Hebrew | THSV11 baseline |
|---|---|
| פַּרְעֹה | **ฟาโรห์** (title; not a personal name except where one Pharaoh is specified) |
| נְבוּכַדְנֶצַּר | **เนบูคัดเนสซาร์** |
| בֶּלְשַׁאצַּר | **เบลชัสซาร์** |
| כּוֹרֶשׁ | **ไซรัส** (Cyrus; Latinized form is dominant in Thai Bible reading tradition) |
| דָּרְיָוֶשׁ | **ดาริอัส** |
| אַחַשְׁוֵרוֹשׁ | **อาหสุเอรัส** (= Xerxes; THSV11 uses Hebrew-form אחשורוש transliterated, not the Persian/Greek form) |

### Geographic names

| Hebrew | THSV11 baseline |
|---|---|
| יְרוּשָׁלִַם | **กรุงเยรูซาเล็ม** (with `กรุง` city-prefix) |
| צִיּוֹן | **ศิโยน** |
| בֵּית־לֶחֶם | **เบธเลเฮม** |
| חֶבְרוֹן | **เฮโบรน** |
| שְׁכֶם | **เชเคม** |
| הַיַּרְדֵּן | **แม่น้ำจอร์แดน** |
| יָם הַמֶּלַח / יָם הַעֲרָבָה | **ทะเลตาย / ทะเลเกลือ** (semantic-translate, not transliterate) |
| מִצְרַיִם | **อียิปต์** (use the modern Thai country-name; readers know "อียิปต์", not transliterated מצרים) |
| אַרַם | **อารัม** (literal) or **ซีเรีย** (modern equivalent) — context-dependent; OT-historical contexts use **อารัม**, NT contexts already use Greek-form **ซีเรีย** |
| בָּבֶל | **บาบิโลน** |
| אַשּׁוּר | **อัสซีเรีย** |

### Tribal / clan / ethnic names

| Hebrew | THSV11 baseline |
|---|---|
| בְּנֵי יִשְׂרָאֵל | **วงศ์วานอิสราเอล / ลูกหลานอิสราเอล / คนอิสราเอล** (context: tribal-collective vs ethnic) |
| לֵוִיִּם | **คนเลวี / คณะเลวี** |
| כְּנַעֲנִי | **คานาอัน** (the place) / **ชาวคานาอัน** (the people) |
| פְּלִשְׁתִּים | **ฟิลิสเตีย** (the people; THSV11 uses ethnic-noun form) |
| חִתִּים | **ฮิตไทต์** (modern English-via-Thai loanword) or **ฮิตเชย** (Hebrew-form) — THSV11 uses **คนฮิตไทต์** |
| מוֹאָב / עַמּוֹן / אֱדוֹם | **โมอับ / อัมโมน / เอโดม** |

### Special-case loanwords (Greek/Latin via Thai-Christian tradition)

A small set of OT terms have entered Thai through the Greek/Latin/English channel rather than direct Hebrew transliteration. Where Thai-Christian-Bible tradition strongly attests these, Eremos retains them and documents the underlying Hebrew etymology in a Layer-2 footer at first occurrence rather than forcing first-principles Hebrew phonology.

| Hebrew | Eremos Thai | Why this form | Layer-2 etymology footer |
|---|---|---|---|
| יוֹבֵל (yobel) | **ปีจูบีลี** (Jubilee year) | Latin `iubilaeus` → English Jubilee → Thai `จูบีลี`; long-established Thai-Christian-Bible tradition (THSV11/TNCV); reader recognition outweighs phonology preservation. The metonymy "year named after the ram's-horn instrument that announces it" is recoverable via footer. | LEV 25:10 (first occurrence) — explains that יוֹבֵל literally means "ram's horn" and notes Joshua 6's `שׁוֹפְרוֹת הַיּוֹבְלִים` (trumpets-of-yobel) connection. Documented 2026-05-16 cross-AI review. |

The decision rule for "is this a special-case loanword": (a) does Thai-Christian-Bible tradition unambiguously attest a single form? (b) is the Hebrew underlying word a *name-of-a-thing* (not a proper noun for a person/place)? (c) does retaining the tradition word lose a *visible* Hebrew wordplay or typological metonymy? — if (a) and (b) are yes and (c) is the only loss, document the loss in a Layer-2 footer and retain the tradition word.

---

## When to override the THSV11 baseline

### Override #1: factual error in baseline

Example: if THSV11 conflates two biblical figures with the same Hebrew name into one Thai form when they are clearly distinct (e.g., two different `אֲבִיָּם` characters in 1 Kings vs. 2 Chronicles), Eremos disambiguates with a contextual qualifier.

Document in: `key_decisions` for the verse + a footnote distinguishing "Abijam king of Judah" vs. "Abijah son of Jeroboam".

### Override #2: theological wordplay obscured

Example: the Eve-namegiving in Gen 3:20 — `חַוָּה` ("life") given because she is the mother of all living. The Thai form `เอวา` (THSV11) is fine but doesn't encode the wordplay. Override in this verse: keep `เอวา` in main text + add a footnote explaining the etymological wordplay.

Document in: `key_decisions` + verse-level footer note.

### Override #3: inconsistent THSV11 transliteration

Some THSV11 names appear in two forms across the canon (typesetting drift). Pick one for Eremos canonical consistency. Document in `data/proper_names_thsv11_baseline.json` with a note about which form was canonicalized + why.

### Override #4: name compound that needs semantic-translation

Place-name compounds where the meaning is the point (e.g., `בְּאֵר־לַחַי־רֹאִי` "Beer-lahai-roi" = "the well of the Living-One who sees me" in Gen 16:14): transliterate the Hebrew compound (`เบเออร์ลาฮัยโรอี`) + footnote the meaning. Same pattern as the YHWH-compound place-names in `divine_names_table_2026-05.md`.

---

## Build process for `data/proper_names_thsv11_baseline.json`

### Phase A — pre-Gen 1 (Day 14, per plan §20 Track B)

Build the baseline file from a one-time scrape of the THSV11 OT text (PD; via STEP Bible or other OSI-friendly Thai-text source). The scrape extracts every proper noun (identified via Hebrew morphology in `morphhb` paired with the Thai translation) and produces a JSON file:

```json
{
  "אַבְרָהָם": {
    "thai": "อับราฮัม",
    "thai_alternates": ["อับราฮัม"],
    "first_occurrence": "GEN 11:26",
    "category": "patriarch",
    "notes": "Renamed from אַבְרָם (อับราม) at Gen 17:5"
  },
  "יְרוּשָׁלִַם": {
    "thai": "เยรูซาเล็ม",
    "thai_alternates": ["กรุงเยรูซาเล็ม"],
    "first_occurrence": "JOS 10:1",
    "category": "place_name",
    "notes": "Use 'กรุงเยรูซาเล็ม' in narrative prose; 'เยรูซาเล็ม' alone is acceptable in poetry/prophetic discourse"
  }
}
```

### Phase B — incremental override accumulation

As translation progresses, every override (per the four override criteria above) is logged in `key_decisions` AND appended to the baseline file as a deviation row.

### Phase C — corpus-wide audit at end-of-OT

End of phase 6H (Twelve Prophets), run a corpus-wide proper-name consistency audit: every proper-name occurrence must map to its baseline-file entry; deviations must be justified.

---

## When to revisit

- **Pilot-end review** (after Ruth + Jonah + Gen 1–11 ship) — review the baseline file. Adjust if the Thai-language reviewer / maintainer find systematic THSV11-form issues.
- **Per-phase boundary** — re-confirm the baseline still applies; THSV11 conventions can drift across genre.
- **If a Phase-6 book introduces a wave of new proper names** (Joshua tribal-allotments, 1 Chr genealogies, Ezra-Neh names) — verify baseline coverage is sufficient before starting; build out the file if not.
