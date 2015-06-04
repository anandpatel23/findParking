#!/usr/bin/env python
#
# Anand Patel
# CS 265 - Section 002
# findParking.py
# Obtains the closest parking spaces to the user's LAT & LONG
import sys
import urllib2
import csv
import philly_loc
import math
from heapq import nsmallest
from optparse import OptionParser

def cols(row):
    """only the important columns"""
    return [row['LAT'], row['LNG'], row['MAT'], row['SPACES']]

def euclidean(lat, lng):
    """ euclidean measure dsitance function given LAT & LNG """
    return math.sqrt(math.pow(lat,2) + math.pow(lng,2))

""" random position [lat, long] """
pos = philly_loc.getLoc()
posLat = float(pos[0])
posLng = float(pos[1])

# determine listSize
listSize = 20

# csv to be read
URL = 'https://raw.githubusercontent.com/CityOfPhiladelphia/ParksDept-geodata/264f2d579ad2662a135893b03c29d13435a74254/Parking%20Areas%20point/Parking_Areas_point.csv'

# open and read csv
response = urllib2.urlopen(URL)
reader = csv.DictReader(response)

# create list for csv
entries = []
for row in reader:
    entries.append(cols(row))

for i in entries:
    # if empty, change to 0
    if i[3] == ' ':
        i[3] = 0
    # change lat and long strings to floating numbers
    i[0] = float(i[0])
    i[1] = float(i[1])
    float(i[3])

# add distance to end of each entry
for i in entries:
    i.append(euclidean(i[0], i[1]))
    float(i[4])
    float(i[3])

# distances of each entry
distances = []
for i in entries:
    distances.append(i[4])

# calculating user's position
userPos =  math.sqrt(math.pow(posLat,2)+math.pow(posLng,2))

# find 20 closest distances using heapq.nsmallest()
# makes a single pass over the data, keeping no more than the n best
# values in memory at any time
closestDists = nsmallest(listSize, distances, key=lambda num: abs(num-userPos))

# tallying closest distances
finalList = []
for i in entries:
    for c in closestDists:
        if i[4] == c:
            finalList.append(i)
            break

# sort in descending order
finalList = sorted(finalList, reverse=True)

# output closest spaces
print "LAT", "LONG", "TYPE", "SPACES"
for i in finalList:
    print i[0], i[1], i[2], i[3]
