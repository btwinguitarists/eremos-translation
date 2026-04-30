#!/bin/zsh
# run_end_of_book_audit.sh — pipe the auto-generated end-of-book audit prompt
# into a fresh Claude session and produce the §2 editorial review + §3 external
# review packet (per docs/END_OF_BOOK_CHECKLIST.md).
#
# Triggered automatically: detect_book_complete.py writes
# output/.book_complete_audit_prompt.md when the last chapter of a NT book
# ships. The shell banner suggests running this script.
#
# Usage:
#   bash scripts/run_end_of_book_audit.sh <BOOK_CODE>
#   bash scripts/run_end_of_book_audit.sh JHN
#   bash scripts/run_end_of_book_audit.sh 2TH
#
# Optional flags:
#   --interactive   open Claude interactively (default)
#   --print         pipe through `claude --print` (non-interactive, for routines)
#   --dry-run       print the prompt path + a preview; do not invoke Claude
#
# Exit codes:
#   0 = audit session ran (or dry-run completed)
#   1 = no audit prompt found (last ship did not complete a book)
#   2 = invalid arguments

set -e

THAI_BIBLE_AI="$HOME/thai-bible-ai"
PROMPT_FILE="$THAI_BIBLE_AI/output/.book_complete_audit_prompt.md"

MODE="interactive"
BOOK=""
while [ $# -gt 0 ]; do
    case "$1" in
        --interactive) MODE="interactive"; shift ;;
        --print) MODE="print"; shift ;;
        --dry-run) MODE="dry-run"; shift ;;
        -h|--help)
            sed -n '2,18p' "$0"
            exit 0
            ;;
        *) BOOK="$1"; shift ;;
    esac
done

if [ -z "$BOOK" ]; then
    echo "Usage: $0 <BOOK_CODE> [--interactive|--print|--dry-run]" >&2
    echo "  e.g. $0 JHN" >&2
    exit 2
fi

if [ ! -f "$PROMPT_FILE" ]; then
    echo "✗ No audit prompt at $PROMPT_FILE" >&2
    echo "  detect_book_complete.py only writes this file when the last chapter" >&2
    echo "  of a book ships. If you want to re-run the audit for a book that" >&2
    echo "  already shipped, regenerate the prompt with:" >&2
    echo "    python3 scripts/detect_book_complete.py $BOOK \$(last chapter number)" >&2
    exit 1
fi

# Sanity check: prompt should reference the requested book. If not, the user
# probably forgot the prompt is from a previous book and would clobber outputs.
if ! grep -q "for ${BOOK} (\|(${BOOK})" "$PROMPT_FILE" 2>/dev/null; then
    echo "⚠  $PROMPT_FILE references a different book than '$BOOK'." >&2
    echo "    Inspect: head -3 '$PROMPT_FILE'" >&2
    echo "    Continue anyway? Re-run with --dry-run to see the prompt header." >&2
    exit 1
fi

cd "$THAI_BIBLE_AI"

case "$MODE" in
    dry-run)
        echo "[dry-run] Audit prompt path: $PROMPT_FILE"
        echo "[dry-run] First 30 lines:"
        echo "----"
        sed -n '1,30p' "$PROMPT_FILE"
        echo "----"
        echo "[dry-run] To run for real:"
        echo "  bash scripts/run_end_of_book_audit.sh $BOOK            # interactive"
        echo "  bash scripts/run_end_of_book_audit.sh $BOOK --print    # non-interactive"
        ;;
    print)
        echo "[run_end_of_book_audit] Piping prompt to claude --print (this may take 5-15 min)..."
        # `claude --print` returns text; the agent will use Bash/Edit/Write to
        # produce the audit docs and open a PR. We print stdout for telemetry.
        claude --print < "$PROMPT_FILE"
        ;;
    interactive)
        echo "[run_end_of_book_audit] Launching Claude interactively with the audit prompt..."
        echo "  Prompt:    $PROMPT_FILE"
        echo "  Book:      $BOOK"
        echo
        echo "  Tip: when the session ends with a PR URL, review + tag book-* before"
        echo "  resuming /loop translation."
        echo
        # Pass the prompt as the initial message; user can interact further.
        claude "$(cat "$PROMPT_FILE")"
        ;;
esac
