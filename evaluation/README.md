# Evaluation results

This directory contains the published validation numbers for `thepapers-niw-evaluate`.

The skill was validated against seven eval fixtures spanning the full conversation taxonomy:

1. **Cold-start orientation** — Indian H-1B petitioner asks "what is NIW?" (Stage 1 only)
2. **Postdoc, no endeavor, partial unfamiliarity** — orientation folded into options (Stage 1 + Stage 2)
3. **Postdoc, specific endeavor** — direct full evaluation (Stage 4)
4. **Postdoc picks Option A** — continuation from a prior turn (Stage 3 → Stage 4)
5. **Industry ML engineer, theme-level endeavor** — endeavor reframing for a too-broad framing
6. **Founder, market-size endeavor** — entrepreneur reframing under USCIS Policy Manual Vol. 6 Pt. F Ch. 5(D)(6)
7. **EB-2 baseline at risk** — eligibility pre-check before any Dhanasar analysis

All seven fixtures are reproducible — they live at `thepapers-niw-evaluate/evals/fixtures/`.

## Headline result

| Metric | With skill | Without skill (baseline Claude) | Delta |
|---|---|---|---|
| **Assertion pass rate** | **100%** (35/35) | **31.7%** (10/35) | **+68 percentage points** |
| Mean time per run | 76 s | 87 s | -11 s |
| Mean tokens per run | 62k | 40k | +22k |

The pass rate is against rubric-based assertions per fixture: correct entry-state detection; correct stage produced; voice discipline (no internal taxonomy leaked to user); inline citation hygiene; no invented probability of approval; archetype-appropriate evidence calibration.

## Files

- `benchmark.json` — full structured benchmark output with per-eval results, expectations, and analyst notes.
- `benchmark.md` — human-readable summary table.

## Caveats

- N=1 per (eval, configuration). Stddev figures should not be interpreted as variance estimates.
- Fixtures are synthetic profiles. Real-user testing pending.
- Attorney sign-off pending separately.
- The skill is calibrated to the USCIS adjudication standard as of the SKILL.md `version` date. Policy updates can change the standard at any time.
