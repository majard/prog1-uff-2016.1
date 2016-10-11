def name_stair(string):
    string = string.upper()
    step = ''
    for char in string:
        step += char
        print(step)

string = input('Input a string: ')
name_stair(string)