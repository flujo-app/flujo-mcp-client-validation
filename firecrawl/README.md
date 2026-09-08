# Firecrawl MCP with FLUJO — partial validation

Validated 2026-09-08 UTC using FLUJO 3.45.2 and Node.js 22.22.0 on an isolated Debian cloud machine. A previously installed public npm runtime was reused with fresh HOME, FLUJO data, and browser profile.

## Tested setup and result

Connected Apps > Connect App > I have connection details > At a remote URL; enter https://mcp.firecrawl.dev/v2/mcp and Connect. The automatic MCP handshake passed and discovered three tools. Update server saved the connection.

The anonymous keyless free tier was used. No API key, OAuth login, model-provider credential or paid tool was used. Calling firecrawl_search with query "site:modelcontextprotocol.io MCP clients" and limit 1 returned success:true and one MCP documentation result. The response reported creditsUsed:2.

## Unresolved client form limitation

Selecting firecrawl_scrape briefly displayed its parameter form and then triggered FLUJO's application error boundary before any scrape call. This reproduced twice. Reloading the workspace recovered the UI; search then succeeded.

The browser reported React error #185 (maximum update depth). No runtime modification was made for this validation. Scrape and parse calls remain unverified, and documentation is proposed as a draft until the limitation is resolved.

Unedited screenshots: [connection](connection.png), [search result](search.png), [form error](form-error.png).
