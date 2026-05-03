## Item A — ὁ υἱὸς τοῦ ἀνθρώπου: Christological-title vs generic-plural disambiguation

**The pattern.** Mark uses υἱὸς τοῦ ἀνθρώπου in two semantically distinct ways. The Eremos rendering preserves the Greek distinction via presence-vs-absence of the Thai genitive particle "ของ":

| Greek | Verses (Mark) | Thai | Sense |
|---|---|---|---|
| ὁ υἱὸς τοῦ ἀνθρώπου (singular, definite, Christological title) | 14×: 2:10, 2:28, 8:31, 8:38, 9:9, 9:12, 9:31, 10:33, 10:45, 13:26, 14:21 ×2, 14:41, 14:62 | **บุตรมนุษย์** (no ของ) | Dan 7:13 echo + Jesus's self-designation |
| τοῖς υἱοῖς τῶν ἀνθρώπων (plural, generic) | 1×: 3:28 | **บุตรของมนุษย์** (with ของ) | "the sons of men" = humanity |

The Thai distinction (presence vs. absence of ของ) is engineered to preserve a Greek title-vs-generic-plural difference that the Thai phonology / morphology would otherwise collapse. RULES.md ratifies the pattern; the corpus-doc `son_of_man_disambiguation_2026-04.md` extends it to Matthew/Luke/John (where Stephen's vision in Acts 7:56 also gets บุตรมนุษย์, and John's special-uses get the same).

**The risk.** Thai readers may not perceive the presence/absence of ของ as a semantic flag — both forms are grammatical Thai and ของ is often optional in genitive constructions. A reader could see บุตรมนุษย์ and บุตรของมนุษย์ and read them as stylistic alternations rather than a deliberate title-vs-generic distinction.

**Two questions:**
1. Is the presence/absence-of-ของ device strong enough as a Christological-title flag for Thai readers, or does the project need a complementary mechanism (e.g., consistent capitalization-equivalent, a thai_summary stanza on first occurrence, a glossary footnote)?
2. The disambiguation locks corpus-wide. Are there Pauline / Hebrews / Revelation passages where υἱὸς τοῦ ἀνθρώπου occurs in ways that don't fit cleanly into the title-vs-generic binary (e.g., Heb 2:6 quoting Ps 8:5 where the Psalm's υἱὸς ἀνθρώπου is generic but is then Christologically-applied in 2:9–10), and how should the device degrade in those cases?

---

## Item B — Mark 16:9–20: Tier 3 longer-ending treatment

**The textual situation.** Mark 16:9–20 is the most-discussed inclusion-variant in the NT. SBLGNT prints it bracketed; NA28/UBS5 mark it as later-addition. Codex Sinaiticus (א) and Vaticanus (B) both end at 16:8. The longer ending appears in A C D W and the bulk of later witnesses.

**Eremos disposition (Tier 3 per `inclusion_variants_absent_verses_2026-04.md`).**
- Verses 16:9–20 rendered in main text wrapped in **⟦double brackets⟧**
- Extended `notes` field at v.9 explains the textual situation, the manuscript witnesses (א/B vs A/C/D/W + Byzantine), and mainstream English-Bible practice (ESV/NIV/NRSV all bracket; KJV does not).
- Reader can simultaneously see: (a) the text exists in the tradition, (b) its inclusion is contested.

**Why Tier 3 (double brackets) and not silent-omission or footnote-only:**
- The block is too long (12 verses) for footnote-only treatment without losing readability
- Silent-omission would falsely imply Eremos editorially "removed" verses Thai pastors expect to find
- Single brackets `[...]` (Tier 1) are reserved for short-phrase variants where the bracket annotation reads cleanly; for a 12-verse narrative block, single brackets are visually overwhelmed

**Forward implication:** The same Tier 3 ⟦...⟧ treatment locks in for **John 7:53–8:11 (pericope adulterae)** when John ships. That's a 12-verse block with the same א/B-omit-but-tradition-includes profile.

**Two questions:**
1. Is the Tier 3 ⟦double-bracket⟧ device the right reader-visible signal for Mark 16:9–20 in the Thai context, or would a different convention (e.g., a section break with an explanatory header above v.9) communicate the textual situation more clearly to non-academic readers?
2. The ⟦...⟧ treatment locks in for John 7:53–8:11. Are there inclusion-variant blocks of intermediate length (3–8 verses) where neither single brackets nor double brackets are the right fit, and should the corpus pre-decide a Tier-2 convention (e.g., bracket-with-note) before such a passage forces an ad-hoc decision?

---

## Item C — Mark 1:1, 3:14, 9:29: Tier 1 short-phrase brackets

**The pattern.** Three short inclusion-variants in Mark, rendered in single Thai brackets `[...]`:

| Verse | Greek (variant content) | Thai bracket-content | Manuscript profile |
|---|---|---|---|
| 1:1 | υἱοῦ θεοῦ ("Son of God") | **[พระบุตรของพระเจ้า]** | Present in B D W + most witnesses; absent in א\* (original hand of Sinaiticus), Origen citations |
| 3:14 | οὓς καὶ ἀποστόλους ὠνόμασεν ("whom he also named apostles") | **[ซึ่งพระองค์ทรงเรียกว่าอัครทูตด้วย]** | Present in א B C\* + Alexandrian witnesses; absent in A C² D W + Byzantine |
| 9:29 | καὶ νηστείᾳ ("and fasting") | **[และการอดอาหาร]** | Absent in earliest witnesses (א\* B); added in most later manuscripts |

**Per-verse rationale lives in `key_decisions`; the policy lives in `inclusion_variants_absent_verses_2026-04.md`.** Single brackets signal "the mainstream tradition includes this; SBLGNT prints with apparatus marker; reader sees both the text and its contested status."

**The interpretive sensitivity.** Each of the three brackets sits at a doctrinally-loaded location:
- 1:1's υἱοῦ θεοῦ is a Christological-title declaration; bracketing it raises Christology-stakes for Thai readers who learn from THKJV/THSV that Mark begins "the gospel of Jesus Christ, the Son of God"
- 3:14's apostles-naming has ecclesiology stakes for Catholic-Protestant differences in Thailand
- 9:29's "and fasting" is the proof-text Thai charismatic + Pentecostal traditions cite for spiritual-discipline-against-demons; bracketing weakens that anchor

**Two questions:**
1. Is the single-bracket `[...]` device the right granularity for these three Mark variants, or do any of them warrant Tier 2 treatment (bracket + verse-level footer note explaining the textual situation rather than relying on `notes`-field opacity to non-scholar readers)?
2. The 9:29 bracket affects a popular pastoral reading. Are there other Tier-1 brackets in the corpus (or pending in Acts/epistles) where doctrinal/pastoral weight should escalate them to Tier 2, and what's the principled criterion for that escalation?

---

## Item D — εὐθύς / εὐθέως: Markan signature, context-sensitive rendering

**The pattern.** Mark uses εὐθύς / εὐθέως 42× — more than all other NT books combined. The word is not given a single locked Thai rendering; instead, three context-sensitive variants are deployed:

| Greek context | Thai | Frequency | Function |
|---|---|---|---|
| Strict-temporal (action immediately follows previous) | **ทันใดนั้น** | dominant | "right then, at that moment" |
| Light-temporal (immediate-but-discourse-marker) | **ในทันใด** | secondary | "immediately" |
| Prose-pacing (Mark's narrative-tempo connector, not strictly temporal) | **และก็** | minority | "and so / and then" — preserves Mark's relentless pace without falsely forcing "immediately" |

**The και-also problem.** Mark's εὐθύς often functions less as a temporal adverb and more as a *narrative-tempo* particle — the Markan signature breathlessness. A strict 1:1 lock to ทันใดนั้น would produce 42 "immediately"s in Thai prose that would read mechanically. The third variant (และก็) acknowledges that Mark's εὐθύς sometimes is closer to a discourse-pacing connective than to a strict temporal claim.

**Forward implications.**
- **Acts** uses παραχρῆμα more often than εὐθύς; the εὐθύς lock applies but with reduced frequency
- **Matthew/Luke** use εὐθύς ~5× and ~7× respectively (both reduced from Mark); the same context-sensitive triplet applies

**Two questions:**
1. Is the three-way context-sensitive split (ทันใดนั้น / ในทันใด / และก็) principled, or does the existence of the prose-pacing variant (และก็) introduce translator-discretion in a way that risks per-verse drift? Should the criterion for choosing between the three be more tightly documented (e.g., a flowchart in `markan_euthys_immediately_2026-04.md`)?
2. If a Thai reader reads Mark cover-to-cover, will the breathless-Markan-pace come through? Or does the contextual variation flatten the cumulative rhetorical effect that the Greek 42-occurrence εὐθύς creates?

---

## Item E — Aramaic transliterations: Mark's "transliterate-then-translate" rhetorical move

**The pattern.** Mark embeds 7 Aramaic phrases. Each is preserved as Thai-script transliteration AND Mark's own Greek-to-Thai translation, matching Mark's "transliterate then translate" original-language move:

| Verse | Greek | Thai transliteration | Thai translation (Mark's own gloss) |
|---|---|---|---|
| 3:17 | Βοανηργές | **โบอาเนอเกส** | บุตรแห่งฟ้าร้อง ("sons of thunder") |
| 5:41 | Ταλιθα κουμ | **ทาลิธา คูม** | "เด็กหญิงเอ๋ย เราสั่งเจ้าว่า ลุกขึ้นเถิด" |
| 7:11 | κορβᾶν | **คอร์บัน** | สิ่งที่ถวายแด่พระเจ้า ("an offering to God") |
| 7:34 | ἐφφαθά | **เอฟฟาธา** | "จงเปิดออกเถิด" |
| 14:36 | αββα | **อับบา** | พระบิดา ("Father") |
| 15:22 | Γολγοθᾶ | **กลโกธา** | สถานที่กะโหลกศีรษะ ("place of the skull") |
| 15:34 | Ελωΐ Ελωΐ λεμὰ σαβαχθανί | **เอโลอี เอโลอี เลมา ซาบัคทานี** | "พระเจ้าของข้าพระองค์ พระเจ้าของข้าพระองค์ ทำไมพระองค์ทรงทอดทิ้งข้าพระองค์?" |

The dual-form preserves Mark's rhetorical move: the Aramaic is kept (because Mark kept it), but Thai readers — who have no native intuition for Aramaic — receive the same gloss Mark provided his Greek readers.

**Forward implication.** The pattern locks for Matthew (extends with Ἐμμανουήλ at 1:23, Ῥακά at 5:22, Ἠλὶ ἠλὶ λεμὰ σαβαχθάνι at 27:46) and any Acts/epistolary occurrences (e.g., μαρὰν ἀθᾶ at 1 Cor 16:22).

**Two questions:**
1. Is the dual transliteration+gloss treatment the right Thai disposition, or would a single-form rendering (transliteration-only with thai_summary explanation) read more naturally to non-academic Thai readers?
2. The pattern applies cleanly when Mark provides his own gloss. For Aramaic embeds where the Greek author DOESN'T gloss (e.g., μαρὰν ἀθᾶ in 1 Cor 16:22, where Paul provides no Greek translation), should Eremos: (a) transliterate-only, (b) transliterate + add a gloss the Greek didn't have, or (c) transliterate + put the gloss in `thai_summary` rather than the main text?

---

## Item F — ἀμὴν λέγω ὑμῖν: the synoptic dominical-saying anchor

**The pattern.** Mark uses ἀμὴν λέγω ὑμῖν 13× (3:28; 8:12; 9:1, 41; 10:15, 29; 11:23; 12:43; 13:30; 14:9, 18, 25, 30). Uniform Thai rendering: **เราบอกความจริงแก่พวกท่าน(ว่า)**.

The phrase is Jesus's signature dominical-pronouncement formula — what Joachim Jeremias called *ipsissima vox*, the closest extant Greek to the Aramaic Jesus likely actually said. The Markan rendering anchors the synoptic lock: Matthew's three drift verses (5:18, 13:17, 5:26 — which had "เราบอกพวกท่านตามจริง") were corrected to this Markan form during Matthew's audit.

**The doctrinal weight.** ἀμὴν is the Aramaic-loanword Jesus retains untranslated in Greek, and Eremos translates it (เราบอกความจริง = "I tell the truth") rather than transliterating (อาเมน). The choice is principled — Mark's *own* rendering of the Aramaic is the Greek λέγω ὑμῖν construction, so translating to "I tell you the truth" matches Mark's own translational intent. But Thai readers familiar with the Greek Orthodox / Catholic / mainstream-Protestant rendering "Truly, truly I say" may notice the divergence from THKJV's "เราบอกความจริงแก่ท่านทั้งหลายว่า."

**Two questions:**
1. Is "เราบอกความจริงแก่พวกท่าน(ว่า)" the right synoptic-lock for ἀμὴν λέγω ὑμῖν, or should the Aramaic ἀμὴν be transliterated (e.g., "อาเมน เราบอกพวกท่าน") to preserve the foreign-marker that Mark himself preserves (he didn't translate ἀμὴν to ἀληθῶς)?
2. The Johannine "ἀμὴν ἀμὴν λέγω σοι/ὑμῖν" doubled formula (25× in John alone) needs to lock to a related but distinct rendering. Is "เราบอกความจริงๆ แก่ท่าน" (with double ๆ to mirror the Greek doubling) the right Johannine extension, or should John get its own non-parallel rendering?
