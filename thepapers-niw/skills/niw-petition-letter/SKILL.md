---
name: niw-petition-letter
description: Drafts the master petition letter for an EB-2 NIW self-petition, the central document USCIS adjudicates. Use when the user asks to draft, write or revise their petition letter, a specific prong section of it, or the argument they will file. Works section by section from the petitioner's actual exhibit manifest, ties every claim to an exhibit id that exists, keeps Prong 1 about the endeavor and Prong 2 about the person, and returns a self-critique naming the passages an adjudicator is most likely to challenge. Requires an exhibit manifest; it will build one first if none exists.
license: Apache-2.0
allowed-tools: Read, Grep, Glob, Write, Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
compatibility: Works on any surface with filesystem access. The bundled script needs python3. No network access required.
---

# niw-petition-letter

Draft the document USCIS actually adjudicates. Everything else in the package exists to support what this argues.

Read [`references/petition-structure.md`](references/petition-structure.md) and [`references/drafting-discipline.md`](references/drafting-discipline.md) before drafting.

## What you need

- **The exhibit manifest** (`niw-case/evidence/manifest.md`). Required. Without it you cannot cite anything, and a petition citing exhibits that do not exist is worse than no petition. If there is none, build one first with `niw-evidence-plan`, or ask the user to list what they have.
- **The proposed endeavor** and, if it exists, the drafted endeavor statement.
- **The petitioner's profile**, the exhibits themselves, and the recommendation letters.
- **National-importance sources**, if any. You may reference a national priority only through them.

## Workflow

```
Petition letter:
- [ ] 1. Validate the manifest
- [ ] 2. Agree the section plan
- [ ] 3. Draft section by section
- [ ] 4. Check citations
- [ ] 5. Self-critique
```

### Step 1: validate the manifest

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/check_manifest.py niw-case/evidence/manifest.md
```

Fix what it reports first. Note which exhibits are marked `NOT FILED`: those the petitioner holds but has not sent. In a petition being drafted now they are simply exhibits to file with it, but if the petition has already been filed, see the filing-date rules in [`references/filing-date-doctrine.md`](references/filing-date-doctrine.md), because nothing may then rest on a fact that arose after filing.

### Step 2: agree the section plan

Propose the sections and what each will argue, then draft only after the user agrees. Conventional order, adapted to what the record supports:

1. Introduction: who the petitioner is, the classification sought, the endeavor in concrete terms.
2. EB-2 classification: advanced degree professional, or exceptional ability. The threshold comes before any waiver argument.
3. The proposed endeavor.
4. Prong 1: substantial merit and national importance **of that endeavor**.
5. Prong 2: the petitioner's documented record and why it positions them to advance **this** endeavor.
6. Prong 3: why waiving the job offer and labor certification benefits the United States on balance.
7. Conclusion.

Sections 4, 5 and 6 carry the weight. Keep 1 and 2 short.

### Step 3: draft

One section at a time. For each, before writing, list the exhibits that will carry it. If a section has no exhibits behind it, say so rather than writing around the hole.

- **Cite inline, where the claim is made.** A sentence that asserts something and then lists four exhibits has not shown how any of them establishes it.
- Use the `[Exhibit id=e3]` token, copied exactly from the manifest.
- Build cumulatively where several exhibits reinforce one point, and say what each adds.
- Use concrete facts: names, dates, titles, institutions, numbers. "Ph.D. in Computer Science, 2018" rather than "an advanced degree".
- Never cite an exhibit that is not being filed with the petition.

**Keep Prong 1 about the endeavor and Prong 2 about the person.** Using the petitioner's achievements to argue Prong 1 is a category error adjudicators penalize. Field-level importance is framing in Prong 1, never proof.

### Step 4: check citations

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/check_manifest.py niw-case/evidence/manifest.md niw-case/petition/<section>.md
```

Run it on every section. Fix everything, then run again. Present nothing that has not passed.

### Step 5: self-critique

With the draft, briefly and honestly: the claims resting on the thinnest evidence, the passage an adjudicator is most likely to challenge and why, which prong is weakest as argued, and what document would most improve it.

Then recommend running `niw-package-review` on the assembled package, which reads the whole thing adversarially rather than section by section.

## Rules

1. **Never invent an exhibit id.** Only ids appearing verbatim in the manifest.
2. **Never assert a fact no supplied document contains.** Not an employer, a citation count, a grant role, a metric.
3. **Never cite a legal authority or quote a source from memory.** Quotation marks require a supplied source.
4. No prediction of approval, no promise of success, no probability.
5. No cover page, mailing address, signature block, exhibit index or certificate. Those depend on packet facts you do not have.
6. No em-dashes. No placeholder or boilerplate language: every sentence is about this petitioner.

## Reference files

- [`references/petition-structure.md`](references/petition-structure.md): what the letter has to do, the section order, citing exhibits, and the common failures. **Read first.**
- [`references/drafting-discipline.md`](references/drafting-discipline.md): evidence fidelity, writing for a skeptical reader, the self-critique.
- [`references/evidence-tiers.md`](references/evidence-tiers.md): basis, tier, filing status and independence.
- [`references/filing-date-doctrine.md`](references/filing-date-doctrine.md): read if the petition has already been filed.
- [`references/policy-manual-substance.md`](references/policy-manual-substance.md): Policy Manual detail per prong.
- [`references/current-adjudication-bar.md`](references/current-adjudication-bar.md): what actually decides these cases. Calibration only, never cited to the petitioner.
- [`references/legal-framework.md`](references/legal-framework.md): the citation set you may use.

## What this skill does not do

- It does not file anything, and it does not prepare forms, fees or filing mechanics.
- It does not review the assembled package adversarially. That is `niw-package-review`, and it should be run after this.
- It does not replace a licensed immigration attorney. Have counsel of your own choosing review the petition before filing.
