# Arrays
# Simple types such as numbers
# Must all be the same type
print('----- array -----')
scores = []
scores.append(98)
scores.append(99)
print(scores)
print(scores[0])    # Collections are zero-indexed

# Lists
# Store anything
# Store any type
# Zero-based index
# Storage order guaranteed
print('----- list -----')

names = ['Susan', 'Chris', 'Tom', 'Jerry']
print(names)
print(len(names))

names.insert(1, 'Bill')
print(names)
print(len(names))

names.sort()
print(names)
print(len(names))

presenters = names[0:2]
print(presenters)

presenters = names[1:2]
print(presenters)

# Dictionaries
# Key:Value pairs
# Storage order not guaranteed
print('----- dictionary -----')

chris = {}
chris['first'] = 'Christopher'
chris['last'] = 'Harrison'

susan = {'first':'Susan', 'last':'Ibach'}

people = [chris, susan]
people.append({'first':'Bill', 'last':'Gates'})
print(people)

presenters = people[0:2]
print(presenters)
