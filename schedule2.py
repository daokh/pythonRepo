__author__ = 'kdao'


from apscheduler.scheduler import Scheduler
from apscheduler.jobstores.shelve_store import ShelveJobStore

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
t5=t4+datetime.timedelta(seconds=5)


print "epochtime T2:",time.mktime(t3.timetuple())
print "epochtime T3:",time.mktime(t3.timetuple())
print "epochtime T5:",time.mktime(t5.timetuple())
print "currentTime:",time.time()
print strftime("%z", gmtime())
print time.timezone
print t5.strftime('%z')

print t3.strftime('%z')


def print_event(name):
    print 'Excute:', time.time(), name



if __name__ == '__main__':


    print 'START:', time.time()


    # Start the scheduler
    sched = Scheduler()


    # Store the job in a variable in case we want to cancel it
    job = sched.add_date_job(print_event, t5, ['text---->'])

    sched.start()

    while True:
        print('This is the main thread.')
        print('schedule list:'),sched.print_jobs()
        time.sleep(2)
    # while True:
    #     time.sleep(1)
    #     print 'Time--->:', time.time()
    #     print "scheduler queue:%s"%sched.
    #     print "Current date & time " + time.strftime("%c")
    #     if scheduler.empty():
    #         break

