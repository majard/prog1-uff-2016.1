def are_anagram(str1, str2):

    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')

    #the length of string1 won't change and we'll need it many times, so we assign a variable to
    #store it's value and then we can only call len(str1) once
    len1 = len(str1)

    if len1 == len(str2):
        anagram = True
        i = 0

        while i < len1 and anagram:

            j = 0

            while j < (len(str2)) and anagram:
                if str1[i] == str2[j]:
                    str2 = str2.replace(str1[i], '', 1)
                    j = len(str2)

                j += 1

            if j == len(str2):
                anagram = False

            i += 1

    else:
        print('false')
        anagram = False

    return anagram

str1 = input('Input first string: ')
str2 = input('Input second string: ')

if are_anagram(str1, str2):
    print('Those strings are anagrams!')

else:
    print('Those strings aren\'t anagrams.')