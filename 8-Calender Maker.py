from datetime import *
import datetime

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
Days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

year = int(input('Enter the year: '))
month = int(input('Enter numeric month: '))

days = []
currentDate = datetime.date(year, month, 1)
while currentDate.weekday() != 6:
    currentDate -= datetime.timedelta(days=1)
days.append(str(currentDate.day).zfill(2))
for i in range(1, 42):
    days.append(str((currentDate + timedelta(days=i)).day).zfill(2))

cal = f'''
                      ...{Months[month - 1]} {year}...
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
|   {days[0]}     |    {days[1]}    |   {days[2]}      |   {days[3]}    |   {days[4]}     |  {days[5]}      |   {days[6]}     |
|          |          |           |         |          |          |          |
|          |          |           |         |          |          |          |
|          |          |           |         |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|    {days[7]}    |    {days[8]}    |    {days[9]}    |    {days[10]}    |    {days[11]}    |    {days[12]}    |    {days[13]}    |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|     {days[14]}   |   {days[15]}     |   {days[16]}     |   {days[17]}     |   {days[18]}     |   {days[19]}     |   {days[20]}     |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|    {days[21]}    |   {days[22]}     |   {days[23]}     |   {days[24]}     |   {days[25]}     |   {days[26]}     |   {days[27]}     |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|    {days[28]}    |   {days[29]}     |   {days[30]}     |   {days[31]}     |   {days[32]}     |   {days[33]}     |   {days[34]}     |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|    {days[35]}    |   {days[36]}     |   {days[37]}     |   {days[38]}     |   {days[39]}     |    {days[40]}    |    {days[41]}    |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+

'''
print(cal)
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
 fileObj.write(cal)
print('Saved to ' + calendarFilename)