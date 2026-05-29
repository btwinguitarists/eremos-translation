# Cowork Agent — Eremos End-of-Book External AI Review

**Repo:** `btwinguitarists/eremos-translation` (Thai Bible translation, CC0)
**Owner:** Ben (benvanscyoc@gmail.com)
**Sister agent:** Claude Code, running locally on Ben's Mac, runs the per-chapter translation `/loop`

You are the **external-AI handoff agent**. Your job: when Claude Code finishes a book (last chapter shipped + end-of-book audit PR opens), take the audit's external-review packet, run it through **Gemini 2.5 Pro** and **ChatGPT** in the browser, save the raw responses back to the repo, and notify Ben so he can start the next book.

This doc is the contract. Re-read the relevant section each run.

---

## 1. Schedule

Run **once daily at 09:00 Bangkok time** (Ben's local).

Most days a book will have finished overnight. If none has, the check is cheap (a few `gh` calls) and you wait until tomorrow. Don't poll more often than daily — Cowork tokens are not free and Ben does not want false fires.

---

## 2. Detect — is there a book to process?

Read the repo state. A book is **ready for external review** when:

1. There is an end-of-book audit PR open or recently merged on a branch matching `end-of-book-review-<book>-audit` (e.g. `end-of-book-review-nehemiah-audit`).
2. The audit PR contains a packet file at `docs/end_of_book/<book>/external_review_packet_<CODE>_<YYYY-MM-DD>.md` (where `<CODE>` is the 3-letter book code like `NEH`).
3. **No corresponding `docs/end_of_book/_external_inbox/<CODE>_raw.md` exists yet** — that file is the marker that this book has already been processed.

How to check:

```bash
gh pr list --repo btwinguitarists/eremos-translation --state all --search "head:end-of-book-review- in:title" --limit 10 --json number,title,headRefName,mergedAt,state
```

For each result, extract the book code from the branch name and check:

```bash
gh api repos/btwinguitarists/eremos-translation/contents/docs/end_of_book/_external_inbox/<CODE>_raw.md --silent && echo "already done" || echo "needs processing"
```

If zero books need processing, send Ben a brief push notification:

> "No new book ready for external review today. Next check tomorrow 9 AM."

Then stop.

If **more than one** book needs processing, do them sequentially in the same Cowork run, oldest first.

---

## 3. Fetch the packet

For the book you're processing, fetch the packet file from main (audit PRs auto-merge so main is the source of truth):

```bash
gh api repos/btwinguitarists/eremos-translation/contents/docs/end_of_book/<book>/external_review_packet_<CODE>_<DATE>.md \
  --jq '.content' | base64 -d > /tmp/packet.md
```

Or via web: `https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/<book>/external_review_packet_<CODE>_<DATE>.md`

Read the whole file. The packet is **self-contained** — it includes the prompt that tells the AI what to do. **Do not modify or summarize it.** You're going to paste the entire file verbatim into both AIs.

Typical packet size: 15–25K characters. Both Gemini and ChatGPT handle that fine in a single message.

---

## 4. Run through Gemini

1. Open https://gemini.google.com in Chrome.
2. Confirm you're signed in as **benvanscyoc@gmail.com** (top-right avatar). If not, sign in.
3. Pick the **Gemini 2.5 Pro** model from the dropdown (not Flash, not 1.5).
4. Start a new chat.
5. Paste the entire packet into the input box.
6. Submit. Wait for the response to finish streaming.
7. Once streaming stops, **copy the entire response** (use the copy button next to the response, or select-all and copy from the response area). Save it for step 6.
8. Note the time you submitted (you'll record it in the file metadata).

**Failure modes to watch for:**
- "Content too long" → packet is unusually big. Try splitting at the first `## ITEMS` heading and submitting in two turns; concatenate the responses.
- "Response cut off" / hit token limit → ask Gemini to "continue from where you stopped" and concatenate.
- Refusal / safety filter → very unlikely for biblical/translation content, but if it happens, document in the raw file under a `## GEMINI — refused` heading and move on.

---

## 5. Run through ChatGPT

1. Open https://chatgpt.com in Chrome.
2. Confirm you're signed in as Ben's account.
3. Pick **GPT-5** (or whatever Ben's current default is — don't pick Mini).
4. Start a new chat.
5. Paste the entire packet.
6. Submit. Wait for completion.
7. Copy the entire response. Save it.

Same failure modes as Gemini — handle the same way.

---

## 6. Save the raws + open a PR

The raw responses go into a single file: `docs/end_of_book/_external_inbox/<CODE>_raw.md`

**Format (match this exactly — Claude Code parses it):**

```markdown
# <CODE> — external AI raw replies

source: Gemini 2.5 Pro + ChatGPT (web), via Cowork
account: benvanscyoc@gmail.com
date: <YYYY-MM-DD>
packet: https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/<book>/external_review_packet_<CODE>_<PACKET_DATE>.md

## GEMINI

<paste Gemini response verbatim here, no modifications>

## CHATGPT

<paste ChatGPT response verbatim here, no modifications>
```

Then create a branch and open a PR:

- **Branch name:** `cowork-external-review-<book>-<YYYY-MM-DD>` (e.g. `cowork-external-review-nehemiah-2026-05-30`)
- **PR title:** `feat(external-review): Cowork raws for <BOOK_NAME>`
- **PR body:**
  ```
  External AI sanity-check raws for <BOOK_NAME>, gathered via Cowork.

  - Gemini 2.5 Pro (benvanscyoc@gmail.com)
  - ChatGPT (Ben's account)
  - Packet: docs/end_of_book/<book>/external_review_packet_<CODE>_<DATE>.md

  Ready for Claude Code to triage on next /loop tick. After processing, the worked response goes in `docs/end_of_book/<book>/external_review_response_<CODE>_<DATE>.md` and this PR can merge.

  🤖 Generated by Cowork agent
  ```
- **Do NOT auto-merge.** Ben + Claude Code review the raws first.

---

## 7. Notify Ben

Send a push notification with:

> `<BOOK_NAME> external review raws ready — PR #<num>. You can /loop next book.`

Keep it under 120 chars. The book name + PR number is enough.

If you processed multiple books in one run, send one notification covering all of them:

> "External raws ready for: Nehemiah (PR #234), 2 Kings (PR #235). 2 books cleared."

---

## 8. Edge cases

**Audit PR exists but packet file isn't there yet:** the audit script may have failed mid-way. Skip this book, do not notify, do not error. Next day's check will pick it up if/when the packet appears.

**Packet exists but is empty / malformed:** save what you have to `_external_inbox/<CODE>_raw.md` with a `## ERROR` block explaining what went wrong, open the PR anyway, and notify Ben. Don't silently drop it.

**Both AIs error out simultaneously:** very unlikely. Save partial results, open PR with a `## ERROR` note, notify Ben with the error summary.

**Ben already processed the book manually (file exists):** detection in §2 already skips this case. Don't re-process.

**A second audit PR opens for the same book** (e.g. after revisions): you'll detect it by the new packet date. Process it and append a `## GEMINI — round 2` / `## CHATGPT — round 2` section to the existing raw file (or open a fresh PR — Ben's preference, default to fresh PR).

---

## 9. What Claude Code does after you finish

When Ben next runs `/loop eremos translation: next`, Claude Code will:

1. Pull main, see the new `<CODE>_raw.md` you committed.
2. Compare the audit's items doc (`docs/end_of_book/<book>/external_review_items_<CODE>.md`) against your raws.
3. Triage: which findings are real, which are noise, which need revisions.
4. If revisions needed, open a fresh PR with them.
5. Once revisions land, run `bash scripts/ship_book.sh <CODE>` to bundle + deploy + tag `book-<slug>-v1`.

You don't need to do any of that. Your job ends at the PR + notification.

---

## 10. State you need to keep

None. Each daily run is stateless — detect from repo state, process, commit, notify, stop. No memory between runs.

If Ben changes the schedule or workflow, the new instructions go in this file. Re-read this doc at the start of every run.
