matrix = []

for row in range(6):
    line = []
    for column in range(3):
        line.append(eval(input('Row {}, Column {} :'.format(row + 1, column + 1))))
    matrix.append(line)

#creates matrices with the value and position of the smallest and greatest number in the matrix.
#assume they are in the first position possible:

smallest = [matrix[0][0], 0, 0]
greatest = [matrix[0][0], 0, 0]

for row in range(6):
    for column in range(3):
        if smallest[0] > matrix[row][column]:
            smallest =[matrix[row][column], row, column]
        elif greatest[0] < matrix[row][column]:
            greatest = [matrix[row][column], row, column]

print('The smallest number is {} in row {} column {}.'.format(smallest[0], smallest[1] + 1, smallest[2] + 1))
print('The greatest number is {} in row {} column {}.'.format(greatest[0], greatest[1] + 1, greatest[2] + 1))
