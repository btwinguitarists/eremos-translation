#!/usr/bin/env python3
"""
Tiny Gemini second-opinion helper for the cross-book audit loop.

Sends a single prompt to gemini-2.5-flash (the free-tier model that works) and
prints the reply. Used in the funnel's self-check stage to get an INDEPENDENT
read on a candidate finding before it becomes a fix. Two-model agreement →
confident; disagreement → route as a question, never an auto-fix.

Usage:
  python3 scripts/ask_gemini.py "Is rendering X for Hebrew Y a real inconsistency or legit variation? Default: not a problem."
  echo "long prompt..." | python3 scripts/ask_gemini.py -
Requires GEMINI_API_KEY.
"""
import json, os, sys, urllib.request, urllib.error

MODEL = "gemini-2.5-flash"


def ask(prompt, timeout=120):
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("GEMINI_API_KEY not set.")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={key}"
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": 2048, "temperature": 0.3}}
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        p = json.loads(r.read().decode())
    cand = (p.get("candidates") or [{}])[0]
    return "".join(part.get("text", "") for part in cand.get("content", {}).get("parts", [])).strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: ask_gemini.py 'prompt'  (or '-' to read stdin)")
    prompt = sys.stdin.read() if sys.argv[1] == "-" else " ".join(sys.argv[1:])
    try:
        print(ask(prompt))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:200]}")
