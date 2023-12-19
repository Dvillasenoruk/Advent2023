# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:43:50 2023

@author: David
"""
def Stringify( a):
    s=''
    for e in a :
        s=s+str(e)
    return s


def FloodFillNoNRecurse (mymap, xpos, ypos, maxX, maxY):
    poi = [(xpos,ypos)]
    
    while len (poi) > 0: 
        p = poi.pop(0)
        if mymap[p[0]][p[1]] != '.' :
            continue
        
        mymap[p[0]][p[1]] = 'X'
        routes = [(p[0]-1,p[1]),
                  (p[0]+1,p[1]),
                  (p[0], p[1]-1),
                  (p[0], p[1]+1)]

        for r in routes:
            if r[0] >=0 and r[0] < maxX:
                if r[1] >=0 and r[1] < maxY:
                    poi.append(r)

def FloodFill(plan, x, y):
    mx = len(plan)
    my = len(plan[0])
    FloodFillNoNRecurse(plan, x,y,mx,my)
        
def PartA(filename):
    
    moves = []
    cx=0
    cy=0
    mx=0
    my=0
    nx =0
    ny =0
    for line in open(filename):
        parts = line.strip().split(' ')
        move = [parts[0], int(parts[1])]
        if move[0] == 'U':
            cx= cx- move[1]
        if move[0] == 'D':
            cx= cx+ move[1]
        if move[0] == 'R':
            cy= cy+ move[1]
        if move[0] == 'L':
            cy= cy- move[1]
        moves.append(move)  
        nx = min(nx,cx)
        ny = min(ny,cy)
        mx=max(mx,cx)
        my=max(my,cy)
    
    mx = mx+1 +(-1* nx)
    my= my+1+(-1* ny)
    plan = []
    print ("We have a grid "+str(mx)+" X " +str (my))
    for x in range(mx):
        plan.append([])
        for y in range(my):
            plan[x].append('.')
    
    cx=nx *-1
    cy=ny *-1
    dx=0
    dy=0
    plan[cx][cy]='#'
    for m in moves:        
        if m[0] == 'U':
            dx=-1
            dy=0
        if m[0] == 'D':
            dx=1
            dy=0
        if m[0] == 'R':
            dx=0
            dy=1
        if m[0] == 'L':
            dx=0
            dy=-1
            
        #print("Applying move " + Stringify(m))
        for i in range(m[1]):
            cx=cx+dx
            cy=cy+dy
            plan[cx][cy]='#'
    
    for l in plan:
        print(Stringify(l))
       
    for x in range(mx):
        FloodFill(plan, x,0)
        FloodFill(plan, x,my-1)

    for y in range (my):
        FloodFill(plan,0, y) 
        FloodFill(plan ,  mx-1, y)
        
    poolsize =0
    for x in range(mx):
        for y in range(my):
            if plan[x][y] !='X':
                poolsize = poolsize +1
                
                
    for l in plan:
        print(Stringify(l))
         
    print ("Lava pool size is " +str( poolsize ))
    
def ScanHex(s):
    r=0
    for c in s[2:]:
        r=r*16
        if c.isdigit():
            r=r+int(c)
        else:
            r= ord(c)-ord('a')+10 +r
            
    return r

def PartB(filename):
    moves = []
    cx=0
    cy=0
    mx=0
    my=0
    nx =0
    ny =0
    for line in open(filename):
        parts = line.strip().split(' ')
        
        move = [parts[2][-2:-1], int(ScanHex(parts[2][:-2]))]
        if move[0] == '3':
            move[0]='U'
            cx= cx- move[1]
        if move[0] == '1':
            move[0]='D'
            cx= cx+ move[1]
        if move[0] == '0':
            move[0] = 'R'
            cy= cy+ move[1]
        if move[0] == '2':
            move[0]='L'
            cy= cy- move[1]
        moves.append(move)  
        nx = min(nx,cx)
        ny = min(ny,cy)
        mx=max(mx,cx)
        my=max(my,cy)
     
    mx = mx+1 +(-1* nx)
    my= my+1+(-1* ny)    
    print ("We have a grid "+str(mx)+" X " +str (my))

PartB("input.txt")