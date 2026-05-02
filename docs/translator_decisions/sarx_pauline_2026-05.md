# σάρξ — single-rendering + contextual-qualifier corpus discipline

**Decision date:** 2026-05-02 (formalized after COL end-of-book external AI review; long-deferred from GAL audit)
**Anchor book:** Colossians (the discipline pattern is cleanest here)
**Forward applicability:** Romans 7–8 (the densest σάρξ text in the corpus); Galatians 5; Ephesians 2:3, 2:11; 1 Cor 1:26, 5:5, 6:16; 2 Cor 7:1, 10:2-4
**Status:** LOCK. Critical to land before Romans 7–8 ships.

## The polyseme

Greek σάρξ in Pauline usage spans four sense-clusters that English translations often render distinctly (NIV: "flesh" / "body" / "sinful nature" / "earthly perspective") but Greek encodes with a single lemma:

| Sense | Description | Pauline examples |
|---|---|---|
| **Neutral physical body** | the physical body as a created reality | Col 1:22 (Christ's body), 1:24, 2:1, 2:5; 1 Cor 6:16 (one flesh in marriage) |
| **Earthly realm / human-relational sphere** | the social / human-cultural sphere as distinct from the spiritual | Col 2:11, 2:13, 3:22 (κατὰ σάρκα masters); 1 Cor 1:26 (κατὰ σάρκα wise) |
| **Moral / sinful disposition** | sin's operating territory in the unredeemed self | Rom 7:18, 7:25, 8:3-13; Gal 5:13-24; Eph 2:3 |
| **Christ's embodied flesh (royal)** | Christ's pre-resurrection bodily existence (royal register) | Col 1:22 (พระวรกายฝ่ายเนื้อหนัง); Eph 2:14-15; 1 Tim 3:16 |

## Project rule

**Single Thai base rendering: เนื้อหนัง (default) or กาย (when the body-as-physical sense is foregrounded).** Then layer contextual qualifiers + RULES §5 polysemy-flag annotations rather than using interpretive Thai lexemes that pre-decide the sense.

Specifically:

- **DO NOT** introduce interpretive moral-coding into the verse text (e.g., เนื้อหนังที่ตกในบาป "sinful flesh"). That reading lives in the surrounding context, the thai_summary, and the verse-level KD — not in the bare lemma rendering.
- **DO** mark RULES §5 polysemy flags in verse-level KDs at every σάρξ occurrence so the translator's sense-decision is auditable.
- **DO** use phrasal-context qualifiers when the Greek itself qualifies (κατὰ σάρκα, ἐν σαρκί, σὰρξ καὶ αἷμα, etc.).
- **DO** use the royal-register prefix **พระวรกาย** for Christ's bodily existence in the embodied-Christ sub-sense (COL 1:22 anchor — *พระวรกายฝ่ายเนื้อหนัง*).

## Why interpretive coding fails

If COL 2:11 (ἀπεκδύσει τοῦ σώματος τῆς σαρκός) gets the moral-σάρξ marker, the translator is committing to Romans 7-style anthropology in a verse that's actually about circumcision-of-the-heart language (the "old self" is taken off, paralleling 3:9). Pre-deciding it forecloses the contextual reading that the immediate verse supports. The thai_summary handles disambiguation; the lemma stays neutral.

If Rom 7:25 (τῇ σαρκὶ νόμῳ ἁμαρτίας) gets the moral-σάρξ marker, that's accurate — but if Rom 8:3 (ὁ θεὸς τὸν ἑαυτοῦ υἱὸν πέμψας ἐν ὁμοιώματι σαρκὸς ἁμαρτίας) gets the same marker, the Christological-incarnation sense gets distorted (Christ came in the LIKENESS of sinful flesh, not IN sinful flesh — the σάρξ here is closer to the physical-embodied sense, qualified). The Greek's flexibility lets Paul pun on σάρξ across these verses. Thai single-rendering preserves that flexibility.

The 1:22 royal-prefix sub-sense (πρῶνεκρωμένος ἐν τῷ σώματι τῆς σαρκὸς αὐτοῦ → ในพระวรกายฝ่ายเนื้อหนังของพระองค์) shows the principled extension: when the subject is Christ pre-resurrection, Thai layers ราชาศัพท์ on top of the standard เนื้อหนัง / กาย rendering rather than swapping to a different lexeme. Same lemma, royal register, semantic distinction preserved.

## Forward applicability — Romans 7–8

The four sense-clusters above all appear in Romans 7–8 within ~30 verses. The Thai handling must:

- **Rom 7:5** ἐν τῇ σαρκί (under the σάρξ-regime) → ฝ่ายเนื้อหนัง (the contextual κατά / ἐν patterns fold into Thai ฝ่าย-prefix where the rendering needs adverbial-modifier shape).
- **Rom 7:18** οὐκ οἰκεῖ ἐν ἐμοί, τοῦτ' ἔστιν ἐν τῇ σαρκί μου, ἀγαθόν → ในเนื้อหนังของข้าพเจ้า, with the moral-disposition reading in the surrounding context (KD names sense (3)).
- **Rom 7:25** τῇ σαρκὶ νόμῳ ἁμαρτίας → ในเนื้อหนัง, KD names sense (3).
- **Rom 8:3** ἐν ὁμοιώματι σαρκὸς ἁμαρτίας → ในลักษณะของเนื้อหนังที่บาป, with the Christological-incarnation sense in KD (Christ came in the LIKENESS — sense (1) physical-with-qualifier, not sense (3) moral).
- **Rom 8:4-13** repeating κατὰ σάρκα / ἐν σαρκί / τῆς σαρκός — each KD names which of senses (2) or (3) is operative without verse-text-marking.

The rule: **the verse renders, the KD disambiguates, the summary explains, and the discipline is auditable across the corpus.**

## Why this doc was overdue

Both Claude and ChatGPT independently flagged that the GAL audit recommended a sarx doc that was never written; COL shipped on undocumented precedent; the audit now repeats the recommendation. Doc-debt cleared in this PR. Critical that the rule lands BEFORE Romans 7–8 because that text's σάρξ density would force per-verse improvisation and potentially establish four different patterns in 30 verses.

## Cross-references

- Verse-level KDs: COL 1:22 (royal-Christ-body), 1:24, 2:1, 2:5, 2:11, 2:13, 3:22; GAL 5:13-24 cluster; Rom 7-8 cluster (forward).
- Companion doc: `spiritual_beings_hierarchy_2026-05.md` (the polemical-cosmology cluster σάρξ sits adjacent to in COL 2 but does not equate with).
- Audit: `docs/end_of_book/colossians/COL_END_OF_BOOK_REVIEW_2026-05-02.md` Item H.
- AI review: `docs/end_of_book/colossians/ai_review_response_COL_2026-05-02.md` Item H.
- RULES.md §5 — polysemy-flag convention is what this doc disciplines for σάρξ specifically.
