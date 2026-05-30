## Item A — `הַשָּׂטָן` rendered as the proper name ซาตาน (the article-marked council role "the accuser")

**The pattern:** Job's prologue uses `הַשָּׂטָן` 11× (1:6, 7, 8, 9, 12 ×2; 2:1, 2, 3, 4, 6, 7), **always with the definite article** `הַ-`. In Hebrew this marks a **title / office** — "*the* accuser / *the* adversary," a prosecuting function within YHWH's heavenly court — not yet the proper personal name "Satan" of later Second-Temple and NT theology. The Eremos Thai renders the **proper name ซาตาน** at every occurrence.

The translator's own `key_decision` at 1:6 identifies the issue and then renders the proper name by convention:
> `הַשָּׂטָן (มีคำนำหน้านามชี้เฉพาะ = ‘ผู้กล่าวหา/ปฏิปักษ์’ ซึ่งเป็นบทบาท/ตำแหน่ง) → ‘ซาตาน’ ตามสำนวนที่ใช้ทั่วพระคัมภีร์`
> ("ha-satan has the definite article = 'the accuser/adversary,' which is a role/office → rendered 'Satan' per familiar biblical convention.")

**Verse evidence:**
- Job 1:6 HEB: `וַיָּבוֹא גַם־הַשָּׂטָן בְּתוֹכָם` → TH: `และ**ซาตาน**ก็มาท่ามกลางพวกเขาด้วย` (English: "and *the accuser* also came among them")
- Job 1:7 HEB: `וַיֹּאמֶר יְהוָה אֶל־הַשָּׂטָן` → TH: `องค์พระผู้เป็นเจ้าตรัสกับ**ซาตาน**ว่า` ("YHWH said to *the accuser*")
- Job 2:1 HEB: `וַיָּבוֹא גַם־הַשָּׂטָן בְּתוֹכָם לְהִתְיַצֵּב עַל־יְהוָה` → TH: `และ**ซาตาน**ก็มาท่ามกลางพวกเขาเพื่อเข้าเฝ้าต่อพระพักตร์พระองค์ด้วย`

**Corpus context (already shipped, unflagged):** `1 Chronicles 21:1` renders the *article-less* `שָׂטָן` ("an adversary stood up against Israel") **also** as ซาตาน:
- 1 Chr 21:1 HEB: `וַיַּעֲמֹד שָׂטָן עַל־יִשְׂרָאֵל` → TH: `แล้ว**ซาตาน**ก็ลุกขึ้นต่อสู้อิสราเอล`

So the corpus has flattened *both* the article-marked council-role (Job) and the article-less form (1 Chr) to the same proper name — a coherent convention, but undocumented and made by default. Modern translations diverge: NRSV "Satan" + footnote "the Accuser"; CEB/NABRE "the Adversary" / "the satan"; ESV/NIV keep "Satan." It compounds forward to **Zechariah 3:1–2** (`הַשָּׂטָן`, the cleanest courtroom-accuser scene) and **Psalm 109:6** (`שָׂטָן` at the accused's right hand).

**Two questions:**
1. Is rendering the article-marked `הַשָּׂטָן` as the proper name **ซาตาน** (rather than a role-noun like **ผู้กล่าวหา** "the accuser") defensible for a Thai reader, given that the Hebrew article marks an *office in the divine council* rather than the personal "Satan" of NT theology? Does the choice import a later-developed identification into the Job prologue?
2. If ซาตาน is retained for corpus consistency (it matches the shipped 1 Chr 21:1), should Job 1:6 carry a Layer-2 footnote explaining that the Hebrew is the article-marked role "ผู้กล่าวหา / the accuser" — parallel to how the project footnotes the "sons of God" interpretive crux? And should the choice be locked in a `translator_decisions/` doc before Zechariah 3 ships?

---

## Item B — Shaddai (`שַׁדַּי`) standalone-title consistency: bare `ผู้ทรงมหิทธิฤทธิ์` vs. `องค์ผู้ทรงมหิทธิฤทธิ์`

**The pattern:** `שַׁדַּי` ("the Almighty") appears 31× in Job — the densest concentration in the OT. All 31 use the locked lexeme **ผู้ทรงมหิทธิฤทธิ์** (per `divine_names_table_2026-05.md`). But the standalone-title form drifts by chapter: the six earliest occurrences are **bare**, and every occurrence from 13:3 onward adds the honorific classifier **`องค์-`** ("the Almighty One"):

| Form | Count | Verses |
|---|---|---|
| `ผู้ทรงมหิทธิฤทธิ์` (bare) | 6 | 5:17, 6:4, 6:14, 8:3, 8:5, 11:7 |
| `องค์ผู้ทรงมหิทธิฤทธิ์` (with `องค์-`) | 25 | 13:3, 15:25, 21:15, 21:20, 22:3, 22:17, 22:23, 22:25, 22:26, 23:16, 24:1, 27:2, 27:10, 27:11, 27:13, 29:5, 31:2, 31:35, 32:8, 33:4, 34:10, 34:12, 35:13, 37:23, 40:2 |

**Verse evidence (same grammatical position, different form):**
- Job 8:3 HEB: `וְשַׁדַּי יְעַוֵּת־צֶדֶק` → TH: `**ผู้ทรงมหิทธิฤทธิ์**ทรงบิดเบือนความเที่ยงธรรมหรือ` (bare; Almighty as subject)
- Job 21:15 HEB: `מַה־שַּׁדַּי כִּי־נַעַבְדֶנּוּ` → TH: `**องค์ผู้ทรงมหิทธิฤทธิ์**คือผู้ใดเล่าที่เราจะต้องปรนนิบัติพระองค์` (`องค์-`; Almighty as subject)

The split is a chapter-progression drift (bare in chs. 5–11, `องค์-` from 13 on), **not** a positional or grammatical distinction. Both are correct Thai; `องค์-` reads more naturally as a standalone divine title. The divine-names table currently locks the bare form `ผู้ทรงมหิทธิฤทธิ์`.

**Question:** Should the six early bare occurrences (5:17, 6:4, 6:14, 8:3, 8:5, 11:7) be normalized to the dominant **`องค์ผู้ทรงมหิทธิฤทธิ์`** (25/31), and the divine-names-table row updated to record `องค์ผู้ทรงมหิทธิฤทธิ์` as the standalone-title form — so the rendering is uniform across Job and forward into Ruth 1:20–21, Isa 13:6, Joel 1:15, Ezek 1:24?

---

## Item C — Job's mediator / arbiter / witness thread and the messianic-marking asymmetry with the Redeemer (19:25)

**The pattern:** Job repeatedly longs for an intermediary between himself and God — a coherent theological thread that Christian tradition reads as foreshadowing Christ the mediator (1 Tim 2:5). The Eremos Thai renders the thread consistently in **plain (human) register**, but renders the parallel "Redeemer" confession at 19:25 in **divine/royal register** — an asymmetry worth examining:

| Verse | Hebrew | Thai | Register |
|---|---|---|---|
| 9:33 | `מוֹכִיחַ` (umpire/arbiter) | **คนกลาง** ("mediator") | plain |
| 16:19 | `עֵד` / `שָׂהֵד` (witness/guarantor in heaven) | **พยาน / ผู้รับรอง** | plain |
| 33:23 | `מַלְאָךְ מֵלִיץ` (mediating angel) | **ทูตสวรรค์ … คนกลาง** | plain |
| **19:25** | `גֹּאֵל` (redeemer) | **พระผู้ไถ่** ("divine Redeemer," royal `พระ-` + `ทรง-`) | **divine** |

**Verse evidence:**
- Job 9:33 HEB: `לֹא יֵשׁ־בֵּינֵינוּ מוֹכִיחַ` → TH: `ไม่มี**คนกลาง**ระหว่างเรา ที่จะวางมือบนเราทั้งสองฝ่าย` ("there is *no* arbiter between us") — KD cross-refs 1 Tim 2:5.
- Job 16:19 HEB: `הִנֵּה־בַשָּׁמַיִם עֵדִי` → TH: `ดูเถิด **พยาน**ของข้าอยู่ในฟ้าสวรรค์ และ**ผู้รับรอง**ของข้าอยู่ ณ เบื้องสูง` — KD cross-refs 19:25.
- Job 19:25 HEB: `וַאֲנִי יָדַעְתִּי גֹּאֲלִי חָי` → TH: `ส่วนข้าพระองค์ ข้าพระองค์รู้ว่า**พระผู้ไถ่**ของข้าพระองค์**ทรง**พระชนม์อยู่` ("I know that my Redeemer lives") — locked divine register per `goel_kinsman_redeemer_2026-05.md`.
- Job 33:23 HEB: `אִם־יֵשׁ עָלָיו מַלְאָךְ מֵלִיץ` → TH: `หากมี**ทูตสวรรค์**อยู่ข้างเขา เป็น**คนกลาง**สักคนในพันคน`

**Question:** Is the register asymmetry principled — i.e., 19:25 marked divine/royal because it is a positive confession of certainty ("I *know* my Redeemer *lives*"), while 9:33/16:19/33:23 are kept plain because they describe a *hypothesized or explicitly absent* arbiter (9:33: "there is *no* umpire") — so that royal-marking them would over-read the Hebrew? Or should the thread be rendered with more consistent register? (Either way: the thread is Job-distinctive, the 1 Tim 2:5 / Heb cross-references make it a recurring reviewer touchpoint, and it currently has no consolidating `translator_decisions/` doc.)

---

## Item D — Textual cruxes: the 13:15 ketiv/qere faith-confession and the 23:2 BSB-over-MT departure

**The pattern:** Job is the OT's most textually difficult book. Two cruxes are worth a reviewer's eye on whether the reader is adequately served.

**13:15 — the book's most-quoted line — turns on a ketiv/qere variant:**
- HEB: `הֵן יִקְטְלֵנִי לוֹ אֲיַחֵל` — **ketiv** `לֹא` = "I have **no** hope"; **qere** `לוֹ` = "yet will I hope **in him**." The two readings are theological opposites (despair vs. faith).
- The translation follows the **qere** (= BSB, the faith-reading): TH: `แม้พระองค์จะทรงประหารข้า ข้าก็ยัง**หวังในพระองค์**` ("though he slay me, yet will I hope in him").
- The choice is recorded in the verse `notes`, but there is **no Tier-2 reader-facing footer** (`output/textual_variants/job_13.json` does not exist).

**23:2 — the surface text follows BSB / ancient versions *against* the Masoretic Text:**
- HEB (MT): `יָדִי כָבְדָה עַל־אַנְחָתִי` — MT reads `יָדִי` ("**my** hand is heavy on my groaning"); ancient versions + BSB read `יָדוֹ` ("**his** [God's] hand is heavy despite my groaning").
- The translation follows BSB: TH: `**พระหัตถ์ของพระองค์**หนักอยู่ทั้งที่ข้าคร่ำครวญ`. Recorded in the verse `notes` only.

The project base text is MT (`ot_canon_and_text_base_2026-05.md`); departures of this kind are exception-(1) ("disputed MT reading; ancient versions preserve a clean reading"). Under `mt_vs_lxx_textual_variant_handling_2026-05.md` §2.3, routine minor cruxes need no reader-facing footer — but 13:15 is arguably *materially reader-affecting* (the difference between despair and the book's signature confession of faith).

**Two questions:**
1. Should **Job 13:15** carry a Tier-2 reader-facing footer noting the ketiv reading ("I have no hope") — given it is the most-quoted line in Job and the ketiv/qere difference inverts the meaning — or is the verse-note disposition + qere-follows-BSB sufficient (since THSV and most English versions also follow the qere)?
2. Is the **23:2** departure from MT (`my hand` → `his hand`, following BSB/ancient versions) the intended treatment, and is a verse-note (rather than a Tier-2 footer) the correct disclosure level for a non-theologically-significant MT departure of this kind?
