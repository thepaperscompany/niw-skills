#!/usr/bin/env bash
# Fail on claims this project must not make in public materials.
#
# Three categories, each for a specific reason:
#
#   1. Claims that counsel reviewed or signed off on this repository. Whether
#      or not such a review happened, publishing the claim invites reliance on
#      it and turns a maintenance question into a liability question.
#   2. Claims that output is lawyer-quality, attorney-grade or equivalent to a
#      licensed professional's work. Unverifiable, and it edges toward the
#      unauthorized practice of law. Describe the method, not the output tier.
#   3. Price comparisons against hiring an attorney, and any guarantee of
#      approval. Adjudication is discretionary; competing on price frames the
#      product against counsel rather than alongside it.
#
# Telling a user to consult their own attorney is not a claim and is expected.
#
# Usage: scripts/check_claims.sh

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

PATTERNS=(
  "claim of counsel review|(attorney|legal|counsel)[ -](sign-?off|reviewed)|reviewed by (a )?(licensed|immigration|U\.S\.) (immigration )?(attorney|counsel)|counsel before release"
  "lawyer-quality claim|(lawyer|attorney)-(quality|grade|equivalent|level)|as good as (a|an) (lawyer|attorney)|replaces? (a|an|your) (lawyer|attorney)"
  "price comparison|\\\$[0-9],?[0-9]{3}[^.]{0,40}(attorney|lawyer|counsel)|(attorney|lawyer|counsel)[^.]{0,40}\\\$[0-9],?[0-9]{3}|cheaper than (a|an|hiring)"
  "approval guarantee|guarantee[sd]? (approval|success|a green card)|will be approved|ensures? approval"
)

is_allowlisted() {
  case "$1" in
    scripts/check_claims.sh) return 0 ;;  # this file defines the patterns
    */evals/*/graders/*)     return 0 ;;  # graders list forbidden phrases by design
    *) return 1 ;;
  esac
}

# A claim stated in order to deny or forbid it is not a claim. Without this,
# "is not guaranteed approval" trips the guarantee pattern, and the checker
# gets ignored, which makes it useless.
NEGATION='(not|never|no|cannot|can not|without|refus|prohibit|forbid|avoid|do not|does not|don.t|neither|nor) '
looks_negated() {
  echo "$1" | grep -qEi "${NEGATION}[^.]{0,60}(guarantee|approv|lawyer|attorney|sign-?off|review)" && return 0
  echo "$1" | grep -qEi "(guarantee|approv|lawyer|attorney|sign-?off|review)[a-z]*[^.]{0,40} (is|are|was|were) not " && return 0
  return 1
}

fail=0
while IFS= read -r file; do
  is_allowlisted "$file" && continue
  case "$file" in *.md|*.json|NOTICE|LICENSE) ;; *) continue ;; esac
  grep -Iq . "$file" 2>/dev/null || continue
  for entry in "${PATTERNS[@]}"; do
    label="${entry%%|*}"
    regex="${entry#*|}"
    if hits=$(grep -nEI -i "$regex" "$file" 2>/dev/null); then
      while IFS= read -r hit; do
        line="$(echo "${hit#*:}" | sed 's/^[0-9]*://')"
        if looks_negated "$line"; then continue; fi
        echo "CLAIM  $file:${hit%%:*}  [$label]"
        echo "       $(echo "$line" | cut -c1-130)"
        fail=1
      done <<< "$hits"
    fi
  done
done < <(git ls-files)

if [ "$fail" -ne 0 ]; then
  echo
  echo "FAILED: public materials contain a claim this project does not make."
  echo "Describe the method and cite the sources; do not claim a review, a"
  echo "quality tier, a price advantage, or an outcome."
  exit 1
fi

echo "OK: no unverifiable or prohibited claims in tracked public materials."
