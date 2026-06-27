# Reviewer pass — Ecclesiastes / Song of Songs / Lamentations / Psalms / Job (2026-06-27)

Source: a 13-item review forwarded by Ben (a Thai reviewer's answers + Ben's ratification), books already shipped.
Status legend: **DONE** = current text already matches · **APPLY** = change queued · **FLAG** = needs Ben's call before applying.

| # | Ref | Question | Reviewer call | Current text | Disposition |
|---|-----|----------|---------------|--------------|-------------|
| 1 | ECC 1:2 (hevel, ~38×) | อนิจจัง vs ไร้แก่นสาร | **ก) อนิจจัง** | ไร้แก่นสาร | **APPLY** (convention — needs new hevel decision doc + propagate all ~38× + re-check; recommend a Layer-2 footnote at 1:2 glossing hevel = "ไอ/ลมหายใจ/ไร้สาระ" so the Buddhist *anicca* frame doesn't fully override the Hebrew) |
| 2 | ECC 9:2 (miqreh) | "เคราะห์เดียวกัน" vs "ชะตากรรม" | **เคราะห์อันเดียวกัน** (matches THSV's word choice; ชะตากรรม too fate-y) | เหตุอย่างเดียวกัน | **APPLY** (adopt the word เคราะห์ in our own phrasing — do NOT replicate THSV's clause, copyright) |
| 3 | ECC 3:11 | "นิรันดร์กาล" readable? | เข้าใจ | — | **DONE** (keep) |
| 4 | ECC 12:13 | "หน้าที่ทั้งสิ้นของมนุษย์" natural? | ธรรมชาติ/เข้าใจง่าย | — | **DONE** (keep) |
| 5 | SNG | ฉัน/เธอ register | ใช้ได้ | — | **DONE** (keep) |
| 6 | SNG | ที่รัก (F→M) vs ยอดรัก (M→F) | ดีเลย — แตกต่างแต่ลงตัว | — | **DONE** (keep the two-term split) |
| 7 | SNG 1:5 | "แต่ก็งดงาม" vs "และงดงาม" | **แต่ก็งดงาม** | "ฉันผิวคล้ำ แต่ก็งดงาม" | **DONE — already matches** |
| 8 | SNG 8:6 | flame-of-Yah: divine name vs superlative | **ก) เปลวเพลิงแห่งพระยาห์** (divine name) | "...คือเปลวเพลิงแห่งพระยาห์" | **DONE — reading already matches.** Separate OPEN item: form พระยาห์ → ยาห์ (Gemini cross-book suggestion) still unresolved |
| 9 | LAM 5:22 (book-final) | does hope remain? | **สิ้นหวังไปเลย** — too hopeless | "เว้นเสียแต่ว่าพระองค์ทรงทอดทิ้ง…อย่างสิ้นเชิงแล้ว และทรงพระพิโรธ…เกินประมาณ" | **APPLY/FLAG** — revise to preserve the thread of hope (options below) + footnote the synagogue v21-echo |
| 10 | LAM 1:1 | "โอ้…เสียแล้ว" elegiac enough? | พอ | — | **DONE** (keep) |
| 11 | Psalms (+ Hab 3, +others) | เซลาห์ inline vs footnote | **ย้ายไปเชิงอรรถ** | inline เซลาห์ across **41 files** | **FLAG** — broad convention reversal (incl. Hab 3 shipped this session). Confirm footnote treatment + scope before mass-edit; needs new Selah decision doc |
| 12 | Psalms/Job (Sheol) | "แดนคนตาย" clear / not too Thai-underworld? | เข้าใจดี | — | **DONE** (keep) |
| 13 | Job 1:6 vs Ps 109:6 (śāṭān) | ซาตาน both / ผู้กล่าวหา both / context-split | **ก) ซาตาน both** | split: Job 1:6 ซาตาน · Ps 109:6 ผู้กล่าวหา | **FLAG — recommend KEEP the split (the existing locked option ค).** Ps 109:6 שָׂטָן is anarthrous + a *human* courtroom adversary ("stand at his right hand" = the prosecutor's place), not the devil. Rendering it ซาตาน would be an exegetical error. Already locked in `satan_accuser_corpus_mapping_2026-05.md` |

## LAM 5:22 — revision options (Ben picks the Thai that sings)
The Hebrew כִּי אִם is open ("unless / but rather"); the synagogue repeats v21 after v22 so the book never ends on despair. The current Thai "เว้นเสียแต่ว่า…ทอดทิ้ง…**แล้ว**" reads as accomplished fact. Two faithful fixes:
- **(a) keep the conditional, drop the completive finality + footnote:** "นอกจากว่าพระองค์ทรงทอดทิ้งข้าพระองค์ทั้งหลายเสียสิ้น ทรงพระพิโรธต่อข้าพระองค์ทั้งหลายยิ่งนัก" + Layer-2 note on the v21 liturgical echo.
- **(b) render as the open question** (NRSV-style "or have you utterly rejected us?"): "หรือว่าพระองค์ทรงทอดทิ้งข้าพระองค์ทั้งหลายเสียสิ้นแล้ว ทรงพระพิโรธต่อข้าพระองค์ทั้งหลายยิ่งนักหรือ?"

## Where these live
- Per-item reviewer record: **this file** (canonical capture).
- Convention-level (needs/updates a decision doc): **#1 hevel** (new), **#11 Selah** (new), **#13 śāṭān** (existing `satan_accuser_corpus_mapping_2026-05.md` — keep as-is).
- Application = a deliberate per-book pass (edit JSON → re-run checks → these are shipped/audited books), not a casual edit.

## Resolution (2026-06-27, final — Ben confirmed)
- **#1 hevel → อนิจจัง** — ✅ DONE, committed `5cab4ec1`. 35× across ECC; *havel havalim* (1:2, 12:8) = the natural Thai superlative doubling "อนิจจัง อนิจจัง"; +1:2 Layer-2 footnote anchoring the Hebrew range. Cross-book hevel (Ps/Job/Prov) left as-is (ECC-scoped for now).
- **#2 miqreh-echad → เคราะห์อันเดียวกัน** — ✅ DONE, committed `5cab4ec1`. Applied to all three "one fate" verses (3:19, 9:2, 9:3) for consistency.
- **#9 LAM 5:22** — ✅ DONE, committed `04d53597`. Option (a): dropped the completive "แล้ว"; book-ending hope footnote (כִּי אִם ambiguity + synagogue v21-echo).
- **#11 Selah** — ✅ RESOLVED: **KEEP INLINE** (option 1). Staged footnote experiment was **reverted, never committed**. Rationale: **BSB keeps "Selah" inline 70/70 verses, end-of-verse, never footnoted**; matches most English Bibles (ESV/NASB/KJV/NIV) + standard Thai-Bible convention (THSV); and Eremos shows BSB in parallel, so footnoting Thai would break the column alignment. Selah is **definitively in the MT** (74×: 71 in 39 Psalms + 3 in Hab 3) — presence certain, meaning (musical/liturgical) uncertain. No change to the corpus.
- **#13 śāṭān split** — ✅ KEEP the split (Job 1:6 ซาตาน / Ps 109:6 ผู้กล่าวหา). Pushback accepted; `satan_accuser_corpus_mapping_2026-05.md` unchanged.
- **#8 form** (พระยาห์ → ยาห์) — still OPEN, separate from this pass (Gemini cross-book item).
- Books touched: **Ecclesiastes + Lamentations only.** Psalms/Hab/Song/Job unchanged.
