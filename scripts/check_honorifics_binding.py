#!/usr/bin/env python3
"""
Honorifics-binding check for OT translations.

Authoritative source of policy:
  docs/translator_decisions/ot_register_policy_2026-05.md  (Rachasap policy)

Background:
  Thai ราชาศัพท์ (royal Thai) layers two distinct vocabulary slots over plain Thai:
  the **noun layer** uses พระ-prefix body-part terms (พระหัตถ์ "hand", พระเนตร
  "eye", พระบาท "foot", etc.) and the **verb layer** uses ทรง-prefix verbs
  (ทรงตรัส "say", ทรงยื่น "stretch out", etc.). The two layers exist
  independently — a verse can use the พระ- nouns without the ทรง- verbs and
  vice versa.

  The Rachasap rule: ทรง- is bound to the verb's grammatical SUBJECT being a
  divine being (YHWH, Christ in OT typology) or a recognised monarch. When
  the subject is a *body-part* of God (พระหัตถ์, พระเนตร, etc.), the verb
  carries no ทรง-: the body-part is performing the action, the divine being
  is not directly the actor. Stacking both yields a category error.

  Ruth 1:13 originally shipped with `พระหัตถ์ขององค์พระผู้เป็นเจ้าทรงยื่นออกมา`
  ("the hand of YHWH ROYALLY-stretched-out") — the construct-chain head-noun
  is `พระหัตถ์` (the hand), not `องค์พระผู้เป็นเจ้า`, so ทรง- on the verb is
  bound to the wrong subject. The fix dropped ทรง- to give
  `พระหัตถ์ขององค์พระผู้เป็นเจ้าได้ยื่นออกมา`. This check catches that class.

What this enforces:

  [A] HARD FAIL — A `ทรง[verb]` whose nearest preceding subject candidate is
      a body-part-of-God noun (`พระหัตถ์`, `พระเนตร`, etc.). The body-part is
      the head of the construct chain; the verb's subject is the body-part,
      not the divine being further up the chain. Pattern:
        BODY-PART [+ ของ + DIVINE_SUBJECT]? [≤25 chars no verb] ทรง<verb>

  [B] WARN — A `ทรง[verb]` with no divine subject and no recognised monarch
      in the preceding ~60 chars (within the same sentence). Either the
      subject is being inferred across a sentence break (legitimate in Thai
      narrative — flag for review) or the translator may have over-applied
      Rachasap to a non-royal subject.

  Both checks honour an EXCUSE keyword in the matching `key_decisions`
  rationale (rachasap, royal register, honorifics, intentional, etc.) so a
  deliberate violation can be documented and waived.

Usage:
  python3 scripts/check_honorifics_binding.py --book RUT --chapter 1
  python3 scripts/check_honorifics_binding.py --all
  python3 scripts/check_honorifics_binding.py --book RUT --chapter 1 --report

Exit codes:
  0 = clean
  1 = at least one [A] hard fail
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSLATIONS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"

OT_SLUG_TO_CODE = {
    "genesis": "GEN", "exodus": "EXO", "leviticus": "LEV", "numbers": "NUM",
    "deuteronomy": "DEU", "joshua": "JOS", "judges": "JDG", "ruth": "RUT",
    "1samuel": "1SA", "2samuel": "2SA", "1kings": "1KI", "2kings": "2KI",
    "1chronicles": "1CH", "2chronicles": "2CH", "ezra": "EZR", "nehemiah": "NEH",
    "esther": "EST", "job": "JOB", "psalms": "PSA", "proverbs": "PRO",
    "ecclesiastes": "ECC", "songofsongs": "SNG", "isaiah": "ISA", "jeremiah": "JER",
    "lamentations": "LAM", "ezekiel": "EZK", "daniel": "DAN", "hosea": "HOS",
    "joel": "JOL", "amos": "AMO", "obadiah": "OBA", "jonah": "JON",
    "micah": "MIC", "nahum": "NAM", "habakkuk": "HAB", "zephaniah": "ZEP",
    "haggai": "HAG", "zechariah": "ZEC", "malachi": "MAL",
}

# Body-part royal nouns per ot_register_policy_2026-05 §1.2 + §1.4. These are
# the "พระ-prefix on body parts" set. Order matters: longer forms first so a
# regex doesn't match พระกร inside พระกรรณ.
BODY_PARTS_OF_GOD = [
    "พระหฤทัย",       # heart (formal)
    "พระวรกาย",       # body
    "พระพักตร์",      # face
    "พระชิวหา",       # tongue
    "พระโอษฐ์",       # mouth
    "พระกรรณ",        # ear
    "พระเนตร",        # eye / sight
    "พระหัตถ์",       # hand
    "พระบาท",         # foot
    "พระทัย",         # heart
    "พระกร",          # arm  (last — substring of พระกรรณ)
]

# Divine + royal subjects whose presence excuses a ทรง-verb (Tier 2 warn level).
# Matches the locked YHWH renderings and common divine epithets per the
# divine_names_table policy. Note: บัลลังก์ ("throne") is NOT divine itself
# but throne-of-God scenes legitimately use ทรง — flagged separately.
DIVINE_SUBJECTS = [
    "องค์พระผู้เป็นเจ้าจอมโยธา",  # YHWH Tsebaoth (longest first)
    "องค์พระผู้เป็นเจ้า",          # YHWH
    "ผู้ทรงมหิทธิฤทธิ์",          # Shaddai (Almighty)
    "พระเจ้าผู้สูงสุด",            # El Elyon
    "พระเจ้าผู้ทรงมหิทธิฤทธิ์",    # El Shaddai
    "พระเจ้านิรันดร์",             # El Olam
    "องค์เจ้านาย",                 # Adonai standalone
    "พระคริสต์",
    "พระเยซู",
    "พระบิดา",
    "พระบุตร",
    "พระวิญญาณบริสุทธิ์",
    "พระวิญญาณ",                   # Spirit (IS divine)
    "พระเจ้า",                     # Elohim — last because it's a substring of compounds
]

# Hebrew kings + foreign emperors that legitimately take Rachasap per
# ot_register_policy §2.2. Add as the OT corpus accumulates them.
KING_INDICATORS = [
    "ดาวิด", "โซโลมอน", "ซาอูล", "เฮซะคียา", "เฮเซคียาห์",
    "โยสิยาห์", "อาหับ", "เยฮู",
    "ฟาโรห์",                   # Pharaoh
    "เนบูคัดเนสซาร์",           # Nebuchadnezzar
    "ไซรัส", "ดาริอัส",         # Cyrus, Darius
    "อาหสุเอรัส", "เซอร์ซีส",   # Ahasuerus, Xerxes
    "อารทาเซอร์เซส",            # Artaxerxes
    "เอสเธอร์",                 # Esther
    "กษัตริย์",                  # generic "king"
]

# Rationale keywords that excuse a flagged use. These need to be specific
# enough that the translator must SPEAK TO the binding decision, not merely
# mention royal-Thai vocabulary in passing. Generic "rachasap" / "royal-Thai"
# tags appear in many kds (e.g. about using พระหัตถ์ vs มือ) without addressing
# whether ทรง- legitimately binds to a body-part subject — those should NOT
# excuse a binding violation.
EXCUSE_KEYWORDS = re.compile(
    r"("
    r"honorifics?[-\s]binding|"           # explicit reference to this check
    r"ทรง[-\s]binding|"
    r"binding[-\s]intentional|"
    r"binding\s+(?:waiver|exception|override)|"
    r"deliberate(?:ly)?\s+(?:bind|stack|apply)|"
    r"intentional\s+ทรง|"
    r"check_honorifics_binding"
    r")",
    re.IGNORECASE,
)

# A ทรง-verb is "ทรง" + a Thai consonant-led stem (Thai verbs typically start
# with a consonant). Stem capped at ~10 chars — Thai verbs are 1–3 syllables,
# rarely longer. Wider regex over-captures into following words and confuses
# the body-part / divine-subject lookup.
TRONG_VERB_RX = re.compile(r"ทรง([ก-ฮ][ก-๛]{0,9})")

# Skip ทรง- inside agentive nouns: `ผู้ทรง[X]` = "the one who is X" (a divine
# title or epithet, not a verb). Examples: ผู้ทรงมหิทธิฤทธิ์ (Almighty),
# ผู้ทรงสร้าง (the Creator). The ทรง- here is part of a noun phrase, not a
# verb prefix bound to a subject.
AGENTIVE_NOUN_PREFIX = "ผู้"

# Thai sentence-ending boundaries (period, Thai pasuq variants, paragraph break).
SENTENCE_BOUNDARY_RX = re.compile(r"[.\n๚๛]")

# How far back to look for a subject relative to a ทรง-verb.
LOOKBACK_CHARS = 60

DECISION_DOC = "ot_register_policy_2026-05.md"


def get_thai(verse: dict) -> str:
    return verse.get("thai") or verse.get("translation", {}).get("thai") or ""


def get_kds(verse: dict) -> list[dict]:
    if isinstance(verse.get("key_decisions"), list):
        return verse["key_decisions"]
    return verse.get("translation", {}).get("key_decisions") or []


def kds_excuse(kds: list[dict]) -> bool:
    """Any rationale field hits the excuse-keyword regex?"""
    for kd in kds:
        if not isinstance(kd, dict):
            continue
        rationale = " ".join(
            str(kd.get(k, "") or "") for k in ("rationale", "reason", "text", "thai")
        )
        if EXCUSE_KEYWORDS.search(rationale):
            return True
    return False


def find_preceding_window(text: str, end: int) -> str:
    """The window of text leading up to position `end` within the same sentence.

    Trimmed at the previous sentence boundary (if any) within LOOKBACK_CHARS.
    """
    start = max(0, end - LOOKBACK_CHARS)
    window = text[start:end]
    last_boundary = -1
    for m in SENTENCE_BOUNDARY_RX.finditer(window):
        last_boundary = m.end()
    if last_boundary >= 0:
        window = window[last_boundary:]
    return window


def find_body_part_subject(window: str) -> str | None:
    """Return the rightmost body-part-of-God noun in `window`, if any."""
    rightmost = None
    rightmost_pos = -1
    for term in BODY_PARTS_OF_GOD:
        pos = window.rfind(term)
        if pos > rightmost_pos:
            rightmost_pos = pos
            rightmost = term
    return rightmost


def has_divine_or_king_subject(window: str) -> bool:
    if any(s in window for s in DIVINE_SUBJECTS):
        return True
    if any(s in window for s in KING_INDICATORS):
        return True
    return False


def check_verse(verse: dict) -> tuple[list[dict], list[dict]]:
    fails: list[dict] = []
    warns: list[dict] = []
    thai = get_thai(verse)
    if not thai:
        return (fails, warns)

    kds = get_kds(verse)
    excused = kds_excuse(kds)
    ref = verse.get("reference") or f"{verse.get('chapter','?')}:{verse.get('verse','?')}"

    for m in TRONG_VERB_RX.finditer(thai):
        # Skip "ผู้ทรง[X]" agentive-noun forms — ทรง- here is part of a divine
        # title (Almighty, Creator, etc.), not a verb prefix.
        prior = thai[max(0, m.start() - 3):m.start()]
        if prior.endswith(AGENTIVE_NOUN_PREFIX):
            continue

        verb_after_trong = m.group(1)
        verb_full = m.group(0)  # "ทรง<stem>"
        window = find_preceding_window(thai, m.start())

        body_part = find_body_part_subject(window)
        if body_part:
            # [A] HARD FAIL — body-part subject + ทรง-verb. Body-part is the
            # head of the construct chain; the verb's grammatical subject is
            # the body-part, not the divine being it possesses.
            if not excused:
                fails.append({
                    "verse": ref,
                    "kind": "BODY_PART_SUBJECT_TAKES_TRONG",
                    "body_part": body_part,
                    "verb": verb_full,
                    "context": window.strip(),
                    "thai_excerpt": thai[max(0, m.start() - 30):m.start() + 30],
                    "why": (
                        f"`{body_part}` (body-part-of-God) is the head of the "
                        f"construct chain in this clause; the verb `{verb_full}` "
                        f"binds ทรง- to the body-part as its grammatical subject. "
                        f"Rachasap rule per {DECISION_DOC} §1.2/§1.4: ทรง- attaches "
                        f"only when the verb's subject is a divine being (YHWH) or "
                        f"a recognised monarch — not to a body-part of God. "
                        f"Drop ทรง- (use the plain verb)."
                    ),
                })
            continue

        if not has_divine_or_king_subject(window):
            warns.append({
                "verse": ref,
                "kind": "TRONG_NO_VISIBLE_DIVINE_SUBJECT",
                "verb": verb_full,
                "context": window.strip(),
                "thai_excerpt": thai[max(0, m.start() - 30):m.start() + 30],
                "why": (
                    f"`{verb_full}` carries ทรง- but no divine being or recognised "
                    f"monarch appears in the preceding {LOOKBACK_CHARS} chars of "
                    f"the same sentence. The subject may be inferred from earlier "
                    f"context (legitimate Thai narrative ellipsis) — verify."
                ),
            })

    return (fails, warns)


def find_ot_chapter_files(book_filter: str | None, chapter_filter: int | None) -> list[Path]:
    files: list[Path] = []
    if not TRANSLATIONS.exists():
        return files
    for path in sorted(TRANSLATIONS.glob("*_*.json")):
        m = re.match(r"^(.+)_(\d+)\.json$", path.name)
        if not m:
            continue
        slug, ch_str = m.group(1), m.group(2)
        if slug not in OT_SLUG_TO_CODE:
            continue
        if book_filter and OT_SLUG_TO_CODE[slug] != book_filter.upper():
            continue
        if chapter_filter is not None and int(ch_str) != chapter_filter:
            continue
        files.append(path)
    return files


def write_report(slug: str, chapter: int, fails: list, warns: list) -> Path:
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / f"honorifics_binding_{slug}_{chapter:02d}.md"

    lines = [
        f"# Honorifics-binding check — {slug} ch. {chapter}",
        "",
        f"Policy: `docs/translator_decisions/{DECISION_DOC}`",
        "",
        f"- Hard fails: **{len(fails)}**",
        f"- Warnings: {len(warns)}",
        "",
    ]

    if fails:
        lines.append("## ❌ Hard fails")
        lines.append("")
        for f in fails:
            lines.append(f"### {f['verse']}  ({f['kind']})")
            lines.append(f"- body-part: `{f['body_part']}`")
            lines.append(f"- verb: `{f['verb']}`")
            lines.append(f"- excerpt: `…{f['thai_excerpt']}…`")
            lines.append(f"- why: {f['why']}")
            lines.append("")

    if warns:
        lines.append("## ⚠ Warnings")
        lines.append("")
        for w in warns:
            lines.append(
                f"- **{w['verse']}** ({w['kind']}): `{w['verb']}` — `…{w['thai_excerpt']}…`"
            )
        lines.append("")

    if not fails and not warns:
        lines.append("✅ No honorifics-binding issues found.")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main():
    parser = argparse.ArgumentParser(
        description="Honorifics-binding check — enforce ot_register_policy Rachasap rules"
    )
    parser.add_argument("--book", help="3-letter OT book code (e.g., RUT)")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--all", action="store_true",
                        help="Check all OT chapters (default if no --book)")
    parser.add_argument("--report", action="store_true",
                        help=f"Write a markdown report to {REPORTS}")
    args = parser.parse_args()

    if args.all or (not args.book and args.chapter is None):
        files = find_ot_chapter_files(None, None)
    else:
        files = find_ot_chapter_files(args.book, args.chapter)

    if not files:
        print("No OT chapter files found (or none matching filter).")
        return 0

    total_fails = 0
    total_warns = 0

    for path in files:
        m = re.match(r"^(.+)_(\d+)\.json$", path.name)
        if not m:
            continue
        slug, ch_str = m.group(1), m.group(2)
        chapter = int(ch_str)

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"⚠ {path.name} is invalid JSON — skipping")
            continue
        if not isinstance(data, list):
            continue

        chapter_fails: list[dict] = []
        chapter_warns: list[dict] = []
        for verse in data:
            f, w = check_verse(verse)
            chapter_fails.extend(f)
            chapter_warns.extend(w)

        if chapter_fails or chapter_warns:
            marker = "❌" if chapter_fails else "⚠"
            print(f"{marker} {slug}_{chapter:02d}: "
                  f"{len(chapter_fails)} fails, {len(chapter_warns)} warns")
            for f in chapter_fails:
                print(f"  ❌ {f['verse']}: {f['kind']} → "
                      f"{f['body_part']} … {f['verb']}")
        elif args.book or args.chapter is not None:
            print(f"✓ {slug}_{chapter:02d}: clean")

        if args.report and (args.book or args.chapter is not None):
            write_report(slug, chapter, chapter_fails, chapter_warns)

        total_fails += len(chapter_fails)
        total_warns += len(chapter_warns)

    if args.all or len(files) > 1:
        print()
        print(f"Total hard fails: {total_fails}")
        print(f"Total warnings: {total_warns}")

    return 1 if total_fails else 0


if __name__ == "__main__":
    sys.exit(main())
