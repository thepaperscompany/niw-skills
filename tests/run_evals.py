#!/usr/bin/env python3
"""Run the eval suite with and without the plugin, and report the delta.

`claude plugin eval` is the official harness and is currently early access.
Cases are authored in its format (<case>/prompt.md with frontmatter, plus
<case>/graders/*.md typed by frontmatter), so they run natively once that is
enabled. This runner executes the same cases today so the suite is not merely
aspirational, and applies the same with/without ablation.

Grader types supported here: regex, llm, tool_used. The official harness also
supports tool_order, file_exists and baseline.

Usage:
    tests/run_evals.py                          run every case, both arms
    tests/run_evals.py --case not-filed*        filter by name glob
    tests/run_evals.py --arms with              skip the baseline arm
    tests/run_evals.py --runs 3                 repeat each arm
    tests/run_evals.py --judge-model sonnet     override the grader model

Exit codes: 0 every case at or above --threshold, 1 below, 2 usage error.
"""

import argparse
import fnmatch
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PLUGIN_DIR = REPO / "thepapers-niw"
EVAL_DIR = PLUGIN_DIR / "evals"

# The grader model is deliberately smaller and cheaper than the model under
# test. A judge that shares the subject's blind spots is not an independent
# check; a smaller judge reading explicit pass/fail criteria is.
DEFAULT_JUDGE = "haiku"


def parse_frontmatter(path):
    """Return (frontmatter dict, body). Values are strings, ints or lists."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.index("\n---\n", 3)
    raw, body = text[4:end], text[end + 5:]
    fm = {}
    for line in raw.split("\n"):
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            fm[key] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        elif value.isdigit():
            fm[key] = int(value)
        else:
            fm[key] = value
    return fm, body


def run_agent(prompt, workspace, max_turns, allowed_tools, with_plugin, model=None):
    """Run one agent turn. Returns (result_text, tools_used, cost_usd, error)."""
    cmd = ["claude", "--output-format", "stream-json", "--verbose",
           "--max-turns", str(max_turns)]
    if allowed_tools:
        cmd += ["--allowedTools", " ".join(allowed_tools)]
    if with_plugin:
        cmd += ["--plugin-dir", str(PLUGIN_DIR)]
    if model:
        cmd += ["--model", model]
    cmd += ["-p", prompt]

    try:
        proc = subprocess.run(cmd, cwd=workspace, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        return "", [], 0.0, "timed out after 900s"

    text, tools, cost = "", [], 0.0
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            for block in ev.get("message", {}).get("content", []):
                if block.get("type") == "tool_use":
                    tools.append(block.get("name", ""))
        elif ev.get("type") == "result":
            text = ev.get("result") or ""
            for usage in (ev.get("modelUsage") or {}).values():
                cost += usage.get("costUSD", 0.0)
    if not text:
        return "", tools, cost, (proc.stderr or "no result event").strip()[:300]
    return text, tools, cost, None


def judge(criteria, response, model, votes=3):
    """Ask a smaller model whether the response meets explicit criteria.

    Sampled several times with a majority vote, as the official harness does.
    A single sample is not reliable enough for nuanced criteria: a one-shot
    judge marked a correct response FAIL while its own justification described
    the response doing the right thing.
    """
    tally, details = [], []
    for _ in range(votes):
        passed, detail, errored = _judge_once(criteria, response, model)
        if errored:
            # Infrastructure failure, not a verdict. Scoring it as FAIL invents
            # a regression that did not happen, which is worse than no signal.
            return None, detail
        tally.append(passed)
        details.append(detail)
    if not tally:
        return None, "no judge verdict"
    passed = sum(tally) > len(tally) / 2
    # Show a dissenting justification when the vote is split, so a flaky
    # grader is visible rather than silently deciding the score.
    if len(set(tally)) > 1:
        agree = [d for p, d in zip(tally, details) if p == passed]
        return passed, f"[{sum(tally)}/{len(tally)} pass] {agree[0]}"
    return passed, details[0]


def _judge_once(criteria, response, model):
    prompt = (
        "You are grading one response against explicit criteria. Be strict and "
        "literal. Answer with a single word, PASS or FAIL, on the first line, "
        "then one sentence of justification.\n\n"
        f"=== CRITERIA ===\n{criteria.strip()}\n\n"
        f"=== RESPONSE UNDER TEST ===\n{response.strip()[:24000]}\n"
    )
    try:
        proc = subprocess.run(
            ["claude", "--output-format", "json", "--max-turns", "1",
             "--model", model, "--disallowedTools", "Bash Read Write Edit Glob Grep",
             "-p", prompt],
            capture_output=True, text=True, timeout=300,
        )
        verdict = (json.loads(proc.stdout or "{}").get("result") or "").strip()
    except Exception as exc:  # noqa: BLE001 - report, do not crash the suite
        return False, f"judge error: {exc}", True
    flat = verdict.replace("\n", " ").strip()
    upper = flat.upper()
    if upper.startswith("PASS"):
        return True, flat[:180], False
    if upper.startswith("FAIL"):
        return False, flat[:180], False
    # Anything else is the judge failing to answer: a usage limit, a refusal,
    # an empty result. Report it as unjudged rather than as a failing verdict.
    return False, f"unjudged: {flat[:150] or 'empty judge response'}", True


def grade(grader_path, response, tools, judge_model, judge_votes):
    fm, body = parse_frontmatter(grader_path)
    gtype = fm.get("type")
    weight = float(fm.get("weight", 1))
    with_only = str(fm.get("with-only", "false")).lower() == "true"
    name = grader_path.stem
    pattern = body.strip()

    if gtype == "regex":
        mode = fm.get("mode", "contains")
        flags = 0
        for ch in str(fm.get("flags", "")):
            flags |= {"i": re.I, "m": re.M, "s": re.S}.get(ch, 0)
        hits = len(re.findall(pattern, response, flags))
        if mode == "contains":
            return name, hits > 0, weight, with_only, f"{hits} match(es)"
        if mode == "not_contains":
            return name, hits == 0, weight, with_only, (f"{hits} forbidden match(es)" if hits else "no match")
        if mode.startswith("count:"):
            want = int(mode.split(":", 1)[1])
            return name, hits == want, weight, with_only, f"{hits} match(es), expected {want}"
        return name, False, weight, with_only, f"unknown regex mode '{mode}'"

    if gtype == "tool_used":
        return name, pattern in tools, weight, with_only, f"tools: {', '.join(sorted(set(tools))) or 'none'}"

    if gtype == "llm":
        passed, detail = judge(body, response, judge_model, judge_votes)
        return name, passed, weight, with_only, detail

    return name, False, weight, with_only, f"unsupported grader type '{gtype}'"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", default="*")
    ap.add_argument("--arms", default="with,without")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--judge-model", default=DEFAULT_JUDGE)
    ap.add_argument("--judge-votes", type=int, default=3,
                    help="judge samples per LLM grader; majority decides")
    ap.add_argument("--model", default=None, help="model under test")
    ap.add_argument("--threshold", type=float, default=0.8)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    arms = [a.strip() for a in args.arms.split(",") if a.strip()]
    cases = sorted(
        d for d in EVAL_DIR.iterdir()
        if d.is_dir() and (d / "prompt.md").is_file() and fnmatch.fnmatch(d.name, args.case)
    )
    if not cases:
        print(f"No cases matching '{args.case}' under {EVAL_DIR}")
        return 2

    results, total_cost = [], 0.0
    for case in cases:
        fm, prompt = parse_frontmatter(case / "prompt.md")
        graders = sorted((case / "graders").glob("*.md")) if (case / "graders").is_dir() else []
        if not graders:
            print(f"SKIP {case.name}: no graders")
            continue

        print(f"\n=== {case.name} ===")
        case_result = {"case": case.name, "tags": fm.get("tags", []), "arms": {}}

        for arm in arms:
            scores = []
            for run in range(args.runs):
                with tempfile.TemporaryDirectory() as tmp:
                    ws = Path(tmp) / "ws"
                    src = case / "workspace"
                    if src.is_dir():
                        shutil.copytree(src, ws)
                    else:
                        ws.mkdir(parents=True)
                    text, tools, cost, err = run_agent(
                        prompt.strip(), ws, fm.get("max_turns", 25),
                        fm.get("allowed_tools", []), arm == "with", args.model)
                total_cost += cost
                if err:
                    print(f"  [{arm}] run {run + 1}: ERROR {err}")
                    scores.append(0.0)
                    continue

                earned = possible = 0.0
                lines, unjudged = [], 0
                for g in graders:
                    gname, passed, weight, with_only, detail = grade(
                        g, text, tools, args.judge_model, args.judge_votes)
                    # A with-only grader is a plugin-fired indicator, not part
                    # of the score, exactly as the official harness treats it.
                    if with_only:
                        lines.append(f"      [indicator] {gname}: {'yes' if passed else 'no'} ({detail})")
                        continue
                    if passed is None:
                        unjudged += 1
                        lines.append(f"      ????  {gname} (w{weight:g}): {detail}")
                        continue
                    possible += weight
                    earned += weight if passed else 0.0
                    lines.append(f"      {'PASS' if passed else 'FAIL'}  {gname} (w{weight:g}): {detail}")
                if possible == 0:
                    print(f"  [{arm}] run {run + 1}: UNJUDGED (every LLM grader failed to run)")
                    for line in lines:
                        print(line)
                    continue
                score = earned / possible if possible else 0.0
                scores.append(score)
                mark = f"  [{unjudged} grader(s) unjudged]" if unjudged else ""
                print(f"  [{arm}] run {run + 1}: {score:.0%}{mark}")
                for line in lines:
                    print(line)

            case_result["arms"][arm] = {
                "mean": sum(scores) / len(scores) if scores else 0.0, "runs": scores}

        w = case_result["arms"].get("with", {}).get("mean")
        wo = case_result["arms"].get("without", {}).get("mean")
        if w is not None and wo is not None:
            print(f"  -> with {w:.0%}  without {wo:.0%}  delta {w - wo:+.0%}")
        results.append(case_result)

    print("\n" + "=" * 62)
    withs = [r["arms"]["with"]["mean"] for r in results if "with" in r["arms"]]
    withouts = [r["arms"]["without"]["mean"] for r in results if "without" in r["arms"]]
    if withs:
        print(f"Suite score with plugin:    {sum(withs) / len(withs):.0%}  ({len(withs)} cases)")
    if withouts:
        print(f"Suite score without plugin: {sum(withouts) / len(withouts):.0%}")
    if withs and withouts:
        print(f"Delta:                      {sum(withs) / len(withs) - sum(withouts) / len(withouts):+.0%}")
    print(f"Approximate cost:           ${total_cost:.2f}")

    if args.out:
        Path(args.out).write_text(json.dumps({
            "generated": datetime.now(timezone.utc).isoformat(),
            "runs_per_arm": args.runs, "judge_model": args.judge_model,
            "threshold": args.threshold, "cases": results}, indent=2), encoding="utf-8")
        print(f"Wrote {args.out}")

    below = [r["case"] for r in results
             if "with" in r["arms"] and r["arms"]["with"]["mean"] < args.threshold]
    if below:
        print(f"\nBelow threshold {args.threshold:.0%}: {', '.join(below)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
