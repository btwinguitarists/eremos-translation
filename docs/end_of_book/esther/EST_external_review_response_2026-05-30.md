# ESTHER — external AI review triage & response

**Date:** 2026-05-30 · **Reviewers:** Gemini 2.5 Pro + ChatGPT (via Cowork) · **Raw:** `docs/end_of_book/_external_inbox/EST_raw.md`
**Triaged by:** Claude Code. As with Daniel, **Esther's own treatment is judged correct**; the MAJOR item is Ezra's inconsistency, not Esther.

| Item | Verdict | Disposition | What changed |
|---|---|---|---|
| **A** — Persian monarch honorifics across the corpus | MAJOR (Gem) / CONCERN (GPT) | **Esther LOCKED; fix is in EZRA** | Both reviewers affirm Esther's full ราชาศัพท์ for Ahasuerus follows the written `ot_register_policy §2.2` correctly; **Ezra is the outlier** (e.g. EZR 4:6 names the same Ahasuerus/Xerxes). Handled as a §2.2 **conformance fix in a separate Ezra PR** (`EZR_register_conformance_2026-05-30.md`). No Esther edits. |
| **B** — דָּת (law/decree) + the "irrevocable" motif | CONCERN ×2 | **APPLIED (motif) + tracked (clustering)** | **Harmonized the irrevocability leitwort**: Esther 1:19 "เพื่อจะเปลี่ยนแปลงไม่ได้" → **"เพื่อจะเพิกถอนไม่ได้"**, matching 8:8 (אֵין לְהָשִׁיב), so the structural hinge (the king cannot revoke his own law) reads identically at both poles. The broader 5-way דָּת tightening is **tracked as a deferred Esther key-term review** (lower priority per both reviewers — "prioritize the 1:19/8:8 motif"); not done here to avoid over-editing shipped verses. |
| **C** — LXX Additions disclosure | FINE (Gem) / FINE+doc (GPT) | **LOCKED as-is** | The existing Esther 1:1 `notes` (MT base; excludes the LXX additions per RULES §0) is sufficient and correct. Gemini: a redundant book-level note "would clutter a canonical boundary the 1:1 note already successfully defends." No change. |
| **D** — Hidden divine-name acrostics | FINE (Gem) / CONCERN (GPT) | **LOCKED as-is (minor maintainer option)** | Split verdict. Chose Gemini's position: the book's theological power *is* its surface silence about the divine name; footnoting the Masoretic letter-acrostics (1:20; 5:4; 5:13; 7:7; אהיה 7:5) crosses from optimal-equivalence translation into study-bible commentary and undermines the author's deliberate ambiguity. Aligns with project philosophy (let the text speak). **Maintainer note:** if Ben prefers scholarly transparency, a single book-level acrostic note can be added later — flagged, not unilaterally applied. |

**Verification:** `run_checks.py` re-run on esther 1 — all local checks green.

**Net:** 1 verse harmonized (the priority motif fix); 2 items locked as-is with rationale; 1 cross-referenced to the Ezra register-conformance PR; 1 sub-item (דָּת clustering) tracked as deferred.
