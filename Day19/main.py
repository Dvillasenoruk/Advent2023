# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 07:05:58 2023

@author: David
"""
class WorkFlow:
    def __init__(self, _name , _rules,d):
        self.name= _name
        self.rules = _rules
        self.default =d
        
    def ProcessPart(self,p):
        for r in self.rules:
            res = r.ProcessPart(p)
            if (res!= None):
                return res
            
        return self.default

class WorkFlowRule:
    def __init__(self, l, op, n, r):
        self.letter=l
        self.operand = op
        self.quantity = int(n)
        self.result =r
        
    def ProcessPart (self, part):
        tv =0
        if self.letter =='x':
            tv = part.x
        if self.letter =='m':
            tv = part.m 
        if self.letter =='a':
            tv = part.a
        if self.letter =='s':
            tv = part.s
            
        if self.operand=='>':
            if tv > self.quantity:
                return self.result
        
        if self.operand=='<':
            if tv < self.quantity:
                return self.result

class MachinePart:
    def __init__(self ,_x,_m,_a,_s):
        self.x=_x
        self.m=_m
        self.a=_a
        self.s=_s
        
    def SumRatings(self):
        return self.x + self.m + self.a + self.s
    
def CreateWorkflow(l):
    rs =l.find('{')
    name = l[0:rs-1]
    rulestext =l[rs:-1].split(',')
    rules = []
    
    for t in rulestext[:-1]:
        l = t[0]
        rules.append(WorkFlowRule(t[0],t[1], t[2:t.find(':')], t[t.find(':')]))

    return WorkFlow(name, rules, rulestext[-1])

def CreatePart (l):
    s=l.strip () [1:-1].split(',')
    x = int(s[0][2:])
    m = int(s[1][2:])
    a = int(s[2][2:])
    s = int(s[3][2:])
    return MachinePart(x,m,a,s)


def PartA(filename):
    workflows ={}
    total =0
    firstFlow = None
    for line in open(filename):
        l = line.strip()
        if l!='':
            if line[0]=='{':
                #process part 
                p = CreatePart(l)
                res = firstFlow.ProcessPart(p)
                while res != 'A' and res!='R':
                    res = workflows[res].ProcessPart(p)
                
                if res =='A':
                    total = total + p.SumRatings()
            else:
                #add workflow
                nwf = CreateWorkflow(l)
                workflows.add(nwf.name, nwf)
                if firstFlow == None:
                    firstFlow= nwf
        
        

PartA("test.txt")
    
    
    
    