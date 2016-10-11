#receive input from the user:
x1 = eval(input('x1: '))
y1 = eval(input('y1: '))
x2 = eval(input('x2: '))
y2 = eval(input('y2: '))
x3 = eval(input('x3: '))
y3 = eval(input('y3: '))
#  Calculate the sides using the Pythagorean Theorem:
side1 = ((x1 - x2)**2 + (y1 - y2)**2) ** (1/2)
side2 = ((x2 - x3)**2 + (y2 - y3)**2) ** (1/2)
side3 = ((x3 - x1)**2 + (y3 - y1)**2) ** (1/2)
#  Use the Triangle Inequality Theorem to check if it's a triangle:
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2 :
    if side1 == side2 == side3:
        print('This triangle is equilateral')
    elif side1 == side2 or side2 == side3 or side1 == side3 :
        print('This triangle is isosceles')
    else:
        print('This triangle is scalene')
else:
    print('This is not a triangle!')