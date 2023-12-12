# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:21:41 2023

@author: chano
"""

class Point:
    def __init__(self,x_coord = 0.0,y_coord = 0.0):
        self.x = x_coord
        self.y = y_coord
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self,new_x):
        self.x = new_x
    
    def setY(self,new_y):
        self.y = new_y
    
    def __str__(self):
        s = "("+ str(self.x) + "," + str(self.y) +")"
        return s
    
    def equals(self, point2):
        is_equal = False
        if (self.x == point2.x and self.y == point2.y):
            is_equal = True
        return is_equal
    
p1 = Point()
p2 = Point(1,2)

print(p1, p2)

print(p1.equals(p2))

p2.setX(p1.getX())
p2.setY(p1.getY())

print(p1.equals(p2))

p2.setX(p1.getX() + 1) 
print(p1.equals(p2))





