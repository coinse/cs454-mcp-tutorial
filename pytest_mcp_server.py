from mcp.server.fastmcp import FastMCP

mcp = FastMCP("pytest-automator")

import glob
import os

TARGET_DIR = os.path.join(os.path.dirname(__file__), "targets")

@mcp.tool()
def list_files() -> str:
    """
    List all Python files in the target directory to generate tests for.
    """
    file_list = []
    for file_path in glob.glob(os.path.join(TARGET_DIR, "*/*.py")):
        file_list.append(file_path.removeprefix(TARGET_DIR + os.sep))
    try:
        files = "\n".join(file_list)
        return f"All Python files in the target directory:\n{files}"
    except Exception as e:
        return f"Error listing files: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport='stdio')