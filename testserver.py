__author__ = 'daokh'

# Additional library imports
import requests
from requests.adapters import HTTPAdapter, PoolManager
import logging

LOGFORMAT = '%(asctime)s - %(lineno)4d: %(levelname)s: %(name)s : %(message)s'

class SSLAdapter(HTTPAdapter):
    """An HTTPS Transport Adapter that uses an arbitrary SSL version."""

    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version

        super(SSLAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=self.ssl_version)


if __name__ == '__main__':
    try:
        logging.basicConfig(format=LOGFORMAT)
        logging.getLogger('requests').setLevel(logging.DEBUG)

        import warnings
        warnings.filterwarnings("ignore",module='requests')

        session = requests.Session()
        session.mount('https://', SSLAdapter("PROTOCOL_TLSv1"))
        res = session.request('GET',"https://[2001:db8:a01:a01:10:6:22:70]:8443/webGUI/",verify=False,timeout=600,)
        # res = session.request('GET',"https://m9-lncs:8443/webGUI/",verify=False)

        if res.status_code == 200:
            print res.content
        else:
            print "Error", res.status_code


    except StandardError as e:
        print "Error=====>", e

