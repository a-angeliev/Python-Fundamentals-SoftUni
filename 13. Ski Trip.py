days = int(input())
type = input()
rate = input()
room_price = 0
if type == 'room for one person':
    room_price = 18
elif type == 'apartment':
    if days-1 <10:
        room_price = 25*70/100
    elif days - 1 <=15:
        room_price = 25*65/100
    elif days - 1 > 15:
        room_price = 25 * 50/100
elif type == 'president apartment':
    if days-1 <10:
        room_price = 35*90/100
    elif days - 1 <=15:
        room_price = 35*85/100
    elif days - 1 > 15:
        room_price = 35 * 80/100
sum_price = (days-1)*room_price
if rate == 'positive':
    print(f"{sum_price+sum_price*25/100:.2f}")
elif rate =='negative':
    print(f"{sum_price - sum_price * 10 / 100:.2f}")

