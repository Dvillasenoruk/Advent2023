
MaxColours= {'red':12,
             'green':13,
             'blue':14}

def IsPossible(game):
    rounds = game.split(';')
    for rnd in rounds:
        drawclrs = rnd.split(',')
        for sel in drawclrs:
            elements = sel.strip().split(' ')
            c = int(elements[0])
            if  c > MaxColours[elements[1]]:
                return False

    return True
        
def Run2A(f):
    runningTotal = 0
    for line in open(f):
        header = line.strip().split(':')
        if IsPossible(header[1]):
            print(header[0]+" is possible")
            runningTotal = runningTotal + int(header[0][5:])
        else:
            print(header[0]+" is NOT possible")
            
    print ("Sum of all games = " + str(runningTotal))
    
     
def CalcMinPower(game):
    mins = {'red':0,'green':0,'blue':0}
    rounds = game.split(';')
    for rnd in rounds:
        drawclrs = rnd.split(',')
        for sel in drawclrs:
            elements = sel.strip().split(' ')
            c = int(elements[0])
            if  c > mins[elements[1]]:
                mins[elements[1]] = c

    rv = 1
    for a in mins:
        rv = mins[a]*rv
        
    return rv;
    
def Run2B(f):
    runningTotal = 0
    for line in open(f):
        header = line.strip().split(':')
        power = CalcMinPower(header[1])
        runningTotal = runningTotal + power
        print(header[0]+" is has power " + str(power))
            
    print ("Sum of all powers = " + str(runningTotal))
    
    
Run2A("test.txt")
Run2A("input.txt")
Run2B("test.txt")
Run2B("input.txt")