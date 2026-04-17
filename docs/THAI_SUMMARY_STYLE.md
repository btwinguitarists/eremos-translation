# `thai_summary` style guide

Editorial spec for the optional **`thai_summary`** field — the reader-facing Thai-language explanation that appears in the Eremos app popup above the scholarly notes. Different content, different audience, different rules from the existing `key_decisions` and `notes` fields.

---

## Purpose

The Thai summary helps an **average Thai Christian** understand the verse better. It is **not** a translation of the scholarly notes. It is **not** a defense of the translation choice. It is **not** scripture (the verse text itself is the translation).

It IS a brief, plain-Thai explanation that surfaces something genuinely useful for reading the verse in context.

---

## When to write a summary

**Not every verse needs one.** Roughly 30–50% of verses across the NT will warrant a summary. Skip simple narrative ("And he went to Capernaum") that has no interpretive payload.

**Write a summary when the verse has:**
- An OT echo or allusion the reader probably wouldn't catch (e.g., Markan ἐγώ εἰμι at 6:50 echoing Exod 3:14)
- Cultural-historical context that meaningfully shifts meaning (e.g., what "Corban" actually was, why Decapolis matters)
- A theological motif worth pointing out (Markan secrecy, Pauline righteousness vocabulary)
- A Thai word choice that captures a Greek nuance the reader wouldn't see otherwise
- A textual variant where our reading differs from common Thai Bibles in a meaningful way (note the variant exists, point to scholarly notes for detail)

**Skip the summary when:**
- The verse is pure narrative with no theological/cultural payload ("They got into the boat and crossed to the other side")
- The Thai already conveys everything a reader needs without external context
- The only "decision" was lexical with no interpretive consequence (e.g., choosing between two near-synonymous Thai words)

When in doubt, skip. Better to have selective high-value summaries than every verse padded with marginal commentary.

---

## Length

**1–2 sentences. Hard cap: 3.**

If you can't say it in 2 sentences, it's a notes-level item not a summary-level item — push it to the English `notes` field instead.

---

## Register

**Plain modern Thai for an educated lay reader.**

- Use vocabulary a Thai high-school graduate understands without a dictionary
- Religious technical terms that are standard in Thai Christianity are fine (พระวิญญาณบริสุทธิ์, ข่าวประเสริฐ, อาณาจักรของพระเจ้า)
- ราชาศัพท์ (royal register) for divine subjects — same as the verse translation
- No Greek script
- No transliterated Greek (don't write "Logos" or "agape")
- No LXX/MT/NA28 references
- No scholarly debate ("some scholars say…")
- No verse references with abbreviations like "Exod 3:14" — write out: "ปฐมกาล 22 ที่อับราฮัมจะถวายอิสอัค"
- Do NOT begin with "this verse means…" or "this verse teaches…" — be specific, don't moralize

---

## Content priorities (in order of value)

1. **Old Testament echo or allusion**, surfaced in plain Thai
   > Example (Mark 9:7): "เมฆที่ปกคลุมพระเยซูคือเมฆแห่งการปรากฏของพระเจ้า แบบเดียวกับที่ปกคลุมพลับพลาในสมัยโมเสส"

2. **Cultural-historical context** that changes how the verse reads
   > Example (Mark 7:11): "คอร์บัน คือธรรมเนียมยิวที่อนุญาตให้คนถวายเงินไว้กับวัด เพื่อหลีกเลี่ยงหน้าที่ดูแลพ่อแม่ พระเยซูทรงชี้ให้เห็นว่าธรรมเนียมนี้ขัดกับพระบัญญัติของพระเจ้า"

3. **Theological motif** that runs through the book
   > Example (Mark 6:52): "นี่คือครั้งแรกในมาระโกที่อธิบายว่าใจของสาวกแข็งกระด้าง — ใช้คำเดียวกันที่อพยพใช้บรรยายฟาโรห์ มาระโกใช้คำนี้ซ้ำเพื่อแสดงว่าแม้แต่สาวกก็ยังไม่เข้าใจพระเยซูจริงๆ"

4. **Textual variant** that meaningfully differs from common Thai Bibles
   > Example (1 Tim 3:16): "ต้นฉบับเก่าแก่ที่สุดอ่านว่า 'พระองค์ผู้ทรงปรากฏ' (กล่าวถึงพระคริสต์) ขณะที่ต้นฉบับสมัยหลังบางฉบับอ่านว่า 'พระเจ้าทรงปรากฏ' การแปลของเรายึดต้นฉบับเก่ากว่า"

5. **Thai word-choice nuance** when the chosen Thai word captures something the reader might miss
   > Example (Mark 1:12): "คำว่า 'ทรงขับ' (ekballō) เป็นคำเดียวกับที่พระเยซูใช้ขับผีออก พระวิญญาณไม่ได้ค่อยๆ พาพระเยซูไป แต่ทรงขับไปอย่างมีพลัง"

---

## What NOT to include

- ❌ Greek text in any script
- ❌ Greek transliteration as the primary content (incidental clarification of a Thai term is OK — see priority 5 example)
- ❌ Translation methodology explanation ("we chose X because…") — that's the `key_decisions` field
- ❌ Defense of textual choices (other than acknowledging variants exist) — that's the `notes` field
- ❌ Reference to specific manuscripts (ℵ, B, D, etc.)
- ❌ Reference to specific scholars by name
- ❌ Long lists of OT cross-references
- ❌ Devotional application ("we should…", "this teaches us to…") — let the reader do that work
- ❌ Sermon-style rhetorical questions ("Have you ever wondered…?")
- ❌ Repeating what the verse already plainly says

---

## Voice / tone

**Informational, neutral, brief.** Like a footnote in a quality study Bible — present the relevant context and trust the reader to do their own interpretive/devotional work.

Avoid:
- Preachy or homiletical tone
- Hagiographic descriptions of biblical figures
- Pious adjectives (ศักดิ์สิทธิ์ used loosely, ทรงเปี่ยมด้วย…)

Do:
- Name the OT text or historical practice plainly
- Say what the word/concept meant in its original context
- Point out the connection to other verses by passage name (not chapter:verse abbreviation)

---

## Verse-type guide

| Verse type | Default approach |
|------------|------------------|
| Pure action narrative ("they crossed the lake") | Skip |
| Dialogue with cultural context | Brief context if needed |
| Parable | Often warranted — explain the cultural reference at minimum |
| Theological discourse (Pauline) | Often warranted — name the key concept |
| OT citation / allusion | Almost always warranted |
| Hapax legomenon | Usually warranted — explain what the rare word implies |
| Healing/miracle | Skip unless OT echo (Mark 7's Isa 35 healing language warrants one) |
| Genealogy | Skip |
| Greeting/farewell formula | Usually skip |
| Apocalyptic imagery (Revelation) | Almost always warranted — explain the symbol |

---

## Consistency across chapters

When the same theme/motif appears across multiple verses, **don't repeat the full explanation each time.** First occurrence gets the full summary; later occurrences can refer back briefly.

> Example: Mark 1:11 introduces the "beloved son" baptism formula. Mark 9:7 (Transfiguration) repeats it. The Mark 9:7 summary should briefly note the connection back ("the same divine declaration heard at the baptism…") rather than fully re-explaining.

---

## Length consistency check

After writing a summary, count the sentences. If more than 2, ask:
1. Can I cut a phrase without losing the core insight?
2. Is one of these sentences notes-level material that should move to `notes` instead?
3. Am I padding with devotional language that doesn't add information?

---

## Example pairs

These show the same verse handled at three different layers — verse, summary, scholarly notes — to demonstrate the role of each.

### Mark 9:7

**Verse (Thai translation):**
> และมีเมฆมาปกคลุมพวกเขา และมีเสียงออกมาจากเมฆว่า "ผู้นี้คือบุตรที่รักของเรา จงฟังท่านเถิด"

**thai_summary (the new layer — for readers):**
> เมฆที่ปกคลุมพระเยซูคือเมฆแห่งการปรากฏของพระเจ้า แบบเดียวกับที่ปกคลุมพลับพลาในสมัยโมเสส คำสั่ง "จงฟังท่านเถิด" ระบุพระเยซูเป็นผู้เผยพระวจนะคนที่ใหญ่กว่าโมเสส (เฉลยธรรมบัญญัติ 18:15)

**notes (scholarly — for reviewers):**
> ALLUSION TO DEUT 18:15 LXX: "The LORD your God will raise up for you a prophet like me from among your brothers — αὐτοῦ ἀκούσεσθε (him you shall hear)." Combined with Exod 24:16 cloud-of-presence and Ps 2:7 royal-son. uW figs-explicit: ἐπισκιάζω 'overshadow/envelop' — the Shekhinah-cloud of divine presence (Exod 40:34–35 LXX uses the same verb of the cloud filling the tabernacle; cf. Luke 1:35 at the Annunciation).

### Mark 7:11

**Verse:**
> แต่พวกท่านสอนว่า ถ้าผู้ใดบอกบิดาหรือมารดาว่า "สิ่งใดของข้าพเจ้าซึ่งอาจเป็นประโยชน์แก่ท่าน เป็นคอร์บัน" (ซึ่งแปลว่า ของถวายแด่พระเจ้า)

**thai_summary:**
> คอร์บัน คือธรรมเนียมยิวที่ให้บุคคลปฏิญาณว่าทรัพย์สินของตนเป็นของถวายแด่วัด เพื่อหลีกเลี่ยงหน้าที่ใช้ทรัพย์นั้นช่วยพ่อแม่ พระเยซูทรงเปิดเผยว่าธรรมเนียมของมนุษย์นี้ทำให้พระบัญญัติให้เกียรติพ่อแม่เป็นโมฆะ

**notes:**
> Κορβᾶν is an Aramaic transliteration (קָרְבָּן 'offering, gift to God'). The Mishnah (Nedarim) discusses this loophole at length…

### Mark 4:35 (skip example — pure narrative)

**Verse:**
> ในวันนั้น เมื่อเวลาเย็นมาถึง พระองค์ตรัสกับสาวกว่า "ให้เราข้ามไปฝั่งโน้นกันเถิด"

**thai_summary:** *(skip — no interpretive payload here, the next verse begins the storm-stilling pericope)*

---

## Versioning

This style guide is v0.1 (2026-04-17). When we discover patterns that work better through actual translation, revise here and note in the change log at the bottom.

### Change log

- **v0.1** (2026-04-17) — Initial spec drafted alongside Eremos app product decision to surface reader-facing summaries separate from scholarly notes.
