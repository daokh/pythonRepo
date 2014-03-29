__author__ = 'kdao'
from abc import ABCMeta, abstractmethod
import logging,logging.config
from threading import Thread, Condition
import time
import random


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
        nums = range(5)
        global queue
        while True:

            num = random.choice(nums)

            print("Produced %i"%num)
            self.notifyObservers(num)
            time.sleep(random.random())




class Observer(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def update(self, eventObj):
        raise NotImplementedError()


class ObseverQueue(Thread,Observer):

    _condition = Condition()
    _queue = []

    def run(self):

        while True:
            self._condition.acquire()
            if not self._queue:
                print "Nothing in queue, consumer is waiting"
                condition.wait()
            num = queue.pop(0)
            self._condition.notify()
            self._condition.release()


            self.notifyObservers(num)

    def update(self, eventObj):
        self._condition.acquire()
        self._queue.append(eventObj)
        self._condition.notify()
        self._condition.release()


class MPObserver(Observer):
    def update(self, eventObj):
        print '-->{name} executing {event}'.format(name=self.name, event=eventObj)


if __name__ == '__main__':
    sender = Sender()
    mpObserver = MPObserver('observer1')

    observerQueue = ObseverQueue()
    observerQueue.register(mpObserver)

    sender.register(observerQueue)

    observerQueue.start()

    sender.start()
