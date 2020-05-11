import random
from pyfiglet import Figlet
from datetime import datetime
import time
#global variables
players =['krishna','paarth','anjali','vipin']
final = 6
p=[0,0,0,0]
max=len(players)
rank=[]
stime =0.0
tend =datetime.now()
tstart = datetime.now()
rules={2:14, 5 : -5, 12 : -7, 8 : 9, 27 : -11, 35: 8, 
       49 : -35, 57 : 12, 65:10, 77 : -7, 80: 19, 99 : -84}
rulekey= sorted(rules)

def printStaus(p,rules,rulekey):
    t=''
    print("")
    print(f'current status.. ', "")
    print("")
    
    for j in range(0,max):
        if j==0:
            t='--'
        elif j==1:  
            t='..'
        elif j==2:
            t='~~'
        else:
             t='@'
        s=p[j]*t
        print(f'{players[j]} {s} {p[j]}', end="")
        print("")
        print("")

    print(" \t \t Rules: ")        
    print("")
    for i in rulekey:
       if rules[i] < 0:
            print("\t \t Next snakes are: ")
            print(f'\t \t {i} -> {rules[i]} -> {int(i)+rules[i]}')
       else:
              print("\t \t Next ladders are: ")
              print(f'\t \t {i} -> {rules[i]} -> {int(i)+rules[i]}')
            
def resetPlayer(players,rn,i,k,rules,rulekey):
    l=0
    yieldx = 0
    if p[i]==p[k] and p[k]>0 and rn>1 and i!=k: #reseting score for previos player
        p[k]=0
        print(f'for {players[k]} setting chip {l+1} to zero!')
        printStaus(p,rules,rulekey)    
        print(f'cool  {players[i].upper()} !') 
        yieldx=handleRepeat(i,6)
    return yieldx
    
def removePlayer(p,pi):
    if p[pi] >= 100:
        p[pi]=-1
        rank.append(players[pi])
        print(f'{players[pi]}, you are done at rank {len(rank)}!')
    return rank    
def getInput():
    status = input('ready[y/n:] ')
    print("")
    if status=='n':
        print('quiting..')
        return '0'  
    elif status not in ['y','n']:
        print('status can be y/n')
        return '1'
    else:
        return status

def handleRepeat(pi,pdice):
    q=0
    if pdice in [6]:
        pass
    else:
        q=pi #preserving previous player index
        pi+=1
        if pi==max:
           pi=0
    yield pi
    yield q
def checkWon(name,rank):
    if name in rank:
        print(f'{name} already won')
        return True   

def getReplacement(rules,p,i):
    try:
        return rules[p[i]]
    except:
        return 0        
#main program
def ludoKing(list):
    
    
    #function variables
    rn=0
    i=random.randint(0,max-1) #random player index
    k=i
    dice=0
    y='' 
    rank=[]
    tdice=0
 
    while True:
        name = players[i]
        name = name.capitalize()
        if checkWon(name,rank):
            i+=1
            if i==max:
                i=0
            continue
        print(f'dice for {name}')
        y=getInput()
        if y =='0':
            break
        elif y=='1':
            continue
        #roll dice
        dice=random.randint(1, 6)
        pdice = str(dice)
        pdice =  "\033[1m" + pdice + "\033[0m"
        pdice = pdice.center(10, '\t')
        print(pdice)
        print("")
        
        #increment chip place
        if p[i] > 0:
            p[i]+=dice
        elif p[i] ==0 and dice in [1,6]:
            tdice=dice
            dice = 1
            p[i]+=dice
            dice=tdice
            print(f"Opening for {name}") 
            time.sleep(2)
        else:
            i+=1
            if i==max:
                i=0
            printStaus(p,rules,rulekey)    
            continue
        r= getReplacement(rules,p,i)    
        p[i]+=r
        printStaus(p,rules,rulekey)   
        if r < 0 :
            time.sleep(1)
            print(f"OOPS! Snake bite {name} by {abs(r)}")
        elif r > 0:
            time.sleep(1)
            print(f"Hurray! {name} got lifted by {r} points")
        else:
            pass
        resetPlayer(players,rn,i,k,rules,rulekey)           
        rank=removePlayer(p,i)
        if len(rank) == max-1:
            print('Game over! Come again!')
            break
        yieldx=handleRepeat(i,dice)
        i=next(yieldx)
        k=next(yieldx)
        print('\n')
        rn+=1
    print(f'you diced for {rn} times ')    
tstart=datetime.now()

custom_fig = Figlet(font='graffiti', width =100)
print(custom_fig.renderText('Snake & Ladder'))
print(f'Welcome back {players}, you started at {tstart}')
print("")
ludoKing(players)
print(f'Well played {players}!')
tend=datetime.now()
stime=tend-tstart
print(f'See you soon, you are leaving at {tend}')
print(f'you enjoyed for {stime} ')

     
   


