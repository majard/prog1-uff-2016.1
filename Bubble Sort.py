list = [0] * 10
iterations = 0

for i in range(10):
    list[i] = eval(input('Insert number {} of the list: '.format(i + 1)))

end = 9
iterations += 1  #comparison before the while
while end != 1:
    iterations += 1  #each while a comparison
    for i in range(end - 1):  #the range is up until the end - 1
        currentvalue = list[i]
        iterations += 1  #each if is one comparison
        if list[i] > list[i + 1]:
            list[i] = list[i + 1]
            list[i + 1] = currentvalue
    end -= 1  #the last one is already the biggest number

print(list, 'Number of comparisons: ', iterations)