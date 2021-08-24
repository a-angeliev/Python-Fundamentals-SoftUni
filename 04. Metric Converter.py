number = float(input())
exchange_from = str(input())
exchange_to = str(input())

if exchange_from == "m" and exchange_to == "cm":
    print(f"{number*100:.3f}")
elif exchange_from =='m' and exchange_to == 'mm':
    print(f"{number*1000:.3f}")
elif exchange_from == 'cm' and exchange_to =='m':
    print(f'{number/100:.3f}')
elif exchange_from =='cm' and exchange_to =='mm':
    print(f"{number*10:.3f}")
elif exchange_from == 'mm' and exchange_to == 'm':
    print(f"{number/1000:.3f}")
elif exchange_from == 'mm' and exchange_to == 'cm':
    print(f"{number/10:.3f}")

