#!/usr/bin/env bash
# Exercise every bundled skill script against a known-bad and a known-good
# fixture. A validator that cannot fail provides no guarantee, so each script
# must exit non-zero on the broken case and zero on the clean one.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

LIB=skill-lib
BROKEN=tests/fixtures/broken-case
CLEAN=tests/fixtures/clean-case

fails=0

expect() {
  local want="$1" label="$2"; shift 2
  local out; out="$("$@" 2>&1)"; local got=$?
  if [ "$got" -ne "$want" ]; then
    echo "FAIL  $label: expected exit $want, got $got"
    echo "$out" | sed 's/^/      /'
    fails=$((fails + 1))
  else
    echo "ok    $label (exit $got)"
  fi
}

echo "== broken fixture: every script must object =="
expect 1 "check_manifest flags NOT FILED citation and unknown id" \
  python3 "$LIB/check_manifest.py" "$BROKEN/manifest.md" "$BROKEN/review.md"
expect 1 "verify_quotes flags a non-verbatim excerpt" \
  python3 "$LIB/verify_quotes.py" "$BROKEN/review.md" "$BROKEN"
expect 1 "filing_date_guard flags post-filing evidence and re-scoping" \
  python3 "$LIB/filing_date_guard.py" "$BROKEN/CASE.md" "$BROKEN/review.md"

echo
echo "== clean fixture: every script must pass =="
expect 0 "check_manifest accepts a well-formed manifest" \
  python3 "$LIB/check_manifest.py" "$CLEAN/manifest.md" "$CLEAN/review.md"
expect 0 "verify_quotes accepts a verbatim excerpt" \
  python3 "$LIB/verify_quotes.py" "$CLEAN/review.md" "$CLEAN"
expect 0 "filing_date_guard is inert before filing" \
  python3 "$LIB/filing_date_guard.py" "$CLEAN/CASE.md" "$CLEAN/review.md"

echo
if [ "$fails" -ne 0 ]; then
  echo "FAILED: $fails script check(s) did not behave as specified."
  exit 1
fi
echo "OK: all bundled validators behave as specified."
