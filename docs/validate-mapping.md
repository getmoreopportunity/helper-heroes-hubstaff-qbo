# Validate mapping

Run from the repo root:

```bash
python scripts/validate_mapping.py
```

Exit `0` if every `draft` / `blocked` row is structurally OK. Exit `1` on confirmed-row ID gaps, name-only confirmed rows, or any header/cell that looks like `pay_rate` / `HH PH` / `net pay` / email / a phone number.

Draft rows may have blank QBO IDs and blank `hubstaff_user_id`. The script warns (does not fail) with the count of draft rows missing `user_id`.

## User ID match rule (exact unique name only)

Fill `hubstaff_user_id` from a **read-only** Hubstaff members list. Never write to Hubstaff. Never match on email.

For each tracker `va_name`:

1. Strip wrapping quotes.
2. Strip a trailing assignment flag with regex (case-insensitive): `VA\s*#\s*\d+.*$`, then leftover punctuation.
3. Trim, collapse whitespace, casefold.
4. Hubstaff `name`: trim, collapse whitespace, casefold.
5. Match **only** if the stripped tracker name equals the Hubstaff name exactly.
6. If that Hubstaff name maps to more than one `user_id`, skip (ambiguous).
7. If zero matches, leave `hubstaff_user_id` blank and note `user_id unmatched: tracker name != any Hubstaff name after VA# strip`.

Do not match `Michael Adao` to `Michael Aeron Adao`. Do not match last-name-only. Remaining unmatched stay unmatched.
