# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:56:46 2023

@author: chano
"""
                
class Node():
    def __init__(self, left , value, right):
        self.left = left
        self.value = value
        self.right = right     
    
    def countNodes(self):
        numNodes = 1
        if(self.left != None):
            numNodes += self.left.countNodes()
        # numNodes += 1
        if(self.right != None):
            numNodes += self.right.countNodes()
        return numNodes
    
    def squareEach(self):
        if(self.left != None):
            self.left.squareEach()
        self.value = self.value**2
        if(self.right != None):
            self.right.squareEach()

# in the class Node
    def __str__(self):
        res = '['
        if(self.left != None):
            res += ' left :' + self.left.__str__()
        res += ' root :' + str(self.value)
        if(self.right != None):
            res += ' right:' + self.right.__str__()
        return res + ']'

class BinTree():
    def __init__(self, root = None):
        self.root = root

    def countNodes(self):
        numNodes = 0
        if(self.root != None):
            numNodes = self.root.countNodes()
        return numNodes
      
    def squareEach(self):
        if(self.root != None):
            self.root.squareEach()
            
   # in the class BinTree
    def __str__(self):
        if(self.root != None):
            return self.root.__str__()
        return 'Empty tree'

x1 = Node(None, 5, None)
x2 = Node(None, 6, None)
x3 = Node(x1, 4, None)
x4 = Node(x2, 9, x3)
x5 = Node(None, 7, None)
x6 = Node(x4, 15, x5)
tree = BinTree(x6)
print(tree)
tree2 = BinTree(x1)
print(tree2)
tree3 = BinTree()
print(tree3)
print(tree.countNodes())
print(tree2.countNodes())
print(tree3.countNodes())
tree.squareEach()
print(tree)