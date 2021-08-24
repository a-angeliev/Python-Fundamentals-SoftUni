data = input()
towns = {}
while not data =="Sail":
    town,population,gold = data.split("||")
    population = int(population)
    gold = int(gold)
    if not population <0 and not gold <0:
        if not town in towns:
            towns[town] = {"population":population, "gold":gold}
        else:
            towns[town]['population'] +=population
            towns[town]['gold'] +=gold
    data = input()

data = input().split('=>')

while not data[0] == "End":
    if data[0] == "Plunder":
        town = data[1]
        people = int(data[2])
        gold = int(data[3])
        if town in towns:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            towns[town]["population"] -= people
            towns[town]["gold"] -= gold
            if towns[town]['population'] <= 0 or towns[town]["gold"] <=0:
                del towns[town]
                print(f"{town} has been wiped off the map!")

    elif data[0] == "Prosper":
        town = data[1]
        gold = int(data[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            if town in towns:
                towns[town]["gold"] +=gold
                print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")

    data = input().split('=>')

if not towns =={}:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for town,info in sorted(towns.items(),key = lambda kvp: (-kvp[1]['gold'],kvp)):
        print(f"{town} -> Population: {info['population']} citizens, Gold: {info['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

