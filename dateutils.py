__author__ = 'kdao'

import time

import pytz
import dateutil.parser
from datetime import datetime, timedelta

#-----------------------------------------------
utc = pytz.utc
PDT = pytz.timezone('America/Los_Angeles')

ZERO = timedelta(0)
HOUR = timedelta(hours=1)

utcdatetime=datetime.now(utc)
utcdelta=utcdatetime.utcoffset()

#-----------------------------------------------
def to_iso8601(when=None, tz=PDT):
    """Convert time object to iso8601, by default use current time"""
    #contruct utc time for comparison

    if not when:
        when = datetime.now(tz)
    if not when.tzinfo:
        when = tz.localize(when)
    #Uncomment this is want to use fraction of seconds
    #_when = when.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    #return _when[:-8] + _when[-5:]  # remove nanoseconds

    delta =when.utcoffset()
    zerodelta= timedelta()
    if abs(utcdelta-delta) > zerodelta: # non UTC time so format the timezone part
        _when = when.strftime("%Y-%m-%dT%H:%M:%S%z")
        _when=_when[:-2] + ":"+_when[-2:]
    else: #UTC time then just add the Z
        _when = when.strftime("%Y-%m-%dT%H:%M:%SZ")

        _when = when.strftime("%Y-%m-%dT%H:%M:%S%z")
        _when=_when[:-2] + ":"+_when[-2:]

    return _when


#-----------------------------------------------
def from_iso8601(when=None, tz=PDT):
    """Convert the time from iso8601 to time object"""

    _when = dateutil.parser.parse(when)
    if _when.tzinfo==dateutil.tz.tzutc():
        _when=_when.replace(tzinfo=pytz.utc)
    else:
        _when=_when.replace(tzinfo=None)
        _when = tz.localize(_when)


    # if not _when.tzinfo:
    #     _when = tz.localize(_when)
    return _when


def datetime_to_utc(date):
    """Returns date in UTC w/o tzinfo"""
    if date.tzinfo:
        utcdate = date.astimezone(pytz.UTC)
        utcdate = utcdate.replace(tzinfo=pytz.utc)
        return utcdate
    return date


def utc_to_local(utc_dt,local_tz):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt) # .normalize might be unnecessary


def local_time_offset(t=None):
    """Return offset of local zone from GMT, either at present or at time t."""
    # python2.3 localtime() can't take None
    if t is None:
        t = time.time()

    if time.localtime(t).tm_isdst and time.daylight:
        return -time.altzone
    else:
        return -time.timezone


def make_tz_aware(dt, tz='UTC'):
    """Add timezone information to a datetime object, only if it is naive."""
    tz = dt.tzinfo or tz
    try:
        tz = pytz.timezone(tz)
    except AttributeError:
        pass
    return tz.localize(dt)

if __name__ == '__main__':

    #Convert current time and UTC to sio8601
    print "Convert current time and UTC to iso8601"
    los=to_iso8601()
    east=to_iso8601(None,pytz.timezone("US/Eastern"))
    utc = to_iso8601(None, pytz.timezone("UTC"))
    print "los angeles iso8601:", los
    print "UTC iso8601:", utc

    #Convert iso8601 back to time object
    print "Convert iso8601 back to time object"
    losobj=from_iso8601(los)
    eastobj=from_iso8601(east)
    utcobj = from_iso8601(utc,)
    print "from los iso8601:", losobj
    print "from utc iso8601:", utcobj

    losobj = datetime.now(pytz.timezone("America/Los_Angeles"))
    utcobj = datetime.now(pytz.timezone("UTC"))

    print "Generate 2 current time: los and utc timezone"
    print losobj
    print utcobj


    print "Convert los timezone to utc"
    utcobj=datetime_to_utc(losobj)
    print utcobj
    print "Convert utc back to los angeles"
    losobj = utc_to_local(utcobj,pytz.timezone("America/Los_Angeles"))
    print losobj

    now=datetime.now(pytz.timezone("UTC"))
    now=make_tz_aware(now)
    print

