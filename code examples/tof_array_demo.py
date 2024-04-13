from machine import I2C
from time import ticks_ms, ticks_diff
from breakout_vl53l5cx import VL53L5CX, RESOLUTION_8X8

# The VL53L5CX requires a firmware blob to start up.
# Make sure you upload "vl53l5cx_firmware.bin" via Thonny to the root of your filesystem
# You can find it here: https://github.com/ST-mirror/VL53L5CX_ULD_driver/blob/no-fw/lite/en/vl53l5cx_firmware.bin

# Constants
SDA_PIN = 16
SCL_PIN = 17

# Create the I2C object for the time of flight sensor
i2c = I2C(0, sda=SDA_PIN, scl=SCL_PIN, freq=400000)

# Create the VL53L5CX object for the time of flight sensor
print("Starting up sensor...")
start_time = ticks_ms()
sensor = VL53L5CX(i2c)
end_time = ticks_ms()
print(f"Done in {ticks_diff(end_time, start_time)}ms...")

# Make sure to set resolution and other settings *before* you start ranging
sensor.set_resolution(RESOLUTION_8X8)
sensor.start_ranging()

# Loop forever
while True:
    if sensor.data_ready():
        # "data" is a namedtuple (attrtuple technically)
        # it includes average readings as "distance_avg" and "reflectance_avg"
        # plus a full 4x4 or 8x8 set of readings (as a 1d tuple) for both values.
        data = sensor.get_data()
        print(f"{data.distance[0]}mm {data.reflectance[0]}% (avg: {data.distance_avg}mm {data.reflectance_avg}%)")
