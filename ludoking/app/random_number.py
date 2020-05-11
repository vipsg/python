import random
final = 50
rn=1
players =['krishna','paarth','vipin','anjali']
p=[0,0,0,0]
max=len(players)
i=random.randint(0,max-1)
k=i
a=0
while True:
    name = players[i]
    print(f'dice for {name}')
    status = input('ready[y/n:] ')
    if status not in ['y','n']:
        print('status can be y/n')
        continue
    dice=random.randint(1, 6)
    p[i]+=dice
    print(f'current status ')
    try:
        for j in range(0,max):
           s=p[j]*'--'
           print(f'{players[j]} {s} {p[j]}', end="")
           print("")
    except:
          print(f'error {j},{p[j]}')         
       
    if p[i]==p[k] and rn>1 and i!=k: #reseting score for previos player
       p[k]=0
       print(f'{players[k]} setting to zero!')
    if p[i]>=final:
       print(f'{name.upper()} won! 🤴') 
       break
    if dice in [6]:
        i=i
    else:
        k=i #preserving previous player index
        i+=1
        if i==max:
            i=0
    print('\n')
    rn+=1
    print(dice)
    if status=='n':
        break   
   


