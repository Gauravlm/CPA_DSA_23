'''
Goal: using x,y co-ordinates of 2 points find distance 
'''

x1 = float(input('Enter x co-ordinate of point A: '))
y1 = float(input('Enter y co-ordinate of point A: ' ))

x2 = float(input('Enter x co-ordinate of point B: '))
y2 = float(input('Enter y co-ordinate of point B: ' ))

d= ((x2-x1)**2 + (y2-y1)**2) **0.5
print(f'Distance bet. the point {d}  units')