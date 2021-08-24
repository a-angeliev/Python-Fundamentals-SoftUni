budget = float(input())
count_statists = int(input())
price_per_statist = float(input())

sum_decor = 0.10 * budget
sum_clothes = count_statists * price_per_statist


if count_statists >150:
    sum_clothes = sum_clothes - 0.10 * sum_clothes


expenses = sum_decor + sum_clothes

if expenses <= budget :
        print('Action!')
        left_money = budget - expenses
        print(f'Wingard starts filming with {left_money:.2f} leva left.')
else:
    print("Not enough money!")
    need_money = expenses - budget
    print(f'Wingard needs {need_money:.2f} leva more.')