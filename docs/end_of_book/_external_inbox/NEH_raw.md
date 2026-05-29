# NEH — external AI raw replies

source: Gemini 2.5 Pro + ChatGPT (web), via Cowork
account: benvanscyoc@gmail.com
date: 2026-05-29
packet: https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/nehemiah/external_review_packet_NEH_2026-05-29.md

## GEMINI

## Item A: How should a foreign (Persian) monarch be honored in Thai?

**Verdict:** MAJOR CONCERN
**Reasoning:** Ezra and Nehemiah feature the exact same historical king (Artaxerxes) but use clashing registers in the narrator voice across the book boundary (e.g., plain `ได้นำ` in EZR 1:7 vs. royal `ตรัส` / `ทรงส่ง` in NEH 2:2, 2:9). Since `ot_register_policy §2.2` explicitly dictates that foreign emperors receive ราชาศัพท์—which aligns well with Thai linguistic expectations for acknowledging absolute sovereign power regardless of covenant status—Nehemiah is executing the policy correctly while Ezra is the outlier.**Recommended action:** Lock Nehemiah's approach (full ราชาศัพท์ for foreign emperors in narrator voice) as the corpus standard. Spot-revise Ezra (and 2 Chr 36) to retroactively elevate Cyrus, Darius, and Artaxerxes to ราชาศัพท์, and write this into a corpus doc to ensure Esther and Daniel follow suit.

## Item B: Nehemiah 9:17 drifts from the locked Exodus-34 formula

**Verdict:** CONCERN
**Reasoning:** The renderings in NEH 9:17 (`พระเจ้าผู้อภัย`, `ทรงเมตตา`, `ทรงพระพิโรธช้า`, `เปี่ยมด้วย...`) and 9:31 (`ทรงเมตตา`) clearly violate the canonical surface locked in `exod_34_attribute_formula_2026-05.md`. While the shipped Thai is natural and high-register, breaking this lock obscures a vital OT theological leitwort, destroying the explicit intertextual echo between Sinai (Exod 34:6) and Nehemiah's penitential prayer.**Recommended action:** Spot-revise Nehemiah 9:17 and 9:31 to perfectly match the locked formula: `พระเจ้าผู้ทรงประทานการอภัย ทรงพระคุณและทรงพระเมตตา ทรงกริ้วช้า ทรงบริบูรณ์ด้วยความรักมั่นคง`.

## Item C: Persian governor-title is rendered three ways in Nehemiah

**Verdict:** CONCERN
**Reasoning:** The internal inconsistency within Nehemiah itself (referring to him as `เจ้าเมือง` in 5:14 but `ผู้ว่าราชการ` in 12:26) creates unnecessary confusion. While the tiering between the satrap Tattenai (`ผู้ว่าราชการแคว้น`) and the sub-provincial Nehemiah is historically sound, silently collapsing the distinct Persian loanword `תִּרְשָׁתָא` into the generic Thai title erases a lexical nuance without a recorded project rationale.**Recommended action:** Ben to decide: First, standardize Nehemiah's `פֶּחָה` translation to a single term across the book (preferably `ผู้ว่าราชการ`, which fits a provincial governor better than the municipal `เจ้าเมือง`). Second, either transliterate `תִּרְשָׁתָא` (e.g., `เทอร์ชาธา`) to preserve the Persian loanword, or officially document the decision to collapse it into the standard governor title.

## Item D: Nehemiah and the Greek tradition (Esdras B / 1 Esdras) disclosure

**Verdict:** FINE
**Reasoning:** The textual situation for Nehemiah falls strictly below the disclosure floor established in `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3. Because 1 Esdras is a distinct recension where the divergence is macro-structural rather than a verse-by-verse material variant, and Esdras B closely tracks the MT, there are no reader-affecting variants that require documentation. The inline note handling the versification discrepancy at NEH 7:68 is the correct approach.**Recommended action:** Lock as-is. Maintain silence in the textual variant files for Nehemiah's Greek tradition, mirroring the precedent set in Ezra.

## CHATGPT

## Item A: Foreign monarch honorifics

**Verdict:** MAJOR CONCERN

**Reasoning:** Same Persian king, Artaxerxes, cannot be common-register in Ezra and full royal-register in Nehemiah without confusing the corpus policy. Since the written policy already says foreign emperors receive ราชาศัพท์, Nehemiah is internally compliant and Ezra/2 Chr 36:23 are the outliers.

**Recommended action:** Ben to decide now, then write corpus doc. My recommendation: normalize Ezra's Persian emperors to Nehemiah's approach before tagging Ezra/Nehemiah/Esther/Daniel.

## Item B: Nehemiah 9:17 Exodus-34 formula drift

**Verdict:** MAJOR CONCERN

**Reasoning:** NEH 9:17 is explicitly one of the Exod 34 formula echoes, and the shipped Thai changes multiple locked components: `ทรงกริ้วช้า` → `ทรงพระพิโรธช้า`, `ทรงบริบูรณ์ด้วยความรักมั่นคง` → `เปี่ยมด้วยความรักมั่นคง`, and `พระเจ้าผู้ทรงประทานการอภัย` → `พระเจ้าผู้อภัย`. This breaks the canonical leitwort thread in a high-profile penitential prayer.

**Recommended action:** Spot-revise NEH 9:17 to the locked canonical surface. Also revise NEH 9:31 to `ทรงพระเมตตา`. Add this full formula to hard-check enforcement, not just the `ความรักมั่นคง` token.

## Item C: Persian governor title

**Verdict:** CONCERN

**Reasoning:** A tiered distinction is defensible: Tattenai as larger Trans-Euphrates official can be `ผู้ว่าราชการแคว้น`, while Nehemiah as Judah's governor can be `เจ้าเมือง`. But NEH 12:26 disrupts Nehemiah's own pattern by calling him `ผู้ว่าราชการ`, and `תִּרְשָׁתָא` is collapsed without documentation.

**Recommended action:** Write a Persian-administration title doc. Normalize NEH 12:26 to `เจ้าเมือง` if that is the Judah-level term. For `תִּרְשָׁתָא`, reader-first translation as `เจ้าเมือง` or `ผู้ว่าราชการ` is better than transliteration, but document that it is the Persian title for Nehemiah's office.

## Item D: Greek tradition disclosure

**Verdict:** FINE

**Reasoning:** Since Eremos is MT-anchored and Nehemiah has no macro reader-affecting LXX/MT divergence requiring per-verse treatment, silence is acceptable under the stated policy. The NEH 7:68 horses/mules issue is already disclosed inline, which is enough.

**Recommended action:** Lock as-is. Optional: add one book-level internal note for audit trail, but do not burden the reader text unless the project wants consistent Ezra-Nehemiah book-level metadata.

§Z skipped.
