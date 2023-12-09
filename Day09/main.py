# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:11:01 2023

@author: David
"""

def AreAllEqual(s):
    for i in range(1, len(s)):
        if s[0] != s[i]:
            return False
        
    return True

def PredictNext(s):
    sub_seq = []
    for i in range (0, len(s) -1):
        sub_seq.append (s[i+1]-s[i])
        
    if AreAllEqual(sub_seq):
        return sub_seq[0]

    return sub_seq[-1]+ PredictNext(sub_seq)     


def PredictPrev(s):
    sub_seq = []
    for i in range (0, len(s) -1):
        sub_seq.append (s[i+1]-s[i])
        
    if AreAllEqual(sub_seq):
        return sub_seq[0]

    return sub_seq[0]- PredictPrev(sub_seq)     
    
    
    
    
def Run9B(filename):
     runningTotal = 0
     for line in open(filename):
         seq = line.strip().split(' ')
         num_seq= []
         for n in seq:
             num_seq.append(int(n))
             
             
         pred = num_seq[0] - PredictPrev(num_seq)
         print("for "+str(num_seq)+ " i got "+ str(pred))
         runningTotal = runningTotal + pred
         
     print("Running total is " + str(runningTotal))
     
    
def Run9A(filename):
     runningTotal = 0
     for line in open(filename):
         seq = line.strip().split(' ')
         num_seq= []
         for n in seq:
             num_seq.append(int(n))
             
             
         pred = PredictNext(num_seq)+num_seq[-1]
         print("for "+str(num_seq)+ " i got "+ str(pred))
         runningTotal = runningTotal + pred
         
     print("Running total is " + str(runningTotal))



#Run9A("input.txt")             
Run9B("input.txt")             