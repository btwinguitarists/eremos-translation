# Ezekiel (EZK) — external AI review response

**Reviewer:** gemini-2.5-flash (Gemini API, independent of the translating model)
**Date:** 2026-06-27  |  **Packet:** `docs/end_of_book/ezekiel/external_review_packet_EZK_2026-06-25.md`  |  finishReason: STOP

> Auto-run via scripts/run_book_review_gemini.py. The main session reads this and decides what to act on; nothing is auto-applied to the translation.

---

Here is the external sanity-check review for Ezekiel:

---

## Item A: A *codified, scaled-up* first-person-plain rule for God's body-parts (hand / eye / face)
**Verdict:** MAJOR CONCERN
**Reasoning:** The codified first-person-plain rule for God's body parts directly contradicts the `divine_anthropomorphism_thai_grammar_2026-05.md` policy of "no person-based exception" for divine anthropomorphisms. This creates an inconsistent and potentially incoherent presentation of God's person in Thai, as seen in the พระหัตถ์/มือ split within Ezekiel 20 for the same idiom.
**Recommended action:** Reverse the first-person-plain rule for divine body parts. All divine anthropomorphisms (hand, eye, face, arm) should consistently use royal register (พระหัตถ์, พระเนตร, พระพักตร์, พระกร) regardless of grammatical person, aligning with the existing corpus policy. Retroactively revise Ezekiel, Isaiah, and Jeremiah to enforce this consistency. The two carve-outs (Exodus formula and hedged vision) can be retained as principled exceptions.

## Item B: Foreign-monarch register: every ruler is plain (a Latter-Prophets vs Writings genre split)
**Verdict:** CONCERN
**Reasoning:** Ezekiel's consistent use of plain register for hostile foreign rulers in judgment oracles is rhetorically effective and theologically coherent, especially for figures like the king of Tyre who claim divinity. However, this practice directly contradicts the existing `ot_register_policy §2.2` which mandates royal register "even if villainous," and creates an undocumented genre-based split with Daniel.
**Recommended action:** Ratify the genre-based exception. Write the `foreign_monarch_register` policy document, explicitly detailing the distinction: royal register for foreign monarchs in court-narrative contexts (e.g., Daniel, Ezra), but plain register for hostile/condemned foreign rulers in prophetic judgment oracles (e.g., Ezekiel, Jeremiah). This allows Ezekiel's current rendering to be locked as-is and provides clarity for future books.

## Item C: Messianic/Davidic notes assert "is the Christ" as fact (a step past Isaiah and Jeremiah)
**Verdict:** CONCERN
**Reasoning:** The `thai_summary` notes at 34:23, 34:1, 17:22, and 21:32 assert messianic identification as bare fact ("who is the Christ," "a foreshadowing of Jesus") which goes beyond reporting an interpretation or NT citation. This directly contradicts RULES §0, which requires interpretive notes to be descriptive rather than assert fulfillment as fact, and deviates from the project's own correct report-form notes elsewhere in Ezekiel.
**Recommended action:** Revise the specified `thai_summary` notes (34:23, 34:1, 17:22, 21:32) to use a descriptive, report-form language consistent with RULES §0 and the project's existing correct notes (e.g., "in Christian tradition, this is understood as referring to the Messiah," or "the New Testament applies this to Christ in John 10:11").

## Item D: MT/LXX temple-vision measurements: incomplete, structurally-fragile disclosure
**Verdict:** MAJOR CONCERN
**Reasoning:** For a book whose defining feature is the detailed temple vision with numerous MT/LXX measurement cruxes, the current disclosure is incomplete and structurally fragile. Bundling measurement variants within the Tetragrammaton footnote makes them inaccessible to readers not opening that specific note, and the lack of a comprehensive section-level or book-level note violates the spirit of `mt_vs_lxx_textual_variant_handling §2.3` for reader-affecting divergences.
**Recommended action:**
1. Create a dedicated, comprehensive temple-section disclosure note (e.g., at the beginning of chapter 40 or a general introduction to the temple vision) outlining the project's adherence to MT and noting the general nature of LXX/English version differences in measurements.
2. For specific measurement cruxes, move these notes out of the Tetragrammaton footnote and into separate, dedicated textual variant footnotes (e.g., `[v.X] Some ancient manuscripts read 'Y' instead of 'Z'`).
3. Systematically review chapters 41, 43, 44, 46, 47, 48 and all internal `key_decisions` for other significant measurement cruxes that require reader-facing disclosure.

## Item E: "son of man" (בֶּן־אָדָם) — a three-way Thai system the policy doc doesn't yet sanction
**Verdict:** FINE
**Reasoning:** The three-way distinction (บุตรมนุษย์ for the Christological title, บุตรแห่งมนุษย์ for the OT mortal-address, and บุตรของมนุษย์ for generic humanity) provides a clear and natural disambiguation in Thai. The addition of แห่ง and the vocative เอ๋ย for Ezekiel's address sufficiently differentiates it from the established Christological title, and the consistent usage reinforces its specific meaning as a mortal address.
**Recommended action:** Lock the current rendering for Ezekiel as-is. Amend the `son_of_man_disambiguation_2026-04.md` document to explicitly include and authorize this three-way system, detailing the specific use cases for each form, especially the "บุตรแห่งมนุษย์" for the OT prophetic mortal-address.

## §Z: Anything else?
**Verdict:** CONCERN
**Reasoning:** While the rendering of אֲדֹנָי יְהוִה as องค์พระผู้เป็นเจ้า is a locked decision, the lack of a specific reader-facing note explaining this convention for the compound, given its high frequency (217x) in Ezekiel and its identical rendering to יהוה, could lead to confusion for readers trying to understand the nuances of the Hebrew source text.
**Recommended action:** Add a specific footer note, perhaps at the first occurrence of אֲדֹנָי יְהוִה in Ezekiel, explaining that the compound Hebrew term אֲדֹנָי יְהוִה (often rendered "Lord GOD" in English) is translated as องค์พระผู้เป็นเจ้า, consistent with the rendering of יהוה, to maintain a unified divine referent in Thai. This could be a separate note or an expansion of the existing Tetragrammaton note if feasible, but it needs to be explicit about the *compound*.
