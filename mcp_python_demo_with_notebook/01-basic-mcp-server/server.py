from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    mcp.run()
