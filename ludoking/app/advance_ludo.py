import random
from pyfiglet import Figlet
from datetime import datetime
#global variables
players =['krishna','paarth','anjali','vipin']
final = 20
p=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
max=len(players)
rank=[]
stime =0.0
tend =datetime.now()
tstart = datetime.now()

def printStaus(p):
    t=''
    print(f'current status ')
    for j in range(0,max):
        if j==0:
            t='--'
        elif j==1:  
            t='..'
        elif j==2:
            t='~~'
        else:
             t='@'
        for l in range(0,max):
            s=p[j][l]*t
            if j%2==0:
                print(f'\t {players[j]}[{l+1}] {s} {p[j][l]}', end="")
                print("")
                print("")
            else:
                print(f'{players[j]}[{l+1}] {s} {p[j][l]}', end="")
                print("")
                print("")
def resetPlayer(players,rn,i,k):
     l=0
     yieldx = 0
     for l in range(0,max):
        if p[i][l]==p[k][l] and p[k][l]>0 and rn>1 and i!=k: #reseting score for previos player
            p[k][l]=0
            print(f'for {players[k]} setting chip {l+1} to zero!')
            printStaus(p)    
            print(f'cool  {players[i].upper()} !') 
            yieldx=handleRepeat(i,6)
            
def removePlayer(p,pi):
    fi=1
    l=0
    for item in p[pi]:
        if item >= final or item ==-1:
            fi+=1
            l=p[pi].index(item)
            p[pi][l]=-1
        else:
            fi*=0
    if fi > 1:
        rank.append(players[pi])
        print(f'{players[pi]}, you are done at rank {len(rank)}!')
    return rank    
def getInput():
    status = input('ready[y/n:] ')
    if status=='n':
        print('quiting..')
        return '0'  
    elif status not in ['y','n']:
        print('status can be y/n')
        return '1'
    else:
        return status
def getChip(i,dice):
    gotit=True
    x=0
    while gotit:
        try:
            g=int(input('which chip you want to play:(1 to 4, 0 to pass) '))
        except ValueError:
            g=random.randint(1, 4)
        if g <0 or g>4:
            print('chip number should be 1 to 4, zero for pass')    
            continue
        elif g==0:
            gotit=False
            x=-1
            continue
        
        x=g-1 #chip index
        
        if p[i][x]<0:
            print(f'This chip is already in for {players[i]}')
            print('Choose another one')
        elif p[i][x]==0  and dice not in [1,6]:
            print('you can open with 1 or 6 only')
        else:
            gotit=False
            
    return x
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
#main program
def ludoKing(list):
    
    
    #function variables
    rn=0
    i=random.randint(0,max-1) #random player index
    k=i
    dice=0
    y='' 
    x=0
    rank=[]
    tdice=0
    while True:
        name = players[i]
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
        print(dice)
        x=getChip(i,dice)
        if x==-1:
            i+=1
            if i==max:
                i=0
            printStaus(p)     
            continue
        #increment chip place
        if p[i][x] > 0:
            p[i][x]+=dice
        elif p[i][x] ==0 and dice in [1,6]:
            tdice=dice
            dice = 1
            p[i][x]+=dice
            dice=tdice
        else:
            i+=1
            if i==max:
                i=0
            printStaus(p)    
            continue
        printStaus(p)   
        resetPlayer(players,rn,i,k)           
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
print(custom_fig.renderText('LudoKing'))
print(f'Welcome back {players}, you started at {tstart}')
ludoKing(players)
print(f'Well played {players}!')
tend=datetime.now()
stime=tend-tstart
print(f'See you soon, you are leaving at {tend}')
print(f'you enjoyed for {stime} ')

     
   


