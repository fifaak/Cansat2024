# tm_bmp
from enable_bmp import enable_bmp280

bmp280 = enable_bmp280()

pressure = bmp280.pressure
