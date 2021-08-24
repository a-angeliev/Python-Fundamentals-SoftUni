energy = 100
coins = 100
is_bancrupted =False
events_list = input().split("|")
for event in events_list:
    event_info = event.split('-')
    if event_info[0] == 'rest':
        if energy + int(event_info[1]) >100:
            print(f'You gained {100 - energy} energy.')
            energy = 100
            print(f"Current energy: {energy}.")
        else:
            print(f'You gained {int(event_info[1])} energy.')
            energy +=int(event_info[1])
            print(f"Current energy: {energy}.")
    elif event_info[0] =='order' and energy >= 30:
        energy -= 30
        coins += int(event_info[1])
        print(f"You earned {int(event_info[1])} coins.")
    elif event_info[0] == 'order' and energy<30:
        energy += 50
        print("You had to rest!")
    else:
        if coins >= int(event_info[1]):
            print(f"You bought {event_info[0]}.")
            coins -=int(event_info[1])
        else:
            is_bancrupted = True
            print(f"Closed! Cannot afford {event_info[0]}.")
            break
if not is_bancrupted:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

