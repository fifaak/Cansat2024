# # tm_mcp
from enable_mcp import enable_mcp
import lora
import time

mcp = enable_mcp
lora = MyLora(verbose=True)
timestamp = time.time()

def gettemp():
    temperature = mcp.temperature
    return temperature

valueSyncSec = str(timestamp)
valueMCPTemp = str(gettemp())

String = "{\"valueSyncSec\":\"" + valueSyncSec + "\","
String += "\"valueMCPTemp\":\"" + valueMCPTemp + "\"}"

lora.setup()
lora.send_data(String)

# print("mcp")