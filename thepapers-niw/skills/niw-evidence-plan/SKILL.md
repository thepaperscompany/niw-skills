---
name: niw-evidence-plan
description: Turns an EB-2 NIW assessment into a concrete list of documents to gather, calibrated to whether the record is academic, industry or entrepreneurial, and writes the exhibit manifest the later skills read. Use when the user asks what evidence they need, what documents to collect, how to prepare for filing, or what to gather to close the gaps an evaluation found. Also use to start an exhibit manifest for a case. Asks only for artifacts the petitioner's field actually produces, and marks items as essential or as strengthening only when an assessment exists to justify that.
license: Apache-2.0
allowed-tools: Read, Grep, Glob, Write
compatibility: Works on any surface with filesystem access. No network access required.
---

# niw-evidence-plan

Turn an assessment into a list of documents someone can actually go and get, and write the exhibit manifest the rest of the suite reads.

Read [`references/evidence-gathering.md`](references/evidence-gathering.md) before building any list.

## What you need

- **A profile**, required.
- **An evaluation**, if one exists (`niw-case/evaluation.md`, or the output of `niw-evaluate`). This changes what you are allowed to produce.

## The rule that governs the whole output

**With an evaluation**, you know which parts of this case are weak and why, so you may emit both essential items and items that strengthen a specific identified gap.

**With only a profile**, you know what the petitioner claims and nothing about how it fares under the framework. Emit **essential items only**. Do not emit a single strengthening item: strengthening presupposes an assessment you were not given, and inventing one here is the failure this rule exists to prevent. Say plainly that the list is short because no assessment was supplied, and that running `niw-evaluate` first will produce a longer and better-targeted one.

## Workflow

```
Evidence plan:
- [ ] 1. Determine whether an assessment exists
- [ ] 2. Identify the archetype
- [ ] 3. Essential items
- [ ] 4. Strengthening items (only with an assessment)
- [ ] 5. Write the manifest
```

### Step 1: what do you have

State at the top which inputs you got, and therefore which kinds of item the list can contain.

### Step 2: archetype

Academic researcher, industry professional, entrepreneur or founder, or genuinely hybrid. State your inference and what in the record supports it. This decides the vocabulary of the whole list: do not ask a founder for citation reports, or an industry professional for editorial board invitations. Where the record genuinely spans two tracks, cover each; do not average them into a list that fits neither.

If the field does not produce the standard markers, do not pad the list with things it cannot generate and do not treat their absence as a gap. Ask for the artifacts that field does produce and that show the same thing: who adopted the work, who paid for it, who selected this person, who outside their organization relies on it.

### Step 3: essential items

Two kinds:

1. **Standard filing documents**: degree certificates and transcripts, CV, passport biographic page, current immigration status documents.
2. **Documentation for what the record already asserts.** Go through the profile claim by claim. A named patent needs its grant certificate by that number. A named employer, role or award needs the document proving it. An asserted but undocumented claim is the weakest thing in a petition.

### Step 4: strengthening items

Only with an assessment. For each identified gap, one item that closes it. Prioritize evidence of the endeavor's specific national importance and of the petitioner's documented record of success (independent citations and adoption, named deployments or users, funded roles, third-party interest) over field-level or credential-only material.

Say which gap each item closes, in the petitioner's terms.

### Step 5: write the manifest

Write or update `niw-case/evidence/manifest.md`. Include every document the petitioner already has. Leave rows for items still to be gathered marked so they are visibly not yet in hand.

```markdown
| id | title | filing status | tier | locator |
|---|---|---|---|---|
| e1 | PhD diploma, 2021 | FILING STATUS UNCONFIRMED | primary | exhibits/diploma.pdf |
| e2 | Independent citation report | NOT YET OBTAINED | primary | |
```

Ask the petitioner for the filing status of anything they have already sent to USCIS. Do not guess it. See [`references/evidence-tiers.md`](references/evidence-tiers.md) for what each status permits and for how evidence tiers work under 8 CFR 103.2(b)(2).

## Output

Group items by document type, so the list maps onto how someone actually files things: recommendation letters, publications, media coverage, government and industry reports, diplomas and degrees, awards and honors, patents, employment records, identity and status documents.

For each item give the document, who holds it, what it establishes, and why it matters here. Mark it essential or strengthening.

Close with what to do first. Anything that must come from a former employer, an institution or a recommender is the schedule risk; things the petitioner writes themselves are not.

## Rules

1. **Never output a URL, a document identifier, an accession number or a publication date you cannot verify.** You have no search tool here. Name an authoritative source by its known name so the petitioner can find it themselves.
2. **Never invent an exhibit id.** Ids you create must be recorded in the manifest.
3. Do not pad. A long list of field-level material is longer without being stronger, and it buries the items that would change the assessment.
4. No em-dashes. Short plain sentences. Explain a term of art on first use.

## Reference files

- [`references/evidence-gathering.md`](references/evidence-gathering.md): the two kinds of item, archetype vocabularies, fields without standard markers, and how to name sources. **Read first.**
- [`references/evidence-tiers.md`](references/evidence-tiers.md): basis, evidence tier, filing status and independence.
- [`references/archetype-calibration.md`](references/archetype-calibration.md): how evidence expectations differ across records.
- [`references/policy-manual-substance.md`](references/policy-manual-substance.md): the Policy Manual's own evidence categories per prong.
- [`references/current-adjudication-bar.md`](references/current-adjudication-bar.md): what actually decides these cases. Calibration only.

## What this skill does not do

- It does not assess the case. That is `niw-evaluate`.
- It does not search for anything. `niw-evidence-finder` does that, and only in environments with network access.
- It does not tell the petitioner their case is strong or weak.
