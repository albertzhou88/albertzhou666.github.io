import datetime
from imp import init_builtin

# Print the current time
def print_time(task_name):
    print(f'{task_name} completed')
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
print_time('name')

for x in range(0, 10):
    print(x)
print_time('loop')

# This function will return the first initial of a name
def get_initial(name, force_uppercase):
    initial = name[0:1]
    if force_uppercase:
        initial = initial.upper()
    return initial

# Ask for someones name and return the initials
first_name = 'albert'
first_name_initial = get_initial(first_name, True)

middle_name = 'panda'
middle_name_initial = get_initial(middle_name, False)

# When you use names parameters, you can specify parameters in any order
last_name = 'zhou'
last_name_initial = get_initial(force_uppercase=True, name=last_name)

print(f'Your initials are {first_name_initial}{middle_name_initial}{last_name_initial}')

# Using the named nottion when calling functions makes your code more readable
def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print(f'{error_code}|{error_severity}|{log_to_db}|{error_message}|{source_module}')

error_logger(error_code=45, error_severity=1, log_to_db=True, \
    error_message='Second is greater than first', \
    source_module='math')