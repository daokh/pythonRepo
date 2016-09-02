import a
from a import display
from geoutils import jsondict

a.SOCKET_TIMEOUT = 989


def one():
    global current
    current = 6
def two():
    global current
    print current


if __name__ == '__main__':

    display()
    one()
    two()
    foo = jsondict({})
    if foo.ad is None:
        print "ere"