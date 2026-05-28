# 1SA — external AI raw replies

source: Gemini + ChatGPT (web), via Cowork
account: benvanscyoc@gmail.com
date: 2026-05-28
packet: https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/1samuel/external_review_packet_1SA_2026-05-22.md

## GEMINI

Item A: Spirit-of-YHWH empowerment book-wide drift

Verdict: MAJOR CONCERN
Reasoning: The 12 Spirit occurrences in 1 Samuel directly violate the May 20 locked decisions by missing the พระ honorific, and the four צָלַח verses (10:6, 10:10, 11:6, 16:13) drop the mandated อย่างทรงพลัง. Furthermore, the 16:14–23 + 18:10 + 19:9 evil-spirit cluster is structurally inconsistent and currently lacks a defined Thai surface strategy separating divine source from troubling effect.
Recommended action: Ship revision branch revision/spirit-of-yhwh-1sam-2026-05 to retroactively normalize all 12 empowerment verses to the lock. Write a new companion doc docs/translator_decisions/evil_spirit_from_yhwh_1sam_2026-05.md to define a separate, locked Thai surface for the troubling-spirit narrative and rule on how to handle the 18:10 צָלַח hybrid.

Item B: MT/LXX inclusion-variant gap

Verdict: MAJOR CONCERN
Reasoning: The transparency layer is a core project promise, yet the 1 Sam 17 39-verse LXX-B minus and the 14:41 Urim/Thummim expansion are completely undocumented in the outputs. Additionally, strictly following the textual corruption of the MT in 13:1 ("สอง ... ปี") creates an opaque, unreadable Thai surface that fails the optimal equivalence goal.
Recommended action: Write the 4 Tier-2 chapter-footer JSON entries for chapters 11, 13, 14, and 17. For 13:1, use NRSV-style bracketed interpolations with a Tier-2 note rather than preserving the opaque textual corruption. Ben to decide if the massive 1 Sam 17 minus warrants stronger Tier-1 brackets/⟦...⟧ given its scale.

Item C: "Is Saul also among the prophets?" inclusio surface drift

Verdict: CONCERN
Reasoning: The verbatim Hebrew proverb הֲגַם שָׁאוּל בַּנְּבִיאִם acts as a deliberate literary inclusio bookending Saul's descent between 10:11-12 and 19:24. Drifting from "ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ" to the reordered paraphrase "ซาอูลก็เป็นหนึ่งในผู้เผยพระวจนะด้วยหรือ?" in 19:24 destroys this structural connection for the Thai reader.
Recommended action: Spot-revise verse 19:24 to exactly match the 10:11/12 rendering ("ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ") to lock the verbatim inclusio.

Item D: Pagan-deity register + Ashtaroth spelling drift

Verdict: MAJOR CONCERN
Reasoning: Rendering Dagon as "พระเจ้า" in 1 Sam 5:7 explicitly violates both pagan_deities_2026-04.md Rule 1 and the polytheistic register lock. Simultaneously, spelling Ashtaroth four different ways across JDG/1SA (อัชเทเรท, อัชโทเรท, อาเชโทรท, อัชทาโรท) while splitting prefixes (พระ vs เทพี) introduces unnecessary corpus-level noise for a single lemma.
Recommended action: Spot-revise 1 Sam 5:7 to a compliant register (Ben to decide between NT-aligned "ดาโกนเทพเจ้าของพวกเรา" or JDG-aligned "ดาโกนพระของพวกเรา"). Write a corpus doc to definitively lock the Ashtaroth transliteration and register, and normalize JDG and 1SA to that single standard.

Item E: Witch of Endor + necromancy vocabulary lock

Verdict: CONCERN
Reasoning: The descriptive paraphrases for אוֹב and יִדְּעֹנִי (28:3) are excellent for avoiding Thai folk-religion baggage, but rendering the plural אֱלֹהִים in 28:13 as the supreme "พระเจ้า" is highly jarring since the medium is describing a lesser spirit/divine being ascending. Applying the supreme title to a summoned spirit misrepresents the textual ambiguity.
Recommended action: Write a new corpus doc locking the descriptive paraphrases ("ผู้ที่ติดต่อกับวิญญาณ" / "ผู้ที่รู้สิ่งล้ำลับ") for the necromancy cluster to protect forward-compounding verses. Spot-revise 1 Sam 28:13 to use "สิ่งศักดิ์สิทธิ์" (or similar) as defined in ot_polytheistic_register_2026-05.md §1.1.

§Z: Anything else?

No additional corpus-level anomalies detected in this packet. The issues isolated above represent the complete set of structural deviations for 1 Samuel.

## CHATGPT

I'll treat this as the external reviewer response you can paste back into the main project. I'm going to accept the packet's locked-decision constraints, but I'll push back where a proposed fix would create a worse theological/register problem.

---

Based on the uploaded 1 Samuel review packet.

Item A: Spirit-of-YHWH empowerment drift

Verdict: MAJOR CONCERN
Reasoning: The good-Spirit empowerment texts in 10:6, 10:10, 11:6, 16:13, 19:20, and 19:23 clearly diverge from the locked Spirit-of-YHWH surface, and the צָלַח verses also fail the locked อย่างทรงพลัง treatment. 16:14 also needs distinction: the departing Spirit of YHWH should be พระวิญญาณ, but the following evil-spirit clause should not be folded into Holy-Spirit register.
Recommended action: Ship revision/spirit-of-yhwh-1sam-2026-05, but do not normalize all 12 in the same way. Revise the good-Spirit/departure occurrences to พระวิญญาณ...; add อย่างทรงพลัง only to the four good-Spirit צָלַח verses: 10:6, 10:10, 11:6, 16:13. Write docs/translator_decisions/evil_spirit_from_yhwh_1sam_2026-05.md for 16:14–23, 18:10, 19:9, keeping วิญญาณชั่ว bare, not พระวิญญาณชั่ว. For 18:10, do not use อย่างทรงพลัง; either keep the evil-spirit family as มาเหนือ or use a non-honorific intensity term such as อย่างรุนแรง if the צָלַח force must be surfaced.

Item B: MT/LXX/Qumran inclusion-variant gap

Verdict: MAJOR CONCERN
Reasoning: Following MT in 10:27b–11:1, 13:1, 14:41, and 17:12–31/17:55–18:5 is defensible under the MT-base policy, but silence in the transparency layer is not defensible because these are exactly the sort of OT textual clusters the variant system exists to disclose. 13:1 is especially reader-facing because the shipped Thai preserves an opaque damaged regnal formula without explanation.
Recommended action: Add Tier-2 chapter-footer entries for 1 Samuel 11, 13, 14, 17, and also 18 if the 17:55–18:5 minus is not handled cleanly by the chapter-17 note. Do not bracket or double-bracket the MT David-Goliath material in the main text; that would over-signal instability against the project's MT-base policy. For 13:1, preserve the MT difficulty rather than interpolating NRSV-style numbers, but add an explicit Tier-2 note that the Hebrew text appears damaged at the age/reign-number slots.

Item C: "Is Saul also among the prophets?" inclusio drift

Verdict: CONCERN
Reasoning: 10:11, 10:12, and 19:24 repeat the same Hebrew proverb formula, so the Thai should preserve the repeated-form effect unless there is a compelling Thai readability reason not to. The current 19:24 rendering is legitimate Thai, but it breaks the inclusio's surface recognition.
Recommended action: Spot-revise 19:24 to match the 10:11/10:12 surface, or have Ben/native reviewer choose one canonical Thai proverb surface and apply it identically to all three occurrences. Given current corpus cost, normalize 19:24 to ก็ซาอูลด้วยในผู้เผยพระวจนะหรือ.

Item D: Pagan-deity register + Ashtaroth spelling drift

Verdict: MAJOR CONCERN
Reasoning: 5:7 is an unambiguous register violation: ดาโกนพระเจ้าของพวกเรา gives Dagon the reserved พระเจ้า title. The Ashtaroth issue is a second-order but real corpus problem: four Thai forms for עַשְׁתָּרוֹת will look accidental, not principled.
Recommended action: Spot-revise 5:7 to ดาโกนเทพเจ้าของพวกเรา; do not use ดาโกนพระเจ้าของพวกเรา, and avoid the awkward ดาโกนพระของพวกเรา. Normalize Ashtaroth spelling to the Judges precedent อัชเทเรท. Keep the OT named-deity convention documented as a principled split: OT named Canaanite deities may use พระ as a name-title, but never พระเจ้า; NT/Greco-Roman deity language may continue using เทพ/เทพเจ้า/เทพี. Then revise 1 Sam 7:3, 7:4, 12:10, 31:10 for one spelling/register pattern, and normalize 7:4 Baal to match 12:10 if the OT convention remains พระบาอัล.

Item E: Witch of Endor + necromancy vocabulary

Verdict: CONCERN
Reasoning: The descriptive handling of אוֹב + יִדְּעֹנִי is broadly defensible, but the current surfaces are not yet a lock: 28:3 uses neutral descriptive language, while 28:7 uses แม่หมอ, which reintroduces Thai folk-religion coding. More seriously, 28:13 ข้าเห็นพระเจ้า ขึ้นมาจากแผ่นดิน is not a good place to preserve the default אֱלֹהִים → พระเจ้า; in context the woman is reporting a supernatural/divine-like being ascending from the earth, not God himself.
Recommended action: Write docs/translator_decisions/necromancy_ob_yiddeoni_2026-05.md. Lock descriptive Thai for אוֹב/יִדְּעֹנִי, preferably ผู้ที่ติดต่อกับวิญญาณ and ผู้ที่รู้สิ่งล้ำลับ, and decide whether 28:7 should be revised from แม่หมอ to a more lemma-aligned phrase such as หญิงผู้ติดต่อกับวิญญาณ. Spot-revise 28:13 away from พระเจ้า; use a non-YHWH divine-being surface such as ข้าเห็นสิ่งศักดิ์สิทธิ์ขึ้นมาจากแผ่นดิน or another locked equivalent from ot_polytheistic_register_2026-05.md, with the doc noting that Hebrew has plural אֱלֹהִים + plural participle but the narrative immediately narrows to the figure of Samuel.
