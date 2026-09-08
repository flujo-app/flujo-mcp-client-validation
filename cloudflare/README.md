# Cloudflare Documentation MCP / FLUJO validation

Tested 2026-09-08 UTC with a fresh npm installation of FLUJO 3.45.2, Node.js 24.20.0 and Chromium 152.0.7977.82 in an isolated cloud environment.

Configured `https://docs.mcp.cloudflare.com/mcp` using Connected Apps → Connect App → I have connection details → At a remote URL. The anonymous Streamable HTTP handshake passed and discovered two tools. Saved with Update server.

In FLUJO's Tool Tester, `search_cloudflare_documentation` with query `How do I create a Cloudflare Worker with Wrangler?` returned multiple Cloudflare documentation results, including First Worker and the Workers CLI guide.

[Connection](connection.png) · [Search result](search.png).

No custom authorization headers, OAuth session, model provider, deployment or paid API call was used. No compatibility with other authenticated Cloudflare servers is inferred. These are unedited browser captures.

