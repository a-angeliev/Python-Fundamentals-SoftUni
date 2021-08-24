number_of_heroes = int(input())
heroes ={}

for _ in range(number_of_heroes):
    hero,HP,MP = input().split()
    MP = int(MP)
    HP = int(HP)
    if not hero in heroes:
        heroes[hero] = {"HP":HP, "MP":MP}

data = input().split(' - ')
while not data[0] == "End":
    if data[0] == "CastSpell":
        hero = data[1]
        MP = int(data[2])
        if hero in heroes:
            if heroes[hero]["MP"] >= MP:
                heroes[hero]["MP"] -= MP
                current_mana = heroes[hero]["MP"]
                print(f"{hero} has successfully cast {data[3]} and now has {current_mana} MP!")
            else:
                print(f"{hero} does not have enough MP to cast {data[3]}!")

    if data[0] == "TakeDamage":
        hero = data[1]
        damage = int(data[2])
        attacker = data[3]
        if hero in heroes:
            heroes[hero]["HP"] -= damage
        if heroes[hero]["HP"] > 0:
            current_hp = heroes[hero]["HP"]
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            del heroes[hero]
            print(f"{hero} has been killed by {attacker}!")

    if data[0] == "Recharge":
        hero = data[1]
        amount = int(data[2])
        if hero in heroes:
            if heroes[hero]['MP'] + amount <= 200:
                heroes[hero]["MP"] += amount
                print(f"{hero} recharged for {amount} MP!")
            else:
                amount = 200 - heroes[hero]['MP']
                heroes[hero]['MP'] = 200
                print(f"{hero} recharged for {amount} MP!")

    if data[0] == "Heal":
        hero = data[1]
        amount = int(data[2])
        if hero in heroes:
            if heroes[hero]['HP'] + amount <= 100:
                heroes[hero]["HP"] += amount
                print(f"{hero} healed for {amount} HP!")
            else:
                amount = 100 - heroes[hero]['HP']
                heroes[hero]['HP'] = 100
                print(f"{hero} healed for {amount} HP!")

    data = input().split(' - ')

for name,info in sorted(heroes.items(),key = lambda  kvp: (-kvp[1]['HP'],kvp)):
    print(name)
    print(f" HP: {info['HP']}")
    print(f" MP: {info['MP']}")
