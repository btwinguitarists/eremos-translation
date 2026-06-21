#!/usr/bin/env python3
"""
Run end-of-book external AI review for every PENDING book via the Gemini API —
no browser, no Cowork. Sends each book's review packet to Gemini and saves the
reply as the book's response file (which marks it done for external_review_status).

Uses gemini-2.5-flash by default (the free-tier model that's reachable; 2.5-pro
is often quota-blocked). Flash is an independent model from Claude (which did the
translation), so it satisfies the "independent eyes" point of the §3 review.

Usage:
  python3 scripts/run_book_review_gemini.py [CODE ...] [--model NAME]
  (no CODE args = every pending book in the queue)

Requires GEMINI_API_KEY in the environment.
"""
import argparse, json, os, sys, time, urllib.request, urllib.error
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EOB = ROOT / "docs" / "end_of_book"
sys.path.insert(0, str(ROOT / "scripts"))
from build_external_review_packet import BOOKS  # CODE -> (slug, name)


def newest_packet(slug):
    pk = sorted((EOB / slug).glob("external_review_packet_*.md"))
    return pk[-1] if pk else None


def has_response(slug):
    return any("response" in p.name.lower() for p in (EOB / slug).glob("*.md"))


def pending_codes():
    out = []
    for code, (slug, _name) in BOOKS.items():
        if (EOB / slug).is_dir() and newest_packet(slug) and not has_response(slug):
            out.append(code)
    return out


def call_gemini(packet_text, model, key, timeout=240):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    body = {
        "contents": [{"parts": [{"text": packet_text}]}],
        "generationConfig": {"maxOutputTokens": 32768, "temperature": 0.4},
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        p = json.loads(r.read().decode())
    cand = (p.get("candidates") or [{}])[0]
    txt = "".join(part.get("text", "") for part in cand.get("content", {}).get("parts", []))
    return txt.strip(), cand.get("finishReason", "?")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("codes", nargs="*")
    ap.add_argument("--model", default="gemini-2.5-flash")
    a = ap.parse_args()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("GEMINI_API_KEY not set.")
    codes = [c.upper() for c in a.codes] or pending_codes()
    if not codes:
        print("No pending books. Backlog clear.")
        return
    today = date.today().isoformat()
    print(f"Reviewing {len(codes)} book(s) with {a.model}: {', '.join(codes)}\n")
    done, failed = [], []
    for i, code in enumerate(codes):
        slug, name = BOOKS[code]
        pkt = newest_packet(slug)
        if not pkt:
            print(f"  ! {code}: no packet — skip"); failed.append(code); continue
        packet_text = pkt.read_text()
        try:
            reply, finish = call_gemini(packet_text, a.model, key)
        except urllib.error.HTTPError as e:
            print(f"  ✗ {code}: HTTP {e.code} {e.read().decode()[:80]}"); failed.append(code); continue
        except Exception as e:
            print(f"  ✗ {code}: {type(e).__name__} {str(e)[:80]}"); failed.append(code); continue
        if not reply:
            print(f"  ✗ {code}: empty reply (finish={finish})"); failed.append(code); continue
        out = EOB / slug / f"external_review_response_{code}_{today}.md"
        header = (f"# {name} ({code}) — external AI review response\n\n"
                  f"**Reviewer:** {a.model} (Gemini API, independent of the translating model)\n"
                  f"**Date:** {today}  |  **Packet:** `{pkt.relative_to(ROOT)}`  |  finishReason: {finish}\n\n"
                  f"> Auto-run via scripts/run_book_review_gemini.py. The main session reads this and "
                  f"decides what to act on; nothing is auto-applied to the translation.\n\n---\n\n")
        out.write_text(header + reply + "\n")
        trunc = " (TRUNCATED — MAX_TOKENS)" if finish == "MAX_TOKENS" else ""
        print(f"  ✓ {code}: {len(reply):,} chars -> {out.relative_to(ROOT)}{trunc}")
        done.append(code)
        if i < len(codes) - 1:
            time.sleep(5)  # be gentle on free-tier RPM
    print(f"\nDone: {len(done)} ({', '.join(done) or '-'}) | Failed: {len(failed)} ({', '.join(failed) or '-'})")


if __name__ == "__main__":
    main()
