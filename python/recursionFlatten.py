# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:11:40 2023

@author: chano
"""


def flatten(m):
    flattendList = []
    for e in range(len(m)):
        for f in range(len(m[e])):
            flattendList.append(m[e][f]) 
    return flattendList




mat = [[1,2,3],['a','b','c'],[1,'c',4]]
print(flatten(mat))

def clean1(aList):
    cleanedList = []
    for element in aList:
        if not element in cleanedList:
            cleanedList.append(element)
    return cleanedList

al = [1,2,3,4,4,4,5,1,2,1,5]
newlist = clean1(al)
print(al)
print(newlist)



def clean2(aList):
    n = len(aList)
    for element in aList:
        n = len(aList)
        for oElement in range(1,n):
            if  element == oElement:
                aList.pop(oElement)


al = [1,2,3,4,4,4,5,1,2,1,5]
print(al)
clean2(al)
print(al)
