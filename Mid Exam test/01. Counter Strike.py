energy = int(input())
levels = 0
command = input()
no_more_energy = False
while not command == "End of battle":
    distance = int(command)
    if energy - distance >=0:
        energy -=distance
        levels+=1
        if levels%3 == 0:
            energy+=levels
    else:
        print(f"Not enough energy! Game ends with {levels} won battles and {energy} energy")
        no_more_energy = True
        break
    command = input()
if not no_more_energy:
    print(f"Won battles: {levels}. Energy left: {energy}" )