from neotimer import *
from machine import Pin

BUTTON_A = Pin(20,Pin.IN)

led = Pin(25,Pin.OUT)

myTimer = Neotimer(3000)
seconds = Neotimer(1000)

while True:
    if not BUTTON_A.value() and seconds.repeat_execution() and not led.value():
        print(myTimer.get_elapsed())
        
    if myTimer.hold_signal(not BUTTON_A.value()):
        led.on()
    else:
        led.off()