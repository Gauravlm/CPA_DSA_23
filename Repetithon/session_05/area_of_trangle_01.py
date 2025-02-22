'''
Goal : Get lenght of a,b,c 
compute area using horns formula
'''

import sys

a = float(input('Enter the length of side a: '))
b = float(input('Enter the length of side b: '))
c = float(input('Enter the length of side c: '))

if (a + b <= c) or (b + c <=a) or (c + a <=b):
    print('Invalide length for sides of a triangle')
    sys.exit()

s = (a + b + c) /2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print(f'Area of triangle {area} sq. units')
