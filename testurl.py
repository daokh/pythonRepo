import urllib2
from urlparse import urlparse


def isValidUrl(url):
    isValid = True
    try:
        result = urlparse(link)
        if not result.netloc or not result.scheme:
            isValid = False
    except:
        isValid = False

    return isValid


links = ['http://[2001:db8:0:1]','http://127.0.0.1','http://www.google.com', 'google.com','http://','[2009:db8:0:1]']

for link in links:

    if not isValidUrl(link):
        print "isValid:", link