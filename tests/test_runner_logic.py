#!/usr/bin/env python3
"""Offline tests for the eval runner's grading logic.

These need no model calls, so they run in CI. They exist because the runner
originally scored a judge infrastructure failure (a usage limit) as a
substantive FAIL, which invented a regression that had not happened. Grading
logic that silently turns an outage into a quality signal is worse than no
grading at all.
"""

import importlib.util
import pathlib
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("run_evals", REPO / "tests" / "run_evals.py")
rv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rv)

tmp = pathlib.Path(tempfile.mkdtemp())
failures = []


def check(label, condition):
    print(f"{'ok   ' if condition else 'FAIL '} {label}")
    if not condition:
        failures.append(label)


def write(name, text):
    p = tmp / name
    p.write_text(text, encoding="utf-8")
    return p


regex_grader = write("regex.md", "---\ntype: regex\nmode: not_contains\nflags: i\nweight: 2\n---\nprobability of approval\n")
check("regex not_contains passes on clean text",
      rv.grade(regex_grader, "No forecast here.", [], "haiku", 1)[1] is True)
check("regex not_contains fails on a forbidden phrase",
      rv.grade(regex_grader, "The probability of approval is high.", [], "haiku", 1)[1] is False)

count_grader = write("count.md", "---\ntype: regex\nmode: count:2\nweight: 1\n---\nExhibit\n")
check("regex count matches an exact count",
      rv.grade(count_grader, "Exhibit a and Exhibit b", [], "haiku", 1)[1] is True)

tool_grader = write("tool.md", "---\ntype: tool_used\nwith-only: true\nweight: 1\n---\nSkill\n")
name, passed, weight, with_only, _ = rv.grade(tool_grader, "x", ["Bash", "Skill"], "haiku", 1)
check("tool_used detects the tool", passed is True)
check("tool_used is marked with-only", with_only is True)
check("tool_used reports absence",
      rv.grade(tool_grader, "x", ["Bash"], "haiku", 1)[1] is False)

llm_grader = write("llm.md", "---\ntype: llm\nweight: 3\n---\nPASS if the sky is blue.\n")

original = rv._judge_once
rv._judge_once = lambda *a, **k: (False, "You've hit your session limit", True)
check("a judge infrastructure error is unjudged, not a FAIL",
      rv.grade(llm_grader, "anything", [], "haiku", 3)[1] is None)

rv._judge_once = lambda *a, **k: (False, "the judge said something unparseable", True)
check("an unparseable judge verdict is unjudged, not a FAIL",
      rv.grade(llm_grader, "anything", [], "haiku", 3)[1] is None)

votes = iter([(True, "PASS a", False), (False, "FAIL b", False), (True, "PASS c", False)])
rv._judge_once = lambda *a, **k: next(votes)
_, passed, _, _, detail = rv.grade(llm_grader, "anything", [], "haiku", 3)
check("a split judge vote resolves to the majority", passed is True)
check("a split judge vote is visible in the detail", "2/3" in detail)

votes = iter([(False, "FAIL a", False), (False, "FAIL b", False), (True, "PASS c", False)])
rv._judge_once = lambda *a, **k: next(votes)
check("a majority FAIL resolves to FAIL",
      rv.grade(llm_grader, "anything", [], "haiku", 3)[1] is False)
rv._judge_once = original

fm, body = rv.parse_frontmatter(write("fm.md", "---\nmax_turns: 30\nallowed_tools: [Read, Bash]\ntags: [a, b]\n---\nbody text\n"))
check("frontmatter parses ints", fm["max_turns"] == 30)
check("frontmatter parses lists", fm["allowed_tools"] == ["Read", "Bash"])
check("frontmatter body is separated", body.strip() == "body text")

print()
if failures:
    print(f"FAILED: {len(failures)} check(s): {', '.join(failures)}")
    sys.exit(1)
print("OK: eval runner grading logic behaves as specified.")
