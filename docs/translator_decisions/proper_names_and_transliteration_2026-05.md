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

### Seven-nations cluster (Deut 7:1, 20:17, Josh 3:10, 24:11, Judg 3:5, etc.)

**Lock added 2026-05-16 (DEU end-of-book audit Item F).** The seven-nations ethnonym cluster recurs in DEU + Josh + Judg + 1 Kgs. Surface drift was detected between DEU 7:1 (ชาว- prefix + bare ethnonym) and DEU 20:17 (คน- prefix + -ต suffix). Locked to the DEU 7:1 form across the corpus.

| Hebrew | Locked Thai (canonical) | Rejected (do not use) |
|---|---|---|
| חִתִּי | **ชาวฮิตไทต์** | คนฮิตไทต์ |
| גִּרְגָּשִׁי | **ชาวเกอร์กาชี** | — |
| אֱמֹרִי | **ชาวอาโมไรต์** | คนอาโมไรต์ |
| כְּנַעֲנִי | **ชาวคานาอัน** | คนคานาอัน |
| פְּרִזִּי | **ชาวเปริซซี** | คนเปริสซีต (rejected — -ต is a Thai pluralization marker absent in the rest of the corpus) |
| חִוִּי | **ชาวฮีไว** | คนฮีไวต์ (rejected) |
| יְבוּסִי | **ชาวเยบุส** | คนเยบุสีต (rejected) |

**Forward-protection:** all subsequent OT books (Joshua, Judges, Samuel, Kings, Chronicles) must use the canonical Thai surface above. `check_phrase_consistency.py` should HARD-FAIL ethnonym drift in any seven-nations occurrence.

### Trans-Jordan place-names (DEU geography)

| Hebrew | Locked Thai | Notes |
|---|---|---|
| פִּסְגָּה | **พิสกาห์** | DEU 3:17, 3:27, 4:49, 34:1; locked 2026-05-16 (DEU audit Item F1 — 34:1 was ปิสกาห์ as mechanical typo, normalized) |
| נְבוֹ (the mountain) | **เนโบ** | DEU 32:49, 34:1 |
| הַעֲרָבָה (the rift valley) | **อาราบาห์ / ที่ราบอาราบาห์** | context-dependent |

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

---

## Amendment (2026-05-20): Judges-figure entries + OT-figure-in-NT-retrospective cross-corpus rule

**Triggered by:** JDG audit Item C + 2-way external AI review (ChatGPT MAJOR-CONCERN / Gemini CONCERN). Heb 11:32 shipped with Greek-form transliterations (`กิเดโอน`, `เยฟธาห์`) while Judges shipped with Hebrew-faithful forms (`กิดเอน`, `เยฟทาห์`). This is the first OT/NT cross-corpus proper-name drift caught in the project — and both AIs converged on a single fix: align the NT side to the OT-Hebrew-faithful surface, since the NT retrospective is explicitly pointing readers back to the OT narrative.

### Judges-figure locked entries

| Hebrew | Greek (in NT retrospectives) | Locked Thai | Anchor |
|---|---|---|---|
| גִּדְעוֹן | Γεδεών | **กิดเอน** | JDG 6:11 (first occurrence); 57 total JDG occurrences; HEB 11:32 (now aligned) |
| בָּרָק | Βαράκ | **บาราค** | JDG 4:6 (first occurrence); 12 total JDG occurrences; HEB 11:32 (was already aligned — Hebrew and Greek forms converge) |
| שִׁמְשׁוֹן | Σαμψών | **แซมสัน** | JDG 13:24 (first occurrence); 50 total JDG occurrences; HEB 11:32 (was already aligned — Greek-style "แซมสัน" matches Hebrew "שִׁמְשׁוֹן" closely enough that no drift was present) |
| יִפְתָּח | Ἰεφθάε | **เยฟทาห์** | JDG 11:1 (first occurrence); 26 total JDG occurrences; HEB 11:32 (now aligned) |
| דְּבוֹרָה | (no NT mention) | **เดโบราห์** | JDG 4:4 (first occurrence) |
| אֵהוּד | (no NT mention) | **เอฮูด** | JDG 3:15 (first occurrence) |
| גָּתְנִיאֵל / עָתְנִיאֵל | (no NT mention) | **โอทนีเอล** | JDG 1:13 (first occurrence) |
| יוֹאָשׁ (father of Gideon) | (no NT mention) | **โยอาช** | JDG 6:11 |
| מָנוֹחַ (father of Samson) | (no NT mention) | **มาโนอาห์** | JDG 13:2 |
| דְּלִילָה | (no NT mention) | **เดลิลาห์** | JDG 16:4 |

### The cross-corpus rule

**When an OT-narrative figure is named in the NT as a direct retrospective reference to the OT story** (e.g., Heb 11:32's faith-hall, Acts 7's Stephen-speech historical sweep, Romans 9–11's Pauline OT references, James 5:17's Elijah reference), **use the OT-Hebrew-faithful Thai spelling** for cross-corpus recognizability — even when the underlying Greek transliteration would naturally produce a slightly different Thai form.

**Rationale:**

1. **Reader experience.** The NT retrospective is explicitly pointing readers back to the OT narrative. A Thai reader who reads HEB 11:32's `กิดเอน` should be able to immediately cross-reference Judges and find the same Thai spelling. Splitting the Thai across testaments (`กิเดโอน` in HEB 11:32 vs. `กิดเอน` in JDG) would create unnecessary friction with no theological benefit.

2. **Greek-form vs. Hebrew-form is a transliteration choice, not a meaning difference.** Γεδεών IS Gideon; Ἰεφθάε IS Jephthah. The Greek author of Hebrews used the LXX/Greek conventions because Greek was his vehicle; he was not naming different people. The Thai translator's task is to render the *same person*, and the OT-Hebrew-faithful Thai is the canonical reference form.

3. **The reverse direction does NOT apply.** When an OT figure has acquired a Greek-conventional Thai form that is *more widely recognized* in Thai-Bible readership (e.g., `โมเสส` matches both Greek Μωυσῆς and Hebrew מֹשֶׁה via THSV11 baseline; same with `ดาวิด`, `ซามูเอล`), use the THSV11 baseline. The rule only kicks in when an OT/NT spelling drift would actively obstruct cross-corpus reading — as it did at HEB 11:32 with `กิเดโอน` (Greek-form) vs. `กิดเอน` (Hebrew-faithful, JDG-side baseline).

### Forward-protection — other OT-figure-in-NT-retrospective targets

A pre-flight scan was performed 2026-05-20 for the specific Judges-side drift targets (`กิเดโอน`, `เยฟธาห์`) across all NT books — only HEB 11:32 had the drift, and it is now fixed. **However**, the same class of issue can recur for other OT figures in NT retrospectives. The following are the highest-stakes upcoming watch-points; pre-flight scan recommended before next OT audit pass:

1. **Acts 7 (Stephen's speech)** — sweeping OT history; checks every patriarch, Moses-cycle figure, judge-era figure, royal-era figure. Highest risk concentration of OT-figure-in-NT-retrospective drift in the NT.
2. **Matt 1 / Luke 3 genealogies** — David-line names; check against 1-2 SAM and 1-2 CHR baselines.
3. **Romans 4 (Abraham), Romans 9–11 (Isaac, Esau, Jacob, Moses, Pharaoh, Elijah)** — Pauline OT retrospectives.
4. **Hebrews 11 (entire faith-hall)** — already audited for Judges figures; check remaining (Abel, Enoch, Noah, Abraham, Sarah, Isaac, Jacob, Joseph, Moses, Rahab) against OT baselines.
5. **James 5:17 (Elijah)** — already locked from earlier audit; spot-confirm.
6. **2 Pet 2:5–8** (Noah, Lot) — short list; spot-confirm.
7. **Jude 11, 14** (Cain, Balaam, Korah, Enoch) — non-canonical Enoch reference but the names need to align with their OT-narrative forms where they appear.

The pre-flight scan is mechanical (greppable) and should be a single one-shot job: every NT verse that mentions an OT figure, cross-check Thai spelling against the OT-side baseline file (`data/proper_names_thsv11_baseline.json`) once that file is built. Recommend running this scan **before** the next NT book is opened for audit (currently main is on 1SA; no immediate NT touch-up planned).

### Boundary

- This rule applies to *OT-figure-in-NT-retrospective* contexts only. NT-native figures (Jesus, Paul, Peter, the apostles, NT-era named individuals) retain their Greek-form Thai surfaces per the existing NT corpus baseline.
- This rule does NOT apply to OT figures cited in NT *theological argument* without retrospective reference to specific OT narrative (e.g., generic "the prophets" in NT exhortation). It applies specifically when the NT author is pointing readers back to a specific OT story.
- This rule does NOT apply to OT place-names in NT contexts that have acquired Greek-convention forms (e.g., `Σιών` → `ศิโยน` is the same whether OT or NT; no drift).

### External AI verdicts (JDG audit Item C, 2026-05-20)

- **ChatGPT:** MAJOR CONCERN — "this is the first serious OT/NT name-alignment problem, and it will confuse Thai readers comparing Heb 11:32 with Judges. The issue is not that either side is 'wrong'… but because Heb 11:32 explicitly points readers back to Judges, the cross-corpus surface should probably match."
- **Gemini:** CONCERN — "leaving mismatched names between Heb 11:32 (Greek-faithful) and JDG (Hebrew-faithful) creates unnecessary friction for Thai readers attempting to cross-reference the NT faith hall of fame with the historical OT narratives. Normalizing the NT to match the OT Hebrew base for these historical figures strengthens cross-testamental unity."
- **Recommended action (both):** spot-revise HEB 11:32 (`กิเดโอน` → `กิดเอน`; `เยฟธาห์` → `เยฟทาห์`); lock an OT-figure-in-NT-retrospective rule. Action taken in this PR.
