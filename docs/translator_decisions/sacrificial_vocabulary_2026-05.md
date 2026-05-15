# OT Sacrificial Vocabulary — Translation Policy

**Status:** LOCKED 2026-05-15
**Triggered by:** Numbers end-of-book audit, Decision 5 (protect Leviticus)
**Cross-AI consensus:** ChatGPT, Gemini, Logos AI 2026-05-15
**Scope:** Leviticus + Numbers + Deuteronomy + every OT book with sacrificial language

---

## 1. The five main sacrificial types

| Hebrew | Transliteration | Thai (locked) | Hebrew root meaning |
|---|---|---|---|
| עֹלָה | ʿōlāh | **เครื่องเผาบูชา** | "that which goes up" — burnt offering, fully consumed |
| מִנְחָה | minḥāh | **เครื่องบูชาธัญพืช** | "gift" — grain offering |
| חַטָּאת | ḥaṭṭāʾt | **เครื่องบูชาไถ่บาป** | "sin" / "sin offering" (polysemous; see §3) |
| אָשָׁם | ʾāšām | **เครื่องบูชาไถ่ความผิด** | "guilt" / "guilt offering" / "reparation" |
| שְׁלָמִים | šəlāmîm | **เครื่องสันติบูชา** | "peace/wholeness offering" — fellowship/peace |

**Already used consistently throughout shipped NUM chapters.**

## 2. Secondary sacrificial vocabulary

| Hebrew | Thai (locked) | Notes |
|---|---|---|
| נֶסֶךְ | **เครื่องดื่มบูชา** | drink offering / libation |
| תְּרוּמָה | **เครื่องบูชายก** / **เครื่องถวาย** | heave offering / contribution |
| תְּנוּפָה | **เครื่องบูชาโบก** | wave offering |
| קָרְבָּן | **เครื่องบูชา** (general) | offering / sacrifice (umbrella term) |
| אִשֶּׁה | **เครื่องบูชาด้วยไฟ** | fire offering / food offering |
| רֵיחַ נִיחֹחַ | **กลิ่นที่พอพระทัย** | pleasing aroma |
| מַחְתָּה | **กระถางเผาเครื่องหอม** | censer / firepan |
| קְטֹרֶת | **เครื่องหอม** | incense |

## 3. The חַטָּאת polysemy problem

חַטָּאת in Hebrew is **inherently polysemous**:
- **As a moral concept** → "sin" (e.g., Gen 4:7 חַטָּאת רֹבֵץ "sin crouches"; Lev 4:3 לְאַשְׁמַת הָעָם "for the people's guilt-of-sin")
- **As a ritual category** → "sin offering" (Lev 4:24 חַטָּאת הוּא "it is a sin offering")
- **As both, in tension** (Lev 6:25; "the sin [offering] shall be slaughtered… most holy is it")

**Locked Thai distinction:**

| Hebrew context | Thai |
|---|---|
| Moral noun ("sin / iniquity") | **บาป** |
| Ritual noun ("sin offering") | **เครื่องบูชาไถ่บาป** |
| Adjectival/genitive in compound | Context-driven; document case-by-case |

**Rule:** Whenever the Hebrew word in question is followed by a verb of slaughtering/burning/sprinkling — or whenever the parallel sequence is עֹלָה / מִנְחָה / __ — it is **ritual** (เครื่องบูชาไถ่บาป). Whenever it is followed by language of forgiveness, atonement, or the moral status of a person — it is **the moral noun** (บาป).

## 4. Compound terms

| Hebrew compound | Thai | Used in |
|---|---|---|
| חַטַּאת הַכִּפֻּרִים | **เครื่องบูชาไถ่บาปสำหรับการลบบาป** | Num 29:11 (Day of Atonement) |
| אֲשַׁם נָקָם | **เครื่องบูชาไถ่ความผิดของการแก้แค้น** | rare; document per occurrence |
| מַיִם חַיִּים | **น้ำสด** (lit. "living water") | Num 19:17 (water of purification); preserve literal |
| מֵי נִדָּה | **น้ำชำระมลทิน** | Num 19:9 etc. |

## 5. Verbal forms

| Hebrew verb | Thai |
|---|---|
| הִקְרִיב (hiphil קרב) | **ถวาย** |
| זָבַח | **ฆ่าถวาย** / **ถวายเป็นเครื่องบูชา** (context-dependent) |
| הִקְטִיר (hiphil קטר) | **เผา** (sacrificially) — distinct from שָׂרַף (general burning) |
| כִּפֵּר (piel) | **ลบบาป** / **ไถ่บาป** / **ทำการลบบาป** |
| הִזָּה (hiphil נזה) | **พรม** |
| יָצַק | **เท** (oil/blood pouring) |
| סָמַךְ יָד | **วางมือ** (laying-on of hands) |

## 6. Status of altar parts and animal portions

| Hebrew | Thai |
|---|---|
| מִזְבֵּחַ | **แท่นบูชา** |
| כַּפֹּרֶת | **พระที่นั่งกรุณา** (per kapporet_atonement_cover doc) |
| חֵלֶב | **ไขมัน** (literal) / **ส่วนที่ดีที่สุด** (idiomatic w/ olive oil, wine) |
| דָּם | **เลือด** |
| בָּשָׂר | **เนื้อ** |
| יָרֵךְ | **ต้นขา** |
| חָזֶה | **หน้าอก** |

## 7. Forward protection — Leviticus

Leviticus 1-7 (the sacrificial manual) ships under this lock. The check script `check_sacrificial_vocab.py` (to be written before LEV 1 ships) will verify:
1. עֹלָה / מִנְחָה / חַטָּאת / אָשָׁם / שְׁלָמִים render to locked Thai 100% in ritual contexts
2. חַטָּאת polysemy splits correctly per §3
3. Verb forms (§5) render consistently

## 8. Reviewer pathway

Native Thai theological reviewers may flag locked Thai for natural-register adjustments. **Lock-changes require book-boundary doc amendment** (not chapter-level drift).
