__author__ = 'kdao'

def testargs(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

if __name__ == '__main__':

    testargs('yasoob', 'python', 'eggs', 'test')

    listargs = ['python', 'eggs', 'test']
    testargs('yasoob', *listargs)