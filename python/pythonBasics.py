# CS 5007 - Homework 1 template
# tpetit@wpi.edu

'''
 Please read the PDF for the questions.
 Once you completed a question, run the module to test.
'''

# ----------
# QUESTION 1
# ----------
# Do not modify the three following statements:
a = True
b = False
c = True

# Write your code below: 
#   be1: (write expression in place of the zero in the next line)
be1 = a and (b or (not c))

#   be2: (write expression in place of the zero in the next line)
be2 = (not b) or (a and c)

#   be3: (write expression in place of the zero in the next line)
be3 = (a and b) or (not (b and c))

#   be4: (write expression in place of the zero in the next line)
be4 = (not a) or ((not b) or (not c))

print(be1,be2,be3,be4)


# ----------
# QUESTION 2
# ----------
# Do not modify the three following statements:
a = 4.0
b = 4.0
c = 2.0

# Write your code below:
#   e1: (write expression in place of the zero in the next line)
e1 = (4*a*b)+(b*c)

#   e2: (write expression in place of the zero in the next line)
e2 = b**4

#   e3: (write expression in place of the zero in the next line)
e3 = (a*b)**(0.5)

#   e4: (write expression in place of the zero in the next line)
e4 = ((a*c)-(b*a))/(b*c)

#   e5: (write expression in place of the zero in the next line)
e5 = (a**2)-(c**4)+(2*a*b)

print(e1,e2,e3,e4,e5)

# ----------
# QUESTION 3
# ----------

# Write your code below
print("\n Results of Problem 3")

x = 15 
y = 3 
z = x//y
t = x//3.0
print(x,y,z,t)
print(str(x)+"\n"+str(y)+"\n"+str(z)+"\n"+str(t))
n1 = "Marie"
n2 = "Paul"
print(n1,"\t",x)
print(n2,"\t",y*3)






# ----------
# QUESTION 4
# ----------

# Write your code below
print("\n Results of Problem 4")

def form(s):
    ls = len(s)
    if ls!=16:
        print("Invalid credit card number")
    else:
        print(s[0:4],s[4:8],s[8:12],s[12:16])
        
        
form("1234")
form("4976539812341234")









# ----------
# QUESTION 5
# ----------

# Write your code below

def WindChill(t,v):
    wc = 13.13+(0.528*t)-(12.1*(v**(0.15)))+(0.3967*t*(v**(0.155)))
    return wc

T = -20
V = 30
print("Windchill is", WindChill(T, V))







