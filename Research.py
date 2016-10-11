opt = 'y'
fla = 0
vas = 0
flu = 0
bot = 0
other = 0
salfla = 0
salvas = 0
salflu = 0
salbot = 0
salother= 0
different = 0
interviewed = 0
while opt == 'y':
    team = eval(input('What is your favorite team (1 - Flamengo, 2 - Vasco, 3 - Fluminense, 4 - Botafogo, 5 - Other)'))
    salary = eval(input('What is your salary? '))
    hometown = eval(input('What is your hometown(1 - Niteroi 2 - Other) ? '))
    if team == 1:
        fla += 1
        salfla += salary
    elif team == 2:
        vas += 1
        salvas += salary
    elif team == 3:
        flu += 1
        salflu += salary
    elif team == 4:
        bot += 1
        salbot += salary
    elif team == 5:
        if hometown == 1:
            different += 1
        other += 1
        salother += salary
    interviewed += 1
    opt = input('Do you want to interview another person (y / n)?')
if fla != 0:
    salfla /= fla
if vas != 0:
    salvas /= vas
if flu !=0:
    salflu /= flu
if bot != 0:
    salbot /= bot
if other !=0:
    salother /= other

print('Fans of each team and their medium salary:\nFlamengo: {}, salary: {}  \nVasco: {}, salary: {} \n'
      'Fluminense: {}, salary: {} \nBotafogo: {}, salary: {} \nOther: {}, salary: {}'.format(fla, salfla, vas, salvas,
                                                                                             flu, salflu, bot, salbot,
                                                                                             other, salother))
print('{} people born in Niteroi are not fans of the major teams in rio'.format(different))
print('{} people were interviewed'.format(interviewed))