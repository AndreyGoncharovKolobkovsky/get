import RPi.GPIO as GPIO
import time
t = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 1)
time.sleep(t)
GPIO.output(2, 0)
time.sleep(t)
GPIO.output(2, 1)
time.sleep(t)
GPIO.output(2, 0)
time.sleep(t)