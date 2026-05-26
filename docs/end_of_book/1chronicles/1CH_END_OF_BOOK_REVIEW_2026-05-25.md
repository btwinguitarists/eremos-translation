# 1 Chronicles — End-of-Book Review

**Date:** 2026-05-25
**Scope:** All 29 chapters of 1 Chronicles (943 verses); `glossary.json`; `docs/translator_decisions/` corpus (~96 docs through the 2 Kings end-of-book audit).
**Trigger:** 1CH 29 shipped (commit `448aaaa`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Twelfth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings) and the **first book of the Chronicler's History** — a distinct literary world from the five Former-Prophets / Deuteronomistic books that precede it. 1 Chronicles is the corpus's first sustained encounter with three things at once: (a) **nine chapters of dense genealogy** (chs 1–9, Adam → the post-exilic returnees) — the largest proper-name-only stretch in the corpus; (b) the **Samuel↔Chronicles synoptic relationship** at scale (1 Chr 10–29 ≈ 1 Sam 31 + 2 Sam 5–24), the first OT-side downstream test of `synoptic_parallel_passages_2026-05.md`; and (c) the **threshing-floor angel-of-YHWH narrative (ch 21 = 2 Sam 24)** — the next divine-מַלְאַךְ test after the 1 Kings 19:7 drift and the 2 Kings clean ship.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **18 cross-cutting items reviewed.** Mechanical gates (§1) pass: 29/29 chapters have green per-chapter reports + back-translations + translations (943 verses); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the 632-chapter corpus); `check_phrase_consistency.py` clean across all 12 audited locks (19,190 verses). The single dirty file in `git status output/` is `output/check_reports/divine_names.md` — a transient single-chapter scratch report whose only diff clears a stale 2SA 1:10 warning; report-only, not a 1 Chronicles translation surface, identical in kind to the note carried in the 1SA / 1KI / 2KI audits.
- **1 Chronicles is the THIRD consecutive book to ship the mal'akh-YHWH lock cleanly — and the first to do so completely OUTSIDE the lock's machine-enforcement scope.**
  - **`malak_yhwh_2026-05.md` HOLDS in the ch-21 threshing-floor narrative.** All five divine מַלְאַךְ occurrences — **21:12, 21:15, 21:16, 21:18, 21:30** — ship the locked **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** (or `ทูตสวรรค์` for the standalone/back-reference forms). This is the parallel narrative to 2 Sam 24 and the clean opposite of the 1 Kings 19:7 drift. **Critically, the malak lock's `check_phrase_consistency.py` enforcement is scoped `["1KI ", "2KI "]` — 1 Chronicles was NOT machine-checked**, and 1 Chr 21 is **not** on the `malak_yhwh_2026-05.md` §3 forward-cover checklist (only "2 Sam 24 (David)" is, still deferred to the cross-book retrofit). The chapter shipped the lock correctly by convention alone. See §3. **REVIEW** (extend lock scope to lock in this win).
- **0 items flagged DECIDE.** For the first time since the Former-Prophets OT books began, the audit finds **no Ben-decision blocker for the `book-1chronicles-v1` tag**. The MT/LXX inclusion-variant gap that was a DECIDE in 1SA §17 + 1KI §17 is **resolved as a non-gap** under the `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3 disclosure-threshold floor (added 2026-05-25, 2 Kings EOB): Chronicles' LXX (Paraleipomena) is textually close to MT with **no macro-structural divergence** (no 3-Reigns-style reordering, no Miscellanies), so its YHWH-only `textual_variants` files are compliant. See §16.
- **5 items flagged REVIEW** (worth Ben's confirmation):
  - **§3 mal'akh-YHWH lock unenforced + unlisted for 1CH** — the lock HELD in ch 21 but only by convention; recommend widening the `check_phrase_consistency.py` `malak` scope to include 1 Chronicles and ticking 1 Chr 21 onto the §3 forward-cover checklist (it is the clean twin of the still-deferred 2 Sam 24 retrofit).
  - **§6 Samuel↔Chronicles synoptic-divergence documentation completeness** — agent / name divergences are well-documented (21:1 Satan, 19:16 Shophach, 21:15 Ornan=Araunah, 20:5 Elhanan/Lahmi-Goliath, 11:11 Jashobeam), but several **number** divergences `synoptic_parallel_passages_2026-05.md` §"Per-verse documentation" specifically names are unflagged: **21:5 census totals** (the doc explicitly names "2 Sam 24:9 census totals"), **21:25 price** (600 shekels gold vs 2 Sam 24:24's 50 shekels silver), **11:11** (300 vs 2 Sam 23:8's 800).
  - **§3b mal'akh human-messenger surface** — 1 Chronicles renders human envoys as `ทูต` (14:1 Hiram, 19:2 David to Hanun) + the paraphrase `ส่งคน` (19:16). A **fifth** corpus surface-set alongside 1SA's `ผู้ส่งสาร`/`ผู้ส่งข่าว`, 1KI's `ผู้สื่อสาร`, 2KI's `ผู้ส่งสาร`/`ทูต`/`คณะทูต`.
  - **§4b 28:12 בָּרוּחַ "by the spirit" vs BSB "in mind"** — the Thai follows BSB's interpretive "all that David had in mind" (`ทุกสิ่งที่ดาวิดทรงดำริไว้`) over the MT's literal בָּרוּחַ ("by the spirit [that was with him]"); the divergence is verse-noted, but it is a translation-base call (MT-anchored vs BSB-gloss) worth confirming.
  - **§13 "until this day" leitwort** — 1 Chronicles uniform `จนถึงทุกวันนี้` (4:41, 17:5); now **JDG + 1KI + 2KI + 1CH all agree**, leaving **1 Samuel the lone corpus outlier** (`จนถึงวันนี้`). Sharpens the standing 1KI §14 / 2KI §11 normalization case.
- **No new corpus docs strongly required.** Two STABLE-but-undocumented threads are worth a Layer-2 note rather than a doc (see §8 inner-OT psalm-quotation forward-watch; §10 NT doxology/sojourner echoes). The previously-recommended `name_theology_deuteronomistic_2026-05.md` (1KI §H / 2KI §10) is **N/A for 1 Chronicles** — the Name-centralization formulas belong to the temple-construction narrative in 2 Chronicles, not David's preparatory chapters here.
- **External AI review (§3) pending.** Suggested 5-item packet (mal'akh lock-scope §3; Samuel↔Chronicles divergence-documentation completeness §6; human-messenger surface §3b; 28:12 בָּרוּחַ translation-base §4b; "until this day" cross-book §13).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה compliance — **LOCKED**

YHWH renders as `องค์พระผู้เป็นเจ้า` throughout. **176 surface occurrences** of `องค์พระผู้เป็นเจ้า` in `thai` verse-text across the 29 chapters (≈ the MT YHWH-verse count for 1 Chronicles; the count is suppressed relative to the narrative books because chs 1–9 are genealogy — five of those nine chapters carry **zero** YHWH).

**ยาห์เวห์ residues in verse text: zero.** No `ยาห์เวห์` surface in any 1 Chronicles `thai` field. (Place-name memorial compounds — the only sanctioned `ยาห์เวห์` survival per `divine_names_table_2026-05.md` — do not occur in 1 Chronicles.)

**Per-chapter first-occurrence YHWH footnote.** 23/23 chapters that contain YHWH carry the locked Tier-2 explanation in `output/textual_variants/1chronicles_NN.json` (`type: tetragrammaton_convention_first_occurrence`). The **six chapters with no `textual_variants` file (1, 3, 4, 7, 8, 20)** are exactly the six with **zero** YHWH surface (the genealogy chapters 1/3/4/7/8 + the David-wars summary ch 20) — no first-occurrence footnote is owed. Spot-checked and clean; this is the convention, not a gap.

**LOCKED** ✓ per `divine_names_table_2026-05.md`.

---

## 2. Elohim + Adonai divine names — **LOCKED (the 1KI §8 Adonai-compound DECIDE does NOT recur)**

- **Elohim → พระเจ้า** uniform across 1 Chronicles ✓. No drift.
- **No אֲדֹנָי occurs anywhere in 1 Chronicles** (Hebrew-grep across all 943 verses: zero). This is itself a significant cross-book datapoint: the Chronicler's version of David's covenant prayer (**1 Chr 17**, parallel to 2 Sam 7) systematically uses **`יְהוָה` / `יְהוָה אֱלֹהִים` / `אֱלֹהִים`** in exactly the slots where 2 Sam 7:18–29 used the **אֲדֹנָי יְהוִה** compound seven times. The 1 Kings 8:53 sentence-final-vocative DECIDE (1KI §8) and the 2 Sam 7 appositional-bare anchor therefore **add no new datapoint here** — there is no compound to position. See §9.
- **`ข้าแต่` vocative for direct YHWH-address in prayer.** David's ch-17 covenant prayer (17:16, 17:19, 17:20, 17:26, 17:27) and his ch-29 assembly prayer (29:10, 29:11, 29:18) address the plain Tetragrammaton יְהוָה → `ข้าแต่องค์พระผู้เป็นเจ้า`. Standard YHWH-vocative, compliant. The embedded quoted name יְהוָה צְבָאוֹת at 17:24 correctly takes **no** `ข้าแต่` (it is a quoted title, not a vocative) → `องค์พระผู้เป็นเจ้าจอมโยธา` (Tsebaoth compound preserved ✓).

**LOCKED** ✓.

---

## 3. mal'akh-YHWH (ch 21, threshing floor) — **LOCKED (the lock HOLDS) + REVIEW (unenforced & unlisted for 1CH)**

`malak_yhwh_2026-05.md` (locked 2026-05-13, tri-AI review) requires every divine מַלְאָךְ → **`ทูตสวรรค์`**, with the genitive carried by `ของ` + the divine-name form (מַלְאַךְ יְהוָה → **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`**). 1 Chronicles 21 is the corpus's third major divine-mal'akh narrative (after 1 Kings 19 and 2 Kings 1/19) and the **parallel to 2 Sam 24**. **All six mal'akh references in ch 21 comply:**

| Ref | Hebrew | 1CH Thai (shipped) | Status |
|---|---|---|---|
| **21:12** | מַלְאַךְ יְהוָה ("the angel of YHWH ravaging") | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้าทำลาย…`** | ✓ |
| **21:15** | מַלְאָךְ (God sent) + הַמַּלְאָךְ הַמַּשְׁחִית + מַלְאַךְ יְהוָה | `ทูตสวรรค์องค์หนึ่ง` + `ทูตสวรรค์ผู้ทำลาย` + **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✓ |
| **21:16** | מַלְאַךְ יְהוָה ("standing between heaven and earth") | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✓ |
| **21:18** | מַלְאַךְ יְהוָה (ordered Gad) | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✓ |
| **21:20** | הַמַּלְאָךְ (Ornan saw the angel) | `ทูตสวรรค์` | ✓ |
| **21:27** | לַמַּלְאָךְ (YHWH spoke to the angel) | `ทูตสวรรค์` | ✓ |
| **21:30** | מַלְאַךְ יְהוָה ("sword of the angel of YHWH") | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✓ |

The two bare-`ทูต` surfaces in the chapter (21:15 "ขณะที่**ทูต**กำลังทำลายอยู่"; 21:27 "และ**ทูต**ก็เก็บดาบ") are **back-references in Thai discourse** to an angel already introduced as `ทูตสวรรค์` in the same verse — pronoun-style subject continuations, **not** fresh renderings of the divine compound. This is the exact opposite of the 1 Kings 19:7 drift, where the *compound itself* (מַלְאַךְ יְהוָה) dropped `สวรรค์`. No drift in 1 Chronicles.

**The REVIEW is about enforcement, not the surface.** The lock held in ch 21 by convention only:
- `check_phrase_consistency.py`'s `malak` lock is scoped **`["books": ["1KI ", "2KI "]]`** — 1 Chronicles is outside it. The clean phrase-consistency result for 1CH reflects out-of-scope, not a passed check. The ch-21 compliance verified in this audit is a **manual** finding.
- `malak_yhwh_2026-05.md` §3's forward-cover checklist names "**2 Sam 24 (David)**" — the *parallel* to 1 Chr 21 — but it is still `[ ]` (deferred to the cross-book retrofit). 1 Chronicles 21 itself is not listed.

**REVIEW — recommended:** widen the `malak` lock's permanent scope to add `"1 Chronicles "` (matching the `reference` prefix), then tick 1 Chr 21 onto the §3 forward-cover checklist. There is a clean symmetry worth recording: **1 Chr 21 ships the divine מַלְאַךְ correctly while its 2 Sam 24 twin still awaits the deferred retrofit** — when that retrofit runs, 1 Chr 21 is the standard 2 Sam 24 should match. **Severity: LOW** (no surface edit; locks in a held win). Not a tag blocker.

---

## 3b. mal'akh human-messenger surface — **REVIEW (fifth cross-book variant)**

Per `malak_yhwh_2026-05.md` §4.4, human-messenger מַלְאָךְ is outside the divine lock. 1 Chronicles renders human envoys as:

| Ref | Hebrew | 1CH Thai |
|---|---|---|
| 14:1 | מַלְאָכִים (Hiram of Tyre to David) | `ทูต` |
| 19:2 | מַלְאָכִים (David's condolence envoys to Hanun) | `ทูต` |
| 19:16 | מַלְאָכִים (Arameans summoning reinforcements) | `ส่งคน(ไป)` (paraphrase) |

This continues the corpus's standing cross-book human-messenger surface variance — now five sets: 1SA `ผู้ส่งสาร` / `ผู้ส่งข่าว`; 1KI `ผู้สื่อสาร`; 2KI `ผู้ส่งสาร` / `ทูต` / `คณะทูต`; and 1CH `ทูต` / `ส่งคน`. 1 Chronicles' `ทูต` matches 2 Kings 17:4. The 19:16 `ส่งคน` is a smoothing paraphrase (the messengers are not the verse's focus), defensible but adds a surface.

**REVIEW.** Folds into the same cross-book normalization the 1KI §3b / 2KI §3b flags already opened (recommended canonical: `ผู้ส่งสาร`). **Severity: LOW.**

---

## 4. Spirit-of-YHWH / Spirit-of-God — **LOCKED (the empowerment lock holds; first לָבַשׁ-class downstream ship)**

`spirit_of_yhwh_empowerment_2026-05.md` requires the divine empowering Spirit to keep the **`พระ`** honorific (`พระวิญญาณขององค์พระผู้เป็นเจ้า` / `พระวิญญาณของพระเจ้า`). 1 Chronicles has one empowerment occurrence + two non-divine רוּחַ:

- **12:18 (Heb 12:19) — Amasai, the לָבַשׁ-class.** וְרוּחַ לָבְשָׁה אֶת־עֲמָשַׂי ("the Spirit clothed Amasai," producing his inspired oath of loyalty to David) → **`แล้วพระวิญญาณก็เสด็จมาสวมทับอามาสัย`** — the `พระ` honorific intact + the royal verb `เสด็จ` + `สวมทับ` ("clothed upon"). The Hebrew here is **anarthrous bare רוּחַ** (no יְהוָה / אֱלֹהִים construct), but it is the same לָבַשׁ idiom as Judg 6:34 (Gideon) and 2 Chr 24:20 (Zechariah), and the translator correctly read it as the divine Spirit and applied the honorific. This is the **first downstream ship of the לָבַשׁ class** (one of the doc's four empowerment verbs: הָיָה עַל / לָבַשׁ / פָּעַם / צָלַח) and it ships cleanly. ✓
- **5:26 — non-divine רוּחַ.** "God stirred up the **spirit** of Pul/Tiglath-Pileser king of Assyria" (וַיָּעַר…אֶת־רוּחַ פּוּל) → `จิตใจ` ("mind/disposition" of the pagan king). Correct — this is a human/national disposition, not the divine Spirit; the `พระ` honorific is rightly withheld. ✓
- **28:12 — בָּרוּחַ ("by the spirit").** See §4b below — the one Spirit-related call worth a confirm.

**LOCKED** ✓. 1 Chronicles validates the לָבַשׁ-class (cf. 2KI 2:16 validating the נָשָׂא edge-case). **Optional doc amendment:** add 1 Chr 12:18 as the corpus's documented anarthrous-בare-רוּחַ-but-contextually-divine לָבַשׁ anchor to `spirit_of_yhwh_empowerment_2026-05.md` §"Edge cases," alongside the נָשָׂא note 2 Kings opened.

---

## 4b. 1 Chr 28:12 בָּרוּחַ — **REVIEW (MT-base vs BSB-gloss)**

David's temple blueprint at 28:11–12 is described in MT as having come **בָּרוּחַ** — literally "by the spirit [that was with him]," widely read as a marker that the plan was divine revelation (parallel to Moses receiving the tabernacle pattern, Exod 25:9, 40 — which 28:19's note cross-references). The shipped Thai follows the **BSB English** interpretive rendering "all that David had **in mind**" → **`แบบแปลนนั้นบรรจุทุกสิ่งที่ดาวิดทรงดำริไว้`** ("everything David had devised/intended"). The verse `notes` field flags the divergence explicitly: *"ฉบับ BSB แปล 'ทุกสิ่งที่ดาวิดทรงดำริไว้' แต่ภาษาฮีบรูใช้คำว่า 'โดยพระวิญญาณที่อยู่กับเขา' (בָּרוּחַ)…"*

This is a genuine, well-known interpretive crux (רוּחַ here = "mind/intention" vs "[divine] Spirit"), and the choice is defensible — most modern translations, including BSB, take the "in mind" reading. But it sits at the seam of the corpus's stated **MT-anchored** OT base (`ot_canon_and_text_base_2026-05.md`) vs its **BSB-style** rendering philosophy: here the Thai prefers BSB's gloss over a more literal MT rendering, and if בָּרוּחַ is the divine Spirit this is a fifth Spirit datapoint the surface effaces.

**REVIEW.** Confirm the BSB "in mind" reading is the intended call (it is documented, so this is a confirm, not a gap), or consider a surface that preserves the בָּרוּחַ ambiguity (e.g., "…ตามที่ดาวิดได้รับโดยพระวิญญาณ"). **Severity: LOW** (1 verse, already noted).

---

## 5. חֶסֶד covenant-love — **LOCKED**

חֶסֶד renders within the `chesed_covenant_love_2026-05.md` family across its four occurrences:

| Ref | Context | 1CH Thai |
|---|---|---|
| **16:34** | the worship refrain כִּי לְעוֹלָם חַסְדּוֹ ("for his chesed endures forever," = Ps 106:1 / 136) | `ความรักมั่นคงของพระองค์ดำรงเป็นนิตย์` (KD flags it as the worship refrain) |
| **16:41** | the same refrain, sung at the Asaphite installation | `ความรักมั่นคง` |
| **17:13** | the Davidic covenant חַסְדִּי ("I will not take my chesed from him," = 2 Sam 7:15) | `ความรักมั่นคงของเรา` |
| **19:2** (×2) | human חֶסֶד (David ↔ Nahash/Hanun loyalty) | `ความรักมั่นคง` (KD notes the human-relationship use of the same locked term) |

The covenant, worship-refrain, and human-loyalty senses all ship the single locked surface `ความรักมั่นคง`, consistent with every prior book. The 16:34/41 refrain is the corpus's first instance of the high-frequency כִּי לְעוֹלָם חַסְדּוֹ liturgical formula — see §8 for the inner-OT-quotation forward-watch (it recurs in 2 Chr 5:13 / 7:3,6 / 20:21 + Ps 118 / 136).

**LOCKED** ✓.

---

## 6. Samuel↔Chronicles synoptic divergence — **REVIEW (documentation completeness)**

1 Chronicles is the first OT book to test `synoptic_parallel_passages_2026-05.md` at scale: 1 Chr 10–29 parallels 1 Sam 31 + 2 Sam 5–24. The doc's lock (parallel passages translated **independently** from each book's own MT, **not** harmonized) is correctly applied throughout — the shipped 1 Chronicles text faithfully follows MT-Chronicles even where it differs from MT-Samuel. The doc's §"Per-verse documentation" further asks for a **Layer-1 note** when a divergence is famous, apologetically prominent, or gives "a substantially different name, number, or agent."

**Well-documented divergences (the doc's standard is met):**

| Ref | Divergence | Documented as |
|---|---|---|
| **21:1** | שָׂטָן incited David ↔ 2 Sam 24:1 "YHWH incited" | `notes` (the agent-divergence; see §7) |
| **20:5** | Elhanan killed **Lahmi brother of Goliath** ↔ 2 Sam 21:19 "Goliath" | `key_decisions` (the doc names this exact crux as the considered-not-emended case) |
| **21:15** | **Ornan** (אָרְנָן) ↔ Araunah (2 Sam 24) | `notes` |
| **19:16** | **Shophach** ↔ Shobach (2 Sam 10:16) | `notes` |
| **11:11** | **Jashobeam** ↔ Josheb-basshebeth (2 Sam 23:8) | `notes` (+ general "this list parallels 2 Sam 23 with spelling variants") |
| **10:13–14** | Chronicler's unique theological verdict on Saul's death (no Samuel parallel) | `notes` |
| **19:18** | 7,000 charioteers ↔ 2 Sam 10:18 "700 chariots" | `notes` (explicitly: "ฉบับเอเรโมสแปลตามรูป MT ของพงศาวดาร") |

**Unflagged number divergences (the gap):** three number divergences the doc's own §"Per-verse documentation" criteria call for are not noted —

- **21:5** — census totals **1,100,000 + 470,000** vs 2 Sam 24:9's **800,000 + 500,000**. The synoptic doc **explicitly names "2 Sam 24:9 census totals"** as a confuse-readers case warranting a note; 21:5 carries none.
- **21:25** — David pays Ornan **600 shekels of gold** for the site, vs 2 Sam 24:24's **50 shekels of silver** (for the floor + oxen). The 21:25 note covers the threshing-floor→temple-site theology but not this well-known price/commodity divergence.
- **11:11** — Jashobeam killed **300** vs 2 Sam 23:8's **800** (the name divergence is noted; the number is not).

**REVIEW.** The translations are MT-faithful and correct — this is a Layer-1 documentation-completeness gap, not a surface error. Recommend adding `notes`/`key_decisions` divergence lines at 21:5 + 21:25 (and a number-clause at 11:11) per the synoptic doc's format. **Severity: LOW–MEDIUM** (no surface edit; the 21:5 census case is the clearest, since the doc names it by reference). Forward-protects the much denser 2 Chronicles synoptic field (2 Chr ≈ 1–2 Kings).

---

## 7. שָׂטָן at 1 Chr 21:1 — **LOCKED/STABLE (the corpus's marquee Samuel↔Chronicles crux, documented)**

The single most-discussed Chronicles divergence — וַיַּעֲמֹד שָׂטָן עַל־יִשְׂרָאֵל ("Then **Satan** stood up against Israel and incited David to take a census") vs 2 Sam 24:1's "the anger of **YHWH**…incited David" — ships **`แล้วซาตานก็ลุกขึ้นต่อสู้อิสราเอล และยุยงดาวิด`**, with a `notes` field that names the divergence and gives the standard reconciliation: *"พงศาวดารกล่าวว่า 'ซาตาน' (שָׂטָן ผู้ปรปักษ์) ยุยงดาวิด ขณะที่ 2 ซมอ. 24:1…พระพิโรธขององค์พระผู้เป็นเจ้ายุยง — สองมุมมองต่อเหตุการณ์เดียวกัน (พระเจ้าทรงอนุญาตให้ผู้ปรปักษ์ทดสอบ)."* This is precisely the handling `synoptic_parallel_passages_2026-05.md` §"Samuel↔Chronicles (MT-faithful)" prescribes (and the doc cites this very verse, line 47, as its worked Thai example). The rendering `ซาตาน` (with the gloss `ผู้ปรปักษ์` "adversary" in the note) is consistent with the corpus's treatment of שָׂטָן where the term functions near-titularly.

**LOCKED/STABLE** ✓. No action. (The dedicated `adversary_speech_register_2026-05.md` governs satanic *speech* register, not the noun rendering, and ch 21:1 has no Satan speech.)

---

## 8. The ch-16 psalm medley (inner-OT quotation) — **STABLE (verse-documented; Psalter forward-watch)**

1 Chr 16:8–36 is David's thanksgiving psalm at the ark's installation — a Chronicler composite of three Psalms. The translation handles it cleanly and documents the sources at 16:8: *"บทเพลงนี้ (ข้อ 8-36)…ข้อ 8-22 = สดด. 105:1-15; ข้อ 23-33 = สดด. 96; ข้อ 34-36 = สดด. 106:1, 47-48."* Spot-checks:

- **16:25–26** — "great is YHWH…feared above all gods…all the gods of the nations are idols" → `เหนือพระทั้งปวง` / `พระทั้งหลายของชนชาติต่างๆ เป็นเพียงรูปเคารพ` — the polytheistic-register call (gods of the nations = `พระ`, never `พระเจ้า`) is correct per `ot_polytheistic_register_2026-05.md`. ✓
- **16:31** — "YHWH reigns" → `องค์พระผู้เป็นเจ้าทรงครอบครอง` ✓
- **16:34** — the chesed refrain (§5) ✓
- **16:35** — "Save us, O God of our salvation" → `ข้าแต่พระเจ้าแห่งความรอด…` (Elohim vocative in prayer) ✓
- **16:36** — doxology + אָמֵן → `อาเมน` ✓

**STABLE.** The inner-OT quotation is documented at verse level — no action now. **Forward-watch (not a gap):** when the Psalter ships, 1 Chr 16:8–36 should be cross-checked against the Thai of Ps 105/96/106 (and the 16:34 כִּי לְעוֹלָם חַסְדּוֹ refrain against Ps 106/118/136 + its recurrences in 2 Chr 5:13 / 7:3 / 20:21). This is the corpus's first large inner-OT quotation block and the natural anchor for that alignment pass; a Layer-2 cross-reference at 16:8 ↔ Ps 105:1 is optional polish. Governed by `ot_nt_cross_quotation_thread_2026-05.md`.

---

## 9. ch 17 Davidic covenant (= 2 Sam 7) — **STABLE/LOCKED (Chronicler's Tetragrammaton-for-Adonai faithfully tracked)**

David's covenant prayer (17:16–27) is the densest divine-address passage in 1 Chronicles and the synoptic twin of 2 Sam 7:18–29. The two MT texts differ systematically in divine names: where 2 Sam 7 used **אֲדֹנָי יְהוִה** (×7), 1 Chr 17 uses plain **יְהוָה** / **יְהוָה אֱלֹהִים** / **אֱלֹהִים**. The translation tracks the Chronicles MT faithfully:

- 17:16 יְהוָה אֱלֹהִים → `ข้าแต่องค์พระผู้เป็นเจ้าพระเจ้า` (sentence-initial vocative, David "sat before YHWH")
- 17:19, 17:20, 17:26 — sentence-initial יְהוָה vocative → `ข้าแต่องค์พระผู้เป็นเจ้า`
- 17:27 — mid-sentence vocative apposition כִּי־אַתָּה יְהוָה → "เพราะพระองค์ **ข้าแต่องค์พระผู้เป็นเจ้า** ได้ทรงอวยพร"
- 17:13 — the covenant promise "I will be his father…I will not take my chesed from him" (= 2 Sam 7:14–15, quoted at Heb 1:5) → `เราจะเป็นบิดาของเขา…เราจะไม่ถอนความรักมั่นคงของเรา` ✓

The plain-YHWH vocative with `ข้าแต่` is the standard direct-address form (matching the 2KI Hezekiah/Elisha prayers); because no אֲדֹנָי יְהוִה compound is present, the 1KI 8:53 / 2 Sam 7 appositional-bare sub-rule does not apply and **the 1KI §8 DECIDE does not recur** (cf. §2). The Chronicler's substitution is correctly preserved rather than harmonized to the Samuel form — the §6 synoptic lock in action on the divine-name axis.

**STABLE/LOCKED** ✓. (Optional Layer-2: 17:13 ↔ Heb 1:5 cross-reference — see §10.)

---

## 10. NT / doxological cross-corpus echoes — **STABLE (Layer-2 opportunities; verse-noted where load-bearing)**

1 Chronicles seeds several NT-cited threads, the heaviest documented inline:

| 1CH ref | Echo | Handling |
|---|---|---|
| **29:11–13** | **Matt 6:13** TR/liturgical doxology ("for thine is the kingdom, the power, and the glory") | 29:11 `notes` documents the echo explicitly ✓ |
| **29:15** | **1 Pet 2:11** (גֵּרִים וְתוֹשָׁבִים "sojourners and strangers") → `คนต่างด้าวและคนแปลกหน้า` | per `parepidemos_paroikos_sojourner_2026-05.md`; surface alignment worth a forward-check when 1 Peter's lock is cross-walked |
| **17:13** | **Heb 1:5** ("I will be his father, and he shall be my son") | Layer-2 cross-ref candidate |
| **1:1–4 / chs 1–9** | **Matt 1 / Luke 3** genealogies (Adam→…) | proper-name alignment (see §15) |

**STABLE.** The 29:11 doxology — the most apologetically prominent — is already verse-noted. The others are corpus-completeness polish, not gaps. **Severity: LOW.** Governed by `ot_nt_cross_quotation_thread_2026-05.md`.

---

## 11. Large numbers + weight/measure units — **STABLE**

1 Chronicles carries the corpus's largest concentration of large numbers + precious-metal weights (the temple-fund chapters 22 + 29). Units render uniformly within the established corpus forms:

- **כִּכָּר (talent) → `ตะลันต์`** (22:14 `หนึ่งแสนตะลันต์` gold / `หนึ่งล้านตะลันต์` silver; 29:4 `สามพันตะลันต์`; 29:7 `ห้าพันตะลันต์` etc.) — matches the NT τάλαντον → `ตะลันต์`.
- **דַּרְכְּמוֹן (daric) → `ดาริค`** (29:7 `หนึ่งหมื่นดาริค`).
- **שֶׁקֶל (shekel) → `เชเขล`** (21:25 `หกร้อยเชเขล`).

Large cardinals are spelled out in Thai (e.g., 21:5 `หนึ่งล้านหนึ่งแสนคน`). The Chronicles-vs-Samuel number divergences themselves are the §6 documentation-completeness item; the **unit renderings** are uniform and consistent.

**STABLE** ✓.

---

## 12. Deuteronomistic regnal-cycle formulas — **LOCKED (death/succession register holds; evaluation cycle is N/A in 1CH)**

`dtr_history_cycle_formulas_2026-05.md` ("Gates 2 Kings + Chronicles") is only *partially* exercised by 1 Chronicles, because 1 Chronicles covers **David's reign only** — there is no multi-king regnal sequence here (the accession/evaluation/"walked in the way"/source-citation formulas belong to **2 Chronicles**, the post-Solomon monarchy). The one formula that applies:

- **Death / succession (David, 29:28).** The Chronicler uses וַיָּמָת בְּשֵׂיבָה טוֹבָה ("died in a good old age") rather than the Deuteronomistic וַיִּשְׁכַּב עִם אֲבֹתָיו ("slept with his fathers") — faithfully rendered `สิ้นพระชนม์เมื่อทรงพระชราภาพ` (not `ล่วงหลับ`; a genuine MT difference, not a drift). David receives the **full Davidic-line royal register** — `สิ้นพระชนม์` / `ทรงพระชราภาพ` / `ซาโลมอนพระราชโอรสครองราชย์แทนพระองค์` — consistent with the doc's dynastic-legitimacy register split (Davidic kings keep `ทรง` + `โอรส` + `แทนพระองค์`). ✓ The same register holds for Saul's death-and-transfer verdict (10:14, `ทรงประหาร…ทรงมอบราชอาณาจักร`).

**LOCKED** ✓ (the death/succession register holds; the evaluation-cycle formulas are 2 Chronicles' stress-test, where the `["1KI ","2KI "]`-scoped phrase-locks should be extended — see §18).

---

## 13. "until this day" leitwort — **REVIEW (cross-book; 1CH joins the majority, 1SA still the outlier)**

1 Chronicles renders עַד הַיּוֹם הַזֶּה uniformly **`จนถึงทุกวันนี้`** (with the `ทุก-` intensifier) — 4:41 + 17:5 (the two occurrences). This matches the **JDG + 1KI + 2KI majority**.

**Cross-book corpus picture now (five DtrH/Chronicler books):**
| Book | Surface | Count |
|---|---|---|
| Judges | `จนถึงทุกวันนี้` | 6× (+1 drift) |
| 1 Samuel | `จนถึงวันนี้` (bare) | 8× uniform |
| 1 Kings | `จนถึงทุกวันนี้` | 5× |
| 2 Kings | `จนถึงทุกวันนี้` | 10× |
| **1 Chronicles** | **`จนถึงทุกวันนี้`** | **2×** |

**Four of five books now agree on `จนถึงทุกวันนี้`; 1 Samuel is the lone outlier.** This further sharpens the standing 1KI §14 / 2KI §11 cross-book REVIEW.

**REVIEW.** Internal 1CH uniformity ✓; the cross-book decision (lock `จนถึงทุกวันนี้`; normalize 1SA's 8 occurrences) should land in `leitwort_handling_policy_2026-05.md`. **Severity: LOW.**

---

## 14. Pagan deities — **LOCKED (1 Chronicles is essentially deity-free; the 1SA §12 Dagon problem does NOT recur)**

Unlike Kings/Judges, 1 Chronicles has **almost no pagan-deity content** — nearly every `บาอัล` surface is a **proper or place name** containing the Baal element, correctly *not* given deity register: Baal-hanan the Edomite king (1:49–50), Baal son of Reaiah (5:5), Merib-baal (8:34, = Mephibosheth), the towns Baal (4:33) / Baal-hermon (5:23) / Baal-perazim (14:11). The two genuine pagan-religion references:

- **10:10 — Dagon.** Saul's head fastened "in the temple of Dagon"; his armor "in the house of **their gods**" (בֵּית אֱלֹהֵיהֶם) → **`วิหารของพระดาโกน`** / **`วิหารของพระของพวกเขา`**. Both use **`พระ`** (the OT-polytheistic register), **never `พระเจ้า`**. This is the same Dagon whose 1 Sam 5:7 occurrence produced the 1SA §12 `พระเจ้า`-for-pagan-deity problem — **here it is handled correctly**, a quiet cross-book win.
- **16:26 (ch-16 psalm)** — "all the gods of the nations are idols" → `พระทั้งหลาย…เป็นเพียงรูปเคารพ` ✓ (§8).

**LOCKED** ✓ per `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md`. No `พระเจ้า`-for-pagan violation in 1 Chronicles.

---

## 15. Proper-name transliteration (genealogies chs 1–9) — **STABLE/LOCKED (the book's signature load; corpus-consistent)**

Chapters 1–9 are the corpus's largest proper-name-only stretch (Adam → the post-exilic returnees) — a massive transliteration-consistency stress-test for `proper_names_and_transliteration_2026-05.md` + `shared_names_normalization_2026-05.md`. The mechanical gate is decisive here: **`check_key_term_consistency.py` is clean (0 rule violations, 0 undocumented multi-renderings) across the 632-chapter corpus**, which includes the 1 Chronicles genealogies. Spot-checks of high-frequency corpus names confirm the established forms hold: อาดัม (Adam), โนอาห์ (Noah), อับราฮัม (Abraham), อิสอัค (Isaac), ยาโคบ (Jacob), เอซาว (Esau), เอโดม (Edom), ยูดาห์/เลวี/เบนยามิน (tribal), ซาโลมอน (Solomon), ซามูเอล (Samuel), เยรูซาเล็ม (Jerusalem). Synoptic spelling variants from Samuel are footnoted where they matter (Ornan=Araunah 21:15, Shophach=Shobach 19:16, Jashobeam=Josheb-basshebeth 11:11).

**STABLE/LOCKED** ✓. The genealogies are the strongest single demonstration that the proper-name machinery scales; no drift surfaced.

---

## 16. MT/LXX textual-variant disposition — **LOCKED (§2.3 floor → non-gap; carried 1SA/1KI DECIDE resolved)**

The `output/textual_variants/1chronicles_NN.json` files contain **only** the per-chapter YHWH first-occurrence footnote (23 files; the 6 YHWH-absent chapters have none). **Zero** inclusion-variant / MT-vs-LXX-divergence entries — the same surface as 1SA §17, 1KI §17, 2KI §15. But the disposition is now settled doctrine, not an open DECIDE:

- `mt_vs_lxx_textual_variant_handling_2026-05.md` **§2.3 disclosure-threshold floor** (added 2026-05-25, 2 Kings EOB) establishes that a book with zero non-YHWH `textual_variant` entries is **COMPLIANT** when all its MT/LXX divergences fall below the macro-structural / canonically-visible / materially-reader-affecting floor.
- **1 Chronicles sits below that floor.** Chronicles' LXX (Paraleipomena) is textually close to MT — **no macro-structural divergence** (no 3-Reigns-style reordering, no Miscellanies, no alternate-narrative blocks), nothing NT-cited at the textual-variant level, no materially-reader-affecting plus/minus cluster. It is a *milder* case than even 2 Kings (the §2.3 anchor).
- **Chronicles' real textual layer is the Samuel↔Chronicles synoptic divergence — a different doc.** That divergence is handled at **Layer-1 verse notes** under `synoptic_parallel_passages_2026-05.md` (§6/§7), not via Layer-2 `textual_variant` footers. The two doc systems partition cleanly: MT-vs-LXX → §2.3 floor → non-gap; Samuel↔Chronicles → synoptic doc → verse notes (with the §6 completeness gap the only open item).

**LOCKED** ✓ — **non-gap**, resolving the question that was a DECIDE in 1SA + 1KI. Recommend adding a 1 Chronicles row to the `mt_vs_lxx_textual_variant_handling_2026-05.md` §3 table ("Paraleipomena ≈ MT, no macro-structural divergence → §2.3 floor; non-gap") to record the disposition explicitly, mirroring the 2 Kings row.

---

## 17. Inherited corpus locks — all compliant except where flagged

| Doc | 1CH evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1 (YHWH 176 surfaces, 0 ยาห์เวห์, 23/23 footnoted); §2 (Elohim→พระเจ้า; **no אֲדֹנָי in 1CH at all**). 1KI §8 compound DECIDE does not recur. | **LOCKED** |
| `malak_yhwh_2026-05.md` | §3 — divine מַלְאַךְ ×7 in ch 21 ship `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`; **lock HOLDS but unenforced (Kings-scoped) + 1CH unlisted on §3 checklist**. | **LOCKED-holds / REVIEW-§3** |
| `spirit_of_yhwh_empowerment_2026-05.md` | §4 — 12:18 לָבַשׁ-class ships `พระวิญญาณ` (first downstream לָבַשׁ ship); 5:26 pagan-king רוּחַ→จิตใจ correct. **EXCEPTION:** 28:12 בָּרוּחַ (§4b). | **LOCKED-with-§4b-REVIEW** |
| `chesed_covenant_love_2026-05.md` | §5 — ความรักมั่นคง ×4 (16:34/41 refrain, 17:13 covenant, 19:2 human). | **LOCKED** |
| `synoptic_parallel_passages_2026-05.md` | §6/§7 — MT-faithful, independent translation; agent/name divergences documented; **number-divergence documentation incomplete (21:5, 21:25, 11:11)**. | **LOCKED-with-§6-REVIEW** |
| `nicham_divine_relenting_2026-05.md` | 21:15 וַיִּנָּחֶם → `ทรงเปลี่ยนพระทัย` (KD cites the lock). | **LOCKED** |
| `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md` | §14 — 10:10 Dagon `พระ` (not `พระเจ้า`); 16:26 gods-of-nations `พระ`/รูปเคารพ. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` + `shared_names_normalization_2026-05.md` | §15 — genealogies chs 1–9 key_term-clean; synoptic spelling variants footnoted. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` + `ot_register_policy_2026-05.md` | royal `ทรง` for David/Solomon throughout (ทรงสร้าง, เสด็จ, ทรงพระชราภาพ); assembly + prayer registers clean. | **LOCKED** |
| `dtr_history_cycle_formulas_2026-05.md` | §12 — David death/succession royal register holds (29:28); evaluation cycle N/A (2 Chronicles). | **LOCKED (partial-N/A)** |
| `hebrew_oath_formulas_2026-05.md` | חַי־יְהוָה ("as YHWH lives") does not occur in 1 Chronicles (Hebrew-grep confirmed). | **LOCKED (N/A)** |
| `leitwort_handling_policy_2026-05.md` | §13 — internal uniform `จนถึงทุกวันนี้`; cross-book 1SA-outlier decision pending. | **LOCKED-with-§13-REVIEW** |
| `ot_nt_cross_quotation_thread_2026-05.md` | §8 (ch-16 psalm medley, sources noted), §10 (29:11 Matt 6:13 doxology noted). | **LOCKED** |
| `parepidemos_paroikos_sojourner_2026-05.md` | §10 — 29:15 גֵּרִים וְתוֹשָׁבִים → คนต่างด้าวและคนแปลกหน้า. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md` | §16 — §2.3 floor → non-gap (Paraleipomena ≈ MT). | **LOCKED (non-gap)** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "hand of YHWH" / "by his hand" (28:19 พระหัตถ์); divine relenting (21:15). Compliant. | **LOCKED** |
| `ot_warfare_ethics_2026-05.md` | David's wars (chs 18–20) narrated without ḥerem-cluster vocabulary; no lock surface triggered. | **LOCKED (N/A)** |

---

## 18. Mechanical (§1) — all green (with two standing infra notes)

- 29/29 chapters: `output/check_reports/1chronicles_NN_review.md` all six checks "✅ clean" / "Ready to ship" ✓
- 29/29 chapters: `output/back_translations/1chronicles_NN.json` ✓
- 29/29 chapters: `output/translations/1chronicles_NN.json` (943 verses) ✓
- 23/23 YHWH-containing chapters: `output/textual_variants/1chronicles_NN.json` (YHWH footnote; the 6 YHWH-absent chapters correctly have none — §1, §16)
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** (632-chapter corpus)
- `check_phrase_consistency.py`: **0 violations across 12 audited locks** (19,190 verses). **Note:** the `malak` + DTr evaluation/high-places locks are scoped `["1KI ", "2KI "]` — **1 Chronicles is out of scope**, so the clean result does not reflect a passed malak check for 1CH (§3 verified manually). Recommend widening scope to 1 Chronicles (and 2 Chronicles, before it ships).
- `audit_inclusion_variants.py --book 1chronicles --strict`: **0 candidates, exit 0** (the heuristic is NT-SBLGNT-tuned; it does not catch Samuel↔Chronicles synoptic divergence — that is the §6 verse-note layer, not an inclusion variant).
- `export_to_usfm.py --book 1CH`: **N/A** — the script's `BOOKS` table is NT-only; OT USFM export remains a carried-over separate concern (as noted in every prior OT audit).
- **Book-code registration:** `1CH` was missing from the §3/§4 tooling slug tables (`build_external_review_packet.py` `BOOKS`, `audit_items_to_yaml.py` `BOOK_SLUGS`); **registered as part of this audit** per the EOB book-code-registration gotcha.
- `git status output/`: **clean except `output/check_reports/divine_names.md`** — a transient single-chapter scratch report whose only diff clears a stale 2SA 1:10 warning; report-only, not a 1 Chronicles surface; identical in kind to the note carried in the 1SA / 1KI / 2KI audits.
- YHWH `องค์พระผู้เป็นเจ้า` surfaces: **176**. `ยาห์เวห์` residues: **zero**.

**Severity: GREEN.**

---

## 19. Flagged for Ben's attention

### A. mal'akh-YHWH lock unenforced + unlisted for 1 Chronicles — **REVIEW** (§3)
The lock HELD in ch 21 (7 divine occurrences ship `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`) — but only by convention: the `check_phrase_consistency.py` `malak` lock is `["1KI ","2KI "]`-scoped and 1 Chr 21 is not on the `malak_yhwh_2026-05.md` §3 forward-cover checklist. Recommend widening the lock scope to `"1 Chronicles "` and ticking 1 Chr 21. Note the symmetry: 1 Chr 21 ships clean while its 2 Sam 24 twin still awaits the deferred cross-book retrofit. **LOW; not a tag blocker.**

### B. Samuel↔Chronicles number-divergence documentation completeness — **REVIEW** (§6)
Agent/name divergences are well-documented; three number divergences the synoptic doc's criteria call for are unflagged: **21:5** census totals (the doc names "2 Sam 24:9 census totals" by reference), **21:25** price (600 gold vs 50 silver), **11:11** (300 vs 800). Add Layer-1 `notes`/`key_decisions` divergence lines per the doc's format. **LOW–MEDIUM; no surface edit.**

### C. mal'akh human-messenger surface — **REVIEW** (§3b)
1 Chronicles adds `ทูต` (14:1, 19:2) + `ส่งคน` (19:16) — a fifth cross-book surface-set. Cross-book normalize with the standing 1KI §3b / 2KI §3b flag (recommended canonical: `ผู้ส่งสาร`). **LOW.**

### D. 1 Chr 28:12 בָּרוּחַ "by the spirit" vs BSB "in mind" — **REVIEW** (§4b)
The Thai follows BSB's "all that David had in mind" over the MT's literal בָּרוּחַ; the divergence is verse-noted. Confirm the BSB-gloss reading, or adopt a surface that preserves the בָּרוּחַ ("by the Spirit") ambiguity. **LOW; 1 verse.**

### E. "until this day" cross-book normalization — **REVIEW** (§13)
1 Chronicles uniform `จนถึงทุกวันนี้` (4:41, 17:5) joins JDG + 1KI + 2KI; **1 Samuel is now the lone corpus outlier** (`จนถึงวันนี้`). Lock `จนถึงทุกวันนี้` in `leitwort_handling_policy_2026-05.md`; normalize 1SA's 8 occurrences. **LOW.**

### F. Existing docs to amend (optional, no tag block)
- **`malak_yhwh_2026-05.md`** — tick 1 Chr 21 onto §3; widen the `check_phrase_consistency.py` `malak` scope (per §A).
- **`spirit_of_yhwh_empowerment_2026-05.md`** — add 1 Chr 12:18 as the documented anarthrous-בare-רוּחַ לָבַשׁ-class anchor (§4).
- **`synoptic_parallel_passages_2026-05.md`** — once §6 notes land, record 1 Chronicles as the doc's first large-scale OT downstream test.
- **`mt_vs_lxx_textual_variant_handling_2026-05.md`** — add the 1 Chronicles §3-table row (Paraleipomena ≈ MT → §2.3 floor; non-gap) per §16.
- **`leitwort_handling_policy_2026-05.md`** — lock `จนถึงทุกวันนี้` as canonical (§E).

### G. External AI review (§3 of checklist) — pending
Recommended 5-item packet (see `external_review_items_1CH.md`):
1. **mal'akh-YHWH lock-scope** (§3) — held by convention, recommend machine-locking
2. **Samuel↔Chronicles divergence-documentation completeness** (§6) — the Chronicles-specific Layer-1 question
3. **mal'akh human-messenger surface** (§3b) — cross-book normalization
4. **1 Chr 28:12 בָּרוּחַ translation-base** (§4b) — MT-anchor vs BSB-gloss
5. **"until this day" cross-book** (§13) — 1SA outlier

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG/1SA/1KI/2KI pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 11 items (§1 YHWH, §2 Elohim/Adonai, §3 mal'akh [holds], §4 Spirit, §5 chesed, §7 Satan-21:1, §9 Davidic covenant, §12 DTr death-register, §14 pagan deities, §15 proper names, §16 MT/LXX [non-gap]; + inherited locks via §17)
- **STABLE:** 4 items (§8 ch-16 psalm medley, §10 NT/doxology echoes, §11 numbers/units, §13b — all verse-documented; no doc required)
- **REVIEW:** 5 items (§3 mal'akh lock-scope, §6 synoptic-divergence documentation, §3b human-messenger surface, §4b 28:12 בָּרוּחַ, §13 "until this day")
- **DECIDE:** 0 items

**No DECIDE items block the `book-1chronicles-v1` tag.** The MT/LXX inclusion-variant question that was a DECIDE in 1SA + 1KI is resolved as a **non-gap** under the §2.3 floor (§16).

**No new translator_decisions docs required.** Five optional existing-doc amendments (§19.F) + one optional Layer-2 cross-reference pass (§8/§10).

---

## Recommendation

**1 Chronicles ships in the cleanest corpus-hygiene shape of any OT book audited to date.** It is the **first book of the Chronicler's History** and the corpus's first large-scale test of three new stress surfaces — nine genealogy chapters, the Samuel↔Chronicles synoptic relationship, and a major divine-מַלְאַךְ narrative. The audit finds:

- **The mal'akh-YHWH lock HOLDS in the ch-21 threshing-floor narrative** (7 divine occurrences ship `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`) — the clean opposite of the 1 Kings 19:7 drift, and remarkably achieved **outside** the lock's machine-enforcement scope and **off** its forward-cover checklist. The only action is to lock in the win (widen scope; tick the checklist).
- **No DECIDE items.** The MT/LXX inclusion-variant gap resolves as a non-gap (§2.3 floor; Paraleipomena ≈ MT), and the Adonai-compound DECIDE thread (1KI §8) does not recur (the Chronicler uses plain יְהוָה).
- **The genealogies scale cleanly** — `check_key_term_consistency.py` clean across the nine name-only chapters confirms the proper-name machinery holds.
- **The Samuel↔Chronicles synoptic lock works** — divergences translated independently, MT-faithful, with the famous cruxes (21:1 Satan, 20:5 Elhanan/Lahmi) documented; the one open item is documentation *completeness* on three unflagged number divergences (§6).
- **Pagan-deity handling is a quiet cross-book win** — the same Dagon that triggered the 1SA §12 `พระเจ้า` problem ships correctly with `พระ` here.

**Tag `book-1chronicles-v1` after:**
1. Ben's confirmation on the **§A–§E REVIEW items** (all LOW / LOW–MEDIUM; none surface-blocking)
2. External AI sanity-check (§G)
3. Optionally, the §19.F existing-doc amendments (none gate the tag)

**The single highest-value forward-protection step** is widening the `malak` (and DTr-formula) phrase-locks beyond `["1KI ","2KI "]` before **2 Chronicles** — the book that re-runs the full Judahite regnal cycle and carries the densest synoptic field — begins shipping.
