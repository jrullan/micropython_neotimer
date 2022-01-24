import gc
import picoexplorer as explorer

print("Free memory before Pimoroni explorer initialization",gc.mem_free())

# Pico Explorer Initialization
width = explorer.get_width()
height = explorer.get_height()
display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
explorer.init(display_buffer)

presses = 0

mem1 = gc.mem_free()
print("Free memory before Neotimer initialization",mem1)
from neotimer import *
myTimer = Neotimer(250)
mem2 = gc.mem_free()
print("Neotimer memory footprint",mem1-mem2)

while True:
    if myTimer.debounce_signal(explorer.is_pressed(explorer.BUTTON_X)):
        presses += 1
        print(presses)