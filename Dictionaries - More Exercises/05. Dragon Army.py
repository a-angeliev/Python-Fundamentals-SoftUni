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

print(dragons_info)
for type,info in sorted(dragons_info.items(),key = lambda kvp: kvp[1], reverse = True):
    damage = 0
    health = 0
    armor = 0
    for name,stats in sorted(info.items(),key = lambda kvp:kvp, reverse = False):
        damage += int(stats[0])
        health += int(stats[1])
        armor +=int(stats[2])
    print(f"{type}::({damage:.2f}/{health:.2f}/{armor:.2f})")
    for name,stats in info.items():
        print(f'-{name} -> damage: {damage}, health: {health}, armor: {armor}')

sorted_list = dict(sorted(dragons_info.items()),key = lambda kvp: kvp[1].keys())
print(sorted_list)



