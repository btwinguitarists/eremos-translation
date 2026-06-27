# Malachi — End-of-Book Review

**Date:** 2026-06-27
**Scope:** All 3 chapters (55 verses; MT versification — MT 3:19–24 = English 4:1–6); `glossary.json`; existing `docs/translator_decisions/`.
**Trigger:** MAL 3 shipped (commit `bacfbcd3`); per `docs/END_OF_BOOK_CHECKLIST.md`.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **11 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 3/3 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings); `check_phrase_consistency.py` clean across all 38 audited locks; `check_divine_names` reports **zero warnings** in all 3 chapters. `git status output/` shows only re-ran-check artifacts (`divine_names.md`, `phrase_consistency.md`) — no source-file dirt.
- **Status counts: 4 LOCKED · 3 STABLE · 3 REVIEW · 1 DECIDE.**
- **1 DECIDE blocks `book-malachi-v1`:** §1 — the **מַלְאָךְ "messenger" leitwort** (the book's namesake) renders the *human* messengers of 2:7 (the priest) and 3:1a (the forerunner) as **ทูตสวรรค์** ("heaven-messenger / angel") per the `malak_yhwh_2026-05` §4.3 body-text lock — in tension with that same doc's §1/§4.4 *human-register* carve-out, and entangled with the **open Zechariah §1 DECIDE** (which proposes *dropping* สวรรค์ for the theophanic angel-of-YHWH). The two must be resolved together.
- **3 REVIEW** (worth Ben's confirmation): §6 the 2:16 "I hate divorce" textual/grammatical crux; §7 the 2:15 crux (subject supplied); §11 `export_to_usfm.py` still rejects MAL (infrastructure).
- **Messianic-surface discipline is the cleanest-tier positive (§5):** every NT-reception note (3:1 forerunner→John; 3:1b Lord-to-temple; 3:20 sun-of-righteousness; 3:23 Elijah→John) lives **only** in §14 footnotes — **zero bare `คือพระคริสต์` in any verse body**. Reinforces the still-unwritten `committal_messianic_surface_2026-06` doc (Zechariah anchor).
- **Sidesteps the open Amos §1 entirely:** Malachi has **no אֲדֹנָי יְהוִה compound** anywhere (like Nahum / Haggai / Zechariah). Bare Adonai → องค์เจ้านาย throughout.
- **Cleanest-tier mechanical state:** versification zone MT 3:19–24 = Eng 4:1–6 **registered + committed** (`data/versification_map.json`, MAL-3-19…24); L2 tetragrammaton footnote present all 3 ch; no §13 anthropomorphism friction (no first-person divine body-part in the book).
- **Registration fixes applied this audit** (were missing): `MAL` added to `build_external_review_packet.py` `BOOKS` dict and to `audit_items_to_yaml.py` `BOOK_SLUGS` (it was in `OT_CODES` only — packet/yaml build would have failed).
- **External AI review (§3):** packet built; 4 reviewer questions generated.

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse-level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. מַלְאָךְ "messenger" leitwort — human messengers rendered ทูตสวรรค์ — **DECIDE** (headline; blocks v1)

This is the book's signature. The name **מַלְאָכִי** (1:1, lit. "my messenger") opens it; the lemma recurs as the structural hinge of ch. 3. Every occurrence ships the locked head-noun **ทูตสวรรค์** ("heaven-messenger / angel"):

| Verse | Hebrew | Referent | Thai (shipped) |
|---|---|---|---|
| 1:1 | מַלְאָכִי | the prophet's name | **มาลาคี** (translit. + footnote on the "my-messenger" meaning) |
| 2:7 | מַלְאַ֥ךְ יְהוָֽה־צְבָא֖וֹת | **the human Levitical priest** | ทูตสวรรค์ขององค์พระผู้เป็นเจ้าจอมโยธา |
| 3:1a | מַלְאָכִ֔י | **the human forerunner** (→ John the Baptist, Matt 11:10) | ทูตสวรรค์ของเรา |
| 3:1b | מַלְאַ֨ךְ הַבְּרִ֜ית | the Messenger of the covenant (divine/messianic) | ทูตสวรรค์แห่งพันธสัญญา |

**The discipline is internally consistent and explicitly documented for this book.** `malak_yhwh_2026-05` §4.3 names Malachi by title — *"the book whose Hebrew title IS מַלְאָכִי"* — and rules: *"the book title is rendered 'มาลาคี' (transliteration); the lemma in the body text retains the lock."* The KDs for 2:7 and 3:1 cite exactly this: keep the uniform head-noun ทูตสวรรค์, carry the human-messenger nuance in the footnote. So the surface is **lock-compliant**, and the OT→NT lemma thread (מַלְאָךְ = ἄγγελος → ทูตสวรรค์) stays unbroken into Matt 11:10 / Mark 1:2 / Luke 7:27.

**Why it is nonetheless a DECIDE.** ทูตสวรรค์ literally = "heaven-messenger," i.e. **angel**. The same `malak_yhwh_2026-05` doc that mandates the lock also draws an explicit boundary in §1 and §4.4: *"For purely human messengers in non-supernatural narrative … use the plain register ผู้ส่งสาร or ทูต as context requires; that is outside this lock."* Malachi sits **astride that boundary**:

- **2:7 — the priest** is a flesh-and-blood Levitical priest. Hebrew exalts him with the divine-messenger *title* (מַלְאַךְ יְהוָה צְבָאוֹת), but he is not a supernatural being. Reading "the priest is **ทูตสวรรค์** (an angel) of the LORD of hosts" risks, in Thai, asserting angelic ontology the Hebrew metaphor does not.
- **3:1a — the forerunner** is the human herald the NT identifies as John the Baptist. Same issue: ทูตสวรรค์ ("angel") for a human prophet.
- **3:1b — the Messenger of the covenant** is, on the classical reading, the divine/messianic figure ("the Lord whom you seek will come to his temple"); here ทูตสวรรค์ is least problematic.

§4.3 was written *anticipating the name-form and the 3:1 forerunner* — it did **not** separately adjudicate the **human priest of 2:7**, which surfaces only in Malachi (this is the corpus's only place מַלְאַךְ יְהוָה is applied to a human).

**Entanglement with the open Zechariah §1 DECIDE.** Zechariah's audit proposed the *opposite* move for the *theophanic* angel: drop สวรรค์ → ทูตขององค์พระผู้เป็นเจ้า, reserving ทูตสวรรค์ for ordinary/interpreting angels. If Zech §1a is ratified, Malachi becomes maximally anomalous: the *divine* angel-of-YHWH loses สวรรค์ while the *human* priest of 2:7 keeps it. **These two DECIDEs cannot be resolved independently.**

**Three coherent end-states for Ben to choose among** (no change proposed here — ratification gate):

1. **Hold the lock as shipped** (status quo): all מַלְאָךְ → ทูตสวรรค์, human nuance in footnote, §4.3 governs uniformly. Simplest; preserves the lemma thread; accepts that a human priest/forerunner reads as "angel."
2. **Human/divine split**: 2:7 + 3:1a → plain human register (ทูต / ผู้ส่งสาร) per §4.4; 3:1b retains ทูตสวรรค์ as the divine Messenger of the covenant. Most faithful to the human/supernatural distinction; **breaks** the מַלְאָכִי 1:1↔3:1 surface echo.
3. **Resolve jointly with Zech §1**: adopt a corpus-wide ทูต-without-สวรรค์ default and reserve สวรรค์ only for explicitly-angelic beings — which would pull 2:7 / 3:1 along and require the malak doc amendment + back-sweep Zechariah already flagged.

→ **Flagged as external review Item A.** Resolution should **amend `malak_yhwh_2026-05`** (§4.3 + a new human-messenger-in-Malachi row) and be decided in the same sitting as the Zechariah §1 malak DECIDE.

---

## 2. יְהוָה צְבָאוֹת "LORD of Hosts" — **LOCKED**

Malachi is saturated with the title (≈21 occurrences: 1:4, 1:6, 1:8, 1:9, 1:10, 1:11, 1:13, 1:14; 2:2, 2:4, 2:7, 2:8, 2:12, 2:16; 3:1, 3:5, 3:7, 3:10, 3:11, 3:12, 3:14, 3:17, 3:19, 3:21 — frequently as the closing speech-formula אָמַר יְהוָה צְבָאוֹת). Uniformly → **องค์พระผู้เป็นเจ้าจอมโยธา**, the corpus lock (= Jas 5:4; `divine_names_table_2026-05`). No drift. **LOCKED.**

---

## 3. Bare Adonai / הָאָדוֹן — **LOCKED** (with one REVIEW sub-note)

Three non-Tetragrammaton "Lord" surfaces, all → **องค์เจ้านาย**:

| Verse | Hebrew | Referent | Thai |
|---|---|---|---|
| 1:12 | שֻׁלְחַ֤ן אֲדֹנָי | "the table of the Lord" (the altar) | โต๊ะขององค์เจ้านาย |
| 1:14 | לַֽאדֹנָ֑י | "to the Lord" (vs YHWH-Sabaoth in the same verse) | องค์เจ้านาย |
| 3:1 | הָאָד֣וֹן | "the Lord" who comes to his temple | องค์เจ้านาย |

The rendering complies with the corpus bare-Adonai → องค์เจ้านาย line (Lam test-case forward-protection; Zech 9:4). Two strengths worth recording:

- **Hebrew-internal YHWH/Adonai distinction is preserved in Thai.** The "table" idiom appears twice: 1:7 reads שֻׁלְחַן **יְהוָה** → โต๊ะขององค์**พระผู้เป็นเจ้า**, while 1:12 reads שֻׁלְחַן **אֲדֹנָי** → โต๊ะขององค์**เจ้านาย**. The translator tracked the source's own lexical switch rather than flattening — a clean discipline the L2 footnote even cross-references.
- **No אֲדֹנָי יְהוִה compound anywhere in Malachi** — so the book **sidesteps the open Amos §1 DECIDE** entirely (the Nahum / Haggai / Zechariah pattern).

**REVIEW sub-note:** at **3:1** הָאָדוֹן is a *divine/messianic* referent ("the Lord … will come to his temple"), yet it carries the same องค์เจ้านาย used for the more generic 1:12/1:14 "Lord." Defensible (the article-marked הָאָדוֹן is a deliberately reverent-but-not-Tetragrammaton title), but the messianic weight of 3:1 makes it worth Ben's eye — see external review Item D.

---

## 4. Tetragrammaton Layer-1 + Layer-2 footnote — **LOCKED**

YHWH (often as YHWH-Sabaoth) is dense across all 3 chapters; Layer-1 → องค์พระผู้เป็นเจ้า throughout, and a **Layer-2 first-occurrence footnote is present in every chapter** (`output/textual_variants/malachi_0{1,2,3}.json`). `check_divine_names` is clean (zero warnings) in all 3 — **no** Micah-ch5 / Joel-ch3 / Lam-ch2-3 missing-footnote gap.

**Minor note (not a blocker):** ch. 3's L2 footnote is typed **`nt_citation_note`** rather than `tetragrammaton_convention_first_occurrence` (the tetragrammaton-convention text is *folded into* the NT-citation note). This is the same type-bundling that produced a `check_divine_names` WARN in Joel ch. 3 — but here the check passes clean, because the ch.3 note still opens with the องค์พระผู้เป็นเจ้า = יהוה convention statement. Worth keeping on the radar if the divine-names checker is ever tightened to key on `type` exactly. **LOCKED.**

---

## 5. Messianic-reception restraint — **STABLE** (positive; reinforces recommended doc)

Malachi is one of the most NT-cited OT books, and the translation holds the committal line at **cleanest-tier**: **every** reception note lives in a §14 footnote, **none** is asserted in a verse body (verified: `พระคริสต์` / `เมสสิยาห์` / `คริสตชน` / `ยอห์น` / `บัพติศมา` appear **only** in footnotes/KDs, never in `translation.thai`):

| Verse | Surface (plain) | Reception (footnote only) |
|---|---|---|
| 3:1 | ทูตสวรรค์ของเรา … ท่านกำลังจะมา | "my messenger" = John the Baptist (Matt 11:10 / Mark 1:2 / Luke 7:27) |
| 3:1b | ทูตสวรรค์แห่งพันธสัญญา | the Lord-to-his-temple read christologically |
| 3:20 (Eng 4:2) | ดวงอาทิตย์แห่งความชอบธรรม | "sun of righteousness" — christological reading framed คริสตชน… |
| 3:23 (Eng 4:5) | เอลียาห์ผู้เผยพระวจนะ | Elijah = John (Matt 11:14; 17:10-13; Luke 1:17) |

The Branch-style restraint (plain surface + reception-only footnote, no bare `คือพระคริสต์`) puts Malachi alongside Zechariah as the **strongest anchors** for the still-unwritten **`committal_messianic_surface_2026-06`** doc (rec'd from Haggai, re-anchored at Zechariah). Clean of the Ezekiel §14 regression. **STABLE — recommend the corpus doc be written before the NT books re-cite these verses.**

---

## 6. 2:16 "I hate divorce" — textual/grammatical crux — **REVIEW**

> כִּֽי־שָׂנֵ֣א שַׁלַּ֗ח אָמַ֤ר יְהוָה֙ אֱלֹהֵ֣י יִשְׂרָאֵ֔ל … (MT)
> **Shipped:** "‘เพราะเราเกลียดการหย่าร้าง’ องค์พระผู้เป็นเจ้าพระเจ้าแห่งอิสราเอลตรัสดังนี้ …"
> **BSB:** "'For I hate divorce,' says the LORD, the God of Israel."

The Hebrew שָׂנֵא שַׁלַּח is famously unstable: (a) the traditional reading takes God as speaker — "I hate divorce" (so KJV/BSB/NIV-1984); (b) a grammatically defensible alternative reads the participle as 3rd-person — "**he who** divorces [out of] hate covers his garment with violence" (ESV/NRSV/NIV-2011). The translation takes (a), with (b) footnoted, and renders the second clue וְכִסָּה חָמָס עַל־לְבוּשׁוֹ as เอาความทารุณคลุมเสื้อผ้าของตน.

The shipped reading is MT-defensible and matches the source-of-record BSB, and the alternate is disclosed in-footnote. Flagged because (i) it is a genuine textual/grammatical fork with **pastoral/ethical weight** in Thai church usage, and (ii) modern critical consensus has shifted toward (b). → External review **Item B**.

---

## 7. 2:15 crux — subject supplied — **REVIEW**

> וְלֹא־אֶחָ֣ד עָשָׂ֗ה וּשְׁאָ֥ר ר֨וּחַ֙ ל֔וֹ … (MT — one of the hardest verses in the prophets)
> **Shipped:** "พระองค์มิได้ทรงสร้างเขาทั้งสองให้เป็นหนึ่งเดียว ทั้งเนื้อและจิตวิญญาณหรือ? …"

The MT is elliptical — literally "and-not one he-made, and-remnant-of spirit to-him." Almost every modern version supplies a subject and an object to make sense of it; BSB supplies "the LORD … made them one." The Thai follows that interpretive path (พระองค์ = God as subject; เขาทั้งสอง = the couple). This is a defensible, BSB-aligned rendering of an admittedly opaque verse, but the supplied subject/object goes beyond the bare MT surface. Lower-stakes than §6 (no live alternative changes the marriage-fidelity thrust), but worth a confirming glance. → External review **Item C**.

---

## 8. "Day of YHWH" leitwort — **STABLE** (reinforces recommended doc)

The book climaxes on the Day motif: 3:2 "the day of his coming"; 3:17 "the day when I act"; **3:19 (Eng 4:1)** "the day is coming, burning like a furnace"; **3:23 (Eng 4:5)** יוֹם יְהוָה הַגָּדוֹל וְהַנּוֹרָא → **วันแห่งองค์พระผู้เป็นเจ้าอันยิ่งใหญ่และน่าสะพรึงกลัว**. The rendering is uniform with the Joel / Amos / Obadiah / Zephaniah / Zechariah witnesses and makes Malachi the **canonical-closing** data point for the still-unwritten **`day_of_the_lord_leitwort_2026-06`** doc. **STABLE.**

---

## 9. Versification — MT 3:19–24 = English 4:1–6 — **LOCKED**

Malachi follows MT chapter division: the book ends at MT 3:24, where MT 3:19–24 = English/BSB 4:1–6. The mapping is **registered and committed** in `data/versification_map.json` (keys `MAL-3-19` through `MAL-3-24`, each carrying `mt_ref` / `english_ref` / `bsb_ref` / `lxx_ref`). `git status` clean. The 3:23 KD also states the equivalence inline ("English versification: this verse = Malachi 4:5"). Cleanest-tier — **no** unregistered-zone gap (unlike Ezekiel 21 / earlier prophets). **LOCKED.**

---

## 10. Divine anthropomorphism (§13) — **STABLE** (no friction)

Malachi is almost entirely first-person divine speech, but it contains **no first-person divine body-part idiom** (no יָדִי / זְרֹעִי / עֵינַי / פִּי / אַפִּי — verified by scan). The honorific-binding check is clean in all 3 chapters. So Malachi adds **no new data** to the open Isaiah/Jeremiah/Ezekiel/Zephaniah §13 "first-person-body-part-plain" DECIDE — it neither moves nor reopens it (the Nahum / Habakkuk / Haggai pattern). **STABLE.**

---

## 11. `export_to_usfm.py` rejects MAL — **REVIEW** (infrastructure)

As with every prophet audited to date, `scripts/export_to_usfm.py` does not yet recognize the `MAL` book code, so a USFM export of Malachi is not yet possible. Not a translation issue and not a v1-tag blocker, but logged for the eventual USFM-coverage sweep. (The packet builder and audit-yaml registrations were both **fixed this audit** — see Summary.) **REVIEW.**

---

## Appendix — items NOT flagged (verified compliant)

- **Key-term & phrase consistency:** 0 / 0 violations across Malachi.
- **`สิบลด` (tithe, 3:8/3:10), `สาปแช่ง` (curse), `พันธสัญญา` (covenant):** consistent with corpus key-terms.
- **`ชั่วร้าย` / `ชั่ว` (evil):** 1:8 "is it not evil?" follows the corpus lock.
- **Foreign-monarch register:** N/A — Malachi names no foreign king (post-exilic but kingless in the text), so the open Ezra/Neh/Esther/Daniel + Jeremiah/Ezekiel monarch threads are **not implicated**.
- **Exodus-34 formula / chesed:** not invoked in Malachi (1:2 "I have loved you" is אָהַב, not the Exod-34 doxology) — no formula-lock interaction.
</content>
</invoke>
