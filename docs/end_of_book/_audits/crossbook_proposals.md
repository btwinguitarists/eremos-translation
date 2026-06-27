# Cross-Book Audit — Proposals (checkbox-gated)

**Rolling output of the cross-book consistency audit loop** (`docs/CROSSBOOK_AUDIT_CHARTER.md`).
Two kinds of output:
1. **Proposals** — text changes behind Ben's gate: review → check `[x]` → merge → the change
   is applied to `output/translations/**` in a follow-up. The loop never edits translations
   directly (§1.1).
2. **Stale-question findings** — live review-questions whose proposed fix the loop has
   *verified is already present in shipped text*, so they can be closed or narrowed. (The
   cross-book sweep appears to predate the OT end-of-book-review fixes, so many flags are
   already resolved — verifying shipped text, never the sweep, is catching this.)

Every item cites its governing decision + the **verified** shipped text.

---

## 1. Proposals — text changes (check `[x]` to apply)

### T8 — OT polytheistic register (Baal)

- [ ] **1 Sam 7:4 — Baal `บาอัลทั้งหลาย` → `พระบาอัลทั้งหลาย`** `[conformance]`
  - **Hebrew:** הַבְּעָלִים ("the Baals") — *identical* form to 1 Sam 12:10.
  - **Shipped 7:4:** "…ก็เอา**บาอัลทั้งหลาย**และพระอัชเทเรทออก…" (bare — no `พระ`).
  - **Shipped 12:10 (internal precedent):** "…ไปนมัสการ**พระบาอัลทั้งหลาย**และพระอัชเทเรททั้งหลาย…" (`พระ` register).
  - **Governing policy:** `ot_polytheistic_register_2026-05.md` §1.3 — foreign deities take the **`พระ` / `เทพ`** register. Bare `บาอัล` at 7:4 under-applies the register that 12:10 (same Hebrew, same book) already uses.
  - **Proposal:** normalize 7:4 → `พระบาอัลทั้งหลาย`. **Forward-watch:** ✓ **1 Kings confirmed** — Baal ships `พระบาอัล` at 16:31/16:32/18:19 (Elijah cycle conforms). So 1 Sam 7:4 bare `บาอัล` is the lone outlier in the cross-book Baal thread.
  - **Second opinion:** Gemini unavailable (HTTP 503) → single-model finding, flagged for extra scrutiny.
  - _Source: `1SA-T8-002`. Not covered by any live review-question._

### T2 — human-messenger avoid-form backlog (2 Kings)

- [ ] **2 Kings — reclassify `ผู้สื่อสาร` → `ผู้ส่งสาร` at 8 ordinary-messenger verses** `[DRAFT]` (contingent on `A_2KI_E_mal` decision)
  - **Verified LIVE** (not stale): `5:10, 6:32, 6:33, 9:18, 10:8, 14:8, 19:9, 19:14` all ship the §4.4 **avoid-form** `ผู้สื่อสาร` for ordinary human messengers (Elisha's runner, the king's messenger, Jehu's rider, Sennacherib's envoys, etc.).
  - **Inconsistent within the same book:** 2 Kgs 1:2 and 19:23 already use the §4.4 default `ผู้ส่งสาร` for the same kind of messenger.
  - **Governing policy:** `malak_yhwh_2026-05.md` §4.4 — human messengers use `ผู้ส่งสาร` (default) or `ทูต`/`คณะทูต` (diplomatic); **avoid `ผู้สื่อสาร`** (reclassify unless documented reason).
  - **Proposal:** reclassify all 8 to `ผู้ส่งสาร` (matching 1:2/19:23); 14:8 (Amaziah's war-challenge) and 19:9 (Sennacherib's royal envoys) may instead take `ทูต` if Ben prefers to mark diplomatic envoys.
  - **Contingency:** this is the concrete, verse-listed form of the deferred normalization that `A_2KI_E_mal.yml` asks the decision on (normalize vs. document-as-principled). These 8 are the *avoid-form* cases — distinct from the acceptable `ผู้ส่งสาร`/`ทูต`/`คณะทูต` variation that question debates. Apply only if Ben chooses to normalize.
  - **Corpus-wide scope (verified counts):** the `ผู้สื่อสาร` avoid-form is not just 2 Kings — 1KI ×12, 2KI ×14, 2CH ×3 (1CH ×0). All fold into the single `A_2KI_E_mal` normalization decision; if Ben chooses to normalize, the find-replace should sweep 1KI + 2KI + 2CH together (the 8 verses above are the 2KI ordinary-messenger subset). 2CH's 3 are the prophet-as-messenger case (36:15–16) that `B_2CH_E_human` leaves genuinely open.
  - _Source: `2KI-T2-002` (+ `1KI-T2-002`, `1CH-T2-002` — same human-messenger thread)._

### T5 — OT↔NT cross-quotation thread (Shema "soul")

- [ ] **Shema `สุดจิต` → `สุดจิตวิญญาณ` at 3 verses** `[conformance]`
  - **Lemma:** נֶפֶשׁ / ψυχή ("soul") — locked to `จิตวิญญาณ` (`ot_nt_cross_quotation_thread_2026-05.md` §2.2; `psyche_vs_pneuma_anthropological_2026-04.md`).
  - **Conformant anchors:** DEU 6:5 `สุดจิตวิญญาณ` ✓ · Luke 10:27 `สุดจิตวิญญาณ` ✓.
  - **Drifted — ship bare `สุดจิต` (= "heart", drops วิญญาณ "soul"):**
    - **DEU 11:13** "…ด้วยสุดใจ…และด้วย**สุดจิต**" → `สุดจิตวิญญาณ`
    - **Matt 22:37** "สุดใจ **สุดจิต** และสุดความคิด" → `สุดจิตวิญญาณ`
    - **Mark 12:30** "สุดใจ… **สุดจิต**… สุดความคิด… สุดกำลัง" → `สุดจิตวิญญาณ`
  - **Doc-status discrepancy:** §2.2's table claims DEU 11:13 was "normalized 2026-05-16" and Matt/Mark are "staged" — **verified against shipped text: none applied.** The doc's status table is stale; the NT reaudit never happened. (διάνοια "mind" = `สุดความคิด` is separate and correct.)
  - **Second opinion:** Gemini unavailable (503). Grounds: explicit §2.2 lock + two conformant anchors.
  - _Source: `DEU-T5-003`. No live review-question._

### T5 — more Deuteronomy NT-citation drifts (vengeance + "word is near")

- [ ] **Heb 10:30 — `ตอบสนอง` → `ตอบแทน`** `[conformance]`
  - DEU 32:35 "vengeance is mine, I will repay" → `เราจะตอบแทน`; **Rom 12:19** (quoting it) → `ตอบแทน` ✓; **Heb 10:30** (same quote, *identical* Greek `ἀνταποδώσω`) → `ตอบสนอง` ✗ — the lone outlier.
  - **Proposal:** Heb 10:30 → `ตอบแทน` (align DEU 32:35 + Rom 12:19). Gemini unavailable (503); grounds: identical Greek + OT anchor + the parallel NT citation. _(from `DEU-T5-007`)_
- [ ] **Rom 10:8 — `จิตใจ` → `ใจ` (minor / low-priority)** `[conformance]`
  - DEU 30:14 "the word is…in your heart" → `ใจ`; Rom 10:8 (quoting it, `καρδία`) → `จิตใจ`. The `καρδία`→`ใจ` pattern (cf. Shema `สุดใจ`) favors `ใจ` for thread consistency. Minor — Ben's call. _(from `DEU-T5-008`)_

### T5 — OT↔NT cross-quotation thread (Isaiah 29:13 ∥ Synoptics)

- [ ] **Mark 7:6 — align to the Isa 29:13 citation thread** `[conformance]`
  - **Thread:** Isa 29:13 (`ให้เกียรติเราด้วยริมฝีปาก`) is quoted at **Matt 15:8** (`ให้เกียรติเรา…ริมฝีปาก` ✓) and **Mark 7:6** — same Greek `τοῖς χείλεσίν με τιμᾷ`.
  - **Drifted (Mark 7:6):** "ชนชาตินี้**นับถือเราแต่ปาก**…" — `นับถือ` (≠ `ให้เกียรติ` for τιμάω) and `ปาก` ("mouth", imprecise for χείλη = "lips").
  - **Proposal:** Mark 7:6 → "ชนชาตินี้**ให้เกียรติเราด้วยริมฝีปาก**…" matching Isa 29:13 + Matt 15:8 (more accurate for χείλη + restores the thread). No KD rationale documents the divergence.
  - **Second opinion:** Gemini unavailable (503). Grounds: identical Greek + OT anchor + the parallel Synoptic.
  - _Source: `ISA-T5-004`. No live review-question._

### T5 — temple-cleansing citation (Isa 56:7 + Jer 7:11 ∥ Synoptics)

- [ ] **Matt 21:13 — align both citation-phrases to the OT sources + Mark/Luke** `[conformance]`
  - **Thread:** the temple-cleansing combines Isa 56:7 ("house of prayer") + Jer 7:11 ("den of robbers"), quoted at Matt 21:13 // Mark 11:17 // Luke 19:46 — identical Greek `οἶκος` / `σπήλαιον λῃστῶν`.
  - **Sources + 2 Synoptics agree:** Isa 56:7 `นิเวศแห่งการอธิษฐาน` + Jer 7:11 `ถ้ำของโจร`; **Mark 11:17 and Luke 19:46 both match** (`นิเวศ` / `ถ้ำของโจร`).
  - **Matt 21:13 drifts on both:** `บ้าน…บ้านแห่งการอธิษฐาน` (vs `นิเวศ`) + `ซ่องของพวกโจร` (vs `ถ้ำของโจร`). No KD documents either choice.
  - **Proposal:** Matt 21:13 → `นิเวศ…นิเวศแห่งการอธิษฐาน` + `ถ้ำของโจร` — restores the thread; `นิเวศ`/`ถ้ำ` are also more apt (sacred dwelling for the temple; `ถ้ำ`=cave for `σπήλαιον`).
  - **Second opinion:** Gemini unavailable (503). Grounds: identical Greek + both OT sources + both other Synoptics.
  - _Source: `JER-T5-001` (den-of-robbers); extends to the paired Isa 56:7 phrase in the same verse._

### T8 — Canaanite-nation name spellings (corpus-wide normalization)

- [ ] **Normalize the rejected `-ต์`/`ส`-variant nation-names to the locked forms** `[conformance]`
  - **Locked** (`proper_names_and_transliteration_2026-05.md` §lines 140–142): `פְּרִזִּי` → `ชาวเปริซซี` · `חִוִּי` → `ชาวฮีไว` · `יְבוּסִי` → `ชาวเยบุส`. The doc **explicitly rejects** the `-ต์` pluralizer forms (`คนฮีไวต์`, `คนเยบุสีต`, `คนเปริสซีต`).
  - **Drift (verified counts):** **EXO** ships the rejected forms — `ฮีไวต์` ×15, `เยบุสต์` ×7, `เปริสซี` ×6; **GEN/NUM/JDG** `ฮีไวต์` ×8; **DEU/JOS** `เปริสซี` ×3. (DEU+JOS otherwise conform with `ฮีไว`/`เยบุส`.)
  - **Proposal:** corpus-wide normalize `ฮีไวต์`→`ฮีไว`, `เยบุสต์`→`เยบุส`, `เปริสซี`→`เปริซซี` (~39 occurrences, concentrated in EXO + early books) to the locked forms. Mechanical, objective find-replace.
  - **Second opinion:** Gemini unavailable (503). Grounds: explicit `proper_names` lock + the DEU/JOS conformant majority.
  - _Source: `JOS-T8-001` — the drift is actually in EXO + early books, not "across DEU+JOS" as the sweep framed it._

### T3 — the divine name "Yah" in Song of Songs (8:6)

- [ ] **Song 8:6 — `เปลวเพลิงแห่งพระยาห์` → `เปลวเพลิงแห่งยาห์`** `[conformance]`
  - **Lemma:** `יָהּ` (Yah, short form of YHWH) — the **only** divine name in Song of Songs (`שַׁלְהֶבֶת יָה`, "the very flame of Yah").
  - **Locked** (`divine_names_table_2026-05.md` line 24): `יָהּ` → `ยาห์` (bare transliteration; Pss 68:4, 77:11, Hallelu-Yah). Compound precedent — Exod 17:16 `כֵּס יָהּ` → `พระที่นั่งของยาห์` (bare `ยาห์`, the `พระ` sits on "throne", not on `ยาห์`).
  - **Drift:** SNG 8:6 ships `พระยาห์` (adds the `พระ` honorific to `ยาห์`), deviating from the locked bare form.
  - **Proposal:** `พระยาห์` → `ยาห์` (the interpretive choice to read `יָה` as the divine name is retained; only the form is normalized to the lock).
  - **Second opinion:** Gemini unavailable (503). Grounds: explicit line-24 lock + the Exod 17:16 `כֵּס יָהּ` precedent.
  - _Source: `SNG-T3-001`._

---

## 2. New review-questions proposed (decide → formalize as `.yml` in EremosVercel2)

### T5 — divine-jealousy thread (DEU 32:21 // Rom 10:19)
- **`קנא`/`ζῆλος`: `หึง` (DEU) vs `ริษยา` (Rom).** DEU 32:21 ships `หึง` (×2); Rom 10:19 (quoting it) ships `ริษยา`. `ot_nt_cross_quotation_thread §2.4` **defers** the lock "pending review of the broader divine-jealousy thread (Pentateuch + Romans)." **Q:** unify the OT↔NT thread — and to which word (does divine jealousy read better as covenant-`หึง` or `ริษยา`?) — or document the OT-affect vs NT-affect split as principled? _(from `DEU-T5-004`; verified both still drift)_

### T5 — Matt-4 temptation verb-drifts (which direction to unify)
- **`πειράζω`/`נסה`: Matt 4:7 `ทดลอง` vs DEU 6:16 `ทดสอบ`; `ζάω`/`חיה`: Matt 4:4 `ดำรงชีวิต` vs DEU 8:3 `มีชีวิตอยู่`.** §2.5 directs "normalize NT-side, DEU stays" (NT→OT). **Tension:** `อย่าทดลองพระเจ้า` (Matt 4:7) is the *familiar* Thai NT form; normalizing to `ทดสอบ` may cost recognition. **Q:** unify NT→OT (per §2.5), OT→NT (preserve the familiar NT form), or document as principled?
- **Footer, not a normalize:** Matt 4:10 `นมัสการ/ปรนนิบัติ` vs DEU 6:13 `เกรงกลัว/รับใช้` — Matt legitimately quotes the **LXX** (προσκυνέω); §2.5 calls this defensible, wanting a Layer-2 footer. _(from `DEU-T5-005`)_

### T5 — God's "soul" in the Servant citation (Isa 42:1 ∥ Matt 12:18)
- **`נֶפֶשׁ`/`ψυχή` (God's own "soul") rendered differently in the thread.** Isa 42:1 "whom my soul delights" → `จิตวิญญาณของเรา`; Matt 12:18 (quoting it, Greek `ψυχή`) → `ดวงพระทัยของเรา` ("my [royal] heart"). The Shema lock (`§2.2`) maps `ψυχή`→`จิตวิญญาณ`, but that lock targets the human "love God with all your soul," not God's *own* `נֶפֶשׁ` (which the anthropomorphism table doesn't list). **Q:** unify the Servant-citation thread (→ `จิตวิญญาณ` per the lemma) or license `ดวงพระทัย` as the natural Thai idiom for God's "soul delights"? _(from `ISA-T5-004`)_

### T6 — Nebuchadnezzar's register: Daniel royal vs Jeremiah plain (cross-book clash)
- **Same emperor, two registers.** **Daniel** gives Nebuchadnezzar full `ราชาศัพท์` (DAN 2:1 `ทรงพระสุบิน`, 3:13 `ทรงพระพิโรธ…รับสั่ง`, `พระทัย`) per `ot_register_policy_2026-05.md §2.2` ("foreign emperors → `ทรง`, even if villainous") — conformant. **Jeremiah** renders his invading actions **plain** (JER 39:1 / 34:1 `ยกมา` + `เขา`, no `ทรง`) — an "invader→plain" pattern — and is even **internally mixed** (52:4 uses royal `พระองค์` for "his army" vs `เขา` in 34:1).
- **Q:** §2.2 as written says royal everywhere. (a) Normalize Jeremiah's Nebuchadnezzar to `ทรง` (match §2.2 + Daniel)? Or (b) document a principled **"hostile-invader / agent-of-judgment → plain"** exception (register tracks narrative role — sovereign in Daniel's court, destroyer in Jeremiah)? Either way, resolve Jeremiah's internal 52:4-vs-34:1 inconsistency. Connects to `A_DAN_A_foreign` (foreign-emperor register decision — this adds the invader-role axis it didn't cover). _(from `JER-T6-001` + `DAN-T6-001`)_

### T8 — divine-council "gods" register (Ps 82 may collide with a lock)
- **The `אֱלֹהִים`/`אֵלִם` "gods" rendering varies across divine-council passages.** "Gods YHWH surpasses" is consistent in the `พระ`-register (EXO 15:11 `พระทั้งหลาย`, DEU 10:17 `บรรดาพระ`, PSA 86:8 `พระทั้งหลาย`, 95:3 `พระทั้งปวง`). **But Ps 82:1/82:6 render the divine-council `אֱלֹהִים` as `เทพ`-class** (`บรรดาเทพ` / `เทพ`); Ps 89:6 `בְּנֵי אֵלִים` → `ผู้บริสุทธิ์`.
- **Lock-tension:** `spiritual_beings_hierarchy_2026-05.md` (§lines 16, 88) reserves the **`เทพ`/`เทพี`/`เทพเจ้า` register for pagan deities** and says the divine-council / sons-of-gods must NOT take `เทพ`-class (collides with `pagan_deities_2026-04.md`). Ps 82's `เทพ` appears to cross that line.
- **Q:** Is Ps 82's `เทพ` deliberate (the condemned council exposed as false-gods), or a lock violation needing a non-`เทพ` rendering (e.g. `พระ` / literal "sons of God")? Should the divine-council "gods" register be unified + documented? Ben's theological call. _(from `EXO-T8-004`)_

### T8 — governor-title `פֶּחָה` (Nehemiah ↔ Ezra, 3 surfaces)
- **`פֶּחָה` ("governor") is rendered 3 ways:** `เจ้าเมือง` (Neh 5:14, 5:18 — Nehemiah himself), `ผู้ว่าราชการ` (Neh 12:26), `ข้าหลวง` (Ezra 5:14 — Sheshbazzar). No OT governor-title decision doc governs it. **Q:** unify to one canonical surface (+ document), or is the variation principled (a local Judah-governor `เจ้าเมือง` vs a Persian-appointed royal commissioner `ข้าหลวง`)? _(from `NEH-T8-002`)_

### T7 — human "slow to anger" in Proverbs (`אֶרֶךְ אַפַּיִם`)
- **The human virtue `אֶרֶךְ אַפַּיִם` is rendered two ways in Proverbs:** `อดทน` (14:29 "the patient have great understanding", 25:15 "with patience a ruler is persuaded") vs `โกรธช้า` (15:18, 16:32 "slow to anger"). Possibly context-sensitive (patience-virtue contexts → `อดทน`; anger contexts → `โกรธช้า`). The **divine** form is separately `ทรงกริ้วช้า` (Exod 34 — the `ทรง` honorific correctly marks the divine/human split). **Q:** unify the human rendering (to one of `โกรธช้า`/`อดทน`), or document the context-split as principled? _(from `PRO-T7-001`)_

### Systematic — OT↔NT citation Layer-2 footers largely not yet added
- **Verified absent** for all 7 NT-cited Isaiah verses in `ISA-T5-004` (9:1, 11:10, 25:8, 29:13, 42:1, 45:23, 65:1) — the chapters carry other footers (tetragrammaton etc.) but no citation footer. Per `ot_nt_cross_quotation_thread §3` each NT-cited OT verse should carry a Layer-2 footer naming the citation + any MT-vs-LXX divergence (several of these are legit LXX-divergences: 25:8 "forever"≠"in victory"; 65:1 LXX clause-reversal; 11:10 LXX "rise to rule"). **This is apparatus, not text** — a systematic project task, not authored by this loop. Flagging once here; the audit will note per-unit footer-gaps but won't generate footers. _(from `ISA-T5-004`; expect recurrence across the 35 T5 units)_
  - **High-priority footer instance — Jer 31:32 ↔ Heb 8:9** (`JER-T4-001`): the text is **correct** (Jer 31:32 ships MT `เป็นเหมือนสามี` "I was a husband"; Heb 8:9 ships the LXX reading "I disregarded them", ἠμέλησα — each faithful to its source), but the divergence is **substantive** (husband vs. disregarded) and NT-cited, with **no footer**. A strong candidate for the footer pass. No text change.

---

## 3. Stale-question findings (verified already-applied — recommend close/narrow)

These live review-questions ask for a text-fix that is **already present** in the shipped
translation (verified verse-by-verse this audit). No edit needed; listed so reviewers don't
re-litigate settled text.

- **`A_1SA_D_pagan.yml` — D1 (Dagon 5:7) + D2 (Ashtaroth spelling): RESOLVED.** Shipped 5:7 reads "เหนือ**ดาโกนพระ**ของพวกเรา" (not the "ดาโกนพระเจ้า" violation cited); 7:3/7:4/12:10/31:10 all use uniform "**อัชเทเรท**". _(from `1SA-T8-002`)_
- **`B_2CH_A_the.yml` — "did evil" normalization: text-fix RESOLVED.** All 7 cited verses (29:6, 33:2, 33:6, 33:22, 36:5, 36:9, 36:12) ship the locked `ทำสิ่งชั่วร้าย`, not bare `ทำชั่ว`. _Possibly-remaining:_ widening `check_phrase_consistency.py` scope to `"2CH "` (tooling, not text). _(from `2CH-T8-001`)_
- **`B_2CH_E_human.yml` — NARROW to prophets only.** The ordinary-envoy cases it flags are already normalized to the §4.4 forms (18:12 → `ผู้ส่งสาร`, 35:21 → `คณะทูต`). Only the **prophet-as-messenger** case (36:15–16 `ผู้สื่อสาร`) remains — and that is the genuinely-open fork the question itself raises (avoid-form vs. license `ผู้สื่อสาร` for prophetic messengers). _(from `2CH-T2-002`)_
- **`B_2SA_A_textual.yml` — Q1 (Tier-2 footers) RESOLVED; NARROW to Q2.** All five 2 Sam cruxes now carry Layer-2 reader footers: `output/textual_variants/2samuel_15.json` (v7 `trigger_1_mt_departure_footer` — the "release-blocker"), `…_21.json` (v19 Elhanan–Goliath synoptic), `…_24.json` (v1/9/13 census synoptic). The only open part is **Q2: endorse the emended "four" at 15:7 vs. revert to MT "forty"** (current behavior = "four" + footer). _(from `2SA-T4-001`)_
- **`B_2SA_C_synoptic.yml` — RESOLVED.** The doc it asks to write, `docs/translator_decisions/synoptic_parallel_passages_2026-05.md`, exists. _(from `2SA-T4-001`)_

> `B_2CH_C_chr.yml` (2 Chr 36:9 age 8-vs-18 + disclosure footer) is **genuinely open** — a real
> unresolved textual fork, correctly left for reviewers (`2CH-T4-001` deduped against it).

---

## 4. Cross-book threads verified conformant (notable — sweep flags were stale)

- **Exod 34:6–7 divine-attribute formula — LOCKS HELD corpus-wide.** Verified every recitation against `exod_34_attribute_formula_2026-05.md`: EXO 34:6–7 (source), NUM 14:18, PSA 86:15 / 103:8 / 111:4 / 145:8, JOL 2:13, JON 4:2, NEH 9:17 / 9:31, 2CH 30:9 — all use the locked components (`ทรงพระเมตตา` / `ทรงพระคุณ` / `ทรงกริ้วช้า` / `ความรักมั่นคง` / `ความซื่อสัตย์`). The sweep's three drift-claims are **all stale**: `EXO-T8-001` "source drifts on every component" (source is exact), `PSA-T7-001` "145:8 `ความเมตตากรุณา`" (ships `ทรงพระเมตตา`), `NEH-T8-001` "9:17 `ทรงพระพิโรธช้า`" (ships `ทรงกริ้วช้า`).
  - **Minor residual (low-priority, optional):** **Nahum 1:3** renders the `וְנַקֵּה לֹא יְנַקֶּה` clause as `จะไม่ทรงปล่อยให้ผู้กระทำผิดลอยนวลพ้นโทษ`, vs. the locked `แต่จะไม่ทรงพิจารณาผู้กระทำผิดให้พ้นโทษ` (Exod 34:7 / Num 14:18). Meaning preserved; `ลอยนวล` ("scot-free") is vivid and arguably fitting for a judgment oracle. Tension: formula-recognition (align) vs. contextual register (keep). Ben's call — left un-staged.

- **חֶסֶד (chesed) → `ความรักมั่นคง` — lock held in Genesis (a pre-lock book).** Verified GEN 19:19 / 21:23 / 32:11 / 39:21 all ship `ความรักมั่นคง` (incl. the casual rescue-thanks at 19:19). **GEN 40:14** ships `ความเมตตา` — but this is a **Ben-approved documented exception** (its `key_decisions`: human-to-human favor, no oath/covenant; Genesis EOB §A 2026-05-12; THSV2011 parallel) → **not a drift; do not normalize.** Sweep's `GEN-T8-001` drift-claim is stale. _(from `GEN-T8-001`)_
- **תְּשׁוּקָה (Gen 3:16 "desire") → `ความปรารถนา` — documented.** `gender_passages_thai_register_2026-05.md §2.4` + a Layer-2 footer (added 2026-05-12) intentionally preserve the polysemy; the 3 occurrences (Gen 3:16 / 4:7 / Song 7:10) differ by sense by design. `GEN-T8-003` is not a drift. _(from `GEN-T8-003`)_
- **Cities-of-refuge + blood-avenger (`מִקְלָט`, `גֹּאֵל הַדָּם`) — verified consistent NUM↔DEU↔JOS.** The 2026-05-18 lock held: avenger uniformly `ผู้แก้แค้นเลือด` (JOS's pre-audit `ผู้แก้แค้นโลหิต` and DEU's `ผู้แก้แค้นแทนเลือด` are gone from the surface); refuge `เมืองลี้ภัย`/`ที่ลี้ภัย` (×36 in JOS; doc-listed verses 20:2/20:3/21:13/21:21/21:27 all conform). Residual `หลบภัย` strings live in `key_decisions` notes, not the shipped surface. Sweep's `JOS-T8-002` claim is stale. _(from `JOS-T8-002`)_
- **Atonement vocabulary (`כִּפֵּר`, `גֹּאֵל`) — locked + LEV-audit-amended (2026-05-16); sweep flags stale.** (a) **`כִּפֵּר`**: deliberate register-split is LOCKED + script-enforced — priestly-purgation (LEV altar/sanctuary) `ลบมลทินบาป`, direct-atonement (NUM/EX) `ลบบาป`. Shipped LEV `ลบมลทินบาป` (1:4, 16:30, 17:11) is correct; the sweep's "shipped vs doc `ลบบาป/ไถ่บาป`" cites the *pre-amendment* lock (normalizing would break the split). (b) **`גֹּאֵל`**: `ไถ่`-root typology consistent — kinsman-redeemer `ญาติผู้ไถ่` at LEV 25:25 (revised 2026-05-16) + Ruth 2:20/4:14, short form `ผู้ไถ่` at LEV 25:26, divine-Redeemer `พระผู้ไถ่` at Job 19:25. The sweep's "LEV drops `ไถ่` → `ญาติสนิทที่สุด`" is the pre-revision form. (Avenger-of-blood Num 35 = `ผู้แก้แค้นเลือด`, a functionally distinct role — expected.) _(from `LEV-T8-001`, `LEV-T8-002`)_
- **Jonah chesed** (`JON-T8-001`): 2:9 + 4:2 ship `ความรักมั่นคง` — the chesed-lock trigger-fixes (doc §4, 2026-05-09) held; sweep's "drift `พระเมตตา`" stale.
- **Judges OT↔NT consistency confirmed (2 sweep flags stale).** (a) **Adonai** `אֲדֹנָי יְהוִה`: JDG 6:22 `อนิจจา ข้าแต่องค์พระผู้เป็นเจ้า` = JOS 7:7 verbatim; 16:28 = the compound + a *separate* `ข้าแต่พระเจ้า` for the later `הָאֱלֹהִים` (**not** "doubled"); 6:15 `ท่านนาย` correct (pre-recognition human address). Conforms to the 2026-05-23 position sub-rule; the open Adonai meta-question is already `B_1KI_D_adonai`. (b) **Names**: `กิดเอน`/`เยฟทาห์` are **already identical** in JDG (6:11, 7:1, 11:1, 12:7) and Heb 11:32 — the sweep's "NT `กิเดโอน/เยฟธาห์`" claim is false. _(from `JDG-T3-001`, `JDG-T5-001`)_
- **Messianic-surface explicitness — principled (undocumented) spread, not a drift.** Verified: **committal** where strongly NT/tradition-supported — Isa 7:14 `עַלְמָה` → `หญิงพรหมจารี` ("virgin", LXX/Matt 1:23) + `อิมมานูเอล`; Isa 9:5 throne-names incl. `אֵל גִּבּוֹר` → `พระเจ้าผู้ทรงฤทธิ์` ("Mighty God"). **Generic/literal** where the referent is genuinely debated — Dan 9:25 `מָשִׁיחַ` → `ผู้ถูกเจิม` ("anointed one", preserves ambiguity). These are *different* translation matters, not an inconsistency; messianic explicitness is Ben's theological call. **Optional:** no dedicated messianic-surface policy doc exists — Ben may want to document the committal-vs-generic principle to protect it forward + guide reviewers. _(from `ISA-T8-001`; not staged — principled, §1.3 default-not-flag)_
- **Divine "arm/hand" (`זְרוֹעַ`/`יָד`) — person-based register is CONSISTENT cross-book.** Verified Isaiah ↔ Jeremiah: **3rd-person** ("his arm / the arm of YHWH") → honorific `พระกร` (Isa 40:10, 52:10, 53:1, 59:16, 63:12); **1st-person** divine speech ("my arm") → plain `แขน`/`มือ` (Isa 51:5, 63:5; Jer 21:5, 27:5). The sweep's `ISA-T1-001` "drift to plain `แขน`" is actually the **correct first-person-plain rule** (one does not apply royal honorifics to oneself), matching `JER-T1-001`'s codification — not a drift. **Recommended (doc-gap):** add the 1st-person-plain carve-out to `divine_anthropomorphism_thai_grammar §2.1` (currently lists only `พระกร`), so the rule is forward-protected. **Minor/optional:** Isa 51:9 vocative ("Awake, awake, O arm of YHWH!") uses plain `แขน` — borderline (apostrophe directness); Ben's call. _(from `ISA-T1-001`; **cross-checked & confirmed at `JER-T1-001`** — JER's "conflicts ISA" flag was the sweep missing the person-distinction; the rule is consistent + codified in JER)_
