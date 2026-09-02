# Verdict rubric

This file defines the assessment levels, the preponderance gate, and the ceiling logic. The skill's verdict discipline depends on applying these definitions consistently.

## Contents

- Per-prong assessment levels
- Preponderance gate
- Overall assessment levels
- Case readiness assessment
- Achievable case ceiling
- Citation requirements at verdict time

## Per-prong assessment levels

Use these exact labels. The label is gated by the preponderance test below.

| Level | Definition |
|---|---|
| **Very Strong** | Documented evidence on this prong is overwhelming and exceeds preponderance with significant margin. Multiple independent third-party indicators present. Endeavor-specific (Prong 1) or person-specific (Prong 2) evidence is detailed, recent, and uncontested. The prong is unlikely to be challenged in an RFE. |
| **Strong** | Documented evidence makes the prong more likely than not satisfied, with a comfortable margin over preponderance. At least one independent third-party indicator. The prong may invite a routine RFE challenge but the record can withstand it. |
| **Promising** | Documented evidence is meaningful but borderline on preponderance. Either the documentation is thin in one critical area, or one or two pieces are aspirational/inferred and would shift to documented with targeted gathering. The prong is likely to be challenged and may be dispositive without strengthening. |
| **Needs Development** | Documented evidence is below preponderance. The foundation exists but the case is not filing-ready on this prong. Requires substantive evidence development (new letters with specific content, new deployments, new publications, new traction). |
| **High Risk** | Documented evidence is fundamentally insufficient. Either the underlying profile does not support this prong (e.g., Prong 2 with no relevant specialty and no record of success), or the proposed endeavor is so broad/disconnected that Prong 1 cannot be assessed. The case is not filing-ready and may not be salvageable as currently framed. |

## Preponderance gate

For each prong, ask:

> Ignoring everything tagged `Inferred` or `Unsupported`, does the **documented** evidence make this prong more likely than not satisfied?

This is the test from *Matter of Chawathe*, 25 I&N Dec. at 375–76. Apply it strictly.

**If the gate fails (passes = false), the prong's assessment is capped:**

| Reason gate fails | Maximum assessment allowed |
|---|---|
| Close miss — preponderance fails by a narrow margin and 1–2 targeted evidence items would lift it | **Promising** |
| Substantive miss — preponderance fails because multiple evidence categories are thin | **Needs Development** |
| Foundational miss — preponderance fails because the underlying profile or endeavor does not support the prong | **High Risk** |

**The gate is not a tie-breaker.** It is the rule. Do not assign "Strong" because the profile looks impressive in absolute terms if the documented record does not clear preponderance.

## Overall assessment levels

The overall verdict reflects the case **as currently framed and evidenced**, not the latent ceiling.

| Level | When to use |
|---|---|
| **Very Strong Candidate** | All three prongs at "Strong" or "Very Strong." Endeavor is Specific. Independent third-party adoption and stakeholder interest are documented. Preponderance passes on all three prongs with margin. |
| **Strong Candidate** | All three prongs at "Strong" or above. Endeavor is Specific. Preponderance passes on all three. At least one independent third-party indicator per relevant prong. |
| **Promising Profile** | Preponderance passes on at least two prongs. The case has a real documented foundation. One or two targeted improvements would make it filing-ready. |
| **Needs Significant Development** | The profile has promise but multiple substantive gaps, or at least one prong's preponderance test fails on documentation. |
| **High Risk of Denial Under Current Standard** | `caseReadinessAssessment` is "Not Filing-Ready" or `topDenialRisks` contains a risk you judge more likely than not to be dispositive. |

**Hard rule:** if **any** prong's preponderance test fails, `overallAssessment.likelihood` **cannot exceed** `Needs Significant Development`.

**Hard rule:** if EB-2 baseline eligibility is in doubt (no advanced degree, no exceptional-ability claim with adequate documentation, occupation does not require a bachelor's degree for entry), the overall assessment cannot exceed `Needs Significant Development` regardless of NIW analysis. Without EB-2 eligibility there is no NIW to grant. *See* USCIS Policy Manual Vol. 6 Pt. F Ch. 5(D)(1).

## Case readiness assessment

This is independent of the per-prong assessments and the overall verdict. It answers a different question: should this case be filed today?

| Level | Definition |
|---|---|
| **Filing-Ready** | All three prongs at Promising or above with preponderance passing on all three. Endeavor is Specific. No top denial risk judged more likely than not to be dispositive. |
| **Needs Targeted Evidence Gathering Before Filing** | Profile is fundamentally sound but specific evidence items are missing. Estimated 1–6 months of targeted gathering would shift the case to Filing-Ready. |
| **Not Filing-Ready — Major Development Required** | Foundational gaps in one or more prongs, or the endeavor needs reframing before evidence can be developed. Estimated 6+ months. |

## Achievable case ceiling

The ceiling is **independent** of the current-state verdict. It answers: what is the best-achievable verdict if the petitioner closes the specified gaps?

### Ceiling rules

1. **Ceiling ≥ current-state.** The ceiling with preparation cannot be worse than the current state. If it would be, set ceiling = current state.
2. **Ceiling reflects the underlying profile, not aspirations.** Tie the ceiling to anchor facts. If the profile shows a Ph.D. with two preprints and no citations, the ceiling cannot be `Very Strong Candidate` even with 24 months of preparation — there is no plausible trajectory from preprints to "Very Strong" in 24 months.
3. **Ceiling can equal current-state if the profile is fundamentally unsuited.** Examples: no EB-2 baseline; field outside national-interest territory (note: "outside national-interest territory" is rare — most fields can support a properly framed endeavor); no documented specialty in the area of the proposed endeavor. In these cases, state directly that the ceiling cannot exceed the current state.
4. **Never use the ceiling to soften the current-state verdict.** They are computed independently and reported separately.

### Estimated prep months — calibration

| Months | Typical scenarios |
|---|---|
| **0** | Filing-ready today. Endeavor Specific. All anchor facts Documented. Preponderance passes on all three prongs. |
| **1–3** | Short targeted gathering — secure 1–2 independent expert letters with specific content; document existing adoption that is not yet in the record; reframe the endeavor narrowly. |
| **4–6** | Substantive preparation — multiple letters from independent adopters at named entities; document deployments or licensing; produce a detailed plan; gather citation breakdowns. |
| **7–12** | Major record development — produce new publications/preprints; secure a PI-role grant or significant funding; achieve first deployment with named users; build documented stakeholder interest. |
| **13–24** | Foundational development — establish a track record in the proposed endeavor space; complete a Ph.D. or major credential; transition from contributor to lead on key projects; secure investment or institutional backing. |
| **25–60** | **Long-horizon roadmap** (use only for long-horizon explorer cohort — typically master's and PhD students 3–5 years from filing). The output is a multi-year plan with revisit milestones, not a pre-filing case. Frame what to build during each phase (years 1–2, 2–3, 3–5), what to revisit at the 12-month and 24-month marks, and which alternative pathways (EB-1A in particular) become viable if the trajectory exceeds NIW requirements. Honest cap: not every profile reaches NIW-ready in 60 months. If a profile is fundamentally misaligned with NIW's requirements (e.g., commerce-only background pursuing commerce work without national-importance pathway), say so and recommend alternative pathways rather than pretending NIW becomes available with enough time. |

**Do not lowball to flatter.** A petitioner told they are 3 months away when they are 12 months away is being misled.

**For long-horizon explorers specifically:** the right output is not a verdict ("Strong Candidate in 36 months!") but a decision-support memo ("Here is where you stand today. Here are the three things that determine whether NIW becomes viable for you. Here is what to build over the next 12 months that would also support EB-1A if that becomes a better fit. Here is when to come back and re-evaluate."). The skill is not a fortune-teller; it is a navigator.

### Prerequisite quality

Each prerequisite must be:

1. **Concrete** — names a specific action, not a category. *"Secure two letters from independent adopters of your fairness-auditing toolkit at named municipal transit agencies"* — not *"strengthen recommender pool."*
2. **Falsifiable** — you can tell whether it has been completed. *"Publish a preprint applying your method to the COMPAS dataset and submit to NeurIPS"* — not *"increase publication output."*
3. **Tied to a specific gap** — names which Unsupported or Inferred claim it would shift to Documented.
4. **Realistic given the timeline** — a prerequisite that would take 18 months should not appear in a 3-month plan.

## Citation requirements at verdict time

Whenever you assign a level, briefly cite the authority that drove the call. Examples:

- *"Capped at Promising under the preponderance gate (Matter of Chawathe, 25 I&N Dec. at 375–76) because no anchor fact documents independent citation."*
- *"High Risk on Prong 1 because the record demonstrates field-level importance only (Matter of Dhanasar at 889; In Re: 37289559 at 4)."*

This discipline keeps the verdicts auditable.
