n = eval(input('Print the first "n" perfect numbers. Input "n": '))
counter = 0
number = 6
while counter < n:
    div = 2
    sum = 1
    square_root = number ** (1/2)
    ##the most efficient way to know the divisors is to test until the square root. the other divisors are
    #the number divided by the preceding divisors:
    while square_root > div:
        if number % div == 0:
            sum += div + (number // div)
        div += 1
    if sum == number:
        print(number)
        counter += 1
    number += 1