from machine import Pin
import picoexplorer as explorer
from neotimer import *

# Pico Explorer Initialization
width = explorer.get_width()
height = explorer.get_height()
display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
explorer.init(display_buffer)

presses = 0
led_pin = Pin(25,Pin.OUT)

myTimer = Neotimer(250)
blinker = Neotimer(200)

while True:
    if myTimer.debounce_signal(explorer.is_pressed(explorer.BUTTON_X)):
        presses += 1
        if blinker.duration < 1000:
            blinker.duration += 50
        print(presses, blinker.duration)

    if myTimer.debounce_signal(explorer.is_pressed(explorer.BUTTON_Y)):
        presses += 1
        if blinker.duration >= 100:
            blinker.duration -= 50
        print(presses, blinker.duration)

    if blinker.repeat_execution():
        led_pin.toggle()