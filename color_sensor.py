#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *

from time import sleep


Sound.beep()

cl = ColorSensor()
ts = TouchSensor()
cl.mode = 'COL-COLOR'

colors = ('unknown black blue green yellow red white brown'.split())

last_color = None
while not ts.value():
    color = colors[cl.value()]
    if not last_color == color:
        Sound.speak(color).wait()
        last_color = color
    sleep(1)

Sound.beep()
