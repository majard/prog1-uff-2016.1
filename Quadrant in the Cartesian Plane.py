x = eval(input('x: '))
y = eval(input('y: '))
solution = 'x: ' + str(x) + ' y: ' + str(y) + '\n' + 'Quadrant: '
if x > 0 and y > 0:
    solution += '1'
elif x < 0 and y > 0:
    solution += '2'
elif x < 0 and y < 0:
    solution += '3'
elif x > 0 and y < 0:
    solution += '4'
elif x == y == 0:
    solution += '0'
elif x == 0 or y == 0:
    solution += '-1'
print(solution)