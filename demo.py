#!/usr/bin/env python3

'''
Source name: demo.py
Author(s): Stoyan Shopov

Python Version: 3.* 32-bit or 64-bit
License: LGPL

Description:
    This program was demoed on EV3D4 at PyCon Australia 2017.
    It kicks off 2 threads a move thread and a feel thread. 
    The move thread drives the bot forward until the feel thread 
    detects an obstacle. 
    Then the move thread makes the bot move around in a circle
    until the feel thread detects a touch on the touch sensor. 

Preconditions:
    The program has been loaded on to EV3 running ev3dev 

Postcoditions:
    Program exits cleanly. 

References:
    https://github.com/sshopov/pyconau2017
    https://github.com/rhempel/ev3dev-lang-python 
    
Release history:
----------------------------------------------------
0.0.1 - 06/08/2017:
    Initial release
'''

import sys
import time
import threading
import signal 

from ev3dev import ev3

def move(done):
    lm = ev3.LargeMotor('outB'); assert lm.connected
    
    rm = ev3.LargeMotor('outC'); assert rm.connected
    
    cl = ev3.ColorSensor(); assert cl.connected
    cl.mode='COL-AMBIENT'
    
    speed = 250 #cl.value()

    lm.run_forever(speed_sp=speed)
    rm.run_forever(speed_sp=speed)

    while not done.is_set():
        time.sleep(1)  
    
    #stop both motors
    lm.stop(stop_action='brake')
    rm.stop(stop_action='brake')
    lm.wait_while('running')
    rm.wait_while('running')
    
    #run around in a circle
    done.clear()
    lm.run_forever(speed_sp=speed)
    
    while not done.is_set():
        time.sleep(1)
        
    lm.stop(stop_action='brake')
    lm.wait_while('running')

def feel(done):
    ir = ev3.InfraredSensor(); assert ir.connected
    ts = ev3.TouchSensor(); assert ts.connected

    screen = ev3.Screen()
    sound = ev3.Sound()

    screen.draw.text((60,40), 'Going for a walk')
    screen.update()

    while ir.proximity > 30:
        if done.is_set(): 
            break
        time.sleep(0.1)

    done.set() #this will set it running in a circle
    
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
    
    screen.clear()
    screen.draw.text((60,20), 'There is something is front of me')
    screen.update()
    
    while not ts.is_pressed:
        sound.speak("Where should I go next?").wait()
        time.sleep(0.5)
    
    done.set() #will stop the circle dance

# The 'done' event will be used to signal the threads to stop:
done = threading.Event()

# We also need to catch SIGINT (keyboard interrup) and SIGTERM (termination
# signal from brickman) and exit gracefully:
def signal_handler(signal, frame):
    done.set()

signal.signal(signal.SIGINT,  signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Now that we have the worker functions defined, lets run those in separate
# threads.
move_thread = threading.Thread(target=move, args=(done,))
feel_thread = threading.Thread(target=feel, args=(done,))

move_thread.start()
feel_thread.start()

# The main thread will wait for the 'back' button to be pressed.  When that
# happens, it will signal the worker threads to stop and wait for their completion.
btn = ev3.Button()
while not btn.backspace and not done.is_set():
    time.sleep(1)

done.set()
move_thread.join()
feel_thread.join()  

ev3.Sound.speak('Farewell and good bye!').wait()
ev3.Leds.all_off()      