# To get current date and time
# we need to use the datetime library
from datetime import datetime, timedelta

# the now function returns a datetime object
today = datetime.now()
output = f'Today is {today}'
print(output)

# timedelta is used to defin a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
output = f'Yesterday was {yesterday}'
print(output)

year = today.year
month = today.month
day = today.date
hour = today.hour
minute = today.minute
second = today.second

output = f'Year {year} \nMonth {month} \nDay {day}'
print(output)
output = f'Hour {hour} \nMinute {minute} \nSecond {second}'
print(output)