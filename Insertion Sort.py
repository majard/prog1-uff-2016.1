list = [0] * 10
iterations = 0

for i in range(10):
    list[i] = eval(input('Insert number {} of the list: '.format(i + 1)))

for i in range(10):
    pos = i
    currentvalue = list[i]
    iterations += 1  #it makes a comparison to decide if it will enter the while loop
    while pos > 0 and list[pos - 1] > currentvalue:
        list[pos] = list[pos - 1]
        pos -= 1
        iterations += 1  #each iteration makes a comparison
    list[pos] = currentvalue
print(list, 'Number of comparisons: ', iterations)