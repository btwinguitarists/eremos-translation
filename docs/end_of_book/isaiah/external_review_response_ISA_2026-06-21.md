# Isaiah (ISA) — external AI review response

**Reviewer:** gemini-2.5-flash (Gemini API, independent of the translating model)
**Date:** 2026-06-21  |  **Packet:** `docs/end_of_book/isaiah/external_review_packet_ISA_2026-06-05.md`  |  finishReason: STOP

> Auto-run via scripts/run_book_review_gemini.py. The main session reads this and decides what to act on; nothing is auto-applied to the translation.

---

## Item A: Messianic committal-surface policy (and a cross-book asymmetry with Daniel)
**Verdict:** CONCERN
**Reasoning:** Isaiah's internal policy for messianic passages is coherent and aligns with the project's stated preference for evangelical-consensus readings in the main text, with the 9:6 summary remaining descriptive. However, the cross-book asymmetry with Daniel 9:25-26's generic rendering of מָשִׁיחַ creates an inconsistency. While Daniel's context allows for a near-horizon referent, the evangelical consensus for Daniel 9:25-26 ultimately points to Christ, making the current generic rendering less aligned with the project's overall "committal evangelical-consensus" policy than Isaiah's approach.
**Recommended action:** Revisit Daniel 9:25-26 to align its rendering of מָשִׁיחַ with the project's committal evangelical-consensus policy, potentially using a term like "พระเมสสิยาห์" or "พระคริสต์" in the main text, with a footnote to describe the interpretive nuances and near-horizon referents.

## Item B: Divine-anthropomorphism register drift: God's "arm" and "Spirit" in first-person divine speech
**Verdict:** MAJOR CONCERN
**Reasoning:** The drift to plain register (แขน, วิญญาณ) for God's "arm" and "Spirit" in first-person divine speech (e.g., 51:5, 63:5, 42:1, 59:21) directly violates the locked corpus decision for Hebrew anthropomorphisms: "royal-Thai พระหัตถ์ / พระเนตร / พระโอษฐ์ / พระบาท (matches Rachasap when divine possessor)." The divine possessor remains YHWH regardless of first- or third-person reference. This inconsistency is particularly stark when plain and royal forms appear in close proximity (e.g., 51:9 vs 52:10).
**Recommended action:** Spot-revise all instances of divine "arm" (זְרוֹעַ) and "Spirit" (רוּחַ) to consistently use the royal register (พระกร, พระวิญญาณ) when the possessor is God, including in first-person divine speech.

## Item C: שָׂעִיר (goat-demon / "satyr"): demonic vs naturalized rendering in the two desert-ruin oracles
**Verdict:** CONCERN
**Reasoning:** The inconsistent rendering of שָׂעִיר as "goat-demons" (ผีปีศาจรูปแพะ) at 13:21 but "wild goat" (แพะป่าตัวหนึ่ง) at 34:14 is problematic. The context of 34:14, which explicitly names Lilith (`นางลีลิท`), is highly uncanny and supports a demonic interpretation for שָׂעִיר, consistent with the Lev 17:7 lock and the LXX's δαιμόνια. The current naturalized rendering at 34:14 flattens the intended mythological/demonic register.
**Recommended action:** Harmonize 34:14's rendering of שָׂעִיר to match the demonic interpretation used at 13:21 (`ผีปีศาจรูปแพะ`), consistent with the broader eerie context and supporting evidence.

## Item D: OT→NT cross-quotation: missing reader-facing footnotes for NT-cited MT/LXX divergences, plus shipped-NT retro-candidates
**Verdict:** MAJOR CONCERN
**Reasoning:**
1.  **Missing Footnotes:** The absence of reader-facing `textual_variants` footnotes for NT-cited MT/LXX divergences (e.g., 25:8, 11:10, 45:23, 65:1-2) directly violates the project's stated policy requiring these notes. The broken reference for 25:8 is a specific error. Internal `key_decisions` documentation is not a substitute for reader-facing notes.
2.  **Retro-candidates:** The discrepancies between Isaiah's translation and already-shipped NT books (e.g., Isa 53:1 `พระกร` vs John 12:38 `พระหัตถ์`; Isa 56:7 `นิเวศแห่งการอธิษฐาน` vs Matt 21:13 `บ้าน`) indicate a lack of cross-corpus consistency. Isaiah's `พระกร` (arm) and `นิเวศแห่งการอธิษฐาน` (house of prayer) are faithful to the Hebrew/LXX, making the NT versions the outliers.
**Recommended action:**
1.  Add all missing `textual_variants` footnotes for NT-cited MT/LXX divergences as per policy, and fix the broken reference for 25:8.
2.  Initiate a staged NT re-audit to normalize the NT surfaces for 53:1 (John 12:38) and 56:7 (Matt 21:13) to match the accurate Isaiah renderings (`พระกร` and `นิเวศแห่งการอธิษฐาน`), prioritizing the OT's faithful translation of the source text.

## Item E: אֲדֹנָי יְהוִה צְבָאוֹת ("the Lord GOD of hosts"): inconsistent Adonai-marking
**Verdict:** CONCERN
**Reasoning:** The inconsistent rendering of אֲדֹנָי יְהוִה צְבָאוֹת, with Adonai dropped in five instances but marked in two (22:14b, 22:15), creates an arbitrary distinction. The project's general rule for the bare אֲדֹנָי יְהוִה compound is to drop Adonai, and extending this principle to the triple stack would ensure greater consistency and avoid potential reader confusion without a clear, documented reason for the differentiation.
**Recommended action:** Normalize all seven occurrences of אֲדֹנָי יְהוִה צְבָאוֹת to consistently drop Adonai, rendering it as `องค์พระผู้เป็นเจ้าจอมโยธา`, aligning with the established policy for the compound.

## Item F: Polytheistic-register / cosmic-creature explanation: reader footnote vs internal-only
**Verdict:** CONCERN
**Reasoning:** While the translation correctly applies the polytheistic register (เทพ/เทพเจ้า, never พระเจ้า) and handles cosmic creatures, the complete absence of reader-facing footnotes explaining these conventions leaves a significant gap in reader orientation. Isaiah's extensive idol polemic and unique mythological references (Leviathan, Lilith, Bel & Nebo) warrant a brief explanation for readers to fully grasp the theological and literary nuances. The current `textual_variants` policy, limited to Tetragrammaton notes, prevents these crucial explanations from reaching the reader.
**Recommended action:** Revise the `textual_variants` policy to allow for reader-facing first-occurrence footnotes for significant corpus-level conventions, such as the pagan-deity register and cosmic-creature names. Subsequently, add such footnotes in Isaiah, including creating a `textual_variants` host file for chapter 46.

---
## §Z: Anything else?
**Verdict:** CONCERN
**Reasoning:** The project's stated philosophy is "optimal equivalence — faithful to Hebrew grammar, natural in modern Thai." While the review focused on specific items, the overall impression is that the project has a robust set of locked decisions. However, the recurring theme of inconsistencies (Items A, B, C, E) and policy violations (Item D) suggests that while the *policies* are sound, their *implementation* across the entire corpus, or even within a single book like Isaiah, requires more rigorous cross-checking. This indicates a potential need for a more comprehensive, automated consistency checker that can flag deviations from locked decisions and cross-book harmonization requirements, beyond the per-chapter checks currently in place.
**Recommended action:** Ben to decide on a project-wide initiative to develop or enhance automated cross-book consistency checks for all locked corpus decisions and inter-book harmonization rules, to prevent similar issues from recurring in future books.
