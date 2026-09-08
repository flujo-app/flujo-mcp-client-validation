# FLUJO MCP client validation

Manual integration checks and screenshots used to support upstream client-documentation contributions. These are FLUJO project tests, not vendor certification.

## Context7 — 2026-09-07

A fresh FLUJO 3.45.2 installation was installed from the public npm package on an isolated Debian cloud machine with Node.js 22.22.0. It used a fresh data directory and browser profile. Tests ran in Chromium through FLUJO's UI.

- Connected Apps → Connect App → I have connection details → At a remote URL.
- URL: `https://mcp.context7.com/mcp`; Streamable HTTP; no API key or OAuth credentials used.
- FLUJO's backend connection test completed the MCP handshake and discovered 2 tools.
- Saved the connection and opened FLUJO's Tools tab.
- `resolve-library-id` with libraryName `React` and query `How to use useState to update a React component` returned library matches, including `/reactjs/react.dev`.
- `query-docs` with that libraryId and query returned React documentation and code examples.

The API-key header instructions follow Context7's documented endpoint convention; API-key and OAuth authentication were not tested. Anonymous quotas and returned results can change.

Screenshots: [connection test](context7/connection-test.png), [saved connection](context7/saved-connection.png), [library lookup](context7/library-lookup.png), [documentation result](context7/documentation-result.jpg).

No host browser, host files, or host credentials were used for installation or these tests.


## Desktop Commander — 2026-09-08 UTC

[Validation record and screenshots](desktop-commander/README.md): FLUJO 3.45.2 connected over stdio, discovered 26 tools, and list_directory returned the expected disposable fixture.

## Additional checks — 2026-09-08 UTC

- [Exa](exa/README.md): both hosted tools passed through FLUJO.
- [Serena](serena/README.md): local HTTP connection and Python symbol lookup passed.
- [Cloudflare Documentation MCP](cloudflare/README.md): hosted connection and documentation search passed.

- [FastMCP](fastmcp/README.md): local stdio handshake and integer addition returned 5.
- [Chrome DevTools](chrome-devtools/README.md): existing Chrome connection, page creation and accessibility snapshot passed.
- [Firecrawl](firecrawl/README.md): keyless connection and search passed; scrape form crashes before invocation, so validation remains partial.

- [Graphiti](graphiti/README.md): local HTTP handshake, FalkorDB status and seeded-episode retrieval passed with zero model API calls.

- [GitHub MCP](github-mcp/README.md): authenticated read-only handshake and exact public-file retrieval passed using a secret Bearer header; interactive OAuth and PAT-specific behavior were not tested.
- [Playwright MCP](playwright/README.md): navigation and snapshots passed; click parameter form crashes before invocation.

- [Tavily](tavily/README.md): public keyless header, saved connection and one bounded search passed; other tools and authentication modes were not tested.

- [Stripe](stripe/README.md): temporary sandbox authentication, nine-tool handshake and one documentation search passed; a subsequent FLUJO interface error is recorded separately.

## Prepared proposals

[Supabase](proposals/supabase/README.md): concrete client-selector draft with scoped URL and React/Markdown checks. Hosted authentication is untested.
