item_list = input().split('|')
amout_of_money = float(input())
buyed_items = []
profit = 0
money_from_items= 0
for item in item_list:
    item_info = item.split("->")
    item_price = float(item_info[1])
    if item_info[0] == 'Clothes' and item_price<= 50:
        if item_price <= amout_of_money:
            amout_of_money -= item_price
            profit += item_price * 40 / 100
            buyed_items.append(item_price + item_price * 40 / 100)
    elif item_info[0] == 'Shoes' and item_price<= 35:
        if item_price <= amout_of_money:
            amout_of_money -= item_price
            profit += item_price * 40 / 100
            buyed_items.append(item_price + item_price * 40 / 100)
    elif item_info[0] == 'Accessories' and item_price<=20.50:
        if item_price <= amout_of_money:
            amout_of_money -= item_price
            profit += item_price * 40 / 100
            buyed_items.append(item_price + item_price * 40 / 100)

for money in buyed_items:
    print(f"{money:.2f}", end=" ")
    money_from_items += money
finished_price = amout_of_money + money_from_items
print(f"\nProfit: {profit:.2f}")
if finished_price >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
