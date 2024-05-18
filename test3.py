import mpu6050
import time
import board
import busio
import adafruit_bmp280
import adafruit_mcp9808

# Initialize MPU6050
mpu6050 = mpu6050.mpu6050(0x68)

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize BMP280
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Initialize MCP9808
mcp9808 = adafruit_mcp9808.MCP9808(i2c)

def read_sensor_data():
    # Read data from MPU6050
    accelerometer_data = mpu6050.get_accel_data()
    gyroscope_data = mpu6050.get_gyro_data()
    mpu_temperature = mpu6050.get_temp()

    # Read data from BMP280
    bmp280_pressure = bmp280.pressure
    bmp280_altitude = bmp280.altitude
    bmp280_temperature = bmp280.temperature

    # Read data from MCP9808
    mcp9808_temperature = mcp9808.temperature

    return (accelerometer_data, gyroscope_data, mpu_temperature, 
            bmp280_pressure, bmp280_altitude, bmp280_temperature, 
            mcp9808_temperature)

while True:
    (accelerometer_data, gyroscope_data, mpu_temperature, 
     bmp280_pressure, bmp280_altitude, bmp280_temperature, 
     mcp9808_temperature) = read_sensor_data()

    print("Accelerometer data:", accelerometer_data)
    print("Gyroscope data:", gyroscope_data)
    print("MPU6050 Temp:", mpu_temperature)
    print("BMP280 Pressure:", bmp280_pressure)
    print("BMP280 Altitude:", bmp280_altitude)
    print("BMP280 Temp:", bmp280_temperature)
    print("MCP9808 Temp:", mcp9808_temperature)

    time.sleep(1)
