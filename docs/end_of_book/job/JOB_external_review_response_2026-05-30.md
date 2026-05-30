# JOB — external AI review triage & response

**Date:** 2026-05-30 · **Reviewers:** Gemini 2.5 Pro + ChatGPT (via Cowork) · **Raw:** `docs/end_of_book/_external_inbox/JOB_raw.md`
**Triaged by:** Claude Code. Both reviewers converged: *"the real fixes are documentation/disclosure rather than major translation reversal."* No DECIDE-level items.

| Item | Verdict | Disposition | What changed |
|---|---|---|---|
| **A** — `הַשָּׂטָן` → ซาตาน flattens the article's role-sense | CONCERN ×2 | **APPLIED** | Layer-2 footnote at **Job 1:6** (`output/textual_variants/job_01.json`) noting the definite-article role "ผู้กล่าวหา/ปฏิปักษ์"; new lock doc **`satan_accuser_corpus_mapping_2026-05.md`** mapping the celestial accuser → ซาตาน vs. the common-noun adversary → ปฏิปักษ์ (protects Zech 3 + 1 Kgs 11). |
| **B** — Shaddai standalone-title drift (bare vs องค์-) | CONCERN ×2 | **APPLIED** | Normalized the **6 bare occurrences** (5:17, 6:4, 6:14, 8:3, 8:5, 11:7) → **องค์ผู้ทรงมหิทธิฤทธิ์**, matching the 25 already-prefixed. Locked the standalone-title form (vs. embedded אֵל שַׁדַּי) in **`divine_names_table_2026-05.md`**. 0 El-Shaddai compounds in Job — no corruption risk. |
| **C** — mediator/Redeemer register asymmetry | FINE ×2 | **LOCKED + documented** | No verse edits. New doc **`job_mediator_thread_2026-05.md`** formalizing: hypothesized/absent third-party (9:33, 16:19, 33:23) = plain register; confessed heavenly vindicator (19:25) = royal. |
| **D** — 13:15 ketiv/qere; 23:2 BSB-over-MT | CONCERN (13:15) / FINE (23:2) | **APPLIED (13:15) + LOCKED (23:2)** | New reader-facing Tier-2 footnote at **Job 13:15** (`output/textual_variants/job_13.json`) noting the ketiv "ข้าไม่มีความหวัง" alternative. 23:2 locked as-is (its existing verse-note is proportionate per `mt_vs_lxx_textual_variant_handling §2.3`). |

**Verification:** `run_checks.py` re-run on job 5, 6, 8, 11 (text-changed) — all 6 local checks green (back-translation skipped: no API key in this env). Footnote-only chapters (1, 13) validated as well-formed JSON.

**Net:** 4 of 4 items resolved. 6 verse normalizations + 3 footnotes + 1 table lock + 2 new decision docs. Nothing deferred.
