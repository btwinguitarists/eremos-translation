# DANIEL — external AI review triage & response

**Date:** 2026-05-30 · **Reviewers:** Gemini 2.5 Pro + ChatGPT (via Cowork) · **Raw:** `docs/end_of_book/_external_inbox/DAN_raw.md`
**Triaged by:** Claude Code. Both reviewers judged **Daniel's own treatment correct** on every axis; the one MAJOR item points outward at **Ezra**, not Daniel.

| Item | Verdict | Disposition | What changed |
|---|---|---|---|
| **A** — Foreign-monarch register (full ราชาศัพท์ for Gentile emperors) | MAJOR (Gem) / CONCERN (GPT) | **Daniel LOCKED; fix is in EZRA** | Both reviewers affirm Daniel's full ราชาศัพท์ for Nebuchadnezzar/Belshazzar/Darius/Cyrus is **correct** per `ot_register_policy §2.2`. The "canonical whiplash" is **Ezra's non-compliance**, not Daniel. Handled as a §2.2 **conformance fix in a separate Ezra PR** (see `EZR_register_conformance_2026-05-30.md`). No Daniel edits. |
| **B** — "Son of man" (7:13) light divine register vs. "man in linen" (10:5–6) plain | FINE ×2 | **LOCKED** | No change. บุตรมนุษย์ (7:13 messianic) vs บุตรแห่งมนุษย์ (8:17 mortal idiom) distinction maintained; 10:5–6 kept plain (preserves christophany/angelophany ambiguity). Per `son_of_man_disambiguation_2026-04.md`. |
| **C** — Seventy weeks: מָשִׁיחַ → ผู้ถูกเจิม (generic), not พระคริสต์ | FINE (Gem) / CONCERN (GPT) | **APPLIED** | Kept ผู้ถูกเจิม in 9:25–26 text (optimal-equivalence). Added the reader-facing Layer-2 footnote at **9:25** (`textual_variants/daniel_09.json`) the existing `key_decisions` already promised ("ดูหมายเหตุ") — notes the mainstream messianic reading + the 9:26 "cut off"→Christ's death connection, while keeping the Hebrew surface generic. |
| **D** — Greek Additions excluded silently | CONCERN (Gem) / MAJOR (GPT) | **APPLIED** | Exclusion is correct (MT-base); silence was the gap. Added reader-facing disposition `notes` at **Daniel 1:1** (MT/Aramaic base; excludes Prayer of Azariah, Song of the Three, Susanna, Bel & the Dragon — mirrors Esther 1:1) and a **3:23 seam note** flagging the Greek insertion of Azariah/Song-of-the-Three between 3:23 and 3:24. |
| **§Z** — Aramaic transition footnotes (2:4b, 8:1) | note ×1 | **APPLIED (2:4) / already present (8:1)** | 8:1 already carried the Aramaic→Hebrew return note. Added the matching Hebrew→Aramaic note at **2:4b** (begins the 2:4b–7:28 Aramaic section). |

**Verification:** `run_checks.py` re-run on daniel 1, 2, 3, 9 — all local checks green.

**Net:** 4 of 5 items applied/locked in Daniel itself; Item A's actual fix is the cross-referenced **Ezra register-conformance PR** (the only item touching a previously-shipped book — isolated for the maintainer's explicit review).
