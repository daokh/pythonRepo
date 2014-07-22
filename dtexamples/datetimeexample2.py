__author__ = 'daokh'
"""
time.strptime
string --> tuple (no timezone applied, so matches string)

time.mktime
local time tuple --> seconds since epoch (always local time)

time.localtime
seconds since epoch --> tuple in local timezone

calendar.timegm
tuple in UTC --> seconds since epoch

time.gmtime
seconds since epoch --> tuple in UTC

"""
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

localNow = datetime.datetime.now()
utcNow = datetime.datetime.utcnow()

localTuple = localNow.timetuple()
utcTuple = utcNow.timetuple()

localUnixTime = time.mktime(localTuple)
utcUnixTime = calendar.timegm(utcTuple)

localString = localNow.strftime('%Y-%m-%d %H:%M:%S %Z')
utcString = utcNow.strftime('%Y-%m-%d %H:%M:%S %Z')
print

