
ScoreSystem= [0,1,2,4,8,16,32,64,128,256, 512, 1024, 2048,4096]

def Winning(card):
    parts=card.strip().split(":")[1].split("|")
    winning= set(parts[0].strip().split(' '))
    drawn = set(parts[1].strip().split(' '))
    winning.add('')
    winning.remove('')
    return len(winning & drawn)

def Score(card):
    return ScoreSystem[Winning(card)]


def  Run4A(filename):
    runningTotal =0
    for line in open(filename):
        runningTotal = runningTotal + Score(line)
    
    print("running total is " + str(runningTotal))

def Run4B(filename):

    cards = []
    count = []
    
    for line in open(filename):
        cards.append(line)
        count.append(1)
        
    running_total=0
    
    for curr_index in range(0, len(cards)):
        running_total = running_total + count[curr_index]
        print("We Have " + str(count[curr_index]) +" copies of card "+ str(curr_index+1))
        winning = Winning(cards[curr_index])
        for i in range(curr_index+1, min(1+curr_index+winning, len(count))):
            count[i]= count[i] + count[curr_index]
    
    print("running total is " + str(running_total))
    
#Run4A("input.txt")

Run4B("input.txt")


