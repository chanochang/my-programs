import pandas as pd
import random
import math
import networkx as nx
import matplotlib.pyplot as plt

class uscities:
    
    def __init__(self):        
        df = pd.read_csv("uscities.csv")
        self.cities = df.loc[:,["city", "lat","lng"]]
        self.numbCities = 5 # can change 5 to any number of cities
        self.randomCities = self.listOfCities()
        self.matrix = self.buildMatrix()       
        self.tour = self.greedyTSP()
        
    def listOfCities(self):
        random.seed(1986) # can change to any seed
        tourList = []
        for i in range(0,self.numbCities):
            randNum = random.randrange(0,30844)
            tourList.append(randNum)
        return tourList

    def buildMatrix(self):
        print('\nMatrix of Distances as a lists of list:\n')
        matrix = []
        for i in range(0,self.numbCities):
            row = []
            for j in range(0,self.numbCities):
                distBetween = 0
                if (self.randomCities[i] == self.randomCities[j]):
                    row.append(100000)
                    continue                
                distBetween = self.calcDistances(i,j)
                row.append(round((distBetween),1))
            print(row)
            matrix.append(row)
        return matrix    
    
    def exhibitMatrix(self):
        print('\nTable of distances:\n')
        strg = ''
        for i in range(0,self.numbCities):
            strg += '\t' + self.cities.at[self.randomCities[i], 'city'] +'\t'
        print('\t\t\t\t' + strg)
        for i in range(0,self.numbCities):
            print('\n')
            strg = ''
            strg += self.cities.at[self.randomCities[i], 'city']
            while len(strg) < 16:
                if len(strg) < 16:
                    strg += ' '
            strg += '\t'
            for j in range(0,self.numbCities):
                distBetween = 00.00
                if (self.randomCities[i] == self.randomCities[j]):
                    strg += str(round((distBetween), 2)) +'\t\t\t\t\t'
                    continue
                distBetween = self.calcDistances(i, j)
                strg += str(round((distBetween), 2)) +'\t\t\t'
            print(strg)
                        
    def calcDistances(self, i, j):   
        earthRadius = 6371000 
        lat1 = self.cities.at[self.randomCities[i], 'lat'] 
        long1 = self.cities.at[self.randomCities[i], 'lng'] 
        lat2 = self.cities.at[self.randomCities[j], 'lat'] 
        long2 = self.cities.at[self.randomCities[j], 'lng'] 
        # THIS FORMULA IS ATTAINED FROM 
        # https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128
        phi_1 = math.radians(lat1)
        phi_2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(long2 - long1)
        a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dist = earthRadius * c  / 1000
        # THIS FORMULA IS ATTAINED FROM 
        # https://www.omnicalculator.com/other/latitude-longitude-distance#the-haversine-formula-or-haversine-distance
        # a = math.sin((lat2 - lat1)/2)**2
        # b = math.cos(lat1)
        # c = math.cos(lat2)
        # d = math.sin((long2 - long1)/2)**2
        # dist = 2 * earthRadius * math.asin(math.sin((a+b*c*d)**0.5)) * rad2deg
        return dist

    def greedyTSP(self):
        visitedCities = [self.randomCities[0]]
        i = 0   
        while len(visitedCities) < self.numbCities:
            remainingCities = self.matrix[i]
            lowestDist = min(remainingCities)        
            indexLowest = remainingCities.index(lowestDist)
            if (self.randomCities[indexLowest] not in visitedCities):
                visitedCities.append(self.randomCities[indexLowest])
                i = indexLowest
            else:
                remainingCities[indexLowest] = 500000    
        visitedCities.append(self.randomCities[0]) 
        return visitedCities
     
    def createTourGraph(self):
        G = nx.Graph()
        G.add_nodes_from(self.randomCities)
        i = 0
        allEdges = []
        while i < (self.numbCities-1):   
            j = self.tour[i]
            k = self.tour[i+1]
            edge = (j,k)
            allEdges.append(edge)
            i +=1
        finalEdge = (self.tour[self.numbCities-1],self.tour[0])
        allEdges.append(finalEdge)
        G.add_edges_from(allEdges)
        pos=nx.spring_layout(G)
        col = []
        for i in range(len(self.randomCities)):
            col.append('green')
        nx.draw_networkx(G,pos,node_color=col,node_size= 1000,alpha=1)
        plt.show()

tsp = uscities()
tsp.createTourGraph()
tsp.exhibitMatrix()
'''

haversine distance formula

                        a              b      c              d
d = 2R × sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁ × cosθ₂ × sin²((φ₂ - φ₁)/2)
                 ])

where:

θ₁, φ₁ – First point latitude and longitude coordinates;
θ₂, φ₂ – Second point latitude and longitude coordinates;
R – Earth's radius (R = 6371 km); and
d – Distance between them along Earth's surface.
'''
