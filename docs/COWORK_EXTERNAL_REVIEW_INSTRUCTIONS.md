# Cowork playbook — gather external AI reviews (Gemini + ChatGPT)

**You are a browser agent.** Your whole job: for each book in the work queue, copy a
review packet, paste it into **Gemini** and **ChatGPT**, wait for each to finish, copy
both replies, and save them into the project repo. You do **not** analyze the replies —
Claude Code does that afterward. Work carefully and never truncate a reply.

## Before you start (prerequisites)

- **Gemini** — be signed in at <https://gemini.google.com> as **benvanscyoc@gmail.com**.
- **ChatGPT** — be signed in at <https://chatgpt.com>.
- **GitHub** — be signed in at <https://github.com> as **btwinguitarists** (owner of the
  `eremos-translation` repo) so you can commit the results.

If any of those is not logged in, **stop and tell Ben** instead of guessing.

## The work queue

Open and read this list — it is the source of truth, ordered oldest-first:

<https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/_external_inbox/QUEUE.md>

Each entry gives you: the **packet URL to copy**, and the **filename to save to**. Work top
to bottom. (If you can only finish some in one session, that's fine — the next run picks up
where the list still shows work.)

**If the queue reads "0 books pending" / "Backlog clear":** there is nothing to do this run.
Stop and tell Ben "queue empty, no books to review today." This is the expected state most
days — books don't ship daily, so the queue is normally empty until a new book finishes
translating. **Do not invent work, retry old books, or modify already-committed responses.**

Ben can run this on any cadence (daily / weekly / on book-ship). The mechanism is idempotent
on an empty queue.

---

## Per-book loop — do this for each book in the queue

### Step 1 — Copy the packet
1. Open the book's packet URL (the "Copy this:" link in the queue). It loads as plain text.
2. Select **all** of it (Cmd+A) and copy (Cmd+C). It's ~15–20K characters — that's normal
   and within what both chat services accept in one paste.

### Step 2 — Gemini
1. Go to <https://gemini.google.com>. Start a **new chat**.
2. Paste the packet. Send it.
3. **Wait for it to fully finish.** It may take 1–3 minutes. It is done when the text stops
   growing and the input box is ready again (the stop/loading indicator is gone). Do not
   copy mid-stream.
4. Select and copy Gemini's **entire** reply.

### Step 3 — ChatGPT
1. Go to <https://chatgpt.com>. Start a **new chat**.
2. Paste the **same packet** (re-copy from the packet tab if needed). Send it.
3. Wait for it to fully finish (the streaming stop-button reverts to the send/compose
   state). Again, 1–3 minutes is normal.
4. Select and copy ChatGPT's **entire** reply.

### Step 4 — Save both replies to the repo
1. Go to: `https://github.com/btwinguitarists/eremos-translation/new/main/docs/end_of_book/_external_inbox`
   (this opens GitHub's "create new file" screen already pointed at the inbox folder).
2. **Filename:** `<CODE>_raw.md` exactly — the queue gives the CODE (e.g. `GEN_raw.md`,
   `1SA_raw.md`, `1JN_raw.md`).
3. **File contents:** paste this, filling in the blanks and the two replies:

   ```
   # <CODE> — external AI raw replies

   source: Gemini + ChatGPT (web), via Cowork
   account: benvanscyoc@gmail.com
   date: <today's date YYYY-MM-DD>
   packet: <the packet URL you copied>

   ## GEMINI

   <paste Gemini's full reply>

   ## CHATGPT

   <paste ChatGPT's full reply>
   ```

4. Keep the headings `## GEMINI` and `## CHATGPT` **exactly** — Claude Code splits the file
   on them. Paste each reply in full; never shorten or summarize.
5. Scroll down, choose **"Commit directly to the `main` branch"**, commit message
   `inbox: <CODE> external AI raw (Gemini+ChatGPT)`, and commit.

### Step 5 — Next book
Move to the next entry in the queue and repeat.

---

## Handling problems (don't guess — degrade gracefully)

- **A model errors, rate-limits, or refuses:** still create the `<CODE>_raw.md` file; under
  that model's heading write `(no usable reply — <short reason>)` and fill in the one that
  worked. A single-model file is still useful. Note it for Ben.
- **A reply looks cut off** (ends mid-sentence): in that chat, send `continue`, wait, and
  append the continuation so the saved reply is complete.
- **The packet seems too long to paste:** it isn't — both services accept it. If a UI truly
  rejects it, note that for Ben and move on; do not split the packet (it must be reviewed
  whole).
- **You're unsure about anything** (which account, a login wall, a CAPTCHA, a 2FA prompt):
  **stop and tell Ben.** Do not enter credentials or solve a CAPTCHA on your own.

## What "done" looks like

One `<CODE>_raw.md` committed to `docs/end_of_book/_external_inbox/` per book, each with a
complete Gemini reply and a complete ChatGPT reply (or a noted reason one is missing). When
you've worked the whole queue, tell Ben how many you completed and flag any that had issues.

---

### Worked example — Genesis (`GEN`)

1. Copy: <https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/genesis/external_review_packet_GEN_2026-05-11.md>
2. Paste → Gemini, wait, copy reply.
3. Paste → ChatGPT, wait, copy reply.
4. New file `GEN_raw.md` in `docs/end_of_book/_external_inbox/`, both replies under the two
   headings, commit to `main`.

> **Alternative save method:** if your Cowork has direct access to Ben's local files, you
> may instead just write the same `<CODE>_raw.md` into the local folder
> `~/thai-bible-ai/docs/end_of_book/_external_inbox/` — skip the GitHub web steps. Either
> way the file must match the format above.
