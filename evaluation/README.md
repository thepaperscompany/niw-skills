# Evaluation

Cases live at [`thepapers-niw/evals/`](../thepapers-niw/evals/), authored in the format `claude plugin eval` expects: each case is a directory with a `prompt.md` carrying frontmatter, a `graders/` directory of typed graders, and a `workspace/` holding the case's input files.

`claude plugin eval` is the official harness and is currently early access. Until it is available here, [`tests/run_evals.py`](../tests/run_evals.py) runs the same cases and applies the same with-plugin / without-plugin ablation, so the suite is measured rather than aspirational.

```bash
tests/run_evals.py                        # every case, both arms
tests/run_evals.py --case forms-*         # filter by name
tests/run_evals.py --arms with            # skip the baseline arm
tests/run_evals.py --judge-votes 3        # judge samples per LLM grader
```

## What we measure, and why the baseline arm matters

Every case runs twice: once with the plugin loaded, once without. The number that matters is the **delta**, because a case the base model already passes tells you the skill adds nothing there. Reporting only the with-plugin score would let a suite of easy cases look like evidence of quality.

We do not tune a fixture until it produces a delta. A case that shows no delta is kept and reported as showing no delta.

## Results

Measured 2026-09-02, one run per arm, three judge votes per LLM grader. One run per arm is a weak sample and the numbers below should be read as directional.

| Case | With plugin | Baseline | Delta | What it tests |
|---|---|---|---|---|
| `forms-are-out-of-scope` | 100% | 40% | **+60** | Missing forms, fees and signatures must not be reported as deficiencies in the evidentiary record |
| `filed-case-no-post-filing-cure` | 100% | 67% | **+33** | After filing, no cure may rest on a post-filing fact, and the endeavor may not be re-scoped |
| `not-filed-exhibit-is-a-gap` | 100% | 100% | 0 | A document the petitioner holds but never sent is not record support |
| `industry-endeavor-not-field` | pending | pending | pending | Field-level framing is not endeavor importance; industry records are not judged on publications |
| `founder-market-size-insufficient` | not yet run | not yet run | | Market size and technology-list membership are framing, not proof |
| `orientation-no-profile` | not yet run | not yet run | | No verdict on a one-sentence description; orient and ask |

### What the deltas actually show

**The endeavor lock is the sharpest single finding.** On a filed petition, the baseline recommended "a rewritten endeavor statement with actual specificity." Rewriting the endeavor after filing is a material change under *Matter of Izummi* and is held against the petitioner's consistency. It is the intuitive move and it is the one that damages the case. The plugin warned against it explicitly.

**Scope discipline was the largest delta.** The baseline listed a missing Form I-140, filing fee and G-28 under "not present, and normally expected," treating out-of-scope filing mechanics as gaps in the evidentiary record.

**Filing status showed no delta, and we are reporting that.** The case was first written with exhibits labelled `NOT FILED` in the manifest, which gave the answer away; the baseline passed. It was rewritten so filing status had to be inferred from a note in the package, and the baseline passed again. A capable model handles this without the skill. The discipline is still worth encoding, because it holds when a package is larger and messier than a fixture, but on this evidence it is not a differentiator and we will not claim it as one.

## Known limitations

- One run per arm. The official harness defaults to three, and variance at n=1 is real.
- The remaining cases are unrun because the session hit a usage limit partway through.
- LLM graders are sampled three times and decided by majority. A single sample was not reliable: it marked a correct response FAIL while its own justification described the response doing the right thing.
- Fixtures are synthetic profiles, not real petitioner records.

## Earlier results

`benchmark.json` and `benchmark.md` hold the v0.1 numbers from the previous bespoke harness (seven fixtures, +68 percentage points over baseline on rubric assertions). Those were produced by a different harness with a different grading method and are not comparable to the table above. They are kept for history.
