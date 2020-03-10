import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)

t1 = GPIO.PWM(27, 50)

t1.start(0)

t1.ChangeDutyCycle(7.5)
time.sleep(3)

t1.stop()

GPIO.cleanup()
quit()
