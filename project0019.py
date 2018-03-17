#File: project0019.py
#This program determines the number of sundays which fell on the first day of the month
#during the twentieth century

#----pseudocode------#
#loop through months Jan, Feb, March... ,Dec
#...loop through years 1901 - 2000
#......check if the first of the month is a sunday
#...add 365 if not leap year, 366 if is leap year
#add number of days in this current month to move to next month in loop
#--------------------#

days_in_month = [31,28,31,30,31,30,31,31,30,31,30]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_of_week = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

#----code------------#
count=0
month_day_count=366 #month, for iterating through months
for m in months:
    d = 0
    year_day_count = month_day_count #year, for iterating through years
    for year in range(1901,2001):
        if days_of_week[year_day_count%7] == 'sun':
            print(str(m) + '1st, ' + str(year) + ': '+ str(days_of_week[year_day_count%7]))
            count = count+1
        if year%4 == 0 and year%400 != 0:
            days = 366
        else:
            days = 365
        year_day_count = year_day_count + days

    month_day_count = month_day_count + days_in_month[d] #add to move to next month b4 begin next iteration
    d=d+1
print(count)
#--------------------#

