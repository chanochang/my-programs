import math
import random

## PART 1

class SinusExpr:
    def __init__(self,expr):
        self.expr = expr
    def value(self,v):
        return math.sin(self.expr.value(v))
    def derivate(self):
        return BinaryExpr(self.expr.derivate(),
                                '*',
                                CosinusExpr(self.expr))
    def __str__(self):
        return 'sin('+self.expr.__str__()+')'

class CosinusExpr:
    def __init__(self,expr):
        self.expr = expr
    def value(self,v):
        return math.cos(self.expr.value(v))
    def derivate(self):
        return BinaryExpr(BinaryExpr(ConstantExpr(0), '-', self.expr.derivate()),
                                '*',
                                SinusExpr(self.expr))
    
    
    def __str__(self):
        return 'cos('+self.expr.__str__()+')'

class ConstantExpr():
    def __init__(self,constant):
        self.constant = constant
    def value(self,v):
        return self.constant
    def derivate(self):
        return ConstantExpr(0)
    def __str__(self):
        return str(self.constant)

class VariableExpr:
    # No constructor
    def value(self,v):
        return v
    def derivate(self):
        return ConstantExpr(1)
    def __str__(self):
        return 'x'

class BinaryExpr:
    def __init__(self,exprL, operator, exprR):
        self.exprL = exprL
        self.operator = operator
        self.exprR = exprR
    def value(self,v):
        valLeft = (self.exprL.value(v))
        valRight = (self.exprR.value(v))
        if self.operator == '+':
            return valLeft + valRight        
        if self.operator == '-':
            return valLeft - valRight        
        if self.operator == '*':
            return valLeft * valRight    
        if self.operator == '/':
            return valLeft / valRight
    def derivate(self):
        derLeft = self.exprL.derivate()
        derRight = self.exprR.derivate()
        if self.operator == '+':
            return BinaryExpr(derLeft, '+', derRight)      
        if self.operator == '-':
            return BinaryExpr(derLeft, '-', derRight)         
        if self.operator == '*':
            return BinaryExpr(BinaryExpr(derLeft ,'*', self.exprR), '+', BinaryExpr(self.exprL, '*', derRight))
        if self.operator == '/':
            return BinaryExpr(BinaryExpr(BinaryExpr(derLeft ,'*', self.exprR), '-', BinaryExpr(self.exprL, '*', derRight)), '/', BinaryExpr(self.exprR, '*', self.exprR))
        # '(' + derLeft + '*' + self.exprR + '+' + self.exprL + '*' + derRight +')/(' + self.exprR + ')**2'
    def __str__(self):
        return self.exprL.__str__() + self.operator + self.exprR.__str__() 

f1 = BinaryExpr(VariableExpr(),'-',ConstantExpr(2))
f2 = BinaryExpr(VariableExpr(),'*',VariableExpr())
g = BinaryExpr(CosinusExpr(f1),'/',
                     BinaryExpr(ConstantExpr(4),'-',f2))

print(f2)
print(f2.derivate())
print(f2.value(2))
print(g)
print(g.derivate())
print(g.value(3))

## PART 2

def newton(expression, x0, precision, maxIt):
    tries = 0
    x1 = x0 + 1 + precision
    precDiff = x1 - x0
    while (tries < maxIt) and (abs( precDiff ) >= precision):
            fX0 = expression.value(x0)
            fPrime = expression.derivate() 
            fPrimeX0 = fPrime.value(x0)
            x1 = x0 -  (fX0 / fPrimeX0)
            precDiff = abs(x1 - x0)
            if (precDiff >= precision):
                x0 = x1
            tries += 1
    try:
        return x1
    except:
        return None
    
def solve(expression, x0, precision, maxIt):
    tries = 0
    res = None
    while tries < 100 and res == None:
        res = newton(expression, x0, precision, maxIt)
        if res < precision:
            break
        x0 = random.randrange(-100,100)
        tries += 1
    try:
        return float(res)
    except:
        print('No convergence')

f1 = BinaryExpr(VariableExpr(),'+',ConstantExpr(2))
print('Solution to '+ f1.__str__() +' = 0:')
r = solve(f1,10.0,0.000001,10000)
print(r)
f2 = BinaryExpr(VariableExpr(),'-',ConstantExpr(3))
f3 = BinaryExpr(VariableExpr(),'*',f2)
h1 = BinaryExpr(f1,'-',f3)
print('Solution to '+ h1.__str__() +' = 0:')
r = solve(h1,10.0,0.000001,10000)
print(r)

# If you have finished, think about how expressions
# could be simplified to avoid that the __str__ method
# displays parts of expressions like 0*(...) or 1*(...)
# or (0 + ...) or (... - 0).
# How could you do this formally?
