__author__ = 'daokh'
import datetime
import time
import pytz
from time import gmtime
import calendar
mpes = ["hi", "foo", "bar", 'hid']

for mpe in mpes:
    if(mpe == "hi"):
        mpes.remove(mpe)

print mpes


S = [1,30,20,30,2]
S.pop()
update=[4,5,6,2]
for i, s in enumerate(S):
    for u in update:
     if s == u:
         S[i] = 999

print S


mpeid = []
if not mpeid:
    print "yes"

print mpeid

result = {"mpeid":1}
foo = result.update({'status':'succeeded'})
print result

input = {"fda":2}
if not input:
    print"YES"


#dt = datetime.datetime.strptime('24052010', "%d%m%Y").date()
dt = datetime.datetime.strptime('01011970 00:00:00 UTC', "%d%m%Y %H:%M:%S %Z")
#dt = dt.astimezone(pytz.UTC)
# tz = pytz.timezone('America/Los_Angeles')
# utc_dt = tz.localize(dt, is_dst=True).astimezone(pytz.utc)
tuple = dt.timetuple()
ans_time = time.mktime(tuple)
ans_time = calendar.timegm(tuple)
print

