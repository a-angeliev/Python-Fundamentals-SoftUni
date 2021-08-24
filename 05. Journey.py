budget = float(input())
season = input()
if 0<budget <= 100:
    country = 'Bulgaria'
    if season == 'summer':
        price = budget *30/100
        place = 'Camp'
    elif season == 'winter':
        price = budget*70/100
        place = "Hotel"
elif budget <=1000:
    country = 'Balkans'
    if season == 'summer':
        price = budget *40/100
        place = 'Camp'
    elif season == 'winter':
        price = budget*80/100
        place = "Hotel"
else:
    country = "Europe"
    price = budget*90/100
    place =  "Hotel"
print(f'Somewhere in {country}')
print(f"{place} - {price:.2f}")
