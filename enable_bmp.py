# bmp280_enable.py
import board
import busio
import adafruit_bmp280

def enable_bmp280():

    i2c = busio.I2C(board.SCL, board.SDA)
    
    bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
        
    return bmp280
