# FLUJO with Stripe MCP: sandbox validation

Verified on 2026-09-08 UTC in a dedicated cloud computer using the unmodified public `flujo-ai@3.45.2` runtime, Node 22.22.0, and a fresh FLUJO data directory and Chromium profile. The previously installed public runtime was reused; no prior Neon connection data or browser authentication was copied.

## Results and limits

| Check | Result |
| --- | --- |
| Official anonymous sandbox provisioning | PASS: one Stripe CLI 1.50.10 attempt, no account/login fallback; temporary sandbox expires 2026-09-15. |
| Hosted MCP authentication | PASS: private sandbox bearer credential; Streamable HTTP at https://mcp.stripe.com/. |
| FLUJO connection test | PASS: MCP handshake and discovery of 9 tools; saved the connection. |
| One FLUJO tool call | PASS: `search_stripe_documentation` returned sandbox and testing documentation for the question below. |
| Client interface after result | LIMITATION: the selected tool disappeared during a periodic tool-list refresh; the result remained visible in the captured screenshot. The interface subsequently showed “The workspace hit a snag.” This is a client UI failure after the successful result, not a failed Stripe tool response. No second call was made. |
| OAuth / real account / financial operations | Not tested. No live data, payment, customer, balance, or other financial mutation was requested. |

The anonymous sandbox is a temporary test environment, not a registered Stripe account or an OAuth test. Its credential was kept only in a private cloud CLI profile and a FLUJO Secret header field. No credential, claim URL, session identifier, browser profile, or FLUJO data file is included in these artifacts.

## Actual UI walkthrough

1. Open Connected Apps, then Connect App. Choose “I have connection details”, “At a remote URL”, enter `https://mcp.stripe.com/`, and continue to setup.
2. The automatic test without credentials returned HTTP 401 as expected. In Configure & Test, add the custom HTTP header `Authorization`; select **Secret** before entering `Bearer <private sandbox credential>`.
3. Select **3) Test run**. The UI displayed a successful handshake, 9 discovered tools, and “Connection test passed. The server is reachable.”
4. Select **Update server**, open the saved server's Tools tab, and select `search_stripe_documentation`.
5. Enter: `How do Stripe sandboxes keep testing separate from live payments?` Leave the optional language and API-reference-only filter at their defaults, then select **Test tool** once.
6. The returned documentation included [Sandboxes](https://docs.stripe.com/sandboxes), [Testing Stripe Connect](https://docs.stripe.com/connect/testing), [Testing use cases](https://docs.stripe.com/testing-use-cases), [Test your integration](https://docs.stripe.com/testing/overview), and [Testing](https://docs.stripe.com/testing). The result screenshot captures the successful response alongside the subsequently cleared tool selection.

## Evidence

- [Connection pass screenshot](evidence/stripe-connection-passed.png)
- [Documentation result screenshot](evidence/stripe-documentation-result.png)
- [Subsequent client error screenshot](evidence/stripe-post-result-ui-error.png)
- [Connection receipt](evidence/connection-test.json)
- [Observed tool-result summary](evidence/documentation-tool-result.json)
- [Sanitized sandbox provisioning receipt](evidence/stripe-sandbox-attempt.json)
- [Sanitized protocol preflight](evidence/stripe-sandbox-preflight.json)
- [Official feedback tool schema](evidence/feedback-tool-schema.json)

The tool-result JSON is a concise transcription of the observed browser response, not a raw wire trace. Screenshots were visually reviewed and contain no credential values.

## Official sources and editorial route

Stripe documents [manual MCP setup](https://docs.stripe.com/mcp), [anonymous sandbox provisioning](https://docs.stripe.com/sandboxes?locale=en-US), and its [CLI implementation](https://github.com/stripe/stripe-cli/blob/master/pkg/cmd/sandbox.go). The official CLI npm package used was `@stripe/cli@1.50.10`.

The MCP documentation page offers an anonymous page-feedback form: **Was this page helpful? → No → Couldn't find what I was looking for**. Its optional text field accepts a precise request about the missing FLUJO guide. One submission attempt with this public evidence returned HTTP 429. The form collapsed without a confirmation, so delivery is unconfirmed; no immediate retry or workaround was attempted. The alternative editorial email published on the page is **mcp@stripe.com**.

The discovered `send_stripe_mcp_feedback` tool accepts feedback about MCP tools only. Its description excludes IDE/environment issues, so it was not used for this client-guide request or the FLUJO UI error.
