dice = [0] * 50
percentage = 0
for i in range(50):
    dice[i] = eval(input('What side did it land on? '))
    if dice[i] == 6:
        percentage += 2
print('The dice landed on 6 in {}% of the throws'.format(percentage))