# Contributing

Thank you for considering it. This project touches decisions people make about their immigration status, so the bar for changes is high and the review is slow on purpose.

## What we most want

**Corrections to the legal substance.** The packs in [`knowledge/`](knowledge/) are plain Markdown, with their sources named. If a rule in them is wrong, incomplete, or has been superseded, open an issue and say which file, which passage, and what the correct position is with its authority. This is the most valuable contribution anyone can make here, and it is the only kind that can tell us we are wrong rather than merely consistent with ourselves.

Critique from practicing immigration attorneys, paralegals and former adjudicators is especially welcome. We are not asking anyone to endorse this project, and we will not describe any review as a sign-off or an endorsement. We are asking to be corrected.

**Policy updates.** USCIS changes guidance often. If a policy alert or a Policy Manual revision affects something in [`knowledge/policy-alerts.md`](knowledge/policy-alerts.md) or the packs, open an issue with the alert number and the effective date.

**Anonymized fixtures.** Realistic profiles and packages for the test cases, with all identifying detail removed. Never submit anyone's real record, including your own, and never anything containing personal data.

**Bug reports from real use.** A case where a skill gave you a wrong or unhelpful answer is worth more than a code review. Include what you asked, what it said, and what it should have said.

## What we will not accept

- Marketing copy, or anything that softens the legal-rigor standard.
- Approved-case lists, or anything proposing that outputs be scored against case outcomes. Outputs are reasoned from law and policy, not matched to results. See [docs/METHODOLOGY.md](./docs/METHODOLOGY.md).
- Claims about the quality tier of what this produces, comparisons against what a licensed professional would charge, or any suggestion that a petition prepared this way is more likely to succeed. Our build rejects these automatically, so a pull request making one will fail before review.
- Anyone's personal data, in any form.

## Making a change

Legal substance lives in [`knowledge/`](knowledge/). The copies under `thepapers-niw/skills/*/references/` are generated, so edit `knowledge/` and rebuild rather than editing a copy.

Before opening a pull request:

```bash
build/package.sh
```

That runs everything: the checks that no private path or prohibited claim reaches a public file, that the generated copies match their sources, that the quotations in the adjudication pack are unchanged, that the bundled validators still catch what they claim to, that internal links resolve, and that the plugin validates. It then rebuilds the distributable files.

If you changed a quotation in the adjudication pack, the quotation check will fail. That is deliberate. Re-verify the quotation against its source decision, then run `scripts/check_quote_integrity.py --update` in the same commit and say in the pull request why the quotation changed.

## Style

- Short plain sentences. Explain a legal term of art briefly the first time it appears.
- No em-dashes.
- Written for a reader who is an educated professional, often not a native English speaker, and not a lawyer.
- Do not use our internal vocabulary in anything a user reads. Describe what the person has to do, not how the skills are wired together.

## Reporting a security or privacy problem

Open an issue for anything routine. For something sensitive, including a case where a skill has exposed data it should not have, please contact us privately through [thepapers.co](https://thepapers.co) rather than filing publicly.

## Licensing

Contributions are accepted under the Apache License 2.0, the same license as the project. See [LICENSE](./LICENSE) and [NOTICE](./NOTICE).
