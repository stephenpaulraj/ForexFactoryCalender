from datetime import datetime, timedelta
import calendar

initialDate = datetime(2007,1,1)
year = int(initialDate.strftime('%Y'))
month = int(initialDate.strftime('%m'))
date = int(initialDate.strftime('%d'))
month_abbrivation=calendar.month_abbr[month]
outputText = str(month_abbrivation)+str(date)+'.'+str(year)

while year < 2021:
    print(year)
    year +=1

