money=float(input())
coins = 0
while money>0:
    if money>=2:
        money = money - 2
        coins +=1
    elif money>=1:
        money -=1
        coins+=1
    elif money>=0.50:
        money -=0.50
        coins+=1
    elif money >=0.20:
        money -=0.20
        coins+=1
    elif money >= 0.10:
        money -=0.10
        coins+=1
    elif money >= 0.05:
        money -= 0.05
        coins+=1
    elif money >= 0.02:
        money -= 0.02
        coins+=1
    else:
        money -= 0.01
        coins+=1
    money = round(money,2)
print(coins)