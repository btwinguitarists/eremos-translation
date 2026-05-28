# NUM — external AI raw replies

source: Gemini + ChatGPT (web), via Cowork
account: benvanscyoc@gmail.com
date: 2026-05-28
packet: https://raw.githubusercontent.com/btwinguitarists/eremos-translation/main/docs/end_of_book/numbers/external_review_packet_NUM_2026-05-14.md

## GEMINI

Here is the external sanity-check review for the Numbers corpus.

Item A: Num 14:18 Sinai attribute-formula recitation drifts from exod_34_attribute_formula_2026-05.md

Verdict: MAJOR CONCERN
Reasoning: The Sinai attribute-formula is a foundational OT divine self-revelation, and preserving its cross-corpus lemma-thread is the exact reason exod_34_attribute_formula_2026-05.md was created. The current shipped version of Num 14:18 diverges on every locked vocabulary item (e.g., using "ความผิด" instead of "ความชั่ว"), which breaks the reader's ability to recognize this vital cross-book recurrence.
Recommended action: Retroactively normalize Num 14:18 to the canonical Thai locked in the corpus doc in tandem with the Exodus 34 commit. Simultaneously, write the check_phrase_consistency.py extension (Checklist §3 item 2) to structurally prevent this exact drift from happening in the upcoming Psalms and Prophets recitations.

Item B: Num 20:16 + Num 22:22-35 (11 occurrences) mal'akh-YHWH cluster drifts from malak_yhwh_2026-05.md

Verdict: MAJOR CONCERN
Reasoning: The rendering of mal'akh YHWH as just ทูต (envoy) strips the supernatural/heavenly marker from one of the OT's most iconic narratives (Balaam's donkey). Because the malak_yhwh_2026-05.md doc explicitly mandates ทูตสวรรค์ to align with the NT lock for angelos and specifically targeted Numbers 22 for forward-cover, leaving it as-is violates a locked corpus-level decision.
Recommended action: Retroactively normalize all 11 occurrences in Numbers 20 and 22 to use ทูตสวรรค์ (and ทูตสวรรค์ขององค์พระผู้เป็นเจ้า). Follow the doc's §2.2 provision by keeping the surface text uniform while carrying any theophanic/Christophanic interpretive nuances in the Layer-2 footers.

Item C: Num 31:17-18 + 25:6-9 sexual-violence + zealot-execution register

Verdict: CONCERN
Reasoning: These passages represent a severe interpretive crux for evangelical readers regarding OT warfare ethics (ḥerem) and divine-sanctioned violence. While the literal Thai surface must remain perfectly faithful to the Hebrew (as it currently is), leaving it without an interpretive framework abandons the reader and invites unnecessary friction that will compound in Deuteronomy and Joshua.
Recommended action: Write docs/translator_decisions/ot_warfare_ethics_2026-05.md (Option c) to establish a uniform, cross-corpus policy for handling OT warfare/ḥerem texts, and implement the Layer-2 doctrinal footers for Num 31 and Num 25 accordingly.

Item D: Sinai = ซีนาย / สีนาย mix within Numbers + drift from Exodus's locked form

Verdict: CONCERN
Reasoning: Internal book inconsistency (10 vs. 27 occurrences) and cross-book drift from Exodus (which locked ซีนาย 100%) violates the project's proper-noun consistency rules. Since ซีนาย aligns with established Thai-Christian-Bible precedent (THSV-1971), it must serve as the standard.
Recommended action: Retroactively normalize the 10 occurrences of สีนาย to ซีนาย before tagging book-numbers-v1. Add an entry to glossary.json or extend the proper-name check-script to lock this corpus-wide and prevent drift in Deuteronomy, Judges, and Psalms.

Item E: Numbers first-occurrence YHWH-footnote wording-drift starting at ch.15

Verdict: FINE
Reasoning: The post-chapter 14 footnote template is well-formed, concise, and accurately references the project's NT-aligned standard. The issue is purely a brittle regex pattern in the check-script, not a missing footnote or a doctrinal error.
Recommended action: Loosen the script's pattern (Option b) by adding "ตามแบบแผนของฉบับพันธสัญญาใหม่" to check_divine_names.py's detection set. Adopt the shorter template as the going-forward OT-corpus standard to avoid 22 manual edits.

Item F: Num 14:17 standalone אֲדֹנָי vocative renders as YHWH-form rather than divine_names_table's Adonai-form

Verdict: CONCERN
Reasoning: The translation องค์พระผู้เป็นเจ้าของข้าพระองค์ beautifully captures the personal, petitionary vocative force of Adonai in prayer, which the flatter title lock (องค์เจ้านาย) lacks. However, because this prayer-vocative pattern will appear hundreds of times in the Psalms and Prophets, it must be officially codified rather than left as a script-invisible exception.
Recommended action: Doc-amend (Option a) — add a sub-rule to divine_names_table_2026-05.md defining องค์พระผู้เป็นเจ้าของข้าพระองค์ for standalone Adonai in personal prayer/vocative contexts within YHWH-contexts. Use Num 14:17 as the OT locking precedent for the corpus.

## CHATGPT

I'll treat the uploaded Numbers packet as the review target and return the item-by-item verdict format it requests.

---

Item A: Num 14:18 Sinai attribute-formula drift

Verdict: MAJOR CONCERN
Reasoning: Num 14:18 is not merely similar to Exod 34:6–7; it is a direct shortened recitation of the same formula. Since the project already locked this recitation family, the shipped Thai breaks the recognition-thread at the first downstream witness.
Recommended action: Spot-revise Num 14:18 to the doc-canonical Thai in tandem with the Exod 34 normalization. Also write the check_phrase_consistency.py extension now, with hard-fail behavior when 3+ formula components co-occur without the locked Thai.

Item B: Num 20:16 + Num 22 mal'akh-YHWH drift

Verdict: MAJOR CONCERN
Reasoning: Num 22:22–35 is a dense, repeated מַלְאַךְ יְהוָה cluster, and the shipped ทูตขององค์พระผู้เป็นเจ้า loses the supernatural/angelic marking carried by the project's locked ทูตสวรรค์ form. Num 20:16 also belongs in the same divine-deliverance category unless the project explicitly classifies it as a human envoy, which the context does not naturally require.
Recommended action: Normalize all 11 occurrences: Num 20:16 → ทูตสวรรค์; Num 22:22, 23, 24, 25, 26, 27, 31, 32, 34, 35 → ทูตสวรรค์ขององค์พระผู้เป็นเจ้า. Surface Thai should stay lexically uniform; the theophanic/Christophanic distinction belongs in Layer 2, not in a separate surface rendering.

Item C: Num 25 + Num 31 warfare/sexual-violence reader crux

Verdict: CONCERN
Reasoning: The shipped Thai for Num 31:17–18 is textually faithful and should not be softened. The issue is not translation accuracy but reader-facing theological handling: Num 25:6–9 and 31:17–18 will function as major interpretive shock-points, especially in a Thai evangelical setting.
Recommended action: Write docs/translator_decisions/ot_warfare_ethics_2026-05.md and add Layer-2 footers for Num 25 and Num 31. Do not revise the verse surface. The doc should establish a forward policy for Deut 7/20/25, Joshua 6–11, 1 Sam 15, and related ḥerem/warfare texts.

Item D: Sinai transliteration drift

Verdict: CONCERN
Reasoning: This is a mechanical proper-name consistency problem, not a semantic debate. Since Exodus is 100% ซีนาย and Numbers mixes ซีนาย/สีนาย, the 10× สีนาย forms should not be allowed to stand inside a tagged Pentateuch corpus.
Recommended action: Spot-revise the 10× Numbers occurrences to ซีนาย. Also normalize Succoth in Num 33:5–6 to the Exodus form สุคโคท, then add both names to glossary.json or the proper-name checker.

Item E: YHWH first-occurrence footnote wording drift

Verdict: CONCERN
Reasoning: The post-chapter-14 footnotes are present and reader-facing acceptable; the problem is template drift plus false-positive script warnings. Since this is a canonical per-chapter convention, inconsistent wording inside one book is undesirable even if the shorter form is defensible.
Recommended action: Restore the ยาห์เวห์ Yahweh phrase in Numbers 15–36 for this tagged book, then separately decide whether the shorter template should become the future standard. Also extend check_divine_names.py to recognize both templates so future convention changes do not create false positives.

Item F: Num 14:17 standalone אֲדֹנָי vocative

Verdict: CONCERN
Reasoning: The shipped Thai is natural petitionary Thai, but it collapses standalone אֲדֹנָי into the YHWH-form and creates a precedent problem before Psalms, Isaiah, Ezekiel, and Daniel. Strictly rendering all standalone אֲדֹנָי as องค์เจ้านาย may preserve the table but will likely sound wooden in vocative prayer contexts.
Recommended action: Amend divine_names_table_2026-05.md with a sub-rule: standalone אֲדֹנָי as prayer-vocative within direct address to YHWH may render as องค์พระผู้เป็นเจ้าของข้าพระองค์. Then mark Num 14:17 as the locking precedent. Do not normalize this verse to องค์เจ้านาย unless Ben decides the lexical distinction must override Thai prayer-register naturalness.

§Z: Anything else?

No additional corpus-level flag beyond the packet items. The main blocker set before book-numbers-v1 is A, B, and D; C and F are policy/doc decisions; E is a template/script hygiene fix.
