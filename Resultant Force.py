vector1 = vector2 = resultant = end = [0] * 3
dict = ['x', 'y', 'z']
for i in range(3):
    vector1[i] = eval(input('Input coordinate {} of vector 1: '.format(dict[i])))
    vector2[i] = eval(input('Input coordinate {} of vector 2: '.format(dict[i])))
    resultant[i] = vector1[i] + vector2[i]
    #creates a list to use the .join method (more efficient than adding a substring to a string):
    end[i] = dict[i] + ': ' + str(resultant[i])
text = 'The resultant force is ' + ', '.join(end)
print(text)
