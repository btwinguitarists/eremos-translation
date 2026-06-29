# Cross-Book Audit Loop — Charter

**This file is the loop's contract. The loop re-reads it at the start of every iteration.**
If anything here conflicts with cleverness, this file wins. Its job is to keep an autonomous
loop from drifting, hallucinating, or over-correcting a finished Bible translation.

---

## 0. North star

The Eremos Thai Bible (CC0) is **translation-complete** (OT 929 + NT 260 = 1,189 ch). Every
book passed per-chapter checks, an end-of-book audit, and an independent external review.
This loop does the one layer those can't: **consistency *across* books, and the OT↔NT seams.**

The goal is a corpus that reads as one faithful, natural Thai Bible — **not** a corpus
flattened to mechanical uniformity. Ben is the Thai-language and theological authority. The
loop proposes; Ben disposes.

## 1. Hard guardrails — never violate

1. **Translation files are READ-ONLY to the loop.** The loop NEVER writes to
   `output/translations/**`. Every text change is a *proposal* in a PR behind Ben's
   checkbox-and-merge gate. (See [[feedback_translation_instructions_readonly]].)
2. **Never touch a LOCKED decision** without surfacing it as a question. If a verse's
   `key_decisions` or a `docs/decisions/*` doc marks the rendering LOCKED/RESOLVED/APPLIED,
   it is settled — do not re-open it as a fix; at most note a genuinely new conflict.
3. **Default to NOT flagging.** Per-book contextual variation is often the *more* natural
   Thai and is legitimate. Before flagging "drift," ask: *is this actually appropriate
   register-fitting that should be documented as licensed, rather than normalized away?*
   When in doubt, leave it alone. (See [[feedback_dont_overflag_thai]].)
4. **Never invent.** Quote the actual verse ref, Hebrew/Greek, and shipped Thai from the
   files. No invented citations, lemmas, or renderings. If you can't verify it in a file,
   don't assert it.
5. **De-dup before emitting anything.** Check, in this order: the existing
   `EremosVercel2/shared/review-questions/*.yml` (372 live questions), the audit ledger,
   and the per-book audit docs. If the item is already asked, already decided, or marked
   RESOLVED/APPLIED/MOOT in the sweep — **skip it**. We do not double-up the reviewers' queue.
6. **One bounded unit per iteration.** Process exactly one (theme × book) unit. Small scope =
   small context = less drift. Do not "while I'm here" into other books.

## 2. The funnel (what one iteration does)

Input: one pending unit from the queue (`crossbook_audit.py next`).

1. **Re-read the spine** — this charter + `RULES.md` + the decision doc(s) governing this
   unit's theme + the ledger rows for this book/theme. (Anti-drift anchor.)
2. **Scan (verse depth)** — `crossbook_audit.py next` hands you the unit's refs with their
   current shipped Thai + Hebrew, plus any NT-quote verse for OT↔NT seams. Read them.
3. **Self-check (anti-over-correction)** — for each candidate, decide honestly: *real
   deviation from a DECIDED/locked policy, or legitimate variation?* Default = leave alone.
4. **Second opinion (Gemini)** — for anything that survives step 3 and is non-trivial, get an
   independent read via `scripts/ask_gemini.py` (gemini-2.5-flash). Two-model agreement →
   confident. Disagreement → it becomes a *question*, never an auto-fix.
5. **Classify + route** (see §3), **de-dup** (§1.5), **emit** (§4), **mark the ledger**.

## 3. Classification — conformance vs draft vs question

Ben's setting: **conformance fixes + marked drafts**, all behind the merge gate.

- **CONFORMANCE** — the rendering violates an *already-decided / locked* policy (e.g. a
  human-messenger surface that contradicts a locked term; a missing `ทรง` the doc names).
  → Stage a verse-edit **diff**, tagged `[conformance]`, citing the governing decision.
- **DRAFT** — the policy is *undecided* (a real fork). → Write a **marked `[DRAFT]`
  proposed rendering** AND a review-question `.yml` so the reviewers decide. Never present a
  draft as settled.
- **QUESTION-ONLY** — judgment call with no defensible default → review-question `.yml`, no
  draft.
- **SKIP** — legitimate variation, or already covered (§1.5). Log it; emit nothing.

Everything that changes text is a PROPOSAL. The loop never edits `main`.

## 4. Outputs & the human gate

- Conformance diffs + draft renderings → **ONE rolling PR** on branch `audit/crossbook`,
  titled `[audit] cross-book consistency`, with a checkbox per item (`- [ ]`) appended under
  a per-theme heading. Each iteration pushes its proposals to this same branch (don't open a
  new PR per unit). Mirrors the cursor daily-review contract: **proposed → Ben checks [x] +
  merges → approved → applied.** The loop only *applies* a text change after Ben has checked
  it and it is on `main`. Track proposals in `docs/end_of_book/_audits/crossbook_proposals.md`
  on that branch (the checkbox ledger), so a fresh iteration appends rather than rewrites.
- New review questions → `.yml` in `EremosVercel2/shared/review-questions/` (same schema as
  the 372 existing: `id, tier, roles, kind, topic{en,th}, question{en,th}, body{en,th}`),
  bilingual, **deduped**, in the same PR.
- Decisions Ben makes get recorded in `docs/decisions/` (then a future iteration can treat
  that theme as DECIDED and do conformance instead of asking again).
- **Ledger** (`docs/end_of_book/_audits/crossbook_queue.json`): every unit's status
  (`pending → in_progress → proposed(#PR) → done | skipped`). The ledger is how re-runs avoid
  re-doing work — it is the loop's memory.

## 5. Token-aware pacing (continuous, self-restarting)

The loop runs continuously and restarts itself until the queue is dry. To avoid burning the
budget:

- After each iteration, schedule the next via `ScheduleWakeup`.
- **Normal:** short delay (~60s) — keep moving.
- **Token-heavy iteration** (a big book, many Gemini calls, or a long context): back off
  **600–900s (10–15 min)** before the next unit. This is the throttle Ben asked for — it
  engages *only* when an iteration was expensive, not every time.
- Stop the loop when `crossbook_audit.py status` shows 0 pending, or when a turn's token
  budget is exhausted. Log a one-line summary each iteration (unit, found, routed, skipped).

## 6. Definition of done (per theme, and overall)

- A theme is **done** when every book's unit for it is `proposed` or `skipped`, the
  conformance PR is open for Ben, and any undecided forks are live questions in the queue.
- The **whole-Bible audit** is done when all themes are done, Ben has dispositioned the
  questions, conformance PRs are merged, and `consolidate_whole_bible_audit.py` runs clean.
- Then — and only then — the OT ships to the app (bundle → 17 missing books → manual prod
  import → verify). Shipping is **out of scope for this loop**; it is a separate, Ben-gated step.

## 7. How to start / stop

- **Start (supervised burn-down):** `/loop run the cross-book audit: next unit` — each turn
  the loop does one unit per this charter, opens/updates the PR, and self-schedules the next.
- **Start (unattended cadence):** a scheduled routine (`/schedule`) that runs the same body
  on a cron, proposing into the checkbox PR for phone approval.
- **Stop:** remove the wakeup / disable the routine, or let it stop on a dry queue.
- **Pause is always safe** — nothing is half-applied; all state is in the ledger + open PRs.
