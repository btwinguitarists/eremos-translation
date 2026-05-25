# Adversary speech-introduction register — formalized rule

**Status:** 🔒 LOCKED — applies retroactively to all gospel + Acts narrative.

**Decided:** 2026-05-01 during Luke end-of-book external AI review. ChatGPT + Gemini both flagged Luke 4 as a RULES §3 violation. Corrected.

---

## Rule

When narrating the speech of demons, the devil, false prophets, sorcerers, or any adversary addressing Jesus (or believers), Thai narration uses **neutral speech-verbs** — never the royal-deferential `ทูล` register reserved for honorific-speech-toward-the-divine.

| Adversary speech | Use | Don't use |
|---|---|---|
| devil → Jesus | `กล่าวกับพระองค์` / `พูดกับพระองค์` | ❌ `ทูลพระองค์` |
| demons → Jesus | `ร้อง` / `ร้องเสียงดัง` / `กล่าว` | ❌ `ทูล` |
| sorcerer → apostle | `กล่าวกับ` / `พูดกับ` | ❌ `เรียน` (deferential) |

**Rationale:** RULES §3 explicitly states "Demons or adversaries use neutral/distancing register, never honorifics." The honorific `ทูล` carries socially-reverent overtones inappropriate to adversary-speech. The fact that the addressee is divine does not transform the speaker's stance — Pauline polemic and Lukan narrative deliberately preserve the social-distance between hostile speakers and Jesus/God/believers.

The narrator's own voice (separate from quoted speech) continues to use Christ-honorifics for direct-objects (`พระองค์`, `พระเยซู`) — what changes is the SPEECH-VERB itself.

---

## Corpus baseline

- **Matthew 4:3, 4:6, 4:9** — uses `กล่าว` (correct, baseline)
- **Mark 1:24, 5:7** — demon-speech uses `ร้อง` / `กล่าว` (correct)
- **Luke 4:3, 4:6, 4:9** — REVISED 2026-05-01 from `ทูล` → `กล่าวกับพระองค์`
- **Luke 4:33-34, 4:41, 8:28** — demon-speech uses `ร้อง` / `กล่าว` (already correct)
- **Acts** — pre-emptive forward enforcement: Acts 5:3 (Peter to Ananias is not adversary-speech-to-Jesus, normal), Acts 8:9-24 (Simon Magus), Acts 13:6-12 (Elymas), Acts 16:16 (Python-spirit), Acts 19:13-16 (sons of Sceva)
- **Revelation** — apocalyptic-adversaries (the dragon, the beasts, the false prophet) — apply same neutral-register rule

---

## Edge cases

**Q: What about the demoniac at Mark 5:7 / Luke 8:28 calling Jesus 'υἱὲ τοῦ θεοῦ τοῦ ὑψίστου'?**
A: The DEMON-content includes a genuine Christological-recognition. The Thai narration still uses `ร้องเสียงดังว่า` (neutral). Inside the quote, address-form choices (`พระเยซูบุตรของพระเจ้า`) preserve the Christological-truth without socially-elevating-the-demon's-speech-stance.

**Q: What about Job's Satan (LXX), or the OT הַשָּׂטָן when reached?**
A: Same rule. Adversary speech-verbs neutral; Christological-content preserved as-content.

**Q: What about the pious-but-mistaken adversaries (e.g., Pharisees challenging Jesus, Acts 23:6 Sanhedrin)?**
A: Pharisees and human-religious-opponents are NOT in the adversary-class for this rule. They're disputants but human, not demonic-adversaries-of-Christ. They typically use neutral speech-verbs anyway (`ถาม`, `ถามว่า`, `ตอบว่า`); the rule above targets specifically demonic/satanic-adversaries.

---

## OT extension — human imperial blasphemers (added 2026-05-25, 2 Kings EOB Item B; verdict FINE / lock-as-is)

The Rabshakeh / Sennacherib confrontation (2 Kings 18–19) extends the rule to the OT's **human imperial-blasphemer** class. ChatGPT + Gemini both reviewed 2 Kings's handling as FINE ("threads the needle"); it is locked. **Three register layers interact and must be kept distinct:**

1. **The blasphemer / envoy's speech-act → neutral speech-verbs.** The Rabshakeh (Assyria's field-commander) taunting Jerusalem and YHWH uses plain `กล่าว` / `พูด` / `ร้อง` — never honorific `ทูล` / `เรียน`. He is not in a reverent posture, so his stance is not elevated. Same principle as demon/devil-speech.
2. **The actual foreign monarch → foreign-royal register, as a head of state.** Sennacherib king of Assyria (the "great king", הַמֶּלֶךְ הַגָּדוֹל) keeps the foreign-emperor register (`ทรง` for his sovereign-political actions) per `ot_register_policy_2026-05.md` §2.2 — he is a real monarch, even while his message is blasphemous. **Register tracks office, not piety.**
3. **YHWH as referent inside the hostile quotation → divine honorifics preserved.** When the blasphemy itself *names or quotes* YHWH (e.g. 18:35 `องค์พระผู้เป็นเจ้าจะทรงช่วยกู้` — "…will the LORD deliver Jerusalem from my hand?"), the divine referent keeps `ทรง` / `องค์พระผู้เป็นเจ้า`. This is **not** deference to the blasphemer — it preserves the divine referent's own grammar/register **as content**, exactly as Mark 5:7's demon-content keeps `บุตรของพระเจ้า` without elevating the demon's speech-verb (see Edge cases above).

**Forward protection:** Isaiah 36–37 (the direct parallel), Jeremiah (Babylon / Nebuchadnezzar oracles + imperial taunts), Daniel (Nebuchadnezzar's and Belshazzar's boasts, ch. 3–5) — apply the same three-way split: blasphemer's verb neutral; emperor-as-head-of-state keeps royal register; YHWH-as-quoted-referent keeps divine honorifics.

---

## Cross-reference

- `RULES.md` §3 (royal register) — the source of this rule.
- `docs/end_of_book/luke/ai_review_response_LUK_2026-05-01.md` — the trigger.
- `docs/translator_decisions/honorifics_non_divine_authorities_2026-04.md` — adjacent-rule for human-authority register.
