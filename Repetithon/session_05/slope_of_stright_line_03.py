import math

x1 = float(input('Enter x co-ordinate of point A: '))
y1 = float(input('Enter y co-ordinate of point A: ' ))

x2 = float(input('Enter x co-ordinate of point B: '))
y2 = float(input('Enter y co-ordinate of point B: ' ))

if x2-x1 != 0.0:
    slope = (y2-y1) / (x2-x1)
    angle = math.atan(slope) # angle of inclination
    print(f'slope= {slope}, Angle= {angle}')
    