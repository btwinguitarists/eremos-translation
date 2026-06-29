#!/usr/bin/env python3
"""
Cross-book audit loop — deterministic driver.

This script is the BACKBONE the audit loop calls. It does the mechanical parts
(queue, ledger, de-dup, verse fetch) so the loop agent only has to do judgment.
It NEVER edits translations. See docs/CROSSBOOK_AUDIT_CHARTER.md.

Subcommands:
  build-queue   Parse the sweep tables + worklist → docs/end_of_book/_audits/crossbook_queue.json
  next          Print the next pending unit (highest priority) + its shipped Thai/Hebrew
                + de-dup matches from the 372 live review questions and decision docs.
                --theme T2  --book JER  to target;  --json for machine output.
  mark ID STATUS [--pr N] [--note ...]   Update one unit's status in the ledger.
  status        Counts by theme / priority / status.

Usage:
  python3 scripts/crossbook_audit.py build-queue
  python3 scripts/crossbook_audit.py next
  python3 scripts/crossbook_audit.py mark GEN-T8-001 proposed --pr 210
  python3 scripts/crossbook_audit.py status
"""
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EOB = ROOT / "docs" / "end_of_book"
AUDITS = EOB / "_audits"
SWEEP = AUDITS / "crossbook_sweep_2026-06-27.md"
WORKLIST = ROOT / "docs" / "WHOLE_BIBLE_CROSSBOOK_AUDIT_2026-06-27.md"
QUEUE = AUDITS / "crossbook_queue.json"
TRANSLATIONS = ROOT / "output" / "translations"
DECISIONS = ROOT / "docs" / "decisions"
REVIEW_Q = Path.home() / "EremosVercel2" / "shared" / "review-questions"

sys.path.insert(0, str(ROOT / "scripts"))
try:
    from build_external_review_packet import BOOKS  # CODE -> (slug, name)
except Exception:
    BOOKS = {}

# ---- book-name normalization (sweep uses "Genesis", "1 Samuel", "2KI", "ISA", ...) ----
NAME2CODE, SLUG2CODE = {}, {}
for _code, (_slug, _name) in BOOKS.items():
    NAME2CODE[_name.lower()] = _code
    SLUG2CODE[_slug.lower()] = _code
# a few extra spellings the sweep uses
EXTRA = {"song of songs": "SNG", "songofsongs": "SNG"}
NAME2CODE.update(EXTRA)


def to_code(book_cell: str):
    b = book_cell.strip()
    if b.upper() in BOOKS:
        return b.upper()
    low = b.lower()
    if low in NAME2CODE:
        return NAME2CODE[low]
    if low in SLUG2CODE:
        return SLUG2CODE[low]
    # leading token like "JOS 9:1" or "1 Samuel"
    m = re.match(r"^(\d?\s?[A-Za-z]+)", b)
    if m:
        t = m.group(1).strip().lower()
        if t in NAME2CODE:
            return NAME2CODE[t]
        if t.upper() in BOOKS:
            return t.upper()
    return None


# ---- disposition → open/closed + priority ----
CLOSED = ("LOCKED", "RESOLVED", "APPLIED", "MOOT", "NO ACTION")
HIGH = ("DECIDE", "REQUIRES SIGN-OFF", "SIGN-OFF", "MAJOR", "CRITICAL", "PROPOSED", "DIVERGENT")
MED = ("REVIEW", "NORMALIZE", "ADD FOOTERS", "ADD TIER", "WIDEN", "RETROFIT", "DOC ROW", "PARTIAL", "PROVISIONAL")


def classify(disp: str):
    d = disp.upper()
    if any(k in d for k in CLOSED) and not any(k in d for k in ("SIGN-OFF", "DECIDE", "PROPOSED")):
        # LOCKED/RESOLVED/etc. — closed for de-dup reference, unless it also carries an open verb
        return "closed", 9
    if any(k in d for k in HIGH):
        return "pending", 1
    if any(k in d for k in MED):
        return "pending", 2
    if "STABLE" in d:
        return "pending", 3  # usually "recommend a doc" — low priority, still real
    return "pending", 2


def parse_themes(theme_cell: str):
    ts = re.findall(r"T\d", theme_cell)
    return ts or ["T?"]


def parse_refs(ref_cell: str):
    return re.findall(r"\d+:\d+", ref_cell)


def slugify_issue(issue: str, n=4):
    words = re.findall(r"[A-Za-z]+", issue)
    return "-".join(words[:n]).lower() or "item"


# ---- markdown table row parser ----
def iter_table_rows(md_path: Path):
    if not md_path.exists():
        return
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        if cells[0] in ("Book", "") or set(cells[0]) <= set("-: "):
            continue
        yield cells[:5]  # Book, Ref, Theme, Issue, Disposition


def build_queue():
    items, counter = [], {}
    for cells in iter_table_rows(SWEEP):
        book_cell, ref_cell, theme_cell, issue, disp = cells
        code = to_code(book_cell)
        if not code:
            continue
        themes = parse_themes(theme_cell)
        primary_theme = themes[0]
        status, prio = classify(disp)
        key = f"{code}-{primary_theme}"
        counter[key] = counter.get(key, 0) + 1
        item_id = f"{code}-{primary_theme}-{counter[key]:03d}"
        items.append({
            "id": item_id,
            "book": code,
            "themes": themes,
            "refs": parse_refs(ref_cell),
            "ref_raw": ref_cell,
            "issue": issue,
            "disposition": disp,
            "status": status,        # pending | closed (closed = de-dup reference only)
            "priority": prio,        # 1 high, 2 med, 3 low, 9 closed
            "source": "sweep",
        })
    # preserve prior ledger statuses if a queue already exists (don't clobber progress)
    if QUEUE.exists():
        old = {x["id"]: x for x in json.loads(QUEUE.read_text())}
        for it in items:
            o = old.get(it["id"])
            if o and o.get("status") not in (None, "pending", "closed"):
                it["status"] = o["status"]
                it["pr"] = o.get("pr")
                it["note"] = o.get("note")
    AUDITS.mkdir(parents=True, exist_ok=True)
    QUEUE.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    pend = sum(1 for x in items if x["status"] == "pending")
    closed = sum(1 for x in items if x["status"] == "closed")
    print(f"Queue built: {len(items)} items ({pend} pending, {closed} closed/de-dup) -> {QUEUE.relative_to(ROOT)}")


def load_queue():
    if not QUEUE.exists():
        sys.exit("No queue. Run: python3 scripts/crossbook_audit.py build-queue")
    return json.loads(QUEUE.read_text())


def fetch_verses(code, refs, limit=4):
    out = []
    if code not in BOOKS:
        return out
    slug = BOOKS[code][0]
    for ref in refs[:limit]:
        ch, vs = ref.split(":")
        f = TRANSLATIONS / f"{slug}_{int(ch):02d}.json"
        if not f.exists():
            continue
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for v in data:
            if str(v.get("chapter")) == ch and str(v.get("verse")) == vs:
                tr = v.get("translation", {}) if isinstance(v.get("translation"), dict) else {}
                out.append({
                    "ref": f"{BOOKS[code][1]} {ref}",
                    "thai": tr.get("thai", v.get("thai", "")),
                    "hebrew": (v.get("hebrew") or "")[:200],
                    "bsb": v.get("bsb_english", ""),
                })
                break
    return out


THEME_KW = {
    "T1": ["anthropo", "hand", "arm", "พระหัตถ์", "พระกร", "body"],
    "T2": ["mal", "messenger", "angel", "ทูต"],
    "T3": ["adonai", "divine", "lord", "เจ้านาย"],
    "T4": ["lxx", "mt", "variant", "textual", "ketiv", "qere"],
    "T5": ["nt", "citation", "quoted", "cross", "seam"],
    "T6": ["pagan", "king", "register", "royal", "monarch", "ราชาศัพท์"],
    "T7": ["parallel", "harmoniz", "chronicle"],
    "T8": ["leitwort", "term", "register", "note", "messianic", "chesed", "redeemer"],
}


def dedup_matches(item, limit=6):
    """Find live review questions + decision docs that may already cover this item."""
    code, themes = item["book"], item["themes"]
    kws = set()
    for t in themes:
        kws.update(THEME_KW.get(t, []))
    matches = []
    # 1) live review questions (372 .yml) — match by book code in id OR theme kw in id/topic
    if REVIEW_Q.exists():
        for f in sorted(REVIEW_Q.glob("*.yml")):
            name = f.name.lower()
            txt = ""
            hit_book = f"_{code.lower()}_" in name or name.startswith(f"a_{code.lower()}_")
            try:
                txt = f.read_text(encoding="utf-8")[:1200].lower()
            except Exception:
                pass
            hit_kw = any(k.lower() in name or k.lower() in txt for k in kws)
            if hit_book and hit_kw:
                matches.append(("review-question", f.name))
    # 2) decision docs
    if DECISIONS.exists():
        for f in sorted(DECISIONS.glob("*.md")):
            if any(k.lower() in f.name.lower() for k in kws):
                matches.append(("decision-doc", f.relative_to(ROOT).as_posix()))
    return matches[:limit]


def cmd_next(args):
    q = load_queue()
    pend = [x for x in q if x["status"] == "pending"]
    if args.theme:
        pend = [x for x in pend if args.theme.upper() in x["themes"]]
    if args.book:
        pend = [x for x in pend if x["book"] == args.book.upper()]
    if not pend:
        print("No pending units" + (f" for filter" if (args.theme or args.book) else "") + ". Queue may be clear.")
        return
    pend.sort(key=lambda x: (x["priority"], x["id"]))
    it = pend[0]
    it["_verses"] = fetch_verses(it["book"], it["refs"])
    it["_dedup"] = dedup_matches(it)
    if args.json:
        print(json.dumps(it, ensure_ascii=False, indent=2))
        return
    print(f"=== NEXT UNIT: {it['id']}  (priority {it['priority']}) ===")
    print(f"Book: {it['book']}  Themes: {', '.join(it['themes'])}")
    print(f"Refs: {it['ref_raw']}")
    print(f"Issue: {it['issue']}")
    print(f"Disposition (from sweep): {it['disposition']}")
    print(f"\n-- shipped text for refs --")
    for v in it["_verses"]:
        print(f"  {v['ref']}")
        print(f"    TH: {v['thai'][:160]}")
        if v["hebrew"]:
            print(f"    HE: {v['hebrew'][:80]}")
    if not it["_verses"]:
        print("  (no verse text auto-loaded — read the files for this ref manually)")
    print(f"\n-- de-dup: already-covered? CHECK before emitting --")
    if it["_dedup"]:
        for kind, ref in it["_dedup"]:
            print(f"  [{kind}] {ref}")
    else:
        print("  (no existing question/decision matched by book+theme — likely genuinely new)")
    print(f"\nReminder: follow docs/CROSSBOOK_AUDIT_CHARTER.md — default to NOT flagging; "
          f"conformance only vs a LOCKED policy; everything is a PROPOSAL behind Ben's gate.")


def cmd_mark(args):
    q = load_queue()
    found = False
    for it in q:
        if it["id"] == args.id:
            it["status"] = args.status
            if args.pr:
                it["pr"] = args.pr
            if args.note:
                it["note"] = args.note
            found = True
            break
    if not found:
        sys.exit(f"id not found: {args.id}")
    QUEUE.write_text(json.dumps(q, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{args.id} -> {args.status}" + (f" (PR #{args.pr})" if args.pr else ""))


def cmd_status(args):
    q = load_queue()
    by_status, by_theme, by_prio = {}, {}, {}
    for it in q:
        by_status[it["status"]] = by_status.get(it["status"], 0) + 1
        if it["status"] == "pending":
            by_prio[it["priority"]] = by_prio.get(it["priority"], 0) + 1
            for t in it["themes"]:
                by_theme[t] = by_theme.get(t, 0) + 1
    print(f"Total units: {len(q)}")
    print("By status: " + ", ".join(f"{k}={v}" for k, v in sorted(by_status.items())))
    print("Pending by priority: " + ", ".join(f"P{k}={v}" for k, v in sorted(by_prio.items())))
    print("Pending by theme:    " + ", ".join(f"{k}={v}" for k, v in sorted(by_theme.items())))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build-queue")
    n = sub.add_parser("next")
    n.add_argument("--theme"); n.add_argument("--book"); n.add_argument("--json", action="store_true")
    m = sub.add_parser("mark")
    m.add_argument("id"); m.add_argument("status")
    m.add_argument("--pr", type=int); m.add_argument("--note")
    sub.add_parser("status")
    a = ap.parse_args()
    if a.cmd == "build-queue": build_queue()
    elif a.cmd == "next": cmd_next(a)
    elif a.cmd == "mark": cmd_mark(a)
    elif a.cmd == "status": cmd_status(a)


if __name__ == "__main__":
    main()
