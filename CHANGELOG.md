# Changelog

All notable changes to the NIW skill suite will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Each skill is versioned independently. The frontmatter `version` field in each `SKILL.md` is the source of truth for that skill.

## Sync policy

The skill prompts in this repository are derived from the prompts used in The Papers Company's hosted product at thepapers.co/immigration. When the hosted product's prompts change, the corresponding skill in this repo is updated in a tagged release.

The hosted prompt is the source of truth. Skills lag behind by zero or more product releases. If you find drift, open an issue.

---

## [Unreleased]

### Plugin — 0.3.0 — the full AAO corpus, published

**`knowledge/` is now the single source of truth for legal substance.** All reference files moved there. Files under `thepapers-niw/skills/*/references/` are generated copies, vendored at build time by `build/vendor.sh` so a standalone `.skill` remains self-contained on claude.ai, where there is no plugin root to resolve a shared path against. `build/vendor.sh --check` fails on drift, and `knowledge/MANIFEST.txt` records a sha256 for every vendored file.

**`knowledge/current-adjudication-bar.md` replaces the previous adjudication-bar file.** The old version was distilled from three AAO decisions. This one is distilled from the **complete public pool of AAO non-precedent NIW (EB-2/B5) decisions issued 2025-01 through 2026-06**: 1,040 decisions crawled and downloaded, 1,036 mechanically classified for outcome and dispositive issue, the highest-substance analysis sections plus about 35 decisions read in full. It carries 21 numbered patterns across cross-cutting posture, EB-2 threshold, all three prongs, what prevails in sustained appeals, and calibration cautions against the opposite errors.

Two disciplines ship with it and are stated in the file itself:

- **Verified quotations.** All 35 quotations were copied from their source decisions and checked against them during distillation. None was generated from memory.
- **Stated sampling bias.** This is a denial-heavy appeal pool: petitions approved at first instance and denials never appealed are invisible in it. The file calibrates how closely to scrutinize a record and is never a source of outcome rates, base rates, or a probability of approval. It also records adjudicator errors the AAO *reverses*, so the model does not imitate service-center overreach.

**Added `knowledge/policy-alerts.md`, including PA-2026-05.** Effective 2026-08-05, USCIS restored officers' full discretion to deny a benefit request without first issuing an RFE or NOID, citing 8 CFR 103.2(b)(8)(ii). A thin filing can no longer be assumed to draw a curable Request for Evidence. `SKILL.md` now reads this file before writing any verdict or filing recommendation, and the "What to do now" section states the consequence of filing early in plain terms. This changes the cost of filing short, not the legal test, and the skill is instructed never to present it as a prediction. Also covers PA-2025-16 (discretion after eligibility) and PA-2025-03.

**Added a table of contents to every reference file over 100 lines,** so a partial read still shows the full scope of what the file contains.

**Added `scripts/check_public_safe.sh`.** This repository is public and its history is permanent. The script fails if any tracked file references private infrastructure: absolute home paths, git worktree ids, private repo names, internal module names, or internal tooling commands. `build/package.sh` runs it, along with `claude plugin validate --strict`, before packing any artifact, and re-checks the built archives afterward.

**Rewrote `docs/METHODOLOGY.md` §2** from "curated AAO, not bulk" to describe the complete-pool method, what we refuse to distill (correlates of approval), and the three distortions corrected rather than inherited.

**README gains a "Check our work" section** pointing at `knowledge/` so a reader can look up any quotation rather than take the claim on trust. The claude.ai upload path is corrected to Settings then Features.


### Plugin — 0.2.1 — license switch

**License changed from MIT to Apache License 2.0** ([SPDX: `Apache-2.0`](https://spdx.org/licenses/Apache-2.0.html)). Chosen over MIT for three reasons specific to this project:

1. **Trademark protection** — Apache 2.0 Section 6 explicitly states the license does not grant rights to use the contributor's trademarks. This matters for "The Papers Company," "Immigration Papers," and "thepapers-niw" branding; if a third party forks and rebrands, Apache 2.0 gives a clearer formal lever beyond trademark law.
2. **Patent grant** — Apache 2.0 Section 3 gives users a perpetual, royalty-free patent license from each contributor for patent claims necessarily infringed by their contributions. This lowers adoption friction for enterprise users whose legal teams flag MIT for the absence of an explicit patent grant.
3. **Ecosystem alignment** — the Claude SDK and most Anthropic-ecosystem tooling use Apache 2.0.

Files updated: `LICENSE` (Apache 2.0 text), new `NOTICE` file (trademark notice + plugin-specific disclaimers), `thepapers-niw/.claude-plugin/plugin.json` (`"license": "Apache-2.0"`), `thepapers-niw/skills/niw-evaluate/SKILL.md` frontmatter (`license: Apache-2.0`), `README.md` (License section explains the change), `dist/*` (rebuilt artifacts).

Done now because the repo is freshly published with no external contributors yet — license changes are clean and unilateral at this stage. Once contributors arrive, license changes require their consent or a contributor license agreement.

### Plugin — 0.2.0

**Restructured to the [official Claude Code plugin format](https://code.claude.com/docs/en/plugins).** The repo now contains a real plugin directory at `thepapers-niw/` with `.claude-plugin/plugin.json` and a `skills/` subdirectory. Skills inside the plugin are namespaced — `niw-evaluate` is invoked as `/thepapers-niw:niw-evaluate` once the plugin is loaded.

**Two distribution artifacts:**

- `dist/thepapers-niw.zip` (53 KB) — the Claude Code plugin. Install with `claude --plugin-dir ./dist/thepapers-niw.zip`. With v0.2 it contains only `niw-evaluate`, but future NIW skills (endeavor-statement, evidence-finder, recommendation-letter, petition-letter, RFE-analyzer) will ship into the same plugin. Installing once means future updates land via plugin update rather than per-skill upload.
- `dist/thepapers-niw-evaluate.skill` (51 KB) — standalone single-skill `.skill` file for claude.ai Settings → Capabilities upload. The standalone version uses the globally-unique name `thepapers-niw-evaluate` (the plugin-namespaced name `niw-evaluate` would conflict if multiple NIW skill plugins exist).

Choosing the right artifact:

- Using claude.ai in the browser: upload the `.skill` file.
- Using Claude Code locally: install the plugin zip (you get future updates).

### `niw-evaluate` (inside `thepapers-niw` plugin) — 0.2.0

### `thepapers-niw-evaluate` — 0.1.0

Initial preview release.

- Ported the full-evaluation prompt from the hosted product (Immigration Papers v1).
- Added inline citation hygiene: *Matter of Dhanasar*, *Matter of Chawathe*, USCIS Policy Manual Vol. 6 Pt. F Ch. 5.
- Added verdict floor rules: no prong can be rated "Strong" or "Very Strong" without preponderance-passing documented evidence.
- Added the *achievable case ceiling* output section for prospective applicants 6–24 months from filing.
- Added anti-hallucination guardrails (no invented AAO IDs, citation counts, grant roles, or employer facts).
- **Added the endeavor-proposal flow** (Step 0). When a user provides a profile without a proposed endeavor, the skill proposes 3–5 candidate endeavors grounded in documented anchor facts before running the evaluation — mirroring the flow in the hosted product. When a user provides a Moderate or Too Broad endeavor, the skill offers 2–3 narrower restatements (Step 0b) for selection before evaluating. Doctrine and worked examples in `references/endeavor-proposal.md`.
- **Added an orientation flow** (Step 0.0). When a user is new to NIW — does not know what NIW is, does not know what a proposed endeavor is, or is choosing among pathways — the skill produces a short plain-language orientation covering the three Dhanasar prongs, the distinction between proposed endeavor and endeavor statement, a comparison against EB-1A and O-1A, and the priority-date backlog reality for India and China nationals. Doctrine in `references/orientation.md`.
- **Added an EB-2 baseline check** (Step 0.5). Catches the statutory disqualifiers that make NIW unavailable regardless of Dhanasar analysis — foreign three-year bachelor's without master's, experience not in the specialty, occupation not a profession, and so on. Doctrine in `references/eb2-baseline.md`.
- **Added explicit terminology discipline** between "proposed endeavor" (short framing — in scope of this skill) and "endeavor statement" (long drafted narrative — out of scope; planned `thepapers-niw-endeavor-statement` skill).
- **Restructured the output memo.** New "At-a-glance" summary at the top with verdict and achievable ceiling side-by-side, so the user sees the path forward immediately. New "Next steps for you" section before the disclaimers, with concrete user-facing actions calibrated to the verdict.
- **Added a Writing for an international, ESL-primary, highly-educated audience section** to `SKILL.md`. All user-facing output (orientation, candidate-endeavor tiles, evaluation memo) is calibrated to short sentences, in-line technical-term explanations, no idioms or cultural references, and standard-form citations.
- **Reframed the backlog handling** in orientation and evaluation memos. For India and China nationals, an approved I-140 is the practical operative benefit because it unlocks indefinite H-1B extension under AC21 § 104(c) (three-year increments) and § 106(a) (one-year increments), and it is portable across employers. The skill no longer treats the priority-date backlog as a discouragement — it treats it as the reason this cohort files NIW.
- **De-emphasized the EB-2 baseline check.** Default assumption is now that the user qualifies for EB-2 (most users have an advanced degree or a clear bachelor's-plus-five-years path). Step 0.5 triggers only on clear contradicting signals such as an unevaluated foreign three-year bachelor's, no advanced degree at all, experience unrelated to specialty under *Matter of Katigbak*, or a non-profession occupation. Routine ambiguities are resolved with one clarifying question, not a full baseline gate.
- **Added `references/policy-manual-substance.md`** capturing the Policy Manual narrative substance not previously in the reference set: Prong 1 worked examples (drug-for-pharma, software-engineer-adapting-code, classroom-teaching, technology-for-employer-clients), Prong 2 full evidence list and letter-persuasiveness test, Prong 3 factor detail, STEM critical-tech triad, interested government agency letters (Section 5), and full entrepreneur evidence categories (ownership, investment, revenue, job creation — Section 6). Wired into Steps 4, 5, 6 of `SKILL.md`.
- **Added the long-horizon explorer cohort.** Master's and PhD international students who are 3–5 years from filing get a multi-year decision-support roadmap (extended ceiling cap of 60 months) rather than a "your case is weak" verdict. The output for this cohort is decision-supportive and includes revisit milestones at 12 and 24 months plus comparison to alternative pathways (EB-1A in particular) if the trajectory exceeds NIW requirements. The skill is calibrated as a navigator for this cohort, not a fortune-teller.
- **Restructured the skill around a 5-stage agentic conversation pattern** (Stage 1 orient and intake → Stage 2 co-design the endeavor → Stage 3 confirm → Stage 4 full evaluation → Stage 5 follow-ups). Replaced the previous "Shape A / Shape B" output abstraction, which leaked engineering taxonomy ("entry state," "Step 0b," "candidate endeavor," "anchor facts," "endeavor specificity check," "preponderance gate") into user-facing prose. The skill now reads like a guided conversation with a senior immigration paralegal — matching the hosted product flow at thepapers.co/immigration.
- **Locked down voice discipline.** Title for evaluation memos is always *"Your NIW evaluation"*; orientation memos use a plain-English orientation title. Internal taxonomy is forbidden on the page. Section headings name the substance, not the process. No idioms, no engineering metaphors, no invented probabilities of approval. Verified across iteration-3 outputs (cold-start orientation, partial-orient+options, Stage 4 direct evaluation, Stage 3→4 continuation).
- Initial eval set: 6 fixtures covering academic/STEM, industry/applied, founder/entrepreneur, the no-endeavor entry path, the orientation-needed entry path, and the EB-2-baseline-fail entry path. Iteration-1 produced quantitative benchmark (+55pp pass rate over baseline). Iteration-2 verified voice fix on 3 evals. Iteration-3 verified agentic pattern on 4 evals (including a new Stage 3→4 continuation fixture).
- Pending: licensed-attorney sign-off (target: v1.0).
- Pending: factoring `thepapers-niw-propose-endeavors` out as its own callable skill (target: v0.2). For v0.1 the proposal flow is integrated into `thepapers-niw-evaluate`.
- Pending: `thepapers-niw-endeavor-statement` skill for drafting the longer narrative document (target: v0.3).
