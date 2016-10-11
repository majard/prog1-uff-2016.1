import random

vector = [0] * 10
value = 0

for index in range(0, 10):
    value = random.randint(0, 20)
    vector[index] = value

print(vector)

ant_value = vector[-1]

for index in range(0, 10):
    current_value = vector[index]
    vector[index] = ant_value
    ant_value = current_value

print(vector)