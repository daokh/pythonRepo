try:
    import simplejson as json
except ImportError:
    import json

from math import pi
import copy
import os

class jsondict(dict):
    """Allows us to use "." notation on json instances"""

    def __init__(self, kwargs):
        self.update(kwargs)
        super(dict, self).__init__()

    def __setattr__(self,key,value):
        super(jsondict, self).__setitem__(key,value)

    def __str__(self):
        return super(dict, self).__str__()

    def __getitem__(self, key):
        if key in self:
            return super(jsondict, self).__getitem__(key)
        return None

    def __getattr__(self,key):
        """return None if key is not in dictionary"""
        #This will help for some operations: <somedict>.foo return None instead of getting Key Error when foo is not
        #in <somedict>
        if key in self:
            return super(jsondict, self).__getitem__(key)
        else:
            return None


    def __deepcopy__(self, memo):
        return jsondict([(copy.deepcopy(k, memo), copy.deepcopy(v, memo)) for k, v in self.items()])


def parseDMI(filename):
    """This function is used to parse the czml file"""
    # f = open(filename, "r")
    # text = f.readline()
    alert = {}
    with open(filename) as f:
        src = os.path.splitext(os.path.split(filename)[1])[0]
        alertdata = json.load(f)

    keep = [ x for x in alertdata if x["nodeId"] != 3 and  x["nodeId"] !=4 and  x["nodeId"] != 5 and  x["nodeId"] != 6 and  x["nodeId"] != 8 ]
    foo = json.dumps(keep);
    foqui = open("out.txt", "w")
    foqui.write(str(foo))
    print

if __name__ == "__main__":
    parseDMI("alerts.json")