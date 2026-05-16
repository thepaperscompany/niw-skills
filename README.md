# NIW Skills — by The Papers Company

> Open-source skills for the U.S. EB-2 National Interest Waiver (NIW), prepared under the current USCIS adjudication standard. Distributed as a [Claude Code plugin](https://code.claude.com/docs/en/plugins) (`thepapers-niw`) and as standalone skill files for claude.ai.

Built and maintained by [The Papers Company](https://thepapers.co) — the team behind [Immigration Papers](https://thepapers.co/immigration), a self-petitioner-first NIW DIY platform.

## Install

### claude.ai (web) — fastest path

1. Download [`thepapers-niw-evaluate.skill`](dist/thepapers-niw-evaluate.skill) from the [`dist/`](dist/) directory or from [Releases](https://github.com/thepaperscompany/niw-skills/releases).
2. Open [claude.ai → Settings → Capabilities](https://claude.ai/settings/capabilities), scroll to **Skills**, click **Upload skill**, upload the file.
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

## How to use it

The skill is a guided multi-turn conversation, not a single-shot evaluator. You can start at any of these points:

**If you have heard of NIW but are not sure what it is:**

> "My senior at work mentioned NIW. I'm an Indian H-1B holder, senior data engineer at a tech company. Can you help me figure out if I should pursue this?"

The skill walks you through what NIW is, the three Dhanasar prongs, what a proposed endeavor means, why specificity matters, and — for Indian and Chinese H-1B petitioners — why an approved I-140 unlocks indefinite H-1B extension under AC21. Then it asks for your profile.

**If you have your CV and want to know what to file under:**

> "I'm a postdoc in computational biology. I don't really know what a 'proposed endeavor' is supposed to look like for someone like me. Can you look at my profile and help me figure out what I should file under?" *[attach your CV]*

The skill reads your profile and proposes 2–4 proposed endeavor options grounded in what your record can credibly support, with strengths, weaknesses, and an anticipated best-case outcome for each. You pick one (or ask for a different framing), and it runs the full prong-by-prong evaluation against the selected option.

**If you have a proposed endeavor and want a full evaluation:**

> "Here is my profile and proposed endeavor. Please run a full evaluation against all three Dhanasar prongs." *[attach CV + endeavor description]*

The skill produces a structured memo: prong-by-prong analysis under preponderance of the evidence, what an adjudicator will challenge, current verdict, achievable case ceiling in N months, and what to do in the next 30/60/90 days.

**If you are 3–5 years from filing (master's or PhD student):**

> "I'm a second-year PhD in [field]. I might apply for NIW in a few years but I'm not sure where I stand or whether NIW is even right for me."

The skill produces a multi-year decision-support roadmap with revisit milestones at 12 and 24 months, including comparison to alternative pathways (EB-1A in particular) if your trajectory exceeds NIW requirements. It is calibrated as a navigator for this cohort, not a fortune-teller.

## Who this is for

**North star:** the user's eventual goal is a successful U.S. green card. The plugin exists to help users (1) decide whether NIW is the right pathway given their life and career, (2) build a maximally strong case toward filing, (3) get through filing successfully, and (4) handle post-filing turbulence if any. Anything that does not serve those four is overhead.

### Primary audience — self-petitioners doing NIW the DIY way

If you are filing your own EB-2 National Interest Waiver petition without paying $5,000–$10,000 to an immigration attorney upfront, this is built for you. The thesis: most of the work of preparing an NIW case is standardized and rule-driven (Dhanasar three-prong analysis, evidence categorization, endeavor specificity, preponderance burden), and a sufficiently rigorous AI tool can do the heavy lifting so you only pay a lawyer for the parts that genuinely need judgment.

Three sub-cohorts within DIY:

- **Filing-ready DIY self-petitioners.** You have a profile and want an honest pre-filing assessment before paying the I-140 fee.
- **Prospective DIY applicants (6–24 months from filing).** Early-career professionals, postdocs, founders pre-launch. You get a current-state verdict plus an achievable case ceiling with concrete prerequisite actions.
- **Long-horizon explorers (3–5 years from filing).** Master's and PhD international students who have heard of NIW but are years away from filing. You get a multi-year decision-support roadmap with revisit milestones.

### Secondary audience — immigration attorneys and paralegals

The plugin is also usable as a paralegal-level pre-screening tool for client intake at solo and boutique immigration firms. It produces a memo your attorney can review in 10 minutes rather than 2 hours.

### Keywords for discovery

EB-2 NIW, National Interest Waiver, DIY immigration, self-petition green card, Matter of Dhanasar, USCIS Policy Manual, immigration attorney tools, NIW evaluation, NIW DIY, proposed endeavor, endeavor statement, NIW prong analysis, AC21 H-1B extension, EB-1A comparison, master's student immigration, PhD student immigration, international student green card, paralegal NIW pre-screen.

## What's in this plugin

The repo at `thepapers-niw/` is a [Claude Code plugin](https://code.claude.com/docs/en/plugins) with the [`.claude-plugin/plugin.json`](thepapers-niw/.claude-plugin/plugin.json) manifest and skills under [`thepapers-niw/skills/`](thepapers-niw/skills/). Inside the plugin, skills are namespaced — the evaluate skill is invoked as `/thepapers-niw:niw-evaluate`.

### Currently shipped

| Skill | What it does | Status |
|---|---|---|
| [`niw-evaluate`](thepapers-niw/skills/niw-evaluate) | Honest pre-filing legal assessment of an NIW case under preponderance of the evidence — prong-by-prong analysis, what an adjudicator will challenge, and an achievable case ceiling for prospective applicants who are not yet filing-ready. Includes guided endeavor co-design when the user does not arrive with one. Handles all three audience cohorts including long-horizon explorers. | v0.2 (preview) |

### Planned next

These ship into the same plugin so the user installs once and gets the suite, with future updates landing via plugin update.

| Skill | What it will do | Status |
|---|---|---|
| `niw-endeavor-statement` | Draft the multi-paragraph **endeavor statement** narrative that goes into the petition letter — distinct from the *proposed endeavor* (a short framing) selected during `niw-evaluate`. Co-designs the brief, triangulates national-importance evidence from multiple authoritative sources, drafts with every claim anchored to a verifiable source, and includes a self-critique alongside the draft. | v0.3 (planned) |
| `niw-evidence-finder` | Search authoritative U.S. government sources (federal R&D priority memos, Executive Orders, OSTP priority documents, congressional testimony, agency program announcements, the National Critical and Emerging Technologies List) for endeavor-specific national-importance evidence. Used standalone and called internally by the endeavor-statement and petition-letter skills. | v0.4 (planned) |
| `niw-recommendation-letter` | Strategy and drafting for expert recommendation letters. Assigns prongs to recommenders by credential and independence; ensures no two letters overlap; produces drafts that name the petitioner's specific contributions. | v0.5 (planned) |
| `niw-petition-letter` | Draft the **master petition letter** — the central document USCIS adjudicates. Integrates the proposed endeavor, the endeavor statement, prong-by-prong argumentation, the evidence index, and the recommendation-letter strategy into a single structured petition letter with full citation discipline. | v0.6 (planned) |
| `niw-rfe-analyzer` | Diagnose a USCIS Request for Evidence (RFE) or Notice of Intent to Deny (NOID) and produce a structured point-by-point response framework that addresses the actual concern. | v0.7 (planned) |

The roadmap is sequenced so each skill builds on the previous: evaluate establishes the framing, endeavor-statement and evidence-finder produce inputs, recommendation-letter rounds out the human-attestation layer, petition-letter is the master document, and RFE-analyzer handles post-filing turbulence. The full suite covers the customer journey from "what is NIW?" through to approval.

See [CHANGELOG.md](./CHANGELOG.md) for the full release history.

## How this differs from other NIW skills

Several open-source NIW skill suites exist on GitHub. We respect them. We approach the problem differently across several dimensions:

| Dimension | Typical approach in other suites | This plugin |
|---|---|---|
| New-user onboarding | Assumes user already knows what NIW is | **Built-in orientation step** for users new to NIW — covers the three Dhanasar prongs, distinguishes proposed endeavor from endeavor statement, compares NIW against EB-1A and O-1A, and surfaces the AC21 H-1B extension framing for backlogged-country petitioners |
| EB-2 baseline check | Assumed | **Explicit baseline check** before NIW analysis. Catches foreign three-year bachelor's, experience not in the specialty, occupation not a profession, and other statutory disqualifiers under 8 C.F.R. § 204.5(k)(2) and *Matter of Katigbak*, 14 I&N Dec. 45 (Reg. Comm. 1971) |
| Reviewer model | Adversarial pre-filing review or petition audit — stress-test reasoning | **Adjudicator simulation** applying the *preponderance of the evidence* standard from *Matter of Chawathe*, 25 I&N Dec. 369, 375–76 (AAO 2010), prong by prong |
| Endeavor framing | User must arrive with their own endeavor | **Plugin proposes 2–4 options** grounded in the user's documented record before evaluating. Field-importance evidence is treated as insufficient on its own under *Matter of Dhanasar*, 26 I&N Dec. 884, 889 (AAO 2016) |
| Verdict discipline | Tiered assessment | **Verdict floor rules.** No prong is rated "Strong" or "Very Strong" unless documented evidence (excluding inferred and unsupported claims) clears preponderance |
| Long-horizon users | Out of scope | **Multi-year decision-support roadmap** for master's and PhD students 3–5 years from filing — not a "your case is weak" verdict, but a navigation tool with revisit milestones |
| Output structure | One large memo | Agentic 5-stage conversation flow that mirrors how attorneys and paralegals actually work |
| Citation hygiene | Inconsistent | **Every legal rule cites authority inline** — Dhanasar, Chawathe, USCIS Policy Manual Vol. 6 Pt. F Ch. 5 |
| Hallucination guardrails | Soft | **Hard rules** against inventing AAO decision IDs, citation counts, employer/grant facts, evidence not in the input, or disclaimer URLs |
| Audience calibration | American-academic register | **Written for an international, ESL-primary, highly-educated audience** — short sentences, technical terms explained on first use, citations in standard form, no idioms, no cultural references |

See [docs/METHODOLOGY.md](./docs/METHODOLOGY.md) for the full reasoning.

## What this is — and is not

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

## Contributing

We welcome contributions of:

- **AAO decisions** for the curated reference corpus — tagged by the *substantive* failure mode they teach (not procedural dismissals).
- **Anonymized profile fixtures** for evals — never with PII.
- **Methodology critiques** — particularly from practicing immigration attorneys, paralegals, and adjudicators. Open an issue.

What we will not accept: marketing copy, approved-case lists used as base rates, or content that softens the legal-rigor standard.

See [CONTRIBUTING.md](./CONTRIBUTING.md) (coming soon).

## Legal review

The legal substance of this plugin has been reviewed by licensed U.S. immigration counsel before release. The evaluation logic was authored by The Papers Company and built against the USCIS Policy Manual, *Matter of Dhanasar*, *Matter of Chawathe*, *Matter of Katigbak*, *Flores v. Garland*, and recent AAO non-precedent decisions.

Outputs are research-grade legal analysis, not legal advice. See [DISCLAIMER.md](./DISCLAIMER.md).

## License

Apache License 2.0. See [LICENSE](./LICENSE) and [NOTICE](./NOTICE).

Apache 2.0 was chosen over MIT for three reasons specific to this project: (1) **trademark protection** — Section 6 explicitly says the license does not grant rights to use the contributor's trademarks, which matters for "The Papers Company" and "thepapers-niw" branding; (2) **patent grant** — Section 3 gives users certainty that no contributor can later sue them over patent claims, which lowers adoption friction for enterprise users; (3) **ecosystem alignment** — the Claude SDK and most Anthropic-ecosystem tooling use Apache 2.0.

## Disclaimer

See [DISCLAIMER.md](./DISCLAIMER.md). Short version: this is not legal advice and does not create an attorney–client relationship.
