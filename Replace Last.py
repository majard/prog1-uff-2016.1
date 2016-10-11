__author__ = '116031030'

def replace_last(string, old, new):
    index = 0
    char_index = -1

    while char_index >= -len(string) and index > -len(old):
        if string[char_index] == old[-1] and index == 0:
            index = -1

            while index != 0 and index > -len(old):
                if string[char_index] == old[index] and index != 0:
                    index -= 1
                    char_index -= 1

                else:
                    index = 0

        char_index -= 1

    if index == 0:
        print('There was no occurrence of {} in the provided string'.format(old))
        return -1

    else:
        char_index += 1
        #the new string will be exactly the same until the point where the word begins, then the same again after the
        #replaced word, with the new word separating them
        new_string = new.join((string[ : len(string) + char_index], string[len(string) + char_index + len(old) : ]))
        return  new_string

string = input('Input a string: ')
old = input('Input the word you want to replace: \n')
new = input('Input the word you want to replace {} with: \n'.format(old))

print(replace_last(string, old, new))