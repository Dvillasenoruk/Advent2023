
def IsSym(c):
    return c!='.' and c.isdigit()==False

def CheckForSymbol(data,x,y):
    start_x = x-1
    if start_x < 0:
        start_x =0
    end_x= x+1
    if end_x >= len(data):
        end_x=x
        
    start_y= y-1
    end_y = y+1
    
    if end_y >= len(data[x].strip()):
        end_y = y
        
    if start_y < 0 :
        start_y = 0
        
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            if (IsSym(data[i][j])):
                return True
            
    return False


        
def Run3A(f):
    runningTotal = 0
    data = []
    for line in open(f):
        data.append(line)
        
    for i in range (0,len(data)):
        has_symbol = False
        buildnum =''
        linetotal=0
        for j in range(0,len(data[i])):
            if data[i][j].isdigit():    
                has_symbol = has_symbol or CheckForSymbol(data,i,j)
                buildnum= buildnum + (data[i][j])
            else:
                if buildnum != '':
                    if has_symbol :
                        runningTotal = runningTotal + int(buildnum)   
                        linetotal = linetotal + int(buildnum)
                    
                has_symbol = False
                buildnum =''
                        
        if buildnum != ''  and has_symbol :
             runningTotal = runningTotal + int(buildnum)
             linetotal= linetotal + MyInt(buildnum)

                        
    print("Running Total is " + str(runningTotal))
def Contains(s, e):
    for i in s:
        if i == e:
            return True
    
    return False

def Clip (n, mini, maxi):
    if n > maxi :
        return maxi
    if n< mini:
        return mini
    return n

Offsets =[[-1,-1],[-1,0],[-1,1], 
          [0,-1],[0,1],
          [1,-1],[1,0],[1,1]]
          
def NumberAt(plan, pos):
    x=pos[0]
    y=pos[1]
    return_value = ''
    while (plan[x][y].isdigit()):
        return_value=return_value+ plan[x][y]
        y = y + 1
    
    return int(return_value)
        
        
def FindStart (plan, x,y):
    firstdigit = y
    print("finding digits in " +plan[x] + "where x is " + str(x) +"and Y is "+ str(y))
    for i in range (0, y+1):
        if plan[x][i].isdigit():
            if firstdigit == y:
                firstdigit = i
        else:
            firstdigit = y
            
    print("Start is now " + str(firstdigit))
    return [x,firstdigit]

def CheckForGear(plan, x,y):
    if plan[x][y]!='*' :
        return 0
    # ok so plan [x][y] == *
    print ("Gear Found at [" +str(x)+","+str(y)+"]")
    startPos= []
    for offset in Offsets:
        newX = Clip (x+offset[0], 0, len(plan))
        newY = Clip (y+offset[1], 0, len(plan[0]))
        if plan[newX][newY].isdigit():
            print ("Founding start of [" +str(newX)+","+str(newY)+"]")
            
            start = FindStart(plan, newX, newY)
            if not Contains(startPos, start):
                print ("ratio Found at [" +str(start[0])+","+str(start[1])+"]") 
                startPos.append(start)
            
    if len(startPos)==2:
        return NumberAt(plan,startPos[0])*NumberAt(plan,startPos[1])
    return 0


def Run3B(filename):
    runningTotal = 0
    data = []
    for line in open(filename):
        data.append(line)
     
    for i in range (0,len(data)):
        for j in range (0,len(data[i])):
            runningTotal = runningTotal + CheckForGear(data, i,j)

 
    print("running total is " + str(runningTotal))

#Run3A("input.txt")
Run3B("input.txt")


