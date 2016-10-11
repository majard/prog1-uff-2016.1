__author__ = '116031030'

def factorial(number):
    result = number
    while number > 1:
        number -= 1
        result *= number
    return result

N = int(input('How many students are there? '))
M = int(input('How many students in a group? '))

combinations = factorial(N)/(factorial(M)*factorial(N-M))

print(combinations)