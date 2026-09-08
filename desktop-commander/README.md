# Desktop Commander / FLUJO validation

Tested on 2026-09-08 UTC in a fresh Debian 12 cloud installation with FLUJO 3.45.2, Desktop Commander 0.2.48, Node.js 22.23.2, and a fresh FLUJO data directory and Chromium profile.

1. Opened Connected Apps → Connect App → I'm an expert → Configure & Test.
2. Used a directory containing the installed Desktop Commander package as the MCP server root.
3. Selected Standard IO, set Run command to `npx`, and entered `-y` and `@wonderwhy-er/desktop-commander@latest` as separate arguments.
4. FLUJO completed the MCP handshake and discovered 26 tools; the saved server showed Connected.
5. In FLUJO's Tool Tester, `list_directory` with path `/workspace/desktop-commander/fixture` and depth `1` returned `[FILE] hello.txt`, matching the disposable fixture. Result captured at 2026-09-08T03:24:18.630Z.

Screenshots: [connection test](connection-test.png), [tool result](tool-result.png).

A cold npx download exceeded the 90-second connection-test budget, so the instructions explicitly install the package first. The executable and arguments must be separate fields; a whole command in Run command produced spawn ENOENT.

Only the handshake and this read-only tool call were verified. Other tools, model chat, cross-platform behavior, and optional MCP Apps rendering were not tested. Any app-disabled notice in the screenshot is distinct from the successful core tool result. These are unedited browser captures.

