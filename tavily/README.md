# Tavily: FLUJO keyless client guide

Verified 2026-09-08 UTC. Actual UI test passed using FLUJO 3.45.2, Node.js 22.22.0 and Chromium 152.0.7977.82 on an isolated Debian cloud machine with fresh application data and browser profile.

## Verified behavior

The original prebuilt FLUJO 3.45.2 connected to `https://mcp.tavily.com/mcp/` over Streamable HTTP with the public `X-Tavily-Access-Mode: keyless` header entered through the visible UI.

The exact path was **Connected Apps → Connect App → I'm an expert → Configure & Test**. After setting a server name, the Streamable HTTP URL and custom header, **3) Test run** reported one custom header sent, successful MCP handshake, and five discovered tools. **Add server** saved the connection. Reopening the server showed the persisted header, and a second connection test passed.

Exactly one `tavily_search` call was made through the Tool Tester, with query `site:modelcontextprotocol.io MCP clients` and `max_results: 1`. It returned one official MCP documentation result: [Understanding MCP clients](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts). The response explicitly reports `auth_mode: "keyless"`. Tavily normalized the response query to `MCP clients`. No API key, OAuth, account, or paid model service was used.

[Header screenshot](header.png), [connection screenshot](connection.png), and [search screenshot](search.png) are real, unedited cloud-browser captures and were visually reviewed. The connection screenshot retains FLUJO's red first-section indicator with the remote server's local root path left blank; saving, the handshake and search all succeeded. The [test summary](test-summary.json) records the submitted inputs, result URL and authentication mode.

## Limits and sources

[Tavily's keyless documentation](https://docs.tavily.com/documentation/keyless) explicitly permits free, rate-limited Search and Extract with this header. Crawl, Map and Research require a key. Actual discovery still advertised all five tools; their presence was not treated as free access. Only Search was called. Extraction, keyed access, OAuth and the other tools remain untested.

Primary setup reference: [official remote MCP documentation](https://docs.tavily.com/documentation/mcp). Documentation target: [README at the tested commit](https://github.com/tavily-ai/tavily-mcp/blob/248dc9e3e385305ad3281120284ff662af4b5940/README.md).

## Documentation contribution

A 13-line README guide uses these tested UI steps and states the keyless limits. The README-only diff passes git diff --check; no runtime source or dependencies changed.
