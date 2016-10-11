def write_date(date):
    date = date.split('/')

    if len(date) != 3:
        print('Input a valid date in the format dd/mm/yyyy.')
        return -1

    else:
        if date[1] == '01':
            date[1] = 'january'

        elif date[1] == '02':
            date[1] = 'february'

        elif date[1] == '03':
            date[1] = 'march'

        elif date[1] == '04':
            date[1] = 'april'

        elif date[1] == '05':
            date[1] = 'may'

        elif date[1] == '06':
            date[1] = 'june'

        elif date[1] == '07':
            date[1] = 'july'

        elif date[1] == '08':
            date[1] = 'august'

        elif date[1] == '09':
            date[1] = 'september'

        elif date[1] == '10':
            date[1] = 'october'

        elif date[1] == '11':
            date[1] = 'november'

        elif date[1] == '12':
            date[1] = 'december'

        print('You were born on {} {} of the year {}'.format(date[1], date[0], date[2]))

    return 0

while True:
    string = input('Input the date you were born in the format dd/mm/yyyy: ')

    write_date(string)