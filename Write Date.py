def write_date(date):

    months = [[], ["January", 31], ["February", 28], ["March", 31], ["April", 30], ["May", 31], ["June", 30],
              ["July", 31], ["August", 31], ["September", 30], ["October", 31], ["November", 30], ["December", 31]]

    date = date.split('/')

    for index in range(len(date)):
         date[index] = int(date[index])

    if len(date) != 3 or date[1] < 1 or date[1] > 12 or date[0] < 1 or date[0] > months[date[1]][1]:
        print('Input a valid date in the format dd/mm/yyyy.')
        return -1

    else:
        print('You were born on {} {} of the year {}'.format(date[0], months[date[1]][0], date[2]))

    return 0

while True:
    string = input('Input the date you were born in the format dd/mm/yyyy: ')

    write_date(string)