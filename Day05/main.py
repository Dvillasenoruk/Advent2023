import datetime

class MappingRange:
    Start=0
    End =1
    Range =1
    TopEnd =0
    Dif =0
    
    
#def IsInRange(m, n):
#       return n >= m.Start and  n<=m.TopEnd    
    
#def Map(m, n):
 #       return n + m.Dif
    
def ReadSeeds (seedsline):
    elements = seedsline.split(':')[1].strip().split(' ')
    r = [] 
    for e in elements:
        r.append(int (e))
        
    return r


def ReadSeedRange(seedsline):
    elements = seedsline.split(':')[1].strip().split(' ')
    r = [] 
    for i in range (0,len(elements), 2):
        r.append(range(int(elements[i]),int(elements[i])+int(elements[i+1])+1))
    
    return r
    
def ReadMap (c):
    r = MappingRange()
    parts = c.strip().split(' ')
    r.Start = int(parts[1])
    r.End = int(parts[0])
    r.Range = int(parts[2])
    r.TopEnd = r.Start + r.Range 
    r.Dif =  r.End - r.Start
    return r
    
def Run5A(filename):
    seeds=[]
    supermaps=[]
    
    curr_map = []
    for line in open(filename):
        if line.startswith('seeds:'):
            seeds = ReadSeeds(line)
        else:
            if line.strip()=='':
                if curr_map != []:
                    supermaps.append (curr_map)
                    curr_map = []
            else:
               if "map:"  in line:
                   print ("loading "+ line)
                   continue
               curr_map.append(ReadMap(line))
             
    if curr_map != []:
        supermaps.append (curr_map)
            
    lowest = 84143085794                
    # ok we are done reading 
    for seed in seeds:
        curr_in = seed
        print ("processing " +str(seed))         
        for submap in supermaps:
           
            for cur_map in submap:
                if curr_in >= cur_map.Start and  curr_in <=cur_map.TopEnd   :
                    curr_in = cur_map.Dif + curr_in                    
                    break
        
            print("changed to " + str(curr_in))
        
        if (curr_in < lowest):
            lowest = curr_in
            
    print ("the lowest we have is " + str(lowest))


def Run5B(filename):
    seeds=[]
    supermaps=[]
    
    curr_map = []
    for line in open(filename):
        if line.startswith('seeds:'):
            seeds = ReadSeedRange(line)
        else:
            if line.strip()=='':
                if curr_map != []:
                    supermaps.append (curr_map)
                    curr_map = []
            else:
               if "map:"  in line:
                   print ("loading "+ line)
                   continue
               curr_map.append(ReadMap(line))
             
    if curr_map != []:
        supermaps.append (curr_map)
            
    lowest = 84143085794                
    # ok we are done reading 
    for seed_r in seeds:
        print (datetime.datetime.now())
        print ("processing " +str(seed_r))   
        for seed in seed_r:
            curr_in = seed                 
            for submap in supermaps:
                
                for cur_map in submap:
                    if curr_in >= cur_map.Start and  curr_in <=cur_map.TopEnd   :
                        curr_in = cur_map.Dif + curr_in                    
                        break
            
            if (curr_in < lowest):
               #print ("seed " +str(seed)+" gives us " + str(curr_in))
                lowest = curr_in
            
    print ("the lowest we have is " + str(lowest))  

          
Run5A("input.txt")

Run5B("input.txt")