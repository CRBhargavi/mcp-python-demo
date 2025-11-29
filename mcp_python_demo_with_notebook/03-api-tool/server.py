import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def crypto_price(symbol: str = "BTC") -> str:
    url = f"https://api.coindesk.com/v1/bpi/currentprice/{symbol}.json"
    res = requests.get(url)
    return res.text

if __name__ == "__main__":
    mcp.run()
