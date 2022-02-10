# Raspberry Pi Pico - Non Blocking Timer (Neotimer)

Library footprint: approx 3kB
Instance footprint: 64-112 bytes

This library implements a non-blocking delay function
to use in your program. It is based on the neotimer library I developed
for Arduino and Propeller 2 in Spin 2.


## Explanation

When you use a time.sleep() function in a program,
the processor stops everything it is doing until this delay is completed.
That is called a blocking delay, because it blocks the processor until it finishes.
 
There are many times when we don't want this to happen.
This library provides a way to use time delays without
blocking the processor, so it can do other things while the timer ends up.
This is called a non-blocking delay timer.
 
The timer provides basic functionality to implement different ways of timing in a program.
You can use the timer in the following ways:
 
### A) Start-Stop-Restart Timer - 

You can start, stop and restart the timer until done.

start()   will reset the time (counting time) and set started and waiting true.

stop()    will set started and waiting false.
It will also return the elapsed milliseconds since it was started

restart() will set the timer to started and waiting but will not reset the time.

 ```python
            note_timer = Neotimer(200) #<-------- Initializes a 200ms timer

            if collision_detected:
                note_timer.start()     #<--------- Starts timer
                explorer.set_tone(beep_tone)
            if note_timer.finished():
                explorer.set_tone(-1)  #<--------- Called after 200ms
```

### B) Periodic trigger - 

The following example will toggle pin 56 every 500ms

```python
            led_pin = Pin(25,Pin.OUT)
            myTimer = Neotimer(500)<---------------- Initializes a 500ms timer

            while True:
                if(myTimer.repeat_execution())
                  led_pin.toggle() <---------------- Called every 500ms
```

### C) Periodic trigger with count - 

The following example will toggle pin 56 every 500ms, only 3 times. 

To reset the repetitions use reset_repetitions().

```python
            led_pin = Pin(25,Pin.OUT)
            button = Pin(2, Pin.IN)

            myTimer = Neotimer(500)<---------------- Initializes a 500ms timer
            
            while True:
                if(myTimer.repeat_execution(3)) <--- Only repeat 3 times
                  led_pin.toggle() <---------------- Called every 500ms
                if(button.value())
                  myTimer.reset_repetitions() <----- Reset repetitions

```

### D) Debouncer for signals

You can debounce a signal using debouce_signal.
The debouncing period will be duration.

In this example, the button pin value signal will
be debounced for 250 milliseconds:
```python
            button = Pin(2, Pin.IN)
            presses = 0
            myTimer = Neotimer(250) <--------------- Initializes a 250ms timer

            while True:
                if myTimer.debounce_signal(button.value()): <----- button pressed signal debounced for 250ms
                   presses += 1
                   print(presses)
```

### E) Waiting - 

The following example will turn on the led for 1000ms each time the button is pressed

```python
            from machine import Pin
            from neotimer import *

            button = Pin(2, Pin.IN)
            led = Pin(25,Pin.OUT)
            led.off()

            myTimer = Neotimer(1000)
            debouncer = Neotimer(200)
 
            while True:
 
                if debouncer.debounce_signal(button.value()):
                    myTimer.start()

                if myTimer.waiting():
                    led.on()
                else:
                    led.off()
``` 

Author: Jose Rullan

Date: January 24, 2022
