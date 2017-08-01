def roll(motor, led_group, direction):
? ? def on_press(state):
        Sound.speak('red is up')
? ? return on_press

rc.on_red_up = roll(0, Leds.LEFT, ? 1)
192.168.178.40

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
   def run(self):
      Sound.speak('i like to move it, move it').wait()
      time.sleep(0.5)
      Sound.speak('you like to move it, move it').wait()
      time.sleep(0.5)
      Sound.speak('we like to ... move it!').wait()


# Create new threads
thread1 = myThread()

# Start new Threads
thread1.start()

print "Exiting Main Thread"

from pydub import AudioSegment
sound = AudioSegment.from_mp3(r"C:/temp/moveit.mp3")
sound.export(r"C:\work\pyconau2017\moveit.wav", format="wav")
http://pydub.com/

from ev3dev.ev3 import *
Sound.play('/home/robot/moveit.wav')
#can't play and talk at the same time because the audio device gets blocked
Sound.speak('i like to move it, move it').wait()
Sound.speak('you like to move it, move it').wait()
Sound.speak('we like to ... move it!').wait()

cool projects http://www.ev3dev.org/projects/

Threads
remote control
sound speak and play
mp3 to wav


ABBRobotics prototyping with lego https://www.youtube.com/watch?v=-tsPuHaHFDw
lays its own bridge https://www.youtube.com/watch?v=oUJ4L4kmbHw
https://www.youtube.com/watch?v=Sjix76QjtMU top 5 3d printer CNC machine

ev3 photo booth https://github.com/dlech/ev3dev-photo-booth
https://lechnology.com/category/ev3dev/


https://sites.google.com/site/ev3python/learn_ev3_python/screen
The EV3 has a 178 x 128 pixels monochrome (black and white) LCD. The coordinates of the top-left pixel are (0, 0) and the coordinates of the bottom-right pixel are (177, 127).
#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
from PIL import Image

lcd = Screen()

from PIL import Image
im = Image.open(r'C:\work\EV3-NU-POGODI\sources\volk\nu_pogodi volk 1.jpg')
im.save(r'C:\work\EV3-NU-POGODI\sources\volk\vl1.bmp','BMP')

for i in range(2,5):
    im = Image.open(r'C:\work\EV3-NU-POGODI\sources\volk\nu_pogodi volk {0}.jpg'.format(i))
    im.save(r'C:\work\EV3-NU-POGODI\sources\volk\vl{0}.bmp'.format(i),'BMP')


logo = Image.open('pics/parkrun_tree_178x128.bmp')
lcd.image.paste(logo, (0,0))
lcd.update()
sleep(5)
sudo chvt 6
robot maker
sudo chvt 1

chmod +x myprogram.py
need #!/usr/bin/env python3

http://www.mindsensors.com/stem-with-robotics/13-pistorms-v2-base-kit-raspberry-pi-brain-for-lego-robot
https://www.smashingrobotics.com/evb-alternative-mindstorms-ev3-intelligent-brick/ evb
https://flybrix.com/ drones lego


chmod u+x job.sh
