persons = [True] * 30
count, index, number = 0, 0, 0
while count < 15:
    if persons[index] == True:
        number += 1
        if number == 9:
            persons[index] = False
            count += 1
            number = 0
    index += 1
    index %= 30

print(persons)        