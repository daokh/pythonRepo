import math
import json
import copy

class dict(dict):
    """Allows us to use "." notation on json instances"""

    def __init__(self, kwargs):
        self.update(kwargs)
        super(dict, self).__init__()

    __getattr__, __setattr__ = dict.__getitem__, dict.__setitem__

    def __str__(self):
        #return json.dumps(self.__dict__.__str__())
        return super(dict, self).__str__()


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



def distance(pointA,pointB):
   return math.sqrt(pow( abs(pointA.lat - pointB.lat),2) +  pow( abs(pointA.lon - pointB.lon),2))

def is_between(pointA,pointC,pointB):
    """ Check if point C is on the line between A and B """
    return distance(pointA,pointC) + distance(pointC,pointB) == distance(pointA,pointB)

def isInCircle(center,radius,point):
    return distance(center,point) <= radius

def getNW_SE(southwest,northeast):
    southwest = dict(southwest)
    northeast = dict(northeast)
    northwest = dict({"lat": northeast.lat, "lon":southwest.lon})
    southeast = dict({"lat": southwest.lat, "lon":northeast.lon})

    return northwest,southeast

def _sign(p1, p2, p3):
    """Supported function for isPointInTriangle"""
    p1 = dict(p1)
    p2 = dict(p2)
    p3 = dict(p3)
    return (p1.lon - p3.lon) * (p2.lat - p3.lat) - (p2.lon - p3.lon) * (p1.lat - p3.lat)

def _isPointInTriangle(point, p1, p2, p3):
    """Check if the point is inside the Triangle"""
    b1 = _sign(point, p1, p2) < 0.0
    b2 = _sign(point, p2, p3) < 0.0
    b3 = _sign(point, p3, p1) < 0.0

    return ((b1 == b2) and (b2 == b3))

def isPointInRectangular(point, sw, ne):
    """Check if the point is inside the Rectangular"""
    # If we divide the rectangular into 2 triangles, the point is determined inside rectangular only if the point
    # is inside at least 1 triangle
    nw,se = getNW_SE(sw,ne)
    return _isPointInTriangle(point,sw,nw,ne) or _isPointInTriangle(point,sw,se,ne)






if __name__ == '__main__':
    A = '{"lat": 2, "lon":2}'
    B = '{"lat": 1, "lon":1}'
    pointA = json.loads(A,object_hook=dict )
    pointB = json.loads(B,object_hook=dict )

    radius = distance(pointA,pointB)

    C = dict({"lat": 1.5, "lon":1.5})

    if isInCircle(pointA,radius,C):
        print "C is inside cirle"


    sw = dict({"lat": 1, "lon":1})
    ne = dict({"lat": 4, "lon":4})

    nw,se = getNW_SE(sw,ne)

    print "North West:%s and South East: %s" %(ne,sw)



    point = {"lat": 4, "lon":4.1}

    if isPointInRectangular(point,sw,ne):
        print "Point is inside Rectangular"