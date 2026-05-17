## Item A — Seven-Nations ethnonym 3-way drift WITHIN Joshua

**The drift:** Joshua's five seven-nations lists ship with THREE different Thai-surface families for the same Hebrew lemma-set (פְּרִזִּי / חִוִּי / יְבוּסִי). The DEU end-of-book audit's §6b within-DEU drift (DEU 7:1 bare-suffix vs DEU 20:17 -ต suffix) here becomes a corpus-wide ethnonym-spelling problem at the FIRST downstream OT-narrative book.

**The Hebrew is identical** at all five JOS occurrences (פְּרִזִּי = Perizzite, חִוִּי = Hivite, יְבוּסִי = Jebusite). Only the Thai-transliteration scheme differs:

| Verse | Thai surface (Perizzite / Hivite / Jebusite) | Family |
|---|---|---|
| **JOS 3:10** | **เปริซซี / ฮีไว / เยบุส** (with `ชาว-` prefix) | matches DEU 7:1 bare-suffix (DEU-canonical) |
| **JOS 9:1** | **เปริซไซต์ / ฮีไวต์ / เยบูไซต์** (with `ชาว-` prefix) | -ต suffix family (new JOS-internal) |
| **JOS 11:3** | **เปริซไซต์ / ฮีไวต์ / เยบูไซต์** | -ต suffix family |
| **JOS 12:8** | **เปริซไซต์ / ฮีไวต์ / เยบูไซต์** | -ต suffix family |
| **JOS 24:11** | **เปริสซี / ฮีไวต์ / เยบุสไซต์** | a THIRD spelling — Perizzite matches DEU 20:17's "เปริสซีต" only at "ส"; Jebusite is "เยบุสไซต์" (NEW form) |

**The principle declared but not maintained.** The JOS 3:10 KD names the principle explicitly:

> **7-NATIONS LIST** — corpus standard ตาม ฉธบ 7:1 precedent... รักษาลำดับฮีบรู (ใน JOS 3:10 ลำดับเริ่มจากคานาอัน — ต่างจาก ฉธบ 7:1 ที่เริ่มจากฮิตไทต์)

But the principle stated at JOS 3:10 is not propagated to the four later JOS ethnonym-list verses (9:1, 11:3, 12:8, 24:11), each of which uses a different transliteration family.

**Cross-corpus compound (DEU + JOS) — six different Thai surfaces for the same Hebrew lemma-set:**

| Anchor | Perizzite | Hivite | Jebusite |
|---|---|---|---|
| DEU 7:1 (DEU-canonical) | เปริซซี | ฮีไว | เยบุส |
| DEU 20:17 (DEU-internal drift) | เปริสซีต | ฮีไวต์ | เยบุสีต |
| JOS 3:10 | เปริซซี | ฮีไว | เยบุส |
| JOS 9:1 / 11:3 / 12:8 | เปริซไซต์ | ฮีไวต์ | เยบูไซต์ |
| JOS 24:11 | เปริสซี | ฮีไวต์ | เยบุสไซต์ |

**Forward-compounding.** The seven-nations cluster recurs across five major downstream contexts: Judg 1:4–6 + 3:5 (Israel-dwelling-among Canaanite-Hittite list), 1 Kgs 9:20–21 / 2 Chr 8:7–8 (Solomon's conscription census), Ezra 9:1 (Ezra's mourning over inter-marriage), Neh 9:8 (covenant-history recital). Each downstream ethnonym list will diverge ad-hoc unless the Thai surface is locked NOW.

**Recommended resolution paths:**

(a) **Normalize all JOS ethnonyms to JOS 3:10 / DEU 7:1 bare-suffix form** (เปริซซี / ฮีไว / เยบุส). Most-frequent + DEU-doc-implicit-canonical + the principle JOS 3:10 already declares. Cost: ~5 surgical verse-edits at JOS 9:1, 11:3, 12:8, 24:11 + DEU 20:17 + glossary entries. Pairs with the DEU-audit §6b REVIEW.

(b) **Normalize all anchors to a different canonical spelling** (e.g. fully-transliterated "เปริซไซต์ / ฮีไวต์ / เยบูไซต์"). Less defensible — would require touching DEU 7:1 + breaking the older DEU-shipped form. Higher cost.

(c) **Leave as-is + accept drift.** Worst path — the 5 forthcoming Former-Prophets / post-exilic ethnonym lists will diverge further; corpus traceability breaks at the FIRST downstream test of this lemma cluster.

**Two questions:**

1. Should JOS 9:1, 11:3, 12:8, 24:11 be retroactively normalized to JOS 3:10's bare-suffix form (เปริซซี / ฮีไว / เยบุส, matching DEU 7:1) before tagging `book-joshua-v1`? The pair with DEU 20:17 would be normalized in the same commit to complete the Pentateuch-to-Former-Prophets ethnonym thread.

2. Should `glossary.json` be amended to add explicit entries for the seven-nations cluster (currently absent), so that `check_key_term_consistency.py` HARD FAILS when these ethnonyms diverge in future books? The DEU-audit §6b + this audit §4 both flagged the missing-glossary-entry as a corpus-protection gap.

---

## Item B — Cities of refuge + blood-avenger Pentateuch surface-divergence

**The drift:** Same Hebrew lemma-pair **עִיר־מִקְלָט** + **גֹּאֵל הַדָּם**, three Thai surfaces across three Pentateuchal-corpus anchors. JOS introduces a NEW Thai surface for both halves of a lemma-pair previously locked in NUM 35 + DEU 19.

| Anchor | "city of refuge" (מִקְלָט) | "blood-avenger" (גֹּאֵל הַדָּם) |
|---|---|---|
| **Numbers 35** (10+ occurrences across 35:6–32) | **เมืองลี้ภัย** | **ผู้แก้แค้นเลือด** |
| **Deuteronomy 19:1–13** + DEU 4:41–43 | **เมืองลี้ภัย** | **ผู้แก้แค้นแทนเลือด** (with the "แทน" particle) |
| **Joshua 20–21** (entire 6-cities + Levitical cities catalog) | **เมืองหลบภัย** | **ผู้แก้แค้นโลหิต** (formal-elevated โลหิต) |

Sample JOS 20:3 verse-context:

> **20:3** Hebrew: לָנֻ֤ס שָׁ֨מָּה֙ רוֹצֵ֔חַ מַכֵּה־נֶ֖פֶשׁ בִּשְׁגָגָ֣ה בִּבְלִי־דָ֑עַת וְהָי֤וּ לָכֶם֙ לְמִקְלָ֔ט מִגֹּאֵ֖ל הַדָּֽם
>
> **Thai (shipped):** "เพื่อผู้ฆ่าคนที่ฆ่าผู้อื่นโดยไม่ได้ตั้งใจและไม่ได้รู้ตัว จะหลบหนีไปที่นั่นได้ และเมือง[**หลบภัย**]เหล่านี้จะเป็นที่หลบภัยจากผู้แก้แค้น[**โลหิต**]สำหรับพวกเจ้า"

The 20:3 KD uses the JOS surface explicitly:

> "ผู้แก้แค้นโลหิต" — (gōʾēl haddām) — ญาติใกล้ที่สุดของผู้ตาย

JOS 21:13, 21:21, 21:27, 21:32, 21:38 all use **เมืองหลบภัยสำหรับผู้ฆ่า** in the Levitical-cities formula — uniform WITHIN Joshua but a one-step lemma-drift from the NUM 35 + DEU 19 corpus-base.

**Forward-compounding.** The cities-of-refuge / blood-avenger language recurs across the Former Prophets + NT:
- 2 Sam 14:7–11 (woman of Tekoa's blood-avenger appeal — the rhetorical setup depends on the avenger-lemma)
- 2 Sam 3:27 + 3:30 (Abner's death = blood-avenger context; Joab acting as avenger for Asahel)
- 1 Kgs 2:5 + 2:31–34 (Solomon's purge of Joab on Davidic-blood-avenger grounds)
- **Heb 6:18** — "we who have fled for refuge to take hold of the hope set before us" (the cities-of-refuge motif as NT-Christological typology)

**Recommended resolution paths:**

(a) **Normalize JOS 20–21 to the NUM 35 + DEU 19 corpus-base surface.** Re-render JOS 20:2+3+5+6+9 + JOS 21:13+21+27+32+38 from **เมืองหลบภัย** → **เมืองลี้ภัย**, and **ผู้แก้แค้นโลหิต** → **ผู้แก้แค้นเลือด** (NUM 35 form; DEU 19's "แทน" particle is a separate sub-drift to resolve in the same pass). Cost: ~10–15 surgical verse-edits across 11 verses in JOS 20–21 + 1 KD update.

(b) **Lift the JOS surface to the corpus-canonical + retroactively normalize NUM 35 + DEU 19.** Symmetric edit cost (NUM 35 has ~10 occurrences, DEU 19 has ~5). Defensible if Ben prefers the JOS "หลบภัย" (more natural-Thai "shelter") + "โลหิต" (elevated "blood" register for legal contexts). Highest forward-protection but rewrites two already-shipped books.

(c) **Write `cities_of_refuge_blood_avenger_2026-05.md`** locking ONE canonical surface for the lemma-pair across all three anchors + normalizing the divergent verses to match. Cost: 1 new corpus-doc + ~15–20 surgical verse-edits. Strongest forward-protection.

**Two questions:**

1. Should JOS 20–21's Thai surface (เมืองหลบภัย / ผู้แก้แค้นโลหิต) be retroactively normalized to NUM 35's surface (เมืองลี้ภัย / ผู้แก้แค้นเลือด) before tagging `book-joshua-v1`? Path (a) is the lowest-cost forward-protection; the JOS-side absorbs the corpus-base.

2. Should the doc-lift path (c) be chosen so all three anchors (NUM 35 / DEU 19 / JOS 20–21) and the downstream Former-Prophets occurrences (2 Sam 3 + 14 / 1 Kgs 2) + Heb 6:18 NT typology are locked under one corpus-doc — protecting the cross-corpus thread for the 2–3 future Davidic-history ships?

---

## Item C — Captain of YHWH's host (JOS 5:13–15) — Christophany-vs-angel ambiguity policy

**The translation choice.** JOS 5:13–15 introduces the OT title **שַׂר־צְבָא־יְהוָה** "Commander/Prince of YHWH's host" — a high-density theophanic-Christological passage. The Thai surface is uniform and preserves Hebrew ambiguity:

| Verse | Hebrew | Thai |
|---|---|---|
| 5:14 | אֲנִי שַׂר־צְבָא־יְהוָה | **เราคือผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า** |
| 5:15 | שַׂר־צְבָא יְהוָה | **ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า** |
| 5:15 | שַׁל־נַעַלְךָ מֵעַל רַגְלֶךָ כִּי הַמָּקוֹם אֲשֶׁר אַתָּה עֹמֵד עָלָיו קֹדֶשׁ הוּא | **จงถอดรองเท้าออกจากเท้าของเจ้า เพราะที่ที่เจ้ายืนอยู่นั้นเป็นที่บริสุทธิ์** (verbatim Exod 3:5 lock) |

The 5:14 KD names the ambiguity-preserved stance:

> **CRITICAL THEOLOGICAL TITLE**... อาจเป็นพระคริสต์ก่อนการปรากฏ หรือทูตสวรรค์ระดับสูงสุด.

The 5:14 NOTES field documents the worship-acceptance argument (Joshua's bowing accepted by the figure — contrast Rev 19:10 + 22:8–9 where ordinary angels REFUSE worship) and explicitly preserves Hebrew ambiguity:

> **WORSHIP ACCEPTED**: ผู้บัญชาการไม่ปฏิเสธการนมัสการของโยชูวา... ฉบับเอเรโมสไม่ตัดสินใจในการแปล — รักษาภาพตามต้นฉบับเปิด.

**The forward-cluster.** The שַׂר־צְבָא title (without יְהוָה) recurs at Daniel 8:11 + 8:25 ("prince of the host"); related titles at Daniel 10:13+20+21 + 12:1 (Michael/princes-of-kingdoms); the heavenly-host motif at 2 Kgs 6:17 (Elisha's servant), 1 Kgs 22:19 / 2 Chr 18:18 (Micaiah's vision), Zech 14:5 (kedoshim coming with YHWH). None of these forward verses are shipped yet; the JOS 5 rendering becomes the corpus-locking precedent.

**No corpus-doc currently covers this title.** The existing `malak_yhwh_2026-05.md` covers a related-but-distinct cluster (mal'akh-YHWH passages — Gen 16, Gen 22, Exod 3, Num 22, Judg 6+13). JOS 5:13–15 uses אִישׁ + שַׂר־צְבָא־יְהוָה, not מַלְאַךְ.

**Recommended path:** Write `docs/translator_decisions/captain_of_yhwh_host_2026-05.md` locking:
1. שַׂר־צְבָא־יְהוָה → **ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า**
2. The Christophany-ambiguity-preserved stance (Thai surface declines to commit to "พระคริสต์"; verse-NOTES name the Christophany-vs-high-angel options)
3. The JOS 5:15 ↔ EXO 3:5 verbatim typological lock (both must read identically in Thai)
4. Explicit cross-reference + boundary with `malak_yhwh_2026-05.md` (Captain-of-host ≠ mal'akh-YHWH at the lemma level)
5. Forward-protect Daniel 8 + 10 + 12, 2 Kgs 6:17, Zech 14:5

**Question:** Is the project's policy that the Thai surface should preserve the Christophany-vs-angel ambiguity at JOS 5:13–15 (current shipped form) the correct corpus-default, OR should the Thai surface make the Christophany interpretation explicit (e.g. by adding **พระบุตรของพระเจ้า** or similar marker)? The current ambiguity-preserved choice is conservative and reformation-defensible, but worth confirming as the corpus-policy before Daniel 8 + Zech 14 ship and the related "Prince of the host" cluster requires the same rendering choice.

---

## Item D — Ḥerem 2-surface binyan-principled split — coordinate with DEU-audit §7 DECIDE

**The pattern.** Joshua's ḥerem-related verses ship with TWO Thai surfaces, principled at the Hebrew binyan (verb-stem) level:

| Surface family | Verses | Thai |
|---|---|---|
| **Nominal חֵרֶם** (the thing devoted/banned) | 6:17, 6:18 (3×), 7:1, 7:11, 7:12, 7:13, 7:15, 22:20 | **อุทิศ ... ให้พินาศ** / **สิ่งที่อุทิศ ... ให้พินาศ** / **อุทิศแด่องค์พระผู้เป็นเจ้าให้พินาศโดยสิ้นเชิง** |
| **Hiphil יַחֲרִים** (the act of devoting/destroying) | 6:21, 10:1, 10:28, 10:37, 10:39, 11:11, 11:12 | **ทำลายล้าง ... จนสิ้น** / **ทำลายล้างจนสิ้น** |

The 6:17 KD names the principle:

> **KEY OT TERM** — 'devoted/the ban': เฮเรม (חֵרֶם)... ไทย 'อุทิศให้พินาศโดยสิ้นเชิง' รักษาทั้งมิติการมอบให้พระเจ้าและการทำลาย

**Compared to DEU.** The DEU end-of-book audit (§7) found DEU ships **5 different Thai surfaces** for the same Hebrew lemma חרם (DEU 2:34, 3:6, 7:2, 7:26, 13:16, 13:18, 20:17 each render differently — including "ถวายเฮเรม" transliterated, "ทุ่มถวายเพื่อทำลายอย่างสมบูรณ์", "แยกถวายเฉพาะเพื่อการทำลาย"). The DEU-audit recommended path-a: normalize all DEU ḥerem occurrences to "ทุ่มถวายเพื่อทำลาย" as canonical.

**JOS does not use "ทุ่มถวายเพื่อทำลาย" at all.** The JOS 2-form split (nominal "อุทิศ ... ให้พินาศ" / verbal "ทำลายล้าง ... จนสิ้น") is a cleaner editorial pattern than DEU's 5-form drift — but it diverges from the DEU-audit's recommended canonical surface.

**Layer-2 anchor density.** JOS has rich Layer-2 doctrinal footers at 6:17, 6:18, 7:1, 7:11, 11:20 (heart-hardening + judgment), and 22:20 — denser than DEU which concentrates at 20:17 alone.

**Coordination paths:**

(a) **JOS surface stays; DEU normalizes TO the JOS 2-form principle.** Replace DEU's 5-form drift with the JOS binyan-principled 2-form. Doc-amend `ot_warfare_ethics_2026-05.md` to lock this distinction:
   - nominal חֵרֶם → **อุทิศ ... ให้พินาศ**
   - hiphil יַחֲרִים → **ทำลายล้าง ... จนสิ้น**

(b) **JOS + DEU both normalize TO a third canonical "ทุ่มถวายเพื่อทำลาย"** (the DEU-audit-§7 recommendation, applied uniformly across both binyan forms). JOS ~12 verses + DEU ~5 verses re-rendered. Strongest unified rendering.

(c) **Leave as-is, accept the cross-book inconsistency.** Forward-protection fails at 1 Sam 15:3–9 (Saul–Amalek ḥerem) + 1 Kgs 20:42 (Ben-Hadad).

**Question:** Which coordination path is correct? (a) is recommended because the JOS binyan-principled split preserves the Hebrew lexical distinction (nominal-devoted-things vs verbal-destroying-act) that the proposed DEU canonical "ทุ่มถวายเพื่อทำลาย" partially collapses; but (b) is the cleaner unified rendering if Ben prefers a single Thai surface across the corpus. The decision is paired with the DEU-audit §7 outstanding DECIDE.

---

## Item E — Adonai-in-prayer 4-way distinction at JOS 7:7–8 — compounds NUM 14:17 + DEU 3:24 / 9:26 outstanding REVIEW

**The pattern across the OT-pilot.** The אֲדֹנָי-in-prayer / Adonai-as-divine-vocative pattern occurs at three Pentateuch verses + one Joshua verse, and JOS 7:7–8 introduces a NEW principled distinction between compound and standalone forms:

| Verse | Hebrew | Thai | Form |
|---|---|---|---|
| NUM 14:17 | אֲדֹנָי (in Moses' prayer context after the spies' rebellion) | **ข้าแต่องค์พระผู้เป็นเจ้า** | compound-treatment (collapses Adonai-YHWH formula) |
| DEU 3:24 | אֲדֹנָי יְהוִה | **ข้าแต่องค์พระผู้เป็นเจ้า** | compound |
| DEU 9:26 | אֲדֹנָי יְהוִה | **ข้าแต่องค์พระผู้เป็นเจ้า** | compound |
| **JOS 7:7** | **אֲדֹנָי יְהוִה** (compound) | **ข้าแต่องค์พระผู้เป็นเจ้า** | compound — matches DEU/NUM precedent |
| **JOS 7:8** | **אֲדֹנָי** (standalone, same prayer) | **ข้าแต่องค์เจ้านาย** | standalone — DISTINCT from compound |

**The principled split JOS 7:8 introduces.** Within the same prayer-of-lament (Joshua at the Ai-defeat), 7:7 uses the compound Adonai-YHWH and 7:8 uses standalone Adonai. The Thai surface distinguishes:
- **Compound אֲדֹנָי יְהוִה** (prayer + Tetragrammaton) → **ข้าแต่องค์พระผู้เป็นเจ้า** (collapses to the standard YHWH-form)
- **Standalone אֲדֹนָי** (prayer-vocative without Tetragrammaton) → **ข้าแต่องค์เจ้านาย** (the YHWH-form is NOT used because the Hebrew explicitly does NOT use it)

This is the FIRST OT-pilot verse where the compound / standalone distinction is preserved in Thai.

**The existing doc-lock.** `divine_names_table_2026-05.md` locks:
- standalone אֲדֹנָי (non-prayer, title use) → **องค์เจ้านาย** / **องค์เจ้านายของบรรดาเจ้านาย** (DEU 10:17)
- single-yodh אֲדֹנִי (my-lord, human/angel address) → **เจ้านายของข้าพเจ้า** (JOS 5:14)

The doc does NOT currently cover Adonai-in-prayer cases. The NUM 14:17 audit + DEU 3:24/9:26 audit both flagged this gap as a REVIEW item.

**Recommended doc-amendment** — extend `divine_names_table_2026-05.md` with a 4-way principled distinction:

| Form | Hebrew | Thai | Locking precedents |
|---|---|---|---|
| Compound אֲדֹנָי יְהוִה (prayer) | אֲדֹנָי יְהוִה / אֲדֹנָי + YHWH | **ข้าแต่องค์พระผู้เป็นเจ้า** | NUM 14:17, DEU 3:24, DEU 9:26, JOS 7:7 |
| Standalone אֲדֹנָי (prayer-vocative) | אֲדֹנָי (alone, prayer-context) | **ข้าแต่องค์เจ้านาย** | JOS 7:8 (precedent) |
| Standalone אֲדֹנָי (title, non-prayer) | אֲדֹנֵי הָאֲדֹנִים etc. | **องค์เจ้านาย / องค์เจ้านายของบรรดาเจ้านาย** | DEU 10:17 |
| Single-yodh אֲדֹנִי (human/angel address) | אֲדֹנִי | **เจ้านายของข้าพเจ้า** | JOS 5:14 |

**Question:** Should `divine_names_table_2026-05.md` be amended with the 4-way principled Adonai distinction as named above, with JOS 7:8 as the explicit locking precedent for the standalone-Adonai-in-prayer-vocative form? The current outstanding REVIEW from NUM 14:17 + DEU 3:24/9:26 audits + this audit §14 compounds into a third-downstream-witness situation; the doc-lift unblocks the Adonai pattern across the Pentateuch + Former-Prophets corpus.
