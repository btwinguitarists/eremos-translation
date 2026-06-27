#!/usr/bin/env bash
# Clear the end-of-book external-review queue via the Gemini API (no browser).
# Reviews every PENDING book (those with a packet but no response file) and
# writes external_review_response_<CODE>_<date>.md for each.
#
# Schedule this (see scripts/com.eremos.external-review.plist) so the backlog
# self-clears. Reads the API key from ~/thai-bible-ai/.review.env if present
# (a gitignored file you create with:  export GEMINI_API_KEY=...   and,
# optionally, export XAI_API_KEY=...). Falls back to the inherited environment.
set -euo pipefail

REPO="$HOME/thai-bible-ai"
cd "$REPO"

# Load secrets from a gitignored env file if you keep one there.
if [ -f "$REPO/.review.env" ]; then
  set -a
  # shellcheck disable=SC1091
  . "$REPO/.review.env"
  set +a
fi

LOG="$REPO/output/review_cron.log"
mkdir -p "$(dirname "$LOG")"

{
  echo "===== $(date '+%Y-%m-%d %H:%M:%S') ====="
  if [ -z "${GEMINI_API_KEY:-}" ]; then
    echo "GEMINI_API_KEY not set (put it in $REPO/.review.env). Skipping."
    exit 0
  fi
  python3 scripts/run_book_review_gemini.py
  echo
} >> "$LOG" 2>&1
