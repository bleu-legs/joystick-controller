import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

joy1_x = AnalogIn(ads, ADS.P0)  # Joystick 1 X
joy1_y = AnalogIn(ads, ADS.P1)  # Joystick 1 Y
joy2_x = AnalogIn(ads, ADS.P2)  # Joystick 2 X
joy2_y = AnalogIn(ads, ADS.P3)  # Joystick 2 Y

while True:
    print(f"Joystick 1 - X: {joy1_x.value}, Y: {joy1_y.value}")
    print(f"Joystick 2 - X: {joy2_x.value}, Y: {joy2_y.value}")
    print("-" * 40)
    time.sleep(0.5)