# 2CH — external AI raw replies

source: Gemini + ChatGPT (web), via Cowork
account: benvanscyoc@gmail.com
date: 2026-05-28
packet: https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/2chronicles/external_review_packet_2CH_2026-05-26.md

## GEMINI

Item A: The "did evil in the eyes of YHWH" evaluation formula drifts

Verdict: CONCERN
Reasoning: The project has firmly established and locked the formulaic surface ทำสิ่งชั่วร้ายในสายพระเนตร... to maintain strict consistency across Deuteronomistic regnal histories, precisely as enforced previously in 1 Kings. Reverting to the thinner bare ทำชั่ว for the six late apostate kings (e.g., 33:2, 36:5) and 29:6 introduces unwarranted variation into a highly formalized cyclical refrain.
Recommended action: Spot-revise the six late-king verses (33:2, 33:6, 33:22, 36:5, 36:9, 36:12) and the non-regnal 29:6 to the locked ทำสิ่งชั่วร้าย to restore consistency.

Item B: 2 Chr 24:20: the named לָבַשׁ-class Spirit forward-protect anchor ships missing the locked honorific ทรง

Verdict: MAJOR CONCERN
Reasoning: The spirit_of_yhwh_empowerment document specifically names 2 Chr 24:20 as the anchor verse for the לָבַשׁ-class, which is locked to ทรงสวมทับ precisely because the divine subject demands the royal verb-honorific. Dropping ทรง here breaks both a named lock and the corpus-wide rules for divine honorifics established in JDG 6:34 and 1 Chr 12:18.
Recommended action: Spot-revise 2 Chr 24:20 to ...พระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์..., restoring the missing ทรง.

Item C: 2 Chr 36:9 silently departs from the MT base on Jehoiachin's age

Verdict: MAJOR CONCERN
Reasoning: The project's foundational commitment is to the MT base, a standard correctly upheld in 22:2 where a difficult chronological number was preserved with an explanatory footnote. Silently adopting the harmonized "18" in 36:9 against the MT's explicit "8" (שְׁמוֹנֶה) without a Layer-2 MT-departure footer violates the core translation philosophy.
Recommended action: Restore the MT reading "eight" (แปด) in the text of 36:9, and include a synoptic-variant footer disclosing that parallel 2 Kgs 24:8 and other manuscript traditions read "eighteen" — aligning its treatment exactly with 22:2.

Item D: The Deuteronomistic-formula phrase-locks are still Kings-scoped

Verdict: CONCERN
Reasoning: 2 Chronicles is the densest regnal book in the corpus; excluding it from the check_phrase_consistency.py Deuteronomistic formula locks directly enabled the undetected drift flagged in Item A. These formulas must be programmatically enforced before moving into the Prophets, where these refrains echo.
Recommended action: Widen the scope of the DTr-formula locks in check_phrase_consistency.py to include "2CH " (and add the kingdom-keyed death-formula register split as a fourth lock) concurrent with resolving the Item A drift.

Item E: Human-messenger מַלְאָךְ ships uniformly as ผู้สื่อสาร

Verdict: CONCERN
Reasoning: While applying ผู้สื่อสาร (communicator/herald) to prophetic messengers in 36:15–16 is an arguably defensible contextual nuance, applying it to ordinary court runners (18:12) and foreign envoys (35:21) directly contradicts the §4.4 hierarchy that explicitly tells translators to avoid this term in favor of ผู้ส่งสาร or ทูต.
Recommended action: Normalize 18:12 to ผู้ส่งสาร and 35:21 to ผู้แทน or คณะทูต per the established lock. For 36:15-16, write an update to the lock document explicitly licensing ผู้สื่อสาร specifically for "prophets-as-messengers," and add the 2 Chronicles normalizations to the deferred cross-book queue.

Item F: "Until this day" leitwort: 2 Chronicles makes it 5-of-6

Verdict: FINE (with action)
Reasoning: With 2 Chronicles bringing the count to 5 out of 6 books naturally preferring the จนถึงทุกวันนี้ surface, the corpus has decisively voted on its preferred rendering for this etiological leitwort. 1 Samuel's bare จนถึงวันนี้ is an isolated outlier rather than a meaningful contextual distinction.
Recommended action: Lock จนถึงทุกวันนี้ in leitwort_handling_policy_2026-05.md as the canonical corpus surface, and add 1 Samuel's 8 occurrences to the batch normalization queue to conform to the rest of the DtrH corpus.

## CHATGPT

I'll treat the uploaded 2 Chronicles packet as the review target and return the requested item-by-item verdicts, not a general summary.

---

I'm seeing three tag-blocking-type issues: the Spirit honorific in 24:20, the silent MT departure in 36:9, and the unenforced DTr formula scope that allowed Item A. Human-messenger and leitwort normalization look more like deferred corpus-maintenance work.

---

Item A: "Did evil in the eyes of YHWH" formula drift

Verdict: CONCERN
Reasoning: The Hebrew formula is identical in the cited regnal evaluations, and the packet shows a clean split: 21:6 and 22:4 use the locked ทรงทำสิ่งชั่วร้าย..., while 33:2, 33:6, 33:22, 36:5, 36:9, and 36:12 drift to bare ทรงทำชั่ว.... Since the project already normalized this formula in Kings, allowing ทำชั่ว here weakens the phrase-lock rather than adding meaningful context-sensitive nuance.

Recommended action: Spot-revise 33:2, 33:6, 33:22, 36:5, 36:9, 36:12 to the locked ทรงทำสิ่งชั่วร้าย... surface, preserving มากมาย appropriately in 33:6. Also revise 29:6 to non-royal-subject ได้ทำสิ่งชั่วร้าย... unless the lock is explicitly regnal-only.

Item B: 24:20 Spirit-clothed idiom missing ทรง

Verdict: CONCERN
Reasoning: This is a straightforward honorific-lock deviation. In 24:20 the subject is พระวิญญาณของพระเจ้า, and the locked לָבַשׁ-class surface requires พระวิญญาณ…ทรงสวมทับ; the shipped Thai has the correct verb-class สวมทับ but omits ทรง.

Recommended action: Spot-revise 24:20 to แล้วพระวิญญาณของพระเจ้าทรงสวมทับเศคาริยาห์.... No defensible register reason appears in the provided evidence for dropping ทรง.

Item C: 36:9 Jehoiachin age silently departs from MT

Verdict: MAJOR CONCERN
Reasoning: The packet states that the MT has שְׁמוֹנֶה / "eight," while the shipped Thai has สิบแปดพรรษา (18) with no note or key decision. That directly conflicts with the project's MT-anchored claim and with the explicitly documented handling of the parallel age crux at 22:2.

Recommended action: Do not tag as-is. My default recommendation is: restore MT 8 with a synoptic-variant footer noting 2 Kgs 24:8 / many LXX witnesses read 18, because that best matches the book's 22:2 precedent. If Ben chooses to keep 18, it must receive a Trigger-1 Layer-2 MT-departure footer before tagging.

Item D: DTr formula locks remain Kings-scoped

Verdict: CONCERN
Reasoning: Item A proves the gap is not theoretical: 2 Chronicles was outside the phrase-check scope, and therefore six formula drifts escaped. The active-removal/high-place narrative concern is manageable because the lock can target the formulaic notice surface, not every occurrence of สถานสูง or reform language.

Recommended action: Widen check_phrase_consistency.py DTr formula locks to include "2CH ". Add the death/succession register split as a fourth lock if the audit already verified the kingdom-keyed ทรง convention.

Item E: Human מַלְאָךְ rendered with avoid-form ผู้สื่อสาร

Verdict: CONCERN
Reasoning: This is not an MT-faithfulness failure, but it is a doc-compliance failure: the packet says §4.4 explicitly avoids ผู้สื่อสาร, yet 18:12, 35:21, 36:15, and 36:16 all use it. The prophetic-messenger cases are semantically understandable, but if they are to remain ผู้สื่อสาร, the lock must license that as a distinct subcategory rather than silently violating the hierarchy.

Recommended action: Fold into the deferred cross-book human-messenger normalization pass. Suggested direction: 18:12 → ผู้ส่งสาร; 35:21 → ทูต / คณะทูต; 36:15–16 → either normalize to ผู้ส่งสาร language or amend the lock to explicitly license ผู้สื่อสาร for prophet-as-messenger contexts.

Item F: "Until this day" leitwort

Verdict: FINE
Reasoning: 2 Chronicles is internally consistent at all six occurrences with จนถึงทุกวันนี้, and the wider corpus evidence in the packet now favors that form by five books to one. The outlier is 1 Samuel, not 2 Chronicles.

Recommended action: Lock จนถึงทุกวันนี้ in leitwort_handling_policy_2026-05.md as the canonical corpus surface, then normalize 1 Samuel's eight จนถึงวันนี้ cases in the deferred corpus cleanup.

§Z: Anything else?

No additional corpus-level concern from the packet. The only clear pre-tag blockers are B and C, with A/D close behind because they involve enforcement drift rather than isolated wording.
