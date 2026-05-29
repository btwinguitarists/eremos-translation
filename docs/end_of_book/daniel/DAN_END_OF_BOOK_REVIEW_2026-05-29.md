# Daniel — End-of-Book Review

**Date:** 2026-05-29
**Scope:** All 12 chapters of Daniel (357 verses); `glossary.json`; `docs/translator_decisions/` corpus (~99 docs through the Esther end-of-book audit).
**Trigger:** DAN 12 shipped (commit `c0aba0b`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Seventeenth OT book in the corpus** and the **climax of the Babylonian/Persian-court block** (Ezra → Nehemiah → Esther → Daniel). Daniel is the single book that exercises the most still-open corpus decisions at once: it is the **second Biblical-Aramaic book** (2:4b–7:28, a far larger Aramaic span than Ezra's), it stages **four foreign emperors** (Nebuchadnezzar, Belshazzar, Darius the Mede, Cyrus) plus **Daniel-the-vizier** — the very figure `ot_register_policy §2.5` names by name — and it is the OT **source text** for several NT-forward apocalyptic surfaces: the "one like a son of man" (7:13 → the Gospels' ὁ υἱὸς τοῦ ἀνθρώπου), the four beasts (7:3–7 → Revelation 13), the abomination of desolation (9:27/11:31/12:11 → Matt 24:15), and the first named angels in canon (Gabriel, Michael). It also reproduces the Esther textual situation — large Greek-version additions (Prayer of Azariah / Song of the Three, Susanna, Bel and the Dragon) excluded under the MT-only base.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **19 cross-cutting items reviewed.** Mechanical gates (§1) pass on the consistency checks: 12/12 chapters have green per-chapter reports + back-translations + translations (357 verses); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the 713-chapter corpus); `check_phrase_consistency.py` clean across all 38 audited locks (20,954 verses); `audit_inclusion_variants.py --book daniel --strict` = **0 candidates, exit 0**. **One mechanical gap surfaced** (§16, versification map — see below). The Tetragrammaton appears **only in Daniel 9** (the Hebrew penitential prayer); accordingly `output/textual_variants/daniel_09.json` is the **sole** textual-variant file and carries exactly the YHWH first-occurrence footnote — the no-YHWH→no-footnote convention (the Ezra-5 / Esther precedent) applied per-chapter across an 11-chapter book that otherwise names God only as Elah / Most High / God of heaven.
- **1 item flagged DECIDE** (Ben choice needed before tagging `book-daniel-v1`):
  - **§1 — the foreign-monarch register, now the *fourth* book of the court block and the strongest vote yet for ratifying `ot_register_policy §2.2` as written.** Daniel grants **all four** emperors full ราชาศัพท์ in narrator voice (Nebuchadnezzar `ทรงยกทัพ`/`ทรงพระพิโรธ` 1:1, 2:12; Belshazzar `ทรงจัดงานเลี้ยง` 5:1 *kept royal through the temple-vessel sacrilege*; Darius `ทรงรับราชอาณาจักร`/`บรรทม`/`เสด็จ` 6:1, 6:18, 6:20; Cyrus as the dating anchor 1:21/6:28/10:1), each citing §2.2 by name, and it holds **Daniel-the-vizier in plain register throughout** (§2.5, which names Daniel explicitly). Daniel is internally policy-compliant and needs no edit — but its tag is gated on the **same corpus ratification Ezra deferred and Esther voted on.** With the written §2.2, Nehemiah, Esther, and now Daniel all on the full-ราชาศัพท์ side, Ezra remains the lone outlier (commoner-register Persian kings, incl. Ahasuerus at Ezra 4:6 — the same king Esther renders with full `ทรง`). **Ratify §2.2, write `foreign_monarch_register_2026-05.md`, normalize Ezra, and tag Ezra + Nehemiah + Esther + Daniel together.** See §1.
- **6 items flagged REVIEW** (worth Ben's confirmation; §15/§16 ideally before tag):
  - **§3 — Nebuchadnezzar's madness downshift uses a trigger §2.2 doesn't name.** During the beast-state (MT 4:30 = Eng 4:33) the narrator drops to plain/passive register (`ถูกขับไล่จากผู้คน`), with the KD calling it deliberate humbling (`กริยาสามัญสื่อการถ่อมลง`). But §2.2 authorizes a foreign-emperor downshift only for **grave moral failure** (the David/2 Sam 11 model). Here the trigger is **divine humiliation / loss of reason**, and — tellingly — Belshazzar's sacrilege (ch.5) is the clearer "grave failure" case yet keeps full royal register. Confirm the downshift taxonomy.
  - **§8 — the "one like a son of man" (7:13) is given *light* royal register** (`เสด็จมา`/`ทรงถูกนำเข้ามา`/`พระพักตร์`), with a KD explicitly invoking "ราชาศัพท์สำหรับบุตรมนุษย์เชิงวิวรณ์." This pre-commits the Danielic figure toward the divine/messianic identification — defensible (he is enthroned and given everlasting dominion) but worth confirming, especially against §9's *deliberately plain* treatment of the man-in-linen (10:5–6) where ambiguity is preserved.
  - **§13 — the seventy-weeks מָשִׁיחַ (9:25, 9:26) is rendered generically as `ผู้ถูกเจิม`** ("anointed one"), with notes that *acknowledge but do not endorse* the Christian messianic reading. This is the highest-visibility messianic crux in the OT; confirm the non-committal stance is the intended editorial position (it is consistent with RULES §0's descriptive-notes policy, but Thai evangelical reviewers will look here first).
  - **§15 — the Greek-version Additions (Prayer of Azariah / Song of the Three between 3:23–24; Susanna; Bel and the Dragon) are excluded with NO reader-facing note anywhere.** Esther got a single 1:1 disposition note for its Additions; Daniel — whose additions are *more* visible (the Song of the Three is liturgically famous; Susanna and Bel are full narratives) and which sit at a concrete seam (between 3:23 and 3:24) — has none. Non-gap under `mt_vs_lxx §2.3`, but recommend a single note + a Daniel row in the MT/LXX doc.
  - **§16 — Daniel's three MT-vs-English versification divergence zones are documented at verse-level but NOT registered in `data/versification_map.json`.** The map carries only the two Aramaic-boundary markers (`DAN-2-4`, `DAN-7-28`, both `diverges:false`). The 4:1 KD itself says the +3 shift "ควรลงทะเบียนใน versification_map.json ที่การตรวจท้ายเล่ม" ("should be registered at the end-of-book check") — i.e., now. This is the known "versification map ship gotcha." See §16.
  - **§11 — the apocalyptic beasts (`สัตว์ร้าย`, ch.7–8) match the locked Revelation θηρίον surface, but Daniel 7 is the *source* of Revelation 13 and the notes don't cross-link the doc.** Uniform and correct; recommend a backward-link note in `therion_beast_apocalyptic_2026-05.md`.
- **Five new / carry-forward corpus docs recommended,** three of them **overdue carry-forwards** from Ezra/Nehemiah/Esther:
  - **`foreign_monarch_register_2026-05.md`** (§1) — the highest-value forward-protection doc, owed since Ezra, now spanning four shipped books; gated on the §1 DECIDE.
  - **`biblical_aramaic_2026-05.md`** (§4) — carry-forward from Ezra (still unwritten); Daniel is the major Aramaic book and the right place to lock the language-switch convention + the no-YHWH-in-Aramaic→no-footnote rule.
  - **`god_of_heaven_persian_title_2026-05.md`** (§5) — carry-forward from Ezra §6 + Nehemiah; Daniel exercises `אֱלָהּ שְׁמַיָּא → พระเจ้าแห่งฟ้าสวรรค์` heavily. Fold in (or add to `divine_names_table`) the **Ancient-of-Days** row (`עַתִּיק יוֹמִין → ผู้เจริญด้วยวัยวุฒิ`), which the table does not yet carry.
  - **`danielic_apocalyptic_imagery_2026-05.md`** (or amend `spiritual_beings_hierarchy_2026-05.md` + `therion_beast_apocalyptic_2026-05.md`) (§8/§10/§11) — Daniel introduces named angels (Gabriel/Michael), the שַׂר territorial-"prince" concept (one Thai surface `เจ้านาย` for both Michael and the hostile princes of Persia/Greece), the watcher (עִיר → `ผู้เฝ้าระวัง`), and the Son-of-Man register call — all of which forward-compound massively into Revelation.
  - **`persian_achaemenid_administrative_titles_2026-05.md`** (§17) — overdue carry-forward from Ezra/Nehemiah/Esther; Daniel adds the satrap/prefect/counsellor tier (ch.3, ch.6).
- **External AI review (§3) pending.** Suggested 4-item packet: foreign-monarch register, now four-book (§1 DECIDE); Son-of-Man light-royal-register vs man-in-linen ambiguity (§8/§9 REVIEW); seventy-weeks מָשִׁיחַ non-committal rendering (§13 REVIEW); Greek-version-Additions disposition note (§15 REVIEW).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Foreign-monarch register (four emperors) — **DECIDE (the headline; fourth book of the court block; Daniel votes with Nehemiah + Esther + the written §2.2, against Ezra)**

This is the register question Ezra **explicitly parked for the "Ezra–Nehemiah–Esther–Daniel" block**, Nehemiah answered (full ราชาศัพท์ per the written §2.2), and Esther ratified by a continuous 10-chapter exercise. Daniel — the *last* book of the named block, and the one with the most emperors — answers it the **same way**, with per-verse §2.2 citations.

**All four foreign emperors receive full ราชาศัพท์ in narrator voice wherever they act:**

| King | Ref | Aramaic/Hebrew | Thai (narrator voice) | Royal marker |
|---|---|---|---|---|
| **Nebuchadnezzar** | 1:1 | בָּא נְבוּכַדְנֶאצַּר | `เนบูคัดเนสซาร์…**ทรง**ยกทัพ…**ทรง**ล้อม` | `ทรง` |
| | 2:12 | בְּנַס וּקְצַף | `**ทรงพระพิโรธ**และกริ้วยิ่งนัก` | royal noun |
| | 3:13, 3:19 | בִּרְגַז וַחֲמָה | `**ทรงพระพิโรธ**…กริ้วจัด` | royal noun |
| **Belshazzar** | 5:1 | עֲבַד לְחֶם רַב | `**ทรง**จัดงานเลี้ยงใหญ่` | `ทรง` |
| **Darius the Mede** | 6:1 | קַבֵּל מַלְכוּתָא | `**ทรง**รับราชอาณาจักร…**ทรง**ตั้ง` | `ทรง` |
| | 6:18/6:20 | (sleepless / rose at dawn) | `**บรรทม**ไม่หลับ … **ทรง**ตื่นบรรทม…รีบ**เสด็จ**` | royal verbs |
| **Cyrus** | 1:21, 6:28, 10:1 | (regnal dating) | dating anchor (`ปีที่ 1/3 ของไซรัส`) | n/a (no narrated action) |

The foundational KD is at **1:1**: "เนบูคัดเนสซาร์เป็นจักรพรรดิต่างชาติ ได้รับราชาศัพท์ 'ทรง' ในเสียงผู้เล่า ตาม ot_register_policy §2.2 (ตารางระบุ 'เนบูคัดเนสซาร์' โดยตรง)." Belshazzar's KD (5:1) and Darius's (6:1) each cite §2.2 the same way, and **Belshazzar's register is held royal straight through the temple-vessel sacrilege** (5:2–4) — the deliberate decision *not* to downshift for sacrilege (parallel to Esther's 1:10 drunk-scene decision; contrast §3).

**The §2.5 Hebrew-servant side is clean and decisive.** Daniel — whom §2.5 names by name as the canonical vizier case alongside Joseph, Mordecai, and Nehemiah — is held in plain/deferential register at every elevation: 2:16 (`ข้าพระบาท`, "§2.5 — ไม่รับราชาศัพท์"), 2:48–49 (promotion, plain), 4:16 (interpreting at the height of office, plain), 5:17 (refusing reward, plain), 6:1–4 (`ใช้ภาษาสามัญ §2.5 แม้ดำรงตำแหน่งสูง`). See §2.

**DECIDE.** The audit changes nothing in Daniel — Daniel follows the written §2.2 and is internally uniform. What is owed is the **corpus-wide ratification Ezra deferred**, now across four shipped, untagged books:
- **Option A (recommended, now overwhelmingly favored): ratify §2.2 as written** — foreign emperors get full ราชาศัพท์ in narrator voice. Keep Nehemiah, Esther, Daniel as-is (all comply); **normalize Ezra's Persian-king narrator verbs to `ทรง`** (the bounded set EZR 1:7, 3:7, 4:6, 6:1, etc.). The written policy + three of four books already point this way; Daniel — which names the emperors *and* the vizier the policy itself names — makes the case airtight.
- **Option B: ratify the Ezra commoner-register split.** Then normalize Nehemiah + Esther + Daniel (a very large edit against the written §2.2) and rewrite §2.2.

Either way: **write `foreign_monarch_register_2026-05.md`** (or amend `ot_register_policy §2.2`) and **tag Ezra + Nehemiah + Esther + Daniel together** once the diverging book is normalized. **Severity: MEDIUM-HIGH** — no theological stakes, but a now-four-book visible inconsistency on shared kings, and Daniel is the natural place to close it because it is the last book of the block the decision was deferred to. **Decide jointly with the Ezra / Nehemiah / Esther tags.**

---

## 2. Daniel-as-vizier + the three friends — plain register — **LOCKED ("the named case")**

`ot_register_policy §2.5` names **Daniel** explicitly (with Joseph, Mordecai, Nehemiah) as a Hebrew servant who never receives royal honorifics in narrator voice, regardless of office. Daniel holds this perfectly across all four reigns:

| Ref | Context | Thai | Register |
|---|---|---|---|
| 1:19–21 | enters royal service, continues to Cyrus | `เข้ารับใช้` (plain) | plain |
| 2:16 | requests time of the king | `ข้าพระบาท` + `ทูล` (deferential up) | plain |
| 2:48–49 | promoted to chief of the wise men | plain verbs | plain |
| 4:16 | interprets the dream at the height of office | `เจ้านายของข้าพระบาท`, plain | plain/deferential |
| 5:17 | refuses Belshazzar's reward | `ขอให้ของกำนัลเป็นของฝ่าพระบาทเอง` (plain) | plain/deferential |
| 6:1–4 | first of three commissioners under Darius | "ใช้ภาษาสามัญ §2.5 แม้ดำรงตำแหน่งสูง" | plain |

The contrast with the king *in the same scenes* (the king acts with `ทรง`; Daniel responds in `ข้าพระบาท`) is exactly the §2.2/§2.5 boundary working as designed. The **three friends** (Shadrach/Meshach/Abednego) are likewise plain throughout ch.3, including the bold direct address to the king at 3:16–18 (`ข้าแต่เนบูคัดเนสซาร์ ข้าพระบาททั้งหลายไม่จำเป็นต้องทูลตอบ` — deferential-but-plain, no royal verbs). Daniel is the fourth consecutive book to confirm the Hebrew-servant plain register, and the one §2.5 cites first.

**LOCKED** ✓ per `ot_register_policy §2.5` + `honorifics_non_divine_authorities_2026-04.md`.

---

## 3. Nebuchadnezzar's madness downshift + pagan-king doxology — **REVIEW (downshift trigger taxonomy)**

Two register events in Daniel 4 (the first-person royal memoir, MT 4:1–34 = Eng 4:4–37) test the §2.2 downshift rule from both sides:

- **The beast-state (MT 4:30 = Eng 4:33).** When the judgment falls, the narrator drops to plain/passive register: `…พระองค์**ถูกขับไล่**จากผู้คน…` ("he was driven from people"), and the KD frames it as deliberate humbling: "สภาพเยี่ยงสัตว์ของเนบูคัดเนสซาร์ (กริยาสามัญสื่อการถ่อมลง)." The royal pronoun `พระองค์` is retained but the royal *verbs* are dropped.
- **The restoration + doxology (MT 4:31–34 = Eng 4:34–37).** As his reason returns, the royal first-person `เรา` returns with it, and the pagan emperor delivers a full doxology to the Most High in royal register: `บัดนี้ เรา เนบูคัดเนสซาร์ ขอสรรเสริญ ยกย่อง และเทิดทูนกษัตริย์แห่งฟ้าสวรรค์` (4:34). A Gentile king praising God *in imperial register* is the theological climax of ch.4, and the translation handles it by keeping the king's own register — correct and moving.

The **doxology side is STABLE** (kept royal per §2.2; a pagan-king-doxology leitwort actually threads chs. 3–6 — note the 6:26 KD cross-references Nebuchadnezzar's 3:31 / 4:1 proclamations). The **downshift side is the REVIEW**: §2.2 authorizes a foreign-emperor register downshift only for **grave moral failure** (the David / 2 Sam 11 model). Daniel's 4:30 downshift is triggered instead by **divine humiliation / loss of reason** — and, crucially, the clearer "grave failure" case in the book, Belshazzar's sacrilege (ch.5), is *not* downshifted (§1). So the corpus is using two different, unstated triggers. Confirm the taxonomy: is the trigger "moral failure" (then 4:30 is an extension to divine-humbling, and Belshazzar arguably should downshift too), or is the principle simply "narrator marks the loss of office/agency" (then it is passive-voice, not a moral judgment)? Worth one line in the foreign-monarch doc. **Severity: LOW.**

---

## 4. Biblical Aramaic (2:4b–7:28) — **STABLE → recommend `biblical_aramaic_2026-05.md`** (overdue carry-forward from Ezra)

Daniel is bilingual: Hebrew (1:1–2:4a; 8:1–12:13) and Biblical Aramaic (2:4b–7:28) — a far larger Aramaic span than Ezra's. The handling is clean and documented at the seam:

- **The Hebrew→Aramaic switch at 2:4b** is flagged at 2:4 (KD: "ข้อ 4ข เป็นจุดที่ต้นฉบับเปลี่ยนเป็นภาษาอาราเมอิก"; `thai_summary`: "ต่อเนื่องไปจนถึงบทที่ 7"). The boundary is registered in `data/versification_map.json` as `DAN-2-4` (`aramaic_section:true`, "Hebrew→Aramaic mid-verse").
- **The Aramaic→Hebrew switch back** is registered as `DAN-7-28` ("Aramaic→Hebrew at end of chapter 7").
- The source text is carried in a `language:"aramaic"` + `aramaic` field on the Aramaic verses (distinct from the Hebrew chapters' `hebrew` field) — clean schema handling of the language switch.
- The no-YHWH-in-Aramaic situation is handled implicitly and correctly: the Tetragrammaton never appears in the Aramaic chapters (or in the Hebrew chs.1, 8, 10–12) — only in the Hebrew prayer of ch.9 — so only ch.9 carries a YHWH footnote (§6).

This is the **second Aramaic book** and the convention is now well-exercised, but it remains **undocumented at corpus level** — the `biblical_aramaic` doc recommended at the Ezra audit is **still unwritten**. Daniel is the right place to write it (it has the larger Aramaic span and the cleaner seams). **STABLE.** **Severity: LOW** (documentation; forward-compounding is nil — only Ezra + Daniel have Aramaic).

---

## 5. Divine titles (God of heaven / Most High / Lord of kings / Ancient of Days) — **STABLE/LOCKED → recommend `god_of_heaven_persian_title_2026-05.md` + an Ancient-of-Days row**

Daniel is the densest OT cluster of Aramaic divine *titles*, all rendered uniformly and per `divine_names_table_2026-05.md`:

| Title | Aramaic/Hebrew | Thai | Refs | Status |
|---|---|---|---|---|
| God of heaven | אֱלָהּ שְׁמַיָּא | **พระเจ้าแห่งฟ้าสวรรค์** | 2:18, 2:19, 2:37, 2:44 | uniform |
| Most High | עִלָּאָה (Aram.) / עֶלְיוֹן (Heb.) | **องค์ผู้สูงสุด / ผู้สูงสุด** | 3:26; 4:2,17,24,25,32,34; 5:18,21; 7:18,22,25,27 | uniform |
| Lord of kings | מָרֵא מַלְכִין | **องค์เจ้านายแห่งกษัตริย์ทั้งหลาย** | 2:47 | locked (table) |
| Lord of heaven | מָרֵא שְׁמַיָּא | **องค์เจ้านายแห่งฟ้าสวรรค์** | 5:23 | locked (xref 2:47) |
| Ancient of Days | עַתִּיק יוֹמִין | **ผู้เจริญด้วยวัยวุฒิ** | 7:9, 7:13, 7:22 | uniform (xref Rev 1:14) |
| (true) God | אֱלָהּ / אֱלָהָא | **พระเจ้า** | throughout | locked (table) |

Two are corpus-doc gaps:
- **"God of heaven" (`אֱלָהּ שְׁמַיָּא` / Heb. `אֱלֹהֵי הַשָּׁמַיִם`)** — the Persian-period divine title flagged for a doc at both the Ezra and Nehemiah audits, **still unwritten**. Daniel exercises it heavily; write `god_of_heaven_persian_title_2026-05.md` now (it covers Ezra, Nehemiah, and Daniel).
- **"Ancient of Days" (`עַתִּיק יוֹמִין → ผู้เจริญด้วยวัยวุฒิ`)** — uniform across 7:9/13/22 with a Rev 1:14 cross-reference at 7:9, but the `divine_names_table` Aramaic section does **not** carry this row. Add it (Daniel-distinctive; recurs only at the white-haired-Judge image of Rev 1:14).

The `divine_names_table` already lists `מָרֵא־מַלְכִין`/`מָרֵא־שְׁמַיָּא` and `עִלָּאָה`, all of which Daniel matches exactly. **STABLE/LOCKED.** **Severity: LOW** (one overdue doc + one table row).

---

## 6. YHWH only in Daniel 9 + Adonai vocatives + the 12:8 "soft warning" — **LOCKED (and the warning is a false positive)**

The Tetragrammaton occurs **only in Daniel 9** (the Hebrew penitential prayer — a well-known feature of the book). The mechanical consequence is handled correctly: `output/textual_variants/daniel_09.json` is the **only** textual-variant file in the book and carries exactly the Layer-2 YHWH first-occurrence footnote (at 9:2, the first YHWH). Every other chapter — Aramaic or Hebrew — names God without the Tetragrammaton and is owed no footnote (the Ezra-5 / Esther convention applied per-chapter).

The Daniel 9 prayer exercises the `divine_names_table` Adonai sub-rules cleanly:
- **9:3** `אֶל־אֲדֹנָי הָאֱלֹהִים` → `องค์เจ้านายพระเจ้า` (standalone Adonai title).
- **9:4, 9:7, 9:8, 9:9, 9:15, 9:16, 9:17** vocative `אֲדֹנָי` / `אָנָּא אֲדֹנָי` → `ข้าแต่องค์เจ้านาย` (the 2026-05-18 vocative-interjection sub-rule — `divine_names_table` forward-protection list names "Daniel 9 (Daniel's prayer — multiple Adonai vocatives)" by name).
- **YHWH** (9:2, 9:4, 9:10, 9:13, 9:14, 9:20) → `องค์พระผู้เป็นเจ้า`.

**The `divine_names.md` aggregate's soft warning is a false positive.** It flags `Daniel 12:8: Hebrew has standalone אֲדֹנָי … Thai may be missing องค์เจ้านาย`. The verse is actually `וָאֹמְרָה **אֲדֹנִי** מָה אַחֲרִית אֵלֶּה` — single-yodh `אֲדֹנִי` ("my lord"), Daniel addressing the **man clothed in linen** (an angelophany), correctly rendered `**เจ้านายของข้าพเจ้า**` per the `divine_names_table` row for `אֲדֹנִי` addressing humans/angels. The check conflates `אֲדֹנִי` (human/angel address) with standalone divine `אֲדֹנָי`; the Thai is right. Worth a one-line follow-up to teach the check the single-yodh distinction so this stops recurring (cf. Psalms, where it will fire often). **LOCKED** ✓ per `divine_names_table_2026-05.md`.

---

## 7. חֶסֶד + the Daniel 9 prayer attributes — **LOCKED (chesed lock fires correctly)**

Daniel 9:4 carries the covenant-keeping divine-attribute language, and the locked `חֶסֶד → ความรักมั่นคง` fires exactly as `chesed_covenant_love_2026-05.md` prescribes:

- **9:4** `שֹׁמֵר הַבְּרִית וְהַחֶסֶד` → `ผู้ทรงรักษาพันธสัญญาและ**ความรักมั่นคง**` (covenant + steadfast-love, divine subject → locked surface).
- **9:9** `הָרַחֲמִים וְהַסְּלִחוֹת` → `พระเมตตาและการอภัยโทษ` (compassion + forgiveness).
- **9:18** `עַל־רַחֲמֶיךָ הָרַבִּים` → `เพราะ**พระเมตตาอันยิ่งใหญ่**ของพระองค์` (the ground of the plea is God's mercy, not human righteousness).

This is the covenant-attribute cluster (covenant + chesed + mercy + forgiveness) but **not** the full Exod-34 self-revelation formula (no "merciful and gracious, slow to anger, abounding in steadfast love…" recitation), so `exod_34_attribute_formula_2026-05.md` correctly does **not** fire — this is the attribute *vocabulary*, not the *formula*. The chesed lock fires at its proper covenant-loyalty sense. **LOCKED** ✓ per `chesed_covenant_love_2026-05.md`.

---

## 8. "One like a son of man" (7:13) — `บุตรมนุษย์` + light royal register — **REVIEW (the most theologically charged verse in Daniel)**

Daniel 7:13 is the OT source of the NT title ὁ υἱὸς τοῦ ἀνθρώπου → `บุตรมนุษย์`. Two editorial decisions:

- **Lexical (STABLE/LOCKED):** `כְּבַר אֱנָשׁ` → `ผู้หนึ่งเหมือน**บุตรมนุษย์**` — the locked title form (no `ของ`), with the KD explicitly citing `son_of_man_disambiguation` and naming "ดนล 7:13 เป็นต้นกำเนิดของตำแหน่งนี้" (Dan 7:13 as the origin of the title). The disambiguation is terminological, not orthographic — and it correctly keeps the *generic-human* form distinct (8:17 addresses Daniel himself as `บุตรแห่งมนุษย์`, *with* `แห่ง`).
- **Register (REVIEW):** the figure receives **light royal register** — `เสด็จมา` (came), `ทรงถูกนำเข้ามาต่อ**พระพักตร์**` (was brought before), `**พระองค์**` — with the KD stating: "บุตรมนุษย์ได้รับราชาศัพท์เบา ๆ (เสด็จมา/ทรง) ในฐานะผู้ครองนิรันดร์ที่ได้รับมอบอำนาจ (เทียบนโยบายราชาศัพท์สำหรับบุตรมนุษย์เชิงวิวรณ์)." 7:14 then gives him `อำนาจการปกครอง พระเกียรติ และราชอาณาจักร` — everlasting dominion.

The register choice pre-commits the Danielic figure toward the **divine/messianic** identification the Christian canon makes (and which the enthronement + everlasting-dominion + worship of 7:14 strongly support). It is defensible and theologically coherent within RULES §0's evangelical-Protestant frame. The **REVIEW** is to confirm this is intended — particularly because it sits in deliberate tension with §9 (the man-in-linen at 10:5–6 is kept *plain* precisely to preserve christophany/angelophany ambiguity). The two figures are treated differently on purpose (7:13 is enthroned and given dominion → divine; 10:5–6 is more ambiguous), but the principle deserves to be stated in one place. **Severity: MEDIUM** (theological; high reviewer-visibility). Good external-AI item.

---

## 9. The "man clothed in linen" (10:5–6, 12:6–7) — plain register, ambiguity preserved — **STABLE (contrast §8)**

The dazzling figure of `אִישׁ־אֶחָד לָבוּשׁ בַּדִּים` (10:5–6: body like beryl, face like lightning, eyes like flaming torches) is rendered with theophanic *imagery* but **plain register** (`มีชายผู้หนึ่งสวมเสื้อผ้าป่าน`, no `ทรง`), with the KD and note deliberately preserving the interpretive openness: "บุคคลสวรรค์ผู้ทรงสง่าราศี (สงวนความกำกวมไว้ ไม่ระบุชัดว่าเป็นพระเจ้าหรือทูตสวรรค์) … บางธรรมเนียมอ่านว่าเป็นพระคริสต์ก่อนทรงรับสภาพมนุษย์ บางธรรมเนียมว่าเป็นทูตสวรรค์ชั้นสูง — ฉบับนี้คงความกำกวมไว้." This is exactly the right call for an ambiguous figure, and the conscious *imagery-yes / register-no* split is principled. It pairs with §8 as the two poles of Daniel's "how much divine register does an exalted figure get" question — worth documenting together. **STABLE.** **Severity: LOW.**

---

## 10. Named angels + the שַׂר territorial-"prince" concept — **STABLE → recommend amending `spiritual_beings_hierarchy_2026-05.md`**

Daniel is the **first book in canon to name individual angels**, and it introduces an angelic-governance vocabulary the existing (Pauline-focused) `spiritual_beings_hierarchy_2026-05.md` does not cover:

- **Gabriel** (`גַּבְרִיאֵל`) → `กาเบรียล` (8:16, 9:21), transliterated, plain register, KD: "ทูตสวรรค์องค์แรกที่ถูกออกชื่อในพระคัมภีร์."
- **Michael** (`מִיכָאֵל`) → `มีคาเอล` — "one of the chief princes" (10:13 `อַחַד הַשָּׂרִים הָרִאשֹׁנִים` → `หนึ่งในบรรดาเจ้านายชั้นหัวหน้า`), "your prince" (10:21 → `เจ้านายของพวกเจ้า`), "the great prince" (12:1 → `เจ้านายผู้ยิ่งใหญ่`).
- **The שַׂר "prince" concept** is rendered uniformly `เจ้านาย` for **both** Michael *and* the hostile angelic powers — "prince of Persia" (10:13 → `เจ้านายผู้ครองอาณาจักรเปอร์เซีย`), "prince of Greece" (10:20 → `เจ้านายแห่งกรีก`). The KD at 10:13 cites `captain_of_yhwh_host` for the deliberate ambiguity-preservation. No divine register (`ทรง`) for any of them — celestial *rank*, not deity.
- **The watcher** (`עִיר וְקַדִּישׁ`, 4:13/17/23) → `ผู้เฝ้าระวัง` ("a holy one" → `ผู้บริสุทธิ์`), with a note that עִיר is a Daniel-only angel-class term.
- **"A son of the gods"** (`כְּבַר־אֱלָהִין`, 3:25) → `บุตรของพระทั้งหลาย` (lowercase, per `ot_polytheistic_register_2026-05.md`), with the KD explicitly *declining* a christological reading in the pagan king's mouth: "מิใช่ 'พระบุตรของพระเจ้า' (ไม่ตีความเชิงคริสต์ศาสตร์ลงในปากกษัตริย์นอกศาสนา) — ในข้อ 28 เนบูคัดเนสซาร์เองเรียกผู้นี้ว่า 'ทูตสวรรค์'." Excellent register/theology discipline.

All uniform and well-reasoned at verse level, but the named-angel + territorial-prince apparatus is **undocumented at corpus level** and forward-compounds heavily into Revelation (Michael at Rev 12:7; the angel-of-the-churches; territorial powers). **Recommend amending `spiritual_beings_hierarchy_2026-05.md`** with an "OT extension: Daniel's named angels + שַׂר celestial governance" section (or a dedicated `danielic_apocalyptic_imagery_2026-05.md` that also carries §8/§9/§11). **STABLE.** **Severity: LOW-MEDIUM** (forward-protection for Revelation).

---

## 11. Apocalyptic beasts (ch.7–8) — `สัตว์ร้าย` — **STABLE → recommend a backward-link in `therion_beast_apocalyptic_2026-05.md`**

The four beasts of ch.7 (`חֵיוָה`) render uniformly `สัตว์ร้าย` (7:3 `สัตว์ร้ายใหญ่สี่ตัว`; lion/bear/leopard/terrible-fourth at 7:4–7), matching the locked Revelation θηρίον → `สัตว์ร้าย` surface. The "little horn" (`קֶרֶן זְעֵירָה`) → `เขาเล็ก` (7:8, with the 7:24–25 king-interpretation). Chapter 8's ram (`אַיִל` → `แกะผู้`) and male goat (`צָפִיר` → `แพะผู้`) are rendered consistently, with Gabriel's interpretation locked to the empires (8:20 Media-Persia; 8:21 Greece; the prominent horn = Alexander). The kingdom-that-shall-never-be-destroyed (2:44 → `อาณาจักรที่จะไม่ถูกทำลาย`) ties the statue vision to 7:14's everlasting dominion.

Daniel 7 is the **source** of Revelation 13's composite beast (lion/bear/leopard reassembled, ten horns). The Daniel renderings are correct and consistent with the θηρίον lock, but the notes do **not** cross-link `therion_beast_apocalyptic_2026-05.md`. **Recommend** adding a backward-link note to that doc recording Daniel 7 as the OT source of the surface it locks (and recording the `สัตว์ร้าย` uniformity here). **STABLE.** **Severity: LOW.**

---

## 12. "Mene Mene Tekel Parsin" (5:25–28) — transliterate-plus-gloss wordplay — **STABLE**

The writing on the wall is handled with the same dual transliterate-the-loanword + gloss-the-meaning strategy as Esther's Purim etiology: 5:25 transliterates `เมเน เมเน เทเคล อูฟารสิน`, then 5:26–28 unfold the paronomasia — `เมเน` = "God has *numbered* (מְנָה) the days of your kingdom"; `เทเคล` = "you have been *weighed* (תְּקַל) and found wanting"; `เปเรส` = "your kingdom is *divided* (פְּרַס) and given to the Medes and *Persians* (פָּרָס)." The KD flags the original weight/currency meanings (mina/mina/shekel/half) and the three-way wordplay. This is a Daniel-distinctive naming-payoff (no forward-compounding) handled exactly right — could optionally be recorded as a datapoint in `proper_noun_wordplay_2026-05.md`. **STABLE.** **Severity: LOW.**

---

## 13. The seventy weeks / מָשִׁיחַ (9:24–27) — generic `ผู้ถูกเจิม`, non-committal note — **REVIEW**

The most contested messianic passage in the OT. The translation renders `מָשִׁיחַ` **generically**:
- **9:25** `עַד־מָשִׁיחַ נָגִיד` → `จนถึง**ผู้ถูกเจิม**ผู้เป็นเจ้านาย` (KD: "ตามตัวอักษร; ธรรมเนียมคริสต์อ่านว่าหมายถึงพระเมสสิยาห์/พระคริสต์ ดูหมายเหตุ").
- **9:26** `יִכָּרֵת מָשִׁיחַ` → `**ผู้ถูกเจิม**จะถูกตัดขาด` (note: "ธรรมเนียมคริสต์อ่านว่าหมายถึงการสิ้นพระชนม์ของพระคริสต์").

So the Thai surface is `ผู้ถูกเจิม` (literal "anointed one"), **not** `พระเมสสิยาห์` / `พระคริสต์`, and the notes *acknowledge but do not endorse* the christological reading. This is consistent with RULES §0 (the surface follows the Hebrew; the notes describe rather than pastorally endorse) — the same descriptive-not-prescriptive stance used at, e.g., the JHN 1:34 ἐκλεκτός decision. **REVIEW** to confirm this is the intended editorial position: it is the verse Thai evangelical reviewers will scrutinize first, and a project that capitalizes/title-marks `บุตรมนุษย์` at 7:13 (§8) but leaves `ผู้ถูกเจิม` generic at 9:25–26 is making a deliberate, defensible distinction (7:13's figure is enthroned and worshipped; 9:25–26's "anointed one" is textually a near-term referent in the Persian/Maccabean horizon with a typological NT fulfillment). Worth stating the principle once. **Severity: MEDIUM** (high reviewer-visibility). Good external-AI item.

---

## 14. Abomination of desolation (9:27, 11:31, 12:11) — **LOCKED/STABLE**

`שִׁקּוּץ שֹׁמֵם` / `שִׁקּוּץ מְשׁוֹמֵם` renders uniformly `**สิ่งน่าสะอิดสะเอียนที่ก่อความเริศร้าง**` across all three occurrences (9:27, 11:31, 12:11), with the 11:31 KD cross-referencing the others and **Matt 24:15** (Jesus's citation in the Olivet Discourse). The OT→NT forward thread is correctly noted; uniform surface; this is the kind of cross-quotation `ot_nt_cross_quotation_thread_2026-05.md` tracks. **STABLE.** **Severity: LOW.** *(Light follow-up: confirm the Matt 24:15 forward-link is captured wherever the cross-quotation thread is registered.)*

---

## 15. Greek-version Additions / MT-vs-Theodotion disposition — **REVIEW (non-gap, but no reader-facing note — unlike Esther)**

Daniel's textual situation is the second large deuterocanonical-expansion case the corpus has shipped (after Esther's Additions). The Greek versions (OG and Theodotion) carry **three additions absent from the MT**: the **Prayer of Azariah + Song of the Three Young Men** (inserted between MT 3:23 and 3:24, ~67 verses), **Susanna** (Greek ch.13), and **Bel and the Dragon** (Greek ch.14). Eremos translates **MT Daniel only** (per RULES §0 + `ot_canon_and_text_base_2026-05.md`, which names Daniel's additions in its §4 divergence-zone table and prescribes MT-only with optional Tier-3 footer disclosure). Under `mt_vs_lxx_textual_variant_handling_2026-05.md §2.3`, these are a **separate-recension / canonical-block question, not a per-verse MT variant → non-gap** (the same call Ezra reached for 1 Esdras and Esther for its Additions A–F).

**The gap vs. Esther:** Esther recorded its Additions exclusion in a single 1:1 disposition note. **Daniel has no such note anywhere** — not at 1:1, not at the 3:23/3:24 seam where the Greek inserts ~67 verses, and there is no Daniel row in the MT/LXX doc. Daniel's additions are *more* reader-visible than Esther's (the Song of the Three is liturgically famous as the *Benedicite*; Susanna and Bel are complete narratives Catholic/Orthodox Bibles print as Daniel 13–14) **and** they sit at a concrete textual seam. **Recommend** (a) a single disposition note (at 1:1, mirroring Esther, and/or a Tier-3 footer at the 3:23 seam) recording that Eremos follows MT and excludes the Prayer of Azariah/Song of the Three, Susanna, and Bel and the Dragon per RULES §0; and (b) an explicit note that the MT base is followed over Theodotion/OG for the text-form. **REVIEW.** No surface change. **Severity: LOW-MEDIUM.** Strong external-AI item.

---

## 16. Versification — three MT/English divergence zones NOT registered in the map — **REVIEW (the "versification map ship gotcha")**

Daniel has **three** genuine MT-vs-English chapter/verse divergences, and Eremos correctly uses **MT numbering** throughout, disclosing each at the verse level:

| Zone | Divergence | Disclosed at |
|---|---|---|
| ch.3/4 boundary | MT 3:31–33 = Eng/BSB 4:1–3 | 3:31 note |
| all of ch.4 | MT 4:1–34 = Eng/BSB 4:4–37 (+3 shift) | 4:1 note + KD |
| all of ch.6 | MT 6:1 = Eng/BSB 5:31; MT 6:N = Eng 6:(N−1) | 6:1 note |

(Chapter counts confirm it: ch.3 has 33 MT verses, ch.4 has 34, ch.6 has 29.) **But `data/versification_map.json` carries only the two Aramaic-boundary markers** (`DAN-2-4`, `DAN-7-28`, both `diverges:false`) — **none of the three divergence zones is registered.** The 4:1 KD itself flags the omission: "ทั้งบทเลื่อน +3 ควรลงทะเบียนใน versification_map.json **ที่การตรวจท้ายเล่ม**" ("the whole chapter shifts +3, should be registered in versification_map.json at the end-of-book check"). This audit *is* that check.

This is the known **"versification map ship gotcha"** (`ship_chapter.sh` does not stage `versification_map.json`, so divergence chapters' map edits must be committed manually — the same failure mode logged for 1 Kings 5). The translation is correct (right numbering, right notes); the **data file is stale**. **Recommend** registering the three zones in `versification_map.json` (with `diverges:true`, MT↔English mappings) before tagging `book-daniel-v1`, so the reader renderer and `check_versification_anchor.py` have the divergence as ground truth (cf. Nehemiah's five divergence chapters, which *are* registered). **REVIEW (mechanical/data; resolve before tag).** **Severity: MEDIUM** (data-integrity; not a translation defect). *Audit-only mandate: flagged for Ben/maintainer to register; not edited here.*

---

## 17. Persian/Babylonian administrative titles — **STABLE → recommend `persian_achaemenid_administrative_titles_2026-05.md`** (overdue carry-forward)

Daniel re-exercises the imperial administrative vocabulary the Ezra/Nehemiah/Esther audits each flagged for an (still-unwritten) doc: the satrap/prefect/governor/counsellor tiers of the dedication assembly (3:2–3) and the 120-satrap administration + commissioners of ch.6 (6:1–7). Renderings are uniform (the corpus key-term check is clean across the 713-chapter set, which includes Daniel's title load). This is the **fourth** book to introduce uniform-but-undocumented Persian administrative surfaces; the recommended `persian_achaemenid_administrative_titles_2026-05.md` should finally be written, folding in Ezra's set, Nehemiah's governor-tier, Esther's satrap/official tier + `דָּת` decree-tier, and Daniel's ch.3/ch.6 administration. **STABLE.** **Severity: LOW** (but the doc is overdue across four books).

---

## 18. "Spirit of the holy gods" (pagan phrasing) — **STABLE**

A small but theologically careful surface: Nebuchadnezzar and Belshazzar describe Daniel as having "the spirit of the holy gods" (`רוּחַ אֱלָהִין קַדִּישִׁין`, 4:8/9/18; 5:11/14) — pagan polytheistic phrasing in a Gentile king's mouth. The translation keeps the polytheistic register (`วิญญาณของพระบริสุทธิ์`-family with `พระทั้งหลาย` lowercase per `ot_polytheistic_register_2026-05.md`), not the covenant `พระวิญญาณบริสุทธิ์` (Holy Spirit) — correctly *not* importing Christian pneumatology into the king's framing, the same discipline applied at 3:25 (§10). This is distinct from `spirit_of_yhwh_empowerment_2026-05.md` (which governs the divine-empowerment idiom with YHWH as source — N/A here). **STABLE.** **Severity: LOW.**

---

## 19. Inherited corpus locks — all compliant or correctly N/A

| Doc | DAN evidence | Status |
|---|---|---|
| `ot_register_policy §2.2` | §1 — four emperors full ราชาศัพท์ (cross-book DECIDE with Ezra); §3 — madness downshift trigger (REVIEW). | **DECIDE-§1 / REVIEW-§3** |
| `ot_register_policy §2.5` | §2 — Daniel + three friends plain throughout ("the named case"). | **LOCKED** |
| `divine_names_table_2026-05.md` | §5 — God of heaven / Most High / Lord of kings/heaven / Ancient of Days uniform; §6 — YHWH only in ch.9, Adonai vocative sub-rules, 12:8 false positive. | **LOCKED-with-§5-additions** |
| `chesed_covenant_love_2026-05.md` | §7 — 9:4 `ความรักมั่นคง` fires correctly (covenant-loyalty sense). | **LOCKED** |
| `exod_34_attribute_formula_2026-05.md` | §7 — attribute *vocabulary* present (9:4/9/18) but not the Sinai *formula* → correctly does not fire. | **N/A (correct)** |
| `son_of_man_disambiguation_2026-04.md` | §8 — 7:13 `บุตรมนุษย์` (title), 8:17 `บุตรแห่งมนุษย์` (generic) kept distinct; Dan 7:13 named as the title's origin. | **LOCKED-with-§8-REVIEW (register)** |
| `therion_beast_apocalyptic_2026-05.md` | §11 — `สัตว์ร้าย` matches θηρίον lock; Daniel 7 = Rev 13 source, cross-link recommended. | **STABLE** |
| `spiritual_beings_hierarchy_2026-05.md` | §10 — named angels + שַׂר territorial-prince + watcher; doc is Pauline-only → amend. | **STABLE (amend)** |
| `ot_polytheistic_register_2026-05.md` | §10 (3:25 son-of-the-gods) + §18 (spirit-of-the-holy-gods) — pagan register held; lowercase `พระทั้งหลาย`. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` + `ot_canon_and_text_base_2026-05.md` | §15 — §2.3 floor → non-gap; no reader-facing note (unlike Esther) → REVIEW. Inclusion audit 0 candidates, exit 0. | **LOCKED-with-§15-REVIEW** |
| `verse_schema_and_versification_2026-05.md` | §16 — MT numbering correct + verse-level notes; three zones unregistered in map → REVIEW. | **LOCKED-with-§16-REVIEW** |
| `ot_nt_cross_quotation_thread_2026-05.md` | §14 — abomination-of-desolation → Matt 24:15; §11 beasts → Rev 13; §5 Ancient of Days → Rev 1:14. | **STABLE** |
| `proper_names_and_transliteration_2026-05.md` | §17 — Nebuchadnezzar/Belshazzar/Belteshazzar/Shadrach-Meshach-Abednego/Gabriel/Michael; key-term check clean (713-ch corpus). | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | No חַי־יְהוָה oath; Darius's "living God" decree (6:26) is doxological, not an oath formula. | **N/A** |
| `malak_yhwh_2026-05.md` | No מַלְאַךְ־יְהוָה; the furnace figure is `מַלְאֲכֵהּ` "his angel" (3:28, plain) and the named angels are §10. | **N/A** |
| `dtr_history_cycle_formulas_2026-05.md` | Apocalyptic/court narrative, no regnal-evaluation cycle. | **N/A** |
| `i_am_yhwh_holiness_formula_2026-05.md` | No "I am YHWH" self-declaration formula in Daniel. | **N/A** |
| `spirit_of_yhwh_empowerment_2026-05.md` | §18 — only the pagan "spirit of the holy gods"; no YHWH-empowerment idiom. | **N/A** |
| `leitwort_handling_policy_2026-05.md` | §3 — pagan-king-doxology thread (3:31/4:1/4:34/6:26) handled by sustained royal register; §12 Mene-Tekel wordplay. | **STABLE** |

---

## 20. Mechanical (§1)

- 12/12 chapters: `output/check_reports/daniel_NN_review.md` — all green ✓
- 12/12 chapters: `output/back_translations/daniel_NN.json` ✓
- 12/12 chapters: `output/translations/daniel_NN.json` (357 verses) ✓
- 1 chapter: `output/textual_variants/daniel_09.json` — **correct**: the YHWH first-occurrence footnote, and ch.9 is the **only** chapter with the Tetragrammaton (§6). All other chapters owed no footnote.
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** (713-chapter corpus).
- `check_phrase_consistency.py`: **0 violations across 38 audited locks** (20,954 verses).
- `audit_inclusion_variants.py --book daniel --strict`: **0 candidates, exit 0** (the Daniel textual layer is the Additions-recension question, §15, not verse-level inclusion).
- `export_to_usfm.py --book DAN`: **N/A** — the script's `BOOKS` table is NT-only (carried-over OT-USFM concern noted in every prior OT audit).
- **Book-code registration:** `DAN` was present in `OT_CODES` but **missing from the §3/§4 tooling slug tables** (`build_external_review_packet.py` `BOOKS`; `audit_items_to_yaml.py` `BOOK_SLUGS`) — **registered as part of this audit** per the EOB book-code-registration gotcha (Ezra, Nehemiah, Esther each hit this).
- `git status output/`: the only deltas are regenerated check reports — `phrase_consistency.md` (re-run) and `divine_names.md` (the pre-session aggregate refresh carrying the 12:8 soft warning, **a false positive — §6**). No source-file dirt. **`versification_map.json` is NOT dirty — but it should be (§16): the three divergence zones are unregistered.**
- **`divine_names.md` soft warning (DAN 12:8):** false positive — `אֲדֹנִי` single-yodh addressing the angel → `เจ้านายของข้าพเจ้า` is correct; the check conflates `אֲדֹנִי` with standalone divine `אֲדֹנָי` (§6). Recommend teaching the check the single-yodh distinction.

**Severity: GREEN on the consistency gates; one data gap (§16 versification map) to register before tag.**

---

## 21. Flagged for Ben's attention

### DECIDE (blocks the `book-daniel-v1` tag until resolved)

**A. Foreign-monarch register — now a four-book corpus decision (§1).** Daniel grants all four emperors full ราชาศัพท์ (per the written `§2.2`) and holds Daniel-the-vizier plain (§2.5, which names Daniel). It votes with Nehemiah + Esther + the written policy, against Ezra (the lone outlier, incl. Ahasuerus rendered plain at Ezra 4:6 vs full `ทรง` in Esther). All four books shipped, untagged. **Ratify §2.2, write `foreign_monarch_register_2026-05.md`, normalize Ezra to `ทรง`, and tag Ezra + Nehemiah + Esther + Daniel together.** Daniel needs no edit. **MEDIUM-HIGH.**

### REVIEW (worth Ben's confirmation; §15/§16 ideally before tag)

**B. Son-of-Man register vs man-in-linen ambiguity (§8/§9).** 7:13 gives the "one like a son of man" *light* royal register (`เสด็จ`/`ทรง`/`พระพักตร์`), pre-committing toward the divine identification; 10:5–6 keeps the man-in-linen *plain* to preserve christophany/angelophany ambiguity. Confirm the principle and document it together. **MEDIUM.**

**C. Seventy-weeks מָשִׁיחַ (§13).** Rendered generically `ผู้ถูกเจิม`, notes acknowledge but don't endorse the messianic reading. Confirm the non-committal stance for the OT's most-scrutinized messianic verse. **MEDIUM.**

**D. Greek-version Additions disposition note (§15).** Unlike Esther (1:1 note), Daniel excludes the Prayer of Azariah/Song of the Three + Susanna + Bel and the Dragon with *no* reader-facing note. Recommend a single disposition note + a Daniel row in `mt_vs_lxx_textual_variant_handling_2026-05.md`. **LOW-MEDIUM.**

**E. Versification map registration (§16).** Three MT/English divergence zones (ch.3/4 boundary, all ch.4, all ch.6) are disclosed at verse-level but unregistered in `versification_map.json`; the 4:1 KD defers registration to this end-of-book check. Register them before tag. **MEDIUM (data).**

**F. Nebuchadnezzar madness-downshift trigger (§3).** The 4:30 beast-state downshift uses a divine-humiliation trigger §2.2 doesn't name, while Belshazzar's sacrilege (the clearer "grave failure") keeps royal register. Confirm the taxonomy in the foreign-monarch doc. **LOW.**

**G. Daniel-7 beast → Revelation-13 backward-link (§11).** `สัตว์ร้าย` matches the θηρίον lock; record Daniel 7 as the source in `therion_beast_apocalyptic_2026-05.md`. **LOW.**

### New / carry-forward translator_decisions docs recommended

1. **`foreign_monarch_register_2026-05.md`** (§1) — gated on the DECIDE; owed since Ezra, now four books. The single highest-value forward-protection doc.
2. **`biblical_aramaic_2026-05.md`** (§4) — carry-forward from Ezra; Daniel is the major Aramaic book. Locks the language-switch convention + no-YHWH-in-Aramaic→no-footnote rule.
3. **`god_of_heaven_persian_title_2026-05.md`** (§5) — carry-forward from Ezra §6 + Nehemiah; covers Ezra/Neh/Daniel. Add an **Ancient-of-Days** row to `divine_names_table_2026-05.md`.
4. **`danielic_apocalyptic_imagery_2026-05.md`** (§8/§9/§10/§11) — *or* amend `spiritual_beings_hierarchy_2026-05.md` (named angels + שַׂר prince concept) + `therion_beast_apocalyptic_2026-05.md` (Dan 7 source). Forward-protects Revelation.
5. **`persian_achaemenid_administrative_titles_2026-05.md`** (§17) — overdue carry-forward from Ezra/Nehemiah/Esther; now also covering Daniel's ch.3/ch.6 administration.

### Existing docs to amend (optional, no tag block)
- **`ot_register_policy §2.2`** — fold in / point to the §1 foreign-monarch decision once ratified; clarify the downshift trigger (§3).
- **`divine_names_table_2026-05.md`** — add the Ancient-of-Days row (§5); teach the divine-names check the `אֲדֹנִי` single-yodh distinction (§6).
- **`mt_vs_lxx_textual_variant_handling_2026-05.md`** — add the Daniel Additions row (§15).
- **`proper_noun_wordplay_2026-05.md`** — record the Mene-Tekel paronomasia (§12).
- **`ot_nt_cross_quotation_thread_2026-05.md`** — confirm Matt 24:15 (abomination), Rev 1:14 (Ancient of Days), Rev 13 (beasts) forward-links (§5/§11/§14).

### External AI review (§3 of checklist) — pending
Recommended 4-item packet (see `external_review_items_DAN.md`):
1. **Foreign-monarch register — four-book corpus decision** (§1-A, DECIDE)
2. **Son-of-Man light-royal-register vs man-in-linen ambiguity** (§8/§9-B, REVIEW)
3. **Seventy-weeks מָשִׁיחַ non-committal rendering** (§13-C, REVIEW)
4. **Greek-version-Additions disposition note** (§15-D, REVIEW)

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG/1SA/1KI/2KI/1CH/2CH/EZR/NEH/EST pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 6 items (§2 Daniel/friends-§2.5, §6 YHWH-only-ch.9 + Adonai sub-rules, §7 chesed, §14 abomination-of-desolation, §17 proper-names via the clean key-term check, + inherited locks via §19)
- **STABLE:** 7 items (§4 Biblical Aramaic [→ doc], §5 divine titles [→ doc + table row], §9 man-in-linen ambiguity, §10 named angels [→ amend doc], §11 beasts [→ cross-link], §12 Mene-Tekel wordplay, §18 spirit-of-the-holy-gods)
- **REVIEW:** 6 items (§3 madness downshift trigger, §8 Son-of-Man register, §11 beast cross-link, §13 seventy-weeks Messiah, §15 Additions note, §16 versification map)
- **DECIDE:** 1 item (§1 foreign-monarch register — now a four-book corpus decision)

**One DECIDE item blocks the `book-daniel-v1` tag** — and like Ezra/Nehemiah/Esther's, it is a **clean, deliberately-deferred policy ratification, not a surface defect**: Daniel follows the written §2.2 and is internally uniform; what is owed is the corpus-wide ratification (now over four shipped books) + the `foreign_monarch_register` doc, after which Ezra is normalized and all four are tagged together.

**One mechanical/data item (§16 versification map) should be resolved before tag** — register the three divergence zones the 4:1 KD itself defers to this check.

**Five new/carry-forward translator_decisions docs recommended** (three overdue carry-forwards from Ezra/Nehemiah/Esther; two Daniel-distinctive). **Five optional existing-doc amendments.**

---

## Recommendation

**Daniel ships in strong corpus-hygiene shape.** It is the most demanding OT book the pilot has audited — bilingual, four emperors, the first named angels, the OT source of several NT-forward apocalyptic surfaces — and its inherited locks all hold or are correctly N/A: Daniel's §2.5 plain register is "the named case," the four emperors' §2.2 royal register is uniform, the chesed lock fires at its covenant sense, `บุตรมนุษย์` / `บุตรแห่งมนุษย์` are kept distinct, the beasts match the θηρίον lock, and the pagan-king register discipline (3:25 son-of-the-gods, 4:8 spirit-of-the-holy-gods) is exemplary. The Tetragrammaton-only-in-ch.9 fact is handled with exactly one textual-variant file.

**The work to do before v1 is, as with Ezra/Nehemiah/Esther, overwhelmingly documentation and one corpus decision, not correction:**

- **§1 is the headline and is bigger than Daniel.** Daniel is the *fourth* and final book of the court block the register decision was deferred to, and it casts the strongest vote: it grants all four emperors `ทรง` and holds the vizier `§2.5` plain — the book where both halves of the policy are exercised hardest. Ratify §2.2 once, write `foreign_monarch_register_2026-05.md`, normalize Ezra, and tag all four books together. **Daniel needs no edit.**
- **§16 (versification map)** is the one mechanical item to fix before tagging — register the three divergence zones, as the 4:1 KD itself instructs.
- **§8/§13/§15** are the editorial confirmations worth Ben's eye (Son-of-Man register; seventy-weeks Messiah; Additions note) — all three are excellent external-AI questions.
- **The three overdue carry-forward docs** (`foreign_monarch_register`, `biblical_aramaic`, `god_of_heaven_persian_title`, plus `persian_achaemenid_administrative_titles`) should finally be written now — they have been owed since Ezra, and `danielic_apocalyptic_imagery` forward-protects Revelation, the next great apocalyptic surface.

**Tag `book-daniel-v1` after:**
1. Ben's decision on the **§1 foreign-monarch register** (ratify + doc + normalize Ezra) — **jointly with the Ezra, Nehemiah, and Esther tags.**
2. **§16** versification-map registration.
3. Ben's confirmation on **§8 / §13 / §15**.
4. External AI sanity-check (the 4-item packet).
5. The carry-forward Persian-block + Aramaic + apocalyptic docs written (or the existing docs amended).

**The single highest-value forward-protection step remains the §1 register decision** — open since Ezra, now a visible four-book inconsistency on shared Babylonian/Persian kings. Daniel is the natural place to close it: it is the last book of the very block the decision was deferred to, and the book whose own key_decisions cite §2.2 and §2.5 by name on nearly every royal verb.
