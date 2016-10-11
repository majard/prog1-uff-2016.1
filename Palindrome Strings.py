def check_palindrome(str1, str2):
    are_palindrome = False  #assume they are not palindrome (probably true)
    if len(str1) == len(str2):
        index = 0
        are_palindrome = True  #assume they are palindromes until proven otherwise
        while index < len(str1) and are_palindrome:
            if str1[index] != str2[-index - 1]:
                are_palindrome = False
            index += 1
    return are_palindrome

str1 = input('Input first string: ')
str2 = input('Input second string: ')

if check_palindrome(str1, str2):
    print('Those strings are mutual palindromes!')

else:
    print('Those strings are not palindromes.')
