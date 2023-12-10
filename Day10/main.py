# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 07:45:37 2023

@author: David
"""


def Visualise(l):
    ret=''
    for c in l:
        if c==0:
            ret=ret+('.')
        else:
            if c== -2:
                ret=ret+(' ')
            else:
                if c== -1:
                    ret=ret+('S')
                else: 
                    ret=ret+('|')
            
    return ret

def ArrToStr(a):
    s=''
    for i in a:
        s=s+i
        
    return s

def FindCompleteLoop(symMap ,steps):
    while True:
        prevPos = steps[-2]
        curPos = steps[-1]
        nextPos = curPos
         
      
        if (curPos[0] <0 ) or (curPos[0] >= len(symMap)) :
            return[]##out of bounds
        
        if (curPos[1] <0 ) or (curPos[1] >= len(symMap[0])) :
            return[]##out of bounds
        
        curSym = symMap[curPos[0]][curPos[1]]    
       
        if curSym =='.':
            return[] # no complete loop
        
        
        if curSym =='S':
            return steps
        
        if curSym == '|':
            if prevPos[0] < curPos[0]:
                nextPos = (curPos [0]+1, curPos[1])
            else:
                nextPos = (curPos [0]-1, curPos[1])
        
        if curSym == '-':
            if prevPos[1] < curPos[1]:
                nextPos = (curPos [0], curPos[1]+1)
            else:
                nextPos = (curPos [0], curPos[1]-1)
       
        if curSym == 'L':
            if prevPos[0] < curPos[0]:
                nextPos = (curPos [0], curPos[1]+1)
            else:
                nextPos = (curPos [0]-1, curPos[1])
                
        if curSym == 'J':
            if prevPos[0] < curPos[0]:
                nextPos = (curPos [0], curPos[1]-1)
            else:
                nextPos = (curPos [0]-1, curPos[1])
                
        if curSym == '7':
            if prevPos[0] > curPos[0]:
                nextPos = (curPos [0], curPos[1]-1)
            else:
                nextPos = (curPos [0]+1, curPos[1])
                
        if curSym == 'F':
            if prevPos[0] > curPos[0]:
                nextPos = (curPos [0], curPos[1]+1)
            else:
                nextPos = (curPos [0]+1, curPos[1])
    
       
        steps.append(nextPos)
  
def IsBoundInt (myMap , steps, maxX, maxY):
    sPos = steps[-1]
  
    routes = [(sPos[0]-1,sPos[1]),
            (sPos[0]+1,sPos[1]),
            (sPos[0], sPos[1]-1),
            (sPos[0], sPos[1]+1)]
    for r in routes:
        if r[0]<=0 or r[1]<=0 or r[0]>= maxX or r[1]>=maxY:
            return False
        
        if (myMap[r[0]][r[1]] ==0):
            if not steps.__contains__(r):
                steps.append(r)
                if IsBoundInt (myMap , steps, maxX, maxY):
                    steps.remove(r)
                else:
                    return False
    
    return True 
        
def ShoeLaceBound (mymap, xpos, ypos):
    c=0
    for i in range(0,ypos):
        if mymap[xpos][i]=='|':
            c=c+1
   
    return c%2==1 or c==0 
    
def IsBound (mymap, xpos, ypos):
    steps = [(xpos, ypos)]
    maxX = len(mymap)
    maxY = len(mymap[0])
    return IsBoundInt(mymap,steps, maxX, maxY)
    
def FloodFill (mymap, xpos, ypos, maxX, maxY):
    if (xpos <0) or xpos>=maxX:
        return 0
    
    if (ypos <0) or ypos>=maxY:
        return 0

    print((xpos,ypos)) 
    if mymap[xpos][ypos]!=0:
        return 0
    
    mymap[xpos][ypos] =  -2
    
    r=1
    r = r + FloodFill(mymap, xpos+1, ypos, maxX, maxY)
    r = r + FloodFill(mymap, xpos, ypos+1, maxX, maxY)
    r = r + FloodFill(mymap, xpos-1, ypos, maxX, maxY)
    r = r + FloodFill(mymap, xpos, ypos-1, maxX, maxY)
    
    return r

def FloodFillNoNRecurse (mymap, xpos, ypos, maxX, maxY):
    poi = [(xpos,ypos)]
    
    while len (poi) > 0: 
        p = poi.pop(0)
        if mymap[p[0]][p[1]] != '.' :
            continue
        
        mymap[p[0]][p[1]] = ' '
        routes = [(p[0]-1,p[1]),
                  (p[0]+1,p[1]),
                  (p[0], p[1]-1),
                  (p[0], p[1]+1)]
        #,
        #          (p[0]-1,p[1]-1),
        #          (p[0]+1,p[1]+1),
        #          (p[0]+1, p[1]-1),
        #          (p[0]-1, p[1]+1)]
        for r in routes:
            if r[0] >=0 and r[0] < maxX:
                if r[1] >=0 and r[1] < maxY:
                    poi.append(r)
            
TransMap={'F': '┌',
          'L': '└',
          '.':'.',
         'X':'X',
         'J':'┘',
         '7':'┐',
         '|':'|',
         '-':'-',
         'S':'S'}
def Trans(c):
    return TransMap[c]
    
def VisualiseSym(seq):
    r=''
    for s in seq:
        r=r+s
        
    return r


def hInter(c):
    return {'┌':'-',
              '└':'-',
              '.':'.',
             'X':'X',
             '┘':'.',
             '┐':'.',
             '|':'.',
             '-':'-',
             'S':'S'}[c]
def vInter(c):
    return {'┌':'|',
              '└':'.',
              '.':'.',
             'X':'X',
             '┘':'.',
             '┐':'|',
             '|':'|',
             '-':'.',
             'S':'S'}[c]

def DoubleMap(symMap):
    r = []
    for i in range(len(symMap)):
        p =[]
        q=[]
        
        for j in range(len(symMap[i])):
            p.append(symMap[i][j])
            p.append(hInter(symMap[i][j]))
            q.append(vInter(p[j*2]))
            q.append(vInter(p[j*2+1]))
        r.append(p)
        r.append(q)
        
    return r

def Run10B(filename):
    symMap = open(filename).readlines()
    stepsMap = []
    i=0
    sPos = (0,0)
    for line in symMap :
        stepsMap.append([])
        for j in range(0,len(line)):
            
            if line[j]=='S':
                sPos = (i,j)
           
            stepsMap[i].append(0)
                
        i=i+1
    
    routes = [(sPos[0]-1,sPos[1]),
              (sPos[0]+1,sPos[1]),
              (sPos[0], sPos[1]-1),
              (sPos[0], sPos[1]+1)]
    
    for rPos in routes:
        
        
        loop = FindCompleteLoop(symMap, [sPos, rPos])
        if (len(loop) >0):
            print ("Found COMPLETE loop")
            currentCount =0
            for c in loop[:-1]:
                if (currentCount < stepsMap[c[0]][c[1]] ) or (stepsMap[c[0]][c[1]] ==0):
                    stepsMap[c[0]][c[1]] = currentCount
                    
                currentCount = currentCount+1
                
            #break;
                

    stepsMap[sPos[0]][sPos[1]] = -1
   
    
    boundSquares=0
    newSymMap=[]
    for x  in range(len(stepsMap)):
        newSymMap.append([])        
        for y in range(len(stepsMap[x])):
            if stepsMap[x][y]==0:
                newSymMap[x].append('.')
            else:
                newSymMap[x].append(Trans(symMap[x][y]))
    
    for l in newSymMap:
        print(ArrToStr(l))
    
    doubleSymMap = DoubleMap(newSymMap)            
    maxX = len(doubleSymMap)
    maxY = len(doubleSymMap[0])
    for x  in range(0, maxX):
        FloodFillNoNRecurse(doubleSymMap,x,0, maxX, maxY)
        FloodFillNoNRecurse(doubleSymMap,x,maxY-1, maxX, maxY)
        
    for y  in range(0, maxY):
        FloodFillNoNRecurse(doubleSymMap,0,y, maxX, maxY)
        FloodFillNoNRecurse(doubleSymMap,maxX-1,y, maxX, maxY)

    for stepline in doubleSymMap:
        print (VisualiseSym(stepline))

    finalMap =[]
    for x  in range(0, len(doubleSymMap),2):
        l=[]
        for y in range (0, len(doubleSymMap[x]),2):
                            
            if doubleSymMap[x][y] == '.' :
                boundSquares = boundSquares +1
                doubleSymMap[x][y]='X'
                #if IsBound(stepsMap,x,y):
                #    boundSquares = boundSquares + FloorFill(stepsMap,x,y, maxX, maxY)
            l.append(doubleSymMap[x][y])
            
        finalMap.append(l)
        
    for l in finalMap:
        print(ArrToStr(l))
    
    
    print("number of bound squares = " +str(boundSquares))

        
def Run10A(filename):
    symMap = open(filename).readlines()
    stepsMap = []
    i=0
    sPos = (0,0)
    for line in symMap :
        stepsMap.append([])
        for j in range(0,len(line)):
            
            if line[j]=='S':
                sPos = (i,j)
           
            stepsMap[i].append(0)
                
        i=i+1
    
    routes = [(sPos[0]-1,sPos[1]),
              (sPos[0]+1,sPos[1]),
              (sPos[0], sPos[1]-1),
              (sPos[0], sPos[1]+1)]
    
    for rPos in routes:
        
        
        loop = FindCompleteLoop(symMap, [sPos, rPos])
        if (len(loop) >0):
            print ("Found COMPLETE loop")
            currentCount =0
            for c in loop[:-1]:
                if (currentCount < stepsMap[c[0]][c[1]] ) or (stepsMap[c[0]][c[1]] ==0):
                    stepsMap[c[0]][c[1]] = currentCount
                    
                currentCount = currentCount+1
                  

    maxSteps = 0
    for stepline in stepsMap:
        print (stepline)
        for s in stepline:
            if s > maxSteps:
                maxSteps =s
                
    print("Max steps is "+ str(maxSteps))

Run10B("input.txt")