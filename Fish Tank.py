a = int(input())
b = int(input())
c = int(input())
obem = float(input())
a_dm = a/10
b_dm = b/10
c_dm = c/10
V=a_dm * b_dm*c_dm
obem_litri = V * obem/100
water = V - obem_litri
print(water)
