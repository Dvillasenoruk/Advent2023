# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:12:12 2023

@author: David
"""

def AddNumerics(l):
    alpha = str('')
    for c in l:
        if c >='0' and c <='9':
            alpha= alpha + c
             
    firstAndLast = alpha[0:1] + alpha[-1:]
    return int(firstAndLast)
        

ValidNums = {'zero': 0, 
             'one':1, 
             'two':2, 
             'three':3,
             'four':4, 
             'five':5, 
             'six':6, 
             'seven':7,
             'eight':8, 
             'nine':9}
 
def AlphaNumerics (line):
    sLine = str(line).lower()
    digits = []
    for i in range(0,len(sLine)):
        if sLine[i] >='0' and sLine[i] <='9':
            digits.append(int(sLine[i]))
        else:
            for candiate in ValidNums:
                if sLine [i:i+len(candiate)] == candiate:
                    digits.append(ValidNums[candiate])
                    break


    return (digits[0] *10)+ digits[-1]
    


runningTotal = 0

for line in open("input.txt"):
    lineTotal =  AlphaNumerics(line)
    runningTotal = runningTotal + lineTotal
 

print ("Finished total is " + str(runningTotal) )