# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 15:15:56 2021

@author: 11357
"""

from math import sqrt
from numpy import arange
import datetime
from operator import itemgetter as ig

class Location():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, loc2):
        return bool(self.x == loc2.x and self.y == loc2.y and self.z == loc2.z)
        
    def __mul__(self, multiplier):
        returnValue = Location(self.x, self.y, self.z)
        returnValue.x *= multiplier
        returnValue.y *= multiplier
        returnValue.z *= multiplier
        return returnValue

    def __rmul__(self, multiplier):
        return self * multiplier

    def __add__(self, added):
        returnValue = Location(self.x, self.y, self.z)
        returnValue.x += added.x
        returnValue.y += added.y
        returnValue.z += added.z
        return returnValue

    def __isub__(self, value):
        return self + -1 * value

    def __itruediv__(self, divider):
        returnValue = Location(self.x, self.y, self.z)
        returnValue.x /= divider
        returnValue.y /= divider
        returnValue.z /= divider
        return returnValue

    def toString(self):
        return "(" + str(self.x) + " ; " + str(self.y) + " ; " + str(self.z) + ")"

    def distanceTo(self, loc):
        return sqrt(pow(self.x - loc.x, 2) + pow(self.y - loc.y, 2) + pow(self.z - loc.z,2))

class RSSVector():
    distances = []
    def __init__(self, n1, n2, n3, n4):
        '''
        :param n1: AP1 RSSI
        :param n2: AP2 RSSI
        :param n3: AP3 RSSI
        :param n4: AP4 RSSI
        '''
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
    
    def __eq__(self, v2):
        return True if v2.n1 == self.n1 and  v2.n2 == self.n2 \
        and  v2.n3 == self.n3 and  v2.n4 == self.n4 else False
        
class Cell():
    def __init__(self, v_, loc):
        '''
        :param v_: RSSI vector of the fingerprint
        :param loc: Location of the fingerprint
        '''
        self.v = v_
        self.location = loc

def NLateration(data, step=.1, xSize=0.0, ySize=0.0, zSize=0.0, md=.0, dmax=10):
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

def newCell(n1, n2, n3, n4, l1, l2):
    return Cell(RSSVector(n1,n2,n3,n4), Location(l1,l2))

def KNeighbors(fingerprints, sample):
    distances = []
    for row in fingerprints:
        for currentItem in row:
            dist = abs(currentItem.v.n1 - sample.n1) \
                 + abs(currentItem.v.n2 - sample.n2) \
                 + abs(currentItem.v.n3 - sample.n3) \
                 + abs(currentItem.v.n4 - sample.n4)
            distances.append((dist, currentItem))
    distances = sorted(distances, key=ig(0))
    sample.distances = [x[0] for x in distances][:4]
    return [x[1] for x in distances][:4]



def solve_center(nC, d):
    return None if len(nC) != 4 or len(d) != 4 else  \
          1 / (1+d[0]/d[1]+d[0]/d[2]+d[0]/d[3])*nC[0].location \
        + 1 / (1+d[1]/d[0]+d[1]/d[2]+d[1]/d[3])*nC[1].location \
        + 1 / (1+d[2]/d[1]+d[2]/d[0]+d[2]/d[3])*nC[2].location \
        + 1 / (1+d[3]/d[1]+d[3]/d[2]+d[3]/d[0])*nC[3].location


# ------------------------------------------main--------------------------------------------
dataset = [(Location(.5,.5,.5), 3.0), (Location(4.0,.0,.0), 2.0), (Location(4.0,5.0,5.0), 4.2), (Location(3.0,3.0,3.0), 2.5)]
dataset1 = [(Location(.5,.5,.5), 3.0), (Location(4.0,.0,.0), 2.0), (Location(4.0,5.0,5.0), 4.2)]
Tf = []
# cells of fingerprint
Tf = [[newCell(-38,-27,-54,-13,2,2),newCell(-74,-62,-48,-33,6,2),newCell(-13,-28,-12,-40,10,2) ],\
      [newCell(-34,-27,-38,-41,2,6), newCell(-64,-48,-72,-35,6,6), newCell(-45,-37,-20,-15,10,6)], \
      [newCell(-17,-50,-44,-33,2,10), newCell(-27,-28,-32,-45,6,10), newCell(-30,-20,-60,-40,10,10)]]
MoblieCell = RSSVector(-26, -42, -13, -46)
# N-Lateration 
start = datetime.datetime.now()
result = NLateration(dataset1, step=.1)
print("\r\nLocation : " + result[0].toString())
end = datetime.datetime.now()
# print (end-start)
# K-Neighbours 

print("\nK-neighbors of Terminal Mobile : ")
neighborsCells = KNeighbors(Tf, MoblieCell)
for k in neighborsCells:
    print("(", k.location.x, ";", k.location.y, ")")

# Result Calculated
print("\r\nResult ax the localization estimate :")
center = solve_center(neighborsCells, MoblieCell.distances)
print(center.toString())
print (end-start)