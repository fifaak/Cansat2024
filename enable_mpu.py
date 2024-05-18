import board
import busio
import mpu6050

def enable_mpu():
    # Initialize I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize MPU6050 with the correct I2C address (0x68)
    mpu = mpu6050.mpu6050(0x68)

    return mpu
