# Alexander Escobedo (Intuit) — QBO model for Hubstaff hours

Source: email to info@ / josh@ 2026-08-27 12:19pm CT, thread “A Escobedo Email”. He cannot send the call recording (Intuit policy). This is his written recommendation.

## Recommendation (verbatim sense)

1. **Each VA is a QBO Product/Service, type Service.** Not a separate customer used to track that VA’s work.
2. **If they have a standard rate, apply it on that Service.** This is the client bill rate on the item, not Hubstaff pay / HH PH / net pay. Those tracker pay columns still never go to QBO.
3. **Each Service needs a revenue account from the Chart of Accounts.**
4. **Created VA Service records populate sales receipts** — one line at a time, or a single large list per customer. The **VA name** appears on the sales receipt. **Rate and hours** are populated on that line.
5. **If this works, merge customer records.** Individual customers will not be used to track VA work. Merging **preserves previous sales receipts** on the merged customer.

## What this changes for us

- Mapping key for a VA is `qbo_item_id` / Service name, not a QBO customer-per-VA.
- QBO **customer** = the real client (legal / DBA as before). One customer, many VA Service lines.
- Recurring sales receipt lines are those Services. Hours field = Qty/hours on the VA Service line; rate lives on the Service (or override on the line).
- **Do not merge live customers from this workflow.** Matt/Alexander only, and only after phantom proves the model. Phantom client first. No new invoices. No ACH from us. No Hubstaff writes.

## Open with Matt

- Which Chart of Accounts revenue account for VA Services.
- Phantom customer + a couple of phantom VA Services to dry-run.
- Whether existing recurring sales receipts already use items, or still need to be rebuilt onto Services before any merge.
