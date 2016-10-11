day1 = 1
while day1 != 0:
    days = 0
    day1 = eval(input('Day of the first date(input 0 to finish the program): '))
    month1 = eval(input('Month of the first date: '))
    year1 = eval(input('Year of the first date (with 4 digits): '))
    day2 = eval(input('Day of the second date: '))
    month2 = eval(input('Month of the second date: '))
    year2 = eval(input('Year of the second date (with 4 digits): '))
    while year1 < year2:
        if month1 <= month2:
            days += 365
            if year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0):
                days += 1
        year1 += 1
    while month1 != month2:
        if month1 == 1 or month1 ==  3 or month1 ==  5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12:
            days += 31
        elif month1 == 2 and year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0):
            days += 29
        elif month1 == 2:
            days += 28
        else:
            days += 30
        if month1 == 12:
            month1 = 1
        else:
            month1 += 1
    days += day2 - day1
    print('There were {} days between these two dates'.format(days))
