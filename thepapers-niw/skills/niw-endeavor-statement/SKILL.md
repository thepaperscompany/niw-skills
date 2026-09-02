---
name: niw-endeavor-statement
description: Drafts the endeavor statement for an EB-2 NIW petition letter, the multi-paragraph narrative describing what the petitioner will do in the United States and why it matters nationally. Use when the user asks to write or draft their endeavor statement, their proposed endeavor section, or the Prong 1 narrative for their petition. This is the long drafted document, distinct from the short proposed endeavor chosen during niw-evaluate. Anchors every national-priority claim to a supplied source, never writes a citation or a quotation from memory, and returns a self-critique naming the draft's weakest claims alongside the draft itself.
license: Apache-2.0
allowed-tools: Read, Grep, Glob, Write
compatibility: Works on any surface with filesystem access. No network access required.
---

# niw-endeavor-statement

Draft the endeavor statement: the narrative in the petition letter that says what the petitioner will specifically do, how they will do it, and what national priority its outputs advance.

**This is not the proposed endeavor.** That is the short framing chosen during `niw-evaluate` and stored in `niw-case/endeavor.md`. This is the long document built on it. Keep the two straight, and never silently change the proposed endeavor while drafting the statement about it.

Read [`references/drafting-discipline.md`](references/drafting-discipline.md) before writing a word.

## What you need

- **The proposed endeavor** (`niw-case/endeavor.md`). Required. If there is none, stop and run `niw-evaluate` first: drafting a statement around an endeavor nobody has chosen produces a document the rest of the petition cannot support.
- **The petitioner's profile and plan**: their role, near-term and long-term goals, and how the work actually gets done.
- **National-importance sources** (`niw-case/research/national-importance.md`), if they exist. **You may reference a national priority only through a source in this file.** If it does not exist, you can still draft: write a more general framing rather than inventing an authority.

## The rule that decides whether this document helps or hurts

**You cannot verify anything from memory, so write nothing that depends on memory.**

Do not name, cite, paraphrase or quote any statute, regulation, executive order, agency program, funding opportunity, report, standard or decision that is not in the supplied sources. Do not place text in quotation marks unless it is copied from one. Do not invent report numbers, docket numbers, order numbers or program names.

Where the evidence is thin, write a general framing the endeavor advances. **A statement citing fewer real sources is far stronger than one citing a fabricated or misremembered authority**, and a fabricated authority in a document filed with a federal agency is a problem no later evidence fixes.

## Workflow

```
Endeavor statement:
- [ ] 1. Confirm the endeavor and gather the components
- [ ] 2. Draft
- [ ] 3. Check every claim against a source
- [ ] 4. Self-critique
```

### Step 1: confirm and gather

Restate the proposed endeavor back to the user verbatim and say you are drafting against it. List which components you have and which are missing, so the gaps in the draft are visible before it is written rather than after.

### Step 2: draft

Four movements, in this order. Do not simply list facts; build an argument.

1. **State the endeavor in concrete terms.** Its specific outputs, the intended beneficiaries beyond the petitioner's own employer, and the pathway by which the benefit travels. This paragraph does the most work in the document, and vagueness here is what refusals are built on.
2. **The plan.** What the petitioner will actually do: their role, near-term and long-term goals, and how the work gets done.
3. **The national priority the outputs advance.** Integrate each supplied source as context the endeavor advances, not as standalone proof of its importance. "This work advances [agency]'s [named program], which states, '[exact quotation from the source]'." Use only the agency names, titles and quotations given to you.
4. **Close** on the petitioner's intent and capacity to carry it out.

Write in continuous prose with real paragraph breaks. Formal, clear, confident where the record supports it and restrained where it does not.

### Step 3: check every claim

Go back through the draft sentence by sentence. For each claim, name what supports it. Anything supported only by your own knowledge comes out or gets rewritten as a plan rather than a fact. Anything in quotation marks must be traceable to a supplied source.

### Step 4: self-critique

Deliver alongside the draft, briefly and honestly:

- the two or three claims resting on the thinnest evidence,
- the sentence an adjudicator is most likely to challenge, and why,
- what document would close the biggest gap,
- anything you left general because no source supported making it specific.

A draft handed over without this reads as finished when it is not.

## Rules

1. Field-level importance is framing, never proof of the endeavor's importance.
2. Keep Prong 1 separate from the petitioner's credentials. This document is about the endeavor.
3. No prediction of approval, no promise of success, no probability.
4. No em-dashes. Real paragraph breaks, never a literal backslash-n.
5. No adjectives doing evidence's work: not "revolutionary", "cutting-edge", "groundbreaking".

## Reference files

- [`references/drafting-discipline.md`](references/drafting-discipline.md): evidence fidelity, writing for a skeptical reader, what never appears, and the self-critique. **Read first.**
- [`references/national-importance-sources.md`](references/national-importance-sources.md): how sources are tiered and why field-level material cannot carry Prong 1.
- [`references/policy-manual-substance.md`](references/policy-manual-substance.md): the Policy Manual on merit and national importance, with worked examples.
- [`references/current-adjudication-bar.md`](references/current-adjudication-bar.md): what actually decides these cases. Calibration only, never cited to the petitioner.
- [`references/legal-framework.md`](references/legal-framework.md): the citation set you may use.

## What this skill does not do

- It does not choose or change the proposed endeavor. `niw-evaluate` does that.
- It does not search for sources. `niw-evidence-finder` does, where network access exists.
- It does not draft the full petition letter. `niw-petition-letter` does, and uses this as one section.
