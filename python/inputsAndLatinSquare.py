# CS 5007 HW2 template


# ---
# Taylor Sinus
# Write your code below

print("Results of Problem 1 \n")

import math
def taylor(x,n):
    sum = 0
    for e in range(n):
        sum += ((-1)**((e+1)+1))*(x**((2*(e+1))-1))/math.factorial(((2*(e+1))-1))
    return sum

x = math.pi/2
print(math.sin(x))
print(taylor(x, 7)) 
print('\n')

 









# ---
# Input

print("Results of Problem 2 part 1\n")

def enterAGrade():
    st = input('Please enter a grade in [0,100]\n')
    grade = int(st)
    print('The grade is',grade,'\n')

enterAGrade()

print("Results of Problem 2 part 2\n")

def enterSomeGrades():
    aList = []
    st = input('Please enter a grade in [0,100]\n')
    aList.append(int(st))
    st = input('continue y or n?\n')
    while st == 'y':
        st = input('Please enter a grade in [0,100]\n')
        aList.append(int(st))
        st = input('continue y or n?\n')
    print(aList,'\n')

enterSomeGrades()




# ---
# Latin square

# Write the row function below and test it

def row(start, n):
    st = list(range(start, n))
    if start != 0:
        st += list(range(0, start))
    return st
 
print("Results of Problem 3 part 1\n")

print(row(0,7))
print(row(3,7))
print('\n')





# Write the latinSquare function below and test it with n equal to 7

print("Results of Problem 3 part 2\n")

n = 7
for e in range(n):
    print(row(e, n))
print('\n')








# Write the rowL function below and test it

def rowL(start, aList):
    st = []
    laList = len(aList)
    if start == 0:
        st = aList
    else:
        for e in range(start, laList):
            st += aList[e]
        for e in range(0, start):
            st += aList[e]
    return st
 
print("Results of Problem 3 part 3\n")

print(rowL(0,['a','b','c','d','e','f','g']))
print(rowL(3,['a','b','c','d','e','f','g']))
print('\n')






# Write the latinSquare function below and test it with
# the following list: ['a','b','c','d','e','f','g']


print("Results of Problem 3 part 4\n")

theList = ['a','b','c','d','e','f','g']
for e in range(len(theList)):
    print(rowL(e, theList))
    

