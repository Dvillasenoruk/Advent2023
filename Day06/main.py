
def ReadArray (l):
    r=[]
    for c in l.strip().split(' '):
        if c !='':
            r.append(int(c))
        
    return r

def ReadSingle(l):
    r=''
    for c in l.strip().split(' '):
        if c.isdigit():
            r =r + c
            
    return int(r)

def Run6A(filename):
    times = []
    distances = []
    for line in open(filename):
        if "Time: " in line:
            times = ReadArray(line.split(':')[1])
        else :
            distances = ReadArray(line.split(':')[1])


    running_total = 1

    for i in range(0,len(times)):
        waystobeat = 0
        for j in range(0,times[i]):
            speed = j
            traveltime = times[i]-j
            thisdistance = speed * traveltime
            if thisdistance > distances[i]:
                waystobeat = waystobeat + 1
        
        print ("I have found this many ways to beat the distance " + str(waystobeat))
        running_total = running_total * waystobeat

    print("product is " + str(running_total))
    
    
def Run6B(filename):
    time =0
    distance =0
    for line in open(filename):
        if "Time: " in line:
            time = ReadSingle(line.split(':')[1])
        else :
            distance = ReadSingle(line.split(':')[1])
            
    waystobeat = 0
    for j in range(0,time):
        speed = j
        traveltime = time-j
        thisdistance = speed * traveltime
        if thisdistance > distance:
            waystobeat = waystobeat + 1
    
    print ("I have found this many ways to beat the distance " + str(waystobeat))
            
#Run6A("input.txt")

Run6B("input.txt")
