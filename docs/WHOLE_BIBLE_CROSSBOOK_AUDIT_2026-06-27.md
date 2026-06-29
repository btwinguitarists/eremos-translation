# Whole-Bible Cross-Book Consistency Audit — Worklist

**Generated:** 2026-06-27
**Scope:** All 66 books (OT 39 + NT 27). The translation is complete (1,189 chapters);
every book has passed per-chapter checks, an end-of-book audit, and an external AI review.
This worklist is the **cross-book** layer the per-book pipeline can't see: consistency of a
decision *across* books, and the OT↔NT seams.

**Status:** ADJUDICATION-PENDING. Nothing here is decided. Each theme below ends with a
**DECIDE** line — Ben's call. The enforcement checks (§ "Checks to build") are written
*after* the decisions, because each check's notion of "correct" is a decision below.

> Decisions get recorded in the corpus decision docs (`docs/decisions/…`, e.g.
> `malak_yhwh_2026-05`), then enforced by a check, then applied to the translation, then
> shipped. Order matters: **decide → check → apply → ship.**

Method note: themes seeded from the 12 freshest reviews (EZK + Minor Prophets, fully
extracted) + the cross-book findings already on record + a keyword sweep of all 39 OT
review responses (book-implication counts below are from that sweep). A verse-level
extraction of the older 27 OT books' review items is the first adjudication-time task
(§ "Next").

---

## Theme 1 — Divine anthropomorphism (God's hand / arm / eye / face)

**The issue:** When God speaks in the first person about *his own* body ("my hand," "my
arm," "my eyes"), do we render plain (มือ / แขน) or royal (พระหัตถ์ / พระกร / พระเนตร / พระพักตร์)?
The reviews want a single codified rule; right now it's inconsistent.

- **Reviews flagging it:** EZK (Item A — asks for a *codified, scaled-up* first-person-plain
  rule), HOS (Item A — same rule + a "face" exception). Keyword sweep hits **8 OT books**:
  exodus, ruth, 2chronicles, isaiah, jeremiah, ezekiel, hosea, jonah.
- **Already on record:** anthropomorphism rendered plain (แขน/มือ) not royal in 1st-person
  speech, but **inconsistent across ISA + JER** (confirmed by the JER audit too).
- **Tension to resolve:** this collides with the honorifics check's "body-part-of-God +
  ทรง" hard-fail rule (`reference_honorifics_bodypart_trong`) — a plain body-part as the
  subject of a ทรง-verb trips the gate. The rule and the check must agree.
- **NT seam:** **John 12:38 พระหัตถ์ (royal) vs Isaiah 53:1 พระกร (royal but different word)** —
  the same "arm of the LORD" rendered two ways across the testaments.

**DECIDE:** (a) the first-person-plain rule and its exact exceptions (does "face"/พระพักตร์
stay royal?); (b) reconcile with the ทรง body-part check; (c) pick ONE rendering for "the
arm of the LORD" that holds in both Isaiah 53:1 and John 12:38.

---

## Theme 2 — Messenger / angel (מַלְאָךְ ‖ מַלְאַךְ יְהוָה)

**The issue:** מַלְאָךְ covers human *messenger*, *angel*, and the theophanic *Angel of the
LORD*. Thai ทูต (envoy) vs ทูตสวรรค์ (heaven-envoy = angel) carries the distinction — but the
corpus lock and the actual renderings don't line up.

- **Reviews flagging it:** MAL (Item A — a human priest [2:7] and forerunner [3:1a]
  rendered ทูตสวรรค์ "angel" is misleading; wants a human/divine split), ZEC (Item A —
  מַלְאַךְ יְהוָה rendered ทูตขององค์พระผู้เป็นเจ้า, *dropping* สวรรค์, blurring the theophany).
  Sweep hits **9 OT books**: exodus, numbers, joshua, 1kings, 2kings, 1–2chronicles,
  zechariah, malachi.
- **Already on record:** `malak_yhwh_2026-05` §4.3 is the governing decision doc; MAL Item A
  explicitly asks to amend it for human messengers and **ratify jointly with the open
  Zechariah angel-of-YHWH question.**
- **NT seam:** ἄγγελος in the NT inherits the same ทูต/ทูตสวรรค์ fork (e.g. John the Baptist as
  "messenger," Mal 3:1 quoted in Mark 1:2).

**DECIDE:** the three-way mapping — human messenger → ทูต/ผู้ส่งสาร; ordinary angel →
ทูตสวรรค์; Angel-of-the-LORD theophany → (keep สวรรค์? a distinct marker?) — then propagate to
the NT ἄγγελος citations.

---

## Theme 3 — Adonai-YHWH compound ("the Lord GOD", אֲדֹנָי יְהוִה)

**The issue:** how to render the compound divine name when both words appear, given the
per-verse divine-names check wants a contiguous องค์พระผู้เป็นเจ้า.

- **Reviews flagging it:** AMO (Item A), ZEP (Item A — called "the strongest witness for the
  open Amos question"). Sweep hits **16 OT books** (the prophets + Pentateuch/historical
  spots).
- **Already on record:** `reference_adonai_yhwh_contiguous` — compound-only verses should use
  **องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย** (not องค์เจ้านายพระผู้เป็นเจ้า, which breaks the check).
- **Status:** there's a recorded fix pattern but the reviews show it isn't applied uniformly.

**DECIDE:** confirm องค์พระผู้เป็นเจ้าผู้ทรงเป็นเจ้านาย as the standard for אֲדֹנָי יְהוִה, then sweep all
16 books to apply it consistently.

---

## Theme 4 — MT/LXX & Ketiv/Qere divergences (and reader footnotes) — **largest**

**The issue:** where our MT base diverges from the LXX or from a scribal tradition, the
divergence currently lives in *internal* notes only. Readers get no footnote — a problem
when the NT quotes the LXX form.

- **Reviews flagging it:** AMO (Item B — fallen booth of David, MT/LXX/Acts 15 fork), HOS
  (Item B — 6:6 חֶסֶד vs Matthew's ἔλεος; Item E — 4:7 tiqqun sopherim "their glory"/"My
  Glory"), JOL (Item B — Joel 3:1–5 MT → Acts 2 / Rom 10), EZK (Item D — temple-measurement
  MT/LXX), ZEC (Item D — 11:13 potter/treasury, 12:10 me/him). Sweep hits **25 OT books** —
  the broadest theme.
- **Already on record:** "MT/LXX divergences only in internal notes, need reader footnotes
  (esp **Jeremiah 31:32 vs Hebrews 8:9**)."

**DECIDE:** a reader-footnote policy — *which* class of divergence surfaces to readers
(NT-quoted ones at minimum?), in what form (chapter-footer note vs inline), and a pass to
add them. This is a policy + a content sweep, not a code fix.

---

## Theme 5 — OT↔NT crossover seams (the "could be crossover" worry) — **explicit**

**The issue:** terms and quotations that must agree across the testaments. The NT is already
shipped, so a mismatch means editing whichever side loses.

- **Sweep hits 17 OT books** referencing NT books/citations. Known concrete seams:
  - **"den of robbers": Matthew 21:13 ซ่องของพวกโจร vs Jeremiah 7:11 / Mark / Luke ถ้ำของโจร** —
    Jesus quotes Jeremiah; the Thai should match.
  - **"arm of the LORD": John 12:38 พระหัตถ์ vs Isaiah 53:1 พระกร** (also Theme 1).
  - **Hosea 6:6 → Matthew 9:13 / 12:7**, **Joel 2:28–32 → Acts 2:17–21 / Rom 10:13**,
    **Amos 9:11–12 → Acts 15:16–17**, **Jeremiah 31:31–34 → Hebrews 8:8–12** (also Theme 4).
- **Why it's its own theme:** these need a *bidirectional* check (does the OT source match
  the NT quotation's Thai?), which neither testament's per-book audit performed.

**DECIDE:** for each seam, which side is canonical (usually the OT quoted *as the NT renders
it*, or a deliberate note explaining the difference), then align.

---

## Theme 6 — Foreign-monarch register (royal honorifics for pagan kings)

**The issue:** do foreign kings (Pharaoh, Nebuchadnezzar, Cyrus, Ahasuerus) get ราชาศัพท์
royal register, and is it consistent?

- **Reviews flagging it:** EZK (Item B — every ruler rendered plain; proposes a Latter-
  Prophets vs Writings genre split). Sweep hits **12 OT books**: exodus, 2kings, ezra,
  nehemiah, esther, proverbs, songofsongs, isaiah, jeremiah, ezekiel, daniel, hosea.
- **Already on record:** "**Nebuchadnezzar plain in Jeremiah vs royal in Daniel**" — a direct
  contradiction between two books about the same king.

**DECIDE:** one rule for foreign-monarch register (plain everywhere? royal everywhere?
genre-split?), then reconcile Nebuchadnezzar across JER and DAN first.

---

## Theme 7 — Parallel-passage harmonization policy

**The issue:** when two books carry the same passage, do we render identically (harmonize)
or translate each independently? Right now it's done *both* ways.

- **Reviews flagging it:** MIC (Item A — Micah 4:1–3 ∥ Isaiah 2:2–4 was **harmonized**) vs
  OBA (Item B — Obadiah 1–9 ∥ Jeremiah 49:7–22 was kept **independent**). Same situation,
  opposite call. Sweep hits **9 OT books** (incl. the 2 Samuel ∥ 1 Chronicles synoptics).

**DECIDE:** a single harmonization policy (e.g. "render independently unless the later book
is explicitly quoting"), then apply to Micah∥Isaiah and Obadiah∥Jeremiah to match it.

---

## Theme 8 — Notes voice & untranslated-term systems (lower priority)

Smaller cross-book consistency items from the fresh reviews:
- **Messianic notes asserting "is the Christ" as fact** (EZK Item C) — a stronger claim than
  Isaiah/Jeremiah notes make. DECIDE: one voice for messianic notes across the prophets.
- **"son of man" (בֶּן־אָדָם)** (EZK Item E) — a three-way Thai system the policy doc doesn't
  yet sanction. DECIDE: ratify or simplify, watching the NT "Son of Man" (υἱὸς τοῦ ἀνθρώπου).
- **"Day of the LORD" leitwort** (JOL Item C) — rendering + lift into a corpus doc so it's
  uniform across the prophets.

---

## Checks to build (AFTER the decisions above)

The existing corpus checks are NT-first; the OT needs Hebrew-aware equivalents. Build these
to *enforce* the decisions, not to discover them:

1. **`check_hebrew_term_consistency.py`** — the Hebrew-lemma analogue of
   `check_key_term_consistency.py` (which keys on the Greek field and so can't see OT drift).
   Maps each Hebrew lemma → its Thai renderings across all 39 books; flags drift. Enforces
   Themes 1–3, 6, 8.
2. **`check_ot_textual_divergence.py`** — given the Theme-4 footnote policy, flag verses
   where an MT/LXX/Ketiv-Qere divergence is in internal notes but lacks the reader footnote
   the policy requires. (`audit_inclusion_variants.py` is SBLGNT/NT-only and won't do this.)
3. **`check_crossbook_citations.py`** — bidirectional: for every OT passage quoted in the NT
   (`check_ot_citations.py` already maps NT→OT), diff the OT source Thai vs the NT quotation
   Thai; flag mismatches. Enforces Theme 5.
4. **`consolidate_whole_bible_audit.py`** — extend `consolidate_ot_audit.py` to cover all 66
   books in one report once the above run clean (the final "v1.0 whole Bible" sign-off).

`polish_review.py` (Thai-flow micro-issues, Stage 2) is language-agnostic but labeled
NT-first — smoke-test it on one OT book before an `--all` run.

---

## Next (proposed order)

1. **Verse-level sweep of the older 27 OT books' review items** into this worklist (the 12
   fresh ones are done) — so every cross-book item is captured, not just keyword-matched.
2. **Ben adjudicates** Themes 1–7 (record each in `docs/decisions/`).
3. **Build checks 1–3**, run, surface residual mismatches.
4. **Apply** decided changes to the translation (each behind its own diff/review).
5. **`consolidate_whole_bible_audit.py`** clean → **ship the whole OT to the app** (bundle →
   17 missing books → manual prod import → verify) as one coordinated release.
