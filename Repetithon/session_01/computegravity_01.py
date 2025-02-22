'''
@Goal: Computa Gravitational
Formula :  G * (m1*m2) / r^2
'''

import sys

def main():
    m1 = float(input('Enter mass of object m1: '))
    m2 = float (input('Enter mass of object m2: '))
    r = float(input('Enter the radius of object:'))
    G = 6.67 * (10 ** -11)
    try:
        F = (G*m1*m2) / r * r
    except:
        exec_name, exec_date, exec_tb = sys.exc_info()
        print(exec_name.__name__, exec_date, sep=':')
        sys.exit(-1)
    print(f'Force of attraction {F} newton')

main()