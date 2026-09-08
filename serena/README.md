# Serena / FLUJO validation

Tested 2026-09-08 UTC with Serena 1.7.0, Python 3.13.15, FLUJO 3.45.2 and Node.js 22.23.2. Serena was installed using `uv tool install -p 3.13 serena-agent`. The installed public FLUJO runtime was reused with fresh isolated data and browser directories.

Started Serena with `serena start-mcp-server --transport streamable-http --port 9121 --project /workspace/serena/fixture --open-web-dashboard false`. Its documented default bind address is 127.0.0.1.

Configured the server through FLUJO's expert form, using Streamable HTTP and `http://127.0.0.1:9121/mcp`. The handshake discovered 30 tools and the saved card showed Connected. FLUJO's Tool Tester successfully called `initial_instructions`, then `get_symbols_overview` with `relative_path: "hello.py"`. The result was `{"Function":["greet"]}`, matching the disposable Python fixture.

[Connection](connection.png) · [Symbol result](symbols.png).

Stdio attempts failed in this environment; only the HTTP route is documented. Other languages, editing tools and model chat were not tested. These are unedited browser captures.

