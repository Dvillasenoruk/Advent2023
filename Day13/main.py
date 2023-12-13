# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 07:45:54 2023

@author: David
"""
def TestVRef(puzzle, i):
    
    l=i
    r=i+1
    maxR = len(puzzle[0])
    maxJ = len(puzzle)
    diffCount  = 0
    if r >= maxR:
        return -1
    
    while (l>=0 and r < maxR):
        for j in range(maxJ):
            if puzzle[j][l] != puzzle[j][r]:
                diffCount  = diffCount  + 1
            
        l = l - 1
        r = r + 1
    
    return diffCount 


def TestHRef(puzzle, i):
    
    t=i
    b=i+1
    maxB = len(puzzle)
    maxV = len(puzzle [0])
    diffCount =0
    
    if b >= maxB:
        return -1
    
    while (t>=0 and b < maxB):
        for j in range(maxV):
            if puzzle[t][j] != puzzle[b][j]:
                diffCount = diffCount  +1
        
        t = t - 1
        b = b + 1
    
    
    return diffCount 

def ScorePuzzle (puzzle, target):
    hRef = 0
    vRef = 0
    for l in puzzle:
        print (l)
    
    for i in range(len(puzzle[0])):
        if (TestVRef(puzzle, i)==target):
            vRef = i +1
            
    for i in range(len(puzzle)):
        if (TestHRef(puzzle, i)==target):
            hRef = i +1
            
    print ("Found H reflections " + str(hRef))
    print ("Found V reflections " + str(vRef))

    return hRef*100 + vRef   


def RunPartA(filename):
    puzzle =[]
    running_total =0
    
    
    for line in open(filename):
        cur_line = line.strip()
        if cur_line !='':
            puzzle.append(cur_line)
            continue
        
        if puzzle == []:
            continue
        
        
        # we have a puzzle to find 
      
        running_total = running_total + ScorePuzzle(puzzle,1)
        puzzle = []

    if puzzle != [] :
        running_total = running_total + ScorePuzzle(puzzle,1)

        
    print ("Total is " + str(running_total))





RunPartA("input.txt")