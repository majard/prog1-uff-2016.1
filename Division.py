x = eval(input('x: '))
y = eval(input('y: '))
result = 0
if y == 0:
    print('Cannot divide by zero!')
else:
    while x >= y:
        x -= y
        result += 1
if y != 0:
    print('x / y = ', result,'\nremainder= ', x)