__author__ = 'daokh'

import copy
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


def find(f, seq):
  """Return first item in sequence where f(item) == True."""
  for item in seq:
    if f(item):
      return item

def iequal(a, b):
    try:
        return a.lower() == b.lower()
    except AttributeError:
        return a == b