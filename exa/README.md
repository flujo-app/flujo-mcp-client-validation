# Exa / FLUJO validation

Tested 2026-09-08 UTC with FLUJO 3.45.2 and Node.js 22.22.0. A clean public npm-installed runtime was copied between isolated cloud machines with matching archive SHA256; the Exa data directory and browser profile were fresh. No application data, account keys or browser profiles were copied.

Using Connected Apps → Connect App → I have connection details → At a remote URL, entered `https://mcp.exa.ai/mcp`, selected Connect, Continue to setup, then Update server after the automatic test passed. Anonymous Streamable HTTP discovered two tools.

Actual FLUJO Tool Tester calls:
- `web_search_exa`: query about the official MCP client documentation, `numResults: 2`; returned two documentation results.
- `web_fetch_exa`: `urls: ["https://example.com"]`, `maxCharacters: 500`; returned Example Domain content.

[Connection](connection.png) · [Search result](search.png) · [Fetch result](fetch.png).

No API key, OAuth session, paid tool, or model provider was used. These screenshots are unedited browser captures; anonymous quotas can change.

