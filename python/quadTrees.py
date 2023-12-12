class Node:
    def __init__(self,sw,nw,ne,se):
        self.sw = sw
        self.nw = nw
        self.ne = ne
        self.se = se
        self.color = -1
    def getColor(self):
        return self.color
    
    def replaceAll(self, x, y):
            
        
    def toString(self):
        res = '['+self.sw.toString()+self.nw.toString()
        res += self.ne.toString()+self.se.toString()+']'
        return res

class Leaf(Node):
    def __init__(self,color):
        Node.__init__(self,None,None,None,None)
        self.color = color
        
    def replaceAll(x,y):
        if self.color == x:
            self.color =y
    def toString(self):
        return str(self.color)

class QuadTree:
    def __init__(self, matrix):
        self.root = QuadTree.build(len(matrix),0,0,matrix)
    def isMonochromeNode(sw,nw,ne,se): 
        res = sw.getColor() != -1
        res = res and nw.getColor() != -1
        res = res and ne.getColor() != -1
        res = res and se.getColor() != -1
        res = res and (sw.getColor() == nw.getColor())
        res = res and (nw.getColor() == ne.getColor())
        res = res and (ne.getColor() == se.getColor())
        return res
    def build(size,i,j,matrix):
        if(size==1):
            return Leaf(matrix[i][j])
        t = size//2
        lsw = QuadTree.build(t, i+t, j, matrix)
        lnw = QuadTree.build(t, i, j, matrix)
        lne = QuadTree.build(t, i, j+t, matrix)
        lse = QuadTree.build(t, i+t, j+t, matrix)
        if QuadTree.isMonochromeNode(lsw,lnw,lne,lse):
            return Leaf(lsw.getColor())
        else:
            return Node(lsw,lnw,lne,lse)
        
    def replaceAll(self, x , y):
        if(self.root != None):
            self.root.replaceAll(x,y)
            
        
    def __str__(self):
        if(self.root!=None):
            return self.root.toString()

matrix =[[0,0,1,1,0,1,1,1],
         [0,0,1,1,1,0,1,1],
         [1,1,0,0,1,1,0,0],
         [1,1,0,0,1,1,0,0],
         [0,0,0,0,0,0,1,1],
         [0,0,0,0,0,0,1,1],
         [0,0,0,0,1,1,0,0],
         [0,0,0,0,1,1,0,0]]

quadt = QuadTree(matrix)
print(quadt)


