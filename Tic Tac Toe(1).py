matrix = []

for row in range(3):
    line = []
    for column in range(3):
        char = input('Row {} Column {} ("x" or "o" or ""): '.format(row + 1, column + 1))
        line.append(char)
        if char == '':
            play = [row, column]  #assigns an available position to play
    matrix.append(line)

for row in range(3):
    print(matrix[row])

won = False

if matrix[0][0] == matrix[1][1] and matrix[2][2] == '':
    play = [2, 2]
    if matrix[0][0] == 'x':
        won = True
elif matrix[0][0] == matrix[2][2] and matrix[1][1] == '':
    play = [1, 1]
    if matrix[0][0] == 'x':
        won = True
elif matrix[1][1] == matrix[2][2] and matrix[0][0] == '':
    play == [0, 0]
    if matrix[1][1] == 'x':
        won = True
elif matrix[0][2] == matrix[1][1] and matrix[2][0] == '':
    play = [2, 0]
    if matrix[0][2] == 'x':
        won = True
elif matrix[0][2] == matrix[2][0] and matrix[1][1] == '':
    play = [1, 1]
    if matrix[0][2] == 'x':
        won = True
elif matrix[1][1] == matrix[2][0] and matrix[0][2] == '':
    play = [0, 2]
    if matrix[1][1] == 'x':
        won = True
else:
    index = 0
    while index < 3 and not won:
        if matrix[index][0] == matrix[index][1] and matrix[index][2] == '':
            play = [index, 2]
            if matrix[index][0] == 'x':
                won = True
        elif matrix[index][0] == matrix[index][2] and matrix[index][1] == '':
            play = [index, 1]
            if matrix[index][0] == 'x':
                won = True
        elif matrix[index][1] == matrix[index][2] and matrix[index][0] == '':
            play = [index, 0]
            if matrix[index][1] == 'x':
                won = True
        elif matrix[0][index] == matrix[1][index] and matrix[2][index] == '':
            play = [2, index]
            if matrix[0][index] == 'x':
                won = True
        elif matrix[0][index] == matrix[2][index] and matrix[1][index] == '':
            play = [1, index]
            if matrix[0][index] == 'x':
                won = True
        elif matrix[1][index] == matrix[2][index] and matrix[0][index] == '':
            play = [0, index]
            if matrix[1][index] == 'x':
                won = True
        index += 1

print('x should play at row {} column {}.'.format(play[0] +1, play[1] + 1))

if won:
    print('x has won!')