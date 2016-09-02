__author__ = 'daokh'


import ConfigParser
from functools import partial
from itertools import chain

class Helper:
    def __init__(self, section, file):
        self.readline = partial(next, chain(("[{0}]\n".format(section),), file, ("",)))



if __name__ == '__main__':
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    with open("mpm.cfg") as ifh:
        config.readfp(Helper("lncs_info", ifh))
    print(config.get("lncs_info", "userid"))