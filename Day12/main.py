# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 07:19:24 2023

@author: David

"""

def Stringify(a):
    s=''
    for e in a:
        s=s+e
    
    return s


def CountVar(aPattern, nPattern, depth):
    
    #check compliance of a v n
    curGroup=0
    foundGroups=[]
    for i  in range(depth):
        if aPattern[i]=='#':
            curGroup = curGroup + 1
        if aPattern[i]=='.':
            if (curGroup> 0):
                foundGroups.append(curGroup)
                curGroup=0
                
                
                
    
    
    if (curGroup> 0):
        foundGroups.append(curGroup)
        curGroup=0   

    if len(foundGroups) > len(nPattern):
        return 0         
    
    tooSmall = False
    for i in range (len(foundGroups)):
        if tooSmall :
            return 0
        if foundGroups[i] > nPattern[i]:
            return 0
        if foundGroups[i] < nPattern[i]:
            tooSmall = True
        
        
    
    # we are valid
    if depth ==len(aPattern):
        if tooSmall:
            return 0
        if len(foundGroups) != len(nPattern):
            return 0
        
        return 1 # valid combo

    if aPattern[depth]=='?':
        aPattern[depth]= '.'
        c = CountVar(aPattern, nPattern, depth+1)
        aPattern[depth]= '#'
        c = c+ CountVar(aPattern, nPattern, depth+1)
        aPattern[depth]='?'
        return c
    
    return CountVar(aPattern, nPattern, depth+1)
        
def ArrayOfStr (s):
    a=[]
    for c in s:
        a.append(c)
        
    return a

def FiveOf (org):
    r = []
    for x in range(5):
        for e in org:
            r.append(e)
            
    return r

def RunA12B (filename):
    lines = open(filename).readlines()

    running_total =0
    for line in lines:
        print ("Processing line " + line)
        notations = line.strip().split(' ')
        damagedPattern = notations[1].split(',')
        numPattern=[]
        for d in damagedPattern:
            numPattern.append(int(d))
        variations = CountVar(FiveOf(ArrayOfStr(notations[0])),FiveOf(numPattern), 0)
        print ("I have found " + str(variations))
        running_total= running_total + variations
        
    print ("I have found a total of " + str(running_total))


def RunA12a (filename):
    lines = open(filename).readlines()

    running_total =0
    for line in lines:
        print ("Processing line " + line)
        notations = line.strip().split(' ')
        damagedPattern = notations[1].split(',')
        numPattern=[]
        for d in damagedPattern:
            numPattern.append(int(d))
        variations = CountVar(ArrayOfStr(notations[0]),numPattern, 0)
        print ("I have found " + str(variations))
        running_total= running_total + variations
        
    print ("I have found a total of " + str(running_total))
    
RunA12B("test2.txt")
