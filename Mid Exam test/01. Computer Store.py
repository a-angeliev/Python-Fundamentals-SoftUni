price = input()

total_price = 0
price_no_tax = 0

while not price == "regular" and not price == "special":

    price = float(price)

    if price < 0:
        print("Invalid price!")
    else:
        price_no_tax += price

    price = input()

tax = price_no_tax * 0.20
total_price = price_no_tax + tax

if total_price == 0:
    print("Invalid order!")

else:
    if price == "special":
        total_price *= 0.90
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_no_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")