# 2 Samuel external review — response + proposed actions

**Date:** 2026-05-28 (ChatGPT data added later same day)
**Reviewers:** Gemini + ChatGPT
**Audit packet:** `docs/end_of_book/2samuel/external_review_packet_2SA_2026-05-23.md`
**Raw replies:** `docs/end_of_book/_external_inbox/2SA_raw.md`
**Status:** proposed-edits-pending (Item A is the release-blocker — Tier-2 footer gap; ChatGPT escalates to MAJOR + expands scope to 24:9 + 24:13)

> **⚠ Leitwort item is MOOT (and reveals why).** Both AIs proposed locking the **bare** `จนถึงวันนี้` here — but this packet was generated on **2026-05-23**, under the v0.3 lock that chose the bare form. The doc was **REVERSED in v0.4 on 2026-05-25** (per 2 Kings audit) to `จนถึงทุกวันนี้`. So the AIs reviewed under the *old* lock direction; the doc has since reversed. **The proposed normalization of Judges (6 verses) in Item D should NOT proceed.** The current canonical surface is `จนถึงทุกวันนี้`; 1 Samuel + Judges + 1 Kings + 2 Kings + 1 Chr + 2 Chr all now use it. 2 Samuel itself is the deferred backlog (4× bare occurrences) per the doc's v0.6 note — **knowingly deferred, not a tag-blocker**.

## Convergence summary

| Item | Gemini | ChatGPT | Synthesized | Action |
|------|--------|---------|-------------|--------|
| A — Tier-2 reader-footer gap (15:7, 21:19, 24:1) | CONCERN | **MAJOR** | **PROPOSED LAYER-2 ADDITIONS** | **ChatGPT escalates to MAJOR + expands scope to 24:9 + 24:13.** 15:7 is the only true release-blocker; others strongly recommended |
| B — Adonai-YHWH compound prayer-vocative | FINE | FINE | LOCK | Lock as-is; amend `divine_names_table_2026-05.md` per ChatGPT's discourse-function rule (aligns with 1 KI Item D recommendation) |
| C — Synoptic/parallel-passage corpus doc | CONCERN | CONCERN | WRITE DOC | Write `synoptic_parallel_passages_2026-05.md`; ChatGPT supplies full 5-principle policy outline |
| ~~D — "Until this day" leitwort~~ | ~~CONCERN~~ | ~~CONCERN~~ | **MOOT — old lock direction** | Both AIs proposed bare; doc has since reversed to expanded; 2 SA is the *deferred backlog*, not the canonical anchor |

## Items in detail

### Item A — Textual-variant Tier-2 reader-footer gap  (ChatGPT MAJOR)
- **Gemini:** CONCERN. Canon policy mandates Tier-2 footnote for Trigger-1 MT departures; absence at 2 Sam 15:7 is a direct compliance failure. "Forty years" is technically grammatical but historically nonsensical (contradicts Absalom's lifespan), justifying the emendation to "four" — but demanding consistent Layer-2 disclosure alongside 21:19 + 24:1.
- **ChatGPT:** **MAJOR.** Surface translation mostly defensible; **transparency layer is not.** Specific scope:
  - **Required:** 15:7 (real MT departure: forty → สี่).
  - **Strongly recommended:** 24:1, 21:19.
  - **Also worth adding:** 24:9 and 24:13 — once chapter 24 already needs a footer for 24:1, the census/famine numerical variants shouldn't remain invisible. **ChatGPT-only additions.**
  - For 15:7: keep `เมื่อสี่ปีผ่านไป` (MT departure) + add footer. **Tighten the policy wording:**
    > "The project remains MT-anchored. Departures from MT require Layer-1 documentation and a Tier-2 reader note when the MT reading is best explained as a numerical or scribal corruption that creates a serious chronological, contextual, or narrative impossibility/implausibility and is corrected by strong early versional or manuscript support."
  - This cleanly distinguishes 15:7 (legitimate controlled emendation) from 24:13 (preserve MT; "seven years" difficult vs LXX/Chr "three" but not narratively impossible).
- **Action:** **Before tagging book-2samuel-v1**, add Tier-2 chapter-footer entries: 15:7 (required); 21:19 + 24:1 (strongly recommended); 24:9 + 24:13 (also worth adding). Tighten canon-policy wording per ChatGPT's draft above. Keep 15:7 verse as `เมื่อสี่ปีผ่านไป`.

### Item B — Adonai-YHWH compound prayer-vocative
- **Gemini:** FINE. Thai syntax: ข้าแต่ functions sentence-initial; forcing into mid-sentence appositional (2 Sam 7:22) would be linguistically unnatural. Document the position-based split (initial ข้าแต่ at JOS 7:7 anchor; bare mid-sentence at 2 SA 7 anchor).
- **ChatGPT:** FINE. Bare `องค์พระผู้เป็นเจ้า` is right for the 2 SA 7 appositional vocatives (7:18, 7:19, 7:22, 7:28, 7:29). **Discourse-function rule (aligns with 1 KI Item D recommendation):**
  > אֲדֹנָי יְהוִה normally surfaces as `องค์พระผู้เป็นเจ้า`. Use `ข้าแต่องค์พระผู้เป็นเจ้า` when the compound occurs in a sentence-initial interjection or petition frame, especially with forms such as אֲהָהּ / בִּי / אָנָּא. In mid-sentence appositional prayer address, omit ข้าแต่; 2 Sam 7:18–29 is the controlling exemplar.
- **Action:** Lock as-is. Amend `divine_names_table_2026-05.md` with ChatGPT's discourse-function rule. **This is the same rule recommended in 1 KI Item D** — one consistent amendment covers JOS 7 + JDG 6 + 2 SA 7 + 1 KI 8 under a single principle.

### Item C — Synoptic / parallel-passage corpus doc
- **Gemini:** CONCERN. 2 Sam 22 // Ps 18 + Samuel↔Chronicles overlaps are handled well, but methodology undocumented guarantees drift before Kings/Chronicles + Psalter compound.
- **ChatGPT:** CONCERN. Same. **Full 5-principle policy outline:**
  1. Translate each canonical occurrence from its own MT context. Do not mechanically harmonize 2 Sam 22 to Ps 18, Kings to Isaiah, or Samuel/Kings to Chronicles.
  2. Layer 1: always document known major parallel-passage divergences in `key_decisions` / `notes`.
  3. Layer 2: add reader-facing footers when divergence is theologically prominent, apologetically predictable, numerically contradictory, or when the translation departs from MT.
  4. Standard wording: *"The parallel account in 1 Chronicles 21:1 identifies Satan as the one who incited David; 2 Samuel preserves the wording that the LORD incited David."*
  5. **Psalter default:** when Ps 18 is reached, translate Psalm 18 from Psalm 18's MT, not from 2 Sam 22; footnote meaningful differences back to 2 Sam 22.
- **Action:** Write `synoptic_parallel_passages_2026-05.md` per ChatGPT's 5-principle outline. **Priority — before next major parallel-heavy book ships.**

### Item D — "Until this day" leitwort (MOOT — see top callout)
- **Gemini:** CONCERN. Proposes locking the **bare** `จนถึงวันนี้` + normalizing Judges (6 occurrences).
- **ChatGPT:** CONCERN. Same direction.
- **Action:** **MOOT — old lock direction.** This audit was generated 2026-05-23 under v0.3 (which chose bare); v0.4 (2026-05-25, triggered by 2 Kings audit) **REVERSED** to `จนถึงทุกวันนี้`. **Do not** normalize Judges to bare — the canonical surface is now the expanded form, and Judges is already conformant. The 2 Samuel 4× bare occurrences are the deferred backlog per v0.6, not a tag-blocker. The AIs reviewed the *old* lock direction in good faith; the doc moved on.

## Proposed verse edits — REQUIRES BEN SIGN-OFF

**No main-text verse edits** (15:7 emendation already shipped; keep `เมื่อสี่ปีผ่านไป`).

Layer-2 footer additions (Item A — release-blocker is 15:7; expanded scope from ChatGPT):
1. **2 Sam 15:7** — Tier-2 footer for MT departure (required pre-tag).
2. **2 Sam 21:19** — Tier-2 footer (strongly recommended).
3. **2 Sam 24:1** — Tier-2 footer (strongly recommended).
4. **2 Sam 24:9** — Tier-2 footer for census numerical variant (ChatGPT addition).
5. **2 Sam 24:13** — Tier-2 footer for famine numerical variant (ChatGPT addition; preserve MT "seven years").

## Proposed new / amended translator decision docs

**Highest priority — before tagging:**
- Add Tier-2 footers per Item A.
- Tighten canon-policy MT-departure wording per ChatGPT's draft.

**Before next major parallel-heavy book:**
- **Amend (already exists): `synoptic_parallel_passages_2026-05.md`** — ChatGPT's full 5-principle policy outline.

**Coordinated cross-book:**
- **Amend `divine_names_table_2026-05.md`** — adopt ChatGPT's discourse-function rule for Adonai-YHWH (covers JOS 7, JDG 6, 2 SA 7, 1 KI 8 under one principle).

## Provenance

Synthesized from `docs/end_of_book/_external_inbox/2SA_raw.md` (Cowork → Gemini + ChatGPT, 2026-05-28). All content above is the AIs' findings; no fresh analysis added. **Item D was MOOT** — both AIs were reviewing under the v0.3 lock direction; v0.4 reversal post-dated the 2 SA packet. ChatGPT escalated A from CONCERN to MAJOR and added two new Layer-2 footer recommendations (24:9, 24:13). Verse-edit proposals flagged for Ben's sign-off — *all Layer-2 metadata, no main-text changes.*
