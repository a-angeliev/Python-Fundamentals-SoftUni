health = 100
bitcoins = 0
commands = [x for x in input().split('|')]
room = 0
is_dead = False
for com in commands:
    room+=1
    command,number = com.split()
    number = int(number)
    if command == 'potion':
        if health + number > 100:
            print(f"You healed for {100 - health} hp.")
            health =100

        else:
            health +=number
            print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == 'chest':
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            is_dead = True
            break

if not is_dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
