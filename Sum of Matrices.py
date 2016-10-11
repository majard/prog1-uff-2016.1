A = []
B = []
C = []

for i in range(2):
    lineA = []
    lineB = []
    lineC = []
    for j in range(2):
        lineA.append(eval(input('Input column {}, row {} of matrix A: '.format(i + 1, j + 1))))
        lineB.append(eval(input('Input column {}, row {} of matrix B: '.format(i + 1, j + 1))))
        lineC.append(lineA[j] + lineB[j])
    A.append(lineA)
    B.append(lineB)
    C.append(lineC)
print('A + B = ', C)
