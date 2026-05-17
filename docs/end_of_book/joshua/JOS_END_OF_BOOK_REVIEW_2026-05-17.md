# Joshua — End-of-Book Review

**Date:** 2026-05-17
**Scope:** All 24 chapters of Joshua (~658 verses); `glossary.json`; existing `docs/translator_decisions/` (87 docs through the LEV / DEU end-of-book audits).
**Trigger:** JOS 24 shipped (commit `fe79175`); per `docs/END_OF_BOOK_CHECKLIST.md`. **Seventh OT book in the corpus** (after Ruth, Jonah, Genesis, Exodus, Numbers, Deuteronomy) and the **first post-Pentateuch / Former-Prophets book** — entering the Deuteronomistic History (Joshua–Kings). JOS is also the **first OT book whose protagonist shares the Greek name of Jesus** (Ἰησοῦς, יְהוֹשֻׁעַ / יֵשׁוּעַ); the explicit NT typology lands at Heb 4:8.
**Mandate:** Internal editorial review (§2 of checklist). Surface only — no translation changes.

## Summary

- **18 cross-cutting items reviewed.** Mechanical gates (§1) all pass: 24/24 chapters have green per-chapter reports + back-translations; `check_key_term_consistency.py` clean (0 rule violations, 0 undocumented multi-renderings) across the 318-chapter corpus; `check_phrase_consistency.py` clean across all 8 audited locks (7,943 verses); `git status output/` clean; `audit_inclusion_variants.py --book joshua --strict` scanned 24 chapter files with 0 candidates.
- **Joshua is the first OT book to enter the Former-Prophets / Deuteronomistic-History corpus** and the FIRST downstream test of every Pentateuch-era OT lock landed by the LEV / DEU / NUM audits OUTSIDE the Torah itself. The audit confirms strong CONTINUITY for the divine-names table (Tetragrammaton-as-องค์พระผู้เป็นเจ้า, El→พระเจ้า), the OT-register policy (royal-ทรง- for YHWH-volitional, plain register for Joshua-as-character), the Hebrew-idioms-and-metaphor doc (the "strong hand and outstretched arm" formula recurs; the heart-melt לֵבָב נָמַס leitwort at 2:11 + 5:1 + 7:5 + 14:8 is cleanly rendered), and the leitwort-handling policy (the famous "this day / to this day" עַד הַיּוֹם הַזֶּה etiology-marker; the שָׁמַע "hear" leitwort that DEU 6:4 plants). The Pentateuch's two big OT-vocabulary-clusters land in JOS without surface re-derivation.
- **Joshua introduces TWO major cross-Pentateuch DRIFT items the per-chapter checks could not catch** — both are cross-book OT-lemma drifts:
  - **Cities of refuge + blood-avenger lexical pair** (§5): the NUM 35 + DEU 19 corpus-locked surfaces (**เมืองลี้ภัย** + **ผู้แก้แค้นเลือด**) DRIFT in JOS 20–21 to **เมืองหลบภัย** + **ผู้แก้แค้นโลหิต**. Same Hebrew lemma מִקְלָט + גֹּאֵל הַדָּם. Three Pentateuchal anchors (NUM 35 / DEU 19 / JOS 20–21) ship with three different Thai surfaces for the same pair. **DECIDE.**
  - **Seven-Nations ethnonym 3-way drift WITHIN Joshua** (§4): five 7-nation lists in JOS (3:10, 9:1, 11:3, 12:8, 24:11) ship with THREE different Thai-surface families for the same Hebrew lemma-set, NONE of which fully matches either DEU 7:1 or DEU 20:17. JOS 3:10 matches DEU 7:1 (bare suffix); JOS 9:1+11:3+12:8 add the -ต suffix family ("เปริซไซต์ / ฮีไวต์ / เยบูไซต์"); JOS 24:11 introduces yet a third spelling ("เปริสซี / ฮีไวต์ / เยบุสไซต์"). The DEU audit's §6b within-DEU drift here becomes a corpus-wide ethnonym-spelling problem. **DECIDE.**
- **3 Joshua-distinctive cross-cutting items are STABLE-but-undocumented** at corpus level (recommend new docs):
  - **Captain of YHWH's host (5:13–15) — Christophany-vs-angel ambiguity policy** — locks the שַׂר־צְבָא־יְהוָה → **ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า** title + the "rendering preserves Hebrew ambiguity" stance + the Exod 3:5 typological lock at 5:15 (§3).
  - **Jordan-crossing dry-ground + heap typology (3:13–17; 4:23) — Red-Sea cross-corpus lock** — locks the JOS-side rendering choices that mirror EXO 14 / EXO 15:8 (פּ פני יבשה → **พื้นแห้ง**; נֵד → **กอง**) so the cross-Pentateuch typology reads in Thai (§7).
  - **Rahab the *zonah* + NT-typology Matt 1:5 / Heb 11:31 / Jas 2:25** — locks the **ราหับหญิงโสเภณี** noun-construct + the NT-triad cross-corpus thread; first non-Israelite "faith-of" + first matriarch-by-incorporation in the OT history before the Ruth audit's parallel-foreign-woman precedent (§6).
- **3 items flagged REVIEW** (worth Ben's confirmation):
  - **Ḥerem 2-surface internal split within JOS** (§9): nominal-cluster verses (6:17–18, 7:1+11+12+13+15, 22:20) use **อุทิศ ... ให้พินาศ**; verbal/devastation-clause verses (6:21, 10:1+28+37+39, 11:11+12) use **ทำลายล้าง ... จนสิ้น**. Two surfaces, principled at the lexical-form level (nominal ḥerem vs verbal hifil) but neither matches the DEU-audit-recommended canonical "ทุ่มถวายเพื่อทำลาย".
  - **Adonai-in-prayer at JOS 7:7 + 7:8 — second downstream test compounding NUM 14:17 + DEU 3:24 / 9:26** (§14). Same prayer, adjacent verses: 7:7 compound אֲדֹנָי יְהוִה → **ข้าแต่องค์พระผู้เป็นเจ้า**; 7:8 standalone אֲדֹנָי → **ข้าแต่องค์เจ้านาย**. Principled split; carries the running corpus-decision-needed forward into Joshua's only prayer-of-lament.
  - **JOS 16 missing `output/textual_variants/joshua_16.json`** (§18): 23 of 24 chapters have textual-variant files; only ch.16 is missing. Mechanical-fix.
- **2 items flagged DECIDE** (Ben choice needed before tagging `book-joshua-v1`):
  - **Ethnonym 3-way drift WITHIN Joshua** (§4). Critical for forward-protection into Judges + 1–2 Sam + 1–2 Kgs (the Former Prophets cite the seven-nations cluster ~14× more times after JOS).
  - **Cities-of-refuge + blood-avenger Pentateuch surface-divergence** (§5). Three Thai surfaces for two locked lemma-pairs across three anchors (NUM 35 / DEU 19 / JOS 20–21). Forward-protects 2 Sam 14 (woman of Tekoa's avenger appeal) + 2 Sam 3 (Abner's blood-avenger argument) + Heb 6:18 (NT typology).
- **External AI review (§3) pending.** Suggested 5-item packet (§4 / §5 ethnonym + cities + DEU's outstanding §17 cross-corpus drift now compounded by JOS / §3 captain-of-host / §9 ḥerem).

Status codes: **LOCKED** — stable + corpus-doc exists. **STABLE** — uniform/principled + rationale at verse level. **REVIEW** — worth Ben's confirmation. **DECIDE** — Ben choice needed before tagging.

---

## 1. Tetragrammaton יהוה + servant-of-YHWH formula — **LOCKED**

YHWH occurs **~225× across the 24 chapters of Joshua** (every chapter except the bare tribal-allotment headers 16, 19 contains YHWH; chs 1, 3, 4, 6, 7, 8, 10, 11, 13, 14, 18, 22, 23, 24 are the high-density chapters). All occurrences render as **องค์พระผู้เป็นเจ้า** per `divine_names_table_2026-05.md` ✓. No Tetragrammaton-itself drift.

**Servant-of-YHWH inclusio.** JOS 1:1 + 24:29 frame the book with the **עֶבֶד יְהוָה / ผู้รับใช้ขององค์พระผู้เป็นเจ้า** title — applied at 1:1 to Moses (continuity with DEU 34:5) and at 24:29 to Joshua (succession completed). The notes field at 24:29 explicitly flags the inclusio:

> **BOOK INCLUSIO COMPLETE**: ยชว 1:1 — 'หลังจากที่โมเสสผู้รับใช้ของพระยาห์เวห์ได้ตาย'. ยชว 24:29 — 'โยชูวาผู้รับใช้ของพระยาห์เวห์ได้ตาย'. โครงสร้างเริ่มต้น + จบของหนังสือเดียวกัน

Note the notes field uses the older "ยาห์เวห์" Thai marker in its commentary while the verse-text itself uses the post-NUM-14 short-template **องค์พระผู้เป็นเจ้า**. This is editorial-prose, not Tetragrammaton-rendering drift; compliant.

**LOCKED** ✓ per `divine_names_table_2026-05.md`. Corpus-total YHWH count after JOS: ~1,695+ occurrences across 318 chapters, all uniformly rendered.

---

## 2. Adonai + compound divine names — **LOCKED-with-§14-REVIEW-flag**

- **Elohim → พระเจ้า** uniform across JOS ✓
- **YHWH Elohim → องค์พระผู้เป็นเจ้าพระเจ้าของ...** uniform ✓ (e.g. JOS 24:2 "องค์พระผู้เป็นเจ้าพระเจ้าของอิสราเอลตรัสดังนี้")
- **YHWH Tseva'ot / YHWH Sebaoth** — not present in JOS (the surface "host" appears under שַׂר־צְבָא־יְהוָה at 5:14–15; see §3, separate construction).
- **Adonai standalone** at JOS 7:8 (Joshua's prayer of lament after Ai-defeat) → **ข้าแต่องค์เจ้านาย** — DIFFERS from the compound form at 7:7. See §14.
- **Adonai-YHWH compound** at JOS 7:7 → **ข้าแต่องค์พระผู้เป็นเจ้า** — matches the DEU 3:24 / 9:26 + NUM 14:17 Adonai-in-prayer pattern. See §14.
- **Adoni / "my lord"** at JOS 5:14 (Joshua to the Captain of YHWH's host) → **เจ้านายของข้าพเจ้า** — single-yodh form, principled ambiguity preserved (could address human/angel/Christophany). The KD names the form: "אֲדֹנִי (single-yodh, 'my lord' addressed to humans/angels)". Compliant with the doc-locked Adoni rendering ✓.

**LOCKED with §14 REVIEW flag** for the Adonai-in-prayer pattern (now confirmed across NUM 14:17 + DEU 3:24+9:26 + JOS 7:7).

---

## 3. Captain of YHWH's host (5:13–15) — **STABLE (undocumented; recommend new doc)**

JOS 5:13–15 is the FIRST OT-corpus occurrence of the title **שַׂר־צְבָא־יְהוָה** "Commander/Prince of YHWH's host" — a high-density theophanic-Christological passage with the Exod 3:5 typological echo at 5:15. The Thai surface is uniform across all three verses:

| Verse | Hebrew | Thai |
|---|---|---|
| 5:14 | אֲנִי שַׂר־צְבָא־יְהוָה | **เราคือผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า** |
| 5:15 | שַׂר־צְבָא יְהוָה | **ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า** |
| 5:15 | שַׁל־נַעַלְךָ מֵעַל רַגְלֶךָ כִּי הַמָּקוֹם אֲשֶׁר אַתָּה עֹמֵד עָלָיו קֹדֶשׁ הוּא | **จงถอดรองเท้าออกจากเท้าของเจ้า เพราะที่ที่เจ้ายืนอยู่นั้นเป็นที่บริสุทธิ์** (verbatim EXO 3:5 lock) |

The 5:14 KD names the principle:

> **CRITICAL THEOLOGICAL TITLE**: 'ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า' — ตำแหน่งที่ปรากฏใน OT อีกแห่งหนึ่ง: ดน 8:11, 25... อาจเป็นพระคริสต์ก่อนการปรากฏ หรือทูตสวรรค์ระดับสูงสุด.

The 5:14 NOTES field documents the worship-acceptance argument for Christophany (vs the worship-rejection of Rev 19:10 + 22:8–9 by ordinary angels) and explicitly preserves Hebrew ambiguity:

> **WORSHIP ACCEPTED**: ผู้บัญชาการไม่ปฏิเสธการนมัสการของโยชูวา — ต่างจาก ทูตสวรรค์ใน วว 19:10, 22:8-9 ที่ปฏิเสธ... แต่ฉบับเอเรโมสไม่ตัดสินใจในการแปล — รักษาภาพตามต้นฉบับเปิด.

The 5:15 KD locks the EXO 3:5 typological mirror explicitly: "**TYPOLOGICAL LOCK** ของ อพย 3:5: คำพูดเดียวกันต่อโมเสสที่พุ่มไม้ไฟ. รักษาการแปลให้ตรงกับ อพย 3:5 ให้ผู้อ่านเห็นการเชื่อมโยง."

**Editorial assessment.** **ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า** is principled, exegetically conservative, and forward-protective:
- It uses **กองทัพ** "host/army" (matching the OT-divine-warrior register) rather than the heavenly-host-only **บริวาร** which would over-narrow.
- It declines to commit to "พระคริสต์" (Christ) in the Thai surface — preserving the ambiguity the Hebrew preserves. Conservative + reformation-defensible.
- The 5:15 EXO 3:5 lock is verbatim; Thai readers will recognize the typology without footnote-prompting.

**Forward-pertinent occurrences:** Daniel 8:11 + 8:25 "Prince of the host" (יְהוָה elided; same construct as JOS 5:14), Daniel 10:13+20+21 (Michael/princes-of-kingdoms), 12:1, 2 Kgs 6:17 (chariots of fire = the YHWH-host visible to Elisha's servant), 2 Chr 18:18 / 1 Kgs 22:19 (Micaiah's vision of "the host of heaven"), Zech 14:5 (kedoshim "holy ones come with him"). The forward-set is dense enough to justify a corpus doc.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/captain_of_yhwh_host_2026-05.md`. The doc should:
1. Lock שַׂר־צְבָא־יְהוָה → **ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า**
2. Lock the Christophany-ambiguity-preserved stance (Thai surface declines to commit to "พระคริสต์"; verse-NOTES name the Christophany-vs-high-angel options)
3. Lock the JOS 5:15 ↔ EXO 3:5 verbatim typological lock — both must read identically in Thai
4. Cite JOS 5:13–15 as the locking precedent
5. Forward-protect Daniel 8 + 10 + 12, 2 Kgs 6:17, Zech 14:5

**Note on `malak_yhwh_2026-05.md` boundary.** The Captain-of-host is NOT a mal'akh-YHWH occurrence — אִישׁ ("a man") is the noun used at 5:13, not מַלְאַךְ. The existing `malak_yhwh_2026-05.md` doc covers mal'akh-YHWH passages (Gen 16, Gen 22, Exo 3, Num 22, Judg 6, Judg 13, etc.) which are a related-but-distinct cluster. The recommended new captain-of-host doc should explicitly cross-reference and DISTINGUISH from the mal'akh-YHWH doc.

---

## 4. Seven-Nations ethnonym 3-way drift WITHIN Joshua — **DECIDE before tagging (HIGH severity)**

Joshua's five seven-nations lists ship with THREE different Thai-surface families for the same Hebrew lemma-set (פְּרִזִּי, חִוִּי, יְבוּסִי). The DEU audit's §6b within-DEU drift (DEU 7:1 vs DEU 20:17) here becomes a corpus-wide ethnonym-spelling problem at the FIRST downstream test:

| Verse | Thai surface (drift highlighted) | Surface family |
|---|---|---|
| **JOS 3:10** | ชาวคานาอัน ชาวฮิตไทต์ ชาว**ฮีไว** ชาว**เปริซซี** ชาวเกอร์กาชี ชาวอาโมไรต์ ชาว**เยบุส** | matches **DEU 7:1** bare-suffix (DEU-canonical) |
| **JOS 9:1** | ชาวฮิตไทต์ ชาวอาโมไรต์ ชาวคานาอัน ชาว**เปริซไซต์** ชาว**ฮีไวต์** ชาว**เยบูไซต์** | -ต / ไซต์ suffix (new JOS-internal family) |
| **JOS 11:3** | ชาว**เปริซไซต์** ... ชาว**เยบูไซต์** ... ชาว**ฮีไวต์** | -ต / ไซต์ suffix |
| **JOS 12:8** | ชาวฮิตไทต์ ชาวอาโมไรต์ ชาวคานาอัน ชาว**เปริซไซต์** ชาว**ฮีไวต์** ชาว**เยบูไซต์** | -ต / ไซต์ suffix |
| **JOS 24:11** | ชาวอาโมไรต์ ชาว**เปริสซี** ชาวคานาอัน ชาวฮิตไทต์ ชาวเกอร์กาชี ชาว**ฮีไวต์** ชาว**เยบุสไซต์** | a THIRD spelling — เปริสซี + เยบุสไซต์ (NEW; matches DEU 20:17 เปริสซีต only at "ส") |

The 3:10 KD names the principle explicitly:

> **7-NATIONS LIST** — corpus standard ตาม ฉธบ 7:1 precedent... รักษาลำดับฮีบรู (ใน JOS 3:10 ลำดับเริ่มจากคานาอัน — ต่างจาก ฉธบ 7:1 ที่เริ่มจากฮิตไทต์)

But the principle-declaration at JOS 3:10 is NOT maintained at the four later JOS ethnonym-list verses (9:1, 11:3, 12:8, 24:11), each of which uses a different spelling family.

**Cross-corpus compound (DEU + JOS) — six different Thai surfaces for the same Hebrew lemma-set:**

| Anchor | Perizzite | Hivite | Jebusite |
|---|---|---|---|
| DEU 7:1 | เปริซซี | ฮีไว | เยบุส |
| DEU 20:17 | เปริสซีต | ฮีไวต์ | เยบุสีต |
| JOS 3:10 | เปริซซี | ฮีไว | เยบุส |
| JOS 9:1 / 11:3 / 12:8 | เปริซไซต์ | ฮีไวต์ | เยบูไซต์ |
| JOS 24:11 | เปริสซี | ฮีไวต์ | เยบุสไซต์ |
| (NUM analogue / future Judg analogue) | ? | ? | ? |

**Editorial assessment.** The principle stated at JOS 3:10 is the correct one — match DEU 7:1 (the most-frequent canonical form). The 9:1 / 11:3 / 12:8 family appears to come from a different drafting-pass that defaulted to a different transliteration scheme. JOS 24:11 introduces a third partially-overlapping spelling. None of this is principled to the Hebrew (the lemma is identical in all five JOS verses).

**Forward-compounding.** The seven-nations cluster recurs in:
- Judg 1:4 + 1:6 (Adoni-bezek's lament + Hittites + Perizzites scattered)
- Judg 3:5 (Israel dwells among Canaanite + Hittite + Amorite + Perizzite + Hivite + Jebusite list — 6-name)
- 1 Kgs 9:20–21 / 2 Chr 8:7–8 (Solomon's conscription census of "all the people left from the Amorite, the Hittite, the Perizzite, the Hivite, and the Jebusite who were not of Israel")
- Ezra 9:1 (Ezra's mourning lists Canaanite + Hittite + Perizzite + Jebusite + Ammonite + Moabite + Egyptian + Amorite)
- Neh 9:8 (covenant-history recital recapitulates the seven-nations list)

Five additional cross-corpus ethnonym-list verses are queued. Each will diverge ad-hoc unless the Thai surface is locked NOW — before the Judges ship + the Ezra-Nehemiah ship + Solomon's census in Kgs.

**DECIDE before tagging — three paths:**

**(a) Normalize all JOS ethnonyms to JOS 3:10 / DEU 7:1 bare-suffix form.** Re-render JOS 9:1, 11:3, 12:8, 24:11 (and DEU 20:17) to **เปริซซี / ฮีไว / เยบุส**. Most-frequent + DEU-doc-implicit-canonical. Cost: ~5 surgical verse-edits. Add corresponding glossary entries to lock for forward books.

**(b) Normalize all JOS ethnonyms to a different canonical spelling.** Less defensible — would require touching DEU 7:1 + breaking the DEU-shipped form.

**(c) Leave as-is.** Worst path — the 5 forthcoming Former-Prophets / post-exilic ethnonym lists will diverge further; corpus traceability breaks at the FIRST downstream test of this lemma cluster.

**Recommend (a).** Pairs cleanly with the DEU-audit §6b REVIEW recommendation. **Severity: HIGH** — direct corpus-lock-violation at the first downstream OT-narrative book; forward-protects 5+ Former-Prophets and post-exilic ethnonym lists.

**Glossary update:** lock the seven-nations cluster in `glossary.json` (currently absent — both DEU-audit §6b and this audit have flagged the missing-glossary-entry).

---

## 5. Cities of refuge + blood-avenger — Pentateuch surface-divergence — **DECIDE before tagging (HIGH severity)**

Same Hebrew lemma-pair **עִיר־מִקְלָט** + **גֹּאֵל הַדָּם**, three Thai surfaces across three Pentateuchal-corpus anchors:

| Anchor | "city of refuge" | "blood-avenger" |
|---|---|---|
| Numbers 35 (~10 occurrences across 35:6, 11, 12, 13, 14, 15, 19, 21, 24, 25, 26, 27, 32) | **เมืองลี้ภัย** | **ผู้แก้แค้นเลือด** |
| Deuteronomy 19:1–13 + 4:41–43 | **เมืองลี้ภัย** | **ผู้แก้แค้นแทนเลือด** (with "แทน" particle) |
| **Joshua 20–21** (entire 6-cities-of-refuge + Levitical-cities passages) | **เมืองหลบภัย** | **ผู้แก้แค้นโลหิต** (formal-elevated โลหิต) |

Sample JOS 20:3 verse-context:

> **20:3** เพื่อผู้ฆ่าคนที่ฆ่าผู้อื่นโดยไม่ได้ตั้งใจและไม่ได้รู้ตัว จะหลบหนีไปที่นั่นได้ และเมือง[หลบภัย]เหล่านี้จะเป็นที่หลบภัยจากผู้แก้แค้น[โลหิต]สำหรับพวกเจ้า

The JOS 20:3 KD names the chosen surface explicitly:

> "ผู้แก้แค้นโลหิต" — (gōʾēl haddām) — ญาติใกล้ที่สุดของผู้ตาย

JOS 21:13, 21:21, 21:27, 21:32, 21:38 all use **เมืองหลบภัยสำหรับผู้ฆ่า** in the Levitical-cities catalog formula — uniform within JOS, but a single-step away from the NUM 35 + DEU 19 locked surface.

**Editorial assessment.** This is the JOS analogue of the DEU-audit §17 NT-cross-corpus DEU-quote drift, but here it lands ENTIRELY WITHIN the OT corpus, between the three Pentateuchal anchors that should constitute the corpus-base for the lemma-pair. The DEU-audit §17 is forward-protective; this finding is BACKWARD-rupturing.

**Forward-compounding.** The cities-of-refuge / blood-avenger language recurs across the Former Prophets + Wisdom:
- 2 Sam 14:7–11 (woman of Tekoa's blood-avenger appeal to David — the entire rhetorical setup hinges on the avenger-lemma)
- 2 Sam 3:27, 3:30 (Abner's death = blood-avenger context; Joab acting as avenger for Asahel)
- 1 Kgs 2:5, 2:31–34 (Solomon's purge of Joab on Davidic-blood-avenger grounds)
- Ruth 3:9–13, 4:1–10 (gōʾēl as kinsman-redeemer; different sense BUT same lemma — already shipped Ruth has its own audit; cross-check)
- NT echo: **Heb 6:18** "we who have fled for refuge to take hold of the hope set before us" — the language draws on the cities-of-refuge motif. Direct quotation in the Hebrews-audit (already shipped) of which Thai surface?

**DECIDE before tagging — three paths:**

**(a) Normalize JOS 20–21 to the NUM 35 + DEU 19 surface.** Re-render JOS 20:2+3+5+6+9 + JOS 21:13+21+27+32+38 from **เมืองหลบภัย** → **เมืองลี้ภัย**, and **ผู้แก้แค้นโลหิต** → **ผู้แก้แค้นเลือด** (NUM 35 form; DEU 19's "แทน" particle is a sub-drift to resolve in the same pass per DEU audit). Cost: ~10–15 surgical verse-edits across 11 verses in JOS 20 + JOS 21 + 1 KD update. Strongest forward-protection.

**(b) Lift the JOS surface to corpus + retroactively normalize NUM 35 + DEU 19.** Symmetric edit cost (NUM 35 has ~10 occurrences, DEU 19 has ~5). Defensible if Ben prefers the JOS "หลบภัย" (more natural-Thai "shelter") + "โลหิต" (elevated "blood" register for legal contexts). Forward-protection requires touching the locked NUM 35 + DEU 19 ship-state.

**(c) Write `cities_of_refuge_blood_avenger_2026-05.md`** — locks ONE canonical surface for the lemma-pair + normalizes all three anchors to the chosen form. Cost: 1 new doc + ~15–20 surgical verse-edits. Strongest forward-protection (also locks 2 Sam 14, 2 Sam 3, 1 Kgs 2, Ruth 3–4, Heb 6:18).

**Recommend (a)** for now (lowest-cost forward-protection at the natural-canonical surface) + flag (c) as a follow-up if Ben prefers an explicit corpus-doc lock. **Severity: HIGH** — same lemma-pair, three different Thai surfaces, all already in the shipped corpus. **DECIDE before tagging.**

---

## 6. Rahab the zonah + NT-typology cluster — **STABLE (undocumented; recommend new doc)**

JOS 2:1 + 6:17 + 6:22–25 introduce **רָחָב הַזּוֹנָה / ราหับหญิงโสเภณี** with uniform rendering across all occurrences. The 6:17 KD names the principle:

> **Proper-noun + descriptor lock**... ไทยรักษาทั้งชื่อและคำขยายตามสำนวนฮีบรู... **NT IMPORTANCE**: ราหับปรากฏใน มธ 1:5 (บรรพบุรุษของพระเยซู), ฮบ 11:31 (รายชื่อวีรชนของความเชื่อ), ยก 2:25

The JOS 2:4 NOTES field cross-references the Heb 11:31 + Jas 2:25 NT-corpus parallel explicitly:

> ราหับเริ่มยุทธวิธีหลอกผู้แทนของกษัตริย์เพื่อปกป้องสายลับ — รากของจริยธรรมที่ ฮบ 11:31 + ยก 2:25 สรรเสริญในฐานะการกระทำของศรัทธา. NT ไม่เน้นที่การโกหก แต่ที่การต้อนรับและการเสี่ยงเพื่อปกป้องประชากรของพระเจ้า.

The Rahab arc cleanly preserves four NT-cross-corpus links:
1. **Genealogical** — Matt 1:5 (Ραχαβ → mother of Boaz → great-grandmother of David → ancestor of Jesus)
2. **Faith-list** — Heb 11:31 (Ραάβ ἡ πόρνη … οὐ συναπώλετο τοῖς ἀπειθήσασιν "Rahab the prostitute did not perish with those who were disobedient")
3. **Faith-with-works** — Jas 2:25 (Ραάβ ἡ πόρνη οὐκ ἐξ ἔργων ἐδικαιώθη "was not Rahab the prostitute justified by works?")
4. **Israel-incorporation** — JOS 6:25 (וַתֵּשֶׁב בְּקֶרֶב יִשְׂרָאֵל עַד הַיּוֹם הַזֶּה "she dwells in Israel to this day")

**Editorial assessment.** The translation handles a notoriously-difficult passage (Rahab's calculated deception of the king's emissaries) with the right balance — preserves the Hebrew "lie" without sanitization, preserves the NT-affirmation of her faith-action without conflating ethics. The **ราหับหญิงโสเภณี** noun-construct is the standard scholarly rendering (no euphemism toward "innkeeper" — the LXX πόρνη and NT πόρνη render the זוֹנָה occupational designation literally).

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/rahab_zonah_nt_typology_2026-05.md` before the 1 Sam 2:22 + 2:25 zonah-cluster, the Ezekiel 16 + 23 zonah-allegory, and the NT πόρνη cross-corpus thread. The doc should:
1. Lock זוֹנָה (occupational designation, non-pejorative) → **หญิงโสเภณี** (Thai standard, non-euphemistic)
2. Lock the Rahab+spies narrative-ethic stance (deception preserved without sanitization; NT-affirmation framed as faith-action)
3. Cross-reference the existing `goel_kinsman_redeemer_2026-05.md` and `pagan_deities_2026-04.md` docs (Rahab's confession at JOS 2:11 acknowledges YHWH as "พระเจ้าในฟ้าเบื้องบนและบนแผ่นดินเบื้องล่าง" — pagan-monotheism-conversion)
4. Cite JOS 2:1 + 6:17+22+25 as the locking precedent
5. Forward-protect 1 Sam 2:22 (sons of Eli + zonot), Jer 3:1 + 5:7 (Israel as zonah), Ezek 16 + 23 (allegorical zonah), Hos 1–3 (Gomer + the zonut formula), Matt 1:5 / Heb 11:31 / Jas 2:25 (NT-affirmation thread)

---

## 7. Jordan-crossing dry-ground + heap typology — **STABLE (undocumented; recommend new doc)**

JOS 3:13–17 + 4:18–24 are an extended-deliberate typological mirror of EXO 14 (Red Sea crossing) + EXO 15:8 (Song of Moses "the waters stood up as a heap"). The Thai surface picks up the EXO 14 + EXO 15:8 vocabulary directly:

| JOS verse | Hebrew | Thai (matches EXO precedent) |
|---|---|---|
| 3:13 | וְיַעַמְדוּ נֵד אֶחָד | จะตั้งขึ้นเป็น**กอง**เดียว |
| 3:16 | קָמוּ נֵד אֶחָד | ตั้งขึ้นเป็น**กอง**เดียว |
| 3:17 | בֶּחָרָבָה (יַבָּשָׁה via 4:22) | บน**พื้นแห้ง** |
| 4:22 | בַּיַּבָּשָׁה עָבַר יִשְׂרָאֵל אֶת־הַיַּרְדֵּן | อิสราเอลข้ามแม่น้ำจอร์แดน**บนพื้นแห้ง** |
| 4:23 | אֲשֶׁר־הוֹבִישׁ יְהוָה אֱלֹהֵיכֶם אֶת־מֵי הַיַּרְדֵּן ... כַּאֲשֶׁר עָשָׂה יְהוָה אֱלֹהֵיכֶם לְיַם־סוּף | ทรงทำให้แม่น้ำจอร์แดนแห้ง ... เหมือนที่ทรงทำต่อทะเลแดง (verse-internal cross-link) |

The 3:17 KD names the typological lock:

> TYPOLOGICAL ECHO LOCK: รักษาการแปลให้ตรงกับ อพย 14:21 ที่ใช้ 'พื้นแห้ง'
> EXOD 15:8 ECHO: น้ำตั้งเป็นกอง (נֵד) — ภาษาเดียวกับเพลงสรรเสริญของโมเสส

**Editorial assessment.** This is exemplary cross-corpus Thai-thread protection — the translator deliberately locked **กอง** for נֵד and **พื้นแห้ง** for יַבָּשָׁה / חָרָבָה so the Thai reader recognizes Joshua's crossing as the deliberate Mosaic-pattern parallel. The 4:23 verse-internal "เหมือนที่ทรงทำต่อทะเลแดง" makes the typology explicit; the lexical lock makes it readable.

**NT echo.** Heb 11:29 (Πίστει διέβησαν τὴν Ἐρυθρὰν Θάλασσαν "by faith they crossed the Red Sea") + 1 Cor 10:1–2 (Israel "baptized in the cloud and in the sea") — the NT picks up the EXO-side; the JOS-side stands as the second-Mosaic-typology event for Pauline + Hebrews readings.

**Recommend: STABLE; lift to corpus doc** `docs/translator_decisions/jordan_red_sea_typology_2026-05.md`. The doc should:
1. Lock נֵד (waters-as-heap) → **กอง** across EXO 15:8 + JOS 3:13+16 + Ps 33:7 + Ps 78:13
2. Lock יַבָּשָׁה / חָרָבָה (dry-ground) → **พื้นแห้ง** across EXO 14:21+22+29 + JOS 3:17 + 4:22 + Ps 66:6 + Isa 51:10
3. Cite JOS 3:13–4:24 + EXO 14–15 as paired locking precedents
4. Cross-reference the existing `hebrew_idioms_and_metaphor_2026-05.md` doc
5. Forward-protect the Psalms-of-deliverance corpus (Pss 66, 74, 77, 78, 89, 106, 114) + Isa 43:16, 51:10, 63:11–13 + Mic 7:15 + the NT Heb 11:29 / 1 Cor 10:1–2 cluster

---

## 8. Sun stood still + Book of Jashar (10:11–14) — **LOCKED (rich Layer-2)**

JOS 10:11–14 is preserved with the most-significant Layer-2 footer in the book:

- **10:11 hailstones** (אַבְנֵי הַבָּרָד) → **ลูกเห็บ / ก้อนหินใหญ่จากท้องฟ้า** — Layer-2 footer cites EXO 9:18–26 (seventh plague hailstone parallel) + Rev 16:21 (eschatological-hailstone parallel) — divine-weapon thread preserved.
- **10:12–13 the sun stood still** (וַיִּדֹּם הַשֶּׁמֶשׁ) → **ดวงอาทิตย์ก็หยุด** — Layer-2 footer transparently names the three interpretive options (literal cosmic-halt / refraction-extended-light / poetic-imagery) without committing the translation.
- **10:13 "Book of Jashar"** (סֵפֶר הַיָּשָׁר) → **หนังสือของยาชาร์** — Layer-2 footer names the ancient-source citation, the post-Mosaic-redaction implications, and the 2 Sam 1:18 second-citation parallel.
- **10:14 YHWH fought for Israel** (כִּי יְהוָה נִלְחָם לְיִשְׂרָאֵל) → **องค์พระผู้เป็นเจ้าทรงรบเพื่ออิสราเอล** — uniform across 10:14 + 10:42 + 23:3 + 23:10 (DEU 1:30 + DEU 3:22 precedent). LOCKED-by-implication ✓ per `ot_warfare_ethics_2026-05.md`.

**LOCKED** ✓.

---

## 9. Ḥerem חרם / OT warfare ethics — **REVIEW (2-surface internal split; coordinate with DEU §7 DECIDE)**

JOS is THE SECOND-CONCENTRATED ḥerem book after DEU. Distribution within JOS (verified via Hebrew-root scan of all 24 chapters):

| Verse | Hebrew | Thai surface | Surface family |
|---|---|---|---|
| **6:17** | יִֽהְיֶה הָעִיר חֵרֶם | จะถูก**อุทิศแด่องค์พระผู้เป็นเจ้าให้พินาศโดยสิ้นเชิง** | nominal (devotion+destruction gloss) |
| **6:18** | פֶּן ... מִן הַחֵרֶם ... שַׂמְתֶּם אֶת מַחֲנֵה יִשְׂרָאֵל לְחֵרֶם | สิ่งที่ถูก**อุทิศให้พินาศ** ... ค่ายของอิสราเอลถูก**อุทิศให้พินาศ** | nominal |
| **6:21** | וַֽיַּחֲרִ֨ימוּ֙ אֶת־כָּל־אֲשֶׁ֣ר בָּעִיר | พวกเขา**ทำลายล้างทุกสิ่งในเมือง ... จนสิ้น** | verbal (hifil) |
| **7:1+11+12+13+15** | בַּחֵרֶם / מִן הַחֵרֶם | ของที่ถูก**อุทิศให้พินาศ** | nominal |
| **10:1, 10:28, 10:37, 10:39, 11:11, 11:12** | יַּחֲרִם / יַחֲרֵם / וַיַּחֲרֵם / וַיַּחֲרֵם | **ทำลายล้าง ... จนสิ้น** | verbal (hifil) |
| **22:20** | מָעַל בַּחֵרֶם | ของที่ถูก**อุทิศให้พินาศ** | nominal |

**Two surfaces, principled at the lexical-form level:**
- **nominal חֵרֶם** (the *thing* devoted/banned) → **อุทิศ ... ให้พินาศ / สิ่งที่อุทิศ** (preserves the "set-apart-for-destruction" gloss)
- **hiphil יַּחֲרִים** (the *act* of devoting/destroying) → **ทำลายล้าง ... จนสิ้น** (preserves the action-form)

This is a **cleaner pattern** than DEU's 5-surface drift (DEU audit §7), but it does NOT match the DEU-audit-recommended canonical "ทุ่มถวายเพื่อทำลาย". JOS chose a different rendering family ("อุทิศ" rather than "ทุ่มถวาย").

The 6:17 KD names the principle:

> **KEY OT TERM — 'devoted/the ban': เฮเรม (חֵרֶם)** เป็นคำเฉพาะของศาสนาอิสราเอลโบราณ = สิ่งที่อุทิศแด่พระเจ้าจนคนใช้ไม่ได้อีกแล้ว... ไทย 'อุทิศให้พินาศโดยสิ้นเชิง' รักษาทั้งมิติการมอบให้พระเจ้าและการทำลาย

JOS 6:17 + 6:18 + 6:21 + 7:1–15 + 22:20 have rich Layer-2 doctrinal footers covering ANE-warfare ethics, Canaan-judgment historicism, Rahab+Gibeonite exceptions, Wright/Copan interpretations. **Layer-2 anchor density is HIGHER in JOS than DEU** (DEU concentrated at ch.20:17 only; JOS has anchor footers at 6:17, 7:1+11, 11:20, 22:20).

**Editorial assessment.** JOS's 2-surface split is **principled by Hebrew binyan** — but it diverges from the DEU-audit-§7 recommended canonical surface ("ทุ่มถวายเพื่อทำลาย"). The DEU audit recommended (path a) normalizing all DEU ḥerem occurrences to **ทุ่มถวายเพื่อทำลาย**; if that resolution lands, the same normalization should propagate to JOS (~12 verses).

**REVIEW flag.** Coordinate with the DEU-audit §7 DECIDE outcome. Two coordination paths:
- **(a) JOS surface stays, DEU normalizes TO the JOS family.** Replace DEU's 5-form drift with the cleaner JOS 2-form principle (nominal "อุทิศ" / verbal "ทำลายล้าง"). Doc-amend `ot_warfare_ethics_2026-05.md` to lock this 2-form distinction. Defensible — the JOS distribution is principled and cleaner.
- **(b) JOS + DEU both normalize TO a third canonical "ทุ่มถวายเพื่อทำลาย".** Per DEU-audit-§7 recommendation. JOS ~12 verses + DEU ~5 verses re-rendered. Strongest unified rendering.

**Recommend (a)** — the JOS 2-form binyan-principled split is the cleaner editorial principle. Doc-amend `ot_warfare_ethics_2026-05.md` to: (1) lock the binyan-principled distinction (nominal "อุทิศ ... ให้พินาศ" / verbal "ทำลายล้าง ... จนสิ้น"); (2) name JOS 6:17 + 6:21 as the paired locking precedents; (3) cite the JOS Layer-2 anchor density as the model for forward ḥerem chapters (1 Sam 15:3–9 Saul-Amalek, 1 Kgs 20:42 Ben-Hadad). **Severity: MEDIUM** — JOS itself ships cleanly; coordination with DEU-audit-§7 DECIDE is the load-bearing decision.

---

## 10. Covenant renewal at Shechem (JOS 24) — **STABLE (recommend doc lift)**

JOS 24 is the second-most-quoted chapter from Joshua in Christian usage (after JOS 1:9). The famous 24:15 + the historical prologue 24:2–13 + the "household salvation" pattern set up the chapter as the OT-corpus benchmark for covenant-renewal theology.

### 24:15 famous challenge:

> וְאִם֩ רַ֨ע בְּֽעֵינֵיכֶ֜ם לַעֲבֹ֣ד אֶת־יְהוָ֗ה בַּחֲר֨וּ לָכֶ֣ם הַיּוֹם֮ אֶת־מִ֣י תַעֲבֹדוּן֒ ... וְאָנֹכִי וּבֵיתִי נַעֲבֹד אֶת־יְהוָה
>
> "แต่ถ้าเป็นที่ไม่พอใจในสายตาของพวกเจ้าที่จะรับใช้องค์พระผู้เป็นเจ้า ก็**จงเลือกเอาในวันนี้**ว่าพวกเจ้าจะรับใช้ผู้ใด ... **แต่สำหรับข้าและครอบครัวของข้า เราจะรับใช้**องค์พระผู้เป็นเจ้า"

The 24:15 NOTES field cross-references the entire NT decision-formula thread:

> **NT echo — Choosing a Lord**: คำท้าทายเดียวกันใน 1 พกษ 18:21 (เอลียาห์ที่ภูเขาคาร์เมล), มธ 6:24 (พระเจ้าหรือมัมโมน), ยน 6:67-69 (เปโตร: 'ข้าจะไปที่ใคร?'). โยชูวา 24:15 = แม่แบบของ existential decisio[n]

**Forward NT echo** at Acts 16:31 / 16:33 (Philippian jailer "Believe on the Lord Jesus, and you will be saved, you and your household" — the JOS 24:15 household-salvation pattern directly).

### 24:25–27 covenant ceremony + witness stone:

> וַיִּכְרֹ֨ת יְהוֹשֻׁ֧עַ בְּרִ֛ית לָעָ֖ם בַּיּ֣וֹם הַה֑וּא וַיָּ֥שֶׂם ל֛וֹ חֹ֥ק וּמִשְׁפָּ֖ט בִּשְׁכֶֽם

→ **ในวันนั้นโยชูวาก็ได้ทำพันธสัญญากับประชาชน และที่เชเคมเขาได้ตั้งกฎข้อบังคับและข้อตัดสินไว้สำหรับพวกเขา**

**STABLE — recommend new doc** `docs/translator_decisions/covenant_renewal_ceremony_2026-05.md` would lock:
1. The 24:15 vocative-decision formula (จงเลือกเอาในวันนี้ ... แต่สำหรับข้าและครอบครัวของข้า เราจะรับใช้องค์พระผู้เป็นเจ้า) + the cross-corpus NT-echo thread (1 Kgs 18:21, Matt 6:24, John 6:67–69, Acts 16:31)
2. The "as for me and my house" household-salvation pattern (24:15b → Acts 16:31 + 1 Cor 1:16 Stephanas-household + Acts 11:14 + Acts 18:8 Crispus-household)
3. The Deuteronomic-covenant-renewal ceremonial structure (DEU 29–31 → JOS 24 → Neh 8–10 → Ezra 9–10) — historical prologue + challenge + people-response + stone-witness pattern

Optional follow-up. Not blocking the v1 tag. **STABLE.**

---

## 11. Joshua's death + triple-burial coda (JOS 24:29–33) — **STABLE (rich Layer-2)**

The book closes with three burials at the end of the conquest era:

| Verse | Burial | Thai cross-reference |
|---|---|---|
| 24:30 | Joshua at Timnath-serah (Ephraim hills) | Layer-2 NOTES cross-references Judg 2:9's "Timnath-heres" anagram |
| 24:32 | Joseph's bones at Shechem | Layer-2 NOTES cites Gen 50:25 (oath) + Exo 13:19 (bone-removal) + Acts 7:16 (Stephen's recap) |
| 24:33 | Eleazar at Gibeah-of-Phinehas | Layer-2 NOTES tracks priestly succession |

The 24:32 KD makes the cross-corpus thread explicit:

> **TRIPLE BURIAL OF SHECHEM**: บทนี้ปิดด้วยการบรรยายการฝังสามคน: (1) โยชูวาที่ทิมนาทเสราห์ (v.30); (2) โยเซฟที่เชเคม (v.32); (3) เอเลอาซาร์ที่กิเบอาห์ของฟีนเฮส (v.33). **โยเซฟ** = บรรพบุรุษของเอฟราอิม

The 24:31 NOTES field flags the verbatim parallel with Judg 2:7:

> **BRIDGE TO JUDGES**: ข้อนี้ปรากฏซ้ำเกือบเหมือนกันใน ผพง 2:7. ผู้เขียนของผพงดูเหมือนจะคัดลอกจากยชว 24:31 เพื่อสร้างสะพานเชื่อมระหว่างหนังสือ. แสดงให้เห็นโครงสร้างของ Deuteronomistic History (Dt-2Kgs).

**STABLE** ✓. Optional enhancement: add a Layer-2 footer at JOS 24:31 anchoring the Deuteronomistic-History structural-bridge (Dt → Josh → Judg → 1–2 Sam → 1–2 Kgs) for the corpus-reader-edition.

---

## 12. "Joshua = Jesus" NT-typology Heb 4:8 — **STABLE (verse-NOTES coverage; recommend Layer-2 enhancement)**

Joshua's Greek-equivalent name (Ἰησοῦς) is the same as Jesus' name — and Heb 4:8 makes the explicit typological point:

> **Heb 4:8 (Greek):** εἰ γὰρ αὐτοὺς Ἰησοῦς κατέπαυσεν "for if Joshua had given them rest..."

The argument is that Joshua's rest-giving (the conquest's settlement) was provisional; "another day of rest" remains for the people of God (Heb 4:9), which Christ supplies. The typology requires the reader to recognize Ἰησοῦς-the-Israelite = Ἰησοῦς-the-Christ wordplay — a typology that Thai readers cannot detect because **โยชูวา** (transliterated) ≠ **พระเยซู** (transliterated).

**Editorial finding.** The JOS-side translation correctly preserves **โยชูวา** as the protagonist's name throughout. The Hebrews-audit (already shipped) renders Heb 4:8 with a Layer-2 footer naming the Joshua-name-equivalence; spot-check of `output/translations/hebrews_04.json` would confirm. **No JOS-side Layer-2 footer flagging the future Heb 4:8 typology** appears at JOS 1:1 (the natural anchor — the protagonist-naming moment) or at 22:4 (the "rest" verb anchor in JOS where the rest-theology lands).

**Recommend: STABLE-with-enhancement.** Optional Layer-2 footer at JOS 1:1 (or JOS 22:4 / 23:1) naming the Heb 4:8 typology + the Greek-name equivalence would forward-protect the cross-corpus thread. Not blocking the v1 tag.

---

## 13. Gibeonites + Hivite-treaty (JOS 9–10) — **STABLE (rich Layer-2)**

JOS 9 is the OT-corpus's most-significant case-study of **oath-validity-under-deception**:

- **9:14** "they did not ask counsel from YHWH" (וְאֶת־פִּי יְהוָה לֹא שָׁאָלוּ) → the procedural-failure named in the verse and noted in the KD
- **9:19–20** "we have sworn to them by YHWH the God of Israel" → the binding nature of the oath
- **9:27** Gibeonites become "hewers of wood and drawers of water" → permanent-Levitical-service status
- **10:1–14** the YHWH-fights-for-Gibeonites consequence

Cross-references in the JOS 9 NOTES + Layer-2 footers:
- 2 Sam 21:1–14 (Saul's later breach of the Gibeonite oath → bloodguilt + famine)
- Heb 6:13–18 (oath-by-greater-than-self theology)

The Gibeonite-treaty is a sub-case of the broader ḥerem-exception cluster (Rahab + Gibeonites = the two non-Israelite groups exempted from JOS-conquest ḥerem). Both already have rich verse-level rationale. **STABLE** ✓.

---

## 14. Adonai-in-prayer at JOS 7:7–8 — **REVIEW (second downstream test of NUM 14:17 + DEU 3:24 / 9:26 pattern)**

Joshua's prayer-of-lament after the Ai-defeat is the only major Joshua-as-character prayer in the book, and it uses the Adonai-in-prayer form twice in adjacent verses with two different surfaces:

| Verse | Hebrew | Thai | Pattern |
|---|---|---|---|
| 7:7 | אֲהָ֣הּ׀אֲדֹנָ֣י יְהוִ֗ה | **อนิจจา ข้าแต่องค์พระผู้เป็นเจ้า** | compound אֲדֹנָי יְהוִה → matches NUM 14:17 + DEU 3:24 / 9:26 |
| 7:8 | בִּ֖י אֲדֹנָ֑י | **โอ้ ข้าแต่องค์เจ้านาย** | standalone אֲדֹנָי → "องค์เจ้านาย" (distinct from compound form) |

**Editorial assessment.** The 7:7 form (compound אֲדֹנָי יְהוִה → ข้าแต่องค์พระผู้เป็นเจ้า) is the third downstream-witness for the NUM 14:17 + DEU 3:24/9:26 Adonai-in-prayer pattern. The 7:8 form (standalone אֲדֹנָי → ข้าแต่องค์เจ้านาย) is a principled split that distinguishes:
- compound אֲדֹנָי יְהוִה (prayer-as-divine-address; Adonai + Tetragrammaton collapsed into the standard YHWH-form) → **ข้าแต่องค์พระผู้เป็นเจ้า**
- standalone אֲדֹנָי (prayer-as-vocative-only) → **ข้าแต่องค์เจ้านาย**

This 2-form principled split is **DIFFERENT** from the simple compound-Adonai pattern in DEU 3:24 + 9:26 + NUM 14:17 (all compound אֲדֹנָי יְהוִה).

**REVIEW flag — confirm with Ben.** The 7:8 standalone-Adonai → "องค์เจ้านาย" rendering is principled (single-yodh adoni / plural-yodh adonai not distinguished; instead the compound-vs-standalone distinction drives the Thai rendering). Worth amending `divine_names_table_2026-05.md` per the DEU-audit §14 + NUM-audit §8 + this audit §14 cumulative pattern:
- **Compound אֲדֹנָי יְהוִה** (prayer + Tetragrammaton) → **ข้าแต่องค์พระผู้เป็นเจ้า**
- **Standalone אֲדֹנָי** (prayer-vocative without Tetragrammaton) → **ข้าแต่องค์เจ้านาย**
- **Standalone אֲדֹנָי** (non-prayer-title — e.g. JOS 10:17 "Adonai of Adonais") → **องค์เจ้านายของบรรดาเจ้านาย** (current DEU-doc form)
- **Single-yodh אֲדֹנִי** (my-lord — human/angel address) → **เจ้านายของข้าพเจ้า** (JOS 5:14 form)

Folded with the DEU audit §14 + NUM audit §8 outstanding REVIEW; JOS 7:7–8 becomes the locking precedent for the 4-way distinction.

---

## 15. Hebrew oath formulas — **LOCKED**

Three major oath-cycles in JOS, all compliant with `hebrew_oath_formulas_2026-05.md`:

| Verse | Sworn by | Thai surface |
|---|---|---|
| 2:12–14 | Rahab + spies (mutual) | חֶ֤סֶד וֶֽאֱמֶת structure preserved; **โดยสาบาน** + ฉัน-fidelity formula |
| 6:26 | Joshua's curse on Jericho-rebuilder | **สาบานในเวลานั้น** (preserves the curse-oath sub-genre) |
| 9:15+20 | Joshua + leaders + Gibeonites (one-way) | **ทำพันธสัญญาแก่พวกเขาและสาบาน** ("made covenant with them and swore"); doc-locked |
| 14:9 | Moses to Caleb (recap) | **สาบาน** preserved |
| 23:7 | Israel future-prohibition on swearing by other gods | **อย่าสาบานในนามของพระอื่น** — directly contrasts JOS 2:12 + 9:15 (legitimate oath-by-YHWH) |

The 9:15–20 KD documents the oath-binding-under-deception interpretive frame and cross-references 2 Sam 21 + Heb 6:13–18 (already noted in §13). The 6:26 curse-oath is one of the DTr-history's most famous "fulfilled curses" (1 Kgs 16:34, Hiel of Bethel rebuilding Jericho).

**LOCKED** ✓ per `hebrew_oath_formulas_2026-05.md`. JOS confirms the doc across the first downstream OT-narrative book.

---

## 16. Inherited corpus locks — **all compliant except where flagged**

| Doc | JOS evidence | Status |
|---|---|---|
| `divine_names_table_2026-05.md` | §1, §2, §14. Tetragrammaton uniform (~225/225); El → พระเจ้า; Adonai compound + standalone split. **EXCEPTION:** JOS 7:7 + 7:8 Adonai-in-prayer 2-form distinction (§14 — folded into NUM 14:17 / DEU 3:24+9:26 outstanding REVIEW). | **LOCKED-with-§14-flag** |
| `ot_register_policy_2026-05.md` | Joshua-as-character uses plain register to humans + humble register to YHWH (7:7–9 lament) ✓. Royal ทรง- maintained for YHWH-volitional actions ✓. Local Canaanite kings (JOS 2:3 king of Jericho → Rahab) plain register ✓. **EXCEPTION:** none flagged. | **LOCKED** |
| `chesed_covenant_love_2026-05.md` | **Zero חֶסֶד occurrences in JOS** verified — JOS is conquest-narrative, not covenant-poetry. The relational-fidelity vocabulary at 2:12 (Rahab+spies oath) uses דֶּ֤סֶד + אֱמֶת but in a human-mutual-oath frame, not divine-chesed; the verse-level rendering preserves the lemma without a doc-anchor. Compliant. | **LOCKED (N/A)** |
| `narrator_vs_character_voice_2026-04.md` | Joshua narrator throughout (3rd-person framing in chs 1, 5, 6, 7, etc.); Joshua-as-character speaks plain register to Israel + humble register to YHWH. Compliant. | **LOCKED** |
| `divine_anthropomorphism_thai_grammar_2026-05.md` | "Strong hand and outstretched arm" formula recurs in JOS 4:24 (יַד יְהוָה כִּי חֲזָקָה הִיא → **พระหัตถ์ของพระเจ้านั้นทรงพลัง**) and 8:18 (יַד הַיְהוָה outstretched-spear motif) — uniform with EXO/NUM/DEU precedent ✓. The 5:13–15 anthropomorphic "drawn sword in his hand" of the Captain (חַרְבּוֹ שְׁלוּפָה בְּיָדוֹ → ดาบที่ชักออกในมือของเขา) preserved literally ✓. | **LOCKED** |
| `hebrew_grammar_transfer_2026-05.md` | Wayyiqtol chains pervasive in conquest-narrative chs 6–11; cognate-accusative דָּגְלוּ + נֵ֖ד forms preserved at 3:13+16 ("waters stood up as one heap"); imperative-of-prohibition (e.g. JOS 1:9 אַל־תַּעֲרֹץ → **อย่าหวาดหวั่น**); the inf-absolute הוֹבִישׁ הוֹבִישׁ at 4:23 + the ḥerem-cognate-accusative הַחֲרֵם תַּחֲרִם idiom — all compliant. | **LOCKED** |
| `hebrew_idioms_and_metaphor_2026-05.md` | The "heart melted" לֵבָב נָמַס leitwort recurs at JOS 2:11, 5:1, 7:5, 14:8 — uniform Thai surface **ใจ ... ละลาย / หัวใจของพวกเขาสลาย** ✓. The "with all your heart and all your soul" formula at 22:5 + 23:14 → **ด้วยใจสุดและจิตสุดของพวกท่าน** (echoes DEU 6:5 Shema; cross-corpus note in §6 of DEU-audit). The "until this day" עַד הַיּוֹם הַזֶּה leitwort at 4:9, 5:9, 6:25, 7:26, 8:28+29, 9:27, 13:13, 14:14, 15:63, 16:10, 22:3, 22:17, 23:8+9 (~15 occurrences) → uniform **จวบจนทุกวันนี้ / จนถึงวันนี้** ✓. Compliant. | **LOCKED** |
| `verse_schema_and_versification_2026-05.md` | No notable MT/English chapter-boundary divergences in JOS. The JOS 8:30–35 (altar on Mount Ebal) is located before JOS 9 in MT but appears after JOS 9 in LXX (the famous LXX-divergence) — verse-order preserved per MT; Layer-2 footer at `output/textual_variants/joshua_08.json` confirms the disposition. Compliant. | **LOCKED** |
| `proper_names_and_transliteration_2026-05.md` | ~500+ proper-noun renderings spot-checked: Joshua **โยชูวา** (uniform), Caleb **คาเลบ**, Phinehas **ฟีนเฮส**, Eleazar **เอเลอาซาร์**, Rahab **ราหับ**, Achan **อาคาน**, Adoni-Zedek **อาโดนีเศ-เดก**, the 31-king-list of ch.12 spot-checked. Place-names: Jericho **เยรีโค**, Ai **อัย**, Gibeon **กิเบโอน**, Gilgal **กิลกาล**, Shechem **เชเคม**, Shiloh **ชิโลห์**, Bethel **เบธเอล**, Hebron **เฮโบรน**, Beersheba **เบเอร์เชบา**, Mount Ebal **เอบาล**, Mount Gerizim **เกริซิม**, Jordan **จอร์แดน** (uniform). **EXCEPTIONS:** Seven-Nations ethnonym 3-way drift across JOS 3:10 / 9:1+11:3+12:8 / 24:11 — see §4 DECIDE. | **LOCKED-with-§4-DECIDE** |
| `proper_noun_wordplay_2026-05.md` | JOS 5:9 Gilgal etymology גַּלּוֹתִי "I rolled away" → **เราได้กลิ้งการตำหนิของอียิปต์ออกจากเจ้า** + KD on the Gilgal-roll wordplay ✓. JOS 7:26 Achor "trouble" → "หุบเขาแห่งความเดือดร้อน" (preserves wordplay) ✓. JOS 24:30 Timnath-serah / Judg 2:9 Timnath-heres anagram noted in 24:30 NOTES ✓. Compliant. | **LOCKED** |
| `mt_vs_lxx_textual_variant_handling_2026-05.md` | 23 of 24 chapters have `output/textual_variants/joshua_NN.json` files. **EXCEPTION:** ch.16 (tribal-allotments-Ephraim) is the only chapter missing a textual_variants file — see §18 mechanical. JOS 10:13 Book-of-Jashar Layer-2 footer ✓. JOS 8:30–35 altar-Ebal LXX-order Layer-2 footer ✓. JOS 24:33 LXX has an additional verse 24:33a-b (about Phinehas's priesthood) — Layer-2 footer at `joshua_24.json` confirms MT shorter form shipped. Compliant. | **LOCKED-with-§18-flag** |
| `ot_warfare_ethics_2026-05.md` | See §9. JOS is the second-densest ḥerem book in the corpus (after DEU). 2-surface internal split principled by binyan; Layer-2 anchor footer density HIGHER than DEU. **STABLE-with-DEU-§7-coordination-flag** — the JOS surface family ("อุทิศ ... ให้พินาศ" / "ทำลายล้าง ... จนสิ้น") differs from the DEU-audit-§7 recommended canonical "ทุ่มถวายเพื่อทำลาย". | **REVIEW (coordinate w/ DEU §7)** |
| `i_am_yhwh_holiness_formula_2026-05.md` | JOS 24:2 has the historical-prologue formula פֹּה אָמַר יְהוָה אֱלֹהֵי יִשְׂרָאֵל ("Thus says YHWH the God of Israel") — uniform with the Pentateuchal prophet-mouth lock ✓. No formal "I am YHWH" אֲנִי יְהוָה occurrences in JOS proper. | **LOCKED (limited test)** |
| `paqad_visit_attend_2026-05.md` | פָּקַד occurs at JOS 8:10 (Joshua "mustered the people"; visiting-purpose); semantic-context preserved. No drift. | **LOCKED** |
| `manah_divine_appointment_2026-05.md` | **Zero מָנָה occurrences in JOS.** N/A. | **LOCKED (N/A)** |
| `malak_yhwh_2026-05.md` | **Zero מַלְאַךְ-יְהוָה occurrences in JOS.** The Captain-of-host (5:13–15) is a DIFFERENT construct (אִישׁ + שַׂר־צְבָא־יְהוָה); see §3 — recommend new doc `captain_of_yhwh_host_2026-05.md` that cross-references and distinguishes from `malak_yhwh_2026-05.md`. | **LOCKED (N/A); new sibling doc recommended** |
| `kapporet_atonement_cover_2026-05.md` | **Zero כַּפֹּרֶת occurrences in JOS.** N/A. | **LOCKED (N/A)** |
| `kareth_penalty_formula_2026-05.md` | **Zero priestly-Levitical karet occurrences in JOS.** The ḥerem-curse cluster is broader. N/A. | **LOCKED (N/A)** |
| `hagiasmos_hagiosune_2026-05.md` | קֹדֶשׁ occurrences at 5:15 ("ที่บริสุทธิ์" — sacred-place) + 7:13 ("ชำระประชาชนให้บริสุทธิ์" — sanctify) — uniform ✓. | **LOCKED** |
| `hebrew_oath_formulas_2026-05.md` | §15 — three major oath-cycles compliant. | **LOCKED** |
| `pagan_deities_2026-04.md` | JOS 24:2 + 24:14 + 24:15 + 24:16 + 24:20 + 24:23 — "other gods" אֱלֹהִים אֲחֵרִים → **พระอื่น / พระอื่นๆ** ✓; the Mesopotamian-river + Egyptian + Amorite-trans-Jordan + Canaanite "other gods" cluster cleanly distinguished from YHWH. Compliant. | **LOCKED** |
| `ot_polytheistic_register_2026-05.md` | JOS 24:2 — fathers worshipped אֱלֹהִים אֲחֵרִים "on the other side of the river" — preserves the historical-polytheistic context without flattening to pagan-pejorative. JOS 22:34 ("Witness between us that YHWH is God") — Reuben+Gad+half-Manasseh altar-of-witness uses the divine-name correctly. Compliant. | **LOCKED** |
| `goel_kinsman_redeemer_2026-05.md` | JOS 20–21 uses גֹּאֵל הַדָּם "blood-avenger" form — **EXCEPTION:** the JOS surface "ผู้แก้แค้นโลหิต" diverges from NUM 35's "ผู้แก้แค้นเลือด" + DEU 19's "ผู้แก้แค้นแทนเลือด" — see §5 DECIDE. | **DRIFT (§5 DECIDE)** |
| `leitwort_handling_policy_2026-05.md` | The שָׁמַע "hear/obey" leitwort recurs across JOS 1:18, 5:1, 6:5, 9:1, 10:1, 11:1, 22:2, 24:24 ~~~ + the "to this day" leitwort recurs ~15× — both uniform Thai ✓. The "heart melted" לֵבָב נָמַס leitwort at 2:11, 5:1, 7:5, 14:8 — uniform ✓. Compliant. | **LOCKED** |
| `divine_object_praise_verbs_2026-04.md` | JOS 7:19 ("Give glory to YHWH the God of Israel" — Achan's confession) → **จงยอมรับเกียรติแด่องค์พระผู้เป็นเจ้า** ✓; JOS 22:25 ("ceasing to fear YHWH" — Reubenite altar concern) → **เลิกยำเกรงองค์พระผู้เป็นเจ้า** ✓. Compliant. | **LOCKED** |
| `historic_present_2026-04.md` | N/A — Hebrew narrative, not Greek-NT. | **LOCKED (N/A)** |
| `inclusion_variants_absent_verses_2026-04.md` | `audit_inclusion_variants.py --book joshua --strict` returns 0 candidates ✓. N/A. | **LOCKED (N/A)** |
| `aramaic_transliterations_2026-04.md` | N/A — pre-Aramaic OT narrative. | **LOCKED (N/A)** |
| `nicham_divine_relenting_2026-05.md` | Zero formal naham occurrences in JOS. N/A. | **LOCKED (N/A)** |
| `uncover_nakedness_euphemism_2026-05.md` | N/A in JOS. | **LOCKED (N/A)** |
| `shared_names_normalization_2026-05.md` | Tribal names + ancestors (Abraham, Isaac, Jacob at 24:2–4) — all match prior-book locks ✓. Tribal-listings in chs 13–19 spot-checked. Compliant. | **LOCKED** |
| `sacrificial_vocabulary_2026-05.md` | JOS 8:30–31 (Mount Ebal altar of unhewn stones — DEU 27:5 fulfilment) → **แท่นบูชาที่ทำด้วยหินที่ไม่ได้สลัก** + **เครื่องบูชาเผา + เครื่องบูชามิตรภาพ** ✓ doc-canonical. JOS 22 (Reubenite altar-of-witness) properly distinguishes the ritual sacrifice from the memorial-witness function. Compliant. | **LOCKED** |

---

## 17. NT-cross-corpus JOS-quote drift cluster — **REVIEW (lower forward-protection priority than DEU §17)**

JOS is **less-quoted-in-the-NT** than DEU, but four important NT cross-references rely on the JOS Thai surface:

| JOS verse | NT echo | Match? |
|---|---|---|
| **JOS 1:5 + 1:9** ("I will be with you...") | **Heb 13:5** (paraphrased: "I will never leave you nor forsake you") | needs Hebrews-side cross-check |
| **JOS 2:11 / 5:1** (heart-melt leitwort) | not directly NT-quoted but the typology recurs in Acts 7 + Heb 11:31 backdrop | N/A (allusion only) |
| **JOS 6:17 + 6:22–25** (Rahab spared) | **Heb 11:31** (Ραάβ ἡ πόρνη), **Jas 2:25**, **Matt 1:5** | needs NT-side cross-check — see §6 |
| **JOS 6:25** (Rahab "dwells in Israel to this day") | not directly NT-quoted but Matt 1:5 incorporation-into-Davidic-line | N/A (background only) |
| **JOS 7:1+11** (Achan's ḥerem-violation) | **Acts 5:1–11** (Ananias + Sapphira ḥerem-typology backdrop) | not formal-quote |
| **JOS 24:32** (Joseph's bones at Shechem) | **Acts 7:16** (Stephen's recap: "they were carried back to Shechem") | needs Acts-side cross-check |
| **JOS 22:5 + 23:14** (love YHWH with all your heart + soul) | **Mark 12:30 / Matt 22:37 / Luke 10:27** (Shema-quotation) | folded into DEU-audit §17 nephesh/psyche cross-corpus DECIDE |

**Note on the JOS-name + Heb 4:8.** See §12 — the most-significant cross-corpus NT-typology that JOS triggers is the Joshua-name = Jesus-name typology of Heb 4:8. **Recommend the Heb 4:8 Layer-2 footer cross-check** on `output/translations/hebrews_04.json`.

**Recommend: REVIEW.** Lower priority than the DEU-audit §17 forward-protection (where the OT-prophet vocabulary + Decalogue + Shema cluster cross-quotation are the load-bearing items). For JOS, the load-bearing NT-thread is the **Rahab cluster** — already covered in §6 recommended doc; the **rest theology + Joshua-name** — already covered in §12 recommended Layer-2 enhancement; and the **Joseph-bones + Acts 7:16** — needs verification on the Acts-side. None of these block the v1 tag.

---

## 18. Mechanical (§1) — **all green except `joshua_16.json` missing textual-variants**

- 24/24 chapters: `output/check_reports/joshua_NN_review.md` + sub-reports ✓
- 24/24 chapters: `output/back_translations/joshua_NN.json` ✓
- 24/24 chapters: `output/translations/joshua_NN.json` ✓
- **23/24 chapters: `output/textual_variants/joshua_NN.json` — `joshua_16.json` is missing.** (Joshua 16 is a tribal-allotments-Ephraim chapter with relatively-low YHWH-density and minor cross-corpus textual issues; the absence may be principled — every-chapter-needs-a-textual-variants-file is not a hard rule in the OT pilot — but worth confirming the disposition.) **REVIEW.**
- `python3 scripts/check_key_term_consistency.py`: **0 rule violations, 0 undocumented multi-renderings** across the 318-chapter corpus
- `python3 scripts/check_phrase_consistency.py`: **0 violations across 8 audited locks** (7,943 verses)
- `python3 scripts/audit_inclusion_variants.py --book joshua --strict`: **0 candidates** ✓
- `git status output/`: **clean** ✓
- Hebrew word-spacing: spot-checked across chs 1, 5, 6, 7, 10, 24 — all clean ✓
- `thai_literal` field: surveyed via Grep for English-token leakage; **3 false-positives** (JOS 01:520, 02:75, 22:135 — all are intentional KD-annotations with parenthetical "literal: ..." or register-marker text, not stray English in the actual Thai surface). **No DEU-15:19-style mechanical leakage in JOS.** ✓
- **Footnote-template wording.** JOS uses the post-NUM-14 short-template form across all 24 chapters; no "ยาห์เวห์" Thai-marker drift in the chapter-footers (the inclusio-note at 24:29 uses "ยาห์เวห์" in commentary-prose but NOT in the verse-text — see §1). Compliant. ✓

**Severity: LOW** — single missing textual-variants file at JOS 16.

---

## 19. Flagged for Ben's attention

### A. Seven-Nations ethnonym 3-way drift WITHIN Joshua — **DECIDE before tagging** (§4)
Normalize JOS 9:1, 11:3, 12:8, 24:11 ethnonyms to the JOS 3:10 / DEU 7:1 bare-suffix form (เปริซซี / ฮีไว / เยบุส). Cost: ~5 surgical verse-edits + glossary entries. Pairs with the DEU-audit-§6b REVIEW. **HIGH severity** — forward-protects Judg 1+3, 1 Kgs 9, Ezra 9, Neh 9 ethnonym lists.

### B. Cities-of-refuge + blood-avenger Pentateuch surface-divergence — **DECIDE before tagging** (§5)
Normalize JOS 20–21 `เมืองหลบภัย` → `เมืองลี้ภัย` + `ผู้แก้แค้นโลหิต` → `ผู้แก้แค้นเลือด` (NUM 35 form). Coordinate with DEU 19's "แทน" particle sub-drift per DEU-audit §17. Cost: ~10–15 surgical verse-edits across JOS 20:2+3+5+6+9 + JOS 21:13+21+27+32+38. **HIGH severity** — forward-protects 2 Sam 14, 2 Sam 3, 1 Kgs 2, Ruth-already-shipped, Heb 6:18 NT typology.

### C. Captain-of-host new corpus doc — **STABLE; new doc** (§3)
Write `docs/translator_decisions/captain_of_yhwh_host_2026-05.md` locking שַׂר־צְבָא־יְהוָה → **ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า** + Christophany-ambiguity-preserved stance + EXO 3:5 typological lock at JOS 5:15. Forward-protects Daniel 8 + 10 + 12, 2 Kgs 6:17, Zech 14:5.

### D. Jordan-crossing dry-ground + heap typology new corpus doc — **STABLE; new doc** (§7)
Write `docs/translator_decisions/jordan_red_sea_typology_2026-05.md` locking נֵד → **กอง** + יַבָּשָׁה/חָרָבָה → **พื้นแห้ง** across EXO 14–15 + JOS 3–4 + Psalms-of-deliverance + NT Heb 11:29 / 1 Cor 10:1–2.

### E. Rahab the zonah + NT-typology new corpus doc — **STABLE; new doc** (§6)
Write `docs/translator_decisions/rahab_zonah_nt_typology_2026-05.md` locking זוֹנָה → **หญิงโสเภณี** + the Rahab+spies narrative-ethic stance + the Matt 1:5 / Heb 11:31 / Jas 2:25 NT-triad cross-corpus thread.

### F. Ḥerem 2-surface binyan-principled split — **REVIEW (coordinate with DEU-audit §7 DECIDE)** (§9)
JOS's nominal-vs-verbal split (**อุทิศ ... ให้พินาศ** vs **ทำลายล้าง ... จนสิ้น**) is cleaner than DEU's 5-form drift. **Recommend amend `ot_warfare_ethics_2026-05.md`** to lock the JOS binyan-principled distinction as the canonical 2-form (path-a in DEU-audit §7), normalize DEU's 5 forms to the JOS pattern, and cite JOS 6:17 + 6:21 as paired locking precedents.

### G. Adonai-in-prayer at JOS 7:7 + 7:8 — **REVIEW (compounds NUM 14:17 + DEU 3:24 / 9:26)** (§14)
Amend `divine_names_table_2026-05.md` with the 4-way distinction:
- compound אֲדֹנָי יְהוִה (prayer) → **ข้าแต่องค์พระผู้เป็นเจ้า** (lock with NUM 14:17 + DEU 3:24/9:26 + JOS 7:7)
- standalone אֲדֹנָי (prayer-vocative) → **ข้าแต่องค์เจ้านาย** (JOS 7:8 becomes the precedent)
- standalone אֲדֹנָי (non-prayer-title) → **องค์เจ้านาย / องค์เจ้านายของบรรดาเจ้านาย** (DEU 10:17 form)
- single-yodh אֲדֹנִי (my-lord, human/angel) → **เจ้านายของข้าพเจ้า** (JOS 5:14 form)

### H. JOS 16 missing textual-variants file — **REVIEW** (§18)
Confirm whether `output/textual_variants/joshua_16.json` should exist (ch.16 is tribal-allotments-Ephraim with limited cross-corpus textual issues; absence may be principled). Mechanical-fix-or-confirm.

### I. Optional Layer-2 enhancement at JOS 1:1 (or 22:4 / 23:1) — Joshua-name + Heb 4:8 typology — **STABLE** (§12)
Add a Layer-2 footer at JOS 1:1 naming the Joshua-name = Jesus-name equivalence + the Heb 4:8 "rest" typology. Forward-protects the cross-corpus thread. Not blocking.

### J. Optional new corpus doc: covenant-renewal ceremony — **STABLE** (§10)
Write `docs/translator_decisions/covenant_renewal_ceremony_2026-05.md` locking the JOS 24:15 + 24:25–27 ceremonial structure + the Acts 16:31 household-salvation NT-echo thread. Not blocking.

### K. New corpus docs to write — **summary**
1. **`captain_of_yhwh_host_2026-05.md`** (§3) — locks שַׂר־צְבָא־יְהוָה title + Christophany-ambiguity policy
2. **`jordan_red_sea_typology_2026-05.md`** (§7) — locks dry-ground + heap typology
3. **`rahab_zonah_nt_typology_2026-05.md`** (§6) — locks Rahab + NT-triad cross-corpus thread
4. **(Optional)** `covenant_renewal_ceremony_2026-05.md` (§10) — JOS 24 ceremonial structure
5. **(Optional, if DEU-audit §17 lands)** `cities_of_refuge_blood_avenger_2026-05.md` (§5) — formal lock for the 3-anchor lemma-pair

### L. Existing docs to amend
- **`divine_names_table_2026-05.md`** — 4-way Adonai distinction per §14 (compounds NUM-audit §8 + DEU-audit §14 + JOS §14)
- **`ot_warfare_ethics_2026-05.md`** — lock the JOS 2-form binyan-principled ḥerem-Thai surface (§9 — coordinate with DEU-audit §7)
- **`proper_names_and_transliteration_2026-05.md`** + **`glossary.json`** — seven-nations cluster (§4 DECIDE)
- **`goel_kinsman_redeemer_2026-05.md`** — note the JOS 20–21 blood-avenger surface and link to the cities-of-refuge cluster (§5 DECIDE)

### M. External AI review (§3 of checklist) — **pending**
Recommended 5-cluster external AI packet:
1. **Ethnonym 3-way drift WITHIN Joshua** (§4 — JOS 3:10 / 9:1+11:3+12:8 / 24:11)
2. **Cities-of-refuge + blood-avenger Pentateuch surface-divergence** (§5 — NUM 35 / DEU 19 / JOS 20–21)
3. **Captain of YHWH's host + Christophany-ambiguity policy** (§3 — JOS 5:13–15 + EXO 3:5 typology)
4. **Ḥerem 2-surface binyan-principled split** (§9 — JOS vs DEU coordination)
5. **Adonai-in-prayer 4-way distinction** (§14 — JOS 7:7+8 as the precedent for the docking-decision)

Use Grok + ChatGPT in parallel per the JHN/GAL/DEU pattern.

---

## Counts per status code (TL;DR)

- **LOCKED:** 14 items (§1 YHWH + servant-of-YHWH inclusio, §2 divine names compound, §8 sun-stood-still + Book of Jashar, §11 triple-burial coda, §13 Gibeonites, §15 oath formulas, §16 inherited locks compliant subset including `ot_register_policy`, `hebrew_grammar_transfer`, `hebrew_idioms`, `verse_schema`, `proper_noun_wordplay`, `pagan_deities`, `ot_polytheistic_register`, `leitwort_handling`, `divine_object_praise_verbs`, `hagiasmos`, `divine_anthropomorphism`, `shared_names_normalization`, `sacrificial_vocabulary`, `historic_present`-N/A, `inclusion_variants`-N/A, `aramaic`-N/A, `nicham`-N/A, `uncover_nakedness`-N/A, `manah`-N/A, `malak_yhwh`-N/A, `kapporet`-N/A, `kareth`-N/A, `chesed`-N/A, `i_am_yhwh`-limited, `paqad`)
- **STABLE (recommend new doc):** 3 items (§3 captain-of-host, §6 Rahab + NT-typology, §7 Jordan/Red-Sea typology); + 2 optional (§10 covenant-renewal, §12 Joshua-name Heb 4:8 layer-2 enhancement)
- **REVIEW:** 3 items (§9 ḥerem 2-surface coordinate-w/DEU, §14 Adonai-in-prayer compounds NUM 14:17/DEU 3:24+9:26, §18 JOS 16 missing textual-variants file)
- **DECIDE:** 2 items (§4 ethnonym 3-way WITHIN-JOS drift HIGH, §5 cities-of-refuge + blood-avenger Pentateuch surface-divergence HIGH)

**2 DECIDE items block the `book-joshua-v1` tag.** (§4, §5)

**3 new translator_decisions docs recommended** (`captain_of_yhwh_host_2026-05.md`, `jordan_red_sea_typology_2026-05.md`, `rahab_zonah_nt_typology_2026-05.md`) + 2 optional + 1 contingent on §5 resolution.

**2 existing docs to amend** (`divine_names_table_2026-05.md` Adonai 4-way distinction; `ot_warfare_ethics_2026-05.md` ḥerem binyan-principled lock) + 2 lower-priority (`proper_names_and_transliteration_2026-05.md` + `goel_kinsman_redeemer_2026-05.md` cross-references).

---

## Recommendation

**Joshua ships in strong corpus-hygiene shape** — and is the FIRST PROOF that the Pentateuch-era OT locks (divine names, OT register, Hebrew idioms + grammar transfer, leitwort handling, divine anthropomorphism, oath formulas, pagan deities, polytheistic register, proper names) carry cleanly into the Former-Prophets corpus. The Layer-2 footer density across JOS 5:13–15 (Captain-of-host), 6:17–25 (ḥerem + Rahab), 10:12–14 (sun-stood-still + Book of Jashar), and 24:29–33 (triple-burial coda) is the **richest cross-corpus annotation density** in the OT-pilot to date.

However, **2 DECIDE items** must resolve before tagging `book-joshua-v1`:
1. **§4 — Seven-Nations ethnonym 3-way drift WITHIN Joshua.** Forward-protects 5+ Former-Prophets + post-exilic ethnonym lists.
2. **§5 — Cities-of-refuge + blood-avenger Pentateuch surface-divergence.** Forward-protects 2 Sam + Kgs + Ruth + Heb 6:18 NT typology.

The 3 STABLE-but-undocumented items (§3 captain-of-host, §6 Rahab + NT-typology, §7 Jordan/Red-Sea typology) should be lifted to corpus docs **before Judges ships** (Judg 6 + Judg 13 will re-test the captain-of-host / mal'akh-YHWH boundary; Judg 1+3 will re-test the ethnonym lock; Ruth-already-shipped contains the gōʾēl-kinsman cluster that interlocks with §5).

Tag `book-joshua-v1` after:
1. Ben's decisions on **§A + §B** (DECIDE: ethnonym drift; cities-of-refuge+blood-avenger drift)
2. Ben's confirmation on **§F + §G + §H** (REVIEW: ḥerem coordinate with DEU §7; Adonai-in-prayer 4-way distinction; JOS 16 textual-variants disposition)
3. Three new translator_decisions docs written (**§C + §D + §E** — captain-of-host, Jordan/Red-Sea typology, Rahab + NT-typology)
4. Two existing docs amended (`divine_names_table_2026-05.md` Adonai 4-way; `ot_warfare_ethics_2026-05.md` JOS ḥerem binyan-split)
5. External AI sanity-check (§M)

The Former-Prophets corpus (Judg, Ruth-already-shipped, 1–2 Sam, 1–2 Kgs) can be queued for next book — but writing the three new docs (especially `captain_of_yhwh_host_2026-05.md` before Judges 6 + 13's mal'akh-YHWH-vs-captain ambiguity recurs) is the load-bearing forward-protection step.
