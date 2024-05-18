from enable_mpu import enable_mpu

mpu = enable_mpu()

accel_data = mpu.get_accel_data()
accel_x = accel_data['x']
accel_y = accel_data['y']
accel_z = accel_data['z']

gyro_data = mpu.get_gyro_data()
gyro_x = gyro_data['x']
gyro_y = gyro_data['y']
gyro_z = gyro_data['z']

print("Accel_X: {:.2f} | Accel_Y: {:.2f} | Accel_Z: {:.2f}".format(accel_x, accel_y, accel_z))
print("Gyro_X: {:.2f} | Gyro_Y: {:.2f} | Gyro_Z: {:.2f}".format(gyro_x, gyro_y, gyro_z))