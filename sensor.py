
import board
import busio
import adafruit_bmp280
import time

i2c = busio.I2C(board.SCL, board.SDA)

# Cuando el SDO (SDA) esta Grounded, podemos seleccionar la dirección 0x76

sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)

while True:
	print("Temperatura: " + str(sensor.temperature) + " Cº")
	print("Presión: " + str(sensor.pressure))
	time.sleep(1)
