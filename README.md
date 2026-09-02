# NIW Skills: by The Papers Company

> Open-source skills for the U.S. EB-2 National Interest Waiver, covering the whole route: working out whether to pursue it and under what proposed endeavor, gathering the evidence, **drafting the petition letter and the supporting documents**, reviewing the package before you file, and answering a Request for Evidence. Written to the current USCIS adjudication standard. Distributed as a [Claude Code plugin](https://code.claude.com/docs/en/plugins) (`thepapers-niw`) and as standalone skill files for claude.ai.

Built and maintained by [The Papers Company](https://thepapers.co), the team behind [Immigration Papers](https://thepapers.co/immigration), a self-petitioner-first NIW DIY platform.

## Install

### claude.ai (web): fastest path

1. Download the skill you want from the [`dist/`](dist/) directory or from [Releases](https://github.com/thepaperscompany/niw-skills/releases). Each skill ships its own file: [`thepapers-niw-evaluate.skill`](dist/thepapers-niw-evaluate.skill) to decide whether to pursue NIW, [`thepapers-niw-package-review.skill`](dist/thepapers-niw-package-review.skill) to review an assembled package before filing, [`thepapers-niw-rfe-response.skill`](dist/thepapers-niw-rfe-response.skill) to work an RFE or NOID.
2. Open claude.ai, go to **Settings** then **Features**, scroll to **Skills**, click **Upload skill**, and upload the file. Requires a plan with code execution enabled.
3. Toggle the skill on. Done.

Claude will invoke the skill automatically when you describe an NIW case or ask any NIW-related question.

### Claude Code (CLI)

```bash
git clone https://github.com/thepaperscompany/niw-skills.git
claude --plugin-dir ./niw-skills/thepapers-niw
```

Or install from the pre-built plugin zip:

```bash
claude --plugin-dir ./niw-skills/dist/thepapers-niw.zip
```

Once loaded, the skill is invoked as `/thepapers-niw:niw-evaluate` or automatically when you describe an NIW case.

### Other agents (ChatGPT, Cursor, Codex, etc.)

The [`SKILL.md`](thepapers-niw/skills/niw-evaluate/SKILL.md) file is plain Markdown. Paste it into a system prompt or custom-GPT instruction block. Quality depends on the host model's ability to read and apply the cited authorities.

## Where you are, and what to use

NIW is a long process. Most people arrive somewhere in the middle of it, so start at the row that describes you.

### "I have heard of NIW but I do not really know what it is"

You are an international student, a postdoc, or someone working in the U.S. on a temporary visa, and a colleague mentioned this route. You do not have a CV ready and you are not sure it applies to you.

> "My senior at work mentioned NIW. I am an Indian citizen on an H-1B, working as a senior data engineer. Can you help me figure out if this is worth pursuing?"

`niw-evaluate` starts with a plain-language orientation: what the waiver is, the three questions USCIS asks, what a "proposed endeavor" means and why it is not your job title, and how NIW compares with the other routes. Then it asks for your background. It will not rate a case it has not seen.

### "I am years away, but I want to know what to build toward"

You are a master's or PhD student, or early in your career, and filing is realistically several years out. You want to know whether to shape your work around this.

> "I am a second-year PhD in materials science. I might apply for NIW eventually. Where do I stand and what should I be doing?"

`niw-evaluate` treats this as navigation rather than a verdict. You get an honest read of where the record stands today, what a realistic ceiling looks like over multiple academic years, which specific things would move it, and when to revisit. If your trajectory points at a different route, it says so.

### "I have a CV but no idea what to file under"

You have a real record and no proposed endeavor, which is the single most common blocker. The endeavor is not your occupation and not your field, and getting it wrong is the most common reason petitions are refused.

> "I am a postdoc in computational biology. I do not know what a proposed endeavor is supposed to look like for someone like me." *(attach your CV)*

`niw-evaluate` reads your record and proposes a few candidate endeavors it can actually support, each with what backs it, what is missing, and what it could become with preparation. You choose or ask for a different framing, then it runs the full analysis against your choice.

### "I have my endeavor and I want an honest assessment"

You are deciding whether to spend the filing fee.

> "Here is my profile and proposed endeavor. Run a full evaluation." *(attach both)*

`niw-evaluate` produces a structured memo: each of the three prongs analyzed on the evidence you actually have, what an adjudicator will push back on, where the case stands today, what it could become and in how long, and what to do in the next 30, 60 and 90 days.

### "I know what I am filing. Now I have to actually write it."

This is the work. The petition letter is the document USCIS reads and decides on, and the evidence only matters through what the letter argues from it.

> "I have my endeavor and my evidence. Help me write the petition letter."

`niw-petition-letter` drafts it section by section: the classification, the endeavor, and each of the three questions USCIS asks, with every claim pointing at a specific piece of your evidence. It refuses to cite evidence you do not have, keeps the argument about your endeavor separate from the argument about you, and tells you honestly which passage is weakest and what would fix it.

Three skills feed it, and you can use them in any order:

- `niw-endeavor-statement` writes the long description of what you will do in the United States and why it matters nationally, anchored to real government sources rather than to claims about your field.
- `niw-recommendation-letter` works out who should write for you and what each person should cover, so no two letters say the same thing, then drafts each one within what that person could genuinely know.
- `niw-evidence-finder` looks for government sources showing your specific work advances a named national priority, and tells you plainly when what it found is only general background.

Everything these produce is a draft for you to read, change and own. None of it is ready to send as written.

### "I have written it. Is it ready to file?"

This is the decision that costs the most to get wrong. Since a 2026 policy change, USCIS can refuse a petition outright without first asking for more evidence, so filing early no longer buys a second chance.

> "Here is my petition draft and my evidence. Is this ready to file?"

`niw-package-review` reads your actual exhibits, letters and petition draft the way a skeptical adjudicator would. It tests each prong against the evidence that is genuinely documented, quotes the specific sentences in your petition that claim more than your record supports, tracks which exhibits USCIS has actually seen, and gives you a prioritized fix list.

### "USCIS sent me a Request for Evidence and I do not know what it wants"

You have a deadline you cannot extend and one submission.

> "I got a Request for Evidence. Here it is. What is it asking for, and how do I respond?"

`niw-rfe-response` reads the deadline printed on your notice rather than calculating one, works through each contested point against the record you actually filed, stops so you can correct anything it got wrong about your own file, and then drafts. It holds two rules that decide these responses and that are easy to get backwards: your eligibility is judged on the facts as they stood the day you filed, and you cannot rewrite your proposed endeavor to fit the notice, even when the notice asks for a more detailed description of it.

## Who this is for

Your goal is a green card. These skills exist to help you decide whether this route fits your life and career, build the strongest case you can before filing, write the petition itself, and handle whatever USCIS sends back.

### Primary audience: self-petitioners doing NIW the DIY way

If you are preparing your own EB-2 National Interest Waiver petition, this is built for you. The thesis: much of the work of preparing an NIW case is standardized and rule-driven (Dhanasar three-prong analysis, evidence categorization, endeavor specificity, the preponderance burden), and a sufficiently rigorous tool can do that part well, so the judgment calls are where a licensed attorney's time is worth most.

Three sub-cohorts within DIY:

- **Filing-ready DIY self-petitioners.** You have a profile and want an honest pre-filing assessment before paying the I-140 fee.
- **Prospective DIY applicants (6–24 months from filing).** Early-career professionals, postdocs, founders pre-launch. You get a current-state verdict plus an achievable case ceiling with concrete prerequisite actions.
- **Long-horizon explorers (3–5 years from filing).** Master's and PhD international students who have heard of NIW but are years away from filing. You get a multi-year decision-support roadmap with revisit milestones.

### Secondary audience: immigration attorneys and paralegals

The plugin is also usable as a paralegal-level pre-screening tool for client intake at solo and boutique immigration firms. It produces a memo your attorney can review in 10 minutes rather than 2 hours.

### Keywords for discovery

EB-2 NIW, National Interest Waiver, DIY immigration, self-petition green card, Matter of Dhanasar, USCIS Policy Manual, immigration attorney tools, NIW evaluation, NIW DIY, proposed endeavor, endeavor statement, NIW prong analysis, AC21 H-1B extension, EB-1A comparison, master's student immigration, PhD student immigration, international student green card, paralegal NIW pre-screen.

## What's in this plugin

Eight skills. You install once and get all of them, and future updates arrive together.

Skills are listed in the order you would use them.

### The eight skills, in the order you would use them

| # | Skill | What it does |
|---|---|---|
| 1 | [`niw-evaluate`](thepapers-niw/skills/niw-evaluate) | Decide whether to pursue NIW, and under what proposed endeavor. Orientation if you are new to it, endeavor co-design if you do not have one, then a prong-by-prong assessment with a realistic ceiling and dated next steps. |
| 2 | [`niw-evidence-plan`](thepapers-niw/skills/niw-evidence-plan) | Turn that assessment into a list of documents you can actually go and get, calibrated to whether your record is academic, industry or entrepreneurial. Leaves you with an organized list of your evidence, including which items USCIS has already seen. |
| 3 | [`niw-evidence-finder`](thepapers-niw/skills/niw-evidence-finder) | Search U.S. government sources for evidence that your specific endeavor advances a named national priority, and rate honestly how strong what it found is. Needs an environment with network access. |
| 4 | [`niw-endeavor-statement`](thepapers-niw/skills/niw-endeavor-statement) | Draft the endeavor statement for the petition letter. Every national-priority claim anchored to a real source, with a self-critique beside the draft. |
| 5 | [`niw-recommendation-letter`](thepapers-niw/skills/niw-recommendation-letter) | Decide who writes about what, then draft. Each writer gets one point they alone can attest to, independent writers count for more, and no two letters cover the same ground. |
| 6 | [`niw-petition-letter`](thepapers-niw/skills/niw-petition-letter) | Draft the petition letter section by section, with every claim pointing at a specific piece of evidence you actually have. It will not cite evidence you do not have. |
| 7 | [`niw-package-review`](thepapers-niw/skills/niw-package-review) | Review the assembled package before filing, as a skeptical adjudicator would. Quotes the sentences that overclaim, tracks which exhibits USCIS has actually seen, returns a prioritized fix list and a readiness verdict. |
| 8 | [`niw-rfe-response`](thepapers-niw/skills/niw-rfe-response) | Work a Request for Evidence or Notice of Intent to Deny through to a drafted response. Reads the printed deadline, works each contested point against the record as filed, stops for your corrections, then drafts. |

Four of these write documents for you (3 through 6). The other four tell you where you stand and what to do next. You will not need all eight, and nobody uses them in one sitting.

See [CHANGELOG.md](./CHANGELOG.md) for the full release history.

## How this differs from other NIW skills

Several open-source NIW skill suites exist on GitHub. We respect them. We approach the problem differently across several dimensions:

| Dimension | Typical approach in other suites | This plugin |
|---|---|---|
| New-user onboarding | Assumes user already knows what NIW is | **Built-in orientation step** for users new to NIW, covers the three Dhanasar prongs, distinguishes proposed endeavor from endeavor statement, compares NIW against EB-1A and O-1A, and surfaces the AC21 H-1B extension framing for backlogged-country petitioners |
| EB-2 baseline check | Assumed | **Explicit baseline check** before NIW analysis. Catches foreign three-year bachelor's, experience not in the specialty, occupation not a profession, and other statutory disqualifiers under 8 C.F.R. § 204.5(k)(2) and *Matter of Katigbak*, 14 I&N Dec. 45 (Reg. Comm. 1971) |
| Reviewer model | Adversarial pre-filing review or petition audit, stress-test reasoning | **Adjudicator simulation** applying the *preponderance of the evidence* standard from *Matter of Chawathe*, 25 I&N Dec. 369, 375–76 (AAO 2010), prong by prong |
| Endeavor framing | User must arrive with their own endeavor | **Plugin proposes 2–4 options** grounded in the user's documented record before evaluating. Field-importance evidence is treated as insufficient on its own under *Matter of Dhanasar*, 26 I&N Dec. 884, 889 (AAO 2016) |
| Verdict discipline | Tiered assessment | **Verdict floor rules.** No prong is rated "Strong" or "Very Strong" unless documented evidence (excluding inferred and unsupported claims) clears preponderance |
| Long-horizon users | Out of scope | **Multi-year decision-support roadmap** for master's and PhD students 3–5 years from filing, not a "your case is weak" verdict, but a navigation tool with revisit milestones |
| Output structure | One large memo | Agentic 5-stage conversation flow that mirrors how attorneys and paralegals actually work |
| Citation hygiene | Inconsistent | **Every legal rule cites authority inline**: Dhanasar, Chawathe, USCIS Policy Manual Vol. 6 Pt. F Ch. 5 |
| Hallucination guardrails | Soft | **Hard rules** against inventing AAO decision IDs, citation counts, employer/grant facts, evidence not in the input, or disclaimer URLs |
| Audience calibration | American-academic register | **Written for an international, ESL-primary, highly-educated audience**: short sentences, technical terms explained on first use, citations in standard form, no idioms, no cultural references |

See [docs/METHODOLOGY.md](./docs/METHODOLOGY.md) for the full reasoning.

## Check our work

Most skill suites assert that they encode expert reasoning. We would rather you verify it.

The legal substance lives in [`knowledge/`](knowledge/) as plain Markdown, and every file states its source and the date it was checked:

- [`current-adjudication-bar.md`](knowledge/current-adjudication-bar.md) is distilled from the **complete public pool of AAO non-precedent NIW decisions issued 2025-01 through 2026-06**. It carries 21 numbered patterns built on verbatim quotations from those decisions. Pick any quote and look it up.
- It also states its own sampling bias in the header. This is a denial-heavy appeal pool: approved petitions and unappealed denials are invisible in it. So it calibrates how closely to scrutinize a record, and is never used to produce approval rates or a probability of approval. A suite that reports base rates from this corpus is reading it wrong.
- [`policy-alerts.md`](knowledge/policy-alerts.md) tracks the USCIS policy changes that alter how a case should be prepared, including PA-2026-05 (effective 2026-08-05), which restored officers' full discretion to deny without first issuing a Request for Evidence.

Each skill carries its own copy of the packs it needs, so a skill you upload to claude.ai works on its own. The copies are generated from `knowledge/`, and a check in our build fails if any of them drifts from the original.

## What this is: and is not

**This is:** a structured legal-analytical framework that helps you (or your attorney) understand how a USCIS adjudicator would currently view your case, where the gaps are, and what targeted preparation would change the verdict.

**This is not:**

- **Legal advice.** Immigration adjudication is discretionary. No skill, no AI, and no template can guarantee an outcome. Use this to prepare for a conversation with a licensed immigration attorney, not to replace one. See [DISCLAIMER.md](./DISCLAIMER.md).
- **A way to "beat" USCIS.** The plugin is calibrated to apply the same preponderance standard a careful adjudicator applies. If it says your case is High Risk, that is the most useful thing it can tell you.

## Want more? Use the hosted product

This plugin is the open foundation behind [thepapers.co/immigration](https://thepapers.co/immigration), which adds:

- A Kanban evidence board you can actually manage over months
- AI-assisted petition letter drafting grounded in your evidence
- Recommendation and expert letter strategy and draft generation
- RFE/NOID analysis and response support
- Tools and resources to help you engage your own licensed immigration counsel for final review and filing (the user selects their own attorney; The Papers Company is not a law firm and does not provide legal advice or operate a lawyer referral service)

The plugin and the hosted product use the same evaluation prompts, kept in sync per the policy in [CHANGELOG.md](./CHANGELOG.md).

## Repository layout

For contributors. The plugin lives at `thepapers-niw/`, skills under `thepapers-niw/skills/`, and the legal packs in [`knowledge/`](knowledge/). Inside the plugin, skills are namespaced, so `niw-evaluate` is invoked as `/thepapers-niw:niw-evaluate`.

## Contributing

We welcome contributions of:

- **AAO decisions** for the curated reference corpus, tagged by the *substantive* failure mode they teach (not procedural dismissals).
- **Anonymized profile fixtures** for evals, never with PII.
- **Methodology critiques**: particularly from practicing immigration attorneys, paralegals, and adjudicators. Open an issue.

What we will not accept: marketing copy, approved-case lists used as base rates, or content that softens the legal-rigor standard.

See [CONTRIBUTING.md](./CONTRIBUTING.md) (coming soon).

## How the legal substance was built

The evaluation logic was authored by The Papers Company against primary sources: the USCIS Policy Manual, *Matter of Dhanasar*, *Matter of Chawathe*, *Matter of Katigbak*, *Flores v. Garland*, and the complete public pool of AAO non-precedent NIW decisions issued 2025-01 through 2026-06.

Every legal pack ships in [`knowledge/`](knowledge/) with its source and the date it was checked, so you can verify any claim rather than take ours. See ["Check our work"](#check-our-work) above and [docs/METHODOLOGY.md](./docs/METHODOLOGY.md).

Outputs are research-grade legal analysis, not legal advice, and using this plugin does not create an attorney-client relationship. Have a licensed U.S. immigration attorney of your own choosing review your case before filing. See [DISCLAIMER.md](./DISCLAIMER.md).

## License

Apache License 2.0. See [LICENSE](./LICENSE) and [NOTICE](./NOTICE).

Apache 2.0 was chosen over MIT for three reasons specific to this project: (1) **trademark protection**: Section 6 explicitly says the license does not grant rights to use the contributor's trademarks, which matters for "The Papers Company" and "thepapers-niw" branding; (2) **patent grant**: Section 3 gives users certainty that no contributor can later sue them over patent claims, which lowers adoption friction for enterprise users; (3) **ecosystem alignment**: the Claude SDK and most Anthropic-ecosystem tooling use Apache 2.0.

## Disclaimer

See [DISCLAIMER.md](./DISCLAIMER.md). Short version: this is not legal advice and does not create an attorney–client relationship.
