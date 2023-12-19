# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 09:41:56 2023

@author: David
"""
class LightBeam:
    def __init__(self, x, y, p):
        self.dX=x
        self.dY=y
        self.history=[p]
    
   
def PartB(filename):
   
    
    plan = open(filename).readlines()
    for i in range(len(plan)):
        plan[i]=plan[i].strip()



   
    maxX = len(plan)
    maxY= len(plan [0])
    startpos=[]
    for i in range (maxX):
        startpos.append(LightBeam(0, 1, (i,-1)))
        startpos.append(LightBeam(0,-1, (i,maxY)))
    
    for i in range (maxY):
        startpos.append(LightBeam(1, 0, (-1,i)))
        startpos.append(LightBeam(-1, 0, (maxX,i)))

    maxE=0
    for p in startpos:
        e = RunSim(plan , p)
        print ("We have " + str(e))
        if e > maxE:
            maxE =e
            
    print("MaxE = "+ str(maxE))

def PartA(filename):
   
    
    plan = open(filename).readlines()
    for i in range(len(plan)):
        plan[i]=plan[i].strip()

    e = RunSim(plan , LightBeam(0,1, (0,-1)))

    print ("We have " + str(e))

def RunSim (plan, start):
    splitpoints=set()
    maxX = len(plan)
    maxY= len(plan [0])
    maxBeamLen = maxX*maxY    
    beams = [start]
    #for i in range (maxX):
    #    beams.append(LightBeam(0, 1, (i,-1)))
    #    beams.append(LightBeam(0, -1, (i,maxY)))
    #for i in range (maxY):
    #    beams.append(LightBeam(1, 0, (-1,i)))
    #    beams.append(LightBeam(-1, 0, (maxX,i)))
    
    i=0
    while i < len(beams):
        beam = beams[i]        
        nextposX = beam.dX+beam.history[-1][0]
        nextposY = beam.dY+beam.history[-1][1]
        
        
        if nextposX < 0 or nextposX >= maxX:
            i=i+1
            continue
        
        if nextposY < 0 or nextposY >= maxY:
            i=i+1
            continue
        
        #print("Attempting to move to " +plan [nextposX][nextposY])
        
        if (len(beam.history) > maxBeamLen):
            i=i+1
            continue
            
        
        beam.history.append((nextposX,nextposY))
        if plan[nextposX][nextposY] ==  '.':
            continue
        
        ##SPLIT
        if plan[nextposX][nextposY] ==  '|':
            if beam.dY !=0:
                beam.dX=1
                beam.dY=0
                start = (nextposX,nextposY)
                if not splitpoints.__contains__(start):
                    newBeam = LightBeam(-1,0,start)
                    beams.append(newBeam)
                    splitpoints.add(start)
            
            
        if plan[nextposX][nextposY] ==  '-':
            if beam.dX !=0:
                
                beam.dX=0
                beam.dY=1
                start = (nextposX,nextposY)
                if not splitpoints.__contains__(start):
                    newBeam = LightBeam(0,-1,start)
                    splitpoints.add(start)                                        
                    beams.append(newBeam)
         
        #reflection   
        if plan[nextposX][nextposY] ==  '/':
            t = beam.dX
            beam.dX = beam.dY *-1
            beam.dY =t  *-1
            
            
            
        if plan[nextposX][nextposY] ==  '\\':           
           t = beam.dX
           beam.dX = beam.dY 
           beam.dY =t  
                

    coll = set()
    for beam in beams:
        for point in beam.history:
            if point[0] < maxX and point[0] >= 0:
                if point[1] < maxY and point[1] >= 0:
                    coll.add (point)
   
    return len(coll)
    #for i in range(maxX) :
    #    s=''
    #    for j in range(maxY):               
    #        if coll.__contains__((i,j)):
    #            s=s + '#'
    #        else:
    #            s=s + '.'

     #   print(s)
        
    #print ("we have this many points " + str(len(coll)))
    
PartB("input.txt")