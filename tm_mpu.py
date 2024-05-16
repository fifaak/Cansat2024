from enable_mpu import enable_mpu

mpu = enable_mpu()

accel_x, accel_y, accel_z = mpu.acceleration

gyro_x, gyro_y, gyro_z = mpu.gyro