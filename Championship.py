def add_match():
    temp = []
    fouls = []
    temp.append(input('Input first team: '))
    temp.append(input('Input second team: '))
    fouls.append(int(input('How many fouls did {} commit? '.format(temp[0]))))
    fouls.append(int(input('How many fouls did {} commit? '.format(temp[1]))))
    temp.append(fouls)
    return temp

def calculate_fouls(games):
    total_fouls = 0
    for index in range(len(games)):
        for fouls in range(2):
            total_fouls += games[index][2][fouls]

    print('There were {} total fouls in the championship until now.'.format(total_fouls))

    return 0

def fouls_table(games):
    table = []
    temp = [games[0][0], games[0][2][0]]
    table.append(temp)
    temp = [games[0][1], games[0][2][1]]
    table.append(temp)

    for match in range(1, len(games)):
        index = 0
        found_first_team = False
        found_second_team = False

        while index < len(table) and not (found_first_team and found_second_team):
            if table[index][0] == games[match][0]:
                table[index][1] += games[match][2][0]
                found_first_team = True

            elif table[index][0] == games[match][1]:
                table[index][1] += games[match][2][1]
                found_second_team = True

            index += 1

        if not found_first_team:
            temp = [games[match][0], games[match][2][0]]
            table.append(temp)

        if not found_second_team:
            temp = [games[match][1], games[match][2][1]]
            table.append(temp)


    return table

def det_most_fouls(games):
    table = fouls_table(games)
    most_fouls_team = [table[0][0]]
    most_fouls = table[0][1]

    for index in range(1, len(table)):
        if most_fouls < table[index][1]:
            most_fouls_team = [table[index][0]]
            most_fouls = table[index][1]

        elif most_fouls == table[index][1]:
            most_fouls_team.append(table[index][0])

    print('The team with the most fouls was {} with {} fouls.'.format(most_fouls_team[0], most_fouls))

    for index in range(1, len(most_fouls_team)):
        print('Tied with {} with the same amount'.format(most_fouls_team[index]))

    return 0

def det_least_fouls(games):
    table = fouls_table(games)
    least_fouls_team = [table[0][0]]
    least_fouls = table[0][1]

    for index in range(1, len(table)):
        if least_fouls > table[index][1]:
            least_fouls_team = [table[index][0]]
            least_fouls = table[index][1]

        elif least_fouls == table[index][1]:
            least_fouls_team.append(table[index][0])

    print('The team with the least fouls was {} with {} fouls.'.format(least_fouls_team[0], least_fouls))

    for index in range(1, len(least_fouls_team)):
        print('Tied with {} with the same amount.'.format(least_fouls_team[index]))

    return 0

def menu():
    print('Choose an option: ')
    print('1 - Show championship table')
    print('2 - Add a match')
    print('3 - Calculate fouls')
    print('4 - Most fouls')
    print('5 - Least fouls')
    print('6 - Exit')
    return int(input())

opt = 0
championship_table = []

while opt != 6:
    if opt == 1:
        print(championship_table)
    elif opt == 2:
        championship_table.append(add_match())
    elif opt == 3:
        calculate_fouls(championship_table)
    elif opt == 4:
        det_most_fouls(championship_table)
    elif opt == 5:
        det_least_fouls(championship_table)
    opt = menu()
