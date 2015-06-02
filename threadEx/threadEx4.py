__author__ = 'kdao'
from threading import Event
import time
from threading import Thread
import sys
import threading
import time
import logging


class StoppableThread(Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        print( "base init")
        super(StoppableThread, self).__init__()
        self._stopper = threading.Event()

    def stopit(self):
        print( "base stop()" )
        self._stopper.set()

    def stopped(self):
        return self._stopper.is_set()

class datalogger(StoppableThread):
    """
    """

    import time

    def __init__(self, name):
      """
      """
      StoppableThread.__init__(self)
      self.nane  = name
      print( "thread init" )

    def run(self):
        print( "thread %s  running" % (self.name) )
        while not self.stopped():
            print "Working"
            time.sleep(3)
        print "Thread is ending"



if __name__ == '__main__':
    t = datalogger("foo")
    t.start()

    time.sleep(3)

    t.stopit()

    print ("Wait for thread to finish")

    t.join()

    t = datalogger("foo")
    t.start()