__author__ = 'daokh'
import datetime
import time
import pytz
from time import gmtime
import calendar
import sys
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


# dt = datetime.datetime.strptime('24052010', "%d%m%Y").date()
dt = datetime.datetime.strptime('01011970 00:00:00 UTC', "%d%m%Y %H:%M:%S %Z")
tuple = dt.timetuple()

localSeconds = time.mktime(tuple)
UTCSeconds = calendar.timegm(tuple)

dt = datetime.datetime.strptime('Jan 01, 1970 12:00:30 AM UTC', "%b %d, %Y %I:%M:%S %p %Z")
tuple = dt.timetuple()
localSeconds = time.mktime(tuple)
UTCSeconds = calendar.timegm(tuple)

localnow = time.time()
gmtnow = time.gmtime()

localString = datetime.datetime.fromtimestamp(int("0")).strftime('%Y-%m-%d %H:%M:%S')
utcString = datetime.datetime.utcfromtimestamp(int("0")).strftime('%Y-%m-%d %H:%M:%S')
humantime = datetime.datetime.fromtimestamp(localnow).strftime('%Y-%m-%d %H:%M:%S %Z')
print

localNow = datetime.datetime.now()
utcNow = datetime.datetime.utcnow()

localTuple = localNow.timetuple()
utcTuple = utcNow.timetuple()

localUnixTime = time.mktime(localTuple)
utcUnixTime = calendar.timegm(utcTuple)
uctUnixTime2 = time.time()
localString = localNow.strftime('%Y-%m-%d %H:%M:%S %Z')
utcString = utcNow.strftime('%Y-%m-%d %H:%M:%S %Z')
print

now=datetime.datetime.now()
ts_epoch = calendar.timegm(datetime.datetime.utcnow().utctimetuple())
strUtcDate = datetime.datetime.utcfromtimestamp(ts_epoch).strftime('%Y-%m-%dT%H:%M:%S%z')

print strUtcDate


################################################################

dtuple = dt.utcnow()

# samething
tuple1 = dtuple.timetuple()
tuple2 = dtuple.utctimetuple()

now1 = calendar.timegm(tuple1)
now2 = calendar.timegm(tuple2)

str1 = dtuple.strftime('%Y-%m-%d %H:%M:%S')
str2 =  time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(now1))


print


