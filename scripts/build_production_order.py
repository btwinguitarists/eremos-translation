#!/usr/bin/env python3
"""
Generate data/production_order.json — the canonical order in which the Bible
should be translated, per GENRES.md and the OT-rollout plan §16-17.

This is a build-time script. Run it once to (re)generate the order file.
The runtime resolver (next_chapter.py) reads the JSON.

Order rationale: SIL/Wycliffe-style complexity progression. Narrative first
(builds vocabulary), Pauline corpus as a block (theological coherence),
general epistles, Revelation (after symbol/vision check infrastructure),
then OT in phase 6 — pilot first (Ruth → Jonah → Gen 1-11) per
docs/translator_decisions plan §17.2 — followed by Pentateuch narrative,
Pentateuch law, Former Prophets, Writings, Wisdom/Poetry, Major Prophets,
the Twelve.
"""
import json
from pathlib import Path

# NT chapter counts (verified against SBLGNT)
NT_CHAPTERS = {
    "MAT": 28, "MRK": 16, "LUK": 24, "JHN": 21, "ACT": 28,
    "ROM": 16, "1CO": 16, "2CO": 13, "GAL": 6, "EPH": 6, "PHP": 4, "COL": 4,
    "1TH": 5, "2TH": 3, "1TI": 6, "2TI": 4, "TIT": 3, "PHM": 1,
    "HEB": 13, "JAS": 5, "1PE": 5, "2PE": 3,
    "1JN": 5, "2JN": 1, "3JN": 1, "JUD": 1, "REV": 22,
}

# OT chapter counts (verified against MACULA Hebrew WLC + standard MT versification)
OT_CHAPTERS = {
    "GEN": 50, "EXO": 40, "LEV": 27, "NUM": 36, "DEU": 34,
    "JOS": 24, "JDG": 21, "RUT": 4,
    "1SA": 31, "2SA": 24, "1KI": 22, "2KI": 25,
    "1CH": 29, "2CH": 36, "EZR": 10, "NEH": 13, "EST": 10,
    "JOB": 42, "PSA": 150, "PRO": 31, "ECC": 12, "SNG": 8,
    "ISA": 66, "JER": 52, "LAM": 5, "EZK": 48, "DAN": 12,
    "HOS": 14, "JOL": 4, "AMO": 9, "OBA": 1, "JON": 4, "MIC": 7,
    "NAM": 3, "HAB": 3, "ZEP": 3, "HAG": 2, "ZEC": 14, "MAL": 3,
}

# Per-book primary language. Most are Hebrew throughout; Daniel and Ezra
# include Aramaic sections (Dan 2:4b–7:28; Ezr 4:8–6:18, 7:12–26). The
# per-verse extract from extract_book_hebrew.py carries the actual word-level
# language; this entry is the *book-level default* for production order metadata.
OT_BOOK_LANGUAGE = {b: "hebrew" for b in OT_CHAPTERS}

# Per-book primary genre, per plan §7 + GENRES.md. Used by the formula-lock
# dispatcher and the genre-aware external-review packet builder. Some books
# span multiple genres (Pentateuch = narrative + law); the primary tag is the
# default; per-chapter override happens via book-range entries below.
OT_BOOK_GENRE = {
    # Narrative
    "GEN": "narrative-primeval-patriarchal",
    "EXO": "narrative-mosaic-exodus",
    "NUM": "narrative-mosaic-exodus",
    "DEU": "law-deuteronomic",  # mostly law w/ narrative frame
    "JOS": "narrative-conquest",
    "JDG": "narrative-cyclical-judges",
    "RUT": "narrative-idyllic-novella",
    "1SA": "narrative-court-monarchy",
    "2SA": "narrative-court-monarchy",
    "1KI": "narrative-court-monarchy",
    "2KI": "narrative-court-monarchy",
    "1CH": "narrative-chronicler",
    "2CH": "narrative-chronicler",
    "EZR": "narrative-post-exilic",
    "NEH": "narrative-post-exilic",
    "EST": "narrative-diaspora-court-tale",
    # Law (subset of Pentateuch)
    "LEV": "law-holiness-priestly",
    # Wisdom / Poetry
    "JOB": "wisdom-suffering-theodicy",
    "PSA": "poetry-psalter",
    "PRO": "wisdom-aphoristic",
    "ECC": "wisdom-philosophical",
    "SNG": "poetry-erotic-allegorical",
    "LAM": "poetry-lament-qinah",
    # Prophecy
    "ISA": "prophecy-classical",
    "JER": "prophecy-classical",
    "EZK": "prophecy-visionary-apocalyptic",
    "DAN": "prophecy-apocalyptic-aramaic",
    "HOS": "prophecy-classical",
    "JOL": "prophecy-day-of-yhwh",
    "AMO": "prophecy-classical",
    "OBA": "prophecy-classical",
    "JON": "narrative-prophetic-novella",  # narrative form
    "MIC": "prophecy-classical",
    "NAM": "prophecy-classical",
    "HAB": "prophecy-classical",
    "ZEP": "prophecy-classical",
    "HAG": "prophecy-post-exilic",
    "ZEC": "prophecy-apocalyptic",
    "MAL": "prophecy-disputation",
}

# Phase ordering for both NT and OT
PHASES = [
    {
        "name": "Phase 2 — NT narrative",
        "books": ["MRK", "MAT", "LUK", "ACT", "JHN"],
    },
    {
        "name": "Phase 3 — Pauline corpus (composition order)",
        "books": ["GAL", "1TH", "2TH", "1CO", "2CO", "ROM", "PHM", "PHP",
                  "COL", "EPH", "1TI", "2TI", "TIT"],
    },
    {
        "name": "Phase 4 — General epistles + Hebrews",
        "books": ["JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "HEB"],
    },
    {
        "name": "Phase 5 — Revelation (after apocalyptic checks built)",
        "books": ["REV"],
    },
    # ─── OT phases (6A through 6H) per plan §16-17 ─────────────────────────
    # 6A Pilot: Ruth → Jonah → Genesis 1-11 (narrative + simple poetry stress
    # tests before tackling primeval-history theological weight). Genesis is
    # split — chapters 1-11 here in the pilot, 12-50 in 6B.
    {
        "name": "Phase 6A — OT pilot (Ruth → Jonah → Gen 1-11)",
        "books": [
            ("RUT", None),     # all 4 chapters
            ("JON", None),     # all 4 chapters
            ("GEN", (1, 11)),  # primeval narrative only
        ],
    },
    {
        "name": "Phase 6B — Pentateuch narrative (Gen 12-50, Exod, Num)",
        "books": [
            ("GEN", (12, 50)),
            "EXO",
            "NUM",
        ],
    },
    {
        "name": "Phase 6C — Pentateuch law (Lev, Deut)",
        "books": ["LEV", "DEU"],
    },
    {
        "name": "Phase 6D — Former Prophets (Josh / Judg / Sam / Kings)",
        "books": ["JOS", "JDG", "1SA", "2SA", "1KI", "2KI"],
    },
    {
        "name": "Phase 6E — Writings (Chr / Ezr / Neh / Esth / Dan)",
        "books": ["1CH", "2CH", "EZR", "NEH", "EST", "DAN"],
    },
    {
        "name": "Phase 6F — Wisdom and Poetry (Job / Psa / Prov / Eccl / Song / Lam)",
        "books": ["JOB", "PSA", "PRO", "ECC", "SNG", "LAM"],
    },
    {
        "name": "Phase 6G — Major Prophets (Isa / Jer / Ezek)",
        "books": ["ISA", "JER", "EZK"],
    },
    {
        "name": "Phase 6H — The Twelve (minor prophets, ex-Jonah)",
        "books": ["HOS", "JOL", "AMO", "OBA", "MIC", "NAM", "HAB", "ZEP",
                  "HAG", "ZEC", "MAL"],
    },
]


def book_chapter_range(book_spec) -> tuple[str, range]:
    """Resolve a phase entry to (book_code, chapter_range).

    The phase `books` list accepts either:
      - "GEN" — all chapters of the book
      - ("GEN", None) — same as above
      - ("GEN", (1, 11)) — chapters 1 through 11 inclusive
    """
    if isinstance(book_spec, str):
        book = book_spec
        chapters = OT_CHAPTERS.get(book) or NT_CHAPTERS.get(book)
        return book, range(1, chapters + 1)
    if isinstance(book_spec, tuple):
        book, rng = book_spec
        if rng is None:
            chapters = OT_CHAPTERS.get(book) or NT_CHAPTERS.get(book)
            return book, range(1, chapters + 1)
        start, end = rng
        return book, range(start, end + 1)
    raise ValueError(f"Unknown book spec: {book_spec!r}")


def main():
    order = []
    for phase in PHASES:
        for book_spec in phase["books"]:
            book, ch_range = book_chapter_range(book_spec)
            is_ot = book in OT_CHAPTERS
            for ch in ch_range:
                entry = {
                    "book": book,
                    "chapter": ch,
                    "phase": phase["name"],
                }
                if is_ot:
                    entry["language"] = OT_BOOK_LANGUAGE.get(book, "hebrew")
                    entry["primary_genre"] = OT_BOOK_GENRE.get(book)
                else:
                    entry["language"] = "greek"
                order.append(entry)

    out = {
        "_note": "Auto-generated by build_production_order.py based on GENRES.md + OT-rollout plan §16-17.",
        "_total_chapters": len(order),
        "_phases": [p["name"] for p in PHASES],
        "order": order,
    }

    out_path = Path(__file__).resolve().parent.parent / "data" / "production_order.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")
    nt_count = sum(1 for e in order if e["language"] == "greek")
    ot_count = len(order) - nt_count
    print(f"  Total chapters: {len(order)} ({nt_count} NT + {ot_count} OT)")


if __name__ == "__main__":
    main()
