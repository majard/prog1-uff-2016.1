list = [0] * 10
iterations = 0

for i in range(10):
    list[i] = eval(input('Insert number {} of the list: '.format(i + 1)))

for i in range(10):
    smallest = i
    for j in range(i + 1, 10):
        #each if is one comparison
        iterations += 1
        if list[smallest] > list[j]:
            smallest = j
    number = list[i]  #store the value of i
    #swaps the leftmost with the smallest:
    list[i] = list[smallest]
    list[smallest] = number

print(list, 'Number of comparisons: ', iterations)