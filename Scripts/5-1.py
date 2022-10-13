import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

def toBin(Value):
    return [int(elm) for elm in bin(Value)[2:].zfill(8)]

def adc(value):
    signal = toBin(value)
    GPIO.output(dac, signal)
    return signal

try:
    while True:
        for value in range(0, 256):
            #print(value)
            s = adc(value)
            V = (value /(2**8)) * 3.3
            CompRes = GPIO.input(comp)
            #print(CompRes)
            time.sleep(0.007)
            if CompRes == 0:
                print(value, s, V)
                break
            
except Exception:
    print("Bad input")
finally:
    for i in range(0, 8):
        GPIO.output(dac[i], 0)
    GPIO.cleanup(dac)