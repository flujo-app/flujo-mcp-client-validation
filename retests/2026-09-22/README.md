# FLUJO integration retests — 2026-09-22

These are project validation results, not vendor certification. Tests ran in an isolated Debian 12 Fly VM through the llm-pc MCP endpoint. The published `flujo-ai@3.46.0` package used a fresh data directory and Chromium profile, with Node.js 22.23.2. No local desktop or host browser was used to run FLUJO or the integration tests.

| Integration | Published-release result | Scope |
| --- | --- | --- |
| Playwright MCP 0.0.82 | PASS for tested operations | 25-tool stdio handshake; browser_navigate, browser_snapshot, browser_click |
| Stripe hosted MCP | PASS for tested operations | Secret Bearer header, nine-tool handshake, documentation search with a fresh free sandbox key |
| Firecrawl hosted MCP | PARTIAL; provider access blocked | Three-tool handshake and stable scrape form; actual scrape rejected because anonymous access was unavailable |

## Playwright

Configured Standard IO with command `node` and arguments `/workspace/retests/tools/node_modules/@playwright/mcp/cli.js` and `--cdp-endpoint=http://127.0.0.1:9227`. The CDP endpoint belonged to a disposable Chromium instance in the VM.

A fixture on loopback port 8081 contained a Confirm test click button and a paragraph initially reading No clicks yet. Navigation and snapshot tools succeeded; the snapshot returned button target `e4`. The click form retained `element=Confirm test click button` and `target=e4` for **229.311 seconds**, with no automatic click. After pressing Test tool, the response showed the click operation; an independent read of the disposable page confirmed **Click confirmed**. The result remained visible during a later check. The single browser console error was the missing favicon (404), verified in the fixture HTTP log.

The earlier 3.45.2 click-form crash was not reproduced in this 3.46.0 run. This does not prove every tool/schema works or establish which change fixed the earlier behavior.

## Stripe

Connected to `https://mcp.stripe.com` over Streamable HTTP using an Authorization Bearer header marked Secret. A fresh free sandbox was provisioned with official Stripe CLI 1.51.1; its advertised expiry was 2026-09-29. Credentials and claim links are excluded from this repository.

The handshake exposed **nine tools**. `search_stripe_documentation` with question “How do I verify Stripe webhook signatures in Node.js?” returned documentation results, including the webhook guide. The same read-only search also succeeded after a VM restart. No payment, customer, or account mutation tool was called. Interactive OAuth and production credentials were not tested.

## Firecrawl

Connected to `https://mcp.firecrawl.dev/v2/mcp` over Streamable HTTP without credentials; handshake exposed **three tools**. The `firecrawl_scrape` form retained `url=https://example.com/` for **109.485 seconds**, without the earlier workspace/React crash. A single invocation then returned **“Anonymous keyless access is unavailable for this request.”** This is not a successful scrape.

Official free-account signup rejected the cloud request with a VPN/proxy restriction. A support request asking for a legitimate free test-key provisioning route was sent to `help@firecrawl.com` from the project mailbox. No network restriction was bypassed. The upstream documentation PR remains draft until a real scrape succeeds.

## Separate issue #517 patch check

The existing four-file uncommitted fix was applied to a separate cloud checkout of commit `15d019f7b952b2f2d3aea1197722ac8d9f520d7c`. Patch SHA-256: `3a1bfa587f43f35e744688d567fea46d5f0e081942e36fbbc842456291e73dc1`. Dependency installation and bundled MCP TypeScript builds completed. The development server started, but route compilation took minutes and the workspace did not become usable before the VM stopped responding to its exec API. The VM required a control-plane restart; saved evidence survived.

**The patch browser validation is incomplete.** No claim is made that this patch is part of 3.46.0 or that published-release results validate its manual-refresh behavior. The VM had one performance CPU and 8 GiB RAM; the precise cause of its unresponsiveness was not established.

## Evidence

- [Playwright click form](playwright-release-click-result.png), [returned click result](playwright-release-click-visible-result.png), [target page after click](playwright-target-after-click.png), [stability measurements](playwright-release-click-stability.json), [navigation](playwright-release-navigation.png), [snapshot](playwright-release-snapshot.png).
- [Stripe connection test](stripe-release-handshake.png), [search form](stripe-release-search-result.png), [returned result](stripe-release-search-visible-result.png).
- [Firecrawl provider rejection](firecrawl-release-key-required.png), [stable form](firecrawl-release-stability.png), [stability measurements](firecrawl-release-stability.json).

Screenshots are unedited browser captures. Some show the form above the result; outcomes were also verified from rendered UI text and, for Playwright, the target page DOM.
