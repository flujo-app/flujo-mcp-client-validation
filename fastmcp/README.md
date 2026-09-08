# FastMCP with FLUJO

Validated 2026-09-08 UTC using FLUJO 3.45.2, FastMCP 4.0.3, Python 3.11.2 and Node.js 22.22.0 on an isolated Debian cloud machine. The public npm FLUJO runtime from the earlier installation was reused, with a fresh FLUJO data directory and browser profile. No account or model-provider credentials were configured.

A new Python virtual environment installed FastMCP. The disposable [server.py](server.py) defines one integer addition tool and starts FastMCP's standard stdio transport.

## Reproduce

1. Create a Python virtual environment and install FastMCP. Save the fixture as server.py.
2. In FLUJO, open Connected Apps > Connect App > I'm an expert > Configure & Test.
3. Enter a server name and the directory containing server.py as MCP server root path. Select Standard IO.
4. Set Run command to the virtual environment's Python executable. Add the full path to server.py as one separate argument.
5. Click 3) Test run. The MCP handshake should pass and discover one tool. Click Add server.
6. Open the saved server's Tools tab, select add, enter a=2 and b=3, then click Test tool.

## Actual result

The MCP handshake passed, one tool was discovered, and the saved server showed Connected. Calling add with integer inputs 2 and 3 returned 5 in FLUJO's Tool Tester. The screenshots show the actual UI and are unedited.

- [Connection test](connection.jpg)
- [Tool result](add-result.jpg)

This tests one local stdio server and a tool call. It does not establish HTTP/OAuth support or a FastMCP installer adapter.

Documentation proposal: https://github.com/PrefectHQ/fastmcp/issues/5035
