from controller import *
from display import *
import time

O1.set_brightness(512)
while True:
  if I1.get_state():
    time.sleep(5)
    O1.set_brightness(0)
    O2.set_brightness(512)
    time.sleep(10)
    O2.set_brightness(0)
    O1.set_brightness(512)
