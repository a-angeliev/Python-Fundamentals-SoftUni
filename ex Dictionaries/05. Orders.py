items = {}
command = input().split()
while not command[0] == 'buy':
    product, price, qty = command
    price = float(price)
    qty = float(qty)
    if not product in items.keys():
        items[product] = {"price":price,"qty":qty}
    else:
        items[product]["price"]  = price
        items[product]["qty"]  += qty
    command = input().split()
for kay,value in items.items():
    print(f"{kay} -> {value['price']*value['qty']:.2f}")