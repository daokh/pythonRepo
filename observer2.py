__author__ = 'daokh'
__author__ = 'daokh'
from abc import ABCMeta, abstractmethod

class Sender(object):
    def __init__(self):
        self.events = dict()

    def register(self, observer, event):
        # Init the event with an empty list
        if not self.events.has_key(event):
            self.events[event] = list()
        # Adding the observer for the event
        self.events[event].append(observer)

    def unregister(self, observer, event):
        if self.events.has_key(event):
            # Remove the observer for the event
            if observer in self.events[event]:
                self.events[event].remove(observer)
            # Remove the event if its empty
            if len(self.events[event]) == 0:
                self.events.pop(event)

    def update(self, event):
        if self.events.has_key(event):
            for observer in self.events[event]:
                observer.notify(event)



class Observer(object):
    __metaclass__ = ABCMeta

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def notify(self, event):
        raise NotImplementedError()


class MPObserver(Observer):

    def notify(self, event):
        print '-->{name} executing {event}'.format(name=self.name, event=event)


if __name__ == '__main__':

    sender = Sender()
    observer1 = MPObserver('observer1')
    sender.register(observer1,'event1')


    observer1 = MPObserver('observer1')

    dictData = tel = {'jack': 4098, 'sape': 4139}
    sender.register(observer1,dictData)
    sender.update(dictData)
