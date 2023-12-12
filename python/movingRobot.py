# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:29:20 2023

@author: chano
"""


print('robot_move function:')
def robot_move(moves):
    x = 0
    y = 0
    for t in moves:
        if t[0]=='N':
            for i in range(t[1]):
                y += 1
        if t[0]=='S':
            for i in range(t[1]):
                y -= 1
        if t[0]=='E':
            for i in range(t[1]):
                x += 1
        if t[0]=='W':
            for i in range(t[1]):
                x -= 1
    return (x,y)

print(robot_move([('N',2), ('E',4), ('S',1), ('W',3)]))

print('robot_move2 function:')
def robot_move2(moves,x,y):
    for t in moves:
        if t[0]=='N':
            for i in range(t[1]):
                y += 1
        if t[0]=='S':
            for i in range(t[1]):
                y -= 1
        if t[0]=='E':
            for i in range(t[1]):
                x += 1
        if t[0]=='W':
            for i in range(t[1]):
                x -= 1
    return (x,y)

print(robot_move2([('N',2), ('E',4), ('S',1), ('W',3)],1,1))

#part 3 of activity

def robot_move3(moves,x_start,y_start):
    x = x_start
    y = y_start
    x_list = [x_start]
    y_list = [y_start]
    move_mat = [['1']]
    for t in moves:
        if t[0]=='N':
            for i in range(t[1]):
                y += 1
            y_list.append(y)
        if t[0]=='S':
            for i in range(t[1]):
                y -= 1
            y_list.append(y)
        if t[0]=='E':
            for i in range(t[1]):
                x += 1
            x_list.append(x)
        if t[0]=='W':
            for i in range(t[1]):
                x -= 1
            x_list.append(x)
    mat_width = x_list.max - x_list.min
    mat_height = y_list.max - y_list.min
    x_startposition = x_list.min - x_start
    y_startposition = y_list.min - y_start
    str = []
    position_num = 1
    for i in range(mat_width):
        for j in range(mat_height):
            str[i][j] = str()
    return (x,y)


#part 4 of activity

def freq(seq, fragments):
    occ = {}
    tot_length = len(seq)
    for e in fragments:
        frag_length = len(e)
        f = 0
        occ[e] = 0
        while f <= (tot_length - frag_length):
            if e in seq[f:f+frag_length]:
                occ[e] +=1
                print(e,f,seq[f:f+frag_length])
            f += 1
    return occ

dna = 'AAAECGTAECGTCECGGCTGTAGTA'
frags = ['A','AAA','CGT','GTC','ATC','CTG','AEC','AEG','GTA','TA'] #['AAA','CTG','ECG', 'GTA']
print(freq(dna, frags))
