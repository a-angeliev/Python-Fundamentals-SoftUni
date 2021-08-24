animals = {}
areas = {}
data = input()
while not data == "EndDay":
    data = data.split(": ")
    if data[0] =="Add":
        name,needed_food,area = data[1].split("-")
        needed_food = int(needed_food)
        if not name in animals:
            animals[name] = {"needed food": needed_food, "area": area}
        else:
            animals[name]['needed food']+= needed_food

    if data[0] =="Feed":
        name,food = data[1].split("-")
        food = int(food)
        if name in animals:
            animals[name]["needed food"]-= food
            if animals[name]["needed food"] <=0:
                del animals[name]
                print(f"{name} was successfully fed")



    data = input()
print("Animals:")
for name,info in sorted(animals.items(),key = lambda kvp:(-kvp[1]['needed food'],kvp)):
    print(f" {name} -> {info['needed food']}g")

for name,info in animals.items():
    if not info['area'] in areas:
        areas[info['area']] = 1
    else:
        areas[info['area']]+= 1
print("Areas with hungry animals:")
for area,value in sorted(areas.items(),key = lambda kvp: (-kvp[1],kvp[0])):
    print(f" {area}: {value}")


