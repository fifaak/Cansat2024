# tm_mcp
from enable_mcp import enable_mcp

mcp = enable_mcp

def gettemp():
    temperature = mcp.temperature
    return temperature