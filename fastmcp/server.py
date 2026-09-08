from fastmcp import FastMCP
mcp = FastMCP("FLUJO validation")
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two integers for a disposable client integration test."""
    return a + b
if __name__ == "__main__":
    mcp.run()
