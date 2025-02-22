import math

x1 = float(input('Enter the x co-ordinate of pt A: '))
y1 = float(input('Enter the y co-oridnate of pt A: '))
x2 = float(input('Enter the x co-ordinate of pt B: '))
y2 = float(input('Enter the y co-oridnate of pt B: '))

if x2-x1 != 0.0:
    slope = (y2-y1) / (x2-x1)
    angle = math.atan(slope)
    print(f'Slope= {slope}, Angle= {angle} radian')

