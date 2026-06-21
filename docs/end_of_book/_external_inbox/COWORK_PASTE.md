# Cowork paste block — Eremos Thai Bible external AI review (run Tue & Fri)

_Copy everything in the fenced block below and paste it into a new Cowork browser-agent task.
It is queue-driven: it always reviews whatever books are currently pending, so the same block
works every run. Source of truth: the QUEUE. Full reference playbook (if Cowork wants detail):
<https://github.com/btwinguitarists/eremos-translation/blob/main/docs/COWORK_EXTERNAL_REVIEW_INSTRUCTIONS.md>_

```
You are a browser agent doing external AI review for the Eremos Thai Bible project. Do NOT
analyze the replies yourself — just collect them and save them. Work carefully; never truncate.

PREREQUISITES (if any is not logged in, STOP and tell Ben):
- Gemini — signed in at https://gemini.google.com as benvanscyoc@gmail.com (paid Gemini Pro).
- Grok — signed in at https://grok.com (Ben's paid Grok plan).
- GitHub — signed in at https://github.com as btwinguitarists (owner of eremos-translation).
- (ChatGPT at https://chatgpt.com is optional — include it only if already logged in.)

STEP 0 — Read the work queue (source of truth, ordered oldest-first):
https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/_external_inbox/QUEUE.md
Each entry gives a book CODE and its packet URL. Work top to bottom.
If the queue says "Backlog clear" / "0 books pending": there is nothing to do — stop and tell
Ben "queue empty, nothing to review today." Do NOT invent work or redo old books.

FOR EACH pending book in the queue, do this:
1. Open the book's packet URL (loads as plain text). Select all (Cmd+A), copy (Cmd+C). ~15–28K chars is normal.
2. GEMINI: open https://gemini.google.com → new chat → paste the packet → send. Wait until it
   fully finishes (1–3 min; loading indicator gone). Copy its ENTIRE reply.
3. GROK: open https://grok.com → new chat → paste the SAME packet → send. Wait until done. Copy its ENTIRE reply.
4. (Optional) CHATGPT: if logged in, same again at https://chatgpt.com.
5. SAVE: go to
   https://github.com/btwinguitarists/eremos-translation/new/main/docs/end_of_book/_external_inbox
   Filename EXACTLY: <CODE>_raw.md  (e.g. JER_raw.md, ISA_raw.md, PSA_raw.md)
   File contents — paste this, keeping the ## headings EXACTLY:

   # <CODE> — external AI raw replies
   source: Gemini + Grok (+ ChatGPT) web, via Cowork
   account: benvanscyoc@gmail.com
   date: <today YYYY-MM-DD>
   packet: <the packet URL you copied>

   ## GEMINI

   <Gemini's full reply>

   ## GROK

   <Grok's full reply>

   ## CHATGPT

   <ChatGPT's full reply, or: (skipped — not logged in)>

   Then "Commit directly to the main branch", message: inbox: <CODE> external AI raw (Gemini+Grok). Commit.
6. Next book in the queue. Repeat.

IF a model errors/rate-limits/refuses: still create <CODE>_raw.md, write "(no usable reply — <reason>)"
under that heading, keep the one that worked. If a reply looks cut off, send "continue" and append it.
NEVER enter credentials or solve a CAPTCHA — if you hit a login wall / 2FA / CAPTCHA, STOP and tell Ben.

WHEN DONE: tell Ben how many books you committed (by CODE) and flag any that had problems.
```
