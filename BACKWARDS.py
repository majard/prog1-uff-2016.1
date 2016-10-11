def upper_backwards(string):
    string = string.upper()
    new_string = ''
    last_char = -len(string) - 1

    for char in range(-1, last_char, -1):
        new_string += string[char]

    return new_string

string = input('Input a string: ')

print('This string backwards is "{}"'.format(upper_backwards(string)))