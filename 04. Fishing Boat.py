budget = int(input())
season = input()
fishmans = int(input())
if season == 'Spring':
    if fishmans <=6:
        price = 3000 * 90/100
    elif 7<=fishmans<=11:
        price = 3000*85/100
    else:
        price = 3000*75/100
elif season == 'Summer' or season =='Autumn':
    if fishmans <=6:
        price = 4200 * 90/100
    elif 7<=fishmans<=11:
        price = 4200*85/100
    else:
        price = 4200*75/100
elif season == 'Winter':
    if fishmans <=6:
        price = 2600 * 90/100
    elif 7<=fishmans<=11:
        price = 2600*85/100
    else:
        price = 2600*75/100
if fishmans%2 == 0 and season != 'Autumn':
    price = price*95/100

if budget>= price:
    print(f"Yes! You have {budget-price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")