# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:13:41 2023

@author: David
"""

def ArrayIze(s):
    a = []
    for  c in s :
        a.append(c)
    return a

def PartA(filename):
    
    table = []
    for line in open(filename):
        table.append(ArrayIze(line.strip()))
       
        
    print("Before : ")
    for r in table:
        print (r)
    
        
    # move all North
    movedSomething = True
    while movedSomething:
        movedSomething = False
        for x in range(1,len(table)):
            for y in range (len(table[0])):
                if table[x][y]=='O':
                    if table[x-1][y]=='.':
                        table[x-1][y] = 'O'
                        table[x][y]='.'
                        movedSomething = True
                        
  
    print("after : ")
    for r in table:
        print (r)
                        
  
    #score everything
    runningScore =0
    scoreOffset = len(table)
    for x in range(scoreOffset):
        for y in range(len(table[0])):
            if table[x][y] =='O':
                runningScore = runningScore + (scoreOffset -x)


    print ("Running total is " + str(runningScore))            
    
    
PartA("input.txt")