matrix = []
highestSum = 0
highestSumLine = 0

for row in range(3):
    line = []
    sum = 0
    for column in range(3):
        line.append(int(input('row {}, column {}: '.format(row + 1, column + 1))))
        sum += line[column]
    if sum > highestSum:
        highestSumLine = row
        highestSum = sum
    matrix.append(line)

print('Matrix: {}\n'
      'Highest Sum Line: {}\n'
      'Highest Sum: {}\n'.format(matrix, matrix[highestSumLine], highestSum))