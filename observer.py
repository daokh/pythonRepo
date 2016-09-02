__author__ = 'daokh'
from abc import ABCMeta, abstractmethod
import logging,logging.config

import sys
# Set log level based on whether a command line parameter exists.
# _logformat = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
# _handler = logging.FileHandler('myapp.log')
#
# if len(sys.argv) > 1 and sys.argv[1] == 'debug':
#     logging.basicConfig(format=_logformat, level=logging.INFO, handler=_handler)
# else:
#     logging.basicConfig(format=_logformat, level=logging.WARNING, handler=_handler)
#
# logger = logging.getLogger(__name__)
# logger.addHandler(_handler)


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

class Sender(object):
    def __init__(self):
        self.observers = list()

    def register(self, observer):
        logger.info('register')
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

    def __init__(self, name):
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
