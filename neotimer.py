##########################################################################
# Raspberry Pi Pico - Non Blocking Timer (Neotimer)
#
# This program shows how to implement a non-blocking delay function
# to use in your program. It is based on the neotimer library I developed
# for Arduino and Propeller 2 in Spin 2.
#
#
#   When you use a time.sleep() function in a program,
#   the processor stops everything it is doing until this delay is completed.
#   That is called a blocking delay, because it blocks the processor until it finishes.
# 
#   Many times we don't want this to happen.
#   This timer provides a way to use time delays without
#   blocking the processor, so it can do other things while the timer ends up.
#   This is called a non-blocking delay timer.
# 
#   The timer provides basic functionality to implement different ways of timing in a program.
#   You can use the timer in the following ways:
# 
#         A) Start-Stop-Restart Timer - You can start, stop and restart the timer until done.
# 
#            start()   will reset the time (counting time) and set started and waiting true.
#            stop()    will set started and waiting false.
#                      It will also return the elapsed milliseconds since it was started
#            restart() will set the timer to started and waiting but will not reset the time.
# 
#         B) Periodic trigger - The following example will toggle pin 56 every 500ms
# 
#             led_pin = Pin(25,Pin.OUT)
#             myTimer = Neotimer(500)
#             while True:
#                 if(myTimer.repeat_execution())
#                   led_pin.toggle()
# 
#         C) Debouncer for signals - You can debounce a signal using debouce_signal.
#            The debouncing period will be duration.
#            In this example, the explorer.is_pressed(explorer.BUTTON_X) signal will
#            be debounced for 1 second:
#
#             presses = 0
#             myTimer = Neotimer(1000)
#             myTimer.start()
# 
#             while True:
#                 if myTimer.debounce_signal(explorer.is_pressed(explorer.BUTTON_X)):
#                     presses += 1
#                     print(presses)
# 
#
# Author: Jose Rullan
# Date: January 24, 2022
##########################################################################
import time

# Neotimer Class
class Neotimer:
    def __init__(self,duration):
        self.duration = duration
        self.last = time.ticks_ms()
        self.started = False
        self.waiting = False
        self.done = False
    
    # Starts the timer
    def start(self):
        self.reset()
        self.started = True
        self.waiting = True
    
    # Stops the timer
    def stop(self):
        self.started = False
        self.waiting = False
        return self.get_elapsed()
        
    # Resets the timer
    def reset(self):
        self.stop()
        self.last = time.ticks_ms()
        self.done = False
        
    # Restarts the timer
    def restart(self):
        if not self.done:
            self.started = True
            self.waiting = True
            
    # Returns True if the timer has finished
    def finished(self):
        if not self.started:
            return False
        
        if self.get_elapsed() >= self.duration:
            self.done = True
            self.waiting = False
            return True
        else:
            return False
    
    # Returns elapsed time
    def get_elapsed(self):
        return (time.ticks_ms() - self.last)
        
    # Debounces a signal with duration
    def debounce_signal(self,signal):
        if not self.started:
            self.start()
        if self.finished() and signal:
            self.start()
            return True
        else:
            return False
    
    # Returns true when timer is done and resets it
    def repeat_execution(self):
        if self.finished():
            self.reset()
            return True
        
        if not self.started:
            self.started = True
            self.waiting = True
            self.last = time.ticks_ms()
        
        return False
    
    # Working example
    def old_time_ellapsed(self):
        if time.ticks_ms()-self.time_ellapsed_last_ms >= self.duration:
            self.time_ellapsed_last_ms = time.ticks_ms()
            return True
        else:
            return False

