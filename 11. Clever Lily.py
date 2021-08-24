age = int(input())
washmachine = float(input())
toy_price = int(input())
a= 0
b=0
for i in range(1,age+1):
    if i%2 == 0:
        a = a+1
    else:
        b=b+1
price = 0
for i in range(1,a+1):
    price = price + i*10
price = price - a
price_for_toys = b * toy_price
all_price = price+price_for_toys
if all_price>= washmachine:
    print(f"Yes! {all_price-washmachine:.2f}")
else:
    print(f"No! {washmachine- all_price:.2f}")