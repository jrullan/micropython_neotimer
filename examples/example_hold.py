from neotimer import *
from machine import Pin

BUTTON_A = Pin(20,Pin.IN)

led = Pin(25,Pin.OUT)

myTimer = Neotimer(1000)

while True:
    if myTimer.hold_signal(BUTTON_A.value()):
        led.on()
    else:
        led.off()