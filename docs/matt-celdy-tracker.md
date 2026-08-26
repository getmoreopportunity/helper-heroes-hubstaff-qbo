# Celdy / Matt tracker schema

Live source of truth for Helper Heroes **VA hours and billing adjustments**. Hubstaff is an input. This sheet is what Matt types from when he updates QBO recurring sales receipts.

**Do not dump PII here** (no phones, emails, or pay rates). **Do not edit the live Sheet** from this repo.

## Live Sheet

| | |
|---|---|
| Title | HELPER HEROES CLIENT LIST & TRACKER |
| Owner | celdy@helperheroesph.com |
| Shared with | josh@joshcollier.ai (edit) — automation is read-only |
| File ID | `1MLutxPmOUVE06xz5OKsTeoH64AAjB8ZV0ewlwNGQeUA` |
| URL | https://docs.google.com/spreadsheets/d/1MLutxPmOUVE06xz5OKsTeoH64AAjB8ZV0ewlwNGQeUA/edit |
| Ingested | 2026-08-26 (xlsx export, all 13 tabs) |

Workbook started as a purchased CRM template (Digital Bee Solutions); Helper Heroes data lives mainly on **Client List** (plus filtered **Won** / **Leads** / **Not Ready**).

## Tabs

| Tab | Header row | What it is | Non-empty rows (approx) |
|---|---|---|---|
| **Client List** | Row 18 | **Canonical client/VA roster + hours.** Dashboard counts in rows 2–17 (Won 71, etc.). Active Clients / Active VAs KPI on rows 16–17. | 181 data rows below the header (plus totals). KPI: 73 active clients / 134 active VAs. |
| **Won** | Row 18 | Filtered won/active view. **Older hours headers** (`Potential Hours`, `Hours Per Week`, weekly col `HH053 (June 29- July 5)`). Do not treat as current weekly hours. | ~147 nonempty; KPI 70 active clients / 121 active VAs. |
| **Leads** | Row 18 | Pipeline / leftover template rows. Same older hours headers as Won (`HH053`). | 24 nonempty; KPI 3 / 0. |
| **Not Ready** | Row 1 | Older “not ready / hold / lost” list. Columns start at C. Mix of Not Ready Now, Hold, Lost, Follow Up. | 52 data rows. |
| **SETUP** | — | Template dropdown labels (client status, source, priority, task status). Includes statuses used on Client List (Won, Discovery Call, Interviewing, Contract Needed, …). | 19 nonempty. |
| **INSTRUCTIONS** | — | Purchased-template how-to. Not HH process. | 5 nonempty. |
| **Call Log** | Row 11 | Empty call CRM. Headers: Call Date, Time, Client, Phone (Auto-filled), Answered, Call Duration, Notes. | Structure only; no logged calls. |
| **Email Log** | Row 11 | Empty email CRM. Headers: Email Date, Time, Client, Email (Auto-filled), Replied, Email Title, Email Content. | Structure only. |
| **Project List** | Row 20 | Empty project tracker (template). | Placeholder rows / calendar flags; no real HH projects. |
| **Task List** | Row 20 | Empty task tracker (template). | Placeholder rows. |
| **Meeting List** | Row 11 | Empty meeting tracker (template). | Placeholder rows. |
| **Invoice Log** | Row 12 | Empty invoice tracker. **Not QBO.** Do not use this tab to create invoices. Unpaid/Partial/Paid all 0. | Template `$` placeholders only. |
| **Calendar View (Tasks & Meeting)** | — | Template calendar plus a client-name sidebar pulled from the roster. | Sidebar names + calendar grid. |

**Billing / hours source of truth = Client List**, not Invoice Log, not Won’s stale `HH053` column.

## Client List column map

Header is row 18. Column A is unused.

| Col | Header | Maps to | Notes |
|---|---|---|---|
| B | **Client Name** | `client_name` (DBA) | Franchise / location / DBA. Hubstaff **project names** usually match this, not legal. |
| C | **Legal Business Name** | `legal_business_name` | Legal entity. QBO customer candidate. |
| D | Contact Person | — | PII. Not in mapping CSVs. |
| E | Phone Number | — | PII. **Never in mapping CSVs.** |
| F | Email Address | — | PII. **Never in mapping CSVs.** |
| G | Last Correspondence | — | Ops notes. Not a billing key. |
| H | **VA Name** | `va_name` | Assigned VA. VA# is embedded in the string. |
| I | **Position** | `position` | Recruiter, Scheduler, Hybrid, Admin, etc. |
| J | **Expected Hours Worked** | `expected_hours` | Sparsely filled (10 / 181 rows on ingest). |
| K | **Actual Hours Worked** | `actual_hours` | **Currently holds contracted weekly hours** (20/40 typical). 131 / 181 rows filled. Not last-week Hubstaff actuals. |
| L | **HH061 (Aug 24-30)** | `weekly_hours_col` / `weekly_hours_value` | Rolling weekly hours for that billing week. **All empty on 2026-08-26 ingest.** This is the column to reconcile Hubstaff prior-week hours against once populated. |
| M | Start Date | — | Assignment start. |
| N | End Date | — | Filled when terminated / ended. |
| O | Priority | — | High / Medium / Low (rarely used on Client List). |
| P | Source | — | Dylan/52 Weeks, Referral, Strategy Lab Podcast/Miriam, etc. |
| Q | **Status** | `tracker_status` | Won, Discovery Call, Interviewing, Contract Needed, Follow Up, Sourcing Replacement, Lost, Not Ready Now, Scheduling Interviews, Job Description Needed, … |
| R | Onboarding Fee | tracker-only | **Never write to QBO.** Not in mapping CSVs. |
| S | VA Hourly Rate to Client | tracker-only | **Never write to QBO.** Not in mapping CSVs. |
| T | VA Hourly Rate to HH PH | tracker-only | **Never write to QBO.** Not in mapping CSVs. |
| U | VAs Hourly Net Pay | tracker-only | **Never write to QBO.** Not in mapping CSVs. |

### VA numbering

`va_number` is parsed from `VA Name` (`VA#2`, `VA #10`, `VA#1 - Replacement`). Replacement / terminated flags stay in `va_name`. One legal client can have many VA# rows; QBO line mapping is per VA, not per project.

### Weekly hour columns (`HH0xx`)

Client List currently uses **`HH061 (Aug 24-30)`**. Won / Leads still show **`HH053 (June 29- July 5)`** — stale, do not reconcile against that. The code rolls each week. Workflow step 5 must use the **current Client List weekly column**, not a hardcoded Excel filename.

Client List also has a **TOTAL ACTIVE CONTRACTED HOURS** footer (and a **TOTAL POTENTIAL HOURS** block under pipeline rows). Those are sums, not mapping rows.

## How this joins to Hubstaff

Hubstaff org **730247**. `mapping/BLANK.csv` already had **67 project IDs** (seeded 2026-08-26). This ingest joins tracker **Client Name / Legal Business Name** to those IDs **only when the names uniquely identify the same client**. No fuzzy-invented IDs.

| | Count |
|---|---|
| Tracker Client List data rows | 181 |
| Of those Status=Won | 135 |
| Tracker rows matched to a Hubstaff project ID | **106** (103 Won) |
| Tracker rows unmatched (kept with a note) | **75** |
| Unique Client Name + Legal pairs matched | 59 |
| Hubstaff projects (of 67) with a unique tracker match | **55** |
| Hubstaff projects left unmatched | **12** |

Project-level join: `mapping/BLANK.csv` (adds `client_name`, `legal_business_name`, `weekly_hours_col`, `tracker_status`).

VA-level join: `mapping/from-tracker.csv` (**106 matched** Client List assignments; QBO IDs blank, `status=draft`). Unmatched VA rows: `mapping/from-tracker-unmatched.csv` (**75** rows with `match_note`; no invented Hubstaff IDs).

### 12 Hubstaff projects not joined

Left unmatched on purpose:

- **Amada Senior Care** — appears on Not Ready tab only, not as a Client List row
- **Assisting Hands IL** — ambiguous among IL locations (Melrose Park, etc.); location-specific projects already mapped
- **BREAK** — internal Hubstaff project
- **Comprehensive Home Health Solutions - Jullian Speegle** — same tracker client as main CHHS (`4159457`); Hubstaff split by contact. Tracker rows joined to the main project only
- **Executive Home Care** — generic / ambiguous across many location DBAs
- **Executive Home Care - Tim** — possible Hayes Enterprise (contact first name Tim) but **names do not match**, so not joined
- **First Light Home Care CA** / **Charlotte** / **Ohio** — ambiguous vs several First Light tracker DBAs (Mission Viejo and Sylvania-Perrysburg have their own projects and are matched)
- **Helper Heroes' Project** — internal
- **Interim Healthcare La Jolla SD** — not found on Client List
- **Senior Helper CA** — ambiguous (Fresno CA vs other CA Senior Helpers). Coastal OC is already mapped to South Orange County

Won tracker clients without a Hubstaff project (examples, not a full dump): Tampa Bay EHC, Lake Washington EHC, several First Light DBAs, Gaddiel, Senior Helpers Glendale AZ, Sheraton Caregivers, Rose's Agency, Qualicare Az, Assisting Hands Cave Creek / Loudon County, Abernathy, in-house 52 Weeks marketing rows.

**Pilot candidate:** Gracious Living / Peter Sotos = tracker DBA **Assisting Hands North Chicago**, legal **Gracious Living Assistance Inc**, Hubstaff project **Assisting Hands Chicago North** `3889080`. A third VA row uses the legal name as Client Name; it joins to the same project.

## QBO-relevant fields (from this tracker)

Use these when Matt fills QBO IDs:

- Legal name → QBO customer
- DBA → display / Hubstaff project match
- VA# → QBO line
- Hours → expected / actual / current `HH0xx` weekly column

**Still unknown (do not invent):**

- Exact QBO hours field name (Qty vs custom vs line) — ask Matt
- Phantom QBO customer ID — Matt has not created it yet
- Hubstaff user IDs per VA (read-only lookup later; **do not log into Hubstaff to seed them** from this pass)
- Whether contracted hours live in Expected vs Actual long-term (today Actual holds the 20/40 contract)

## Rules

- Read-only on the Google Sheet
- Do not touch Hubstaff clients, projects, members, rates, or hours
- Do not create QBO invoices
- Do not write `pay_rate` or tracker rate columns to QBO
- Phantom QBO only until validated
- Mapping rows stay `status=draft` until Matt confirms
