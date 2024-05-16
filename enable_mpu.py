# enable_mpu
import board
import busio
import adafruit_mpu6050

def enable_mpu():
  
  i2c = busio.I2C(board.SCL, board.SDA)

  mpu = adafruit_mpu6050(i2c)

  return mpu