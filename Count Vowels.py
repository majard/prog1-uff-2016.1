def count_vowels(string):
    vowels = dict(a=0, e=0, i=0, o=0, u=0)
    string = string.lower()

    for vowel in list(vowels):
        for char in string:
            if char == vowel:
                vowels[vowel] += 1

        if vowels[vowel] == 0:
            vowels.pop(vowel)


    return vowels

text = input('Input text to count their vowels: ')
print(sorted(count_vowels(text).items()))