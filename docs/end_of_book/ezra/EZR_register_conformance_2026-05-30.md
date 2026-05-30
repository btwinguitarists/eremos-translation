# EZRA — foreign-monarch register conformance (§2.2)

**Date:** 2026-05-30 · **Triggered by:** DANIEL + ESTHER end-of-book external AI review (Gemini 2.5 Pro + ChatGPT via Cowork) · **Applied by:** Claude Code.

## What this is (and is not)

The Daniel and Esther reviewers both raised the **foreign-monarch register** as their MAJOR/CONCERN item — but **neither flagged Daniel or Esther as wrong.** Both books correctly apply full ราชาศัพท์ (ทรง) to the Persian/Babylonian emperors per the **already-written `ot_register_policy_2026-05.md` §2.2** ("Foreign emperors … ราชาศัพท์ (ทรง) — they are the imperial sovereigns of their narratives, even if villainous"). The unanimous finding: **Ezra is the lone outlier**, using plain action-verbs for the same emperors (Cyrus, Darius, Artaxerxes, Ahasuerus) and creating cross-book "canonical whiplash" inside the Ezra–Nehemiah–Esther–Daniel block.

**This is therefore a conformance fix, not a new editorial decision.** It is the **mirror image of §2.5** (the Joseph-vizier correction): there the Genesis audit *stripped* wrongly-granted ทรง- from a patriarch; here Ezra's foreign emperors were *missing* the ทรง- that §2.2 requires. Same class of fix — strict compliance with settled policy.

## Scope finding (smaller than the reviewers implied)

Ezra **already** uses royal register at the noun/pronoun level throughout: พระราชกฤษฎีกา, พระราชสาส์น, พระราชโองการ, ประทาน, พอพระทัย, พระองค์ (e.g. 4:6 — the verse the reviewers specifically cited — already uses the royal pronoun พระองค์). The actual gap was a handful of **narrator-voice emperor action-verbs** missing ทรง.

## Verses changed (7 verses, 8 verb-markings)

| Verse | Before | After | Subject |
|---|---|---|---|
| 1:2 | …กล่าวดังนี้ว่า | …**ตรัส**ดังนี้ว่า | Cyrus (royal quotative) |
| 1:7 | …ยัง**ได้นำ**เครื่องใช้…ออกมา | …ยัง**ทรงนำ**เครื่องใช้…ออกมา | Cyrus |
| 1:8 | …**ได้ให้**มิทเรดาท…นำ…ออกมา | …**ทรงให้**มิทเรดาท…นำ…ออกมา | Cyrus |
| 5:13 | ไซรัส**ได้ออก**พระราชกฤษฎีกา… | ไซรัส**ทรงออก**พระราชกฤษฎีกา… | Cyrus |
| 5:14 | **ได้นำ**ออก… **มอบให้**… ซึ่งไซรัส**ได้แต่งตั้ง** | **ทรงนำ**ออก… **ทรงมอบให้**… ซึ่งไซรัส**ทรงแต่งตั้ง** | Cyrus (×3) |
| 6:1 | กษัตริย์ดาริอัสจึง**สั่ง**ให้ค้น | กษัตริย์ดาริอัสจึง**ทรงบัญชา**ให้ค้น | Darius |
| 6:3 | ไซรัส**ได้ออก**พระราชกฤษฎีกา… | ไซรัส**ทรงออก**พระราชกฤษฎีกา… | Cyrus |

## Left as-is (deliberate)

- **Hebrew-servant viziers** (Ezra, Zerubbabel, Sheshbazzar) — remain plain per §2.2 + §2.5. Not touched.
- **Sub-imperial officials** (Tattenai, Rehum, Shimshai) — remain plain. Not touched.
- **Temporal / genitive references** ("ในรัชกาลของ…", "พระราชกฤษฎีกาของ…") — no verb to mark; not touched.
- **Subjects' deferential address to the king** in the Aramaic letters (ขอกราบทูล…) — already correct commoner-to-king register.
- **A few borderline subordinate/character-speech clauses** (1:1 result-clause, 3:7 / 4:3 relative clauses, 5:5, 6:13) — left for a native-Thai reviewer's judgment; flagged here rather than force-edited.

## Name spelling — checked, consistent

Ezra's only Ahasuerus/Xerxes reference (4:6) is spelled **อาหสุเอรัส**, matching Esther. No cross-book name-spelling drift. ("เซอร์ซีส" appears only as a substring of อารทาเซอร์ซีส/Artaxerxes.)

## Verification & gate

`run_checks.py --skip-back-translation` green on ezra 1, 5, 6 — including **Honorifics binding (Rachasap)**, which validates the new ทรง markings.

**Recommended merge gate:** because this retroactively edits a previously-shipped book's royal register, a **native-Thai reviewer pass on the royal phrasing** is the right final check before merge. The conformance basis (§2.2) is settled; the phrasing naturalness is the open question. Left as a PR for the maintainer's explicit ratification rather than self-merged.

*Forward protection: `ot_register_policy_2026-05.md` §2.6 (added in this PR) tags Ezra–Nehemiah–Esther–Daniel as a unified register block.*
