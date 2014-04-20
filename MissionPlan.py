__author__ = 'kdao'
import json


class Trigger:
    tgCount = 0

    def __init__(self, id, triggertype):
        self.id = id
        self.triggertype = triggertype
        Trigger.tgCount += 1
    def displaytrigger(self):
        print "TriggerType : ", self.triggertype, ", id: ", self.id


class MissionPlan:
    'Common base class for MissionPlan'
    mpCount = 0

    def __init__(self, id, name='', shortname=''):
        self.id = id
        self.shortname = shortname
        self.name = name
        MissionPlan.mpCount += 1
        self.trigger = None



    def settrigger(self,trigger):
        self.trigger = trigger



    def displaycount(self):
        print "Total MissionPlan %d" % MissionPlan.mpCount

    def displaymissionplan(self):
        print "Name : ", self.name, ", ShortName: ", self.shortname, " id: ", self.id

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d


def serialize_object(o):
    if isinstance(o, set):
        return list(o)
    elif isinstance(o,MissionPlan):
        mpdict = o.__dict__
        mpdict.update({'id': o.id})
        return mpdict
    return o.__dict__


###############################################################################3
#Testing

mp1 = MissionPlan(3,"This is long name of MP","mp3")
trigger = Trigger(2,"GeoFence")
mp1.settrigger(trigger)

mp2 = MissionPlan(1)
s = json.dumps(mp1, default=serialize_object)

#print s
print(json.dumps(mp1, default=serialize_object))
s = json.dumps(mp1, default=serialize_object)
#print(json.dumps(mp2, default=serialize_object))

mpobj = json.loads(s, object_hook=unserialize_object)

print(json.dumps(mpobj, default=serialize_object))


#put in db
#mpurl = /mission_plan_manager/MissionPlans/'+mp1.id
#r = requests.post('http://localhost:9200/mission_plan_manager/MissionPlans',json.dumps(mp1, default=serialize_object))


# edata = """
# {
#        "query" : {
#         "term" : { "shortname" : "mp3" }
#     }
# }
# """
# r = requests.post('http://localhost:9200/_search', data=edata)
#
# tJSON = json.loads(r.text)
# tJSON = tJSON['hits']['hits'][0]['_source']
# #print(json.dumps(tJSON))
#
# mpobj = json.loads(json.dumps(tJSON), object_hook=unserialize_object)
# print(json.dumps(mpobj, default=serialize_object))




