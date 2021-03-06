#!usr/bin/env python
__author__ = "Xiaoguang Zhang"
__email__ = "xzhang@westwoodrobotics.net"
__copyright__ = "Copyright 2020 Westwood Robotics"
__date__ = "Jan 8, 2020"
__version__ = "0.0.1"
__status__ = "Prototype"

# GPIO 27 for output

import time
from ESC_Setup import *
import RPi.GPIO as GPIO

A10 = ESC('A10',50,90,5)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
ESC = GPIO.PWM(27, A10.freq) # Set GPIO27 to output 50Hz PWM

print("Make sure the ESC is powered OFF. Starting in 3 sec...")
time.sleep(3)
ESC.start(A10.duty_min)
user = input("Power on the ESC and press Enter.")
user = float(input("Input desired speed:(10~90)"))
ESC.stop()
ESC.start(user)
run = True
while run:
    try:
        1
    except:
        print("An exception occurred")
        run = False

