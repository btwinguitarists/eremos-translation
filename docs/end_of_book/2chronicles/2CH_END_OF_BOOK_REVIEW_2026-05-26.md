# 2 Chronicles — End-of-Book Review

**Date:** 2026-05-26
**Scope:** All 36 chapters of 2 Chronicles (822 verses); `glossary.json`; `docs/translator_decisions/` corpus (~96 docs through the 1 Chronicles end-of-book audit).
**Trigger:** 2CH 36 shipped (commit `0c19b0a`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Thirteenth OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles) and the **conclusion of the Chronicler's History**. 2 Chronicles is the corpus's first sustained encounter with three stress-surfaces at once: (a) **the full Judahite regnal cycle** (Solomon → Rehoboam → … → Zedekiah, ~20 reigns), which exercises the Deuteronomistic regnal-cycle formulas more densely than any book except 2 Kings — `dtr_history_cycle_formulas_2026-05.md` explicitly declares it "Gates 2 Kings + **Chronicles**"; (b) the **densest synoptic field in the OT** (2 Chr ≈ large stretches of 1 Kings + 2 Kings, plus the temple narrative ≈ 1 Kings 5–9 and the Assyrian-crisis ≈ 2 Kings 18–19 / Isaiah 36–37); and (c) the **temple Name-theology** (chs 6–7, Solomon's dedication = 1 Kings 8) — the motif prior audits (1KI §H, 2KI §10) deferred to 2 Chronicles as the natural home of a `name_theology_deuteronomistic` doc.
**Mandate:** Internal editorial review (§2 of checklist) + external AI packet (§3). Surface only — no translation changes.

## Summary

- **17 cross-cutting items reviewed.** Mechanical gates (§1) pass: 36/36 chapters have green per-chapter reports + back-translations + translations (822 verses); `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings across the 668-chapter corpus); `check_phrase_consistency.py` clean across all 12 audited locks (20,012 verses); `audit_inclusion_variants.py --book 2chronicles --strict` = 0 candidates, exit 0. The single dirty file in `git status output/` is `output/check_reports/divine_names.md` — a transient single-chapter scratch report whose only diff clears a stale 2SA 1:10 warning; report-only, not a 2 Chronicles surface, identical in kind to the note carried in the 1SA/1KI/2KI/1CH audits.
- **The mal'akh-YHWH lock now ships 2 Chronicles UNDER machine enforcement** — the 1 Chronicles audit's headline REVIEW (lock held by convention only, scope `["1KI ","2KI "]`) was actioned 2026-05-26: the `check_phrase_consistency.py` `malak` scope was widened to `["1KI ","2KI ","1CH ","2CH "]`. 2 Chronicles' one divine-angel occurrence — **32:21** (= 2 Kings 19:35, the Assyrian-camp destroyer) — ships **`ทูตสวรรค์องค์หนึ่ง`** (anarthrous standalone מַלְאָךְ, correctly without the genitive compound per `malak_yhwh_2026-05.md` §4.1). The human/prophetic messengers (35:21 Neco's envoys; 36:15–16 the prophets-as-messengers) correctly stay outside the divine lock (`ผู้สื่อสาร`). See §3. **LOCKED.**
- **3 items flagged DECIDE** (Ben choice needed before tagging `book-2chronicles-v1`):
  - **§4 — the "did evil" evaluation formula drifts in the six late apostate kings.** 21:6 (Jehoram) and 22:4 (Ahaziah) ship the locked **`ทำสิ่งชั่วร้าย`** (with `ร้าย`) *and* carry an explicit key_decision citing the lock; but **33:2, 33:6 (Manasseh), 33:22 (Amon), 36:5 (Jehoiakim), 36:9 (Jehoiachin), 36:12 (Zedekiah)** all ship bare **`ทำชั่ว`** (no `ร้าย`) with **no** key_decision. This is the exact surface defect the 1 Kings EOB normalized at 22:53 (`ชั่ว`→`ชั่วร้าย`), recurring across six verses — undetected because the DTr evaluation lock is scoped `["1KI ","2KI "]` and **never machine-checked 2 Chronicles** (see §7).
  - **§8 — 24:20, the named לָבַשׁ-class Spirit forward-protect anchor, ships missing the locked honorific `ทรง`.** `spirit_of_yhwh_empowerment_2026-05.md` explicitly names "2 Chr 24:20 (forward-protect)" and locks the *clothed-by-the-Spirit* class as **`ทรงสวมทับ`** (corpus-verified at JDG 6:34 `ทรงสวมทับกิดเอน`). The shipped Thai reads **`พระวิญญาณของพระเจ้าสวมทับเศคาริยาห์`** — the divine-name half is correct (רוּחַ אֱלֹהִים → `พระวิญญาณของพระเจ้า`), but `ทรง` is dropped, with no key_decision justifying the deviation.
  - **§12 — 36:9 silently departs from MT on Jehoiachin's age.** MT reads בֶּן־**שְׁמוֹנֶה** שָׁנִים = "**eight** years old"; the shipped Thai reads **`สิบแปดพรรษา` (18)**, following 2 Kings 24:8 / LXX / BSB with **no `notes` and no key_decision**. Under the project's MT-anchored base (`ot_canon_and_text_base_2026-05.md`; `synoptic_parallel_passages_2026-05.md` §1), an emendation away from MT requires a Trigger-1 Layer-2 MT-departure footer — exactly as 2 Sam 15:7 ("forty"→"four") received. Contrast 22:2, where the equally-famous 42/22 crux **preserves** MT and documents it. 36:9 is an undocumented, unflagged MT departure.
- **6 items flagged REVIEW** (worth Ben's confirmation):
  - **§7 DTr evaluation + high-places phrase locks remain Kings-scoped** (`["1KI ","2KI "]`) — **not** extended to 2 Chronicles, the densest DtrH regnal book. The clean phrase-consistency result for the eval/high-places locks reflects out-of-scope, not a passed check; it is the structural reason the §4 "did evil" drift shipped undetected. This is the "single highest-value forward-protection step" the 1CH audit named (the `malak` half was actioned; the DTr half was not).
  - **§3b human-messenger surface** — 2 Chronicles uniformly renders human/prophetic מַלְאָךְ as **`ผู้สื่อสาร`** (18:12, 35:21, 36:15, 36:16), which is the `malak_yhwh_2026-05.md` §4.4 **"avoid"** form (reclassify to `ผู้ส่งสาร`). Adds 2 Chronicles to the standing deferred human-messenger normalization queue (1KI §3b / 2KI §3b / 2KI ผู้สื่อสาร backlog).
  - **§12b synoptic documentation completeness** — beyond the 36:9 DECIDE, two lesser gaps: **4:5** (molten sea holds 3,000 baths vs 1 Kings 7:26's 2,000) carries only a unit-explanation note, no divergence note; and **ch 32** (the Assyrian deliverance) carries **no** Layer-1 cross-reference tying it to 2 Kings 18–19 / Isaiah 36–37 — the most famous three-witness parallel set, named in `synoptic_parallel_passages_2026-05.md` §1/§6.
  - **§10 temple Name-theology** — the שֵׁם "for my name / that my name may be there / called by my name" motif (chs 6–7, ~15 occurrences) is rendered uniformly by translator habit but is **undocumented and unenforced**; recommend writing the long-deferred `name_theology_deuteronomistic_2026-05.md` (1KI §H / 2KI §10).
  - **§14 "until this day" leitwort** — 2 Chronicles uniform `จนถึงทุกวันนี้` (6×: 5:9, 8:8, 10:19, 20:26, 21:10, 35:25); **JDG + 1KI + 2KI + 1CH + 2CH now all agree**, leaving **1 Samuel the lone corpus outlier** (`จนถึงวันนี้`). Sharpens the standing 1KI §14 / 2KI §11 / 1CH §13 normalization case to a 5-of-6 majority.
  - **§16 end-of-book intertextual notes** — three optional Layer-1/Layer-2 cross-reference opportunities are unmarked: 33:18–19 (the deuterocanonical *Prayer of Manasseh* connection), 36:21 (the Jeremiah-70-years / Lev 26 land-sabbaths intertext), and 36:22–23 (the Cyrus decree ≈ Ezra 1:1–3 verbatim duplication + the Hebrew-canon terminus). Low severity; polish, not gaps.
- **One new corpus doc recommended:** `name_theology_deuteronomistic_2026-05.md` (§10). The §6 death-formula succession-clause variance (`ขึ้นครองราชย์แทน` vs the Kings-era lock's `…แทนพระองค์`) is a minor existing-doc note, not a new doc.
- **External AI review (§3) pending.** Suggested 6-item packet (the three DECIDE items + DTr lock-scope §7; human-messenger surface §3b; "until this day" §14).

Status codes: **LOCKED** — stable + corpus-doc exists in `docs/translator_decisions/`. **STABLE** — uniform/principled + rationale at verse level (no corpus doc). **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה compliance — **LOCKED**

YHWH renders as `องค์พระผู้เป็นเจ้า` throughout. **383 surface occurrences** of `องค์พระผู้เป็นเจ้า` in `thai` verse-text across the 36 chapters — the highest YHWH-density of any Chronicler book (2 Chronicles is dominated by temple-worship and prophetic-confrontation narrative, unlike the genealogy-heavy 1 Chronicles).

**ยาห์เวห์ residues in verse text: zero.** No `ยาห์เวห์` surface in any 2 Chronicles `thai` field. (The only sanctioned `ยาห์เวห์` survival per `divine_names_table_2026-05.md` — place-name memorial compounds — does not occur in 2 Chronicles.)

**Per-chapter first-occurrence YHWH footnote.** All **36/36** chapters carry the locked Tier-2 explanation in `output/textual_variants/2chronicles_NN.json` (`type: tetragrammaton_convention_first_occurrence`). Unlike 1 Chronicles (six YHWH-absent genealogy chapters with no footnote owed), every 2 Chronicles chapter contains YHWH, so all 36 carry the footnote. Spot-checked and clean.

**LOCKED** ✓ per `divine_names_table_2026-05.md`.

---

## 2. Elohim + Adonai divine names — **LOCKED (the 1KI §8 Adonai-compound DECIDE does NOT recur)**

- **Elohim → พระเจ้า** uniform across 2 Chronicles ✓. No drift.
- **Only one אֲדֹנָי occurs in all of 2 Chronicles** (Hebrew-grep across all 822 verses): **13:6**, וַיִּמְרֹד עַל־אֲדֹנָיו ("Jeroboam rebelled against **his lord**" [Solomon]) — a **human** master, not the divine title. So 2 Chronicles, like 1 Chronicles, adds no divine-Adonai datapoint.
- **The Solomon temple-dedication prayer (ch 6 = 1 Kings 8) uses plain יְהוָה where 1 Kings 8 used אֲדֹנָי יְהוִה.** The Chronicler's version contains **no אֲדֹנָי compound** — exactly the pattern 1 Chr 17 showed against 2 Sam 7. The 1 Kings 8:53 sentence-final-vocative DECIDE (1KI §8) therefore **does not recur**: there is no compound to position. The prayer's direct-address vocatives all ship the standard plain-YHWH form `ข้าแต่องค์พระผู้เป็นเจ้า…` (6:14, 6:16, 6:17 יְהוָה אֱלֹהֵי יִשְׂרָאֵל → `ข้าแต่องค์พระผู้เป็นเจ้าพระเจ้าแห่งอิสราเอล`; 6:40 אֱלֹהַי → `ข้าแต่พระเจ้าของข้าพระองค์`; 6:41–42 יְהוָה אֱלֹהִים → `ข้าแต่องค์พระผู้เป็นเจ้าพระเจ้า`). Where 1 Kings 8 closes with the Exodus-plea coda, Chronicles substitutes the Psalm 132 quotation (6:41–42) — neither carries Adonai.

**LOCKED** ✓.

---

## 3. mal'akh-YHWH — **LOCKED (the 1CH §3 REVIEW is RESOLVED: lock now machine-enforced for 2CH)**

2 Chronicles has **one** divine-מַלְאָךְ occurrence, **32:21** — the angel who destroyed the Assyrian camp under Sennacherib (= 2 Kings 19:35; the synoptic twin shipped under enforcement at the 2 Kings ship). The Hebrew is **anarthrous standalone** מַלְאָךְ (וַיִּשְׁלַח יְהוָה מַלְאָךְ "YHWH sent an angel", not the construct מַלְאַךְ יְהוָה):

| Ref | Hebrew | 2CH Thai (shipped) | Status |
|---|---|---|---|
| **32:21** | וַיִּשְׁלַח יְהוָה מַלְאָךְ ("YHWH sent an angel") | **`องค์พระผู้เป็นเจ้าก็ทรงส่งทูตสวรรค์องค์หนึ่งมาทำลาย…`** | ✓ |

The surface is bare **`ทูตสวรรค์`** + classifier `องค์หนึ่ง` ("an / one"), with **no** genitive compound — exactly what `malak_yhwh_2026-05.md` §4.1 prescribes for standalone מַלְאָךְ ("use ทูตสวรรค์ without qualifier — narrative context makes the divine source clear"). It matches the 2 Kings 19:35 rendering.

**The 1 Chronicles audit's headline REVIEW is now closed for 2 Chronicles.** The `malak` phrase-lock scope was widened 2026-05-26 to `["1KI ","2KI ","1CH ","2CH "]` (per the 1CH external review; ChatGPT + Gemini both CONCERN on "passed by convention, not enforcement"). So 2 Chronicles ships the divine-angel lock **inside** machine scope — a step up from both 1 Chronicles (held by convention) and the 1 Kings 19:7 drift. (Mechanical nuance: the lock keys on `מלאך`+divine-name patterns; 32:21's word order is YHWH→מַלְאָךְ, so the *anarthrous* form is not pattern-matched and passes by being correct, while any future *compound* מַלְאַךְ יְהוָה in 2CH would be hard-caught. The standalone surface is verified manually-clean here.)

**LOCKED** ✓ per `malak_yhwh_2026-05.md`.

---

## 3b. mal'akh human-messenger surface — **REVIEW (the §4.4 "avoid" form recurs)**

Per `malak_yhwh_2026-05.md` §4.4, human-messenger מַלְאָךְ is outside the divine lock, with a locked **hierarchy**: default `ผู้ส่งสาร`; `ทูต`/`คณะทูต` for diplomatic; **avoid `ผู้สื่อสาร`/`ผู้ส่งข่าว` (reclassify)**. 2 Chronicles renders **every** human/prophetic messenger as **`ผู้สื่อสาร`** — the explicit avoid-form:

| Ref | Hebrew | 2CH Thai | Sense |
|---|---|---|---|
| 18:12 | הַמַּלְאָךְ (the envoy summoning Micaiah) | `ผู้สื่อสาร` | court runner |
| 35:21 | מַלְאָכִים (Neco's envoys to Josiah) | `ผู้สื่อสาร` | royal envoy |
| 36:15 | בְּיַד מַלְאָכָיו (YHWH's messengers = the prophets) | `ผู้สื่อสาร` | prophet-as-messenger |
| 36:16 | מַלְאֲכֵי הָאֱלֹהִים (the messengers of God = prophets) | `ผู้สื่อสารของพระเจ้า` | prophet-as-messenger |

The lemma-thread holds where it matters most — the divine angel (`ทูตสวรรค์`, §3) and the prophets-as-messengers (`ผู้สื่อสาร`/`ผู้เผยพระวจนะ`) are cleanly separated, so **`ทูตสวรรค์` never leaks into 36:15–16** (verified). But 2 Chronicles uses the §4.4 avoid-form uniformly rather than the `ผู้ส่งสาร` default. This is the same standing cross-book normalization the 1KI §3b / 2KI §3b flags opened (the 2 Kings `ผู้สื่อสาร` backlog: 5:10, 6:32–33, 9:18, 10:8, 14:8, 19:9, 19:14).

**REVIEW.** Folds into the deferred human-messenger normalization pass (§3 of `malak_yhwh_2026-05.md`). 36:15–16 are prophet-as-messenger (arguably licensing a distinct surface — `ผู้สื่อสาร` reads naturally there); 18:12/35:21 are the ordinary-messenger/royal-envoy cases that the hierarchy would route to `ผู้ส่งสาร`/`ทูต`. **Severity: LOW** (MT-faithful either way; not a tag blocker).

---

## 4. DTr Formula 2 — Evaluation ("did right / did evil") — **LOCKED (did-right) + DECIDE (did-evil drift, 6 kings)**

`dtr_history_cycle_formulas_2026-05.md` Formula 2 locks **did-right → `ทำสิ่งที่ถูกต้องในสายพระเนตรขององค์พระผู้เป็นเจ้า`** and **did-evil → `ทำสิ่งชั่วร้ายในสายพระเนตรขององค์พระผู้เป็นเจ้า` (with `ร้าย`)**.

**Did-right — clean.** All eight good/mixed kings ship the locked surface (or a faithful Hebrew-tracking variant): Asa 14:1 (`ดีและถูกต้อง`, Heb הַטּוֹב וְהַיָּשָׁר), Jehoshaphat 20:32, Joash 24:2, Amaziah 25:2, Uzziah 26:4, Jotham 27:2, Hezekiah 29:2, Josiah 34:2 — all `ทำสิ่งที่ถูกต้องในสายพระเนตร…`. Ahaz 28:1 correctly negates it (`ไม่ได้ทรงทำสิ่งที่ถูกต้อง…`, Heb לֹא הַיָּשָׁר). Hezekiah's summary 31:20 uses a three-fold Hebrew form (`ดี ถูกต้อง และสัตย์ซื่อ`, Heb הַטּוֹב וְהַיָּשָׁר וְהָאֱמֶת) — faithful, not the standard formula. ✓

**Did-evil — a clean split, with a six-verse drift in the late kings:**

| Ref | King | Thai eval clause | Lock? |
|---|---|---|---|
| **21:6** | Jehoram | `ทรงทำสิ่งชั่วร้ายในสายพระเนตร…` | ✓ (+ key_decision cites lock) |
| **22:4** | Ahaziah | `ทรงทำสิ่งชั่วร้ายในสายพระเนตร…` | ✓ (+ key_decision cites lock) |
| **33:2** | Manasseh | `ทรงทำชั่วในสายพระเนตร…` | ✗ bare `ทำชั่ว`, no key_decision |
| **33:6** | Manasseh | `ทรงทำชั่วมากมายในสายพระเนตร…` | ✗ bare `ทำชั่ว` |
| **33:22** | Amon | `ทรงทำชั่วในสายพระเนตร…` | ✗ bare `ทำชั่ว` |
| **36:5** | Jehoiakim | `ทรงทำชั่วในสายพระเนตร…` | ✗ bare `ทำชั่ว` |
| **36:9** | Jehoiachin | `ทรงทำชั่วในสายพระเนตร…` | ✗ bare `ทำชั่ว` |
| **36:12** | Zedekiah | `ทรงทำชั่วในสายพระเนตร…` | ✗ bare `ทำชั่ว` |

(Also non-regnal: 29:6 "our fathers did evil" → bare `ทำชั่ว`, in Hezekiah's reform speech — outside the regnal formula but the same surface.)

The split is exact: the **two early apostates carry an explicit key_decision and ship the locked `ทำสิ่งชั่วร้าย`**; the **six late apostates carry no key_decision and ship bare `ทำชั่ว`**. This is the identical surface defect the 1 Kings EOB normalized at 22:53 (`ชั่ว`→`ชั่วร้าย` to match the seven compliant 1 Kings usages), here recurring across six verses. The Hebrew is the same idiom in every case (וַיַּעַשׂ הָרַע בְּעֵינֵי יְהוָה).

**DECIDE.** The audit cannot change translations. Recommend normalizing the six (and 29:6) to **`ทำสิ่งชั่วร้าย`** before tagging `book-2chronicles-v1`, restoring the lock's `ร้าย`. The reason it shipped is structural (§7): the DTr evaluation lock is scoped `["1KI ","2KI "]` and never machine-checked 2 Chronicles. **Severity: MEDIUM** (six framing verses against a LOCKED surface; thin-but-not-wrong; the fix is mechanical once authorized).

---

## 5. DTr Formula 3 — High-places notice — **LOCKED (a coherent two-surface system)**

`dtr_history_cycle_formulas_2026-05.md` Formula 3 locks the **summary notice** "the high places were not removed" → **`สถานบูชาบนที่สูงยังไม่ถูกกำจัด`** (noun `สถานบูชาบนที่สูง` + verb `กำจัด`). 2 Chronicles uses the locked noun **exactly and only** at the three theological-notice/build verses, and a distinct narrative idiom for active removal:

- **Summary "not removed" notices → locked surface.** 15:17 (Asa) + 20:33 (Jehoshaphat) both ship `สถานบูชาบนที่สูงยังไม่ถูกกำจัด` — noun + `กำจัด`, matching the lock to the letter.
- **Built/legitimized → locked noun, no `กำจัด`.** 21:11 (Jehoram **builds** high places) ships `ทรงสร้างสถานบูชาบนที่สูง` — the locked noun, correctly without the removal verb.
- **Active removal narratives → separate idiom.** Asa (14:2/14:4 `รื้อ…สถานสูง`), Jehoshaphat (17:6 `รื้อ`), Hezekiah (31:1 `รื้อ…ทำลายเสียสิ้น`), Josiah (34:3 `ชำระ…ให้พ้นจาก`) use narrative verbs (`รื้อ`/`ชำระ`) with plain `สถานสูง`. Other cult-context mentions (Solomon at Gibeon 1:3/1:13, Jeroboam's cult 11:15, Ahaz 28:4/28:25, Manasseh's rebuild 33:3/33:19, the people-still-sacrifice tension 33:17) use plain `สถานสูง`.

This is internally coherent and preserves the Chronicler's reform-tension (kings who *removed* shrines vs the framing notice that they *were not removed*) — the same two-surface pattern accepted in Kings. The locked noun appears only where the lock scopes it.

**LOCKED** ✓ (but the lock is Kings-scoped and not machine-checked for 2CH — see §7).

---

## 6. DTr Formula 5 — Death / burial / succession — **LOCKED (kingdom-keyed `ทรง` holds, even for apostates; the anticipated §2.2 tension resolves cleanly)**

`dtr_history_cycle_formulas_2026-05.md` Formula 5 sets a **dynastic-legitimacy register split**: Davidic/Judahite line → royal `ทรงล่วงหลับไปอยู่กับบรรพบุรุษ…ขึ้นครองราชย์แทนพระองค์`; Northern line → plain. The split is **keyed by kingdom**, and the doc states the death-honorific is the legitimate-line marker — *not* gated by the king's morality. 2 Chronicles is the decisive stress-test, because it is **all-Judahite** yet contains kings with explicitly **dishonorable deaths/burials**, where the §2.2 theological downshift (which denies `ทรง` to apostate kings' *shameful acts*) could in principle pull against the kingdom-key.

**The death-honorific is applied uniformly to every Davidic king, apostate or not — with zero §2.2 leakage into the death verb:**

| King | Death verb (Thai) | Royal register | Burial-dishonor preserved? |
|---|---|---|---|
| Solomon 9:31, Rehoboam 12:16, Abijah 13:23, Asa 16:13, Jehoshaphat 21:1, Jotham 27:9, Hezekiah 32:33 | `ทรงล่วงหลับ…` / `สิ้นพระชนม์` | YES | — (honored) |
| **Jehoram 21:19–20** (apostate) | `สิ้นพระชนม์…โดยไม่มีใครอาลัย` | YES | YES — `ฝัง…แต่ไม่ใช่ในอุโมงค์ของบรรดากษัตริย์` |
| **Joash 24:25** (apostate, murdered) | `ปลงพระชนม์…สิ้นพระชนม์…พระศพ` | YES | YES — `ไม่ได้ฝังไว้ในอุโมงค์ของบรรดากษัตริย์` |
| **Amaziah 25:27–28** (apostate, hunted) | `เสด็จหนี…พระศพ…ฝัง` | YES | mild |
| **Uzziah 26:23** (leper) | `ทรงล่วงหลับ…` | YES | YES — `ฝัง…ในทุ่งฝังศพ…เพราะทรงเป็นโรคเรื้อน` |
| **Ahaz 28:27** (apostate) | `ทรงล่วงหลับไปอยู่กับบรรพบุรุษ` | YES | YES — `ไม่ได้นำ…เข้าไปไว้ในอุโมงค์ของบรรดากษัตริย์แห่งอิสราเอล` |
| **Manasseh 33:20** (apostate-then-penitent) | `ทรงล่วงหลับ…` | YES | mild — buried in his own palace |
| **Amon 33:24–25** (assassinated) | `ปลงพระชนม์พระองค์ในวัง` | YES | — |
| **Josiah 35:24** (killed in battle) | `สิ้นพระชนม์…อุโมงค์ของบรรพบุรุษ` | YES | — (mourned) |
| ch 36 last four (deposed/exiled) | no death formula — `ถอด`, `ล่ามด้วยโซ่`, `นำมายังบาบิโลน` | royal `ทรง`/`พระองค์` | n/a |

In every dishonor case the **moral judgment is carried lexically** (not-in-kings'-tombs, no honoring fire, leper-field, no-regret), while the **death verb keeps the royal register**. This is exactly the kingdom-keyed behavior the lock specifies — and it resolves the question the audit anticipated: in 2 Chronicles the death formula is kingdom-keyed, the §2.2 downshift governs the apostates' *shameful acts* (idol-building, child-sacrifice — narrated without `ทรง`-elevation), and the two systems do not collide.

**LOCKED** ✓.

**Minor REVIEW (succession clause).** All 12 succession notices end on `…ราชโอรส…ก็ขึ้นครองราชย์แทน` (plain `แทน`), not the Kings-era lock's literal `…แทนพระองค์`. It is **uniform across 2 Chronicles** (9:31, 12:16, 13:23, 17:1, 21:1, 24:27, 26:23, 27:9, 28:27, 32:33, 33:20, 36:8) — a consistent corpus choice, not drift. Worth a one-line note in `dtr_history_cycle_formulas_2026-05.md` recording that the Chronicler's succession surface drops the resumptive pronoun, before the death-formula lock is widened to 2CH (§7). **Severity: LOW.**

---

## 7. DTr formula enforcement scope — **REVIEW (the load-bearing gap; the §4 drift's root cause)**

The `check_phrase_consistency.py` DTr locks — evaluation `ชั่วร้าย`, evaluation `ถูกต้อง`, high-places `สถานบูชาบนที่สูง` — are all scoped **`"books": ["1KI ", "2KI "]`**. **2 Chronicles is outside all three.** The clean phrase-consistency result for these locks therefore reflects 2CH being out of scope, **not** a passed check — every DTr-formula compliance finding in §4/§5/§6 is a *manual* finding.

This is precisely the gap the 1 Chronicles audit named as **"the single highest-value forward-protection step … widening the `malak` (and DTr-formula) phrase-locks beyond `['1KI ','2KI ']` before 2 Chronicles."** The `malak` half was actioned 2026-05-26 (§3). **The DTr-formula half was not** — and 2 Chronicles, the densest DtrH regnal book in the corpus, shipped its full ~20-king cycle with the evaluation/high-places locks blind to it. The direct consequence is the §4 "did evil" drift (six bare-`ทำชั่ว` verses), which a 2CH-scoped evaluation lock would have hard-caught.

**REVIEW — recommended:** widen the three DTr-formula locks' scope to include `"2CH "` (and add the death-formula register split as a fourth lock keyed by kingdom, per the doc's own Enforcement section). Run it; it will flag the six §4 verses. Once those are normalized (the §4 DECIDE), the locks pass in-scope and the corpus is forward-protected for the Prophets (where the same formulas recur). **Severity: MEDIUM** (no surface edit in this item itself; it is the enforcement that gates §4). Not in itself a tag blocker, but it is the mechanism that should accompany the §4 fix.

---

## 8. Spirit-of-God / Spirit-of-YHWH empowerment — **LOCKED (הָיָה עַל class) + DECIDE (24:20 לָבַשׁ-class missing `ทรง`)**

`spirit_of_yhwh_empowerment_2026-05.md` locks a 4-way verb split. 2 Chronicles triggers two of the four classes:

| Ref | Agent | Hebrew verb | Class | 2CH Thai | Status |
|---|---|---|---|---|---|
| **15:1** | Azariah b. Oded | הָיְתָה עָלָיו רוּחַ אֱלֹהִים | הָיָה עַל | `พระวิญญาณของพระเจ้าเสด็จมาเหนืออาซาริยาห์…` | ✓ |
| **20:14** | Jahaziel | הָיְתָה עָלָיו רוּחַ יְהוָה | הָיָה עַל | `แล้วพระวิญญาณขององค์พระผู้เป็นเจ้าเสด็จมาเหนือยาฮาซีเอล…` | ✓ |
| **24:20** | Zechariah b. Jehoiada | רוּחַ אֱלֹהִים **לָבְשָׁה** | **לָבַשׁ** | `แล้วพระวิญญาณของพระเจ้า**สวมทับ**เศคาริยาห์…` | **✗ missing `ทรง`** |

The two הָיָה עַל occurrences are clean: `…เสด็จมาเหนือ` with the correct divine-name halves (Elohim→`พระเจ้า` at 15:1; YHWH→`องค์พระผู้เป็นเจ้า` at 20:14). No פָּעַם or צָלַח occurrences in 2 Chronicles. Non-empowerment רוּחַ correctly falls outside the lock (18:22 lying spirit `วิญญาณมุสา`; 21:16 YHWH stirred the Philistines/Arabs `ทรงเร้าใจ`; 36:22 stirred Cyrus' spirit `จิตใจ` — §16).

**24:20 is the DECIDE.** The lock doc **explicitly names "2 Chr 24:20 (forward-protect)"** as the downstream anchor of the לָבַשׁ ("clothed") class and locks the surface as **`ทรงสวมทับ`** — corpus-verified at JDG 6:34 (`พระวิญญาณขององค์พระผู้เป็นเจ้าก็ทรงสวมทับกิดเอน`) and validated as the first downstream ship at 1 Chr 12:18 (`พระวิญญาณก็เสด็จมาสวมทับอามาสัย`, 1CH §4). The shipped 2 Chr 24:20 reads `พระวิญญาณของพระเจ้า**สวมทับ**เศคาริยาห์` — the divine-name half is correct, but the locked honorific **`ทรง`** is dropped, with no key_decision justifying the deviation. Because the Spirit is the divine subject, the royal verb-honorific is owed (as at JDG 6:34 / 1 Chr 12:18).

**DECIDE.** Recommend adding `ทรง` → `…ทรงสวมทับเศคาริยาห์` before tagging, restoring the named לָבַשׁ-class anchor to the lock surface. **Severity: LOW–MEDIUM** (one verse, one particle, but it is *the* verse the lock forward-protected by name).

---

## 9. חֶסֶד covenant-love — **LOCKED**

חֶסֶד renders within the `chesed_covenant_love_2026-05.md` family. The liturgical refrain כִּי לְעוֹלָם חַסְדּוֹ ("for his steadfast love endures forever") — which the 1CH §8 forward-watch flagged as recurring in 2 Chronicles — ships uniformly:

| Ref | Context | 2CH Thai |
|---|---|---|
| **5:13** | ark enters the temple, the cloud fills it | `ความรักมั่นคงของพระองค์ดำรงเป็นนิตย์` |
| **7:3** | fire falls, the people worship | `ความรักมั่นคงของพระองค์ดำรงเป็นนิตย์` |
| **7:6** | Levites with David's instruments | `ความรักมั่นคงของพระองค์ดำรงเป็นนิตย์` |
| **20:21** | Jehoshaphat's singers march before the army (worship-as-warfare) | `ความรักมั่นคงของพระองค์ดำรงเป็นนิตย์` |

Other divine-חֶסֶד occurrences uniform (`ความรักมั่นคง`): 1:8, 6:14 (covenant + chesed), 6:42 (the chesed promised to David). Two correctly-handled non-violations: 24:22 **human** חֶסֶด (Jehoiada's kindness to Joash) → `ความกรุณา` per the doc's human/divine split; 30:9 renders רַחוּם/רַחֲמִים (mercy, not chesed) → `ความเมตตา`, out of scope. No חֶסֶד rendered as anything other than the locked form.

**LOCKED** ✓.

---

## 10. Temple Name-theology (שֵׁם, chs 6–7) — **STABLE → recommend `name_theology_deuteronomistic_2026-05.md`**

Solomon's dedication (chs 6–7 = 1 Kings 8) is the corpus's densest **Name-theology** passage — the שֵׁם "name" motif recurs ~15× as the theological spine of Deuteronomistic temple ideology (shared with Deut 12 and forward into Jeremiah / Ezekiel). The shipped Thai is **uniform by translator habit**, built on a small, coherent surface-set:

- *"that my name may be there"* (לִהְיוֹת שְׁמִי שָׁם): 6:5 `ให้นามของเราอยู่ที่นั่น`, 6:6, 7:16; 6:20 (לָשׂוּם שִׁמְךָ) `ให้นามของพระองค์อยู่ที่นั่น`.
- *"a house for my/your name"* (לְשֵׁם / לִשְׁמִי): 6:7–10, 6:34, 6:38, 7:20 → `เพื่อนามของเรา` / `เพื่อพระนามของพระองค์`.
- *"called by my name"* (נִקְרָא…שֵׁם…עַל): 6:33 `เรียกตามพระนามของพระองค์`; 7:14 (עַמִּי אֲשֶׁר נִקְרָא־שְׁמִי) `ประชากร…ผู้ซึ่งเขาเรียกตามนามของเรา` — **the one verse with a שֵׁם-specific key_decision**.

The motif is rendered consistently, but **only 7:14 documents the idiom**; the rest carry the boilerplate YHWH→องค์พระผู้เป็นเจ้า decision. There is **no `name_theology_deuteronomistic` doc** in `docs/translator_decisions/` — the 1KI §H / 2KI §10 recommendation has not been actioned, and 2 Chronicles is exactly the book those audits said it "belongs to." A minor cosmetic note: the พระ- honorific on "name" varies (`นามของเรา` in 1st-person YHWH-speech vs `พระนามของพระองค์` in 2nd/3rd-person) — it tracks divine person but is not stated as a rule.

**STABLE — recommend writing `name_theology_deuteronomistic_2026-05.md`** capturing: (a) the שֵׁม surface-set above; (b) the พระ-/person rule (or a decision to normalize); (c) the forward-cover (Deut 12 retrofit + Jeremiah/Ezekiel). The motif is handled correctly now but is unenforced and undocumented — the canonical end-of-book "lock it before it compounds" case. **Severity: LOW** (no surface defect; documentation/forward-protection).

---

## 11. Large numbers, weights, units, transliteration — **STABLE**

2 Chronicles carries heavy temple-fund and tribute numerics; units render uniformly within established corpus forms (`ตะลันต์` talent, `เชเขล` shekel, `บัท` bath, `คอร์` cor). Proper-name transliteration across ~20 reigns + the prophets (อาสา, เยโฮชาฟัท, อุสซียาห์, มนัสเสห์, เซนนาเคอริบ, ไซรัส, etc.) is decisive at the mechanical gate: `check_key_term_consistency.py` is clean (0 rule violations, 0 undocumented multi-renderings) across the 668-chapter corpus, which includes 2 Chronicles. The Kings↔Chronicles **number divergences** are the §12 item; the **unit renderings** are uniform.

**STABLE** ✓.

---

## 12. Synoptic Kings↔Chronicles divergences — **LOCKED (independent MT; prominent cases noted) + DECIDE (36:9) + REVIEW (12b)**

2 Chronicles is the densest synoptic field in the OT. `synoptic_parallel_passages_2026-05.md` §1 locks independent-MT translation (each book from its own MT, not harmonized), and §5.1 sets the **2 Chronicles threshold**: document name/agent/substantial-number divergences that are *famous, apologetically prominent, or reader-confusing vs Kings* — not every minor variant. The prominent cases comply:

| Ref | 2CH (MT) | Kings parallel | Divergence noted? |
|---|---|---|---|
| 8:18 | 450 talents gold | 1 Kgs 9:28 = 420 | ✓ Layer-1 key_decision |
| 9:25 | 4,000 stalls | 1 Kgs 4:26 = 40,000 | ✓ Layer-1 key_decision |
| **22:2** | **42 years** (Ahaziah's age) | 2 Kgs 8:26 = 22 | ✓ Layer-1 (fullest — flags chronological impossibility, **preserves MT**, cites LXX/Syriac) |
| 3:4 | 120 cubits (porch height) | LXX/Syriac/BSB = 20 | ✓ both `notes` + key_decision (preserves MT, records variant) |

**36:9 is the DECIDE — an undocumented MT departure.** MT reads בֶּן־**שְׁמוֹנֶה** שָׁנִים = "**8** years old"; the shipped Thai reads **`สิบแปดพรรษา` (18)**, silently following 2 Kings 24:8 / LXX / BSB — with **no `notes`, no key_decision**. This is the one place 2 Chronicles **emends away from MT** without disclosure. Under `ot_canon_and_text_base_2026-05.md` + `synoptic_parallel_passages_2026-05.md` §1/§4, an emendation requires a **Trigger-1 Layer-2 MT-departure footer** (the treatment 2 Sam 15:7 "forty"→"four" received). The contrast with 22:2 — the equally-famous 42/22 crux, where MT is *preserved* and documented — makes 36:9 internally inconsistent with the book's own handling. **DECIDE:** either (a) restore MT "8" + a synoptic-variant footer, or (b) keep "18" + a Trigger-1 MT-departure footer. **Severity: MEDIUM.**

**12b — REVIEW (two lesser documentation gaps).** (i) **4:5** (molten sea 3,000 baths vs 1 Kgs 7:26's 2,000) is a well-known Kings↔Chronicles divergence that arguably meets the §5.1 "reader-confusing" threshold but carries only a bath-unit explanation, no divergence note. (ii) **Ch 32** (the Assyrian deliverance) carries **no** Layer-1 cross-reference to 2 Kgs 18–19 / Isa 36–37 — the most famous three-witness parallel set, named in `synoptic_parallel_passages_2026-05.md` §1/§6/§"Forward application". No individual ch-32 divergence rises to DECIDE, but the total absence of a synoptic anchor on this passage is a documentation gap. Note: no Layer-2 synoptic footers exist anywhere in 2 Chronicles (all 36 `textual_variants` files are YHWH-footnote-only) — consistent with the MT-faithful-Layer-1 policy, *except* where an actual MT departure (36:9) would mandate one. **Severity: LOW–MEDIUM.**

**LOCKED** (independent-MT principle + prominent divergences documented) with the **36:9 DECIDE** and **12b REVIEW**.

---

## 13. Pagan deities / idolatry / child sacrifice — **LOCKED**

2 Chronicles is the corpus's richest apostasy field (Baal cult under Athaliah/Ahaz/Manasseh, Asherah, the host of heaven, the gods of conquered/conquering nations, Molech-style child sacrifice). Every pagan-deity / idol surface takes the **`พระ`** polytheistic register, **never `พระเจ้า`** (`pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md`):

- **Baal**: `พระบาอัล(ทั้งหลาย)` (17:3, 23:17 temple+priests, 24:7, 28:2, 33:3, 34:4).
- **Asherah**: image `เทพีอาเชราห์` (15:16, Maacah's idol); poles `เสาอาเชราห์` (14:2, 17:6, 19:3, 24:18, 31:1, 33:3/19, 34:3/4/7).
- **"gods of" the nations**: all `พระ` — `พระของชาวเสอีร์`/`พระของเอโดม` (25:14, 25:20), `พระของชาวดามัสกัส` (28:23), `พระของบรรดาประชาชาติ` (32:13–19). In ch 32 the Sennacherib speeches correctly contrast pagan `พระของ…` against `พระเจ้าแห่งเยรูซาเล็ม` (= YHWH) — register marks the difference, no violation.
- **Host of heaven**: `บริวารแห่งฟ้าสวรรค์` (33:3, 33:5).
- **Child sacrifice**: 28:3 (Ahaz) `ทรงเผาบุตรชายของพระองค์ในไฟ` in `หุบเขาเบนฮินโนม`; 33:6 (Manasseh) `ทรงเผาบุตรชายของพระองค์เป็นเครื่องบูชาในหุบเขาเบนฮินโนม` — explicit, no euphemism; the Valley transliterated `หุบเขาเบนฮินโนม`. Manasseh's full occult list (33:6 divination/omens/sorcery/mediums/spiritists) renders completely.

**Zero `พระเจ้า`-for-pagan violations** in 2 Chronicles.

**LOCKED** ✓.

---

## 14. "until this day" leitwort — **REVIEW (cross-book; 2CH joins the majority, 1SA still the lone outlier)**

2 Chronicles renders עַד הַיּוֹם הַזֶּה uniformly **`จนถึงทุกวันนี้`** (with the `ทุก-` intensifier) at all six occurrences — 5:9, 8:8, 10:19, 20:26, 21:10, 35:25. (Two bare `วันนี้` hits at 6:15 + 35:21 are ordinary "today" deictics, not the etiological leitwort.)

**Cross-book corpus picture now (six DtrH/Chronicler books):**
| Book | Surface | Count |
|---|---|---|
| Judges | `จนถึงทุกวันนี้` | 6× (+1 drift) |
| **1 Samuel** | **`จนถึงวันนี้`** (bare) | **8× uniform** |
| 1 Kings | `จนถึงทุกวันนี้` | 5× |
| 2 Kings | `จนถึงทุกวันนี้` | 10× |
| 1 Chronicles | `จนถึงทุกวันนี้` | 2× |
| **2 Chronicles** | **`จนถึงทุกวันนี้`** | **6×** |

**Five of six books now agree on `จนถึงทุกวันนี้`; 1 Samuel is the lone outlier.** This is the strongest the standing 1KI §14 / 2KI §11 / 1CH §13 case has been.

**REVIEW.** Internal 2CH uniformity ✓; the cross-book decision (lock `จนถึงทุกวันนี้`; normalize 1SA's 8 occurrences) should land in `leitwort_handling_policy_2026-05.md`. **Severity: LOW.**

---

## 15. MT/LXX textual-variant disposition — **LOCKED (§2.3 floor → non-gap)**

All 36 `output/textual_variants/2chronicles_NN.json` files contain **only** the per-chapter YHWH first-occurrence footnote — **zero** inclusion-variant / MT-vs-LXX entries (the same surface as 1SA §17, 1KI §17, 2KI §15, 1CH §16). The disposition is settled doctrine:

- `mt_vs_lxx_textual_variant_handling_2026-05.md` **§2.3 disclosure-threshold floor** establishes that a book with zero non-YHWH `textual_variant` entries is **COMPLIANT** when its MT/LXX divergences fall below the macro-structural / canonically-visible / materially-reader-affecting floor.
- **2 Chronicles sits below that floor.** Its LXX (Paraleipomena B) is textually close to MT — no macro-structural divergence (no 3-Reigns-style reordering, no Miscellanies, no alternate-narrative blocks), the same milder case 1 Chronicles documented.
- **2 Chronicles' real textual layer is the Kings↔Chronicles synoptic divergence — a different doc** (§12), handled at Layer-1 verse notes under `synoptic_parallel_passages_2026-05.md`. The two systems partition cleanly. The one exception that *does* cross into Layer-2 territory is 36:9 (§12 DECIDE) — an MT departure, not an LXX-disclosure question.

`audit_inclusion_variants.py --book 2chronicles --strict` = 0 candidates, exit 0.

**LOCKED** ✓ — non-gap. Recommend adding a 2 Chronicles row to `mt_vs_lxx_textual_variant_handling_2026-05.md` §3 ("Paraleipomena ≈ MT, no macro-structural divergence → §2.3 floor; non-gap"), mirroring the 1 Chronicles / 2 Kings rows.

---

## 16. End-of-book intertextual notes (chs 33–36) — **REVIEW (optional cross-reference polish) + STABLE (renderings clean)**

The renderings in the closing chapters are clean; the gaps are **missing interpretive / cross-reference notes** (all governed by `ot_nt_cross_quotation_thread_2026-05.md`):

- **33:18–19 — the *Prayer of Manasseh*.** Manasseh's repentance arc (33:12–13) and the cited "prayer of Manasseh … in the records of the seers" render fully; the source-records are named in-text (`จดหมายเหตุของบรรดากษัตริย์/ผู้ทำนาย`). No note flags the **deuterocanonical *Prayer of Manasseh*** that this verse spawned. Optional Layer-2.
- **35:21–22 — Neco speaks "from the mouth of God" (מִפִּי אֱלֹהִים).** Rendered `พระโอษฐ์ของพระเจ้า` + אֱלֹהִים → `พระเจ้า` with full honorifics (`ทรงบัญชา`, `ผู้สถิตกับเรา`). This is **correct** — the **narrator** (35:22) affirms Neco genuinely spoke from God (cf. God speaking through Balaam, Cyrus), so the true-God rendering is right, not a violation. An *optional* interpretive note on "a pagan king as God's mouthpiece" could aid readers, but no surface change is warranted. (The 35:21 messengers correctly `ผู้สื่อสาร` — §3b; 35:25 הַקִּינוֹת correctly disambiguated from canonical Lamentations via key_decision.)
- **36:21 — the 70 years / land sabbaths.** Renders cleanly (`จนกว่าแผ่นดินจะได้ชดเชยวันสะบาโต…ครบเจ็ดสิบปี`, `ตรัสผ่านเยเรมีย์`); no cross-reference to Jer 25:11–12 / 29:10 or Lev 26:34–35. Optional Layer-1.
- **36:22–23 — the Cyrus decree (≈ Ezra 1:1–3).** Renders fully; "stirred up the spirit of Cyrus" correctly reads `ทรงเร้าจิตใจ` (disposition, **not** `พระวิญญาณ` — matching the 1 Chr 5:26 pagan-king precedent ✓). No note flags the **verbatim duplication with Ezra 1:1–3** or that 36:23 is the **terminus of the Hebrew canon**. Optional Layer-2 (the synoptic policy's forward-application list will revisit it when Ezra ships).

**REVIEW (optional notes) / STABLE (renderings).** None of these is a surface defect or a tag blocker; they are corpus-completeness polish, lower-priority than the §10 Name-theology doc. **Severity: LOW.**

---

## 17. Inherited corpus locks — all compliant except where flagged

| Doc | 2CH evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1 (YHWH 383 surfaces, 0 ยาห์เวห์, 36/36 footnoted); §2 (Elohim→พระเจ้า; only human Adonai at 13:6). 1KI §8 compound DECIDE does not recur. | **LOCKED** |
| `malak_yhwh_2026-05.md` | §3 — 32:21 standalone divine angel `ทูตสวรรค์องค์หนึ่ง`; **now machine-enforced (scope widened to 2CH 2026-05-26)**. §3b — human messengers `ผู้สื่อสาร` (the §4.4 avoid-form). | **LOCKED / REVIEW-§3b** |
| `dtr_history_cycle_formulas_2026-05.md` | §4 (did-right clean; **did-evil drift, 6 kings → DECIDE**), §5 (high-places two-surface system clean), §6 (death/succession kingdom-keyed `ทรง` holds for apostates), §7 (**locks Kings-scoped, not 2CH → REVIEW**). | **LOCKED-with-§4-DECIDE + §7-REVIEW** |
| `spirit_of_yhwh_empowerment_2026-05.md` | §8 — 15:1 + 20:14 (הָיָה עַל) clean; **24:20 (לָבַשׁ-anchor) ships `สวมทับ` missing `ทรง` → DECIDE**. | **LOCKED-with-§8-DECIDE** |
| `chesed_covenant_love_2026-05.md` | §9 — refrain ความรักมั่นคง ×4 (5:13/7:3/7:6/20:21) + others; human chesed 24:22 → ความกรุณา. | **LOCKED** |
| `synoptic_parallel_passages_2026-05.md` | §12 — independent-MT; prominent divergences noted (8:18/9:25/22:2/3:4); **36:9 undocumented MT departure → DECIDE**; 4:5 + ch-32 cross-ref gaps → REVIEW. | **LOCKED-with-§12-DECIDE/REVIEW** |
| `pagan_deities_2026-04.md` + `ot_polytheistic_register_2026-05.md` | §13 — Baal/Asherah/host-of-heaven/gods-of-nations all `พระ`; child sacrifice explicit; 0 `พระเจ้า`-for-pagan. | **LOCKED** |
| `honorifics_non_divine_authorities_2026-04.md` + `ot_register_policy_2026-05.md` | royal `ทรง` for the Davidic kings throughout; §2.2 downshift on apostates' shameful acts (idol-building, child-sacrifice) without `ทรง`-elevation; death-honorific kingdom-keyed (§6). | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` + `inclusion_variants_absent_verses_2026-04.md` | §15 — §2.3 floor → non-gap (Paraleipomena ≈ MT); inclusion audit 0 candidates. | **LOCKED (non-gap)** |
| `leitwort_handling_policy_2026-05.md` | §14 — internal uniform `จนถึงทุกวันนี้` (6×); cross-book 1SA-outlier decision pending. | **LOCKED-with-§14-REVIEW** |
| `ot_nt_cross_quotation_thread_2026-05.md` | §16 — Cyrus/Ezra, 70-years/Jer/Lev, Prayer-of-Manasseh cross-refs unmarked (optional). | **LOCKED-with-§16-REVIEW** |
| `nicham_divine_relenting_2026-05.md` | divine relenting language (e.g. 12:7, 12:12 YHWH relents toward Rehoboam) compliant. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "eyes of YHWH" idiom `สายพระเนตร` (the evaluation formula, §4) carries no errant `ทรง`-binding (per the doc's `סור` body-part trap). | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | חַי־יְהוָה ("as YHWH lives") does not occur in 2 Chronicles (Hebrew-grep confirmed). | **LOCKED (N/A)** |
| `ot_warfare_ethics_2026-05.md` | the holy-war narratives (13:14–18 Abijah; 14:9–15 Asa/Zerah; 20 Jehoshaphat) narrated without ḥerem-cluster lock surfaces; 20:21 worship-as-warfare uses the chesed refrain (§9). | **LOCKED (N/A)** |

---

## 18. Mechanical (§1) — all green (with the standing infra notes)

- 36/36 chapters: `output/check_reports/2chronicles_NN_review.md` — all six checks "✅ clean" / "Ready to ship" ✓
- 36/36 chapters: `output/back_translations/2chronicles_NN.json` ✓
- 36/36 chapters: `output/translations/2chronicles_NN.json` (822 verses) ✓
- 36/36 chapters: `output/textual_variants/2chronicles_NN.json` (YHWH first-occurrence footnote; every chapter contains YHWH so all 36 are owed — §1, §15)
- `check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** (668-chapter corpus)
- `check_phrase_consistency.py`: **0 violations across 12 audited locks** (20,012 verses). **`malak` lock now includes `2CH ` (widened 2026-05-26).** **Note:** the **DTr evaluation/high-places locks remain `["1KI ","2KI "]`-scoped — 2 Chronicles is out of scope**, so the clean result does not reflect a passed DTr check for 2CH (§4/§5 verified manually; §7 REVIEW recommends widening — and would catch the §4 drift).
- `audit_inclusion_variants.py --book 2chronicles --strict`: **0 candidates, exit 0** (NT-SBLGNT-tuned heuristic; does not catch Kings↔Chronicles synoptic divergence — that is the §12 verse-note layer).
- `export_to_usfm.py --book 2CH`: **N/A** — the script's `BOOKS` table is NT-only; OT USFM export remains the carried-over separate concern noted in every prior OT audit.
- **Book-code registration:** `2CH` was missing from the §3/§4 tooling slug tables (`build_external_review_packet.py` `BOOKS`; `audit_items_to_yaml.py` `BOOK_SLUGS`) — **registered as part of this audit** per the EOB book-code-registration gotcha. (It was already present in `OT_CODES`, so the Hebrew-base packet branch was unaffected.)
- `git status output/`: **clean except `output/check_reports/divine_names.md`** — a transient single-chapter scratch report whose only diff clears a stale 2SA 1:10 warning; report-only, not a 2 Chronicles surface; identical in kind to the 1SA/1KI/2KI/1CH note.
- YHWH `องค์พระผู้เป็นเจ้า` surfaces: **383**. `ยาห์เวห์` residues: **zero**.

**Severity: GREEN.**

---

## 19. Flagged for Ben's attention

### DECIDE (block the `book-2chronicles-v1` tag until resolved)

**A. "did evil" evaluation formula drift — 6 late kings (§4).**
33:2, 33:6 (Manasseh), 33:22 (Amon), 36:5 (Jehoiakim), 36:9 (Jehoiachin), 36:12 (Zedekiah) ship bare `ทำชั่ว` with no key_decision; 21:6 + 22:4 ship the locked `ทำสิ่งชั่วร้าย` with key_decisions. Recurrence of the 1 Kings 22:53 defect, undetected because the DTr eval lock is Kings-scoped (§7). **Recommend normalizing the six (+ 29:6) to `ทำสิ่งชั่วร้าย`** + widening the eval lock to 2CH. **MEDIUM.**

**B. 24:20 לָבַשׁ-class Spirit anchor missing `ทรง` (§8).**
The lock-named forward-protect verse ships `พระวิญญาณของพระเจ้าสวมทับเศคาริยาห์` — should be **`ทรงสวมทับ`** per `spirit_of_yhwh_empowerment_2026-05.md` (cf. JDG 6:34, 1 Chr 12:18). **Recommend adding `ทรง`.** **LOW–MEDIUM.**

**C. 36:9 silent MT departure — Jehoiachin's age (§12).**
MT = "8" (שְׁמוֹנֶה); shipped Thai = "18" (`สิบแปดพรรษา`), following 2 Kings/LXX/BSB with no note. Undocumented emendation away from the MT base; inconsistent with 22:2's documented MT-preservation. **Recommend either (a) restore MT "8" + synoptic-variant footer, or (b) keep "18" + Trigger-1 MT-departure footer.** **MEDIUM.**

### REVIEW (worth Ben's confirmation; not tag blockers)

**D. Widen the DTr-formula phrase-locks to 2CH (§7).** The eval/high-places (and a new death-formula) locks should add `"2CH "` scope — the highest-value forward-protection step the 1CH audit named; the `malak` half is done, the DTr half is not. Gates the §4-A fix. **MEDIUM.**

**E. Human-messenger surface `ผู้สื่อสาร` (§3b).** 2 Chronicles uses the §4.4 avoid-form (18:12, 35:21, 36:15–16); folds into the deferred cross-book normalization toward `ผู้ส่งสาร`/`ทูต`. **LOW.**

**F. Synoptic documentation gaps (§12b).** 4:5 (3,000/2,000 baths) + ch 32 (no 2 Kgs 18–19 / Isa 36–37 cross-ref). Add Layer-1 notes per the §5.1 threshold. **LOW–MEDIUM.**

**G. Temple Name-theology doc (§10).** Write `name_theology_deuteronomistic_2026-05.md` — the long-deferred 1KI §H / 2KI §10 doc; 2 Chronicles is its home. **LOW.**

**H. "until this day" cross-book normalization (§14).** Lock `จนถึงทุกวันนี้`; normalize 1SA's 8 bare occurrences. 5-of-6 majority now. **LOW.**

**I. Optional intertextual / minor notes (§16, §6).** Cyrus≈Ezra 1:1–3 + canon-terminus; 36:21 Jer/Lev 70-years; Prayer-of-Manasseh; the succession-clause `แทน` vs `แทนพระองค์` note. All LOW.

### Existing docs to amend (optional, no tag block)
- **`dtr_history_cycle_formulas_2026-05.md`** — widen lock scope to 2CH (§D); record the Chronicler's `…ขึ้นครองราชย์แทน` succession surface (§6).
- **`spirit_of_yhwh_empowerment_2026-05.md`** — once 24:20 is fixed, record it as the second downstream לָבַשׁ ship (after 1 Chr 12:18).
- **`synoptic_parallel_passages_2026-05.md`** — record 2 Chronicles as the doc's first dense Kings↔Chronicles downstream test; add the 36:9 disposition.
- **`mt_vs_lxx_textual_variant_handling_2026-05.md`** — add the 2 Chronicles §3-table row (Paraleipomena ≈ MT → §2.3 floor; non-gap).
- **`leitwort_handling_policy_2026-05.md`** — lock `จนถึงทุกวันนี้` as canonical (§H).
- **`malak_yhwh_2026-05.md`** — record 2 Chronicles `ผู้สื่อสาร` on the §3 deferred human-messenger queue (§E).

### External AI review (§3 of checklist) — pending
Recommended 6-item packet (see `external_review_items_2CH.md`):
1. **"did evil" eval drift** (§4-A, DECIDE)
2. **24:20 Spirit-clothing `ทรง`** (§8-B, DECIDE)
3. **36:9 MT departure** (§12-C, DECIDE)
4. **DTr lock-scope** (§7-D, REVIEW)
5. **human-messenger `ผู้สื่อสาร`** (§3b-E, REVIEW)
6. **"until this day" cross-book** (§14-H, REVIEW)

Use Grok + ChatGPT + Gemini in parallel per the JHN/GAL/DEU/JOS/JDG/1SA/1KI/2KI/1CH pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 9 items (§1 YHWH, §2 Elohim/Adonai, §3 mal'akh [now enforced], §5 high-places, §6 death/succession, §9 chesed, §12 synoptic [independent-MT principle], §13 pagan deities, §15 MT/LXX [non-gap]; + inherited locks via §17)
- **STABLE:** 3 items (§10 Name-theology [→ recommend doc], §11 numbers/units/names, §16 closing-chapter renderings)
- **REVIEW:** 6 items (§3b human-messenger, §7 DTr lock-scope, §12b synoptic-doc gaps, §10 Name-theology doc, §14 "until this day", §16 intertextual notes; + §6 succession-clause minor)
- **DECIDE:** 3 items (§4 "did evil" drift; §8 24:20 missing `ทรง`; §12 36:9 MT departure)

**Three DECIDE items block the `book-2chronicles-v1` tag** — all three are small, lock-anchored surface fixes the audit cannot make itself. They share a root cause worth noting: the enforcement that would have caught them is either Kings-scoped (the §4 eval lock) or convention-only (the §8 `ทรง`, the §12 MT-departure footer). 2 Chronicles, the densest DtrH/synoptic book, is exactly where convention-only finally slipped.

**One new translator_decisions doc recommended:** `name_theology_deuteronomistic_2026-05.md` (§10). Five optional existing-doc amendments (§19).

---

## Recommendation

**2 Chronicles ships in strong shape, but — unlike the exceptionally clean 1 Chronicles — it surfaces three genuine, fixable defects that should be resolved before v1.** As the conclusion of the Chronicler's History it is the corpus's hardest test to date of three surfaces at once, and the audit finds:

- **The mal'akh-YHWH lock now ships under machine enforcement** (32:21 `ทูตสวรรค์องค์หนึ่ง`), closing the 1 Chronicles headline REVIEW — a real win.
- **The death/burial/succession formula resolves the anticipated tension cleanly** — the kingdom-keyed `ทรง` holds for every Davidic king including the apostates, with moral judgment carried lexically (not by stripping the honorific). The §2.2 downshift and the dynastic-legitimacy split do not collide.
- **Pagan-deity register, chesed, high-places, "until this day", and MT/LXX disposition are all clean/LOCKED.**
- **But three lock-anchored surfaces slipped:** the "did evil" formula drifts to bare `ทำชั่ว` in the six late kings (the 1 Kings 22:53 defect, recurring); the named לָבַשׁ-class Spirit anchor 24:20 drops `ทรง`; and 36:9 silently emends MT "8" to "18" without the mandated departure footer. The common thread is enforcement scope — the DTr eval lock never reached 2 Chronicles.

**Tag `book-2chronicles-v1` after:**
1. Ben's decision + fix on the **three DECIDE items (§A/§B/§C)** — all small surface edits.
2. Widening the **DTr-formula phrase-locks to 2CH (§D)** alongside the §A fix, so the eval lock is enforced going forward.
3. Ben's confirmation on the **REVIEW items (§E–§I)** (all LOW).
4. External AI sanity-check (the 6-item packet).
5. Optionally, writing **`name_theology_deuteronomistic_2026-05.md` (§G)** and the existing-doc amendments (none gate the tag except as they relate to §A).

**The single highest-value forward-protection step remains the one the 1CH audit named:** widen the DtrH formula locks beyond `["1KI ","2KI "]`. The `malak` half is done; doing the DTr half now (§D) both fixes 2 Chronicles' §4 drift and protects the regnal-formula echoes coming in the Prophets.
