A = []
B = []
C = []

rows_A = eval(input('Input number of rows in A: '))
columns_A = eval(input('Input number of columns in A: '))
rows_B = eval(input('Input number of rows in B: '))
columns_B = eval(input('Input number of columns in B: '))

for rows in range(rows_A):
    line = []
    for columns in range(columns_A):
        line.append(eval(input('Row: {}, column {} of matrix A: '.format(rows + 1, columns + 1))))
    A.append(line)

for rows in range(rows_B):
    line = []
    for columns in range(columns_B):
        line.append(eval(input('Row: {}, column {} of matrix B: '.format(rows + 1, columns + 1))))
    B.append(line)

if columns_A == rows_B:
    for rows in range(rows_A):
        line = []
        for columns in range(columns_B):
            sum = 0
            for index in range(columns_A):
                sum += A[rows][index] * B[index][columns]
            line.append(sum)
        C.append(line)

else:
    print('The multiplication of A and B is undefined (the number of columns in '
          'Matrix A does not equal the number of rows in Matrix B.).')

print('A: ', A)
print('B: ', B)
print('C: ', C)