#!/usr/bin/env python3
"""
Phrase-level consistency audit.

Extends `check_key_term_consistency.py` to multi-word Greek phrases that carry
corpus-level theological weight. Where the single-lemma checker treats ἄφεσις
as one unit, this checker treats **ἄφεσις ἁμαρτιῶν** as one unit — catching
drift between e.g., MAT 26:28 and LUK 24:47 that the single-lemma checker
missed.

Scope: covers phrases locked by `docs/translator_decisions/*.md`. New phrases
are added as new locks are written.

Usage:
  python3 scripts/check_phrase_consistency.py              # audit all books
  python3 scripts/check_phrase_consistency.py --stdout     # print to stdout
  python3 scripts/check_phrase_consistency.py --json       # JSON output

Exit codes:
  0 — all locked phrases consistent
  1 — drift detected (verse-level violations printed + report written)
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"


# =============================================================================
# PHRASE LOCKS — each entry corresponds to a doc in docs/translator_decisions/
# =============================================================================
#
# Format:
#   ("docstring-tag", [greek_form_variants], "expected_thai_substring",
#    {verse_refs_excepted_from_lock_with_reason})
#
# The Greek variants cover case/accent/word-order variation. If ANY variant is
# present in the Greek text of a verse, the expected Thai substring should
# appear in the Thai rendering. Exceptions (e.g., contextual-meaning shifts
# like LUK 4:18's ἄφεσις="release") are listed with a reason so the check
# doesn't false-positive.
#
# Add a new entry when a new translator_decisions doc locks a corpus-level
# phrase.
# =============================================================================

PHRASE_LOCKS = [
    # ===== OT (Hebrew-keyed) locks — hebrew_patterns match niqqud-stripped Hebrew =====
    # malak_yhwh_2026-05.md — angel of the LORD (divine compound)
    {
        "doc": "malak_yhwh_2026-05.md",
        "label": "מַלְאַךְ יְהוָה / מַלְאַךְ הָאֱלֹהִים (angel of the LORD/God)",
        "hebrew_patterns": [r"מלאך\s*יהוה", r"מלאך\s*ה?אלהים"],
        # Kings + Chronicles. 1CH 21 (threshing-floor; the 2 Sam 24 parallel) audited
        # clean 2026-05-26. Patterns key on מלאך+divine-name, so genealogies and human
        # messengers (bare מלאך / מלאכים) never match — safe to widen without false
        # positives. Cross-book retrofit (Gen/Judg/Sam/Zech) remains the §3 backlog.
        "books": ["1KI ", "2KI ", "1CH ", "2CH "],
        "expected_thai_contains": "ทูตสวรรค์",
        "must_not_contain": [],
        "exceptions": {},
    },
    # dtr_history_cycle_formulas_2026-05.md — evaluation formula "did evil in the eyes of YHWH"
    {
        "doc": "dtr_history_cycle_formulas_2026-05.md",
        "label": "הָרַע בְּעֵינֵי יְהוָה (did evil in the eyes of YHWH)",
        "hebrew_patterns": [r"הרע\s+בעיני\s+יהוה"],
        "books": ["1KI ", "2KI ", "2CH "],
        "expected_thai_contains": "ชั่วร้าย",
        "must_not_contain": [],
        "exceptions": {},
    },
    # dtr_history_cycle_formulas_2026-05.md — evaluation formula "did right in the eyes of YHWH"
    {
        "doc": "dtr_history_cycle_formulas_2026-05.md",
        "label": "הַיָּשָׁר בְּעֵינֵי יְהוָה (did right in the eyes of YHWH)",
        "hebrew_patterns": [r"הישר\s+בעיני\s+יהוה"],
        "books": ["1KI ", "2KI ", "2CH "],
        "expected_thai_contains": "ถูกต้อง",
        "must_not_contain": [],
        "exceptions": {},
    },
    # dtr_history_cycle_formulas_2026-05.md — high-places notice "the high places were not removed"
    {
        "doc": "dtr_history_cycle_formulas_2026-05.md",
        "label": "הַבָּמוֹת לֹא־סָרוּ (high places not removed)",
        "hebrew_patterns": [r"הבמות\s*לאסרו"],
        "books": ["1KI ", "2KI ", "2CH "],
        "expected_thai_contains": "สถานบูชาบนที่สูง",
        "must_not_contain": [],
        "exceptions": {},
    },

    # aphesis_forgiveness_of_sins_2026-04.md
    {
        "doc": "aphesis_forgiveness_of_sins_2026-04.md",
        "label": "ἄφεσις ἁμαρτιῶν",
        "greek_patterns": [
            r"ἄφεσιν\s+ἁμαρτιῶν",
            r"ἄφεσιν\s+τῶν\s+ἁμαρτιῶν",
            r"ἀφέσει\s+ἁμαρτιῶν",
            r"ἄφεσις\s+ἁμαρτιῶν",
            r"ἀφέσεως\s+ἁμαρτιῶν",
            r"ἄφεσιν\s+εἰς\s+τὸν\s+αἰῶνα",  # MRK 3:29 standalone-with-ἁμαρτήματος
        ],
        # Match the root "ยกโทษ" to accept both noun (การยกโทษ) and verb (ทรงยกโทษ / ยกโทษบาป)
        # forms — the syntactic construction varies but the root is locked.
        "expected_thai_contains": "ยกโทษ",
        "must_not_contain": ["การอภัยบาป", "การอภัยเลยตลอด"],
        "exceptions": {
            # Verses where ἄφεσις means "release" (Jubilee/Isaianic), not "forgiveness"
            "Luke 4:18": "Isa 61:1 citation; ἄφεσις = Jubilee-release of captives, not forgiveness-of-sins; correctly rendered ปลดปล่อย",
        },
    },

    # basileia_kingdom_rendering_2026-04.md
    {
        "doc": "basileia_kingdom_rendering_2026-04.md",
        "label": "βασιλεία τοῦ θεοῦ",
        "greek_patterns": [
            r"βασιλεί\w+\s+τοῦ\s+θεοῦ",
            r"βασιλεί\w+\s+θεοῦ",  # anarthrous form
        ],
        "expected_thai_contains": "อาณาจักรของพระเจ้า",
        "must_not_contain": ["อาณาจักรสวรรค์"],  # that's the οὐρανῶν form
        "exceptions": {},
    },
    {
        "doc": "basileia_kingdom_rendering_2026-04.md",
        "label": "βασιλεία τῶν οὐρανῶν (Matthew)",
        "greek_patterns": [
            r"βασιλεί\w+\s+τῶν\s+οὐρανῶν",
        ],
        "expected_thai_contains": "อาณาจักรสวรรค์",
        "must_not_contain": [],
        "exceptions": {},
    },

    # amen_saying_formula_2026-04.md (Synoptic single-amen)
    # Matches the distinctive prefix "เราบอกความจริง"; the pronoun can vary by
    # register (พวกท่าน default; พวกเจ้า in principled downward-address contexts
    # like parable-judgment scenes; ท่านทั้งหลาย as an earlier Markan form).
    # The core lock is the "เราบอกความจริง" stem; downstream pronoun/preposition
    # variations are either documented exceptions or pending normalization.
    # Negative lookbehind excludes Johannine doubled-amen (handled by the next
    # lock).
    {
        "doc": "amen_saying_formula_2026-04.md",
        "label": "ἀμὴν λέγω ὑμῖν (Synoptic single)",
        "greek_patterns": [
            r"(?<!ἀμὴν\s)(?<!Ἀμὴν\s)ἀμὴν\s+λέγω\s+ὑμῖν",
            r"(?<!ἀμὴν\s)(?<!Ἀμὴν\s)Ἀμὴν\s+λέγω\s+ὑμῖν",
        ],
        "expected_thai_contains": "เราบอกความจริง",
        "must_not_contain": [],
        "exceptions": {
            # MAT register-appropriate downward-address (parable-judgment); documented per-verse
            "Matthew 25:12": "bridegroom to excluded foolish virgins; พวกเจ้า = downward-distancing register, documented per-verse as principled variation",
            "Matthew 25:45": "king judgment to goats; พวกเจ้า = downward-distancing register, documented per-verse as principled variation",
            # MAT anomalies Gemini flagged — already documented as pending normalization
            "Matthew 5:18": "pending normalization per MAT end-of-book review",
            "Matthew 5:26": "σοι singular; different formula",
            "Matthew 13:17": "pending normalization per MAT end-of-book review",
        },
    },

    # johannine_doubled_amen_2026-04.md (John only — Aramaic-embed treatment)
    # Distinct from the Synoptic single-amen lock above. The doubled form
    # appears 25× in John and renders "อาเมน อาเมน" preserving the Aramaic
    # word as embed (consistent with aramaic_transliterations_2026-04.md).
    {
        "doc": "johannine_doubled_amen_2026-04.md",
        "label": "ἀμὴν ἀμὴν λέγω ὑμῖν (Johannine doubled)",
        "greek_patterns": [
            r"ἀμὴν\s+ἀμὴν\s+λέγω\s+ὑμῖν",
            r"Ἀμὴν\s+ἀμὴν\s+λέγω\s+ὑμῖν",
        ],
        "expected_thai_contains": "อาเมน อาเมน",
        "must_not_contain": [],
        "exceptions": {},
    },

    # son_of_man_disambiguation_2026-04.md
    {
        "doc": "son_of_man_disambiguation_2026-04.md",
        "label": "ὁ υἱὸς τοῦ ἀνθρώπου (Christological title)",
        "greek_patterns": [
            r"ὁ\s+υἱὸς\s+τοῦ\s+ἀνθρώπου",
            r"τὸν\s+υἱὸν\s+τοῦ\s+ἀνθρώπου",
            r"τοῦ\s+υἱοῦ\s+τοῦ\s+ἀνθρώπου",
            r"τῷ\s+υἱῷ\s+τοῦ\s+ἀνθρώπου",
        ],
        "expected_thai_contains": "บุตรมนุษย์",
        "must_not_contain": [],
        "exceptions": {
            # Heb 2:6 is a Ps 8:4 citation in generic-anthropological sense — documented
            "Hebrews 2:6": "Ps 8:4 LXX citation; generic υἱὸς ἀνθρώπου, not Christological title — expected to render differently; documented per son_of_man_disambiguation doc",
        },
    },

    # pneuma ἅγιον (glossary-locked + in RULES §4)
    {
        "doc": "RULES.md §4 + glossary",
        "label": "πνεῦμα ἅγιον",
        "greek_patterns": [
            r"πνεῦμα\s+ἅγιον",
            r"πνεύματος\s+ἁγίου",
            r"πνεύματι\s+ἁγίῳ",
            r"πνεῦμα\s+ἅγιόν",
            r"ἁγίου\s+πνεύματος",
            r"ἁγίῳ\s+πνεύματι",
            r"ἅγιον\s+πνεῦμα",
        ],
        "expected_thai_contains": "พระวิญญาณบริสุทธิ์",
        "must_not_contain": [],
        "exceptions": {},
    },

    # ekklesia_2026-04.md
    {
        "doc": "ekklesia_2026-04.md",
        "label": "ἐκκλησία (Christian community sense)",
        "greek_patterns": [
            r"ἐκκλησί\w+",
        ],
        "expected_thai_contains": "คริสตจักร",
        "must_not_contain": [],
        "exceptions": {
            # Acts 7:38 (LXX assembly-of-Israel) + Acts 19:32/39/40 (secular civic — SBLGNT combines TR v.40+41 into v.40)
            "Acts 7:38": "OT/LXX assembly-of-Israel; use ที่ประชุม per ekklesia doc exception",
            "Acts 19:32": "secular civic Greek assembly; use ที่ประชุม/การชุมนุม",
            "Acts 19:39": "secular civic Greek assembly; use ที่ประชุม/การชุมนุม",
            "Acts 19:40": "secular civic Greek assembly; use ที่ประชุม/การชุมนุม (SBLGNT combines TR v.40+41)",
        },
    },
    # ===== auto-wired 2026-05-29 from the lock-enforcement audit (23 validated of 28 checkable) =====
    # Each was corpus-validated via audit_one_lock; current drift is documented as exceptions
    # pending Ben sign-off. See docs/end_of_book/_audits/locked_surface_audit_2026-05-29.md
    {
        "doc": 'captain_of_yhwh_host_2026-05.md',
        "label": "שַׂר־צְבָא־יְהוָה (commander of YHWH's army)",
        "hebrew_patterns": ['שרצבא\\s*יהוה'],
        "books": ['JOS ', 'Daniel ', 'Zechariah '],
        "expected_thai_contains": 'ผู้บัญชาการกองทัพขององค์พระผู้เป็นเจ้า',
        "must_not_contain": [],
        "exceptions": {},
    },
    {
        "doc": 'cities_of_refuge_blood_avenger_2026-05.md',
        "label": 'גֹּאֵל הַדָּם (avenger of blood) → ผู้แก้แค้นเลือด',
        "hebrew_patterns": ['גאל\\s*הדם'],
        "books": ['NUM ', 'DEU ', 'JOS ', '2SA ', '1KI ', '2KI ', '1 Kings '],
        "expected_thai_contains": 'ผู้แก้แค้นเลือด',
        "must_not_contain": ['ผู้แก้แค้นโลหิต', 'แทนเลือด'],
        "exceptions": {},
    },
    {
        "doc": 'decalogue_parallel_text_2026-05.md',
        "label": 'NT Decalogue citation 8th cmd (Οὐ/Μὴ κλέψεις inside the murder+adultery list) → อย่าลักทรัพย์ (per §3/§4 HARD-FAIL; reje',
        "greek_patterns": ['μοιχεύσ\\w+.*κλέψ\\w+', 'κλέψ\\w+.*μοιχεύσ\\w+'],
        "books": ['Matthew ', 'MRK ', 'Mark ', 'Luke ', 'Romans ', 'James '],
        "expected_thai_contains": 'ลักทรัพย์',
        "must_not_contain": ['ขโมย'],
        "exceptions": {
            'Romans 13:9': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
        },
    },
    {
        "doc": 'dikaioo_dikaiosyne_family_2026-05.md',
        "label": "δικαιόω verb (forensic-declarative 'justify' of believers) — Pauline corpus + James",
        "greek_patterns": ['δικαιω\\w*', 'δικαιοῦ\\w*', 'δικαιοῖ', 'ἐδικαι\\w*', 'δεδικαι\\w*'],
        "books": ['Romans ', '1 Corinthians ', '2 Corinthians ', 'Galatians ', 'Ephesians ', 'Philippians ', 'Colossians ', '1 Thessalonians ', '2 Thessalonians ', '1 Timothy ', '2 Timothy ', 'Titus ', 'Philemon ', 'James '],
        "expected_thai_contains": 'ประกาศ',
        "must_not_contain": ['นับว่าชอบธรรม'],
        "exceptions": {
            '1 Corinthians 6:11': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'James 2:21': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'James 2:24': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'James 2:25': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Romans 2:13': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Romans 3:4': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
        },
    },
    {
        "doc": 'epiphaneia_christou_2026-05.md',
        "label": "ἐπιφάνεια (Christ's appearing — Pastorals)",
        "greek_patterns": ['ἐπιφανεί\\w+', 'ἐπιφάνει\\w+'],
        "books": ['1 Timothy ', '2 Timothy ', 'Titus '],
        "expected_thai_contains": 'การทรงปรากฏ',
        "must_not_contain": ['การเสด็จมาปรากฏ'],
        "exceptions": {},
    },
    {
        "doc": 'evil_spirit_from_yhwh_1sam_2026-05.md',
        "label": 'רוּחַ רָעָה מֵאֵת יְהוָה (evil spirit from YHWH/God) — 1 Samuel cluster',
        "hebrew_patterns": ['רוח\\s*(?:יהוה|אלהים)?\\s*רעה'],
        "books": ['1SA ', '2SA '],
        "expected_thai_contains": 'วิญญาณชั่ว',
        "must_not_contain": [],
        "exceptions": {},
    },
    {
        "doc": 'huiothesia_adoption_2026-05.md',
        "label": 'υἱοθεσία (Pauline adoption-as-sons; Greco-Roman legal-rights force)',
        "greek_patterns": ['υἱοθεσ'],
        "expected_thai_contains": 'สิทธิ์การเป็นบุตร',
        "must_not_contain": ['การรับเป็นบุตร'],
        "exceptions": {},
    },
    {
        "doc": 'hygiaino_sound_doctrine_2026-05.md',
        "label": 'ὑγιαίνω/ὑγιής family (sound-doctrine metaphor) → ถูกต้อง (Pastorals only)',
        "greek_patterns": ['ὑγι'],
        "books": ['1 Timothy ', '2 Timothy ', 'Titus '],
        "expected_thai_contains": 'ถูกต้อง',
        "must_not_contain": [],
        "exceptions": {},
    },
    {
        "doc": 'i_am_yhwh_holiness_formula_2026-05.md',
        "label": 'אֲנִי יְהוָה (I-am-YHWH Holiness/recognition formula) → องค์พระผู้เป็นเจ้า (leitwort divine name)',
        "hebrew_patterns": ['(?:^|\\s)אני\\s+יהוה'],
        "expected_thai_contains": 'องค์พระผู้เป็นเจ้า',
        "must_not_contain": ['เราคือพระยาห์เวห์', 'เราคือพระเจ้าของพวกเจ้า'],
        "exceptions": {},
    },
    {
        "doc": 'kapporet_atonement_cover_2026-05.md',
        "label": 'כַּפֹּרֶת (kapporet — mercy seat / cover of ark)',
        "hebrew_patterns": ['(?<!ו)כפרת'],
        "expected_thai_contains": 'พระที่นั่งกรุณา',
        "must_not_contain": ['ที่ลบล้างบาป'],
        "exceptions": {},
    },
    {
        "doc": 'kareth_penalty_formula_2026-05.md',
        "label": 'kāret niphal penalty — וְנִכְרְתָה הַנֶּפֶשׁ ... מֵעַמָּיו (the soul shall be cut off from his people)',
        "hebrew_patterns": ['ו?נכרת[הו]?\\s*ה?נפש', 'ו?נכרת[הו]?(?!\\s*ברית)[\\s\\w]{0,22}?(מעמי|מעמ|מקרב|מתוך|עמם|עמ\\b)'],
        "expected_thai_contains": 'ตัดออก',
        "must_not_contain": [],
        "exceptions": {
            'Genesis 17:14': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
        },
    },
    {
        "doc": 'logos_johannine_2026-04.md',
        "label": 'ὁ Λόγος (Christological titular Logos — John Prologue + REV 19:13 → พระวาทะ)',
        "greek_patterns": ['ἀρχῇ\\s*ἦν\\s*ὁ\\s*λόγος', 'ὁ\\s*λόγος\\s*σὰρξ\\s*ἐγένετο', 'ὁ\\s*Λόγος\\s*τοῦ\\s*Θεοῦ'],
        "expected_thai_contains": 'พระวาทะ',
        "must_not_contain": ['พระวจนะ'],
        "exceptions": {},
    },
    {
        "doc": 'manah_divine_appointment_2026-05.md',
        "label": "Pi'el וַיְמַן + divine name (divine-subject appointment Leitwort — manah → ทรงจัดเตรียม)",
        "hebrew_patterns": ['וימן\\s*(?:יהוה|אלהים|האלהים|יהוהאלהים)'],
        "expected_thai_contains": 'ทรงจัดเตรียม',
        "must_not_contain": [],
        "exceptions": {},
    },
    {
        "doc": 'metanoeo_vs_metamelomai_2026-04.md',
        "label": 'μετανοέω / μετάνοια (salvific repentance → กลับใจ root; distinct from μεταμέλομαι)',
        "greek_patterns": ['[ΜμMm]ετ[αά]νο'],
        "expected_thai_contains": 'กลับใจ',
        "must_not_contain": [],
        "exceptions": {},
    },
    {
        "doc": 'ot_nt_cross_quotation_thread_2026-05.md',
        "label": 'נביא / προφήτης (prophet, person-noun) -> ผู้เผยพระวจนะ (cross-quotation thread §2.1)',
        "greek_patterns": ['(?<!ψευδο)προφ[ήῆ]τ(?:ης|ου|ῃ|ην|αι|ῶν|αις|ας)\\b'],
        "expected_thai_contains": 'ผู้เผยพระวจนะ',
        "must_not_contain": ['ผู้พยากรณ์'],
        "exceptions": {
            '1 Corinthians 14:29': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            '1 Corinthians 14:32': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            '1 Corinthians 14:37': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            '2 Peter 2:16': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Acts 21:10': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Luke 9:8': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Luke 9:19': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Luke 10:24': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Revelation 10:7': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Revelation 11:10': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Revelation 11:18': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
            'Titus 1:12': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
        },
    },
    {
        "doc": 'parepidemos_paroikos_sojourner_2026-05.md',
        "label": 'παρεπίδημος (passing-through sojourner) -> คนต่างถิ่น',
        "greek_patterns": ['παρεπ[ιί]δ[ηή]μ'],
        "expected_thai_contains": 'คนต่างถิ่น',
        "must_not_contain": [],
        "exceptions": {
            'Hebrews 11:13': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
        },
    },
    {
        "doc": 'pharaoh_heart_hardening_2026-05.md',
        "label": 'Pharaoh / heart-hardening idiom — חזק/קשה/כבד + לב(ב) → แข็งกระด้าง',
        "hebrew_patterns": ['חזק\\w{0,3}\\s+(?:את)?\\s*לב(?:ב)?(?:פרעה|כם|נו|ו|ם|ך|י|בכם)?(?=\\s|$)', 'כבד\\w{0,3}\\s+(?:את)?\\s*לב(?:ב)?(?:פרעה|כם|נו|ו|ם|ך|י|בכם)?(?=\\s|$)', 'קש\\w{0,2}\\s+(?:את)?\\s*לב(?:ב)?(?:פרעה|כם|נו|ו|ם|ך|י|בכם)?(?=\\s|$)', 'אחזק\\s+(?:את)?\\s*לב(?:ב)?(?:פרעה|כם|נו|ו|ם|ך|י)?(?=\\s|$)', 'חזקתי\\s+(?:את)?\\s*לב(?:ב)?(?:פרעה|כם|נו|ו|ם|ך|י)?(?=\\s|$)'],
        "expected_thai_contains": 'แข็งกระด้าง',
        "must_not_contain": [],
        "exceptions": {
            '1SA 6:6': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
        },
    },
    {
        "doc": 'revelation_divine_self_titles_2026-05.md',
        "label": 'παντοκράτωρ (Almighty) — Revelation',
        "greek_patterns": ['παντοκράτ\\w*'],
        "books": ['Revelation '],
        "expected_thai_contains": 'ผู้ทรงฤทธานุภาพยิ่งใหญ่',
        "must_not_contain": [],
        "exceptions": {},
    },
    {
        "doc": 'shared_names_normalization_2026-05.md',
        "label": 'Ἀράμ → ราม (Ram; shared OT/NT name, Hebrew form wins)',
        "greek_patterns": ['Ἀρ[άὰ]μ'],
        "books": ['Matthew '],
        "expected_thai_contains": 'ราม',
        "must_not_contain": [],
        "exceptions": {},
    },
    {
        "doc": 'spiritual_beings_hierarchy_2026-05.md',
        "label": 'κυριότητες / κυριότης (dominions) -> ผู้ทรงเดชานุภาพ; cosmic-being class must NOT take เทพ deity-register',
        "greek_patterns": ['κυριότητ'],
        "books": ['Colossians ', 'Ephesians '],
        "expected_thai_contains": 'ผู้ทรงเดชานุภาพ',
        "must_not_contain": ['เทพ'],
        "exceptions": {},
    },
    {
        "doc": 'stoicheia_tou_kosmou_2026-05.md',
        "label": 'στοιχεῖα τοῦ κόσμου (basic-principles default) -> หลักการพื้นฐานของโลก',
        "greek_patterns": ['στοιχεῖα\\s+τοῦ\\s+κόσμου', 'στοιχείων\\s+τοῦ\\s+κόσμου'],
        "expected_thai_contains": 'หลักการพื้นฐานของโลก',
        "must_not_contain": [],
        "exceptions": {},
    },
    {
        "doc": 'telos_paidagogos_christ_2026-05.md',
        "label": 'τέλος νόμου Χριστὸς (Rom 10:4) -> จุดสิ้นสุดของธรรมบัญญัติ (TERMINAL; not goal-sense)',
        "greek_patterns": ['τέλος\\s+\\w*\\s*νόμου\\s+Χριστὸς', 'τέλος\\s+νόμου\\s+Χριστὸς'],
        "books": ['Romans '],
        "expected_thai_contains": 'จุดสิ้นสุดของธรรมบัญญัติ',
        "must_not_contain": ['เป้าหมาย', 'จุดมุ่งหมาย'],
        "exceptions": {},
    },
    {
        "doc": 'therion_beast_apocalyptic_2026-05.md',
        "label": 'θηρίον (apocalyptic Beast, Revelation) -> สัตว์ร้าย',
        "greek_patterns": ['θηρί'],
        "books": ['Revelation '],
        "expected_thai_contains": 'สัตว์ร้าย',
        "must_not_contain": ['สัตว์ป่า'],
        "exceptions": {
            'Revelation 6:8': 'auto-audit 2026-05-29: drift pending Ben sign-off (see locked_surface_audit report)',
        },
    },

]


def load_all_verses():
    """Yield (reference, verse-dict) for every shipped translation."""
    for f in sorted(TRANSLATIONS.glob("*.json")):
        try:
            data = json.load(open(f))
        except (json.JSONDecodeError, OSError):
            continue
        if not isinstance(data, list):
            continue
        for v in data:
            if isinstance(v, dict) and ("greek" in v or "hebrew" in v) and "translation" in v:
                yield v.get("reference", f"?{v.get('chapter')}:{v.get('verse')}"), v


def strip_niqqud(s):
    """Drop Hebrew vowel-points + cantillation + maqqef so hebrew_patterns can be
    written consonantally (robust to pointing/maqqef variation)."""
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", s) if not (0x0591 <= ord(c) <= 0x05C7))


def audit_one_lock(lock, verses):
    """Return list of violation dicts for one phrase lock."""
    violations = []
    matches = []  # all matching verses (for reporting total coverage)
    gpats = lock.get("greek_patterns", [])
    hpats = lock.get("hebrew_patterns", [])  # matched against niqqud-stripped Hebrew (OT)
    books = lock.get("books")  # optional ref-prefix scope, e.g. ["1KI ", "2KI "] for Kings-only locks
    for ref, v in verses:
        if books and not any(ref.startswith(b) for b in books):
            continue
        greek = v.get("greek", "") or ""
        hebrew_cons = strip_niqqud(v.get("hebrew", "") or "")
        # Any source pattern match? Greek for NT verses, consonantal Hebrew for OT.
        matched = any(re.search(p, greek) for p in gpats) or any(re.search(p, hebrew_cons) for p in hpats)
        if not matched:
            continue
        # Exception?
        if ref in lock.get("exceptions", {}):
            matches.append({"ref": ref, "status": "EXCEPTED", "reason": lock["exceptions"][ref]})
            continue
        thai = v["translation"].get("thai", "") or ""
        expected = lock["expected_thai_contains"]
        forbidden = lock.get("must_not_contain", [])
        # Check: does Thai contain expected substring?
        has_expected = expected in thai
        has_forbidden = any(f in thai for f in forbidden) if forbidden else False
        if has_expected and not has_forbidden:
            matches.append({"ref": ref, "status": "OK"})
        else:
            snippet_idx = -1
            for f in forbidden + [expected]:
                idx = thai.find(f)
                if idx >= 0:
                    snippet_idx = idx
                    break
            snippet = thai[max(0, snippet_idx - 20): snippet_idx + 60] if snippet_idx >= 0 else thai[:80]
            violations.append({
                "ref": ref,
                "greek": (greek or v.get("hebrew", "") or "")[:100],
                "thai_snippet": snippet,
                "expected": expected,
                "forbidden_hit": [f for f in forbidden if f in thai],
            })
            matches.append({"ref": ref, "status": "VIOLATION"})
    return violations, matches


def write_report(results, out_path):
    lines = ["# Phrase-level consistency audit report", ""]
    any_violations = False
    for lock, violations, matches in results:
        ok_count = sum(1 for m in matches if m["status"] == "OK")
        excepted_count = sum(1 for m in matches if m["status"] == "EXCEPTED")
        viol_count = len(violations)
        lines.append(f"## {lock['label']}")
        lines.append(f"**Doc:** `{lock['doc']}`  ")
        lines.append(f"**Expected Thai contains:** `{lock['expected_thai_contains']}`  ")
        lines.append(f"**Total matching verses:** {len(matches)}  ")
        lines.append(f"**OK:** {ok_count} · **Excepted:** {excepted_count} · **Violations:** {viol_count}")
        lines.append("")
        if violations:
            any_violations = True
            lines.append("### ❌ Violations")
            for v in violations:
                lines.append(f"- **{v['ref']}**")
                lines.append(f"  - Greek: `{v['greek']}`")
                lines.append(f"  - Thai snippet: `{v['thai_snippet']}`")
                if v["forbidden_hit"]:
                    lines.append(f"  - Found forbidden rendering: `{', '.join(v['forbidden_hit'])}`")
                else:
                    lines.append(f"  - Missing expected `{v['expected']}`")
            lines.append("")
        if lock.get("exceptions"):
            lines.append("### Documented exceptions (not violations)")
            for ref, reason in lock["exceptions"].items():
                lines.append(f"- **{ref}** — {reason}")
            lines.append("")
    out_path.write_text("\n".join(lines))
    return any_violations


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stdout", action="store_true", help="Print report to stdout instead of writing file")
    ap.add_argument("--json", action="store_true", help="JSON output")
    args = ap.parse_args()

    verses = list(load_all_verses())
    print(f"Scanned {len(verses)} verses across {len(list(TRANSLATIONS.glob('*.json')))} chapter files.")

    results = []
    total_violations = 0
    for lock in PHRASE_LOCKS:
        violations, matches = audit_one_lock(lock, verses)
        results.append((lock, violations, matches))
        total_violations += len(violations)

    if args.json:
        out = []
        for lock, violations, matches in results:
            out.append({
                "label": lock["label"],
                "doc": lock["doc"],
                "expected": lock["expected_thai_contains"],
                "matches_total": len(matches),
                "ok": sum(1 for m in matches if m["status"] == "OK"),
                "excepted": sum(1 for m in matches if m["status"] == "EXCEPTED"),
                "violations": violations,
            })
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS / "phrase_consistency.md"
        has_viol = write_report(results, out_path)
        print(f"Wrote {out_path}")
        print(f"  Phrase locks audited: {len(PHRASE_LOCKS)}")
        print(f"  Total violations: {total_violations}")
        if has_viol:
            print()
            print("VIOLATIONS DETECTED — see report above. Fix or document exception.")
            sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
