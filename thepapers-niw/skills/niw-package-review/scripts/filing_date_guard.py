#!/usr/bin/env python3
"""Flag advice that depends on facts postdating the filing date.

Once a petition is filed, eligibility is judged on the facts as they stood on
the filing date (8 CFR 103.2(b)(12); Matter of Katigbak), and the proposed
endeavor is fixed by the petition as filed (Matter of Izummi). The intuitive
fixes for a weak filed record violate both: send the updated citation count,
sharpen the endeavor description the officer just called vague.

This flags candidates for human review. It reports, it does not decide: a date
after the filing date is often legitimate, because evidence created now may
document a fact that already existed then. The point is that each one is a
deliberate choice rather than an oversight.

Usage:
    filing_date_guard.py <CASE.md> <document.md> [document.md ...]
    filing_date_guard.py --filing-date YYYY-MM-DD <document.md> [...]

Exit codes: 0 nothing flagged, 1 items to review, 2 usage or file error.
"""

import re
import sys
from datetime import date
from pathlib import Path

FILING_DATE_RE = re.compile(r"^\s*[-*]?\s*filing date\s*:\s*(\d{4}-\d{2}-\d{2})\s*$", re.IGNORECASE | re.MULTILINE)
ISO_DATE_RE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], 1)}
PROSE_DATE_RE = re.compile(
    r"\b(" + "|".join(MONTHS) + r")\s+(\d{1,2}),?\s+(\d{4})\b", re.IGNORECASE)

# Phrases that describe re-scoping the endeavor rather than evidencing it.
# Matter of Izummi bars the change; the notice asking for "a detailed
# description" is not an invitation to describe a different endeavor.
RESCOPE_PATTERNS = [
    (r"\b(broaden|narrow|reframe|re-?scope|restate|redefine|sharpen|revise|rewrite)\w*\s+"
     r"(the\s+|your\s+|their\s+)?(proposed\s+)?endeavor\b", "proposes changing the endeavor"),
    (r"\bnew(ly)?\s+(proposed\s+)?endeavor\b", "refers to a new endeavor"),
    (r"\bchange\s+(the\s+|your\s+)?(proposed\s+)?endeavor\b", "proposes changing the endeavor"),
]

# Evidence categories that are only ever post-filing facts when they are new.
POST_FILING_EVIDENCE = [
    (r"\b(updated|refreshed|current|new)\s+(citation|bibliometric|scholar|h-index|h index)\w*",
     "refreshed citation or bibliometric data cannot establish filing-date eligibility"),
    (r"\b(recent|new|since filing)\s+(publication|paper|article)s?\b",
     "publications after filing cannot establish filing-date eligibility"),
    (r"\b(promotion|new role|new position|new title)\b",
     "a role obtained after filing cannot establish filing-date eligibility"),
    (r"\bnewly\s+awarded\s+(funding|grant)\w*", "funding awarded after filing cannot establish eligibility"),
]


def read_filing_date(case_path):
    try:
        text = case_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: cannot read {case_path}: {exc}")
        return None
    m = FILING_DATE_RE.search(text)
    if not m:
        return None
    y, mo, d = (int(p) for p in m.group(1).split("-"))
    try:
        return date(y, mo, d)
    except ValueError:
        print(f"ERROR: {case_path} has an invalid filing date: {m.group(1)}")
        return None


def dates_in(line):
    """Every date mentioned on a line, as (date, literal-text) pairs."""
    found = []
    for m in ISO_DATE_RE.finditer(line):
        try:
            found.append((date(int(m.group(1)), int(m.group(2)), int(m.group(3))), m.group(0)))
        except ValueError:
            continue
    for m in PROSE_DATE_RE.finditer(line):
        try:
            found.append((date(int(m.group(3)), MONTHS[m.group(1).lower()], int(m.group(2))), m.group(0)))
        except ValueError:
            continue
    return found


def scan(doc_path, filing_date):
    try:
        lines = doc_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        print(f"ERROR: cannot read {doc_path}: {exc}")
        return 0

    flagged = 0
    for lineno, line in enumerate(lines, 1):
        low = line.lower()

        for d, literal in dates_in(line):
            if d > filing_date:
                print(f"REVIEW  {doc_path}:{lineno}: mentions {literal}, after the filing date {filing_date}")
                print(f"        {line.strip()[:140]}")
                print("        Confirm this documents a fact that already existed at filing, and say so on its face.")
                flagged += 1

        for pattern, why in RESCOPE_PATTERNS:
            if re.search(pattern, low):
                print(f"REVIEW  {doc_path}:{lineno}: {why} (Matter of Izummi bars a material change)")
                print(f"        {line.strip()[:140]}")
                flagged += 1
                break

        for pattern, why in POST_FILING_EVIDENCE:
            if re.search(pattern, low):
                print(f"REVIEW  {doc_path}:{lineno}: {why}")
                print(f"        {line.strip()[:140]}")
                flagged += 1
                break

    return flagged


def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__.strip())
        return 2

    if args[0] == "--filing-date":
        if len(args) < 3:
            print(__doc__.strip())
            return 2
        try:
            y, mo, d = (int(p) for p in args[1].split("-"))
            filing_date = date(y, mo, d)
        except ValueError:
            print(f"ERROR: --filing-date expects YYYY-MM-DD, got '{args[1]}'")
            return 2
        docs = args[2:]
    else:
        case_path = Path(args[0])
        if not case_path.is_file():
            print(f"ERROR: no such case file: {case_path}")
            return 2
        filing_date = read_filing_date(case_path)
        if filing_date is None:
            print(
                f"No filing date in {case_path}. The petition is not filed, or the date is not recorded.\n"
                "Filing-date rules do not apply to a pre-filing review. Nothing to check."
            )
            return 0
        docs = args[1:]

    if not docs:
        print("ERROR: no documents to scan")
        return 2

    print(f"Filing date: {filing_date}\n")
    total = sum(scan(Path(d), filing_date) for d in docs)

    if total:
        print(f"\n{total} item(s) to review.")
        print("Each must either document a fact that existed at filing, stated on its face, or be removed.")
        return 1
    print("OK: nothing depends on a post-filing fact, and no re-scoping language found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
