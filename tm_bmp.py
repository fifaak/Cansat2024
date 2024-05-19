# tm_bmp
from enable_bmp import enable_bmp280

bmp280 = enable_bmp280()

def getpress():
    pressure = bmp280.pressure
    return pressure
