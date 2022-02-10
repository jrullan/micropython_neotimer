from neotimer import *

seconds = 0
myTimer = Neotimer(1000)

while True:
    if myTimer.repeat_execution():
        seconds += 1
        print(seconds)