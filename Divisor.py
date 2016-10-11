opt = ''
while opt == '':
    number = eval(input('Input a number: '))
    div = 2
    divisors = 'These are the divisors of '+ str(number)  + ': 1'
    check = 'n'  #check to see if it has been divided succesfully yet
    square_root = number ** (1/2)
    aux = ''
    ##the most efficient way to know the divisors is to test until the square root. the other divisors are
    #the number divided by the preceding divisors:
    while square_root > div:
        if number % div == 0:
            divisors += ', ' + str(div)
            aux = ', ' + str(number // div) + aux
            check = 'y'
        div += 1
    if div == square_root:
        check = 'y'
        divisors += ', ' + str(div)
    divisors +=  aux + ', ' + str(number) + '.'
    if check == 'n':
        divisors = 'This is a prime number.'
    print(divisors)
    opt = input('Press enter to go again or enter something else to quit.\n')
