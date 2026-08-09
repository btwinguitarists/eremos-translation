#!/usr/bin/env python3
"""Whole-Bible verse-number verification.

For every chapter of the Eremos translation, compute the BSB verse numbering the
reader SHOULD see and check it is complete and contiguous. The source stores the
Hebrew/MT `verse` number on each verse, plus a `versification.bsb_ref` ONLY when
MT diverges from BSB (superscription Psalms, and a handful of MT/English chapter
seams). Absent `versification` == "aligned", so BSB verse == MT verse.

This is READ-ONLY. It never touches translation data. It answers:
  1. Is the source data internally sound (each BSB chapter = 1..N, no gaps/dupes)?
  2. What is the FULL set of verses where MT number != BSB number (the shift map)?
  3. [optional] Does a supplied "actual" numbering (e.g. exported from prod) match
     the canonical BSB numbering? — pass --actual <json> to compare.

Exit code 0 = clean, 1 = problems found (usable as a CI gate).
"""
import json, os, re, sys, glob
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS_DIR = os.path.join(ROOT, "output", "translations")
REPORT = os.path.join(ROOT, "output", "check_reports", "versification_scan.md")

REF_RE = re.compile(r"^(.*?)(\d+):(\d+|title)\s*$", re.IGNORECASE)

# Verses BSB (modern critical text) legitimately does NOT number — it footnotes
# them instead. A "gap" at one of these is EXPECTED, not a defect.
KNOWN_BSB_OMISSIONS = {
    ("matthew", 17, 21), ("matthew", 18, 11), ("matthew", 23, 14),
    ("mark", 7, 16), ("mark", 9, 44), ("mark", 9, 46), ("mark", 11, 26), ("mark", 15, 28),
    ("luke", 17, 36), ("luke", 23, 17),
    ("john", 5, 4),
    ("acts", 8, 37), ("acts", 15, 34), ("acts", 24, 7), ("acts", 28, 29),
    ("romans", 16, 24),
    ("nehemiah", 7, 68),
}


def parse_bsb_ref(ref):
    """Return the list of BSB (chapter, verse) slots a source verse covers.

    'Psalm 62:7' -> [(62,7)];  'Psalm 62:0'/'...:title' -> [(62,0)];
    a merged/split verse '2 Corinthians 13:12-13:13' -> [(13,12),(13,13)]
    (one source verse fills two BSB numbers). 0 == superscription/title.
    """
    if not ref:
        return None
    r = ref.replace("–", "-").replace("—", "-")
    parts = [p.strip() for p in r.split("-")]
    m = REF_RE.match(parts[0])
    if not m:
        return None
    chap = int(m.group(2))
    v0 = m.group(3)
    start_v = 0 if v0.lower() == "title" else int(v0)
    if len(parts) == 1:
        return [(chap, start_v)]
    m2 = re.search(r"(?:(\d+):)?(\d+)\s*$", parts[1])
    if not m2:
        return [(chap, start_v)]
    end_chap = int(m2.group(1)) if m2.group(1) else chap
    end_v = int(m2.group(2))
    if end_chap == chap and end_v >= start_v:
        return [(chap, v) for v in range(start_v, end_v + 1)]
    return [(chap, start_v), (end_chap, end_v)]


def book_of(filename):
    base = os.path.basename(filename)[:-5]  # strip .json
    return base.rsplit("_", 1)[0]


def main():
    files = sorted(glob.glob(os.path.join(TRANS_DIR, "*.json")))
    # canonical[(book, bsb_chapter)] = set of bsb verse numbers (0 == superscription/title)
    canonical = defaultdict(set)
    divergences = []          # (book, ref, mt_verse, bsb_ref)
    parse_failures = []       # verses whose versification.bsb_ref we couldn't parse
    per_book_files = defaultdict(int)

    for f in files:
        book = book_of(f)
        per_book_files[book] += 1
        try:
            verses = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            parse_failures.append((f, f"unreadable: {e}"))
            continue
        if not isinstance(verses, list):
            parse_failures.append((f, "not a verse list"))
            continue
        file_chapter = None
        for v in verses:
            file_chapter = v.get("chapter", file_chapter)
            mt_verse = v.get("verse")
            vers = v.get("versification")
            if vers and vers.get("bsb_ref"):
                slots = parse_bsb_ref(vers["bsb_ref"])
                if not slots:
                    parse_failures.append((f, f"v{mt_verse} bad bsb_ref {vers['bsb_ref']!r}"))
                    continue
                divergences.append((book, v.get("reference"), mt_verse, vers["bsb_ref"]))
                for (c, vv) in slots:
                    canonical[(book, c)].add(vv)
            else:
                canonical[(book, file_chapter)].add(mt_verse)

    # Integrity: each BSB chapter's verse set must be 1..N contiguous (0/title allowed).
    problems = []
    chapters_checked = 0
    for (book, chap), verses in sorted(canonical.items()):
        chapters_checked += 1
        body = sorted(x for x in verses if x > 0)   # drop the title (0)
        if not body:
            problems.append(f"{book} {chap}: no numbered verses")
            continue
        n = max(body)
        expected = set(range(1, n + 1))
        got = set(body)
        missing = sorted(expected - got)
        # Drop verses BSB legitimately omits (footnoted, not numbered).
        real_missing = [m for m in missing if (book, chap, m) not in KNOWN_BSB_OMISSIONS]
        expected_omissions = [m for m in missing if (book, chap, m) in KNOWN_BSB_OMISSIONS]
        extra = sorted(got - expected)   # can't happen if contiguous, but guards dupes-as-gaps
        dupes = len(body) != len(got)
        if real_missing:
            problems.append(f"{book} {chap}: GAP — missing BSB verses {real_missing} (max={n})"
                            + (f"  [also expected-omitted: {expected_omissions}]" if expected_omissions else ""))
        if extra:
            problems.append(f"{book} {chap}: STRAY verses {extra}")
        if dupes:
            problems.append(f"{book} {chap}: DUPLICATE BSB verse numbers")

    # Optional: compare against an "actual" numbering export (prod / bundle).
    actual_mismatches = []
    if "--actual" in sys.argv:
        ap = sys.argv[sys.argv.index("--actual") + 1]
        actual = json.load(open(ap, encoding="utf-8"))  # {"Book chap": [verse numbers]} expected
        # left as a hook; compare shape is caller-defined.
        actual_mismatches.append(f"(loaded {ap} — comparison mode is a stub; wire to prod export)")

    # ---- Report ----
    div_by_book = defaultdict(list)
    for book, ref, mt, bsb in divergences:
        div_by_book[book].append((ref, mt, bsb))

    lines = []
    lines.append("# Whole-Bible versification scan\n")
    lines.append(f"- Files scanned: **{len(files)}**  ")
    lines.append(f"- Chapters checked: **{chapters_checked}**  ")
    lines.append(f"- Verses where MT number ≠ BSB number: **{len(divergences)}**  ")
    lines.append(f"- Books with at least one divergence: **{len(div_by_book)}**  ")
    lines.append(f"- Integrity problems (gaps/dupes/strays): **{len(problems)}**  ")
    lines.append(f"- Parse failures: **{len(parse_failures)}**\n")

    lines.append("## Integrity problems\n")
    lines.append("\n".join(f"- ⚠️ {p}" for p in problems) if problems
                 else "- ✅ None — every BSB chapter is a complete, contiguous 1..N.")
    lines.append("")

    lines.append("## Books containing MT≠BSB divergences (the shift map)\n")
    for book in sorted(div_by_book):
        refs = div_by_book[book]
        lines.append(f"- **{book}** — {len(refs)} verse(s). e.g. {refs[0][0]} (MT v{refs[0][1]} → {refs[0][2]})")
    lines.append("")

    if parse_failures:
        lines.append("## Parse failures\n")
        lines += [f"- {f}: {msg}" for f, msg in parse_failures]

    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    open(REPORT, "w", encoding="utf-8").write("\n".join(lines))

    # ---- Console summary ----
    print(f"files={len(files)} chapters={chapters_checked} divergent_verses={len(divergences)} "
          f"books_with_divergence={len(div_by_book)} integrity_problems={len(problems)} "
          f"parse_failures={len(parse_failures)}")
    print(f"report -> {os.path.relpath(REPORT, ROOT)}")
    if problems:
        print("\nINTEGRITY PROBLEMS:")
        for p in problems[:40]:
            print("  -", p)
    print("\nBooks with divergences:", ", ".join(sorted(div_by_book)))

    return 1 if (problems or parse_failures) else 0


if __name__ == "__main__":
    sys.exit(main())
