
import datetime
from datetime import date
import time
six_days = []

year = date.today().year
def weeknum_to_dates(weeknum):
    return [datetime.datetime.strptime(str(year) + "-W"+ str(weeknum) + str(x), "%Y-W%W-%w").strftime('%d.%m.%Y') for x in range(-6,0)]



six_days = weeknum_to_dates(2)
print(six_days)