---
name: niw-evidence-finder
description: Searches authoritative U.S. government sources for evidence that a specific EB-2 NIW proposed endeavor advances a named national priority, and rates honestly how strong the result is. Use when the user asks for evidence of national importance, for government sources or programs supporting their endeavor, for help with Prong 1 evidence, or when drafting an endeavor statement or petition section that needs sources. Sorts what it finds into endeavor-specific, sub-field and field-level tiers, and says plainly when nothing better than field-level framing exists rather than dressing it up. Requires a working search tool, so it needs an environment with network access.
license: Apache-2.0
allowed-tools: WebSearch, WebFetch, Read, Write, Grep, Glob
compatibility: Requires network access and a search tool. Works in Claude Code. On claude.ai it depends on whether network access is enabled for your account. It cannot work through the Claude API, where skills have no network access.
---

# niw-evidence-finder

Find evidence that **this specific endeavor** advances a named U.S. national priority, and be honest about how strong what you found actually is.

Read [`references/national-importance-sources.md`](references/national-importance-sources.md) first.

## Before you start: can you search?

This skill depends on a working search tool. If you have none, **stop and say so.** Do not answer from memory: program names, report titles and agency initiatives change, and a plausible-sounding one that does not exist is worse than nothing. Tell the user this skill needs an environment with network access, and offer to continue without sourced evidence by naming the *kinds* of source that would help.

## The problem this solves

Prong 1 asks about the endeavor, not the field. Evidence that a technology is important, that a market is large, or that a public problem is serious is framing. Records resting on it are refused for exactly that reason.

So the question is narrower: **is there a named national priority that this endeavor's specific outputs would advance, and is that advance plausible from what the endeavor actually is?**

## Workflow

```
Evidence search:
- [ ] 1. Read the endeavor and extract what to search for
- [ ] 2. Run multiple targeted searches
- [ ] 3. Tier each source and record it
- [ ] 4. Rate sufficiency honestly
- [ ] 5. Write the memo
```

### Step 1: what to search for

Read the endeavor from `niw-case/endeavor.md` or from the user. Extract the specific problem, technology, method, population and outcome. Search for **those**, not for the field.

If what you are given is a field rather than an endeavor ("advancing AI for healthcare"), say so first. No search will fix a field-level endeavor, and finding Tier C material for it will make the petition worse by encouraging reliance on it.

### Step 2: search

Run several targeted searches across the specific problem, the technology, likely program names and the agencies that would own it. Prefer official U.S. government sources: the White House, executive agencies, Congress, GAO, national laboratories, agency strategic plans and funding announcements. News articles and academic papers are not primary evidence of a national priority.

### Step 3: tier and record

For each source: full official title, issuing body, tier with one phrase on why, the concrete connection to the endeavor's **specific outputs**, how it should be used, and a short quotation copied exactly from what you actually retrieved.

- **Tier A**, endeavor-specific: a program, funding opportunity, contract, report, strategic plan or regulation targeting the specific problem, technology, method or outcome.
- **Tier B**, sub-field priority: a national strategy naming the endeavor's specific sub-area.
- **Tier C**, field-level framing: fact sheets, mission statements, technology lists, market reports. Context only. Label it as such.

If the honest connection is only field-level, say so, even for a source you would rather present as Tier A.

### Step 4: rate it

Strong is two or more Tier A. Moderate is one Tier A or two or more Tier B. Otherwise Weak.

If it is not Strong, say what to do instead, and do not suggest finding more Tier C. The useful next step is usually letters from people at the specific programs named, or documenting adoption directly.

**If nothing above Tier C genuinely fits, say that plainly.** Do not invent a Tier A source and do not promote a Tier C one to improve the rating.

### Step 5: write the memo

Write `niw-case/research/national-importance.md`, ordered Tier A first. Include the retrieval date. Downstream skills draft only from sources in this file, so anything not in it will not be cited.

## Rules

1. **Search. Never answer from memory.**
2. **Never write a URL you did not retrieve.** Record the one the search actually returned, or record none.
3. **Never place text in quotation marks unless you copied it from the retrieved source.** Where no verbatim quotation is available, write that instead of composing one.
4. **Never invent report numbers, docket numbers, order numbers or program names.**
5. Do not upgrade a tier to make a case look better. The rating is the useful output.
6. No em-dashes. Short plain sentences.

## Reference files

- [`references/national-importance-sources.md`](references/national-importance-sources.md): the tiers, the rating, and the anti-fabrication rules. **Read first.**
- [`references/current-adjudication-bar.md`](references/current-adjudication-bar.md): why field-level evidence fails. Calibration only.
- [`references/policy-manual-substance.md`](references/policy-manual-substance.md): the Policy Manual on national importance, including the STEM and critical-technology considerations.

## What this skill does not do

- It does not assess the case or the endeavor's merits.
- It does not draft anything. `niw-endeavor-statement` and `niw-petition-letter` draft from what this produces.
- It does not search open case law or cite legal authority. Its subject is government priorities, not law.
