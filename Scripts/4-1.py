import RPi.GPIO as GPIO
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
for i in dac:
    GPIO.setup(i, GPIO.OUT)
def toBin(Value):
    return [int(elm) for elm in bin(Value)[2:].zfill(8)]
try:
    while True:
        f = input()
        if f == "q":
            print("ok")
            break
        Value = int(f)
        S = toBin(Value)
        print(S)
        if Value > 255:
            print("Bad input")
            break
        else:
            print((3.3/256)*Value)
            for i in range(0, 8):
                GPIO.output(dac[i], S[i])
except Exception:
    print("Bad input")
finally:
    for i in range(0, 8):
        GPIO.output(dac[i], 0)