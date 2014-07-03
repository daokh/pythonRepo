__author__ = 'daokh'

import datetime
from datetime import datetime as dt
import json

from dateutil import parser
import pytz
from pytz import timezone
import requests
import geoutils
from mpmutils import jsondict
import dateutils

dt_str = dt(datetime.MINYEAR, 1, 1)
print dt_str
# dt = parser.parse(dt_str)
# print dt

parser.parse('2011-01-02', None)

S = []

print len(S)
now = dt.now(pytz.utc)
t1 = dt.now(timezone("UTC"))
t2 = t1 + datetime.timedelta(seconds=5)

print dateutils.timestamp(t1)
print dateutils.timestamp(t2)

testdict = jsondict({})
if testdict.radius: testdict.pop("radius")

list = [{'name': 'a'}, {'name': 'b'}]

jsondict = {'commplans': list}
jsonstring = json.dumps(jsondict)

d = dict([("age", 25), ("foo", 25)])


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(2)
print f(42)

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print reduce(lambda x, y: x + y, foo)

adder = lambda x, y: x + y

sum = adder(1, 3)
print sum

try:
    foo = None
    foo.something = 1
except AttributeError as e:
    print "error"

def query(strquery, *fields):
    strFields = "&fields="
    strSearchQuery = ""
    if fields:
        for field in fields:
            strFields += field + "&"

        strSearchQuery = "pretty=true&sort=id&q=" + strquery + strFields + "_source=true"
    else:
        strSearchQuery = "pretty=true&sort=id&q=" + strquery + "&_source=true"
    try:
        res = requests.get("http://localhost:9200/mission_plan_manager/MissionPlans/_search?" + strSearchQuery)
        jsonstr = json.dumps(res.json())
        retJson = json.loads(jsonstr, object_hook=geoutils.jsondict)
        return [hit._source for hit in retJson.hits.hits]

    except:
        return {}


normalQuery = "mission"
activeQuery = "False"

activeQuery = activeQuery.lower()

querystr = """
            {
                "query": {
                    "bool": {
                        "must": {
                            "query_string": {
                                "query": "<QUERY_STRING>"
                            }
                        },
                        "must": {
                            "query_string": {
                                "query": "<ACTIVE_QUERY_STRING>",
                                "fields": ["active"]
                            }
                        }
                    }
                }
            }
"""

querystr = querystr.replace("<QUERY_STRING>",normalQuery)
querystr = querystr.replace("<ACTIVE_QUERY_STRING>",activeQuery)
print querystr

foo = dict ([("name", "fi"),("foo",33)])
print foo

items1 = [ {"key": "abc","notification": "a"},  {"key": "abc2","notification": "b"} ]
items2 = [ {"key": "abc","notification": "aa"},  {"key": "abc2","notification": "bb"}, {"key": "abc3","notification": "bb"}  ]
notificationDitc = {}
for item in items1:
    notificationDitc[item["key"]]  = item["notification"]
for item in items2:
    notificationDitc[item["key"]]  = item["notification"]
listitems = notificationDitc.items()

data = [[1,33,3], [4,5,6], [7,8,9]]
sorted_by_second = sorted(data, key=lambda tup: tup[1])
print
if __name__ == '__main__':
    list = query("9", "missionPlanElements.id")
    print
