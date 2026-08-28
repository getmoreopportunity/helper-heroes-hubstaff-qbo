# Status — Helper Heroes Hubstaff / QBO

Updated 2026-08-27 9:30pm CT.

Goal: Matt’s ChatGPT Codex is the daily driver. Hubstaff (read-only), QBO, Excel, and this repo’s workflow all live there. Hours stay 1:1 across Hubstaff time, the tracker/Excel adjustments, and QBO sales-receipt lines. No live Hubstaff writes. No invoices. No ACH from us. Phantom QBO first.

Deterministic join (grain, keys, naming, fail-closed routing): [`docs/data-model.md`](data-model.md).

## Now

- Repo: https://github.com/getmoreopportunity/helper-heroes-hubstaff-qbo (private). Workflow **v0.3.0**.
- Hubstaff org Helper Heroes **730247**. Josh and Matt are org owners. **67** active projects. **Do not touch live clients, projects, members, rates, or hours.**
- Hubstaff MCP on this Grok Bot: **connected** read-only (josh@, 2026-08-27).
- Celdy tracker ingested (read-only): 106 VA rows matched, 75 unmatched. Mapping QBO IDs and `hubstaff_user_id` still blank (`draft`).
- Alexander (Intuit, 2026-08-27): each VA is a QBO **Service**; one customer per real client; hours/rate on the sales-receipt line. Merge live customers only later, and only if the model works. Doc: [`docs/from-alexander-qbo.md`](from-alexander-qbo.md).
- Phantom A/B spec ready: [`docs/mock-ab-current-vs-alexander.md`](mock-ab-current-vs-alexander.md). Same sample week, both totals **$60**. Not created in QBO yet.
- Jean’s MCP paste commands: [`docs/hubstaff-mcp-setup.md`](hubstaff-mcp-setup.md). Codex: leave **OIDC unchecked**. Matt’s Codex Hubstaff connect still blocked (Windows / invalid_scope). Emailed Jean 2026-08-27 evening.
- Matt’s Codex already has QBO and Excel. Hubstaff MCP is the missing connector on his side.

## Open

| Item | Owner | Notes |
|---|---|---|
| Accept GitHub invite | Matt | Invite went to mmiller.acc22@gmail.com. Only `getmoreopportunity` is on the repo today. |
| Hubstaff MCP on Codex | Matt / Jean | Windows config + `invalid_scope` (write/OIDC). Jean has the snag list. |
| Create Mock A + Mock B in QBO | Matt (+ Josh) | Fake names only. Do not send. Do not ACH. |
| Live VA Services revenue account | Matt | After phantom works. Not the mock income account. |
| Excel view-only link + column map | Matt | Required for 1:1 vs Client List. Same grain: client + VA + week. |
| `hubstaff_user_id` per VA | Grok/Codex read-only | Required before a row can leave `draft`. Do not invent. |
| Jean GitHub invite | Jean | Still pending (`JeanFin`). |
| Live customer merge | nobody yet | Only if Mock B wins. Matt/Alexander. Not from this workflow. |

## Hard rules

- Never create/update/delete Hubstaff clients, projects, members, rates, or hours.
- Never write HH PH / net pay / Hubstaff pay_rate into QBO.
- Recurring sales receipts only. No invoices. Matt confirms Monday, ACH Tuesday — we do not send.
- Phantom QBO until Matt says the hours match what he would type.
- Names never route. Unmatched stays unmatched.
