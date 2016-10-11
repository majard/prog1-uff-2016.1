__author__ = '116031030'
import math

def result(shape, perimeter, area):
    print('The perimeter of this {} is {} and the area is {}.\n'.format(shape, perimeter, area))

def circumference_perimeter(radius):
    return 2 * math.pi * radius

def circumference_area(radius):
    return math.pi * radius ** 2

def circumference():
    radius = eval(input('What is the circumference radius? '))
    perimeter = circumference_perimeter(radius)
    area = circumference_area(radius)
    result('circumference', perimeter, area)

def triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

def triangle_area(a, b, c):
    s = triangle_perimeter(a, b, c)
    s /= 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def triangle():
    side1 = eval(input('Side 1: '))
    side2 = eval(input('Side 2: '))
    side3 = eval(input('Side 3: '))
    area = triangle_area(side1, side2, side3)
    perimeter = triangle_perimeter(side1, side2, side3)
    result('triangle', perimeter, area)

def rectangle_perimeter(a, b):
    return 2 * a + 2 * b

def rectangle_area(a, b):
    return a * b

def rectangle():
    side1 = eval(input('Side 1: '))
    side2 = eval(input('Side 2: '))
    area = rectangle_area(side1, side2)
    perimeter = rectangle_perimeter(side1, side2)
    result('rectangle', perimeter, area)

shape = 0

while shape != 4:
    shape = int(input('Choose the shape: \n'
                      '1 - Circumference \n'
                      '2 - Triangle \n'
                      '3 - Rectangle \n'
                      '4 - Exit\n'))

    if shape == 1:
        circumference()

    elif shape == 2:
        triangle()

    elif shape == 3:
        rectangle()

