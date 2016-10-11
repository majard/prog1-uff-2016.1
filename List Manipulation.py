vet = [0] * 20
pos = []
semdup = []
for i in range(20):
    vet[i] = eval(input('Input value {} of the list: '.format(i + 1)))
    if vet[i] == int(vet[i]) and vet[i] > 0:
        pos.append(vet[i])
#iterates the list up to the second to last item for unique numbers:
for i in range(len(pos) - 1):
    j = i + 1
    #stops the code if it finds equal numbers, else continue to the end of the list:
    while pos[i] != pos[j] and j < len(pos) - 1:
        j += 1
    if pos[i] != pos[j]:
        semdup.append(pos[i])
#adds the last item on pos to semdup because it won't have been added yet if it's repeated:
semdup.append(pos[j])
print('vet: {}, pos: {}, semdup: {}'.format(vet, pos, semdup))