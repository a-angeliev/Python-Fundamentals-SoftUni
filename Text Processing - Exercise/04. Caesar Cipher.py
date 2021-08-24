data = input()
new= ''
for ch in data:
    new_car = chr(ord(ch) +3)
    new +=new_car
print(new)