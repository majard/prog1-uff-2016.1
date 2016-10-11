import random


vector = []
length = int(input('Input the length '
	                   'of the vector: '))
	                   
for index in range(length):
  vector.append(eval(input('input number:')))

average = 0

for value in vector:
  average += value

average /= len(vector)
smallestDifference = abs(average - vector[0])
closest = vector[0]

for value in vector:
  difference = abs(average - value)
  if difference < smallestDifference:
    smallestDifference = difference
    closest = value

  elif difference == smallestDifference:
    if value < closest:
      closest = value

print('Vector: {}, average: {}, closest to average: {}'.format(vector, average, closest))
