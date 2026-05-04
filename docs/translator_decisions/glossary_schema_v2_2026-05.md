# Glossary schema v2 — semantic domains + allowed renderings + context rules

**Scope:** The `glossary.json` schema needed to handle Hebrew lemmas whose semantic range is broader than English/Greek equivalents. Replaces the v1 single-Thai-rendering-per-lemma model.

**Decided:** 2026-05-04 (per plan §10 + ChatGPT P9).

---

## 1. The problem v1 doesn't solve

The NT-era `glossary.json` schema is a `lemma → Thai-rendering` dictionary. That worked for Greek because most NT terms have a relatively narrow Thai equivalent at the lemma level (`ἀγάπη → ความรัก`, `χάρις → พระคุณ`, `ἐκκλησία → คริสตจักร`).

Hebrew lexemes are **broader and more concrete**:

- **רוּחַ** (ruach) covers wind, breath, spirit, the Holy Spirit. Single-rendering is impossible.
- **נֶפֶשׁ** (nefesh) covers life, self, throat, person, desire. Single-rendering flattens.
- **לֵב / לֵבָב** (lev) covers heart, mind, will, inner-person.
- **חֶסֶד** (chesed) covers covenant loyalty, steadfast love, mercy, kindness.
- **צֶדֶק / צְדָקָה** (tsedeq/tsedaqah) covers righteousness, justice, right-order, vindication.
- **חַטָּאת** (chattat) covers sin AND sin-offering — the same lexeme!
- **שָׁלוֹם** (shalom) covers peace, well-being, wholeness, prosperity, completeness.

Forcing single-rendering on these creates false consistency that misrepresents the OT's actual usage.

---

## 2. The v2 schema

```json
{
  "lemma": "רוּחַ",
  "language": "hebrew",
  "strong": "H7307",
  "transliteration": "ruach",
  "english_glosses": ["wind", "breath", "spirit"],
  "semantic_domains": [
    "meteorological",
    "physiological",
    "anthropological",
    "theological"
  ],
  "allowed_renderings": [
    "ลม",
    "ลมหายใจ",
    "วิญญาณ",
    "พระวิญญาณ",
    "จิตวิญญาณ"
  ],
  "forbidden_renderings": [
    "จิตใจ"
  ],
  "context_rules": [
    {
      "when": "meteorological / atmospheric phenomenon",
      "prefer": "ลม",
      "examples": ["GEN 8:1", "EXO 14:21", "1KI 19:11"],
      "rationale": "Plain Thai 'wind' captures atmospheric movement; ราชาศัพท์ inappropriate"
    },
    {
      "when": "physiological breath of life (in humans/animals)",
      "prefer": "ลมหายใจ",
      "examples": ["GEN 7:22", "JOB 27:3", "ECC 3:19"],
      "rationale": "Distinguishes from theological-spirit usage; clear physiological reference"
    },
    {
      "when": "Spirit of God / Holy Spirit (רוּחַ יהוה / רוּחַ אֱלֹהִים / רוּחַ קֹדֶשׁ)",
      "prefer": "พระวิญญาณ / พระวิญญาณขององค์พระผู้เป็นเจ้า / พระวิญญาณบริสุทธิ์",
      "examples": ["GEN 1:2", "JDG 3:10", "PSA 51:11", "JOL 3:1"],
      "rationale": "Locks divine-Spirit to ราชาศัพท์ พระวิญญาณ; matches NT corpus rendering of πνεῦμα"
    },
    {
      "when": "human inner spirit / disposition / mood",
      "prefer": "วิญญาณ / จิตวิญญาณ",
      "examples": ["GEN 41:8", "EXO 6:9", "1SA 1:15", "PSA 51:10"],
      "rationale": "Inner-life dimension; matches Thai rendering for human-side spirit"
    },
    {
      "when": "evil/unclean spirit (רוּחַ רָעָה / רוּחַ שֶׁקֶר)",
      "prefer": "วิญญาณชั่ว / วิญญาณโสโครก / วิญญาณแห่งการมุสา",
      "examples": ["1SA 16:14", "1KI 22:21-23"],
      "rationale": "Adversary-register; not capitalized; not ราชาศัพท์"
    }
  ],
  "cross_language_links": [
    {
      "language": "greek",
      "lemma": "πνεῦμα",
      "strong": "G4151",
      "note": "Same multi-rendering pattern; cross-corpus alignment matters for NT-cited OT verses"
    }
  ],
  "first_occurrence": "GEN 1:2",
  "frequency": 389
}
```

### 2.1 Field descriptions

- **`lemma`** — the dictionary form of the Hebrew/Aramaic word.
- **`language`** — `"hebrew"` or `"aramaic"`. NT entries use `"greek"`.
- **`strong`** — the Strong's number identifier (PD; from MACULA Hebrew inline).
- **`transliteration`** — SBL-style transliteration for translator/reader convenience.
- **`english_glosses`** — short list of dominant English glosses (for translator orientation; not authoritative).
- **`semantic_domains`** — controlled-vocabulary list of the lemma's semantic domains. Drawn from a fixed set (see §3).
- **`allowed_renderings`** — the closed set of acceptable Thai renderings. Translator may not render this lemma as anything outside this set without first updating the glossary.
- **`forbidden_renderings`** — Thai renderings to actively avoid (often because they introduce false-consistency or wrong-domain associations).
- **`context_rules`** — array of rules with `when` (semantic-domain or contextual trigger), `prefer` (the recommended rendering), `examples` (verse references illustrating the rule), `rationale` (why).
- **`cross_language_links`** — pointers to Greek/Aramaic equivalents that interact at NT-OT-quotation boundaries. Used by `check_nt_quotation_alignment.py`.
- **`first_occurrence`** — first verse where the lemma appears (for navigation).
- **`frequency`** — count of occurrences in the canon (informational; updated at end-of-OT corpus audit).

---

## 3. The fixed semantic-domain vocabulary

Drawn from Louw-Nida (NT) + SDBH (OT) + project-specific additions. The full list lives in `data/semantic_domains.json` and is referenced from glossary entries.

Top-level domains (~40 total):
- **physical-natural:** meteorological, geological, biological, astronomical, hydrological
- **physiological:** body-part, sensation, breathing, eating, reproduction, death
- **psychological-anthropological:** emotion, will, intellect, conscience, identity, social-role
- **social-relational:** family, kinship, marriage, friendship, enmity, community
- **political-legal:** kingship, judgment, covenant, law, authority, treaty
- **economic:** property, commerce, agriculture, taxation, debt
- **military:** warfare, weapons, fortification, battle, victory, defeat
- **religious-cultic:** sacrifice, priesthood, festival, sanctity, ritual, defilement, purification
- **theological:** divine-nature, divine-action, divine-attribute, salvation, judgment, covenant-relationship
- **moral-ethical:** righteousness, sin, holiness, repentance, evil, goodness
- **temporal:** time, season, age, lifespan, memorial
- **spatial:** location, motion, direction, distance, dwelling
- **linguistic-rhetorical:** speech, name, blessing, curse, oath, vow, song
- **wisdom:** knowledge, folly, instruction, fear-of-the-Lord, discipline
- **prophetic:** vision, oracle, sign-act, dream, calling, judgment-warning, salvation-promise

Each glossary entry tags 1-4 domains. The `context_rules` map domain to preferred rendering.

---

## 4. The 150-lemma seed list (pre-Genesis 1)

Per plan §10: pre-seed ~150 high-frequency Hebrew lemmas with full semantic-domain entries before Gen 1 starts. These cover the lemmas that will recur most frequently and most polysemously.

### Seed-list categories

**Divine-nature lexemes (15):** יהוה, אֱלֹהִים, אֲדֹנָי, אֵל, שַׁדַּי, רוּחַ, קָדוֹשׁ, אֱמֶת, חֶסֶד, רַחֲמִים, חֵן, צֶדֶק, צְדָקָה, מִשְׁפָּט, יְשׁוּעָה

**Human-side anthropological (12):** נֶפֶשׁ, לֵב/לֵבָב, רוּחַ (human side), בָּשָׂר, אִישׁ, אִשָּׁה, אָדָם, גֶּבֶר, יַד, פֶּה, עַיִן, אֹזֶן

**Covenantal-theological (12):** בְּרִית, תּוֹרָה, מִצְוָה, חֻקָּה, עֵדוּת, דְּבַר־יהוה, אָמַן (verb), שָׁמַע, יָדַע, אָהַב, יָרֵא, בָּטַח

**Cultic vocabulary (15):** מִקְדָּשׁ, מִשְׁכָּן, אֹהֶל מוֹעֵד, אֲרֹן, מִזְבֵּחַ, קֹרְבָּן, זֶבַח, עֹלָה, חַטָּאת (sin/sin-offering!), אָשָׁם, מִנְחָה, פֶּסַח, יוֹם הַכִּפֻּרִים, שַׁבָּת, חֵרֶם

**Sin / repentance / forgiveness (10):** חֵטְא, פֶּשַׁע, עָוֹן, רֶשַׁע, שׁוּב, נָחַם, סָלַח, כָּפַר, רָחַץ, טָהַר

**Wisdom / instruction (8):** חָכְמָה, בִּינָה, דַּעַת, מוּסָר, יִרְאַת־יהוה, אֱוִילִי / כְּסִיל, צַדִּיק, רָשָׁע

**Salvation / deliverance (8):** יָשַׁע (verb), פָּדָה, גָּאַל, מָלַט, נָצַל, סָתַר, מָגֵן, מַעֲרֶת

**Worship / liturgy (8):** הָלַל, יָדָה, זָמַר, שִׁיר, נָשַׁק (raised hands), בָּרַךְ, פָּלַל (pray), הִתְפַּלֵּל

**Prophetic (10):** נָבִיא, נְאֻם, מַשָּׂא, חָזוֹן, חֲלוֹם, רָאָה (seer), שָׁלַח (send), צוּר (bind), עָבַד (serve), אוֹת (sign)

**Polity / kingship (10):** מֶלֶךְ, מְלוּכָה, כִּסֵּא, כֶּתֶר, יוֹעֵץ, שַׂר, מִשְׁפַּחַת, שֵׁבֶט, עַם (people), גּוֹי (nation)

**Spatial / temporal (10):** עוֹלָם, יוֹם, לַיְלָה, חֹדֶשׁ, שָׁנָה, אֶרֶץ, שָׁמַיִם, יָם, מִדְבָּר, הַר

**Connectives / particles (5):** כִּי (causal/affirmative), אִם (if), הִנֵּה (behold), אַךְ (only/surely), פֶּן (lest)

**Body-language verbs (10):** הָלַךְ, רָאָה, שָׁמַע, אָכַל, שָׁתָה, יָשַׁב, עָמַד, נָפַל, קוּם, בּוֹא

**Action verbs (10):** עָשָׂה, נָתַן, לָקַח, אָמַר, דִּבֶּר, קָרָא, שָׁלַח, שׁוּב, יָצָא, בּוֹא

**Negative-experiences (7):** רָעָה, צָרָה, אֲסוֹן, עָנִי, מָוֶת, יָגוֹן, אֵבֶל

≈ 150 entries.

---

## 5. Migration plan

### 5.1 Build pre-Gen 1 (Day 6-9 per plan §20)

1. Generate the seed list above as `glossary_seed_ot.json` (~150 entries).
2. For each entry: research the semantic domains, populate `allowed_renderings` from THSV11/TNCV reference + Eremos NT corpus precedent, write 2-4 `context_rules`, add cross-language links to NT corpus terms.
3. Merge into `glossary.json` alongside existing NT entries.
4. `build_glossary.py` extended to accept the polymorphic `language` field (per plan §9.4).

### 5.2 Incremental growth during translation

- Each chapter's translation may surface 5-15 new lemmas needing glossary entries.
- `next_chapter.py` (plan §18 step 3) surfaces uncovered-lemma list per chapter.
- Translator adds new entries in `glossary.json` during chapter-translation work.
- End-of-book audits verify glossary coverage matches actual chapter content.

### 5.3 End-of-book audit

`check_glossary_coverage.py` (extension of NT-side check):
- Reads the chapter's lemma list from morphology.
- Verifies every lemma appears in `glossary.json`.
- Verifies every Thai rendering used falls within `allowed_renderings` for that lemma.
- Flags any rendering that contradicts a `context_rules` `forbidden_renderings`.

---

## 6. The cross-corpus problem (NT-OT alignment)

Most Hebrew lemmas have direct Greek equivalents in the NT-corpus glossary that translate to the same Thai. The Tetragrammaton specifically aligns by design (per the 2026-05-04 third-revision lock): OT `יהוה → องค์พระผู้เป็นเจ้า` matches NT `κύριος → องค์พระผู้เป็นเจ้า`, with per-verse `key_decisions` capturing the underlying Hebrew form for transparency.

The `cross_language_links` field tracks these:

```json
{
  "lemma": "יהוה",
  "cross_language_links": [
    {
      "language": "greek",
      "lemma": "κύριος",
      "thai_in_other_corpus": "องค์พระผู้เป็นเจ้า",
      "alignment": "intentional_divergence",
      "rationale_doc": "divine_names_table_2026-05.md"
    }
  ]
}
```

`check_nt_quotation_alignment.py` reads these `cross_language_links` to know which divergences are documented (auto-pass) vs. unexpected (require translator decision).

---

## When to revisit

- **At pilot end** — review the seed-150 entries for any that turned out wrong; correct.
- **At each phase boundary** — review new-since-last-phase additions for consistency with existing entries.
- **At end-of-OT corpus audit** — confirm every Hebrew lemma in any shipped OT chapter has a glossary entry; gap-fill remaining.
- **If a Hebrew lemma's allowed_renderings turns out too narrow** — expand and document the addition in `key_decisions` for the verse that triggered the expansion.
