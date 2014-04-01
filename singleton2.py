__author__ = 'kdao'
from singleton import MyClass,Singleton
from threading import Thread, Condition
import time

@Singleton
class manager(Thread):


    def __init__(self):
        self.count = 0
        Thread.__init__(self)

    def run(self):
        while True:
            print ('count: %i'%self.count)
            time.sleep(5)
            self.count +=1

a = manager.Instance()

a.start()

b = manager.Instance()

b.start()