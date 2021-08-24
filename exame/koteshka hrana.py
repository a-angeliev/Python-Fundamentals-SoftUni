maz = int(input())
port = int(input())
vug = int(input())
call = int(input())
water = int(input())
allmaz = (maz/100 * call )/ 9
allprot = (port/100* call)/4
allcug = (vug/100* call)/4
allfood = allmaz+allprot+allcug
a = call/ allfood
b = (100 - water)/100 * a
print(f"{b:.4f}")