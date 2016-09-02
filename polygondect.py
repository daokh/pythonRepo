__author__ = 'daokh'

from  geoutils import is_between,jsondict
import json
def point_inside_polygon(point, poly):
    n = len(poly)
    inside = False

    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if point.lat > min(p1y, p2y):
            if point.lat <= max(p1y, p2y):
                if point.lon <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (point.lat - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or point.lon<= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def isPointOnPolygon(point, poly):
    n = len(poly)
    for i in range(n):
        lon1,lat1 = poly[i]
        p1 = jsondict({"lat":lat1,"lon":lon1})

        lon2,lat2= poly[-n+i+1]
        p2 = jsondict({"lat":lat2,"lon":lon2})
        if is_between( p1, point, p2):
            return True
    return False





if __name__ == '__main__':

    poly =  [(-117, 32), (-114, 32), (-115, 29)]
    a = '{"lat": 32, "lon":-116}'
    point = json.loads(a,object_hook=jsondict )

    isPointOnPolygon(point,poly)

    # poly = [(1, 1), (2, 2), (4, 1.8), (4.5, 1.6), (3, 1.4), (2, 0.8)]
    #
    # x1 = 2.7
    # y1 = 1.4
    # isInside = point_inside_polygon(x1,y1,poly)
    # print isInside


    poly = [(-117, 32), (-118, 33), (-119, 34), (-113, 34.5), (-113.6, 32), (-116, 31)]
    point = jsondict({"lat": 34, "lon":-119})
    isInside = point_inside_polygon(point,poly) or isPointOnPolygon(point,poly)
    print isInside