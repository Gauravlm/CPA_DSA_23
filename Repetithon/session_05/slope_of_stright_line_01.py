'''
Goal: using x,y coordinate of 2 points find out
1. slope
2. angle of inclination
'''

import sys
import math

x1 = float(input('Enter x coordinate of point 1:'))
y1 = float(input('Enter x coordinate of point 1:'))
x2 = float(input('Enter x coordinate of point 2:'))
y2 = float(input('Enter x coordinate of point 2:'))

if x2 - x1 != 0.0:
    slope = (y2-y1) / (x2-x1)
    angle = math.atan(slope)
    print(f'slope ={slope}, Angle={angle} radians')
