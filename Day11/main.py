# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:28:23 2023

@author: David
"""
def Stringify(seq):
    r=''
    for s in seq:
        r=r+s
        
    return r

def Run11B(filename,   expansionConstant ):
    universe=[]
    newRows =[]
    x=0
    for line in open(filename):
        universe.append(line.strip())
        if line.__contains__('#') == False:
            newRows.append(x)
            print ("New Row added at "+str(x))
        
        x=x+1

    newCols=[]
    for y in range (len(universe[0])):
        hasGal =False
        for x in range(len(universe)):
            if universe[x][y] == '#':
               hasGal = True
               break
           
        if not hasGal:
            newCols.append(y)
            print ("New Col added at "+str(y))



    galaxyPoints = []

    for x in range(len(universe)):
        for y in range (len(universe[0])):
            if universe[x][y]=='#':    
                galaxyPoints.append ((x,y))
                
    #expand galaxy 
  
    newGalaxyPoints=[]
    for g  in galaxyPoints:
        eRO=0
        for eR in newRows:
            if g[0] > eR:
                eRO=eRO+expansionConstant
                
        
         
        eCO= 0
        for eC in newCols:
            if g[1] > eC:
                eCO=eCO+expansionConstant
                
        newGalaxyPoints.append((g[0]+eRO, g[1]+eCO))
    
    for g in galaxyPoints:
        print("Old galaxy location " + str(g))    
    
    for g in newGalaxyPoints:
        print("New galaxy location " + str(g))    
    
    galaxyPoints = newGalaxyPoints
    sum_of_distances=0
    for i in range(len(galaxyPoints)):
        for j in range (i+1, len(galaxyPoints)):
            
            difx = abs(galaxyPoints[j][0] - galaxyPoints[i][0])
            dify = abs(galaxyPoints[j][1] - galaxyPoints[i][1])
            distance =   difx+ dify
            sum_of_distances= sum_of_distances + distance
            print ("Distance between galaxies " +str(i+1) +" and "+str(j+1)+ " is " + str(distance)+ " sum  "+ str(sum_of_distances))
            

                
                
    print ("sum of shortest distance is " + str(sum_of_distances))
    
                

def Run11A(filename):
    universe=[]
    for line in open(filename):
        universe.append(line.strip())
        if line.__contains__('#') == False:
            universe.append(line.strip())
  
    newCols=[]
    for y in range (len(universe[0])):
        hasGal =False
        for x in range(len(universe)):
            if universe[x][y] == '#':
               hasGal = True
               break
           
        if not hasGal:
            newCols.append(y)
    
    newCols.append(len(universe[0]))        
        
    for x in range(len(universe)):
        print(universe[x])
        
    newUniverse= []
    
    for x in range(len(universe)):
        newline =[]
        lastcol=0
        for newCol in newCols:
            for i in range (lastcol, newCol):
                newline.append (universe[x][i])
            newline.append('.')
            lastcol = newCol
        newUniverse.append(Stringify(newline)) 
        
    universe = newUniverse
    sum_of_distances=0
    
    galaxyPoints = []
    
    for x in range(len(universe)):
        for y in range (len(universe[0])):
            if universe[x][y]=='#':    
                galaxyPoints.append ((x,y))
                print ("Galaxy Location " + str((x,y)))
    
    for x in range(len(universe)):
        print(universe[x])
    
    
    for i in range(len(galaxyPoints)):
        for j in range (i+1, len(galaxyPoints)):
            
            
            difx = abs(galaxyPoints[j][0] - galaxyPoints[i][0])
            dify = abs(galaxyPoints[j][1] - galaxyPoints[i][1])
            distance =   difx+ dify
            sum_of_distances= sum_of_distances + distance
            print ("Distance between galaxies " +str(i+1) +" and "+str(j+1)+ " is " + str(distance)+ " sum  "+ str(sum_of_distances))
            

                
                
    print ("sum of shortest distance is " + str(sum_of_distances))
    
    
    
#Run11A("Test.txt")
Run11B("input.txt",999999)