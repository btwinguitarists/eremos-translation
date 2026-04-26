# Praise verbs with divine object → สรรเสริญ (default collapse)

**Scope:** Greek verbs and verb-phrases of praise/worship when **God** (or the risen Christ) is the **grammatical object** of the praise-act. Four distinct lexemes collapse to a single Thai default for naturalness; per-verse rationale specifies which Greek lexeme generated the Thai choice.

**Decided:** 2026-04-23 during Claude external-review pass. Documents a principled collapse that was already operative verse-by-verse across the shipped Luke corpus; this doc lifts it to corpus-level visibility before Acts (which has heavy doxological vocabulary).

**Evidence base (Luke, representative verses):**
- **δοξάζω (object = God):** LUK 2:20, 5:25, 5:26, 7:16, 13:13, 17:15, 18:43, 23:47 → **สรรเสริญ** (8 verses, uniform)
- **εὐλογέω (object = God):** LUK 1:64, 2:28, 24:53 → **สรรเสริญ** (3 verses, uniform)
- **αἰνέω / αἶνον δίδωμι:** LUK 2:13, 2:20, 18:43, 19:37, 24:53 → **สรรเสริญ** (5 verses, uniform)
- **μεγαλύνω (magnify):** LUK 1:46 (Magnificat) → **เทิดทูน**; 1:58 (neighbors on Elizabeth's mercy) → **ยกย่อง / สรรเสริญ** (context-sensitive, see §Exceptions)

---

## The rule

**When God is the grammatical object, the following Greek praise-verbs default to Thai สรรเสริญ:**

| Greek | Lexical sense | Thai default |
|---|---|---|
| δοξάζω + τὸν θεόν | "glorify" — ascribe-weight-to | **สรรเสริญพระเจ้า** |
| εὐλογέω + τὸν θεόν | "bless" — acknowledge-as-blessed-source | **สรรเสริญพระเจ้า** |
| αἰνέω + τὸν θεόν (and αἶνον δίδωμι) | "praise" — speak-commendation-of | **สรรเสริญพระเจ้า** |
| ὑψόω + τὸν θεόν | "exalt" — lift-up-high (rare w/ God-obj) | **ยกย่อง / เทิดทูน** context-specific |

When these verbs appear consecutively (e.g., LUK 18:43 δοξάζω + αἶνον δίδωμι; LUK 24:53 εὐλογέω paralleling 24:52 προσκυνέω; LUK 2:20 δοξάζω + αἰνέω), the second occurrence may be rephrased (ร่วมกันสรรเสริญ / สรรเสริญต่อเนื่อง) to avoid Thai repetition-fatigue, but the base verb stays สรรเสริญ.

### When this does NOT apply

- **Humans as object of these verbs** — different Thai register:
  - δοξάζω (humans glorifying Jesus, LUK 4:15) → **ยกย่อง / สรรเสริญ** per context (the fame-spreading sense fits ยกย่อง better).
  - εὐλογέω (humans blessing humans, LUK 6:28 pray for enemies) → **อวยพร** (traditional "bless").
  - εὐλογέω (Jesus blessing disciples / bread / children, LUK 9:16, 24:30, 24:50) → **อวยพร** (ceremonial blessing from a superior to a non-divine recipient).
- **Object is person/item/event, not God.** Use lexeme-specific Thai verb; don't default to สรรเสริญ.

## Why the collapse (rather than distinguishing)

**Argument for the collapse (chosen):**
- **Thai naturalness.** The three primary Greek praise-verbs (δοξάζω / εὐλογέω / αἰνέω) do not have neat 1:1 Thai counterparts when God is the recipient. Thai Christian tradition (THSV, NTV, other major Thai translations) defaults to สรรเสริญ for all three in God-object contexts. Following convention aids reader comprehension.
- **เอกลักษณ์ของการนมัสการแบบไทย.** Thai doxological language around God is functionally centered on สรรเสริญ (praise), ถวาย (offer), นมัสการ (worship), and ยกย่อง (exalt). The fine-grained Greek distinctions don't map to distinct Thai lexemes natively; forcing a 1:1 map produces stilted Thai.
- **Per-verse rationale already specifies the Greek source.** When a reader or scholar needs to know which Greek lexeme underlies a given "สรรเสริญ," the verse-level `key_decisions` entry carries the Greek + Thai + rationale — so the lexical granularity is preserved for scholarship without cluttering the main-text Thai.

**Argument against (considered and rejected): maintain 1:1 lexical distinction.**
- Would force awkward Thai: δοξάζω → "ให้เกียรติ" (give honor — too administrative); εὐλογέω → "กล่าวคำอวยพร" (speak blessing-words — doesn't fit God-as-recipient in Thai); αἰνέω → "กล่าวคำสรรเสริญ" (speak praise-words — stilted).
- Would break with Thai Christian liturgical/hymnic convention.
- Per Paul's inclusive praise clauses (Eph 1:3 εὐλογητός / εὐλογέω + Eph 1:6/12/14 εἰς ἔπαινον δόξης αὐτοῦ), multiple lexemes appear in tight succession — forcing distinct Thai verbs there would overwhelm the Thai reader.

## Key exceptions and edge cases

### 1. μεγαλύνω ("magnify") — per-verse choice

- LUK 1:46 (Mary's Magnificat: μεγαλύνει ἡ ψυχή μου τὸν κύριον) → **เทิดทูน** (lift-up-in-honor) — elevated register fits hymnic register; per-verse rationale documents the choice.
- LUK 1:58 (neighbors rejoicing at Elizabeth's mercy: ἐμεγάλυνεν κύριος τὸ ἔλεος αὐτοῦ) → **ได้ทรงกระทำ... ยิ่งใหญ่** or **ทรงสำแดงความเมตตา** (God magnifying his own mercy — different construction).
- Acts 5:13, 10:46, 19:17 (people magnifying God/the Name): default to **สรรเสริญ** unless the hymnic-emphatic register demands เทิดทูน.

### 2. ὑψόω ("exalt") — per-verse

- When God is subject exalting Christ (Acts 2:33, 5:31 — τῇ δεξιᾷ τοῦ θεοῦ ὑψωθείς): **ยกขึ้นสูง** / **เชิดชู** with ราชาศัพท์.
- When God/Christ is object (rare in gospels; Jas 4:10 "humble yourselves before the Lord and he will exalt you"): the "exalt" is God's action toward the humble; not in this doc's scope.

### 3. προσκυνέω ("worship / prostrate")

NOT included in this doc's collapse — προσκυνέω is specifically bodily-prostration worship, distinct semantically from verbal-praise. Thai default: **นมัสการ** (worship) for divine object; **คุกเข่าลงกราบ** (kneel-and-bow) for specific posture emphasis. See separate glossary entry.

### 4. ἐπαινέω ("praise") — rare w/ God-obj in NT

Almost always human-object in the NT (Rom 15:11 LXX citation "praise the Lord all nations" — here God-obj, hymnic). When God-obj, defaults to **สรรเสริญ** per this rule.

### 5. ὁμολογέω / ἐξομολογέω ("confess / acknowledge")

NOT praise proper — distinct semantic field (confession of faith or sin). Separate glossary entries; not in this doc.

## Forward implications

### Acts (~25 praise-verb occurrences with God as object)

- **Acts 2:47** (αἰνοῦντες τὸν θεόν): **สรรเสริญพระเจ้า**
- **Acts 3:8–9** (ἁλλόμενος καὶ αἰνῶν τὸν θεόν... εἶδεν... αὐτὸν... αἰνοῦντα τὸν θεόν): **สรรเสริญพระเจ้า** (twice, with per-verse rephrasing for variation)
- **Acts 4:21, 11:18, 21:20** (ἐδόξαζον τὸν θεόν, narrator-doxological corporate-acclamation contexts): **ถวายเกียรติแด่พระเจ้า** — see "δοξάζω narrator sub-rule" below
- **Acts 10:46, 19:17** (μεγαλυνόντων τὸν θεόν): **สรรเสริญ** or **เทิดทูน** per register-context
- **Acts 13:48** (ἐδόξαζον τὸν λόγον τοῦ κυρίου — object is "the word," not "God"): **เทิดทูน** (extends the doxological register to the divine λόγος; per-verse decision, not corpus-default)
- **Acts 28:15** (εὐχαρίστησεν τῷ θεῷ — thanksgiving, not praise per se): **ขอบพระคุณพระเจ้า** (thanks) — see εὐχαριστέω glossary entry; not this doc.

### δοξάζω narrator sub-rule (added 2026-04-26)

**Sub-rule:** When δοξάζω appears in narrator voice as a corporate-acclamation-after-salvific-event ("they glorified God"), default to **ถวายเกียรติแด่พระเจ้า** rather than สรรเสริญพระเจ้า. The ถวาย-verb register more closely tracks the Greek δοξάζω's "ascribe-glory-to" sense in formal-public contexts.

**Conditions:** narrator voice + corporate subject (πάντες / οἱ ἀκούσαντες / ὁ ὄχλος) + post-event acclamation contour. Verse-by-verse confirmation of conditions:
- **Acts 4:21** — Sanhedrin can't punish apostles because πάντες ἐδόξαζον τὸν θεόν (corporate-public)
- **Acts 11:18** — Jerusalem-believers ἡσύχασαν καὶ ἐδόξασαν τὸν θεὸν (corporate-formal-deliberation)
- **Acts 21:20** — James + elders οἱ ἀκούσαντες ἐδόξαζον τὸν θεόν (corporate-formal-report-reception)

**When NOT to apply (default to สรรเสริญ):**
- Single-subject δοξάζω (individual praise: Luke 5:25, 7:16, 17:15, 18:43, 23:47 — all individual healed people praising God in narrative; one-on-one acclamation register).
- Imperatival or hortatory δοξάζω in direct speech (e.g., 1 Pet 4:16 ἐν τῷ ὀνόματι τούτῳ δοξαζέτω τὸν θεόν → สรรเสริญ + imperative).
- δοξάζω with non-God object (Acts 13:48 ἐδόξαζον τὸν λόγον — see "Forward implications" above for the doxological-register extension).

**Decided 2026-04-26** during Acts external AI review (Gemini + ChatGPT both verdict FINE on the existing pattern; recommended documenting it as a sub-rule rather than normalizing to flat สรรเสริญ default).

### Pauline corpus

- **Rom 15:6–11** (doxological cluster, δοξάζητε τὸν θεόν + ἔπαινος + ἐξομολογήσομαί σοι + ὑμνήσω + Αἰνεῖτε + ἐπαινεσάτωσαν — five praise-verbs in six verses, multiple LXX citations): apply this doc's default **สรรเสริญ** for most; use **ถวายพระเกียรติ** for the opening "glorify God together" if the doxological register needs amplification.
- **Phil 2:11** (εἰς δόξαν θεοῦ πατρός — noun-construction): not this doc.
- **1 Tim 1:17, 6:15–16** (doxology): traditional hymnic language; default **สรรเสริญ** + ถวายพระเกียรติ for glory-ascription.

### Hebrews

- **Heb 13:15** (ἀναφέρωμεν θυσίαν αἰνέσεως): sacrificial-praise construction — **ถวายเครื่องบูชาแห่งการสรรเสริญ**. The αἰνέσεως genitive → สรรเสริญ.

### Revelation

- Heavy doxology in 4:8–11, 5:9–14, 7:10–12, 11:15–18, 15:3–4, 19:1–8. Apply this doc's default **สรรเสริญ**; enhance with ถวายพระเกียรติ, นมัสการ, ถวายคำสรรเสริญ for hymnic register.

## Alternatives considered

- **สรรเสริญ universal default (chosen).**
- **1:1 lexical distinction (distinct Thai verb for each Greek praise-verb).** Rejected for naturalness.
- **Full collapse to ถวายพระเกียรติ ("give glory").** Rejected — ถวายพระเกียรติ is appropriate for doxological-formal contexts but over-heavy for everyday praise-reports (e.g., people healed praising God spontaneously in healing narratives).

## When to revisit

- If a doctrinal-review flagging finds the collapse obscures a theological distinction (e.g., εὐλογέω-as-covenantal-blessing vs. αἰνέω-as-liturgical-praise) that matters in a specific passage, document the exception at the verse-level.
- Revelation's doxological hymns (ch. 4-5, 19) may warrant a refinement — the hymnic register often uses multiple praise-verbs in parallel for rhetorical effect; a consistent Thai collapse may need per-passage variation.

## Cross-reference

- `docs/LUK_END_OF_BOOK_REVIEW_2026-04-22.md` §17 — Claude external-review flag.
- `glossary.json` — δοξάζω, εὐλογέω, αἰνέω entries should document the collapse.
- `RULES.md` §4 — key-term consistency.
