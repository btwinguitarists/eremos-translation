# Psalms — External Review Items

Source: `docs/end_of_book/psalms/PSA_END_OF_BOOK_REVIEW_2026-05-31.md` (§2 audit). These are the REVIEW / DECIDE items where independent eyes (Greek/Hebrew + Thai) add value beyond Claude's own corpus-level self-review. Each block carries verse evidence inline; the closing **Question** becomes a YAML reviewer question.

## Item A — Exod 34:6 compassion-formula (`חַנּוּן וְרַחוּם`) lexeme consistency

The "gracious and compassionate, slow to anger, abounding in steadfast love" formula recurs across the Psalter (echoing Exod 34:6). `check_phrase_consistency.py` flags an inconsistency in how `רַחוּם` ("compassionate") is rendered:

- **Ps 103:8** `רַחוּם וְחַנּוּן יְהוָה` → "องค์พระผู้เป็นเจ้าทรงเปี่ยมด้วย**พระเมตตา**และพระคุณ ทรงกริ้วช้า…"
- **Ps 86:15** `אֵל־רַחוּם וְחַנּוּן` → "พระเจ้าผู้เปี่ยมด้วย**พระเมตตา**และพระคุณ…"
- **Ps 111:4** `חַנּוּן וְרַחוּם יְהוָה` → "ทรงเปี่ยมด้วยพระคุณและ**พระเมตตา**"
- **Ps 145:8** `חַנּוּן וְרַחוּם יְהוָה` → "ทรงเปี่ยมด้วยพระคุณและ**ความเมตตากรุณา**"  ← the outlier

`רַחוּם` = พระเมตตา in three places but **ความเมตตากรุณา** at 145:8 (chosen to avoid the honorific `พระกรุณา`/`พระกร` body-part trap, but `พระเมตตา` is itself trap-free and already the established form). The audit recommends normalizing 145:8 to `พระเมตตา`.

Two notes: (1) the **word order** legitimately varies with the MT (compassion-first `רַחוּם וְחַנּוּן` at 86:15/103:8 vs. grace-first `חַנּוּן וְרַחוּם` at 111:4/145:8) — should the Thai preserve Hebrew order, or fix one canonical order for the formula? (2) Ps 112:4 applies the same pair to the *righteous man* (plain ความเมตตา, no royal พระ-) — correct to keep distinct.

**Question:** Should `רַחוּם` be rendered uniformly as พระเมตตา across all divine occurrences of the Exod 34:6 formula (normalizing Ps 145:8 from ความเมตตากรุณา), and should the Thai preserve the Hebrew word-order variation or standardize the formula's order?

## Item B — Imprecatory-psalm footnote frame

The Psalter's imprecatory passages (137:8–9 "dashes your infants against the rocks"; 139:19–22 "do I not hate those who hate You"; 140:9–11 "burning coals"; 149:6–9 "a double-edged sword in their hands… vengeance on the nations") are rendered **faithfully and unsoftened** from the MT, each with a Tier-2 pastoral footnote using a consistent four-part frame:

> (1) faithful unsoftened rendering; (2) vengeance entrusted to God, not self-executed (Deut 32:35 / Rom 12:19); (3) lex talionis / God's righteous judgment; (4) NT trajectory — Christ's call to love enemies (Matt 5:44) + the spiritual-warfare / eschatological-judgment reading (Eph 6:17, Heb 4:12, Rev 19:15).

Example (Ps 137:9 footnote, abridged): *"…ฉบับเอเรโมสแปลตามต้นฉบับภาษาฮีบรูอย่างซื่อตรง ไม่ตัดทอน… ผู้ประพันธ์มอบการแก้แค้นไว้กับพระเจ้า ไม่ลงมือเอง… ในพระคริสต์ ผู้เชื่อได้รับการทรงเรียกให้รักศัตรู (มธ 5:44)…"*

**Question:** Is the four-part pastoral-footnote frame the right corpus-level approach for the imprecatory psalms (faithful text + theological/NT framing in the footnote), and is the Thai framing pastorally and theologically sound for a Thai Buddhist-background readership?

## Item C — Ps 145:13 missing-נun verse (MT vs. 11QPsaᵃ/LXX/Syriac)

Ps 145 is an alphabetic acrostic, but the MT **omits the נun verse** (jumps מ at v13 → ס at v14). 11QPsaᵃ (Dead Sea Scrolls Hebrew), the LXX, and the Syriac all carry it, and most modern translations supply it. The Eremos rendering keeps the **MT as base** (v13 = the מ-line only) and places the נun line in a Tier-2 footnote, quoting it:

> נֶאֱמָן יְהוָה בְּכָל־דְּבָרָיו וְחָסִיד בְּכָל־מַעֲשָׂיו → "องค์พระผู้เป็นเจ้าทรงสัตย์ซื่อในพระวจนะทั้งสิ้นของพระองค์ และทรงเปี่ยมด้วยความรักในพระราชกิจทั้งปวงของพระองค์"

`bsb_english` for v13 was truncated to the מ-line to match the MT-based Thai (the supplied line lives only in the footnote).

**Question:** For an acrostic whose structure *requires* the נun line and where Hebrew manuscript evidence (11QPsaᵃ) supplies it, is MT-base-with-footnote the right call, or should the נun line be promoted into the verse text (as a v13b) with the footnote explaining the MT omission?

## Item D — `הַלְלוּ־יָהּ` → ฮาเลลูยาห์ (transliterate vs. translate)

The frozen liturgical frame `הַלְלוּ־יָהּ` opening/closing the Hallel psalms (104, 105, 106, 111–113, 115–117, 135, 146–150) is **transliterated** to ฮาเลลูยาห์ (like เซลาห์), while mid-clause `הַלְלוּ יָהּ` ("praise YAH", e.g. 135:3) is **translated** as จงสรรเสริญองค์พระผู้เป็นเจ้า.

**Question:** Is transliterating the framing `הַלְלוּ־יָהּ` as ฮาเลลูยาห์ (a form Thai Christians may recognize liturgically) the right choice, versus translating it as จงสรรเสริญองค์พระผู้เป็นเจ้า throughout for a readership without that liturgical background?
