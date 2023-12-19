# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 08:30:49 2023

@author: David
"""
UNCHARTED = 99999999

def  FindPath(curPoint,endpoint, lines, mhl, delta, moves, history):
    if history.__contains__(curPoint):
        return
    
    if moves <=0 :
        return
    
    if curPoint[0]<0 or curPoint[0] >endpoint[0]:
        return
    
    if curPoint[1]<0 or curPoint[1] >endpoint[1]:
        return
    
    if curPoint==endpoint:
       mhl[curPoint[0]][curPoint[1]] = int(lines[curPoint[0]][curPoint[1]] )
       return mhl[curPoint[0]][curPoint[1]]
    
    
    
    
    history.add(curPoint)
    
    if mhl[curPoint[0]][curPoint[1]] != UNCHARTED:
        return mhl[curPoint[0]][curPoint[1]]
    
    print("Trying to score " + str(curPoint))
    
    deltas=[(0,1),(0,-1), (1,0),(-1,0)]
    
    maxR = mhl[curPoint[0]][curPoint[1]]
  
    for d in deltas:
        newPoint= (curPoint[0]+ d[0], curPoint[1]+d[1])
        rm =3
        if d==delta:
            rm= moves -1
        r= FindPath(newPoint,endpoint, lines, mhl, d, rm, history)
        if r is not None and (maxR > r):
            maxR =r
            
    history.remove(curPoint)
    rVal =  maxR + int(lines[curPoint[0]][curPoint[1]] )
    if moves == 3:
        mhl[curPoint[0]][curPoint[1]] = rVal
    return rVal
    
    
def PartA(filename):
    
    lines = open(filename).readlines()
    
    mhl=[]
    for l in lines:
        ml=[]
        for c in l.strip():
            ml.append(UNCHARTED)
        mhl.append(ml)
        
    maxX = len(mhl)
    maxY = len(mhl[0])
    
    #mhl[maxX-1][maxY-1]= int (lines[maxX-1][maxY-1])
    
    FindPath((0,0),(maxX-1,maxY-1), lines, mhl, (0,1),3 ,set())
    
    for sub in mhl:
        print(sub)

PartA("test.txt")