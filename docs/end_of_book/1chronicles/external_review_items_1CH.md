## Item A — mal'akh-YHWH lock held in the ch-21 threshing-floor narrative, but entirely outside machine enforcement

**The pattern:** A locked corpus doc (`docs/translator_decisions/malak_yhwh_2026-05.md`, finalized 2026-05-13 via tri-AI review) requires every divine מַלְאָךְ to render as **`ทูตสวรรค์`** ("heaven-messenger"), with the genitive qualifier carried by `ของ` + the established divine-name form — so מַלְאַךְ יְהוָה → **`ทูตสวรรค์ขององค์พระผู้เป็นเจ้า`**. 1 Kings 19:7 was the corpus's one drift against this lock (bare `ทูต`, fixed at the 1 Kings audit); 2 Kings then shipped it cleanly under machine enforcement. 1 Chronicles 21 (the threshing-floor census-plague, **parallel to 2 Sam 24**) is the next major divine-מַלְאַךְ narrative.

**All seven divine מַלְאָךְ references in 1 Chronicles 21 comply:**

| Ref | Hebrew | Thai (shipped) | Status |
|---|---|---|---|
| **21:12** | מַלְאַךְ יְהוָה מַשְׁחִית | `ทูตสวรรค์ขององค์พระผู้เป็นเจ้าทำลาย…` | ✓ |
| **21:15** | מַלְאָךְ + הַמַּלְאָךְ הַמַּשְׁחִית + מַלְאַךְ יְהוָה | `ทูตสวรรค์องค์หนึ่ง` + `ทูตสวรรค์ผู้ทำลาย` + `ทูตสวรรค์ขององค์พระผู้เป็นเจ้า` | ✓ |
| **21:16** | מַלְאַךְ יְהוָה עֹמֵד בֵּין הָאָרֶץ וּבֵין הַשָּׁמַיִם | `ทูตสวรรค์ขององค์พระผู้เป็นเจ้ายืนอยู่ระหว่างฟ้าสวรรค์กับแผ่นดินโลก` | ✓ |
| **21:18** | מַלְאַךְ יְהוָה אָמַר אֶל־גָּד | `ทูตสวรรค์ขององค์พระผู้เป็นเจ้าก็สั่งกาด` | ✓ |
| **21:30** | חֶרֶב מַלְאַךְ יְהוָה | `ดาบของทูตสวรรค์ขององค์พระผู้เป็นเจ้า` | ✓ |

**Sample verses:**
- **21:16 HEB:** `וַיַּרְא אֶת־מַלְאַךְ יְהוָה עֹמֵד בֵּין הָאָרֶץ וּבֵין הַשָּׁמַיִם וְחַרְבּוֹ שְׁלוּפָה` → **TH:** "ก็เห็น**ทูตสวรรค์ขององค์พระผู้เป็นเจ้า**ยืนอยู่ระหว่างฟ้าสวรรค์กับแผ่นดินโลก ถือดาบที่ชักออกอยู่ในมือ"
- The two bare-`ทูต` surfaces in the chapter (21:15 "ขณะที่**ทูต**กำลังทำลายอยู่"; 21:27 "และ**ทูต**ก็เก็บดาบกลับเข้าฝัก") are Thai discourse back-references to an angel already named `ทูตสวรรค์` in the same verse — subject continuations, not fresh renderings of the divine compound.

**Editorial context:** the chapter shipped the lock correctly **by convention only**. Two enforcement facts: (1) the `malak` lock in `check_phrase_consistency.py` is scoped `"books": ["1KI ", "2KI "]` — 1 Chronicles was never machine-checked; the clean phrase-consistency result reflects out-of-scope, not a passed check. (2) `malak_yhwh_2026-05.md` §3's forward-cover checklist names "**2 Sam 24 (David)**" — the *parallel* to 1 Chr 21 — but it is still unchecked (deferred to the cross-book retrofit); 1 Chronicles 21 itself is not listed. So 1 Chr 21 ships the divine מַלְאַךְ correctly while its 2 Sam 24 twin still awaits the retrofit.

**Forward-compounds to:** 2 Chronicles (Solomon + the Judahite monarchy); the deferred cross-book retrofit (Gen 16/21/22/31, Num 22, Judg 6/13, **2 Sam 24** — the 1 Chr 21 twin); Zech 1–6; Malachi.

**Question:** Should the project (a) widen the `check_phrase_consistency.py` `malak` lock's permanent scope to include 1 Chronicles (and 2 Chronicles, before it ships), and (b) tick 1 Chr 21 onto the `malak_yhwh_2026-05.md` §3 forward-cover checklist — recording that 1 Chr 21 is the clean standard the still-deferred 2 Sam 24 retrofit should be matched against? Is there any reading under which leaving 1 Chronicles out of machine scope is preferable (e.g., to avoid false positives on the genealogy chapters), or is widening the scope the right lock-in for a held win?

---

## Item B — Samuel↔Chronicles synoptic divergence: documentation completeness on number divergences

**The pattern:** `synoptic_parallel_passages_2026-05.md` locks that parallel passages are translated **independently** from each book's own MT (not harmonized), and asks for a **Layer-1 verse note** when a divergence is famous, apologetically prominent, or gives "a substantially different **name**, **number**, or **agent**." 1 Chronicles is the first OT book to test this at scale (1 Chr 10–29 ≈ 1 Sam 31 + 2 Sam 5–24). The **agent and name** divergences are well-documented:

- **21:1** — שָׂטָן incited David (`ซาตาน`) ↔ 2 Sam 24:1 "YHWH incited" — `notes` reconcile the two; the doc itself cites this verse as its worked Thai example.
- **20:5** — Elhanan killed **Lahmi the brother of Goliath** (`ลามีน้องชายของโกลิอัท`) ↔ 2 Sam 21:19 "Goliath" — `key_decisions` document the crux (the doc's named considered-not-emended case).
- **21:15** Ornan=Araunah; **19:16** Shophach=Shobach; **11:11** Jashobeam=Josheb-basshebeth — all `notes`.
- **19:18** — 7,000 charioteers ↔ 2 Sam 10:18 "700 chariots" — `notes` ("ฉบับเอเรโมสแปลตามรูป MT ของพงศาวดาร").

**The gap — three unflagged number divergences:**

| Ref | 1CH MT (shipped) | 2 Sam parallel | Documented? |
|---|---|---|---|
| **21:5** | 1,100,000 + 470,000 (`หนึ่งล้านหนึ่งแสน` + `สี่แสนเจ็ดหมื่น`) | 2 Sam 24:9 — 800,000 + 500,000 | ❌ no note |
| **21:25** | 600 shekels of **gold** (`ทองคำหกร้อยเชเขล`) | 2 Sam 24:24 — 50 shekels of **silver** | ❌ (note covers temple-site theology only) |
| **11:11** | killed **300** (`สังหารคนสามร้อยคน`) | 2 Sam 23:8 — 800 | ⚠ name noted, number not |

**Editorial context:** the synoptic doc **explicitly names "2 Sam 24:9 census totals"** as a confuse-readers case warranting a note — and 21:5 is precisely the Chronicles side of that, unflagged. The translations are MT-faithful and correct; this is a Layer-1 documentation-completeness gap, not a surface error. The 21:25 price divergence (600 gold vs 50 silver) and the 11:11 troop count (300 vs 800) are both the "substantially different number" the doc's criteria target.

**Forward-compounds to:** 2 Chronicles (a far denser synoptic field, ≈ 1–2 Kings), where a documentation convention set now will scale; and the reviewer-facing apologetics packet (these number divergences are the ones Thai readers familiar with Samuel will notice).

**Question:** Should the project add Layer-1 divergence `notes`/`key_decisions` at **21:5** (census totals), **21:25** (600 gold vs 50 silver), and a number-clause at **11:11** (300 vs 800), per `synoptic_parallel_passages_2026-05.md`'s documentation format? And more broadly: for the high volume of minor number/spelling divergences coming in 2 Chronicles, what is the right documentation **threshold** — every divergence, or only those that are famous / apologetically prominent / large enough to confuse a reader who knows the Samuel–Kings parallel (the doc's current wording)?

---

## Item C — mal'akh human-messenger surface: a fifth cross-book variant

**The pattern:** `malak_yhwh_2026-05.md` §4.4 places **human**-messenger מַלְאָךְ outside the divine lock (free register). Across the OT corpus the human-messenger surface has drifted book-by-book:

| Book | Surface(s) for human-messenger מַלְאָךְ |
|---|---|
| 1 Samuel | `ผู้ส่งสาร` / `ผู้ส่งข่าว` |
| 1 Kings | `ผู้สื่อสาร` |
| 2 Kings | `ผู้ส่งสาร` / `ทูต` / `คณะทูต` |
| **1 Chronicles** | **`ทูต`** (14:1 Hiram of Tyre; 19:2 David's envoys to Hanun) + **`ส่งคน`** (19:16, paraphrase) |

**Sample verses:**
- **14:1 HEB:** `וַיִּשְׁלַח חוּרָם מֶלֶךְ־צֹר מַלְאָכִים אֶל־דָּוִיד` → **TH:** "ฮีรามกษัตริย์แห่งไทระทรงส่ง**ทูต**มาหาดาวิด"
- **19:2 HEB:** `וַיִּשְׁלַח דָּוִיד מַלְאָכִים לְנַחֲמוֹ` → **TH:** "ดาวิดจึงทรงส่ง**ทูต**ไปแสดงความเสียใจ"
- **19:16 HEB:** `וַיִּשְׁלְחוּ מַלְאָכִים` → **TH:** "พวกเขาก็**ส่งคน**ไปนำชาวอารัม…" (smoothing paraphrase)

**Editorial context:** 1 Chronicles' `ทูต` matches 2 Kings 17:4; the 19:16 `ส่งคน` is a defensible smoothing where the messengers are not the verse's focus. This is the standing cross-book normalization the 1 Kings §3b and 2 Kings §3b audits already flagged — 1 Chronicles is the fifth surface-set, not a new problem.

**Question:** Should the project lock a single corpus surface for human-messenger מַלְאָךְ (the audits to date recommend `ผู้ส่งสาร`, the widest footprint) and normalize the back-catalogue (1SA/1KI/2KI/1CH) in the same cross-book pass — or is per-book contextual variation (`ทูต` for a foreign king's formal envoy, `ผู้ส่งสาร` for a domestic courier) actually the more natural Thai, in which case the "drift" is really appropriate register-fitting and should be documented as licensed rather than normalized away?

---

## Item D — 1 Chr 28:12 בָּרוּחַ: MT-anchor ("by the spirit") vs BSB-gloss ("in mind")

**The pattern:** the Eremos OT is **MT-anchored** (`ot_canon_and_text_base_2026-05.md`) but rendered in **BSB style** (optimal-equivalence). At 1 Chr 28:12 these two commitments pull apart. David hands Solomon the temple blueprint that came to him **בָּרוּחַ** — literally "by the spirit [that was with him]," widely read as a marker of divine revelation (the parallel to Moses receiving the tabernacle pattern, Exod 25:9, 40, which the 28:19 note cross-references).

- **28:12 HEB:** `וְתַבְנִית כֹּל אֲשֶׁר הָיָה **בָרוּחַ** עִמּוֹ…`
- **28:12 TH (shipped, follows BSB):** "แบบแปลนนั้นบรรจุ**ทุกสิ่งที่ดาวิดทรงดำริไว้** คือลานของพระนิเวศ…"
- **28:12 `notes` (flags it):** *"ฉบับ BSB แปล 'ทุกสิ่งที่ดาวิดทรงดำริไว้' แต่ภาษาฮีบรูใช้คำว่า 'โดยพระวิญญาณที่อยู่กับเขา' (בָּרוּחַ) — บ่งบอกว่าแบบแปลนพระวิหารเป็นการเปิดเผยจากพระเจ้า ไม่ใช่เพียงความคิดของมนุษย์."*

**Editorial context:** this is a genuine interpretive crux (רוּחַ = "mind/intention" vs "[divine] Spirit"); BSB and most modern translations take "in mind," so the choice is mainstream and is documented. But it is the one place in 1 Chronicles where the Thai prefers the BSB English gloss over a more literal MT rendering — and if בָּרוּחַ is the divine Spirit, the surface effaces a Spirit-of-God datapoint (the rest of the book keeps the `พระ` honorific on the empowering Spirit, e.g. 12:18 `พระวิญญาณ`).

**Question:** Is the BSB "in mind" reading the intended call for 28:12 (in which case this is a confirm, since it is already noted) — or, given the MT-anchor policy and the strong "divine revelation" reading the verse-note itself endorses, should the surface preserve the בָּרוּחַ ambiguity (e.g., "…ตามที่ดาวิดได้รับโดยพระวิญญาณ" / "ทุกสิ่งที่อยู่ในใจของดาวิด โดยพระวิญญาณ")? More generally: when MT-literal and BSB-gloss diverge on an interpretive crux, which commitment is the tie-breaker for the surface text, and which goes to the Layer-2 note?

---

## Item E — "until this day" leitwort: 1 Chronicles joins the majority; 1 Samuel is now the lone outlier

**The pattern:** עַד הַיּוֹם הַזֶּה ("until this day") has two competing Thai surfaces across the corpus. 1 Chronicles ships it uniformly **`จนถึงทุกวันนี้`** (with the `ทุก-` intensifier) at both its occurrences — **4:41** and **17:5**.

**Cross-book corpus picture (five DtrH/Chronicler books):**
| Book | Surface | Count |
|---|---|---|
| Judges | `จนถึงทุกวันนี้` | 6× (+1 drift) |
| **1 Samuel** | **`จนถึงวันนี้`** (bare) | **8× uniform** |
| 1 Kings | `จนถึงทุกวันนี้` | 5× |
| 2 Kings | `จนถึงทุกวันนี้` | 10× |
| **1 Chronicles** | **`จนถึงทุกวันนี้`** | **2×** |

**Editorial context:** four of five books now agree on `จนถึงทุกวันนี้`; only 1 Samuel uses the bare `จนถึงวันนี้`. `leitwort_handling_policy_2026-05.md` still does not lock a Thai surface for this leitwort. This is the standing 1 Kings §14 / 2 Kings §11 cross-book REVIEW, now with a fourth concurring book.

**Question:** Should `leitwort_handling_policy_2026-05.md` lock **`จนถึงทุกวันนี้`** as the canonical corpus surface (the 4-of-5 majority, and the form 1 Chronicles independently uses) and normalize 1 Samuel's 8 bare-`จนถึงวันนี้` occurrences to match — or is the `ทุก-` intensifier a meaningful nuance (`ทุกวันนี้` "these very days / right up to now" vs `วันนี้` "this day") that could legitimately vary by context, leaving 1 Samuel's form defensible?
