# From Andrew Martin — 2026-08-25

Sources: "Hubstaff: Meeting Tech Follow Up" and "Hubstaff: 2nd Meeting Follow Up".

## Direction
Custom API/MCP, not native QBO. Goal is **updating hours** on existing QBO recurring billing/sales receipts, not creating invoices. Mapping is the foundation.

## Agreed next steps
1. Nom confirms Matt owner-level Hubstaff access.
2. Matt/Nom confirm Josh Hubstaff/developer access.
3. Josh creates OAuth app at developer.hubstaff.com/account/apps. Redirect: `http://localhost:44444/callback`. Share **application ID only** with Jean.
4. Jean configures MCP.
5. Josh builds this GitHub repo (JSON/workflow) for Jean to review endpoints.
6. Matt creates phantom QBO client.
7. Matt/Josh align mapping from recurring billing list + Excel + Hubstaff project/member structure.
8. Jean reviews endpoints (detailed activity vs daily totals).
9. Nom supports account structure, permissions, screenshots.

## MVP test
1. Phantom QBO client
2. One clean Hubstaff project/member set
3. Prior-week hours from Hubstaff
4. Push/update test QBO sales receipt hours
5. Compare to Matt's manual process
6. Document mismatches before a real client

Later live pilot candidate: **Gracious Living / Peter Sotos**.

Wise/VA payroll stays separate with Celdy.
