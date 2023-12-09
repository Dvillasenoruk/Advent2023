# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:03:27 2023

@author: David
"""
class LRPair:
    L=''
    R=''
    
def Run8B(filename):
    inst, *maps = open(filename).readlines()
    coOrds={}
    startPos=[]
    for m in maps:
        c=m.strip()
        if c=='' :
            continue

        parts = c.split('=')
        newPair = LRPair()
        newPair.L=parts[1][2:5]
        newPair.R=parts[1][7:10]
        k= parts[0].strip()
        coOrds[k] = newPair
        if (k[-1]=='A'):
            startPos.append(k)
     
    
    startPos= startPos[-3:]
    done = False
    counter =0
    while not done :
        for i in inst:
            if i =='L':
                for i in range(0,len(startPos)):
                    startPos[i]  = coOrds[startPos[i] ].L
               
                counter = counter +1
            else:
                if i =='R':
                    for i in range(0,len(startPos)):
                        startPos[i]  = coOrds[startPos[i] ].R
               
                    counter = counter +1
                else:
                   continue
            #print("move " + str (counter) + " " + str(startPos))
            done = True
            
            for  k in range(0,len(startPos)):
                if startPos[k][-1]== 'Z':
                    print ("Solved for column " +str(k)+ " in move " +str(counter))
                    
            for p in startPos:
                done = done and p[-1]== 'Z'
                
            
    print("found it in " + str(counter))

Stop = [18157, 14363, 16531, 12737, 19783,  19241]

def findLCF():
    for i  in range(3337, 1000000000):
        subject= i * Stop[0]
        zeroFactor  = True
        for s in Stop:
            zeroFactor = zeroFactor and ((subject%s)==0)
        
        if zeroFactor:
            return subject 
        

def Run8A(filename):
    inst, *maps = open(filename).readlines()
    coOrds={}
    startPos='AAA'
    finishPos='ZZZ'
    for m in maps:
        c=m.strip()
        if c=='' :
            continue

        parts = c.split('=')
        newPair = LRPair()
        newPair.L=parts[1][2:5]
        newPair.R=parts[1][7:10]
        coOrds[parts[0].strip()] = newPair
     
    
    done = False
    counter =0
    while not done :
        for i in inst:
            if i =='L':
                print("Move from " + startPos + " to "+coOrds[startPos].L)
                startPos = coOrds[startPos].L
                counter = counter +1
            if i =='R':
                print("Move from " + startPos + " to "+coOrds[startPos].R)
               
                startPos = coOrds[startPos].R
                counter = counter +1
            
            if startPos == finishPos:
                done = True
                break
            
    print("found it in " + str(counter))


import datetime
print(datetime.datetime.now())
print("Lowest common is " + str(findLCF())) 
print(datetime.datetime.now())

# Run8B("input.txt")

    
#Run8A("input.txt")
