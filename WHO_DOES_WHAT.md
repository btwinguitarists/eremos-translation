# Who does what

This is the **first file a new collaborator should read.** It maps roles to the files you should open first. Find your role below, read the three or four files listed, and ignore the rest until you need them.

The repo looks bigger than it is. There are really only **three kinds of people** working on this translation project, and each one only touches a small slice of the tree.

---

## Find your role

| If you are... | Read these first | Then go here to do work |
|---|---|---|
| **A native Thai speaker, lay reader, or pastor** giving feedback on whether the translation sounds natural and faithful | `README.md`, the relevant book in `output/reader/` | The review form (link in the onboarding manual) — answer questions one at a time |
| **A Thai-speaking editor or theologian** weighing in on cross-cutting choices (key terms, register, transliteration) | `RULES.md`, `docs/translator_decisions/`, the relevant book in `output/reader/` | Same review form, plus optional PRs against `docs/translator_decisions/` |
| **A Greek/biblical-studies scholar** reviewing methodology and exegesis | `README.md`, `RULES.md`, the latest `docs/reviewer_packet_en_*.md` | Reply by email or comments on the packet — you don't need a GitHub account |
| **A maintainer** running the translation pipeline | `docs/TRANSLATION_WORKFLOW.md`, `STATUS.md`, `docs/END_OF_BOOK_CHECKLIST.md` | The pipeline scripts in `scripts/` — start with `ship_chapter.sh` |
| **A Thai-language UI contributor** fixing how Thai text appears in the Eremos app | (this repo not relevant) | The `EremosVercel2` repo — branch + PR + Vercel preview |

If none of those describe you, the manual at the URL below has a longer chapter for newcomers.

---

## Roles, in plain language

### Maintainer
Runs the translation pipeline. Triggers each chapter, reviews the automated check reports, ships chapters, runs end-of-book audits, and shepherds external reviewer feedback back into the corpus. **One person at a time** holds this role; today that's the project owner.

### Native-speaker reviewer
Reads completed chapters in `output/reader/` and answers editorial questions in the web review form. Tier-A questions (register, rhythm, naturalness) are the sweet spot — they require a native ear and don't require theology training. **Several reviewers help here**, and the more the better.

### Theological reviewer
A pastor or trained theologian who answers tier-B questions (translation choices for technical Greek terms — `dikaiosyne`, `parakletos`, `pistis Christou`, etc.). These take longer than tier-A and require some Greek or seminary background. **One to three reviewers** is the right size.

### Editor
A Thai editor — ideally with translation experience — who weighs in on cross-cutting style: when to use formal vs. familiar register, how to transliterate proper nouns, whether one Greek word should consistently map to one Thai word. Answers tier-C questions in the review form, and may open PRs against `docs/translator_decisions/`. **One reviewer**, ideally.

### Greek/biblical-studies scholar
Reads a per-book "reviewer packet" (a self-contained PDF/Markdown bundle in `docs/reviewer_packet_en_*.md`) and replies in plain English. Doesn't touch GitHub. **One to three reviewers per book** is plenty.

### Thai UI contributor
Different repo (`EremosVercel2`), different rhythm. Notices when the app shows awkward Thai phrasing or layout, opens a branch + PR, the maintainer reviews and merges. Doesn't need to know anything about the translation pipeline.

---

## The workflow at a glance

1. **Translate** — maintainer triggers a chapter; the pipeline drafts a translation from Greek, runs automated consistency checks, and writes a check report.
2. **AI review (per chapter)** — maintainer pastes the chapter into an external AI (Gemini, ChatGPT, etc.) using the prompt at `docs/CHAPTER_REVIEW_PROMPT.md`. Findings either become locked decisions or new questions for human reviewers.
3. **Ship** — chapter is committed, the reader edition (`output/reader/<book>.md`) gets regenerated, and any new reviewer questions get queued in the app's question bank.
4. **Human review (async)** — reviewers visit the form on their own schedule and answer questions one at a time. Their answers persist between sessions.
5. **End-of-book audit** — when the last chapter of a book ships, the maintainer walks `docs/END_OF_BOOK_CHECKLIST.md` before starting the next book. This is where corpus-level decisions get locked in.

You don't have to understand every step to contribute. A native-speaker reviewer only touches step 4.

---

## Where things live

```
.
├── README.md                  ← project overview
├── RULES.md                   ← sacred translation rules — never edit casually
├── STATUS.md                  ← auto-generated dashboard of progress
├── WHO_DOES_WHAT.md           ← you are here
├── docs/
│   ├── TRANSLATION_WORKFLOW.md     ← maintainer's pipeline
│   ├── END_OF_BOOK_CHECKLIST.md    ← end-of-book audit ritual
│   ├── CHAPTER_REVIEW_PROMPT.md    ← prompt for external AI per-chapter review
│   ├── translator_decisions/       ← locked corpus-level rules (one file per decision)
│   ├── end_of_book/<book>/         ← per-book audit + external review packets
│   ├── reviewer_packet_en_*.md     ← packet for English-reading scholars
│   └── reviewer_packet_th_*.md     ← packet for Thai-language reviewers
├── scripts/                   ← pipeline scripts (maintainer territory)
├── sources/                   ← Greek manuscripts + reference Bibles (read-only)
├── data/                      ← lookup tables (citations, parallels, production order)
└── output/
    ├── reader/<book>.md       ← FINAL reading edition for end users
    ├── plain/<book>.md        ← verses-only edition for impressionistic reading
    ├── feedback/<book>.md     ← per-verse review edition (with comment blocks)
    └── (other dirs are intermediate artifacts; you can ignore them)
```

The three things most reviewers ever open are `README.md`, `RULES.md`, and the relevant book in `output/reader/`. Everything else is plumbing.

---

## What I'm asked to do, and what I'm not

If you're new, **the most useful thing you can do is be a reviewer.** The translation pipeline does not need more cooks; the review queue does. The form is built so that a reviewer can answer one question, close the laptop, come back a week later, and pick up where they left off.

**Do not edit:**
- `RULES.md` — locked, change requires maintainer review and a corpus-level decision
- `docs/translator_decisions/*.md` — same
- `output/translations/*.json` — pipeline-generated, edit upstream not here
- Anything in `sources/` — read-only manuscripts and reference data

**Feel free to edit (with a PR):**
- This file (`WHO_DOES_WHAT.md`) if a role is unclear or missing
- The onboarding manual (separate repo)
- Translator decision proposals — open as a new file in `docs/translator_decisions/` with a `proposed-` prefix; the maintainer reviews and either accepts (renames to drop the prefix) or closes

---

## Where to ask questions

- **Setup or onboarding questions:** the onboarding manual (private repo — get the link from the maintainer)
- **Translation questions a Thai reader would care about:** the review form (link in the manual)
- **A Greek/textual question or methodology question:** open a GitHub issue on this repo
- **A bug in the Eremos app's Thai text:** open an issue on the `EremosVercel2` repo

If you don't know which is which, ask the maintainer.
