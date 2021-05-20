# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:15:21 2021

@author: shiva
"""

from Cell import MarkovModel
from random import random
from math import floor


def main():
        flag = False
        num_cell = 0
        print("No. of cells to process with?: \n")
        num_cell = int(input())
        MM = MarkovModel(num_cell + 1)
        
       
        print("Values: \n")
        MM.printValues()
        print("\nPercentage by Columns:\n")
        MM.printPercentagesRow()
        print("\nPercentage by Row:\n")
        MM.printPercentagesCol()
        
        while not flag:
            print("\n WHere are you now?")
            print(MM.previousCell)
            print("\n WHere you wanna go? Or If you wanna stop press 'Q or Press 'q'")
            num1 = input()
            if num1 == 'Q' or num1 == 'q':
                flag = True
            else:
                if num1.isdigit():
                    num1 = int(num1)
                    if(num1 <= num_cell and num1 >= 0):
                        MM.moveToCellID(num1)
                        print("Values: \n")
                        MM.printValues()
                        print("\nPercentage by Columns:\n")
                        MM.printPercentagesRow()
                        print("\nPercentage by Row:\n")
                        MM.printPercentagesCol()
                        print("\nMost Probably you came from: ")
                        print(MM.getMostLikely())
                        print("\nMost Probably you would go: ")
                        print(MM.getMostLikelycf())
                    else:
                        print("\nOut of range ... Try again")
                else:
                     print("\nWrong Format Input ... Try again")

if __name__ == '__main__':
        main()