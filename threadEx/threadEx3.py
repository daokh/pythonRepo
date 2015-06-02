__author__ = 'kdao'
from threading import Event
import time
from threading import Thread
from threading import current_thread
class myObj ():
    def __init__(self, name, counter):

        self._stopper = Event()
        self.name = name
        self.counter = counter
        self.t  = None
        self.count = 0

    def start(self):
        self.t  = Thread(name = self.name, target = self._doWork, args=(self.name, ) )
        self.t.start()



    def _doWork(self,threadName):
        self._stopper.clear()


        while not self._stopper.is_set():
            print "%s: %s" % ( current_thread().getName(),time.ctime(time.time()) )
            self.count += 1
            self._stopper.wait(10)

        print "Done"
        print ("Count: %d"%self.count)

    def stopit(self):
        self._stopper.set()
        self.t.join()

    def stopped(self):
        return self._stopper.is_set()

if __name__ == '__main__':
    my = myObj("foo",3)

    my.start()

    time.sleep(5)

    print "Stop now"
    my.stopit()

    my.start()

    time.sleep(15)
    my.stopit()