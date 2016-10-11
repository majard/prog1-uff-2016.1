def replace_space(string):
    new_string = ''
    for char in string:
        if char == ' ':
            new_string += '#'
        else:
            new_string += char
    return new_string

def input_data():
    string = input('Input a string: ')
    return string

print(replace_space(input_data()))