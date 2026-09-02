#!/usr/bin/env python3
"""Verify that every quoted excerpt in a review appears verbatim in its source.

A pre-filing review quotes the petition draft back at the petitioner to show
exactly which sentence overclaims. If the model paraphrases while presenting
the text as a quotation, the petitioner searches their own document, fails to
find the sentence, and loses confidence in a finding that may well be correct.
Worse, a near-quote can change what the passage says on the one point at issue.

This checks the mechanical part: does the quoted string actually occur in the
named file? It cannot judge whether the right passage was chosen.

Excerpt convention, which the skill instructs the model to follow:

    > "the exact continuous text copied from the source"
    > -- source: petition/prong-1.md

Usage:
    verify_quotes.py <review.md> <source-dir>

Exit codes: 0 all quotes verified, 1 one or more failed, 2 usage or file error.
"""

import difflib
import re
import sys
import unicodedata
from pathlib import Path

QUOTE_RE = re.compile(r'^>\s*"(.+)"\s*$')
SOURCE_RE = re.compile(r"^>\s*--\s*source:\s*(\S+)\s*$", re.IGNORECASE)

# Word processors and PDF extraction produce typographic variants of characters
# the model then reproduces as plain ASCII (or the reverse). Normalizing these
# prevents false failures on a quote that is genuinely correct. Nothing here
# changes which words are present.
EQUIVALENTS = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"',
    "–": "-", "—": "-", "−": "-", "‐": "-", "‑": "-",
    " ": " ", " ": " ", " ": " ", " ": " ",
    "…": "...",
}


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    for src, dst in EQUIVALENTS.items():
        text = text.replace(src, dst)
    # Collapse runs of whitespace: a line wrap in the source is not a difference
    # in the words quoted.
    return re.sub(r"\s+", " ", text).strip()


def load_sources(source_dir, exclude=None):
    """Return {relative-path: normalized-text} for every readable text file.

    The review being checked is excluded: it necessarily contains its own
    quotations, and counting it as a source turns every failure into a
    misleading "found it elsewhere" hint.
    """
    exclude = exclude.resolve() if exclude else None
    sources = {}
    for path in sorted(source_dir.rglob("*")):
        if not path.is_file():
            continue
        if exclude and path.resolve() == exclude:
            continue
        try:
            raw = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue  # binary or unreadable; nothing to quote from
        sources[str(path.relative_to(source_dir))] = normalize(raw)
    return sources


def parse_excerpts(review_path):
    """Pull (line number, quote, declared source) triples out of the review."""
    lines = review_path.read_text(encoding="utf-8").splitlines()
    excerpts, pending = [], None
    for lineno, line in enumerate(lines, 1):
        qm = QUOTE_RE.match(line)
        if qm:
            pending = (lineno, qm.group(1))
            continue
        sm = SOURCE_RE.match(line)
        if sm and pending:
            excerpts.append((pending[0], pending[1], sm.group(1)))
            pending = None
        elif line.strip() and not line.startswith(">"):
            pending = None
    return excerpts


def nearest(quote, haystack, width=90):
    """Best-matching span in haystack, to show what the source actually says."""
    matcher = difflib.SequenceMatcher(None, quote, haystack, autojunk=False)
    match = matcher.find_longest_match(0, len(quote), 0, len(haystack))
    if match.size < 12:
        return None
    start = max(0, match.b - 20)
    return haystack[start:start + width]


def main(argv):
    if len(argv) != 3:
        print(__doc__.strip())
        return 2

    review_path, source_dir = Path(argv[1]), Path(argv[2])
    if not review_path.is_file():
        print(f"ERROR: no such review file: {review_path}")
        return 2
    if not source_dir.is_dir():
        print(f"ERROR: no such source directory: {source_dir}")
        return 2

    sources = load_sources(source_dir, exclude=review_path)
    if not sources:
        print(f"ERROR: no readable text files under {source_dir}")
        return 2

    excerpts = parse_excerpts(review_path)
    if not excerpts:
        print(
            "No quoted excerpts found. If the review quotes the petition, each excerpt "
            'must be a blockquote line of the form >"..." followed by > -- source: <path>.'
        )
        return 0

    failures = 0
    for lineno, quote, declared in excerpts:
        needle = normalize(quote)

        if declared in sources:
            candidates = {declared: sources[declared]}
        else:
            # The declared path may not match exactly; fall back to any file
            # whose path ends with what was declared before reporting.
            candidates = {p: t for p, t in sources.items() if p.endswith(declared)}
            if not candidates:
                print(f"FAIL  {review_path}:{lineno}: declared source '{declared}' not found under {source_dir}")
                failures += 1
                continue

        if any(needle in text for text in candidates.values()):
            continue

        # Not in the declared source. Say whether it is anywhere at all, since
        # a misattributed real quote and an invented one need different fixes.
        elsewhere = [p for p, t in sources.items() if needle in t]
        print(f'FAIL  {review_path}:{lineno}: quote not found in {declared}')
        print(f'      quoted: "{quote[:100]}"')
        if elsewhere:
            print(f"      but it does appear in: {', '.join(elsewhere)}  (wrong source attributed)")
        else:
            hint = nearest(needle, next(iter(candidates.values())))
            if hint:
                print(f'      nearest text in source: "...{hint}..."')
            else:
                print("      no similar text in that source; the excerpt may be paraphrased or invented")
        failures += 1

    print(f"\n{len(excerpts)} excerpts checked, {failures} failed.")
    if failures:
        print("FAILED: every excerpt must be an exact continuous quotation from its named source.")
        return 1
    print("OK: every excerpt is verbatim in its named source.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
