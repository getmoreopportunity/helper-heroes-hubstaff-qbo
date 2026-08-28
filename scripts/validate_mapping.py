#!/usr/bin/env python3
"""Fail-closed mapping validator. No Hubstaff writes. No rates/emails."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

CONFIRMED_REQUIRED = [
    "hubstaff_org_id",
    "hubstaff_project_id",
    "hubstaff_user_id",
    "qbo_customer_id",
    "qbo_item_id",
    "qbo_recurring_sales_receipt_id",
]

# Column names that must never appear (PII / pay).
FORBIDDEN_HEADER_RE = re.compile(
    r"(pay[_\s-]?rate|bill[_\s-]?rate|hh[_\s-]?ph|net[_\s-]?pay|\bemail\b|\bphone\b|\biphone\b)",
    re.IGNORECASE,
)
# Cell leaks: explicit rate language or an email address. Job titles like
# "Phone Support" are not a phone number and are allowed.
FORBIDDEN_CELL_RATE_RE = re.compile(
    r"(pay[_\s-]?rate|bill[_\s-]?rate|hh\s*ph|net\s*pay)",
    re.IGNORECASE,
)
EMAIL_RE = re.compile(r"\b[^@\s,]+@[^@\s,]+\.[^@\s,]+\b")
# Telephone-shaped cells (not the word "phone" in a job title).
PHONE_CELL_RE = re.compile(
    r"(?<![A-Za-z])(?:\+?\d[\d\-\s().]{7,}\d)(?![A-Za-z])"
)

UNMATCHED_NOTE = (
    "user_id unmatched: tracker name != any Hubstaff name after VA# strip"
)


def repo_root() -> Path:
    here = Path(__file__).resolve()
    return here.parent.parent


def load_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = [{k: (v if v is not None else "") for k, v in row.items()} for row in reader]
    return fields, rows


def looks_forbidden_header(name: str) -> bool:
    return bool(FORBIDDEN_HEADER_RE.search(name or ""))


def looks_forbidden_cell(value: str) -> str | None:
    if not value:
        return None
    if FORBIDDEN_CELL_RATE_RE.search(value):
        return "rate-like"
    if EMAIL_RE.search(value):
        return "email"
    if PHONE_CELL_RE.search(value):
        return "phone"
    return None


def main() -> int:
    root = repo_root()
    mapping = root / "mapping"
    tracker_path = mapping / "from-tracker.csv"
    unmatched_path = mapping / "from-tracker-unmatched-users.csv"

    errors: list[str] = []
    warnings: list[str] = []

    if not tracker_path.is_file():
        print(f"ERROR: missing {tracker_path}", file=sys.stderr)
        return 1

    fields, rows = load_csv(tracker_path)

    for h in fields:
        if looks_forbidden_header(h):
            errors.append(f"forbidden header: {h}")

    confirmed_violations = 0
    matched = 0
    unmatched = 0
    draft_missing_user = 0
    confirmed_name_only = 0

    for i, row in enumerate(rows, start=2):
        status = (row.get("status") or "").strip()
        loc = f"{tracker_path.name}:row {i} sheet={row.get('tracker_sheet_row', '')}"

        for col, val in row.items():
            if col is None:
                continue
            kind = looks_forbidden_cell(val)
            if kind:
                errors.append(f"{loc} {kind} leak in column {col}")

        uid = (row.get("hubstaff_user_id") or "").strip()
        uname = (row.get("hubstaff_user_name") or "").strip()
        if uid:
            matched += 1
        else:
            unmatched += 1

        if status == "draft":
            if not uid:
                draft_missing_user += 1
            continue

        if status == "blocked":
            # Structurally OK with blanks; still no PII (checked above).
            continue

        if status == "confirmed":
            missing = [c for c in CONFIRMED_REQUIRED if not (row.get(c) or "").strip()]
            hours = (row.get("qbo_hours_field") or "").strip()
            if hours != "Qty":
                missing.append("qbo_hours_field!=Qty")
            if missing:
                confirmed_violations += 1
                errors.append(f"{loc} confirmed missing/invalid: {', '.join(missing)}")
            if not uid:
                confirmed_name_only += 1
                confirmed_violations += 1
                errors.append(f"{loc} confirmed name-only (empty hubstaff_user_id)")
            continue

        errors.append(f"{loc} unknown status {status!r}")

    ambiguous = 0
    if unmatched_path.is_file():
        ufields, urows = load_csv(unmatched_path)
        for h in ufields:
            if looks_forbidden_header(h):
                errors.append(f"forbidden header in unmatched-users: {h}")
        for j, row in enumerate(urows, start=2):
            for col, val in row.items():
                if col is None:
                    continue
                kind = looks_forbidden_cell(val)
                if kind:
                    errors.append(
                        f"{unmatched_path.name}:row {j} {kind} leak in column {col}"
                    )
            reason = (row.get("reason") or "").casefold()
            if "ambiguous" in reason:
                ambiguous += 1

    if draft_missing_user:
        warnings.append(
            f"{draft_missing_user} draft row(s) missing hubstaff_user_id "
            "(allowed for draft; warn only)"
        )

    print("mapping validator summary")
    print(f"  tracker rows: {len(rows)}")
    print(f"  matched: {matched}")
    print(f"  unmatched: {unmatched}")
    print(f"  ambiguous: {ambiguous}")
    print(f"  confirmed violations: {confirmed_violations}")
    print(f"  draft missing user_id: {draft_missing_user}")
    for w in warnings:
        print(f"WARNING: {w}")
    if errors:
        print("FAIL")
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
