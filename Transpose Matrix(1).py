order = int(input('Order of matrix A: '))

A = []
AT = []

for i in range(order):
    A.append([0] * order)
    AT.append([0] * order)

for i in range(order):
    for j in range(order):
        A[i][j] = eval(input('Row {}, column {} of matrix A: '.format(i + 1, j + 1)))
        AT[j][i] = A[i][j]

print('A: ')

for i in range(order):
    print(A[i])

print('B: ')

for i in range(order):
    print(AT[i])