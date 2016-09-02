__author__ = 'daokh'
from iso3166 import countries

country = countries.get('us')

print country[0]

countryCoord = []
with open("countrylatlon.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    countryAbbre,lat,lon = line.split("\t")
    lon = lon.strip()
    try:
        c = countries.get(countryAbbre)
        if c:
            countryFull = c[0]
        else:
            countryFull = countryAbbre
    except KeyError:
        countryFull = countryAbbre
    item = {"countryFull": countryFull, "countryAbbre": countryAbbre, "lat":float(lat), "lon":float(lon)}
    countryCoord.append(item)
    print


print