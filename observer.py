__author__ = 'daokh'
from abc import ABCMeta, abstractmethod

class Sender(object):
    def __init__(self):
        self.observers = list()

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            return True
        else:
            return False

    def unregister(self, observer):
        if observer in self.observers:
            return self.observers.remove(observer)

    def update(self, event):
        for observer in self.observers:
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
    sender.register(observer1)

    sender.register(observer1)

    sender.unregister(observer1)

    dictData = tel = {'jack': 4098, 'sape': 4139}
    sender.register(observer1)
    sender.update(dictData)
