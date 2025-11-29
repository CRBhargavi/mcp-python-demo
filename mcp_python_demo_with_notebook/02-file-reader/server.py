from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def read_file(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

if __name__ == "__main__":
    mcp.run()
