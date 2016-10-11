a = eval(input('a: '))
b = eval(input('b: '))
op = input('Operation (+, -, *, /): ')
if op == '+':
    print('a + b =', a + b)
elif op == '-':
    print('a - b =', a - b)
elif op == '*':
    print('a * b =', a * b)
elif op == '/':
    print('a / b =', a / b)
else:
    print('Input a valid operation! + or - or * or /')


