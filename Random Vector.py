import random

vector = [0] * 5

N = int(input('Input N: '))

for index in range(0, 5):
    vector[index] = random.randint(0, N)

text = 'Original vector: {}\n'.format(vector)

for index in range(0, 2):
    a = vector[index]
    mirror = -index - 1  #to invert you only need to swap content in each index for the content in it's mirror index
    vector[index] = vector[mirror]
    vector[mirror] = a

text += 'Inverted Vector: {}'.format(vector)

print(text)