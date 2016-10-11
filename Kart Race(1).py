def main():
    table = {}

    for racer in range(6):
        temp = []
        name = input('Input name of the racer {}: '.format(racer + 1))

        for lap in range(10):
            temp.append(eval(input('Time of the {} lap in seconds: '.format(lap + 1))))
        table[name] = temp

    best_lap = {}
    best_lap['name'] = [name]
    best_lap['time'] = table[name][0]
    best_lap['lap'] = [1]
    ranking = []

    for name in table:
        for lap in range(10):
            if best_lap['time'] > table[name][lap]:
                best_lap['name'] = [name]
                best_lap['time'] = table[name][lap]
                best_lap['lap'] = [lap + 1]

            elif best_lap['time'] == table[name][lap] and not (name == best_lap['name'][0] and lap == 0):
                best_lap['name'].append(name)
                best_lap['lap'].append(lap + 1)

        average = sum(table[name]) / len(table[name])
        index = 0

        while index < len(ranking) and average > ranking[index]['time']:
            index += 1

        temp = {'name': name, 'time': average}
        ranking.insert(index, temp)

    print('The best lap was by {} at lap {} in {} seconds'.format(best_lap['name'], best_lap['lap'], best_lap['time']))
    print('Ranking: ')

    for index in range(len(ranking)):
        if ranking[index]['time'] == ranking[index - 1]['time']:
            classification = index
        else:
            classification = index + 1

        print('{}: {}'.format(classification, ranking[index]))

main()