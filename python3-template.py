#!python3

import sys
import time
from math import pi

def circle_area(r):
    return round(pi * r**2,2)

print(sys.version)
print(circle_area(1))
time.sleep(2)

