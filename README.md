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
