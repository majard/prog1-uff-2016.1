__author__ = '116031030'

def factorial(number):
    result = number
    while number > 0:
        result *= number
        number -= 1
    return result

N = int(input('How many students are there? '))
M = int(input('How many students in a group? '))

combinations = factorial(N)/(factorial(M)*factorial(N-M))

print(combinations)