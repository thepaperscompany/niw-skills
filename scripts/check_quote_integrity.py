#!/usr/bin/env python3
"""Guard the verbatim quotations in the adjudication-bar pack.

Every quotation in knowledge/current-adjudication-bar.md was copied from an AAO
decision and checked against it. The pack's credibility rests on a reader being
able to look any of them up. An ordinary edit to surrounding prose, or a
well-meaning style pass, can silently alter one.

This records a checksum over the extracted quotations. Changing a quotation
then requires deliberately updating the checksum, which makes it a decision
rather than an accident.

Usage:
    check_quote_integrity.py           verify against the stored checksum
    check_quote_integrity.py --update  store the current checksum

Exit codes: 0 verified, 1 changed, 2 usage or file error.
"""

import hashlib
import re
import sys
from pathlib import Path

PACK = Path("knowledge/current-adjudication-bar.md")
STORE = Path("knowledge/QUOTES.sha256")


def quotations(text):
    """Text inside each pair of double quotes, paired sequentially."""
    marks = [m.start() for m in re.finditer('"', text)]
    return [text[marks[i] + 1:marks[i + 1]] for i in range(0, len(marks) - 1, 2)]


def main(argv):
    if not PACK.is_file():
        print(f"ERROR: {PACK} not found (run from the repository root)")
        return 2

    quotes = quotations(PACK.read_text(encoding="utf-8"))
    digest = hashlib.sha256("\n".join(quotes).encode("utf-8")).hexdigest()

    if "--update" in argv:
        STORE.write_text(f"{digest}  {len(quotes)} quotations\n", encoding="utf-8")
        print(f"stored: {digest} over {len(quotes)} quotations")
        return 0

    if not STORE.is_file():
        print(f"ERROR: {STORE} not found. Run with --update to create it.")
        return 2

    stored = STORE.read_text(encoding="utf-8").split()[0]
    if stored != digest:
        print("FAILED: the quotations in the adjudication-bar pack changed.")
        print(f"  stored:  {stored}")
        print(f"  current: {digest} over {len(quotes)} quotations")
        print("\nIf you deliberately re-distilled the pack, re-verify every changed")
        print("quotation against its source decision, then run:")
        print("  scripts/check_quote_integrity.py --update")
        return 1

    print(f"OK: {len(quotes)} quotations unchanged ({digest[:16]}...).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
