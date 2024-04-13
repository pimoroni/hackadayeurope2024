from time import sleep, ticks_ms, ticks_diff
from pimoroni import Button
from servo import Servo, CONTINUOUS


"""
Movement example using two continuous rotation servos, and a button to stop the program
"""

# Constants
LEFT_SERVO_PIN = 0
RIGHT_SERVO_PIN = 1
BUTTON_PIN = 3

DRIVE_SPEED = 1.0
TURN_SPEED = 1.0

# Create Servo objects for the continuous rotation servos
left_servo = Servo(LEFT_SERVO_PIN, calibration=CONTINUOUS)
right_servo = Servo(RIGHT_SERVO_PIN, calibration=CONTINUOUS)

# Create a Button object
button = Button(BUTTON_PIN)


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

# Variables
sequence = 0
wait_time = 0
start = ticks_ms()

# Loop until the attached button is pressed
while not button.raw():
    
    # Check if enough time has passed to start the next part of the sequence
    current = ticks_ms()
    if ticks_diff(current, start) >= wait_time * 1000:
        start = current  
        
        # Set the motor speeds, based on the sequence
        if sequence == 0:
            drive_forward(DRIVE_SPEED)
        elif sequence == 1:
            drive_backward(DRIVE_SPEED)
        elif sequence == 2:
            turn_right(DRIVE_SPEED)
        elif sequence == 3:
            turn_left(DRIVE_SPEED)
        elif sequence == 4:
            stop()
        
        # Wait for 2 seconds
        wait_time = 2
        
        # Move on to the next part of the sequence
        sequence += 1

        # Loop the sequence back around
        if sequence >= 5:
            sequence = 0

# Turn off the servos
disable()