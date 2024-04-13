from time import sleep, ticks_ms, ticks_diff
from pimoroni import Button
from servo import Servo, CONTINUOUS


"""
Movement example using two continuous rotation servos, and two buttons controlling each servo independently
"""

# Constants
LEFT_SERVO_PIN = 0
RIGHT_SERVO_PIN = 1
LEFT_BUTTON_PIN = 3
RIGHT_BUTTON_PIN = 22

UPDATES = 100
UPDATE_RATE = 1 / UPDATES

# Create Servo objects for the continuous rotation servos
left_servo = Servo(LEFT_SERVO_PIN, calibration=CONTINUOUS)
right_servo = Servo(RIGHT_SERVO_PIN, calibration=CONTINUOUS)

# Create the Button objects
left_button = Button(LEFT_BUTTON_PIN)
right_button = Button(RIGHT_BUTTON_PIN)


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


# Loop forever
while True:
    
    left_speed = 1.0 if left_button.raw() else 0.0
    right_speed = 1.0 if right_button.raw() else 0.0
    drive(left_speed, right_speed)
    
    sleep(UPDATE_RATE)
