__author__ = 'daokh'

import json


class TS:

    def __init__(self,pStart=0,pEnd=0):
        self.start = 0
        self.end = 0

    def setStart(self,pStart):
        self.start = pStart

    def setEnd(self,pEnd):
        self.start = pEnd

    def start(self):
        return self.start

    def end(self):
        return self.start

class MF:

    def __init__(self,pId=0,pMpId=0):
        self.mpId = pMpId
        self.mpeIds = []
        self.timespans = []
        self.id = pId

    def appendMpeId(self,*mpeId):
        self.mpeIds.append(mpeId)

    def setMpeIds(self,*pMpeIds):
        self.mpeIds = pMpeIds

    def getMpeIds(self):
        return self.mpeIds

    def appendTimeSpan(self,ptimeSpan):
        self.timespans.append(ptimeSpan)

    def getTimeSpans(self):
        return self.timespans

    def setTimeSpans(self,*pTimeSpans):
        self.timespans = pTimeSpans


def deserialize_object(d):

    if d.has_key('id'):
        mf = MF(d['id'],d['mpId'])
        mf.setTimeSpans(d['timespans'])
        return mf

    elif d.has_key('start'):
        return TS(d['start'],d['end'])

    else:
        return d


def serialize_object(o):
    if isinstance(o, set):
        return list(o)
    elif isinstance(o,TS):
        mpdict = o.__dict__
        # mpdict.update({'id': o.id})
        return mpdict
    return o.__dict__


if __name__ == '__main__':
    ts1 = TS()
    ts2 = TS()
    ts2.start = 22
    ts = [ts1,ts2]

    s = json.dumps(ts, default=serialize_object)

    mf = MF(324)
    mf.timespans.append(ts1)
    mf.timespans.append(ts2)

    mf.mpeIds = [234234,3243]

    s = json.dumps(mf, default=serialize_object)

    mfobj = json.loads(s, object_hook=deserialize_object)
    print
