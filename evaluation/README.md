# Regression tests

These cases pin specific legal rules the skills are supposed to enforce. Each one is a record shaped so the intuitive answer is the wrong answer under a named authority, plus a grader that checks whether the rule survived.

Cases live at [`thepapers-niw/evals/`](../thepapers-niw/evals/), authored in the format `claude plugin eval` expects: a directory per case with a `prompt.md` carrying frontmatter, a `graders/` directory of typed graders, and a `workspace/` holding the case's input files.

## This is not a quality benchmark, and we do not publish a score

We could. We are choosing not to, for two reasons.

**An ablation measures influence, not correctness.** Running a case with and without the plugin tells you how far the skill moved the answer. It says nothing about whether the answer is right. If a rule we encoded is wrong, a large delta is a precise measurement of how firmly we planted the mistake, reported as a win.

**The cases and the skills were written by the same hand.** Both come from the same reading of the same authorities. A suite built that way tends to confirm its own premises. It will keep passing exactly where those premises are shared, including where they are shared and wrong, and it cannot detect that about itself. Publishing its output as evidence of quality would dress up a closed loop as an external check.

So the suite is used for the one job it is genuinely good at: catching the day an edit to a knowledge pack or a skill quietly stops enforcing a rule that used to hold.

## What each case pins

| Case | The rule it pins | Authority |
|---|---|---|
| `forms-are-out-of-scope` | Missing forms, fees and signatures are filing mechanics, not gaps in the evidentiary record | Scope of a package review |
| `filed-case-no-post-filing-cure` | After filing, eligibility is fixed as of the filing date, so no cure may rest on a fact that arose later | 8 CFR 103.2(b)(12); *Matter of Katigbak*, 14 I&N Dec. 45 (Reg. Comm. 1971) |
| `not-filed-exhibit-is-a-gap` | A document the petitioner holds but never sent is not record support | 8 CFR 103.2(b)(2) |
| `rfe-endeavor-detail-trap` | An RFE asking for "a detailed description of the proposed endeavor" is not license to re-scope the endeavor | *Matter of Izummi*, 22 I&N Dec. 169 (Comm. 1998) |
| `industry-endeavor-not-field` | Field-level importance is not endeavor importance, and an industry record is not judged on publication counts | *Matter of Dhanasar*, 26 I&N Dec. 884, 889 (AAO 2016) |
| `founder-market-size-insufficient` | Market size and membership in a named technology list are framing, not proof | *Matter of Dhanasar*, 26 I&N Dec. 884, 889 (AAO 2016) |
| `orientation-no-profile` | No verdict on a one-sentence self-description. Orient the user and ask for the record | Preponderance standard, *Matter of Chawathe*, 25 I&N Dec. 369, 375–76 (AAO 2010) |

## Running them

`claude plugin eval` is the official harness and is currently early access. Until it is available here, [`tests/run_evals.py`](../tests/run_evals.py) runs the same cases in the same format.

```bash
tests/run_evals.py                        # every case
tests/run_evals.py --case forms-*         # filter by name
tests/run_evals.py --arms with            # skip the baseline arm
tests/run_evals.py --judge-votes 3        # judge samples per LLM grader
```

The baseline arm is still worth running, not as a scoreboard but as a triviality check: a case the base model passes on its own is not testing the skill, and knowing which cases those are keeps us from mistaking an easy suite for a strong one. Cases that show no delta are kept and left alone. We do not tune a fixture until it produces one.

## Reading a result honestly

- A pass means the rule held on this fixture, with this model, on this run. It is not a statement about the next case a real person brings.
- Fixtures are synthetic profiles. There are no real petitioner records in this repository.
- LLM graders are sampled three times and decided by majority. A single sample was not reliable: it once marked a correct response FAIL while its own justification described the response doing the right thing.
- Grader infrastructure failures are recorded as unjudged and excluded, never scored as substantive failures. [`tests/test_runner_logic.py`](../tests/test_runner_logic.py) covers that offline.

## What would actually be evidence

Real petitioners, real notices, real adjudications, and correction from people who do this work. None of that can be manufactured in a fixture, and none of it is in this repository. The most useful thing anyone can send us is the case where a skill states a rule wrongly, with the authority that says so. [CONTRIBUTING.md](../CONTRIBUTING.md) explains how.
