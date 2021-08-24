presonal_score ={}
contest_info = {}
cont = []

data = input()
while not data == 'no more time':
    name,contest,points = data.split(" -> ")
    points = int(points)
    if not contest in contest_info:
         contest_info[contest] = {name:points}
    elif not name in contest_info[contest]:
        contest_info[contest][name] = points
    else:
        if contest_info[contest][name] < points:
            contest_info[contest][name] = points
    data = input()

for contest,info in contest_info.items():
    for name,points in info.items():
        if name in presonal_score:
            presonal_score[name] += points
        else:
            presonal_score[name] = points

for contest,info in contest_info.items():
    print(f"{contest}: {len(contest_info[contest])} participants")
    position = 0
    for name,points in sorted(info.items(),key = lambda kvp: (-kvp[1],kvp[0])):
        position += 1
        print(f"{position}. {name} <::> {points}")
pos = 1
print(f"Individual standings:")
for name,points in sorted(presonal_score.items(),key = lambda kvp: (-kvp[1],kvp[0])):
    print(f"{pos}. {name} -> {points}")
    pos +=1