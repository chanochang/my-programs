# -*- coding: utf-8 -*-
"""



a = True
b = False 
c = ((4*8)-4) <27
print ("a" ,a,"b",b,"c",c)
print ("a %s b %s c %s" % (a, b, c))
be = (not c) or (a and b)
print ("be %s" % (be))
"""

def isLeapYear(year):
    if year%400 == 0:
        return True
    elif (not (year%100 == 0)) and (year%4 == 0):
        return True
    else:
        return False
    
print ("---------------")
print (isLeapYear(2021))
print (isLeapYear(2020))
print (isLeapYear(1900))
print (isLeapYear(2000))

def numberOfDays(month, year):
    if month != 2:
        if month == (9 or 4 or 6 or 11 ):
            return 30
        else:
            return 31
    elif isLeapYear(year):
        return 29
    else:
        return 28
     
        
print ("---------------")
print (numberOfDays(5,2021))  
print (numberOfDays(2,2021))    
print (numberOfDays(2,2024))      


def nextDay(year,month, day):
    if day < numberOfDays(month, year):
        day+= 1
    elif (numberOfDays(month, year) == day) and (month == 12):
        year+= 1
        month = 1
        day = 1
    elif numberOfDays(month, year) == day:
       month+= 1 
       day = 1

    print ("---------------")
    print("[%d-%d-%d]" % (year , month, day))
   

nextDay(2021,5,14)
nextDay(2021,2,28)    
nextDay(2024,2,29)
nextDay(2023,12,31)
nextDay(2023,11,16)
nextDay(1986,4,24)

