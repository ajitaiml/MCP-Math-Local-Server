from __future__ import annotations
from fastmcp import FastMCP

mcp = FastMCP("arith")

def _as_number(x):
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(x.strip())
    raise TypeError("Expected a number (int/float or numeric string)")

@mcp.tool()
async def add(a: float, b: float) -> float:
    """Return a + b."""
    return _as_number(a) + _as_number(b)

@mcp.tool()
async def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return _as_number(a) - _as_number(b)

@mcp.tool()
async def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return _as_number(a) * _as_number(b)

@mcp.tool()
async def divide(a: float, b: float) -> float:
    """Return a / b."""
    num_b = _as_number(b)
    if num_b == 0: raise ValueError("Cannot divide by zero.")
    return _as_number(a) / num_b

@mcp.tool()
async def power(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    return _as_number(base) ** _as_number(exponent)

@mcp.tool()
async def modulus(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    num_b = _as_number(b)
    if num_b == 0: raise ValueError("Cannot modulo by zero.")
    return _as_number(a) % num_b

if __name__ == "__main__":
    mcp.run()