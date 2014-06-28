__author__ = 'daokh'
import datetime
import time
import pytz
from time import gmtime
import calendar


#dt = datetime.datetime.strptime('24052010', "%d%m%Y").date()
dt = datetime.datetime.strptime('01011970 00:00:00 UTC', "%d%m%Y %H:%M:%S %Z")
tuple = dt.timetuple()
ans_time = time.mktime(tuple)
ans_time = calendar.timegm(tuple)

dt = datetime.datetime.strptime('Jan 01, 1970 12:00:00 AM UTC', "%b %d, %Y %I:%M:%S %p %Z")
tuple = dt.timetuple()
ans_time = time.mktime(tuple)
ans_time = calendar.timegm(tuple)



print

