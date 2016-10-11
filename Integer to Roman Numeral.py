integer = int(input('Input a positive integer: '))
if integer > 0:
    roman = ''
    roman += (integer // 1000) * ('M')
    integer = integer % 1000
    if integer // 100 == 9:
        roman += 'CM'
    else:
        roman += (integer // 500) * 'D'
        integer = integer % 500
        if integer // 100 == 4:
            roman += 'CD'
        else:
            roman += (integer // 100) * 'C'
    integer %= 100
    if integer // 10 == 9:
        roman += 'XC'
    else:
        if integer // 10 == 4:
            roman += 'XL'
        else:
            roman += integer // 50 * 'L'
            integer %= 50
            roman += integer // 10 * 'X'
    integer %= 10
    if integer == 9:
        roman += 'IX'
    else:
        if integer == 4:
            roman += 'IV'
        else:
            roman += integer // 5 * 'V'
            integer %= 5
            roman += integer * 'I'
    print('In roman numerals: ', roman)
else:
    print('Input a positive integer!')