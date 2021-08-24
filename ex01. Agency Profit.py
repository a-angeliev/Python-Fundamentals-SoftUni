name = input()
adult_number = int(input())
kids_number = int(input())
adult_price = float(input())
vat = float(input())

kids_price = adult_price*30/100
adult_allprice = (adult_price +vat) * adult_number
kids_allprice = (kids_price +vat) * kids_number
profit = (adult_allprice + kids_allprice) * 20/100
print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")