vacation_price = float(input())
puzzel_number = int(input())
dols_number = int(input())
bears_number = int(input())
minians_number = int(input())
trucks_number = int(input())
puzzel_price = 2.6
dol_price = 3
bear_price = 4.1
minian_price = 8.2
truck_price = 2
money  = puzzel_number* puzzel_price + dols_number* dol_price + \
         bears_number*bear_price + minians_number*minian_price +\
         trucks_number*truck_price
toys = puzzel_number+dols_number+bears_number+trucks_number+minians_number
if toys >= 50:
   endmoney = money *75/100
else :
    endmoney =  money

afterrent = endmoney *90/100

if afterrent >= vacation_price:
    print(f"Yes! {afterrent - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - afterrent:.2f} lv needed.")





