from time import sleep
from servo import Servo, CONTINUOUS


"""
Simple movement example using two continuous rotation servos
"""

# Constants
LEFT_SERVO_PIN = 0
RIGHT_SERVO_PIN = 1

DRIVE_SPEED = 1.0
TURN_SPEED = 1.0

# Create Servo objects for the continuous rotation servos
left_servo = Servo(LEFT_SERVO_PIN, calibration=CONTINUOUS)
right_servo = Servo(RIGHT_SERVO_PIN, calibration=CONTINUOUS)


# Movement functions
def drive_forward(speed=1.0):
    left_servo.value(speed)
    right_servo.value(-speed)

def drive_backward(speed=1.0):
    left_servo.value(-speed)
    right_servo.value(speed)

def turn_right(speed=1.0):
    left_servo.value(speed)
    right_servo.value(speed)

def turn_left(speed=1.0):
    left_servo.value(-speed)
    right_servo.value(-speed)

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
    # Drive forward for 2 seconds
    drive_forward(DRIVE_SPEED)
    sleep(2)

    # Drive forward for 2 seconds
    drive_backward(DRIVE_SPEED)
    sleep(2)

    # Turn right for 2 seconds
    turn_right(TURN_SPEED)
    sleep(2)
    
    # Turn left for 2 seconds
    turn_left(TURN_SPEED)
    sleep(2)
    
    # Stop for 2 seconds
    stop()
    sleep(2)
