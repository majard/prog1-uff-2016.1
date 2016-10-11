n = eval(input('How many numbers will you input? '))
sum = 0
for i in range (n):
    number = eval(input('Input a number: '))
    sum += number ** 2
print('The sum of the squares is ', sum)