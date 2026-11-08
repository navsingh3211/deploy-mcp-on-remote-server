from fastmcp import FastMCP
import random
import json

mcp = FastMCP("SimpleCalculatorServer")

# Add two number
@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: Fisrt number
        b: Second number
    Returns:
        The sum of a and b
    """
    return a + b

# Tool:Generate a random number
@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """
    Generate a random number within a range

    Args:
        min_val: Minimum value (default:1)
        max_val: Maximum value (default:100)
    Returns:
        A random integer between min_val and max_val
    """
    return random.randint(min_val, max_val)

# Resource : Server Information
@mcp.resource("info://server")
def server_info()->str:
    """Get information about this server."""

    info={
        "name": "Simple Calculator Server",
        "description": "A basic MCP server with math tools",
        "version": "1.0.0",
        "author": "Navneet Kumar Singh",
        "tools": ["add", "random_number"]
    }
    return json.dumps(info, indent=2)

#start server
if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)