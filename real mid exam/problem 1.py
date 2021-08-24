ordes = int(input())
all_price = 0
for _ in range(ordes):
    ppc = float(input())
    days = int(input())
    cc = int(input())
    cur_price = ppc*days*cc
    print(f"The price for the coffee is: ${cur_price:.2f}")
    all_price +=cur_price
print(f"Total: ${all_price:.2f}")