#!/usr/bin/env python3
'''
Source name: starwars.py
Author(s): Stoyan Shopov

Python Version: 2.7, 3.* 32-bit or 64-bit
License: LGPL

Description:
    This program was run on the EV3D4 (R2D2 look-a-like) at Mount Barker parkrun 175. 
    The droid help deliver the welcome speech. 
    It had queued lines and they were delivered when the remote control was pressed (to allow 
    for interaction with the presenter).
    The photo album can be found here: 
    https://www.facebook.com/mountbarkerparkrun/posts/1603265023049154

Preconditions:
    The program has been loaded on to EV3 running ev3dev 

Postcoditions:
    Program exits when back button is pressed. 

References:
    http://www.ev3dev.org/
    https://sites.google.com/site/ev3python/
    The WAVs came from http://www.moviewavs.com/Movies/Star_Wars.html 
    
Release history:
----------------------------------------------------
0.0.1 - 01/07/2017:
    Initial release
'''

import os
import time

from ev3dev.ev3 import *

Sound.beep()

rc = RemoteControl()

mB = LargeMotor('outB')
mC = LargeMotor('outC')

counter = -1
script = [ 'My name is R2 D2 and I come from a galaxy far far away!',
    '''It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire.
    During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armo=red space station with enough power to destroy an entire planet.
    Unfortunately, the rebels have dropped the secret plans somewhere between here and the turn around flag near Bald Hills Road. I call for heros to look for them, find them and bring them back here to the start line.''',
    'Are there any visitors or first timers?',
    'That is good! You can go first and act as decoy for the storm troopers.',
    'Wait, wait!',
    '''I feel a disturbance in the force. There is someone here who has reached 50 parkruns.
    He has a personal best of 26 22. He runs and volunteers with his wife Melissa and his sons Bailey and Sam. The force is strong with this one. His name is Leon.''',
    '/home/robot/sounds/myonlyhope.wav',
    'Yes, I meant Leon Wan Kenobi. Sorry!',
    'Chancellor Brian Haddy will give you a voucher to take with you.',
    '/home/robot/sounds/lightsaber.wav',
    'You must also take a young jedai with you to help you on your quest. Bryannan Coook has just done 10 park runs.',
    'Farewell heros! Run fast!',
    'Do not forget to thank our volunteer Jedai knights: Jo, Georgia, Andrew, Jackson, Martin and Sammy.',
    'May the force be with you!',
    '/home/robot/sounds/starwars.wav',
]

say = Sound.speak
play = Sound.play

def queue():
    print(counter)
    if counter in range(0, len(script)):
        line = script[counter]
        print(line)
        if os.path.exists(line):
            play(line)
        else:
            say(line)

def next_line():
    print('next line')
    def on_press(state):
        print(state)
        global counter
        if state:
            if not counter > len(script) - 2:
                counter += 1
                queue()
    return on_press

def test():
    for i in range(20):
        rc.process()
        time.sleep(0.01)
    Sound.beep()

def previous_line():
    def on_press(state):
        global counter
        if state:
            if counter > 1:
                counter -= 1
                queue()
    return on_press

def roll(duration, speed):
    def on_press(state):
        if state:
            mB.run_timed(time_sp=duration, speed_sp=speed)
            mC.run_timed(time_sp=duration, speed_sp=speed)
            play('/home/robot/sounds/r2d2-1.wav').wait()
            play('/home/robot/sounds/r2d2-2.wav').wait()
            play('/home/robot/sounds/r2d2-3.wav').wait()
            play('/home/robot/sounds/r2d2-4.wav').wait()
            play('/home/robot/sounds/r2d2-5.wav').wait()
    return on_press

# Assign event handler to each of the remote buttons
rc.on_red_up = next_line()
rc.on_red_down = previous_line()
rc.on_blue_up = roll(2000, -250)
rc.on_blue_down = roll(2000, 250)



##mB.stop()
##mC.stop()
##
### to make extra sure the motors have stopped:
##mB.run_forever(speed_sp=0)
##mC.run_forever(speed_sp=0)

while True: #replaces previous line so use Ctrl-C to exit
    rc.process()
    time.sleep(0.01)

#  Ctrl-C if on terminal or a long press on the back button if on Brickman
