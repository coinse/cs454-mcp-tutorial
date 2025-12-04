from mcp.server.fastmcp import FastMCP

mcp = FastMCP("pytest-automator")

@mcp.tool()
def say_hello() -> str:
    return "Hello, students! I just wanted to say hi from the MCP server."

if __name__ == "__main__":
    mcp.run()
