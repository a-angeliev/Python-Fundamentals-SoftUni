enough_money = float(input())
aveable_money = float(input())
spend_days = 0
days = 0
while aveable_money<enough_money and spend_days<5:
    spend_save = input()
    if spend_save == "spend":
        spend_days+=1
    else:
        spend_days= 0
    money = float(input())
    if spend_save == 'save':
        aveable_money+=money
    else:
        aveable_money = aveable_money -money
        if aveable_money <0:
            aveable_money=0
    days +=1
if  spend_days == 5:
    print(f"You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
