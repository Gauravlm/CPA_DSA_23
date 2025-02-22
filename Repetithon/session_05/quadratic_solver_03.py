

import sys

a = float(input('Enter CF of x^2: '))
b = float(input('Enter the CF of x: '))
c = float(input('Enter the constant of eqn'))

if a== 0.0:
    print('CF of x^2 cannot be zero')
    sys.exit()
if b**2 - (4 * a*c) < 0.0:
    print('This eq. does not have in real numbers')
    sys.exit()

r1 = (-b + (b**2 - 4*a*c) ** 0.5) /(2*a)
r2 = (-b -(b**2 - 4*a*c) ** 0.5) /(2*a)
print(f'root1: {r1}, Root: {r2}')