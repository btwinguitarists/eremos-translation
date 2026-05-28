# 2 Chronicles external review — response + proposed actions

**Date:** 2026-05-28
**Reviewers:** Gemini only (ChatGPT paste failed during Cowork run — retry recommended)
**Audit packet:** `docs/end_of_book/2chronicles/external_review_packet_2CH_2026-05-26.md`
**Raw replies:** `docs/end_of_book/_external_inbox/2CH_raw.md`
**Status:** proposed-edits-pending (Items A, B, C, E propose verse edits — two are MAJOR CONCERN named-lock violations)

## Convergence summary

| Item | Gemini | Action |
|------|--------|--------|
| A — "Did evil in YHWH's eyes" formula drift (6 late kings + 29:6) | CONCERN | **PROPOSED VERSE EDITS** (7 verses) — normalize to locked ทำสิ่งชั่วร้าย |
| B — 2 Chr 24:20 missing locked honorific ทรง (named anchor verse) | **MAJOR CONCERN** | **PROPOSED VERSE EDIT** — restore ทรง for לָבַשׁ-class Spirit empowerment |
| C — 2 Chr 36:9 silent MT departure (Jehoiachin's age) | **MAJOR CONCERN** | **PROPOSED VERSE EDIT** — restore MT "eight" + add synoptic-variant Layer-2 footer |
| D — DTr-formula machine locks still Kings-scoped | CONCERN | Widen `check_phrase_consistency.py` to `2CH ` + add kingdom-keyed death-formula register split as 4th lock |
| E — Human-messenger מַלְאָךְ uniformly ผู้สื่อสาร — contradicts §4.4 hierarchy | CONCERN | **PROPOSED VERSE EDITS** — normalize 18:12 + 35:21 per existing lock; license ผู้สื่อสาร only for "prophets-as-messengers" (36:15–16) |
| F — "Until this day" leitwort: 2 Chronicles makes 5-of-6 | FINE (with action) | Lock จนถึงทุกวันนี้; queue 1 Samuel normalization (⚠ conflicts with 2SA review) |

## Items in detail

### Item A — Evaluation formula drift
- **Gemini:** CONCERN. Project locked formulaic surface `ทำสิ่งชั่วร้ายในสายพระเนตร...` for cross-book consistency in Deuteronomistic regnal histories (precedent: 1 Kings). Reverting to thinner bare `ทำชั่ว` for 6 late apostate kings (33:2, 33:6, 33:22, 36:5, 36:9, 36:12) and the non-regnal 29:6 introduces unwarranted variation in a highly formalized cyclical refrain.
- **Action:** Spot-revise 7 verses (33:2, 33:6, 33:22, 36:5, 36:9, 36:12, 29:6) to locked `ทำสิ่งชั่วร้าย`.

### Item B — 2 Chr 24:20 missing ทรง  (MAJOR CONCERN)
- **Gemini:** This verse is **explicitly named** in `spirit_of_yhwh_empowerment` as the anchor for the לָבַשׁ-class, locked to `ทรงสวมทับ` because the divine subject demands the royal verb-honorific. Dropping ทรง breaks both a named lock and the corpus-wide divine-honorifics rule established in JDG 6:34 and 1 Chr 12:18.
- **Action:** Spot-revise to `...พระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์...`, restoring the missing ทรง.

### Item C — 2 Chr 36:9 silent MT departure (Jehoiachin's age)  (MAJOR CONCERN)
- **Gemini:** Project's foundational commitment is the MT base — upheld correctly in 22:2 where a difficult chronological number was preserved with an explanatory footnote. Silently adopting the harmonized "18" in 36:9 against MT's explicit "8" (שְׁמוֹנֶה) **without** a Layer-2 MT-departure footer violates the core translation philosophy.
- **Action:** Restore the MT reading "eight" (`แปด`) in the text of 36:9. Add a synoptic-variant footer disclosing that the parallel at 2 Kgs 24:8 and other manuscript traditions read "eighteen" — align the treatment exactly with 22:2's pattern.

### Item D — DTr-formula machine locks still Kings-scoped
- **Gemini:** CONCERN. 2 Chronicles is the densest regnal book in the corpus; excluding it from `check_phrase_consistency.py` directly enabled Item A's drift. Formulas must be programmatically enforced before moving into the Prophets where these refrains echo.
- **Action:** Widen the DTr-formula locks in `check_phrase_consistency.py` to include `2CH `. Add a fourth lock: kingdom-keyed death-formula register split (Judah vs Israel-Northern). Schedule concurrent with Item A's verse edits.

### Item E — Human-messenger מַלְאָךְ
- **Gemini:** CONCERN. Applying `ผู้สื่อสาร` (communicator/herald) to prophetic messengers in 36:15–16 is arguably defensible; applying it to ordinary court runners (18:12) and foreign envoys (35:21) contradicts §4.4 hierarchy that explicitly steers translators to `ผู้ส่งสาร` or `ทูต`.
- **Action:** Normalize 18:12 → `ผู้ส่งสาร`; 35:21 → `ผู้แทน` or `คณะทูต` per existing lock. For 36:15–16 specifically, update the lock doc to license `ผู้สื่อสาร` for "prophets-as-messengers" usage. Queue 2 Chronicles normalizations on the deferred cross-book list.

### Item F — "Until this day" leitwort: 5-of-6 books converge
- **Gemini:** FINE (with action). 2 Chronicles brings the count to 5 of 6 books naturally preferring `จนถึงทุกวันนี้`. 1 Samuel's bare `จนถึงวันนี้` is an isolated outlier, not a meaningful contextual distinction.
- **Action:** Lock `จนถึงทุกวันนี้` in `leitwort_handling_policy_2026-05.md`; queue 1 Samuel's 8 occurrences for normalization.
- **⚠ Cross-book conflict:** 2 Samuel's review proposes the *opposite* (lock bare; normalize Judges). 2CH/2KI/1CH all agree against 2SA. **Ben to adjudicate.**

## Proposed verse edits — REQUIRES BEN SIGN-OFF

1. **2 Chr 33:2, 33:6, 33:22, 36:5, 36:9, 36:12, 29:6** — normalize evaluation formula `ทำชั่ว` → `ทำสิ่งชั่วร้าย`. Source: Gemini Item A.
2. **2 Chr 24:20** — restore `ทรง` → `...พระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์...`. MAJOR CONCERN, named-lock violation. Source: Gemini Item B.
3. **2 Chr 36:9** — restore MT reading "eight" (`แปด`); add synoptic-variant Layer-2 footer pointing at 2 Kgs 24:8's "eighteen". MAJOR CONCERN, MT-base violation. Source: Gemini Item C.
4. **2 Chr 18:12** — `ผู้สื่อสาร` → `ผู้ส่งสาร` (ordinary court runner). Source: Gemini Item E.
5. **2 Chr 35:21** — `ผู้สื่อสาร` → `ผู้แทน` or `คณะทูต` (foreign envoy). Source: Gemini Item E.
6. **1 Samuel — 8 occurrences of עַד הַיּוֹם הַזֶּה** — cross-book normalization (direction pending Ben's adjudication; see Item F conflict).

## Proposed new / amended translator decision docs

- Amend `spirit_of_yhwh_empowerment` doc — verify 2 Chr 24:20 anchor implementation; document the fix.
- Amend the lock doc covering messenger surfaces — license `ผู้สื่อสาร` for "prophets-as-messengers" specifically (carve-out from §4.4).
- Amend `leitwort_handling_policy_2026-05.md` — lock canonical "until this day" surface (pending Ben's choice).
- Amend canon-policy / MT-departure doc — formalize the requirement for synoptic-variant footers when departing MT for the harmonized synoptic reading (anchor: 22:2 and the proposed 36:9 fix).

## Proposed check-script / tooling updates

- Widen `scripts/check_phrase_consistency.py` to include `2CH ` for DTr-formula locks; add kingdom-keyed death-formula register-split lock (4th lock).

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/2CH_raw.md` (Cowork → Gemini, 2026-05-28). All content above is Gemini's findings; no fresh analysis added. **ChatGPT paste failed during the Cowork run** — recommend a retry, particularly for the two MAJOR CONCERN verse edits (B and C) and the leitwort cross-book conflict (F). Verse-edit proposals flagged for Ben's sign-off.
