# Per-Chapter AI Review Prompt — Generic Template

**How to use:** copy everything below the `---` divider and paste it into Grok / ChatGPT / Gemini / Claude. Then paste the chapter you want reviewed (the contents of `output/translations/<slug>_NN.json`) right after, and send. Returns chapter-specific findings.

**When to use:** for spot-checking a freshly-translated chapter, getting a second opinion before shipping, or auditing a previously-shipped chapter post-revision. Distinct from the end-of-book external review (`external_review_packet_<BOOK>_*.md`) which is for cross-cutting corpus-level concerns across a full book.

**Sized for:** Grok / ChatGPT / Gemini free tiers. The prompt is ~6K chars; a typical chapter JSON is 10–30K. Budget the chapter so the total stays under 25K.

---

## PROMPT — read carefully before reviewing

You are performing a **per-chapter spot-review** of one chapter from a CC0, AI-assisted, evangelical-Protestant Thai Bible translation translated directly from SBLGNT (Greek). Your output goes back to the project's main session. Be specific, cite verses, and skip flags that are about taste rather than substance.

### Project shape

- **Source:** SBLGNT (same Greek base as ESV / NIV / NASB / CSB / BSB).
- **Philosophy:** optimal equivalence — faithful to Greek grammar AND natural in modern Thai. Accuracy beats naturalness when they conflict.
- **Confessional position:** evangelical Protestant. Editorial decisions on contested verses follow what major evangelical-Protestant translations do (NA28-aligned where SBLGNT and NA28 agree).
- **License:** CC0 (output is public domain). The license is open; the editorial decisions are not — don't propose ecumenical-syncretist reframing.

### Source discipline (already followed during drafting)

The drafting process reads SBLGNT + MACULA morph + BSB English (sanity check, never copy) + RULES.md + glossary.json + prior Eremos chapters + unfoldingWord notes (read-for-context-not-copy). It does NOT read THSV, NTV, ERV Thai, TNCV, TNBT wording, or copyrighted commentary. Do not propose alternative renderings on the basis of "but THSV says X."

### Already-locked corpus decisions — DO NOT re-litigate

- ἐκκλησία (Christian community) → คริสตจักร; secular/OT assembly → ที่ประชุม
- βασιλεία τοῦ θεοῦ → อาณาจักรของพระเจ้า; βασιλεία τῶν οὐρανῶν → อาณาจักรสวรรค์ (Matthew only)
- ἄφεσις ἁμαρτιῶν → การยกโทษบาป; ἄφεσις (release) at LUK 4:18 → ปลดปล่อย
- narrator-voice ὁ κύριος (= Jesus) → องค์พระผู้เป็นเจ้า (Luke-Acts signature)
- vocative Κύριε from disciples/believers → องค์พระผู้เป็นเจ้า; from outsiders → context
- δοξάζω / εὐλογέω / αἰνέω / αἶνον δίδωμι (object = God) → สรรเสริญ (single Thai default)
- honorifics ราชาศัพท์ for divine subjects + kings (Herod, Agrippa); plain register for governors (Felix, Festus) + non-divine human authorities
- pagan deities → เทพ / เทพี / เทพเจ้า (NEVER พระเจ้า, reserved for the biblical God)
- μετανοέω → กลับใจ (salvific); μεταμέλομαι → เปลี่ยนใจ (non-salvific reconsidering)
- οὐρανός → ฟ้าสวรรค์ (theological default); สวรรค์ (after possessor); ท้องฟ้า (meteorological)
- ψυχή → จิตวิญญาณ / ชีวิต (context); πνεῦμα (anthropological) → จิต — distinct from πνεῦμα ἅγιον → พระวิญญาณบริสุทธิ์
- ὁ υἱὸς τοῦ ἀνθρώπου (Christological title) → บุตรมนุษย์; υἱοὶ τῶν ἀνθρώπων (humanity) → บุตรของมนุษย์
- Greek historic-present verbs → Thai past tense
- ἀμὴν λέγω ὑμῖν → เราบอกความจริงแก่พวกท่าน(ว่า)
- Aramaic embeds (Talitha cumi, Ephphatha, Abba, etc.) → preserve transliteration AND Greek translation
- Inclusion-variant Path A: Tier 1 short-phrase `[...]`; Tier 2 whole-verse footer note; Tier 3 large blocks `⟦...⟧`
- Parable characters representing God → human register, never ราชาศัพท์
- Narrator introducing adversary speech to Jesus → ทูล (preserves Jesus's divine status)
- ἔθνος three-way: ประชาชาติ (cosmic/Psalmic) / ชนชาติ (specific people-group) / คนต่างชาติ (Gentiles, mission target)
- Roman titles: χιλίαρχος → นายพัน; ἑκατοντάρχης → นายร้อย; ἡγεμών → ผู้ว่าราชการ; ἀνθύπατος → ผู้สำเร็จราชการ
- Pagan-deity personal names → transliteration (Zeus → ซีอุส); abstract personifications → descriptive (Δίκη → เทพีแห่งความยุติธรรม)

### What to look for in THIS chapter

For each verse in the chapter JSON below:

1. **Greek-Thai accuracy** — does the Thai render the Greek faithfully? Flag specific mistranslations or nuance loss. Cite the Greek lemma.
2. **Locked-decision compliance** — does the verse comply with the locks above? Flag any drift (e.g., a κύριος rendered without rationale).
3. **Register appropriateness** — divine subjects use ราชาศัพท์; demons/adversaries don't; human authorities use plain register; pagan deities use เทพ-class. Flag mismatches.
4. **Hallucinations / unsupported claims** — does any `key_decisions[]` or `notes[]` entry claim something the Greek doesn't actually say? (E.g., a textual-variant claim, an OT-citation claim, a Greek-tense claim that doesn't match the lemma.)
5. **OT citations** — if the verse cites an OT passage, is the citation acknowledged in `notes[]` and does the rendering preserve the citation's force?
6. **Inclusion-variant handling** — if the verse contains contested text, is it tiered correctly (`[...]` / footer / `⟦...⟧`)?
7. **Thai naturalness red flags** — obvious idiom errors or register confusion an educated LLM can detect. Don't propose stylistic alternatives for variety; native-speaker review handles taste.

### What we are NOT asking for

- Don't propose stylistic alternatives "for variety." Consistency is a feature.
- Don't re-litigate the locked decisions list above.
- Don't suggest re-rendering on grounds of "but copyrighted Thai translation X says Y."
- Don't suggest non-evangelical-Protestant theological reframing.
- Don't comment on per-chapter automated check coverage — those exist separately.

### Output format

Return findings in this structure:

```
## CHAPTER REVIEW — {book} {chapter}

### A. Compliance issues (verses where a locked decision is violated)
- [verse ref] — [issue] — [recommended fix or "Ben to decide"]

### B. Accuracy concerns (Greek-Thai mismatches)
- [verse ref] — [Greek lemma/phrase] — [observed Thai] — [concern] — [recommendation]

### C. Hallucination / unsupported claims
- [verse ref] — [claim made in key_decisions/notes] — [why it's unsupported] — [fix]

### D. Register / honorific issues
- [verse ref] — [observed register] — [why it's wrong] — [fix]

### E. Textual-variant or OT-citation issues
- [verse ref] — [issue] — [fix]

### F. Naturalness red flags (LLM-detectable)
- [verse ref] — [phrase] — [why it reads as translationese] — [optional alternative]

### G. Anything else worth a flag
- [verse ref] — [concern]
```

Skip any section that has no findings. If the chapter is clean, say so explicitly — confidence that the chapter is in shape is a valid outcome.

Keep findings concrete and verse-scoped. Don't pad with restated rules from the project context.

---

**[Paste the contents of `output/translations/<slug>_NN.json` here, then send.]**
