__author__ = 'kdao'

#-----------------------------------------------
import datetime
import pytz
from datetime import  datetime
from dateutil import tz


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
  return _when[:-8] + _when[-5:] # remove nanoseconds
#-----------------------------------------------
def from_iso8601(when=None, tz=PDT):
  _when = dateutil.parser.parse(when)
  if not _when.tzinfo:
    _when = tz.localize(_when)
  return _when

def datetime_to_utc(date):
    """Returns date in UTC w/o tzinfo"""
    if date.tzinfo:
        return date.astimezone(pytz.UTC).replace(tzinfo=None)
    return  date

print to_iso8601(None)
utc=to_iso8601(None,pytz.timezone("UTC"))
print utc

timeobj=from_iso8601(utc)
print timeobj

timeobj=datetime.now(timezone("America/Los_Angeles"))

utcobj=datetime_to_utc(timeobj)
print timeobj
print utcobj

foo=utcobj.astimezone(PDT)
print "HERE"