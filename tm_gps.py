# from enable_gps import gpsdata
# import lora
# import time

# lora = MyLora(verbose=True)
# timestamp = time.time()

# if gpsdata == "$GPGGA":
#     newmsg=pynmea2.parse(newdata)
#     lat = newmsg.latitude
#     lng = newmsg.longitude
#     altitude = newmsg.altitude

# valueSyncSec = str(timestamp)
# valueLat = str(lat)
# valueLng = str(lng)
# valueGPSAltitude = str(altitude)

# String = "{\"Module\":\"" + "GPS" + "\","
# String += "\"valueSyncSec\":\"" + valueSyncSec + "\","
# String += "\"valueLat\":\"" + valueLat + "\","
# String += "\"valueLng\":\"" + valueLng + "\","
# String += "\"valueGPSAltitude\":\"" + valueGPSAltitude + "\"}"

# f = open("log.txt", "w")
# f.write(String)
# f.write("\n")
# f.close

# lora.setup()
# lora.send_data(String)

print("gps")