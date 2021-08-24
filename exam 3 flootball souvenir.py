club = input()
type = input()
number = int(input())

if club == "Argentina" or club == 'Brazil' or club == 'Croatia' or club =='Denmark':
    if club == 'Argentina':
        if type == "flags":
            print(f"Pepi bought {number} {type} of {club} for {number * 3.25:.2f} lv.")
        elif type == 'caps':
            print(f"Pepi bought {number} {type} of {club} for {number * 7.20:.2f} lv.")
        elif type == 'posters':
            print(f"Pepi bought {number} {type} of {club} for {number * 5.10:.2f} lv.")
        elif type == 'stickers':
            print(f"Pepi bought {number} {type} of {club} for {number * 1.25:.2f} lv.")
        else:
            print("Invalid stock!")
    elif club == 'Brazil':
        if type == "flags":
            print(f"Pepi bought {number} {type} of {club} for {number * 4.20:.2f} lv.")
        elif type == 'caps':
            print(f"Pepi bought {number} {type} of {club} for {number * 8.50:.2f} lv.")
        elif type == 'posters':
            print(f"Pepi bought {number} {type} of {club} for {number * 5.35:.2f} lv.")
        elif type == 'stickers':
            print(f"Pepi bought {number} {type} of {club} for {number * 1.20:.2f} lv.")
        else:
            print("Invalid stock!")
    elif club == 'Croatia':
        if type == "flags":
            print(f"Pepi bought {number} {type} of {club} for {number * 2.75:.2f} lv.")
        elif type == 'caps':
            print(f"Pepi bought {number} {type} of {club} for {number * 6.90:.2f} lv.")
        elif type == 'posters':
            print(f"Pepi bought {number} {type} of {club} for {number * 4.95:.2f} lv.")
        elif type == 'stickers':
            print(f"Pepi bought {number} {type} of {club} for {number * 1.10:.2f} lv.")
        else:
            print('Invalid stock!')
    elif club == 'Denmark':
        if type == "flags":
            print(f"Pepi bought {number} {type} of {club} for {number * 3.10:.2f} lv.")
        elif type == 'caps':
            print(f"Pepi bought {number} {type} of {club} for {number * 6.50:.2f} lv.")
        elif type == 'posters':
            print(f"Pepi bought {number} {type} of {club} for {number * 4.80:.2f} lv.")
        elif type == 'stickers':
            print(f"Pepi bought {number} {type} of {club} for {number * 0.90:.2f} lv.")
        else:
            print('Invalid stock!')
else:
    print("Invalid country!")