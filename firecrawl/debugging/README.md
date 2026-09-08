# FLUJO 3.45.2: opening Firecrawl scrape parameters can crash the workspace

Status: reproduced; no source fix proposed. Investigation stopped after one instrumented full-app pass because the isolated editor/form tests do not reproduce the failure and the cause of repeated mounting is unresolved.

## Original release reproduction

Environment: Debian cloud VM with 1 performance CPU and 2 GB RAM, Node 22.22.0, Chromium, published flujo-ai 3.45.2. Public source inspected at mario-andreschak/FLUJO commit 1eb55adad24a9c692054b0889473870ca3ed132e (package version 3.45.2). All browser and filesystem work occurred on the cloud computer. No credentials or paid integration were used.

1. In FLUJO, open Connected Apps > Connect App > I have connection details > At a remote URL.
2. Connect to https://mcp.firecrawl.dev/v2/mcp with no credentials; wait for a successful connection test and save with Update server.
3. Open the saved server's Tools tab.
4. Choose firecrawl_scrape in Tool Tester and leave its parameter form open.

Observed twice in the unmodified release: the form appears, may be replaced by loading tools, and the workspace error boundary displays "The workspace hit a snag". Reload workspace recovers. Neither scrape nor parse was invoked. The same saved connection successfully discovered three tools and executed firecrawl_search once, so this is a client form failure after a working MCP connection. This does not establish support for the failed tool.

Original browser console: React error #185, maximum update depth exceeded. First application frame:
`/_next/static/chunks/2496-e24197f8d2d02168.js:1:7809`

The [original console/stack](original-ui-limitation.json) and [release screenshot](../form-error.png) are retained with this report. [React's error reference](https://react.dev/errors/185) explains the update-depth error.

## Source investigation and tests

The compiled frame maps to the async-suggestion effect in `src/frontend/components/shared/GlobalReferenceEditor.tsx` around line 564. Its inactive branch calls `setAsyncSuggestions([])`. An empty-array state setter alone is not enough evidence that this effect is the cause: its dependencies are stable for a mounted scrape URL editor, and the source creates the editor with useMemo(..., []).

Tests ran against unchanged source using the repository Jest configuration:
- GlobalReferenceEditor.test.tsx and GlobalReferenceEditorFocus.test.tsx: 2 suites, 8 tests passed (21.066 s; existing act warnings in log).
- A temporary diagnostic test mounted SchemaParamsForm with the actual captured Firecrawl scrape inputSchema, confirmed the URL field, edited formats JSON, and checked the controlled value: 1 test passed (10.182 s). This is a passing diagnostic, not a regression test demonstrating a fix.

The tool schema was obtained with public MCP initialize/tools-list only; no additional tool invocation. Test dependencies were isolated outside the preserved runtime.

## One instrumented full-app pass

An independent copy of the FLUJO package was explicitly labeled DIAGNOSTIC-RUNTIME. Only the implicated compiled effect was instrumented; no behavior fix was applied. It records editor/configuredRoots/workspaceRoots identities, enhanced-hitlist state, and timestamps before running the original effect. Public dependencies were reused read-only. Original data and browser profiles were not reused.

The diagnostic app ran on port 4300 with its sandbox on 4301, fresh home/data/browser directories, and an explicit public, credential-free Firecrawl server fixture placed in the isolated configuration while the app was stopped. This fixture insertion was diagnostic setup, not another UI connection validation.

Selecting firecrawl_scrape initially showed its complete form. About 24.46 seconds later, repeated editor recreation began. The retained probe contains 27 distinct editor identities and 27 distinct configuredRoots identities over roughly 38.93 seconds from the first mount; every record has enhancedHitlist=false and workspaceRoots=null. The form disappeared and the workspace error boundary appeared before a scrape invocation. No successful URL edit occurred.

This is evidence of repeated editor mounting/recreation, rather than a single stable editor rerunning this effect. ToolManager has a 30-second refresh and useServerTools clears tools before reloading, but the exact trigger of the rapid subsequent mounts is not established. Neither that refresh nor the empty-array setter should be changed speculatively based on this evidence alone.

## Integrity and limit

The preserved original application chunk still has SHA256:
`3a2de283bd61d54ee8b31374a3a01b1b4e045838b91e94ea68123663b6c416a3`

No tracked upstream source files were changed. No source patch, full rebuild, release, merge, or authentication claim is included. Next focused investigation would capture parent component identity and tool-refresh/render events in a development build and reproduce the whole ToolManager lifecycle before choosing a fix.

Published evidence: compact probe JSON, original UI limitation/stack and unchanged-source test logs. Further diagnostic captures and temporary test source remain preserved on the test machine.
