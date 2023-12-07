Highest=['A', 'K', 'Q', 'J', 'T','9', '8', '7','6', '5', '4', '3', '2']

def cardoffset (c):
    for i in range(0, len(Highest)):
        if c==Highest[i]:
            return 15-i
    
    
def secondOrderScore(a,b):
    for i in range(0,len(a)):
        sa = cardoffset (a[i]) 
        sb = cardoffset (b[i]) 
        if sa > sb :
            return True
        if sa < sb :
            return False
        
    # we should never get here
    return False

def score(a):
    co = {}
    for c in a:
        co[c]=0
        
    for c in a:
        co[c]= co[c] + 1

    hasTwo = False
    hasThree = False
    threeCards = ''
    twoCards = []
    highestcard = 0
    for k in co:
        if co[k] ==5:
            return 1000 
        if co[k] ==4:
            return 800
        
        if co[k] == 3:
            hasThree =True
            threeCards =k
            
        
        if co[k] ==2:
            hasTwo = True
            twoCards.append(k)

        if (cardoffset(k)> highestcard):
            highestcard = cardoffset(k)
            
    
    if  hasThree and hasTwo:
        return 600 
    
    if hasThree:
        return 500 
    
    if hasTwo :
        if (len (twoCards) ==2):
            return 400 
        return 300 
    
    return highestcard

def beats(a ,b):
    sa= score(a)
    sb = score(b)
    if sa == sb:
        return secondOrderScore(a,b)
    
    return sa > sb


def Run7A(filename):
    handToBet = {}
    order=[]
    for line in open(filename):
        lineParts  =line.strip().split(' ')
        handToBet[lineParts[0]] = int (lineParts[-1])
        order.append(lineParts[0])

    print (order)
    
    for i in range (1, len(order)):
        for j in range(0,i):
            if not beats (order[i], order[j]):
                t = order[i]
                order[i]=order[j]
                order[j]=t
    
    
    print (order)
    total =0
    for i in range (0, len(order)):
        thismoney= (i+1)* handToBet[order[i]]
        total = total+ thismoney
    
    print("total = " + str (total))

#Run7A("input.txt")
print(beats('75682','49586'))
