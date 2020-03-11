from datetime import datetime,timedelta
import calendar

initialDate = datetime.strptime('01-01-2007','%d-%m-%Y').date()
year = int(initialDate.strftime('%Y'))


while year < 2021:
    initialDate = initialDate + timedelta(days=7)
    month = calendar.month_abbr[int(initialDate.strftime('%m'))]
    day = int(initialDate.strftime('%d'))
    output = 'https://www.forexfactory.com/calendar.php?week='+str(month)+str(day)+'.'+str(initialDate.strftime('%Y'))
    year = int(initialDate.strftime('%Y'))
    print(output)

