integer = eval(input('Input an integer: '))
x = 1
if integer == 0:
    counter = 1
else:
    counter = 0
while integer // x > 0:
    x *= 10
    counter += 1
print('The integer has', counter, 'digit(s).')
