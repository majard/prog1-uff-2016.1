number = eval(input('Insert an integer between 0 and 9999: '))
if 0 <= number < 10000:
    if number == int(number):  # check if it's an integer
        d1 = number // 1000  # the most significant number is the integer part of division by 1000
        # takes the integer part of the remainder of dividing number by 1000
        # divided by 100:
        d2 = (number % 1000) // 100
        # takes the remainder of number by 100 and the integer part of dividing that by 10:
        d3 = (number % 100) // 10
        # the least significant one is the remainder of dividing number by 10
        d4 = number % 10

        numberFull = ''  # creates a string variable to make it easier to manipulate
        if d1 == 1:
            numberFull += 'one'
        elif d1 == 2:
            numberFull += 'two'
        elif d1 == 3:
            numberFull += 'three'
        elif d1 == 4:
            numberFull += 'four'
        elif d1 == 5:
            digit1 = 'five'
        elif d1 == 6:
            numberFull += 'six'
        elif d1 == 7:
            numberFull += 'seven'
        elif d1 == 8:
           numberFull += 'eight'
        elif d1 == 9:
            numberFull += 'nine'

        if d1 != 0:
            numberFull += ' thousand '

        if d2 == 1:
            numberFull += 'one'
        elif d2 == 2:
            numberFull += 'two'
        elif d2 == 3:
            numberFull += 'three'
        elif d2 == 4:
            numberFull += 'four'
        elif d2 == 5:
            numberFull = 'five'
        elif d2 == 6:
            numberFull += 'six'
        elif d2 == 7:
            numberFull += 'seven'
        elif d2 == 8:
           numberFull += 'eight'
        elif d2 == 9:
            numberFull += 'nine'

        if d2 != 0:
            numberFull += ' hundred '

        if d3 == 2:
            numberFull += 'twenty-'
        elif d3 == 3:
            numberFull += 'thirty-'
        elif d3 == 4:
            numberFull += 'forty-'
        elif d3 == 5:
            numberFull = 'fifty-'
        elif d3 == 6:
            numberFull += 'sixty-'
        elif d3 == 7:
            numberFull += 'seventy-'
        elif d3 == 8:
           numberFull += 'eighty-'
        elif d3 == 9:
            numberFull += 'ninety-'
        if d3 == 1:
            if d4 == 1:
                numberFull += 'eleven'
            elif d4 == 2:
                numberFull += 'twelve'
            elif d4 == 3:
                numberFull += 'thirteen'
            elif d4 == 4:
                numberFull += 'fourteen'
            elif d4 == 5:
                numberFull = 'fifteen'
            elif d4 == 6:
                numberFull += 'sixteen'
            elif d4 == 7:
                numberFull += 'seventeen'
            elif d4 == 8:
               numberFull += 'eighteen'
            elif d4 == 9:
                numberFull += 'nineteen'
        else:
            if d4 == 1:
                numberFull += 'one'
            elif d4 == 2:
                numberFull += 'two'
            elif d4 == 3:
                numberFull += 'three'
            elif d4 == 4:
                numberFull += 'four'
            elif d4 == 5:
                numberFull = 'five'
            elif d4 == 6:
                numberFull += 'six'
            elif d4 == 7:
                numberFull += 'seven'
            elif d4 == 8:
               numberFull += 'eight'
            elif d4 == 9:
                numberFull += 'nine'
            elif d4 == 0:
                numberFull += 'zero'
        print(numberFull)

    else:
        print("This is not an integer!")
elif number < 0 or number > 9999:
    print('This number is not between 0 and 9999!')