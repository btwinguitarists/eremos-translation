# Song of Songs (SNG) — external AI review response

**Reviewer:** gemini-2.5-flash (Gemini API, independent of the translating model)
**Date:** 2026-06-21  |  **Packet:** `docs/end_of_book/songofsongs/external_review_packet_SNG_2026-06-03.md`  |  finishReason: STOP

> Auto-run via scripts/run_book_review_gemini.py. The main session reads this and decides what to act on; nothing is auto-applied to the translation.

---

## Item A: "flame of Yah" divine name
**Verdict:** CONCERN
**Reasoning:** The decision to render `יָה` as the short-form divine name "Yah" is defensible for an evangelical-Protestant translation, aligning with a "faithful to Hebrew grammar" approach for this unique occurrence. However, the current rendering `พระยาห์` (Phra-Yah) is inconsistent with the project's locked divine-names table (`יָהּ → ยาห์` bare). Furthermore, the absence of a first-occurrence footnote indicates a tooling or policy gap for this specific case, which needs to be addressed if the theophoric reading is maintained.
**Recommended action:**
1. **Spot-revise 8:6:** Change `พระยาห์` to `ยาห์` to conform to the locked divine-names table.
2. **Implement footnote:** Ensure a first-occurrence translator footnote is generated for 8:6, explaining the short-form divine name `ยาห์` and noting the alternative superlative reading. This may require a tooling update or manual override.
3. **Write doc:** Create a brief `divine_name_yah_song_8_6.md` decision doc to record this specific choice and its rationale.

## Item B: King-persona + Solomon: royal honorifics for human kings?
**Verdict:** FINE
**Reasoning:** The Song of Songs is a unique poetic book, celebrating love often personified by a king (Solomon). The use of `ราชาศัพท์` (royal honorifics) for human kings in this context enhances the poetic grandeur and aligns with the literary intent of the Hebrew text. This is distinct from Psalms and Proverbs, where the focus is either on God's supreme kingship or general wisdom, making a uniform policy across all poetic books less appropriate. The sophisticated modulation at 7:6 (removing honorifics for a "conquered" king) demonstrates intentional and nuanced application of the register.
**Recommended action:** Lock as-is. However, the project should prioritize writing the `human_king_register` decision doc, explicitly outlining the rationale for varying policies across different genres (narrative, Psalms/Proverbs, Song of Songs).

## Item C: Proper-noun wordplay: surface for readers, or keep in scholarly notes?
**Verdict:** FINE
**Reasoning:** The project's policy for reader-facing footers on wordplay is clear: it must be an "active argument-engine across multiple verses" and "comprehension-dependent." The Shulammite/Shalom inclusio, while structural and multi-verse, functions as a poetic echo rather than an argument essential for comprehension. Furthermore, the translation explicitly notes that Thai cannot reproduce the sound-play, making a footer less impactful. The other puns (dudaim/dodi, shem/shemen) are single-verse and do not meet the criteria.
**Recommended action:** Lock as-is. The current approach of keeping these in scholarly notes is consistent with the established policy.

## Item D: Erotic body-imagery: faithful (non-euphemized) — confirm the stance
**Verdict:** FINE
**Reasoning:** The stance of rendering the Song's erotic body imagery faithfully and without euphemism is appropriate for an evangelical-Protestant CC0 Thai Bible. The Song celebrates marital love and sexuality, and euphemizing its imagery would diminish the literary and emotional impact intended by the Hebrew text. The examples provided (`ทรวงอก`, `สะดือ`, `ต้นขา`, `ระหว่างทรวงอกของฉัน`, `ใจของฉันก็เร่าร้อนถึงเขา`) use standard, non-vulgar Thai terms that accurately convey the original's meaning and sensual charge within a literary register. This approach is distinct from the project's policy for juridical-shame contexts (e.g., Leviticus), demonstrating a nuanced and context-sensitive handling of sensitive material.
**Recommended action:**
1. **Lock as-is.** The current translation choices for body imagery are appropriate.
2. **Write doc:** Create a `erotic_imagery_policy.md` translator-decisions doc. This document should explicitly record the distinction between handling celebratory eros (Song of Songs) and juridical-shame contexts (Leviticus), providing clear guidance for future books like Ezekiel 16/23.

---
**§Z: Anything else?**
No additional corpus-level concerns beyond those addressed in the specific items. The project appears to have a robust framework for handling complex translation decisions.
