# Playwright MCP with FLUJO — partial tool coverage

Validated 2026-09-08 UTC using FLUJO 3.45.2, @playwright/mcp 0.0.80, Node.js 22.23.2 and official Google Chrome for Testing 152.0.7977.82. Public binaries were reused on an isolated Debian cloud machine with fresh FLUJO data and browser profiles.

The existing-browser CDP route was tested. The server package was preinstalled in a local directory. In Connected Apps > Connect App > I'm an expert > Configure & Test, select Standard IO, Run command npx, and separate arguments -y, @playwright/mcp@latest and --cdp-endpoint=http://127.0.0.1:9227. The debugging port was dedicated to a disposable Chrome profile.

The FLUJO handshake passed with 24 tools. After saving, browser_navigate opened a local fixture and browser_snapshot returned its heading, paragraph and button. A repeat snapshot after recovery also passed.

Selecting browser_click later triggered FLUJO's React #185 workspace error boundary before arguments or a click request were submitted. Reload restored the UI. No click-tool success, automatic browser launch, model chat or all-tools compatibility is claimed. The navigation response also reported one browser console error whose cause was not investigated.

Unedited screenshots: [handshake](connection.png), [navigation](navigation.png), [snapshot](snapshot.png), [click-form failure](click-form-error.png). [Captured browser console](click-console.json).

A [14-line README draft](proposed-docs.patch) passed git diff --check. [Issue #1741](https://github.com/microsoft/playwright-mcp/issues/1741) requests approval under the contribution policy; no PR or Microsoft CLA signature is implied. The client form failure is tracked in [FLUJO #517](https://github.com/mario-andreschak/FLUJO/issues/517).
