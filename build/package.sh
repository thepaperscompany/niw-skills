#!/usr/bin/env bash
# Build the distributable artifacts.
#
#   dist/thepapers-niw.zip            Claude Code plugin (all skills)
#   dist/thepapers-niw-evaluate.skill Standalone skill for claude.ai upload
#
# Runs the safety and vendoring gates first. A build that would ship private
# infrastructure, or stale copies of knowledge/, fails instead of packing.

set -euo pipefail
cd "$(dirname "$0")/.." || exit 2

echo "==> Refreshing vendored references from knowledge/"
build/vendor.sh

echo "==> Checking no tracked file references private infrastructure"
scripts/check_public_safe.sh

echo "==> Checking for unverifiable or prohibited claims"
scripts/check_claims.sh

echo "==> Checking the pack's verbatim quotations are unchanged"
python3 scripts/check_quote_integrity.py

echo "==> Checking the bundled validators behave as specified"
tests/run_script_tests.sh

echo "==> Checking internal links and bundled references resolve"
python3 scripts/check_links.py

echo "==> Checking the eval runner's grading logic"
python3 tests/test_runner_logic.py

echo "==> Validating the plugin"
if command -v claude >/dev/null 2>&1; then
  claude plugin validate ./thepapers-niw --strict || {
    echo "FAILED: claude plugin validate rejected the plugin."; exit 1; }
else
  echo "    (claude CLI not found; skipping. Run 'claude plugin validate ./thepapers-niw --strict' before release.)"
fi

rm -rf dist && mkdir -p dist
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

echo "==> Building dist/thepapers-niw.zip"
mkdir -p "$tmp/plugin"
cp -R thepapers-niw "$tmp/plugin/"
( cd "$tmp/plugin" && find . -name '.DS_Store' -delete && zip -qr "$OLDPWD/dist/thepapers-niw.zip" . )

# Each skill also ships standalone for claude.ai upload. Inside the plugin a
# skill is namespaced as /thepapers-niw:<name>, but a claude.ai upload shares
# one flat namespace with every other skill the user has installed, so the
# standalone copy takes a globally unique name.
for skill_dir in thepapers-niw/skills/*/; do
  skill="$(basename "$skill_dir")"
  unique="thepapers-${skill}"
  echo "==> Building dist/${unique}.skill"
  mkdir -p "$tmp/standalone/$unique/$unique"
  cp -R "$skill_dir." "$tmp/standalone/$unique/$unique/"
  find "$tmp/standalone/$unique" -name '.DS_Store' -delete
  # evals/ are for maintainers and CI, not for a claude.ai upload.
  rm -rf "$tmp/standalone/$unique/$unique/evals"
  python3 build/rename_skill.py "$tmp/standalone/$unique/$unique/SKILL.md" "$skill" "$unique"
  ( cd "$tmp/standalone/$unique" && zip -qr "$OLDPWD/dist/${unique}.skill" . )
done

echo "==> Verifying the built artifacts carry no private infrastructure"
verify="$tmp/verify"; mkdir -p "$verify"
unzip -qo dist/thepapers-niw.zip -d "$verify/plugin"
for s in dist/*.skill; do
  unzip -qo "$s" -d "$verify/$(basename "$s" .skill)"
done
# Reuse the one definition of the patterns rather than restating them here.
scripts/check_public_safe.sh --path "$verify"

echo
ls -lh dist/
echo "OK: artifacts built and verified."
