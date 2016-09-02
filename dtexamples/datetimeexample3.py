from datetime import datetime as dt
import time
import pytz
from time import gmtime
import calendar
import sys

d = dt.utcnow()
now = calendar.timegm(d.utctimetuple())



now2 = time.time()

print