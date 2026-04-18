# Greek NT options — survey & decision (2026-04-18)

## Why this doc exists

When Ben noticed that Mark 1:1 reads `จุดเริ่มต้นของข่าวประเสริฐเรื่องพระเยซูคริสต์` without "พระบุตรของพระเจ้า" — unlike THSV, NIV, ESV, BSB, and most published Bibles — the obvious question was: *why are we using a Greek source that omits this when other free editions include it?*

This doc answers that question and saves the next person who asks it from re-running the survey. **Decision: stay on SBLGNT for now. Use the single-bracket convention to make contested words visible to readers.** The bracket policy is in `RULES.md §5`; specific bracketed verses are tracked there.

This is not a "we considered everything once" doc; it's a "here's the field as of 2026-04 and the conditions under which we'd revisit."

---

## What's actually available

Free-license Greek NTs that could legally be embedded in a CC0 project:

| Edition | License | Textual family | Mark 1:1 "Son of God"? |
|---|---|---|---|
| **SBLGNT** (current) | CC BY 4.0 | Modern critical / Alexandrian-leaning (NA family) | omits |
| Byzantine Majority Text (Robinson-Pierpont) | Public domain | Byzantine / Majority | includes |
| Westcott-Hort 1881 | Public domain | 19th-c. critical (Alexandrian) | omits |
| Antoniades 1904 (Patriarchal) | Public domain | Byzantine / Greek Orthodox | includes |
| Nestle 1904 | Public domain | Pre-modern critical | includes |
| Tischendorf 8th | Public domain | 19th-c. critical (Alexandrian) | omits |
| Stephanus 1550 | Public domain | TR / Reformation-era | includes |
| **SR-GNT** (CNTR / Bunning) | CC BY 4.0 | Modern algorithmic eclectic | (modern eclectic — likely brackets, would verify) |

Editions evaluated and ruled out as not CC0-compatible:

| Edition | License | Why ruled out |
|---|---|---|
| THGNT (Tyndale House 2017) | Proprietary "free to read" | Not CC-licensed; cannot redistribute in our repo |
| Tregelles 1857-79 | CC BY-NC-SA 3.0 | NC clause incompatible with CC0 derivative work |
| OpenGNT | CC BY-SA 4.0 | Share-alike propagates copyleft to our translation output |
| NA28 / UBS5 | Copyright Deutsche Bibelgesellschaft | Cannot legally embed; ESV/NIV/etc. license access |

---

## Why SBLGNT stays even though some editions include "Son of God"

The free-license editions that include "Son of God" at Mark 1:1 without brackets fall in **two textual families**:

- **Byzantine / Patriarchal** (Robinson-Pierpont, Antoniades 1904) — the manuscript tradition the Greek Orthodox church uses; the basis of the Textus Receptus → KJV. Differs from SBLGNT at thousands of places, not just Mark 1:1.
- **Pre-modern critical** (Nestle 1904) — older eclectic text, mostly Alexandrian-leaning but pre-dating much 20th-c. textual research.

Switching to either family to fix Mark 1:1 would simultaneously change:

- **Mark 9:29** — adds back "and fasting"
- **1 Tim 3:16** — changes "He who" to "God" (a major Christological textual question)
- **Dozens of other verses** — different rendering of double readings, harmonizations, etc.

Most of those changes would push us *away from* the modern evangelical Protestant translation mainstream (ESV, NIV, CSB, NASB, BSB) that we currently sit comfortably with. **We'd be solving a one-verse reader-trust problem by creating a much larger family-tradition mismatch.**

The bracket convention (`[พระบุตรของพระเจ้า]`) is the same editorial response that NA28, NRSV-Updated, and NET use. It honestly signals "the words appear in many manuscripts and translations; our base text just doesn't print them in the main line." Reader trust preserved without changing source-text family.

---

## The watch item: SR-GNT

**Statistical Restoration Greek New Testament**, edited by Alan Bunning at the Center for New Testament Restoration (CNTR).

- **License**: CC BY 4.0 — fully CC0-derivable
- **Methodology**: Algorithmic eclectic text — transparent statistical reconstruction from the earliest available manuscripts. Modern critical-text family, not Byzantine.
- **Format**: TSV, machine-readable
- **Status**: Active, maintained by Bunning + community
- **Repo**: <https://github.com/Freely-Given-org/CNTR-SR>
- **Already evaluated**: see `docs/CNTR_SPIKE_2026-04.md` (we evaluated CNTR's *Universal Apparatus* and deferred until it's machine-readable; SR.tsv is a separate, currently-usable artifact)

If SBLGNT ever ages out, gets withdrawn, or develops licensing issues, **SR-GNT is the natural migration path** — same critical-text family, free license, modern methodology. Worth a deeper look in 2026 H2 or 2027 to see how it's matured.

For now, SR-GNT would represent a parallel-but-different editorial methodology. Migrating today would re-open every translation decision against a different base text — too much churn for too little gain.

---

## When to revisit

Re-run this survey if any of these become true:

1. **SBLGNT changes its license** (currently CC BY 4.0, stable since 2010 — no signal of change)
2. **SR-GNT publishes a 2.0** with broader scholarly endorsement and a stable manuscript-apparatus dataset
3. **A new CC-licensed eclectic Greek NT** emerges in the modern critical-text tradition (THGNT can't help us unless its license changes)
4. **The bracket convention proves insufficient** — e.g. native-speaker reviewers (Stage B.3) tell us readers are still confused or distrustful despite the brackets
5. **We start a major book where SBLGNT and mainstream diverge much more frequently** (some Pauline epistles have heavier divergence; the cumulative bracket density might become a UX problem)

If none of those happen, no action. SBLGNT + bracket convention is the answer.

---

## Sources verified during this survey

- <https://sblgnt.com/license/> — SBLGNT CC BY 4.0
- <https://github.com/Faithlife/SBLGNT> — Mark 1:1 raw text confirmed
- <https://github.com/byztxt/byzantine-majority-text> — Robinson-Pierpont, public domain
- <https://github.com/byztxt/greektext-antoniades> — Patriarchal 1904, public domain
- <https://github.com/byztxt/greektext-westcott-hort> — Westcott-Hort 1881, public domain
- <https://github.com/eliranwong/OpenGNT> — CC BY-SA 4.0 (incompatible with our CC0 output)
- <https://github.com/mrgreekgeek/tregelles-greek-nt> — Tregelles, CC BY-NC-SA (incompatible)
- <https://github.com/Freely-Given-org/CNTR-SR> — SR-GNT, CC BY 4.0
- <https://berean.bible/licensing.htm> — Berean licensing (BGB Greek not explicitly named in PD declaration; status ambiguous, would need direct confirmation if pursued)
- <https://greekcntr.org/> — CNTR home (and `docs/CNTR_SPIKE_2026-04.md` for the Universal Apparatus evaluation)
