__author__ = '116031030'

def count_words(string):
    found_word = False
    words = 0

    for char in string:
        if char == ' ' and found_word:
            found_word = False

        elif char != ' ' and not found_word:
            found_word = True
            words += 1

    return words

string = input('Input the string to count the words: ')

print(count_words(string))