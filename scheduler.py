__author__ = 'kdao'

import sys
import sched
import time
from datetime import datetime as dt
import datetime
import dateutils
from pytz import timezone
from time import gmtime, strftime
import threading

def now_str():
    """Return hh:mm:ss string representation of the current time."""
    t = dt.now(timezone("America/Los_Angeles"))
    return t.strftime("%Y-%m-%d--%H:%M:%S")

#t3 = dt.combine(dt.now() + datetime.timedelta(seconds=10), datetime.time(0, 0))

print "Now:",now_str()

t2 = dt.now(timezone("America/Los_Angeles")) + datetime.timedelta(seconds=10)

t3 = dt.now() + datetime.timedelta(seconds=15)
print "t2",t3.strftime("%H:%M:%S")
print "t3",t3.strftime("%H:%M:%S")
epoch=time.mktime(t3.timetuple())

los=dateutils.to_iso8601()
t4=dateutils.from_iso8601(los)
t5=t4+datetime.timedelta(seconds=10)


print "epochtime T2:",time.mktime(t3.timetuple())
print "epochtime T3:",time.mktime(t3.timetuple())
print "epochtime T5:",time.mktime(t5.timetuple())
print "currentTime:",time.time()
print strftime("%z", gmtime())
print time.timezone
print t5.strftime('%z')

print t3.strftime('%z')

datimeobj=datetime.datetime.fromtimestamp(epoch)
print "datetime:",datimeobj.strftime(("%Y-%m-%d--%H:%M:%S"))





# datetime.date(2011, 01, 01)
def print_event(mp):
    print "EVENT: %s at %s" %(time.time(), mp['name'])




def runschedule(scheduler):
    scheduler.run()


if __name__ == '__main__':

    scheduler = sched.scheduler(time.time, time.sleep)

    scheduler.enterabs(time.mktime(t3.timetuple()),2,print_event,({"id":1,"name":"T3"},))
    scheduler.enterabs(time.mktime(t5.timetuple()),1,print_event,({"id":2,"name":"T5"},))
    print 'START:', time.time()

    #scheduler.enter(20, 2, print_event, ({"id":1,"name":"first message"},))
    #scheduler.enter(3, 1, print_event,({"id":1,"name":"second message"},))

    print "scheduler queue:%s"%scheduler.queue
    thread = threading.Thread(target=runschedule,args=(scheduler,) )
    thread.start()

    while True:
        time.sleep(1)
        print 'Time--->:', time.time()
        print "scheduler queue:%s"%scheduler.queue
        print "Current date & time " + time.strftime("%c")
        if scheduler.empty():
            break



