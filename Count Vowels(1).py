def count_vowels(string):
    vowels = dict(a = 0, e = 0, i = 0, o = 0, u = 0)
    for vowel in vowels:
        for char in string:
            if char == vowel:
                vowels[vowel] += 1

    return vowels

string = input('Input text to count their vowels: ')
print(count_vowels(string))