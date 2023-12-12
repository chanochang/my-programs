# Problem 1
print("\n\nProblem 1 \n\n")

def NDflatten(m):
    flattendList = []

    for e in range(len(m)):
        if not(type(m[e]) == list):
            flattendList.append(m[e])
        else:
            flattendList += NDflatten(m[e])
            
    return flattendList

    
x = [ [1,2,[1,2,3]], ['a',['a',['b','c'],'d'],'e'], ['x','y','z'] ]
# x = []
# x = [[],[]]
# x = [[1,2,3],[4,5,6]]
# x =[1,2,3,4]
# x = [{'a':[1,2],'b':[1,2,3]},{}]
print(NDflatten(x))


# Problem 2
print("\n\nProblem 2 \n\n")

class House:
    def __init__(self, p,s,c):
        self.price = p
        self.sqft = s
        self.city = c
        
    def unitPrice(self):
        unPr = round(self.price/self.sqft)
        return unPr
        
    def __str__(self):
        s = str(self.price)+ "\n" + str(self.sqft) + "\n" + self.city 
        return s
        
        
h1 = House(240000, 1400, 'Philadelphia')
print(h1)
print(h1.unitPrice())
    
h2 = House(160000, 1000, 'New York')

dico = {} 
dico['Paul'] = h1
dico['Mary'] = h2
print(dico['Mary'])

# Problem 3
print("\n\nProblem 3 \n\n")

def displayUnit(d):
    lengthDict = len(d) 
    for e in d:
        uPrStr = str((dico[e].unitPrice()))
        print("Unit price of " + e + "'s house: " , uPrStr)
        
        
displayUnit(dico)