#!/usr/bin/env bash
# Fail if any tracked file mentions private infrastructure.
#
# This repository is public and its git history is permanent. A single
# absolute path or internal module name committed here cannot be taken back
# by deleting it later. Run in CI on every push.
#
# Usage:
#   scripts/check_public_safe.sh              scan tracked files
#   scripts/check_public_safe.sh --path DIR   scan every file under DIR
#                                             (used to re-check built artifacts)
#   add --verbose to list skipped binaries
#
# The patterns live here and only here. Anything else that needs to scan for
# private infrastructure calls this script rather than restating them, so the
# scanner cannot itself become the thing that leaks the names.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

VERBOSE=0
SCAN_PATH=""
while [ $# -gt 0 ]; do
  case "$1" in
    --verbose) VERBOSE=1; shift ;;
    --path)    SCAN_PATH="${2:-}"; shift 2 ;;
    *) echo "unknown argument: $1"; exit 2 ;;
  esac
done
if [ -n "$SCAN_PATH" ] && [ ! -d "$SCAN_PATH" ]; then
  echo "ERROR: --path $SCAN_PATH is not a directory"; exit 2
fi

list_files() {
  if [ -n "$SCAN_PATH" ]; then
    find "$SCAN_PATH" -type f
  else
    git ls-files
  fi
}

# Each entry: <label>|<extended-regex>
# Keep patterns specific. A pattern that fires on ordinary prose gets ignored,
# and an ignored check is not a check.
PATTERNS=(
  "absolute home path|/(Users|home)/[a-zA-Z0-9_.-]+"
  "developer username|shukai"
  "git worktree id|\.claude/worktrees"
  "private app repo|thepapers-app"
  "private backend repo|immigration-papers-service"
  "backend prompt asset path|prompts/(niw|categories|shared|eb1a|o1a)/"
  "versioned prompt asset filename|\b(core|user|reference|research|structure|base)\.v[0-9]+\.md\b"
  "backend prompt module|(promptSpecs|taskRegistry|prefixAssets|validateAITaskRegistry|composeSystemInstruction|BaseAIService|AIRun)"
  "backend tooling command|(pm:drift|eval:niw|npm run [a-z:]*niw)"
  "prompt layer vocabulary|Layer-[0-9] (prefix|pack)"
  "internal datastore or vendor|(Firestore|Vertex AI|Cloud Run|OnePassportService)"
  # How a corpus or pack was actually assembled is internal method. What it
  # covers and what it says are public; the pipeline that produced it is not.
  "corpus build method|(crawl|scrape|download)(ed|ing)? [0-9,]+|mechanically classified|read in full|during distillation|classified for outcome"
)

# Files that legitimately contain a trigger word. Justify every entry.
is_allowlisted() {
  case "$1" in
    scripts/check_public_safe.sh) return 0 ;;  # this file defines the patterns
    *) return 1 ;;
  esac
}

fail=0
while IFS= read -r file; do
  is_allowlisted "$file" && continue
  # Skip binaries (dist archives are checked by build/package.sh before packing).
  if ! grep -Iq . "$file" 2>/dev/null; then
    [ "$VERBOSE" -eq 1 ] && echo "  skip (binary): $file"
    continue
  fi
  for entry in "${PATTERNS[@]}"; do
    label="${entry%%|*}"
    regex="${entry#*|}"
    if hits=$(grep -nEI "$regex" "$file" 2>/dev/null); then
      while IFS= read -r hit; do
        echo "LEAK  $file:${hit%%:*}  [$label]"
        echo "      ${hit#*:}" | sed 's/^[0-9]*://' | cut -c1-120
        fail=1
      done <<< "$hits"
    fi
  done
done < <(list_files)

if [ "$fail" -ne 0 ]; then
  echo
  echo "FAILED: tracked files reference private infrastructure."
  echo "This repo is public and its history is permanent. Fix before committing."
  exit 1
fi

if [ -n "$SCAN_PATH" ]; then
  echo "OK: $(list_files | wc -l | tr -d ' ') files under $SCAN_PATH, no private infrastructure referenced."
else
  echo "OK: $(list_files | wc -l | tr -d ' ') tracked files, no private infrastructure referenced."
fi
