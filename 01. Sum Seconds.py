import math
a = int(input())
b = int(input())
c = int(input())
sum = a+b+c
minutes = math.floor(sum /60)
secounds = sum% 60
if secounds <10:

    print(f"{minutes}:0{secounds}")
else :
    print(f"{minutes}:{secounds}")



