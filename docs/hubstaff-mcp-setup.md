# Hubstaff MCP paste commands

From Jean Fin, 2026-08-27. Sign in to the Hubstaff web app at least once before connecting. The account links on first login, and MCP sign-in relies on that step.

Read-only. Do not write Hubstaff clients, projects, members, rates, or hours.

## Grok (Josh)

```bash
grok mcp add --transport http hubstaff https://mcp.hubstaff.com/
```

## Codex / ChatGPT (Matt)

When adding the connector in ChatGPT, leave the OIDC checkbox **unchecked**. The server grants only `hubstaff:read`, so sign-in fails if OIDC is enabled.

```bash
codex mcp add hubstaff --url https://mcp.hubstaff.com/
```
