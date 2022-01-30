from machine import Pin
from neotimer import *

led = Pin(25,Pin.OUT)
led.off()

myTimer = Neotimer(1000)

while myTimer.waiting():
    led.on()

led.off()