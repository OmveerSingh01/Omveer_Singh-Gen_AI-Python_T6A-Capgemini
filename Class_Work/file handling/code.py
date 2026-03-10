import csv
from datetime import date
file = open('expense.csv','a+')
w = csv.writer(file)

w.writerow(['DATE','CATEGORY','AMOUNT'])
w.writerows([ 
    [date.today(),'Travel',2000],
    [date.today(),'Food',550],
    [date.today(),'Entertainment',1700],
])
file.close()