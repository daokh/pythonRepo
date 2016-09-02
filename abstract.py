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

    @abstractmethod
    def say_something(self):
        return "I'm an animal!"

    @abstractmethod
    def notify(self, event):
        print '{name} executing {event}'.format(name=self.name, event=event)


class MPObserver(Observer):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        s = super(MPObserver, self).say_something()
        print "%s - %s" % (s, self.name)

    def notify(self, event):
        print '-->{name} executing {event}'.format(name=self.name, event=event)


class MPObserver2(Observer):
    def __init__(self, name):
        self.name = name

    def say_something(self):
        s = super(MPObserver, self).say_something()
        print "%s - %s" % (s, self.name)

    def notify(self, event):
        print '***{name} executing {event}'.format(name=self.name, event=event)


if __name__ == '__main__':
    c = MPObserver("meo")
    c.say_something()
    c.notify("event1")

    sender = Sender()
    observer1 = MPObserver('observer1')
    sender.register(observer1, 'event1')
    observer2 = MPObserver2('observer2')
    sender.register(observer1, 'event1')
    sender.register(observer2, 'event1')
    sender.update('event1')


