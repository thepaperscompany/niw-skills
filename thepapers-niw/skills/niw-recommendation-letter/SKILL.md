---
name: niw-recommendation-letter
description: Plans and drafts recommendation and expert letters for an EB-2 NIW petition. Use when the user asks about recommendation letters, reference letters, expert opinion letters, who should write for them, what each letter should say, or asks to draft one. Assigns each writer a distinct point they alone can attest to, weights independent writers over supervisors and co-authors, keeps any two letters from covering the same ground, and writes only what that specific writer could plausibly know. Every draft is returned as a draft for the named writer to edit and adopt in their own words.
license: Apache-2.0
allowed-tools: Read, Grep, Glob, Write
compatibility: Works on any surface with filesystem access. No network access required.
---

# niw-recommendation-letter

Two jobs, in order: decide who writes about what, then draft. Doing the second without the first produces a set of letters that all say the same thing, which subtracts weight rather than adding it.

Read [`references/letter-strategy.md`](references/letter-strategy.md) before either.

## What you need

- **The proposed endeavor** and the petitioner's profile.
- **The list of possible writers**, with each one's relationship to the petitioner and what they have first-hand knowledge of. If the user has not given you this, ask. It is the input the whole strategy depends on.
- **An evaluation or package review**, if one exists. The gaps it names are what the letters should be aimed at.

## Stage 1: the plan

Start from the gaps, not from the list of people willing to write.

For each candidate writer, answer one question: **what single thing does this person have first-hand knowledge of that nobody else on the list does?**

Then produce a coverage map: writer, relationship, independence, the one point they are being asked to establish, and which prong it serves. Show it to the user before drafting anything.

**Independence is the main lever.** Someone who adopted, cited, funded, licensed or built on the work is usually the most valuable letter available, because they can testify to Prong 2 positioning from outside. A direct supervisor or advisor can attest to specific contributions and role, and is worth having, but carries less weight. A senior figure with no relationship helps only if they engage the endeavor specifically rather than praising the person.

**No two letters may cover the same ground.** If two writers can only speak to the same thing, use the more independent one and ask the other for something different, or for nothing. A set of letters that all say the same thing reads as coordinated rather than corroborative.

Say plainly if the writer list has a structural problem: all supervisors, nobody independent, nobody who can speak to the endeavor's prospective impact. That is worth more to the petitioner than four polished letters aimed at the same point.

## Stage 2: drafting

One letter at a time, only after the plan is agreed.

**Write only what this writer could plausibly know.** A letter asserting knowledge the writer could not have is the single most common reason USCIS discounts one entirely, and the discount tends to spread across the rest.

The petitioner's full profile is context for you, not a script. An academic advisor knows the research and the publications. An industry colleague knows the project work. An independent expert can speak to field-wide impact and to how they encountered the work. None of them knows all of it. **Three things a writer genuinely knows beats a recitation of the CV.**

A letter that carries weight:

- establishes the writer's own standing and how they came to know the work,
- describes the **proposed endeavor** and its prospective impact, not only the petitioner's past,
- gives concrete, personal detail: what specifically changed in the writer's own work or organization because of the petitioner's contribution,
- states independence explicitly where it exists, including the absence of any employment, funding or authorship relationship,
- and is corroborated by documents elsewhere in the record.

Match register to the writer. An academic writes differently from a VP of engineering, and a letter that does not sound like its signatory is a letter that reads as drafted for them.

Start directly with the letter content. No preamble, no "here is the letter".

## Stage 3: hand it over honestly

Every letter you produce is a draft. Say so, each time, in these terms: the named writer must read it, edit it, and adopt it as their own words before signing.

This is not a formality. A signature creates a strong presumption of knowledge and assent, and a record found to rest on letters the named authors did not actually write faces consequences reaching beyond a refusal to the petitioner's admissibility. Never produce a letter framed as ready to sign.

## Rules

1. **Never assert a fact the supplied record does not contain**, about the writer or the petitioner.
2. **Never invent a credential, a title, an institution or a relationship** for a writer.
3. Do not predict approval or state any probability of success.
4. Field-level importance is framing. A letter arguing the industry matters has not argued the endeavor matters.
5. No em-dashes. No generic praise: "remarkable", "world-class", "one of the best I have known" carry nothing.

## Reference files

- [`references/letter-strategy.md`](references/letter-strategy.md): assignment, independence, non-overlap, what carries weight, and integrity. **Read first.**
- [`references/drafting-discipline.md`](references/drafting-discipline.md): evidence fidelity and what never appears in a draft.
- [`references/evidence-tiers.md`](references/evidence-tiers.md): how independence is weighted alongside basis, tier and filing status.
- [`references/current-adjudication-bar.md`](references/current-adjudication-bar.md): what makes letters persuasive or worthless in practice. Calibration only.
- [`references/policy-manual-substance.md`](references/policy-manual-substance.md): the Policy Manual on letters, including interested government agency letters.

## What this skill does not do

- It does not contact anyone or send anything.
- It does not produce a letter for signature. Every output is a draft for its named writer to adopt.
- It does not assess the case. That is `niw-evaluate` or `niw-package-review`.
