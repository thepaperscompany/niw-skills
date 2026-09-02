#!/usr/bin/env python3
"""Validate an exhibit manifest, and check that a draft cites only what exists.

Two failure modes this catches, both silent and both damaging:

  1. A draft cites an exhibit id that is not in the manifest. In a petition
     letter that becomes a citation to an exhibit USCIS will not find.
  2. A draft treats a NOT FILED exhibit as already in the record. USCIS has
     not seen that document, so relying on it overstates the filed record.

Usage:
    check_manifest.py <manifest.md>                 validate the manifest alone
    check_manifest.py <manifest.md> <draft.md> ...  also check citations in drafts

Exit codes: 0 clean, 1 problems found, 2 usage or file error.
"""

import re
import sys
from pathlib import Path

# Filing status values, and what each permits. See knowledge/evidence-tiers.md.
FILED = "filed"
UNCONFIRMED = "unconfirmed"
NOT_FILED = "not_filed"

STATUS_ALIASES = {
    "filed": FILED,
    "filed with the petition": FILED,
    "unconfirmed": UNCONFIRMED,
    "filing status unconfirmed": UNCONFIRMED,
    "not filed": NOT_FILED,
    "not_filed": NOT_FILED,
}

VALID_TIERS = {"primary", "secondary", "affidavit", "not_documented"}

# Exhibit references in a draft are written as [Exhibit id=<id>] so the id is
# unambiguous and machine-checkable. Prose names are not parsed: a name can be
# paraphrased, an id cannot.
CITATION_RE = re.compile(r"\[Exhibit id=([A-Za-z0-9_-]+)\]")


def parse_manifest(path):
    """Read a Markdown-table manifest into {id: {title, status, tier, locator}}.

    Returns (exhibits, errors). A malformed row is reported rather than
    skipped silently, because a dropped exhibit reads as a missing document.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return {}, [f"cannot read {path}: {exc}"]

    exhibits, errors = {}, []
    header_seen = False

    for lineno, line in enumerate(text.splitlines(), 1):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not header_seen:
            # First table row is the header; the row after it is the separator.
            if any(c.lower() in ("id", "exhibit id") for c in cells):
                header_seen = True
            continue
        if all(set(c) <= set("-: ") for c in cells if c):
            continue  # separator row

        if len(cells) < 3:
            errors.append(f"{path}:{lineno}: row has {len(cells)} columns, need at least 3 (id, title, filing status)")
            continue

        ex_id, title, raw_status = cells[0], cells[1], cells[2]
        tier = cells[3].strip().lower() if len(cells) > 3 and cells[3].strip() else ""
        locator = cells[4] if len(cells) > 4 else ""

        if not ex_id:
            errors.append(f"{path}:{lineno}: empty exhibit id")
            continue
        if ex_id in exhibits:
            errors.append(f"{path}:{lineno}: duplicate exhibit id '{ex_id}'")
            continue
        if not title:
            errors.append(f"{path}:{lineno}: exhibit '{ex_id}' has no title")

        status = STATUS_ALIASES.get(raw_status.lower())
        if status is None:
            errors.append(
                f"{path}:{lineno}: exhibit '{ex_id}' has filing status '{raw_status}'; "
                f"expected one of: FILED WITH THE PETITION, FILING STATUS UNCONFIRMED, NOT FILED"
            )
            status = UNCONFIRMED

        if tier and tier not in VALID_TIERS:
            errors.append(
                f"{path}:{lineno}: exhibit '{ex_id}' has tier '{tier}'; "
                f"expected one of: {', '.join(sorted(VALID_TIERS))}"
            )

        exhibits[ex_id] = {"title": title, "status": status, "tier": tier, "locator": locator, "line": lineno}

    if not header_seen:
        errors.append(f"{path}: no manifest table found (expected a Markdown table with an 'id' column)")

    return exhibits, errors


def check_draft(draft_path, exhibits):
    """Report citations in a draft that are unknown or not actually filed."""
    try:
        text = draft_path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"cannot read {draft_path}: {exc}"]

    problems = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for ex_id in CITATION_RE.findall(line):
            entry = exhibits.get(ex_id)
            if entry is None:
                known = ", ".join(sorted(exhibits)) or "(manifest is empty)"
                problems.append(
                    f"{draft_path}:{lineno}: cites unknown exhibit '{ex_id}'. Known ids: {known}"
                )
            elif entry["status"] == NOT_FILED:
                problems.append(
                    f"{draft_path}:{lineno}: cites exhibit '{ex_id}' ({entry['title']}), which is NOT FILED. "
                    f"USCIS has not seen it, so it cannot be cited as part of the record. "
                    f"Treat it as a gap the petitioner can close by submitting the document they already hold."
                )
    return problems


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip())
        return 2

    manifest_path = Path(argv[1])
    exhibits, errors = parse_manifest(manifest_path)

    for e in errors:
        print(f"ERROR  {e}")

    problems = []
    for draft in argv[2:]:
        problems.extend(check_draft(Path(draft), exhibits))
    for p in problems:
        print(f"PROBLEM  {p}")

    counts = {FILED: 0, UNCONFIRMED: 0, NOT_FILED: 0}
    for entry in exhibits.values():
        counts[entry["status"]] += 1

    print(
        f"\n{len(exhibits)} exhibits: {counts[FILED]} filed, "
        f"{counts[UNCONFIRMED]} unconfirmed, {counts[NOT_FILED]} not filed."
    )

    if errors or problems:
        print("FAILED: fix the items above before relying on this manifest.")
        return 1
    print("OK: manifest is well formed and every citation resolves to a filed or unconfirmed exhibit.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
