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

# The standalone skill needs a globally unique name: inside the plugin the
# skill is namespaced as /thepapers-niw:niw-evaluate, but a claude.ai upload
# shares one flat namespace with every other skill the user has installed.
echo "==> Building dist/thepapers-niw-evaluate.skill"
mkdir -p "$tmp/standalone/thepapers-niw-evaluate"
cp -R thepapers-niw/skills/niw-evaluate/. "$tmp/standalone/thepapers-niw-evaluate/"
find "$tmp/standalone" -name '.DS_Store' -delete
python3 - "$tmp/standalone/thepapers-niw-evaluate/SKILL.md" <<'PY'
import io, sys
p = sys.argv[1]
s = io.open(p, encoding="utf-8").read()
assert s.startswith("---\nname: niw-evaluate\n"), "unexpected frontmatter; refusing to rename"
s = s.replace("---\nname: niw-evaluate\n", "---\nname: thepapers-niw-evaluate\n", 1)
io.open(p, "w", encoding="utf-8").write(s)
PY
# evals/ are for maintainers and CI, not for a claude.ai upload.
rm -rf "$tmp/standalone/thepapers-niw-evaluate/evals"
( cd "$tmp/standalone" && zip -qr "$OLDPWD/dist/thepapers-niw-evaluate.skill" . )

echo "==> Verifying the built artifacts carry no private infrastructure"
verify="$tmp/verify"; mkdir -p "$verify"
unzip -qo dist/thepapers-niw.zip -d "$verify/plugin"
unzip -qo dist/thepapers-niw-evaluate.skill -d "$verify/skill"
# Reuse the one definition of the patterns rather than restating them here.
scripts/check_public_safe.sh --path "$verify"

echo
ls -lh dist/
echo "OK: artifacts built and verified."
