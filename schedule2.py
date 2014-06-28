from timeexamples import dateutils

__author__ = 'kdao'


from apscheduler.scheduler import Scheduler
import sched
import time
from datetime import datetime as dt
import datetime
from pytz import timezone
from time import gmtime, strftime
import pytz
import logging,logging.config


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

def now_str():
    """Return hh:mm:ss string representation of the current time."""
    t = dt.now(timezone("America/Los_Angeles"))
    return t.strftime("%Y-%m-%d--%H:%M:%S")

#t = dt.combine(dt.now() + datetime.timedelta(seconds=10), datetime.time(0, 0))

print "Now:",now_str()

t1 = dt.now(timezone("UTC")) + datetime.timedelta(seconds=5)

t2 = dt.now() + datetime.timedelta(seconds=10)
t2= dateutils.naive_to_local(t2,"America/Los_Angeles")

utc= dateutils.to_iso8601(None,pytz.utc)
t3= dateutils.from_iso8601()+ datetime.timedelta(seconds=10)

print "t1",t1.strftime("%Y-%m-%d--%H:%M:%S")
print "t2",t2.strftime("%Y-%m-%d--%H:%M:%S")
print "t3",t3.strftime("%Y-%m-%d--%H:%M:%S")
epoch=time.mktime(t3.timetuple())

los= dateutils.to_iso8601()
t4= dateutils.from_iso8601(los)
t5=t4+datetime.timedelta(seconds=15)
print "t5",t5.strftime("%Y-%m-%d--%H:%M:%S")

print "epochtime T2:",time.mktime(t3.timetuple())
print "epochtime T3:",time.mktime(t3.timetuple())
print "epochtime T5:",time.mktime(t5.timetuple())
print "currentTime:",time.time()
print strftime("%z", gmtime())
print time.timezone
print t5.strftime('%z')

print t3.strftime('%z')


def print_event(name):
    print 'Execute Schedule---->>>>>:', time.time(), name



if __name__ == '__main__':


    print 'START:', time.time()


    # Start the scheduler
    sched = Scheduler()

    sched.start()
    # Store the job in a variable in case we want to cancel it
    job = sched.add_date_job(print_event, t1, ['T1---->'])
    job = sched.add_date_job(print_event, t2, ['T2---->'])
    job = sched.add_date_job(print_event, t3, ['T3---->'])
    job = sched.add_date_job(print_event, t5, ['T5---->'])

    print('schedule list--->:'),sched.get_jobs()

    while True:
        logger.info('This is the main thread.')
        #print('schedule list:'),sched.print_jobs()
        logger.info(sched.get_jobs())
        time.sleep(2)
    # while True:
    #     time.sleep(1)
    #     print 'Time--->:', time.time()
    #     print "scheduler queue:%s"%sched.
    #     print "Current date & time " + time.strftime("%c")
    #     if scheduler.empty():
    #         break

