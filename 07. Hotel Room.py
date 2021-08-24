mounth = input()
nights = int(input())

if mounth == 'May' or mounth == 'October':
    if 7<nights <= 14:
        studio = 50*95/100
        apart = 65
    elif nights> 14:
        studio = 50*70/100
        apart = 65*90/100
    else:
        studio = 50
        apart = 65
elif mounth == 'June' or mounth =='September':
    if nights > 14:
        studio = 75.2 * 80 / 100
        apart = 68.70 * 90 / 100
    else:
        studio = 75.2
        apart = 68.7
elif mounth == 'July' or mounth == 'August':
    if nights > 14:
        apart = 77 * 90 / 100
        studio = 76
    else:
        studio = 76
        apart = 77

print(f"Apartment: {nights * apart:.2f} lv.")
print(f"Studio: {nights * studio:.2f} lv.")