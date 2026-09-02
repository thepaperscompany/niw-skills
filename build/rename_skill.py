#!/usr/bin/env python3
"""Rewrite a standalone skill's frontmatter name.

Inside the plugin a skill is namespaced (/thepapers-niw:niw-evaluate). A
claude.ai upload shares one flat namespace with every skill the user has
installed, so the standalone copy needs a globally unique name.

Usage: rename_skill.py <SKILL.md> <old-name> <new-name>
"""
import io
import sys

if len(sys.argv) != 4:
    print(__doc__.strip())
    sys.exit(2)

path, old, new = sys.argv[1], sys.argv[2], sys.argv[3]
text = io.open(path, encoding="utf-8").read()
marker = f"---\nname: {old}\n"
if not text.startswith(marker):
    print(f"ERROR: {path} does not start with 'name: {old}'; refusing to rename")
    sys.exit(1)
io.open(path, "w", encoding="utf-8").write(text.replace(marker, f"---\nname: {new}\n", 1))
