A = []
B = []

rows_A = int(input('Rows in A: '))
columns_A = int(input('Columns in A: '))

for row in range(rows_A):
    line = []
    for column in range(columns_A):
        line.append(eval(input('Row {}  Column {} of A: '.format(row +1, column + 1))))
    A.append(line)

rows_B = int(input('Rows in B: '))
columns_B = int(input('Columns in B: '))

for row in range(rows_B):
    line = []
    for column in range(columns_B):
        line.append(eval(input('Row {}  Column {} of B: '.format(row +1, column + 1))))
    B.append(line)

#check if they are multipliable and will generate a square matrix (identity):
if rows_B == columns_A == rows_A == columns_B:
    theyAreInverse = True  #assume A and B are inverse matrices

    # A * B:
    for row in range(rows_A):
        for column in range(columns_B):
            sum = 0
            for i in range(columns_A):
                sum += A[row][i] * B[i][column]
            sum = round(sum, 10)  #round because floats aren't precise

            #check if it is an identity matrix:
            if column == row:
                if sum != 1:
                    theyAreInverse = False
            elif sum != 0:
                theyAreInverse = False


    #B * A:

    for row in range(rows_B):
        line = []
        for column in range(columns_A):
            sum = 0
            for i in range(columns_B):
                sum += B[row][i] * A[i][column]
            sum = round(sum, 10)  #round because floats aren't precise
            line.append(sum)

            #check if it is an identity matrix:
            if column == row:
                if sum != 1:
                    theyAreInverse = False
            elif sum != 0:
                theyAreInverse = False

    if theyAreInverse:
        print('A and B are inverse matrices.')
    else:
        print('A and B are not inverse matrices.')

else:
    print('A and B are not inverse matrices.')