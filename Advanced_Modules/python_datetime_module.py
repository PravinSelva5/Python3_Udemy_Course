import datetime 

mytime = datetime.time(2,20)
print(mytime.minute, mytime.hour, mytime.microsecond)

#to be more precious
print("A more precious way of showing time:")
mytime2 = datetime.time(13,20,1,20)
print(mytime2.minute, mytime2.hour, mytime2.microsecond)
print("\n")

# To print the date
today = datetime.date.today()
print(today)

print(today.ctime())


from datetime import datetime

mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)


from datetime import date

date1 = date(2021,11,3)
date2 = date(2020,11,3)

print(date1 - date2)