gpa = input('Input GPA ')
gpa = float(gpa)
lowest_grade = input('Lowest grade is ')
lowest_grade = float(lowest_grade)

if lowest_grade >= 0.70 and gpa >= 0.85:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('You make honour roll')

    