__author__ = 'kdao'

import sys
import sched
import time
from datetime import datetime as dt
import datetime

def now_str():
    """Return hh:mm:ss string representation of the current time."""
    t = dt.now().time()
    return t.strftime("%Y-%m-%d--%H:%M:%S")


#t3 = dt.combine(dt.now() + datetime.timedelta(seconds=10), datetime.time(0, 0))

print now_str()
t3 = dt.now() + datetime.timedelta(seconds=10)

print t3.strftime("%H:%M:%S")
epoch=time.mktime(t3.timetuple())


datimeobj=datetime.datetime.fromtimestamp(epoch)
print datimeobj.strftime(("%Y-%m-%d--%H:%M:%S"))

# datetime.date(2011, 01, 01)


def print_event(name):
    print 'EVENT:', time.time(), name


scheduler = sched.scheduler(time.time, time.sleep)

scheduler.enterabs(time.mktime(t3.timetuple()),1,print_event,('FOOO',))

print 'START:', time.time()
scheduler.enter(20, 2, print_event, ('first',))
print "scheduler queue:%s"%scheduler.queue
scheduler.enter(3, 1, print_event, ('second',))

scheduler.run()