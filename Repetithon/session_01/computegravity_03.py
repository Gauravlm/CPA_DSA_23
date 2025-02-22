import sys

def main():
    m1= float(input('Enter the mass of object m1: '))
    m2 = float(input('Enter the mass of object m2: '))
    r = float(input('Enter the radius of object r: '))

    G = 6.67 * (10 ** -11)
    try:
        f = (G * m1 * m2) /(r * r)
    except:
        exec_name, exec_date, exec_tb= sys.exc_info()
        print(exec_name.__name__, exec_date, sep=':')
        sys.exist()

    print(f'Force of attraction {f} newton')

main()
