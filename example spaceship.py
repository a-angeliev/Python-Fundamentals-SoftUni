from math import floor
a = float(input())
b = float(input())
h = float(input())
hight = float(input())
allship = a*b*h
oneroom = (hight+0.40)*2*2
ppl = floor(allship/oneroom)
if 3<=ppl<=10:
    print(f"The spacecraft holds {ppl} astronauts.")
elif ppl<3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")

