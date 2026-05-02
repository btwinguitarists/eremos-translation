# Inclusion-variant gap analysis — 2026-05-02

**Trigger:** while reviewing Romans 16 prior to the Romans end-of-book audit, Ben noticed verses 25-27 (the famous doxology) were silently absent from `output/translations/romans_16.json` — no Tier 2 chapter-footer file, no `⟦…⟧` block, no documented dismissal. Investigation revealed this was **systemic, not isolated**: 9 SBLGNT-omits-mainstream-includes candidates across 4 books had been silently dropped without going through any of the dispositions RULES §5 prescribes.

## What was correctly in place

The pipeline already had:
- `scripts/audit_inclusion_variants.py` — scans translation `notes` for inclusion-variant signals (`SBLGNT omits`, `shorter reading`, `Byzantine adds`, etc.)
- The Tier 2 footer-remark mechanism (`output/textual_variants/<slug>_<NN>.json` → renders as USFM chapter-footer remark via `scripts/export_to_usfm.py`)
- The Tier 1 `[…]` phrase-bracket convention (used widely: Mark 1:1, 3:14, 9:29; Matt 5:22, 5:44, 6:13, 6:15, 6:33; many others)
- The Tier 3 `⟦…⟧` large-block convention (used for Mark 16:9-20)

What was **missing**: an end-of-book gate that **enforces** every audit-flagged candidate to land in one of those bins. Without enforcement, the books shipped successively, the audit was never wired into the checklist, and translators could ship chapters whose `notes` flagged an omission without ever creating the corresponding Tier 2 file.

## What slipped — the 9 cases

**Truly surprising omissions** (mainstream English/Thai readers will notice these missing):

| Verse | Status | Disposition required |
|---|---|---|
| **John 5:4** (angel troubling Bethesda) | `notes` claims Tier 2 file at `output/textual_variants/john_05.json` — **but the file does not exist**. Worst kind of slip: the translator's intent was right, the artifact was never created. | Tier 2 backfill |
| **Romans 16:25-27** (the doxology) | Absent from JSON, no Tier 2 file. Notes correctly flag the gap and even propose the remediation path. | Tier 2 OR Tier 3 (large-block ⟦…⟧) — Ben's call |

**Likely silent-omission per RULES §5** (modern critical-text consensus matches our practice; mainstream readers won't notice):

| Verse | Notes' rationale | Recommended disposition |
|---|---|---|
| Mark 7:16 | Already explicitly listed in RULES §5 silent-omission exemptions | Already fine |
| Mark 9:44 | Already explicitly listed in RULES §5 silent-omission exemptions | Already fine |
| Mark 9:46 | Already explicitly listed in RULES §5 silent-omission exemptions | Already fine |
| Mark 11:26 | "Likely scribal harmonization to Matt 6:15"; modern critical text consensus omits | Add to RULES §5 exemption list OR `_resolved/` doc |
| Mark 15:28 | "Likely secondary insertion harmonizing to Luke 22:37"; SBLGNT/NA28/UBS5 omit | Add to RULES §5 exemption list OR `_resolved/` doc |
| Luke 17:36 | Likely harmonization to Matt 24:40-41; modern texts omit | Add to RULES §5 exemption list OR `_resolved/` doc |

## Why the gate matters

Pulling this thread surfaced a much larger map. Running the corpus-wide audit shows:

```
$ python3 scripts/audit_inclusion_variants.py
```

surfaces **dozens** of inclusion-variant candidates across all completed books. Many are correctly handled (Tier 1 phrase brackets visible in the `thai` field, or Tier 2 files exist). But many are simply unresolved — the translator wrote a textual-variant note and moved on.

Most of the unresolved candidates are likely **legitimately silent-omission** (the translator's prose makes that case clearly: "Following SBLGNT, note-only", "All modern critical texts agree", "likely scribal expansion"). The audit just couldn't recognize the disposition because the translator didn't use the canonical phrase. Strengthening `audit_inclusion_variants.py`'s `SILENT_OMISSION_RE` to match these patterns reduces the noise; what remains is genuine work.

## What was done in this fix

1. **Strict mode added to `scripts/audit_inclusion_variants.py`.** `--strict` exits non-zero if any candidate lacks an explicit disposition (Tier 1 phrase brackets / Tier 2 file / Tier 3 ⟦…⟧ / silent-omission per RULES §5 / `_resolved/` doc).

2. **End-of-book gate added.** `scripts/run_end_of_book_audit.sh` now runs the strict audit before generating the audit prompt for Claude. Books cannot enter end-of-book review with unresolved inclusion variants. Override via `SKIP_INCLUSION_VARIANT_GATE=1` for explicit policy decisions.

3. **`docs/END_OF_BOOK_CHECKLIST.md` §1 updated** with the strict audit as a mechanical-gate requirement.

4. **`output/textual_variants/_resolved/` directory convention introduced** — markdown docs named `<slug>_<NN>_v<V>.md` document candidate dismissals when no Tier 1/2/3 treatment is appropriate. Each doc states which RULES §5 category applies, the manuscript witnesses, and what mainstream English/Thai translations do.

## What still needs to happen (backfill — pipeline work, not in-chat drafting)

These are real translation tasks that must run through the existing pipeline (RULES.md context, glossary enforcement, structured `key_decisions`, audit trail). They cannot be hand-drafted in a chat session.

### Tier 2 backfills (text needed in `output/textual_variants/<slug>_<NN>.json`)

- [ ] **John 5:4** — angel troubling the Bethesda waters. TR/Byz Greek: `ἄγγελος γὰρ κατὰ καιρὸν κατέβαινεν ἐν τῇ κολυμβήθρᾳ, καὶ ἐτάρασσε τὸ ὕδωρ· ὁ οὖν πρῶτος ἐμβὰς μετὰ τὴν ταραχὴν τοῦ ὕδατος, ὑγιὴς ἐγίνετο, ᾧ δήποτε κατείχετο νοσήματι.` Witnesses include: Byz, A, C³, K, L, X, Δ, Θ, Ψ, 063, 078, f¹, f¹³, KJV, THKJV; omit: 𝔓⁶⁶, 𝔓⁷⁵, ℵ, B, C*, D, T, W, 0125, 0141, sa, bo (most), most modern English (BSB, ESV, NIV, CSB).
- [ ] **Romans 16:25-27** — doxology. TR/Byz Greek (each verse spelled out in standard NA28 apparatus / TR Stephanus 1550). Decision still required: **Tier 2** (chapter footer, matching Matthew 17:21 / Acts 8:37 model) or **Tier 3** (large-block `⟦…⟧` in main text after v.24, matching Mark 16:9-20 / John 7:53-8:11 model). The doxology is closer in scale to a Tier 3 large-block transmission; recommend Tier 3 unless the absence is judged less surprising than for Mark 16's longer ending.

### `_resolved/` dismissals (no translation work; just a documented dismissal)

- [ ] **Mark 11:26** — `output/textual_variants/_resolved/mark_11_v26.md`
- [ ] **Mark 15:28** — `output/textual_variants/_resolved/mark_15_v28.md`
- [ ] **Luke 17:36** — `output/textual_variants/_resolved/luke_17_v36.md`

Each `_resolved/` doc should state: (1) which RULES §5 category applies, (2) the manuscript witnesses on each side, (3) what mainstream English (BSB / ESV / NIV / CSB) and mainstream Thai (THSV / THKJV) do, (4) why this case is reader-unsurprising and therefore Tier 2 is unnecessary.

### RULES.md update

- [ ] Extend the explicit silent-omission exemption list in RULES §5 to include Mark 11:26, 15:28, Luke 17:36 (matching the existing list of Mark 7:16, 9:44, 9:46) — once the `_resolved/` docs above are in place, those resolved cases can be promoted to first-class exemption mention.

### Re-export USFM after backfills

- [ ] `python3 scripts/export_to_usfm.py --all` — once Tier 2 files for John 5 + Romans 16 exist, the SFM exports for those books will gain the chapter-footer remarks. Re-run for JHN and ROM specifically; the other books' SFMs do not change.

### Sweep the rest of the corpus

- [ ] After the named cases are dispositioned, run `python3 scripts/audit_inclusion_variants.py --strict` against every shipped book and resolve every remaining UNRESOLVED candidate before tagging the next `book-{slug}-v1`. Most will be silent-omission per RULES §5 (just need a notes phrasing tweak or a `_resolved/` doc); a few may need real Tier 2 backfill.

## Process lessons

1. **An audit script that is not a hard gate is not enforcement.** `audit_inclusion_variants.py` was correct from day one. It just wasn't run as part of the end-of-book workflow.
2. **`notes` claiming "see Tier 2 file" is not the same as the file existing.** John 5:3's notes asserted the Tier 2 file existed at `output/textual_variants/john_05.json` — it did not. The new strict audit detects this divergence and fails.
3. **Translator candor is the right default.** Every one of these 9 cases was correctly flagged in `notes` at translation time. The pipeline didn't lie or omit — it just lacked a follow-through enforcer.

## Confidence statement

After the strict gate is in place, no future SBLGNT-omits-mainstream-includes case will silently ship. The gap was infrastructure, not translation discipline. The actual translations remain rigorous; the work captured in `notes` and `key_decisions` across all completed books shows consistent textual-critical attention. What is needed now is the backfill list above — a finite, well-documented set of work, not a fundamental re-translation.
