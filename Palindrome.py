number = eval(input('Insert 5 digit integer to test if it\'s a palindrome: '))
if 100000 > number > 9999:  # check to see if it's a 5 digit number
    if number == int(number):  # check to see if it's an integer
        d1 = number // 10000  # returns the integer part of number divided by 10000
        # takes the remainder of number divided by 10000 and then
        # the integer part of dividing by a thousand to get digit 2:
        d2 = (number % 10000) // 1000
        # divides number by 100 and takes the integer part of dividing the remainder by 10 to get digit 4:
        d4 = (number % 100) // 10
        # the least significant number is purely the remainder of division by 10:
        d5 = number % 10
        if d1 == d5 and d2 == d4:  # digit 3 is not important to check if it's a palindrome
            print('This integer is a palindrome!')
        else:
            print('This integer is not a palindrome!')
    else:
        print("This is not an integer!")
else:
    print('This is not a 5 digit number!')