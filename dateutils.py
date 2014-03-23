__author__ = 'kdao'

#-----------------------------------------------
import pytz
from datetime import datetime

from pytz import timezone
import dateutil.parser
#-----------------------------------------------
utc = pytz.utc
PDT = pytz.timezone('America/Los_Angeles')
#-----------------------------------------------
def to_iso8601(when=None, tz=PDT):
    if not when:
        when = datetime.now(tz)
    if not when.tzinfo:
        when = tz.localize(when)
    _when = when.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    return _when[:-8] + _when[-5:]  # remove nanoseconds


#-----------------------------------------------
def from_iso8601(when=None, tz=PDT):
    _when = dateutil.parser.parse(when)
    if not _when.tzinfo:
        _when = tz.localize(_when)
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






los=to_iso8601()
utc = to_iso8601(None, pytz.timezone("UTC"))
print los
print utc

losobj=from_iso8601(los)
utcobj = from_iso8601(utc,)
print "from iso8601", losobj
print "from iso8601:", utcobj

losobj = datetime.now(timezone("America/Los_Angeles"))
utcobj = datetime.now(timezone("UTC"))

print utcobj
print losobj


utcobj=datetime_to_utc(losobj)
print utcobj

losobj=utc_to_local(losobj,pytz.timezone("America/Los_Angeles"))
print losobj
foo= utc_to_local(utcobj,pytz.timezone("America/Los_Angeles"))
#foo = utcobj.astimezone(PDT)
print "HERE"