__author__ = 'daokh'
import ConfigParser
from configutils import Helper


config = ConfigParser.RawConfigParser(allow_no_value=True)
with open("mpm.cfg") as ifh:
    config.readfp(Helper("lncs_info", ifh))
lncsuserid = config.get("lncs_info", "userid")
lncsuserpass = config.get("lncs_info", "userpass")
baseurl = config.get("lncs_info", "baseurl")