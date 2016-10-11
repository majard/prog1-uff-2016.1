matrix = []

for i in range(3):
    line = []
    for j in range(3):
        line.append(eval(input('Input column {}, row {}: '.format(i + 1, j + 1))))
    matrix.append(line)

k = eval(input('Input k: '))

print('Matrix before multiplying: ', matrix)

for i in range(3):
    matrix[i][i] *= k  #the main diagonal is where j = i

print('Matrix after multiplying: ', matrix)