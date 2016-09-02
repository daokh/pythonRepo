__author__ = 'kdao'
import time
import thread
from threading import Thread



# Define a function for the thread
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName, time.ctime(time.time()) )

    print "Done"


if __name__ == '__main__':

    # Create two threads as follows
    try:
       t1 = Thread(target = print_time, args=("Thread-1", 2, ) )
       t1.start()
       t2 = Thread(target = print_time, args=("Thread-2", 2, ) )
       t2.start()
    except:
       print "Error: unable to start thread"

    while 1:
       pass