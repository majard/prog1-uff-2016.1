
import random

dice = []
for index in range(10): 
  dice.append(random.randint(1, 6))
    
numbers = []
for i in range(6):
  numbers.append(0)

for value in dice:
  numbers[value - 1] += 1

print('Dice outcomes: {}'.format(dice))
print('Times each number was rolled: {}'.format(numbers))
