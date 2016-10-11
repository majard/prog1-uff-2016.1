CLASSES = 2
STUDENTS = 3
GRADES = 2

M = []

for clss in range(CLASSES):
    diary = []
    for student in range(STUDENTS):
        report = []
        for grade in range(GRADES):
            report.append(eval(input('What grade did student {} of class {} get in test {}? '
                                    .format(student + 1, clss + 1, grade + 1))))
        gpa = (report[0] + report[1]) / 2
        report.append(gpa)
        diary.append(report)
    M.append(diary)

TURMA = []
bestClass = 0
brightest = []

for clss in range(CLASSES):
    average = 0
    for student in range(STUDENTS):
        average += M[clss][student][2]
    average /= STUDENTS
    for student in range(STUDENTS):
        if M[clss][student][2] > average:
            brightest.append([clss, student])
    TURMA.append(average)
    if average > TURMA[bestClass]:
        bestClass = clss


print('The class with the best average is {} with an average of {}'.format(bestClass + 1, TURMA[bestClass]))
print('The students that had best average than their class were: ')

for student in range(len(brightest)):
    print('Class {}, student {}'.format(brightest[student][0] + 1, brightest[student][1] + 1))

