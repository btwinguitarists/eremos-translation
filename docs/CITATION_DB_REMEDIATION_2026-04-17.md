# OT Citation DB remediation — 2026-04-17

## What happened

Between the Mark 10 ship (2026-04-17 07:13) and the Mark 15 ship (2026-04-17 16:40),
the workflow for recording OT citations in `data/nt_ot_citations.json` silently
fell out. During chapters 1–10 and 12, Claude added entries to the curated DB
as part of each chapter's translation commit — a hand-curated step that
happened in-chat. When the `ship_chapter.sh` automation matured, that manual
step was never captured as a required pipeline action, and chapters 11, 13,
14, and 15 shipped with **zero** DB entries despite rich OT intertextual
identifications in the translation notes.

The `scripts/check_ot_citations.py` audit was read-only: it reported whether
notes acknowledged the DB's entries, but had no way to detect that the DB
itself had gaps. `"0 links found ✅ clean"` was treated as passing,
indistinguishable from `"no OT content in this chapter"`.

A contributing factor: the Opus 4.6 → 4.7 model update (mid-pipeline run)
appears to have given the translator more leeway in following explicit
instructions — the notes in Mark 11/13/14/15 include phrases like
"Added to nt_ot_citations.json" that were never actually executed.

## What changed (quality-neutral)

Nothing in the **Thai translations or scholarly notes** was altered. All
remediation is pipeline / audit-trail work:

1. **`data/nt_ot_citations.json`** — grew from 26 entries to 104. Each new
   entry reproduces an OT-identification already present in a chapter's
   translation notes; no new scholarly claims are introduced. Entries were
   sorted by canonical order for deterministic diffs.

2. **`scripts/check_ot_citations.py`** — hardened with a **DB drift detector**
   that fails ship when a verse's notes make an explicit citation-claim
   (phrases like "OT CITATION", "composite citation", "FULFILLMENT:")
   co-located within ~80 chars of an OT book reference, yet no entry exists
   for that verse in the DB. Negation guards (`"NOT an OT citation"`) and a
   proximity window suppress false positives from synoptic-parallel mentions
   and generic cross-references.

3. **`RULES.md` §5 and §7** — updated to state explicitly that adding a DB
   entry is required in the same editing pass as writing the verse's
   intertextual note. Not a separate downstream step.

4. **Backfill scripts** — `scripts/backfill_ot_citations_11_13_14_15.py`
   and `scripts/backfill_ot_citations_all.py` are committed for full
   reproducibility. They were one-time tools; future drift should be caught
   at translation-time by the hardened check.

## Verification

After remediation, all 15 translated Mark chapters pass
`check_ot_citations.py` cleanly — 0 drift, 0 unacknowledged DB entries.

## Not affected

- No Thai translation text was edited.
- No verse-level scholarly notes were edited.
- No glossary entries changed.
- No HASHES.md regeneration needed for translation files
  (file contents unchanged).

The remediation is strictly to the **auditability infrastructure** that sits
alongside the translation. This matters for the CC0 project's
transparency commitment — reviewers need to be able to cross-reference
every OT-intertextual claim in the notes against a machine-readable manifest —
but the translation itself was already correct in flagging these links.
