list = [0] * 10
size = len(list)
different = 1  #the user will input at least one value
for i in range(size):
    list[i] = eval(input('Input value {}: '.format((i + 1))))
for i in range(size - 1):
    j = i + 1
    #iterates from i + 1 to size - 1 of the list to check it there are equal numbers
    while j < (size - 1) and list[i] != list[j]:
        j += 1
    #the last time the while loops, it will add 1 to j, reaching the last item in the list
    if list[i] != list[j]:  #check if it has reached the end of the iteration without finding the same number
        different += 1
print('There are {} different values on the list'.format(different))