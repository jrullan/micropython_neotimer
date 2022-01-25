from machine import Pin
from neotimer import Neotimer

led = Pin(25,Pin.OUT)
led.off()

blinker = Neotimer(150)

while True:
    if blinker.repeat_execution_times(10):
        led.toggle()
        print(blinker.repetitions)