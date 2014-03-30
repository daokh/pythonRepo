__author__ = 'kdao'
from abc import ABCMeta, abstractmethod
import logging,logging.config
from threading import Thread, Condition
import time
import random

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

condition = Condition()
queue = []
MAX_NUM = 10


class Sender(Thread):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.observers = list()
        Thread.__init__(self)

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            return True
        else:
            return False

    def unregister(self, observer):
        if observer in self.observers:
            return self.observers.remove(observer)

    def notifyObservers(self, eventObj):
        for observer in self.observers:
            observer.update(eventObj)

    def run(self):
        nums = range(10)
        global queue
        while True:
            num = random.choice(nums)
            logger.debug("Produced %i"%num)
            self.notifyObservers(num)
            time.sleep(5)


class Observer(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def update(self, eventObj):
        raise NotImplementedError()


class ObseverQueue(Sender,Observer):

    _condition = Condition()
    _queue = []

    def run(self):

        while True:
            self._condition.acquire()
            if not self._queue:
                logger.debug("Nothing in queue, waiting for udpate")
                self._condition.wait()
            num = self._queue.pop(0)
            logger.debug ("observerqueue got %i" %num)
            self._condition.notify()
            self._condition.release()
            self.notifyObservers(num)

            time.sleep(15)

    def update(self, eventObj):
        logger.debug("observerqueue update %i" %eventObj)
        self._condition.acquire()
        self._queue.append(eventObj)

        logger.debug("total queues is %i and queue is %s" %(len(self._queue), self._queue)  )
        self._condition.notify()
        self._condition.release()


class MPObserver(Observer):
    def update(self, eventObj):
        print '-->{name} processes {event}'.format(name=self.name, event=eventObj)


if __name__ == '__main__':

    sender = Sender()
    mpObserver = MPObserver('observer1')
    observerQueue = ObseverQueue()
    observerQueue.register(mpObserver)

    sender.register(observerQueue)

    observerQueue.start()

    sender.start()
