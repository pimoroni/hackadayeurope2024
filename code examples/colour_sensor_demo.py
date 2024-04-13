from time import sleep
from machine import I2C
from breakout_bh1745 import BreakoutBH1745

# Constants
SDA_PIN = 16
SCL_PIN = 17
SLEEP = 2

# Create the I2C and BH1745 for the colour sensor
i2c = I2C(0, sda=SDA_PIN, scl=SCL_PIN, freq=400000)
bh1745 = BreakoutBH1745(i2c)

# Turn on the sensor's LEDs
bh1745.leds(True)

# Loop forever
while True:
    # Read the sensor's values
    rgbc_raw = bh1745.rgbc_raw()
    rgb_clamped = bh1745.rgbc_clamped()
    rgb_scaled = bh1745.rgbc_scaled()
    
    # Print out the sensor's values in a formatted way
    print("Raw: {}, {}, {}, {}".format(*rgbc_raw))
    print("Clamped: {}, {}, {}, {}".format(*rgb_clamped))
    print("Scaled: #{:02x}{:02x}{:02x}".format(*rgb_scaled))

    sleep(SLEEP)
