# importing datetime class
import datetime
import random




date1 = input("enter a date in a format YYYY-MM-DD \n")
date2 = input("enter a date in a format YYYY-MM-DD \n")
x1 = date1.split("-")
print(x1)

x2 = date2.split("-")
print(x2)

dat1 = datetime.date(int(x1[0]), int(x1[1]), int(x1[2]))
print(dat1)
print(dat1.strftime('%A'))

dat2 = datetime.date(int(x2[0]), int(x2[1]), int(x2[2]))
print(dat2)
print(dat2.strftime('%A'))

time_delta = dat2-dat1
print(time_delta.days)
r = random.randint(0, time_delta.days)
print("the random number: ", r)
newDate = dat1+datetime.timedelta(days=r)
print(newDate)
print(newDate.strftime('%A'))
if newDate.strftime('%A') == 'Monday':
    print("I don't have a vinaigrette")