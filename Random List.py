import random

vector = [0] * 50
sum = 0
nines = 0
highest = 0
positions = []

for index in range(0, 50):
    value = random.randint(0, 20)
    vector[index] = value
    sum += value
    if value > highest:
        highest = value
        positions = [index]
    elif value == highest:
        positions.append(index)
    if value == 9:
        nines += 1

print('Vector = {},\n Sum = {}, Nines = {}, Highest = {}, Positions = {} '.format(vector, sum, nines,highest, positions))
