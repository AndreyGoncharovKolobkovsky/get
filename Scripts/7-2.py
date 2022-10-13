import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
troyka = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
for i in range(len(leds)):
    GPIO.setup(leds[i], GPIO.OUT)

def toBin(Value):
    return [int(elm) for elm in bin(Value)[2:].zfill(8)]

def LedsOutput(Num):
    Bin = toBin(Num)
    for i in range(len(leds)):
        GPIO.output(leds[i], Bin[i])

def adc():
    r = 256
    left = 0
    md = (r + left) // 2
    while (r - left) > 1:
        GPIO.output(dac, toBin(md))
        time.sleep(0.001)
        compVal = GPIO.input(comp)
        if compVal == 0:
            r = md
        else:
            left = md
        md = (r + left) // 2
    #volt = 3.3 * left / 256
    return left

try:
    Array = []
    print("Exp. is running...")
    Begin = time.time()
    GPIO.output(troyka, 1)
    while True:
        Temp = adc()
        Array.append(Temp)
        print(3.3 * Temp / 256)
        LedsOutput(Array[len(Array) - 1])
        if Array[len(Array) - 1] >= 0.97 * 3.3:
            break
    GPIO.output(troyka, 0)
    while True:
        Temp = adc()
        Array.append(Temp)
        print(3.3 * Temp / 256)
        LedsOutput(Array[len(Array) - 1])
        if Array[len(Array) - 1] < 0.02 * 3.3:
            break
    End = time.time()
    Timeresult = End-Begin
    print("Process time", Timeresult, "sec")
    SamplingFrequency = Timeresult/len(Array)
    QuantizationStep = 3.3/256
    String_Array = [str(i) for i in Array]
    with open("data.txt", "w") as DataOutput:
        DataOutput.write('/n'.join(String_Array))
    with open("settings.txt", "w") as DataOutput:
        DataOutput.write("Sampling frequensy = " + str(SamplingFrequency))
        DataOutput.write("Quantization step = " + str(QuantizationStep))
    print("Experiment time =", Timeresult)
    print("Period =", Timeresult/len(Array))
    print("Sampling frequensy = " + str(SamplingFrequency))
    print("Quantization step = " + str(QuantizationStep))
    plt.plot(Array)
    plt.show()
finally:
    for i in range(0, 8):
        GPIO.output(dac[i], 0)
        GPIO.output(leds[i], 0)
    GPIO.cleanup(dac)
    GPIO.output(troyka, 0)