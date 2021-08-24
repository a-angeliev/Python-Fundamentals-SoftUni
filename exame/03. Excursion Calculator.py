people = int(input())
season = input()
if people <= 5:
    if season == 'spring':
        price = 50
    elif season =='summer':
        price = 48.50
    elif season =='autumn':
        price = 60
    elif season =='winter':
        price = 86
else:
    if season == 'spring':
        price = 48
    elif season =='summer':
        price = 45
    elif season =='autumn':
        price = 49.50
    elif season =='winter':
        price = 85
sum = people * price
if season == 'summer':
    allsum = sum -sum * 15/100
elif season == 'winter':
    allsum = sum * 108/100
else:
    allsum = sum
print(f"{allsum:.2f} leva.")
