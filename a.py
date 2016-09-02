

from time import clock


SOCKET_TIMEOUT = 10 # in secs


now = clock()
entry = '{:016.6f} \n'.format(now)
now = clock()
entry2 = '{:016.6f} \n'.format(now)
print
def display():
    print SOCKET_TIMEOUT