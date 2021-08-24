legendaries = {'shards' : 0, 'fragments' : 0, 'motes' : 0}
legendaries_mats = {'shards':'Shadowmourne', 'fragments':'Valanyr', 'motes':'Dragonwrath'}
junks = {}
list = input().split()
not_obtained = True
while not_obtained:
    for index in range(0, len(list), 2):
        if list[index+1].lower() not in legendaries_mats:
            if list[index+1].lower() not in junks:
                junks[list[index + 1].lower()] = int(list[index])
            else:
                junks[list[index + 1].lower()] += int(list[index])
        else:
            legendaries[list[index+1].lower()] += int(list[index])

        for key,value in legendaries.items():
            if value >= 250:
                print(f"{legendaries_mats[key]} obtained!")
                legendaries[key] -= 250
                not_obtained = False
                break
        if not not_obtained:
            break
    if not_obtained:
        list = input().split()
sortet_legendaries = sorted(legendaries.items(), key = lambda  kvp: (-kvp[1],kvp[0]))
for tup in sortet_legendaries:
    print(f"{tup[0]}: {tup[1]}")

sorted_junks = sorted(junks.items(),key = lambda kvp: kvp)
for tup in sorted_junks:
    print(f"{tup[0]}: {tup[1]}")



