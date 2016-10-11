matrix = []

for row in range(3):
    line = []
    for column in range(3):
        line.append(input('Row {} Column {} ("x" or "o" or "-"): '.format(row + 1, column + 1)))
    matrix.append(line)

for row in range(3):
    print(matrix[row])


played = False
cantWin = False  #the computer always assumes it can win
won = False

if matrix[0][0] == matrix[1][1] != '-' and matrix[2][2] == '-':
    play = [2, 2]
    played = True
    if matrix[0][0] == 'x':
        won = True

elif matrix[0][0] == matrix[2][2] != '-' and matrix[1][1] == '-':
    play = [1, 1]
    played = True
    if matrix[0][0] == 'x':
        won = True

elif matrix[1][1] == matrix[2][2] != '-' and matrix[0][0] == '-':
    play == [0, 0]
    played = True
    if matrix[1][1] == 'x':
        won = True

elif matrix[0][2] == matrix[1][1] != '-' and matrix[2][0] == '-':
    play = [2, 0]
    played = True
    if matrix[0][2] == 'x':
        won = True

elif matrix[0][2] == matrix[2][0] != '-' and matrix[1][1] == '-':
    play = [1, 1]
    played = True
    if matrix[0][2] == 'x':
        won = True

elif matrix[1][1] == matrix[2][0] != '-' and matrix[0][2] == '-':
    play = [0, 2]
    played = True
    if matrix[1][1] == 'x':
        won = True

else:
    index = 0

    while index < 3 and not won:  #stops the loop if x has won
        if matrix[index][0] == matrix[index][1] != '-' and matrix[index][2] == '-':
            play = [index, 2]
            played = True
            if matrix[index][0] == 'x':
                won = True

        elif matrix[index][0] == matrix[index][2] != '-' and matrix[index][1] == '-':
            play = [index, 1]
            played = True
            if matrix[index][0] == 'x':
                won = True

        elif matrix[index][1] == matrix[index][2] != '-' and matrix[index][0] == '-':
            play = [index, 0]
            played = True
            if matrix[index][1] == 'x':
                won = True

        elif matrix[0][index] == matrix[1][index] != '-' and matrix[2][index] == '-':
            play = [2, index]
            played = True
            if matrix[0][index] == 'x':
                won = True

        elif matrix[0][index] == matrix[2][index] != '-' and matrix[1][index] == '-':
            play = [1, index]
            played = True
            if matrix[0][index] == 'x':
                won = True

        elif matrix[1][index] == matrix[2][index] != '-' and matrix[0][index] == '-':
            play = [0, index]
            played = True
            if matrix[1][index] == 'x':
                won = True

        index += 1

    index = 0

    while index < 3 and not played:
        if matrix[index][0] == matrix[index][1] == '-' and matrix[index][2] == 'x':
            play = [index, 0]
            played = True

        elif matrix[index][0] == matrix[index][2] == '-' and matrix[index][1] == 'x':
            play = [index, 0]
            played = True

        elif matrix[index][1] == matrix[index][2] == '-' and matrix[index][0] == 'x':
            play = [index, 1]
            played = True

        elif matrix[0][index] == matrix[1][index] == '-' and matrix[2][index] == 'x':
            play = [0, index]
            played = True

        elif matrix[0][index] == matrix[2][index] == '-' and matrix[1][index] == 'x':
            play = [0, index]
            played = True

        elif matrix[1][index] == matrix[2][index] == '-' and matrix[0][index] == 'x':
            play = [1, index]
            played = True

        index += 1

    if not played:
        cantWin = True  #if it could not win until now, maybe it can't after all
        index = 0

        while index < 3 and cantWin:  #if x can win, computer will set a strategy to do so and stick with it
            for j in range(3):
                if matrix[index][j] == '-':
                    play = [index, j]
                    played = True

                if (matrix[index][j - 1] == matrix[index][j - 2] == '-'
                    or matrix[index - 1][j] == matrix[index - 2][j]):
                    cantWin = False

            index += 1

        if cantWin:
            if matrix[0][0] == matrix[1][1] == matrix[2][2] == '-':
                play = [0, 0]
                cantWin = False


            elif matrix[0][2] == matrix[1][1] == matrix[2][0] == '-':
                play = [2, 0]
                cantWin = False

if played:
    print('x should play at row {} column {}.'.format(play[0] +1, play[1] + 1))

else:
    print('there is no place left to play.')

if won:
    print('x has won!')

if cantWin:
    print("x can't win.")