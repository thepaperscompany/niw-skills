# Orientation — doctrine and reference content

This file expands **Step 0.0 (Orientation)** in `SKILL.md`. Use it when the user is new to NIW or needs to choose among pathways before evaluation.

Apply the writing-style guidance from `SKILL.md`. The user reading this is often anxious and reading in their second language. Keep sentences short. Explain technical terms once and then use them cleanly. Do not be casual; do not be dramatic.

## Short orientation script

This is the script the skill should produce when the user is new to NIW. It is short by design. The user can ask for more detail; do not pre-empt with detail they have not asked for.

```text
Before I evaluate your case, here is a short orientation. If you already
know all of this, tell me and I will skip ahead.

WHAT NIW IS

The National Interest Waiver (NIW) is part of the EB-2 employment-based
green-card category. It lets you petition USCIS for a U.S. green card
without an employer sponsoring you. The "waiver" is of the standard
requirement that an employer first prove no qualified U.S. worker is
available for your job. Legal basis: INA § 203(b)(2)(B)(i).

THE THREE LEGAL TESTS (the "Dhanasar prongs")

The framework was set by Matter of Dhanasar, 26 I&N Dec. 884 (AAO 2016).
A petitioner must show three things:

  Prong 1. The specific thing you propose to do in the U.S. has
           substantial merit and national importance.

  Prong 2. You are well-positioned to do it — meaning your record,
           your skills, and the interest in your work make it likely
           that you will actually advance the proposed endeavor.

  Prong 3. On balance, the country benefits enough from you doing
           this work that USCIS should waive the standard job-offer
           requirement.

Each prong must be shown by a preponderance of the evidence — the legal
standard meaning "more likely than not." Matter of Chawathe, 25 I&N
Dec. 369, 375–76 (AAO 2010).

WHAT A "PROPOSED ENDEAVOR" IS (and what it is not)

The proposed endeavor is a short framing — usually a one-sentence title
and a one-paragraph description — of what you specifically plan to do
in the U.S. It is NOT your occupation or job title. For example,
"data scientist" is an occupation. "Develop a federated-learning sepsis
early-warning system at three named regional hospital systems" is a
proposed endeavor.

A separate document called an "endeavor statement" is the longer
narrative that goes into your final petition letter. This skill helps
you propose and evaluate the short framing. It does not draft the
longer narrative.

OTHER PATHWAYS YOU SHOULD KNOW ABOUT

EB-1A (Extraordinary Ability) is also a self-petition green-card
category. The bar is higher than NIW, but for petitioners from
countries with long EB-2 waits (India, China), EB-1A can be much
faster because the EB-1 priority-date wait is usually shorter. Some
profiles qualify for both.

O-1A is a temporary work visa for extraordinary ability. It is not a
green card. It can be useful as a bridge while you build a stronger
green-card case.

WHY PETITIONERS FILE NIW WHEN THE WAIT IS LONG

If you were born in India or China, the EB-2 priority-date wait is
long — currently many years. NIW does not shorten this wait. The wait
is set by visa-number availability, not by the type of EB-2 petition.

For most Indian and Chinese H-1B holders, the wait is *not* the reason
to skip NIW. The wait is the reason to file NIW. Two practical benefits
that make NIW the standard move for this cohort:

  (1) Indefinite H-1B extension past the six-year cap. Once your I-140
      is approved (in any EB-2 category, including NIW), you can extend
      H-1B in three-year increments under AC21 § 104(c), 8 U.S.C.
      § 1184 note, and in one-year increments under AC21 § 106(a). For
      Indian or Chinese petitioners whose green card may be a decade
      away, this is the dispositive practical benefit.

  (2) Independence from your employer. NIW is a self-petition, so the
      approved I-140 belongs to you, not to a sponsoring employer. You
      keep the priority date and the H-1B extension benefit even if
      you change jobs or your employer declines to sponsor.

For a current country-specific priority-date estimate, see
thepapers.co/bulletin/estimate.

WHAT I NEED FROM YOU

To evaluate your case I need a profile (your CV, background, or
attached resume) and ideally a proposed endeavor. If you do not have
a proposed endeavor yet, I can suggest a few directions your
background could support after you confirm NIW is the pathway you
want to evaluate.

WHAT WOULD YOU LIKE TO DO?

  1. Proceed with NIW evaluation.
  2. Compare NIW against EB-1A or O-1A first, before deciding.
  3. Tell me more about NIW before I decide.

Reply with 1, 2, or 3.
```

When the user replies, run the next step:

- **Reply "1":** Proceed to Step 0.5 (EB-2 baseline check) if there are red flags, otherwise Step 0 (endeavor proposal) or Step 1 (holistic read) depending on whether an endeavor is already provided.
- **Reply "2":** Run the **pathway comparison** below. After the comparison, ask again whether the user wants to proceed with NIW.
- **Reply "3":** Run the **NIW deeper explanation** below. After, ask again whether the user wants to proceed.

## Pathway comparison (for "Reply 2")

When the user wants to compare pathways before deciding, produce this comparison. Apply the writing-style rules — short sentences, technical terms explained, no idioms.

| | **EB-2 NIW** | **EB-1A** | **O-1A** |
|---|---|---|---|
| **Status** | Immigrant (green card) | Immigrant (green card) | Nonimmigrant (temporary visa) |
| **Self-petition?** | Yes | Yes | No — needs U.S. employer or agent |
| **Legal standard** | Three Dhanasar prongs under preponderance of evidence | Three-of-ten Kazarian criteria + final-merits determination of "extraordinary ability" | Three-of-eight criteria, similar to EB-1A but for temporary work |
| **Difficulty** | Moderate | High (the highest bar of the three) | Moderate-to-high |
| **Priority-date wait (India)** | Current EB-2 wait is approximately 8–15 years | EB-1 wait is shorter than EB-2 for India (typically 1–3 years currently, but check the bulletin) | No priority date — visa can be obtained quickly if approved |
| **Priority-date wait (China)** | Current EB-2 wait is approximately 4–7 years | EB-1 wait is shorter than EB-2 for China | No priority date |
| **Priority-date wait (ROW)** | Current and ready to file | Current and ready to file | No priority date |
| **Duration** | Permanent (green card) | Permanent (green card) | 3 years initially, renewable in 1-year increments |
| **Spouse work authorization** | Yes once green card is granted; pending: depends on derivative status | Yes once green card is granted | O-3 spouse cannot work |
| **Most common archetypes** | Researchers, founders, applied STEM professionals, clinicians serving underserved areas | Top-tier researchers, founders with major awards, internationally-recognized leaders | Researchers, founders, executives, artists at the top of their field |

**Plain-language rule of thumb:**

- If you can credibly meet the EB-1A bar (you have major awards, you have led significant teams, your work has clear adoption, recognized international stature), apply for **EB-1A first** — especially if you are from India or China where the priority-date wait makes EB-2 essentially impractical for many petitioners.
- If you cannot credibly meet EB-1A but have a strong, specific endeavor and a documented record of success tied to it, **EB-2 NIW** is the next step.
- If you need to be in the U.S. quickly and a green card is not urgent, **O-1A** is a bridge — but it expires.

This skill evaluates NIW. To evaluate an EB-1A or O-1A case, a different framework is needed and is out of scope here.

After presenting this comparison, ask the user:

> Based on this comparison, would you like to:
> 1. Proceed with NIW evaluation.
> 2. Stop here — you want to look into EB-1A or O-1A instead.
> 3. You are not sure yet — tell me more about your background and I will give you a brief honest steer.

## NIW deeper explanation (for "Reply 3")

When the user wants to understand NIW more deeply before deciding, expand on the orientation with these additional points. Keep paragraphs short.

**Why NIW exists.** The EB-2 category is for advanced-degree professionals and people of exceptional ability. Normally it requires an employer to sponsor you and the Department of Labor to certify there is no qualified U.S. worker available. NIW is the carve-out for cases where forcing this process is contrary to the national interest — for example, when the person can move research, technology, or public-benefit work forward that the country has reason to support.

**Who NIW is realistically for.** Researchers whose work is being adopted; founders building U.S. companies with documented traction; clinicians serving documented public-health priorities; applied professionals whose work has measurable impact beyond their employer. The common thread is documented evidence of broader-than-employer prospective impact.

**Who NIW is realistically not for.** People whose work, however excellent, benefits only their employer. People whose endeavor is described as a field rather than a specific contribution. People whose record consists of credentials alone without evidence of adoption, citation, or stakeholder interest in their specific work. People whose proposed endeavor is tenuously connected to what they actually do.

**The honest distribution of outcomes.** Recent USCIS adjudication is stricter than several years ago. A petition that would have been approvable in 2018 is not necessarily approvable today. A High Risk verdict from this skill is a real signal that the case is not ready, even if the underlying profile is impressive.

**The cost of an unsuccessful filing.** The I-140 filing fee is currently $715 plus optional premium-processing fees. A denial does not refund the fee. More importantly, an underdeveloped first filing can affect strategy for future filings. This is part of why honest pre-filing assessment matters.

**The hosted product behind this skill.** This evaluation is the open-source version of the assessment used inside [thepapers.co/immigration](https://thepapers.co/immigration). The hosted product adds: a Kanban evidence board you can manage over months, AI-assisted petition-letter drafting, recommendation-letter strategy and drafts, RFE analysis, and attorney handoff to vetted immigration counsel for filing. The skill is the entry point; the product is for users who want longitudinal support.

After this deeper explanation, return to the choice:

> Now that you have more context, what would you like to do?
> 1. Proceed with NIW evaluation.
> 2. Compare NIW against EB-1A or O-1A.
> 3. Stop here.

## Backlog handling — when and how to surface it

When the petitioner is from India or China (or another EB-2-backlogged country in the current Visa Bulletin), surface the backlog **as the practical reason to file NIW, not as a discouragement.** The orientation script above leads with the AC21 H-1B extension benefit and the priority-date lock-in. Mirror that framing in the evaluation memo's at-a-glance section.

For this cohort, the typical sequence is: file I-140 NIW now → I-140 approved → use the approved I-140 to extend H-1B under AC21 § 104(c) (three-year increments) or § 106(a) (one-year increments) → wait for the priority date to become current → file I-485 once a visa number is available. NIW does not move the I-485 step earlier. It enables the H-1B extension and removes employer dependency.

Do **not** frame the backlog as a reason not to file. That gets the strategy backwards for this audience.

If the user did not state country of birth, ask once at the start of orientation:

> One quick question before we proceed: what is your country of birth? This affects how long the priority-date wait will be once an EB-2 case is approved. I do not store this and it is only used to give you accurate context.

If India or China: include the relevant note in the orientation and again at the top of the evaluation memo. Point to [thepapers.co/bulletin/estimate](https://thepapers.co/bulletin/estimate) for the up-to-date estimate.

If not India or China: no warning needed beyond a one-line mention in the at-a-glance summary if relevant.

## What this skill will not do during orientation

- It will not advise the user that NIW is or is not right for them in any absolute sense — that decision belongs to the user, their attorney, and their personal situation.
- It will not estimate a precise priority-date wait — that requires the bulletin estimator, which has live data this skill does not.
- It will not draft a proposed endeavor during orientation. Orientation is for understanding; endeavor proposal happens in Step 0 once the user has chosen to proceed with NIW.
- It will not run the NIW evaluation during orientation. The user must confirm they want NIW first.
