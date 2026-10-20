#!/usr/bin/env python3
"""
check_uw_wording.py — license gate: no unfoldingWord wording in our CC0 output.

unfoldingWord Translation Notes are CC BY-SA 4.0. They are fetched into
output/uw_notes/<slug>_<NN>.md for context only; copying their wording into our
notes/rationales would make those fields share-alike, breaking the CC0 claim.

This check tokenizes every English free-text field in a chapter's translation
JSON (`notes`, `key_decisions[].rationale`, and `thai_literal`/`thai_summary` if
they contain Latin text) and fails if any field shares N (default 8) or more
consecutive normalized words with the chapter's uW note file, or with the uW
book introduction (<slug>_FRONT.md).

Usage:
  python3 scripts/check_uw_wording.py --book ROM --chapter 3 [--report]
  python3 scripts/check_uw_wording.py --all [--json queue.jsonl]   # whole corpus
Exit 1 on any hit (ship-blocking).
"""
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANS = ROOT / "output" / "translations"
UW = ROOT / "output" / "uw_notes"
REPORTS = ROOT / "output" / "check_reports"
sys.path.insert(0, str(ROOT / "scripts"))
try:
    from run_checks import resolve_book_slug as resolve_book  # type: ignore
except Exception:
    resolve_book = None

N_DEFAULT = 8
WORD = re.compile(r"[a-z0-9']+")


def norm_words(text: str):
    t = text.lower()
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)   # markdown links -> label
    t = t.replace("’", "'").replace("‘", "'")
    return WORD.findall(t)


def prose(gram):
    """A shingle counts only if most of its words are real words, so bare
    verse-reference lists (6:7, 9:31, 12:24, ...) do not trip the gate."""
    return sum(1 for w in gram if re.search(r"[a-z]", w)) >= (len(gram) + 1) // 2 + 1


def shingles(words, n):
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1) if prose(words[i:i + n])}


def uw_shingles(slug: str, chapter: int, n: int):
    files = [UW / f"{slug}_{chapter:02d}.md", UW / f"{slug}_FRONT.md"]  # chapter notes + book intro
    out = set()
    for f in files:
        if f.exists():
            out |= shingles(norm_words(f.read_text(encoding="utf-8")), n)
    return out


def english_fields(verse: dict):
    t = verse.get("translation") or {}
    v = verse.get("verse")
    if t.get("notes"):
        yield (v, "notes", None, t["notes"])
    for i, kd in enumerate(t.get("key_decisions") or []):
        if kd.get("rationale"):
            yield (v, "key_decisions", i, kd["rationale"])
    for k in ("thai_literal", "thai_summary"):
        s = t.get(k)
        if s and re.search(r"[A-Za-z]{4,}", s):
            yield (v, k, None, s)


def longest_run(words, uw, n):
    """Return (start, length) of the longest run of words whose every n-gram is in uw."""
    best = (0, 0); i = 0
    while i <= len(words) - n:
        if tuple(words[i:i + n]) in uw and prose(words[i:i + n]):
            j = i
            while j + n <= len(words) and tuple(words[j:j + n]) in uw and prose(words[j:j + n]):
                j += 1
            run = j - i + n - 1
            if run > best[1]:
                best = (i, run)
            i = j
        else:
            i += 1
    return best


def check_chapter(slug: str, chapter: int, n: int):
    path = TRANS / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return []
    uw = uw_shingles(slug, chapter, n)
    if not uw:
        return []
    hits = []
    for verse in json.loads(path.read_text(encoding="utf-8")):
        for v, field, idx, text in english_fields(verse):
            words = norm_words(text)
            start, run = longest_run(words, uw, n)
            if run >= n:
                hits.append({"file": str(path.relative_to(ROOT)), "slug": slug, "chapter": chapter,
                             "verse": v, "field": field, "index": idx,
                             "overlap_words": run, "overlap": " ".join(words[start:start + run]),
                             "text": text})
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book"); ap.add_argument("--chapter", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--ngram", type=int, default=N_DEFAULT)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--json", help="write hits as JSONL to this path")
    a = ap.parse_args()

    if a.all:
        targets = []
        for p in sorted(TRANS.glob("*_[0-9][0-9][0-9].json")) + sorted(TRANS.glob("*_[0-9][0-9].json")):
            m = re.match(r"(.+)_(\d+)$", p.stem)
            targets.append((m.group(1), int(m.group(2))))
    else:
        if not (a.book and a.chapter):
            ap.error("--book and --chapter, or --all")
        slug = resolve_book(a.book) if resolve_book else a.book.lower()
        targets = [(slug, a.chapter)]

    hits = []
    for slug, ch in targets:
        hits.extend(check_chapter(slug, ch, a.ngram))

    chapters = sorted({(h["slug"], h["chapter"]) for h in hits})
    print(f"uW wording check: {len(hits)} field(s) in {len(chapters)} chapter(s) share "
          f"{a.ngram}+ consecutive words with unfoldingWord notes")
    for h in hits[:40]:
        print(f"  {h['slug']} {h['chapter']}:{h['verse']} {h['field']}"
              f"{'' if h['index'] is None else '['+str(h['index'])+']'} ({h['overlap_words']} words): "
              f"\"{h['overlap'][:90]}\"")
    if len(hits) > 40:
        print(f"  ... {len(hits) - 40} more")

    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            for h in hits:
                f.write(json.dumps(h, ensure_ascii=False) + "\n")
    if a.report and not a.all:
        slug, ch = targets[0]
        REPORTS.mkdir(parents=True, exist_ok=True)
        out = REPORTS / f"uw_wording_{slug}_{ch:02d}.md"
        lines = [f"# unfoldingWord wording check — {slug} {ch}", "",
                 "✅ clean" if not hits else f"❌ {len(hits)} field(s) reuse uW wording ({a.ngram}+ consecutive words)", ""]
        for h in hits:
            lines.append(f"- v{h['verse']} `{h['field']}`{'' if h['index'] is None else '['+str(h['index'])+']'} "
                         f"({h['overlap_words']} words): \"{h['overlap']}\"")
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
