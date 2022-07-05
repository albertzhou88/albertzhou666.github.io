# first_name = input('What is your first name? ')
# last_name = input('What is your last name? ')

first_name = 'albert'
last_name = 'zhou'

print('1> Hello ' + first_name + ' ' + last_name)
print('2> Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

output = '3> Hello, ' + first_name + ' ' + last_name
print(output)
output = '4> Hello, {} {}'.format(first_name, last_name)
print(output)
output = '5> Hello, {1}, {0}'.format(first_name, last_name)
print(output)

# Only available in python3
output = f'6> Hello, {first_name} {last_name}'
print(output)