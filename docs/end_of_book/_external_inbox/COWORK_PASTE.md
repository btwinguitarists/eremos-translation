# Cowork paste block — Eremos Thai Bible external AI review (run Tue & Fri)

_Copy everything in the fenced block below and paste it into a new Cowork browser-agent task.
It is queue-driven: it always reviews whatever books are currently pending, so the same block
works every run. **No GitHub login needed** — Cowork only reads public files and saves replies
to Ben's local project folder; Claude Code (already authenticated) handles all git commits._

```
You are a browser agent doing external AI review for the Eremos Thai Bible project. Your ONLY
job: paste each book's review packet into Gemini and Grok, collect the full replies, and save
them to Ben's local project folder. Do NOT analyze the replies. Do NOT touch GitHub. Never truncate.

PREREQUISITES (if either chat is not logged in, STOP and tell Ben):
- Gemini — signed in at https://gemini.google.com as benvanscyoc@gmail.com (paid Gemini Pro).
- Grok — signed in at https://grok.com (Ben's paid Grok plan).
(No GitHub, no other logins. The packet URLs below are public and need no sign-in.)

STEP 0 — Read the work queue (public, no login). It lists the books to review and each packet URL:
https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/_external_inbox/QUEUE.md
Work top to bottom. If it says "Backlog clear" / "0 books pending": stop and tell Ben
"queue empty, nothing to review today." Do NOT invent work or redo old books.

FOR EACH pending book in the queue:
1. Open the book's packet URL (loads as plain text). Select all (Cmd+A), copy (Cmd+C). ~15-28K chars is normal.
2. GEMINI: https://gemini.google.com -> new chat -> paste -> send. Wait until fully done
   (1-3 min; loading indicator gone). Copy its ENTIRE reply.
3. GROK: https://grok.com -> new chat -> paste the SAME packet -> send. Wait until done. Copy its ENTIRE reply.
4. SAVE to Ben's local folder as a new text file (NOT GitHub):
   /Users/benvanscyoc/thai-bible-ai/docs/end_of_book/_external_inbox/<CODE>_raw.md
   (e.g. JER_raw.md, ISA_raw.md). Use the book CODE from the queue. File contents, keeping the
   ## headings EXACTLY:

   # <CODE> — external AI raw replies
   source: Gemini + Grok (web), via Cowork
   account: benvanscyoc@gmail.com
   date: <today YYYY-MM-DD>
   packet: <the packet URL you copied>

   ## GEMINI

   <Gemini's full reply>

   ## GROK

   <Grok's full reply>

5. Next book. Repeat.

IF YOU CANNOT WRITE LOCAL FILES: instead, at the end, output ALL the collected replies in
this same format in your final message (each book under a clear "===== <CODE> =====" header),
so Ben can copy them in one go. Do NOT silently skip saving.

IF a model errors/rate-limits/refuses: still record that book; under that model's heading write
"(no usable reply — <reason>)" and keep the one that worked. If a reply looks cut off, send
"continue" and append it. NEVER solve a CAPTCHA or enter credentials — if you hit a login wall,
STOP and tell Ben which site.

WHEN DONE: tell Ben how many books you saved (by CODE) and where (local files, or pasted in chat),
and flag any problems. Then Ben tells Claude Code "ingest the reviews."
```
