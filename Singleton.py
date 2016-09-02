__author__ = 'kdao'
from abc import ABCMeta, abstractmethod
class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


class Observer(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def notify(self, event):
        raise NotImplementedError()


@Singleton
class MyClass(Observer):
    tgCount = 0

    def __init__(self):
        Observer.__init__(self,"foo")
        print 'Foo created'
        self.count = 0


    def message(self):
        print ('count = %i'%self.count)

    def inc(self ):
        self.count+=1

    def notify(self, event):
        print '-->{name} executing {event}'.format(name=self.name, event=event)


a = MyClass.Instance()
a.inc()
b = MyClass.Instance()
b.inc()
b.message()
b.notify("hi")
print a is b
