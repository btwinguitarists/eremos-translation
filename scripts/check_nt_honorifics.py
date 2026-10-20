#!/usr/bin/env python3
"""
check_nt_honorifics.py — NT register gate: the royal verb prefix ทรง- only on
divine or royal subjects (RULES.md §3).

The OT cadence has check_honorifics_binding.py; the NT cadence had nothing,
which is how Romans 2–5 shipped with 'เราทรงถูกประกาศว่าชอบธรรม' (royal register
on the people being justified) and Hebrews 11 with ทรง on the patriarchs.

Two hard-fail classes, on the `thai` verse text:
  [A] NAMED HUMAN SUBJECT — a known human name followed, with no divine or
      royal noun in between, by a ทรง-verb within a short window.
  [B] HUMAN PASSIVE — ทรงถูก… / ทรงได้รับ… whose explicit subject just before
      it is a human noun or pronoun (เรา, ท่าน, มนุษย์, เนื้อหนัง, ทุกสิ่ง, a name…).
      (ได้รับการทรง… is the normal Thai idiom for receiving God's act and is
      not flagged.)
  [C] WARN only — ทรงถูก… / ทรงได้รับ… with no subject in reach: usually Christ
      carried over from the previous clause, occasionally a Romans 3:24.
A verse is waived when a matching key_decisions rationale contains an excuse
keyword (rachasap, royal register, honorific, intentional) AND the word
'waiver', so a deliberate exception has to be written down as one.

Usage:
  python3 scripts/check_nt_honorifics.py --book HEB --chapter 11 [--report]
  python3 scripts/check_nt_honorifics.py --all
Exit 1 on any hard fail.
"""
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANS = ROOT / "output" / "translations"
REPORTS = ROOT / "output" / "check_reports"
sys.path.insert(0, str(ROOT / "scripts"))
from run_checks import resolve_book_slug, CODE_TO_SLUG  # type: ignore

NT_SLUGS = set(CODE_TO_SLUG.values())

HUMANS = ("อับราฮัม|อิสอัค|ยาโคบ|โมเสส|โนอาห์|เอโนค|อาเบล|ซาราห์|ราหับ|กิเดโอน|บาราค|แซมสัน|เยฟธาห์|"
          "ซามูเอล|เอลียาห์|เอลีชา|อาโรน|โยเซฟ|มารีย์|มารธา|ลาซารัส|เศคาริยาห์|เอลีซาเบธ|นิโคเดมัส|"
          "เปาโล|เปโตร|ซีโมน|ยอห์น|ยากอบ|อันดรูว์|ฟีลิป|โธมัส|มัทธิว|ยูดาส|สเทเฟน|บารนาบัส|ทิโมธี|ทิตัส|"
          "สิลาส|อปอลโล|อานาเนีย|คอร์เนลิอัส|ปีลาต|กายาฟาส|อันนาส|ยอห์นผู้ให้บัพติศมา|ลูกา|มาระโก|"
          "ฟีเลโมน|โอเนสิมัส|ปริสสิลลา|อาควิลลา|ลิเดีย|โดรคัส|ทาบิธา")
DIVINE = re.compile(r"พระ|องค์|กษัตริย์|จักรพรรดิ|ซีซาร์|เฮโรด|ฟาโรห์|ดาวิด|โซโลมอน")
NAMED = re.compile(r"(?<!ของ)(?<!กับ)(?<!แก่)(?<!ต่อ)(?<!ถึง)(?<!แด่)(?<!ใน)(%s)([^ ]{0,12} ){0,3}?[^ ]{0,14}?(ก็|จึง|ได้|จะ|ยัง|ไม่|เมื่อ)?(?<!การ)(?<!ผู้)(?<!ผู้ที่)ทรง" % HUMANS)
HUMAN_SUBJ = re.compile(r"(?<!ของ)(?<!แก่)(?<!กับ)(เรา|พวกเรา|ท่าน|พวกท่าน|เขา|พวกเขา|ข้าพเจ้า|มนุษย์|เนื้อหนัง[^ ]{0,6}|ทุกสิ่ง|สิ่งสารพัด|คน[^ ]{0,8}|ผู้ใด|ใคร|%s)(จะ|ก็|ได้|จึง|ยัง|ไม่|เมื่อ)?(ทรงถูก|ทรงได้รับ)" % HUMANS)
PASSIVE = re.compile(r"ทรงถูก|ทรงได้รับ")
EXCUSE = re.compile(r"(rachasap|royal register|honorific|intentional)", re.I)


def check_chapter(slug, chapter):
    path = TRANS / f"{slug}_{chapter:02d}.json"
    if not path.exists():
        return []
    fails = []; warns = []
    for v in json.loads(path.read_text(encoding="utf-8")):
        t = v["translation"].get("thai") or ""
        waived = any(EXCUSE.search(k.get("rationale", "")) and "waiver" in k.get("rationale", "").lower()
                     for k in v["translation"].get("key_decisions") or [])
        for m in NAMED.finditer(t):
            between = t[m.start() + len(m.group(1)):m.end()]
            if DIVINE.search(between):
                continue
            fails.append((v["verse"], "A", t[max(0, m.start() - 10):m.end() + 16]))
        for m in HUMAN_SUBJ.finditer(t):
            fails.append((v["verse"], "B", t[max(0, m.start() - 10):m.end() + 16]))
        for m in PASSIVE.finditer(t):
            pre = t[max(0, m.start() - 70):m.start()]
            if DIVINE.search(pre) or HUMAN_SUBJ.search(t[max(0, m.start() - 24):m.end()]):
                continue
            warns.append((v["verse"], "C", t[max(0, m.start() - 30):m.end() + 16]))
        if waived:
            fails = [f for f in fails if f[0] != v["verse"]]
    return fails, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book"); ap.add_argument("--chapter", type=int)
    ap.add_argument("--all", action="store_true"); ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    if a.all:
        targets = []
        for p in sorted(TRANS.glob("*_[0-9][0-9].json")):
            m = re.match(r"(.+)_(\d+)$", p.stem)
            if m.group(1) in NT_SLUGS:
                targets.append((m.group(1), int(m.group(2))))
    else:
        if not (a.book and a.chapter):
            ap.error("--book and --chapter, or --all")
        targets = [(resolve_book_slug(a.book), a.chapter)]
    total = 0
    for slug, ch in targets:
        fails, warns = check_chapter(slug, ch)
        if slug not in NT_SLUGS:
            print(f"{slug} is not an NT book; use check_honorifics_binding.py"); continue
        total += len(fails)
        for verse, cls, ctx in fails:
            print(f"  ❌ [{cls}] {slug} {ch}:{verse}  …{ctx}…")
        if not a.all:
            for verse, cls, ctx in warns:
                print(f"  ⚠ [{cls}] {slug} {ch}:{verse}  …{ctx}…")
        if a.report and not a.all:
            REPORTS.mkdir(parents=True, exist_ok=True)
            out = REPORTS / f"nt_honorifics_{slug}_{ch:02d}.md"
            lines = [f"# NT honorifics check — {slug} {ch}", "",
                     "✅ clean" if not fails else f"❌ {len(fails)} royal-register violation(s)", ""]
            lines += [f"- ❌ v{verse} [{cls}]: …{ctx}…" for verse, cls, ctx in fails]
            lines += [f"- ⚠ v{verse} [{cls}] (warning, implicit subject): …{ctx}…" for verse, cls, ctx in warns]
            out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"NT honorifics: {total} hard fail(s) across {len(targets)} chapter(s)")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
