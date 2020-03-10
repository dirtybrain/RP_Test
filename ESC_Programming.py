#!usr/bin/env python
__author__ = "Xiaoguang Zhang"
__email__ = "xzhang@westwoodrobotics.net"
__copyright__ = "Copyright 2020 Westwood Robotics"
__date__ = "Jan 8, 2020"
__version__ = "0.0.1"
__status__ = "Prototype"

# A piece of code to program T-Motor A10 ESC without stick
# GPIO 27 for output

import time
import ESC_Setup
import RPi.GPIO as GPIO

A10 = ESC('A10',50,90,10)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
ESC = GPIO.PWM(27, A10.freq) # Set GPIO27 to output 50Hz PWM

print("Make sure the ESC is powered OFF. Starting ESC Programming in 3 sec...")
time.sleep(3)
ESC.start(A10.duty_max)
user = input("Power on the ESC and press Enter.")
user = input("Press Enter when the ESC is in desired mode...")
ESC.ChangeDutyCycle(A10.duty_min)
time.sleep(4)
print("ESC programming complete.")
ESC.stop()

GPIO.cleanup()
#quit()
