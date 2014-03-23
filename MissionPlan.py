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

    def __init__(self, id, name, shortname):
        self.id = id
        self.shortname = shortname
        self.name = name
        MissionPlan.mpCount += 1
        self.trigger = None

    def settrigger(self, trigger):
        self.trigger = trigger


    def displaycount(self):
        print "Total MissionPlan %d" % MissionPlan.mpCount

    def displaymissionplan(self):
        print "Name : ", self.name, ", ShortName: ", self.shortname, " id: ", self.id


def jdefault(o):
    if isinstance(o, set):
        return list(o)
    elif isinstance(o, MissionPlan):
        mpdict = o.__dict__
        mpdict.update({'id': o.id})
        return mpdict
    return o.__dict__


###############################################################################3
#Testing

mp1 = MissionPlan(1, "This is long name of MP", "mp1")
trigger = Trigger(2, "GeoFence")
mp1.settrigger(trigger)

print json.dumps(mp1, default=jdefault)