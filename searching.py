#-------------------------------------------------------------------------------
# Name:        searching.py
# Purpose:
#
# Author:      Emman & Posh & Marshall
#
# Created:     12/09/2018
# Copyright:   (c) Emman 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import timeit
import time

def sequentialfn(dList, dItem):
    '''Set up a random experiment to test the difference between a sequential
    search and a binary search on a list of integers.'''

    pos = 0
    while pos < len(dList) and True:
        if dItem == dList[pos]:
            return True
        else:
            pos += 1
    return False


dList = [1, 2, 3, 4, 5, 3]
dItem = int(input('Input the number you want to search in Sequential Search: '))
print(sequentialfn(dList, dItem))
thetime = timeit.Timer('sequentialfn(dList, dItem)', 'from __main__ import sequentialfn, dList, dItem')
print('Sequential Search Time: ', thetime.timeit(), 'milliseconds')


def binaryfn(randomlist, dItem):
    if len(randomlist) <= 1:
        return False
    else:
        middleList = len(randomlist) // 2
        if dItem == randomlist[middleList]:
            return True
        else:
            if dItem < randomlist[middleList]:
                return binaryfn(randomlist[:middleList], dItem)
            else:

                return binaryfn(randomlist[middleList + 1:], dItem)


randomlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
dItem = int(input('\nInput the number you want to search in Binary Search: '))
print(binaryfn(randomlist, dItem))
time_binaryTime = timeit.Timer('binaryfn(randomlist, dItem)', 'from __main__ import binaryfn, randomlist, dItem')
print('Binary Search Time: ', time_binaryTime.timeit())



