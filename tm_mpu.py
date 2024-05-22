# # from enable_mpu import enable_mpu
# import lora
# import time

# mpu = enable_mpu()
# lora = MyLora(verbose=True)
# timestamp = time.time()

# def getAccGy():
#     accel_data = mpu.get_accel_data()
#     accel_x = accel_data['x']
#     accel_y = accel_data['y']
#     accel_z = accel_data['z']

#     gyro_data = mpu.get_gyro_data()
#     gyro_x = gyro_data['x']
#     gyro_y = gyro_data['y']
#     gyro_z = gyro_data['z']

#     return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z

# valueSyncSec = str(timestamp)
# valueAccX = str(getAccGy()[0])
# valueAccY = str(getAccGy()[1])
# valueAccZ = str(getAccGy()[2])
# valueGyX = str(getAccGy()[3])
# valueGyY = str(getAccGy()[4])
# valueGyZ = str(getAccGy()[5])


# String = "{\"Module\":\"" + "GY521" + "\","
# String += "\"valueSyncSec\":\"" + valueSyncSec + "\","
# String += "\"valueAccX\":\"" + valueAccX + "\","
# String += "\"valueAccY\":\"" + valueAccY + "\","
# String += "\"valueAccZ\":\"" + valueAccZ + "\","
# String += "\"valueGyX\":\"" + valueGyX + "\","
# String += "\"valueGyY\":\"" + valueGyY + "\","
# String += "\"valueGyZ\":\"" + valueGyZ + "\"}"

# f = open("log.txt", "w")
# f.write(String)
# f.write("\n")
# f.close

# lora.setup()
# lora.send_data(String)

# # print(getAccGy())

print("mpu")