# NIW Skills — by The Papers Company

> Open-source skills for the U.S. EB-2 National Interest Waiver (NIW), prepared under the current USCIS adjudication standard. Distributed as a [Claude Code plugin](https://code.claude.com/docs/en/plugins) (`thepapers-niw`) and as standalone skill files for claude.ai.

Built and maintained by [The Papers Company](https://thepapers.co) — the team behind [Immigration Papers](https://thepapers.co/immigration), a self-petitioner-first NIW DIY platform.

## Who this is for

**North star:** the user's eventual goal is a successful U.S. green card. The plugin exists to help them (1) decide whether NIW is the right pathway given their life and career, (2) build a maximally strong case toward filing, (3) get through filing successfully, and (4) handle post-filing turbulence if any. Anything that does not serve those four is overhead.

### Primary audience — self-petitioners doing NIW the DIY way

If you are filing your own EB-2 National Interest Waiver petition without paying $5,000–$10,000 to an immigration attorney upfront, this plugin is built for you. The TurboTax-for-NIW thesis: most of the work of preparing an NIW case is standardized and rule-driven (Dhanasar three-prong analysis, evidence categorization, endeavor specificity, preponderance burden), and a sufficiently rigorous AI tool can do the heavy lifting so you only pay a lawyer for the parts that genuinely need judgment.

Three sub-cohorts within DIY:

- **Filing-ready DIY self-petitioners.** You have a profile and want an honest pre-filing assessment before paying the I-140 fee. The plugin produces a structured Dhanasar memo with verdict, ceiling, and concrete next steps.
- **Prospective DIY applicants (6–24 months from filing).** Early-career professionals, postdocs, founders pre-launch. Current-state verdict plus achievable case ceiling with concrete prerequisite actions.
- **Long-horizon explorers (3–5 years from filing).** Master's and PhD international students who have heard of NIW but are years away from filing. They want to know where they stand today, whether NIW is the right pathway for them (versus EB-1A or employer-sponsored EB-2), and what to build over multiple academic years to keep that pathway open. The plugin produces a multi-year decision-support roadmap with revisit milestones at the 12- and 24-month marks — not a near-term filing recommendation.

### Secondary audience — immigration attorneys and paralegals

The plugin is also usable as a paralegal-level pre-screening tool for client intake at solo and boutique immigration firms. It produces a memo your attorney can review in 10 minutes rather than 2 hours.

### Keywords for discovery

EB-2 NIW, National Interest Waiver, DIY immigration, self-petition green card, Matter of Dhanasar, USCIS Policy Manual, immigration attorney tools, NIW evaluation, NIW DIY, proposed endeavor, endeavor statement, NIW prong analysis, AC21 H-1B extension, EB-1A comparison, master's student immigration, PhD student immigration, international student green card, paralegal NIW pre-screen.

## What's in this plugin

This is a [Claude Code plugin](https://code.claude.com/docs/en/plugins) at `thepapers-niw/` containing the [`.claude-plugin/plugin.json`](thepapers-niw/.claude-plugin/plugin.json) manifest and one or more skills under [`thepapers-niw/skills/`](thepapers-niw/skills/). Skills inside a plugin are namespaced — when installed, the evaluate skill is invoked as `/thepapers-niw:niw-evaluate`.

### Currently shipped

| Skill | What it does | Status |
|---|---|---|
| [`niw-evaluate`](thepapers-niw/skills/niw-evaluate) | Honest pre-filing legal assessment of an NIW case under preponderance of the evidence — prong-by-prong analysis, what an adjudicator will challenge, and an achievable case ceiling for prospective applicants who are not yet filing-ready. Includes guided endeavor co-design when the user does not arrive with one. Handles all three audience cohorts including long-horizon explorers. | v0.2 (preview) |

### Planned next

These skills will ship into the same plugin so the user installs once and gets the suite, with future updates landing via plugin update.

| Skill | What it will do | Status |
|---|---|---|
| `niw-endeavor-statement` | Draft the multi-paragraph **endeavor statement** narrative that goes into the petition letter — distinct from the *proposed endeavor* (a short framing) selected during `niw-evaluate`. The drafting flow: (1) co-design the brief — beneficiaries, impact pathway, petitioner's role, timeline with milestones; (2) triangulate national-importance evidence from multiple authoritative sources (federal R&D priority memos, Executive Orders, OSTP priority documents, congressional testimony, agency program announcements, peer-reviewed evidence); (3) draft the statement with every claim anchored to a verifiable source; (4) produce a self-critique alongside the draft naming the weakest passages and what would strengthen them; (5) iterate based on user refinements. | v0.3 (planned) |
| `niw-evidence-finder` | Search authoritative U.S. government sources for endeavor-specific national-importance evidence — NSF, NIH, ARPA-H, DARPA, DOE program announcements; OSTP and OMB R&D priority memos; the National Critical and Emerging Technologies List; congressional committee documents; agency strategic plans. Used standalone (for evaluation prep, RFE response, or letter drafting) and called internally by the endeavor-statement and petition-letter skills. | v0.4 (planned) |
| `niw-recommendation-letter` | Strategy and drafting for expert recommendation letters. Assigns prongs to recommenders by credential and independence; ensures no two letters overlap; produces drafts that name the petitioner's specific contributions rather than generic praise. | v0.5 (planned) |
| `niw-petition-letter` | Draft the **master petition letter** — the central document USCIS adjudicates. Integrates the proposed endeavor (from evaluate), the endeavor statement (from `niw-endeavor-statement`), prong-by-prong argumentation (from evaluate's analysis), the evidence index (from `niw-evidence-finder`), and the recommendation-letter strategy (from `niw-recommendation-letter`). Produces a structured petition letter draft with full citation discipline and an audit trail tying each claim to its source. | v0.6 (planned) |
| `niw-rfe-analyzer` | Diagnose a USCIS Request for Evidence (RFE) or Notice of Intent to Deny (NOID) — what the adjudicator flagged, what specific deficiency drove it, and what the strongest response framework looks like prong by prong. Outputs a structured point-by-point response plan that addresses the actual concern rather than restating the original filing. | v0.7 (planned) |

The roadmap is sequenced so that each skill builds on the previous: evaluate establishes the framing, endeavor-statement and evidence-finder produce inputs, recommendation-letter rounds out the human-attestation layer, petition-letter is the master document, and RFE-analyzer handles post-filing turbulence. The full suite covers the customer journey from "what is NIW?" through to approval (and adjustment of status, which lives outside this plugin).

See [CHANGELOG.md](./CHANGELOG.md) for the full release history.

## Why another NIW plugin

Two skill suites already exist:

- **[VeraSuperHub/vera-eb-suite](https://github.com/VeraSuperHub/vera-eb-suite)** — 19 skills built by a NIW self-petitioner. Polished, granular. Author explicitly notes she is not a lawyer.
- **[juntoku9/claude_immigration_attorney](https://github.com/juntoku9/claude_immigration_attorney)** — 10 skills referencing Neo Global, an immigration consultancy (not a U.S.-licensed law firm).

We respect both. We approach the problem differently:

| Dimension | Other suites | This plugin |
|---|---|---|
| New-user onboarding | Assumes user knows what NIW is | **Built-in orientation step** for users new to NIW — covers the three Dhanasar prongs, distinguishes proposed endeavor from endeavor statement, compares NIW against EB-1A and O-1A, and surfaces the AC21 H-1B extension framing for backlogged-country petitioners |
| EB-2 baseline check | Assumed | **Explicit baseline check** before NIW analysis. Catches foreign three-year bachelor's, experience not in the specialty, occupation not a profession, and other statutory disqualifiers ([8 C.F.R. § 204.5(k)(2)](https://www.ecfr.gov/current/title-8/chapter-I/subchapter-B/part-204/subpart-A/section-204.5#p-204.5(k)(2)); [Matter of Katigbak, 14 I&N Dec. 45](https://www.justice.gov/d9/2022-09/3134.pdf)) |
| Reviewer model | "Adversarial pre-filing review" / "petition audit" — stress-test reasoning | **Adjudicator simulation** applying the *preponderance of the evidence* standard ([Matter of Chawathe, 25 I&N Dec. 369, 376 (AAO 2010)](https://www.justice.gov/sites/default/files/eoir/legacy/2014/07/25/3675.pdf)) prong by prong |
| Endeavor framing | User must arrive with their own endeavor | **Plugin proposes 2–4 options** grounded in the user's documented record before evaluating — mirrors the hosted product flow. Field-importance evidence is treated as insufficient on its own ([Matter of Dhanasar, 26 I&N Dec. 884, 889 (AAO 2016)](https://www.justice.gov/eoir/page-file/921616/dl)) |
| Verdict discipline | Tiered assessment | **Verdict floor rules.** No prong is rated "Strong" or "Very Strong" unless documented evidence (excluding inferred and unsupported claims) clears preponderance |
| Long-horizon users | Out of scope | **Multi-year decision-support roadmap** for master's and PhD students 3–5 years from filing — not a "your case is weak" verdict, but a navigation tool with revisit milestones |
| Output structure | Detailed sections only | Agentic 5-stage conversation flow that mirrors how attorneys and paralegals actually work |
| Citation hygiene | Inconsistent | **Every legal rule cites authority inline** — Dhanasar, Chawathe, USCIS Policy Manual Vol. 6 Pt. F Ch. 5 |
| Hallucination guardrails | Soft | **Hard rules** against inventing AAO decision IDs, citation counts, employer/grant facts, or evidence not in the input |
| Audience calibration | American-academic register | **Written for an international, ESL-primary, highly-educated audience** — short sentences, technical terms explained on first use, citations in standard form, no idioms, no cultural references |

See [docs/METHODOLOGY.md](./docs/METHODOLOGY.md) for the full reasoning.

## Install

### Claude Code — install the plugin

The plugin follows the [official Claude Code plugin specification](https://code.claude.com/docs/en/plugins) with `.claude-plugin/plugin.json` and a `skills/` subdirectory.

```bash
# Clone the repo and load the plugin directly (development)
git clone https://github.com/thepaperscompany/niw-skills.git
cd niw-skills
claude --plugin-dir ./thepapers-niw
```

Or install from the packaged zip:

```bash
claude --plugin-dir ./dist/thepapers-niw.zip
```

Once loaded, the evaluate skill is invoked as `/thepapers-niw:niw-evaluate` or automatically by Claude when the user asks about NIW. Run `/reload-plugins` to pick up plugin updates.

When the plugin is published to the [official Anthropic marketplace](https://claude.ai/settings/plugins/submit), users will be able to install with:

```bash
/plugin install thepapers-niw
```

### claude.ai (web) — install the individual skill

For users on claude.ai who do not use Claude Code, the standalone single-skill `.skill` file is available:

1. Download `thepapers-niw-evaluate.skill` from [Releases](https://github.com/thepaperscompany/niw-skills/releases) or from the [`dist/`](dist/) directory of this repository.
2. Go to [Settings → Capabilities](https://claude.ai/settings/capabilities), scroll to **Skills**, click **Upload skill**, and upload the file.
3. Toggle it on. Claude will invoke it automatically when you describe an NIW case, ask whether your profile is strong enough, or ask what to file under.

The single-skill `.skill` does not include the future-planned skills (endeavor-statement, evidence-finder, etc.). For the full suite as it grows, use the Claude Code plugin path.

### Other agents (ChatGPT, Cursor, Codex)

The [`SKILL.md`](thepapers-niw/skills/niw-evaluate/SKILL.md) file is plain Markdown. You can paste it into a system prompt or custom-GPT instruction block. Quality will depend on the host model's ability to read and apply the cited authorities.

## What this is — and is not

**This is:** a structured legal-analytical framework that helps you (or your attorney) understand how a USCIS adjudicator would currently view your case, where the gaps are, and what targeted preparation would change the verdict.

**This is not:**

- **Legal advice.** Immigration adjudication is discretionary. No skill, no AI, and no template can guarantee an outcome. Use this to prepare for a conversation with a licensed immigration attorney, not to replace one. See [DISCLAIMER.md](./DISCLAIMER.md).
- **A way to "beat" USCIS.** The plugin is calibrated to apply the same preponderance standard a careful adjudicator applies. If it says your case is High Risk, that is the most useful thing it can tell you.

## Want more? Use the hosted product

This plugin is the open foundation behind [thepapers.co/immigration](https://thepapers.co/immigration), which adds:

- A Kanban evidence board you can actually manage over months
- AI-assisted petition letter drafting grounded in your evidence
- Recommendation/expert letter strategy and draft generation
- RFE/NOID analysis and response support
- Attorney handoff to vetted immigration counsel for final review and filing

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

MIT. See [LICENSE](./LICENSE).

## Disclaimer

See [DISCLAIMER.md](./DISCLAIMER.md). Short version: this is not legal advice and does not create an attorney-client relationship.
