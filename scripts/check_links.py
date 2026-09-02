#!/usr/bin/env python3
"""Verify that every internal link and bundled-script reference resolves.

A skill that points at a reference file which was never vendored degrades
silently: the model reads SKILL.md, tries to open the file, finds nothing, and
carries on without the doctrine it was told to apply. Nothing errors. The
output is just quietly worse.

Checks:
  - Markdown links to local paths resolve, from any tracked .md file.
  - Every references/*.md a SKILL.md mentions was actually vendored.
  - Every ${CLAUDE_SKILL_DIR}/scripts/*.py a SKILL.md tells the model to run exists.

Usage: scripts/check_links.py
"""

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKILL_SCRIPT = re.compile(r"\$\{CLAUDE_SKILL_DIR\}/(scripts/[A-Za-z0-9_./-]+)")
REF_MENTION = re.compile(r"`(references/[A-Za-z0-9_.-]+\.md)`")

problems = []

tracked = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True, text=True).stdout.split()

for rel in tracked:
    if not rel.endswith(".md"):
        continue
    path = REPO / rel
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        continue

    for target in MD_LINK.findall(text):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            problems.append(f"{rel}: broken link -> {target}")

    if path.name == "SKILL.md":
        skill_dir = path.parent
        for ref in set(REF_MENTION.findall(text)):
            if not (skill_dir / ref).exists():
                problems.append(f"{rel}: mentions {ref}, which is not vendored into this skill")
        for script in set(SKILL_SCRIPT.findall(text)):
            if not (skill_dir / script).exists():
                problems.append(f"{rel}: tells the model to run {script}, which is not bundled with this skill")

if problems:
    for p in sorted(problems):
        print(f"BROKEN  {p}")
    print(f"\nFAILED: {len(problems)} unresolved reference(s).")
    sys.exit(1)

print(f"OK: every internal link and bundled reference resolves ({len(tracked)} tracked files scanned).")
