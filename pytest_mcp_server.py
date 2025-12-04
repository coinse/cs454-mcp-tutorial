from mcp.server.fastmcp import FastMCP

mcp = FastMCP("pytest-automator")


@mcp.tool()
def list_files() -> str:
    pass  # TODO
