n = int(input())
water = 0
for i in range(n):
    liters = int(input())
    if water + liters <=255:
        water += liters
    else:
        print("Insufficient capacity!")
print(water)
