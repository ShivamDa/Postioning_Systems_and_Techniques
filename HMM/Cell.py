# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:17:22 2021

@author: shiva
"""

from operator import itemgetter as ig
from math import floor, sqrt, ceil
from numpy import arange
import sys 


class MarkovValue():
    def __init__(self, nb=0, percentageCol=0.0, percentageRow = 0.0):
        self.nb = nb
        self.percentageCol = percentageCol
        self.percentageRow = percentageRow 

class MarkovModel():
    def __init__(self, num_cell):
        self.MarkovValues = [] 
        self.previousCell = 0
        self.num_cell = num_cell
        for i in range (0, self.num_cell):
            self.MarkovValues.append([])
            for _ in range (0, self.num_cell):
                self.MarkovValues[i].append(MarkovValue())
       # self.MarkovValues[10][0].nb = 1
       # self.MarkovValues[0][10].nb = 1

    def moveToCellID(self, nextCell):
        self.MarkovValues[nextCell][self.previousCell].nb += 1
        self.MarkovValues[self.num_cell-1][self.previousCell].nb += 1
        self.MarkovValues[nextCell][self.num_cell - 1].nb += 1        
        self.refreshPercentageCol(self.previousCell)
        self.refreshPercentageRow(self.previousCell)
        self.previousCell = nextCell
        

    def refreshPercentageCol(self, col):
       if  self.MarkovValues[self.num_cell -1][col].nb:
            for k in range(0,self.num_cell - 1):
                    self.MarkovValues[k][col].percentageCol = self.MarkovValues[k][col].nb / self.MarkovValues[self.num_cell - 1][col].nb
    
    def refreshPercentageRow(self, row):
       if  self.MarkovValues[row][self.num_cell - 1].nb:
            for j in range(0,self.num_cell -1):
                self.MarkovValues[row][j].percentageRow = self.MarkovValues[row][j].nb / self.MarkovValues[row][self.num_cell - 1].nb
    
            
    def printValues(self):
        for j in range(0,self.num_cell -1):
            print("\t\t ", j, end="")
        print("    Tot_row")
        for i in range (0, self.num_cell):
            if i == self.num_cell - 1:
                print("\n\n","Tot_col  ", end='')
            else:
                print("\n\n", i, end='\t\t  ')
            for k in range (0,self.num_cell):
                print(str(floor(self.MarkovValues[k][i].nb)), end='\t\t  ')
        print("")


    def printPercentagesCol(self):
        for j in range(0,self.num_cell - 1):
            print("\t  ", j, end="")
        for i in range (0, self.num_cell -1):
            print("\n", i, end='\t  ')
            for k in range (0,self.num_cell - 1):
                print(str(floor(self.MarkovValues[k][i].percentageCol * 100)), end='%\t  ')
        print("")

    def getMostLikely(self):
       
        return self.getMostLikelytoCell(self.previousCell)
    
    def getMostLikelycf(self):
       
        return self.getMostLikelyFromCell(self.previousCell)
    
    
    
    def printPercentagesRow(self):
        for j in range(0,self.num_cell -1):
            print("\t  ", j, end="")
        for i in range (0, self.num_cell -1):
            print("\n", i, end='\t  ')
            for k in range (0,self.num_cell -1):
                print(str(floor(self.MarkovValues[k][i].percentageRow * 100)), end='%\t  ')
        print("")
    
    
    def getMostLikelytoCell(self, currentCell):
        max_value=0
        max_id=0
        for k in range(1,self.num_cell -1):
            if self.MarkovValues[currentCell][k].nb > max_value:
                max_value = self.MarkovValues[currentCell][k].nb
                max_id = k
        return max_id
    
    def getMostLikelyFromCell(self, currentCell):
        max_value=0
        max_id=0
        for k in range(1,self.num_cell -1):
            if self.MarkovValues[k][currentCell].nb > max_value:
                max_value = self.MarkovValues[k][currentCell].nb
                max_id = k
        return max_id

    def path(self, locationIDs):
        for loc in locationIDs:
            self.moveToCellID(loc)
 