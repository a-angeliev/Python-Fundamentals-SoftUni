аnumber_plants = int(input())
plants = {}
for _ in range(number_plants):
    plant,rarity = input().split("<->")
    rarity = int(rarity)
    plants[plant] = {"rarity": rarity,"rating":[]}

data = input().split(": ")
while not data[0] == "Exhibition":
    if data[0] == "Rate":
        plant,rating = data[1].split(" - ")
        rating = int(rating)
        if plant in plants:
            plants[plant]['rating'].append(rating)
        else:
            print("error")

    elif data[0] == "Update":
        plant,new_rarity = data[1].split(" - ")
        new_rarity = int(new_rarity)
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print("error")

    elif data[0] == "Reset":
        plant = data[1]
        if plant in plants:
            plants[plant]['rating'].clear()
        else:
            print("error")
    else:
        print("error")
    data = input().split(": ")

print(f"Plants for the exhibition:")
for plant,info in plants.items():
    if not len(info['rating']) ==0:
        if not sum(info['rating']) ==0:
            avg_sum = sum(info['rating'])/len(info['rating'])
    else:
        avg_sum = 0
    plants[plant]['rating'] = avg_sum

for plant,info in sorted(plants.items(),key = lambda kvp: (-kvp[1]['rarity'],-kvp[1]['rating'])):
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {info['rating']:.2f}")

