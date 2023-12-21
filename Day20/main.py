# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:00:12 2023

@author: David
"""
class FlipFlop:
    def __init__(self, name, nodes):
        self.name=name
        self.nodes=nodes
        self.state =0
        self.NextPulse=0
        self.rPulses =[]
        
    def __str__ (self):
        return self.name+" : "+ str(self.nodes)
    
    def CountLow(self):
        if self.rPulses[0]==0:
            return 1
        return 0
    
    def CountHigh(self):
        if self.rPulses[0]==0:
            return 1
        return 0
        
    def Process (self):
        if len(self.rPulses) ==0:
            print ("BROKEN "+str(self))
        first =self.rPulses[0]
        self.rPulses=[]
        
        if first==1 :
            return False
        if self.state ==0:
           self.state =1
           self.NextPulse =1
        else:
           self.state =0
           self.NextPulse =0
           
        return True
    
class DudNode:
    
    def __init__(self):
        self.nodes=[]
        self.rPulses=[]
        
    def Process (self):
        return False

    def CountLow(self):
        return 0
    def CountHigh(self):
        return 0
    
class Conjunction:
        def __init__(self, name, nodes):
            self.name=name
            self.nodes=nodes
            self.prevPulse =0
            self.NextPulse=0
            self.rPulses=[]
            
        def CountLow(self):
            c=0
            for e in self.rPulses:
                if e==0:
                    c=c+1
            return c
        
        def CountHigh(self):
            c=0
            for e in self.rPulses:
                if e==1:
                    c=c+1
            return c
        
        def Process (self):
              allhigh = True
              for p in self.rPulses:
                  allhigh = allhigh and p!=0
                  
              if allhigh:
                  self.NextPulse = 0
              else:
                  self.NextPulse = 1
            
              self.rPulses=[]
              return True


def CreateFlipFlop (l):
    arrowPos = l.find('->')
    name = l[1:arrowPos].strip()
    nodes = []
    for n in l[arrowPos+2:].split(','):
        nodes.append(n.strip())
    
    return FlipFlop(name, nodes)

def CreateConj(l):
    arrowPos = l.find('->')
    name = l[1:arrowPos].strip()
    nodes = []
    for n in l[arrowPos+2:].split(','):
        nodes.append(n.strip())
    
    return Conjunction(name, nodes)

def RunA(filename):
    broadcasts=[]
    nodes = {"output":DudNode(), "rx":DudNode()}
    
    for line in open(filename):
        if line.__contains__('broadcaster ->'):
            for n in line[14:].strip().split(','):
                broadcasts.append(n.strip())
                
        if line[0]=='%':
            n= CreateFlipFlop(line)
            nodes[n.name]=n
        if line [0]=='&' :
            n= CreateConj(line)
            nodes[n.name]=n
        
    cH=0
    cL=0        
    for i in range(1000):
        for n in nodes:
            nodes[n].rPulses=[]
        
        withPulse=[]
        for n in broadcasts:
            nodes[n].rPulses = [0]
            if nodes[n].Process():
                withPulse.append(nodes[n])
                

        
        cL=cL+len(broadcasts)+1
        while len(withPulse)>0:
            nextNodes =set()
            for node in withPulse:
                for nn in node.nodes:
                    nodes[nn].rPulses.append(node.NextPulse)
                    nextNodes.add(nodes[nn])
                                        
            withPulse=[] 
            for n in nextNodes:
                cL = cL + n.CountLow()
                cH = cH + n.CountHigh()
                if n.Process():
                    withPulse.append(n)
                    
    print ("WE have this many low pulses " + str(cL))
    print ("WE have this many high pulses " + str(cH))
    print ("The magic number is "+str(cL*cH))
            
                
        
            
            
                
            
        
            
        
            




RunA("test2.py")