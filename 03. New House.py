type = input()
number = int(input())
budget = int(input())
if type == 'Roses':
    if number > 80:
        price = 5*90/100
    else:
        price = 5
elif type == 'Dahlias':
    if number > 90:
        price = 3.8*85/100
    else:
        price = 3.8
elif type == 'Tulips':
    if number > 80:
        price = 2.8*85/100
    else:
        price = 2.8
elif type == 'Narcissus':
    if number < 120:
        price = 3*115/100
    else:
        price = 3
elif type =='Gladiolus':
    if number < 80:
        price = 2.50*120/100
    else:
        price = 2.50
allprice =price * number
if budget >= allprice:
    print(f"Hey, you have a great garden with {number} {type} and {budget-allprice:.2f} leva left.")
else:
    print(f"Not enough money, you need {allprice-budget:.2f} leva more.")
