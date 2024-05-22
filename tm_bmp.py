# # tm_bmp
# from enable_bmp import enable_bmp280
# import lora
# import time

# bmp280 = enable_bmp280()
# timestamp = time.time()
# lora = MyLora(verbose=True)

# def getpress():
#     pressure = bmp280.pressure
#     return pressure

# valueSyncSec = str(timestamp)
# valuePress = str(getpress())

# String = "{\"Module\":\"" + "BMP280" + "\","
# String += "\"valueSyncSec\":\"" + valueSyncSec + "\","
# String += "\"valuePress\":\"" + valuePress + "\"}"

# f = open("log.txt", "w")
# f.write(String)
# f.write("\n")
# f.close

# lora.setup()
# lora.send_data(String)


print("bmp")