# οὐρανός — ฟ้าสวรรค์ / สวรรค์ / ท้องฟ้า rendering

**Scope:** The Greek noun οὐρανός ("heaven / sky"), singular and plural. Common across the gospels, dense in Acts (Ascension + Pentecost + visions), and theologically loaded in Paul (ἐν τοῖς οὐρανοίς / ἐπουράνιος word-family) and Revelation.

**Decided:** 2026-04-23 during Claude external-review pass. Flagged for book-wide pattern drift (Luke uses three Thai renderings without a locked principle). This doc establishes the working principle going forward; retrospective normalization of shipped Luke is deliberately minimal (one spot-revision at 10:20 for parallelism; rest of shipped corpus left as-is with the documented-drift acknowledged).

**Evidence base (Luke, all 29 οὐρανός occurrences audited 2026-04-23):**

| Thai | Count | Representative verses |
|---|---|---|
| ฟ้าสวรรค์ | 15 | 3:21, 3:22, 9:16, 9:54, 10:15, 10:18, 10:21, 11:16, 15:18, 15:21, 21:11, 21:26, 21:33, 22:43 |
| สวรรค์ (only) | 7 | 2:15, 10:20 *(normalized 2026-04-23)*, 11:13, 12:33, 18:22, 20:4, 20:5, 24:51 |
| ท้องฟ้า | 2 | 4:25, 12:56 (sky-as-meteorological-object) |
| (other / rephrased) | 5 | 8:5, 9:58, 13:19, 16:17, 17:24, 17:29 — figurative / "birds of the air" / "heaven and earth pass" phrases rendered idiomatically per verse |

---

## The rule (going forward)

### Default: **สวรรค์**

Use **สวรรค์** as the default rendering of οὐρανός when:
- The context is locative ("in heaven," "from heaven," "to heaven") — εν, εκ, εἰς + οὐρανός.
- The context is theological-abode ("heavens opened," "Father in heaven," "treasure in heaven," "names in heaven," "ascended to heaven").
- The referent is the destination/origin of divine action in general.

### Emphatic: **ฟ้าสวรรค์**

Use **ฟ้าสวรรค์** when the context specifically emphasizes the *cosmic-vertical* scope — the "heavens" as paired with "earth," the "powers of the heavens," "heavens-and-earth" pair, apocalyptic-cosmological imagery.

Examples:
- "heaven and earth pass away" — οὐρανὸς καὶ ἡ γῆ (LUK 21:33; MAT 24:35; Acts 4:24, 14:15, 17:24)
- "powers of the heavens shall be shaken" — αἱ δυνάμεις τῶν οὐρανῶν (LUK 21:26)
- "signs in the heavens" apocalyptic — σημεῖα ἐν οὐρανῷ (LUK 21:11)
- "Lord of heaven and earth" — κύριε τοῦ οὐρανοῦ καὶ τῆς γῆς (LUK 10:21)

### Sky-as-object: **ท้องฟ้า**

Use **ท้องฟ้า** when οὐρανός refers to the physical sky as a meteorological-natural-phenomenon subject: shut-heaven (drought), face-of-sky (weather signs), birds of the air if the "sky" dimension dominates.

Examples:
- "the heaven was shut" (Elijah drought) — ἐκλείσθη ὁ οὐρανός (LUK 4:25)
- "you know how to discern the face of the sky" — τὸ πρόσωπον τοῦ οὐρανοῦ (LUK 12:56)

### Idiomatic / figurative — per verse

- "birds of the air" — τὰ πετεινὰ τοῦ οὐρανοῦ: Thai uses **นกในอากาศ** or **นกในท้องฟ้า** — natural Thai phrase, no strict rule.
- "heaven" as euphemism for God (Prodigal Son "I have sinned against heaven" = "against God") — keep **ฟ้าสวรรค์** because it's already established at LUK 15:18, 15:21 and the emphatic register fits the confessional weight.

---

## The parallelism rule

**When two or more οὐρανός-clauses in the same discourse or parabolic-unit share construction, they must render identically.**

Example of the parallelism violation that prompted this doc:
- LUK 10:20: "rejoice that your names are written in heaven" ἐν τοῖς οὐρανοῖς → originally **ฟ้าสวรรค์** (before 2026-04-23)
- LUK 18:22: "you will have treasure in heaven" ἐν [τοῖς] οὐρανοῖς → **สวรรค์**
- Same construction, same theological weight. **Normalized:** LUK 10:20 → สวรรค์.

**Future parallelism watches:**
- MAT "treasures in heaven" 6:20 (already shipped) — verify on Matthew re-visit.
- Acts Pentecost sermon's "heaven" references must track uniformly.

---

## Retrospective treatment of Luke's shipped drift

The documented book-wide inconsistency is NOT being fully normalized retrospectively. This is a deliberate choice:

- **Cost of full retrospective revision:** 15+ verses touched; each needs key_decision rationale update; cascades into back-translation + check regeneration.
- **Benefit of documenting vs. revising:** the drift is minor and context-bound; Thai readers will not notice the alternation within the book the way they would notice e.g., a Κύριε-vocative misfire or an ἄφεσις drift in the gospel-content phrase.
- **What IS being fixed:** the parallelism-violation at 10:20/18:22 and the Acts-forward anchor at 24:51 (Ascension to heaven uses สวรรค์ — so Acts 1:10–11 must match).

**Revisit trigger:** when John ships (John has heavy οὐρανός: 1:32, 1:51, 3:13, 3:27, 3:31, 6:31–58 "bread from heaven," 12:28 "voice from heaven," 17:1 "lifted his eyes to heaven"). At that point, run the principle above across MAT + MRK + LUK + ACT and normalize systematically.

---

## Forward implications

### Acts (~70 οὐρανός occurrences)

- **Acts 1:10–11** (Ascension — 4 οὐρανός in 2 verses): **สวรรค์** uniformly to match LUK 24:51. **Lock before Acts 1 ships.**
- **Acts 2:2, 2:5** (Pentecost — sound "from heaven," devout men "from every nation under heaven"): locative default **สวรรค์**.
- **Acts 2:19, 2:34** (signs in heaven, Ps 110 citation "sit at my right hand"): 2:19 = apocalyptic cosmological → **ฟ้าสวรรค์**; 2:34 = locative-abode → **สวรรค์**.
- **Acts 7:49, 7:55–56** (Stephen's vision — "heaven is my throne" / "I see the heavens opened"): theological-abode → **สวรรค์** default. 7:49 is Isa 66:1 quotation — follow the Isaianic rendering convention.
- **Acts 10:11** (Peter's rooftop — "saw the heaven opened"): **สวรรค์** (vision context, not cosmic-pair).

### Pauline corpus
- **Eph 1:10, 1:20, 2:6, 3:10, 6:12** (ἐν τοῖς ἐπουρανίοις "in the heavenly places"): separate adjective ἐπουράνιος, not οὐρανός. Different lock required — tentatively **ในสวรรค์สถาน / ในแดนสวรรค์** per context.
- **Col 1:5, 1:16, 1:20** (οὐρανός plural, cosmic-theological): mixed — 1:5 "treasure-laid-up-in-heaven" → **สวรรค์**; 1:16, 1:20 "all things in heaven and on earth" → **ฟ้าสวรรค์** (cosmic-pair).

### Hebrews
- Heavy use of οὐρανός + cognates. Heb 4:14 "passed through the heavens"; Heb 9:23 "heavenly things"; Heb 11:12 "stars of heaven"; Heb 12:23 "firstborn registered in heaven" (parallels LUK 10:20).
- Most are theological-abode → สวรรค์; cosmic-pair → ฟ้าสวรรค์.

### Revelation
- Many heaven-earth pairs and heaven-as-location. Apply rule verse-by-verse; most apocalyptic imagery favors **ฟ้าสวรรค์** for cosmic scope.

---

## Alternatives considered

- **Default ฟ้าสวรรค์, emphatic สวรรค์.** Rejected — reverses the Acts-critical 24:51 Ascension (which uses สวรรค์ and Acts 1:10–11 must match).
- **Collapse all to สวรรค์** (Claude's Option C). Rejected for now — would force ~15 Luke retro-revisions for marginal gain; and loses the legitimate cosmic-emphatic register ฟ้าสวรรค์ provides at 21:26, 21:33, 10:21.
- **Transliterate (โออูรานอส).** Rejected — foreign.
- **Case-by-case per verse with no doc.** Rejected — this is exactly what produced the current drift.

## When to revisit

- **Immediately before Acts 1:10 ships.** Lock the Ascension rendering at Acts 1:10–11; cross-check 2:2, 2:5, 2:34 before Pentecost sermon.
- **When John ships.** Full systematic pass across MAT + MRK + LUK + ACT with this doc as the guideline.
- If a native-Thai reader flags the ฟ้าสวรรค์/สวรรค์ alternation as stylistic noise rather than semantic signal, revisit with specific verse complaints.

## Cross-reference

- `docs/LUK_END_OF_BOOK_REVIEW_2026-04-22.md` §17 — Claude external-review flag.
- `glossary.json` — οὐρανός entry should document both primary renderings after this doc.
- `RULES.md` §4 — key-term consistency (this doc is the corpus-level lock).
