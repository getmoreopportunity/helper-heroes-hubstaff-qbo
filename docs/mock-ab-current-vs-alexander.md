# Mock A/B — current QBO vs Alexander Services

Two **phantom** QBO setups. Same sample hours. No live clients. No Hubstaff writes. No ACH. No invoices. No customer merge.

QBO records are created in Matt’s Helper Heroes company (this bot has no QBO connector). Names are obviously fake so they never collide with live customers.

## Sample week (invented, not Hubstaff)

Week of **Mon Aug 17 – Sun Aug 23, 2026**. Example client bill rate **$1.00/hr** so the receipts are obviously mock.

| VA | Hours | Rate | Amount |
|---|---:|---:|---:|
| HH MOCK VA One | 40 | $1.00 | $40.00 |
| HH MOCK VA Two | 20 | $1.00 | $20.00 |
| **Total** | **60** | | **$60.00** |

Both setups must total **$60.00**. Rate is example only. Do not copy tracker HH PH / net pay.

## Mock A — current setup (VA as customer)

This is the pattern Alexander said to stop: individual customers used to track VA work.

Create in QBO:

1. Customer `HH MOCK Current VA One`
2. Customer `HH MOCK Current VA Two`
3. Recurring sales receipt on VA One — Qty **40**, rate **$1.00**, do not send, do not ACH
4. Recurring sales receipt on VA Two — Qty **20**, rate **$1.00**, do not send, do not ACH

VA identity lives on the **customer name**. Two customers, two receipts, same $60.

## Mock B — Alexander (VA as Service)

1. Chart of Accounts income account `HH MOCK VA Services` (revenue account for the Services)
2. Product/Service, type **Service**, name `HH MOCK VA One` — rate $1.00 — income account `HH MOCK VA Services`
3. Product/Service, type **Service**, name `HH MOCK VA Two` — rate $1.00 — same income account
4. Customer `HH MOCK Alexander Client` (the “real client”, not a VA)
5. Recurring sales receipt on that **one** customer, two lines:
   - `HH MOCK VA One` Qty 40
   - `HH MOCK VA Two` Qty 20
   - do not send, do not ACH

VA name appears on the receipt from the **Service**. Rate and hours on the line. One customer, $60.

## Pass / fail

- Totals match ($60 = $60)
- Mock B receipt shows both VA names as Service lines
- Mock A still has two customers (the merge problem, left unmerged)
- Nothing sent, no ACH, no live names, no Hubstaff writes

If Mock B is the one Matt would actually confirm on Monday, keep it and ignore Mock A. Customer merge of **live** records is still later, Matt/Alexander only.

Mapping: [`mapping/mock-ab.csv`](../mapping/mock-ab.csv). Dry-run payload: [`workflow/mock-ab-dry-run.json`](../workflow/mock-ab-dry-run.json).
