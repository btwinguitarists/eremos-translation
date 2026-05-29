# Locked-surface audit — 2026-05-29

**The lock↔check gap, closed.** The project encodes ~93 translation decisions as locks in `docs/translator_decisions/`, but only ~20 were enforced by any `check_*.py`. This audit (triggered by the Nehemiah review finding NEH 9:17 had silently drifted from the locked Exod-34 formula) swept the remaining 72 unenforced locks for drift, and ran a cross-book consistency sweep for same-source/different-Thai divergences that per-book checks miss.

**Method.** Multi-agent workflow (read-only): 18 agents audited the 72 docs — each extracting a candidate check and validating it against the live corpus with the project's own `audit_one_lock` logic (the same false-positive discipline used on Exod-34); 6 agents ran the cross-book sweep; each cross-book candidate was adversarially re-checked against the JSONs. ~4.4M tokens across 50 agents.

## Outcomes at a glance

| | Count |
|---|---|
| Unenforced locks audited | 72 |
| Machine-checkable | 28 (23 wired here · 5 need manual refinement) |
| Correctly non-checkable (register/sense-split/meta-policy) | 44 |
| **Guards wired this PR** (`check_phrase_consistency.py`: 12 → 35 locks) | **23** |
| Drift verses found (lock-audit) | 38 |
| Cross-book inconsistencies confirmed | 21 (9 high · 12 medium) |

**This PR changes no shipped text** — it only adds the 23 validated guards (current drift is recorded as documented exceptions so the suite stays green). The verse fixes below are a sign-off worklist; the cross-book decisions are yours to adjudicate.

---
## Part 1 — Guards wired in this PR (23)

Each was corpus-validated (catches its drift, zero false positives on correct verses). 16 found the corpus already compliant (pure forward-protection); 7 found current drift (excepted, pending sign-off in Part 2).

| Lock | Enforces (Thai) | Current drift |
|---|---|---|
| `captain_of_yhwh_host` | ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า | — clean |
| `cities_of_refuge_blood_avenger` | ผู้แก้แค้นเลือด | — clean |
| `decalogue_parallel_text` | ลักทรัพย์ | 2 |
| `dikaioo_dikaiosyne_family` | ประกาศ | 5 |
| `epiphaneia_christou` | การทรงปรากฏ | — clean |
| `evil_spirit_from_yhwh_1sam` | วิญญาณชั่ว | — clean |
| `huiothesia_adoption` | สิทธิ์การเป็นบุตร | — clean |
| `hygiaino_sound_doctrine` | ถูกต้อง | — clean |
| `i_am_yhwh_holiness_formula` | องค์พระผู้เป็นเจ้า | — clean |
| `kapporet_atonement_cover` | พระที่นั่งกรุณา | — clean |
| `kareth_penalty_formula` | ตัดออก | 1 |
| `logos_johannine` | พระวาทะ | — clean |
| `manah_divine_appointment` | ทรงจัดเตรียม | — clean |
| `metanoeo_vs_metamelomai` | กลับใจ | — clean |
| `ot_nt_cross_quotation_thread` | ผู้เผยพระวจนะ | 12 |
| `parepidemos_paroikos_sojourner` | คนต่างถิ่น | 1 |
| `pharaoh_heart_hardening` | แข็งกระด้าง | 1 |
| `revelation_divine_self_titles` | ผู้ทรงฤทธานุภาพยิ่งใหญ่ | — clean |
| `shared_names_normalization` | ราม | — clean |
| `spiritual_beings_hierarchy` | ผู้ทรงเดชานุภาพ | — clean |
| `stoicheia_tou_kosmou` | หลักการพื้นฐานของโลก | — clean |
| `telos_paidagogos_christ` | จุดสิ้นสุดของธรรมบัญญัติ | — clean |
| `therion_beast_apocalyptic` | สัตว์ร้าย | — clean |

---
## Part 2 — Drift to fix (38 verses)

All are "conform shipped text to an existing lock" (enforcement, not new decisions). **Regressions** (a decision documented as already-corrected but never applied to the shipped file) are the highest-confidence, lowest-risk fixes. Grouped by lock; ☑ = guard wired this PR.

> **✅ APPLIED in this PR (19 highest-confidence, Ben-approved 2026-05-29):** the 10 true-prophet `ผู้พยากรณ์→ผู้เผยพระวจนะ` (Luke 9:8/9:19/10:24, Acts 21:10, 1 Cor 14:29/14:32/14:37, Rev 10:7/11:10/11:18); `δικαιόω` Rom 2:13 + 1 Cor 6:11 (`นับว่า→ถูกประกาศว่า/ประกาศว่า`); Decalogue Rom 13:9 (`อย่าขโมย→อย่าลักทรัพย์`); kareth Gen 17:14 (`ตัดขาด→ตัดออก`); `parepidemos` Heb 11:13; `judges` 1 Sam 4:18/7:6/7:15/7:16/7:17 (`ตัดสิน→วินิจฉัย`). Their guard exceptions were removed — the checks now enforce them.
>
> **⏸ HELD for your call (not applied):** **Titus 1:12** + **2 Pet 2:16** (προφήτης = pagan Cretan poet / Balaam — `ผู้เผยพระวจนะ` may be wrong for non-true-prophets); **Exodus 20:7** (Decalogue — clean §1 rule to mirror DEU 5:11, but a multi-phrase rewrite of a flagship verse — wants your glance); **1 Sam 6:6** (idiom reinterpretation heavy→hardened); **James 2:21/24/25** (doc has a deferral clause); and the non-checkable-doc drifts in `ot_warfare_ethics`, `nicham_divine_relenting`, `nomos_pauline`, `ot_polytheistic_register`, `hebrew_oath_formulas` (judgment-scoped).

### `ot_nt_cross_quotation_thread` — 12 verses · ☑ wired
- **Luke 9:8** — προφήτης τις (a prophet of old) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **Luke 9:19** — προφήτης rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **Luke 10:24** — πολλοὶ προφῆται (many prophets) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **Acts 21:10** — προφήτης (Agabus, a prophet) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **1 Corinthians 14:29** — προφῆται (the prophets) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **1 Corinthians 14:32** — προφητῶν προφήταις (of/to prophets) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **1 Corinthians 14:37** — προφήτης εἶναι (to be a prophet) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **2 Peter 2:16** — προφήτου (Balaam the prophet) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **Titus 1:12** — ἴδιος αὐτῶν προφήτης (their own prophet, Epimenides) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **Revelation 10:7** — τοὺς προφήτας (his servants the prophets) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **Revelation 11:10** — οἱ δύο προφῆται (the two prophets) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ
- **Revelation 11:18** — τοῖς προφήταις (the prophets) rendered ผู้พยากรณ์; locked form is ผู้เผยพระวจนะ

### `dikaioo_dikaiosyne_family` — 5 verses · ☑ wired
- **Romans 2:13** — δικαιωθήσονται (passive future, believer-justification) — doc REQUIRES จะทรงถูกประกาศว่าชอบธรรม and the doc's own 'Stale Romans 1-5 corrections' table (line 118) records this verse as already corrected on 2026-05-01. Shipped Thai still read…
- **1 Corinthians 6:11** — ἐδικαιώθητε (passive aorist, 'you were justified') — 1 Corinthians is in the doc's stated forward-scope (line 100). Shipped Thai uses the rejected ได้รับการนับว่าชอบธรรม instead of the locked ประกาศว่าชอบธรรม. (Note: the neighboring ได้รับก…
- **James 2:21** — ἐδικαιώθη (Abraham justified by works) — doc §'James 2:21-25' (lines 107-108) directs the SAME ถูกประกาศว่าชอบธรรม so Thai readers see the same verb in Paul and James. Shipped Thai uses ได้รับการนับว่าชอบธรรม. Caveat: the doc adds a deferra…
- **James 2:24** — δικαιοῦται ('a person is justified by works') — same James rule (lines 107-108); shipped Thai uses ได้รับการนับว่าชอบธรรม instead of the locked ประกาศว่าชอบธรรม. Same deferral caveat as James 2:21.
- **James 2:25** — ἐδικαιώθη (Rahab justified by works) — same James rule (lines 107-108); shipped Thai uses ได้รับการนับว่าชอบธรรม instead of locked ประกาศว่าชอบธรรม. Same deferral caveat.

### `judges_shaphat_deliverer_cycle` — 5 verses · ○ non-checkable (judgment-scoped)
- **1SA 4:18** — Deliverer-office tenure formula וְהוּא שָׁפַט אֶת־יִשְׂרָאֵל אַרְבָּעִים שָׁנָה (Eli 'had judged Israel forty years', BSB 'judged Israel') — locked surface วินิจฉัยอิสราเอล (identical syntax to JDG 15:20 'Samson judged Israel twenty years' …
- **1SA 7:6** — וַיִּשְׁפֹּט שְׁמוּאֵל אֶת־בְּנֵי יִשְׂרָאֵל בַּמִּצְפָּה — Samuel judging Israel at Mizpah, deliverer-office sense the doc cites explicitly (Forward-protection: '1 SAM 7:6 ... deliverer-sense → วินิจฉัยอิสราเอล'). Shipped uses courtroom ตั…
- **1SA 7:15** — וַיִּשְׁפֹּט שְׁמוּאֵל אֶת־יִשְׂרָאֵל כֹּל יְמֵי חַיָּיו ('Samuel judged Israel all the days of his life') — lifelong-tenure deliverer formula the doc explicitly forward-locks (1 SAM 7:15-17 → วินิจฉัยอิสราเอล). Shipped uses ตัดสิน, not the…
- **1SA 7:16** — וְשָׁפַט אֶת־יִשְׂרָאֵל — Samuel's annual Bethel/Gilgal/Mizpah circuit. The doc explicitly states this 'IS deliverer-office circuit, not courtroom-circuit ... Same handling as Deborah' → วินิจฉัย. Shipped uses courtroom ตัดสิน, the exact 'e…
- **1SA 7:17** — וְשָׁם שָׁפָט אֶת־יִשְׂרָאֵל (Samuel at Ramah) — deliverer-office formula in the 7:15-17 block the doc forward-locks to วินิจฉัยอิสราเอล. Shipped uses ตัดสิน, not the locked วินิจฉัย.

### `ot_warfare_ethics` — 5 verses · ○ non-checkable (judgment-scoped)
- **1SA 15:3** — Hiphil וְהַחֲרַמְתֶּם (devote-to-destruction command, Amalek herem) ships the SUPERSEDED §4.1 surface ทุ่มถวาย outside DEU; §4.1.1 requires 1 Sam 15 to use the new forms (Hiphil verbal -> ทำลายล้าง…จนสิ้น) from the start.
- **1SA 15:15** — Hiphil herem ships superseded §4.1 surface ทุ่มถวาย outside DEU; §4.1.1 new verbal form ทำลายล้าง…จนสิ้น required.
- **1SA 15:18** — Hiphil וְהַחֲרַמְתָּה ships superseded §4.1 surface ทุ่มถวาย outside DEU; §4.1.1 new verbal form required.
- **1SA 15:20** — Hiphil herem ships superseded §4.1 surface ทุ่มถวาย outside DEU; §4.1.1 new verbal form ทำลายล้าง…จนสิ้น required.
- **1SA 15:21** — nominal הַחֵרֶם (the devoted thing) ships superseded §4.1 surface ทุ่มถวาย outside DEU; §4.1.1 new nominal form อุทิศ…ให้พินาศ required.

### `decalogue_parallel_text` — 2 verses · ☑ wired
- **Romans 13:9** — §4 HARD-FAIL: NT Decalogue citation of the 8th commandment (Οὐ κλέψεις) ships the rejected colloquial verb อย่าขโมย instead of the locked judicial-register §3 surface อย่าลักทรัพย์. The other three list-citations (Matt 19:18, MRK 10:19, Luk…
- **Exodus 20:7** — §1 identical-Hebrew→identical-Thai violation: EXO 20:7 and DEU 5:11 are byte-identical Hebrew (לא תשא את שם יהוה אלהיך לשוא...), but EXO 20:7 ships 'อย่ายกพระนาม...โดยเปล่าประโยชน์' while DEU 5:11 (the §3-locked form) ships 'อย่าออกพระนาม..…

### `hebrew_oath_formulas` — 2 verses · ○ non-checkable (judgment-scoped)
- **Nehemiah 9:15** — §1.1 raised-hand oath. Hebrew אֲשֶׁר נָשָׂאתָ אֶת־יָדְךָ (God 'lifted his hand' = swore the land-promise) — explicitly listed in the doc §1.1 occurrence list (Neh 9:15). The two sibling DIVINE raised-hand-oath verses render the locked core …
- **Genesis 22:16** — §1.3 self-oath, doc-string-vs-corpus mismatch (NOT a translation drift, but a lock-doc accuracy issue). Doc §1.3 quotes the Thai lock as 'เราสาบานในตัวของเราเอง', but the only shipped occurrence (Gen 22:16, בִּי נִשְׁבַּעְתִּי) ships 'เราได…

### `nicham_divine_relenting` — 2 verses · ○ non-checkable (judgment-scoped)
- **1SA 15:11** — Doc §2 'Thai (locked)' table (line 58) AND §3.1 (line 80) explicitly classify 1 Sam 15:11 (נִחַמְתִּי כִּי־הִמְלַכְתִּי אֶת־שָׁאוּל) as sub-sense A and lock the Thai as 'เราเปลี่ยนพระทัยที่เราตั้งซาอูลเป็นกษัตริย์'. The shipped Thai instead…
- **1SA 15:35** — Same Saul-rejection lemma (וַיהוָה נִחָם כִּי־הִמְלִיךְ אֶת־שָׁאוּל) one verse-cluster from 15:11. Not given its own row in §2, but §3.1 groups the whole Saul-rejection episode under sense A. Shipped Thai uses ทรงเสียพระทัย (grief form), co…

### `kareth_penalty_formula` — 1 verse · ☑ wired
- **Genesis 17:14** — Kareth penalty formula וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא מֵעַמֶּיהָ. Locked Thai surface = ตัดออก (ถูกตัดออกจาก...ชนชาติ), used by all 20 other Pentateuch occurrences. Genesis 17:14 ships the variant ถูกตัดขาด (จะถูกตัดขาดจากชนชาติของเขา) — ตัดข…

### `nomos_pauline` — 1 verse · ○ non-checkable (judgment-scoped)
- **1 Corinthians 9:21** — ἔννομος Χριστοῦ ('within-the-law-of / under the law of Christ') is shipped as ธรรมบัญญัติของพระคริสต์ ('Mosaic Torah of Christ'), but the doc locks this Pauline νόμος-of-Christ construction as กฎของพระคริสต์ ('principle/governing-norm of Ch…

### `ot_polytheistic_register` — 1 verse · ○ non-checkable (judgment-scoped)
- **1SA 8:8** — אֱלֹהִים אֲחֵרִים (foreign 'other gods' that Israel goes and serves) rendered พระเจ้าอื่น, applying the YHWH-reserved word พระเจ้า to foreign deities — the exact slide §1.3 forbids. Locked surface is พระอื่น (used in 42/44 occurrences) or เ…

### `parepidemos_paroikos_sojourner` — 1 verse · ☑ wired
- **Hebrews 11:13** — Doc locks παρεπίδημος -> คนต่างถิ่น (and the matched doublet ξένος -> คนแปลกหน้า), and names this exact verse as the cross-corpus test ('preserve the doublet; ξένος -> คนแปลกหน้า to distinguish from the παρεπίδημος -> คนต่างถิ่น lock'). Shi…

### `pharaoh_heart_hardening` — 1 verse · ☑ wired
- **1SA 6:6** — Locked idiom is ใจ...แข็งกระด้าง (harden the heart). 1 Sam 6:6 uses Hebrew כבד ('make heavy') with לבבכם/לבם (heart) and is EXPLICITLY in the doc's §4 trajectory checklist ('1 Samuel 6:6 — Philistine reflection on Pharaoh, retrospective ...…

---
## Part 3 — Cross-book inconsistencies (21 confirmed)

Same source rendered differently across books — the class per-book checks miss. **Bucket A** = align an outlier to an existing lock (sign-off, like Part 2). **Bucket B** = genuine "pick one form" decisions for you.

### HIGH severity (9)
- **παντοκράτωρ (pantokrator) — 'the Almighty', a NT divine title; LXX rendering of YHWH Tseba**
  - → Pick one Thai form for παντοκράτωρ corpus-wide and align both books. The Revelation lock (ผู้ทรงฤทธานุภาพยิ่งใหญ่) is the senior decision (formal decision doc, 9 occurrences, externally reviewed FINE), so normalize 2 Cor…
- **חַי־יהוה (chay-YHWH), the asseverative oath 'As surely as YHWH lives' — the single most fr**
  - → Add a חַי־יהוה entry to hebrew_oath_formulas_2026-05.md and pick ONE asseverative Thai surface (the Kings comparative ‘…ทรงพระชนม์อยู่แน่ฉันใด’ is the most idiomatic and unambiguous). Correct Judges 8:19 and Ruth 3:13 aw…
- **כֹּה יַעֲשֶׂה (אֱלֹהִים/יהוה) … וְכֹה יֹסִיף — the covenant self-curse oath 'May God do th**
  - → Lock one rendering of כֹּה יַעֲשֶׂה … וְכֹה יֹסִיף in hebrew_oath_formulas_2026-05.md (the literal ทรงทำเช่นนี้แก่… และยิ่งกว่านี้อีก best preserves the doubled-oath idiom and is already the majority/Samuel form) and con…
- **בָּרוּךְ יהוה (baruk YHWH) — the doxological benediction 'Blessed be YHWH', standardly fol**
  - → Lock บָרูค-YHWH to the well-attested liturgical สาธุการแด่องค์พระผู้เป็นเจ้า (used by Exodus/Kings/Chronicles/Ezra) and conform Genesis, Ruth, and Samuel. Keep genuine variation only where Hebrew differs (e.g. a finite v…
- **Foreign Persian/Babylonian emperors as narrator-voice subjects: כּוֹרֶשׁ (Cyrus), דָּרְיָו**
  - → Resolve the open question the Ezra translator flagged: apply ot_register_policy §2.2 uniformly — give foreign emperors (Cyrus, Darius, Artaxerxes, Nebuchadnezzar) full narrator-voice ราชาศัพท์ (ทรง/ตรัส/เสด็จ) in Ezra, m…
- **δικαιόω (dikaioō) — the verb "to justify / declare righteous" (Pauline forensic-declarativ**
  - → Revise the verb δικαιόω to the locked ประกาศว่าชอบธรรม family in Rom 2:13 (จะทรงถูกประกาศว่าชอบธรรม), 1 Cor 6:11 (ได้รับการทรงประกาศว่าชอบธรรมแล้ว), and James 2:21/24/25 — reserving นับ strictly for λογίζομαι. Keep the d…
- **חֶׁסֶד (chesed) in human-to-human contexts — the action 'do / show chesed (loyal kindness)**
  - → Revise Gen 40:14, Jdg 1:24, Jdg 8:35, and 2 Chr 24:22 to ความรักมั่นคง to match Joshua/Samuel/Ruth and the doc's §3.2 lock. If the project genuinely wants a covenant/non-covenant register split for human chesed, that is …
- **יַד יהוה / בְּיַד יהוה — 'the hand of YHWH' (as afflicting/empowering divine agent), incl.**
  - → Normalize the Samuel-corpus 'hand of YHWH' occurrences (1SA 5:6, 5:9, 5:11, 6:3, 6:5, 6:9, 7:13; 2SA 24:14) from มือ to พระหัตถ์ to match the documented §2.1 mandate and the rest of the corpus. The Ark plague is a high-v…
- **פְּלִשְׁתִּים / פְּלִשְׁתִּי (pelishtim, 'Philistine(s)') — one of the most frequent OT et**
  - → Pick one canonical surface (the locked ฟิลิสเตีย per proper_names_and_transliteration_2026-05.md) and normalize all four variants to it corpus-wide. Highest-volume fixes: Judges (36x ฟีลิสตี → ฟิลิสเตีย), 2 Chronicles (7…

### MEDIUM severity (12)
- **עֶלְיוֹן ('Elyon) standalone — the divine title 'the Most High' used by itself (not in the**
  - → Normalize standalone OT Elyon to the locked table form ผู้สูงสุด — i.e., change DEU 32:8 องค์ผู้สูงสุด → ผู้สูงสุด to match NUM 24:16 and 2SA 22:14. Alternatively, if the maintainer prefers องค์ผู้สูงสุด for the standalo…
- **δεσπότης (despotes) — 'Sovereign Master', a divine title applied to God/Christ (distinct f**
  - → Align all divine δεσπότης to the locked องค์เจ้านาย, using the vocative particle ข้าแต่ for the direct addresses: Luke 2:29 → ข้าแต่องค์เจ้านาย, Acts 4:24 → ข้าแต่องค์เจ้านาย (matching Rev 6:10's องค์เจ้านาย). This also …
- **וְנִכְרְתָה הַנֶּפֶשׁ … מֵעַמָּיו / מִקֶּרֶב עַמּוֹ — the kareth penalty 'that soul shall **
  - → Conform Genesis 17:14 to the locked ถูกตัดออกจาก (it is the canonical first kareth and should anchor the leitwort). Add Acts 3:23 to the kareth doc's NT-echo list and align it to the OT form (ถูกตัดออกจาก…ชนชาติ / ประชาก…
- **ἡγεμών (governor — imperial-province prefect/procurator: Pilate, Felix, Festus)**
  - → Apply the documented lock: change 1 Peter 2:14 from ผู้ปกครอง to ผู้ว่าราชการ (so v.13-14 read กษัตริย์...ผู้ว่าราชการ), per roman_administrative_titles_2026-04.md line 69. Reserve ผู้ปกครอง for generic governing-authori…
- **פֶּחָה / פַּחוֹת (peḥah — Persian-era provincial governor)**
  - → Pick one Thai rendering for פֶּחָה across the Persian-period corpus (Ezra/Nehemiah/Esther + the Solomonic parallels) and apply it uniformly. Recommend เจ้าเมือง (provincial governor, distinct from the NT-locked ผู้ว่าราช…
- **οἱ ἅγιοι / τοῖς ἁγίοις (hoi hagioi) — the substantival 'the saints / holy ones' as an eccl**
  - → Revise 2 Thess 1:10 from วิสุทธิชนของพระองค์ to ธรรมิกชนของพระองค์ to match the corpus lock and the parallel in 2 Thess 1:10's sibling letters.
- **רַב־חֶׁסֶד (rav-chesed) 'abounding in steadfast love' — the chesed clause of the Exodus 34**
  - → Revise Neh 9:17 from เปี่ยมด้วยความรักมั่นคง to ทรงบริบูรณ์ด้วยความรักมั่นคง to render the rav-chesed clause identically with Exod 34:6 / Num 14:18 / Jonah 4:2, per §3.1. (Worth a separate broader pass: the other attribu…
- **לֵב / לֵבָב of God — the divine 'heart' (seat of will/decision), e.g. בִּלְבָבִי 'in my he**
  - → Lift 1SA 2:35 from หัวใจ to the Rachasap พระทัย (e.g. ตามพระทัยและพระประสงค์ของเรา) and 1SA 13:14 to a พระทัย-based phrase (ชายที่ตรงตามพระทัยของพระองค์) so the divine-heart idiom is uniform with Genesis per §2.1. หัวใจ …
- **בְּעֵינֵי יהוה — 'in the eyes/sight of YHWH' (esp. the Deuteronomistic 'evil/right in the **
  - → Normalize DEU 4:25 from สายตา to สายพระเนตร to match the corpus-wide locked rendering of the evil/right-in-the-eyes-of-YHWH formula. Optionally document that the רַע 'be-evil-before-YHWH' stative (Gen 38:7,10; 1CH 2:3) m…
- **בְּאָזְנֵי יהוה — 'in the ears of YHWH' (something said/done within YHWH's hearing)**
  - → Revise 1SA 8:21 to use the Rachasap พระกรรณ (e.g. กล่าวซ้ำเข้าในพระกรรณขององค์พระผู้เป็นเจ้า) or a royal-hearing paraphrase consistent with §2.1/§2.5, so the divine-ear idiom matches the Numbers handling and never uses p…
- **יִתְנֶחָם — Hithpael of נָחַם with God as subject ('relent / have compassion / change his **
  - → Decide Deut 32:36 explicitly: either (a) treat it as the same relenting/compassion sense and bring it under the נָחַם thread (e.g. retain ทรงเมตตา but add a key_decisions note that this is divine-subject נָחַם in the 'co…
- **בְּנֵי עַמּוֹן / עַמּוֹן ('the Ammonites / sons of Ammon')**
  - → Normalize 1 Chronicles' 13x คนอัมโมน → ชาวอัมโมน to match 2 Chronicles and the rest of the corpus (and Ezra 9:1 as part of the seven-nations cleanup). Extend the ethnonym-prefix consistency check beyond the seven nations…

---
## Part 4 — Decisions for Ben (consolidated)

These are judgment calls (no senior lock to conform to). Three already had open threads:

- **Foreign-emperor register** (cross-book #8) — *this is Item A from PR #173*. `ot_register_policy §2.2` says foreign emperors get narrator-voice ราชาศัพท์; Ezra/2 Chr use plain register; the sweep independently re-confirmed the divergence. Decision governs Esther (Ahasuerus) + Daniel.
- **Persian governor title** `פֶּחָה`/`תִּרְשָׁתָא` (cross-book #10) — *this is Item C from PR #173*. Pick one Thai term across Ezra/Nehemiah/Esther.
- **Covenant/oath/benediction formulas** rendered inconsistently: `חי־יהוה` (as-YHWH-lives), `כֹּה יעשה` (oath-curse), `ברוך יהוה` (benediction) — pick one surface each and lock in `hebrew_oath_formulas`.
- **Deut 32:36** divine relenting (`נחם`) — decide sense vs the `nicham` lock.
- **James 2:21/24/25** `δικαιόω` — the lock directs `ประกาศว่าชอบธรรม`, but the doc adds a "document at James end-of-book audit if a separate decision is warranted" clause. Confirm whether James conforms or gets a documented exception.

---
## Part 5 — Coverage detail

### 5 checkable locks needing manual refinement (NOT wired)
Each encodes more than one rendering in a single field, so it can't be a single `expected_thai_contains`:

- `arnion_amnos_lamb_disambiguation` — regex matched 0 — needs corrected Greek trigger
- `diakonos_pauline` — over-matches (5 false positives) — needs a tighter trigger or is a register-split
- `goel_kinsman_redeemer` — two senses (redeemer גאל vs avenger גאל הדם) → split into 2 locks
- `hilasterion_heb-rom_distinction` — Hebrews (พระที่นั่งกรุณา) vs Romans (เครื่องบูชาลบบาป) → split into 2 locks
- `spirit_of_yhwh_empowerment` — per-pattern Thai (มาเหนือ / สวมทับ / …) → one lock per verb

### 44 correctly non-checkable (register policies, sense-splits, meta-policies)
Not drift — these legitimately have no single fixed Thai surface to enforce. Listed for the record:

`adversary_speech_register`, `chesed_covenant_love`, `christ_hymn_kenosis`, `divine_object_praise_verbs`, `divine_anthropomorphism_thai_grammar`, `erchomai_tachy_revelation_register_split`, `ethnos`, `gender_passages_thai_register`, `glossary_schema_v2`, `hagiasmos_hagiosune`, `hebrew_grammar_transfer`, `hebrew_oath_formulas`, `hebrew_idioms_and_metaphor`, `jephthah_vow`, `judges_shaphat_deliverer_cycle`, `kyrios_narrator_voice_luke_acts`, `leitwort_handling_policy`, `markan_euthys_immediately`, `mt_vs_lxx_textual_variant_handling`, `narrator_vs_character_voice`, `nicham_divine_relenting`, `nomos_pauline`, `ot_polytheistic_register`, `ot_warfare_ethics`, `ouranos_heaven_rendering`, `pagan_deities`, `paqad_visit_attend`, `parousia_christou`, `pascho_pathema_suffering`, `pastoral_corpus_locks`, `petrine_eschatological_disambiguation`, `phroneo_pauline`, `pistis_christou`, `poimen_episkopos_register_split`, `porneia_vs_moicheia_DEFERRED`, `prototokos_pauline`, `psyche_vs_pneuma_anthropological`, `roman_administrative_titles`, `sarx_pauline`, `speech_verbs_adversaries_addressing_divine`, `synoptic_parallel_passages`, `uncover_nakedness_euphemism`, `vocative_kyrie_didaskale_register`, `wordplay_and_paronomasia`

---
## Provenance
Generated from the `lock-enforcement-audit` workflow (run 1: cross-book; run 2: lock-audit, after an args bug zeroed run 1's lock track). All findings corpus-validated read-only; no shipped text changed in this PR. Verse fixes (Parts 2 + 3A) await Ben's sign-off; decisions (Parts 3B + 4) await Ben's adjudication. Companion: the 5 refinement locks and any approved fixes become follow-up PRs.
