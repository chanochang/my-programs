# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:37:45 2023

@author: chano
"""

class Counter:
    
    def __init__(self , x = 0):
        if (x<0):
            self.__val = 0
        else:
            self.__val = x
    
    def increment(self):
        self.__val +=1
        
    def setCounterValZero(self):
        self.__val = 0
        
    def __str__(self):
        return str(self.__val)


def testCounter():
    test1 = Counter()
    test2 = Counter(350)
    print(test1)
    print(test2)
    test1.increment()
    test2.increment()
    test1.increment()
    test2.increment()
    print(test1)
    print(test2)
    
# testCounter()
        

class BCounter(Counter):
    
    def __init__(self , y = 1 , x = 0):
        Counter.__init__(self, x = 0)
        if (y<1):
            self.ub = 1
        else:
            self.ub = y
        # print(self.__val)
        if (x >= self.ub):
            print('Warning, value set at or above upper bound, value set to 0')
            Counter.setCounterValZero(self)
            
    def increment(self):
        Counter.increment(self)
        # print(int(Counter.__str__(self)))
        if (int(Counter.__str__(self)) == self.ub):
            Counter.setCounterValZero(self)
        # if Counter.increment(self) == self.ub:
            # Counter.setCounterValZero(self)

    
    def __str__(self):
        return Counter.__str__(self) + ' ' + str(self.ub)

def testBCounter():
    test1 = BCounter(2)
    test2 = BCounter(2,350)
    print("test1 = ", test1)
    print("test2 = " , test2)
    test1.increment()
    test2.increment()
    print("test1 = ", test1)
    print("test2 = " , test2)
    test2.increment()
    # print("test1 = ", test1)
    print("test2 = " , test2)
        
testBCounter()