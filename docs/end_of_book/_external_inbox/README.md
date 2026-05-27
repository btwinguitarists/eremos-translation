# External AI review — inbox (handoff between Cowork and Claude Code)

This folder is the **drop zone** between the two halves of the end-of-book external
AI review:

1. **Cowork (browser agent)** gathers raw replies from Gemini + ChatGPT and drops one
   file here per book: **`<CODE>_raw.md`** (e.g. `GEN_raw.md`, `1SA_raw.md`).
2. **Claude Code** picks each file up, cross-checks every claim against the translation
   JSONs, and writes the worked-through outcome to
   `docs/end_of_book/<book>/external_review_response_<CODE>_<date>.md` — which is the
   real DONE marker for that book.

## Files here

| File | Written by | Purpose |
|---|---|---|
| `QUEUE.md` | `scripts/external_review_status.py` | Ordered work list (oldest debt first) with the exact packet URL per book. Re-generated; do not hand-edit. |
| `<CODE>_raw.md` | Cowork | Raw Gemini + ChatGPT replies for one book. Provenance + Claude Code's input. |
| `_TEMPLATE_raw.md` | — | The exact shape a `<CODE>_raw.md` file must take. |

## `<CODE>_raw.md` format (must match `_TEMPLATE_raw.md`)

The two reply sections are delimited by `## GEMINI` and `## CHATGPT` headings so Claude
Code can parse them mechanically. Paste each model's **complete** reply, untruncated.

## Rules

- These raw files are **inputs and provenance**, not the deliverable. The worked response
  in the book's own folder is what counts as the review being done.
- Claude Code never auto-applies verse edits from these. Findings become a **proposed**
  action list in the response doc for Ben's sign-off (shipped/locked surfaces are sacred).
- To see what's still outstanding at any time: `python3 scripts/external_review_status.py`.
