# Status — Helper Heroes Hubstaff / QBO

Updated 2026-08-27 12:45pm CT.

Goal: Matt’s ChatGPT Codex is the daily driver. Hubstaff (read-only), QBO, Excel, and this repo’s workflow all live there. Hours stay 1:1 across Hubstaff time, the tracker/Excel adjustments, and QBO sales-receipt lines. No live Hubstaff writes. No invoices. No ACH from us. Phantom QBO first.

## Now

- Repo: https://github.com/getmoreopportunity/helper-heroes-hubstaff-qbo (private). Workflow **v0.3.0**.
- Hubstaff org Helper Heroes **730247**. Josh and Matt are org owners. **67** active projects. **Do not touch live clients, projects, members, rates, or hours.**
- Celdy tracker ingested (read-only): 106 VA rows matched, 75 unmatched. Mapping QBO IDs still blank.
- Alexander (Intuit, 2026-08-27): each VA is a QBO **Service**; one customer per real client; hours/rate on the sales-receipt line. Merge live customers only later, and only if the model works. Doc: [`docs/from-alexander-qbo.md`](from-alexander-qbo.md).
- Phantom A/B spec ready: [`docs/mock-ab-current-vs-alexander.md`](mock-ab-current-vs-alexander.md). Same sample week, both totals **$60**. Not created in QBO yet.
- Jean’s MCP paste commands: [`docs/hubstaff-mcp-setup.md`](hubstaff-mcp-setup.md). Codex: leave **OIDC unchecked**.
- Matt’s Codex already has QBO and Excel (Josh to Jean, 2026-08-26). Hubstaff MCP is the missing connector on his side.

## Open

| Item | Owner | Notes |
|---|---|---|
| Accept GitHub invite | Matt | Invite went to mmiller.acc22@gmail.com. Only `getmoreopportunity` is on the repo today. Check spam. Then connect GitHub inside ChatGPT and open this repo. |
| Hubstaff MCP on Codex | Matt | `codex mcp add hubstaff --url https://mcp.hubstaff.com/` — OIDC off. Sign into Hubstaff web first. Read-only. |
| Hubstaff MCP on Grok Bot | Josh | Still needs the connect-card sign-in as josh@ on **desktop**, not phone. |
| Create Mock A + Mock B in QBO | Matt (+ Josh on Zoom) | Fake names only. Do not send. Do not ACH. |
| Live VA Services revenue account | Matt | After phantom works. Not the mock income account. |
| Excel view-only link into the repo | Matt | Celdy Google Sheet is ingested; Matt’s Excel is still the sheet he types from. Need both visible to Codex so they stay 1:1. |
| Jean GitHub invite | Jean | Still pending (`JeanFin`). |
| Live customer merge | nobody yet | Only if Mock B wins. Matt/Alexander. Not from this workflow. |

## Zoom — configure (Josh + Matt)

Do these in order. Nothing live. Nothing sent.

1. Matt accepts the GitHub invite and connects the repo in ChatGPT / Codex.
2. Matt runs the Hubstaff MCP command (OIDC off) and signs in. Confirm read-only (can list org 730247, cannot edit a client).
3. Josh finishes Grok Bot Hubstaff connect (desktop).
4. In QBO, create Mock A (current: two VA-named customers) and Mock B (Alexander: one customer + two Services + `HH MOCK VA Services` income account). Checklist in the mock doc.
5. Confirm Codex can see QBO, Hubstaff, Excel, and this repo in one chat.
6. Dry-run the sample week (Aug 17–23, 40h + 20h at $1.00). Both mocks total $60. VA names on Mock B are Service lines.
7. Stop. Do not merge live customers. Do not update a real sales receipt. Do not write Hubstaff.

## Hard rules

- Never create/update/delete Hubstaff clients, projects, members, rates, or hours.
- Never write HH PH / net pay / Hubstaff pay_rate into QBO.
- Recurring sales receipts only. No invoices. Matt confirms Monday, ACH Tuesday — we do not send.
- Phantom QBO until Matt says the hours match what he would type.

## 1:1 across surfaces

| Surface | What it is | Role |
|---|---|---|
| Hubstaff | Time by project / member | Input. Read-only. |
| Celdy tracker | Client List hours/billing adjustments | Source of truth for what should be billed. |
| Matt Excel | What he actually types today | Must reconcile to the tracker, not replace it. |
| QBO | Recurring sales receipts | Hours = Qty on the VA Service line (Alexander). |
| This repo | Mapping + workflow | The join table. Draft until QBO IDs are filled. |
| Matt Codex | Daily driver | Reads all of the above. Does not invent hours. |
