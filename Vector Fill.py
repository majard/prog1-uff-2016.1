vector = []
greaterThanFive = 0
evenNumSum = 0
oddNumSum = 0
number = int(input('Input a number: '))

while number > -1:
    vector.append(number)
    if number > 5:
        greaterThanFive += 1
    if number % 2 == 0:
        evenNumSum += number
    else:
        oddNumSum += number
    number = int(input('Input a number: '))

print('Vector: {} \nNumber of values greater than five: {} \nEven number sum: {} \nOdd number sum: {}\n'
      'Total number of values stored in the vector: {}'.format(vector, greaterThanFive, evenNumSum,
                                                               oddNumSum, len(vector)))
