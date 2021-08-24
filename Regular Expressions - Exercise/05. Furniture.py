import re
pattern = r"^>>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)*)!(?P<quantity>\d+)$"
furniture = []
price = 0

data = input()
while data !='Purchase':
    for match in re.finditer(pattern,data):
        furniture.append(match.group('furniture'))
        price += float(match.group('price')) * float(match.group('quantity'))


    data = input()

print('Bought furniture:')
for el in furniture:
    print(el)
print(f"Total money spend: {price:.2f}")