__author__ = 'daokh'

import time
import pytz, datetime
from pytz import timezone
from time import gmtime, strftime,ctime,localtime,mktime
from datetime import tzinfo, timedelta, datetime


ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime2 = time.localtime(time.time())
print "Local current time :", localtime

localtime2 = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime2

#print time.altzone

print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "stftime GMT TIME: %s" %strftime('%a, %d %b %Y %H:%M:%S +0000', gmtime())
print "strftime LOCALTIME:",strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
#print "strftime ctime:",strftime("%a, %d %b %Y %H:%M:%S +0000", ctime())
print "LOCALTIME CTIME:",ctime()
print "LOCALTIME LOCAL",localtime()
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"


def local_to_utc(t):
    secs = mktime(t)
    return gmtime(secs)


naive = time.strptime ("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
gmt = local_to_utc(naive)


print "convert-->",strftime('%d %b %Y %H:%M:%S +0000 %Z',naive)
print "convert GMT-->",strftime('%d %b %Y %H:%M:%S +0000 %Z',gmt)
print "++++++++++++++++++++++++++++++++++++++++++"

now_time = datetime.now(timezone("UTC"))
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
print "UTC TIME from datetime:",now_time.strftime(fmt)

now_time = datetime.now(timezone("America/Los_Angeles"))
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
print "PDT TIME from datetime:",now_time.strftime(fmt)


print "++++++++++++++++++++++++++++++++++++++++++"
now_time = datetime.now(timezone("America/Los_Angeles"))
timetuple = now_time.timetuple()
print "now is:",strftime(fmt,timetuple)


now_time = datetime.now(timezone("UTC"))
timetuple = now_time.timetuple()
print "now in UTC is:",strftime(fmt,timetuple)

dt = datetime.fromtimestamp(mktime(gmt))
timetuple = now_time.timetuple()

print "here",timetuple





