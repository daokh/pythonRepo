#!/usr/bin/python

# Convert XYZ coordinates to cartesien LLA (Latitude/Longitude/Altitude)
# Alcatel Alenia Space - Nicolas Hennion
# Version 0.1
#
# Python version translation by John Villalovos
# 

from optparse import OptionParser
import os, sys
from math import atan2, cos, pi, sin, sqrt, tan

def main():
     options, args = parseCommandLine()
     calculate(options)

def parseCommandLine():
     usage = "%prog X Y Z"
     parser = OptionParser(usage = usage)
     options, args = parser.parse_args()

     if len(args) != 3:
         print "Error: 3 arguments are required"
         displayUsage(parser)
         sys.exit(1)
     try:
         options.x = float(args[0])
         options.y = float(args[1])
         options.z = float(args[2])
     except ValueError:
         print "Error: Arguments must be floating point numbers"
         displayUsage(parser)
         sys.exit(1)
     return options, args

def calculate(options):
     x = options.x
     y = options.y
     z = options.z

     # Constants (WGS ellipsoid)
     a = 6378137
     e = 8.1819190842622e-2
     # Calculation
     b = sqrt(pow(a,2) * (1-pow(e,2)))
     ep = sqrt((pow(a,2)-pow(b,2))/pow(b,2))
     p = sqrt(pow(x,2)+pow(y,2))
     th = atan2(a*z, b*p)
     lon = atan2(y, x)
     lat = atan2((z+ep*ep*b*pow(sin(th),3)), (p-e*e*a*pow(cos(th),3)))
     n = a/sqrt(1-e*e*pow(sin(lat),2))
     alt = p/cos(lat)-n
     lat = (lat*180)/pi
     lon = (lon*180)/pi
     print "%s %s %s" % (lat, lon, alt)

def displayUsage(parser):
     parser.print_help()
     print "\nOutput: Latitude Longtitude Altitude"
     return

if '__main__' == __name__:
     main()
