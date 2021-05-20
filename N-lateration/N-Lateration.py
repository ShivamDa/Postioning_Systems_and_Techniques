# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:36:44 2021

@author: Shiv
"""

from math import sqrt
from numpy import arange
import datetime

# Class Location
class Location():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def toString(self):
        return "(" + str(self.x) + " ; " + str(self.y) + " ; " + str(self.z) + ")"

    def distanceTo(self, loc):
        return sqrt(pow(self.x - loc.x, 2) + pow(self.y - loc.y, 2) + pow(self.z - loc.z,2))

# N-Lateration Algorithm
def NLateration(data, step=.1, xSize=0.0, ySize=0.0, zSize=0.0, md=.0,\
                dmax=10):
    minLoc = Location()
    minDist = 0.0
    for k in data:
        minDist += abs(k[0].distanceTo(Location()) - k[1])
        xSize = k[0].x if k[0].x > xSize  else xSize
        ySize = k[0].y if k[0].y > ySize  else ySize
        zSize = k[0].z if k[0].z > zSize  else zSize
    for k in arange(0,xSize,step):
        for l in arange(0,ySize,step):
            for m in arange(0,zSize,step):
                d = .0
                for n in data:
                    d += abs(n[0].distanceTo(Location(k,l,m)) - n[1])
                if d < minDist:
                    minDist = d
                    minLoc = Location(round(k,2),round(l,2),round(m,2))
            
                    
    return (minLoc, minDist)


# Use dataset for 4 AP's in 3D space.
dataset = [(Location(.5,.5,.5), 3.0), (Location(4.0,.0,.0), 2.0), (Location(4.0,5.0,5.0), 4.2), (Location(3.0,3.0,3.0), 2.5)]
# Use dataset1 for 3 AP's in 2D space.
dataset1 = [(Location(.5,.5,.5), 3.0), (Location(4.0,.0,.0), 2.0), (Location(4.0,5.0,5.0), 4.2)]

# Get Location of Mobile Terminal
start = datetime.datetime.now()
result = NLateration(dataset, step=.1)
print("\r\nLocation : " + result[0].toString())
end = datetime.datetime.now()
print (end-start)