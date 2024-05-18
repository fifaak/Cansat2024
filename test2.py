import mpu6050

mpu = mpu6050.mpu6050(0x68)

# Read accelerometer data directly using the appropriate method
accel_data = mpu.get_accel_data()

# Extract accelerometer values from the data
accel_x = accel_data['x']
accel_y = accel_data['y']
accel_z = accel_data['z']

gyro_data = mpu.get_gyro_data()

# Extract accelerometer values from the data
gyro_x = gyro_data['x']
gyro_y = gyro_data['y']
gyro_z = gyro_data['z']

# Print the data
print("Accel_X: {:.2f} | Accel_Y: {:.2f} | Accel_Z: {:.2f}".format(accel_x, accel_y, accel_z))
