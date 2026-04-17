#!/usr/bin/env python3
"""One-time: add Mark 9:12 OT citation (caught by claim-consistency check)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "nt_ot_citations.json"

ENTRY = {
    "MRK 9:12": {
        "type": "composite_allusion",
        "sources": ["ISA 53:3", "PSA 22:6"],
        "greek_matches": "LXX-echo",
        "notes": "Jesus's question about the Son of Man being 'treated with contempt' (ἐξουδενηθῇ, hapax in Mark) echoes the Suffering-Servant rejection language of Isa 53:3 LXX and Ps 22:6 LXX (related form ἐξουθενέω). The Suffering-Servant and Suffering-Son-of-Man strands are here fused, preparing the Passion narrative. Jesus's reply holds the Elijah-prophecy AND the suffering-Son-of-Man in tension — both are 'written,' so there is no dilemma, only a sequence.",
    },
}


def main():
    db = json.loads(DB_PATH.read_text(encoding="utf-8"))
    citations = db["citations"]
    for key, entry in ENTRY.items():
        if key in citations:
            print(f"skip: {key} already present")
            continue
        citations[key] = entry
        print(f"added: {key}")

    def sk(k):
        b, r = k.split(" ")
        c, v = r.split(":")
        return (b, int(c), int(v))

    db["citations"] = {k: citations[k] for k in sorted(citations.keys(), key=sk)}
    DB_PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Total citations now: {len(db['citations'])}")


if __name__ == "__main__":
    main()
