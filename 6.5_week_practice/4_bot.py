import datetime

now = datetime.datetime.now()

time = now.strftime('%H:%M')
year = now.strftime('%d/%m/%y')
print(time)
print(year)