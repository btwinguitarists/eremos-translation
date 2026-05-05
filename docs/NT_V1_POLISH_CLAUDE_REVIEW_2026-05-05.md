# NT v1 polish review — Claude verdicts

**Date:** 2026-05-05
**Reviewer:** Claude (Opus 4.7, 1M context)
**Input:** `docs/NT_V1_POLISH_SUMMARY_2026-05-05.md` (10 proposals)
**Method:** read each affected verse JSON for Greek/BSB/Thai context + locked `key_decisions`; corpus-grep for consistency on the typographic/lexical patterns the proposal touches; cross-check against `RULES.md` §4 and `divine_names_table_2026-05.md` for anything that looks register-locked.
**Output:** **8 APPROVE / 2 REJECT.** Both rejections are the title_collision pair; rationale below.

## Summary table

| ID | Verse | Type | Verdict | One-line reason |
|---|---|---|---|---|
| `mark_03_001` | Mark 3:7 | redundant_directional | ✅ APPROVE | Greek has one motion verb (ἀνεχώρησεν); current Thai stacks ไป twice |
| `mark_03_002` | Mark 3:11 | awkward_phonetic | ✅ APPROVE *(with corpus note)* | พระ-พระ stack is real; corpus already accommodates both forms — see §A |
| `john_15_001` | John 15:12 | awkward_phonetic | ✅ APPROVE | Doesn't break the Jn 13:34 phrase-lock (different syntax there — uses ว่า) |
| `john_15_002` | John 15:19 | awkward_phonetic | ✅ APPROVE | Greek δὲ + ἀλλά don't both need to surface in Thai; first แต่ carries it |
| `john_15_003` | John 15:21 | awkward_phonetic | ✅ APPROVE | Restores the Greek διά / ὅτι distinction Thai had collapsed |
| `romans_03_001` | Romans 3:20 | awkward_phonetic | ✅ APPROVE *(with corpus note)* | Same as Mark 3:11 |
| `1john_03_001` | 1 John 3:11 | awkward_phonetic | ✅ APPROVE | Same pattern; explanatory function preserved with ได้แก่ |
| `1john_03_002` | 1 John 3:23 | awkward_phonetic | ✅ APPROVE | Same; note the third (apposition) คือ correctly stays |
| `acts_03_001` | Acts 3:22 | title_collision | ❌ REJECT | Breaks the corpus-locked `องค์พระผู้เป็นเจ้าพระเจ้า` no-space form |
| `revelation_16_001` | Revelation 16:7 | title_collision | ❌ REJECT | Same — would create drift from 5+ shipped chapters |

---

## §A. Per-proposal rationale

### ✅ Mark 3:7 — APPROVE

> เสด็จออกไปกับบรรดาสาวกของพระองค์**ไป**ยัง → เสด็จออกไปกับบรรดาสาวกของพระองค์ยัง

Greek (`ἀνεχώρησεν πρὸς τὴν θάλασσαν`) has **one** motion verb + one destination preposition. The current Thai stacks `ออกไป` (motion) + `ไปยัง` (motion-particle + destination), producing the audible double-`ไป`. Dropping the second `ไป` keeps the destination marker `ยัง` and aligns Thai to the Greek's single motion. No theology, no register implication.

### ✅ Mark 3:11 — APPROVE *(corpus inconsistency flagged)*

> ทรุดตัวลงต่อเบื้องพระพักตร์พระองค์ → ทรุดตัวลงต่อเบื้องพระพักตร์ของพระองค์

The phonetic stumble is real (royal-noun `พระพักตร์` + royal-pronoun `พระองค์` directly clipped). Inserting `ของ` is purely additive — no meaning change, no demon-register interaction (the demon-speech `ท่านคือพระบุตรของพระเจ้า` later in the verse is untouched).

**Corpus-consistency note (worth Ben's eye):** the corpus already runs ~22 verses with `พระพักตร์พระองค์` (no `ของ`) AND ~12+ verses with `พระพักตร์ของพระองค์` (with `ของ`). Both forms are accepted Thai. The polish proposal touches 2 of the ~22 no-`ของ` cases (Mk 3:11 + Rom 3:20) — the rationale "พระ-พระ stumbles aloud" applies to all ~22, not just these 2. Approve as a spot-improvement, but flag for a future corpus-wide normalization pass if Ben wants either form locked uniformly. Not a blocker either way.

### ✅ John 15:12 — APPROVE

> นี่**คือ**พระบัญญัติของเรา **คือ** ให้พวกท่านรักกันและกัน → นี่**คือ**พระบัญญัติของเรา **ได้แก่** ให้พวกท่าน...

The first `คือ` is an equative copula ("this **is**"); the second was an explanatory marker ("namely"). Same word, two different functions, with the audible echo. `ได้แก่` covers the explanatory slot cleanly.

The KD calls out a phrase-lock with John 13:34 (`พระบัญญัติใหม่`). Verified: **Jn 13:34's Thai is** `เราให้พระบัญญัติใหม่แก่พวกท่าน**ว่า** ให้พวกท่านรักกันและกัน` — uses `ว่า`, NOT a double-`คือ`. The two verses already differ in syntax; this fix doesn't disturb the shared lexeme `พระบัญญัติ` or the rendering of `ἵνα ἀγαπᾶτε ἀλλήλους`.

### ✅ John 15:19 — APPROVE

> **แต่**เพราะพวกท่านไม่ได้เป็นของโลก **แต่**เราได้เลือกพวกท่านออกมาจากโลกแล้ว → ...**แต่**เพราะ ... เราได้เลือก...

Greek has two contrast markers (`δὲ` + `ἀλλά`), but Thai discourse rarely needs both surfaced. The first `แต่` already establishes the contrast frame; the second was carrying `ἀλλά` redundantly. The "I chose you out of the world" clause's force is theologically intact — it's the affirmative payoff of the contrast already opened by the initial `แต่`. The drop is a register move, not a meaning move.

### ✅ John 15:21 — APPROVE

> **เพราะ**พระนามของเรา **เพราะ**พวกเขาไม่รู้จัก... → **เพราะ**พระนาม... **เนื่องจาก**พวกเขาไม่รู้จัก...

This one I like a lot. Greek differentiates two causal markers — `διά` (instrumental, "by reason of my name") + `ὅτι` (subordinating, "since they do not know") — and the Thai had flattened both to `เพราะ`. The proposal **restores the distinction** the Greek already makes. The KD's `phrase-lock` on `ผู้ทรงใช้เรามา` (Jn 14:24) is untouched.

### ✅ Romans 3:20 — APPROVE

Identical to Mark 3:11 case; same corpus-consistency note applies. The KD calls out the OT echo of Ps 143:2 LXX — the change is a Thai surface-flow tweak, not a textual claim. Lock unchanged.

### ✅ 1 John 3:11 — APPROVE

Identical pattern to Jn 15:12. The verse opens with the Johannine `αὕτη ἐστὶν ἡ ἀγγελία` ("this is the message") + `ἵνα ἀγαπῶμεν ἀλλήλους` (purpose-explanatory). Two different `คือ` functions; differentiating the second to `ได้แก่` reads cleaner without losing anything.

### ✅ 1 John 3:23 — APPROVE

> นี่**คือ**พระบัญญัติของพระองค์ **คือ** ให้เราเชื่อในพระนามของพระบุตรของพระองค์ **คือ**พระเยซูคริสต์ → นี่**คือ**พระบัญญัติของพระองค์ **ได้แก่** ให้เราเชื่อในพระนามของพระบุตรของพระองค์ **คือ**พระเยซูคริสต์

The verse has THREE `คือ`s. Critically the proposal touches only the **second** — leaving the third (`คือพระเยซูคริสต์`, an apposition: "namely Jesus Christ") in place. That's correct: the third `คือ` has a different role (apposition-naming) and reads naturally there. The polish reduces 3→2 occurrences cleanly.

---

### ❌ Acts 3:22 — REJECT *(this is the title_collision case Ben flagged)*

> องค์พระผู้เป็นเจ้าพระเจ้าจะทรงตั้งผู้เผยพระวจนะ → องค์พระผู้เป็นเจ้า พระเจ้าจะทรงตั้ง...

**The corpus-lock is real.** I grepped for the no-space `องค์พระผู้เป็นเจ้าพระเจ้า` form — it appears in main `thai` field of 5+ shipped chapters as the established rendering of `κύριος ὁ θεός`:

| Verse | Greek | Thai (no-space — locked) |
|---|---|---|
| Luke 4:8 | προσκυνήσεις κύριον τὸν θεόν σου | **องค์พระผู้เป็นเจ้าพระเจ้า**ของเจ้า |
| Luke 4:12 | οὐκ ἐκπειράσεις κύριον τὸν θεόν σου | **องค์พระผู้เป็นเจ้าพระเจ้า**ของเจ้า |
| Mark 12:29 | κύριος ὁ θεὸς ἡμῶν κύριος εἷς | **องค์พระผู้เป็นเจ้าพระเจ้า**ของเรา ... |
| Revelation 15:3 | κύριε ὁ θεὸς ὁ παντοκράτωρ | **องค์พระผู้เป็นเจ้าพระเจ้า** ผู้ทรงฤทธานุภาพ... |
| Revelation 19:6 | κύριος ὁ θεὸς ἡμῶν ὁ παντοκράτωρ | **องค์พระผู้เป็นเจ้าพระเจ้า** ผู้ทรงฤทธานุภาพ... |

The Luke 4:12 KD says explicitly: *"κύριον τὸν θεόν σου → องค์พระผู้เป็นเจ้าพระเจ้าของเจ้า (RULES.md §4 non-negotiable)."* That is a deliberate, locked, no-space rendering anchored to RULES §4 key-term consistency.

The space-separated form (`องค์พระผู้เป็นเจ้า พระเจ้า`) **does** appear in the corpus — but only in the `thai_literal` field (the word-for-word literal-alignment field) and `thai_summary` field, never in the main `thai` field. The literal field deliberately spaces title-clusters; the main `thai` field doesn't. That's the contract.

Approving Acts 3:22 + Rev 16:7 with the space would create drift from 5 already-shipped renderings of the same compound + violate the RULES §4 non-negotiable lock the Luke 4:12 KD names. The audible-readability concern is real but doesn't override the lock — and any reader-tool that needs a typographic break can render the space at display time without changing the source-of-truth `thai` field.

**Reject.** If Ben judges the readability concern important enough, the right move is a corpus-wide policy decision (touching all 5+ existing verses + future Genesis 2 once OT translates `יהוה אֱלֹהִים`) — not a 2-verse spot-revise that creates new asymmetry.

### ❌ Revelation 16:7 — REJECT

Identical case to Acts 3:22. Same lock, same reason, same recommendation. Reject.

---

## §B. Implementation suggestion if Ben wants to apply

The 8 APPROVE proposals can land cleanly via:

```
# 1. Edit docs/NT_V1_POLISH_SUMMARY_2026-05-05.md:
#    - 8 proposals: change "**Decision:** pending" → "**Decision:** approve"
#    - Acts 3:22 + Rev 16:7: change "**Decision:** pending" → "**Decision:** reject"
# 2. Run:
python3 scripts/apply_polish_deltas.py --all
# 3. Re-render derived files for the touched chapters:
python3 scripts/render_reader.py --book MRK
python3 scripts/render_reader.py --book JHN
python3 scripts/render_reader.py --book ACT  # no-op for the rejected case but keeps the chapter fresh
python3 scripts/render_reader.py --book ROM
python3 scripts/render_reader.py --book 1JN
python3 scripts/render_reader.py --book REV  # no-op for the rejected case
# 4. Run check_phrase_consistency.py + check_key_term_consistency.py to confirm no drift
# 5. Commit + open a single PR (chore/nt-v1-polish-2026-05-05)
```

## §C. Optional follow-up (separate PR, not blocking the polish PR)

The two corpus-wide questions surfaced by this audit but **not** decided by it:

1. **`พระพักตร์พระองค์` vs `พระพักตร์ของพระองค์` corpus split.** ~22 / ~12 occurrence ratio. Either lock both forms as legitimate (no action) or pick one and normalize. Touching only the 2 verses in this polish round is partial; Ben may want a normalization sweep at next polish-pass.

2. **`องค์พระผู้เป็นเจ้าพระเจ้า` no-space form: typographic question only.** The lock holds. If reader-tool feedback later judges the run-on jarring at oral-reading time, the right fix is at the renderer (insert a non-breaking space at display time) rather than in the `thai` field — keeps the source-of-truth uniform, lets the surface adapt to medium.
