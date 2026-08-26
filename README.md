# Helper Heroes — Hubstaff → QBO hours

Custom API/MCP workflow. **Not** the native Hubstaff→QBO integration (payroll-only).
We do **not** create new QBO invoices. Matt updates existing QBO **recurring sales receipts**; he confirms Monday and ACH auto-sends Tuesday. Exact hours-field name in QBO is still TBD with Matt.

No live keys. No live billing. Phantom QBO client first, then Gracious Living / Peter Sotos.

**Do not touch active Hubstaff clients, projects, members, rates, or hours.** Integration setup only.

Jean Fin (Hubstaff): review `workflow/hubstaff-qbo-hours-mvp.json` for endpoint selection (timesheets vs daily totals vs time_entries).

## Matt's billing spreadsheet

Matt manually enters and adjusts VA hours and billing in **his own spreadsheet**, then copies those adjustments onto the QBO recurring sales receipts. That spreadsheet is the source of truth for hours and billing tweaks. Hubstaff time is an input. It does not replace Matt's sheet. Dry-run success means proposed QBO hours match what Matt would have typed from that spreadsheet. We do not yet have a copy/link of Matt's file in this repo.

## Plan
1. Fill `mapping/BLANK.csv` from Matt's Excel (legal vs DBA, VA number, hours field).
2. Matt creates a phantom QBO client. No live ACH.
3. Josh gets Hubstaff developer access, creates the OAuth app (`http://localhost:44444/callback`), shares **only** the application ID with Jean.
4. Jean enables MCP and confirms endpoints.
5. Dry-run prior-week hours → phantom hours field → reconcile vs Matt's spreadsheet.
6. First live pilot only after that: Gracious Living / Peter Sotos.

## Owners
| Who | Does |
|---|---|
| Josh | This repo + OAuth later. Never email the client secret. Never edit live Hubstaff clients. |
| Matt | Phantom QBO client + his billing spreadsheet + mapping rows. |
| Jean | MCP + Hubstaff endpoint review. |
| Nomfundo | Hubstaff permissions / Josh developer access. |
| Andrew | Check-in. Wise payroll with Celdy is a **separate** workstream. |

## MVP success
1. Hubstaff project → correct QBO customer
2. Hubstaff member/VA → correct QBO billing line
3. Legal vs DBA handled
4. Correct hours in the correct QBO field
5. Rounding defined if included
6. Reconciles vs Matt's billing spreadsheet (the manual hours/billing adjustments)
7. No live billing until phantom is validated

Drive copies: https://drive.google.com/drive/folders/1deRJYHERbViADjff5KStMRamNYfY_Cd0
