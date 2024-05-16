import board
import busio
import adafruit_mcp9808

def enable_mcp():

    i2c = busio.I2C(board.SCL, board.SDA)

    mcp = adafruit_mcp9808.MCP9808(i2c)

    return mcp

