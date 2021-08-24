city = input()
selse= float(input())
if city == "Sofia":
    if 0<= selse <= 500:
        print(f"{selse*5/100:.2f}")
    elif 500<selse <=1000:
        print(f"{selse * 7/100:.2f}")
    elif 1000< selse <=10000:
        print(f"{selse * 8/100:.2f}")
    elif selse > 10000:
        print(f"{selse * 12 / 100:.2f}")
    else:
        print('error')
elif city == 'Varna':
    if 0<= selse <= 500:
        print(f"{selse*4.5/100:.2f}")
    elif 500<selse <=1000:
        print(f"{selse * 7.5/100:.2f}")
    elif 1000< selse <=10000:
        print(f"{selse * 10/100:.2f}")
    elif selse > 10000:
        print(f"{selse * 13 / 100:.2f}")
    else:
        print('error')
elif city =='Plovdiv':
    if 0<= selse <= 500:
        print(f"{selse*5.5/100:.2f}")
    elif 500<selse <=1000:
        print(f"{selse * 8/100:.2f}")
    elif 1000< selse <=10000:
        print(f"{selse * 12/100:.2f}")
    elif selse > 10000:
        print(f"{selse * 14.5 / 100:.2f}")
    else:
        print('error')
else:
    print('error')

