from datetime import date
todays_date= date.today()
print('todays_date',todays_date)
print('current year',todays_date.year)
print('current month',todays_date.month)
print('current day',todays_date.day)

#To print the calender
from calendar import*
year=int(input('Enter the year = '))
print(calendar(year))

#Caluclate the number of days between two date
from datetime import date
f_date=date(2014,7,2)
l_date=date(2014,7,11)
date_diff=l_date-f_date
print('Difference between first of last date',date_diff.days)



