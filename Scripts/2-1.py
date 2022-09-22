import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
for i in range(len(leds)):
    GPIO.setup(leds[i], GPIO.OUT)

for i in range(0, 10):
    for j in leds:
        GPIO.output(j, 1)
        time.sleep(0.1)
        GPIO.output(j, 0)