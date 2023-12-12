# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:46:16 2023

@author: chano
"""
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from('0123456')
edges = [('0','1'), ('0','2'), ('0','3'), ('1','2'), ('1','4') , ('2','3'),
         ('3','4'),('3','5'),('5','6')]
G.add_edges_from(edges)
pos = nx.spring_layout(G)
names = ['0','1','2','3','4','5','6']
col = []
for i in range(len(names)):
    col.append('lightblue')
nx.draw_networkx(G, pos, node_color = col, node_size = 750, alpha = 1)
plt.show()
"""

import networkx as nx
import matplotlib.pyplot as plt
import pyvis.network as pyv

G = nx.read_edgelist("facebook_sample2.txt",
create_using = nx.Graph(),
nodetype=int)

nt = pyv.Network('700px', '900px', heading = "Week 11 graph")
nt.from_nx(G)
nt.barnes_hut(gravity=-1000)

neighbor_map = nt.get_adj_list()
for node in nt.nodes:
    node['value']=len(neighbor_map[node['id']])
    s = 'Node'+str(node['id'])
    s += '\ndegree='+str(len(neighbor_map[node['id']]))
    node['title']=s

nt.show("try2.html", notebook=False)
