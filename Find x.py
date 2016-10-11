list = [0] * 5
i = 0
pos = -1  #initialize the variable position with value -1. if the number is not in the list, pos will not be changed
for i in range(5):
    list[i] = eval(input('Input the value of position {}: '.format(i + 1)))
x = eval(input('Input the number "x" you want to find on the list: '))
i = 0
while x != list[i] and i < 4:
    i += 1
if x == list[i]:
    pos = i + 1
print('x was in the position {} of the list'.format(pos))
