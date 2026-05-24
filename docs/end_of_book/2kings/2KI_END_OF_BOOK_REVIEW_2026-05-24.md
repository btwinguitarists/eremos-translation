# 2 Kings — End-of-Book Review

**Date:** 2026-05-24
**Scope:** All 25 chapters of 2 Kings (719 verses); `glossary.json`; `docs/translator_decisions/` corpus (~96 docs through the 1 Kings end-of-book audit, including the `dtr_history_cycle_formulas_2026-05.md` doc that 1 Kings created).
**Trigger:** 2KI 25 shipped (commit `6541d2f`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Eleventh OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, 1 Samuel, 2 Samuel, 1 Kings) and the **fifth Former-Prophets / Deuteronomistic-History book.** 2 Kings is the **first OT-corpus book to ship downstream of two forward-protective locks that 1 Kings created and that explicitly named 2 Kings as their next stress-test**: `dtr_history_cycle_formulas_2026-05.md` ("**2 Kings is composed almost entirely of them**") and the `malak_yhwh_2026-05.md` §3 forward-cover checklist ("2 Kings 1 — Elijah + Ahaziah's messengers — next: enforce at 1:3,15"). It is therefore the cleanest test yet of whether end-of-book locking actually prevents downstream drift.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **18 cross-cutting items reviewed.** Mechanical gates (§1) pass: 25/25 chapters have green per-chapter reports + back-translations + translations (719 verses); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the 603-chapter corpus); `check_phrase_consistency.py` clean across all 12 audited locks (18,247 verses), **including the four Kings-scoped OT locks** (`malak`, evaluation-evil, evaluation-right, high-places) that are now machine-enforced for `2KI `. The single dirty file in `git status output/` is `output/check_reports/divine_names.md` — a transient single-chapter scratch report (`Chapters checked: 1`) whose only diff clears a stale 2SA 1:10 warning; report-only, not a 2 Kings translation surface, identical in kind to the note carried in the 1SA / 1KI audits.
- **2 Kings is the first downstream book to ship BOTH forward-protective Kings locks CLEANLY — the locks did their job.**
  - **`malak_yhwh_2026-05.md` HOLDS in 2 Kings.** All three divine מַלְאַךְ יְהוָה occurrences — **1:3** + **1:15** (the angel of YHWH to Elijah re: Ahaziah's messengers) and **19:35** (the angel of YHWH striking 185,000 Assyrians) — ship the locked **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`**. These are the *exact* forward-cover targets the lock named. This is the **opposite** of 1 Kings' 19:7 drift (1KI audit §3 DECIDE), and the malak lock is now machine-enforced for `2KI ` in `check_phrase_consistency.py`. See §3.
  - **`dtr_history_cycle_formulas_2026-05.md` HOLDS across all five formulas.** 2 Kings is wall-to-wall regnal cycle (~40 regnal notices, every king of Israel + Judah to the exile), and ships the accession, evaluation, "walked in the way of Jeroboam," high-places, source-citation, and death/burial/succession formulas uniformly per the doc the 1 Kings audit created. Critically, the **death-formula dynastic-register split is exceptionless** — Judahite/Davidic kings get `ทรงล่วงหลับ … ราชโอรส … แทนพระองค์`, Northern kings get plain `ล่วงหลับ … บุตรของเขา … แทน`, and **Manasseh (the worst Judahite king) keeps `ทรง`**, confirming the split is dynastic-legitimacy, not moral. See §5–6.
- **1 item flagged DECIDE** (Ben choice needed before tagging `book-2kings-v1`):
  - **§15 MT/LXX inclusion-variant gap** — carried forward from 1SA §17 + 1KI §17. The 25 `output/textual_variants/2kings_NN.json` files contain **only** the YHWH first-occurrence footnote (25×); **zero** inclusion-variant / MT-vs-LXX-divergence entries. This is the **third consecutive DtrH book** to ship the identical gap. (2 Kings — the LXX kaige-section — is a *less* macro-structurally divergent case than 1 Kings' 3 Reigns: no Miscellanies, no whole-narrative reordering, mostly verse-level pluses/minuses + the chronological-synchronism cruxes. The recommendation pivots from per-book re-flagging to a **corpus-level policy resolution** — see §15.)
- **5 items flagged REVIEW** (worth Ben's confirmation):
  - **§8b Baal-zebub `พระ`-register** — `บาอัลเซบูบ` (1:2/1:3/1:6/1:16) is the **lone foreign deity in 2 Kings shipped WITHOUT the `พระ` prefix**; every other foreign proper-noun god takes `พระ` (`พระบาอัล`, `พระสุคโคทเบโนท`, `พระเนอร์กัล`, `พระนิสรอค`, `พระโมเลค`, `พระอัชเทเรท`, `พระเคโมช`). The bare form has a verse-level rationale (the `אֱלֹהֵי` → `เทพเจ้า`-not-`พระเจ้า` polemic) but the `พระ`-drop on the proper noun is under-specified.
  - **§9 Adversary-speech register — human-imperial-blasphemer class (Rabshakeh)** — 2 Kings 18–19 is the corpus's first sustained *human* imperial blasphemer taunting YHWH, a class `adversary_speech_register_2026-05.md` (written for NT demons/devil) does not explicitly cover. The handling is principled but undocumented for this configuration.
  - **§3b mal'akh human-messenger surface** — 2 Kings adds `ผู้ส่งสาร` (1:2/1:3 — the form 1KI §3b recommended as canonical) **plus** `ทูต` (17:4) **plus** `คณะทูต` (20:13) — a within-book + cross-book human-messenger surface variance.
  - **§11 "until this day" leitwort** — 2 Kings uniform `จนถึงทุกวันนี้` ×10; now **JDG + 1KI + 2KI all agree**, making **1 Samuel the lone corpus outlier** (`จนถึงวันนี้`). Sharpens the 1KI §14 normalization case.
  - **§8c cross-book pagan-deity micro-variance** — Molech ships `พระโมเลค` (2KI 23:10) vs 1KI's `โมเลคเทพอันน่าสะอิดสะเอียน` (1KI 11:7); a `พระ`-vs-`เทพ`-descriptor surface drift to fold into the pagan-deity doc when §8b lands.
- **2 items recommend new / amended corpus docs** (STABLE-but-undocumented):
  - **§10 Deuteronomistic Name-theology** — `นามของเรา` uniform (21:4, 21:7, 23:27) continuing the 1 Kings 8 thread; the `name_theology_deuteronomistic_2026-05.md` doc / Layer-2 that 1KI §H recommended is still unwritten. MEDIUM.
  - **§4 spirit-of-yhwh נָשָׂא edge-case** — 2 Kgs **2:16** ships `พระวิญญาณขององค์พระผู้เป็นเจ้า` for the נָשָׂא-class "the Spirit of YHWH carried him," **validating the 1KI §I recommended amendment** to `spirit_of_yhwh_empowerment_2026-05.md` (add נָשָׂא as an out-of-empowerment-split verb that keeps the `พระ` honorific). LOW.
- **External AI review (§3) pending.** Suggested 5-item packet (Baal-zebub register §8b; adversary-speech human-blasphemer extension §9; MT/LXX gap as corpus-policy §15; "until this day" cross-book §11; mal'akh human-messenger surface §3b).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה compliance — **LOCKED**

YHWH renders as `องค์พระผู้เป็นเจ้า` throughout. **228 verses** carry the `องค์พระผู้เป็นเจ้า` surface across the 25 chapters (≈ the MT YHWH-verse count for 2 Kings; surface-vs-lemma variance from verses with multiple occurrences + compound collapses).

**ยาห์เวห์ residues in verse text: zero.** No `ยาห์เวห์` surface in any 2 Kings `thai` field. (Place-name memorial compounds — the only sanctioned `ยาห์เวห์` survival per `divine_names_table_2026-05.md` — do not occur in 2 Kings.)

**Per-chapter first-occurrence YHWH footnote.** 25/25 chapters carry the locked Tier-2 explanation in `output/textual_variants/2kings_NN.json` (`type: tetragrammaton_convention_first_occurrence`).

**LOCKED** ✓ per `divine_names_table_2026-05.md`.

---

## 2. Elohim + Adonai divine names — **LOCKED (1KI §8 issue does NOT recur)**

- **Elohim → พระเจ้า** uniform across 2 Kings ✓. No drift.
- **Standalone divine אֲדֹנָי (third-person, narrator).** 2 Kgs **7:6** — וַאדֹנָי הִשְׁמִיעַ אֶת־מַחֲנֵה אֲרָם ("the Lord made the Aramean army hear…") → **`องค์เจ้านายทรงทำให้กองทัพอารัมได้ยิน`**. Correctly uses the standalone-Adonai third-person form `องค์เจ้านาย`, distinct from YHWH's `องค์พระผู้เป็นเจ้า` — matches the 2026-05-18 4-way distinction (the same call as 1KI 3:10). ✓
- **Human "my lord the king" (אֲדֹנִי הַמֶּלֶךְ).** 6:12, 6:26, 8:5 → `ข้าแต่กษัตริย์เจ้านายของข้าพระองค์` — human-royal `เจ้านาย` register, correct.
- **`ข้าแต่` vocative for direct YHWH-address in prayer.** Elisha (6:17, 6:20) + Hezekiah (19:15, 19:16, 19:17, 19:19, 20:3) all address the plain Tetragrammaton יהוה (incl. 20:3's אָנָּא יהוה interjection) → `ข้าแต่องค์พระผู้เป็นเจ้า`. Standard YHWH-vocative, compliant.
- **No אֲדֹנָי יְהוִה compound occurs in 2 Kings** (Hebrew-grep confirmed). The 1KI §8 sentence-final-vocative DECIDE (1 Kgs 8:53) therefore **does not recur** here — 2 Kings adds no new datapoint to the Adonai-compound sub-rule.

**LOCKED** ✓.

---

## 3. mal'akh-YHWH — **LOCKED (the lock HOLDS; first clean downstream ship of a previously-drifted lock)**

`malak_yhwh_2026-05.md` (locked 2026-05-13, tri-AI review) requires every divine מַלְאָךְ → **`ทูตสวรรค์`**, with the genitive carried by `ของ` + the divine-name form (מַלְאַךְ יְהוָה → **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`**). Its §3 implementation checklist explicitly named **"2 Kings 1 (Elijah + Ahaziah's messengers — next: enforce at 1:3,15)"** as the forward-cover target. 2 Kings has three divine-mal'akh occurrences — **all three ship the locked form:**

| Ref | Hebrew | 2KI Thai (shipped) | Status |
|---|---|---|---|
| **1:3** | מַלְאַךְ יְהוָה (the angel of YHWH to Elijah) | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✓ |
| **1:15** | מַלְאַךְ יְהוָה (the angel of YHWH, again) | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✓ |
| **19:35** | מַלְאַךְ יְהוָה (strikes the Assyrian camp) | **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`** | ✓ |

**This is the headline finding.** 1 Kings drifted at 19:7 (shipped `ทูต`, missing `สวรรค์` — a 1KI DECIDE) *because the lock had no machine enforcement*. Between the 1 Kings audit and the 2 Kings run, the `malak` lock was added to `check_phrase_consistency.py` (`hebrew_patterns` `מלאך\s*יהוה` → expected `ทูตสวรรค์`, `"books": ["1KI ", "2KI "]`). 2 Kings ships all three occurrences clean, and the check is green. **The end-of-book lock-then-enforce loop demonstrably prevented the drift it was created to catch.** Forward-protects Zech 1–6 + Malachi.

**LOCKED** ✓. (Recommend ticking "2 Kings 1" on the `malak_yhwh_2026-05.md` §3 forward-cover checklist; 19:35 was not separately listed but also complies.)

---

## 3b. mal'akh human-messenger surface — **REVIEW (within-book + cross-book variance)**

Per `malak_yhwh_2026-05.md` §4.4, human-messenger מַלְאָךְ is **outside the lock** ("use the plain register `ผู้ส่งสาร` or `ทูต` as context requires"). 2 Kings ships **three surfaces** for the human-envoy מַלְאָךְ / שָׁלַח-class:

| Ref | Context | Thai |
|---|---|---|
| **1:2, 1:3** | Ahaziah's messengers to Baal-zebub / "the messengers of the king of Samaria" | **`ผู้ส่งสาร`** |
| **17:4** | Hoshea's envoys to So of Egypt | **`ทูต`** |
| **20:13** | the Babylonian envoys (Merodach-baladan) | **`คณะทูต`** |

Notably, 1:2/1:3 ships **`ผู้ส่งสาร`** — the exact form the 1KI §3b audit recommended as the canonical cross-book surface (over 1SA's `ผู้ส่งสาร`/`ผู้ส่งข่าว` and 1KI's `ผู้สื่อสาร`). But 17:4/20:13 then use `ทูต`/`คณะทูต`. (Separately, `ผู้สื่อสาร` appears at 19:23 for Sennacherib's "messengers" in poetic taunt — a fourth surface, though that is inside quoted poetry.)

**REVIEW.** Cross-book + within-book normalization. The corpus now carries `ผู้ส่งสาร` / `ผู้ส่งข่าว` / `ผู้สื่อสาร` / `ทูต` / `คณะทูต` across JDG/1SA/1KI/2KI for the identical human-messenger lemma. Recommend confirming `ผู้ส่งสาร` as the canonical narrative surface (widest footprint; 2KI 1:2 already uses it) and folding the cross-book pass into the 1SA §3 / 1KI §3b flag. **Severity: LOW.**

---

## 4. Spirit-of-YHWH (2 Kgs 2:16) — **LOCKED (validates the 1KI §I נָשָׂא edge-case amendment)**

2 Kings has one Spirit-of-YHWH occurrence and two non-divine רוּחַ occurrences; all three are handled correctly:

| Ref | Hebrew | Referent | 2KI Thai |
|---|---|---|---|
| **2:16** | רוּחַ יְהוָה (the sons of the prophets: "lest the Spirit of YHWH has **carried** him," נָשָׂא) | Spirit of YHWH | **`พระวิญญาณขององค์พระผู้เป็นเจ้าทรงรับท่านขึ้นไป`** (`พระ` honorific ✓) |
| **2:9** | פִּי־שְׁנַיִם בְּרוּחֲךָ ("a double portion of **your** [Elijah's] spirit") | Elijah's prophetic spirit | `วิญญาณของท่าน` (bare — correct) |
| **2:15** | רוּחַ אֵלִיָּהוּ ("the spirit of Elijah rests on Elisha") | Elijah's prophetic spirit | `วิญญาณของเอลียาห์` (bare — correct) |
| **19:7** | רוּחַ (YHWH: "I will put **a** spirit in him" — Sennacherib's panic-impulse) | indefinite created spirit/disposition | `วิญญาณอย่างหนึ่ง` (bare — correct) |

The single Spirit-of-YHWH occurrence (**2:16**, נָשָׂא "carry") ships the `พระ` honorific — **exactly the edge-case the 1 Kings audit (§I) recommended documenting**, where it noted "add נָשָׂא (1 Kgs 18:12 / **2 Kgs 2:16** — 'the Spirit will carry/lift him') … as a documented out-of-empowerment-split verb class that still takes the `พระ` honorific." 2 Kings ships it compliant, validating that recommendation. The two Elijah-spirit verses (2:9, 2:15) and the indefinite spirit-in-Sennacherib (19:7, רוּחַ without יהוה) correctly stay bare `วิญญาณ`.

**LOCKED** ✓. **Recommend** finally landing the 1KI §I amendment to `spirit_of_yhwh_empowerment_2026-05.md` §"Edge cases," now citing both 1 Kgs 18:12 and 2 Kgs 2:16 as the נָשָׂא anchors. **Severity: LOW.**

---

## 5. Deuteronomistic regnal-cycle formulas — **LOCKED (the 1KI-created doc HOLDS across all five formulas)**

`dtr_history_cycle_formulas_2026-05.md` was created by the 1 Kings end-of-book audit (§C) precisely because "**2 Kings is composed almost entirely of them**." 2 Kings is the validation: ~40 regnal notices, and the formula family ships uniformly per the locked surfaces.

**(a) Evaluation formula** הָרַע / הַיָּשָׁר בְּעֵינֵי יְהוָה — locked `(ทำ)สิ่งชั่วร้าย / สิ่งที่ถูกต้อง ในสายพระเนตรขององค์พระผู้เป็นเจ้า`, **machine-enforced** (`check_phrase_consistency.py` evaluation-evil/right locks, `2KI `-scoped, green). The register split operates verse-by-verse:
- **Northern kings → plain `ทำสิ่งชั่วร้าย`** (no `ทรง`): Jehoram-of-Israel 3:2, Jehoahaz 13:2, Jehoash 13:11, Jeroboam II 14:24, Zechariah 15:9, Menahem 15:18, Pekahiah 15:24, Pekah 15:28, Hoshea 17:2.
- **Judahite kings → `ทรงทำสิ่งชั่วร้าย / ที่ถูกต้อง`** (with `ทรง`): Jehoram 8:18, Ahaziah 8:27, Joash 12:3, Amaziah 14:3, Azariah 15:3, Jotham 15:34, Ahaz 16:2, Hezekiah 18:3, Manasseh 21:2, Amon 21:20, Josiah 22:2, Jehoahaz 23:32, Jehoiakim 23:37, Jehoiachin 24:9, Zedekiah 24:19.

**(b) "Did not turn from the sin of Jeroboam who made Israel sin"** — uniform `ไม่ได้หันจากบาปของเยโรโบอัมบุตรของเนบัทที่ชักนำอิสราเอลให้ทำบาป` (13:2, 13:11, 14:24, 15:9, 15:18, 15:24, 15:28; the Jeroboam-sin tag also at 10:29, 17:21–22, 23:15). ✓

**(c) High-places formula** הַבָּמוֹת לֹא־סָרוּ → uniform **`สถานบูชาบนที่สูงยังไม่ถูกกำจัด`** (the lock's normalized surface — `สถานบูชาบนที่สูง` + `กำจัด`), machine-enforced: 12:4, 14:4, 15:4, 15:35 (the king-was-good-but refrain). The same `สถานบูชาบนที่สูง` noun carries the Josiah-purge (ch 23) and resettlement (ch 17) high-places throughout. ✓

**(d) Source-citation formula** "are they not written in the Book of the Chronicles…" — uniform `ส่วนพระราชกิจอื่น ๆ ของ[king] … ได้บันทึกไว้ในหนังสือพงศาวดารของกษัตริย์แห่ง[ยูดาห์/อิสราเอล]มิใช่หรือ?` (1:18, 8:23, 10:34, 12:20, 13:8, 13:12, 14:15, 14:18, 14:28, 15:6, 15:11, 15:15, 15:21, 15:26, 15:31, 15:36, 16:19, 20:20, 21:17, 21:25). Per Formula 4, this **keeps the elevated `พระราชกิจ`/`ทรงทำ` register for ALL kings incl. Northern** (Jehu 10:34, Jeroboam II 14:28 use `ทรงทำ`) — correct, because it is a stylized royal-record citation. (The `มิใช่หรือ?` rhetorical tag is present/absent tracking the Hebrew הֲלוֹא — absent for several assassinated Northern kings at 15:11/15/26/31 — fidelity, not drift.) ✓

**(e) Accession formula** — Judahite kings get the full royal register (`พระชนมายุ … พรรษา`, `ทรงครองราชย์ในกรุงเยรูซาเล็ม … ปี`, `พระมารดาทรงพระนามว่า …`): 8:26, 12:2, 14:2, 15:2, 15:33, 18:2, 21:1, 21:19, 22:1, 23:31, 23:36, 24:8, 24:18. (The mother's-name notice is a Judahite-only feature in the Hebrew formula, so the royal register applies uniformly to the set.) ✓

**LOCKED** ✓ per `dtr_history_cycle_formulas_2026-05.md`. **Forward note:** the doc's "Enforcement (forward)" section asked that the evaluation + high-places + death surfaces be machine-checked before 2 Kings ships. The **evaluation + high-places** locks are in `check_phrase_consistency.py` and green. The **death-formula register split** is NOT machine-checked (it is kingdom-keyed — `ทรง` for Judah, plain for Israel — which the substring checker cannot key on); it was verified clean by hand (see §6). Source-citation + accession are also not machine-checked but verified clean here. Consider whether a kingdom-keyed death-formula check is worth building for Chronicles.

---

## 6. DTr death/burial/succession formula — register split **LOCKED (was 1KI §6 REVIEW; now exceptionless)**

The death formula `וַיִּשְׁכַּב … עִם אֲבֹתָיו … וַיִּמְלֹךְ … תַּחְתָּיו` was a **REVIEW** in the 1 Kings audit (§6: `ทรง` applied inconsistently — Davidic line + Jeroboam got `ทรง`, Baasha/Omri/Ahab were bare). The dtr doc's **Formula 5** then locked the split as a **dynastic-legitimacy register decision** (Judah/Davidic → `ทรงล่วงหลับ … โอรส … แทนพระองค์`; Northern/breakaway → plain `ล่วงหลับ … บุตรของเขา … แทน`). **2 Kings ships this split exceptionless across all 14 death-formula occurrences:**

| Judahite/Davidic → `ทรงล่วงหลับ … (ราช)โอรส … แทนพระองค์` | Northern/Israel → plain `ล่วงหลับ … บุตรของเขา … แทน` |
|---|---|
| Jehoram 8:24, Azariah 15:7, Jotham 15:38, Ahaz 16:20, Hezekiah 20:21, **Manasseh 21:18**, Jehoiakim 24:6 | Jehu 10:35, Jehoahaz 13:9, Jehoash 13:13, Jehoash 14:16, Jeroboam II 14:29, Menahem 15:22 |

**The Manasseh datapoint is decisive.** Manasseh (21:18) is 2 Kings' most-condemned Judahite king (the cause of the exile, per 21:10–15 + 23:26 + 24:3), yet his death formula keeps the full `ทรงล่วงหลับ … ราชโอรส … แทนพระองค์`. This proves the split is keyed to **dynastic legitimacy (the Davidic covenant line), not the king's morality** — exactly as Formula 5 documents. The Northern kings who died naturally ("rested with fathers," as opposed to the many who were assassinated — Zechariah, Shallum, Pekahiah, Pekah, etc., who get no שכב formula) uniformly take the plain form.

(Micro-nuance, not a drift: **14:22**'s subordinate temporal back-reference — "after Amaziah [a Judahite] rested with his fathers" — ships `อามาซิยาห์ราชบิดาล่วงหลับ` with the `ราชบิดา` honorific noun but a plain `ล่วงหลับ` verb. This is a dependent clause, not Amaziah's death-notice proper [he was assassinated, 14:19–20]; strict Formula 5 application would prefer `ทรงล่วงหลับ`, but the dependent-clause context makes the plain verb defensible.)

**LOCKED** ✓ per `dtr_history_cycle_formulas_2026-05.md` Formula 5. The 1KI §6 REVIEW is now resolved by the doc and validated by the 2 Kings ship.

---

## 7. חַי־יְהוָה oath formula — **LOCKED**

"As YHWH lives" → uniform **`องค์พระผู้เป็นเจ้า…ทรงพระชนม์อยู่`**:

| Ref | Speaker | Surface |
|---|---|---|
| 2:2, 2:4, 2:6 | Elisha (refusing to leave Elijah) | `องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่ และตราบที่ท่านยังมีชีวิตอยู่…` |
| **3:14** | Elisha (to Jehoram + Jehoshaphat) | **`องค์พระผู้เป็นเจ้าจอมโยธา…ทรงพระชนม์อยู่แน่ฉันใด`** (YHWH-Tsebaoth compound preserved ✓) |
| 4:30 | the Shunammite mother | `องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่…` |
| 5:16 | Elisha (refusing Naaman's gift) | `องค์พระผู้เป็นเจ้า…ทรงพระชนม์อยู่แน่ฉันใด` |
| 5:20 | Gehazi | `องค์พระผู้เป็นเจ้าทรงพระชนม์อยู่แน่ฉันใด` |

Matches `hebrew_oath_formulas_2026-05.md` + the 1SA/1KI locks; the Tsebaoth compound at 3:14 is preserved as in 1KI 18:15. (Separately, "the **living** God," אֱלֹהִים חַי, in the Rabshakeh narrative at 19:4 + 19:16 → `พระเจ้าผู้ทรงพระชนม์` — a distinct construction, also using `ทรงพระชนม์`, correct.)

**LOCKED** ✓.

---

## 8. Pagan deities + host of heaven — **LOCKED (with §8b Baal-zebub REVIEW + §8c Molech micro-variance)**

2 Kings is the corpus's densest pagan-deity book after Judges/1 Kings (the Jehu Baal-purge ch 10; the Samaria resettlement pantheon ch 17; Manasseh's apostasy ch 21; Josiah's purge ch 23). The shipped renderings apply the OT-precedent `พระ`/`เทพ`/`เทพี` register (`pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md`) uniformly — **with one exception (§8b):**

| Deity | Hebrew | 2KI Thai | Verses |
|---|---|---|---|
| **Baal** (Israelite cult) | בַּעַל | **`พระบาอัล`** (uniform) | 3:2, 10:18–28, 11:18, 17:16, 21:3, 23:4 |
| **Baal-zebub** (Ekron) | בַּעַל זְבוּב | **`บาอัลเซบูบ เทพเจ้าแห่งเอโครน`** (no `พระ` — see §8b) | 1:2, 1:3, 1:6, 1:16 |
| Asherah | אֲשֵׁרָה | `เสาอาเชราห์` (pole) | 13:6, 17:16, 18:4, 21:3, 21:7, 23:4, 23:6, 23:15 |
| Resettlement gods (ch 17) | — | **`พระสุคโคทเบโนท`, `พระเนอร์กัล`, `พระอาชิมา`, `พระนิบหัส`, `พระทารทัก`, `พระอัดรัมเมเลค`, `พระอานัมเมเลค`** | 17:30–31 |
| Nisroch | נִסְרֹךְ | **`พระนิสรอค`** | 19:37 |
| Molech | מֹלֶךְ | **`พระโมเลค`** (cf. 1KI `โมเลคเทพ…` — see §8c) | 23:10 |
| Ashtoreth / Chemosh / Milcom | עַשְׁתֹּרֶת / כְּמוֹשׁ / מִלְכֹּם | `พระอัชเทเรทเทพี…ของชาวซีโดน` / `พระเคโมชเทพ…ของโมอับ` / `มิลโคมเทพ…ของชาวอัมโมน` | 23:13 |
| host of heaven | צְבָא הַשָּׁמַיִם | **`บริวารแห่งฟ้าสวรรค์`** (uniform) | 17:16, 21:3, 21:5, 23:4, 23:5 |

**Cross-book wins:** the ch-23 trio `อัชเทเรท / เคโมช / มิลโคม` matches 1KI 11:5/11:7/11:33 **exactly** (incl. the `พระ`-on-Ashtoreth/Chemosh, bare-Milcom pattern + the `(เทพ)อันน่าสะอิดสะเอียน` שִׁקֻּץ descriptor). **No `พระเจ้า`-for-pagan-deity violation** anywhere (the 1SA §12 Dagon problem does not recur; the resettlement gods + Nisroch + Molech all take `พระ`/`เทพ`, never the supreme `พระเจ้า`). Calf-idols → `(รูป)ลูกวัวทองคำ` (10:29, 17:16); the bronze serpent Nehushtan → `เนหุชทาน` (18:4); Topheth → `โทเฟท` (23:10).

**LOCKED** ✓ (with §8b + §8c flags).

---

## 8b. Baal-zebub `พระ`-register — **REVIEW (lone exception to the 2KI pagan-deity register)**

Every foreign proper-noun deity in 2 Kings takes the `พระ` prefix (§8 table) — `พระบาอัล`, `พระสุคโคทเบโนท`, `พระเนอร์กัล`, `พระอาชิมา`, `พระนิบหัส`, `พระทารทัก`, `พระอัดรัมเมเลค`, `พระอานัมเมเลค`, `พระนิสรอค`, `พระโมเลค`, `พระอัชเทเรท`, `พระเคโมช` — **except `บาอัลเซบูบ` (1:2, 1:3, 1:6, 1:16), which ships bare** (`บาอัลเซบูบ เทพเจ้าแห่งเอโครน`).

The bare form **does** carry a verse-level rationale (1:2 `key_decisions`): the deliberate `אֱלֹהֵי` → **`เทพเจ้า`** (not `พระเจ้า`, "which is reserved for YHWH") is "the heart of the chapter" (the YHWH-vs-Baal-zebub polemic of "is there no God in Israel?"), and the consultation verb is deliberately plain `สอบถาม` (not deferential `ทูลถาม`, reserved for inquiring of YHWH). **That part is principled and well-documented.** But the rationale is *silent on why the proper noun drops `พระ`* — it cites `เทียบ พระบาอัล 1 Kings 16:31` (i.e., it was aware of the `พระบาอัล` form) yet renders bare. So either:
- **(a) the bare form is a deliberate further deprecation** of the Ekron oracle-god (distinct from the established Israelite-apostasy cult of `พระบาอัล`), in which case it should be *documented* as an intentional carve-out; or
- **(b) the `พระ` was dropped inadvertently** along with the `เทพเจ้า` decision, in which case it should normalize to `พระบาอัลเซบูบ` for register consistency with `พระบาอัล` + every other 2KI foreign deity.

**REVIEW.** Recommend Ben confirm (a) document the carve-out or (b) normalize. The asymmetry is real — Adrammelech and Anammelech (17:31), to whom the Sepharvites *burned their children*, keep `พระ`; the Ekron oracle does not. **Severity: LOW–MEDIUM** (4 verses; register-consistency against a locked pattern, but a documented verse-level decision already exists). Folds into the same pagan-deity-doc update as §8c.

---

## 8c. Molech `พระ`-vs-`เทพ` cross-book micro-variance — **REVIEW**

Molech ships **`พระโมเลค`** at 2 Kgs 23:10 but **`โมเลคเทพอันน่าสะอิดสะเอียน`** at 1 Kgs 11:7 (no `พระ`; `เทพ`-descriptor). Same deity, two cross-book surfaces. (Both are within the sanctioned `พระ`/`เทพ` register, so neither is a violation, but the surface differs.) Recommend normalizing when §8b lands; the `พระ`-prefix form (`พระโมเลค`) is the more consistent with the 2KI pattern. **Severity: LOW.**

---

## 9. Adversary-speech register — human-imperial-blasphemer class (Rabshakeh) — **REVIEW (new class; principled but undocumented)**

`adversary_speech_register_2026-05.md` (LOCKED 2026-05-01, from the Luke audit) requires *neutral* speech-verbs for adversaries — never the deferential `ทูล` — and was written for **NT demons / the devil / false prophets** (its edge-cases mention OT הַשָּׂטָן but no human imperial blasphemer). 2 Kings 18–19 (the Rabshakeh / Sennacherib confrontation) is the corpus's **first sustained human imperial blasphemer taunting YHWH directly**. The handling is a sophisticated three-way register interaction:

| Speaker / referent | 2KI Thai register | Verses |
|---|---|---|
| **Rabshakeh** (the envoy/official) → neutral speech-verbs | `กล่าวแก่` / `ตอบว่า` / `ร้องเสียงดัง` | 18:19, 18:27, 18:28 |
| **The Assyrian "great king"** (a foreign monarch) → foreign-royal speech register | `มหาราชา…ตรัสดังนี้` / `พระดำรัสของมหาราชา` / Sennacherib `ทรงส่ง` | 18:19, 18:28, 19:9 |
| **YHWH** (mocked, inside the adversary's quote) → divine honorific preserved as content | `องค์พระผู้เป็นเจ้า…จะทรงช่วยกู้` | 18:30, 18:32, 18:35 |
| **Pagan "gods" of the nations** (in the taunt) → pagan register | `พระของชนชาติ` / `พระของเมืองฮามัท…` | 18:33–35 |
| YHWH's reply via Isaiah: "the Holy One of Israel" | `องค์บริสุทธิ์แห่งอิสราเอล`; reproach/blaspheme verbs `เย้ยหยัน`/`หมิ่นประมาท` (חרף/גדף) | 19:4, 19:6, 19:16, 19:21, 19:22, 19:23 |

This is **consistent with the doc's principle** (neutral speech-verb for the adversary's *stance*; the divine referent keeps its honorific *as content*, exactly as the demon edge-case preserves `พระเยซูบุตรของพระเจ้า`) — and it correctly layers in the *separate* foreign-monarch royal register (`honorifics_non_divine_authorities_2026-04.md`: the Assyrian "great king" gets `ตรัส`/`พระดำรัส` as a head of state, while his *envoy* Rabshakeh gets neutral verbs). But the **configuration is undocumented**: the adversary-speech doc names only NT demonic/satanic adversaries, and the interaction of (envoy-neutral) × (foreign-king-royal) × (mocked-divine-honorific-as-content) has not been written down.

**REVIEW.** Recommend confirming the handling and adding a short OT-extension note to `adversary_speech_register_2026-05.md` (or `ot_register_policy_2026-05.md`) covering the human-imperial-blasphemer class — Rabshakeh now, but forward-protecting Sennacherib/Nebuchadnezzar elsewhere, the Chaldean taunts in Isaiah/Jeremiah, and Belshazzar in Daniel. **Severity: LOW** (no surface change needed; documentation of an existing principled pattern).

---

## 10. Deuteronomistic Name-theology — **STABLE; doc/Layer-2 still pending (MEDIUM)**

The "put my **Name** there" centralization theology (Deut 12 → 1 Kings 8 substrate) recurs in 2 Kings at the hinge moments of the Manasseh apostasy + the final rejection: 21:4 (`เราจะตั้งนามของเราไว้ในกรุงเยรูซาเล็ม`), 21:7 (`เราจะสถาปนานามของเราไว้เป็นนิตย์`), 23:27 (`นามของเราจะอยู่ที่นั่น`). Rendered cleanly with `นาม(ของเรา)` — consistent with the 1 Kings 8 surfaces.

**STABLE; not documented in `docs/translator_decisions/`.** The 1 Kings audit (§H) recommended a brief `name_theology_deuteronomistic_2026-05.md` or a Layer-2 cross-ref at 1 Kgs 8:29 ↔ Deut 12; it remains unwritten. 2 Kings 21:7 / 23:27 are the thread's theological climax (the Name placed → the Name's house rejected), strengthening the case. **Recommend** the doc or Layer-2 now (forward-protects 1–2 Chronicles' temple theology + the NT echoes, Acts 7:47–49). **Priority: MEDIUM.**

---

## 11. "Until this day" leitwort — **REVIEW (cross-book; 1 Samuel is now the lone outlier)**

2 Kings renders עַד הַיּוֹם הַזֶּה uniformly as **`จนถึงทุกวันนี้`** (with the `ทุก-` intensifier) — 2:22, 8:22, 10:27, 14:7, 16:6, 17:23, 17:34, 17:41, 20:17, 21:15 (10×). This matches the JDG-majority + 1KI-uniform form.

**Cross-book corpus picture now (four DtrH books):**
| Book | Surface | Count |
|---|---|---|
| Judges | `จนถึงทุกวันนี้` | 6× |
| 1 Samuel | `จนถึงวันนี้` (bare) | 8× uniform |
| 1 Kings | `จนถึงทุกวันนี้` | 5× uniform |
| **2 Kings** | **`จนถึงทุกวันนี้`** | **10× uniform** |

**Three of four Former-Prophets books now agree on `จนถึงทุกวันนี้`; 1 Samuel is the lone outlier** — and 2 Kings (10×) is now the largest single-book witness. This further sharpens the 1KI §14 cross-book REVIEW: lock `จนถึงทุกวันนี้` as the canonical Former-Prophets surface in `leitwort_handling_policy_2026-05.md` and normalize 1 Samuel's 8 occurrences.

**REVIEW.** Internal 2 Kings uniformity ✓; the cross-book lock + 1SA normalization is the pending decision. **Severity: LOW.**

---

## 12. "Man of God" (אִישׁ הָאֱלֹהִים) — **STABLE**

Elisha's (and Elijah's, ch 1) standing title אִישׁ הָאֱלֹהִים renders uniformly **`คนของพระเจ้า`** across **33 verses** (chs 1, 4–8, 13, 23). The address form `ข้าแต่คนของพระเจ้า` (1:9, 1:11, 1:13 — the captains to Elijah) correctly uses the deferential `ข้าแต่` for a revered human. No drift.

**STABLE** ✓ (uniform; covered in spirit by `honorifics_non_divine_authorities_2026-04.md` — no separate doc needed).

---

## 13. צָרַעַת "leprosy" — **STABLE**

צָרַעַת renders uniformly **`โรคเรื้อน`** across the Naaman narrative (5:1, 5:3, 5:6, 5:7, 5:11, 5:27 — incl. Gehazi's transfer), the four lepers (7:3, 7:8), and Azariah/Uzziah's affliction (15:5). Uniform within 2 Kings and consistent with the traditional Thai rendering. (Modern translation theory distinguishes biblical צָרַעַת — a broader category of "defiling skin condition" — from Hansen's disease, but the corpus's `โรคเรื้อน` should track whatever Leviticus 13–14 established; assumed consistent with the Leviticus purity-vocabulary lock.)

**STABLE** ✓ (defer to the Leviticus precedent; no 2 Kings-specific action).

---

## 14. Royal ทרง-register (Judahite + foreign kings) — **LOCKED**

The narrator's royal `ทรง`-register per `honorifics_non_divine_authorities_2026-04.md` + the `ot_register_policy_2026-05.md` §2.2 downshift is applied throughout and is the engine behind the dtr register split (§5–6):
- **Judahite kings → `ทรง`** (Hezekiah `ทรงรื้อ` 18:4, Josiah `ทรงกำจัด` 23:5, etc.).
- **Apostate Northern kings → register downshift** (plain death/evaluation; the §5 split). 2 Kings 1:1 opens by explicitly reserving `สิ้นพระชนม์` for the Davidic line and using plain `สิ้นชีวิต` for Ahab (1:1 `key_decisions`, citing `ot_register_policy_2026-05.md` §2.2).
- **Foreign monarchs → `ทรง`/`ตรัส`** as heads of state: the Assyrian "great king" (`ตรัส`, `พระดำรัส`, §9), Sennacherib (`ทรงส่ง` 19:9), Pharaoh Neco, the king of Babylon. This is the foreign-royal register, distinct from the divine.

**LOCKED** ✓.

---

## 15. MT/LXX inclusion-variant gap — **DECIDE before tagging (third consecutive DtrH book; recommend corpus-policy resolution)**

The 25 `output/textual_variants/2kings_NN.json` files contain **only** 25× `tetragrammaton_convention_first_occurrence` (the YHWH footnote). **Zero** `inclusion_variant_minus` / `inclusion_variant_plus` / MT-vs-LXX-divergence entries exist. The shipped text follows MT throughout (defensible, matching `ot_canon_and_text_base_2026-05.md`), but the Tier-2 transparency layer for textual divergence is absent — **identical to 1SA §17 and 1KI §17. This is now the third consecutive DtrH book to ship the same gap.**

**Honest sizing:** 2 Kings is a *less acute* case than 1 Kings. 1 Kings (LXX 3 Reigns) had macro-structural divergences (the two Miscellanies, the alternate Jeroboam narrative, the MT 20↔21 chapter swap) that genuinely cried out for a reader note. 2 Kings sits largely in the LXX **kaige** recension, which is a *translation-character* phenomenon, not a content reordering; the MT/LXX divergences here are mostly scattered verse-level pluses/minuses + the famously knotty **regnal-synchronism chronology** (the reign-length / co-regency data that does not arithmetically reconcile). There is no 2 Kings equivalent of the 1 Kings Miscellanies.

**DECIDE — but the recommended path is a corpus-level policy decision, not another per-book chapter-footer scramble.** Re-flagging the identical DECIDE for the third book in a row is itself the signal: Ben should choose, once, between —
- **(a) Commit to Tier-2 disposition corpus-wide** — i.e., a standing convention that each OT book whose MT-base diverges materially from LXX/OG carries at least a book-level prefatory note (and chapter-footers where a divergence is locally significant). For 2 Kings this would be a single brief note: "follows MT; the LXX kaige text differs in translation character and scattered detail; the regnal synchronisms are a known crux." Cheap; closes the gap for 2 Kings + sets the rule for Jeremiah (the big one: LXX ~⅛ shorter, reordered oracles) + Daniel (Greek additions).
- **(b) Formally accept silent MT-base adherence per RULES §5** for books without macro-structural divergence, and **stop re-flagging it per-book** — documenting in `mt_vs_lxx_textual_variant_handling_2026-05.md` that the Tier-2 obligation triggers only on macro-structural divergence (1 Kings 3 Reigns, Jeremiah, Daniel), not on kaige-character or routine verse-level variants.

Either resolution unblocks the tag and ends the recurring DECIDE. **Severity: MEDIUM** (the gap is real and now systemic, but 2 Kings is the low-acuteness end of it; the value is in the *policy*, not the 2 Kings footers per se). Gates Jeremiah + Daniel.

---

## 16. Versification — **LOCKED**

2 Kings has no famous chapter-shift like 1 Kings 5 (MT 5 = English 4:21–5:18). The per-chapter `versification_2kings_NN.md` anchor checks are all green, and `data/versification_map.json` carries 2 Kings entries. The minor MT-vs-English verse-number offsets in 2 Kings (a handful of places where the English splits/joins differently) are handled by the map. No reader-facing versification note was required.

**LOCKED** ✓ per `verse_schema_and_versification_2026-05.md`.

---

## 17. Inherited corpus locks — all compliant except where flagged

| Doc | 2KI evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1 (YHWH 228 surfaces, 0 ยาห์เวห์ residue, 25/25 footnote), §2 (Elohim/Adonai; 7:6 องค์เจ้านาย; **no Adonai-YHWH compound — 1KI §8 issue absent**) | **LOCKED** |
| `malak_yhwh_2026-05.md` | §3 — **HOLDS** (1:3, 1:15, 19:35 all ทูตสวรรค์ขององค์พระผู้เป็นเจ้า; machine-enforced). Human-messenger surface §3b REVIEW. | **LOCKED** |
| `dtr_history_cycle_formulas_2026-05.md` | §5–6 — **HOLDS** across all five formulas; death-formula register split exceptionless (Manasseh keeps ทรง). First downstream ship of the doc 1KI created. | **LOCKED** |
| `spirit_of_yhwh_empowerment_2026-05.md` | §4 — 2:16 (נָשָׂא) ships พระวิญญาณ; validates the 1KI §I edge-case amendment. Elijah-spirit (2:9/2:15) + indefinite spirit (19:7) correctly bare. | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | §7 — חַי־יְהוָה ×6 uniform ทรงพระชนม์อยู่; 3:14 Tsebaoth compound preserved. | **LOCKED** |
| `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md` | §8 — พระ/เทพ/เทพี register uniform; ch-23 trio matches 1KI; no พระเจ้า-for-pagan violation. **EXCEPTIONS:** Baal-zebub bare (§8b), Molech cross-book (§8c). | **LOCKED-with-§8b/§8c-REVIEW** |
| `adversary_speech_register_2026-05.md` | §9 — Rabshakeh envoy neutral verbs ✓; principled but undocumented for the human-imperial-blasphemer class. | **LOCKED-with-§9-REVIEW** |
| `honorifics_non_divine_authorities_2026-04.md` | §14 — Judahite + foreign-king ทรง/ตรัส register; §2.2 downshift for apostate Northern kings. | **LOCKED** |
| `ot_register_policy_2026-05.md` | §5–6, §14 — the §2.2 downshift is the engine of the dtr register split; applied cleanly (1:1 Ahab สิ้นชีวิต, Davidic สิ้นพระชนม์). | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | King-name + place-name + foreign-king spot-check clean (เอลีชา, เยฮู, เฮเซคียาห์, มนัสเสห์, โยสิยาห์, เซนนาเคอริบ, เนบูคัดเนสซาร์, ราบชาเคห์; อัชเทเรท/เคโมช/มิลโคม match 1KI). `check_key_term_consistency.py` clean. | **LOCKED** |
| `leitwort_handling_policy_2026-05.md` | §11 — internal uniform จนถึงทุกวันนี้ ×10; cross-book 1SA-outlier decision pending. | **LOCKED-with-§11-cross-book-REVIEW** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md` | §15 — **INCLUSION-VARIANT GAP** (zero non-YHWH entries; third consecutive book). | **DECIDE-§15** |
| `verse_schema_and_versification_2026-05.md` | §16 — anchors green; map carries 2KI entries; no chapter-shift. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | חֶסֶד sparse in 2 Kings; no dense cluster; renderings within the locked family where they occur. | **LOCKED (light)** |
| `ot_warfare_ethics_2026-05.md` | No dense ḥerem cluster; the Jehu/Moab/Aram campaigns render within established warfare vocabulary. | **LOCKED (N/A-light)** |
| `nicham_divine_relenting_2026-05.md` | No load-bearing נחם crux in 2 Kings. | **LOCKED (N/A)** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "hand of YHWH" (3:15), YHWH's anger/`ทรงพระพิโรธ` (17:18, 23:26), `พระพักตร์` (17:18/23, 23:27). Compliant. | **LOCKED** |

---

## 18. Mechanical (§1) — all green (one transient report file)

- 25/25 chapters: `output/check_reports/2kings_NN_review.md` all "✅ Ready to ship" ✓
- 25/25 chapters: `output/back_translations/2kings_NN.json` ✓
- 25/25 chapters: `output/translations/2kings_NN.json` (719 verses) ✓
- 25/25 chapters: `output/textual_variants/2kings_NN.json` ✓ (YHWH footnote deployed; inclusion-variant gap flagged §15)
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** (603-chapter corpus)
- `check_phrase_consistency.py`: **0 violations across 12 audited locks** (18,247 verses), incl. the four Kings-scoped OT locks (`malak`, evaluation-evil, evaluation-right, high-places) now machine-enforced for `2KI `
- `git status output/`: **clean except `output/check_reports/divine_names.md`** — a transient single-chapter scratch report (`Chapters checked: 1`; its only diff clears a stale 2SA 1:10 warning). Report-only, not a 2 Kings translation surface; identical in kind to the 1SA/1KI notes.
- YHWH `องค์พระผู้เป็นเจ้า` surfaces: **228 verses**. `ยาห์เวห์` residues: **zero**.
- `audit_inclusion_variants.py --book 2KI --strict` / `export_to_usfm.py --book 2KI`: the NT-tuned heuristic + NT-only USFM table do not cover OT/MT-vs-LXX (carried-over separate concern, as in prior OT audits; the §15 gap is the substantive item). **Book-code `2KI` registration in the §3/§4 tooling slug tables (`build_external_review_packet.py`, `audit_items_to_yaml.py`) — verify/register per the EOB book-code-registration gotcha before building the packet.**

**Severity: GREEN.**

---

## 19. NT cross-corpus echoes from 2 Kings — **STABLE (Layer-2 opportunities)**

| 2KI ref | NT echo | Note |
|---|---|---|
| 5:1–14 (Naaman the Syrian healed) | **Luke 4:27** (Jesus cites Naaman) | direct citation — verify Thai surface alignment |
| 1:8 / 1:10–12 (Elijah's mantle + fire from heaven) | **Luke 9:54** ("call down fire, as Elijah did"); Elijah-Baptist typology | Layer-2 candidate |
| 2:11 (Elijah taken up in the whirlwind) | **Mark 9:4 / Mal 4:5 / Matt 17** (Elijah at the Transfiguration; "Elijah must come first") | thematic |
| 4:42–44 (Elisha feeds 100 with 20 loaves) | **John 6 / Mark 6:30–44** (feeding miracles) | Layer-2 candidate |
| 4:32–37 (Elisha raises the Shunammite's son) | **Luke 7:11–15** (Nain widow's son); resurrection-miracle type | thematic |

**STABLE.** Renderings are sound; the cross-references are corpus-completeness polish. **Severity: LOW.** (Prioritize Luke 4:27 Naaman — a direct dominical citation.)

---

## 20. Flagged for Ben's attention

### A. MT/LXX inclusion-variant gap — **DECIDE before tagging** (§15)
Zero non-YHWH textual-variant entries in 2KI; third consecutive DtrH book. 2 Kings is the low-acuteness end (kaige character, not macro-structural like 1 Kings). **Recommend a one-time corpus-policy decision** — (a) commit to Tier-2 disposition corpus-wide (a single book-level note for 2 Kings) or (b) formally accept silent MT-base adherence per RULES §5 and stop re-flagging per book — rather than another per-book footer scramble. Gates Jeremiah + Daniel.

### B. Baal-zebub `พระ`-register — **REVIEW** (§8b)
`บาอัลเซบูบ` (1:2/1:3/1:6/1:16) is the lone foreign deity in 2 Kings shipped without `พระ`; all others (incl. the child-sacrifice gods Adrammelech/Anammelech, Nisroch, Molech) take `พระ`. Verse-level rationale documents the `เทพเจ้า`-not-`พระเจ้า` polemic but not the `พระ`-drop. Confirm: document the carve-out, or normalize to `พระบาอัลเซบูบ`.

### C. Adversary-speech register — human-imperial-blasphemer class (Rabshakeh) — **REVIEW** (§9)
2 Kings 18–19 is the corpus's first human imperial blasphemer taunting YHWH; the three-way register interaction (envoy-neutral × foreign-king-royal × mocked-divine-honorific-as-content) is principled but undocumented. Confirm + add an OT-extension note to `adversary_speech_register_2026-05.md`. Forward-protects Isaiah/Jeremiah Chaldean taunts + Daniel's Belshazzar.

### D. "Until this day" leitwort cross-book normalization — **REVIEW** (§11)
2 Kings uniform `จนถึงทุกวันนี้` ×10 (largest single-book witness); now JDG + 1KI + 2KI agree, **1 Samuel is the lone outlier**. Lock `จนถึงทุกวันนี้` in `leitwort_handling_policy_2026-05.md`; normalize 1SA's 8 occurrences.

### E. mal'akh human-messenger surface — **REVIEW** (§3b)
2 Kings ships `ผู้ส่งสาร` (1:2/1:3 — the 1KI-recommended canonical form) + `ทูต` (17:4) + `คณะทูต` (20:13). Cross-book + within-book normalize (recommend `ผู้ส่งสาร`); fold into the 1SA §3 / 1KI §3b pass.

### F. Molech cross-book micro-variance — **REVIEW** (§8c)
`พระโมเลค` (2KI 23:10) vs `โมเลคเทพ…` (1KI 11:7). Normalize when §8b lands.

### G. New / amended corpus docs — summary
1. **`name_theology_deuteronomistic_2026-05.md`** (§10) — still unwritten since 1KI §H; 2KI 21:7/23:27 are the thread's climax. MEDIUM (or Layer-2).
2. **`spirit_of_yhwh_empowerment_2026-05.md`** §"Edge cases" amendment (§4) — add נָשָׂא (1 Kgs 18:12 + **2 Kgs 2:16**) as the out-of-split verb class that keeps `พระ`. The 1KI §I recommendation; 2KI validates it. LOW.
3. **`adversary_speech_register_2026-05.md`** OT-extension note (§9) — human-imperial-blasphemer class. LOW.
4. **`leitwort_handling_policy_2026-05.md`** (§11) — lock `จนถึงทุกวันนี้`. LOW.
5. **`pagan_deities_2026-04.md` / `ot_polytheistic_register_2026-05.md`** (§8b/§8c) — Baal-zebub carve-out-or-normalize + Molech normalization. LOW.
6. **`malak_yhwh_2026-05.md`** §3 checklist — tick "2 Kings 1" (now shipped clean). Bookkeeping.

### H. External AI review (§3 of checklist) — pending
Recommended 5-cluster packet (see `external_review_items_2KI.md`):
1. **Baal-zebub `พระ`-register** (§8b) — distinctively-2KI editorial question
2. **Adversary-speech human-blasphemer extension** (§9) — Rabshakeh; novel OT class
3. **MT/LXX gap as corpus-policy** (§15) — the recurring DECIDE, reframed
4. **"Until this day" cross-book normalization** (§11) — 1SA outlier
5. **mal'akh human-messenger surface** (§3b) — cross-book convergence

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG/1SA/1KI pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 11 items (§1 YHWH, §2 Elohim/Adonai, §3 mal'akh [lock holds], §4 Spirit-of-YHWH, §5 DTr formulas, §6 death-formula split, §7 oath, §8 pagan deities, §14 royal register, §16 versification, §18 mechanical; + inherited locks via §17)
- **STABLE (recommend doc / Layer-2 / no action):** 4 items (§10 Name-theology [MEDIUM], §12 man-of-God [no action], §13 leprosy [defer to Leviticus], §19 NT echoes [LOW])
- **REVIEW:** 5 items (§3b mal'akh human-messenger surface, §8b Baal-zebub register, §8c Molech cross-book, §9 adversary-speech human-blasphemer extension, §11 "until this day" cross-book)
- **DECIDE:** 1 item (§15 MT/LXX inclusion-variant gap — recommend corpus-policy resolution)

**1 DECIDE item blocks the `book-2kings-v1` tag** (§15) — and the recommended resolution is a one-time corpus policy, not 2 Kings-specific work.

**No new translator_decisions doc is *required*; 2 amendments + 1 optional new doc recommended:** amend `spirit_of_yhwh_empowerment` (נָשָׂא) + `leitwort_handling_policy` (`จนถึงทุกวันนี้`) + `adversary_speech_register` (OT blasphemer note); optionally write `name_theology_deuteronomistic` (carried from 1KI §H).

---

## Recommendation

**2 Kings ships in the strongest corpus-hygiene shape of any DtrH book to date** — and it is the proof-of-concept for end-of-book locking. It is the **fifth Former-Prophets book** and the first to ship *downstream* of locks created by a prior book's audit. The audit finds:

- **The mal'akh-YHWH lock HOLDS** (1:3, 1:15, 19:35 all `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`) — the 1 Kings 19:7 drift was the trigger to add the `malak` machine-check, and 2 Kings ships all three named forward-cover targets clean. The lock-then-enforce loop worked.
- **The DTr regnal-cycle formulas doc HOLDS** across all five formulas in the book it was written to protect (~40 regnal notices), and the death-formula dynastic-register split is **exceptionless** — Manasseh, the worst Judahite king, still keeps `ทรง`, confirming the split is dynastic-legitimacy, not morality.
- **The spirit-of-YHWH נָשָׂא edge-case** (2:16 → `พระวิญญาณ`) validates the amendment the 1 Kings audit recommended.
- The only genuinely-new editorial questions are local register decisions (**Baal-zebub** `พระ`-drop; the **Rabshakeh** adversary-speech configuration) — neither blocks the tag.
- The **MT/LXX inclusion-variant gap** is the lone DECIDE, now in its third consecutive book — the signal that a one-time corpus *policy* decision is overdue (not more per-book footers).

**Tag `book-2kings-v1` after:**
1. Ben's decision on **§A** (DECIDE: MT/LXX gap — recommend the corpus-policy resolution)
2. Ben's confirmation on **§B–§F** (REVIEW items — all LOW/LOW-MEDIUM, none surface-blocking)
3. The recommended doc amendments (§G — spirit-of-YHWH נָשָׂא, leitwort `จนถึงทุกวันนี้`, adversary-speech OT note; optional Name-theology doc)
4. External AI sanity-check (§H)

**The load-bearing takeaway:** 2 Kings demonstrates that the end-of-book audit → lock → machine-enforce loop prevents downstream drift. The two locks that 1 Kings created specifically to protect 2 Kings (dtr formulas + malak) both held, exceptionlessly.
