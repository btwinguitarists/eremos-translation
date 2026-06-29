# Zechariah (ZEC) — external AI review response

**Reviewer:** gemini-2.5-flash (Gemini API, independent of the translating model)
**Date:** 2026-06-27  |  **Packet:** `docs/end_of_book/zechariah/external_review_packet_ZEC_2026-06-27.md`  |  finishReason: STOP

> Auto-run via scripts/run_book_review_gemini.py. The main session reads this and decides what to act on; nothing is auto-applied to the translation.

---

## Item A: מַלְאַךְ יְהוָה rendered ทูตขององค์พระผู้เป็นเจ้า (drops สวรรค์): theophanic distinction vs corpus lock
**Verdict:** CONCERN
**Reasoning:** The Zechariah translation's deliberate distinction for the theophanic `מַלְאַךְ יְהוָה` (dropping `สวรรค์`) aligns with common evangelical theological interpretations of this unique figure. However, this directly conflicts with the existing corpus lock `malak_yhwh_2026-05.md`, which mandates `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า` for the compound, creating a significant corpus-level inconsistency.
**Recommended action:** Re-evaluate `malak_yhwh_2026-05.md` to establish a specific carve-out for the theophanic `מַלְאָךְ יְהוָה` (e.g., in Zechariah 1-6, 12:8, and similar Christophany passages) to be rendered as `ทูตขององค์พระผู้เป็นเจ้า`. For corpus consistency, conduct a targeted review of already-shipped books (Genesis, Exodus, Judges, 2 Kings) for instances of theophanic `מַלְאָךְ יְהוָה` to apply this revised rendering, with Ben deciding on the scope of the back-sweep.

## Item B: Messianic / NT-citation reception at maximal density: policy ratification + the 12:10 me/him crux
**Verdict:** FINE
**Reasoning:** The translation's discipline of rendering the Hebrew text faithfully in the body, employing non-committal language for messianic figures/prophecies, and using Layer-2 footnotes for NT reception and Christological identification is a robust and transparent approach. This adheres to the project's MT-primary rule and provides necessary theological context without imposing later interpretations directly into the source text. For 12:10, preserving the MT's "look on me" while footnoting the NT's "look on him" is consistent with the project's base-text decisions.
**Recommended action:** Lock as-is. This approach sets a strong, transparent precedent for handling messianic prophecies and NT citations in future OT books.

## Item C: Satan article-role footnote at Zechariah 3:1 — doc-mandated note appears absent
**Verdict:** CONCERN
**Reasoning:** The `satan_accuser_corpus_mapping_2026-05.md` document explicitly mandates a first-occurrence Layer-2 footnote at Zechariah 3:1 to explain the definite article and role-sense of `הַשָּׂטָן` (ผู้กล่าวหา / ปฏิปักษ์), mirroring Job 1:6. The existing `nt_citation_note` at 3:2 for Jude 9 serves a different purpose and does not fulfill this distinct requirement, leaving a critical linguistic and theological transparency point unaddressed for the reader.
**Recommended action:** Add a dedicated Layer-2 first-occurrence footnote at Zechariah 3:1, noting that `הַשָּׂטָן` includes a definite article, indicating a role ("the accuser" / "the adversary") rather than solely a proper name in this context, and referencing Job 1:6.

## Item D: Zechariah 11:13 potter/treasury and 12:10 me/him: MT-primary textual choices
**Verdict:** FINE (for MT-primary choice) / CONCERN (for 11:13 footnote completeness)
**Reasoning:** The decision to translate the MT-primary readings ("potter" in 11:13 and "me" in 12:10) is entirely consistent with the project's foundational RULES §0 (MT-primary) and `mt_vs_lxx_textual_variant_handling_2026-05` §2.3. The footnotes are the correct place for discussing textual variants and NT reception. However, for 11:13, while the existing `nt_citation_note` implicitly addresses the variant's outcome, an explicit `textual_variant`-type footnote detailing the Hebrew consonantal fork (`הַיּוֹצֵר` vs. `הָאוֹצָר`) would enhance transparency and align with the more comprehensive approach taken for 12:10.
**Recommended action:** Lock the MT-primary body text renderings as-is. Add a distinct Layer-2 `textual_variant` footnote at Zechariah 11:13 to explicitly mention the Hebrew consonantal variant (potter/treasury) alongside the existing `nt_citation_note`.

---
## §Z: Anything else?
No additional corpus-level concerns were identified beyond the specific items raised in the review packet. The project's extensive locked decisions and consistent application of rules appear to cover most potential issues.
