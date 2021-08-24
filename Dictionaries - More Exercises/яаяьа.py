number_lines = int(input())
dragons_info = {}
for index in range(number_lines):
    type,name,damage,health,armor = input().split()
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    damage = int(damage)
    health = int(health)
    armor = int(armor)

    if not type in dragons_info:
        dragons_info[type] = {name:[damage,health,armor]}
    else:
        dragons_info[type][name] = [damage,health,armor]


for type,info in dragons_info.items():
    damage = 0
    health = 0
    armor = 0
    for name,stats in info.items():
        damage += int(stats[0])
        health += int(stats[1])
        armor +=int(stats[2])
    print(f"{type}::({damage/len(info):.2f}/{health/len(info):.2f}/{armor/len(info):.2f})")
    for name,stats in sorted(info.items(),key= lambda kvp: kvp[0]):
        print(f'-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}')


