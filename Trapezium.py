a = eval(input('A: '))
b = eval(input('B: '))
c = eval(input('C: '))
if a > 0 and b > 0 and c > 0:
    area = (a + b) / 2 * c
    print('The area is', area)
else:
    print('All numbers must be positive!')