# Locked-formula compliance audit — 2026-05-29

**Trigger.** The Nehemiah external review (PR #173) found that NEH 9:17 had drifted from the
locked Exod-34 attribute formula on **all four** components, yet every automated check passed.
That raised a fair question: if a locked formula drifted undetected in one "done" book, did it
drift in others? This audit answers that and closes the gap.

**Method.** Mechanical comparison of shipped `output/translations/*.json` (`translation.thai`)
against the canonical Thai surfaces tabulated in the lock docs, keyed on the distinctive
**Hebrew** source collocations (the same niqqud-stripped approach `check_phrase_consistency.py`
already uses). No judgment calls promoted to "drift" without a verse-level match.

## Scope checked + findings

| Formula | Lock doc | Result |
|---|---|---|
| **Exod-34 divine-attribute formula** | `exod_34_attribute_formula_2026-05.md` | **3 confirmed drifts** (below). Had **no machine check** — only the single token `ความรักมั่นคง` was ever referenced, in the packet-builder, never enforced. |
| **DtH regnal evaluation formula** ("did evil/right in the eyes of YHWH") | `dtr_history_cycle_formulas_2026-05.md` | **62 / 62 in-scope uses correct** (44 evil + 18 right). Clean. This formula **has** a check (`check_phrase_consistency.py`) → it stayed clean. |

### The one-sentence diagnosis
> **Where there was a machine check, the text stayed clean. The one recurring formula with no check drifted.**

This is a missing guard rail, not a translation-quality problem.

## Confirmed drifts (Exod-34 formula)

All three are the same `ทรงพระเมตตา` → `ทรงเมตตา` (dropped `พระ`) slip; NEH 9:17 also drifts two
more components.

| Verse | Component(s) | Shipped (drift) | Locked |
|---|---|---|---|
| Nehemiah 9:17 | רחום; אֶרֶךְ אַפַּיִם; רַב־חֶסֶד | `ทรงเมตตา` · `ทรงพระพิโรธช้า` · `เปี่ยมด้วยความรักมั่นคง` | `ทรงพระเมตตา` · `ทรงกริ้วช้า` · `ทรงบริบูรณ์ด้วยความรักมั่นคง` |
| Nehemiah 9:31 | רחום | `ทรงเมตตา` | `ทรงพระเมตตา` |
| 2 Chronicles 30:9 | רחום | `ทรงเมตตา` | `ทรงพระเมตตา` |

## Fix delivered in this PR (no shipped-text changes)

Added three Hebrew-keyed Exod-34 locks to `scripts/check_phrase_consistency.py` (now 15 phrase
locks, suite green). Each was validated against the full translated corpus: they catch exactly
the drifts above and pass every correct occurrence (Exod 34:6, Num 14:18, Jonah 4:2), with a
negative-lookahead on `רַב־חֶסֶד` to exclude pronominal-suffix petitions (e.g. NEH 13:22
`כְּרֹב חַסְדֶּךָ`). The check auto-covers future books (Psalms et al. recite this formula
heavily). This closes the `run_checks.py` note *"check_phrase_consistency (needs Hebrew
PHRASE_LOCKS extension)."*

The three drifted verses are recorded as **documented exceptions** in the check (so the suite
stays green and the debt is visible) until the edits below are signed off — then remove the
exceptions.

## Proposed verse edits — REQUIRES BEN SIGN-OFF

These realign shipped text to an **already-locked** canonical surface (the lock doc tabulates the
exact target string per verse); they are enforcement, not new translation decisions.

1. **2 Chronicles 30:9** (NEW — found by this audit)
   - **Before:** `…เพราะองค์พระผู้เป็นเจ้าพระเจ้าของท่านทรงพระคุณและทรงเมตตา…`
   - **After:** `…เพราะองค์พระผู้เป็นเจ้าพระเจ้าของท่านทรงพระคุณและทรงพระเมตตา…`
2. **Nehemiah 9:17, 9:31** — already proposed in **PR #173** (Nehemiah external review). Same `ทรงพระเมตตา` realignment; 9:17 also restores `ทรงกริ้วช้า` + `ทรงบริบูรณ์ด้วยความรักมั่นคง`.

## Open question for Ben (low priority — no action by default)

The DtH regnal lock (`ชั่วร้าย`) is **scoped to the regnal cycle**, and all 62 regnal uses comply.
Five non-regnal occurrences render "do evil in the eyes" with bare `ชั่ว` instead: **Deut 9:18,
17:2, 31:29** (law/sermon, pre-monarchy) and **1 Sam 15:19, 2 Sam 12:9** (direct divine/prophetic
rebuke speech). These are **outside the lock's stated scope** and may be a deliberate
register/context distinction. Flagged only so Ben can decide if he ever wants the "do evil in the
eyes of the LORD" surface unified corpus-wide. Default: leave as-is.

## Going forward

- When the verse edits above are signed off, apply them and **remove the three exceptions** so
  the guard fully enforces.
- The same audit pattern (compare shipped Thai vs a lock doc's tabulated canonical surface, then
  fold the lock into `check_phrase_consistency.py`) generalizes to any other fixed-surface
  recurring formula. Exod-34 and the DtH formulas are now covered; others can be swept as needed.
