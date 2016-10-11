record = []

for racer in range(1, 7):
    line = []
    line.append(input('Input racer {} name: '.format(racer)))
    for lap in range(1, 11):
        time = eval(input('Lap {} in seconds: '.format(lap)))
        line.append(time)
    record.append(line)

bestLapRacer = [record[0][0]]
bestLapTime = record[0][1]
bestLap = []

classification = []

averageLap = [0] * 10

for i in range(6):
    sum = 0  #total seconds spent racing


    for j in range(1, 11):
        if record[i][j] < bestLapTime:
            bestLapTime = record[i][j]
            bestLap = [j]
            bestLapRacer = [record[i][0]]

        elif record[i][j] == bestLapTime:
            bestLap.append(j)
            bestLapRacer.append(record[i][0])

        sum += record[i][j]
        averageLap[j - 1] += record[i][j]

        if i == 5:
            averageLap[j - 1] /= 6  #if it is the last iteration of the i loop, calculates the average for that lap
            if j == 1: #if it is the first iteration of the j loop, initialize the variables
                bestAverageLap = j
                bestAverageLapTime = averageLap[j - 1]

            elif averageLap[j - 1] < bestAverageLapTime:
                bestAverageLapTime = averageLap[j - 1]
                bestAverageLap = j

    average = sum / 10
    line = []
    line.append(record[i][0])
    line.append(average)

    j = 0

    while j < i :
        if average < classification[j][1]:
            classification.insert(j, line)
            j = i  #stops the loop
        j += 1

    if j == i:
        classification.append(line)


for i in range(len(bestLap)):
    print('Best Lap was lap {} completed by {} in {} seconds '.format(bestLap[i], bestLapRacer[i], bestLapTime))

print('Classification: ')
for racer in range(6):

    print(classification[racer][0], ' Average Lap: ', classification[racer][1])

print('The best Average Lap Time was {} seconds in Lap {}'.format(bestAverageLapTime, bestAverageLap))
