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
    if r > maxR:
        return False
    while (l>=0 and r < maxR):
        for j in range(maxJ):
            if puzzle[j][l] != puzzle[j][r]:
                return False
            
        l = l - 1
        r = r + 1
    
    return True


def TestHRef(puzzle, i):
    
    t=i
    b=i+1
    maxB = len(puzzle)
    maxV = len(puzzle [0])
    
    
    if (b >= maxB):
        return False
    
    while (t>=0 and b < maxB):
        for j in range(maxV):
            if puzzle[t][j] != puzzle[b][j]:
                return False
        
        t = t - 1
        b = b + 1
    
    
    return True




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
        hRef = 0
        vRef = 0
        for l in puzzle:
            print (l)
        
        for i in range(len(puzzle)-1):
            if (TestVRef(puzzle, i)):
                vRef = i +1
                
        for i in range(len(puzzle[0])-1):
            if (TestHRef(puzzle, i)):
                hRef = i +1
                
        print ("Found H reflections " + str(hRef))
        print ("Found V reflections " + str(vRef))

        running_total = running_total + hRef * 100 + vRef   
        puzzle =[]
        
    print ("Total is " + str(running_total))





RunPartA("input.txt")