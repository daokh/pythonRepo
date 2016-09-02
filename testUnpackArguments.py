__author__ = 'daokh'



def isNotNone(*itemToCheck):
    for i in itemToCheck:
        if i is None:
            return False
    return True

if __name__ == '__main__':
    a  = 1
    b = 0
    c = None

    foo = isNotNone(a,b,c)
    print foo