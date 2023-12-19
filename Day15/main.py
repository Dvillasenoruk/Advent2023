# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 08:38:01 2023

@author: David
"""

def GetHash(s):
    h =0
    for c in s:
        h=h + ord(c)
        h=h*17
        h=h % 256
        
    return h

def RunA():
    #inp = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')
    inp =  open("input.txt").readline()
    parts=inp.strip().split(',')
    
    total =0
    for p in parts:
        h = GetHash(p)
        total = total + h
        print ("for " + p + "I got a hash of " + str(h))
        
    print("total is " + str(total))
    
    
def PrintHashMap(hashmap):
    for i in range(len(hashmap)):
        lj = len(hashmap[i])
        if lj ==0:
            continue
        
        s= "Box " + str(i) + ": "
        for j in range(lj):
            s=s+'['+hashmap[i][j][0]+','+str(hashmap[i][j][1])+'] '
            
        print(s)
    
def RunPartB():
    hashmap = []
    for i in range(256):
        hashmap.append([])
        
        
    parts=open("input.txt").readline().strip().split(',')  
    
    #parts= "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')
    
    
    
    for p in parts:
        if p[-1]== '-':
            k=p[:-1]
            h = GetHash(k)
            tbr=None
            for e in hashmap[h]:
                if e[0] ==k :
                    tbr=e
            
            if tbr!=None:
                hashmap[h].remove(tbr)
                print("Removed " + tbr[0])
                
        if p.__contains__('='):
            kvp = p.split('=')
            found = False       
            h= GetHash(kvp[0])
            for e in hashmap[h]:
                if e[0] ==kvp[0] :
                    e[1] = int(kvp[1])
                    found = True
                    print ("Updated " + kvp[0] + "  to "+ kvp[1])
            
            if not found:
                hashmap[h].append ([kvp[0], int(kvp[1])])
                print ("Adding " + kvp[0] + " "+ kvp[1])
            
       # PrintHashMap(hashmap)
                                           
    total =0                                        
    for i in range(256):
        for j in range(len(hashmap[i])):
            a = (i+1)* (j+1)* hashmap[i][j][1] 
            total = total + a
    
    print ("My Total is " + str(total))
        
RunPartB()