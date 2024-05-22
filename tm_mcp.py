# # # tm_mcp
# from enable_mcp import enable_mcp
# import lora
# import time

# mcp = enable_mcp
# lora = MyLora(verbose=True)
# timestamp = time.time()

# def gettemp():
#     temperature = mcp.temperature
#     return temperature

# valueSyncSec = str(timestamp)
# valueMCPTemp = str(gettemp())

# String = "{\"Module\":\"" + "MCP9808" + "\","
# String += "\"valueSyncSec\":\"" + valueSyncSec + "\","
# String += "\"valueMCPTemp\":\"" + valueMCPTemp + "\"}"

# f = open("log.txt", "w")
# f.write(String)
# f.write("\n")
# f.close

# lora.setup()
# lora.send_data(String)

print("mcp")