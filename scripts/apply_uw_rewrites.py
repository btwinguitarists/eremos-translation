#!/usr/bin/env python3
"""
apply_uw_rewrites.py — apply rewritten English note fields, then re-run the
unfoldingWord wording gate on every touched chapter.

Input JSONL rows: {"file": "output/translations/acts_09.json", "verse": 5,
                   "field": "notes" | "key_decisions" | "thai_literal" | "thai_summary",
                   "index": <int or null>, "new_text": "..."}
Rules enforced here:
  - the row must address an existing verse/field
  - every Greek/Hebrew/Thai-script token present in the old text must still be
    present in the new text (no source-language tokens lost or altered)
  - after writing, check_uw_wording.py must report 0 hits for the chapter
Usage: python3 scripts/apply_uw_rewrites.py replacements.jsonl
Exit 1 if any row was rejected or a chapter still has hits.
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NONLATIN = re.compile(r"[Ͱ-Ͽἀ-῿֐-׿฀-๿]+")

rows = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
by_file = {}
for r in rows:
    by_file.setdefault(r["file"], []).append(r)

rejected = 0
for rel, rs in by_file.items():
    path = ROOT / rel
    data = json.loads(path.read_text(encoding="utf-8"))
    idx = {v["verse"]: v for v in data}
    for r in rs:
        v = idx.get(r["verse"])
        if not v:
            print(f"REJECT {rel} v{r['verse']}: no such verse"); rejected += 1; continue
        t = v["translation"]
        if r["field"] == "key_decisions":
            try:
                holder, key = t["key_decisions"][r["index"]], "rationale"
            except (IndexError, TypeError, KeyError):
                print(f"REJECT {rel} v{r['verse']}: no key_decisions[{r.get('index')}]"); rejected += 1; continue
        else:
            holder, key = t, r["field"]
        old = holder.get(key) or ""
        new = r["new_text"].strip()
        if not new:
            print(f"REJECT {rel} v{r['verse']} {r['field']}: empty"); rejected += 1; continue
        missing = [tok for tok in NONLATIN.findall(old) if tok not in new]
        if missing:
            print(f"REJECT {rel} v{r['verse']} {r['field']}: source-language tokens missing: {missing[:5]}"); rejected += 1; continue
        holder[key] = new
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

failed = 0
for rel in by_file:
    m = re.match(r"(.+)_(\d+)\.json$", Path(rel).name)
    code = subprocess.call([sys.executable, str(ROOT / "scripts" / "check_uw_wording.py"),
                            "--book", m.group(1), "--chapter", str(int(m.group(2)))])
    failed += (code != 0)
print(f"applied {len(rows) - rejected}/{len(rows)} rows; rejected {rejected}; chapters still failing: {failed}")
sys.exit(1 if (rejected or failed) else 0)
