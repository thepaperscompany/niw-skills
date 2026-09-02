# Methodology

This document explains *why* the NIW skills in this repository are built the way they are. It exists because the design choices are deliberate, sometimes counterintuitive, and shape the quality of the legal analysis the skills produce.

If you disagree with any of these choices, open an issue. They have been argued out once; they can be argued out again.

## Table of contents

1. [Preponderance of the evidence, not adversarial stress-testing](#1-preponderance-not-adversarial)
2. [The complete pool, read for reasoning, not for outcomes](#2-the-complete-pool-read-for-reasoning-not-for-outcomes)
3. [Field importance is not endeavor importance, the single most load-bearing rule](#3-field-vs-endeavor)
4. [Verdict floor: no "Strong" without documented evidence](#4-verdict-floor)
5. [Achievable case ceiling for prospective applicants](#5-achievable-ceiling)
6. [Citation hygiene as a discipline, not decoration](#6-citation-hygiene)
7. [Hard rules against hallucinated facts](#7-anti-hallucination)
8. [Industry vs. academic profiles, same standard, different evidence](#8-industry-vs-academic)

---

## 1. Preponderance, not adversarial

**The rule we apply.** Each Dhanasar prong must be established by a preponderance of the evidence, "more likely than not." *Matter of Chawathe*, 25 I&N Dec. 369, 375–76 (AAO 2010). This is the *legal burden* the petitioner must carry. Our skill applies it as the verdict floor: if the documented evidence does not make a prong more likely than not satisfied, that prong cannot be rated "Strong" or "Very Strong," regardless of how impressive the profile looks in absolute terms.

**Why not pure adversarial stress-testing.** Both of the other major NIW skill suites use some variant of "adversarial pre-filing review" or "petition audit." Stress-tests are useful, they surface objections an adjudicator might raise, but they have two structural weaknesses:

1. **They produce hearsay-style objections, not legal analyses.** A stress-test asks "what would a skeptic say?" That can be answered with hand-wavy plausibility. Preponderance asks "would a neutral fact-finder, on this record, conclude the prong is more likely than not satisfied?" That requires reading the record and applying a defined burden.
2. **They drift toward over-cautious or over-confident verdicts depending on temperament.** Without a defined burden, the same model run twice produces different verdicts because there is no anchor. Preponderance anchors the analysis to a legal standard that does not move.

**The adversarial review still has a place.** Our skill includes an adversarial section that predicts likely RFE challenges and ranks denial risks. But it does so *after* the preponderance gate has been applied, and the adversarial review cannot upgrade a verdict the preponderance gate fails. The two are complementary, not interchangeable.

---

## 2. The complete pool, read for reasoning, not for outcomes

**What the corpus is.** The complete public pool of AAO non-precedent NIW (EB-2/B5) decisions issued 2025-01 through 2026-06: 1,040 decisions crawled and downloaded, 1,036 mechanically classified for outcome and dispositive issue, with the highest-substance analysis sections and about 35 decisions read in full. The distillation is published in [`knowledge/current-adjudication-bar.md`](../knowledge/current-adjudication-bar.md) so you can check it rather than take our word for it.

**Every quotation is verified.** Each quote in that file was copied from its source decision and checked against it during distillation. None was generated from memory. This matters because the Stanford RegLab study found leading commercial legal-research tools hallucinate 17 to 33 percent of the time even with retrieval and grounding. Verification at authoring time, in a file you can read, is a stronger guarantee than a promise about runtime behavior.

**What we distill, and what we refuse to.** We read the decisions to reconstruct how an adjudicator reasons: which arguments fail, why they fail, what the AAO says when it sustains an appeal, and which adjudicator errors the AAO reverses. We do not mine them for correlates of approval. The distinction is not cosmetic. It is why the file can record that Prong 3 is usually reserved once an earlier element fails, and that the pool contains no decision denying an otherwise-eligible NIW on separate negative discretionary factors, so the model must never invent adverse discretionary findings. A model trained to match outcomes has no way to represent either statement.

**The selection bias is stated, not hidden.** This is a denial-heavy appeal pool. Petitions approved at first instance and denials never appealed are both invisible in it. So the distillation calibrates *how closely to scrutinize a record* and is never used to produce outcome rates, base rates, or a probability of approval. Reading a skewed pool as a prior would teach the model that most NIW petitions fail, which is not true of NIW filings overall.

Three further distortions we correct for rather than inherit:

1. **Procedural versus substantive.** A large share of dismissals never reach all three prongs, reserving the rest under *INS v. Bagamasbad*, 429 U.S. 24, 25 (1976). We distill substantive failure modes and skip pure procedural dismissals, which carry little reasoning signal.
2. **Appellate posture.** AAO de novo review under *Matter of Christo's, Inc.*, 26 I&N Dec. 537, 537 n.2 (AAO 2015) asks whether the Director's decision can be sustained on the record as filed. That is a different question from whether a petitioner could qualify by filing later with a developed record, which is what most users are actually asking.
3. **Adjudicator overreach.** The pool also shows the AAO *reversing* service-center errors, such as blanket per-role attenuation findings and importing EB-1A's "contributions of major significance" into an NIW case. Distilling only the dismissals would teach the model to imitate those errors, so the corrections are recorded alongside the failures.

**Calibration, not citation.** The decisions shape how closely the model scrutinizes a record. They are not authority to hand the petitioner, and the skill does not cite these case numbers in user-facing output. It also performs no unconstrained AAO retrieval at request time: the corpus is a fixed, versioned file, refreshed deliberately, not searched live.

---

## 3. Field vs. endeavor

This is the single most load-bearing rule in our skill. It is also the rule most consistently violated in NIW filings.

**The legal source.** *Matter of Dhanasar*, 26 I&N Dec. 884, 889 (AAO 2016) explicitly directs Prong 1 analysis to focus on "the specific endeavor that the foreign national proposes to undertake", not the importance of the field, occupation, or industry.

**Why this matters.** The most common pattern in dismissals we have studied: petitioner cites field-level evidence (Big Data's $1.3 trillion impact, AI on the Critical and Emerging Technologies List, public health is important, climate change is urgent) and relies on this to establish Prong 1 national importance. The AAO routinely rejects this:

> Our assessment of national importance does not focus on the importance of a field or occupation in general, but instead "focuses on the specific endeavor that the foreign national proposes to undertake."
>
>, *In Re: 37289559*, March 7, 2025, at 4 (quoting *Matter of Dhanasar* at 889).

**What our skill does about it.** Our evaluation prompt encodes a hard rule: field-level importance materials are treated as *necessary framing* but *insufficient on their own* for Prong 1. When the record relies on field-level evidence without endeavor-specific prospective-impact documentation, the prong cannot exceed "Promising", and is typically "High Risk."

This rule alone produces visibly more accurate evaluations than the competition.

---

## 4. Verdict floor

**The rule.** Every prong has an `evidenceBasis` tag on each strength: `Documented`, `Inferred`, or `Unsupported`. Only `Documented` evidence counts toward the preponderance test. If ignoring `Inferred` and `Unsupported` items leaves a prong below preponderance, that prong's verdict is capped at "Promising" or lower. The overall verdict cannot exceed "Needs Significant Development" if any prong fails preponderance.

**Why this is a hard rule, not a soft heuristic.** Without it, the model drifts toward affirming the petitioner. The most common AI failure mode in NIW evaluation is grading on impressive-sounding credentials rather than record-supported facts. The verdict floor is the discipline that prevents this drift.

**Why we accept the cost.** The cost is that an applicant who hopes to hear "Strong Candidate" will sometimes hear "Promising Profile" or "Needs Significant Development" instead. That is the right outcome. A skill that tells petitioners what they want to hear is worse than no skill.

---

## 5. Achievable ceiling

**What it is.** After the current-state verdict, the skill produces a separate `caseCeiling` analysis: the best-achievable outcome if the petitioner closes specified gaps, with concrete prerequisites and an estimated prep timeline (0–24 months).

**Why.** Most NIW skill suites are document-in-the-bag tools, they evaluate the record the petitioner has *today*. That is useful for petitioners who are ready to file. It is useless for the large cohort of prospective applicants, international students, postdocs, early-career professionals, founders 12 months pre-launch, who could become strong candidates but are not strong candidates yet.

**The structural guardrails.**

- The ceiling never softens the current-state verdict. The two are computed independently.
- The ceiling can equal the current-state verdict if the underlying profile is fundamentally unsuited. We do not promise ceilings the profile cannot reach.
- Prerequisites must be concrete and verifiable ("secure two letters from independent adopters of your method at named agencies") rather than vague ("strengthen recommender pool").

**Why this matters strategically.** A petitioner who runs this evaluation as a first-year PhD, gets a 24-month roadmap, and returns at month 12 to re-evaluate is being served by the tool. A petitioner who is told "you're not strong enough, come back when you are" without a roadmap is not.

---

## 6. Citation hygiene

**The rule.** Every legal rule the skill applies cites its authority inline. Not as decoration, as the basis on which the rule is enforced. Common citations:

- **Burden of proof:** *Matter of Chawathe*, 25 I&N Dec. 369, 375–76 (AAO 2010).
- **Three-prong framework:** *Matter of Dhanasar*, 26 I&N Dec. 884, 889 (AAO 2016).
- **De novo appellate review:** *Matter of Christo's, Inc.*, 26 I&N Dec. 537, 537 n.2 (AAO 2015).
- **Field vs. endeavor:** *Matter of Dhanasar*, 26 I&N Dec. 884, 889 (AAO 2016).
- **Reserved-issue doctrine:** *INS v. Bagamasbad*, 429 U.S. 24, 25 (1976); *Matter of L-A-C-*, 26 I&N Dec. 516, 526 n.7 (BIA 2015).
- **NIW as discretionary:** *Flores v. Garland*, 72 F.4th 85, 88 (5th Cir. 2023).
- **Prong 2 sub-factors:** USCIS Policy Manual, Vol. 6, Pt. F, Ch. 5(D)(3).
- **STEM triad for Prong 3:** USCIS Policy Manual, Vol. 6, Pt. F, Ch. 5(D)(4).
- **EB-2 statutory basis:** INA § 203(b)(2), 8 U.S.C. § 1153(b)(2).

**Why.** Without citations, "the rule is X" is just an assertion. With citations, the user (or their attorney) can verify the rule independently. This is the difference between a research tool and a black box.

**Citation form, by case name, not by URL.** Legal citations in this repository use Bluebook-form case names (case name, volume, reporter, page, court, year) and **never** include direct URL links to specific case-text PDFs. Two reasons:

1. **Verifiability is the reader's responsibility, with stable inputs.** The reader who wants to verify a citation can search by case name in the official source of their choice (the I&N Decisions volumes published by EOIR, the USCIS adjudication archive, Westlaw, Lexis, CourtListener, Google Scholar). Pointing them at a specific URL would be convenient but only if the URL is genuinely correct, and the cost of being wrong is severe in a legal-domain repository.
2. **URL drift and content drift are real.** Government legal-text URLs change, get reorganized, and sometimes return HTTP 200 while serving the wrong document. We have no continuous-verification process for external URLs. The conservative discipline, name-only citations, eliminates both failure modes.

**Hard rule for contributors and maintainers.** Do not add URL links to specific legal-case PDFs or case-text pages in this repository (README, CHANGELOG, METHODOLOGY, NOTICE, SKILL.md, references) unless the URL has been independently verified to serve the exact correct content *at the time the link is added*. HTTP 200 status is not verification, the actual content must be read and confirmed to match the citation. When in doubt, drop the URL and keep only the case name.

---

## 7. Anti-hallucination

**The rule.** The skill will not invent:

- AAO non-precedent decision IDs.
- Citation counts, h-index values, or other quantitative facts not in the input.
- Grant roles (e.g., "PI vs. co-PI") not documented in the input.
- Employer, customer, or deployment facts not documented in the input.
- Cases beyond the well-known precedent citations listed in [§6](#6-citation-hygiene).

If the skill needs a fact to complete an analysis and the fact is not in the input, it labels the analysis as gap-dependent in `suggestedInformationToGather` rather than fabricating the fact.

**Why this is a hard rule.** Hallucinated facts in a legal-analysis tool are not "rough drafts to refine", they are misinformation that a stressed petitioner may rely on. The skill's value comes from rigor, not from sounding authoritative. When the record is silent, the skill says so.

---

## 8. Industry vs. academic

**The rule.** The Dhanasar standard applies identically across profile types. What qualifies as evidence differs. Holding an industry professional to academic evidence types (publications, citations, peer review) is an error. Holding an academic to industry evidence types (revenue, customer wins, market share) is also an error.

**What we do.**

- **Academic researchers**: independent citation breakdown, peer reviewing, editorial roles, adoption of methods/datasets, follow-on work building on the person's findings, mentions in policy documents tied to the person's specific work.
- **Industry professionals**: licensing, enterprise deployments, market share, patents cited by other inventors, industry-analyst mentions tied to the person's specific work, standards-body participation, named customer references.
- **Founders/entrepreneurs**: company milestones, revenue, hires, named customer wins, investor commitments, sector traction. Subject to the additional rule from USCIS Policy Manual Vol. 6 Pt. F Ch. 5(D)(6) that broad assertions about industry size or general job creation will not establish national importance.

The `applicantArchetype` field carries this calibration through the analysis. It is set in the upstream endeavors step (or by the user at evaluation time) and the skill uses it to calibrate Prong 2 expectations and Prong 1 framing without softening the legal standard.

---

## Updates and policy drift

The USCIS adjudication standard is not static. Policy manual updates, AAO precedent decisions, federal-court rulings on judicial review, and shifts in adjudicator practice all move the bar. The skill is dated. Re-evaluate before filing.

The current calibration reflects the standard as of the date in [CHANGELOG.md](../CHANGELOG.md). Material changes will be reflected in subsequent versions.
