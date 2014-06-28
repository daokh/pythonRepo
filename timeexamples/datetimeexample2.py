__author__ = 'daokh'
import datetime
import time
import pytz
from time import gmtime
import calendar


#dt = datetime.datetime.strptime('24052010', "%d%m%Y").date()
dt = datetime.datetime.strptime('01011970 00:00:00 UTC', "%d%m%Y %H:%M:%S %Z")
#dt = dt.astimezone(pytz.UTC)
# tz = pytz.timezone('America/Los_Angeles')
# utc_dt = tz.localize(dt, is_dst=True).astimezone(pytz.utc)
tuple = dt.timetuple()
ans_time = time.mktime(tuple)
ans_time = calendar.timegm(tuple)
print

