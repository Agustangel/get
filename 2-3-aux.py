import RPi.GPIO as asd 
import time

asd.setmode(asd.BCM)

leds = [24, 25, 8, 7, 12, 16, 20, 21]
aux = [2, 3, 14, 15, 18, 27, 23, 22]

asd.setup(leds, asd.OUT)
asd.setup(aux, asd.IN)

while True:
        for i in range(8):
            asd.output(leds[i], asd.input(aux[i]))