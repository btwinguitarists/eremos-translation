# Jeremiah (JER) — external AI review response

**Reviewer:** gemini-2.5-flash (Gemini API, independent of the translating model)
**Date:** 2026-06-21  |  **Packet:** `docs/end_of_book/jeremiah/external_review_packet_JER_2026-06-21.md`  |  finishReason: STOP

> Auto-run via scripts/run_book_review_gemini.py. The main session reads this and decides what to act on; nothing is auto-applied to the translation.

---

## Item A: A *codified* first-person-plain rule for God's body-parts (arm / hand / eyes)
**Verdict:** MAJOR CONCERN
**Reasoning:** The Jeremiah KD for 1st-person divine body parts (e.g., "my arm") contradicts the corpus's general rule for divine anthropomorphisms, which implies royal register regardless of grammatical person. This creates internal inconsistencies within Jeremiah (e.g., 15:6 vs 6:12 for the identical idiom "I stretch out my hand") and is grammatically unsound in Thai, where royal register is tied to the referent's status, not the speaker's person.
**Recommended action:** Reverse the Jeremiah KD decision. All divine body parts, regardless of grammatical person, should consistently use royal register (e.g., พระกร, พระหัตถ์, พระเนตร). Spot-revise 21:5, 27:5, 6:12, 51:25, and relevant "eyes" verses in Jeremiah to royal register, and retroactively apply this consistency to Isaiah and other books.

## Item B: Foreign-monarch register: Nebuchadnezzar in plain register (vs Daniel's royal register for the same king)
**Verdict:** MAJOR CONCERN
**Reasoning:** Jeremiah's "hostile-invader downshift" rule for Nebuchadnezzar directly contradicts the corpus's `ot_register_policy §2.2` (which Daniel follows) and creates cross-book inconsistency for the same historical figure. Jeremiah also exhibits internal inconsistency by using royal register for Babylonian kings in other contexts (39:11, 52:31–32). The theological framing of Nebuchadnezzar as YHWH's "servant" should be handled in notes, not by altering the narrator's register, which is based on the referent's status.
**Recommended action:** Reverse the Jeremiah KD decision. All foreign emperors, including Nebuchadnezzar and Pharaoh Hophra, should consistently receive full Thai royal register (ราชาศัพท์) in narrator voice, matching Daniel and the corpus policy. Spot-revise all instances of Nebuchadnezzar and other foreign emperors in Jeremiah to royal register.

## Item C: MT-vs-LXX: the OT's largest textual divergence is documented only in internal (non-reader-facing) notes
**Verdict:** MAJOR CONCERN
**Reasoning:** Jeremiah's substantial MT-LXX textual divergences, including the OAN reorder and significant MT-plus passages (e.g., 33:14–26), are currently documented only in internal notes, which is insufficient for reader transparency. Crucially, the lack of a reader-facing note at 31:32, where the shipped Hebrews 8:9 quotes the LXX ("I disregarded them") against the MT-based main text ("I was a husband to them"), creates a direct contradiction for the reader and violates the project's `mt_vs_lxx §2.3` policy for NT-cited LXX variants.
**Recommended action:** Implement a book-level prefatory note for Jeremiah explaining the MT-LXX divergence (shorter LXX, OAN reorder). Add reader-facing chapter-footer anchors at key divergence points (e.g., 25, 33, 39, 46, 52) for major MT-plus passages and the OAN reorder. Specifically, add a Layer-2 footnote at 31:32 explaining the MT/LXX difference and its citation in Hebrews 8:9.

## Item D: Messianic "Branch" oracles: committal surface, register, and the YHWH-our-Righteousness name-title
**Verdict:** FINE
**Reasoning:** The rendering of "Branch" (หน่ออันชอบธรรม) and the name-title "Yahweh-Tsidkenu" (ยาห์เวห์ซิดเคนู + gloss) are consistent with corpus practice and sound. The register difference between 23:5 (royal, explicit kingship verb) and 33:15 (plain, no explicit kingship verb) is defensible based on the Hebrew text. The 31:31 summary line, being an internal note describing the New Testament's use of the passage, adheres to the "describe, don't endorse" principle for internal documentation.
**Recommended action:** Lock as-is. Add a brief note to the `key_decisions` for 33:15 explaining that the register shifts to plain because the explicit kingship verb present in 23:5 is absent, clarifying the distinction for future reference.

## Item E: "Lord GOD of hosts" (אֲדֹנָי יְהוִה צְבָאוֹת): inconsistent Adonai-marking
**Verdict:** CONCERN
**Reasoning:** The handling of `אֲדֹנָי` in the triple-stack `אֲדֹנָי יְהוִה צְבָאוֹת` is inconsistent, with 2:19 dropping it while other instances (46:10, 49:5, 50:25, 50:31) mark it. While the marking in the Oracles Against the Nations might be an intentional emphasis, this split needs a clear, documented decision. The oath at 44:26, which marks Adonai, is defensible as a distinct audible form from the bare `חַי־יְהוָה`.
**Recommended action:** Ben to decide whether `אֲדֹנָי` should be marked in the `אֲדֹנָי יְהוִה צְבָאוֹת` triple-stack (e.g., for emphasis in judgment contexts) or dropped for consistency with the bare `אֲדֹנָי יְהוִה` rule. Once decided, normalize all instances (2:19, 46:10, 49:5, 50:25, 50:31) to match the chosen convention and document this decision. The 44:26 oath can remain as-is.

## Item F: Jeremiah 31:22 crux ("a woman shall encompass a man") — interpretive note not reader-facing
**Verdict:** CONCERN
**Reasoning:** The interpretive note for the famously obscure crux at Jeremiah 31:22 (`נְקֵבָה תְּסוֹבֵב גָּבֶר`) is currently only in internal `key_decisions`. This is inconsistent with the project's precedent of providing reader-facing Layer-2 footnotes for comparable interpretive cruxes in Genesis (e.g., 3:15, 3:16), which aids reader understanding without endorsing a single interpretation.
**Recommended action:** Add a reader-facing Layer-2 footnote at Jeremiah 31:22, briefly outlining the main interpretive reading-families (e.g., role-reversal, Israel-encompasses-warrior, historic messianic/Marian interpretations), consistent with the descriptive approach taken in the internal KD.

## Item G: "den of robbers" (Jer 7:11): the shipped Matthew disagrees with Jeremiah/Mark/Luke
**Verdict:** MAJOR CONCERN
**Reasoning:** The Greek phrase `σπήλαιον λῃστῶν` is identical in Matthew 21:13, Mark 11:17, and Luke 19:46, all quoting Jeremiah 7:11. Jeremiah, Mark, and Luke consistently render this as `ถ้ำของโจร`. Matthew 21:13, however, uses `ซ่องของพวกโจร`, creating an unnecessary and confusing inconsistency for the reader across the corpus for an identical source phrase.
**Recommended action:** Normalize Matthew 21:13 to `ถ้ำของโจร` to align with Jeremiah 7:11, Mark 11:17, and Luke 19:46. This requires a spot-fix in the already-shipped Matthew via a staged re-audit.

## §Z: Anything else?
No additional corpus-level concerns were identified beyond the specific items reviewed above.
