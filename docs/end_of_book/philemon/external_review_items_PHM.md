## Item A — πρεσβύτης lexical default vs minority πρεσβευτής variant (PHM 1:9)

**The text in question.** PHM 1:9 in SBLGNT reads:

> διὰ τὴν ἀγάπην μᾶλλον παρακαλῶ, τοιοῦτος ὢν ὡς Παῦλος **πρεσβύτης** νυνὶ δὲ καὶ δέσμιος Χριστοῦ Ἰησοῦ

Paul calls himself "πρεσβύτης" — lexical default = "old man, aged person." Eremos renders **ผู้สูงอายุ** (ผู้ "person" + สูงอายุ "of high age"), preserving the lexical default.

**The variant.** A minority text-tradition + a few patristic citations have **πρεσβευτής** (one extra letter ευ) = "envoy, ambassador." Bentley conjectured πρεσβευτής in the 18th century; J.B. Lightfoot adopted it in his 1875 commentary. The case for πρεσβευτής is rhetorically attractive — Paul as Christ's *ambassador*-in-chains rhymes with 2 Cor 5:20 (πρεσβεύομεν) and Eph 6:20 (πρεσβεύω).

**The case for πρεσβύτης (the current rendering).** SBLGNT/NA28/UBS5/WH all print πρεσβύτης. The internal-grammatical case: Paul's self-description in v.9 reads as a TWO-FOLD physical-condition pairing — "an aged-man (πρεσβύτης) and now also a prisoner (δέσμιος)." Both descriptors name his present physical-condition. Reading πρεσβευτής (ambassador) breaks the parallelism — "an ambassador and now also a prisoner" mixes a role descriptor with a physical-condition descriptor. The role-vs-condition asymmetry is grammatically defensible but rhetorically less coherent.

**Mainstream English critical-text Bibles' choice.** ESV/NIV/NLT/CSB/BSB all print "aged" or equivalent. NRSV-1989 had "ambassador"; NRSV-updated (NRSVue, 2021) reverted to "old man." THSV (Thai Standard) and THKJV (Thai King James, Philip Pope) both have "ผู้สูงอายุ"-equivalent.

**The current Eremos disposition.** Silent-omission per RULES §5b — the variant has minority manuscript weight + the mainstream critical-text convention agrees with πρεσβύτης + Thai readers' existing Bibles (THSV, THKJV) also have "aged." The verse-level note in `output/translations/philemon_01.json` documents the variant for translators/scholars but the main `thai` field carries no bracket or footer note.

**Question:** Is silent-omission the right disposition here, or should Eremos add a brief verse-level footer note acknowledging the πρεσβευτής reading? The argument for a note: this is one of the more famous lexical variants in Paul, and the rhetorical attractiveness of "ambassador in chains" is sometimes preached on by Thai pastors who may notice the divergence. The argument against: surfacing every minority lexical reading would clutter the corpus; we're a critical-text translation (RULES §0), not an apparatus.

---

## Item B — Onesimus name-wordplay surfacing strategy (PHM 1:10-11, 1:20)

**The pattern.** Greek Ὀνήσιμος = "useful / profitable" (from ὀνίνημι "to derive benefit"). Paul plays on the name THREE TIMES in this short 25-verse letter:

| Verse | Greek | Thai (current) | Wordplay |
|---|---|---|---|
| 1:10 | παρακαλῶ σε περὶ τοῦ ἐμοῦ τέκνου, ὃν ἐγέννησα ἐν τοῖς δεσμοῖς **Ὀνήσιμον** | ข้าพเจ้าขอวิงวอนท่านในเรื่องลูกของข้าพเจ้า ผู้ที่ข้าพเจ้าได้ให้กำเนิดในระหว่างที่ถูกจองจำ — **โอเนซิมัส** | Greek puts the name at sentence-END for rhetorical reveal |
| 1:11 | τόν ποτέ σοι **ἄχρηστον** νυνὶ δὲ σοὶ καὶ ἐμοὶ **εὔχρηστον** | ผู้ซึ่งครั้งหนึ่งเคย**ไม่มีประโยชน์**แก่ท่าน แต่บัดนี้กลับ**มีประโยชน์**ทั้งแก่ท่านและแก่ข้าพเจ้า | ἄ-χρηστος / εὔ-χρηστος pun on "useless / useful" — etymologically tied to Ὀνήσιμος |
| 1:20 | ναί, ἀδελφέ, ἐγώ σου **ὀναίμην** ἐν κυρίῳ | ใช่แล้ว พี่น้องเอ๋ย ขอให้ข้าพเจ้า**ได้รับประโยชน์**จากท่านในองค์พระผู้เป็นเจ้า | ὀναίμην (NT-hapax optative of ὀνίνημι) — the verbal ROOT of Onesimus's name |

The Thai uses **ประโยชน์** ("benefit / usefulness") consistently across all three wordplays, preserving the semantic field. But Thai readers cannot see the etymological tie to the name "โอเนซิมัส" without external context — Greek-name etymology is invisible in Thai script.

**Current strategy: surface in `thai_summary` only.** The thai_summary at v.10:
> ในกรีก ชื่อ 'โอเนซิมัส' (Ὀνήσιμος) ปรากฏที่ส่วนท้ายสุดของประโยค — ทำให้เกิดผลของการ 'เปิดเผย' ที่น่าตื่นเต้น ...

The thai_summary at v.11:
> การเล่นสำนวน — 'โอเนซิมัส' (Ὀνήσιμος) ในภาษากรีกแปลว่า 'ผู้มีประโยชน์' เปาโลพูดเล่นกับชื่อของเขา ...

The thai_summary at v.20:
> การเล่นสำนวนอีกครั้งกับชื่อโอเนซิมัส — กริยา 'ὀναίμην' (ขอให้ได้รับประโยชน์) มาจากรากเดียวกับ 'โอเนซิมัส' (ผู้มีประโยชน์) ...

**Alternative strategy: add a v.10 verse-level footer note.** A brief note at the introduction of the name — something like *`ชื่อโอเนซิมัสในภาษากรีกหมายความว่า "ผู้มีประโยชน์" — เปาโลเล่นสำนวนกับความหมายนี้ในข้อ 11 และ 20`* — would make the wordplay visible to ALL readers, not just those who engage with the thai_summary.

**The corpus-wide pattern.** Other proper-noun etymologies in the Eremos corpus (e.g., Πέτρος "rock" at Matt 16:18, Ἰησοῦς "YHWH saves" at Matt 1:21) are surfaced via `thai_summary` and scholarly notes, NOT via verse-level footer notes. Adding a footer note for Onesimus would be an EXCEPTION to the corpus-wide convention.

**The case for an exception:** Onesimus is unusually pun-heavy for a single short letter (3 wordplays in 25 verses), and the pun is the rhetorical engine of the appeal — Paul is literally arguing "Onesimus has now become his name." Missing the pun is missing the letter's central irony. A 30-Thai-character footer note would be an inexpensive exception that materially improves comprehension.

**The case against:** Setting the precedent for proper-noun-etymology footnotes is non-trivial. If Onesimus gets one, why not Πέτρος, Ἰησοῦς, Βαρναβᾶς, Βαρ-Ἰωνᾶ, the entire Hebrew Acts-1-noun cluster, etc.? Better to keep the corpus convention uniform and treat thai_summary as the etymology-surfacing layer.

**Two questions:**
1. Is the current `thai_summary`-only strategy sufficient for surfacing the Onesimus wordplay, or does the rhetorical-engine status of this pun warrant a verse-level footer note exception?
2. If yes to a footer note, should the precedent extend to other Pauline name-wordplays (e.g., Onesiphorus in 2 Tim 1:16-18; ὀνίνημι is wordplayed there too)? Or kept as a one-off for Philemon?
