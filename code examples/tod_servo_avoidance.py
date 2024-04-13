
from machine import I2C
from time import sleep, ticks_ms, ticks_diff
from servo import Servo, CONTINUOUS
from time import ticks_ms, ticks_diff
from breakout_vl53l5cx import VL53L5CX, RESOLUTION_8X8
import random


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

"""
Movement example using two continuous rotation servos
"""

# Constants
LEFT_SERVO_PIN = 0
RIGHT_SERVO_PIN = 1
TURNTIME = 2

UPDATES = 100
UPDATE_RATE = 1 / UPDATES

# Create Servo objects for the continuous rotation servos
left_servo = Servo(LEFT_SERVO_PIN, calibration=CONTINUOUS)
right_servo = Servo(RIGHT_SERVO_PIN, calibration=CONTINUOUS)

# Movement functions
def drive(left_speed=1.0, right_speed=1.0):
    left_servo.value(left_speed)
    right_servo.value(-right_speed)

def stop(duration=0.0):
    left_servo.value(0)
    right_servo.value(0)
    
def enable():
    left_servo.enable()
    right_servo.enable()
    
def disable():
    left_servo.disable()
    right_servo.disable()
    
def random_direction():
    return random.choice(['left', 'right'])


# Loop forever
while True:
    if sensor.data_ready():
        # "data" is a namedtuple (attrtuple technically)
        # it includes average readings as "distance_avg" and "reflectance_avg"
        # plus a full 4x4 or 8x8 set of readings (as a 1d tuple) for both values.
        data = sensor.get_data()
        print(f"{data.distance_avg}mm")
        if data.distance_avg < 100:
            
            direction = random_direction()
            print("Turning", direction)
            if direction == 'left':
                left_speed = 0.1
                right_speed = 0.0
                drive(left_speed, right_speed)
                sleep(TURNTIME)
            else:
                left_speed = 0.0
                right_speed = 0.1
                drive(left_speed, right_speed)
                sleep(TURNTIME)

    
    left_speed = 0.1
    #right_speed = 1.0 if right_button.raw() else 0.5
    right_speed = 0.1
    drive(left_speed, right_speed)
    
    sleep(UPDATE_RATE)
