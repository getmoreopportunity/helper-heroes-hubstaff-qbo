# Helper Heroes — Hubstaff → QBO hours

Custom API/MCP workflow. **Not** the native Hubstaff→QBO integration (payroll-only).
We do **not** create new QBO invoices. Matt updates existing QBO **recurring sales receipts**; he confirms Monday and ACH auto-sends Tuesday. Exact hours-field name in QBO is still TBD with Matt.

No live keys. No live billing. Phantom QBO client first, then Gracious Living / Peter Sotos.

**Do not touch active Hubstaff clients, projects, members, rates, or hours.** Integration setup and read-only reporting only. Never create/update/delete Hubstaff clients from this repo or workflow.

Jean Fin (Hubstaff): MCP already submitted. Review `workflow/hubstaff-qbo-hours-mvp.json` for endpoint selection (timesheets vs daily totals vs time_entries).

## Source of truth — Celdy / Matt tracker

Live Google Sheet (read-only for this repo; do not edit it from automation):

**[HELPER HEROES CLIENT LIST & TRACKER](https://docs.google.com/spreadsheets/d/1MLutxPmOUVE06xz5OKsTeoH64AAjB8ZV0ewlwNGQeUA/edit)**

- Owner: celdy@helperheroesph.com
- Shared with josh@joshcollier.ai (edit) — we still treat it as read-only
- File ID: `1MLutxPmOUVE06xz5OKsTeoH64AAjB8ZV0ewlwNGQeUA`
- Schema: [`docs/matt-celdy-tracker.md`](docs/matt-celdy-tracker.md)

This tracker is the **source of truth for VA hours and billing adjustments**. Hubstaff time is an input. Dry-run success means proposed QBO hours match what Matt would type from this sheet — not from a mystery Excel.

### DBA vs legal vs VA#

| Tracker column | Meaning |
|---|---|
| **Client Name** | DBA / franchise / location name (what Hubstaff project names usually look like) |
| **Legal Business Name** | Legal entity (QBO customer candidate) |
| **VA Name** | Assigned VA; VA# is embedded (e.g. `VA#2`) |
| **Position** | Recruiter, Scheduler, Hybrid, etc. |
| **Expected Hours Worked** | Expected hours (sparsely filled) |
| **Actual Hours Worked** | On Client List this currently holds **contracted weekly hours** (20/40), not last-week actuals |
| **HH061 (Aug 24-30)** | Current rolling **weekly hours** column (empty on 2026-08-26 ingest). Code rolls (HH053, HH061, …) |
| **Status** | Won / pipeline (Discovery Call, Interviewing, …) |

Rate columns (VA Hourly Rate to Client / HH PH / Net Pay) and phones/emails stay **out of mapping CSVs** and are **never written to QBO**.

One client can have many VA rows. Mapping is therefore VA-level in `mapping/from-tracker.csv` and project-level in `mapping/BLANK.csv`.

## Plan
1. Fill mapping from the live tracker (legal vs DBA, VA number, hours fields) joined to Hubstaff project IDs already in `mapping/BLANK.csv` (org 730247). Unmatched rows stay unmatched — no fuzzy-invented IDs.
2. Matt creates a phantom QBO client. No live ACH.
3. Josh gets Hubstaff developer access, creates the OAuth app (`http://localhost:44444/callback`), shares **only** the application ID with Jean.
4. Jean enables MCP and confirms endpoints. **MCP already submitted to Jean.**
5. Dry-run prior-week hours → phantom hours field → reconcile vs this tracker (expected / actual / weekly HH0xx). Still phantom QBO only. Still never create invoices. Still never write `pay_rate` to QBO.
6. First live pilot only after that: Gracious Living / Peter Sotos (tracker DBA **Assisting Hands North Chicago**, legal **Gracious Living Assistance Inc**, Hubstaff project **Assisting Hands Chicago North** `3889080`).

## Owners
| Who | Does |
|---|---|
| Josh | This repo + OAuth later. Never email the client secret. Never edit live Hubstaff clients. |
| Matt | Phantom QBO client + mapping rows / QBO IDs. Hours adjustments live on the Celdy tracker. |
| Celdy | Owns the live Client List & Tracker (hours/billing source of truth). |
| Jean | MCP (already submitted) + Hubstaff endpoint review. |
| Nomfundo | Hubstaff permissions / Josh developer access. |
| Andrew | Check-in. Wise payroll with Celdy is a **separate** workstream. |

## MVP success
1. Hubstaff project → correct QBO customer
2. Hubstaff member/VA → correct QBO billing line
3. Legal vs DBA handled
4. Correct hours in the correct QBO field
5. Rounding defined if included
6. Reconciles vs the Celdy tracker (expected / actual / weekly hours)
7. No live billing until phantom is validated
8. No Hubstaff client/project/member/rate/hours writes

## Mapping files
- `mapping/BLANK.csv` — 67 Hubstaff project IDs (org 730247) plus two example rows. Tracker DBA/legal filled where uniquely matched (55 of 67). QBO IDs blank. `status=draft`.
- `mapping/from-tracker.csv` — 106 VA-level Client List rows uniquely matched to those project IDs. QBO IDs blank. `status=draft`. No rates/phones/emails.
- `mapping/from-tracker-unmatched.csv` — 75 Client List rows with no unique Hubstaff project ID (notes only; no invented IDs).
- `mapping/schema.json` — includes tracker fields. Names the rate columns as tracker-only / never write to QBO.

Drive copies: https://drive.google.com/drive/folders/1deRJYHERbViADjff5KStMRamNYfY_Cd0
