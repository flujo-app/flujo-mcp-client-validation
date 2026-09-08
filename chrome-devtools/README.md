# Chrome DevTools MCP with FLUJO

Validated 2026-09-08 UTC on an isolated Debian cloud machine, using FLUJO 3.45.2, Node.js 22.23.2, chrome-devtools-mcp 1.8.0, and Google Chrome for Testing 152.0.7977.82. The existing public FLUJO runtime was reused with a fresh data directory and browser profile.

## Verified workflow

1. Install chrome-devtools-mcp in a local directory. Start a separate Chrome instance with remote debugging enabled and a fresh profile.
2. In FLUJO, open Connected Apps > Connect App > I'm an expert > Configure & Test.
3. Set MCP server root path to the package directory. Select Standard IO and Run command npx.
4. Add three separate arguments: -y, chrome-devtools-mcp@latest, and --browser-url=http://127.0.0.1:9225. This test used port 9225; use the port configured for your own Chrome instance.
5. Click 3) Test run, then Add server after the handshake passes.
6. Open Tools and call new_page with the synthetic local fixture URL. Call take_snapshot with the returned page ID.

## Actual result

The handshake discovered 29 tools. The saved connection showed Connected. new_page returned page 2, titled "FLUJO Chrome DevTools Fixture". take_snapshot returned that title, the heading "FLUJO browser connection verified", explanatory text and "Fixture button".

Chrome was downloaded from official Chrome for Testing release metadata. Its profile was separate from the browser controlling FLUJO. The fixture was local and disposable. No credentials or real browsing history were used.

Unedited screenshots: [connection test](connection.png), [page snapshot](snapshot.png).

## Limits

This validates the existing-browser stdio route and two browser tool calls. Automatic browser launch, performance tracing, other operating systems and the full tool suite were not tested. The root-run cloud test browser used --no-sandbox; that environment-specific flag is not included in the proposed client guide.

For the 16-line docs-only patch, repository-scoped Prettier and git diff --check passed. Full-repository formatting exceeded the 2GB VM's memory and is recorded as incomplete, not a passing check. The Google CLA has not been signed.
