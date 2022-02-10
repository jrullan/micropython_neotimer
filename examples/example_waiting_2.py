from machine import Pin
from neotimer import *
import picoexplorer as explorer

# Pimoroni Explorer Initialization
width = explorer.get_width()
height = explorer.get_height()
display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
explorer.init(display_buffer)

led = Pin(25,Pin.OUT)
led.off()

myTimer = Neotimer(1000)
debouncer = Neotimer(200)

while True:

    if myTimer.waiting():
        led.on()
    else:
        led.off()

    if debouncer.debounce_signal(explorer.is_pressed(explorer.BUTTON_A)):
        myTimer.start()
