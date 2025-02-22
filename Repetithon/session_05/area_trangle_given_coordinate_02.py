import sys 

x1= float(input('Enter x coordinate of point A: '))
y1= float(input('Enter y coordinate of point A: '))

x2= float(input('Enter x coordinate of point B: '))
y2= float(input('Enter y coordinate of point B: '))

x3= float(input('Enter x coordinate of point C: '))
y3= float(input('Enter y coordinate of point C: '))

slop_AB = abs((y2-y1)/(x2-x1))
slop_AC = abs((y3-y1)/(x3-x1))

if slop_AB == slop_AC:
    print('A,B, C')
    sys.exit()

a = ((x3-x2)**2 + (y3-y2)**2) ** 0.5
b= ((x3-x1) **2 + (y3- y1)**2) ** 0.5
c= ((x2-x1) **2 + (y2-y1)**2) ** 0.5

s = (a+b+c)/2

area = (s * (s-a) * (s-b) * (s-c)) ** 0.5

print(f'Area = {area} units')
