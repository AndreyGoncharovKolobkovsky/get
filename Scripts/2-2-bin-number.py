import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
for i in dac:
    GPIO.setup(i, GPIO.OUT)
time.sleep(2)
number = [1, 1, 0, 0, 1, 0, 0 ,0]
while True:
    f = int(input())
    if f == 1000:
        for i in range(0, 7):
            GPIO.output(dac[i], 0)
        print('ok')
        break
    for i in range(0, 7):
        GPIO.output(dac[i], 0)
    s = bin(f) [2:]
    while len(s) != 8:
        s = '0'+s
    print('s =', s)
    for i in range(0, 7):
        GPIO.output(dac[i], int(s[i]))
