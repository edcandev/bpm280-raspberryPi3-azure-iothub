import board
import busio
import adafruit_bmp280

import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import Message
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)

idMensaje = 1
textoSinFormato = '{{"messageId": {messageId},"deviceId": "Raspi","temperature": {temperature},"humidity": {humidity}}}'


async def main():
    # Fetch the connection string from an environment variable
    conn_str = "HostName=RaspberryPiSensor.azure-devices.net;DeviceId=raspi-py;SharedAccessKey=muqAFLhtzA9A5GPzTpuRt65/dUtqPoyizEOKZz0eGSk="

    # Create instance of the device client using the authentication provider
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Enviando mensaje...")

    temperature = sensor.temperature
    pressure = sensor.pressure

    msg_txt_formatted = textoSinFormato.format(messageId = idMensaje, deviceId = "Raspi - Py", temperature = temperature, humidity = pressure)
    message = Message(msg_txt_formatted)


    await device_client.send_message(message)
        #"Temperatura: " + str(sensor.temperature) + " Cº Presión: " + str(sensor.pressure))

    print("El mensaje se ha enviado!")

    # finally, shut down the client
    await device_client.shutdown()

if __name__ == "__main__":

    while(True):
        asyncio.run(main())
        idMensaje += 1
        time.sleep(2)
