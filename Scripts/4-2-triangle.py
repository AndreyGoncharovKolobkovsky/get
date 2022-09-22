import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
for i in dac:
    GPIO.setup(i, GPIO.OUT)
def toBin(Value):
    return [int(elm) for elm in bin(Value)[2:].zfill(8)]
try:
    while True:
        for j in range(0, 256):
            for i in range(0, 8):
                GPIO.output(dac[i], 0)
            S = toBin(j)
            for i in range(0, 8):
                GPIO.output(dac[i], S[i])
            time.sleep(0.1)
        for j in range(254, -1, -1):
            for i in range(0, 8):
                GPIO.output(dac[i], 0)
            S = toBin(j)
            for i in range(0, 8):
                GPIO.output(dac[i], S[i])
            time.sleep(0.1)
except Exception:
    print("Bad input")
finally:
    for i in range(0, 8):
        GPIO.output(dac[i], 0)