number = eval(input('Input a number to calculate it\'s fibonacci sequence: '))
if number == 0:
    result = 0
    fibonacci = '0'
elif number == 1:
    result = 1
    fibonacci = '0, 1'
else:
    fminus1 = 1  #f(n-1)
    fminus2 = 0  #f(n-2)
    fibonacci = '0, 1,'
    for n in range(2, number+1):
        result = fminus1 + fminus2  #f(n) receives f(n-1) + f(n-2)
        fminus2 = fminus1  #f(n-2) receives f(n-1)
        fminus1 = result  #f(n-1) receives f(n)
        fibonacci += ' ' + str(result) + ','  #manipulation of strings to make it easier to print the result
print(fibonacci)